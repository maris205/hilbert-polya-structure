#!/usr/bin/env python3
"""CS11 read-only saved-data audit; no scientific runner import or new solve.

Only saved-array algebra/DST, scalar metrics, records and hashes are evaluated.
No propagation, eigendecomposition, SVD, root search, optimization or new target.
Prints a JSON summary, writes nothing. Run only after the parent confirms exit0.
"""
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

import numpy as np
from scipy.fft import dst

PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[1]
RUN = PACKAGE / 'evidence/run-1'
OLD = ROOT / 'papers/259-hyperbolic-tail-heat-search/evidence/run-1'
WINDOWS = {'1-100': (0, 100), '101-300': (100, 300),
           '301-320': (300, 320), '1-320': (0, 320)}
MREF, WREF = 1.695273790061038, 5.234299091683695
RUNNER_SHA = '0906eb57fad26b523b544ca0763c9246dc79ab5a0f01ff42569d64a33bbd5c7f'
checks, maxima, failures = Counter(), {}, []


def read(name):
    return json.loads((RUN / name).read_text())


def verify(ok, label):
    checks[label.split(':')[0]] += 1
    if not bool(ok):
        failures.append(label)


def close(actual, expected, label, atol=5e-11, rtol=2e-12):
    a, b = np.asarray(actual), np.asarray(expected)
    verify(a.shape == b.shape, label + ':shape')
    if a.shape != b.shape:
        return
    verify(np.allclose(a, b, atol=atol, rtol=rtol, equal_nan=True), label)
    if a.size and np.issubdtype(a.dtype, np.number) and np.issubdtype(b.dtype, np.number):
        mask = np.isfinite(a) & np.isfinite(b)
        error = float(np.max(np.abs(a[mask]-b[mask]))) if np.any(mask) else 0.
        key = label.split(':')[0]
        maxima[key] = max(maxima.get(key, 0.), error)


def norm(value):
    return float(np.sqrt(np.sum(np.abs(value)**2)))


def transform(value):
    return dst(value, type=1, axis=0, norm='ortho', workers=1)


def metrics(prediction, target):
    error = prediction-target
    ratio = np.abs(error)/target
    return dict(count=len(target), mape_percent=float(100*np.mean(ratio)),
                max_percent_error=float(100*np.max(ratio)), mse=float(np.mean(error**2)),
                max_absolute_error=float(np.max(np.abs(error))),
                mean_absolute_spacing_error_in_target_gaps=float(
                    np.mean(np.abs(np.diff(prediction)-np.diff(target))/np.diff(target))))


def metric_check(pred, target, recorded, label):
    for key, value in metrics(pred, target).items():
        close(value, recorded[key], label+':'+key)


def sha(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024*1024), b''):
            digest.update(block)
    return digest.hexdigest()


def occupation(states, q, length, arrays, prefix, label):
    boundary = np.sum(np.abs(states[np.abs(q) > .9*length])**2, axis=0)
    count = (len(q)+4)//5
    tail = np.sum(np.abs(transform(states)[-count:])**2, axis=0)
    close(boundary, arrays[prefix+'boundary_mass'], 'occupation:'+label+':boundary', atol=2e-12)
    close(tail, arrays[prefix+'high_momentum_mass'], 'occupation:'+label+':tail', atol=2e-12)


def compact(arrays):
    return dict(pred=arrays['predicted_320'].copy(), energy=arrays['energy'][:320].copy(),
                scale=float(arrays['scale']), theta=arrays['theta'].copy(),
                valid=bool(arrays['resolution_valid']) if 'resolution_valid' in arrays else True,
                meta=dict(form=str(arrays['form_key']), N=int(arrays['grid_n']),
                          L=float(arrays['L']), B=int(arrays['sample_count']), profile=str(arrays['profile'])))


def main():
    result, manifest = read('result.json'), read('manifest.json')
    verify(result['status'] in ('completed', 'completed_with_missing_roles'), 'completed_record')
    truth = np.asarray(read('known-targets.json')['ordinates'])
    verify(len(truth) == 320 and np.all(np.diff(truth) > 0), 'truth_shape_order')
    minima = read('minimum-ledger.json')
    members, training, counts = {}, {}, Counter()
    residual_max = dict(forward=0., adjoint=0., heat_orthogonality=0., heat_fro_relative=0.,
                        kinetic_owner=0., kinetic_equation=0., kinetic_orthogonality=0.,
                        kinetic_symmetry=0., kinetic_P=0., static_owner=0., static_equation=0.,
                        static_orthogonality=0., static_symmetry=0.)
    files = sorted((RUN/'evaluations').glob('*-N*.npz'))+sorted(RUN.glob('*.npz'))
    for path in files:
        name = path.stem
        record = json.loads(path.with_suffix('.json').read_text())
        with np.load(path, allow_pickle=False) as a:
            n, length, samples = int(a['grid_n']), float(a['L']), int(a['sample_count'])
            theta = a['theta']; h, ast, mass, z = theta[:4]
            form, profile = str(a['form_key']), str(a['profile'])
            kappa = theta[4] if form == 'M' else 0.
            verify(len(theta) == (5 if form == 'M' else 4), 'theta_dimension:'+name)
            close(theta, record['theta'], 'theta_record:'+name, atol=0, rtol=0)
            verify(record['N'] == n and record['L'] == length and record['B'] == samples, 'grid_record:'+name)
            q, p, kinetic = a['q'], a['p'], a['kinetic_minus_mass']
            close(q, -length+2*length*np.arange(1, n+1)/(n+1), 'q:'+name)
            close(p, np.pi*h*np.arange(1, n+1)/(2*length), 'p:'+name)
            close(kinetic, p*p/(np.hypot(mass, p)+mass), 'kinetic:'+name)
            close(a['target_100'], truth[:100], 'target:'+name, atol=0, rtol=0)
            u = (np.arange(samples)+.5)/samples
            w = (np.log(11+299*u)**-2-np.log(310.)**-2)/(np.log(11.)**-2-np.log(310.)**-2)
            close(a['schedule'], 1.02+(ast-1.02)*w, 'schedule:'+name, atol=2e-14)
            natural = (2*1.02*q)**2/(1+(2*1.02*q)**2)
            expected_g = np.ones(n) if profile == 'constant_one' else natural
            close(a['g'], expected_g, 'profile:'+name, atol=0, rtol=0)
            close(a['R_diagonal'], np.sqrt(1+kappa*expected_g), 'R:'+name, atol=0, rtol=0)
            verify(np.all(a['R_diagonal'] > 0), 'R_positive:'+name)
            if 'K' in a or 'H_avg' in a:
                basis = transform(np.eye(n))
                k0 = transform(kinetic[:, None]*basis)
                expected_k = a['R_diagonal'][:, None]*k0*a['R_diagonal'][None, :]
            if 'K' in a:
                counts['full_K'] += 1
                matrix, vectors, values = a['K'], a['kinetic_Q'], a['kinetic_nu']
                verify(matrix.shape == vectors.shape == (n, n), 'kinetic_shapes:'+name)
                verify(np.all(np.isfinite(values)) and np.all(values > 0) and np.all(np.diff(values) >= 0), 'nu_positive_order:'+name)
                owner_error = norm(matrix-expected_k)/norm(matrix)
                verify(owner_error < 2e-13, 'kinetic_owner:'+name)
                eq = np.sqrt(np.sum((matrix@vectors-vectors*values)**2, axis=0))
                orth, sym = norm(vectors.T@vectors-np.eye(n)), norm(matrix-matrix.T)/norm(matrix)
                rhs = float(np.sum(np.diag(k0)*a['R_diagonal']**2))
                close(np.trace(matrix), rhs, 'trace_identity:'+name)
                close(np.sum(values), np.trace(matrix), 'trace_eigenvalues:'+name)
                expected_p = (vectors*np.exp(-float(a['delta'])*values))@vectors.T
                p_error = norm(a['P_delta']-expected_p)/norm(expected_p)
                verify(p_error < 2e-13, 'saved_P:'+name)
                if form == 'M':
                    close(eq, a['kinetic_eigen_equation_residual'], 'kinetic_saved_residual:'+name, atol=2e-11)
                    close(rhs, a['kinetic_trace_identity_rhs'], 'kinetic_saved_trace:'+name)
                    for key, value in [('kinetic_equation_residual_max', np.max(eq)), ('kinetic_orthogonality_fro', orth),
                                       ('kinetic_symmetry_relative_fro', sym), ('kinetic_trace', np.trace(matrix)),
                                       ('kinetic_trace_identity_rhs', rhs)]:
                        close(value, record[key], 'kinetic_record:'+name+':'+key)
                else:
                    close(vectors, basis, 'B_basis:'+name, atol=0, rtol=0)
                    close(values, kinetic, 'B_nu:'+name, atol=0, rtol=0)
                for key, val in [('kinetic_owner', owner_error), ('kinetic_equation', np.max(eq)),
                                 ('kinetic_orthogonality', orth), ('kinetic_symmetry', sym), ('kinetic_P', p_error)]:
                    residual_max[key] = max(residual_max[key], float(val))
            if 'sigma' in a:
                counts['heat_npz'] += 1
                nu = a['kinetic_nu']
                verify(nu.shape == (n,) and np.all(np.isfinite(nu)) and np.all(nu > 0)
                       and np.all(np.diff(nu) >= 0), 'all_saved_nu_positive_order:'+name)
                if form == 'M':
                    close(nu[[0, -1]], [record['kinetic_min_eigenvalue'], record['kinetic_max_eigenvalue']],
                          'all_saved_nu_record:'+name, atol=0, rtol=0)
                else:
                    close(nu, kinetic, 'all_B_nu:'+name, atol=0, rtol=0)
                sigma, energy, beta = a['sigma'], a['energy'], float(a['beta'])
                verify(beta == .02, 'beta:'+name)
                mask = np.isfinite(sigma) & (sigma > 0)
                expected_e = np.full(n, np.nan)
                expected_e[mask] = mass-np.log(sigma[mask])/beta
                mask &= np.isfinite(expected_e)
                close(energy, expected_e, 'energy:'+name, atol=0, rtol=0)
                verify(np.array_equal(mask, a['energy_resolved_mask']), 'mask:'+name)
                required = min(n, 320)
                valid = (0 < sigma[0] <= 1+1e-10 and np.all(mask[:required])
                         and np.all(np.diff(sigma[:required]) <= 0)
                         and (n < 320 or sigma[required-1]/sigma[0] >= 1e-10)
                         and energy[0] > 0 and np.all(energy[:required] >= mass-1e-8))
                verify(valid == bool(a['resolution_valid']) == record['resolution_valid'], 'valid:'+name)
                counts['invalid_heat_npz'] += int(not valid)
                prediction = a['predicted_320' if n >= 320 else 'predicted_control']
                expected_scale = truth[0]/energy[0] if np.isfinite(energy[0]) and energy[0] > 0 else np.nan
                expected_prediction = expected_scale*energy[:required] if np.isfinite(expected_scale) else np.full(required, np.nan)
                close(a['scale'], expected_scale, 'scale:'+name, atol=0, rtol=0)
                close(prediction, expected_prediction, 'prediction:'+name, atol=0, rtol=0)
                if record.get('training_metrics') is not None:
                    metric_check(prediction[:100], truth[:100], record['training_metrics'], 'train_metrics:'+name)
                order = np.arange(samples)
                if str(a['order_name']) == 'reverse': order = order[::-1]
                verify(np.array_equal(order, a['sample_order_zero_based']), 'order:'+name)
                verify(np.array_equal(order+1, a['sample_order_one_based']), 'order1:'+name)
                close(a['delta'], beta/samples, 'delta:'+name, atol=0, rtol=0)
                close(a['midpoint_u'], u, 'midpoints:'+name, atol=0, rtol=0)
                close(a['g_henon_reference'], natural, 'natural_profile:'+name, atol=0, rtol=0)
                if str(a['potential_mode']) != 'zero_control':
                    ids = a['minimum_ids']
                    verify(np.all((ids >= 0) & (ids < len(minima))), 'minimum_ids:'+name)
                    values = np.asarray([minima[int(i)]['minimum'] for i in ids])
                    close(a['minimum_values'], values, 'minimum_values:'+name, atol=0, rtol=0)
                    close(a['minimizers'], [minima[int(i)]['minimizer'] for i in ids], 'minimizers:'+name, atol=0, rtol=0)
                    close(a['schedule'], [minima[int(i)]['a'] for i in ids], 'minimum_schedule:'+name, atol=0, rtol=0)
                    close(np.full(samples, z), [minima[int(i)]['z'] for i in ids], 'minimum_z:'+name, atol=0, rtol=0)
                    shifted = (-q+q*q+.05*q**4+z*q**5+.002*q**6)[None, :]+a['schedule'][:, None]*q[None, :]**3/3-values[:, None]
                    verify(float(np.min(shifted)) >= -1e-10, 'W_nonnegative:'+name)
                    close(a['W_samples'], np.maximum(shifted, 0), 'W:'+name, atol=3e-10)
                else:
                    verify(not np.any(a['W_samples']), 'free_W:'+name)
                close(a['mean_W'], np.mean(a['W_samples'], axis=0), 'mean_W:'+name, atol=0, rtol=0)
                if 'C_tilde' in a:
                    counts['full_heat'] += 1
                    c, left, right = a['C_tilde'], a['singular_left'], a['singular_right']
                    verify(c.shape == (n, n) and left.shape == right.shape == (n, required), 'heat_shapes:'+name)
                    verify(not np.iscomplexobj(c) and not np.iscomplexobj(left), 'real_heat:'+name)
                    forward = np.sqrt(np.sum((c@right-left*sigma[:required])**2, axis=0))
                    adjoint = np.sqrt(np.sum((c.T@left-right*sigma[:required])**2, axis=0))
                    for key, values in [('forward', forward), ('adjoint', adjoint)]:
                        close(values, a['singular_'+key+'_residual'], 'singular_saved:'+name+':'+key, atol=2e-13)
                        close(values/sigma[0], a['singular_'+key+'_residual_over_sigma0'], 'singular_relative:'+name+':'+key, atol=2e-13)
                        residual_max[key] = max(residual_max[key], float(np.max(values)))
                    lo, ro = norm(left.T@left-np.eye(required)), norm(right.T@right-np.eye(required))
                    fro, moment = np.sum(c*c), np.sum(sigma*sigma)
                    for key, val in [('matrix_frobenius_squared', fro), ('full_sigma_squared_sum', moment),
                                     ('left_orthogonality_fro', lo), ('right_orthogonality_fro', ro)]:
                        close(val, record[key], 'heat_record:'+name+':'+key)
                    residual_max['heat_orthogonality'] = max(residual_max['heat_orthogonality'], lo, ro)
                    residual_max['heat_fro_relative'] = max(residual_max['heat_fro_relative'], float(abs(fro-moment)/fro))
                    occupation(left, q, length, a, 'left_', name+':left')
                    occupation(right, q, length, a, 'right_', name+':right')
                if n >= 320:
                    (training if path.parent.name == 'evaluations' else members)[name] = compact(a)
            else:
                counts['static'] += 1
                matrix, energy, states = a['H_avg'], a['energy'], a['states']
                expected_h = expected_k.copy()
                expected_h.flat[::n+1] += mass+a['mean_W']
                owner = norm(matrix-expected_h)/norm(matrix)
                verify(owner < 2e-13, 'static_owner:'+name)
                residual = np.sqrt(np.sum((matrix@states-states*energy[:320])**2, axis=0))
                close(residual, a['equation_residual'], 'static_saved_residual:'+name, atol=2e-11)
                orth, sym = norm(states.T@states-np.eye(320)), norm(matrix-matrix.T)/norm(matrix)
                for key, val in [('equation_residual_max', np.max(residual)), ('orthogonality_fro', orth), ('symmetry_relative_fro', sym)]:
                    close(val, record[key], 'static_record:'+name+':'+key)
                verify(np.all(np.diff(energy) >= 0) and energy[0] > 0, 'static_positive_order:'+name)
                close(a['scale'], truth[0]/energy[0], 'static_scale:'+name, atol=0, rtol=0)
                close(a['predicted_320'], float(a['scale'])*energy[:320], 'static_prediction:'+name, atol=0, rtol=0)
                metric_check(a['predicted_320'][:100], truth[:100], record['training_metrics'], 'static_train:'+name)
                occupation(states, q, length, a, '', name)
                for key, val in [('static_owner', owner), ('static_equation', np.max(residual)), ('static_orthogonality', orth), ('static_symmetry', sym)]:
                    residual_max[key] = max(residual_max[key], float(val))
                with np.load(RUN/str(a['kinetic_owner_source']), allow_pickle=False) as heat:
                    for key in ('theta', 'q', 'p', 'kinetic_minus_mass', 'g', 'R_diagonal', 'mean_W', 'schedule', 'minimum_ids'):
                        verify(np.array_equal(a[key], heat[key]), 'static_identity:'+name+':'+key)
                members[name] = compact(a)
    print('ARRAY_AUDIT_COMPLETE', dict(counts), flush=True)
    finish(result, manifest, truth, minima, members, training, counts, residual_max)


def finish(result, manifest, truth, minima, members, training, counts, residual_max):
    target_path = ROOT/'papers/253-structural-homotopy-search/evidence/run-1/evaluations/CS03-Q-QUARTIC-0103.npz'
    with np.load(target_path, allow_pickle=False) as original:
        portions = [original['target_100'].copy()]
    for folder, filename, count in [
        ('251-constructive-fit-portfolio', 'reference-101-150.json', 50),
        ('253-structural-homotopy-search', 'reference-151-200.json', 50),
        ('254-global-forms-joint-fit', 'reference-201-240.json', 40),
        ('255-path-operator-multigrid', 'reference-241-300.json', 60),
        ('256-chronological-heat-spectrum', 'reference-301-320.json', 20)]:
        values = np.asarray([float(value) for value in json.loads((ROOT/'papers'/folder/'evidence/run-1'/filename).read_text())['ordinates']])
        verify(len(values) == count, 'original_target_portion:'+filename)
        portions.append(values)
    verify(np.array_equal(np.concatenate(portions), truth), 'original_target320_identity')
    with np.load(OLD/'post-B-N1279.npz', allow_pickle=False) as a:
        members['old-B0055-N1279'] = dict(pred=a['predicted_320'].copy(), energy=a['energy'][:320].copy(),
            theta=a['theta'].copy(), scale=float(a['scale']), valid=bool(a['resolution_valid']),
            meta=dict(form='B0055', N=1279, L=8., B=64, profile='old-flat'))
    aliases = read('ablation-aliases.json')
    for name, row in aliases.items():
        verify(row['status'] == 'ALIASED_EXACT_KAPPA_ZERO' and row['requested_theta'][4] == 0., 'alias_zero:'+name)
        verify(not row['additional_propagation'] and not row['additional_eigh'] and row['budget_not_transferred'], 'alias_no_science:'+name)
        verify(not (RUN/(name+'.npz')).exists(), 'alias_no_duplicate_npz:'+name)
        for field, key in [('source_npz', 'source_sha256'), ('static_source_npz', 'static_source_sha256')]:
            verify(sha(RUN/row[field]) == row[key], 'alias_hash:'+name+':'+field)
        for target, source in [(name, row['source_object']), ('static-'+name, row['static_source_object'])]:
            members[target] = {**members[source], 'meta': {**members[source]['meta'], 'profile': row['requested_profile']}}
    rows, calls, frozen = read('unique-members.json'), read('calls.json'), read('winners-frozen.json')
    ranks, by_id = {}, {}
    for row in rows:
        eid, form = row['evaluation_id'], row['form_key']
        by_id[eid] = row
        aa, bb = training[eid+'-N511'], training[eid+'-N639']
        close(aa['theta'], row['theta'], 'pair_theta:'+eid, atol=0, rtol=0)
        close(bb['theta'], row['theta'], 'pair_theta_other:'+eid, atol=0, rtol=0)
        valid = aa['valid'] and bb['valid']
        verify(valid == row['resolution_valid'], 'pair_valid:'+eid)
        if not valid:
            verify(row['joint_score'] == 1e30 and row['status'] == 'INVALID_RESOLUTION', 'invalid_penalty:'+eid)
            continue
        ma, mb = metrics(aa['pred'][:100], truth[:100]), metrics(bb['pred'][:100], truth[:100])
        g = float(100*np.max(np.abs(aa['pred'][:100]-bb['pred'][:100])/truth[:100]))
        j = max(ma['mape_percent']/MREF, mb['mape_percent']/MREF,
                ma['max_percent_error']/WREF, mb['max_percent_error']/WREF, g/2)
        for field, val in [('joint_score', j), ('J_minus_1', j-1), ('cross_grid_percent', g),
                           ('max_mape_percent', max(ma['mape_percent'], mb['mape_percent'])),
                           ('max_percent_error', max(ma['max_percent_error'], mb['max_percent_error']))]:
            close(val, row[field], 'pair:'+eid+':'+field)
        ranks.setdefault(form, []).append((j, max(ma['mape_percent'], mb['mape_percent']),
                                           max(ma['max_percent_error'], mb['max_percent_error']), g, eid))
    verify(frozen['roles'] == result['roles'], 'frozen_roles')
    for form, ranked in ranks.items():
        winner = min(ranked)[-1]
        verify(winner == result['roles'][form]['evaluation_id'], 'winner:'+form)
        for n in (511, 639):
            for key in ('pred', 'energy', 'theta'):
                close(members[f'winner-{form}-N{n}'][key], training[f'{winner}-N{n}'][key], 'winner_arrays:'+form+':'+key, atol=0, rtol=0)
    primary = min((min(rr), form) for form, rr in ranks.items())[1] if ranks else None
    verify(primary == result['global_joint_winner'] == frozen['global_joint_winner'], 'global_winner')
    nonzero = [row for row in rows if row['form_key'] == 'M' and row['theta'][4] != 0. and row['resolution_valid']]
    best_nonzero = min(nonzero, key=lambda row: (row['joint_score'], row['max_mape_percent'], row['max_percent_error'], row['cross_grid_percent'], row['evaluation_id'])) if nonzero else None
    for name, member in members.items():
        if name == 'old-B0055-N1279': continue
        form = member['meta']['form']
        expected_theta = np.asarray(result['roles'][form]['theta']).copy()
        if 'ablation-M-Z-' in name: expected_theta[4] = 0.
        close(member['theta'], expected_theta, 'fixed_post_theta:'+name, atol=0, rtol=0)
    for n in (511, 639):
        with np.load(OLD/'evaluations'/f'CS09-B-QUINTIC-REFIT-0055-N{n}.npz', allow_pickle=False) as old:
            new = training[f'CS11-B-QUINTIC-REFIT-0001-N{n}']
            close(new['pred'], old['predicted_320'], 'old_regression_prediction:'+str(n), atol=1e-6, rtol=0)
            before, after = metrics(old['predicted_320'][:100], truth[:100]), metrics(new['pred'][:100], truth[:100])
            for key in ('mape_percent', 'max_percent_error'):
                close(before[key], after[key], 'old_regression_metric:'+str(n)+':'+key, atol=1e-6, rtol=0)
    fits, comparisons = read('development-fit-metrics.json'), read('comparisons.json')
    verify(set(fits) == set(members), 'fit_object_coverage')
    for name, saved in fits.items():
        if not members[name]['valid']:
            verify(saved is None, 'invalid_fit_retained:'+name)
            continue
        for window, (start, stop) in WINDOWS.items():
            metric_check(members[name]['pred'][start:stop], truth[start:stop], saved[window], 'fit:'+name+':'+window)
    verify(fits == result['fit_metrics'], 'result_fits')
    for name, saved in comparisons.items():
        aa, bb = members[saved['left']], members[saved['right']]
        if not (aa['valid'] and bb['valid']):
            verify(saved['windows'] is None, 'invalid_comparison_retained:'+name)
            continue
        for window, (start, stop) in WINDOWS.items():
            g = float(100*np.max(np.abs(aa['pred'][start:stop]-bb['pred'][start:stop])/truth[start:stop]))
            e = float(100*np.max(np.abs(aa['energy'][start:stop]-bb['energy'][start:stop])/aa['energy'][start:stop]))
            close(g, saved['windows'][window]['G_percent'], 'comparison_G:'+name+':'+window)
            close(e, saved['windows'][window]['raw_energy_max_relative_percent'], 'comparison_E:'+name+':'+window)
            verify((g < 2) == saved['windows'][window]['G_below_2_percent'], 'comparison_gate:'+name+':'+window)
    verify(comparisons == result['comparisons'], 'result_comparisons')
    structure = read('structure-assessment.json')
    verify(structure == result['structure_assessment'], 'result_structure')
    if 'M' in result['roles']:
        kappa = result['roles']['M']['theta'][4]
        below = 'B' in result['roles']
        if below:
            for n in (511, 639):
                for key, ref in [('mape_percent', MREF), ('max_percent_error', WREF)]:
                    mv, bv = fits[f'winner-M-N{n}']['1-100'][key], fits[f'winner-B-N{n}']['1-100'][key]
                    row = structure['training_components'][str(n)][key]
                    for field, val in [('M_value', mv), ('B_value', bv), ('M_minus_B', mv-bv)]:
                        close(val, row[field], 'structure_component:'+str(n)+':'+key+':'+field)
                    below = below and mv < bv and mv < ref
        dev_better = bool('B' in result['roles'] and fits['post-M-N1279'] and fits['post-B-N1279']
                          and fits['post-M-N1279']['1-320']['mape_percent'] < fits['post-B-N1279']['1-320']['mape_percent'])
        gates = ['M-N1023-N1279']+(['primary-time-N1279-B128', 'primary-box-N1599-L10'] if primary == 'M' else [])
        engineering = {key: all(row['G_below_2_percent'] for row in comparisons[key]['windows'].values())
                       if comparisons[key]['windows'] is not None else None for key in gates}
        necessary = bool(kappa != 0 and primary == 'M' and below and dev_better and all(v is True for v in engineering.values()))
        verify(below == structure['both_training_M_W_below_refitted_B_and_old_reference'], 'structure_training')
        verify(dev_better == structure['N1279_full320_M_below_refitted_B'], 'structure_development')
        verify(engineering == structure['engineering_all_windows'], 'structure_engineering')
        verify(necessary == structure['necessary_finite_criteria_met'], 'structure_necessary')
        verify(structure['status'] == ('NECESSARY_FINITE_CRITERIA_MET_MAGNITUDE_REVIEW_REQUIRED' if necessary else 'NECESSARY_FINITE_CRITERIA_NOT_MET'), 'structure_status')
        for name, windows in structure['actual_discretization_metric_changes_percentage_points'].items():
            if windows is None: continue
            for window, row in windows.items():
                for key, val in row.items():
                    close(fits[name][window][key]-fits['post-M-N1279'][window][key], val, 'discretization_change:'+name+':'+window+':'+key)
        verify(structure['micro_gain_not_certified_by_2_percent_line'] and structure['robust_structure_label_not_automatically_awarded'], 'magnitude_caveat')
    csv_count, object_counts = 0, Counter()
    with (RUN/'points.csv').open(newline='') as stream:
        for row in csv.DictReader(stream):
            name, index = row['object_id'], int(row['index'])-1
            aa = members[name]; pred, energy, target = aa['pred'][index], aa['energy'][index], truth[index]
            for key, value in [('target', target), ('predicted', pred), ('energy', energy),
                               ('residual', pred-target), ('percent_error', 100*abs(pred-target)/target)]:
                close(float(row[key]), value, 'csv:'+key, atol=0, rtol=0)
            for key in ('form', 'profile'):
                verify(row[key] == aa['meta'][key], 'csv_meta:'+key)
            for key in ('N', 'L', 'B'):
                close(float(row[key]), aa['meta'][key], 'csv_meta:'+key, atol=0, rtol=0)
            verify(row['resolution_valid'] == str(aa['valid']), 'csv_valid')
            verify(row['window'] == ('1-100' if index < 100 else '101-300' if index < 300 else '301-320'), 'csv_window')
            csv_count += 1; object_counts[name] += 1
    verify(set(object_counts) == set(members) and all(c == 320 for c in object_counts.values()), 'csv_coverage')
    controls = {}
    names = ('control-1-free-B', 'control-2-base', 'control-3-M-zero', 'control-4-M-one', 'control-5-M-reverse', 'control-6-free-M')
    for name in names:
        with np.load(RUN/(name+'.npz'), allow_pickle=False) as a:
            controls[name] = {k:a[k] for k in ('C_tilde', 'sigma', 'energy', 'kinetic_nu', 'theta', 'beta')}
    for name in (names[0], names[-1]):
        aa = controls[name]
        verify(np.max(np.abs(aa['sigma']-np.sort(np.exp(-.02*aa['kinetic_nu']))[::-1])) <= 1e-10, 'free_sigma:'+name)
        verify(np.max(np.abs(aa['energy']-np.sort(aa['theta'][2]+aa['kinetic_nu']))) <= 1e-8, 'free_energy:'+name)
    for left, right, transpose in [(names[2], names[1], False), (names[4], names[3], True)]:
        aa, bb = controls[left], controls[right]
        expected = bb['C_tilde'].T if transpose else bb['C_tilde']
        verify(norm(aa['C_tilde']-expected) <= 1e-10*max(1, norm(bb['C_tilde'])), 'null_control_matrix:'+left)
        verify(np.max(np.abs(aa['sigma']-bb['sigma'])) <= 1e-10, 'null_control_sigma:'+left)
    for row in minima:
        a, z, q = row['a'], row['z'], np.asarray(row['stationary_roots'])
        values = -q+q*q+a*q**3/3+.05*q**4+z*q**5+.002*q**6
        derivative = -1+2*q+a*q*q+.2*q**3+5*z*q**4+.012*q**5
        verify(np.max(np.abs(derivative)) <= 1e-9, 'saved_root_residual')
        close(values, row['stationary_values'], 'saved_root_values', atol=2e-11)
        close(np.min(values), row['minimum'], 'saved_root_minimum', atol=2e-11)
    for path, expected in manifest['inputs'].items(): verify(sha(ROOT/path) == expected, 'input_hash:'+path)
    verify(sha(PACKAGE/'run_search.py') == manifest['script_sha256'] == RUNNER_SHA, 'runner_hash')
    verify(sha(PACKAGE/'input-locks.json') == manifest['input_locks_sha256'], 'locks_hash')
    freeze = read('training-arrays-frozen.json')
    for path, expected in freeze['files_sha256'].items(): verify(sha(RUN/path) == expected, 'frozen_hash:'+path)
    verify(sha(RUN/'winners-frozen.json') == freeze['winner_identity_sha256'] == result['winner_identity_sha256'], 'winner_identity_hash')
    inventory = read('file-inventory.json')['files']
    for name, item in inventory.items():
        verify((RUN/name).stat().st_size == item['bytes'], 'inventory_size:'+name)
        verify(sha(RUN/name) == item['sha256'], 'inventory_hash:'+name)
    verify(set(inventory) == {str(p.relative_to(RUN)) for p in RUN.rglob('*') if p.is_file() and p.name != 'file-inventory.json'}, 'inventory_coverage')
    events = [json.loads(line) for line in (RUN/'events.jsonl').read_text().splitlines()]
    names = [e['event'] for e in events]
    verify(names.index('winner_identities_frozen') < names.index('training_arrays_frozen') < names.index('development_reference_read_start'), 'freeze_order')
    verify(max(i for i, name in enumerate(names) if name == 'pair_complete') < names.index('winner_identities_frozen'), 'no_postfreeze_training')
    verify(names[-1] == 'completed' and 'failed' not in names, 'completed_events')
    lines = [json.loads(line) for line in (RUN/'calls.jsonl').read_text().splitlines()]
    verify(calls == lines and len(calls) == result['calls'] <= 44 and len(rows) == result['unique_members'], 'call_counts')
    verify(sum(bool(row['cached']) for row in calls) == result['cached_calls'], 'cache_count')
    for call in calls:
        original = by_id[call['evaluation_id']]
        for key in ('theta', 'form_key', 'joint_score', 'resolution_valid'):
            verify(call[key] == original[key], 'cached_or_unique_identity:'+key)
    counter = result['counters']
    for stem, event_name, limit in [('propagations', 'propagation_start', 102), ('full_svd', 'full_svd_complete', 102),
                                  ('kinetic_eigh', 'kinetic_eigh_start', 54), ('static_readouts', 'static_readout_start', 12)]:
        actual = names.count(event_name)
        verify(counter[stem+'_attempted'] == counter[stem+'_completed'] == actual <= limit, 'science_count:'+stem)
    verify(counter['training_propagations_completed'] == 2*len(rows), 'train_forward_count')
    verify(counter['control_propagations_completed'] == 6, 'control_count')
    verify(counter['postfreeze_propagations_completed'] == len(result['postfreeze']) <= 8, 'post_count')
    verify(counts['heat_npz'] == counter['propagations_completed']+2*len(result['roles']), 'heat_array_count')
    verify(counts['full_heat'] == 6+counter['full_heat_grids_saved'] and counts['full_K'] == counter['kinetic_full_grids_saved'], 'full_array_count')
    verify(counts['static'] == counter['static_grids_saved'] == counter['static_readouts_completed'], 'static_array_count')
    verify(len(training) == 2*len(rows) and len(aliases) == counter['aliased_ablation_roles'], 'compact_alias_count')
    verify(result['invalid_unique_members'] == sum(not row['resolution_valid'] for row in rows), 'invalid_count')
    verify(all(value < 5e-9 for value in residual_max.values()), 'residual_engineering_ceiling')
    summary = dict(status='ANALYZED' if not failures else 'ISSUES_FOUND', failures=failures,
        checks=dict(checks), maximum_recomputation_differences=maxima, array_counts=dict(counts),
        training_pairs=len(rows), calls=len(calls), cached_calls=result['cached_calls'], csv_rows=csv_count,
        fitted_objects=len(members), fit_windows=sum(v is not None for v in fits.values())*4,
        comparison_windows=sum(v['windows'] is not None for v in comparisons.values())*4,
        aliases=len(aliases), minimum_records_checked=len(minima), input_hashes=len(manifest['inputs']),
        inventory_files=len(inventory), residual_maxima=residual_max, structure_assessment=structure,
        counters=counter, winners={key:{field:value[field] for field in ('evaluation_id', 'theta', 'joint_score', 'max_mape_percent', 'max_percent_error')}
                                  for key, value in result['roles'].items()}, checker_sha256=sha(Path(__file__)),
        valid_nonzero_M_count=len(nonzero), best_nonzero_M={key:best_nonzero[key] for key in
            ('evaluation_id', 'theta', 'joint_score', 'max_mape_percent', 'max_percent_error')} if best_nonzero else None,
        scope='Saved-array algebra, metrics and hashes only. ANALYZED, not a scientific rerun, decomposition or certified error bound.')
    print(json.dumps(summary, ensure_ascii=False, indent=2, allow_nan=False))
    if failures: raise SystemExit(1)


if __name__ == '__main__':
    main()
