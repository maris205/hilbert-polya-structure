# HCS-C24: Rauzy chronology and the discrete metaplectic obstruction

**Date:** 2026-08-09
**Status:** `PROVED_TWO_CLASS_OBSTRUCTION; CANONICAL ANALYTIC APPLICATION OPEN`

This round makes the planned large system switch away from another local
Hénon scan.  The frozen base is the literal four-letter reversal

\[
\pi_0=\begin{pmatrix}1&2&3&4\\4&3&2&1\end{pmatrix}.
\]

It passes the source lock without substitution: its labeled hyperelliptic
Rauzy class has seven states, its crossing form has rank four and determinant
one, and the associated translation surfaces lie in \(\mathcal H(2)\).

## Large-gate result

The round produces two independent obstructions to the naive
chronology-preserving metaplectic Fredholm proposal.

First, let \(\mu\) be the oscillator representation on
\(L^2(\mathbb R^2)\).  For a norm-convergent discrete atomic extension

\[
T=\sum_h A_h\otimes\mu(\widetilde g_h),
\qquad \sum_h\|A_h\|<\infty,
\]

combine only terms with the same projected symplectic matrix, retaining the
actual metaplectic central sign.  If one signed aggregate \(A_g\) is nonzero,
then \(T\) is not compact.  The proof sends a Weyl coherent state to infinity;
metaplectic covariance separates the distinct atoms in phase space.  This
removes the main weakness of the preliminary branch-projection argument.

The elementary special case is exact and quantitative:

\[
\|K\otimes U\|_{\mathrm{ess}}=\|K\|
\]

for every bounded \(K\) and every unitary \(U\) on an infinite-dimensional
fiber.  Hence an exact or modulo-compact nonzero branch compression is already
enough when norm summability on a chosen analytic space has not been proved.

Second, the exact periodic ledger shows that the regular point formula for
the Weil distribution character does not define a finite weight on every
selected primitive labeled Rauzy cycle.  Through elementary
length 12 there are

\[
4,2,4,4,8,11,22,35,64,110,204,360
\]

primitive labeled directed free cycles, for a total of 828.  Exactly 146 are
eventually positive in every cyclic phase, with counts

\[
1,6,14,36,89\qquad (n=8,9,10,11,12).
\]

Among those eventually-positive labeled cycles, 21 satisfy

\[
\det(I-M)=0.
\]

Their reciprocal characteristic polynomial contains \((x-1)^2\), so
\(\det(I-M^r)=0\) for every repetition.  The familiar expression involving
\(|\det(I-M)|^{-1/2}\) is therefore on the fixed-vector/singular locus and
outside the regular point formula for these coded periodic cycles.  It cannot be used as an ordinary
operator trace or a finite pointwise Euler weight.

The 146 eventually-positive labeled cycles realize only 41 reciprocal characteristic
polynomials.  They are distinct periodic words in the fixed-label Rauzy
coding; no distinctness claim is made after forgetting markings.  This
collision is another reason not to identify primitive dynamics with
homological spectral data alone; no codes are quotiented by their spectrum.

## Exact chronology

For an edge with winner \(w\) and loser \(\ell\), the forward homology matrix
is

\[
B_e=I+E_{\ell,w}.
\]

For \(w=e_1\cdots e_n\), later edges act on the left:

\[
B_w=B_{e_n}\cdots B_{e_1}.
\]

Open edges transport changing crossing forms,

\[
B_e\Omega_{\rm src}B_e^T=\Omega_{\rm dst};
\]

they are not silently treated as elements preserving one fixed form.  Closed
loops preserve \(J=\Omega^{-1}\).  Cycles are quotiented only by cyclic phase;
direction, directed edge tokens, proper-power metadata, every elementary
matrix, the central sign boundary, and the unaccelerated word all remain.
Maximal cyclic `t`/`b` runs (the combinatorial same-type/Zorich-run itinerary)
and the induced returns to the central state are recorded in addition, never
substituted for the chronology.  No accelerated roof or canonical analytic
Zorich transfer space is claimed here.

## Decision

Two explicit realization classes are closed:

> an unsmoothed, discrete, infinite-dimensional metaplectic fiber admitting
> either a nonzero exact/modulo-compact branch compression or an absolutely
> norm-summable atomic expansion with a nonzero signed aggregate.

The first class is obstructed by the compression theorem.  The second is
obstructed by the discrete-atom theorem unless all signed same-matrix
aggregates vanish.  The compression theorem permits Banach ambient spaces;
the atomic theorem as stated uses Hilbert base spaces.  A particular canonical
analytic Zorich space has not yet
been proved to satisfy either application hypothesis, so the unrestricted
operator proposal is not declared globally dead.  Finite oscillator cutoffs
and inserted heat factors change the candidate and are not repairs.

The ledger counts labeled directed Rauzy codes.  It does not assert that all
146 are distinct primitive unmarked Teichmüller geodesics.  This does **not**
rule out a distributional character, a flat/dynamical trace,
a geometrically forced semifinite determinant, continuous group smoothing,
or a different canonical quantum fiber.  Such an object would be a new
candidate and must explain the singular labeled-return cycles.

Route-A verdict:

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)
ROUTE_A_REJECTED
```

The system has a strong intrinsic periodic/symplectic structure, but no
prime-like law, no ordinary determinant, no Riemann divisor, and no analytic
completion.  Route B is not authorized.

## Reproduction

```bash
python -m pip install -r requirements.txt
./code/run_c24.sh
```

Primary artifacts:

- [`SOURCE_AUDIT.md`](SOURCE_AUDIT.md) — conventions and primary-source lock;
- [`THEOREM_PACKAGE.md`](THEOREM_PACKAGE.md) — the two noncompactness theorems;
- [`results/c24_certificate.json`](results/c24_certificate.json) — complete
  exact ledger through length 12;
- [`results/c24_independent_check.json`](results/c24_independent_check.json) —
  independent seven-state/Möbius verification;
- [`results/RESULTS.md`](results/RESULTS.md) — interpreted result;
- [`paper/main.pdf`](paper/main.pdf) — compiled technical note.

No prime table, Riemann-zero table, time fit, unfolding, averaged transition
matrix, or post-selection is used.
