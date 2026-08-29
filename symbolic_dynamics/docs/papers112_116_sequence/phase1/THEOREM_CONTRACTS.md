# Frozen theorem contracts for P112--P116

**Provenance note:** these contracts are the historical Stage-1 targets.
Post-review qualifications in the paper-local consolidated
`HOSTILE_REVIEW.md`, `CLAIMS_EVIDENCE.md`, and `FINAL_QA.md` are authoritative.

Every item marked **must prove** belongs in the theorem text and in the
canonical exact verifier whenever it is finitely testable.  A computation is
control evidence, not a substitute for proof.

## P112 -- synchronous tournament score-upset reversal

**Must prove.**  The update is orientation-unambiguous and fixes `n=0,1`.
Quadratic score energy strictly rises at every nonfixed state, so there are no
nontrivial cycles.  Successive equal-score blocks refine pointwise; the
refinement tree gives `tau(T) <= n-1`.  Fixed tournaments are exactly ordered
sums of regular tournaments.  Their labelled counts obey the induced
recurrence and EGF `F(x)=1/(1-R(x))`; the finite-map zeta follows from the
fixed count.  Exhibit the first non-idempotent orbit at `n=6`.

**May not claim.**  No sharp global maximum-depth formula and no complete
transient enumerator unless separately proved.

**Independent routes.**  Corrected-arc energy; recursive score-class/ordinal-
sum decomposition.

## P113 -- principal-hook partition iteration

**Must prove.**  On partitions of `n>=1`, `(n)` is globally absorbing in the
finite-time sense (every orbit reaches it) and is the unique fixed point.  For
`g(lambda)=lambda_1-lambda_2`, every nonfixed step raises `g` by at least two:
for Durfee size at least two the exact increment is
`ell(lambda)-lambda'_2+2=2+m_1(lambda)`, while the hook-shaped boundary is
handled separately.  Therefore the maximum depth is exactly `floor(n/2)`,
attained by the balanced two-row partition.  State the depth-state-weighted
fibre transport identity (explicitly not a closed scalar recurrence in the
layer counts), the one-step identity `H(lambda)=H(lambda')`, equality of
positive-time iterates, and the unique entrance-depth exception
`(n),(1^n)` for `n>1`.  Global finite-time absorption, that transport
identity, the timing consequence, the fixed point, and zeta are low-credit
corollaries; the exact gap increment and sharp depth theorem are the residual
main result.

**Zero-credit background.**  The one-step image consists of strict gap-at-
least-two partitions, and the fibre weight is the classical
`h_r product(gap-1)` formula.  Gutschwager owns the principal-hook partition
object and first-hook identity, Goupil the one-step image/fibre formulas, and
Chern--Yee direct diagonal-hook symmetry context.

**Owner-subtracted route division.**  Frobenius coordinates/fibres supply
zero-credit one-step inputs and the low-credit transport identity; Ferrers
geometry supplies the residual gap Lyapunov and sharp depth theorem.

## P114 -- parallel rooted-forest leaf peeling

**Must prove.**  The endpoint is the original root set and entry time is
forest height.  For an endpoint of size `r`, prove
`B_(n,r)=sum_k binom(n-r,k) r(r+k)^(k-1)` with the empty conventions.  For a
target on `m` vertices with `s` nonroot leaves, prove the alternating local-
fibre formula.  Derive the bounded-height EGF recursion
`A_0=1`, `A_h=exp(x A_(h-1))`.  Give the empty-height and depth-zero-shell
conventions.  Prove `2^n` fixed states; for `n>=2`, maximum depth `n-1` and
exactly `n!` deepest states; state the `n=0,1` boundaries; and derive the zeta.

**Independent routes.**  Metric peeling/parent maps; labelled species and
Pruefer-style enumeration.

## P115 -- bounded Cartier-operator dynamics

**Must prove.**  Give the closed iterate formula, exact iterate image and
uniform nonempty fibre sizes.  Identify constants as the periodic core and
derive all fixed/core-cycle counts from inverse Frobenius.  Prove the exact
entry-time formula and every depth CDF.  Establish the stated lattice reverse-
defect limit along `n_L=floor(alpha p^L)`.  Show that the temporal signature
recovers `(p,a,n)`, including all small and constant-image boundaries.  With
`d_(u,v)=sigma^(-v)(c_(u p^v))`, give the explicit inverse coordinates and
prove `Psi C Psi^(-1)=sigma^(-1) x N`.  Show that every inverse-Frobenius
cycle of length `d` supports one weak component of size `d q^n`, with the
same attached nilpotent in-trees, per-root entry layers, and indegree type.

**Complementary routes.**  Coefficient `p`-chains establish the iterate,
conjugacy, and clock; finite-field `F_p`-linear rank and fixed-subfield counts
recount the already identified images, fibres, and periodic data.

**Zero-credit background.**  Cartier/Bridy coefficient selection and Jeong's
nearby Cartier families; generic finite-linear state diagrams,
cyclic--nilpotent products, components, and attached-tree machinery of Elspas,
Wang, Hernandez Toledo, Panario--Reis, and Reis.

## P116 -- switching-induced max-plus growth

**Must prove.**  Fix chronological multiplication and `H_0=0`.  Each
generator separately has tropical spectral radius zero and bounded powers,
and neither is tropical rank one.  Prove literal projective gaps strongly
lump to the advertised three-state reward chain.  Prove that no length-one or
length-two word is a projective reset and that the four shortest resets are
exactly `ABA, ABB, BAA, BAB`, with forced gaps `-3,0,0,3`.  Derive its exact
finite-time PGF and cubic characteristic equation, stationary law,
`mu=3pq/(2+pq)>0`, and
`sigma^2=4pq(1-pq)(5-2pq)/(2+pq)^3`.  Derive pressure/LDP, exact word range
and alternating maximizers, both zero-temperature edges, and treat `p=0,1`
outside the irreducible argument.

**Complementary routes.**  Literal tropical gap dynamics constructs the
finite reward chain; tilted Markov-additive spectral analysis then controls
its transforms and limits.  Poisson-equation and Perron-derivative variance
calculations provide a genuinely independent internal cross-check after the
kernel is fixed.

## Common release gate

Each paper requires: a canonical reproducible verifier; two hostile reviews
by different nonauthors; an author repair ledger; clean PDF compilation;
visual, bibliography, font, anonymous and hash QA; and scoped Git sync.
