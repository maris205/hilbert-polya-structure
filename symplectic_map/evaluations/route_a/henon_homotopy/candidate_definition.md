# Candidate definition: `henon_homotopy_v2_shadow_transport`

## Frozen object

The candidate family is

\[
H_{a,\rho}(x,y)=(1-a x^2-\rho y,x),\qquad 0\leq\rho\leq1.
\]

The arithmetic-seed arm fixes (a=u_c=1.5436890126920763), the positive
real root of (a^3-2a^2+2a-2=0).  This value is inherited from the
one-dimensional quadratic-map work and is not chosen from prime labels,
periodic-orbit multipliers, or zeta zeros.  The label *arithmetic seed* is
attributed: prior work supports a parity shadow but not an exact prime-sieve
isomorphism.

The endpoint \(\rho=0\) is a singular reference, not a member of the smooth
symplectic family.  The endpoint \(\rho=1\) is the planar polynomial
symplectomorphism under test.  Values \(0<\rho<1\) are matched conformally
symplectic controls.

## Phase space and geometry

The phase space is \(\mathbb R^2\).  At \(\rho=1\), it carries the standard
two-form \(dx\wedge dy\).  Exactly,

\[
DH=\begin{pmatrix}-2ax&-\rho\\1&0\end{pmatrix},\qquad
DH^T\Omega DH=\rho\Omega,
\]

and a period-\(n\) monodromy matrix has determinant \(\rho^n\).

## Stage-1 arithmetic observable

The only arithmetic content tested in this version is the inherited mod-2
symbolic shadow.  Write `L` when \(x<0\) and `R` otherwise.  For consecutive
`L` visits, let \(g\) be their iteration gap.  The frozen primary statistic is

\[
P=\frac{N_{\rm even}-N_{\rm odd}}{N_{\rm even}+N_{\rm odd}}.
\]

The parent prediction is \(P=1\).  At \(\rho=1\), a result is eligible only
when at least 80% of trajectory-time remains finite inside the frozen escape
box and at least 10,000 return gaps are observed.  The exact pass rule,
neighbor controls, splits, cutoffs, and forbidden data are in
`papers/1-symp-vs-diss/experiments/source_lock.json`.

## Primitive-orbit layer

Primitive cycles are intrinsic solutions of

\[
q_{j+1}+\rho q_{j-1}-1+a q_j^2=0
\]

modulo cyclic rotation and with strict minimal period.  Monodromy, orientation,
action, residual, and missed-orbit risk must be recorded.  The binary
horseshoe arm \((a,\rho)=(6,1)\) is an enumeration positive control.  No
completeness claim is made for the mixed/pruned \(a=u_c\) arm without
validated root isolation.

## Clock, normalization, and determinant convention

Iteration period and the optional instability clock
\(\ell_\gamma=\log|\Lambda_{u,\gamma}|\) are reported separately.  There is
no fitted scale, offset, unfolding, phase, or orbit reassignment.  Stage 1
does not evaluate a dynamical determinant.  In particular, an
unstable-Jacobian Ruelle product is not identified with a Gutzwiller stability
denominator.

## Data boundary

Prime labels and Riemann zeros are forbidden throughout Stage 1.  Development,
validation, and sealed test ensembles use fixed seeds.  The source lock was
amended after development-only smoke tests, so only the untouched validation
and test results may support confirmatory language.

Workspace provenance: the current workspace is not a Git repository, hence
`code_commit=UNAVAILABLE_NON_GIT_WORKSPACE`.  Proposal SHA-256:
`3437e0bf3a54918a524038fc0e61a1c7005d5f64116a52a5979e7dec4773a68a`.

