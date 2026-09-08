# Arithmetic scout: three frozen candidates

Date: 2026-09-07. Owner: `scout_henon_arithmetic`. All candidates are
AI-generated starting points. **No candidate is admitted, numbered, formally
evaluated, or represented by a manuscript.** This first-pass report is bounded
to three materially different questions. Prior sealed artifacts are read-only.

This initial contract text is frozen before any mathematical CPU diagnostic.
The companion `SOURCE_AUDIT.md` records actual primary-source access and
ownership separately. A finite test cannot prove any all-parameter claim or
prime-density theorem. No target Euler factor, root number, functional equation,
zero correspondence, or Hilbert–Pólya realization follows from these sources.
`NO_BAD_EULER_OR_ROOT_NUMBER` is unconditional.

## AR1: a single bad prime for conservative quadratic Hénon maps

**Complete family and observable.**
`H_c(x,y)=(y,y²+c−x)`, on `Q²`, with `c=A/p^(2e)`, where `p` is any odd
prime, `e≥1`, and `A∈Z` is coprime to `p`. One application is the native
clock; the object is the ordinary rational periodic-point locus, including
least periods and all parameter overlaps, not a local scheme length.

**Paper-level question.** Classify this entire family, beyond necessary
denominator restrictions, by a complete local-to-global periodicity theorem.
The intrinsic arithmetic carrier is the unique bad prime and the rational
orbit lattice after denominator clearing. There is no present target bridge.

**Ownership deducted.** Local C412 already classifies every monic integral
conservative quadratic Hénon map. Pezda's integral-plane period bound is not
a rational-denominator classification. Ingram's well-known concrete period
conjecture concerns the opposite Jacobian sign `(y,x+y²+b)`; it must not be
silently applied here. General canonical-height finiteness is not the desired
uniform classification.

**Cheap decisive check and success condition.** Use the local escape estimate
to obtain denominator restrictions, then ask whether a parameter-independent
finite symbolic reduction actually follows. Success requires a new closure
argument for all `p,e,A`; a finite parameter census or the necessary condition
`−A` square modulo `p` is insufficient.

**Replacement boundary.** Reject from this pass if only the familiar
denominator reduction is available, or if full closure remains an unresolved
global periodicity problem. Do not replace the question by a coefficient
cutoff. No numerical search is authorized or useful at that boundary.

## AR2: all-parameter rational Somos-4 quotient dynamics

**Complete family and observable.** For `α,β∈Q*`, set
`F_(α,β)(u,v)=(v,(αv+β)/(uv²))`. The domain is the maximal two-sided subset
of `(Q*)²` on which every positive and negative iterate remains nonzero and
finite. Its inverse is `((αu+β)/(vu²),u)`. The native clock is one application
of this two-dimensional map, not one four-dimensional Somos update or a
point on a compactification. Count ordinary rational periodic states.

**Paper-level question.** Give an exact rational periodic-locus atlas for all
`α,β`, retaining singular invariant fibers and the excluded orbit domain.
The arithmetic carrier is the rational genus-one pencil and its rational
translation point. The conserved quantity is
`h=uv+α/u+α/v+β/(uv)`; its fiber is
`u²v²−huv+α(u+v)+β=0`.

**Ownership deducted.** Hone and the Somos/elliptic-divisibility literature
already own elliptic translation and the general sigma-function solution;
Mazur owns rational elliptic torsion constraints. Local C390 owns a distinct
Lyness real/rational contrast, while C115 is a bounded McMillan atlas.
Neither relabeling an elliptic translation nor adding a larger rational table
is an independent increment. This is not the other lane's coefficient-free
rank-two two-mutation cluster family.

**Cheap decisive check and success condition.** Compare the exact map and
invariant to the primary Somos-4 source. Success needs a substantial complete
arithmetic/domain theorem left after the imported elliptic and singular
degeneration machinery is deducted.

**Replacement boundary.** Reject if the available mechanism is just elliptic
translation plus known torsion, with no demonstrated independent all-fiber
increment. Do not run a periodic table to manufacture that increment.

## AR3: prime-varying density for every quartic CM twist

**Complete family and observable.** For every `D∈Q*` modulo fourth powers,
normalize `D` to a nonzero fourth-power-free integer, and use the degree-four
Lattès map

`φ_D(x)=(x²+D)² / (4x(x²−D))`

from doubling on `E_D:y²=x³−Dx`. For each odd prime `p∤D`, its domain is
the complete `P¹(F_p)`, with poles mapped to infinity and infinity fixed.
The native clock is one `φ_D` iterate. Define the ordinary periodic fraction
`ρ_D(p)=#Per(φ_D,P¹(F_p))/(p+1)`. The proposed observable is its empirical
probability distribution over good rational primes `p≤X`, for each **fixed**
`D`, as `X→∞`; also its prime mean. No uniformity for growing `D` is proposed.

**Paper-level question and carrier.** Determine the full limiting law for
every twist, with exact atoms, masses, accumulation points, and mean, using
the intrinsic joint 2-adic Frobenius valuations of the elliptic curve and its
quadratic finite-field twist. Resolve all quadratic entanglement classes,
rather than compute a prime sample.

**Ownership deducted.** Bell et al. already prove the exact finite-field
periodic-density formula. Local C382 already gives the base `D=1` primary
Gaussian Frobenius and all extension counts; C180 already gives the complex
Lattès three-channel census. Neither formula is a new claim here. Juul et al.
and the recent arithmetic-exceptionality paper are compulsory external
collisions; fixed-point reduction densities for one chosen infinite-order
elliptic point are a different observable, not interchangeable evidence.

**Frozen pre-proof conjecture (historical status retained).** A possible law has
universal inert atoms `2^(−k)` of mass `2^(−k)`, `k≥2`. The split base atoms
are `1/8+2^(−k−1)`, `k≥3`, with masses `2^(1−k)`. If `D=±square`, keep all
these atoms (predicted mean `1/6`). If `D=±2·square`, replace the `k=3` split
atom by mass `1/4` at `1/2` (predicted mean `47/192`). In all other square
classes, halve the split masses and add mass `1/4` at `1/2` (predicted mean
`1/4`). These assertions require a complete CM ray-class/Chebotarev proof
and fresh ownership review; current status is only a falsifiable hypothesis.

The paragraph above records the pre-diagnostic freeze. Its later author proof
and substantive-increment rejection are recorded in the completed disposition
below; the conjectured formulas themselves were not adjusted to the sample.

**Cheap decisive diagnostic, frozen scope.** For every odd prime `p≤101` and
`D∈{−8,−7,−5,−4,−3,−2,−1,1,2,3,4,5,7,8}`, excluding `p|D`, compare exact
functional-graph periodic counts with the imported elliptic odd-part formula.
Also test the predicted finite-prime reductions: inert trace zero; split
quadratic nonresidue gives `ρ=1/2`; split quadratic residue gives the base
fraction; base split valuations are `{2,k≥3}` with `k=3` exactly at `p≡5 mod8`.
This is an implementation/convention check only, not a test of limiting mass.

**Success condition and replacement boundary.** Recommend at most a separately
frozen bounded proof contract if the diagnostic is consistent and the complete
prime-varying law has a defensible residual increment after source subtraction.
Reject as a paper if the law is already owned, collapses to an immediate known
corollary without substantial new content, or needs an unproved independence
claim. A successful finite sample does not cross this boundary.

## Completed first-pass dispositions

| Candidate | Mathematical outcome | Author recommendation |
|---|---|---|
| AR1 | Necessary local denominator/congruence reduction; no complete all-parameter rational orbit atlas. | **NOT READY; do not assign a slot.** |
| AR2 | Exact map and invariant are expressly covered by Hone's Proposition 2.1. No substantial residual all-fiber arithmetic theorem has been established. | **REJECT SOURCE-HEAVY at the proposed scope.** |
| AR3 | The frozen weak-law conjecture has a complete author proof using imported Bell, C382, and class-field inputs; finite convention diagnostic passes. | **RETAIN AS A SHORT UNNUMBERED COROLLARY; reject as a substantial independent paper.** |

These are lane recommendations, not coordinator admissions or formal Route A
evaluations. The first pass supplies **zero recommended paper admissions**.
No additional candidates, large censuses, manuscripts, or previous-tree reruns
were launched to fill a numerical quota.

### AR1: what the cheap reduction actually proves

For a finite scalar orbit, write
$x_{n+1}+x_{n-1}=x_n^2+c$. At a prime $\ell\ne p$, a maximal orbit norm
$M>1$ would give $|x_n^2+c|_\ell=M^2>M$, impossible. Hence all coordinates
are integral there. At $p$, put $R=|c|_p^{1/2}=p^e>1$. A maximal norm
$M>R$ is impossible by the same comparison; $M<R$ would make the constant
term dominate with norm $R^2>M$. Thus $M=R$. If any single coordinate had
norm less than $R$, its equation would again have left norm $R^2$ but both
neighbors norm at most $R$. Every coordinate therefore has denominator
exactly $p^e$ and can be written $x_n=z_n/p^e$ with $z_n\in\mathbb Z$,
$p\nmid z_n$.

Clearing denominators gives
$$
z_n^2+A=p^e(z_{n-1}+z_{n+1}),\qquad z_n^2\equiv-A\pmod{p^e}.
$$
If solutions exist, the odd-prime unit congruence has exactly two roots,
so all coordinates lie in two residue lattices $\mathbb Z\pm r/p^e$.
This restriction is not sufficient for a periodic orbit. Real escape bounds
can further restrict the coordinates to bounded intervals for each fixed
parameter, but this does not supply the missing complete parameter atlas.
No coefficient or period table was computed. The exact conservative
single-bad-prime classification is **unresolved by this scout**, not asserted
to coincide with a particular named open conjecture. The opposite-Jacobian
Ingram conjecture is explicitly not imported.

### AR2: exact primary collision and the missing residual

Hone, `arXiv:math/0501554v3`, Proposition 2.1, equations (2.4)–(2.6), writes
the very recurrence, invariant, and elliptic solution proposed in AR2.
The later primary exposition also explicitly allows degeneration of the
sigma formula and notes algebraic validity over the coefficient field.
This does **not** certify that every proposed singular-domain atlas has been
written down by a predecessor. It does mean that the current scout has not
identified a substantial theorem beyond imported translation/torsion and
boundary bookkeeping. No all-parameter classification is claimed or silently
completed by treating a rational starting point itself as a torsion point.

### AR3: proof closure is not paper admission

The coordinator authorized a bounded proof after the conjecture was frozen.
`CM_DENSITY_PROOF.md` proves the exact three laws and means, verifies total
mass and disjoint exceptional square classes, resolves
$K(\sqrt D)\cap R_N$ for every $N\ge3$, and proves the infinite-shell step
with omitted prime density at most $3\cdot2^{-M}$. It keeps fixed-parameter
natural density distinct from Dirichlet density and from growing-parameter
uniformity. The law concerns weak limits, not exact equality of finite-prime
fractions to every limit atom.

`cm_density_diagnostic.py` was executed once after the freeze and completed
with exit 0. It checked 344 graph/formula cells comprising 16,540 projective
domain points, plus 178 inert, 94 split-residue, 72 split-nonresidue, and
12 base-valuation identities. The result is recorded in
`CM_DIAGNOSTIC_RESULT.json`; no asymptotic frequencies were fitted.

After Bell's density theorem and C382's primary trace are subtracted, the
remaining proof is a short quadratic-twist and Gaussian residue calculation
with a standard ramification argument and a geometric tail. The new-looking
constants do not by themselves establish a paper-level increment. A complete
research note is retained so the tested idea and its rejection boundary are
reproducible; it is not expanded into a manuscript or offered as three papers.
