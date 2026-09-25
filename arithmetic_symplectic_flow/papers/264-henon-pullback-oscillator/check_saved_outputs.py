#!/usr/bin/env python3
"""CS14 saved-evidence analysis only; first invocation belongs to the parent.

No runner import, eig/SVD, propagation, optimizer, roots, integration, target
generation, or file writes. Reconstructs finite Hermite polynomial algebra and
checks saved spectra/states/metrics, not an independently repeated experiment.
"""
import csv
import hashlib
import json
import math
from collections import Counter
from pathlib import Path

import numpy as np

PACKAGE = Path(__file__).resolve().parent
ROOT, RUN = PACKAGE.parents[1], PACKAGE/'evidence/run-1'
WINDOWS = {'1-100': (0, 100), '101-300': (100, 300), '301-320': (300, 320), '1-320': (0, 320)}
READOUTS = {'power_3_2': ('predicted_320', 'energy_power_3_2'), 'raw_J': ('raw_J_predicted_320', 'lambda_raw')}
MREF, WREF, FULLREF = 1.695273790061038, 5.234299091683695, 3.5251249515592384
RUNNER_SHA = 'a40936fc20007a06186e503e0e746dc8973f3fd52a416d182b022f49e3e6fd85'
checks, differences, failures = Counter(), {}, []


def read(name):
    return json.loads((RUN/name).read_text())


def sha(path):
    value = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024*1024), b''): value.update(block)
    return value.hexdigest()


def verify(condition, label):
    checks[label.split(':')[0]] += 1
    if not bool(condition): failures.append(label)


def close(actual, expected, label, atol=5e-11, rtol=2e-12):
    a, b = np.asarray(actual), np.asarray(expected)
    verify(a.shape == b.shape, label+':shape')
    if a.shape != b.shape: return
    verify(np.allclose(a, b, atol=atol, rtol=rtol, equal_nan=True), label)
    if a.size:
        mask = np.isfinite(a) & np.isfinite(b)
        value = float(np.max(np.abs(a[mask]-b[mask]))) if np.any(mask) else 0.
        key = label.split(':')[0]; differences[key] = max(differences.get(key, 0.), value)


def metrics(prediction, target):
    error = np.abs(prediction-target)
    return dict(count=len(target), mape_percent=float(100*np.mean(error/target)),
                max_percent_error=float(100*np.max(error/target)), rmse=float(np.sqrt(np.mean((prediction-target)**2))),
                max_absolute_error=float(np.max(error)))


def check_metrics(pred, target, saved, label):
    for key, value in metrics(pred, target).items(): close(value, saved[key], label+':'+key, atol=0, rtol=0)


def independent_hermite(h, n, rho):
    """Explicit ladder coefficients, including analytic two-step Q^2 chain."""
    b = rho*h
    x, derivative, q_squared = (np.zeros((n+2, n)) for _ in range(3))
    for j in range(n):
        if j:
            x[j-1, j] = math.sqrt(b*j/2)
            derivative[j-1, j] = math.sqrt(j/(2*b))
        x[j+1, j] = math.sqrt(b*(j+1)/2)
        derivative[j+1, j] = -math.sqrt((j+1)/(2*b))
        q_squared[j, j] = b*(j+.5)+.25
        if j >= 2: q_squared[j-2, j] = b/2*math.sqrt(j*(j-1))
        q_squared[j+2, j] = b/2*math.sqrt((j+1)*(j+2))
    q = x.copy(); q[np.arange(n), np.arange(n)] += .5
    q_squared += x  # (X + 1/2)^2 = X^2 + X + 1/4.
    h0 = np.diag((h*h/b+b)*(np.arange(n)+.5))
    off = (b-h*h/b)/2*np.sqrt(np.arange(1, n-1)*np.arange(2, n))
    h0 += np.diag(off, 2)+np.diag(off, -2)
    return {'X_rect': x, 'D_rect': derivative, 'Q_rect': q, 'Q_squared_rect': q_squared,
            'H0': h0, 'Q2': q.T@q, 'Y2': x.T@x, 'Q4': q_squared.T@q_squared}


def assemble_from_factors(factors, kappa, n):
    eye = np.eye(n)
    return np.kron(factors['H0'], eye)+np.kron(eye, factors['H0'])+kappa*(np.kron(factors['Q4'], eye)+4*np.kron(factors['Q2'], factors['Y2']))


def oscillator(h, n):
    return np.sort(np.asarray([2*h*(i+j+1) for i in range(n) for j in range(n)]))


def compact(a):
    keys = ('theta', 'lambda_raw', 'energy_power_3_2', 'predicted_320', 'raw_J_predicted_320')
    return {**{key:a[key][:320].copy() for key in keys}, 'valid':bool(a['valid']),
            'n':int(a['n']), 'rho':float(a['rho']), 'scale':float(a['scale']), 'raw_J_scale':float(a['raw_J_scale'])}


def inspect_array(path, truth, maxima):
    name = path.stem; record = json.loads(path.with_suffix('.json').read_text())
    control = name.startswith('control-')
    with np.load(path, allow_pickle=False) as a:
        n, dimension, h, kappa, rho = int(a['n']), int(a['dimension']), float(a['h']), float(a['kappa']), float(a['rho'])
        verify(dimension == n*n == record['dimension'] and n == record['n'], 'dimension:'+name)
        close(a['theta'], [h, kappa], 'theta:'+name, atol=0, rtol=0)
        for key, value in [('h', h), ('kappa', kappa), ('rho', rho), ('eta', .5), ('a_representative', 2*math.sqrt(kappa))]:
            close(value, a[key], 'parameter:'+name+':'+key, atol=0, rtol=0)
            close(value, record[key], 'metadata:'+name+':'+key, atol=0, rtol=0)
        close(a['theta'], record['theta'], 'theta_record:'+name, atol=0, rtol=0)
        close(rho*h, a['hermite_width_b'], 'width:'+name, atol=0, rtol=0)
        if not control:
            verify(.015 <= h <= .6 and (kappa == 0. if name.startswith('sourceoff') else .05 <= kappa <= 30.), 'box:'+name)
            verify(n == int(name.rsplit('-n', 1)[1]) and rho == (1.25 if 'width125' in name else 1.), 'named_grid:'+name)
        qdegree, ydegree = np.repeat(np.arange(n), n), np.tile(np.arange(n), n)
        verify(np.array_equal(qdegree, a['basis_q_degree']) and np.array_equal(ydegree, a['basis_y_degree']), 'basis_order:'+name)
        factors = independent_hermite(h, n, rho)
        for key, value in factors.items(): close(value, a[key], 'Hermite_factor:'+name+':'+key)
        source_matrix = a['matrix_S']
        expected = assemble_from_factors(factors, kappa, n)
        scale = max(1., float(np.max(np.abs(source_matrix))))
        error = float(np.max(np.abs(expected-source_matrix)))/scale
        verify(source_matrix.shape == (dimension, dimension) and error < 1e-12, 'matrix_formula:'+name)
        maxima['matrix_relative'] = max(maxima['matrix_relative'], error)
        from_saved = assemble_from_factors(a, kappa, n)
        close(from_saved, source_matrix, 'matrix_saved_factors:'+name, atol=0, rtol=0)
        symmetry = float(np.max(np.abs(source_matrix-source_matrix.T)))
        verify(symmetry < 1e-12*scale, 'matrix_symmetry:'+name)
        close(symmetry, record['matrix_symmetry_max_difference'], 'symmetry_record:'+name, atol=0, rtol=0)
        if rho == 1.:
            close(np.diag(h*(2*np.arange(n)+1)), a['H0'], 'oscillator_H0:'+name)
        raw = a['lambda_raw']; required = dimension if control else 320
        verify(raw.shape == (dimension,) and np.all(np.isfinite(raw)) and raw[0] > 0 and np.all(np.diff(raw) >= 0), 'raw_lambda:'+name)
        with np.errstate(over='ignore', invalid='ignore'):
            energy = raw**1.5; prediction = truth[0]*(raw[:320]/raw[0])**1.5; raw_prediction = truth[0]*raw[:320]/raw[0]
        finite = np.isfinite(energy); reasons = []
        if dimension < required: reasons.append('INSUFFICIENT_SPECTRAL_COUNT')
        if not np.all(finite[:required]) or not np.all(np.isfinite(prediction[:required])) or not np.all(energy[:required] > 0): reasons.append('PRIMARY_PREFIX_ENERGY_OR_PREDICTION_INVALID')
        if not np.all(np.diff(energy[:required]) >= 0): reasons.append('PRIMARY_PREFIX_ENERGY_NOT_NONDECREASING')
        if not np.all(np.isfinite(raw_prediction[:required])): reasons.append('RAW_J_PREFIX_PREDICTION_INVALID')
        verify(reasons == a['invalid_reasons'].tolist() == record['invalid_reasons'], 'invalid_reasons:'+name)
        verify(bool(a['valid']) == record['valid'] == (not reasons), 'valid:'+name)
        verify(np.array_equal(finite, a['finite_mask']) and np.array_equal(np.isfinite(raw), a['raw_J_finite_mask']), 'finite_masks:'+name)
        for key, value in [('energy_power_3_2', energy), ('predicted_320', prediction), ('raw_J_predicted_320', raw_prediction),
                           ('scale', truth[0]/energy[0]), ('raw_J_scale', truth[0]/raw[0]), ('target_100', truth[:100])]:
            close(value, a[key], 'readout:'+name+':'+key, atol=0, rtol=0)
        verify(record['no_clipping_or_deleted_modes'] and record['full_spectrum_count'] == dimension and record['required_energy_count'] == required, 'whole_spectrum:'+name)
        if record['valid'] and not control:
            check_metrics(prediction[:100], truth[:100], record['training_metrics'], 'train_metrics:'+name)
            check_metrics(raw_prediction[:100], truth[:100], record['raw_J_training_metrics'], 'train_raw_metrics:'+name)
        else: verify(record['training_metrics'] is None and record['raw_J_training_metrics'] is None, 'no_invalid_fit:'+name)
        trace, fro = float(np.trace(source_matrix)), float(np.sum(source_matrix*source_matrix))
        trace_error = abs(trace-float(np.sum(raw)))/max(1., abs(trace))
        moment_error = abs(fro-float(np.sum(raw*raw)))/max(1., fro)
        rows = float(np.max(np.sum(np.abs(source_matrix), axis=1)))
        for key, value in [('trace_J', trace), ('full_lambda_sum', np.sum(raw)), ('trace_relative_difference', trace_error),
                           ('frobenius_squared_J', fro), ('full_lambda_squared_sum', np.sum(raw*raw)), ('second_moment_relative_difference', moment_error),
                           ('J_absolute_row_sum_max', rows), ('lambda_min', raw[0]), ('lambda_max', raw[-1])]:
            close(value, record[key], 'spectral_record:'+name+':'+key)
        verify(max(trace_error, moment_error) < 1e-11, 'spectral_moments:'+name)
        maxima['trace_relative'] = max(maxima['trace_relative'], trace_error)
        maxima['second_moment_relative'] = max(maxima['second_moment_relative'], moment_error)
        retained = min(dimension, 320); high_count = (n+4)//5
        boundary = (qdegree >= n-high_count) | (ydegree >= n-high_count)
        verify(np.array_equal(boundary, a['truncation_edge_mask']) and record['edge_top_modes_each_axis'] == high_count, 'edge_union:'+name)
        saved_error, saved_edge = a['eigenvector_residual'], a['truncation_edge_occupation']
        verify(saved_error.shape == saved_edge.shape == (retained,) and record['retained_states'] == retained, 'diagnostic_shapes:'+name)
        close(np.max(saved_error), record['eigenvector_residual_max'], 'saved_residual_summary:'+name)
        close(float(np.max(saved_error))/max(1., rows), record['eigenvector_residual_relative_row_norm_max'], 'saved_relative_summary:'+name)
        windows = [(str(k), k) for k in (100, 320) if retained >= k] or [('all_control_states', retained)]
        for label, count in windows:
            for key, value in [('mean', np.mean(saved_edge[:count])), ('max', np.max(saved_edge[:count]))]:
                close(value, record['edge_occupation_summary'][label][key], 'edge_summary:'+name+':'+label)
        has_states = 'states' in a
        verify(has_states == record['states_saved'], 'states_saved:'+name)
        if has_states:
            states = a['states']; verify(states.shape == (dimension, retained), 'state_shape:'+name)
            residual = np.sqrt(np.sum((source_matrix@states-states*raw[:retained])**2, axis=0))
            orth = float(np.sqrt(np.sum((states.T@states-np.eye(retained))**2)))
            edge = np.sum(states[boundary]**2, axis=0)
            close(residual, saved_error, 'state_residual:'+name, atol=5e-10)
            close(edge, saved_edge, 'state_edge:'+name, atol=2e-13)
            close(orth, record['states_orthogonality_fro'], 'state_orthogonality:'+name)
            relative = float(np.max(residual))/max(1., rows)
            verify(relative < 1e-11 and orth < 1e-8, 'state_engineering_check:'+name)
            maxima['state_absolute'] = max(maxima['state_absolute'], float(np.max(residual)))
            maxima['state_relative'] = max(maxima['state_relative'], relative)
            maxima['orthogonality'] = max(maxima['orthogonality'], orth)
        if 'expected_lambda' in a:
            expected_lambda = oscillator(h, n); error = float(np.max(np.abs(raw-expected_lambda)))
            tolerance = 1e-10*max(1., float(np.max(np.abs(expected_lambda))))
            close(expected_lambda, a['expected_lambda'], 'analytic_reference:'+name, atol=0, rtol=0)
            saved = record['control_checks'] if control else record['sourceoff_control']
            close(error, saved['lambda_max_absolute_difference'], 'analytic_error:'+name, atol=0, rtol=0)
            close(tolerance, saved['lambda_tolerance'], 'analytic_tolerance:'+name, atol=0, rtol=0)
            verify(error <= tolerance and saved['passed'] and len(raw) == n*n, 'analytic_full_spectrum:'+name)
        if control:
            verify(n == 8 and h == .16 and record['control_checks']['passed'], 'small_control:'+name)
            if 'independent_padding4_matrix_S' in a:
                reference = a['independent_padding4_matrix_S']; error = float(np.max(np.abs(source_matrix-reference)))
                tolerance = 1e-10*max(1., float(np.max(np.abs(reference))))
                close(reference, expected, 'padding_control_reference:'+name)
                close(error, record['control_checks']['matrix_max_absolute_difference'], 'padding_error:'+name, atol=0, rtol=0)
                close(tolerance, record['control_checks']['matrix_tolerance'], 'padding_tolerance:'+name, atol=0, rtol=0)
                verify(error <= tolerance, 'padding_control_gate:'+name)
        return compact(a), has_states, control


def main():
    result, manifest = read('result.json'), read('manifest.json')
    verify(result['status'] in ('completed', 'completed_no_valid_member'), 'completed_result')
    truth = np.asarray(read('known-targets.json')['ordinates'])
    verify(truth.shape == (320,) and np.all(np.diff(truth) > 0), 'target320')
    maxima = dict(matrix_relative=0., trace_relative=0., second_moment_relative=0., state_absolute=0., state_relative=0., orthogonality=0.)
    training, members, array_counts, invalid = {}, {}, Counter(), []
    paths = sorted((RUN/'evaluations').glob('*-n*.npz'))+sorted(RUN.glob('*.npz'))
    for path in paths:
        member, has_states, control = inspect_array(path, truth, maxima)
        array_counts['object_npz'] += 1; array_counts['full_state_npz'] += int(has_states); array_counts['control_npz'] += int(control)
        if not member['valid']: invalid.append(path.stem)
        if not control: (training if path.parent.name == 'evaluations' else members)[path.stem] = member
    print('ARRAY_AUDIT_COMPLETE', dict(array_counts), flush=True)
    finish(result, manifest, truth, training, members, array_counts, maxima, invalid)


def finish(result, manifest, truth, training, members, array_counts, maxima, invalid):
    with np.load(ROOT/'papers/253-structural-homotopy-search/evidence/run-1/evaluations/CS03-Q-QUARTIC-0103.npz', allow_pickle=False) as old:
        portions = [old['target_100'].copy()]
    for folder, file, count in [
        ('251-constructive-fit-portfolio', 'reference-101-150.json', 50),
        ('253-structural-homotopy-search', 'reference-151-200.json', 50),
        ('254-global-forms-joint-fit', 'reference-201-240.json', 40),
        ('255-path-operator-multigrid', 'reference-241-300.json', 60),
        ('256-chronological-heat-spectrum', 'reference-301-320.json', 20)]:
        values = np.asarray([float(v) for v in json.loads((ROOT/'papers'/folder/'evidence/run-1'/file).read_text())['ordinates']])
        verify(len(values) == count, 'target_portion:'+file); portions.append(values)
    verify(np.array_equal(np.concatenate(portions), truth), 'original_target320')
    rows, calls, frozen = read('unique-members.json'), read('calls.json'), read('winners-frozen.json')
    ranks, by_id = [], {}
    for row in rows:
        eid = row['evaluation_id']; by_id[eid] = row
        aa, bb = training[eid+'-n24'], training[eid+'-n28']
        for member in (aa, bb): close(member['theta'], row['theta'], 'pair_theta:'+eid, atol=0, rtol=0)
        verify((aa['valid'] and bb['valid']) == row['valid'], 'pair_valid:'+eid)
        if not row['valid']:
            verify(row['joint_score'] == 1e30 and row['status'] == 'INVALID_MEMBER', 'invalid_penalty:'+eid)
            continue
        ma, mb = metrics(aa['predicted_320'][:100], truth[:100]), metrics(bb['predicted_320'][:100], truth[:100])
        for n, member in ((24, aa), (28, bb)):
            check_metrics(member['predicted_320'][:100], truth[:100], row['grids'][str(n)]['training_metrics'], 'pair_grid_metrics:'+eid+':'+str(n))
            check_metrics(member['raw_J_predicted_320'][:100], truth[:100], row['grids'][str(n)]['raw_J_training_metrics'], 'pair_grid_raw_metrics:'+eid+':'+str(n))
        gap = float(100*np.max(np.abs(aa['predicted_320'][:100]-bb['predicted_320'][:100])/truth[:100]))
        maximum_m, maximum_w = max(ma['mape_percent'], mb['mape_percent']), max(ma['max_percent_error'], mb['max_percent_error'])
        score = max(maximum_m/MREF, maximum_w/WREF, gap/2)
        for key, value in [('joint_score', score), ('J_minus_1', score-1), ('max_mape_percent', maximum_m), ('max_percent_error', maximum_w), ('G100_percent', gap)]:
            close(value, row[key], 'pair_score:'+eid+':'+key, atol=0, rtol=0)
        ranks.append((score, maximum_m, maximum_w, gap, eid))
    winner = result['winner']
    verify(frozen['winner'] == winner and not frozen['development_metrics_evaluated'], 'frozen_identity')
    verify((min(ranks)[-1] if ranks else None) == (winner['evaluation_id'] if winner else None), 'winner_rank')
    verify(set(training) == {row['evaluation_id']+'-n'+str(n) for row in rows for n in (24, 28)}, 'training_coverage')
    if winner:
        for n in (24, 28):
            with np.load(RUN/f'winner-n{n}.npz', allow_pickle=False) as a, np.load(RUN/'evaluations'/f'{winner["evaluation_id"]}-n{n}.npz', allow_pickle=False) as b:
                for key in ('theta', 'matrix_S', 'lambda_raw', 'energy_power_3_2', 'predicted_320', 'raw_J_predicted_320', 'eigenvector_residual', 'truncation_edge_occupation'):
                    close(a[key], b[key], 'winner_copies:'+str(n)+':'+key, atol=0, rtol=0)
        verify(set(members) == {'winner-n24', 'winner-n28', 'post-n36', 'post-n44', 'post-n52', 'post-width125-n52', 'sourceoff-n52'}, 'full_objects')
        for name, member in members.items():
            expected = list(winner['theta'])
            if name == 'sourceoff-n52': expected[1] = 0.
            close(member['theta'], expected, 'fixed_theta:'+name, atol=0, rtol=0)
    else: verify(not members, 'no_winner_no_post')
    fits, comparisons = read('development-fit-metrics.json'), read('comparisons.json')
    verify(set(fits) == set(members) and fits == result['fit_metrics'], 'fit_coverage')
    for name, saved in fits.items():
        for readout, (predkey, energykey) in READOUTS.items():
            if not members[name]['valid']:
                verify(saved[readout] is None, 'invalid_fit:'+name+':'+readout); continue
            for window, (start, stop) in WINDOWS.items():
                check_metrics(members[name][predkey][start:stop], truth[start:stop], saved[readout][window], 'fit:'+name+':'+readout+':'+window)
    verify(comparisons == result['comparisons'], 'comparison_result')
    expected_pairs = [('n24-n28', 'winner-n24', 'winner-n28'), ('n28-n36', 'winner-n28', 'post-n36'),
                      ('n36-n44', 'post-n36', 'post-n44'), ('n44-n52', 'post-n44', 'post-n52'),
                      ('width125', 'post-n52', 'post-width125-n52'), ('SOURCEOFF', 'post-n52', 'sourceoff-n52')] if winner else []
    verify(set(comparisons) == {row[0] for row in expected_pairs}, 'comparison_coverage')
    for label, left, right in expected_pairs:
        aa, bb = members[left], members[right]
        for readout, (predkey, energykey) in READOUTS.items():
            saved = comparisons[label][readout]
            verify(saved['left'] == left and saved['right'] == right and saved['readout'] == readout and saved['G_threshold_percent'] == 2., 'comparison_owner:'+label+':'+readout)
            if not (aa['valid'] and bb['valid']):
                verify(saved['windows'] is None and saved['right_minus_left_fit_percentage_points'] is None, 'invalid_comparison:'+label); continue
            for window, (start, stop) in WINDOWS.items():
                gap = float(100*np.max(np.abs(aa[predkey][start:stop]-bb[predkey][start:stop])/truth[start:stop]))
                raw_gap = float(100*np.max(np.abs(aa[energykey][start:stop]-bb[energykey][start:stop])/aa[energykey][start:stop]))
                lam = float(np.max(np.abs(aa['lambda_raw'][start:stop]-bb['lambda_raw'][start:stop])))
                for key, value in [('G_percent', gap), ('unscaled_energy_max_relative_percent', raw_gap), ('raw_lambda_max_absolute_difference', lam)]:
                    close(value, saved['windows'][window][key], 'comparison:'+label+':'+readout+':'+window+':'+key, atol=0, rtol=0)
                verify((gap < 2) == saved['windows'][window]['G_below_threshold'], 'comparison_gate:'+label+':'+readout+':'+window)
                for key in ('mape_percent', 'max_percent_error'):
                    close(fits[right][readout][window][key]-fits[left][readout][window][key], saved['right_minus_left_fit_percentage_points'][window][key], 'comparison_shift:'+label+':'+readout+':'+window+':'+key, atol=0, rtol=0)
    external = read('external-history-comparator.json')
    verify(not external['raw_spectrum_comparison_permitted'] and sha(ROOT/external['source']) == external['source_sha256'], 'external_owner')
    with np.load(ROOT/external['source'], allow_pickle=False) as old:
        close(old['predicted_320'], external['predicted_320'], 'external_predictions', atol=0, rtol=0)
        for window, (start, stop) in WINDOWS.items(): check_metrics(old['predicted_320'][start:stop], truth[start:stop], external['fit_metrics'][window], 'external_fit:'+window)
    close(external['fit_metrics']['1-320']['mape_percent'], FULLREF, 'external_reference', atol=1e-10, rtol=0)
    historical = json.loads((ROOT/'papers/259-hyperbolic-tail-heat-search/evidence/run-1/result.json').read_text())['roles']['B']
    verify(historical['evaluation_id'] == 'CS09-B-QUINTIC-REFIT-0055', 'external_identity')
    close(historical['max_mape_percent'], MREF, 'external_M', atol=1e-12, rtol=0)
    close(historical['max_percent_error'], WREF, 'external_W', atol=1e-12, rtol=0)
    assessment = read('finite-discovery-assessment.json')
    if winner:
        training_better = all(fits[f'winner-n{n}']['power_3_2']['1-100']['mape_percent'] < MREF and fits[f'winner-n{n}']['power_3_2']['1-100']['max_percent_error'] < WREF for n in (24, 28))
        resolution = {label: all(v['G_below_threshold'] for v in comparisons[label]['power_3_2']['windows'].values()) if comparisons[label]['power_3_2']['windows'] is not None else None for label in ('n36-n44', 'n44-n52', 'width125')}
        full = fits['post-n52']['power_3_2']
        better_full = full is not None and full['1-320']['mape_percent'] < FULLREF
        complete = bool(winner['joint_score'] < 1 and training_better and better_full and all(v is True for v in resolution.values()))
        status = 'NECESSARY_FINITE_ADVANCE_CONDITIONS_MET_MAGNITUDE_REVIEW_REQUIRED' if complete else 'NECESSARY_FINITE_ADVANCE_CONDITIONS_NOT_MET'
        verify(assessment['each_training_M_W_below_external_reference'] == training_better and assessment['n52_full320_M_below_external_reference'] == better_full, 'assessment_fits')
        verify(assessment['fine_and_width_checks'] == resolution and assessment['full_necessary_conditions_met'] == complete and assessment['status'] == status, 'assessment_gate')
    else: verify(assessment['status'] == 'NO_VALID_MEMBER' and not assessment['full_necessary_conditions_met'], 'empty_assessment')
    verify(assessment == result['finite_discovery_assessment'] and result['raw_J_never_reselected'] and result['primary_readout_fixed_power'] == 1.5, 'assessment_result')
    csv_counts = inspect_csv(members, truth, fits, comparisons)
    for path, expected in manifest['inputs'].items(): verify(sha(ROOT/path) == expected, 'input_hash:'+path)
    verify(len(manifest['inputs']) == 16 and json.loads((PACKAGE/'input-locks.json').read_text()) == manifest['inputs'], 'input_lock_set')
    verify(sha(PACKAGE/'input-locks.json') == manifest['input_locks_sha256'], 'input_lock_hash')
    verify(sha(PACKAGE/'run_search.py') == manifest['script_sha256'] == RUNNER_SHA, 'runner_hash')
    freeze = read('training-arrays-frozen.json')
    for path, expected in freeze['files_sha256'].items(): verify(sha(RUN/path) == expected, 'frozen_array_hash:'+path)
    verify(len(freeze['files_sha256']) == (4 if winner else 0), 'frozen_array_count')
    verify(sha(RUN/'winners-frozen.json') == freeze['winner_identity_sha256'] == result['winner_identity_sha256'], 'frozen_identity_hash')
    inventory = read('file-inventory.json')['files']
    for path, row in inventory.items():
        verify((RUN/path).stat().st_size == row['bytes'], 'inventory_size:'+path)
        verify(sha(RUN/path) == row['sha256'], 'inventory_hash:'+path)
    files = [p for p in RUN.rglob('*') if p.is_file()]
    verify(set(inventory) == {str(p.relative_to(RUN)) for p in files if p.name != 'file-inventory.json'}, 'inventory_coverage')
    events = [json.loads(line) for line in (RUN/'events.jsonl').read_text().splitlines()]
    names = [row['event'] for row in events]
    verify(max(i for i, e in enumerate(names) if e == 'pair_complete') < names.index('winner_identity_frozen') < names.index('training_arrays_frozen') < names.index('development_reference_read_start'), 'freeze_order')
    verify(names[-1] == 'completed' and 'failed' not in names, 'completed_events')
    verify(calls == [json.loads(line) for line in (RUN/'calls.jsonl').read_text().splitlines()] and len(calls) == result['calls'] <= 30 and len(rows) == result['unique_members'], 'call_counts')
    verify(sum(bool(row['cached']) for row in calls) == result['cached_calls'], 'cache_count')
    seen = set()
    for i, call in enumerate(calls, 1):
        verify(call['call'] == i, 'call_order')
        key = tuple(float(v).hex() for v in call['theta'])
        verify(call['cached'] == (key in seen), 'exact_cache_identity'); seen.add(key)
        for key in ('theta', 'valid', 'joint_score'): verify(call[key] == by_id[call['evaluation_id']][key], 'call_row:'+key)
    seeds = [[h, k] for h in (.025, .08, .25, .6) for k in (.1, 1., 10.)]
    verify(read('seed-design.json')['physical_seeds'] == seeds and [c['theta'] for c in calls[:12]] == seeds, 'seed_design')
    for call in calls:
        normalized = (np.log(call['theta'])-np.log([.015, .05]))/(np.log([.6, 30.])-np.log([.015, .05]))
        close(normalized, call['normalized_log_x'], 'log_coordinates', atol=5e-15, rtol=0)
    counter = result['counters']
    number = names.count('forward_start')
    verify(counter['forwards_attempted'] == counter['forwards_completed'] == counter['physical_eigh_attempted'] == counter['physical_eigh_completed'] == names.count('physical_eigh_complete') == number <= 68, 'physical_counts')
    for stage, limit in [('control', 3), ('training', 60), ('postfreeze', 4), ('sourceoff', 1)]:
        num = sum(e['event'] == 'forward_start' and e['stage'] == stage for e in events)
        verify(counter[stage+'_forwards_attempted'] == counter[stage+'_forwards_completed'] == num <= limit, 'stage_counts:'+stage)
    verify(counter['matrix_assemblies_attempted'] == counter['matrix_assemblies_completed'] == number and counter['independent_control_matrix_assemblies_attempted'] == counter['independent_control_matrix_assemblies_completed'] == 2, 'assembly_counts')
    verify(counter['training_forwards_completed'] == 2*len(rows) == len(training), 'pair_physical_count')
    verify(all(counter[key] == 0 for key in ('svd_calls', 'root_calls', 'quadrature_calls', 'extra_state_eigh_calls', 'new_target_generations')), 'no_extra_science')
    verify(array_counts['object_npz'] == number+(2 if winner else 0) and array_counts['full_state_npz'] == counter['full_arrays_saved']+3 and array_counts['control_npz'] == 3, 'array_counts')
    verify(result['invalid_unique_members'] == sum(not row['valid'] for row in rows), 'invalid_count')
    verify(result['optimizer'] == frozen['optimizer'] and result['optimizer']['nfev'] <= 18, 'optimizer_budget')
    summary = dict(status='ANALYZED' if not failures else 'ISSUES_FOUND', failures=failures, checks=dict(checks),
                   maximum_recomputation_differences=differences, residual_maxima=maxima, array_counts=dict(array_counts),
                   physical_decompositions_in_science=number, calls=len(calls), unique_training_pairs=len(rows), cached_calls=result['cached_calls'],
                   fitted_objects=len(members), fitted_windows=sum(v['power_3_2'] is not None for v in fits.values())*8,
                   comparison_windows=sum(v['power_3_2']['windows'] is not None for v in comparisons.values())*8, csv_rows=csv_counts,
                   input_hashes=len(manifest['inputs']), training_frozen_files=len(freeze['files_sha256']), inventory_members=len(inventory),
                   all_files_including_inventory=len(files), all_bytes_including_inventory=sum(p.stat().st_size for p in files),
                   invalid_objects=invalid, winner=None if winner is None else {k:winner[k] for k in ('evaluation_id', 'theta', 'joint_score', 'max_mape_percent', 'max_percent_error', 'G100_percent')},
                   optimizer=result['optimizer'], assessment=assessment, counters=counter, checker_sha256=sha(Path(__file__)),
                   scope='Saved evidence and finite Hermite algebra only; no new eig/SVD/optimization/root/integration/runner import/targets.',
                   missing_state_limit='Nonwinner states absent: their full matrices/spectra/moments/readouts and saved diagnostic summaries checked, not the missing vector equations.')
    print(json.dumps(summary, ensure_ascii=False, indent=2, allow_nan=False))
    if failures: raise SystemExit(1)


def inspect_csv(members, truth, fits, comparisons):
    counts, objects = Counter(), Counter()
    with (RUN/'points.csv').open(newline='') as stream:
        for row in csv.DictReader(stream):
            name, readout, index = row['object_id'], row['readout'], int(row['index'])-1
            a = members[name]; predkey, energykey = READOUTS[readout]
            target, pred, energy, lam = truth[index], a[predkey][index], a[energykey][index], a['lambda_raw'][index]
            for key, value in [('target', target), ('predicted', pred), ('energy', energy), ('lambda_raw', lam), ('residual', pred-target), ('percent_error', 100*abs(pred-target)/target)]:
                close(float(row[key]), value, 'csv_point:'+key, atol=0, rtol=0)
            verify(int(row['n']) == a['n'] and int(row['dimension']) == a['n']**2 and float(row['h']) == a['theta'][0] and float(row['kappa']) == a['theta'][1] and float(row['rho']) == a['rho'] and row['valid'] == str(a['valid']), 'csv_metadata')
            verify(row['window'] == ('1-100' if index < 100 else '101-300' if index < 300 else '301-320'), 'csv_window')
            objects[name, readout] += 1; counts['points'] += 1
    verify(set(objects) == {(name, readout) for name in members for readout in READOUTS} and all(v == 320 for v in objects.values()), 'csv_point_coverage')
    fitkeys = []
    with (RUN/'fit-rows.csv').open(newline='') as stream:
        for row in csv.DictReader(stream):
            name, readout, window = row['object_id'], row['readout'], row['window']
            saved = fits[name][readout]
            verify(row['valid'] == str(members[name]['valid']), 'csv_fit_valid')
            for key in ('count', 'mape_percent', 'max_percent_error', 'rmse', 'max_absolute_error'):
                if saved is None: verify(row[key] == '', 'csv_invalid_fit')
                else: close(float(row[key]), saved[window][key], 'csv_fit:'+key, atol=0, rtol=0)
            fitkeys.append((name, readout, window)); counts['fits'] += 1
    verify(len(fitkeys) == len(set(fitkeys)) and set(fitkeys) == {(name, readout, window) for name in members for readout in READOUTS for window in WINDOWS}, 'csv_fit_coverage')
    compkeys = []
    with (RUN/'comparison-rows.csv').open(newline='') as stream:
        for row in csv.DictReader(stream):
            label, readout, window = row['comparison'], row['readout'], row['window']; saved = comparisons[label][readout]
            verify(row['left'] == saved['left'] and row['right'] == saved['right'] and row['status'] == saved['status'], 'csv_comparison_owner')
            if saved['windows'] is None:
                verify(all(row[k] == '' for k in ('G_percent', 'G_below_2_percent', 'unscaled_energy_max_relative_percent', 'raw_lambda_max_absolute_difference', 'right_minus_left_M', 'right_minus_left_W')), 'csv_invalid_comparison')
            else:
                for key in ('G_percent', 'unscaled_energy_max_relative_percent', 'raw_lambda_max_absolute_difference'):
                    close(float(row[key]), saved['windows'][window][key], 'csv_comparison:'+key, atol=0, rtol=0)
                verify(row['G_below_2_percent'] == str(saved['windows'][window]['G_below_threshold']), 'csv_comparison_gate')
                for column, key in [('right_minus_left_M', 'mape_percent'), ('right_minus_left_W', 'max_percent_error')]:
                    close(float(row[column]), saved['right_minus_left_fit_percentage_points'][window][key], 'csv_comparison_shift:'+column, atol=0, rtol=0)
            compkeys.append((label, readout, window)); counts['comparisons'] += 1
    verify(len(compkeys) == len(set(compkeys)) and set(compkeys) == {(label, readout, window) for label in comparisons for readout in READOUTS for window in WINDOWS}, 'csv_comparison_coverage')
    return dict(counts)


if __name__ == '__main__':
    main()
