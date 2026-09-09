# R4 E1: independent review of the isometric-cycle measure bridge

2026-09-09 UTC. Current-session nonauthor review of D1's
[PROOF_PACKAGE.md](../../d1_isometric_cycle_limit/PROOF_PACKAGE.md)
and consistency readback of its [REPORT.md](../../d1_isometric_cycle_limit/REPORT.md).
The arithmetic proof in A1 is the separate E2 assignment. Source priority
and paper admission are separate coordinator gates.

## Verdict

**PROVABLE AS STATED for the general theorem and the conditional quadratic
interfaces. Open mathematical must-fixes: 0. Open source-applicability
must-fixes within this review: 0.**

The audit includes the exact finite-cycle coupling identities, compact
classical closure, Hausdorff and full-sequence measure convergence,
minimality, unique ergodicity, finite-cycle/$\mathbb Z_p$ dichotomy,
Berkovich implementation, optional countable-closure lemma, direct
aperiodicity refinement and abstract nonconvergence control.

This verdict does not independently certify A1's average-contact formula.
If that formula passes its separate all-parameter arithmetic review, D1
has proved the needed topology/measure implication, including the
nonatomic adding-machine refinement. Without that input, the application
remains conditional. This is one bridge to the same measure question,
not a separately counted paper or a priority determination.

### Reviewed bytes

Paths below are relative to `henon_dynamics/research_c429_c433/`.

```text
e2daa9770024c62e7b7fb09855d4c23eaa0c4cd0aa5416ad268288dbe569aedd  continuation_round4/d1_isometric_cycle_limit/PROOF_PACKAGE.md
56a2b94c51d34786f3ab5957dc4ec3ab93c09fb6671e40018c02cb1e72d5e665  continuation_round4/d1_isometric_cycle_limit/REPORT.md
```

The A1 interface statement read is (MC2), at proof hash
`038cdb412d1b83b94c1ebcfb742090e3937251225077a0f6842d7933c458174e`.
This is an interface-version receipt, not a second review of its proof.
The final D1 proof includes the direct bound (7); the earlier isolation-only
formulation is not the version being accepted here.
The report binding includes the author's final E1 status/link update,
which was read back separately; the mathematical proof bytes did not change.

## Exact claim and dependencies

The general theorem assumes a complete ultrametric space $(X,d)$, an
isometry $T:X\to X$, and nonempty finite single cycles $C_e$. It does
not assume that $T$ is onto $X$, that $X$ is locally compact or separable,
or that the different cycles have nested supports. With uniform cycle
probabilities $\mu_e$, define

$$a_{d,e}=\min_{x\in C_d,y\in C_e}d(x,y),
\qquad \varepsilon_d=\sup_{e>d}a_{d,e}.$$

The additional hypothesis is $\varepsilon_d\to0$. Its conclusion is
compactness of the entire classical closure $B$, Hausdorff convergence
to a nonempty compact invariant $A$, and weak convergence of $\mu_e$
to the unique invariant probability on the minimal system $A$.
When $|C_e|=p^e$, the limit is a finite $p$-power cycle or a $p$-adic
adding machine.

The proof's dependency order is valid: exact coupling first; total
boundedness and completeness second; compact-space limit arguments third;
finite clopen quotients fourth. Berkovich compactness is not substituted
for classical compactness. The actual quadratic map enters only after
this general theorem, through its complete invariant disk, isometry and
the explicitly conditional contact hypothesis.

## 1. One nearest pair gives the exact support and transport distances

For cycles of lengths $m,n$, the proposed coupling over
$L=\operatorname{lcm}(m,n)$ has the correct marginals: every first-coordinate
point occurs $L/m$ times and every second-coordinate point $L/n$ times.
All coupled pairs have the nearest-pair distance $a$ by isometry.
Conversely, every pair of support points has distance at least $a$.
Thus every coupling has cost and essential supremum at least $a$, while
the displayed one attains both:

$$W_1(\mu_C,\mu_D)=W_\infty(\mu_C,\mu_D)=a.$$

Orbit transport also supplies, for every point of either cycle, a point
of the other at distance $a$. Each directed Hausdorff distance is therefore
exactly $a$. These assertions hold for arbitrary finite periods, including
equal cycles and one-point cycles, and do not need the ultrametric
inequality. Finite supports ensure all first moments exist even before
compactness of the larger union is established. All probability weights
are real numbers; no division inside a field of characteristic $p$ occurs.

Consequently the supremum condition is exactly Hausdorff-Cauchyness:
it is the uniform pairwise Cauchy requirement for all sufficiently late
indices. It is not asserted to characterize weak convergence in a larger
compactification, which would be a stronger and unsupported necessity claim.

## 2. Classical compactness, Hausdorff limit and surjectivity

For each prescribed radius, one sufficiently late finite cycle gives a
finite net for every later cycle. Adding the finitely many earlier cycles
gives a finite net for the entire union. This is total boundedness, not
an appeal to local compactness of a surrounding disk. Its closure is
complete because $X$ is complete, so $B$ is compact metric.

Although ambient surjectivity was not assumed, it follows on $B$:
$T(B)$ is a compact, hence closed, subset of $B$ containing the dense
union of cycles. Thus $T(B)=B$. The Hausdorff-Cauchy argument now takes
place entirely inside a proved compact metric space. The subsequential
point-limit construction gives the nonempty compact tail intersection
$A$, and the Cauchy property upgrades this to convergence of the full
sequence of supports, with

$$A=\bigcap_N\overline{\bigcup_{e\ge N}C_e}^{\,B},
\qquad d_H(C_d,A)\le\varepsilon_d.$$

Both directions of $T(A)=A$ are accounted for. Forward invariance follows
from continuity. For the reverse inclusion, predecessors of a sequence
of cycle points have a convergent subsequence in $B$ whose limit is again
in the tail set $A$. This avoids assuming that a merely forward-invariant
ambient disk has an inverse map everywhere.

## 3. Full-sequence weak convergence and limiting couplings

Every real-valued continuous function on $B$ is uniformly continuous.
The exact finite coupling therefore makes its sequence of cycle integrals
Cauchy, with error bounded by $\omega_f(\varepsilon_d)$. Taking these
limits defines a positive norm-one functional on $C(B,\mathbb R)$.
The Riesz representation theorem is being used on compact Hausdorff $B$,
with positivity and normalization explicitly checked. It supplies a
regular Borel probability and proves convergence of the full sequence,
not just one extracted subsequence.

Invariance passes to the limit by testing $f\circ T$. The support is
contained in $A$: each compact subset of $B\setminus A$ has positive
distance from $A$ and eventually misses every cycle, and continuous
test functions plus regularity eliminate mass there.

The later coupling extraction is also legitimate. Probabilities on the
compact metric space $B\times B$ are sequentially compact for weak
convergence. One may see the precise hypothesis by taking a countable
uniformly dense family in $C(B\times B)$, extracting diagonally, and
using Riesz representation for the resulting positive functional.
The weak limit has the desired marginals. Its mass stays on the closed
distance bound $d(x,y)\le\varepsilon_d$, so

$$W_1(\mu_d,\mu)\le W_\infty(\mu_d,\mu)\le\varepsilon_d.$$

This establishes the stated quantitative result without a global
metrizability assumption on a Berkovich compactification. The proof does
not claim that every invariant probability on the larger space $B$ is
this limit; early finite cycles themselves also support invariant measures.
Unique ergodicity is asserted only on $A$.

## 4. Minimality, unique ergodicity and the prime-power dichotomy

Approximating arbitrary $x,y\in A$ by points on one sufficiently late
single cycle allows a forward iterate of the first approximant to equal
the second. Isometry preserves its error from $x$, and the ultrametric
inequality bounds the resulting error from $y$. Every forward orbit in
$A$ is dense. The nonempty support of the invariant limit measure is
closed and forward invariant, hence equals $A$.

For each radius tending to zero, the relation $d(x,y)<\eta_j$ is an
equivalence relation on $A$. Its classes are clopen; compactness makes
their quotient $Q_j$ finite. Since $T(A)=A$, the induced action is a
permutation. Minimality forces one quotient cycle. Every invariant
probability must therefore assign each cell mass $1/|Q_j|$. The refining
partitions have mesh tending to zero, so step functions on their cells
approximate continuous functions uniformly. These masses uniquely
determine the probability. No outside unique-ergodicity theorem is
assumed to complete this step.

When $|C_e|=p^e$, sufficiently close Hausdorff approximations yield a
well-defined onto equivariant map from $C_e$ to $Q_j$. The strict radius
inequality and ultrametric inequality ensure independence of the nearby
point chosen in $A$. Thus $|Q_j|\mid p^e$, so $|Q_j|=p^{k_j}$.
One basepoint in $A$ labels every quotient consistently by forward time.
Refinement then gives ordinary reduction maps, not arbitrarily twisted
bonding maps. The resulting map to the inverse limit is injective by
vanishing mesh and onto by nested compact cells.

The integers $k_j$ are nondecreasing. If bounded they stabilize and the
inverse limit is a finite $p$-power cycle, including a singleton. If
unbounded, their powers are cofinal and the limit is $\mathbb Z_p$.
The invariant measure is uniform on every finite quotient, hence Haar.
In the infinite case a point has mass at most $p^{-k_j}$ for every $j$,
which proves non-atomicity. The argument does not assume in advance that
the limit is a Cantor set or has no periodic point.

## 5. Berkovich topology and the optional countable-closure lemma

For a complete algebraically closed ultrametric field, the closed
classical disk in Step 8 is complete, without being assumed compact.
After the general theorem proves compactness of $B$, the evaluation
seminorm map is a continuous injection into the Hausdorff Berkovich
space, hence an embedding on $B$. Restricting any continuous test
function on the Berkovich projective line to $B$ proves the required
weak convergence there. The pushed-forward probability is Radon and
has compact type-I support; it cannot acquire additional nonclassical
support points outside the compact embedded image.

Step 9 is a separate valid assertion without the contact condition.
For a bounded countable classical set $D$, its closure $\mathcal C$ in
a closed Berkovich disk is compact. To check the claimed separating
family, take distinct $x,y\in\mathcal C$. Their seminorms differ on
a polynomial. Algebraic closedness and factorization give a linear
factor $z-b$ on which they differ. Choose $t$ strictly between the two
values and use density of $D$ on the smaller side to obtain $a\in D$
with $|a-b|<t$. Then

$$|z-a|_x\le\max\{|z-b|_x,|a-b|\}<t,
\qquad |z-a|_y=|z-b|_y>t.$$

Thus the countable family $x\mapsto|z-a|_x$, $a\in D$, really does
separate all points of $\mathcal C$, including nonclassical ones. Its
map into a countable product of bounded intervals is an embedding by
compactness. This proves metrizability of this closure only; it does not
assume a countable dense subfield of $K$, or assert metrizability of the
whole Berkovich line from separability of an arbitrary subset.

The optional subsequence consequence is correspondingly sound:
probabilities on $\mathcal C$ admit weakly convergent subsequences,
and their limits are invariant and supported on the tail closure
$\mathcal Y$. Unique ergodicity of $T|_{\mathcal Y}$, if independently
proved, would force full-sequence convergence. Step 9 does not supply
that missing unique-ergodicity hypothesis on its own.

## 6. Conditional quadratic interface and direct aperiodicity

The map $P(z)=(1+s)z+z^2$ has
$P(x)-P(y)=(x-y)(1+s+x+y)$. On the disk of radius
$R=|s|^{(p-1)/p}<1$, the second factor has absolute value $1$.
The disk is invariant as well, since $|P(x)|=|x|$ there. Hence the
complete-space isometry hypotheses really apply to the stated cycles.

The A1 assertion (MC2) has exactly the same all-$e>d$ quantifier and
finite average $c_d$ as D1's (AC$'$). Taking one summand at least the
average gives a pair of distance at most $|s|^{c_d}$; the sign reversal
from $0<|s|<1$ is correct. Since $c_d\to+\infty$, this yields the
uniform contact criterion and all the claimed convergence bounds.
No compatible choice of pair orientations or nested splitting fields
is required. This implication is accepted here; the derivation of
(MC2), including finite multiplier valuations and transport to every
allowed field, remains assigned to E2.

The strengthened aperiodicity argument uses the finite equality, not
just its divergent lower bound. Fix $d$, $e>d$, $\beta\in S_d$,
$\alpha\in S_e$, and $h=v(\beta-\alpha)$. The points
$P^{jp^d}(\alpha)$ form a subset of size $p^{e-d}$ of $S_e$.
Every one has contact $h$ with $\beta$, because $P^{p^d}$ fixes
$\beta$ and is an isometry. All remaining contacts are at least
$r=(p-1)/p$ since both points lie on the radius-$R$ sphere. The exact
fraction is $p^{e-d}/p^e=p^{-d}$, giving

$$c_d\ge p^{-d}h+(1-p^{-d})r,
\qquad h\le U_d=p^dc_d-(p^d-1)r<\infty.$$

Thus the distance from each fixed old cycle to every later cycle is
at least $|s|^{U_d}>0$. Passing to the Hausdorff limit excludes
$A\cap S_d$ for every fixed $d$. A finite limit of period $p^k$,
$k\ge1$, would equal the unique cycle $S_k$ in the open unit disk,
a contradiction. A singleton limit is impossible because the fixed
points are $0,-s$, whereas $A$ remains on the closed sphere of radius
$R>|s|$. This proves the nonatomic $\mathbb Z_p$ alternative under
the very same finite average identity, with no added isolation theorem.

The retained isolation alternative is valid under its separately stated
hypothesis: a periodic point in $A$ would be approached by distinct
higher-period points, contradicting isolation. The characteristic-$p$
root-of-unity observation used in discussing multipliers is correct.
This optional route is not needed by the direct bound above and is not
being used to mask an unverified multiplier assumption.

## 7. Abstract top-level-matching control

The finite/infinite word metric is an ultrametric: it is determined by
first disagreement, counting termination as a disagreement. Its radii
$\rho_j\to0$ give total boundedness. A nonstationary Cauchy sequence
has successively consistent prefixes of arbitrary length, so its limit
is an infinite word; terminated words are isolated. This verifies
completeness and compactness.

Addition by one preserves the length of the common prefix, including
a truncation boundary, and is an isometry. In the product with the
invariant bit, the selected subspace is closed because every excluded
finite word with the wrong bit is isolated. Finite words of each length
$e$ give exactly one cycle of length $p^e$ in the prescribed bit.
Infinite words give no finite cycles: a positive integer cannot be zero
modulo every power of $p$.

Since $\rho_1<\eta<\rho_0$, the first digit supplies the same $p$
top-level clusters across all levels. Adding $p^j$ changes the digit
following exactly $j$ unchanged digits, giving the claimed internal
distance $\rho_j$ for $j<e$. Nevertheless the continuous bit function
has alternating cycle integrals. Uniform masses on finite prefix
cylinders and the bound $\rho_e\to0$ verify the two stated subsequence
Haar limits. In particular, opposite-parity levels stay at distance at
least $\eta$, so they do not satisfy the contact criterion.

The example refutes the stated abstract inference from internal return
control and stable top-level matching to convergence. It is not presented
as the quadratic polynomial, an arithmetic contact counterexample, or a
counterexample to the general theorem.

## Source applicability, remaining gates and receipt

The actual primary source statements used for the boundary check were:

- [Lindahl–Rivera-Letelier, arXiv:1311.4478v3](https://arxiv.org/html/1311.4478v3):
  Problem 1.3 has the stated complete, algebraically closed, odd-characteristic
  field and multiplier quantifiers. Theorem C and its $q=1$ discussion
  supply the single optimal cycles; the characteristic-$p$ specialization
  gives their common sphere. Corollary 1.1 supplies the optional isolation
  statement only for irrationally indifferent periodic points. These
  source inputs do not assert the new cross-level contact formula.
- [Baker's lecture notes](https://swc-math.github.io/aws/2007/BakerNotesMarch21.pdf),
  Section 1.2 and Theorem 2.3.2, with surrounding hypotheses: the seminorm
  topology, classical inclusion and compact Hausdorff analytic background
  apply. Their displayed compactness proof uses a product of bounded
  seminorm coordinates. No blanket ambient metrizability assertion is
  imported; metrizability of the particular closures is proved locally
  in D1.
- [Hurder–Lukina, Sections 2.2–2.3](https://homepages.math.uic.edu/~hurder/papers/93manuscript.pdf):
  the inverse-limit and uniform invariant-measure mechanism is classical
  for minimal equicontinuous Cantor actions. This is source subtraction,
  not a substitute for D1's proof, which also handles the finite alternative.

The source checks establish applicability of these stated inputs, not
current priority or the absence of a later solution. That search remains
outside this review. No claim about target Euler factors, root numbers,
automorphy or a Hilbert–Pólya realization follows from this source-system
measure result.

The proof-writer guidance kept original hypotheses, derived topology and
the conditional arithmetic application distinct. Research-review guidance
supplied a nonauthor proof and source-applicability audit. The current
batch's internal-agent rule supersedes older external-model examples.

New write: only this review. Mathematical executions, new agents, external
model calls, frozen-file changes, shared-index edits, Git actions and
manuscript/PDF work: **0**. The author was notified that no proof edits
were requested. The remaining gates are E2's arithmetic verdict and the
coordinator's separate source-priority/admission decision.
