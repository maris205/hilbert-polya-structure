# C428 — first actual nonauthor manuscript review

2026-09-09 UTC. Reviewer: coordinator, not the IH6 proof or C428 manuscript
author. This is a separate actual-manuscript review after the earlier proof
admission. It is current-team internal AI-assisted review, not human peer
review, a worldwide-priority finding, or a final-release approval.

## Verdict and required disposition

The all-degree, double-sign theorem has transferred correctly into the
article. No mathematical gap in its analytic reduction, finite certificate
dependency, or realization direction was found. One concrete pseudocode
representation defect must be corrected before the second manuscript pass:
P1 below. It is a migration defect, not a failure of the frozen executable
certificate. One minor bibliography correction P2 should be made alongside it.

**Analytic/certificate theorem must-fix: 0. Manuscript algorithm-interface
must-fix: 1 (P1). Minor presentation correction: 1 (P2).** The reviewer
adopts both corrections. No new mathematical execution is justified by either.

## Actual object and coverage

Frozen PDF: `papers/C428_integer_period_spectrum/main.pdf`, 16 pages,
387701 bytes, SHA-256
`d5aeb4ae86009dc9f229a54c50083ccb03eba1f3bdc562d13a12400140dd8cde`.
The `builds/initial_03/source.tar` hash is
`8b39c36f7186e3754818ee139793165bfd55844208b483b64f6b2bf62e664adc`.
The actual pseudocode source hash is
`78c1719d5e43b9cf54d609f9f0f562290fc7930f0c57c10225ee6556b2047d69`;
bibliography hash:
`bbbc3f5900b74e563556d856c742d0982f041126f8443daab47e34da7e82be42`.

All 15 active manuscript inputs were read in full: main, bibliography,
seven sections, two appendices and four tables. The entire extracted
16-page PDF text was read, including a separately requested segment after
combined tool output was truncated. All 16 individual current page images
were actually viewed. README, SOURCE_AUDIT and BUILD_LEDGER were read.

The earlier admission included full reading of the six-file author package,
the independent 337-line checker and contract, the full 336-line review,
the 114-line run receipt and all 611 output lines. This manuscript pass
separately reread the author small-diameter program, relevant independent
algorithm source, receipt and author execution ledger for the migration.
It compared all ten small-diameter rows, both six-row symbolic tables,
eleven witnesses and the recorded three-run evidence boundary. The earlier
full code/proof reads remain provenance; they are not labelled new executions.

## Claim-by-claim audit

| Actual location | Result and decisive checks |
| --- | --- |
| Theorem 1.1 / Section 1 | The domain is the whole integer lattice, with all `p in Z[t]` of degree at least two and both unit Jacobian signs. The two displayed sets are unions across coefficient families, not every polynomial's spectrum, coexistence list or point atlas. The original single-factor clock is retained. |
| Lemma 2.1 | Translation subtracts `(a+1)m` and preserves the coefficient ring and native period. Endpoint divisibility makes `q` integral in `[-2,2]`; two monic divisions give `h in Z[t]`. Both actual and secant values lie in an interval of length `2D`, giving the absolute remainder bound. Congruences apply only to actual selected letters. |
| Lemma 3.2 | At `D=10` the middle bound remains strict. A selected letter in `[4,D-4]` forces every possible nonzero endpoint remainder to vanish. Position 3 rules out the opposite cluster in a nonaffine orbit; both endpoint clusters have cross-distance at least six, exceeding the possible difference four. The three exhaustive templates, including missing letters and the common nonzero two-ended value, follow. |
| Lemma 3.3 | The centroid is a rational affine fixed point, sufficient for a necessary period restriction. The companion matrix gives orders dividing 3, 4, 6 for the three elliptic slopes; the two unipotent cases give 1 or 2. For negative sign, nonzero slope gives two distinct real non-roots of unity; zero slope gives an involution. |
| Lemmas 4.1–4.3 | Integer Newton coefficients are necessary by monic division and sufficient by expansion. Adding a vanishing monic polynomial realizes degree at least two, including singleton alphabets. Every allowed output comes from `E+aE`, not merely its interval hull. Complete partial-function graph traversal imposes no orbit-length cutoff. The 35778 restrictions through diameter nine are exactly the proof prefix, not the author's extra diameter-ten layer. |
| Lemma 5.1 | Every edge equation is affine in the diameter. Identity edges and all integral roots at least ten partition the entire infinite parameter range; alphabet collisions cannot occur in the proved templates. Roots 10, 11 and 12 are actual outputs, not a chosen cutoff. |
| Lemma 5.2 | Template congruences are explicitly necessary overapproximations, not interpolation sufficiency. Intercept representatives cover every actual endpoint output. Necessary-output pruning uses an intersection of finite root sets when no identity exists. Independent unpruned scope covers all 9020 identity graphs and 512 exceptional graphs. The four generic cycles are negative-sign two-ended period-four cycles, not a positive-sign period-four count. |
| Section 6 / Table 4 | All eleven displayed words close under `p(x_i)=x_(i+1)+a*x_(i-1)` and have distinct adjacent ordered states. Repeated scalar letters are allowed. The negative eight-cycle is checked in the native map, not its square or a quotient. The witnesses prove union realizability only. |
| Appendix B | The highest Lagrange coefficient equals the next Newton coefficient even in alternating-extreme order. Exact fractional weights give the required congruence. The indegree-peeling proof accounts for partial-function exits and tails; the retained graph is a disjoint cycle union by edge counting. The controls test nonintegral interpolation and full-support extraction, not just some return. |
| Sections 1.1 and 7 | Pezda's general period bound, C417's positive spectrum/endpoint framework, and elementary methods are subtracted. The increment is the complete arbitrary-degree remainder-congruence and interpolation extension with both signs. No rational quadratic conjecture, point-count bound, Euler factor or spectral target is claimed. |

The actual source programs and their historical reconstruction remain the
finite proof dependencies. Their correctness is not inferred from hashes.
No source certificate was executed during this manuscript review, and no
new experiment or guessed upper diameter is being introduced.

## Corrections

### P1 — explicit coordinate-keyed maps in pseudocode (required)

In Appendix A.2, `EXTEND` emits an ordered list `values`, but
`SMALL_CERTIFICATE` passes it directly as the argument `v` of `FULL_CYCLES`.
Appendix A.1 then reads `v[y]` with `y` an actual coordinate in `E`.
For a nonconsecutive alphabet such as `(0,2)`, list index 2 is not the
second stored value. The frozen author implementation correctly constructs
`val = dict(zip(alphabet, values))`; the underlying certificate is unaffected.

Make the interface unambiguous throughout the appendix:

- State that `v` is a map keyed by actual integer letters, not list positions.
- After each emitted list construct `v := {e[j]: values[j] : 0 <= j < k}`
  and call `FULL_CYCLES(E,v,a)`.
- At a numerical exceptional diameter construct the map
  `v := {u(D): V[u](D) : u in U}` explicitly.
- Clarify that a template emits its remainder map keyed by affine letters
  in `U` (thus the right-hand letter `D-b` receives the selected `h[b]`).
  In the optional pruning loop, iterate over values of `V`, not an
  implementation-dependent iteration over dictionary keys.

These are representation clarifications of the already-proved algorithm;
do not modify or rerun the frozen executable evidence. The second pass must
check the actual revised PDF and the whole pseudocode interface, not only
whether the word “dictionary” was inserted.

### P2 — duplicated years (minor)

References [4] and [5] on PDF page 15 each print `9 September 2026, 2026`.
Remove the duplicated year from their descriptive publication fields while
retaining a single bibliographic year and the actual date. No source
ownership, title, path, or unpublished/internal status should change.

## Bounded primary-source and citation checks

The current primary [Kim et al. v2 text](https://arxiv.org/html/2412.01668v2)
was reopened. The version header, introduction and Theorems A–B, Section 4.1's
explicit leading coefficient `1/d!`, and Section 5's Theorem 5.1 and displayed
proof support the narrow coefficient-ring comparison. The HTML display date
is not the deposited version date. No whole-paper or figure inspection is
claimed from these targeted reads.

The official [open-problems Section 11](https://armj.math.stonybrook.edu/html-articles/Files-2015-2024/23-70/index.html)
was reread through the displayed arithmetic questions and conjectures;
Conjecture 3 is explicitly about rational points of the quadratic negative-sign
map over Q. The [publisher record](https://link.springer.com/article/10.1007/s40598-024-00252-x)
confirms credited author, title, 2024 issue year, volume 10, pages 585–620
and DOI. A guessed alternate journal URL failed before the actual recorded
official URL was used; this was a lookup failure, not a source contradiction.

The [DML-CZ record](https://dmlcz-proxy.ics.muni.cz/handle/10338.dmlcz/120574?show=full)
confirms Pezda's title, abbreviated name, journal, year, volume, issue and
pages. The earlier primary full-text source audit supplies its precise
Theorem 2.1 and local special-cycle scope; no new full PDF read is claimed.
All seven bibliography items are cited. Four are internal working sources
(57.1%); this exceeds the selected citation-audit flag threshold, but their
predecessor/proof/evidence roles justify retention. This is internal-source
concentration, not verified personal self-citation. Retraction, competing
interest and venue checks remain unperformed, not PASS.

## PDF/build observations and remaining gate

The current final engine and BibTeX logs have no Warning/Error/Overfull/
Underfull/undefined match. All 19 font resources are embedded Type 1 with
Unicode mappings. The full 16-page view found no clipped equation, missing
table row, code collision or unreadable continuation. References ending on
a lightly filled page 16 are intentional, not a failure. The three preserved
initial builds, their real layout changes and the ASCII shell-option repair
are accurately recorded; they are not the final identical-input pair.

After P1 and P2: preserve the baseline, record the complete source diff,
build the real revision, inspect its text/pages, then obtain the separately
authorized second manuscript pass. Formal Route A evaluation, final fresh
double build and release/Git gates remain pending. This report alone was
written; no manuscript, old proof, program, global registry or Git object
was modified by this review.
