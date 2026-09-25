#!/usr/bin/env python3
"""Read-only CS10 saved-data audit. No propagation, root search or decomposition.

Writes nothing; prints a JSON summary. Does not import any scientific runner.
DST is used solely to check saved-state occupations and the saved static formula.
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
WINDOWS = {'1-100': (0, 100), '101-300': (100, 300),
           '301-320': (300, 320), '1-320': (0, 320)}
MREF, WREF = 1.695273790061038, 5.234299091683695
checks = Counter()
maxima = {}
failures = []


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
        error = float(np.max(np.abs(a[mask] - b[mask]))) if np.any(mask) else 0.
        key = label.split(':')[0]
        maxima[key] = max(maxima.get(key, 0.), error)


def norm(value):
    return float(np.sqrt(np.sum(np.abs(value) ** 2)))


def transform(value):
    out = dst(value.real, type=1, axis=0, norm='ortho', workers=1)
    if np.iscomplexobj(value):
        out = out + 1j * dst(value.imag, type=1, axis=0, norm='ortho', workers=1)
    return out


def metrics(prediction, target):
    error = prediction - target
    ratio = np.abs(error) / target
    return dict(count=len(target), mape_percent=float(100*np.mean(ratio)),
                max_percent_error=float(100*np.max(ratio)), mse=float(np.mean(error**2)),
                max_absolute_error=float(np.max(np.abs(error))),
                mean_absolute_spacing_error_in_target_gaps=float(
                    np.mean(np.abs(np.diff(prediction)-np.diff(target))/np.diff(target))))


def metric_check(pred, target, recorded, label):
    for key, value in metrics(pred, target).items():
        close(value, recorded[key], label + ':' + key)


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024*1024), b''):
            h.update(block)
    return h.hexdigest()


def occupation(states, q, length, a, prefix, label):
    boundary = np.sum(np.abs(states[np.abs(q) > .9*length])**2, axis=0)
    count = (len(q)+4)//5
    tail = np.sum(np.abs(transform(states)[-count:])**2, axis=0)
    close(boundary, a[prefix+'boundary_mass'], 'occupation:'+label+':boundary', atol=2e-12)
    close(tail, a[prefix+'high_momentum_mass'], 'occupation:'+label+':tail', atol=2e-12)


def compact(a):
    return dict(pred=a['predicted_320'].copy(), energy=a['energy'][:320].copy(),
                scale=float(a['scale']), valid=bool(a['resolution_valid']) if 'resolution_valid' in a else True)


def main():
    result = read('result.json')
    manifest = read('manifest.json')
    truth = np.asarray(read('known-targets.json')['ordinates'])
    members, training = {}, {}
    minima = read('minimum-ledger.json')
    full_heat, static_count, heat_count = 0, 0, 0
    residual_max = {'forward': 0., 'adjoint': 0., 'heat_orthogonality': 0.,
                    'heat_fro_relative': 0., 'static_equation': 0.,
                    'static_orthogonality': 0., 'static_hermitian': 0., 'static_owner_relative': 0.}
    files = sorted((RUN/'evaluations').glob('*-N*.npz')) + sorted(RUN.glob('*.npz'))
    for path in files:
        name = path.stem
        record = json.loads(path.with_suffix('.json').read_text())
        with np.load(path, allow_pickle=False) as a:
            n, length = int(a['grid_n']), float(a['L'])
            theta = a['theta']; h, ast, mass, z = theta[:4]
            close(theta, record['theta'], 'theta_record:'+name, atol=0, rtol=0)
            q, p, kinetic = a['q'], a['p'], a['kinetic_minus_mass']
            close(q, -length+2*length*np.arange(1, n+1)/(n+1), 'q:'+name)
            close(p, np.pi*h*np.arange(1, n+1)/(2*length), 'p:'+name)
            close(kinetic, p*p/(np.hypot(mass, p)+mass), 'kinetic:'+name)
            close(a['target_100'], truth[:100], 'target:'+name, atol=0, rtol=0)
            samples = int(a['sample_count'])
            u = (np.arange(samples)+.5)/samples
            w = (np.log(11+299*u)**-2-np.log(310.)**-2)/(np.log(11.)**-2-np.log(310.)**-2)
            close(a['schedule'], 1.02+(ast-1.02)*w, 'schedule:'+name, atol=2e-14)
            amplitude = theta[4] if len(theta) == 5 else 0.
            mode = str(a['phase_mode']) if 'phase_mode' in a else 'conjugated'
            chi = np.full(samples, amplitude) if mode == 'constant' else amplitude*np.sin(2*np.pi*u)
            close(a['chi'], chi, 'chi:'+name, atol=2e-14)
            if 'phase_diagonal_samples' in a:
                close(a['phase_diagonal_samples'], np.exp(1j*chi[:, None]*q[None, :]**2/(2*h)),
                      'phases:'+name, atol=2e-13)
            if 'sigma' in a:
                heat_count += 1
                sigma, energy = a['sigma'], a['energy']
                beta, repeats = float(a['beta']), int(a['repeats'])
                mask = np.isfinite(sigma) & (sigma > 0)
                expected_energy = np.full(n, np.nan)
                expected_energy[mask] = mass-np.log(sigma[mask])/beta
                mask &= np.isfinite(expected_energy)
                close(energy, expected_energy, 'energy:'+name, atol=0, rtol=0)
                verify(np.array_equal(mask, a['energy_resolved_mask']), 'mask:'+name)
                required = min(n, 320)
                valid = (0 < sigma[0] <= 1+1e-10 and np.all(mask[:required])
                         and np.all(np.diff(sigma[:required]) <= 0)
                         and (n < 320 or sigma[required-1]/sigma[0] >= 1e-10)
                         and energy[0] > 0 and np.all(energy[:required] >= mass-1e-8))
                verify(valid == bool(a['resolution_valid']) == record['resolution_valid'], 'valid:'+name)
                pred_key = 'predicted_320' if n >= 320 else 'predicted_control'
                close(a['scale'], truth[0]/energy[0], 'scale:'+name, atol=0, rtol=0)
                close(a[pred_key], float(a['scale'])*energy[:required], 'prediction:'+name, atol=0, rtol=0)
                if 'training_metrics' in record:
                    metric_check(a[pred_key][:100], truth[:100], record['training_metrics'], 'train_metrics:'+name)
                order = str(a['order_name'])
                indices = np.arange(samples)
                if order == 'P': indices = np.r_[indices[::2], indices[1::2]]
                if order == 'reverse': indices = indices[::-1]
                verify(np.array_equal(indices, a['sample_order_zero_based']), 'order:'+name)
                verify(np.array_equal(indices+1, a['sample_order_one_based']), 'order1:'+name)
                verify(np.array_equal(np.repeat(indices, repeats), a['fine_step_sample_indices_zero_based']), 'repeat:'+name)
                close(a['delta'], beta/(samples*repeats), 'delta:'+name, atol=0, rtol=0)
                if str(a['potential_mode']) != 'zero_control':
                    ids = a['minimum_ids']
                    verify(np.all((ids >= 0) & (ids < len(minima))), 'minimum_ids:'+name)
                    values = np.asarray([minima[int(i)]['minimum'] for i in ids])
                    close(a['minimum_values'], values, 'minimum_values:'+name, atol=0, rtol=0)
                    close(a['minimizers'], [minima[int(i)]['minimizer'] for i in ids], 'minimizers:'+name, atol=0, rtol=0)
                    close(a['schedule'], [minima[int(i)]['a'] for i in ids], 'minimum_schedule:'+name, atol=0, rtol=0)
                    close(np.full(samples, z), [minima[int(i)]['z'] for i in ids], 'minimum_z:'+name, atol=0, rtol=0)
                    unshifted = (-q+q*q+.05*q**4+z*q**5+.002*q**6)[None, :]+a['schedule'][:, None]*q[None, :]**3/3
                    shifted = unshifted-values[:, None]
                    verify(float(np.min(shifted)) >= -1e-10, 'Wnonnegative:'+name)
                    close(a['W_samples'], np.maximum(shifted, 0), 'W:'+name, atol=3e-10)
                else:
                    verify(not np.any(a['W_samples']), 'free_W:'+name)
                close(a['mean_W'], np.mean(a['W_samples'], axis=0), 'mean_W:'+name, atol=0, rtol=0)
                if 'C_tilde' in a:
                    full_heat += 1
                    c, left, right = a['C_tilde'], a['singular_left'], a['singular_right']
                    k = left.shape[1]
                    verify(c.shape == (n, n) and left.shape == right.shape == (n, required), 'heat_shapes:'+name)
                    verify(np.iscomplexobj(c) and np.iscomplexobj(left) and np.iscomplexobj(right), 'complex:'+name)
                    forward = np.sqrt(np.sum(np.abs(c@right-left*sigma[:k])**2, axis=0))
                    adjoint = np.sqrt(np.sum(np.abs(c.conj().T@left-right*sigma[:k])**2, axis=0))
                    close(forward, a['singular_forward_residual'], 'forward_saved:'+name, atol=2e-13)
                    close(adjoint, a['singular_adjoint_residual'], 'adjoint_saved:'+name, atol=2e-13)
                    close(forward/sigma[0], a['singular_forward_residual_over_sigma0'], 'forward_relative:'+name, atol=2e-13)
                    close(adjoint/sigma[0], a['singular_adjoint_residual_over_sigma0'], 'adjoint_relative:'+name, atol=2e-13)
                    lo, ro = norm(left.conj().T@left-np.eye(k)), norm(right.conj().T@right-np.eye(k))
                    fro, moment = np.sum(np.abs(c)**2), np.sum(sigma**2)
                    for key, val in [('matrix_frobenius_squared', fro), ('full_sigma_squared_sum', moment),
                                     ('left_orthogonality_fro', lo), ('right_orthogonality_fro', ro)]:
                        close(val, record[key], 'heat_record:'+name+':'+key)
                    residual_max['forward'] = max(residual_max['forward'], float(np.max(forward)))
                    residual_max['adjoint'] = max(residual_max['adjoint'], float(np.max(adjoint)))
                    residual_max['heat_orthogonality'] = max(residual_max['heat_orthogonality'], lo, ro)
                    residual_max['heat_fro_relative'] = max(residual_max['heat_fro_relative'], float(abs(fro-moment)/fro))
                    occupation(left, q, length, a, 'left_', name+':left')
                    occupation(right, q, length, a, 'right_', name+':right')
                if n >= 320:
                    if path.parent.name == 'evaluations': training[name] = compact(a)
                    else: members[name] = compact(a)
            else:
                static_count += 1
                matrix, energy, states = a['H_avg'], a['energy'], a['states']
                modes = transform(np.eye(n))
                expected = transform(kinetic[:, None]*modes)
                phases = a['phase_diagonal_samples']
                expected = expected*(phases.T@phases.conj()/samples)
                expected.flat[::n+1] += mass+a['mean_W']
                owner_error = norm(matrix-expected)/norm(matrix)
                verify(owner_error < 2e-13, 'static_owner:'+name)
                residual = np.sqrt(np.sum(np.abs(matrix@states-states*energy[:320])**2, axis=0))
                close(residual, a['equation_residual'], 'static_residual_saved:'+name, atol=2e-11)
                orth, herm = norm(states.conj().T@states-np.eye(320)), norm(matrix-matrix.conj().T)/norm(matrix)
                for key, val in [('equation_residual_max', np.max(residual)), ('orthogonality_fro', orth),
                                 ('hermiticity_relative_fro', herm)]:
                    close(val, record[key], 'static_record:'+name+':'+key)
                close(a['scale'], truth[0]/energy[0], 'static_scale:'+name, atol=0, rtol=0)
                close(a['predicted_320'], float(a['scale'])*energy[:320], 'static_prediction:'+name, atol=0, rtol=0)
                metric_check(a['predicted_320'][:100], truth[:100], record['training_metrics'], 'static_train:'+name)
                occupation(states, q, length, a, '', name)
                residual_max['static_equation'] = max(residual_max['static_equation'], float(np.max(residual)))
                residual_max['static_orthogonality'] = max(residual_max['static_orthogonality'], orth)
                residual_max['static_hermitian'] = max(residual_max['static_hermitian'], herm)
                residual_max['static_owner_relative'] = max(residual_max['static_owner_relative'], owner_error)
                members[name] = compact(a)
    print('ARRAY_AUDIT_COMPLETE', heat_count, full_heat, static_count, flush=True)
    oldpath = ROOT/'papers/259-hyperbolic-tail-heat-search/evidence/run-1/post-B-N1279.npz'
    with np.load(oldpath, allow_pickle=False) as a:
        members['old-B0055-N1279'] = compact(a)
    rows = read('unique-members.json')
    oldeval = ROOT/'papers/259-hyperbolic-tail-heat-search/evidence/run-1/evaluations'
    for n in (511, 639):
        with np.load(oldeval/f'CS09-B-QUINTIC-REFIT-0055-N{n}.npz', allow_pickle=False) as old:
            new = training[f'CS10-B-QUINTIC-REFIT-0001-N{n}']
            close(new['pred'], old['predicted_320'], 'baseline_prediction:'+str(n), atol=1e-6, rtol=0)
            before, after = metrics(old['predicted_320'][:100], truth[:100]), metrics(new['pred'][:100], truth[:100])
            for key in ('mape_percent','max_percent_error'):
                close(before[key], after[key], 'baseline_metrics:'+str(n)+':'+key, atol=1e-6, rtol=0)
    ranked = {}
    for row in rows:
        key = row['evaluation_id']
        aa, bb = training[key+'-N511'], training[key+'-N639']
        ma, mb = metrics(aa['pred'][:100], truth[:100]), metrics(bb['pred'][:100], truth[:100])
        g = float(100*np.max(np.abs(aa['pred'][:100]-bb['pred'][:100])/truth[:100]))
        j = max(ma['mape_percent']/MREF, mb['mape_percent']/MREF,
                ma['max_percent_error']/WREF, mb['max_percent_error']/WREF, g/2)
        for field, val in [('joint_score', j), ('cross_grid_percent', g),
                           ('max_mape_percent', max(ma['mape_percent'], mb['mape_percent'])),
                           ('max_percent_error', max(ma['max_percent_error'], mb['max_percent_error']))]:
            close(val, row[field], 'pair:'+key+':'+field)
        rank = (j, max(ma['mape_percent'], mb['mape_percent']), max(ma['max_percent_error'], mb['max_percent_error']), g, key)
        ranked.setdefault(row['form_key'], []).append(rank)
    for form, ranks in ranked.items():
        winner = min(ranks)[-1]
        verify(winner == result['roles'][form]['evaluation_id'], 'winner:'+form)
        for n in (511, 639):
            for key in ('pred', 'energy'):
                close(members[f'winner-{form}-N{n}'][key], training[f'{winner}-N{n}'][key], 'winner_array:'+form+':'+key, atol=0, rtol=0)
    verify(min((min(ranks), form) for form, ranks in ranked.items())[1] == result['global_joint_winner'], 'primary_rank')
    fits = read('development-fit-metrics.json')
    for name, saved in fits.items():
        for window, (start, stop) in WINDOWS.items():
            metric_check(members[name]['pred'][start:stop], truth[start:stop], saved[window], 'fit:'+name+':'+window)
    verify(fits == result['fit_metrics'], 'result_fits')
    comparisons = read('comparisons.json')
    for name, saved in comparisons.items():
        aa, bb = members[saved['left']], members[saved['right']]
        for window, (start, stop) in WINDOWS.items():
            g = float(100*np.max(np.abs(aa['pred'][start:stop]-bb['pred'][start:stop])/truth[start:stop]))
            e = float(100*np.max(np.abs(aa['energy'][start:stop]-bb['energy'][start:stop])/aa['energy'][start:stop]))
            close(g, saved['windows'][window]['G_percent'], 'comparison_G:'+name+':'+window)
            close(e, saved['windows'][window]['raw_energy_max_relative_percent'], 'comparison_E:'+name+':'+window)
            verify((g < 2) == saved['windows'][window]['G_below_2_percent'], 'comparison_gate:'+name+':'+window)
    mechanism = read('mechanism-comparisons.json'); computed = {}
    for name, saved in mechanism.items():
        aa, bb = members[saved['left']], members[saved['right']]
        computed[name] = {}
        for window, (start, stop) in WINDOWS.items():
            value = float(100*np.max(np.abs(aa['energy'][start:stop]-bb['energy'][start:stop])/aa['energy'][start:stop]))
            close(value, saved['windows'][window], 'mechanism:'+name+':'+window)
            computed[name][window] = value
    verdict = read('mechanism-verdict.json')
    for window in WINDOWS:
        delta = computed['order_r2'][window]
        epsilon = max(computed['O_refinement'][window], computed['P_refinement'][window])
        gate = max(1e-6, 10*epsilon)
        for field, val in [('Delta_percent', delta), ('epsilon_percent', epsilon), ('threshold_percent', gate)]:
            close(val, verdict[window][field], 'mechanism_gate:'+window+':'+field, atol=0, rtol=0)
        verify(verdict[window]['status'] == ('RESOLVED_ORDER_EFFECT' if delta > gate else 'UNRESOLVED'), 'mechanism_status:'+window)
    probe_keys = ['theta','q','p','kinetic_minus_mass','midpoint_u','schedule','chi','W_samples',
                  'mean_W','minimum_values','minimizers','phase_diagonal_samples']
    with np.load(RUN/'probe-O-r1.npz', allow_pickle=False) as ref:
        for name in ('probe-P-r1','probe-O-r2','probe-P-r2'):
            with np.load(RUN/(name+'.npz'), allow_pickle=False) as a:
                for key in probe_keys: verify(np.array_equal(ref[key], a[key]), 'probe_multiset:'+name+':'+key)
                verify(str(a['static_owner_id']) == 'static-probe-O-r1', 'probe_static_ref:'+name)
    csv_count, object_counts = 0, Counter()
    with (RUN/'points.csv').open(newline='') as stream:
        for row in csv.DictReader(stream):
            name, index = row['object_id'], int(row['index'])-1
            aa = members[name]; pred, energy, actual = aa['pred'][index], aa['energy'][index], truth[index]
            for key, value in [('target', actual), ('predicted', pred), ('energy', energy),
                               ('residual', pred-actual), ('percent_error', 100*abs(pred-actual)/actual)]:
                close(float(row[key]), value, 'csv:'+key, atol=0, rtol=0)
            verify(row['window'] == ('1-100' if index < 100 else '101-300' if index < 300 else '301-320'), 'csv_window')
            csv_count += 1; object_counts[name] += 1
    verify(set(object_counts) == set(members) and all(c == 320 for c in object_counts.values()), 'csv_coverage')
    controls = {}
    for i, kind in enumerate(('free','base','shear','constant','transport','reverse'), 1):
        with np.load(RUN/f'control-{i}-{kind}.npz', allow_pickle=False) as a:
            controls[kind] = {k:a[k] for k in ('C_tilde','sigma','energy','kinetic_minus_mass','phase_diagonal_samples','theta','beta')}
    free = controls['free']; beta = float(free['beta'])
    verify(np.max(np.abs(free['sigma']-np.exp(-beta*free['kinetic_minus_mass']))) <= 1e-10, 'control_free_sigma')
    verify(np.max(np.abs(free['energy']-(free['theta'][2]+free['kinetic_minus_mass']))) <= 1e-8, 'control_free_energy')
    for kind in ('constant', 'transport'):
        verify(np.max(np.abs(controls['base']['sigma']-controls[kind]['sigma'])) <= 1e-10, 'control_'+kind+'_spectrum')
    expected = controls['transport']['phase_diagonal_samples'][-1,:,None]*controls['base']['C_tilde']
    verify(norm(controls['transport']['C_tilde']-expected) <= 1e-10*max(1,norm(controls['base']['C_tilde'])), 'control_transport_matrix')
    verify(norm(controls['reverse']['C_tilde']-controls['shear']['C_tilde'].conj().T) <= 1e-10*max(1,norm(controls['shear']['C_tilde'])), 'control_reverse_matrix')
    verify(np.max(np.abs(controls['reverse']['sigma']-controls['shear']['sigma'])) <= 1e-10, 'control_reverse_spectrum')
    for row in minima:
        a,z = row['a'],row['z']; q=np.asarray(row['stationary_roots'])
        values=-q+q*q+a*q**3/3+.05*q**4+z*q**5+.002*q**6
        derivative=-1+2*q+a*q*q+.2*q**3+5*z*q**4+.012*q**5
        verify(np.max(np.abs(derivative)) <= 1e-9, 'saved_root_residual')
        close(values, row['stationary_values'], 'saved_root_values', atol=2e-11)
        close(np.min(values), row['minimum'], 'saved_root_minimum', atol=2e-11)
    for path, expected in manifest['inputs'].items(): verify(sha(ROOT/path) == expected, 'input_hash:'+path)
    verify(sha(PACKAGE/'run_search.py') == manifest['script_sha256'], 'runner_hash')
    verify(sha(PACKAGE/'input-locks.json') == manifest['input_locks_sha256'], 'locks_hash')
    freeze=read('training-arrays-frozen.json')
    for path, expected in freeze['files_sha256'].items(): verify(sha(RUN/path) == expected, 'frozen_hash:'+path)
    verify(sha(RUN/'winners-frozen.json') == freeze['winner_identity_sha256'], 'winner_identity_hash')
    inventory=read('file-inventory.json')['files']
    for name, item in inventory.items():
        verify((RUN/name).stat().st_size == item['bytes'], 'inventory_size:'+name)
        verify(sha(RUN/name) == item['sha256'], 'inventory_hash:'+name)
    events=[json.loads(line) for line in (RUN/'events.jsonl').read_text().splitlines()]
    names=[e['event'] for e in events]
    verify(names.index('winner_identities_frozen') < names.index('training_arrays_frozen') < names.index('development_reference_read_start'), 'freeze_order')
    calls=read('calls.json'); call_lines=[json.loads(line) for line in (RUN/'calls.jsonl').read_text().splitlines()]
    verify(calls == call_lines and len(calls)==54 and len(rows)==52, 'call_counts')
    verify(sum(bool(r['cached']) for r in calls)==2, 'cache_count')
    verify(result['counters']['propagations_completed']==120 and result['counters']['full_svd_completed']==120, 'prop_svd_counts')
    verify(heat_count==124 and full_heat==20 and static_count==11, 'array_coverage')
    verify(len(training)==104 and len(members)==26 and csv_count==8320, 'coverage_counts')
    verify(all(v < 5e-10 for v in residual_max.values()), 'residual_engineering_ceiling')
    summary = dict(status='ANALYZED' if not failures else 'ISSUES_FOUND', failures=failures,
                   checks=dict(checks), maximum_recomputation_differences=maxima,
                   heat_npz_including_4_duplicate_winners=heat_count, full_complex_C_records=full_heat,
                   static_records=static_count, training_pairs=len(rows), csv_rows=csv_count,
                   fitted_objects=len(members), fit_windows=len(fits)*4, comparison_windows=len(comparisons)*4,
                   mechanism_windows=len(mechanism)*4, minimum_records_checked=len(minima),
                   input_hashes=len(manifest['inputs']), inventory_files=len(inventory),
                   residual_maxima=residual_max, mechanism_verdict=verdict,
                   winners={k:{x:v[x] for x in ('evaluation_id','theta','joint_score','max_mape_percent','max_percent_error')}
                            for k,v in result['roles'].items()}, checker_sha256=sha(Path(__file__)),
                   scope='Saved-array algebra, metrics and hashes only; no rerun/decomposition/root search; no certified error bound')
    print(json.dumps(summary, ensure_ascii=False, indent=2, allow_nan=False))
    if failures: raise SystemExit(1)


if __name__ == '__main__':
    main()
