# Claim-driven experiment and theorem plan

**Status:** T1--T3 complete; T4--T5 pending
**Primary mode:** exact theorem development plus computer-assisted proof
**Fallback mode:** scoped obstruction paper, followed by a dynamical-form
pivot

## Claim contract

The positive claim is intentionally conditional:

> The frozen two-letter Paper-5 Hénon skew product possesses a common local
> hyperbolic survivor whose intrinsic instability-weighted dynamical
> determinant retains protocol information beyond symbol counts, bounded
> local word counts, cyclic phase, and reversal, and is represented by a
> trace-compatible nuclear ordered transfer operator.

The project is successful as a negative result if it rigorously identifies
the first false clause and proves the corresponding collapse or obstruction.

## Gate T1 -- common real survivor: PASS

### Goal

Certify one common four-rectangle covering/cone system for every
\(a\in[59/10,61/10]\), and prove existence and uniqueness of the signed-root
solution for every admissible joint word.

### Producer

1. Re-derive all covering inequalities for
   \(H_a(q,p)=(1-aq^2-p,q)\) with rational outward-rounded bounds.
2. Freeze the four state symbols in order \(--,-+,+-,++\) and the inherited
   adjacency matrix

   \[
   A=\begin{pmatrix}
   1&0&1&0\\
   1&0&0&0\\
   0&1&0&1\\
   0&1&0&0
   \end{pmatrix}.
   \]

3. Prove the signed-root self-map and uniform contraction for variable
   \(a_i\), not only for a constant parameter.
4. Add a cone or derivative certificate sufficient for the unstable
   multiplier used later.

### Independent checker

The checker independently reconstructs every rational margin from the
frozen interval endpoints.  It imports no producer functions.  Mutation
tests must fail if either parameter endpoint is moved outside the certified
window or if one chronological index is reversed.

### Pass condition

All boxes, edges, contraction constants, and cones are proved uniformly for
the closed frozen interval, with nonzero exact margins.

### Kill/pivot condition

Any missing common edge/cone or nonunique branch closes this local form.  Do
not repair it by changing parameters after seeing weighted-zeta results.

## Gate T2 -- joint chronology and exact witnesses: PASS

### Goal

Construct the primitive joint-orbit ledger and prove the complete symmetry
quotient before looking for an anomaly.

### Procedure

1. Enumerate pairs \((w,\varepsilon)\), where \(w\) is a binary parameter
   word and \(\varepsilon\) an \(A\)-admissible sign word.
2. Determine primitivity under the simultaneous microstep shift.
3. Canonicalize only under the joint cyclic action; store the reversal orbit
   separately as a mandatory equality control.
4. Compute each real orbit with a rational Banach a-posteriori enclosure.
5. Enclose the ordered derivative product, trace, unstable multiplier,
   instability length, signed flat weight, and absolute flat weight.
6. Aggregate over **all** local state cycles above each parameter necklace.

### Predeclared short-word comparisons

- same Parikh vector, non-dihedral pair at length five:
  \(aaabb\) versus \(aabab\);
- same cyclic bigram counts, non-dihedral pair at length seven:
  \(0000101\) versus \(0001001\);
- if the bigram pair separates after complete aggregation, test the minimal
  same-trigram pair at length eight:
  \(00101011\) versus \(00101101\).

The length-seven pair and sign word \(++--+--\) are the first interval target
because the numerical pilot has a large separation relative to working
precision.  This target was selected before formal interval certification
and must be recorded as such.

### Controls

- every cyclic rotation must agree;
- every reversal must agree for pure instability and signed/absolute flat
  trace weights;
- constant protocols recover the autonomous endpoint systems;
- swapping the two parameter labels produces the corresponding conjugate
  ledger, not a new candidate;
- joint canonicalization and a brute-force no-quotient sum must agree;
- finite-field witnesses are used only as exact order-sensitivity controls,
  never as evidence of the real survivor;
- comparison is repeated after complete state-orbit aggregation, preventing
  a single selected branch from masquerading as a zeta coefficient.

### Pass condition

At least one interval-certified, completely aggregated pair outside the
dihedral class differs in an intrinsic weight.  The strongest tested
parameter-word memory obstruction is stated exactly, without extrapolating
to all finite-memory potentials on the joint symbolic system.

### Kill/pivot condition

If complete aggregation removes every tested difference, or if the weight is
cohomologous to a bounded-memory potential already captured by a static SFT,
the proposed chronology mechanism closes.  A single branch-level difference
does not pass.

## Gate T3 -- universal collapse controls: PASS

### Goal

Prove which apparently rich trace data are forced by polynomial geometry and
therefore nondiagnostic.

### Proved theorem controls

For a fixed length-\(n\) protocol, the periodic equations form a complete
intersection of scheme length \(2^n\) whenever every letter is nonzero,
independent of protocol order.  Over the full binary base, the corresponding
bare global scheme count is \(4^n\), with formal bare zeta
\((1-4z)^{-1}\).

Under the explicit reduced/nondegenerate hypothesis, the pointwise forms of
the global residue identities are

\[
\sum_{F_wx=x}\frac{1}{\det(I-DF_w(x))}=0,
\qquad
\sum_{F_wx=x}\frac{\operatorname{tr}DF_w(x)}
 {\det(I-DF_w(x))}=-2^n.
\]

These identities are now proved using the cyclic fixed scheme, a Hill
identity, and global residues.  At multiple roots they are residue, not
pointwise-quotient, identities.  Bare counts and the unit-numerator signed
global residue trace are negative controls; local absolute/nonpolynomial
intrinsic weights and nontrivial insertions are outside this collapse theorem.

### Pass condition

Every stated identity has a precise domain, multiplicity convention, and
proof.  Degenerate parameters and points at infinity are treated explicitly.

### Kill condition

A failed identity is reported rather than numerically patched.  The weighted
program may continue only with the corrected exact control.

## Gate T4 -- intrinsic determinant: OPEN

### Frozen candidate

On the certified local survivor define

\[
Z_{\mathrm{inst}}(z,s)^{-1}
=\prod_{\Gamma\ \mathrm{primitive\ joint}}
 \left(1-z^{n(\Gamma)}e^{-s\ell(\Gamma)}\right),
\qquad
\ell(\Gamma)=\log|\Lambda_u(M_\Gamma)|.
\]

The equivalent logarithmic cycle expansion must use
\(M_\Gamma^r\) for the \(r\)-fold repetition.  If a flat determinant weight
is introduced, its repetition law is written separately; the two
determinants may not be conflated.

### Tests

- absolute convergence from the certified expansion rate and a uniform
  instability lower bound;
- equality between primitive-product and fixed-point/log-trace coefficients;
- cutoff and precision convergence inside the proved domain;
- neighboring-parameter and constant-protocol controls;
- no Riemann-zero or prime calibration.

### Pass condition

There is a nonzero, theorem-backed convergence domain and an exact trace
identity at the level claimed.

## Gate T5 -- common complex operator: OPEN

### Goal

Construct one common complex pinning domain for both Hénon letters and exact
branch operators \(\mathcal L_-\), \(\mathcal L_+\) on one Banach space.
The autonomous skew-product operator is

\[
\mathcal L=\mathcal L_-+\mathcal L_+.
\]

This sum is not an average: expansion of \(\mathcal L^n\) contains the sum of
all strictly ordered word products.

### Required theorem

Prove nuclearity or trace-class membership and

\[
\operatorname{Tr}(\mathcal L^n)
=\sum_{w\in\{-,+\}^n}
  \operatorname{Tr}(\mathcal L_{w_{n-1}}\cdots\mathcal L_{w_0}),
\]

with each word trace equal to the declared periodic-orbit weight.  Only then
may \(\det(I-z\mathcal L)\) be called a Fredholm determinant.

For a periodic word of length \(m\), the block-cyclic Floquet operator is a
diagnostic.  Under the same trace hypotheses it must satisfy

\[
\det(I-z\mathcal B_w)=\det(I-z^m\mathcal M_w).
\]

This identity is a collapse control, not the main construction.

### Stop/pivot condition

Failure to find a common complex domain, a uniform nuclear bound, or a
trace-compatible exact kernel ends the positive operator claim.  No
finite-rank Ulam approximation, fitted kernel, or chronology-averaged matrix
is accepted as a replacement.  The output becomes an operator obstruction
and C22 closes.

## Reproducibility and artifact contract

The T1--T3 release must contain:

- a deterministic CLI with all parameters and conventions serialized;
- exact-rational producer and nonimporting checker programs;
- interval certificates with precision, rounding mode, and package versions;
- unit, property, chronology-mutation, and regression tests;
- a JSON ledger for boxes, joint necklaces, witnesses, and determinant
  coefficients;
- an artifact hash manifest and a one-command clean rerun;
- theorem documentation whose labels exactly match the certificate labels.

All of these items are present in the T1--T3 release.  A T4--T5 continuation
must append the complex-domain, operator, trace, and convergence artifacts;
it may not mutate the frozen T1--T3 certificate.

The code may reuse formulas but must not import result artifacts from C19--C21
as proof.  Those projects are source/control inputs only.

## Route-A evaluation contract

Formal evaluation occurs only after the frozen object and artifacts exist.
The expected exploratory ceiling before an arithmetic mechanism is

\[
(\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},
  \mathrm{A3\_FAIL},\mathrm{A4\_FORMAL\_HINT}).
\]

Internal analytic determinant quality is recorded separately from formal
Route-A A2.  A good dynamical Fredholm determinant is not a target-divisor
identification.  Route B remains closed.

## Work budget

After the design freeze, the plan uses two large research rounds:

1. T1--T3 formal producer/checker, certified witnesses, and the go/no-go
   decision for T4--T5;
2. either T4--T5 plus manuscript, or an obstruction manuscript followed by a
   new dynamical-form proposal.

At most two adversarial revision loops are allowed before release.  Repeated
micro-optimization of a failed finite section is outside budget.
