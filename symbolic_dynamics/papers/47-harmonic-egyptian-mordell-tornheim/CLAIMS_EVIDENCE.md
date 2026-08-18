# P47 claims--evidence matrix

Status: `CANONICAL STATE-A BOUND / INFINITE CLAIMS REMAIN PROOF-OWNED`.

This writer-side matrix is bound to the 91-node protected authority manifest
SHA-256 `30a79c4be4bc9b9333cb2a9f809d2039430cebc86686a054765734a782eea473`,
the State-A output tree SHA-256
`328527680d533e34ce3aabc17f2cf5688759b0674b7fc8740d0c2df332b64c42`,
and the writer canonical summary SHA-256
`45185ea8750dec4557b055f0381137076df5d1615c51c482fa96e623f8ed1d7f`.
It separates mathematical proof, finite implementation replay, and
governance evidence.

## Claim matrix

| ID | Exact claim | Analytic owner | Canonical State-A evidence observed | Status / forbidden inference |
|---|---|---|---|---|
| C1 | Ordered edges are in bijection with `t>=1`, coprime ordered `(a,b)`, through `m=t a(a+b)`, `n=t b(a+b)`; for fixed `m`, neighbors are independently in bijection with `d|m^2`, `d<m` | gcd reduction and divisor-row algebra in `PROOF_PACKAGE.md`, Steps 2--3 | D's remainder predicate and P's coprime triples/divisor rows agree for all declared cutoffs and all rows `m<=128`; X reports `coprime_coordinate_bijection`, `full_divisor_rows`, and support checks PASS | Exact implementation replay matched.  The elementary parameterizations receive no priority credit. |
| C2 | The coefficient array has a bounded realization on `ell^2(N)`, and that realization is compact, iff `Re(s)>0` | divisor-row Schur estimate and finite-rank approximation; even loops for `Re(s)<0`; unbounded squarefree row support at zero | the proof-result audit labels the wall `PROOF_ONLY_Re_s_gt_0`; P records the strict squarefree-degree witness | The infinite wall is established by the manuscript proof.  No finite singular value or cutoff proves it. |
| C3 | `E_s` is Hilbert--Schmidt iff `Re(s)>1/2` | exact ordered-edge norm sum; even-loop scale divergence; coprime double-sum majorant | proof-result audit records `PROOF_ONLY_Re_s_gt_one_half`; finite direct and parameter second traces agree | The finite trace controls test implementation only.  The endpoint is strict and proof-owned. |
| C4 | `E_s` is trace class iff `Re(s)>1` | entrywise absolute summability above one and absolute even-diagonal obstruction at and below one | proof-result audit records `PROOF_ONLY_Re_s_gt_1`; type and domain audits PASS | Hilbert--Schmidt membership never implies trace class.  The standard-basis diagonal lower bound is analytic, not numerical. |
| C5 | On `Re(s)>1`, `Tr(E_s)=2^{-s} zeta(s)`; on `Re(s)>1/2`, `Tr(E_s^2)=zeta(2s) P(s)=zeta(2s) zeta_MT(s,s;2s)/zeta(4s)` with `P` the coprime double sum | loop classification, trace-ideal legality, ordered-edge parameterization, and exact gcd extraction | X reports both legal finite trace projections PASS; the N=128 values at `s=2,4` agree exactly across direct matrix, ordered edges, parameter triples, and termwise finite scale cutoffs | Infinite zeta factors are never extracted from a finite matrix.  The MT function is a prior-owned comparator, while this same-object trace identity is the paper's central realization theorem. |
| C6 | `det_2(I-zE_s)` is legal only on `Re(s)>1/2`, and the ordinary Fredholm determinant only on `Re(s)>1`; their local logarithms contain the legal trace powers | standard trace-ideal determinant definitions plus C3--C5; graph-specific coefficients proved directly | phase/domain certificates and both Route validators agree; no ordinary determinant is emitted in the Hilbert--Schmidt-only strip | Determinants are operator consequences, not analytic continuation of the displayed zeta functions.  No completed divisor or functional equation is claimed. |
| C7 | The graph has genuinely mixed temporal cycles and its real trace-class operator need not be positive semidefinite | exact triangle `15-30-60-15` with quotients `10,20,12`; `{3,6}` principal determinant `-18^{-s}` | D and P preserve the triangle; X's mixed-walk/support checks PASS; D records exact negative minors `-1/324` at `s=2` and `-1/104976` at `s=4` | Coprime edge coordinates are not temporal primitives, and complex symmetry is not positivity or nonreal Hermiticity. |
| C8 | Canonical replay is independent, exact, and mutation-closed | not a mathematical theorem | 12 X checks PASS; D/P have no project-local scientific imports; 39 theorem/governance, 35 expanded, and 15 external-auditor mutation instances have zero survivors; Route is rejected with Route B forbidden | Establishes reproducibility and provenance only.  It proves neither the infinite theorem nor novelty. |

## Canonical extraction map

`scripts/extract_canonical_results.py` reads and hash-checks the State-A
ledger, both evaluator records, the exact comparison, eleven audit records,
both mutation records, the mechanical report, and the Route record.  It
rejects duplicate keys, noncanonical JSON, a failed status, any ledger/hash
mismatch, a changed comparison key set, a mutation survivor, or a different
Route tuple.  The manuscript reads only the resulting candidate-local
`figures/data/canonical_summary.json`.

## Finite values authorized for reporting

The four complete support cutoffs contain respectively 16, 40, 96, and 228
ordered edges, with 8, 16, 32, and 64 loops.  All twelve named comparison
checks pass.  These values may appear only as finite exact implementation
replay; they do not estimate an infinite endpoint.

## Failure gates

Writer freeze is forbidden if any of the following appears:

- the complex left--right factorization is called unitary conjugacy or used
  to transfer spectra, powers, traces, or determinants;
- `E_s` is named as a bounded operator on `Re(s)<=0`;
- compactness or an ideal wall is inferred from a finite grid;
- a common infinite `zeta(2s)` factor is extracted from a finite cutoff;
- an extra factor two is inserted into the ordered-edge second trace;
- coprime coordinates or harmonic quotients are called temporal primitives;
- ordinary determinants are used on `1/2<Re(s)<=1`;
- symmetry is identified with positivity or nonreal self-adjointness;
- MT identities, Egyptian fractions, or bounded search absence become a
  priority claim;
- Route rejection is hidden, Route B is invoked, or a Hilbert--Pólya claim
  is introduced.

