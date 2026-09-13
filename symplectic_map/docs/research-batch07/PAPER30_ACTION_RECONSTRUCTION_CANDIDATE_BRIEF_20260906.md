# Paper30 candidate brief: minimal periodic data for action reconstruction

Date: 2026-09-06. Status: `SAME_COMPLETE_INPUT_FOR_BLIND_CANDIDATE_REVIEWS`.
This is a candidate-selection brief, not a manuscript, publication lock,
formal Paper30 project, accepted paper or physical page measurement.
Route applicability: `NOT_APPLICABLE`.

## 1. Single problem and proposed scientific scope

For scalar complex symplectic Hénon maps, how much of the unmarked periodic
action spectrum determines the map, and where do complete low-period data
fail? All spectra below have a fixed absolute action normalization and
include local periodic-scheme lengths. They are not derivative spectra.

The proposed article answers this one question in three complementary
regimes: the entire centered cubic family, an infinite binomial family
with a parity-dependent reconstruction mechanism, and sharp low-period
obstructions (quartic and seventh degree, and all even periods). The
cubic and quartic results are not new additions made after a body count:
their independent proofs preceded the binomial extension. Nevertheless,
their inclusion requires an actual scientific-cohesion judgment. Sharing
the words “action spectrum” is not itself sufficient to justify an article.
Reviewers may find the total package too narrow, too composite or too short.

The main increment is not generic finite determination. Classical
Lyashko–Looijenga theory already makes every fixed-point action fiber
finite. The proposed increment is explicit *minimal* low-period resolution
of those ambiguities, with an infinite-degree theorem and a proved
two-versus-three cutoff transition. Finite phase symmetries explain a
genuine obstruction to reconstruction using all even periods.

No stopped formal-gauge, geometric, quantum, wild-cover or matrix-cocycle
result contributes to the claims, narrative capacity or scores.

## 2. Frozen mathematical input and actual audit status

All links in this brief are local inputs. The two eventual candidate
reviewers must receive the same complete final brief and same files.
Reviewers must fully read the files below, not just their abstracts,
conclusions or previous agent summaries. The prior reports contain other
branches for provenance; only their action-inverse deductions are in scope.

1. [Low-degree action author proof](PAPER30_ACTION_INVERSE_FIRST_PROBE_20260906.md),
   478 lines, SHA256
   `763a957cf851119a97f5a3d8f8e4a09b64027e7ebcf20c11254548f116c33ba4`.
   This supplies the complete centered-cubic theorem and quartic obstruction.
2. [Independent low-degree mathematical check](PAPER30_ACTION_INVERSE_INDEPENDENT_CHECK_20260906.md),
   480 lines, SHA256
   `615bbee575c2a2972889fff5271f2957d77e77801dcae438196ab54c1d188684`.
   Completed and fully read by root: all stated results are independently
   PROVABLE AS STATED, with no required theorem repair.
3. [Binomial author proof](PAPER30_BINOMIAL_ACTION_HIGHER_DEGREE_PROBE_20260906.md),
   390 lines, SHA256
   `804be063faf1b07371c51b5dd8ca80bcd6fb402abdf7c678e411643aad363125`.
   Its original short-stop conclusion remains frozen. The new theorem in
   item 4 is genuinely stronger, not a re-vote on that old input alone.
4. [Parity reconstruction author proof](PAPER30_ACTION_PARITY_RECONSTRUCTION_PROOF_20260906.md),
   372 lines, SHA256
   `2d7a84ce1478566153d0639222fec9995b70e4a9acd3c33a00f7913c55862bb3`.
   This adds uniform trace extraction, all degrees one modulo four and
   exact seventh-degree minimum cutoff three.
5. [Independent parity/binomial mathematical check](PAPER30_ACTION_PARITY_INDEPENDENT_CHECK_20260906.md),
   497 lines, SHA256
   `8dfab030d3080427dc3d462a7cc90060c961874c128d76f07d6e820f97a04532`.
   Completed and fully read by root: both complete inputs are independently
   PROVABLE AS STATED, with no required formula, quantifier or hypothesis
   change. In particular, the three-row certificate is independently
   exhaustive and its exact imaginary part is verified.
6. [Original action/LL prior preflight](PAPER30_GAUGE_ACTION_PRIOR_PREFLIGHT_20260906.md),
   305 lines, SHA256
   `d5128f87fb9525e8827fcd4143b2c25b81d5a756adf23501a071ab58b2f432ce`.
   Completed and fully read by root. Its older open/audit-pending statements
   describe its actual date-stage, not a reversal of subsequent proof checks.
7. [Symmetry/action prior report](PAPER30_ACTION_PARITY_MATRIX_PRIOR_20260906.md),
   254 lines, SHA256
   `41f7bc6ac14ed5a50dad159f6ae663d1e7e10259b079ffb560fc2786643f5a3a`.
   Completed and fully read by root. Matrix-cocycle literature is not
   scientific content or capacity for this candidate.
8. [Dedicated reconstruction novelty supplement](PAPER30_ACTION_RECONSTRUCTION_NOVELTY_SUPPLEMENT_20260906.md),
   214 lines, SHA256
   `6fe9b49d9cde512b91135acd29376df97ac7395b3d5d8ecff55a1066393e36c2`.
   Completed and fully read by root. It addresses the new infinite-degree
   and seventh-degree claims rather than silently upgrading the older
   symmetry-only search. No direct covering theorem was located in the
   bounded search; the new strong 2026 multiplier prior is deducted below.

No candidate reviewer may inspect the other candidate report, message the
other reviewer or reuse a previous candidate's scores or page estimates.
Neither earlier action author has performed a candidate-capacity review of
this full new package. No formal Paper30 manuscript has been commissioned.

## 3. Object, normalization and exact meaning of the data

Let $H_p(x,y)=(p(x)-y,x)$, with monic centered $p\in\mathbb C[x]$ of
degree $d\ge3$. Fix $P'=p$ and $P(0)=0$. On the complete periodic algebra
$$
R_{n,p}=\mathbb C[x_0,\ldots,x_{n-1}]/
(p(x_i)-x_{i-1}-x_{i+1})_i
$$
use the action and characteristic polynomial
$$
\mathcal A_{n,p}=\sum_{i\bmod n}(x_ix_{i+1}-P(x_i)),\qquad
\chi_{n,p}(T)=\det(TI-m_{\mathcal A_{n,p}}).
$$
Repeated neighbors at $n=1,2$ are retained. Short-period points are not
removed, the cyclic phase action is not quotiented, and the radical is not
taken. A monic Gröbner basis gives the standard $d^n$-element basis at
every parameter, including collisions. The spectrum satisfies
$$
\chi_{n,p}(T)=\prod_z(T-\mathcal A_{n,p}(z))^{\ell_z},
$$
where $\ell_z$ is the local length. This does **not** record Jordan blocks
or determine the full coordinate algebra. The absolute normalization
matters: adding a potential constant shifts every $n$th action by $-nC$.

Conjugacy means global biholomorphic conjugacy of $\mathbb C^2$; a stated
positive symplectic conjugacy must also preserve $dx\wedge dy$.
The results below distinguish true conjugacy from unit-root ambiguities
of a one-variable critical-value map or a phase-dependent periodic-ring
isomorphism. Fixed-point derivative traces are used only to *prove
nonconjugacy*, never supplied as extra inverse data.

## 4. Complete claims to evaluate

### C1. Entire centered-cubic family: exact two-period recovery

For $p=x^3+Ax+B$, the first-period action spectrum has exactly the
parameter fiber generated by
$$
(a,b)\mapsto(-a,ib),\qquad a=A-2,\quad b=B.
$$
The full first two spectra agree exactly when $A'=A$ and $B'^2=B^2$.
This is also exactly the global biholomorphic conjugacy relation in this
family, realized symplectically by $\pm I$. The minimum initial-period
cutoff is two. The proof covers $A=2$, $B=0$ and all nonreduced fibers.

Key recovery certificates are
$$
T_1=(A-2)^2/2,\quad T_2=3A^2,\quad
A=1+T_2/12-T_1/2,
$$
and at $A=2$, $U_2=132-27B^2$. The exact first-spectrum coefficients,
the two-period trace table and the local-length conjugacy invariants are
proved in the input. Do not count each coefficient or exceptional case
as an independent major contribution.

### C2. Every binomial degree one modulo four: exact cutoff two

For $p=x^d+Bx$, put $d=2q+1$, $m=q+1$, $\kappa=q/(q+1)$. The
all-parameter factorization is
$$
\chi_{1,B}=T[T^q+(-\kappa/2)^q(B-2)^m]^2,
$$
$$
\chi_{2,B}=TD_{-,B}^2D_{+,B}^2G_B^4,\qquad
D_{\pm,B}=T^q+(-\kappa)^q(B\pm2)^m,
$$
with monic $G_B\in\mathbb C[B,T]$ of degree $q^2$.
The ratio involution and scalar rotations explain multiplicities on a
nonempty simple open; polynomial extension proves the whole identity at
every parameter. Taking the parity of root multiplicities extracts
$(B+2)^m$ even when factors collide or their constant term vanishes.

For all odd $d$ and $n\ge2$,
$$
\operatorname{Tr}(m_{\mathcal A_{n,B}}^q)
=-n(d-1)d^{n-1}(-\kappa/2)^qB^m.
$$
A single-reduction trace lemma proves this formula in the standard basis.
For odd $m$, the three translated powers $B^m,(B-2)^m,(B+2)^m$
determine $B$: reduction of the relevant roots of unity at a prime over
two is injective and forces equality. Therefore for every $d\equiv1$
modulo four, $d\ge5$, the first two complete spectra reconstruct every
complex $B$, and the exact minimum cutoff is two.

The separate explicit fifth-degree factor and second/fourth moments are
valid corroboration, but its older reconstruction proof is superseded
by this uniform argument. Re-proving that special case is not a separate
capacity contribution. A brief explicit illustration is optional only if
it adds explanatory value without duplicating the theorem's proof.

### C3. Seventh-degree transition and all-even-period obstruction

For $d=7$, equality of the first two spectra has exactly one nontrivial
unordered fiber, $\{2i,-2i\}$. The third-period action spectra separate
it, so the minimum initial cutoff for the entire family is exactly three.
The finite certificate is
$$
\operatorname{Im}\operatorname{Tr}
(m_{\mathcal A_{3,2i}}^9)=-5338324845/2048\ne0.
$$
This is not an opaque $343\times343$ computation: exactly three reductions
can contribute, proper supports have real total trace by a bipartite
symmetry, and all remaining contributions are the three monomial types
$(7,7,4),(7,6,5),(6,6,6)$. The input supplies their multinomial coefficients,
all ten output assignments and exact admissible-basis counts.

In every degree $d\equiv3\pmod4$, the phase transformation
$x_j\mapsto i(-1)^jx_j$ preserves the complete action algebra at all even
periods while sending $B$ to $-B$. For $d\ge7$, there are exactly
$(d-3)/4$ nonzero unordered sign pairs that additionally share the first
spectrum, described by
$$
B=2(1+\eta)/(1-\eta),\qquad\eta^m=1,\quad\eta\ne\pm1.
$$
Different $B$ are not biholomorphically conjugate, as the local-length
weighted fixed-point derivative trace is
$2d(d-1)-d(d-2)B$. Thus the first spectrum plus *all even spectra*
does not suffice. No all-odd-period collision or general $N(d)$ for
$d\equiv3\pmod4$, $d>7$, is claimed.

The ordinary-map finite-symmetry mechanism is existing background,
not a new general conjugacy principle. The action-preserving ring
identity and its precise inverse-data consequences are what is evaluated.

### C4. Quartic obstruction to a universal two-period rule

Already within $p=x^4+Bx$, the first two complete spectra do not always
reconstruct $B$. Their explicit factors are proved in the input. For
$\zeta^5=1$, $\zeta\ne1$, set
$$
B=2-8/(1+\zeta),\qquad B'=-B-4.
$$
Then $B'\ne B$ but $\chi_{1,B}=\chi_{1,B'}$ and
$\chi_{2,B}=\chi_{2,B'}$ as whole polynomials. The proof uses the
two-period reciprocal-ratio quotient and Vieta identities; it does not
infer whole spectra from a few moments. The derivative-trace invariant
$24-8B$ excludes biholomorphic conjugacy.

This is an explicit boundary to generalizing C1/C2, not a classification
of all centered quartic fibers or a proof of all-period nonrigidity.
The quartic third-period question remains open in this package.

## 5. Mandatory prior and local deductions

The novelty reports, including their read-depth and access limitations,
are part of the complete evidence. Do not equate a search miss to proven
world novelty, nor a preprint to a refereed theorem.

- Classical LL finite maps, collision strata and marked-monodromy
  reconstruction must be deducted. The directly read modern formulation
  is Dougherty–McCammond, arXiv:2410.03047v1, Theorems 7.3 and 7.14 and
  Proposition 11.6. Here $Q=(d+1)(P-x^2)$ is monic centered, $Q(0)=0$,
  and $\mathcal A_1=-Q/(d+1)$ on $Q'=0$. Restriction to this constant-zero
  slice is still finite; the full-space generic degree must not be
  transferred to the slice without proof.
- The explicit critical-value Jacobian/stratification framework in
  Dougherty–McCammond (PAMS 2020) is also prior. Zvonkine (1997) is a
  strong multiplicity precedent with the original full text unread in
  the bounded search; no unread formula is invoked as verified proof.
- Gómez–Meiss, Nonlinearity 17 (2004), 975–1000, provides the finite
  polynomial symmetry framework. Root directly read its Theorem 1,
  Example 5.1 and neighboring square-iterate example in the published
  author-hosted PDF. Imaginary scalings of opposite-linear-term odd
  polynomials and finite central factors are strong prior deductions.
  A short sign symmetry alone would not support this candidate.
- Li, arXiv:2512.03865v1 (2025), concerns deformations preserving selected
  infinite families of standard-map actions. It is relevant inverse-action
  prior, but not equality of all complete spectra in a fixed-degree
  polynomial family. The distinction does not by itself prove novelty.
- Cantat–Dujardin, [arXiv:2603.09445v1](https://arxiv.org/html/2603.09445v1),
  submitted 10 March 2026, Theorem 4.2, proves finite fibers from first-two
  derivative-multiplier data at Jacobian not equal to minus one and generic
  uniqueness up to conjugacy. Our Jacobian is plus one, so this is an
  applicable ambient family but a different observable, not an irrelevant
  setting. Root directly read the theorem and its setup/proof. It supplies
  neither action-to-multiplier conversion nor our all-parameter minimal
  cutoffs. The binomial fixed derivative-trace sum already determines $B$
  in one period if derivative data were supplied; that is why the data
  distinction is substantive rather than terminological.
- D'Andrea–Jeronimo, [arXiv:math/0503721v2](https://arxiv.org/html/math/0503721v2),
  Theorem 2.1, supplies a general characteristic-zero zero-dimensional
  algebra trace formula with local multiplicities. Root directly read
  the theorem, hypotheses and proof. Deduct this broad trace/elimination
  framework; the short one-reduction identity is not a new trace theory.
- Monic Gröbner bases, local Artin trace formulas, polynomial extension,
  elementary cyclotomic reduction, Newton identities and Vieta arithmetic
  are existing tools. Local Paper5 already supplies the action framework;
  Paper15's derivative-spectrum finiteness is not a new claim here.

The dedicated supplement is now incorporated and this complete brief is
frozen. The claim deltas are explicit minimal cutoff and residual-fiber
theorems, not new general LL, trace, number-theory or symmetry principles.

## 6. Unchanged candidate-selection contract

Each of two fresh, mutually blind independent reviewers must evaluate
this *whole same package*, giving separate determinations for:

1. Novelty at least 7.5/10 after all mandatory deductions.
2. Stand-alone scientific value at least 7.5/10, with an explicit answer
   about cohesion versus a collection of degree-specific short results.
3. Complete-proof confidence at least 9/10 under the exact stated scope.
4. Credible natural capacity of 22–30 substantive English body pages.

Publication geometry for capacity reasoning is the existing contract:
anonymous English single-column `article`, 11pt, letter paper, one-inch
margins, standard spacing; references start separately and do not count
as body. Do not enlarge displays, fonts or spacing, add blank pages,
force artificial breaks, or treat logs/code/appendices as body content.
The fourth gate is not implied by the first three. It is a pre-draft
judgment, not physical PDF acceptance.

Each reviewer must give a justified low/central/high natural-body table
by mathematical block, credit each proof once, deduct shared foundations,
and say whether a genuinely complete natural article credibly meets the
whole interval. Counting proof-note lines, enormous matrix listings,
redundant fifth-degree calculations, open problems or contextual padding
as substantive capacity is not acceptable. No author page target is
provided. If the result is naturally a shorter article, say so and fail
the locked capacity gate without denying its mathematical value.

The required decision is the conjunction of all four gates in *both*
reports. Do not average scores, combine different reviewers' best
components, revise thresholds afterward or inherit Paper29's exceptional
one-time natural-draft permission. A capacity disagreement preserves
both reports and fails the conjunction; it is not automatic permission
to draft. Any failed gate stops selection of this unchanged package.

No experiment, numerical fit, zero targeting, Route evaluation, paid
resource, external write or submission is required. All author and audit
inputs remain frozen. Only a subsequent complete PASS could authorize
the ordinary local manuscript stage under the existing workflow.
