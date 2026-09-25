#!/usr/bin/env python3
"""CS12 saved-output analysis only; run after the parent confirms run exit0.

No runner import, forward, four-step product, SVD/eigh, optimizer or new target.
Reconstructs saved kernel blocks and scalar readouts; checks saved state equations,
FFT occupations, closed-form small controls, metrics, events and hashes.
Writes nothing; prints a JSON summary. No independent scientific rerun is claimed.
"""
import csv
import hashlib
import json
import math
from collections import Counter
from pathlib import Path

import numpy as np
from scipy import fft

PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[1]
RUN = PACKAGE/'evidence/run-1'
RUNNER_SHA = 'da7e7cabe03ae29d49cd1bb3913cb4addc6110f9d4b248e5b88bc036e335bc19'
WINDOWS = {'1-100': (0, 100), '101-300': (100, 300), '301-320': (300, 320), '1-320': (0, 320)}
MREF, WREF, FULLREF = 1.695273790061038, 5.234299091683695, 3.5251249515592384
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
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024*1024), b''): h.update(block)
    return h.hexdigest()


def metrics(prediction, target):
    error = np.abs(prediction-target)
    return dict(mape_percent=float(100*np.mean(error/target)), max_percent_error=float(100*np.max(error/target)),
                mae=float(np.mean(error)), mse=float(np.mean(error**2)), rmse=float(np.sqrt(np.mean(error**2))))


def metric_check(pred, target, saved, label):
    for key, value in metrics(pred, target).items(): close(value, saved[key], label+':'+key)


def compact(a):
    return dict(pred=a['predicted_320'].copy(), energy=a['energy'][:320].copy(), sigma=a['sigma'].copy(),
                valid=bool(a['resolution_valid']), scale=float(a['scale']), theta=a['theta'].copy(),
                coefficients=a['coefficients'].copy(), times=a['times'].copy(), L=float(a['L']),
                n=int(a['n']), dimension=int(a['dimension']), form=str(a['form_key']), epsilon=float(a['epsilon']))


def path_coefficients(form, parameter):
    if form == 'A': return np.full(4, parameter)
    u = np.array([0., 1/3, 2/3, 1.])
    start, end = math.log(11.)**-2, math.log(310.)**-2
    weight = (np.log(11+299*u)**-2-end)/(start-end)
    weight[0], weight[-1] = 1., 0.
    result = 1.02+(parameter-1.02)*weight
    result[0], result[-1] = parameter, 1.02
    return result


def state_check(a, record, side, n, label):
    states = a['singular_'+side]
    d, retained = states.shape
    constant = np.ones(d)/math.sqrt(d)
    projection = constant@states
    transformed = fft.fftn(states.reshape(n, n, retained), axes=(0, 1), norm='ortho', workers=1)
    modes = np.arange(n); modes[modes > n//2] -= n
    cutoff = math.floor(.4*n)
    high = np.maximum(np.abs(modes[:, None]), np.abs(modes[None, :])) >= cutoff
    occupancy = np.sum(np.abs(transformed[high])**2, axis=0)
    close(projection, a[side+'_constant_projections'], 'projection:'+label+':'+side, atol=2e-13)
    close(projection[1:], a[side+'_nontrivial_constant_projections'], 'nonconstant_projection:'+label+':'+side, atol=2e-13)
    close(occupancy, a[side+'_high_frequency_occupation'], 'FFT_occupation:'+label+':'+side, atol=2e-13)
    summary = record[side+'_state_diagnostics']
    verify(summary['frequency_threshold'] == cutoff, 'FFT_cutoff:'+label)
    for count in (100, 320):
        if retained < count+1: continue
        for key, value in [('high_frequency_max', np.max(occupancy[1:count+1])),
                           ('high_frequency_mean', np.mean(occupancy[1:count+1])),
                           ('constant_projection_abs_max', np.max(np.abs(projection[1:count+1])))]:
            close(value, summary['windows'][str(count)][key], 'FFT_summary:'+label+':'+key)
    distance = min(norm(states[:, 0]-constant), norm(states[:, 0]+constant))
    close(projection[0], record['constant_'+side+'_inner_product'], 'constant_inner_product:'+label+':'+side, atol=2e-13)
    close(distance, record['constant_'+side+'_sign_distance'], 'constant_distance:'+label+':'+side, atol=2e-13)
    return float(projection[0]), distance


def main():
    result, manifest = read('result.json'), read('manifest.json')
    verify(result['status'] in ('completed', 'completed_with_missing_roles'), 'completed_result')
    truth = np.asarray(read('known-targets.json')['ordinates'])
    verify(len(truth) == 320 and np.all(np.diff(truth) > 0), 'truth_order')
    members, training, controls, counts = {}, {}, {}, Counter()
    residual_max = dict(forward=0., transpose=0., orthogonality=0., frobenius_relative=0.,
                        product_row_sum=0., product_column_sum=0., constant_left=0., constant_right=0.,
                        block_row_sum=0., block_column_sum=0., block_symmetry=0., nontrivial_constant_projection=0.)
    files = sorted((RUN/'evaluations').glob('*-n*.npz'))+sorted(RUN.glob('*.npz'))
    for path in files:
        name = path.stem
        record = json.loads(path.with_suffix('.json').read_text())
        with np.load(path, allow_pickle=False) as a:
            counts['kernel_npz'] += 1
            n, d, length = int(a['n']), int(a['dimension']), float(a['L'])
            theta, form, epsilon = a['theta'], str(a['form_key']), float(a['epsilon'])
            q, times, coefficients, steps = a['q'], a['times'], a['coefficients'], int(a['step_count'])
            control = 'control_only' in a
            verify(d == n*n and n % 2 == 1 and length == 2., 'grid_dimension:'+name)
            verify(record['n'] == n and record['dimension'] == d and record['L'] == length, 'grid_record:'+name)
            close(theta, record['theta'], 'theta_record:'+name, atol=0, rtol=0)
            close(q, -length+2*length*np.arange(n)/n, 'q:'+name, atol=0, rtol=0)
            close(epsilon, theta[0], 'epsilon:'+name, atol=0, rtol=0)
            close(a['target_100'], truth[:100], 'target100:'+name, atol=0, rtol=0)
            close(coefficients, record['coefficients'], 'coefficient_record:'+name, atol=0, rtol=0)
            close(times, record['times'], 'times_record:'+name, atol=0, rtol=0)
            verify(steps == len(coefficients) == len(times) and steps in (1, 4), 'steps:'+name)
            if not control:
                verify(n == int(name.rsplit('-n', 1)[1]), 'named_grid:'+name)
                verify(np.all(theta >= [.04, 1.02]) and np.all(theta <= [.32, 2.10]), 'parameter_box:'+name)
                expected_coeff = path_coefficients(form, theta[1])
                if 'ablation-D-END-' in name: expected_coeff[[0, -1]] = 0.
                if 'ablation-D-ZERO-' in name: expected_coeff[:] = 0.
                close(coefficients, expected_coeff, 'path:'+name, atol=0, rtol=0)
                close(times, [0., 1/3, 2/3, 1.], 'times:'+name, atol=0, rtol=0)
            else:
                verify(n == 7 and epsilon == .30, 'control_grid_epsilon:'+name)
                control_coeff = {
                    'control-1-one-step': np.array([1.30]), 'control-2-zero-source': np.zeros(4),
                    'control-3-D-default': path_coefficients('D', 1.655042492001211),
                    'control-4-D-reverse': path_coefficients('D', 1.655042492001211)[::-1],
                    'control-5-A-end': np.full(4, 1.02), 'control-6-D-end': np.full(4, 1.02)}[name]
                close(coefficients, control_coeff, 'control_coefficients:'+name, atol=0, rtol=0)
                close(times, [0.] if steps == 1 else [0., 1/3, 2/3, 1.], 'control_times:'+name, atol=0, rtol=0)
            residual = q[None, None, :]+q[0]-1+coefficients[:, None, None]*q[None, :, None]**2
            raw = np.exp(-(2*length/np.pi)**2*np.sin(np.pi*residual/(2*length))**2/(2*epsilon**2))
            z = np.sum(raw, axis=2)
            close(raw, a['raw_first_column'], 'raw_kernel:'+name, atol=0, rtol=0)
            close(z, a['Z'], 'normalizer:'+name, atol=0, rtol=0)
            circular = (np.arange(n)[:, None]+np.arange(n)[None, :]) % n
            expected_blocks = (raw/z[:, :, None])[:, :, circular]
            blocks = a['K_blocks']
            verify(blocks.shape == (steps, n, n, n), 'block_shape:'+name)
            close(blocks, expected_blocks, 'blocks:'+name, atol=0, rtol=0)
            verify(np.all(np.isfinite(blocks)) and np.min(blocks) > 0 and np.min(raw) > 0 and np.min(z) > 0, 'kernel_positive:'+name)
            br = np.max(np.abs(np.sum(blocks, axis=3)-1), axis=(1, 2))
            bc = np.max(np.abs(np.sum(blocks, axis=2)-1), axis=(1, 2))
            bs = np.max(np.abs(blocks-blocks.swapaxes(2, 3)), axis=(1, 2, 3))
            # NPZ stores C-contiguous blocks, unlike the original advanced-index
            # view. Identical entries can have different floating reduction order.
            # Check original diagnostics exactly from restored original layout;
            # independently enforce the unchanged 1e-12 gate on loaded blocks.
            original_br = np.max(np.abs(np.sum(expected_blocks, axis=3)-1), axis=(1, 2))
            original_bc = np.max(np.abs(np.sum(expected_blocks, axis=2)-1), axis=(1, 2))
            original_bs = np.max(np.abs(expected_blocks-expected_blocks.swapaxes(2, 3)), axis=(1, 2, 3))
            for key, values, original_values in [('row_sum', br, original_br), ('column_sum', bc, original_bc), ('symmetry', bs, original_bs)]:
                close(original_values, a['block_'+key+'_errors'], 'block_saved:'+name+':'+key, atol=0, rtol=0)
                close(np.max(original_values), record['block_'+key+'_error_max'], 'block_record:'+name+':'+key, atol=0, rtol=0)
                close(values, original_values, 'block_layout_reduction:'+name+':'+key, atol=4*n*np.finfo(float).eps, rtol=0)
                residual_max['block_'+key] = max(residual_max['block_'+key], float(np.max(values)))
            verify(np.max(br) <= 1e-12 and np.max(bc) <= 1e-12, 'block_stochastic_gate:'+name)
            sigma = a['sigma']; nontrivial = sigma[1:]
            verify(sigma.shape == (d,), 'sigma_dimension:'+name)
            energy = np.full(d-1, np.nan)
            positive = np.isfinite(nontrivial) & (nontrivial > 0)
            energy[positive] = -np.log(nontrivial[positive])/steps
            mask = positive & np.isfinite(energy) & (energy > 0)
            close(energy, a['energy'], 'energy:'+name, atol=0, rtol=0)
            verify(np.array_equal(mask, a['energy_resolved_mask']), 'energy_mask:'+name)
            verify(np.array_equal(np.arange(1, d), a['energy_sigma_indices']), 'energy_sigma_indices:'+name)
            verify(int(np.count_nonzero(mask)) == record['resolved_nontrivial_energy_count'], 'resolved_count:'+name)
            ldot, rdot = record['constant_left_inner_product'], record['constant_right_inner_product']
            ld, rd = record['constant_left_sign_distance'], record['constant_right_sign_distance']
            if 'C' in a:
                counts['full_C'] += 1
                c, left, right = a['C'], a['singular_left'], a['singular_right']
                retained = d if control else 321
                verify(c.shape == (d, d) and left.shape == right.shape == (d, retained), 'full_shapes:'+name)
                verify(not np.iscomplexobj(c) and np.all(np.isfinite(c)) and np.min(c) >= 0, 'nonnegative_real_C:'+name)
                constant = np.ones(d)/math.sqrt(d)
                close(a['constant_vector'], constant, 'constant_vector:'+name, atol=0, rtol=0)
                pr, pc = np.max(np.abs(np.sum(c, axis=1)-1)), np.max(np.abs(np.sum(c, axis=0)-1))
                cr, cl = norm(c@constant-constant), norm(c.T@constant-constant)
                for key, value in [('product_row_sum_error', pr), ('product_column_sum_error', pc),
                                   ('right_constant_residual', cr), ('left_constant_residual', cl)]:
                    close(value, record[key], 'product_record:'+name+':'+key)
                verify(max(pr, pc, cr, cl) <= 1e-10, 'product_gate:'+name)
                fwd = np.sqrt(np.sum((c@right-left*sigma[:retained])**2, axis=0))
                trans = np.sqrt(np.sum((c.T@left-right*sigma[:retained])**2, axis=0))
                for key, value in [('forward', fwd), ('transpose', trans)]:
                    close(value, a['singular_'+key+'_residual'], 'singular_saved:'+name+':'+key, atol=2e-13)
                    close(np.max(value), record['singular_'+key+'_residual_max'], 'singular_record:'+name+':'+key, atol=2e-13)
                    residual_max[key] = max(residual_max[key], float(np.max(value)))
                lo, ro = norm(left.T@left-np.eye(retained)), norm(right.T@right-np.eye(retained))
                fro, moment = float(np.sum(c*c)), float(np.sum(sigma*sigma))
                for key, value in [('left_orthogonality_fro', lo), ('right_orthogonality_fro', ro),
                                   ('frobenius_squared', fro), ('full_sigma_squared_sum', moment),
                                   ('frobenius_moment_relative_difference', abs(fro-moment)/fro)]:
                    close(value, record[key], 'state_record:'+name+':'+key)
                ldot, ld = state_check(a, record, 'left', n, name)
                rdot, rd = state_check(a, record, 'right', n, name)
                for key, val in [('orthogonality', max(lo, ro)), ('frobenius_relative', abs(fro-moment)/fro),
                                 ('product_row_sum', pr), ('product_column_sum', pc), ('constant_left', cl), ('constant_right', cr)]:
                    residual_max[key] = max(residual_max[key], float(val))
                if not control:
                    residual_max['nontrivial_constant_projection'] = max(residual_max['nontrivial_constant_projection'],
                        float(np.max(np.abs(a['left_nontrivial_constant_projections']))), float(np.max(np.abs(a['right_nontrivial_constant_projections']))))
                else:
                    controls[name] = {key:a[key].copy() for key in ('C', 'sigma', 'K_blocks', 'coefficients', 'theta', 'times')}
                    if 'expected_matrix' in a: controls[name]['expected_matrix'] = a['expected_matrix'].copy()
                    if 'expected_sigma' in a: controls[name]['expected_sigma'] = a['expected_sigma'].copy()
            verify(bool(ldot*rdot > 0) == record['constant_signs_consistent'], 'constant_signs:'+name)
            if control:
                counts['controls'] += 1
                verify(record['status'] == 'CONTROL_ONLY' and record['resolution_valid'] is None and not record['formal_unique_constant_gate_applied'], 'control_exception:'+name)
                continue
            reasons = []
            if not np.isfinite(sigma[0]) or abs(sigma[0]-1) > 1e-10: reasons.append('CONSERVATIVE_SIGMA0_NOT_ONE')
            if d < 321 or not np.all(np.isfinite(sigma[:321])) or not np.all(sigma[:321] > 0): reasons.append('REQUIRED_321_SINGULAR_VALUES_NOT_POSITIVE_FINITE')
            if not np.all(np.diff(sigma[:321]) <= 0): reasons.append('REQUIRED_SINGULAR_VALUES_NOT_DESCENDING')
            ratio = float(sigma[320]/sigma[0]) if d >= 321 and sigma[0] > 0 else np.nan
            if not np.isfinite(ratio) or ratio < 1e-10: reasons.append('SIGMA320_RELATIVE_RESOLUTION_BELOW_1E-10')
            if not (np.isfinite(sigma[1]) and sigma[1] < 1 and 1-sigma[1] >= 1e-8): reasons.append('NONTRIVIAL_GAP_BELOW_1E-8')
            if ld > 1e-6 or rd > 1e-6: reasons.append('TOP_SINGULAR_STATES_NOT_CONSTANT')
            if not ldot*rdot > 0: reasons.append('TOP_CONSTANT_STATE_SIGNS_INCONSISTENT')
            if len(energy) < 320 or not np.all(mask[:320]): reasons.append('REQUIRED_NONTRIVIAL_ENERGIES_NOT_POSITIVE_FINITE')
            verify(reasons == a['invalid_reasons'].tolist() == record['invalid_reasons'], 'invalid_reasons:'+name)
            valid = not reasons
            verify(valid == bool(a['resolution_valid']) == record['resolution_valid'], 'valid:'+name)
            verify(int(a['excluded_conservation_modes']) == 1 and record['required_sigma_count'] == 321, 'one_excluded_mode:'+name)
            counts['invalid_formal_npz'] += int(not valid)
            scale = truth[0]/energy[0] if np.isfinite(energy[0]) and energy[0] > 0 else np.nan
            prediction = scale*energy[:320] if np.isfinite(scale) else np.full(320, np.nan)
            close(a['scale'], scale, 'scale:'+name, atol=0, rtol=0)
            close(a['predicted_320'], prediction, 'prediction:'+name, atol=0, rtol=0)
            if valid: metric_check(prediction[:100], truth[:100], record['training_metrics'], 'training_metrics:'+name)
            else: verify(record['training_metrics'] is None, 'invalid_metrics:'+name)
            (training if path.parent.name == 'evaluations' else members)[name] = compact(a)
    print('ARRAY_AUDIT_COMPLETE', dict(counts), flush=True)
    finish(result, manifest, truth, members, training, controls, counts, residual_max)


def finish(result, manifest, truth, members, training, controls, counts, residual_max):
    target_path = ROOT/'papers/253-structural-homotopy-search/evidence/run-1/evaluations/CS03-Q-QUARTIC-0103.npz'
    with np.load(target_path, allow_pickle=False) as old: portions = [old['target_100'].copy()]
    for folder, file, count in [
        ('251-constructive-fit-portfolio', 'reference-101-150.json', 50),
        ('253-structural-homotopy-search', 'reference-151-200.json', 50),
        ('254-global-forms-joint-fit', 'reference-201-240.json', 40),
        ('255-path-operator-multigrid', 'reference-241-300.json', 60),
        ('256-chronological-heat-spectrum', 'reference-301-320.json', 20)]:
        values = np.asarray([float(x) for x in json.loads((ROOT/'papers'/folder/'evidence/run-1'/file).read_text())['ordinates']])
        verify(len(values) == count, 'target_portion:'+file)
        portions.append(values)
    verify(np.array_equal(np.concatenate(portions), truth), 'target320_source_identity')
    aliases = read('ablation-aliases.json')
    for name, row in aliases.items():
        source = members[row['source_object']]
        requested = path_coefficients(row['requested_form'], row['requested_theta'][1])
        if '-END-' in name: requested[[0, -1]] = 0.
        if '-ZERO-' in name: requested[:] = 0.
        close(requested, row['requested_coefficients'], 'alias_requested_path:'+name, atol=0, rtol=0)
        verify(row['status'] == 'EXACT_OWNER_ALIAS' and not row['additional_forward_or_svd'] and row['budget_not_transferred'], 'alias_policy:'+name)
        close(source['epsilon'], row['requested_theta'][0], 'alias_epsilon:'+name, atol=0, rtol=0)
        close(source['coefficients'], row['requested_coefficients'], 'alias_coefficients:'+name, atol=0, rtol=0)
        close(source['times'], row['requested_times'], 'alias_times:'+name, atol=0, rtol=0)
        verify(source['n'] == row['n'] and source['L'] == row['L'], 'alias_grid:'+name)
        key = [row['n'], float(row['requested_theta'][0]).hex(), float(row['L']).hex(), 'endpoint-periodic-i*n+j',
               'column-forward-circular-Hankel-own-Z', [float(v).hex() for v in row['requested_times']],
               [float(v).hex() for v in row['requested_coefficients']]]
        verify(key == row['exact_owner_key'], 'alias_exact_key:'+name)
        verify(sha(RUN/row['source_npz']) == row['source_sha256'], 'alias_npz_hash:'+name)
        verify(sha(RUN/(row['source_object']+'.json')) == row['source_json_sha256'], 'alias_json_hash:'+name)
        verify(not (RUN/(name+'.npz')).exists(), 'alias_no_duplicate_npz:'+name)
        members[name] = {**source, 'form':row['requested_form'], 'theta':np.asarray(row['requested_theta'])}
    rows, calls, frozen = read('unique-members.json'), read('calls.json'), read('winners-frozen.json')
    ranked, by_id, invalid_ids = {}, {}, []
    for row in rows:
        eid, form = row['evaluation_id'], row['form_key']
        by_id[eid] = row
        aa, bb = training[eid+'-n23'], training[eid+'-n27']
        for member in (aa, bb): close(member['theta'], row['theta'], 'pair_theta:'+eid, atol=0, rtol=0)
        valid = aa['valid'] and bb['valid']
        verify(valid == row['resolution_valid'], 'pair_valid:'+eid)
        if not valid:
            invalid_ids.append(eid)
            verify(row['joint_score'] == 1e30 and row['status'] == 'INVALID_RESOLUTION', 'invalid_penalty:'+eid)
            verify(all(row[key] is None for key in ('J_minus_1', 'max_mape_percent', 'max_percent_error', 'cross_grid_percent')), 'invalid_summary:'+eid)
            continue
        ma, mb = metrics(aa['pred'][:100], truth[:100]), metrics(bb['pred'][:100], truth[:100])
        g = float(100*np.max(np.abs(aa['pred'][:100]-bb['pred'][:100])/truth[:100]))
        j = max(ma['mape_percent']/MREF, mb['mape_percent']/MREF, ma['max_percent_error']/WREF, mb['max_percent_error']/WREF, g/2)
        mm, ww = max(ma['mape_percent'], mb['mape_percent']), max(ma['max_percent_error'], mb['max_percent_error'])
        for key, value in [('joint_score', j), ('J_minus_1', j-1), ('max_mape_percent', mm), ('max_percent_error', ww), ('cross_grid_percent', g)]:
            close(value, row[key], 'pair_summary:'+eid+':'+key, atol=0, rtol=0)
        ranked.setdefault(form, []).append((j, mm, ww, g, eid))
    verify(frozen['roles'] == result['roles'], 'frozen_roles')
    verify(set(ranked) == set(result['roles']), 'valid_role_coverage')
    for form, ranks in ranked.items():
        winner = min(ranks)[-1]
        verify(winner == result['roles'][form]['evaluation_id'], 'winner:'+form)
        for n in (23, 27):
            for key in ('pred', 'energy', 'sigma', 'theta', 'coefficients'):
                close(members[f'winner-{form}-n{n}'][key], training[f'{winner}-n{n}'][key], 'winner_array:'+form+':'+key, atol=0, rtol=0)
    primary = min((min(ranks), form) for form, ranks in ranked.items())[1] if ranked else None
    verify(primary == result['global_joint_winner'] == frozen['global_joint_winner'], 'primary')
    for name, member in members.items():
        close(member['theta'], result['roles'][member['form']]['theta'], 'fixed_theta:'+name, atol=0, rtol=0)
    fits, comparisons = read('development-fit-metrics.json'), read('comparisons.json')
    verify(set(fits) == set(members), 'fit_objects')
    for name, saved in fits.items():
        if not members[name]['valid']:
            verify(saved is None, 'invalid_fit:'+name)
            continue
        for window, (start, stop) in WINDOWS.items():
            metric_check(members[name]['pred'][start:stop], truth[start:stop], saved[window], 'fit:'+name+':'+window)
    verify(fits == result['fit_metrics'], 'result_fits')
    for name, saved in comparisons.items():
        left, right = members[saved['left']], members[saved['right']]
        same_d = len(left['sigma']) == len(right['sigma'])
        verify(same_d == saved['full_sigma_comparable_dimension'], 'comparison_dimension:'+name)
        if same_d:
            close(np.max(np.abs(left['sigma']-right['sigma'])), saved['full_sigma_max_absolute_difference'], 'comparison_fullsigma:'+name, atol=0, rtol=0)
        else: verify(saved['full_sigma_max_absolute_difference'] is None, 'different_dimension_sigma:'+name)
        close(np.max(np.abs(left['sigma'][:321]-right['sigma'][:321])), saved['first321_sigma_max_absolute_difference'], 'comparison_321sigma:'+name, atol=0, rtol=0)
        threshold = .1 if '-END-' in name else 2.
        verify(saved['G_threshold_percent'] == threshold, 'comparison_threshold:'+name)
        if not (left['valid'] and right['valid']):
            verify(saved['windows'] is None and saved['status'] == 'UNASSESSABLE_INVALID_RESOLUTION', 'invalid_comparison:'+name)
            continue
        for window, (start, stop) in WINDOWS.items():
            g = float(100*np.max(np.abs(left['pred'][start:stop]-right['pred'][start:stop])/truth[start:stop]))
            e = float(100*np.max(np.abs(left['energy'][start:stop]-right['energy'][start:stop])/left['energy'][start:stop]))
            close(g, saved['windows'][window]['G_percent'], 'comparison_G:'+name+':'+window, atol=0, rtol=0)
            close(e, saved['windows'][window]['raw_energy_max_relative_percent'], 'comparison_E:'+name+':'+window, atol=0, rtol=0)
            verify((g < threshold) == saved['windows'][window]['G_below_threshold'], 'comparison_gate:'+name+':'+window)
    verify(comparisons == result['comparisons'], 'result_comparisons')
    external = read('external-history-comparator.json')
    verify(not external['raw_energy_or_sigma_comparison_permitted'], 'external_owner_boundary')
    verify(sha(ROOT/external['source']) == external['source_sha256'], 'external_source_hash')
    with np.load(ROOT/external['source'], allow_pickle=False) as old:
        close(external['predicted_320'], old['predicted_320'], 'external_prediction', atol=0, rtol=0)
        for window, (start, stop) in WINDOWS.items():
            metric_check(old['predicted_320'][start:stop], truth[start:stop], external['fit_metrics'][window], 'external_fit:'+window)
    close(external['fit_metrics']['1-320']['mape_percent'], FULLREF, 'external_full_reference', atol=1e-10, rtol=0)
    verify(external['fit_metrics'] == result['external_history_fit_metrics'], 'external_result')
    assessments = read('finite-discovery-assessments.json')
    for form, row in assessments.items():
        training_better = True
        for n in (23, 27):
            mm, ww = fits[f'winner-{form}-n{n}']['1-100']['mape_percent'], fits[f'winner-{form}-n{n}']['1-100']['max_percent_error']
            close(mm, row['training_by_grid'][str(n)]['M'], 'assessment_training:'+form+':M')
            close(ww, row['training_by_grid'][str(n)]['W'], 'assessment_training:'+form+':W')
            training_better = training_better and mm < MREF and ww < WREF
        grid_checks = {key: all(item['G_below_threshold'] for item in comparisons[key]['windows'].values())
                       if comparisons[key]['windows'] is not None else None for key in (form+'-n31-n39', form+'-n39-n47')}
        full_better = bool(fits[f'post-{form}-n47'] is not None and fits[f'post-{form}-n47']['1-320']['mape_percent'] < FULLREF)
        j_better = result['roles'][form]['joint_score'] < 1
        necessary = bool(j_better and training_better and full_better and all(value is True for value in grid_checks.values()))
        verify(training_better == row['each_training_M_W_below_external_reference'], 'assessment_training_gate:'+form)
        verify(grid_checks == row['fine_grid_checks'], 'assessment_grid_gate:'+form)
        verify(full_better == row['n47_full320_M_below_external_reference'] and j_better == row['J_below_1'], 'assessment_score_gates:'+form)
        verify(necessary == row['necessary_finite_discovery_criteria_met'], 'assessment_necessary:'+form)
        verify(row['status'] == ('NECESSARY_FINITE_DISCOVERY_CRITERIA_MET_MAGNITUDE_REVIEW_REQUIRED' if necessary else 'NECESSARY_FINITE_DISCOVERY_CRITERIA_NOT_MET'), 'assessment_status:'+form)
    verify(assessments == result['finite_discovery_assessments'], 'result_assessments')
    cooling = read('cooling-versus-autonomous.json')
    if all(form in result['roles'] for form in ('A', 'D')):
        train_better = True
        for n in (23, 27):
            for key in ('mape_percent', 'max_percent_error'):
                difference = fits[f'winner-D-n{n}']['1-100'][key]-fits[f'winner-A-n{n}']['1-100'][key]
                close(difference, cooling['training_D_minus_A_percentage_points'][str(n)][key], 'cooling_training:'+str(n)+':'+key, atol=0, rtol=0)
                train_better = train_better and difference < 0
        final_valid = fits['post-D-n47'] is not None and fits['post-A-n47'] is not None
        difference = fits['post-D-n47']['1-320']['mape_percent']-fits['post-A-n47']['1-320']['mape_percent'] if final_valid else None
        if difference is None: verify(cooling['n47_full320_M_D_minus_A'] is None, 'cooling_invalid_final')
        else: close(difference, cooling['n47_full320_M_D_minus_A'], 'cooling_final', atol=0, rtol=0)
        end_checks = {str(n): all(row['G_below_threshold'] for row in comparisons[f'D-END-n{n}']['windows'].values())
                      if comparisons[f'D-END-n{n}']['windows'] is not None else None for n in (39, 47)}
        comparative = bool(primary == 'D' and train_better and difference is not None and difference < 0 and all(v is True for v in end_checks.values()))
        necessary = bool(comparative and assessments['D']['necessary_finite_discovery_criteria_met'])
        verify(train_better == cooling['all_training_M_W_better'], 'cooling_training_gate')
        verify(end_checks == cooling['END_four_window_G_below_point1_percent'], 'cooling_END_gates')
        verify(comparative == cooling['relative_D_A_conditions_met'] and necessary == cooling['all_necessary_cooling_advantage_criteria_met'], 'cooling_necessary')
        verify(cooling['status'] == ('NECESSARY_D_OVER_A_CRITERIA_MET_MAGNITUDE_REVIEW_REQUIRED' if necessary else 'NECESSARY_D_OVER_A_CRITERIA_NOT_MET'), 'cooling_status')
        for name, saved in cooling['actual_grid_END_metric_changes_percentage_points'].items():
            left, right = name.split('__')
            if saved is None:
                verify(fits[left] is None or fits[right] is None, 'cooling_invalid_metric_change:'+name)
                continue
            for window, row in saved.items():
                for key, value in row.items(): close(fits[right][window][key]-fits[left][window][key], value, 'cooling_metric_change:'+name+':'+window+':'+key, atol=0, rtol=0)
    else: verify(cooling['status'] == 'MISSING_D_OR_A_ROLE', 'missing_cooling_role')
    verify(cooling == result['cooling_versus_autonomous'], 'result_cooling')
    csv_count, objects = 0, Counter()
    with (RUN/'points.csv').open(newline='') as stream:
        for row in csv.DictReader(stream):
            name, index = row['object_id'], int(row['index'])-1
            aa, target = members[name], truth[index]
            pred, energy = aa['pred'][index], aa['energy'][index]
            for key, value in [('target', target), ('predicted', pred), ('nontrivial_energy', energy),
                               ('residual', pred-target), ('percent_error', 100*abs(pred-target)/target)]:
                close(float(row[key]), value, 'csv:'+key, atol=0, rtol=0)
            verify(row['form'] == aa['form'] and int(row['n']) == aa['n'] and int(row['dimension']) == aa['dimension'], 'csv_owner')
            close(float(row['epsilon']), aa['epsilon'], 'csv_epsilon', atol=0, rtol=0)
            verify(row['resolution_valid'] == str(aa['valid']), 'csv_valid')
            verify(row['window'] == ('1-100' if index < 100 else '101-300' if index < 300 else '301-320'), 'csv_window')
            csv_count += 1; objects[name] += 1
    verify(set(objects) == set(members) and all(count == 320 for count in objects.values()), 'csv_coverage')
    one, zero = controls['control-1-one-step'], controls['control-2-zero-source']
    expected = np.sort(np.abs(fft.fft(one['K_blocks'][0, :, 0, :], axis=1)).ravel())[::-1]
    close(expected, one['expected_sigma'], 'control_one_expected', atol=0, rtol=0)
    verify(np.max(np.abs(one['sigma']-expected)) <= 1e-10, 'control_one_sigma')
    verify(np.count_nonzero(np.abs(one['sigma']-1) <= 1e-10) == 7, 'control_one_seven_unit_modes')
    block = zero['K_blocks'][0, 0]
    squared = block@block
    expected_matrix = np.kron(squared, squared)
    factors = np.abs(fft.fft(block[0]))**2
    expected_sigma = np.sort((factors[:, None]*factors[None, :]).ravel())[::-1]
    close(expected_matrix, zero['expected_matrix'], 'control_zero_expected_matrix', atol=0, rtol=0)
    close(expected_sigma, zero['expected_sigma'], 'control_zero_expected_sigma', atol=0, rtol=0)
    verify(norm(zero['C']-expected_matrix) <= 1e-10*max(1, norm(zero['C'])), 'control_zero_matrix')
    verify(np.max(np.abs(zero['sigma']-expected_sigma)) <= 1e-10, 'control_zero_sigma')
    for left, right, reverse in [('control-4-D-reverse', 'control-3-D-default', True), ('control-6-D-end', 'control-5-A-end', False)]:
        aa, bb = controls[left], controls[right]
        swap = np.arange(49).reshape(7, 7).T.ravel()
        expected = bb['C'].T[np.ix_(swap, swap)] if reverse else bb['C']
        close(aa['expected_matrix'], expected, 'control_expected:'+left, atol=0, rtol=0)
        verify(norm(aa['C']-expected) <= 1e-10*max(1, norm(bb['C'])), 'control_matrix:'+left)
        verify(np.max(np.abs(aa['sigma']-bb['sigma'])) <= 1e-10, 'control_sigma:'+left)
    for path, wanted in manifest['inputs'].items(): verify(sha(ROOT/path) == wanted, 'input_hash:'+path)
    verify(sha(PACKAGE/'run_search.py') == manifest['script_sha256'] == RUNNER_SHA, 'runner_hash')
    verify(sha(PACKAGE/'input-locks.json') == manifest['input_locks_sha256'], 'locks_hash')
    freeze = read('training-arrays-frozen.json')
    for path, wanted in freeze['files_sha256'].items(): verify(sha(RUN/path) == wanted, 'frozen_hash:'+path)
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
    call_lines = [json.loads(line) for line in (RUN/'calls.jsonl').read_text().splitlines()]
    verify(calls == call_lines and len(calls) == result['calls'] <= 56 and len(rows) == result['unique_members'], 'call_counts')
    verify(sum(bool(row['cached']) for row in calls) == result['cached_calls'], 'cache_count')
    for call in calls:
        source = by_id[call['evaluation_id']]
        for key in ('theta', 'form_key', 'joint_score', 'resolution_valid'): verify(call[key] == source[key], 'call_identity:'+key)
    counter = result['counters']
    verify(counter['forwards_attempted'] == counter['forwards_completed'] == names.count('forward_start') == names.count('forward_complete') <= 128, 'forward_counts')
    verify(counter['full_svd_attempted'] == counter['full_svd_completed'] == names.count('full_svd_complete') == counter['forwards_completed'], 'SVD_counts')
    for stage, limit in [('control', 6), ('training', 112), ('postfreeze', 6), ('ablation', 4)]:
        number = sum(row['event'] == 'forward_start' and row['stage'] == stage for row in events)
        verify(counter[stage+'_forwards_attempted'] == counter[stage+'_forwards_completed'] == number <= limit, 'stage_counts:'+stage)
    verify(counter['training_forwards_completed'] == 2*len(rows), 'paired_training_count')
    verify(counter['eigh_calls'] == counter['root_calls'] == counter['extra_state_svd_calls'] == counter['new_target_generations'] == 0, 'zero_extra_science')
    verify(counts['kernel_npz'] == counter['forwards_completed']+2*len(result['roles']), 'array_count')
    verify(counts['full_C'] == 6+counter['full_arrays_saved'] and counts['controls'] == counter['control_arrays_saved'] == 6, 'full_control_counts')
    verify(len(training) == 2*len(rows) and len(aliases) == counter['ablation_aliases_saved'], 'training_alias_counts')
    verify(len(invalid_ids) == result['invalid_unique_members'], 'invalid_pair_count')
    verify(all(value < 5e-9 for key, value in residual_max.items() if key != 'nontrivial_constant_projection'), 'residual_engineering_ceiling')
    summary = dict(status='ANALYZED' if not failures else 'ISSUES_FOUND', failures=failures, checks=dict(checks),
        maximum_recomputation_differences=maxima, array_counts=dict(counts), training_pairs=len(rows),
        calls=len(calls), cached_calls=result['cached_calls'], invalid_training_pairs=invalid_ids,
        fitted_objects=len(members), csv_rows=csv_count, fit_windows=sum(row is not None for row in fits.values())*4,
        comparison_windows=sum(row['windows'] is not None for row in comparisons.values())*4,
        aliases=len(aliases), input_hashes=len(manifest['inputs']), training_frozen_files=len(freeze['files_sha256']),
        inventory_files=len(inventory), residual_maxima=residual_max, counters=counter,
        winners={key:{field:value[field] for field in ('evaluation_id', 'theta', 'joint_score', 'max_mape_percent', 'max_percent_error')}
                 for key, value in result['roles'].items()}, assessments=assessments, cooling_assessment=cooling,
        checker_sha256=sha(Path(__file__)), scope='Saved evidence only; no four-step recomposition, forward, decomposition, root search, optimization or new target.',
        nonwinner_constant_gate_limit='Top-state directions/signs checked from saved diagnostics only; actual vectors absent. Full objects independently checked from saved vectors.')
    print(json.dumps(summary, ensure_ascii=False, indent=2, allow_nan=False))
    if failures: raise SystemExit(1)


if __name__ == '__main__':
    main()
