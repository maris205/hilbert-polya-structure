"""Finite exact checks of the original q=1 degree 4 -> 5 jet extension.

This is not a Smith calculation or an all-degree/all-prime proof. It keeps
tau and never divides by tau or 3. All output is stdout; no files are written.
The original J formula is transcribed from the accepted actual-jet package.
"""

import importlib.util
import json
import math
from pathlib import Path
import sys
import time

import sympy as sp

TAU = sp.Symbol('tau')


def indices(n):
    return [(i, j) for i in range(2*n+1) for j in range(2*n+1)
            if n+i-j >= 0 and i+j >= n and i+2*j >= 2*n
            and i+j <= 3*n]


def rows(n):
    return [(r, a, b) for r in range(1, 5)
            for a in range(n) for b in range(n-a)]


def actual_jet(n):
    cols, names = indices(n), rows(n)
    matrix = sp.zeros(len(names), len(cols))
    for ci, (i, j) in enumerate(cols):
        powers = [(2*n-i, j, 1), (n+i-j, i, TAU),
                  (i+2*j-2*n, i+j-n, TAU),
                  (3*n-i-j, 2*n-i, 1)]
        for ri, (r, a, b) in enumerate(names):
            upow, vpow, center = powers[r-1]
            if upow == a and vpow >= b:
                matrix[ri, ci] = math.comb(vpow, b)*center**(vpow-b)
    return matrix, cols, names


def target_map(n):
    old, new = rows(n), rows(n+1)
    locate = {row: i for i, row in enumerate(new)}
    matrix = sp.zeros(len(new), len(old))
    for j, (r, a, b) in enumerate(old):
        matrix[locate[r, a+1, b], j] = TAU if r in (2, 3) else 1
        if a+b+2 < n+1:
            matrix[locate[r, a+1, b+1], j] = 1
    return matrix


def zero(matrix):
    return all(sp.expand(value) == 0 for value in matrix)


def combination(left, right, scalar):
    result = dict(left)
    for key, value in right.items():
        entry = sp.expand(result.get(key, 0)-scalar*value)
        if entry == 0:
            result.pop(key, None)
        else:
            result[key] = entry
    return result


def unit_reduce(original, vectors):
    """Exact local-unit cancellations, with source certificates for vectors."""
    mat = [dict((j, value) for j, value in enumerate(original.row(i)) if value)
           for i in range(original.rows)]
    available_cols = list(range(original.cols))
    available_rows = list(range(original.rows))
    # The current source columns, expressed in the original source basis.
    source = {j: {j: sp.Integer(1)} for j in available_cols}
    reduced_vectors = [[v[i, 0] for i in available_rows] for v in vectors]
    certificates = [dict() for _ in vectors]
    pivots = []
    while True:
        pivot = None
        for i, row in enumerate(mat):
            for j in available_cols:
                entry = row.get(j, 0)
                if entry != 0 and entry.is_Rational and int(entry.p) % 3:
                    assert int(entry.q) % 3
                    pivot = i, j, entry
                    break
            if pivot is not None:
                break
        if pivot is None:
            break
        i, j, entry = pivot
        pivot_row, pivot_source = mat[i], source[j]
        for vi, values in enumerate(reduced_vectors):
            scalar = sp.cancel(values[i]/entry)
            certificates[vi] = combination(certificates[vi], pivot_source, -scalar)
            for r, row in enumerate(mat):
                if r != i and row.get(j, 0):
                    values[r] = sp.expand(values[r]-row[j]*scalar)
            values.pop(i)
        for c in available_cols:
            if c != j and pivot_row.get(c, 0):
                source[c] = combination(source[c], pivot_source,
                                        sp.cancel(pivot_row[c]/entry))
        for r, row in enumerate(mat):
            if r != i:
                if row.get(j, 0):
                    mat[r] = combination(row, pivot_row, sp.cancel(row[j]/entry))
                mat[r].pop(j, None)
        mat.pop(i)
        pivots.append(str(entry))
        available_rows.pop(i)
        available_cols.remove(j)
        source.pop(j)
    result = sp.Matrix([[row.get(j, 0) for j in available_cols] for row in mat])
    embedding = sp.zeros(original.rows, len(available_rows))
    for j, row in enumerate(available_rows):
        embedding[row, j] = 1
    domain = sp.zeros(original.cols, len(available_cols))
    for j, col in enumerate(available_cols):
        for row, value in source[col].items():
            domain[row, j] = value
    assert zero(original*domain-embedding*result)
    for original_vector, values, certificate in zip(vectors, reduced_vectors, certificates):
        cert = sp.zeros(original.cols, 1)
        for row, value in certificate.items():
            cert[row, 0] = value
        assert zero(original_vector-embedding*sp.Matrix(values)-original*cert)
    return result, reduced_vectors, available_rows, pivots


def entries(matrix):
    return [[i, j, str(sp.factor(matrix[i, j]))]
            for i in range(matrix.rows) for j in range(matrix.cols) if matrix[i, j]]


def main():
    started = time.monotonic()
    j4, cols4, rows4 = actual_jet(4)
    j5, cols5, rows5 = actual_jet(5)
    sys.dont_write_bytecode = True
    old_path = Path(__file__).with_name('qpi_nonunit_tau_jets_diagnostic_v1_20260909.py')
    spec = importlib.util.spec_from_file_location('original_eight_jet_check', old_path)
    old_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(old_module)
    for n, actual, columns, names in [(4, j4, cols4, rows4), (5, j5, cols5, rows5)]:
        eight, eight_columns, eight_names = old_module.jet_matrix(n, TAU, sp.Integer(1))
        row_lookup = {label: i for i, label in enumerate(eight_names)}
        col_lookup = {label: i for i, label in enumerate(eight_columns)}
        charts = {1: 'c1', 2: 'c2b', 3: 'c3c', 4: 'c4b'}
        selected = eight.extract([row_lookup[charts[r], a, b] for r, a, b in names],
                                 [col_lookup[label] for label in columns])
        assert zero(actual-selected)
    mu = target_map(4)
    shift = sp.zeros(len(cols5), len(cols4))
    locate5 = {col: i for i, col in enumerate(cols5)}
    for i, (x, y) in enumerate(cols4):
        shift[locate5[x+1, y+1], i] = 1
    assert zero(j5*shift-mu*j4)
    old_rows = {row: i for i, row in enumerate(rows4)}
    new_rows = {row: i for i, row in enumerate(rows5)}
    vectors, labels = [], []
    for r in (2, 3):
        for a in range(1, 5):
            m = 5-a
            h = sp.zeros(len(rows4), 1)
            for b in range(m):
                h[old_rows[r, a-1, b], 0] = (-1)**b*TAU**(m-1-b)
            target = sp.zeros(len(rows5), 1)
            target[new_rows[r, a, 0], 0] = TAU**m
            assert zero(target-mu*h)
            vectors.append(h)
            labels.append({'chart': r, 'u_power': a, 'annihilator_power': m})
    reduced, image_vectors, kept_rows, pivots = unit_reduce(j4, vectors)
    pure_columns = []
    for r, monomial in [(2, (2, 5)), (3, (3, 3))]:
        h = sp.zeros(len(rows4), 1)
        h[old_rows[r, 1, 0], 0] = TAU**2
        h[old_rows[r, 1, 1], 0] = -TAU
        h[old_rows[r, 1, 2], 0] = 1
        uv = sp.zeros(len(rows4), 1)
        uv[old_rows[r, 1, 1], 0] = 1
        column = j4[:, cols4.index(monomial)]
        assert zero(h+3*TAU*uv-column)
        pure_columns.append({'chart': r, 'source_monomial': list(monomial),
                             'identity': 'h + 3*tau*[u*v]_r = J4(source_monomial)',
                             'all_original_rows': 'PASS_EXACT'})
    output = {
        'evidence': 'FINITE_EXACT_INTEGER_LOCAL_MODULE_CERTIFICATES',
        'ring': 'Z_(3)[tau]; maps valid after localization at (3,tau)',
        'fixed_case': 'q=1, degree 4 -> 5',
        'sympy_version': sp.__version__,
        'J4_shape': list(j4.shape), 'J5_shape': list(j5.shape),
        'original_eight_jet_transcription_n4_n5': 'PASS_EXACT',
        'chain_map_identity': 'PASS_EXACT',
        'eight_extension_lift_identities': 'PASS_EXACT',
        'J4_local_unit_pivots': len(pivots),
        'pivot_values': sorted(set(pivots)),
        'reduced_J4_shape': list(reduced.shape),
        'reduced_target_original_rows': [rows4[i] for i in kept_rows],
        'reduced_J4_entries': entries(reduced),
        'extension_classes': [dict(label, reduced_representative=[str(sp.factor(x)) for x in vector])
                              for label, vector in zip(labels, image_vectors)],
        'two_original_pure_column_certificates': pure_columns,
        'source_and_vector_certificates': 'PASS_EXACT',
        'limits': ['not Smith data', 'no tau or 3 inverted',
                   'does not prove an all-prime or all-degree classification',
                   'extension classes retain the specified original generators'],
        'elapsed_seconds': round(time.monotonic()-started, 6),
    }
    print(json.dumps(output, ensure_ascii=False, indent=2), flush=True)


if __name__ == '__main__':
    main()
