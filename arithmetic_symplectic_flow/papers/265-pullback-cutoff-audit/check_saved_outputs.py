#!/usr/bin/env python3
"""CS15 saved-array analysis only: no eig/SVD, optimization, roots or integration.

Reconstructs polynomial factors, saved block equations and genuine rectangular
actions. Does not import the scientific runner, generate targets or write files.
First invocation belongs to the parent after its observed scientific exit 0.
"""
import csv
import hashlib
import json
import math
from collections import Counter
from pathlib import Path

import numpy as np

PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[1]
RUN = PACKAGE/'evidence/run-1'
OLD = ROOT/'papers/264-henon-pullback-oscillator/evidence/run-1'
RUNNER_SHA = 'cf05402b4ac5e756b97780e65d3902e4a669535181559a5040c56a5c1a011c33'
THETA = (.02263390483074383, 11.825457423506625)
PRIMARY = 'fine-n96'
WINDOWS = {'1-100': (0, 100), '101-300': (100, 300), '301-320': (300, 320), '1-320': (0, 320)}
READOUTS = {'power_3_2': ('predicted_320', 'energy_power_3_2'), 'raw_J': ('raw_J_predicted_320', 'lambda_raw')}
SPECS = [('control-sourceoff', 8, .16, 0., 1.), ('control-winner-rho1', 8, *THETA, 1.),
         ('control-winner-rho080', 8, *THETA, .8), ('control-winner-rho125', 8, *THETA, 1.25),
         ('bridge-n52', 52, *THETA, 1.), ('fine-n64', 64, *THETA, 1.), ('fine-n80', 80, *THETA, 1.),
         ('fine-n96', 96, *THETA, 1.), ('width080-n96', 96, *THETA, .8), ('width125-n96', 96, *THETA, 1.25)]
checks, maximum_differences, failures = Counter(), {}, []
maxima = dict(matrix_relative=0., finite_equation_absolute=0., orthogonality_max=0.,
              trace_relative=0., second_moment_relative=0., tensor_action_relative=0., pythagorean_relative=0.)


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
        key = label.split(':')[0]; maximum_differences[key] = max(maximum_differences.get(key, 0.), value)


def norm(x, axis=None):
    return np.sqrt(np.sum(np.abs(x)**2, axis=axis))


def check_gate(saved, error, tolerance, label):
    close(error, saved['error'], 'gate_error:'+label)
    close(tolerance, saved['tolerance'], 'gate_tolerance:'+label, atol=1e-20)
    passed = error < tolerance if saved.get('strict_less') else error <= tolerance
    verify(passed and saved['passed'] == passed, 'hard_gate:'+label)


def matrix_match(actual, expected, label):
    error = float(np.max(np.abs(actual-expected)))/max(1., float(np.max(np.abs(expected))))
    verify(actual.shape == expected.shape and error < 1e-12, 'matrix_formula:'+label)
    maxima['matrix_relative'] = max(maxima['matrix_relative'], error)


def factors(h, n, rho):
    """Independent ladder-coefficient algebra on +8, then true rectangles.

    No eigenproblem or numerical integration. H0's explicit coefficients avoid
    squaring a truncated differential matrix at the physical cutoff.
    """
    b = rho*h; size = n+8
    x, d = np.zeros((size, size)), np.zeros((size, size))
    for j in range(size):
        if j:
            x[j-1, j] = math.sqrt(b*j/2); d[j-1, j] = math.sqrt(j/(2*b))
        if j+1 < size:
            x[j+1, j] = math.sqrt(b*(j+1)/2); d[j+1, j] = -math.sqrt((j+1)/(2*b))
    q = x+.5*np.eye(size); q2, y2 = q@q, x@x; q4 = q2@q2
    h0 = np.diag((h*h/b+b)*(np.arange(size)+.5))
    off = (b-h*h/b)/2*np.sqrt(np.arange(1, size-1)*np.arange(2, size))
    h0 += np.diag(off, 2)+np.diag(off, -2)
    xr, dr, qr, qsr = x[:n+2, :n], d[:n+2, :n], q[:n+2, :n], q2[:n+2, :n]
    return dict(X_rect=xr, D_rect=dr, Q_rect=qr, Q_squared_rect=qsr, H0=h0[:n, :n],
                Q2=qr.T@qr, Y2=xr.T@xr, Q4=qsr.T@qsr,
                E_action=np.eye(size)[:n+4, :n], H0_action=h0[:n+4, :n],
                Q2_action=q2[:n+4, :n], Y2_action=y2[:n+4, :n], Q4_action=q4[:n+4, :n])


def matrix_from_factors(f, kappa, y):
    n = len(f['H0']); eyeq, eyey = np.eye(n), np.eye(len(y))
    return np.kron(f['H0'], eyey)+np.kron(eyeq, f['H0'][np.ix_(y, y)])+kappa*(np.kron(f['Q4'], eyey)+4*np.kron(f['Q2'], f['Y2'][np.ix_(y, y)]))


def rectangular_action(f, states, n, kappa):
    c = states.reshape(n, n, -1); result = np.zeros((n+4, n+4, c.shape[2]))
    result[:, :n] = np.tensordot(f['H0_action']+kappa*f['Q4_action'], c, axes=(1, 0))
    result[:n, :] += np.tensordot(c, f['H0_action'].T, axes=(1, 0)).transpose(0, 2, 1)
    result += 4*kappa*np.einsum('ai,ijc,bj->abc', f['Q2_action'], c, f['Y2_action'], optimize=True)
    return result


def finite_check(a, record, label):
    matrix, raw, states = a['matrix_S'], a['lambda_raw'], a['states']; count = states.shape[1]
    verify(matrix.shape == (len(raw), len(raw)) and states.shape == (len(raw), min(320, len(raw))), 'finite_shapes:'+label)
    verify(np.all(np.isfinite(raw)) and raw[0] > 0 and np.all(np.diff(raw) >= 0), 'positive_sorted_spectrum:'+label)
    action = matrix@states; delta = action-states*raw[:count]; residual = norm(delta, axis=0)
    orth = states.T@states-np.eye(count); trace, fro = float(np.trace(matrix)), float(np.sum(matrix*matrix))
    close(residual, a['eigenvector_residual'], 'finite_residual:'+label)
    close(np.max(residual), record['retained_state_residual_norm_max'], 'finite_residual_summary:'+label)
    close(norm(orth), record['retained_state_orthogonality_fro'], 'finite_orth_summary:'+label)
    fields = dict(trace_J=trace, full_lambda_sum=np.sum(raw), frobenius_squared_J=fro, full_lambda_squared_sum=np.sum(raw*raw), lambda_min=raw[0], lambda_max=raw[-1])
    for key, value in fields.items(): close(value, record[key], 'finite_moments:'+label+':'+key)
    errors = {'symmetry': (np.max(np.abs(matrix-matrix.T)), 1e-10*max(1., float(np.max(np.abs(matrix))))),
              'retained_state_matrix_equation': (np.max(np.abs(delta)), 1e-10*max(1., float(np.max(np.abs(action))), float(np.max(np.abs(states*raw[:count]))))),
              'retained_state_orthogonality': (np.max(np.abs(orth)), 1e-10),
              'full_trace': (abs(trace-np.sum(raw)), 1e-10*max(1., abs(trace))),
              'full_squared_trace': (abs(fro-np.sum(raw*raw)), 1e-10*max(1., fro))}
    for key, (error, tolerance) in errors.items(): check_gate(record['checks'][key], float(error), tolerance, label+':'+key)
    verify(record['passed'] and record['same_call_states'] and record['extra_state_eigh_calls'] == 0, 'finite_record:'+label)
    maxima['finite_equation_absolute'] = max(maxima['finite_equation_absolute'], float(np.max(np.abs(delta))))
    maxima['orthogonality_max'] = max(maxima['orthogonality_max'], float(np.max(np.abs(orth))))
    maxima['trace_relative'] = max(maxima['trace_relative'], float(abs(trace-np.sum(raw))/max(1., abs(trace))))
    maxima['second_moment_relative'] = max(maxima['second_moment_relative'], float(abs(fro-np.sum(raw*raw))/max(1., fro)))


def inspect_object(spec, truth, preceding):
    name, n, h, kappa, rho = spec; small = name.startswith('control-'); record = read(name+'.json')
    with np.load(RUN/(name+'-factors.npz'), allow_pickle=False) as z: saved_f = {key:z[key] for key in z.files}
    expected_f = factors(h, n, rho)
    for key, value in expected_f.items(): close(value, saved_f[key], 'factor:'+name+':'+key)
    for key, value in [('n', n), ('h', h), ('kappa', kappa), ('rho', rho), ('theta', [h, kappa]), ('hermite_width_b', rho*h), ('action_output_axis_dimension', n+4)]:
        close(saved_f[key], value, 'factor_metadata:'+name+':'+key, atol=0, rtol=0)
    with np.load(RUN/(name+'.npz'), allow_pickle=False) as z: a = {key:z[key] for key in z.files}
    for key, value in [('n', n), ('dimension', n*n), ('h', h), ('kappa', kappa), ('rho', rho), ('theta', [h, kappa])]:
        close(a[key], value, 'object_metadata:'+name+':'+key, atol=0, rtol=0)
        close(record[key], value, 'record_metadata:'+name+':'+key, atol=0, rtol=0)
    verify(record['primary'] == (name == PRIMARY) and record['small_control'] == small, 'primary_control_identity:'+name)
    even, odd = np.arange(0, n, 2), np.arange(1, n, 2)
    cross = max(float(np.max(np.abs(saved_f[key][np.ix_(even, odd)]))) for key in ('H0', 'Y2'))
    check_gate(record['checks']['one_dimensional_parity_cross_zero'], cross, 1e-10*max(1., float(np.max(np.abs(saved_f['H0']))), float(np.max(np.abs(saved_f['Y2'])))), name+':parity_cross')
    reference = None
    if small:
        with np.load(RUN/(name+'-full.npz'), allow_pickle=False) as z: full = {key:z[key] for key in z.files}
        full_record = read(name+'-full.json'); finite_check(full, full_record, name+':full')
        reference = full['matrix_S']; matrix_match(reference, matrix_from_factors(expected_f, kappa, np.arange(n)), name+':full')
    elif name == 'bridge-n52':
        with np.load(OLD/'post-n52.npz', allow_pickle=False) as old:
            reference, old_raw, old_pred = old['matrix_S'].copy(), old['lambda_raw'].copy(), old['predicted_320'].copy()
            close(old['theta'], [h, kappa], 'bridge_old_theta', atol=0, rtol=0)
    blocks, traces, moments = [], [], []; block_difference = 0.
    for parity in (0, 1):
        partname = name+f'-parity{parity}'
        with np.load(RUN/(partname+'.npz'), allow_pickle=False) as z: part = {key:z[key] for key in z.files}
        part_record = read(partname+'.json'); finite_check(part, part_record, partname)
        y = np.arange(parity, n, 2); indices = (np.arange(n)[:, None]*n+y[None, :]).ravel()
        verify(np.array_equal(part['y_degrees'], y) and np.array_equal(part['global_basis_indices'], indices) and int(part['parity']) == parity, 'parity_labels:'+partname)
        for key, value in [('theta', [h, kappa]), ('n', n), ('h', h), ('kappa', kappa), ('rho', rho)]: close(part[key], value, 'block_metadata:'+partname+':'+key, atol=0, rtol=0)
        matrix_match(part['matrix_S'], matrix_from_factors(expected_f, kappa, y), partname)
        if reference is not None:
            difference = float(np.max(np.abs(part['matrix_S']-reference[np.ix_(indices, indices)])))
            block_difference = max(block_difference, difference)
            check_gate(record['checks'][f'parity{parity}_reference_matrix'], difference, 1e-10*max(1., float(np.max(np.abs(reference)))), partname+':reference')
        verify(part_record == record['block_records'][parity], 'block_record_copy:'+partname)
        traces.append(part_record['trace_J']); moments.append(part_record['frobenius_squared_J'])
        del part['matrix_S']; blocks.append(part)
    if reference is not None:
        cross = float(np.max(np.abs(reference[np.ix_(blocks[0]['global_basis_indices'], blocks[1]['global_basis_indices'])])))
        tolerance = 1e-10*max(1., float(np.max(np.abs(reference))))
        check_gate(record['checks']['reference_cross_block_zero'], cross, tolerance, name+':reference_cross')
        check_gate(record['checks']['block_reconstruction'], max(cross, block_difference), tolerance, name+':block_reconstruction')
    concat = np.concatenate([p['lambda_raw'] for p in blocks])
    parity_tags = np.concatenate([np.full(len(p['lambda_raw']), i, dtype=int) for i, p in enumerate(blocks)])
    local = np.concatenate([np.arange(len(p['lambda_raw'])) for p in blocks]); order = np.lexsort((local, parity_tags, concat))
    raw, tags, locals_ = concat[order], parity_tags[order], local[order]
    for key, value in [('lambda_raw', raw), ('global_concat_index', order), ('global_parity', tags), ('global_local_index', locals_), ('block0_lambda_raw', blocks[0]['lambda_raw']), ('block1_lambda_raw', blocks[1]['lambda_raw'])]:
        close(value, a[key], 'exact_merge:'+name+':'+key, atol=0, rtol=0)
    verify(len(raw) == n*n and raw[0] > 0 and np.all(np.isfinite(raw)) and np.all(np.diff(raw) >= 0), 'global_spectrum:'+name)
    count = min(320, n*n); states, projected = np.zeros((n*n, count)), np.empty(count)
    for j in range(count):
        part = blocks[int(tags[j])]; index = int(locals_[j])
        verify(index < part['states'].shape[1], 'available_same_call_state:'+name)
        states[part['global_basis_indices'], j] = part['states'][:, index]; projected[j] = part['eigenvector_residual'][index]
    close(states, a['states'], 'exact_state_embedding:'+name, atol=0, rtol=0)
    close(projected, a['projected_block_residual'], 'projected_residual:'+name, atol=0, rtol=0)
    for key, value in [('full_lambda_sum', np.sum(raw)), ('full_lambda_squared_sum', np.sum(raw*raw)), ('block_trace_sum', sum(traces)), ('block_frobenius_squared_sum', sum(moments))]: close(value, record[key], 'merged_moment:'+name+':'+key)
    energy, prediction, raw_prediction = raw**1.5, truth[0]*(raw[:320]/raw[0])**1.5, truth[0]*raw[:320]/raw[0]
    for key, value in [('energy_power_3_2', energy), ('predicted_320', prediction), ('raw_J_predicted_320', raw_prediction), ('scale', truth[0]/energy[0]), ('raw_J_scale', truth[0]/raw[0]), ('target_320', truth)]: close(value, a[key], 'readout:'+name+':'+key, atol=0, rtol=0)
    verify(np.array_equal(np.isfinite(energy), a['finite_mask']) and np.array_equal(np.isfinite(raw), a['raw_J_finite_mask']) and np.all(np.isfinite(energy)), 'finite_masks:'+name)
    if small: check_gate(record['checks']['full_vs_merged_spectrum'], float(np.max(np.abs(raw-full['lambda_raw']))), 1e-10*max(1., float(np.max(np.abs(full['lambda_raw'])))), name+':full_merge')
    if kappa == 0:
        analytic = np.sort(np.asarray([2*h*(i+j+1) for i in range(n) for j in range(n)]))
        close(analytic, a['expected_lambda'], 'oscillator_reference:'+name, atol=0, rtol=0)
        check_gate(record['checks']['sourceoff_analytic_full_spectrum'], float(np.max(np.abs(raw-analytic))), 1e-10*max(1., float(np.max(np.abs(analytic)))), name+':oscillator')
    if name == 'bridge-n52':
        check_gate(record['checks']['old_n52_full_spectrum'], float(np.max(np.abs(raw-old_raw))), 1e-10*max(1., float(np.max(np.abs(old_raw)))), name+':old_spectrum')
        check_gate(record['checks']['old_n52_prediction'], float(100*np.max(np.abs(prediction-old_pred)/truth)), 1e-7, name+':old_prediction')
    previous_name = {'fine-n64':'bridge-n52', 'fine-n80':'fine-n64', 'fine-n96':'fine-n80'}.get(name)
    if previous_name:
        previous = preceding[previous_name]['lambda_raw']
        check_gate(record['checks']['same_width_nested_raw_Ritz'], float(np.max(raw[:len(previous)]-previous)), 1e-10*max(1., float(np.max(np.abs(previous))), float(np.max(np.abs(raw)))), name+':nested')
        verify(record['checks']['same_width_nested_raw_Ritz']['compared_count'] == len(previous), 'nested_count:'+name)
    continuous_check(name, n, h, kappa, rho, a, record, expected_f, saved_f, small)
    verify(record['passed'] and record['all_multiplicities_retained'] and record['global_merged_count'] == n*n and record['merge_order'] == ['lambda', 'parity', 'local_index'], 'object_record:'+name)
    return {key:a[key] for key in ('lambda_raw', 'energy_power_3_2', 'predicted_320', 'raw_J_predicted_320')}, record


def continuous_check(name, n, h, kappa, rho, a, record, independent, saved, small):
    states, raw = a['states'], a['lambda_raw']; count = states.shape[1]
    action = rectangular_action(independent, states, n, kappa)
    saved_action = a['continuous_residual_tensor'].copy(); saved_action[:n, :n] += states.reshape(n, n, count)*raw[:count]
    error = float(np.max(np.abs(action-saved_action)))/max(1., float(np.max(np.abs(saved_action))))
    verify(error < 1e-12, 'true_rectangular_action:'+name); maxima['tensor_action_relative'] = max(maxima['tensor_action_relative'], error)
    # Recompute exact saved-layout diagnostics from its saved residual tensor;
    # independent action above controls that tensor's mathematical origin.
    residual = a['continuous_residual_tensor']; norms = norm(states, axis=0)
    r2 = np.sum(residual*residual, axis=(0, 1))/norms**2
    ri2 = np.sum(residual[:n, :n]**2, axis=(0, 1))/norms**2
    ro2 = (np.sum(residual[n:, :]**2, axis=(0, 1))+np.sum(residual[:n, n:]**2, axis=(0, 1)))/norms**2
    r, rin, rout = np.sqrt(r2), np.sqrt(ri2), np.sqrt(ro2); high = (n+4)//5
    boundary = (np.arange(n)[:, None] >= n-high) | (np.arange(n)[None, :] >= n-high)
    edge = np.sum(states.reshape(n, n, count)[boundary]**2, axis=0)/norms**2
    values = {'state_norm':norms, 'continuous_residual':r, 'continuous_relative_residual':r/raw[:count], 'inside_residual':rin,
              'outside_leak':rout, 'continuous_residual_squared':r2, 'inside_residual_squared':ri2, 'outside_leak_squared':ro2,
              'truncation_edge_occupation':edge}
    for key, value in values.items(): close(value, a[key], 'continuous_diagnostic:'+name+':'+key, atol=2e-12, rtol=2e-12)
    verify(np.array_equal(boundary, a['truncation_edge_mask']), 'continuous_edge_union:'+name)
    diagnostics = record['continuous_diagnostics']; pyth = float(np.max(np.abs(r2-ri2-ro2))); ptol = 1e-10*max(1., float(np.max(r2)))
    projection = float(np.max(np.abs(rin-a['projected_block_residual']/norms))); projection_tol = 1e-10*max(1., float(np.max(np.abs(raw[:count]))))
    orth = float(np.max(np.abs(states.T@states-np.eye(count))))
    for key, value in [('global_orthogonality_max_difference', orth), ('pythagorean_max_difference', pyth), ('pythagorean_tolerance', ptol), ('inside_vs_block_residual_max_difference', projection), ('inside_vs_block_tolerance', projection_tol)]: close(value, diagnostics[key], 'continuous_identity_record:'+name+':'+key)
    verify(orth <= 1e-10 and pyth <= ptol and projection <= projection_tol and diagnostics['algebra_checks_passed'], 'continuous_identities:'+name)
    maxima['pythagorean_relative'] = max(maxima['pythagorean_relative'], pyth/max(1., float(np.max(r2))))
    for label, values_ in [('residual', r), ('relative_residual', r/raw[:count]), ('inside_residual', rin), ('outside_leak', rout), ('edge_occupation', edge)]:
        prefixes = [(str(k), k) for k in (100, 320) if count >= k] or [('all_control_states', count)]
        for prefix, stop in prefixes:
            for key, value in [('mean', np.mean(values_[:stop])), ('max', np.max(values_[:stop]))]: close(value, diagnostics[label][prefix][key], 'residual_summary:'+name+':'+label+':'+prefix)
    verify(diagnostics['rounding_error_not_enclosed'] and diagnostics['not_an_index_or_normalized_320_certificate'] and diagnostics['not_a_K_vector_residual'] and diagnostics['continuous_residual_not_a_fit_or_rejection_gate'], 'residual_scope:'+name)
    if small:
        with np.load(RUN/(name+'-padded-reference.npz'), allow_pickle=False) as ref:
            matrix_match(ref['matrix_S'], matrix_from_factors(factors(h, n+4, rho), kappa, np.arange(n+4)), name+':padded_Gram')
            indices = (np.arange(n)[:, None]*(n+4)+np.arange(n)[None, :]).ravel(); embedded = np.zeros(((n+4)**2, count)); embedded[indices] = states
            verify(np.array_equal(indices, ref['embedding_indices']), 'padded_embedding_indices:'+name)
            close(embedded, ref['embedded_states'], 'padded_embedding:'+name, atol=0, rtol=0)
            reference_action = ref['matrix_S']@embedded
            close(reference_action, ref['reference_action'], 'padded_reference_action:'+name)
            close(saved_action.reshape((n+4)**2, count), ref['tensor_action'], 'saved_tensor_action:'+name)
            close(action.reshape((n+4)**2, count), reference_action, 'independent_padded_action:'+name)
            # Hard-control scalar used the actual saved tensor before subtraction.
            error = float(np.max(np.abs(ref['tensor_action']-reference_action))); tol = 1e-10*max(1., float(np.max(np.abs(reference_action))))
            check_gate(record['checks']['true_tensor_action_vs_independent_padded_Gram'], error, tol, name+':padded_action')
            if kappa == 0: check_gate(record['checks']['sourceoff_zero_leak'], float(np.max(rout)), tol, name+':zero_leak')


def metrics(pred, target):
    error = np.abs(pred-target)
    return dict(count=len(target), mape_percent=float(100*np.mean(error/target)), max_percent_error=float(100*np.max(error/target)), rmse=float(np.sqrt(np.mean((pred-target)**2))), max_absolute_error=float(np.max(error)))


def main():
    result, manifest, identity = read('result.json'), read('manifest.json'), read('fixed-identity.json')
    truth = np.asarray(read('known-targets.json')['ordinates'])
    verify(result['status'] == 'completed' and result['primary'] == PRIMARY and tuple(result['fixed_theta']) == THETA, 'completed_fixed_identity')
    verify(result['resource_monitor_closed'] and result['resource_monitor_failure'] is None, 'monitor_completion_record')
    verify(manifest['monitor_regression']['passed'] and read('pure-interface-tests.json')['monitor']['passed'], 'monitor_pure_test_record')
    verify(truth.shape == (320,) and np.all(np.isfinite(truth)) and np.all(np.diff(truth) > 0), 'targets')
    for name in ('known-targets.json', 'external-history-comparator.json'):
        verify((RUN/name).read_bytes() == (OLD/name).read_bytes(), 'old_copy:'+name)
    verify((RUN/'source-winners-frozen.json').read_bytes() == (OLD/'winners-frozen.json').read_bytes(), 'old_identity_copy')
    oldwinner = json.loads((OLD/'winners-frozen.json').read_text())['winner']
    verify(oldwinner['evaluation_id'] == identity['source_evaluation_id'] == 'CS14-HENON-PULLBACK-OSCILLATOR-0028' and tuple(identity['theta']) == THETA, 'source_winner')
    verify(identity['primary'] == PRIMARY and identity['primary_n'] == 96 and identity['primary_rho'] == 1. and identity['no_search_or_reselection'] and not identity['science_started'] and not identity['target_scoring_started'], 'primary_prefrozen')
    verify(identity['source_CS14_joint_score'] == result['historical_CS14_joint_score'] == oldwinner['joint_score'] == 1.8560562377080405 and not identity['source_CS14_joint_gate_passed'] and result['historical_CS14_joint_failure_not_revised'], 'old_failure_retained')
    plan = read('object-plan.json')
    verify(plan['primary'] == PRIMARY and [(row['name'], row['n'], row['h'], row['kappa'], row['rho']) for row in plan['objects']] == SPECS, 'frozen_object_plan')
    members, records = {}, {}
    for spec in SPECS:
        name = spec[0]
        arrays, record = inspect_object(spec, truth, members)
        records[name] = record
        if not name.startswith('control-'): members[name] = arrays
        print('OBJECT_AUDITED', name, flush=True)
    verify(result['objects'] == records and result['controls'] == {name:row for name, row in records.items() if row['small_control']}, 'all_record_copies')
    fits, comparisons, nesting = read('fit-metrics.json'), read('comparisons.json'), read('nested-Ritz-controls.json')
    verify(set(fits) == set(members) and fits == result['fit_metrics'] and comparisons == result['comparisons'] and nesting == result['nested_Ritz_controls'], 'result_metric_copies')
    for name, values in fits.items():
        for readout, (key, _) in READOUTS.items():
            for window, (start, end) in WINDOWS.items():
                for metric, value in metrics(members[name][key][start:end], truth[start:end]).items():
                    close(value, values[readout][window][metric], 'fit:'+name+':'+readout+':'+window+':'+metric, atol=0, rtol=0)
    pairs = [('n52-n64', 'bridge-n52', 'fine-n64'), ('n64-n80', 'fine-n64', 'fine-n80'), ('n80-n96', 'fine-n80', 'fine-n96'), ('width080', PRIMARY, 'width080-n96'), ('width125', PRIMARY, 'width125-n96')]
    verify(set(comparisons) == {row[0] for row in pairs}, 'comparison_coverage')
    for label, left, right in pairs:
        a, b = members[left], members[right]
        for readout, (predkey, energykey) in READOUTS.items():
            row = comparisons[label][readout]
            verify(row['left'] == left and row['right'] == right and row['readout'] == readout and row['G_threshold_percent'] == 2., 'comparison_owner:'+label+':'+readout)
            for window, (start, end) in WINDOWS.items():
                gap = float(100*np.max(np.abs(a[predkey][start:end]-b[predkey][start:end])/truth[start:end]))
                energy = float(100*np.max(np.abs(a[energykey][start:end]-b[energykey][start:end])/a[energykey][start:end]))
                rawdiff = float(np.max(np.abs(a['lambda_raw'][start:end]-b['lambda_raw'][start:end])))
                for key, value in [('G_percent', gap), ('unscaled_energy_max_relative_percent', energy), ('raw_lambda_max_absolute_difference', rawdiff)]: close(value, row['windows'][window][key], 'comparison:'+label+':'+readout+':'+window+':'+key, atol=0, rtol=0)
                verify((gap < 2) == row['windows'][window]['G_below_threshold'], 'comparison_gate:'+label+':'+readout+':'+window)
                for key in ('mape_percent', 'max_percent_error'): close(fits[right][readout][window][key]-fits[left][readout][window][key], row['right_minus_left_fit_percentage_points'][window][key], 'comparison_shift:'+label+':'+readout+':'+window+':'+key, atol=0, rtol=0)
        if label.startswith('n'):
            x, y = a['lambda_raw'], b['lambda_raw']; increase = float(np.max(y[:len(x)]-x))
            tolerance = 1e-10*max(1., float(np.max(np.abs(x))), float(np.max(np.abs(y))))
            close(increase, nesting[label]['max_raw_lambda_increase'], 'nesting_increase:'+label, atol=0, rtol=0)
            close(tolerance, nesting[label]['tolerance'], 'nesting_tolerance:'+label, atol=0, rtol=0)
            verify(increase <= tolerance and nesting[label]['passed'] and nesting[label]['compared_count'] == len(x) and nesting[label]['left'] == left and nesting[label]['right'] == right, 'whole_prefix_nesting:'+label)
    external = read('external-history-comparator.json')
    for window, (start, end) in WINDOWS.items():
        for metric, value in metrics(np.asarray(external['predicted_320'])[start:end], truth[start:end]).items(): close(value, external['fit_metrics'][window][metric], 'historical_metric:'+window+':'+metric, atol=0, rtol=0)
    close(external['fit_metrics']['1-320']['mape_percent'], 3.5251249515592384, 'external_full320', atol=1e-10, rtol=0)
    verify(not external['raw_spectrum_comparison_permitted'], 'distinct_external_owner')
    assessment = read('finite-stability-assessment.json')
    stability = {label: all(v['G_below_threshold'] for v in comparisons[label]['power_3_2']['windows'].values()) for label in ('n64-n80', 'n80-n96', 'width080', 'width125')}
    stable = all(stability.values()); main_m = fits[PRIMARY]['power_3_2']['1-320']['mape_percent']
    verify(assessment == result['finite_stability_assessment'] and assessment['stability_checks'] == stability and assessment['all_four_window_G_below_2_percent'] == stable, 'assessment_stability')
    verify(assessment['status'] == ('ADVANCE_FINITE_FIXED_PARAMETER_STABILITY_ONLY' if stable else 'STOP_FORK_FINITE_STABILITY_GATE_FAILED'), 'assessment_status')
    verify(assessment['primary_predeclared'] == PRIMARY and assessment['primary_rho_not_reselected'] and assessment['old_CS14_joint_gate_remains_failed'] and assessment['raw_J_does_not_reselect'] and assessment['continuous_index_accuracy_not_certified'], 'assessment_scope')
    close(main_m, assessment['primary_full320_M'], 'assessment_fit', atol=0, rtol=0)
    verify(assessment['primary_full320_M_below_external_reference'] == (main_m < 3.5251249515592384), 'assessment_historical_comparison')
    csv_counts = inspect_csv(truth, members, records, fits, comparisons)
    hash_summary = inspect_hashes(manifest, identity)
    events = [json.loads(line) for line in (RUN/'events.jsonl').read_text().splitlines()]; names = [row['event'] for row in events]
    verify(names[0] == 'fixed_identity_frozen' and names.index('fixed_identity_frozen') < names.index('known_reference_read_start') < names.index('object_start') and names[-1] == 'completed' and 'failed' not in names, 'identity_before_science_and_score')
    verify([e['name'] for e in events if e['event'] == 'object_start'] == [s[0] for s in SPECS] == [e['name'] for e in events if e['event'] == 'object_completed'], 'execution_object_order')
    counter = result['counters']
    for base, count in [('objects', 10), ('physical_eigh', 24), ('fullspace_eigh', 4), ('parity_eigh', 20), ('continuous_actions', 10), ('small_padded_reference_assemblies', 4)]: verify(counter[base+'_attempted'] == counter[base+'_completed'] == count, 'science_counts:'+base)
    verify(names.count('physical_eigh_start') == names.count('physical_eigh_complete') == 24 and names.count('continuous_action_start') == 10, 'event_science_count')
    for kind, count in [('fullspace', 4), ('parity', 20)]: verify(sum(e['event'] == 'physical_eigh_complete' and e['kind'] == kind for e in events) == count, 'event_decomposition_kind:'+kind)
    for key, count in [('objects_saved', 10), ('fullspace_arrays_saved', 4), ('parity_arrays_saved', 20), ('factor_arrays_saved', 10)]: verify(counter[key] == count, 'saved_counts:'+key)
    verify(all(counter[key] == 0 for key in ('svd_calls', 'root_calls', 'quadrature_calls', 'optimization_calls', 'extra_state_eigh_calls', 'new_target_generations')), 'zero_extra_science')
    verify(len(list(RUN.glob('*.npz'))) == 48, 'npz_count')
    summary = dict(status='ANALYZED' if not failures else 'ISSUES_FOUND', failures=failures, checks=dict(checks),
                   maximum_recomputation_differences=maximum_differences, residual_maxima=maxima,
                   saved_objects=10, parity_spectra_and_state_sets=20, small_full_spectra_and_state_sets=4,
                   merged_spectra_and_state_sets=10, factor_archives=10, padded_reference_archives=4, all_npz=48,
                   fitted_objects=6, fit_windows=48, comparison_windows=40, csv_rows=csv_counts,
                   hash_coverage=hash_summary, counters=counter, assessment=assessment,
                   primary_fit=fits[PRIMARY], primary_continuous_diagnostics=records[PRIMARY]['continuous_diagnostics'],
                   frozen_theta=THETA, checker_sha256=sha(Path(__file__)),
                   scope='Saved-array algebra only; no eig/SVD/optimization/root/integration/propagation/runner import or new target.',
                   residual_scope='Observed extended-basis S residual, no rounding enclosure, index certificate or K-vector residual.')
    print(json.dumps(summary, ensure_ascii=False, indent=2, allow_nan=False))
    if failures: raise SystemExit(1)


def inspect_csv(truth, members, records, fits, comparisons):
    counts, seen = Counter(), set()
    with (RUN/'points.csv').open(newline='') as stream:
        for row in csv.DictReader(stream):
            name, readout, index = row['object_id'], row['readout'], int(row['index'])-1
            predkey, energykey = READOUTS[readout]; a = members[name]
            pred, target = a[predkey][index], truth[index]
            for key, value in [('target', target), ('predicted', pred), ('energy', a[energykey][index]), ('lambda_raw', a['lambda_raw'][index]), ('residual', pred-target), ('percent_error', 100*abs(pred-target)/target)]: close(float(row[key]), value, 'csv_point:'+key, atol=0, rtol=0)
            for key in ('n', 'h', 'kappa', 'rho'): close(float(row[key]), records[name][key], 'csv_metadata:'+key, atol=0, rtol=0)
            verify(row['window'] == ('1-100' if index < 100 else '101-300' if index < 300 else '301-320'), 'csv_window')
            key = (name, readout, index); verify(key not in seen, 'csv_point_unique'); seen.add(key); counts['points'] += 1
    verify(seen == {(name, readout, j) for name in members for readout in READOUTS for j in range(320)}, 'csv_point_coverage')
    seen = set()
    with (RUN/'fit-rows.csv').open(newline='') as stream:
        for row in csv.DictReader(stream):
            name, readout, window = row['object_id'], row['readout'], row['window']
            for key, value in fits[name][readout][window].items(): close(float(row[key]), value, 'csv_fit:'+key, atol=0, rtol=0)
            key = (name, readout, window); verify(key not in seen, 'csv_fit_unique'); seen.add(key); counts['fits'] += 1
    verify(seen == {(name, readout, window) for name in members for readout in READOUTS for window in WINDOWS}, 'csv_fit_coverage')
    seen = set()
    with (RUN/'comparison-rows.csv').open(newline='') as stream:
        for row in csv.DictReader(stream):
            label, readout, window = row['comparison'], row['readout'], row['window']; saved = comparisons[label][readout]
            verify(row['left'] == saved['left'] and row['right'] == saved['right'] and row['G_below_2_percent'] == str(saved['windows'][window]['G_below_threshold']), 'csv_comparison_metadata')
            for key in ('G_percent', 'unscaled_energy_max_relative_percent', 'raw_lambda_max_absolute_difference'): close(float(row[key]), saved['windows'][window][key], 'csv_comparison:'+key, atol=0, rtol=0)
            for key, label_ in [('mape_percent', 'right_minus_left_M'), ('max_percent_error', 'right_minus_left_W')]: close(float(row[label_]), saved['right_minus_left_fit_percentage_points'][window][key], 'csv_shift:'+key, atol=0, rtol=0)
            key = (label, readout, window); verify(key not in seen, 'csv_comparison_unique'); seen.add(key); counts['comparisons'] += 1
    verify(seen == {(label, readout, window) for label in comparisons for readout in READOUTS for window in WINDOWS}, 'csv_comparison_coverage')
    seen = set(); expected = set()
    for name, record in records.items():
        for diagnostic in ('residual', 'relative_residual', 'inside_residual', 'outside_leak', 'edge_occupation'):
            expected.update((name, prefix, diagnostic) for prefix in record['continuous_diagnostics'][diagnostic])
    with (RUN/'continuous-residual-summary.csv').open(newline='') as stream:
        for row in csv.DictReader(stream):
            name, prefix, diagnostic = row['object_id'], row['prefix'], row['diagnostic']
            for key in ('mean', 'max'): close(float(row[key]), records[name]['continuous_diagnostics'][diagnostic][prefix][key], 'csv_residual:'+key, atol=0, rtol=0)
            key = (name, prefix, diagnostic); verify(key not in seen, 'csv_residual_unique'); seen.add(key); counts['residuals'] += 1
    verify(seen == expected, 'csv_residual_coverage')
    return dict(counts)


def inspect_hashes(manifest, identity):
    locks = json.loads((PACKAGE/'input-locks.json').read_text())
    verify(locks == manifest['inputs'] == identity['inputs'] and len(locks) == 16, 'input_set')
    for path, digest in locks.items(): verify(sha(ROOT/path) == digest, 'input_hash:'+path)
    verify(sha(PACKAGE/'input-locks.json') == manifest['input_locks_sha256'], 'input_lock_hash')
    verify(sha(PACKAGE/'run_audit.py') == manifest['script_sha256'] == identity['script_sha256'] == RUNNER_SHA, 'runner_hash')
    verify(sha(RUN/'fixed-identity.json') == manifest['fixed_identity_sha256'] == read('result.json')['fixed_identity_sha256'], 'fixed_identity_hash')
    verify(sha(OLD/'winners-frozen.json') == identity['source_identity_sha256'], 'source_identity_hash')
    old_inventory = json.loads((OLD/'file-inventory.json').read_text())['files']
    for path, row in old_inventory.items():
        verify(sha(OLD/path) == row['sha256'] and (OLD/path).stat().st_size == row['bytes'], 'old_science_inventory:'+path)
    old_files = [p for p in OLD.rglob('*') if p.is_file()]
    verify(set(old_inventory) == {str(p.relative_to(OLD)) for p in old_files if p.name != 'file-inventory.json'} and len(old_files) == 185, 'old_inventory_coverage')
    frozen = read('object-files-frozen.json'); covered = set()
    for name, entries in frozen['files_by_object'].items():
        for path, digest in entries.items(): verify(sha(RUN/path) == digest, 'object_frozen_hash:'+path); covered.add(path)
    verify(set(frozen['files_by_object']) == {spec[0] for spec in SPECS} and frozen['no_selection_or_reselection'] and frozen['fixed_identity_sha256'] == manifest['fixed_identity_sha256'], 'object_freeze_scope')
    verify({p.name for p in RUN.glob('*.npz')} <= covered, 'object_freeze_array_coverage')
    inventory = read('file-inventory.json')['files']
    for path, row in inventory.items():
        verify(sha(RUN/path) == row['sha256'] and (RUN/path).stat().st_size == row['bytes'], 'science_inventory:'+path)
    files = [p for p in RUN.rglob('*') if p.is_file()]
    verify(set(inventory) == {str(p.relative_to(RUN)) for p in files if p.name != 'file-inventory.json'}, 'science_inventory_coverage')
    return dict(input_hashes=len(locks), old_inventory_members=len(old_inventory), old_files_including_inventory=len(old_files),
                frozen_object_files=len(covered), scientific_inventory_members=len(inventory), scientific_files_including_inventory=len(files),
                scientific_bytes_including_inventory=sum(p.stat().st_size for p in files))


if __name__ == '__main__':
    main()
