# R401-VAL / A4.11 — Validated Theorem-Domain Protocol

## 1. Purpose and claim boundary

This is the prospective computer-assisted-proof protocol for the remaining
gap between the fixed-energy theorem A4.9 and the numerical R401-SC cell at
\(\delta=0.01\).  It uses the exact constants

\[
 a=\frac{51}{50},
 \qquad
 c=2\left(\sqrt{\frac{101}{50}}-1\right),
 \qquad
 0\le\epsilon\le\frac{101}{1000},
 \qquad \delta=\epsilon^2.
\]

The target is to certify, uniformly over this full energy band:

1. the warped shell has exactly one geometric periodic orbit with
   \(0<T\le0.75\), namely the fast Lyapunov orbit;
2. its only return in that window is its primitive return;
3. its transverse determinant has a strictly positive uniform lower bound;
4. its period lies in the frozen R401 Fourier plateau with a positive margin;
5. the radial shell has no return in the same time window.

The R401 value \(\epsilon=0.1\), \(\delta=0.01\), is strictly inside this
validation band.  Only if every item is certified through the larger endpoint
may the project record

\[
 \boxed{\delta_{\rm tr}\ge0.010201>0.01,}
\]

which places the R401 endpoint strictly inside the open A4.9 theorem domain.

Dense floating-point sampling, failure to find another orbit, or agreement
of the R401 trace with A4.10 is not a proof of this statement.  This protocol
uses no prime table and no zeta-zero data and does not advance \(P_0\) or
\(Z\).

## 2. Analytic reductions already proved

Two complete intervals require no validated ODE search:

- A4.11a proves that every nonconstant radial orbit throughout
  \(0<\delta\le0.010201\) has \(T>0.99\).  Hence
  \(\bar\delta(0.75)\ge0.010201\).
- A4.11b places the complete warped configuration domain in a convex box,
  proves \(\|\nabla^2V_a\|_{\rm op}<103\) there, and therefore proves that
  every nonconstant warped periodic orbit has \(T>0.60\) throughout the same
  extended band.

The computer-assisted warped return search is consequently restricted to

\[
 0.60\le T\le0.75.
\]

The remaining threshold components are \(\delta_*\) (warped full-shell
uniqueness) and \(\delta_{\rm nd}\) (uniform transverse nondegeneracy).

## 3. Nonsingular normalized Hamiltonian

Set

\[
 \epsilon=\sqrt\delta\in[0,0.101],
 \qquad q=\epsilon Q,
 \qquad p=\epsilon P,
\]

and write

\[
 W_\epsilon(Q)=A_aQ+\epsilon(-aQ_x^2,0),
 \qquad
 A_a=\begin{pmatrix}-c&-1\\1&0\end{pmatrix}.
\]

The normalized Hamiltonian must be evaluated as

\[
 K_\epsilon(Q,P)
 =\frac{|P|^2}{2}
 +2\pi^2|W_\epsilon(Q)|^2
 \operatorname{exprel}\!\left(
   \pi\epsilon^2|W_\epsilon(Q)|^2
 \right),
\]

where

\[
 \operatorname{exprel}(s)=\frac{e^s-1}{s},
 \qquad \operatorname{exprel}(0)=1.
\]

The validated implementation must enclose `exprel` by a series or a library
primitive near zero.  Direct evaluation of
\((e^s-1)/\epsilon^2\) on an interval containing \(\epsilon=0\) is forbidden.

Physical time is unchanged by this normalization.

## 4. Exact complete-shell parameterization

The entire shell \(K_\epsilon=1\), including its turning sets, is covered by

\[
 \begin{aligned}
 U&=R_\epsilon(\theta)(\cos\alpha,\sin\alpha),\\
 P&=\sqrt2\sin\theta(\cos\beta,\sin\beta),\\
 R_\epsilon(\theta)
 &=\frac{\cos\theta}{\sqrt2\,\pi}
   \sqrt{\frac{\log(1+x)}{x}},\\
 x&=\frac{\epsilon^2\cos^2\theta}{2\pi},
 \end{aligned}
\]

Here \(U=W_\epsilon(Q)\); after constructing \(U\), the exact inverse below
recovers \(Q\).

with

\[
 \theta\in[0,\pi/2],
 \qquad \alpha,\beta\in[0,2\pi],
\]

and

\[
 \operatorname{log1prel}(x)=\frac{\log(1+x)}x,
 \qquad \operatorname{log1prel}(0)=1.
\]

On every interval containing \(x=0\), the implementation must evaluate this
factor by a validated series or a directed-rounding `log1prel` primitive.
Assigning the point value one and then performing interval division by an
interval containing zero is forbidden.  The inverse polynomial map is exact:

\[
 Q=(U_2,-cU_2-a\epsilon U_2^2-U_1).
\]

The redundant angle at each endpoint gives an over-cover, not a gap.  The
cover checker must verify this explicitly.

Before any flow integration, directed rounding must reproduce the common
outer box

\[
 |Q_1|\le0.226,
 \qquad |Q_2|\le0.421,
 \qquad |P_j|\le1.415.
\]

Every validated trajectory and variational enclosure must remain inside a
declared guard box strictly larger than this shell box.

## 5. Domain split and overlap

The normal coordinates are not a floating eigensolver convention.  Define

\[
 G=A_a^TA_a=
 \begin{pmatrix}c^2+1&c\\c&1\end{pmatrix},
 \qquad
 \lambda_\pm
 =\frac{c^2+2\pm c\sqrt{c^2+4}}2,
\]

and the deterministically oriented unit vectors

\[
 e_-=\frac{(1-\lambda_-,-c)}
 {\sqrt{(1-\lambda_-)^2+c^2}},
 \qquad
 e_+=\frac{(\lambda_+-1,c)}
 {\sqrt{(\lambda_+-1)^2+c^2}}.
\]

With \(O=(e_-\ e_+)\), apply the same orthogonal matrix to configuration
and momentum,

\[
 (Q_-,Q_+)^T=O^TQ,
 \qquad
 (P_-,P_+)^T=O^TP,
 \qquad
 \omega_\pm=2\pi\sqrt{\lambda_\pm}.
\]

This block-diagonal transformation is canonical.  Production and checker
must reconstruct its algebraic entries with outward rounding from
\(a=51/50\); stored decimal eigenvectors are not inputs.

In these exact orthogonal normal coordinates define

\[
 r_-^2=(\omega_-Q_-)^2+P_-^2.
\]

Use the overlapping routing domains

\[
 I=[0.60,0.75],
 \qquad
 I_{\rm far}=[0.60,0.64]\cup[0.69,0.75],
 \qquad
 I_{\rm near}=[0.64,0.69].
\]

Thus \(I=I_{\rm far}\cup I_{\rm near}\), with the slow-radius predicate
deciding which engine owns the overlap in state space.

The global exclusion engine covers:

\[
 I_{\rm far}\times\Sigma_\epsilon
 \quad\text{and}\quad
 I_{\rm near}\times\{r_-\ge0.05\}.
\]

The local Poincaré engine covers

\[
 I_{\rm near}\times\{r_-\le0.06\}.
\]

The overlap \(0.05\le r_-\le0.06\) is deliberate.  A box crossing one
routing boundary must be split or accepted by both routes; it may not be
dropped as ambiguous.

## 6. Validated global return exclusion

The global parameter domain is

\[
 (\epsilon,\theta,\alpha,\beta,T)
 \in[0,0.101]\times[0,\pi/2]\times\mathbb T^2\times I.
\]

Treat \(\epsilon\) as a constant state variable \(\dot\epsilon=0\).  Flow
enclosures must use directed-rounding interval arithmetic and a validated
Taylor/Lohner or equivalently rigorous ODE method.  Ordinary DOP853,
double-precision gridding, and unchecked Taylor truncation are inadmissible.

For every terminal parameter box \(B\), let

\[
 F(B)=\Phi_\epsilon^T(Z(B))-Z(B).
\]

A leaf is excluded only if the certificate stores a rational separation
vector \(v_B\) and verifies

\[
 0\notin v_B\cdot F(B).
\]

Componentwise exclusion is allowed as the special case in which \(v_B\) is
a coordinate vector.  Adaptive subdivision must prioritize time, the two
angles, and flow substeps according to measured interval width; it must not
use midpoint residuals as a logical gate.

The archived dyadic tree must prove all of the following:

1. root boxes cover the complete routed parameter domains;
2. every nonterminal parent equals the union of its children;
3. every leaf is either separated or routed into the validated local tube;
4. there are no `UNKNOWN`, maximum-depth skips, NaN leaves, or
   sample-certified leaves.

Failure of this tree to terminate is `INCONCLUSIVE`, not evidence for an
additional orbit.

## 7. Validated local Poincaré branch

Use the positive fast turning section

\[
 P_+=0,
 \qquad Q_+>0,
 \qquad K_\epsilon=1.
\]

For every parameter slab in \(\epsilon\), validate the four-equation system

\[
 \mathcal F_\epsilon(Q_-,Q_+,P_-,T)=
 \begin{pmatrix}
 K_\epsilon(Q_-,Q_+,P_-,0)-1\\
 Q_-(T)-Q_-\\
 P_-(T)-P_-\\
 P_+(T)
 \end{pmatrix}=0
\]

inside the preregistered root box

\[
 Q_-\in[-0.02,0.02],
 \quad Q_+\in[0.12,0.17],
 \quad P_-\in[-0.08,0.08],
 \quad T\in[0.64,0.69].
\]

A parameterized interval-Newton or Krawczyk inclusion must prove existence
and uniqueness in every slab, with consecutive slabs overlapping from
\(\epsilon=0\) through \(0.101\).  The root box outside the included root tube
must separately be excluded; finding one branch is not enough.

A validated flow-box lemma must also certify that every remaining candidate
orbit:

1. remains in \(r_-<0.06\) for its complete putative period;
2. has a positive fast turning-section crossing;
3. has exactly one such positive crossing modulo time translation;
4. lands in the declared Poincaré root box.

Use a finite fast-angle cover with times \(t^-<t^+\) satisfying

\[
 P_+(t^-)>0>P_+(t^+),
 \qquad
 \dot P_+<-\kappa_{\rm sec}<0
\]

throughout each crossing enclosure.  The proof object is a separate dyadic
phase-cover tree: its roots cover the complete local-tube/fast-angle domain,
every parent equals its children, and every leaf records its crossing-time
bracket, oriented derivative bound, full-orbit tube enclosure, and resulting
Poincaré-box inclusion.  No stored Boolean `flow_box_passed` may substitute
for this tree.  This is the required bridge from local fixed-point uniqueness
to whole-shell orbit uniqueness.

To recover the full state from the four displayed equations, production must
also certify one connected enclosure

\[
 Q_+^{\rm initial},Q_+^{\rm final}\in[0.10,0.18]
\]

and a uniform signed energy derivative on that whole enclosure, for example

\[
 \partial_{Q_+}K_\epsilon\ge\kappa_E>0.
\]

Energy conservation, equality of \((Q_-,P_-)\), and
\(P_+^{\rm initial}=P_+^{\rm final}=0\) then force
\(Q_+^{\rm final}=Q_+^{\rm initial}\).  Pointwise or disconnected
nonvanishing derivative checks are insufficient.

## 8. Frozen hard gates

The production result is `PASS_FULL` only if all of the following hold with
strict outward-rounded margins for every \(\epsilon\in[0,0.101]\):

1. **period:**
   \[
   0.66<T_\gamma(\epsilon)<0.67;
   \]
2. **Fourier plateau and primitivity:**
   \[
   T_\gamma<0.68,
   \qquad 2T_\gamma>0.75;
   \]
3. **transverse determinant:**
   \[
   \det(I-D\Pi_\epsilon)>3.0;
   \]
4. **monodromy identity cross-check:** independently enclose
   \[
   D_\Pi=\det(I-D\Pi_\epsilon),
   \qquad D_M=4-\operatorname{tr}M,
   \]
   require both interval widths to be at most \(2^{-30}\), require
   \(D_\Pi\cap D_M\ne\varnothing\), and verify the residual enclosure
   \[
   D_\Pi-D_M\subset[-2^{-28},2^{-28}];
   \]
   the proof object must also record that the nonzero flow tangent satisfies
   \(MX_K=X_K\), and that symplecticity makes the unit multiplier have even
   algebraic multiplicity, supplying the two trivial unit multipliers used
   in the identity;
5. **section transversality:** uniform constants \(\kappa_E,\kappa_{\rm sec}>0\)
   certify the fixed signs of the energy-elimination derivative on the
   complete connected \(Q_+\) enclosure and of the oriented crossing
   derivative on the complete phase tree;
6. **endpoint closure:** both endpoint \(Q_+\) values lie in
   \([0.10,0.18]\), where the signed energy derivative is uniform, so energy
   conservation and the section equations recover the complete state return;
7. **tube margin:** the fast branch satisfies \(r_-<0.04\) along its full
   orbit, strictly inside the local-routing boundary;
8. **root inclusion:** every Krawczyk image lies strictly inside its root
   box;
9. **global and phase coverage:** every leaf in both the global exclusion
   tree and the local phase-cover tree is classified with no omissions;
10. **precision replication:** every strict inequality remains strict in
    separate runs at no less than 128-bit and 256-bit precision.

The archive must report the actual smallest margins, not only Boolean pass
flags.

For `PASS_ENDPOINT` or `PASS_PARTIAL`, the same gates are evaluated only on
the completely certified interval \([0,\epsilon_{\max}]\); no claim is made
for the uncovered remainder up to \(0.101\).

The narrow period band \((0.66,0.67)\), determinant lower bound \(3.0\), and
inner-tube bound \(0.04\) are deliberately stronger than the minimal theorem
hypotheses.  Failure of one of these auxiliary robustness bounds is
`PROTOCOL_BOUND_FAILED` (an inconclusive protocol result), not `INVALID`, a
theorem counterexample, or evidence for another orbit.

## 9. Certificate archive

The immutable successful result directory must contain at least:

```text
results/r401_validated_theorem_domain/
├── manifest.json
├── exact_constants.json
├── analytic_bounds.json
├── shell_cover.json
├── global_cover_tree.json.zst
├── global_leaf_certificates.json.zst
├── local_branch_slabs.json.zst
├── local_phase_cover_tree.json.zst
├── flow_box_certificates.json.zst
├── monodromy_intervals.json
├── margins.json
├── independent_checker.json
└── R401_VAL_RESULT_REPORT.md
```

The manifest binds the exact protocol, source, checker, dependency-lock, and
all certificate hashes.  Interrupted or invalid attempts are moved to
explicitly named attempt directories; they are never edited into a passing
archive.

## 10. Independent checker

The checker must not import the production orbit, flow, or interval modules.
It must reconstruct \(c,A_a,\omega_\pm\) from \(a=51/50\) and independently:

1. verify the analytic radial and warped period bounds;
2. rederive `exprel`, `log1prel`, the shell parameterization, the algebraic
   normal-coordinate matrix, and the outer box;
3. verify that the subdivision tree has no coverage gap;
4. replay each stored separation inequality using an independent
   MPFR/Arb-capable outward-rounded implementation;
5. replay the parameterized Krawczyk inclusions, the complete local
   phase-cover tree, uniform endpoint monotonicity, tube margins, and both
   determinant constructions including their quantitative residual;
6. verify every source/protocol/certificate hash;
7. derive the final status from inequalities rather than trusting stored
   Boolean values.

The preferred certificate format stores Taylor coefficients, rigorous
remainders, and rational separation vectors so that the checker verifies a
proof object instead of rerunning the same opaque ODE call.

## 11. Status logic and fallback

Let the largest completely certified parameter interval be

\[
 0\le\epsilon\le\epsilon_{\max},
 \qquad
 \delta_{\rm cert}=\epsilon_{\max}^2.
\]

- `PASS_FULL`: \(\epsilon_{\max}\ge0.101\) and every theorem and robustness
  gate passes.  Only this status licenses
  \(\delta_{\rm tr}\ge0.010201>0.01\) and upgrades the R401 cell to a
  theorem-domain numerical audit.
- `PASS_ENDPOINT`: \(0.1<\epsilon_{\max}<0.101\) and all other gates pass.
  Report the exact positive margin
  \(\delta_{\rm tr}\ge\delta_{\rm cert}>0.01\); this is sufficient to place
  R401 inside the theorem domain, although the preferred cap was not reached.
- `PASS_PARTIAL`: \(0<\epsilon_{\max}\le0.1\).  Report exactly
  \(\delta_{\rm tr}\ge\delta_{\rm cert}\); R401 at \(0.01\) remains
  A4.9-guided because no strict endpoint margin was certified.
- `PROTOCOL_BOUND_FAILED`: the minimal cover may remain viable, but a
  deliberately strong frozen bound such as \(0.66<T<0.67\), \(D>3\), or
  \(r_-<0.04\) fails.  This is inconclusive under this protocol and is not a
  mathematical counterexample.
- `INCONCLUSIVE`: interval wrapping, unresolved leaves, dependency failure,
  or exhausted resources prevent a complete proof.  This is not a
  counterexample.
- `COUNTEREXAMPLE_CANDIDATE`: a non-excluded small box contains an
  independently reproducible approximate zero.  This status is not evidence
  for a second orbit until a separate interval-Newton existence certificate,
  phase/energy interpretation, and independent audit all pass.
- `INVALID`: a coverage, rounding, hash, or checker-integrity condition
  fails.

If only `PASS_PARTIAL` is obtained, a later spectral audit may be moved to a
preregistered \(0<\delta<\delta_{\rm cert}\), but the frozen R401 conclusion
at \(0.01\) is not rewritten.

## 12. Resource and sequencing policy

Begin on the present 32-vCPU/60-GB host with checkpointed depth-first or
work-stealing subdivision and compressed leaf certificates.  Run, in order:

1. exact-constant and outward-rounding self-tests;
2. shell-parameterization and analytic-bound checker;
3. a small non-claiming implementation smoke;
4. local branch and flow-box certification;
5. global exclusion tree;
6. 256-bit replication and independent certificate replay.

If the global cover exceeds memory or wrapping prevents contraction, stop
and report the measured bottleneck before requesting more resources.  More
hardware may accelerate a valid cover but cannot repair a missing
mathematical classification.

The desired coverage identity is

\[
 \boxed{
 \text{complete energy shell}
 =\text{analytic short-time exclusion}
 \cup\text{validated global exclusion}
 \cup\text{validated unique root tube}.}
\]
