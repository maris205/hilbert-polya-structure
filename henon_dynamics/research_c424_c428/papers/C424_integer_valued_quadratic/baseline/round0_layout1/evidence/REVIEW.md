# AM1 independent proof, certificate, and increment review

2026-09-08 UTC. Current-team nonauthor review under the repository batch
adaptation of `research-review`. No external model or human-peer-review
claim. Final review artifacts are confined to this review directory;
the author producer was read, never imported or executed. No admission,
TeX, Git mutation or formal Route-A evaluation is authorized by this report.

## Verdict

**Mathematical verdict: complete computer-assisted classification, with
no blocking proof or certificate defect found.** The all-integer-parameter
theorem, sharp bound/equality locus, exact period set and pushforward to
every integer-valued quadratic polynomial are justified by the reviewed
arguments and the independent finite-core computation below.

**Increment judgment: recommend one integrated classification contract
for the entire degree-two integer-valued class, not several papers and
not a new-method claim.** This is a result-level extension of C412 with
strong methodological dependence. It is not a literal corollary of C412's
classification, but a short companion treatment that merely displayed the
eleven exceptions would fail the substantive gate. The case for a single
complete paper rests on the natural full-class atlas and its sharp uniform
theorem. This qualitative recommendation is not coordinator admission,
worldwide novelty certification or a prediction of journal acceptance.

## Material actually reviewed

Read the author's PROOF_PACKAGE.md in full, including Step 8; then checked
its updated status/closure pointers. Read FINITE_CORE_CONTRACT.md and the
entire producer source, the full JSON metadata and every parameter record
through lossless compact renderings, the scout/source report and its new
handoff, and the complete CLASSIFICATION.md. Independently read C412's
classification, complete annulus/six-symbol reduction, local-word proof,
and sharp-bound section from its actual TeX source; no old code or PDF
build was run. Exact source accesses are recorded below.

| Reviewed artifact | SHA-256 |
| --- | --- |
| Author CLASSIFICATION.md | `0ceaf810ce1ed7d4ec868d350a0e59c45e7a492764cdcb65cddb7453657bd6b5` |
| Author PROOF_PACKAGE.md | `e3c979b66d2d151c3d5b82be7cbc4f6acbab332d68fef7280d28be11987828fa` |
| Author finite contract | `20abae0a2d2755578f535656f31db00de74d3121b9a47935ce2c2b040f524350` |
| Author producer, read not run | `f80ffcf177fd7a8e98b8ea4d3112b7cca5ef986b5725025e70c836aa088132a0` |
| Author exact output | `44ccf0f5d062587eb07d2837c455a9c3843c3ce0b9e0c8df033d2223d227196a` |
| Independent checker | `b5953b44db6042a81cff542972566499f02aff698ffc1048966e25e0b43cb29b` |
| Independent output | `17561a62401766018f68baf75e3439d33f04e6cba7c5c6f5c398e5263618e842` |

## Analytic claims audit

| Claim | Independent check |
| --- | --- |
| Rational periodic points of F_a are integral | At any prime, the coordinate of maximal norm >1 has a uniquely dominant quadratic term. At two its norm is 2M^2, versus 2M for the linear term. No cancellation loophole remains. |
| Normalization | Substitution in u=x/2+1/4 gives H_(a/2+7/16), on the quarter-shifted half-lattice. The constant denominator is exactly 16. The five-cycle at a=0 consists of five distinct states. |
| Upper parameter boundary | The summed-square identity forbids a>=2; at a=1 every integral coordinate is 1 or 2, and a coordinate 1 forces both neighbors to be 1. The two fixed points exhaust the boundary. |
| Large negative parameters | At a<=-146, N=-2a-2>=290 gives k>=17 and r>=35/2. The upper annulus bound uses R<r+3 and half-integral rounding. The lower contradiction is 5r-17/2>4r+8, exactly requiring r>33/2. The stated threshold meets it strictly. |
| Exact coefficient separation | The remainder is bounded by 12+abs(s)<=r+23/2<2r. The multiplying coefficient is integral, hence zero. Neighboring signs sum to an even integer, forcing even offsets; division then gives exactly C412's two local equations. |
| Symbol exhaustion and small-index existence | The local cases and cyclic boundaries of periods one and two are covered. The four surviving patterns substitute algebraically for every k>=0. All claimed least periods and the two distinct three-cycles survive k=0. |
| Finite-core completeness | Odd-coordinate division is exact, the stated B_a and S_a contain every periodic coordinate, and the stabilized finite injective restriction is a permutation. This is an exact residual proof, not extrapolation. Independently checked without that algorithm. |
| Sharp17/equality and period set | The infinite classified region has at most six points; the complete finite core has maximum17 only at a=-1. At that parameter two four-cycles and one nine-cycle are disjoint. Every claimed period occurs. |
| All integer-valued quadratics | Newton-basis coefficients m,n,r are integral and m!=0. For m even the stated nonzero rational scaling reaches C412. For m odd the affine shift q and A=mr+(3q-q^2)/2 are correct, including negative m. Rational coordinates, counts and least periods are preserved; original coordinates need not be integral. |

At overlapping symbolic parameters the cycle lengths distinguish different
rows, and the within-row distinctness arguments are valid. The exceptional
four-cycles at -11 and -1 are not their symbolic four-cycles. Consequently
the indicator formulas C_d(a) have no missing subtraction. The return and
finite-orbit zeta formulas are ordinary consequences, not separate results.

## Independent finite computation

The check was frozen first in
[INDEPENDENT_CHECK_CONTRACT.md](INDEPENDENT_CHECK_CONTRACT.md), implemented
in [check_original_square.py](check_original_square.py), and run once.
It succeeded with exit code zero in approximately 0.21 seconds. It computed
all graphs before loading the author's result and recorded both input hashes.

For all 147 parameters a=-145,...,1, use original coordinates on the fixed
square {-19,...,19}^2. The independent real bound is
M^2-5M-290<=0, which forces integer M<=19 since the polynomial is positive
at 20 and increasing thereafter. There is no filtered alphabet, doubled
coordinate transformation, pruning iteration or period cutoff. Path-index
functional-graph traversal retains every cycle suffix and processes every
vertex once. Escapes terminate paths rather than being counted as cycles.

[INDEPENDENT_RESULTS.json](INDEPENDENT_RESULTS.json) records all original
periodic states and oriented words. The run processed 223,587 graph vertices
and matched every full cycle/state set at every parameter, not just totals:

- 306 periodic states and 113 oriented cycles across the 147 different maps;
- least periods exactly {1,2,3,4,5,6,7,9,10};
- largest periodic set 17, attained only at a=-1;
- all author period labels, cycle/point counts and summary fields agreed.

These are finite dependencies made exhaustive by the analytic reduction.
The large-parameter theorem was checked analytically, not tested by running
more large negative parameters. The author producer's detailed pruning
trajectory was inspected but not independently rerun; the differing full
graph algorithm supplies an independent endpoint/completeness certificate.

## Source and predecessor subtraction

The C412 classification has monic integral quadratic coefficients and
native periods only 1--4. Its local six-symbol theorem, maximum argument,
annulus strategy, finite partial-permutation machinery and elementary
coordinate normalization are fully deducted. Step 8 is an adaptation of
that engine, not a new symbolic method. The integer-valued Newton-basis
classification is elementary. Neither the count17 nor a list of exceptional
cycles is by itself a new proof mechanism.

External primary sources were checked afresh on 2026-09-08:

| Primary source | Actual access and scope |
| --- | --- |
| [Kim--Krieger--Postolache--Szeto v2](https://arxiv.org/html/2412.01668v2) | Read introduction/Theorems A--B, integer-valued construction definitions, Sections 3.3--3.4 and Section 4 opening. The Hénon long-cycle construction assumes growing odd degree. Section 3.4's quadratic compression statement is one-dimensional, not AM1's two-dimensional atlas. |
| [Pezda original journal record and PDF](https://dml.cz/handle/10338.dmlcz/120574) | Record verified. Browser PDF failed; a read-only curl-to-pdftotext stream read the cover and first three printed pages, including definitions and Theorem2.1. Its maps have coefficients in Z, not merely values in Z. No saved local PDF or whole-proof inspection. |
| [Hénon problems, Section11](https://amj.math.stonybrook.edu/html-articles/Files-2015-2024/23-70/index.html) | Read the general number-field boundedness questions and explicit quadratic sign convention. The particular displayed Ingram period conjecture uses +x, determinant -1; AM1 has -x, determinant +1. No claimed solution of those general conjectures. |

Four actual fresh query strings: `"Henon" "integer-valued quadratic" periodic`;
`"Hénon" "triangular" "17" periodic`; `"Henon" "y(y+1)" periodic`;
`"Hénon" "7/16" periodic`. Their mostly irrelevant returns are not evidence
of worldwide absence. Read-only source retrieval used the actual PDF link
from the verified Pezda landing page, not a guessed citation. No subscription
source's unseen theorem was assumed.

## Why the result-level increment survives, and its limit

There are two separate judgments here. First, this is not a direct use of
the C412 theorem on a renamed lattice: the exact five-cycle at a=0 excludes
a rational conjugacy of that map to any C412 member. The missing branch
has genuinely different return data, and its entire parameter range needed
a new, explicitly checked lattice-to-symbol reduction plus a complete
residual certificate. Second, that proof is strongly derivative: almost all
its conceptual machinery is C412's and must be presented that way.

The justification for ONE complete result is the closure of a natural
coefficient class: every degree-two P in Int(Z), not a chosen finite
parameter perturbation, now has a full Q-periodic atlas, a uniform sharp
bound with an exact coefficient equality locus, and an exhaustive native
period list. This completion is stronger than an enlarged finite table or
the statement that the same old graph algorithm terminates for each P.
The bounded review found no theorem that supplies that full conclusion by
immediate substitution. It does not certify global priority.

I therefore support a single integrated theorem-centered contract, while
rating the methodological increment low and the full-class result increment
meaningful. If presented only as another coefficient-family computation,
or if its inherited symbol theorem were advertised as new, my substantive
recommendation would be negative. Do not split the nonmonic normalization,
sharp bound, return zeta, or exceptional periods into separate paper slots.

## Required presentation boundaries and minor cleanup

No mathematical fix is required by this review. Before any manuscript:
identify the finite computation as a proof dependency; cite/deduct C412
at the actual reduction; state Int(Z), degree exactly two, all rational
points, determinant +1 and native time in the main theorem. Preserve the
complete exception table and exact equality condition. The analytic
package's strategy item5 still says the general-class application is
conditional future work; update that historical wording to point to the
now-complete companion classification. This is documentation, not a
remaining mathematical gap.

No arithmetic-prime trace ownership, target Euler factor, root number,
automorphy, target-zero identity or Hilbert--Polya realization follows.
This is a scoped arithmetic-dynamics classification recommendation, not
an A1/A2 target-success grade. Coordinator admission remains separate.
