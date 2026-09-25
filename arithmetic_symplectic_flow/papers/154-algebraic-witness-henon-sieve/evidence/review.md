# Independent mathematical audit — 154

Candidate: **ASFS-20260915-AWH01**. Date: 2026-09-15.
Audit basis: the frozen [version-1 card](../candidate-card.md), the local
[plan](../../../plan.md), and the all-state equations below.

This is a bounded model-generated mathematical review, not human peer review,
not an editorial acceptance, and not a formal Route evaluation.
Calibration status: **NOT_CALIBRATED**. Venue-criteria binding unavailable;
no venue-alignment claim is made. The reviewer is a separately invoked agent
in the same agent family, with the parent's task description visible. No
other review report was consulted. Invocation separation does not establish
independent error processes.

## Verdict and coverage

The frozen construction's symplecticity, full periodic-set classification,
prime-packet multiplicity, hyperbolicity, and ordinary-zeta convergence
claims survive the checks below. No mathematical blocker was identified in
the card or the subsequently reviewed manuscript. The manuscript-specific
receipt is recorded separately at the end of this file.

| Criterion | Authority and evidence anchor | Judgment | Scope |
| --- | --- | --- | --- |
| Full intrinsic periodic set | Card map equation; cyclic recurrence below | MEETS | Every real coordinate and every positive integer period, not a finite search |
| Prime multiplicity and repetition | Card cyclic phase and unit roof | MEETS | One primitive orbit per prime, length K_n and r K_n |
| Symplecticity and nondegeneracy | Card map; inverse and derivative below | MEETS | Real smooth disconnected plane carrier; not an automatic contact owner |
| Arithmetic controls | Card witness count and interpolation control | MEETS | Exact integer-gap selector; not special Riemann naturalness |
| Ordinary zeta | Card central analytic object; convergence comparison below | MEETS | Ordinary full-orbit product only; no operator or trace identity |
| Exact log-prime clock or formal Route | Card cost/clock and Route rows | NOT ASSESSED | These stronger claims are not the candidate's established result |

## Direct independent checks

Put H_a(q,p)=(p,2p-q+g_a(p)), where
g_a(t)=(1-a)t+a sqrt(1+t^2). Its inverse is

    H_a^{-1}(Q,P)=(2Q+g_a(Q)-P,Q).

Both maps are globally smooth. The derivative has determinant one;
equivalently dQ wedge dP equals dq wedge dp. The cyclic phase is inverted
by stepping backward, so the entire countable disjoint union is a single
smooth symplectomorphism. Countably many Euclidean planes give a Hausdorff,
second-countable smooth manifold. A unit roof is positive and non-Zeno;
the suspension is complete and three-dimensional, not automatically
symplectic, contact, or Hamiltonian.

On a periodic trajectory, write x_j=p_j=q_{j+1}. Then

    x_{j+1}-2x_j+x_{j-1}=g_a(x_j).

Summing over its actual full period gives zero on the left. If integer
a>=1, then g_a(t)>0 for every real t. For t<0 both terms in the displayed
definition are nonnegative and the square-root term is positive. For t>=0,
g_a(t)=t+a(sqrt(1+t^2)-t)>0. Thus no periodic trajectory of any period
exists in any composite-labelled component. No boundedness assumption,
selected centre, or selected section enters this exclusion.

For a=0 the plane map is exactly linear with matrix

    B = [[0,1],[-1,3]].

Its eigenvalues are lambda_+=(3+sqrt(5))/2>1 and lambda_-=1/lambda_+<1.
Neither has any positive power equal to one. Therefore B^m z=z forces
z=0 for every integer m>=1. The full phase increment then has least
period K_n, so each prime n supplies exactly one primitive orbit, formed
by all K_n origin states. In particular n=2 and n=3 supply distinct
length-one primitive orbits; they must not be merged because their lengths
coincide. Every repeat has period r K_n and monodromy B^{r K_n}, with

    det(I-B^{r K_n}) = 2-lambda_+^{r K_n}-lambda_-^{r K_n} < 0.

This removes parabolic degeneracy for this map's own prime packets, not by
borrowing a monodromy from another candidate. A nonzero determinant still
does not prove existence of a trace-class operator or a trace identity.

## Noninteger interpolation control

The actual arithmetic parameter is a nonnegative integer. The contrast
parameter a in this subsection does not change the frozen candidate.

For 0<=a<1/2, the unique zero is

    t_*=-a/sqrt(1-2a),

and g_a'(t)>=1-2a>0. Multiplying the recurrence by x_j-t_* and summing
cyclically yields

    -sum_j (x_{j+1}-x_j)^2
      = sum_j (x_j-t_*) g_a(x_j) >= 0.

Every periodic state is therefore the constant state t_*. It yields one
K_n-phase orbit. At that point

    g_a'(t_*)=(1-2a)/(1-a)>0,

so the plane derivative has trace 2+g_a'(t_*)>2 and is hyperbolic.
For a>=1/2 the force is strictly positive everywhere: for t>=0 use
the previous expression; for t<0 write t=-u and observe
a sqrt(1+u^2)-(1-a)u>=(2a-1)u, with strictness at a=1/2 as well.
Thus there are no periodic states at or above the threshold.

Consequently the decisive arithmetic property is the gap from a=0 to
integer a>=1, not continuity from zero or robustness against arbitrary
small positive real witnesses.

## Ordinary-zeta comparison

The full ordinary orbit product is

    Z(s)=prod_{p prime} (1-exp(-s K_p))^{-1}.

For positive sigma, absolute convergence of its logarithmic repetition
series is equivalent to convergence of sum_p exp(-sigma K_p), because
K_p>=1 bounds the repetition tail by a sigma-dependent constant. Since
K_p differs from log_2(p-1) by a bounded amount, the latter series has
the same convergence behavior as sum_p p^{-sigma/log(2)}. It converges
for sigma>log(2) by comparison with the full integer series of exponent
greater than one. At sigma=log(2), its terms dominate 1/p and the prime
harmonic series diverges; smaller positive sigma only increases terms.
At sigma<=0, even one primitive orbit's repetition series fails absolute
convergence. Thus the absolute-convergence abscissa is exactly log(2).

The prime-harmonic divergence used here has an elementary finite-product
proof: if sum_p 1/p converged, finite products prod_{p<=N}(1-1/p)^{-1}
would be uniformly bounded. Their geometric expansions contain every
1/m for 1<=m<=N by unique factorization, contradicting divergence of
the harmonic partial sums. No prime-number theorem is needed.

This establishes normal convergence on compact subsets of the right
half-plane and hence a nonzero ordinary zeta there. It does not establish
an exact-log-prime Euler product, analytic continuation, a target divisor,
or a Fredholm determinant.

## Strongest counterargument and its boundary

The strongest surviving objection concerns interpretation, not the preceding
periodic-set proof. The arithmetic witness count is recomputed in every
update and is designed to vanish exactly on primes. The force then turns
this zero set into the complete recurrent set. A comparable construction
can represent many other prescribed decidable admissibility conditions;
therefore the existence of prime packets alone does not show a distinguished
connection with Riemann's analytic geometry. The dyadic phase also imposes
a binary macrostep convention, while a full cycle still performs
K_n(n-2) elementary divisor tests under the stated direct implementation.
Its logarithmic-order geometric clock is real for the frozen unit-roof
flow, but it is not sequential runtime and is not exact log p.

These objections would defeat stronger claims of unique arithmetic
naturalness or a Riemann trace identity. They do not refute a correctly
scoped positive construction theorem: all labels are present, no prime
table is imported, divisibility is executed by one uniform rule, and the
full continuous periodic set is proved rather than post-selected. The
paper must keep that constructive statement distinct from the stronger
target interpretation.

## Issue list and handoff

No Critical or Major mathematical defect is identified in the frozen
card and manuscript claims checked here. Exact target clock, operator domain,
trace identity, and target-divisor structure remain open limitations,
not silently passed obligations. Arithmetic/source, full-map orbit,
unit-roof clock, and ordinary-zeta ownership remained intact throughout
this audit. Formal Route coordinates remain UNASSIGNED and Route B is
NOT INVOKED. The warranted decision is advance the bounded same-object
result or fork a genuinely different analytic/clock owner under a new
card; do not rebrand this product as a Riemann determinant.

## Manuscript receipt

After the card-first checks above, the reviewer read the entire
[paper](../paper.md), [README](../README.md),
[claim ledger](../claim-ledger.md), [evidence index](README.md), and
the card's dated outcome. All five documents name ASFS-20260915-AWH01 and
the same status:

**PRIME-ONLY HYPERBOLIC SYMPLECTIC PACKETS AND ORDINARY ZETA ESTABLISHED; TARGET CLOCK AND OPERATOR OPEN.**

The manuscript's equation (1),
g_a(t)=sqrt(1+t^2)+(a-1)(sqrt(1+t^2)-t), is an especially direct correct
integer-gap positivity argument. Its equations (2)--(5), all-state
quantifiers, n=2 and n=3 multiplicity, transverse-monodromy convention,
ordinary rather than weighted zeta, and exact-convergence comparison
match the independently checked arguments above. Section 7 deliberately
claims only fixed-point existence below the interpolation threshold;
the stronger all-period control proved in this review is compatible
but is not required for the manuscript's main claim. All source, clock,
analytic-naturalness, and formal-Route limitations remain visible.

No manuscript revision was required by this review. The evidence index's
finite arithmetic command was read as a regression method, not used as
support for the infinite theorems. Its execution-output receipt is owned
by the author and was still pending at the time of this mathematical
review; no finite-run success is certified here.
