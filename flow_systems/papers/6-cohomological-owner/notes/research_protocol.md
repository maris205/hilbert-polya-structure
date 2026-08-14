# Stage 6 Research Protocol — Which Operator Owns the Zeta?

Protocol date: **2026-08-13**  
Candidate family: finite-field Frobenius suspensions  
Frozen example: \(X=\mathbb P^1_{\mathbb F_2}\)  
Candidate ID: `FF-FROB-OPERATOR-OWNERSHIP-P1-F2`  
Route scope: Route-A same-object audit plus the limited early Route-B audit
explicitly allowed by `skills/route-b-evaluator.md`

## 1. Research question

The Stage-4 Frobenius suspension has an exact arithmetic primitive-orbit zeta,
while Stage 5 tests its natural Koopman unitary lift.  The final paper in this
batch asks a more discriminating question:

> Which operator actually owns the exact Hasse--Weil determinant, and can the
> self-adjointness of the Koopman generator be combined with the exactness of
> the Frobenius--Lefschetz determinant in one Route-B certificate?

The preregistered answer is split.  Both constructions have the same
arithmetic parent \((X,F)\), so this is stronger than a splice of unrelated
systems.  Nevertheless, the two analytic ledgers belong to different
operators:

- the Koopman generator is a self-adjoint differential operator on the
  suspension Hilbert space, but has dense point frequencies, infinite
  multiplicity and essential spectrum \(\mathbb R\);
- geometric Frobenius on graded etale cohomology gives the exact finite
  determinant and Lefschetz trace, but is an algebraic cohomological action,
  not the self-adjoint Koopman generator and not a Hilbert--Polya Hamiltonian.

The paper will prove this operator-ownership separation exactly for
\(\mathbb P^1/\mathbb F_2\).  It will not claim a no-go theorem for all
cohomological quantizations, all arithmetic schemes, or all future enrichments.

## 2. Frozen objects and conventions

### 2.1 Arithmetic parent and suspension

Let

\[
 X=\mathbb P^1_{\mathbb F_2},\qquad
 S=X(\overline{\mathbb F}_2)_{\rm disc},\qquad
 F(a)=a^2,\qquad \tau=\log 2.
\]

The point map \(F\) is the arithmetic Frobenius permutation.  Its mapping
torus is

\[
 M_F=(S\times\mathbb R)/((a,u)\sim(Fa,u-\tau)),
 \qquad \phi^t[a,u]=[a,u+t].
\]

As proved in Stage 4,

\[
 M_F\cong\coprod_{x\in|X|}\mathbb R/(\deg(x)\tau)\mathbb Z,
\]

and the primitive orbit indexed by \(x\) has length
\(\ell_x=\deg(x)\tau=\log N(x)\).

### 2.2 Koopman ledger

Choose any positive component weights \(w_x>0\), and put

\[
 \mathcal H_K=\bigoplus_{x\in|X|}
 L^2\!\left(\mathbb R/(\deg(x)\tau)\mathbb Z,
 w_x\,du\right).
\]

The vertical translation group \(U_t\) is frozen with its natural periodic
boundary condition.  With the sign convention
\((U_t f)(z)=f(\phi^{-t}z)\), its Stone generator is

\[
 A_K=-i\frac d{du},
\]

on the direct-sum periodic Sobolev domain

\[
 \mathcal D(A_K)=\left\{(f_x):
 f_x\in H^1_{\rm per}(\mathbb R/(\deg(x)\tau)\mathbb Z),\quad
 \sum_x\left(\|f_x\|^2_{L^2(w_xdu)}
 +\|f_x'\|^2_{L^2(w_xdu)}\right)<\infty\right\}.
\]

No Riemann zero, boundary parameter, scale fit or phase fit is allowed.

### 2.3 Cohomological ledger

Fix an auxiliary prime \(\ell\ne2\).  Let \(\Phi\) denote the geometric
Frobenius action in the Grothendieck--Lefschetz convention on

\[
 H^i=H^i_{\mathrm{et}}(X_{\overline{\mathbb F}_2},\mathbb Q_\ell).
\]

For \(X=\mathbb P^1\),

\[
 H^0\cong\mathbb Q_\ell,\quad H^1=0,\quad
 H^2\cong\mathbb Q_\ell(-1),
\]

and the Frobenius eigenvalues are respectively \(1\) and \(2\).  The point
permutation uses arithmetic Frobenius while the cohomological trace convention
uses geometric Frobenius; inverse point Frobenius reverses each finite cycle
and therefore leaves the primitive lengths unchanged.  This convention split
must be stated whenever the ledgers are compared.

The native variable is \(t\), with the clock substitution \(t=2^{-s}\).  The
graded determinant convention is

\[
 Z(X,t)=\prod_{i=0}^2
 \det(1-t\Phi\mid H^i)^{(-1)^{i+1}}.
\]

For this example it reduces to

\[
 Z(X,t)=\frac1{(1-t)(1-2t)}.
\]

This is not to be renamed a zeta-regularized determinant of \(A_K\).

## 3. Preregistered theorem package

### Theorem O1 — exact native operator ownership

For every \(n\ge1\),

\[
 \#X(\mathbb F_{2^n})=1+2^n
 =\sum_i(-1)^i\operatorname{tr}(\Phi^n\mid H^i).
\]

Consequently,

\[
 \exp\left(\sum_{n\ge1}\frac{\#X(\mathbb F_{2^n})}{n}t^n\right)
 =\prod_i\det(1-t\Phi\mid H^i)^{(-1)^{i+1}}
 =\frac1{(1-t)(1-2t)}.
\]

**Planned status:** `PROVED`, first by the two one-dimensional Frobenius
actions and independently by formal power-series algebra.  Deligne's
cohomological trace/determinant theorem is the primary framework source.

### Theorem O2 — exact Koopman spectral type

Every degree \(d\ge1\) occurs among the closed points of
\(\mathbb P^1/\mathbb F_2\).  Hence

\[
 \sigma_p(A_K)=\frac{2\pi}{\tau}\mathbb Q.
\]

Every eigenvalue in this set has infinite multiplicity; its closure is
\(\mathbb R\), and

\[
 \sigma(A_K)=\sigma_{\rm ess}(A_K)=\mathbb R.
\]

The operator has no compact resolvent, every open interval (equivalently,
every interval of positive width) has infinite-dimensional spectral
projection, and \(e^{-tA_K^2}\) is not trace class for any \(t>0\) because
the zero eigenspace is already infinite-dimensional.

**Planned status:** `PROVED`.  The result must be invariant under all positive
component weights \(w_x\); changing those weights is a unitary diagonal
rescaling and cannot change the spectrum.

### Theorem O3 — common source does not imply common operator

The exact determinant in O1 is a graded finite-dimensional determinant of
\(\Phi\), not a spectral determinant of \(A_K\).  The two ledger identities
cannot be combined by crediting B2 from \(A_K\) and a determinant/trace gate
from \(\Phi\) to one unnamed operator.  Any block-diagonal operator containing
\(A_K\) retains essential spectrum \(\mathbb R\), so a direct-sum repair does
not produce compact resolvent or the Riemann--von Mangoldt counting law.

**Planned status:** `PROVED` for the two frozen operators and their direct
sums; `OPEN` for genuinely new source-defined bridges.

### Theorem O4 — determinant-variable lift

The two native determinant factors have divisor equations

\[
 1-\alpha2^{-s}=0,
 \qquad \alpha\in\{1,2\},
\]

so their lifts to the \(s\)-plane are the vertical lattices

\[
 s=\frac{\log\alpha+2\pi ik}{\log2},\qquad k\in\mathbb Z.
\]

For \(\mathbb P^1\) these are pole lattices at real parts \(0\) and \(1\),
not a discrete self-adjoint energy spectrum on the critical line.  The
periodicity \(2\pi i/\log2\) arises from the exponential change of variable,
not from additional Frobenius eigenvalues.

**Planned status:** `PROVED` by elementary complex algebra.

## 4. Same-object certificate policy

The Stage-3 T0--T7 certificate will be applied at two levels.

1. **Parent provenance:** the orbit ledger and cohomological ledger both arise
   functorially from the frozen scheme/Frobenius pair; this passes the common
   source check and is a genuine native Lefschetz positive control.
2. **Operator ownership:** Route B asks for one operator, domain, trace,
   spectral parameter and determinant.  `A_K` and `Phi` remain different
   analytic objects.  Common parent provenance is necessary but does not
   permit a coordinatewise maximum across operators.

For the native finite-field zeta, T0--T6 may be certified in the
cohomological/Lefschetz sense, while T7 for rational primes fails.  For the
Riemann target, the one-characteristic clock and the wrong divisor close the
promotion.

## 5. Route-A and limited Route-B decision policy

### Native Hasse--Weil target

- A0: `A0_ANALYTIC_ARITHMETIC_ORIGIN`.
- A1: `A1_PASS_ANALYTIC`.
- A2: `A2_ANALYTIC_DETERMINANT`.
- A3: native rational continuation and exact cohomological determinant are
  proved, but must be described as a finite-field positive control.
- A4: there is a natural cohomological action and a natural Koopman lift, but
  neither statement is a Hilbert--Polya claim.

### Riemann target

- A0 fails: a single characteristic-two clock cannot generate all rational
  prime clocks.
- A2--A3 fail for the Riemann divisor and completed functional equation.
- Route A remains rejected for rational-prime Hilbert--Polya promotion.

### Limited early Route-B audit

The audit is allowed only because a completely natural Hilbert space,
unitary group, domain and self-adjoint generator are available.  It is not a
rescue attempt.

- B1 for \(A_K\): expected `B1_COMPLETE_OPERATOR_DEFINITION`.
- B2 for \(A_K\): expected `B2_SELF_ADJOINT`.
- B3: expected `B3_FAIL` by O2.
- B4: expected `B4_FAIL` for a rational-prime trace from the same operator;
  the native Lefschetz identity belongs to \(\Phi\) and is reported
  separately.
- B5: expected `B5_FAIL`; there is no completed-xi identity.
- Overall: expected `ROUTE_B_REJECTED`, with
  `hilbert_polya_claim_allowed: false`.

## 6. Required adversarial controls

1. **Positive component weights.**  Vary \(w_x>0\); the Koopman spectral type
   must remain unchanged.
2. **Same-cycle-type permutation.**  Replace Frobenius on the discrete set by
   a permutation with the same finite cycle counts.  The bare orbit and
   Koopman ledgers survive, while algebraic/cohomological provenance is lost.
3. **Finite degree truncation.**  It may give finite matrices and finite heat
   traces, but all conclusions must be tested as the degree cutoff grows; no
   truncation is an operator realization.
4. **Direct-sum repair.**  \(A_K\oplus B\) with finite-dimensional \(B\)
   retains the essential spectrum of \(A_K\).
5. **Spectral-variable substitution.**  Distinguish Frobenius eigenvalues in
   \(t\) from the periodic divisor lattice created by \(t=2^{-s}\).
6. **Universal Euler compiler.**  A disjoint union of circles of prescribed
   lengths can encode arbitrary Euler factors and therefore cannot establish
   arithmetic origin.
7. **False-RH control boundary.**  The paper proves no positivity theorem
   that would imply an RH statement for a Davenport--Heilbronn or planted-zero
   control; its exact claim is operator separation.

## 7. Deterministic artifact plan

No network access, target zeros, floating-point root finder, optimizer or
fitted parameter is permitted in the reproduction code.

The script will:

- compute degree counts \(a_d\) exactly by Mobius inversion;
- verify \(\sum_{d\mid n}d a_d=2^n+1\);
- verify equality of point-count, orbit-log and cohomological trace
  coefficients;
- verify the polynomial determinant identity
  \((1-t)(1-2t)=1-3t+2t^2\);
- enumerate finite Koopman frequency cutoffs only as illustrations of the
  exact theorem, recording multiplicity growth for selected rational
  frequencies;
- verify that every output is hash-locked in `results/manifest.sha256`.

## 8. Source hierarchy and integrity rules

Primary framework sources are:

- Deligne, *La conjecture de Weil I*, Publications Mathématiques de l'IHÉS 43
  (1974), especially Section 1 for the closed-point, fixed-point,
  cohomological trace and determinant formulas;
- the original Stone theorem or a standard functional-analysis reference for
  strongly continuous unitary groups, although self-adjointness of the direct
  sum will also be proved directly;
- the Stage-4 source lock for Artin--Mazur/Hasse--Weil and suspension facts.

The Stacks Project trace-formula chapter may be used as an authoritative
definition/checking reference, not as a substitute for the primary Deligne
claim.  Exact page/section locators, URLs and access dates must appear in the
source audit.  Any statement about general varieties, semisimplicity,
canonical complex Hilbert structures or positivity beyond the frozen
\(\mathbb P^1\) example is forbidden unless separately sourced and proved.

## 9. Stop conditions and claim boundary

The paper stops if any of the following would be required:

- identifying an abstract \(\ell\)-adic vector space with a canonical complex
  Hilbert space without a source-defined comparison;
- assigning Frobenius phases through a fitted logarithm branch;
- calling the graded rational function a zeta-regularized determinant of the
  Koopman generator;
- importing B2 from Koopman and B4/B5 from cohomology without naming the
  operator change;
- promoting a finite cutoff matrix to a Hilbert--Polya realization;
- using Riemann zeros to choose any construction datum.

The strongest permitted conclusion is:

> The finite-field model supplies a genuine same-arithmetic-parent
> orbit--Lefschetz determinant, but its natural self-adjoint flow generator and
> its exact determinant owner are different operators.  For the frozen
> \(\mathbb P^1/\mathbb F_2\) example, neither operator has the spectral type or
> rational-prime trace required by Route B.
