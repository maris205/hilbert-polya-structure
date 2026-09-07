# C414 nonauthor manuscript review

Date: 2026-09-07 02:31 UTC.
Reviewer: current-team scout_henon_arithmetic, not an author of the
C414 manuscript or its height proof. The reviewer authored the
separate cubic C417 manuscript. This is an independent internal
manuscript review, not human journal peer review.

## Verdict

**PASS / CLOSED — no required manuscript repair.**

The actual article faithfully typesets the accepted complete
polynomial-point height theorem, with its assumptions, exhaustive
degree-valley argument, coefficient-uniform multiplicities, sector
summation, all combined poles, meromorphic boundary and lattice-sensitive
real-height asymptotic. No missing parameter case, pole cancellation,
unjustified exchange or strengthened domain was found.

The additional periodic-remainder explanation in the double-pole proof
is valid and makes the required implication explicit. The prior
source-provenance corrections remain incorporated. A prior proof PASS
was not treated as automatic approval of the manuscript: the complete
current TeX, bibliography and nine-page PDF text were read and checked.

No mathematical script or LaTeX build was run by this reviewer.
Only this review file was written. Formal evaluation, two fresh final
builds, final every-page visual inspection, release sealing and Git
integration remain separate coordinator-owned gates.

## Inputs actually read

Read completely:

- main.tex, all seven included section files and references.bib;
- CITATION_AUDIT.md and AUTHOR_HANDOFF.md;
- all text extracted directly from the actual nine-page main.pdf;
- the frozen 379-line HEIGHT_PROOF_PACKAGE.md, the complete
  HEIGHT_SOURCE_AUDIT.md, my original full REVIEW_HEIGHT_PROOF.md
  including its source-fix closure, and HEIGHT_EXACT_CHECK_REPORT.md.

The relevant final TeX/BibTeX logs were scanned read-only for warning,
undefined-reference/citation, overfull, underfull and error entries:
there were no matches. Ripgrep's no-match exit 1 is not a build failure.
The PDF is nine pages and 355,639 bytes. Its current main/PDF/Bib/log
hashes match the author handoff. The seven section inputs all resolve,
and all four bibliography entries are actually cited.

The source comparisons rely on the primary text sections actually read
in the earlier independent review, reread here through its exact record.
I did not repeat the author's new DOI metadata requests or claim a new
full-text access to Hsia or final Ingram/Takehira versions. No page image
was rendered or visually reviewed in this manuscript check.

## 1. Scope, degree valleys and arithmetic multiplicities

Section 2 retains every prime power q, every degree d at least two,
every polynomial f of that exact degree over F_q, and every nonzero
constant a. The domain is F_q[t]², not F_q(t)². Canonical heights
are measured in units of log q and are the sum of the forward and
backward limits. The series counts actual polynomial points by height,
not periodic orbits, scheme lengths or an orientation quotient.

The degree comparison in Section 3 uses only nonzero leading coefficient
and a. It is valid when the characteristic divides d and when f is
inseparable. A nonconstant bi-infinite orbit cannot have two consecutive
degree-zero coordinates; the constant square is invariant under both
map and inverse. Failure to escape in a remaining direction would
produce an infinite decreasing sequence of nonnegative degrees.
This proves both-sided escape, existence of a global degree minimum,
and injectivity of the ordinary integer-time labeling.

At a strict minimum, unequal neighboring degrees have maximum d times
the minimum and give the unique open-cone edge. Equal neighbors give
the turn, including a degree-zero middle coordinate. The plateau case
gives one positive edge. The outward geometric patterns exclude another
edge or turn in the same orbit. Thus the representative census is
disjoint and exhaustive; it is not a local definition silently assumed
to cover all points.

Lemma 3.2 has the correct height normalization: an edge has
(hhat-minus,hhat-plus)=(m,n), and a turn has (M,M/d). Its two
equal minimum total heights at shifts 0 and 1 correspond to two
different points, not two representatives. The same patterns prove
naive height at most canonical height and bounded-height finiteness.

For M=dr, the strict turn portion is (q−1)q^((d+1)r) and the
equal-leading-degree portion is (q−1)(q−2)q^((d+1)r).
Their sum is exactly (q−1)²q^((d+1)r). At q=2 only the
boundary portion vanishes. For M=dr+j with 1≤j<d, the number
of possible second coordinates is q^(r+1), giving the other row
of (2.4). No division by a vanishing small-characteristic factor
or separability condition enters the computation.

## 2. Sector summation and normal convergence

The closed tails removed in (4.2) are disjoint for d≥2 and positive
degrees. In (4.3), positive real coordinates along (d,1) and (1,d)
are uniquely split into nonnegative integers and remainders in (0,1].
The remainder is still an integer lattice point with positive
coordinates. Consequently the finite numerator and the two cone
denominators genuinely eliminate the spurious axial singularities.

The turn generating function (4.4) agrees with both residue classes
in (2.4). The symmetries C_−k=C_k and E_(1−k)=E_k yield the
precise weights in (4.6): one C_0 and twice each positive-index
edge and turn sector.

On each compact subset with Re(s)≥epsilon>0, the tail has bounded
A_k and doubly-exponentially decreasing B_k and z_k. Every exponent
of B in the finite cone numerator is positive; the two denominators
tend uniformly to one. This proves locally normal convergence of
the holomorphic tail, leaving only finitely many meromorphic sectors
on the compact set. It justifies continuation and excludes extra
poles; it does not assert normal holomorphic convergence through
the finitely many actual poles.

The coefficient b_j in (4.7) is the exact number of integers strictly
between j/(d+1) and dj/(d+1), including multiples of d+1 and the
small j cases. Its linear growth gives divergence of the absolute
positive series for Re(s)≤1. Thus the exact convergence abscissa
is supported independently of the continuation formula.

## 3. Combined residue and every boundary phase

At level k≥2, distinct L_k imply that only C_(k−1), C_k and E_k
meet the chosen pole. Their coefficients and common weight two
are correctly retained. I checked the three displayed algebraic
steps leading from (5.2) to

    R = (q−1)(q−v)(q−A)(vA−1) /
        ((v−1)(A−1)(q−vA)).

The finite geometric sum uses v^d=q, and the remaining numerator
identity is exact. The modulus inequalities in (5.4) make every
asserted numerator and denominator factor nonzero for every
root-of-unity phase. The derivative of the common denominator is
positive L_k log q at its zero, so (5.5) has the correct sign
and normalization.

At k=1 and w≠1, the two coincident cone denominators in C_0
supply coefficient 2(q−1)²/(w−1), although C_0 itself has
weight one. With the twice-weighted C_1 and E_1 this gives
the same total 2R, not R or 4R. The factor q−vA vanishes
exactly when w=1; otherwise the surviving modulus conditions
prove a simple pole.

For the double-pole case, the new explanation is sufficient:
from the exact b_j formula one has

    rho_j = b_j − ((d−1)/(d+1))j
          = 2{j/(d+1)} − 1.

Thus rho_j is genuinely periodic with period d+1, not merely
bounded. Its generating function has denominator 1−w^(d+1)
and at most a simple pole at w=1. The linear part is
alpha*w/(1−w)². Since w=q^(1−s), its contribution is
(q−1)²(d−1)/((d+1)(log q)²) times (s−s_0)^−2,
as stated in (2.7). The other sectors are at most simple
there and cannot cancel this coefficient.

This covers k=1, all phases, q=2 and d=2. The subsequent
nearest-integer choice of ell_k gives actual poles converging
to every imaginary-axis point. A meromorphic extension across
one such point would inherit an interior accumulation of poles,
which is impossible. The argument concerns the combined function,
not unaggregated summand boundaries.

## 4. Arbitrary real B and the strict exterior gap

Section 6 begins with N=floor(B), so the central edge sum gives
alpha(q−1)q^(N+1)N with an O(q^N) error. Adjacent edge shifts
are correctly bounded by setting e=dn−m≥1 and summing a
geometric progression in n. The remaining e weight is
q^(−(1−1/d)e), which is summable. The central two turn
shifts likewise contribute only O(q^B).

For the other edge shifts, the ratio of m+n to the shifted
height is increasing in m/n for positive k. Its cone supremum
is (d+1)/L_k and is at most alpha_2<1. The first exterior
turn shifts have exactly the same upper ratio. Minimality of
the representative height bounds the core degrees by B; the
displayed lower bounds on shifted heights give only O(log B)
possible times. The polynomial/logarithmic number of terms is
absorbed by the strict exponential gap.

Replacing N by B only in the linear factor costs O(q^B);
replacing it in the exponent would not. The abstract, Theorem
2.3 and proof consistently preserve q^(floor(B)+1)B.
The nonconstant factor q^(1−{B}) therefore follows for real
B, without a single-pole Tauberian assumption.

## 5. Sources, evidence and release boundary

The introduction and citation audit preserve the prior closed
precision fixes: Hsia's published development is distinguished
from the secondary attribution of the definition to Silverman's
unaccessed talk; header and internal manuscript dates are not
silently merged with journal years. Hsia's original full text
and the final Ingram/Takehira proof texts remain outside the
claimed reading. New successful metadata requests are not
promoted to full-text access.

Canonical-height construction, scaling, local escape and generic
cone summation remain credited as established tools. Kawaguchi's
one-orbit naive-height scope and Takehira's one-variable finite
discrepancy partition are not invoked outside their hypotheses.
The equal-degree edge counterexample to a bounded additive
discrepancy applies on the stated entire domain.

The eleven-case, 77,974-pair diagnostic is reported exactly as
a prior finite check, not a proof of prime-power or infinite
parameter quantifiers and not a newly reproduced experiment.
All necessary infinite arguments are present in the article.
No source height series, pole divisor or counting exponent is
promoted to target Euler factors, root numbers, automorphy,
target divisor matching or a Hilbert–Pólya realization.
NO_BAD_EULER_OR_ROOT_NUMBER remains unconditional.

No required change was found; no affected-revision cycle is needed.
The current review closes the nonauthor manuscript gate only.

## Exact reviewed identities

| Current manuscript input | SHA256 |
|---|---|
| main.tex | 1944b5a5b8275c8ce296bb59499a5ff5b84295b67d522c8081087a4746cc17b6 |
| references.bib | f39b2c2588908287103bb78dd40b57195799d35f1f3bcbb9fccf2b5ec0cd7fb8 |
| main.pdf | 23f41109cd6fa6f3c5f4eb209f1274ed4a45c77dd4ab34d3257dcd0d245267fe |
| sections/1_introduction.tex | abcd57bf98d12a0002a5dbe97f5167ac857c8a4c1ec2f432356405e892562642 |
| sections/2_statements.tex | 1a154a3d6099066891b7afded962b9638c8d4d7b37aa3476729cf271fd40cd89 |
| sections/3_valleys.tex | ddd5b8bd28f98c7921d1491e144374b2727640f648a1525e72a49cb9728be4e0 |
| sections/4_series.tex | 13b55130f40796a37e5e852413c760e838db32a71414a6ca366396ef3fe1a5d1 |
| sections/5_poles.tex | 9258a0bdeebb44174a581af790d7bf6e5767eb4f640252116ff034ca68dea6cb |
| sections/6_counting.tex | 4e727afc7cd2ffb6ef45e62c50b6e011fa3c77f226042ac5ce9f36dfdb5f310a |
| sections/7_scope.tex | c1bbd439636798485fef145db5baf9de461f5d28b50c3e48d23d60dca28177c6 |
| CITATION_AUDIT.md | 48eeaacce491e2654a6c8c130dd822e66bfc16f1e569c90fffabf1953194d804 |
| AUTHOR_HANDOFF.md | d782a20437f039f404d690dd3b5ee371e3d261a87b5f3d10e4660a045b90177a |

The frozen proof hash remains
fc2fd3acdcbd1695997cecf02aaf6024e224fb89918777775ac95111a77d7ae7;
the source-fix-closed audit remains
32ded9aa931d95ccd5374b4df947b91c5b5a1a6efdd2495deab3883dfb9f13fc;
the original review with closure is
e6437f12b739d68ef29116dd2775aa476732618b93802b9524cfb0fe1e55af6a.
Those identities were checked read-only; no frozen file was modified.
