# Paper 05 Exact Experiment Report

Status: **SCOPED THEOREM STOP — EXACT GRADING, NO A3 DUAL DOMAIN**

## Outcome

The tensor-factorization topology does supply an exact intrinsic grading.
For every registered full shift through `N=512`, the reduced order complex of
the open tensor-divisor interval has Euler characteristic and homology
supertrace equal to the Möbius coefficient.  The atom fibers occur in degree
`-1`, so they are canonically odd in the standard reduced chain grading.

This produces an exact graded pair in the Euler half-plane:

\[
 \operatorname{Ber}(I-T_s)=\zeta(s),
 \qquad
 \operatorname{Str}_{\Lambda V}\Gamma(T_s)
 =\det(I-T_s)=\zeta(s)^{-1},
 \qquad \Re s>1.
\]

The result does not pass the preregistered A3 gate.  The `s` and `1-s`
sectors have no common ordinary trace-class domain, the naive relative ratio
is not compact on an open set, finite dual phases drift with the atom cutoff,
and no archimedean/Gamma structure is registered.  No candidate ID is
assigned and Route B remains locked.

## Frozen object and data discipline

The source objects are the finite full shifts

\[
 F_m\otimes F_n\cong F_{mn},
 \qquad h_{\rm top}(F_n)=\log n.
\]

For each `n>1`, the experiment forms the open tensor-divisor interval

\[
 P_n=(F_1,F_n)
\]

and its reduced order complex `Delta_n`.  A simplex is a strict chain of
proper tensor divisors.  The augmented signed boundary is

\[
 \partial[d_0<\cdots<d_j]
 =\sum_{i=0}^j(-1)^i
 [d_0<\cdots<\widehat d_i<\cdots<d_j].
\]

The construction reads the tensor relation, unit, and entropy norm.  It does
not read a prime table, Riemann-zero table, fitted sign, fitted clock, or
fitted Gamma factor.  Trial division is used only after complex construction
as a sealed verifier of the expected squarefree/acyclic Betti pattern.

## B1 — exact factorization complexes

All prescribed cutoffs passed exactly.

| `N` | objects | `d^2=0` | Euler=`mu` | homology supertrace=`mu` | Betti pattern | simplices including empty |
|---:|---:|---:|---:|---:|---:|---:|
| 64 | 63 | 1.000 | 1.000 | 1.000 | 1.000 | 440 |
| 128 | 127 | 1.000 | 1.000 | 1.000 | 1.000 | 1,441 |
| 256 | 255 | 1.000 | 1.000 | 1.000 | 1.000 | 4,742 |
| 512 | 511 | 1.000 | 1.000 | 1.000 | 1.000 | 15,629 |

At `N=512`, the largest fiber is `n=480` with 976 simplices including the
empty simplex; the largest chain dimension is seven.  The exact Möbius counts
are 159 coefficients `-1`, 198 coefficients `0`, and 155 coefficients `+1`.

The computed `F_2` Betti pattern agrees at every fiber with the following
integral shellability theorem for products of finite chains:

\[
 \widetilde H_j(\Delta_n)
 \cong
 \begin{cases}
 \mathbb Z,& n\text{ squarefree and }j=\omega(n)-2,\\
 0,& n\text{ not squarefree}.
 \end{cases}
\]

The prime case uses the standard empty-complex convention
`H_tilde_{-1}=Z`.

## B2 — graded determinant and parity controls

There are 97 tensor atoms through 512.  The finite products assembled from
the recovered atoms give:

- odd one-particle Berezinian zeta coefficients: `512/512` exact;
- exterior-Fock supertrace Möbius coefficients: `512/512` exact;
- canonical coprime multiplicativity: `2347/2347` exact.

The two determinant data types are not merged.  The Berezinian is the
reciprocal determinant on the purely odd one-particle atom space, while the
Fock supertrace is the ordinary exterior determinant.

### Global parity reversal

Keeping the vacuum even and flipping every nonunit fiber gives coefficient
accuracy `0.388671875` and coprime multiplicativity `1607/2347 = 0.684704`.
Flipping the vacuum as well changes the normalized constant term to `-1`.

### Random parity

For 32 deterministic random simplex parity assignments, the fraction of
boundary incidences on which the differential is odd was

```text
mean  0.500707
range 0.496390 -- 0.505914
```

The canonical degree gives `1.000`.  Random simplex parity therefore does
not define the required chain supercomplex.

Sixty-four random atom characters remain multiplicative, but their mean
sign accuracy on nonunit squarefree masses is `0.492512`, with range
`0.412141--0.559105`.  This separates an arbitrary monoidal character from
the actual homological degree.

### Factor count with multiplicity

The control `(-1)^Omega(n)` produces the Liouville ledger.  It remains
multiplicative but matches only `314/512 = 0.61328125` coefficients and gives
198 false nonzero coefficients on nonsquarefree masses.  Repeated tensor
atoms are killed by reduced factorization homology, not assigned another
alternating occupation.

### Orientation gauge

Sixteen deterministic simplex reorientations preserve `d^2`, ranks,
homology, Euler characteristic, and all supertrace coefficients.  A valid
reorientation has the form

\[
 B'_j=G_{j-1}B_jG_j
\]

and is a chain-basis gauge.  The experiment selects homological parity but
does not claim a physical simplex orientation.

## B5 — proves-too-much controls

### Shifted multiplication

For `m star n=(m-1)(n-1)+1`, the UFD topology survives, but the intrinsic
full-shift entropy mass does not.  Its coefficient accuracy is `0.26953125`
and ordinary-mass multiplicativity is `1381/2347 = 0.588411`.  A post-hoc
clock `log(n-1)` restores the target, which is precisely the forbidden
`PROVES_TOO_MUCH` move.

### Additive monoid

The additive law has one atom of entropy zero.  Its Euler factor
`1-1^(-s)` vanishes, so no analytic Euler product is defined.  Only one of
130,816 positive registered pairs satisfies entropy additivity under the
full-shift norm; the maximum entropy-additivity error is `4.85203`.

### Positive free mixing

All 28 pairs among the first eight recovered atoms show the same exact
failure.  Isolated atom loops give

\[
 \operatorname{coeff}_{n=pq} Z=1,
 \qquad
 \operatorname{coeff}_{n=pq}(-Z'/Z)=0,
\]

whereas free positive mixing gives coefficient two in `Z` and the spurious
coefficient `log(pq)>0` in `-Z'/Z`.  Word-length parity cannot cancel the two
ordered even words `pq` and `qp`.

## B3 — finite dual ratio diagnostics

For atom cutoffs `31,127,257,509`, the frozen seven-point grid tests

\[
 R_P(s)=\prod_{p\le P}
 \frac{1-p^{-(1-s)}}{1-p^{-s}}.
\]

The algebraic finite identities pass to floating precision:

| diagnostic | maximum residual |
|---|---:|
| `R_P(1-s) R_P(s)=1` | `2.70e-15` |
| `abs(R_P(1/2+it))=1` | `7.77e-16` |

The maximum wrapped phase change between adjacent cutoffs is `3.10576`
radians.  This drift is fully reported and the finite identities receive
`NONE_FINITE_ALGEBRA_ONLY` analytic credit.

## B4 — Schatten and relative nuclear diagnostics

For `T_s=diag(p^{-s})`, the exact membership criterion is

\[
 T_s\in S_q \iff q\Re s>1,
 \qquad
 T_{1-s}\in S_q \iff q(1-\Re s)>1.
\]

Consequently:

- `S_1`/trace-class overlap: none;
- `S_2` overlap: none;
- `S_4` overlap: `1/4 < Re(s) < 3/4`.

The `S_4` fact does not define an ordinary Fredholm determinant and no
regularized determinant is introduced after seeing it.

The naive relative ratio is diagonal with

\[
 Q_s-I
 =T_{1-s}T_s^{-1}-I
 =\operatorname{diag}(p^{2s-1}-1).
\]

It is zero at the isolated real center `s=1/2`, but does not define a compact
relative perturbation on any open domain.  At `s=1/2+i`, its partial trace
norm grows across the four cutoffs as

```text
11.3980, 45.6491, 86.2878, 114.2360.
```

The ordinary `s` and `1-s` Fredholm determinants therefore have disjoint
initial domains, and the finite ratio does not repair this analytically.

## Functional-equation and Gamma audit

The divisor-complement map `d -> n/d` is order reversing, but fixes the total
mass `n`.  It does not map `n^(-s)` to `n^(-(1-s))`.  No archimedean symbolic
sector, Gamma factor, trivial-zero mechanism, or internally controlled
continuation is present.  No zeta zeros were loaded or fitted.

The final gate decision is:

```text
G0 definition/source lock: PASS
G1 intrinsic chain parity: PASS; simplex orientation remains gauge
G2 exact trace ledger: PASS
G3 analytic domain: original Euler half-plane only
G4 A3 progress: FAIL
overall: SCOPED THEOREM STOP
Route B: LOCKED
```

## Reproduction

From the Paper05 project root:

```bash
PYTHONDONTWRITEBYTECODE=1 \
  python code/intrinsic_grading_experiment.py --N 512 --output results

PYTHONDONTWRITEBYTECODE=1 \
  python -m unittest discover -s code -p 'test_*.py' -v
```

The implementation uses only the Python standard library.  Two independent
full executions produced byte-identical result files.

## Result files

- `results/summary.json` — gates, main results, controls, and analytic verdict.
- `results/factorization_complexes.csv` — all 511 exact complex certificates.
- `results/coefficient_ledgers.json` — canonical and control coefficients.
- `results/free_mixing_controls.csv` — all 28 mixed-word tests.
- `results/dual_ratio_diagnostics.csv` — finite `R_P` grid.
- `results/schatten_partial_norms.csv` — `q=1,2,4` partial norms by sector.
- `results/selected_complex_certificates.json` — hand-auditable fibers.
