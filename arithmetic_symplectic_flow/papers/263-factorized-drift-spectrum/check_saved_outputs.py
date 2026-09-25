#!/usr/bin/env python3
"""CS13 read-only saved-output analysis; never a new physical spectrum solve.

No runner import, eig/SVD, optimizer, root/target generation or output writes.
Uses saved quadrature to restore FE bands, scalar readouts, moments and saved-state
equations/occupations. Execute only after the parent confirms scientific exit0.
"""
import csv
import hashlib
import json
import math
from collections import Counter
from pathlib import Path

import numpy as np
from scipy.fft import dst

PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[1]
RUN = PACKAGE/'evidence/run-1'
WINDOWS = {'1-100': (0, 100), '101-300': (100, 300), '301-320': (300, 320), '1-320': (0, 320)}
MREF, WREF, FULLREF = 1.695273790061038, 5.234299091683695, 3.5251249515592384
RUNNER_SHA = '7ecba20d179f969776af1263c950327a118d86ee2e660afc01fbe8106d1bf29a'
checks, maxima, failures = Counter(), {}, []


def read(name):
    return json.loads((RUN/name).read_text())


def verify(ok, label):
    checks[label.split(':')[0]] += 1
    if not bool(ok): failures.append(label)


def close(actual, expected, label, atol=5e-11, rtol=2e-12):
    a, b = np.asarray(actual), np.asarray(expected)
    verify(a.shape == b.shape, label+':shape')
    if a.shape != b.shape: return
    verify(np.allclose(a, b, atol=atol, rtol=rtol, equal_nan=True), label)
    if a.size and np.issubdtype(a.dtype, np.number) and np.issubdtype(b.dtype, np.number):
        mask = np.isfinite(a) & np.isfinite(b)
        error = float(np.max(np.abs(a[mask]-b[mask]))) if np.any(mask) else 0.
        maxima[label.split(':')[0]] = max(maxima.get(label.split(':')[0], 0.), error)


def norm(value):
    return float(np.sqrt(np.sum(np.abs(value)**2)))


def sha(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024*1024), b''): digest.update(block)
    return digest.hexdigest()


def metrics(prediction, target):
    error = np.abs(prediction-target)
    return dict(count=len(target), mape_percent=float(100*np.mean(error/target)), max_percent_error=float(100*np.max(error/target)),
                rmse=float(np.sqrt(np.mean((prediction-target)**2))), max_absolute_error=float(np.max(error)))


def metric_check(pred, target, saved, label):
    for key, value in metrics(pred, target).items(): close(value, saved[key], label+':'+key)


def tridiagonal_apply(diagonal, off, vectors):
    """Matrix-vector algebra on already saved bands, not a decomposition."""
    answer = diagonal[:, None]*vectors
    answer[:-1] += off[:, None]*vectors[1:]
    answer[1:] += off[:, None]*vectors[:-1]
    return answer


def restore_fe_bands(q_full, spacing, hbar, mean_a, variance, z, nodes, weights,
                     source_off=False, constant_drift=None):
    """Element Gram algebra using saved nodes/weights; no physical solve."""
    qg = (q_full[:-1, None]+q_full[1:, None])/2+spacing*nodes[None, :]/2
    phi_left, phi_right = (1-nodes)/2, (1+nodes)/2
    if constant_drift is not None:
        drift = np.full_like(qg, constant_drift)
        variance = 0.
    else:
        drift = .2*qg**3+5*z*qg**4+.012*qg**5
        if not source_off: drift = drift-1+2*qg+mean_a*qg**2
        else: variance = 0.
    left = -hbar/spacing+drift*phi_left
    right = hbar/spacing+drift*phi_right
    potential = variance*qg**4
    ll = spacing/2*np.sum(weights*(left*left+potential*phi_left*phi_left), axis=1)
    rr = spacing/2*np.sum(weights*(right*right+potential*phi_right*phi_right), axis=1)
    lr = spacing/2*np.sum(weights*(left*right+potential*phi_left*phi_right), axis=1)
    diagonal = (rr[:-1]+ll[1:])/spacing
    off = lr[1:-1]/spacing
    q4ll = spacing/2*np.sum(weights*qg**4*phi_left**2, axis=1)
    q4rr = spacing/2*np.sum(weights*qg**4*phi_right**2, axis=1)
    q4lr = spacing/2*np.sum(weights*qg**4*phi_left*phi_right, axis=1)
    return diagonal, off, (q4rr[:-1]+q4ll[1:])/spacing, q4lr[1:-1]/spacing


def compact(a):
    return {**{key:a[key].copy() for key in ('theta', 'lambda_raw', 'energy', 'predicted_320', 'path_a')},
            'valid':bool(a['valid']), 'scale':float(a['scale']), 'N':int(a['N']), 'L':float(a['L']),
            'midpoint_count':int(a['midpoint_count']), 'form_key':str(a['form_key']),
            'mode':str(a['mode']), 'varoff':bool(a['varoff'])}


def occupations(a, record, name):
    states = a['states']; retained = states.shape[1]
    high_count = (int(a['N'])+4)//5
    momentum = dst(states, type=1, norm='ortho', axis=0, workers=1)
    high = np.sum(momentum[-high_count:]**2, axis=0)
    edge = np.sum(states[np.abs(a['q']) > .9*float(a['L'])]**2, axis=0)
    close(high, a['high_DST_occupation'], 'high_DST:'+name, atol=2e-13)
    close(edge, a['edge_occupation'], 'edge:'+name, atol=2e-13)
    verify(record['high_DST_mode_count'] == high_count, 'DST_count:'+name)
    windows = [(str(count), count) for count in (100, 320) if retained >= count]
    if retained < 100: windows = [('all_control_states', retained)]
    for label, count in windows:
        summary = record['state_diagnostics'][label]
        for key, val in [('edge_mean', np.mean(edge[:count])), ('edge_max', np.max(edge[:count])),
                         ('high_DST_mean', np.mean(high[:count])), ('high_DST_max', np.max(high[:count]))]:
            close(val, summary[key], 'occupation_summary:'+name+':'+label+':'+key)


def main():
    result, manifest = read('result.json'), read('manifest.json')
    verify(result['status'] in ('completed', 'completed_with_missing_roles'), 'completed_result')
    truth = np.asarray(read('known-targets.json')['ordinates'])
    verify(truth.shape == (320,) and np.all(np.diff(truth) > 0), 'target_order')
    with np.load(RUN/'quadrature.npz', allow_pickle=False) as quad:
        nodes, weights = quad['nodes'].copy(), quad['weights'].copy()
        moments = np.asarray([np.sum(weights*nodes**degree) for degree in range(14)])
        expected = np.asarray([2/(degree+1) if degree % 2 == 0 else 0. for degree in range(14)])
        close(moments, quad['moments_0_to_13'], 'saved_Gauss_moments', atol=0, rtol=0)
        close(expected, quad['expected_moments'], 'expected_Gauss_moments', atol=0, rtol=0)
    verify(nodes.shape == weights.shape == (7,) and np.all(weights > 0) and np.all(np.isfinite(nodes)) and np.all(np.isfinite(weights)), 'Gauss_nodes_weights')
    moment_error = float(np.max(np.abs(moments-expected)))
    verify(moment_error <= 1e-13 and read('quadrature.json')['passed'], 'Gauss_gate')
    close(moment_error, read('quadrature.json')['max_absolute_moment_error'], 'Gauss_record', atol=0, rtol=0)
    members, training, controls, counts = {}, {}, {}, Counter()
    residual_max = dict(FE_band_relative=0., state_absolute=0., state_relative=0., orthogonality=0.,
                        trace_relative=0., second_moment_relative=0.)
    negative_objects, invalid_objects = [], []
    paths = sorted((RUN/'evaluations').glob('*-N*.npz'))+[p for p in sorted(RUN.glob('*.npz')) if p.stem != 'quadrature']
    for path in paths:
        name = path.stem; record = json.loads(path.with_suffix('.json').read_text())
        with np.load(path, allow_pickle=False) as a:
            counts['physical_npz'] += 1
            N, length, spacing = int(a['N']), float(a['L']), float(a['spacing'])
            theta = a['theta']; hbar, ast, mass, z = theta
            form, mode, varoff, steps = str(a['form_key']), str(a['mode']), bool(a['varoff']), int(a['midpoint_count'])
            control = name.startswith('control-')
            close(theta, record['theta'], 'theta_record:'+name, atol=0, rtol=0)
            verify(N == record['N'] and length == record['L'] and steps == record['midpoint_count'] and form == record['form_key'], 'grid_record:'+name)
            close(spacing, 2*length/(N+1), 'spacing:'+name, atol=0, rtol=0)
            close(a['q_full'], -length+spacing*np.arange(N+2), 'q_full:'+name, atol=0, rtol=0)
            close(a['q'], a['q_full'][1:-1], 'q:'+name, atol=0, rtol=0)
            expected_mass = np.full(N+2, spacing); expected_mass[[0, -1]] = spacing/2
            close(a['mass_lumped_full'], expected_mass, 'full_cell_mass:'+name, atol=0, rtol=0)
            close(a['mass_diagonal'], np.full(N, spacing), 'Dirichlet_mass:'+name, atol=0, rtol=0)
            u = (np.arange(steps)+.5)/steps
            start, end = math.log(11.)**-2, math.log(310.)**-2
            path_a = 1.02+(ast-1.02)*(np.log(11+299*u)**-2-end)/(start-end)
            mean_a = float(np.mean(path_a)); variance = float(np.mean((path_a-mean_a)**2))
            effective = variance if form == 'V' and not varoff and mode == 'source' else 0.
            close(u, a['path_u'], 'path_u:'+name, atol=0, rtol=0)
            close(path_a, a['path_a'], 'path_a:'+name, atol=3e-15, rtol=0)
            for key, value in [('a_mean', mean_a), ('a_variance', variance), ('effective_variance', effective)]:
                close(value, a[key], 'path_moment:'+name+':'+key, atol=3e-15, rtol=0)
                close(float(a[key]), record[key], 'path_record:'+name+':'+key, atol=0, rtol=0)
            if not control:
                verify(np.all(theta >= [.12, 1.4, .3, -.006]) and np.all(theta <= [.22, 1.8, .9, .006]), 'theta_box:'+name)
                verify(N == int(name.rsplit('-N', 1)[1]), 'named_N:'+name)
                verify(steps == (128 if '-time128-' in name else 64), 'named_steps:'+name)
                verify(length == (10. if '-box10-' in name else 8.), 'named_L:'+name)
                verify(varoff == ('VAROFF' in name or 'SOURCEOFF' in name), 'named_varoff:'+name)
                verify(mode == ('sourceoff' if 'SOURCEOFF' in name else 'source'), 'named_mode:'+name)
            constant = float(a['constant_drift']) if 'constant_drift' in a else None
            restored = restore_fe_bands(a['q_full'], spacing, hbar, float(a['a_mean']), float(a['effective_variance']), z,
                                        nodes, weights, source_off=mode == 'sourceoff', constant_drift=constant)
            diagonal, off = a['J_diagonal'], a['J_off_diagonal']
            band_scale = max(1., float(np.max(np.abs(diagonal))), float(np.max(np.abs(off))))
            band_error = max(float(np.max(np.abs(restored[0]-diagonal))), float(np.max(np.abs(restored[1]-off))))/band_scale
            verify(band_error < 1e-12, 'FE_formula:'+name)
            residual_max['FE_band_relative'] = max(residual_max['FE_band_relative'], band_error)
            close(restored[2], a['q4_diagonal'], 'q4_diagonal:'+name, atol=2e-10, rtol=2e-12)
            close(restored[3], a['q4_off_diagonal'], 'q4_off:'+name, atol=2e-10, rtol=2e-12)
            raw = a['lambda_raw']; verify(raw.shape == (N,) and np.all(np.isfinite(raw)) and np.all(np.diff(raw) >= 0), 'raw_lambda:'+name)
            rows = np.abs(diagonal).copy(); rows[:-1] += np.abs(off); rows[1:] += np.abs(off)
            row_norm = float(np.max(rows)); tolerance = 64*np.finfo(float).eps*max(1., row_norm)
            close(tolerance, a['psd_tolerance'], 'PSD_tolerance:'+name, atol=0, rtol=0)
            close(row_norm, record['J_absolute_row_sum_max'], 'row_norm:'+name, atol=0, rtol=0)
            verify(raw[0] >= -tolerance and not record['raw_lambda_clipped'], 'PSD_raw_gate:'+name)
            negative_count = int(np.sum(raw < 0))
            verify(negative_count == record['negative_lambda_count'] and bool(negative_count) == record['small_negative_eigenvalues_noncertified'], 'raw_negative_record:'+name)
            if negative_count: negative_objects.append(dict(name=name, count=negative_count, minimum=float(raw[0]), tolerance=tolerance))
            radicand = mass*mass+raw; positive = np.isfinite(radicand) & (radicand > 0)
            energy = np.full(N, np.nan); energy[positive] = np.sqrt(radicand[positive]); finite = np.isfinite(energy)
            close(energy, a['energy'], 'energy:'+name, atol=0, rtol=0)
            verify(np.array_equal(positive, a['radicand_positive_mask']) and np.array_equal(finite, a['finite_mask']), 'masks:'+name)
            required = N if control else 320; reasons = []
            if N < required: reasons.append('INSUFFICIENT_ENERGY_COUNT')
            if not radicand[0] > 0: reasons.append('NONPOSITIVE_M_SQUARED_PLUS_LAMBDA_MIN')
            if not np.all(finite[:required]) or not np.all(energy[:required] > 0): reasons.append('PREFIX_ENERGY_NOT_FINITE_POSITIVE')
            if not np.all(np.diff(energy[:required]) >= 0): reasons.append('PREFIX_ENERGY_NOT_NONDECREASING')
            verify(reasons == a['invalid_reasons'].tolist() == record['invalid_reasons'], 'invalid_reasons:'+name)
            valid = not reasons; verify(valid == bool(a['valid']) == record['valid'], 'valid:'+name)
            if not valid: invalid_objects.append(name)
            close(a['target_100'], truth[:100], 'target100:'+name, atol=0, rtol=0)
            scale = truth[0]/energy[0] if finite[0] and energy[0] > 0 else np.nan
            close(scale, a['scale'], 'scale:'+name, atol=0, rtol=0)
            close(scale*energy[:min(N, 320)], a['predicted_320'], 'prediction:'+name, atol=0, rtol=0)
            if valid and not control: metric_check(a['predicted_320'][:100], truth[:100], record['training_metrics'], 'train_metric:'+name)
            else: verify(record['training_metrics'] is None, 'no_invalid_or_control_fit:'+name)
            trace, spectrum_trace = float(np.sum(diagonal)), float(np.sum(raw))
            fro, moment2 = float(np.sum(diagonal*diagonal)+2*np.sum(off*off)), float(np.sum(raw*raw))
            trace_error, second_error = abs(trace-spectrum_trace)/max(1., abs(trace)), abs(fro-moment2)/max(1., fro)
            for key, value in [('trace_J', trace), ('full_lambda_sum', spectrum_trace), ('trace_relative_difference', trace_error),
                               ('frobenius_squared_J', fro), ('full_lambda_squared_sum', moment2), ('second_moment_relative_difference', second_error)]:
                close(value, record[key], 'spectral_moment_record:'+name+':'+key)
            verify(max(trace_error, second_error) < 1e-11, 'spectral_moments:'+name)
            residual_max['trace_relative'] = max(residual_max['trace_relative'], trace_error)
            residual_max['second_moment_relative'] = max(residual_max['second_moment_relative'], second_error)
            if 'states' in a:
                counts['full_state_npz'] += 1
                states = a['states']; retained = min(N, 320)
                verify(states.shape == (N, retained), 'state_shape:'+name)
                error = np.sqrt(np.sum((tridiagonal_apply(diagonal, off, states)-states*raw[:retained])**2, axis=0))
                orth = norm(states.T@states-np.eye(retained)); relative = float(np.max(error))/max(1., row_norm)
                close(error, a['eigenvector_residual'], 'state_residual:'+name, atol=2e-10, rtol=2e-12)
                close(np.max(error), record['eigenvector_residual_max'], 'state_residual_record:'+name, atol=2e-10)
                close(relative, record['eigenvector_residual_relative_row_norm_max'], 'state_relative_record:'+name)
                close(orth, record['states_orthogonality_fro'], 'orthogonality_record:'+name)
                verify(relative < 1e-11 and orth < 1e-8, 'state_engineering_residual:'+name)
                residual_max['state_absolute'] = max(residual_max['state_absolute'], float(np.max(error)))
                residual_max['state_relative'] = max(residual_max['state_relative'], relative)
                residual_max['orthogonality'] = max(residual_max['orthogonality'], orth)
                occupations(a, record, name)
            if control:
                counts['control_npz'] += 1
                verify(N == 31 and length == 2., 'control_grid:'+name)
                controls[name] = {key:a[key].copy() for key in a.files if key != 'states'}
            else: (training if path.parent.name == 'evaluations' else members)[name] = compact(a)
    print('ARRAY_AUDIT_COMPLETE', dict(counts), flush=True)
    finish(result, manifest, truth, nodes, weights, controls, members, training, counts, residual_max, negative_objects, invalid_objects, moment_error)


def finish(result, manifest, truth, nodes, weights, controls, members, training, counts, residual_max, negative_objects, invalid_objects, moment_error):
    target_source = ROOT/'papers/253-structural-homotopy-search/evidence/run-1/evaluations/CS03-Q-QUARTIC-0103.npz'
    with np.load(target_source, allow_pickle=False) as old: portions = [old['target_100'].copy()]
    for folder, file, count in [
        ('251-constructive-fit-portfolio', 'reference-101-150.json', 50),
        ('253-structural-homotopy-search', 'reference-151-200.json', 50),
        ('254-global-forms-joint-fit', 'reference-201-240.json', 40),
        ('255-path-operator-multigrid', 'reference-241-300.json', 60),
        ('256-chronological-heat-spectrum', 'reference-301-320.json', 20)]:
        values = np.asarray([float(x) for x in json.loads((ROOT/'papers'/folder/'evidence/run-1'/file).read_text())['ordinates']])
        verify(len(values) == count, 'target_portion:'+file); portions.append(values)
    verify(np.array_equal(np.concatenate(portions), truth), 'original_target320')
    for name, constant in [('control-1-constant-zero', 0.), ('control-2-constant-point7', .7)]:
        a = controls[name]; angle = np.pi*np.arange(1, 32)/32
        expected = 4*a['theta'][0]**2/float(a['spacing'])**2*np.sin(angle/2)**2+constant**2*(2/3+np.cos(angle)/3)
        close(expected, a['expected_lambda'], 'analytic_control_reference:'+name, atol=0, rtol=0)
        verify(np.max(np.abs(expected-a['lambda_raw'])) <= 1e-10*max(1., np.max(np.abs(expected))), 'analytic_control_gate:'+name)
    mm, vv = controls['control-3-M-default'], controls['control-4-V-default']
    direct_diagonal, direct_off = np.zeros(31), np.zeros(30)
    for value in vv['path_a']:
        frame = restore_fe_bands(vv['q_full'], float(vv['spacing']), float(vv['theta'][0]), value, 0., float(vv['theta'][3]), nodes, weights)
        direct_diagonal += frame[0]; direct_off += frame[1]
    direct_diagonal /= 64; direct_off /= 64
    for key, direct, q4key in [('J_diagonal', direct_diagonal, 'q4_diagonal'), ('J_off_diagonal', direct_off, 'q4_off_diagonal')]:
        expected = mm[key]+float(vv['a_variance'])*vv[q4key]
        close(expected, vv['identity_expected_'+key], 'variance_identity_saved:'+key)
        close(direct, vv['direct_frame_mean_'+key], 'direct_frame_saved:'+key)
        close(expected, vv[key], 'variance_identity:'+key)
        close(direct, vv[key], 'direct_mean_Gram:'+key)
    em, ev = controls['control-5-M-end'], controls['control-6-V-end']
    for key in ('J_diagonal', 'J_off_diagonal', 'lambda_raw'):
        close(em[key], ev[key], 'endpoint_control:'+key, atol=1e-10)
    for name, a in controls.items():
        verify(read(name+'.json')['control_checks']['passed'], 'control_pass_record:'+name)
    rows, calls, frozen = read('unique-members.json'), read('calls.json'), read('winners-frozen.json')
    ranks, by_id = {}, {}
    for row in rows:
        eid, form = row['evaluation_id'], row['form_key']; by_id[eid] = row
        aa, bb = training[eid+'-N1023'], training[eid+'-N1279']
        for member in (aa, bb): close(member['theta'], row['theta'], 'pair_theta:'+eid, atol=0, rtol=0)
        valid = aa['valid'] and bb['valid']; verify(valid == row['valid'], 'pair_valid:'+eid)
        if not valid:
            verify(row['joint_score'] == 1e30 and row['status'] == 'INVALID_MEMBER', 'invalid_penalty:'+eid)
            continue
        ma, mb = metrics(aa['predicted_320'][:100], truth[:100]), metrics(bb['predicted_320'][:100], truth[:100])
        g = float(100*np.max(np.abs(aa['predicted_320'][:100]-bb['predicted_320'][:100])/truth[:100]))
        maximum_m, maximum_w = max(ma['mape_percent'], mb['mape_percent']), max(ma['max_percent_error'], mb['max_percent_error'])
        score = max(maximum_m/MREF, maximum_w/WREF, g/2)
        for key, value in [('joint_score', score), ('J_minus_1', score-1), ('max_mape_percent', maximum_m), ('max_percent_error', maximum_w), ('G100_percent', g)]:
            close(value, row[key], 'pair_score:'+eid+':'+key, atol=0, rtol=0)
        ranks.setdefault(form, []).append((score, maximum_m, maximum_w, g, eid))
    verify(frozen['roles'] == result['roles'] and set(ranks) == set(result['roles']), 'frozen_roles')
    for form, ranked in ranks.items():
        winner = min(ranked)[-1]; verify(winner == result['roles'][form]['evaluation_id'], 'winner:'+form)
        for N in (1023, 1279):
            for key in ('theta', 'lambda_raw', 'energy', 'predicted_320'):
                close(members[f'winner-{form}-N{N}'][key], training[f'{winner}-N{N}'][key], 'winner_arrays:'+form+':'+key, atol=0, rtol=0)
    primary = min((min(ranked), form) for form, ranked in ranks.items())[1] if ranks else None
    verify(primary == result['global_joint_winner'] == frozen['global_joint_winner'], 'primary_rank')
    for name, member in members.items(): close(member['theta'], result['roles'][member['form_key']]['theta'], 'fixed_theta:'+name, atol=0, rtol=0)
    if primary is not None:
        base, expanded = members[f'post-{primary}-N4095'], members[f'post-{primary}-box10-N5119']
        verify(2*base['L']/(base['N']+1) == 2*expanded['L']/(expanded['N']+1) == 1/256, 'box_same_spacing')
    if 'V' in result['roles']:
        for N in (3071, 4095):
            with np.load(RUN/f'post-V-N{N}.npz', allow_pickle=False) as v, np.load(RUN/f'ablation-V-VAROFF-N{N}.npz', allow_pickle=False) as m:
                for key in ('theta', 'path_a', 'a_mean', 'a_variance', 'q', 'mass_diagonal'):
                    close(v[key], m[key], 'VAROFF_same_owner:'+str(N)+':'+key, atol=0, rtol=0)
                verify(float(m['effective_variance']) == 0. and bool(m['varoff']), 'VAROFF_only_variance:'+str(N))
                for key, q4key in [('J_diagonal', 'q4_diagonal'), ('J_off_diagonal', 'q4_off_diagonal')]:
                    close(v[key], m[key]+float(v['a_variance'])*v[q4key], 'VAROFF_Gram_identity:'+str(N)+':'+key, atol=2e-9, rtol=2e-12)
    fits, comparisons = read('development-fit-metrics.json'), read('comparisons.json')
    verify(set(fits) == set(members), 'fit_object_coverage')
    for name, saved in fits.items():
        if not members[name]['valid']:
            verify(saved is None, 'invalid_fit:'+name); continue
        for window, (start, stop) in WINDOWS.items(): metric_check(members[name]['predicted_320'][start:stop], truth[start:stop], saved[window], 'fit:'+name+':'+window)
    verify(fits == result['fit_metrics'], 'result_fits')
    for name, saved in comparisons.items():
        aa, bb = members[saved['left']], members[saved['right']]
        verify(saved['G_threshold_percent'] == 2., 'comparison_threshold:'+name)
        if not (aa['valid'] and bb['valid']):
            verify(saved['windows'] is None and saved['right_minus_left_fit_percentage_points'] is None, 'invalid_comparison:'+name); continue
        for window, (start, stop) in WINDOWS.items():
            gap = float(100*np.max(np.abs(aa['predicted_320'][start:stop]-bb['predicted_320'][start:stop])/truth[start:stop]))
            raw = float(100*np.max(np.abs(aa['energy'][start:stop]-bb['energy'][start:stop])/aa['energy'][start:stop]))
            lam = float(np.max(np.abs(aa['lambda_raw'][start:stop]-bb['lambda_raw'][start:stop])))
            for key, value in [('G_percent', gap), ('raw_energy_max_relative_percent', raw), ('raw_lambda_max_absolute_difference', lam)]:
                close(value, saved['windows'][window][key], 'comparison:'+name+':'+window+':'+key, atol=0, rtol=0)
            verify((gap < 2) == saved['windows'][window]['G_below_threshold'], 'comparison_gate:'+name+':'+window)
            for key in ('mape_percent', 'max_percent_error'):
                close(fits[saved['right']][window][key]-fits[saved['left']][window][key], saved['right_minus_left_fit_percentage_points'][window][key], 'comparison_fit_change:'+name+':'+window+':'+key, atol=0, rtol=0)
    verify(comparisons == result['comparisons'], 'result_comparisons')
    external = read('external-history-comparator.json')
    verify(not external['raw_energy_comparison_permitted'] and sha(ROOT/external['source']) == external['source_sha256'], 'external_owner_hash')
    with np.load(ROOT/external['source'], allow_pickle=False) as old:
        close(external['predicted_320'], old['predicted_320'], 'external_prediction', atol=0, rtol=0)
        for window, (start, stop) in WINDOWS.items(): metric_check(old['predicted_320'][start:stop], truth[start:stop], external['fit_metrics'][window], 'external_fit:'+window)
    close(external['fit_metrics']['1-320']['mape_percent'], FULLREF, 'external_reference', atol=1e-10, rtol=0)
    assessments = read('finite-discovery-assessments.json')
    for form, row in assessments.items():
        training_better = all(fits[f'winner-{form}-N{N}']['1-100']['mape_percent'] < MREF and fits[f'winner-{form}-N{N}']['1-100']['max_percent_error'] < WREF for N in (1023, 1279))
        fine = {suffix: all(v['G_below_threshold'] for v in comparisons[form+'-'+suffix]['windows'].values())
                if comparisons[form+'-'+suffix]['windows'] is not None else None for suffix in ('N2047-N3071', 'N3071-N4095')}
        full_better = bool(fits[f'post-{form}-N4095'] is not None and fits[f'post-{form}-N4095']['1-320']['mape_percent'] < FULLREF)
        partial = bool(result['roles'][form]['joint_score'] < 1 and training_better and full_better and all(value is True for value in fine.values()))
        special = {key: all(v['G_below_threshold'] for v in comparisons[form+'-'+key]['windows'].values())
                   if comparisons[form+'-'+key]['windows'] is not None else None for key in ('time128', 'box10')} if primary == form else None
        complete = bool(partial and primary == form and all(value is True for value in special.values()))
        expected_status = ('NECESSARY_FINITE_ADVANCE_CONDITIONS_MET_MAGNITUDE_REVIEW_REQUIRED' if complete else
                           'PARTIAL_CONDITIONS_MET_PRIMARY_ONLY_DIAGNOSTICS_NOT_RUN' if partial and primary != form else 'NECESSARY_FINITE_ADVANCE_CONDITIONS_NOT_MET')
        verify(row['each_training_M_W_below_external_reference'] == training_better and row['N4095_full320_M_below_external_reference'] == full_better, 'assessment_fit:'+form)
        verify(row['fine_grid_checks'] == fine and row['own_time_box_checks'] == special, 'assessment_own_checks:'+form)
        verify(row['training_and_fine_necessary_conditions_met'] == partial and row['full_necessary_conditions_met'] == complete and row['status'] == expected_status, 'assessment_status:'+form)
    verify(assessments == result['finite_discovery_assessments'], 'result_assessments')
    variance = read('variance-effect-assessment.json')
    if 'V' in result['roles']:
        verify(variance['status'] == 'DESCRIPTIVE_SAME_THETA_VAROFF_ONLY' and variance['independently_optimized_M_is_not_VAROFF_control'] and variance['time_order_effect_not_claimed'], 'variance_scope')
        for N in (3071, 4095): verify(variance['same_theta_VAROFF_comparisons'][str(N)] == comparisons[f'V-VAROFF-N{N}'], 'variance_comparison:'+str(N))
    verify(variance == result['variance_effect_assessment'], 'result_variance')
    csv_count, object_counts = 0, Counter()
    with (RUN/'points.csv').open(newline='') as stream:
        for row in csv.DictReader(stream):
            name, index = row['object_id'], int(row['index'])-1; a = members[name]
            target, pred, energy, lam = truth[index], a['predicted_320'][index], a['energy'][index], a['lambda_raw'][index]
            for key, value in [('target', target), ('predicted', pred), ('energy', energy), ('lambda_raw', lam), ('residual', pred-target), ('percent_error', 100*abs(pred-target)/target)]:
                close(float(row[key]), value, 'csv:'+key, atol=0, rtol=0)
            verify(row['valid'] == str(a['valid']) and row['form_key'] == a['form_key'] and int(row['N']) == a['N'] and float(row['L']) == a['L'] and int(row['midpoint_count']) == a['midpoint_count'], 'csv_metadata')
            verify(row['window'] == ('1-100' if index < 100 else '101-300' if index < 300 else '301-320'), 'csv_window')
            csv_count += 1; object_counts[name] += 1
    verify(set(object_counts) == set(members) and all(v == 320 for v in object_counts.values()), 'csv_coverage')
    for path, expected in manifest['inputs'].items(): verify(sha(ROOT/path) == expected, 'input_hash:'+path)
    verify(sha(PACKAGE/'run_search.py') == manifest['script_sha256'] == RUNNER_SHA, 'runner_hash')
    verify(sha(PACKAGE/'input-locks.json') == manifest['input_locks_sha256'], 'locks_hash')
    freeze = read('training-arrays-frozen.json')
    for path, expected in freeze['files_sha256'].items(): verify(sha(RUN/path) == expected, 'frozen_hash:'+path)
    verify(sha(RUN/'winners-frozen.json') == freeze['winner_identity_sha256'] == result['winner_identity_sha256'], 'winner_identity_hash')
    inventory = read('file-inventory.json')['files']
    for name, row in inventory.items():
        verify((RUN/name).stat().st_size == row['bytes'], 'inventory_size:'+name)
        verify(sha(RUN/name) == row['sha256'], 'inventory_hash:'+name)
    verify(set(inventory) == {str(p.relative_to(RUN)) for p in RUN.rglob('*') if p.is_file() and p.name != 'file-inventory.json'}, 'inventory_coverage')
    events = [json.loads(line) for line in (RUN/'events.jsonl').read_text().splitlines()]
    names = [row['event'] for row in events]
    verify(names.index('winner_identities_frozen') < names.index('training_arrays_frozen') < names.index('development_reference_read_start'), 'freeze_order')
    verify(max(i for i, name in enumerate(names) if name == 'pair_complete') < names.index('winner_identities_frozen'), 'no_postfreeze_training')
    verify(names[-1] == 'completed' and 'failed' not in names, 'completed_events')
    verify(calls == [json.loads(line) for line in (RUN/'calls.jsonl').read_text().splitlines()] and len(calls) == result['calls'] <= 66 and len(rows) == result['unique_members'], 'call_counts')
    verify(sum(bool(row['cached']) for row in calls) == result['cached_calls'], 'cache_count')
    for call in calls:
        for key in ('theta', 'form_key', 'valid', 'joint_score'): verify(call[key] == by_id[call['evaluation_id']][key], 'call_identity:'+key)
    counter = result['counters']
    verify(counter['forwards_attempted'] == counter['forwards_completed'] == counter['physical_eigh_attempted'] == counter['physical_eigh_completed'] == names.count('forward_start') == names.count('physical_eigh_complete') <= 149, 'physical_counts')
    for stage, limit in [('control', 6), ('training', 132), ('postfreeze', 8), ('ablation', 3)]:
        number = sum(row['event'] == 'forward_start' and row['stage'] == stage for row in events)
        verify(counter[stage+'_forwards_attempted'] == counter[stage+'_forwards_completed'] == number <= limit, 'stage_count:'+stage)
    verify(counter['quadrature_constructors_attempted'] == counter['quadrature_constructors_completed'] == names.count('quadrature_constructor_start') == names.count('quadrature_constructor_complete') == 1, 'one_quadrature_constructor')
    verify(counter['control_direct_frame_gram_assemblies'] == 64 and counter['cell_gram_assemblies_attempted'] == counter['cell_gram_assemblies_completed'] == counter['forwards_completed']+64, 'Gram_assembly_counts')
    verify(counter['svd_calls'] == counter['extra_state_eigh_calls'] == counter['new_target_generations'] == 0, 'zero_extra_science')
    verify(counter['training_forwards_completed'] == 2*len(rows) and len(training) == 2*len(rows), 'paired_training_count')
    verify(counts['physical_npz'] == counter['forwards_completed']+2*len(result['roles']) and counts['full_state_npz'] == counter['full_arrays_saved']+6 and counts['control_npz'] == 6, 'array_counts')
    verify(result['invalid_unique_members'] == sum(not row['valid'] for row in rows), 'invalid_pair_count')
    summary = dict(status='ANALYZED' if not failures else 'ISSUES_FOUND', failures=failures, checks=dict(checks),
        maximum_recomputation_differences=maxima, array_counts=dict(counts), physical_decompositions=counter['physical_eigh_completed'],
        Gauss_constructor_count=counter['quadrature_constructors_completed'], Gauss_moment_max_error=moment_error,
        calls=len(calls), unique_training_pairs=len(rows), cached_calls=result['cached_calls'], invalid_objects=invalid_objects,
        raw_negative_lambda_objects=negative_objects, fitted_objects=len(members), csv_rows=csv_count,
        fit_windows=sum(v is not None for v in fits.values())*4, comparison_windows=sum(v['windows'] is not None for v in comparisons.values())*4,
        input_hashes=len(manifest['inputs']), training_frozen_files=len(freeze['files_sha256']), inventory_files=len(inventory),
        residual_maxima=residual_max, counters=counter, assessments=assessments,
        winners={key:{field:value[field] for field in ('evaluation_id', 'theta', 'joint_score', 'max_mape_percent', 'max_percent_error', 'G100_percent')} for key, value in result['roles'].items()},
        checker_sha256=sha(Path(__file__)), scope='Saved evidence and FE-band algebra only; no physical eig/SVD/optimization/runner import or new target.',
        missing_state_limit='Nonwinner eigenvectors absent; their bands, all raw eigenvalues, moments, energy and ranking checked, not missing state equations.')
    print(json.dumps(summary, ensure_ascii=False, indent=2, allow_nan=False))
    if failures: raise SystemExit(1)


if __name__ == '__main__':
    main()
