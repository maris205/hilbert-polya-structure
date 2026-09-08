# Arithmetic continuation: primary-source and ownership audit

Search/retrieval date: 2026-09-07 UTC. Scope: the two frozen candidates in
[FROZEN_CONTRACTS.md](FROZEN_CONTRACTS.md), not a global novelty
certificate. The outcomes and the retained local calculation are in
[SCOUT_REPORT.md](SCOUT_REPORT.md). No source manuscript was uploaded to
an external review service.

## Retrieval and search record

The current environment offered no callable Zotero or Obsidian connector.
The relevant existing local proofs were read first. Primary arXiv HTML,
author/institutional PDFs and publication metadata were then retrieved.
“Read” below means the specifically identified theorem and its defining
hypotheses, not a claim to have independently verified every proof in a
whole paper. Preprints are labelled as such, not treated as peer-review
certificates. Search snippets and abstracts are leads unless an actual
statement was opened.

The following eleven distinct query formulations were actually submitted
in this continuation. They are a representative record, not a claim that
these were the only searches or that all literature was exhausted.

| Lane | Fresh query |
|---|---|
| ED1 | `"Lattes" "joint" "periodic" density elliptic` |
| ED1 | `"elliptic curves" "quadratic twist" "distribution" "2-adic"` |
| ED1 | `"GL(2" "det" "1" "Haar" elliptic valuation` |
| ED1 | `"Density of periodic points" "Lattès" 2024 2025 2026` |
| ED1 | `"joint distribution" "elliptic" "twist" "finite fields" group orders` |
| ED1 | `"2-adic images of Galois" Rouse Zureick-Brown theorem "1208"` |
| ED1 | `"The 1-eigenspace for matrices" "GL" Lombardo Perucca` |
| ED2 | `"basilica" "periodic points" "finite fields"` |
| ED2 | `"x^2-1" "periodic points" "log" primes` |
| ED2 | `"postcritically finite" "periodic points" "uniform" finite fields` |
| ED2 | `"Bridy" "Jones" "Kelsey" "Lodge" "periodic"` |

ED1 was frozen before its new diagnostic. The ED1 early simplicity
decision and the ED2 contract were written before the ED2 queries.
Subsequent title/author searches followed the primary-source citation
chain into January and August 2026, so the stopping decision is not based
only on older 2013–2022 literature.

## ED1: exact imported ownership and remaining content

### L1 — Bell et al.: the finite-field Lattès counting formula

[Density of Periodic Points for Lattès maps over Finite Fields,
arXiv:2103.00074v1](https://arxiv.org/html/2103.00074v1), 2021 preprint;
Theorem 1.2 and Lemmas 2.2–2.3 were read. The later journal record is
distinct; the author list in v1 was not silently merged with it.

The theorem assumes an elliptic curve over `F_q` and multiplication
integer `d` coprime to `q`. It counts ordinary points on `P^1(F_q)` in
terms of the prime-to-`d` parts of the curve and its quadratic twist,
with an explicit Hasse-size correction. ED1 has `d=2` and good odd
primes, so these hypotheses hold. This source owns the entire exact
finite-field bridge. Its extension-field progressions are not a prime
weak law, and we do not attribute the particular joint Haar generating
function to this theorem.

### L2 — Lombardo–Perucca: open-image Haar algorithms

[The 1-eigenspace for matrices in GL2(Z_l), author/institutional
PDF](https://arpi.unipi.it/retrieve/e0d6c92e-36b5-fcf8-e053-d805fe0aa794/1Eigenspace-second-ArXiv.pdf),
also [arXiv:1612.02845](https://arxiv.org/abs/1612.02845).
Theorems 1–2 and Remark 5, PDF pages 1–3, were read.

For any open subgroup of `GL_2(Z_l)` or of a Cartan normalizer, Theorem 1
gives a finite procedure for all Haar masses of possible one-eigenspace
group structures. Theorem 2 gives explicit full-`GL_2` masses. This owns
the one-eigenspace/marginal determinant valuation machinery and its
elliptic reduction interpretation. It does not, as stated, give the
joint pair for `g-I` and `g+I`. ED1's residual is that dependence, which
the elementary residue calculation makes too short for this batch's
independent-paper requirement.

### L3 — Rouse–Zureick-Brown: non-CM 2-adic images over Q

[Elliptic curves over Q and 2-adic images of Galois,
primary published-paper PDF](https://d-nb.info/1118128559/34), 2015.
Corollary 1.3 and the associated introductory hypotheses were read.

For non-CM elliptic curves over `Q`, it classifies 1208 possible 2-adic
images; each contains the level-32 kernel, and its index divides 64 or
96. This already owns the finite catalogue needed for an image-by-image
table. ED1 deliberately fixes full image, and no existing-image table
is offered as a replacement contribution. A classification of Galois
images is not itself a periodic-proportion limiting law.

### L4 — Juul–Kurlberg–Madhu–Tucker: prior prime-varying Lattès work

[Density of periodic points in reductions of maps over global fields,
author PDF](https://kurlberg.github.io/eprints/Paper1005.pdf),
Example 7.3, PDF pages 21–22, was read.

The example treats a fixed `E/Q`, prime-multiplication Lattès maps and
Galois-image/Chebotarev conditions yielding small periodic proportions
along primes; the surjective full-image situation is explicitly
discussed. Thus using prime variation and elliptic Galois images is not
a new mechanism. The example is not attributed the precise full joint
distribution computed in this scout.

### L5 — Gekeler: relevant lead, insufficient theorem access

[Frobenius distributions of elliptic curves over finite prime fields,
EMS source](https://ems.press/content/serial-article-files/25986), 2006.
The source and its discussion of group-structure distributions were
identified, but follow-up retrieval of the needed exact theorem failed.
This entry is therefore **lead / ownership risk**, not a verified
theorem-level collision. No formula or applicability assertion in the
scout depends on this access gap. ED1 is already rejected by its short
residual, without claiming an exhaustive novelty certificate.

### L6 — March 2026 Lattès work: different question and family

[Panraksa–Samart–Sriwongsa, Arithmetic exceptionality of Lattès maps,
arXiv:2603.25014](https://arxiv.org/abs/2603.25014), March 2026 preprint.
Theorem 2 was inspected in the primary v1 text. It concerns arithmetic
exceptionality for a CM class-number-one setting, with its stated
discriminant restriction, not ED1's non-CM full-image joint prime law.
It was not promoted to an exact collision merely because its title
mentions Lattès arithmetic.

### L7 — Local ownership deducted without rerunning it

The existing [CM_DENSITY_PROOF.md](../../arithmetic/CM_DENSITY_PROOF.md)
was read. Its CM Frobenius decomposition, prime weak-law passage and
tail reasoning belong to the prior AR3 screening result, which was
itself not admitted merely for obtaining a mean/weak law.

The local C382 [ANALYTIC_PROOF.md](../../../henon_cm_elliptic_frobenius_phase_zeta_route_a/proof/ANALYTIC_PROOF.md)
was also read for the Gaussian CM source arithmetic and its boundary.
Its path is recorded here only as a read-only dependency. Neither file,
its checker, its status, nor the admitted M1/AS2 artifacts were changed
or re-evaluated. ED1 does not republish those arguments under non-CM
terminology.

## ED2: theorem hypotheses and quantifier audit

### B1 — Pink: arithmetic/geometric distinction is unavoidable

[Richard Pink, Profinite iterated monodromy groups arising from
quadratic polynomials, arXiv:1307.5678v3](https://arxiv.org/pdf/1307.5678v3),
2013 preprint. Theorems 2.8.2 and 2.8.4, PDF page 42, were read in their
periodic-critical setting.

The geometric group is identified by the periodic critical-orbit
recursion. The arithmetic quotient is described by the cyclotomic
character followed by a diagonal map into copies of `Z_2^*`. For
`x^2-1` over `Q`, the finite critical point has period two and the
cyclotomic image is infinite. Thus the constants extension is not
finite, and replacing arithmetic Frobenius cosets by the geometric
group is invalid. Pink's classification is imported ownership, not
a newly proved ED2 fixed-point contraction rate.

### B2 — Ahmad–Benedetto–Cain–Carroll–Fang: exact arithmetic Basilica

[The arithmetic basilica: a quadratic PCF arboreal Galois group,
arXiv:1909.00039](https://arxiv.org/pdf/1909.00039), checked in its
December 2021 revised text; journal publication is
[Journal of Number Theory 238 (2022), 842–868](https://doi.org/10.1016/j.jnt.2021.10.004).
Lemma 1.2, PDF page 5, and Theorem 5.1, PDF page 18, were read.

For `f=x^2-1`, Lemma 1.2 constructs all 2-power roots of unity in the
inverse tower of a base point outside `{0,-1}`. Theorem 5.1 identifies
the full arithmetic Basilica group over `k(t)` when `char(k)!=2` and
`[k(zeta_8):k]=4`; `k=Q` satisfies both. This supplies an exact tower,
not the proposed `sup_coset FPP_n = O(1/n)` estimate. In particular,
assuming regularity over `Q` at every level would contradict this
verified structural input.

### G1 — Garton: the attractive all-prime effective theorem does not specialize

[Derek Garton, Periodic points of polynomials over finite fields,
arXiv:2103.16533v3](https://arxiv.org/html/2103.16533v3), December 2021
revision. Theorems 3.4 and 5.6 and the disjointness definition were read.

Theorem 5.6 gives effective growing-level image/FPP control over global
fields under several hypotheses, including a `phi`-disjoint subset `C`
of rational critical points with at most one omitted critical point.
The required distinctness includes different iterate times of the same
critical point. For `x^2-1`, the critical points on `P^1` are `0` and
infinity; both are periodic, so neither can belong to such a subset.
No `C` meets the complement condition. Theorem 3.4's fixed-level
specialization framework does not by itself remove the all-level
constants/coset issue. The paper's averaged quadratic-family bounds
are not a bound for this fixed polynomial at all primes.

### G2 — Bridy–Jones–Kelsey–Lodge: prime liminf is the stated conclusion

[Iterated monodromy groups of rational functions and periodic points
over finite fields, arXiv:2107.10310](https://arxiv.org/pdf/2107.10310),
first posted in 2021; the inspected PDF is dated 7 March 2022.
Theorems 1.4–1.5 and 3.11 were inspected with their
hypotheses.

Theorem 1.5 treats PCF, non-dynamically-exceptional maps over number
fields under its listed prime-degree / monodromy / polynomial
conditions. The conclusion is a prime-norm **liminf** of periodic
proportions equal to zero, not an all-prime rate. The fixed-finite-field
result in Theorem 1.4 assumes strictly preperiodic finite critical
points and a square-field condition; Basilica's periodic critical
point fails the former. These are not interchangeable quantifiers or
critical portraits. No strengthening of these statements is imported.

### F1 — January 2026: geometric classification still gives a prime liminf

[Jorge Fariña-Asategui and Santiago Radi, Fixed-point proportion of
geometric iterated Galois groups, arXiv:2601.16173v1](https://arxiv.org/html/2601.16173v1),
22 January 2026 preprint. Theorem 2 and Corollaries 3–4 were read.

Theorem 2 classifies the geometric fixed-point proportion for tame
polynomials, isolating the Chebyshev cases. Corollary 3 is explicitly a
prime-norm liminf over a number field, zero exactly outside the stated
prime-power Chebyshev conjugacy cases. In degree two, `x^2-1` has a
period-two critical point and is not conjugate to that Chebyshev
portrait, so the liminf conclusion applies. It remains weaker than
ED2's every-prime effective decay. The theorem is not an arithmetic
coset-uniform rate and is not presented here as peer-reviewed fact.

### F2 — August 2026: the arithmetic corollary requires finite constants

[Santiago Radi, The inverse Galois problem of iterated Galois groups
and their fixed-point proportion, arXiv:2608.14524v1](https://arxiv.org/html/2608.14524v1),
14 August 2026 preprint. Corollary 3 was read, including its constants
extension and martingale assumptions.

Its arithmetic conclusion assumes
`K^sep intersection K_infinity(f,t) / K` is finite, along with the
stated tameness/martingale conditions (and extra conditions in the
exceptional case). B1–B2 show that the finite-constant condition fails
for the Basilica over `Q`. Therefore this corollary cannot be cited as
closing ED2, irrespective of its usefulness for other rational maps.
The broad abstract about geometric groups does not override this
explicit arithmetic hypothesis.

### F3 — Another January 2026 extension result: branch is a hypothesis

[Jorge Fariña-Asategui, Arboreal Galois representations of rational
functions: fixed-point proportion and the extension problem,
arXiv:2601.19414v1](https://arxiv.org/html/2601.19414v1), 27 January 2026
preprint. Theorem 2 was read. It proves finiteness of the constants
extension under a branch-group hypothesis. That hypothesis cannot be
inserted without proof for the Basilica; indeed it would conflict with
the infinite-constants conclusion B1–B2 here. This is an applicability
boundary, not a new group-theoretic non-branch theorem claimed by this
scout.

### F4 — Self-similar group progress is not an automatic coset estimate

[Fariña-Asategui–Radi, On the fixed-point proportion of self-similar
groups, arXiv:2503.00185v2](https://arxiv.org/html/2503.00185v2), revised
11 August 2026; [BLMS publication record](https://doi.org/10.1112/blms.70368).
Theorem 1 was read. Its super-strong-fractal group hypothesis yields
zero fixed-point proportion. That is a qualitative statement for the
specified group; a rate uniform across an infinite arithmetic quotient
does not follow merely by renaming it. No claimed correction to older
work is repeated from its introductory citations without inspecting
the underlying source.

## Other leads deliberately not used as proofs

[Penkov–Stoll, Prime numbers and dynamics of the polynomial x^2-1,
author PDF](https://mathe2.uni-bayreuth.de/stoll/papers/Penkov-problem.pdf),
2025: the abstract and introductory pages concern prime divisors of
integer forward orbits, a different observable. No periodic-proportion
theorem is attributed to it.

[Heath-Brown, arXiv:1701.02707](https://arxiv.org/abs/1701.02707): the
retrieved abstract concerns recurrence lengths under critical-orbit
assumptions, not the total periodic count for all odd primes in ED2.
Only lead-level access is claimed here.

## Final confidence and exclusion ledger

ED1's finite formula bridge and general marginal Haar ownership are
verified. The precise displayed joint rational expression is a local
calculation, not assigned to a source that does not state it. The
substantive-content rejection does not require proving it appeared
previously. The Gekeler access limitation remains explicit.

ED2's infinite-constant obstruction to the regular/geometric shortcut
is supported by two primary structural sources. The recent geometric,
liminf and finite-constant arithmetic statements were checked at their
actual hypotheses. No inspected theorem supplied both missing estimates
in the frozen all-prime contract. This records an unclosed route in a
bounded scout, not a claim that no such result exists anywhere.

No target Euler factor, root number, automorphy, zero correspondence or
Hilbert–Pólya assertion is licensed by any source in this audit. The
standing `NO_BAD_EULER_OR_ROOT_NUMBER` boundary is unchanged.
