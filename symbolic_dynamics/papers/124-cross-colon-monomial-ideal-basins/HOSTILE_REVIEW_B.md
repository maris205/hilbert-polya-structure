# Hostile Review B — repaired round 1

**Paper:** P124, “Cross-Colon Dynamics on Rectangular Monomial Ideals: Complete Basins and a Four-State Contact Transfer”  
**Role:** independent nonauthor hostile reviewer B  
**Artifact reviewed:** repaired round 1 and its support package, not the superseded round-0 support text  
**Review date:** 2026-08-30

## Verdict

**GO for the internal mathematical, computational, and artifact gate.**  
**STOP: no.**  
**External status: HOLD.**

The paper’s stated theorem package is internally supported. I found no theorem counterexample, missing boundary case, verifier/canonical-output mismatch, build defect, PDF defect, or anonymity leak. Review A’s two minor support-document findings have been repaired at the correct anchors, including the explicit P107/P104 firewall. The remaining HOLD is external and non-corrective: the direct-owner/prior-art search is necessarily bounded and must be independently cleared before any novelty or submission claim is released.

### Severity counts

| Severity | Count |
|---|---:|
| CRITICAL | 0 |
| MAJOR | 0 |
| MINOR | 0 |

No actionable manuscript or artifact correction is identified in this review.

## 1. Scope, independence, and frozen artifacts

I did not author this paper or Review A. I audited the current source, proofs, support files, both verifier implementations and their canonical transcripts, the supplied PDF artifacts, and a fresh isolated build.

The following PDF artifacts are intentionally byte-identical:

| Artifact | Bytes | Pages | SHA-256 |
|---|---:|---:|---|
| main.pdf | 293,617 | 5 | 3dd3316a0abbc504a65c6214bc52d4a439a4e16f8290ca655b7fcece2b501f81 |
| main_round1.pdf | 293,617 | 5 | 3dd3316a0abbc504a65c6214bc52d4a439a4e16f8290ca655b7fcece2b501f81 |
| main_round0_original.pdf | 293,617 | 5 | 3dd3316a0abbc504a65c6214bc52d4a439a4e16f8290ca655b7fcece2b501f81 |

That equality is not evidence that the repairs were omitted: Review A’s findings concerned support-document anchors and provenance/firewall language, not the theorem text, code, or rendered paper. IMPROVEMENT_LOG.md records this distinction consistently.

## 2. Review-A repair closure

Both Review-A findings are closed.

| Review-A item | Required repair | Round-1 evidence | Review-B result |
|---|---|---|---|
| MINOR 1 | Correct the sharp-depth and layer/ballot claim anchors | CLAIMS_EVIDENCE.md now points the square/non-square sharp maximum-depth claim to **Theorem 3.2**, and the layer identity plus terminal ballot count to **Theorem 5.1** | **Closed.** The named theorem statements contain the corresponding claims; the old nonexistent/misassigned anchors are gone. |
| MINOR 2 | Add an explicit internal-project firewall for P107 and P104 | CONTROL_RESULTS.md and NARRATIVE_REPORT.md explicitly distinguish P107’s annihilator-power map on ideals of \(\mathbb Z/N\mathbb Z\) and P104’s random \(2\times2\) contraction cocycle from P124’s cross-colon monomial-ideal map | **Closed.** The distinctions are substantive, not merely title-level. |

The README and BUILD notes correctly describe the package as a round-1 internal freeze with the support-only repairs applied and an external HOLD retained.

## 3. Hostile mathematical audit

### 3.1 State space and the operator

The paper works in
\[
R_{a,b}=k[x,y]/(x^a,y^b),\qquad
T(I)=x(I:y)+y(I:x).
\]
For monomial ideals, the exponent set is an upper set in the \(a\times b\) grid. The staircase encoding
\[
I=\langle x^iy^j:j\ge h_i\rangle,\qquad
b\ge h_0\ge\cdots\ge h_{a-1}\ge0
\]
is bijective, including the empty column convention \(h_i=b\). The number of such states is therefore \(\binom{a+b}{a}\).

I checked the literal quotient-ring membership law against colon formation. Multiplication by \(y\) can enter an ideal either through the predecessor \((i,j-1)\) or because \(y^{j+1}=0\) at the top boundary; multiplication by \(x\) has the analogous right boundary. This gives the paper’s equation (2.5), including the quotient-annihilation source terms. No polynomial-ring colon rule is incorrectly substituted at a truncated boundary.

### 3.2 Staircase recurrence: equations (2.1)–(2.4)

For \(a\ge2\), the claimed height update
\[
\begin{aligned}
h'_0&=\min(b,h_1+1),\\
h'_i&=\min\{\max(0,h_{i-1}-1),h_{i+1}+1\},\quad 1\le i\le a-2,\\
h'_{a-1}&=\min\{\max(0,h_{a-2}-1),1\}
\end{aligned}
\]
follows from the literal OR of the two predecessor conditions. The endpoint caps encode the annihilating top/right boundaries correctly. For \(a=1\), direct evaluation gives \(T(I)=(y)\) for every monomial ideal, as separately stated; the generic recurrence is not improperly used in this degenerate strip.

On a total-degree diagonal, the update is
\[
(G_dw)_s=w_{s-1}\lor w_{s+1},
\]
with a left source exactly when \(d\ge b\) and a right source exactly when \(d\ge a\). The source-band table is correct:

- \(d<m=\min(a,b)\): length \(d+1\), no sources;
- \(m\le d<M=\max(a,b)\): length \(m\), exactly one source;
- \(M\le d\le a+b-2\): length \(a+b-1-d\), two sources.

The middle band is absent precisely for \(a=b\).

### 3.3 Path dynamics: Lemma 3.1

I checked all four source types and the short-path exceptions.

- With no sources and \(n\ge2\), sufficiently long walks preserve only vertex parity. The recurrent states are the two constant parity classes and the two alternating checker states; the checker states form the nontrivial 2-cycle. The maximum transient depth is \(n-2\).
- With no sources and \(n=1\), the only recurrent state is \(0\), and the maximum depth is \(1\). This exception is necessary and is present.
- With exactly one source, every vertex is reached after its source-distance with the required parity padding, so the unique recurrent state is the all-one word and the maximum depth is \(n\).
- With two sources, the unique recurrent state is again all one, with maximum depth \(\lceil n/2\rceil\).

The walk-reachability proof handles parity through two-step backtracking and does not silently assume a loop. Direct exhaustive verification for every word of lengths \(1,\ldots,14\) and all source types independently agrees with the lemma.

### 3.4 Recurrent ideals and sharp global depth: Definition 3.1 and Theorem 3.2

The checker ideals
\[
C_r^\epsilon=
\langle x^iy^j:i+j>r\ \text{or}\ (i+j=r,\ i\equiv\epsilon\pmod2)\rangle,
\qquad 1\le r<m,
\]
are genuine upper sets because every monomial above the checker diagonal is included.

The recurrent classification is exhaustive:

- the fixed ideals \(\mathfrak m^r\), \(1\le r\le m\);
- the checker pairs \(C_r^0\leftrightarrow C_r^1\), \(1\le r<m\).

Thus there are \(m+2(m-1)=3m-2\) recurrent states and no periods beyond \(1\) and \(2\). The compatibility step is sound: the first nonzero recurrent diagonal is either full or a checker; every higher diagonal must be full by upward closure, and the exceptional single-vertex source-free diagonal cannot create an omitted recurrent family.

The sharp maximum entrance depth is also correct:
\[
\max_I\tau(I)=
\begin{cases}
m,&a\ne b,\\
\max(1,m-2),&a=b=m.
\end{cases}
\]
For a nonsquare rectangle, the one-source band has length \(m\), and the zero ideal attains the bound. For a square, the longest source-free contribution is \(m-2\), while the two-source contribution is at most \(\lceil(m-1)/2\rceil\), which is bounded by \(\max(1,m-2)\). The witnesses named in the proof cover all square boundaries: the unit ideal for \(m=1\), the zero ideal for \(m=2\), and \((y^{m-1})\) for \(m\ge3\).

Because \(T\) acts independently on total-degree diagonals, a state enters the recurrent set exactly when all its diagonal projections have entered their compatible recurrent patterns. Taking the maximum of the diagonal entrance times is therefore justified; no cross-diagonal timing term is omitted.

### 3.5 Complete basin classification: equations (4.1)–(4.5) and Theorem 4.1

Let \(\nu(I)\) be the first occupied total degree and \(S_r(I)\) the set of \(x\)-exponents occupied on that first diagonal. The cases in Theorem 4.1 are mutually disjoint and exhaustive:

- for \(m=1\), every ideal belongs to the sole basin of \(\mathfrak m\);
- the unit ideal and the \(\nu=1\) mixed-parity case form the basin of \(\mathfrak m\);
- for \(2\le r<m\), \(\nu=r\) with both parities present converges to \(\mathfrak m^r\);
- \(\nu\ge m\), including the zero ideal, converges to \(\mathfrak m^m\);
- \(\nu=r\) with \(S_r\) confined to one parity converges to the checker 2-cycle at level \(r\).

The unit boundary \(\nu=0\) is treated separately and satisfies \(T(R)=\mathfrak m\). On a first source-free diagonal, exact walks preserve and eventually expose precisely the parity support; all later sourced diagonals fill. This proves both attraction and exclusion from the other basins.

The eventual phase statement
\[
T^t(I)=C_r^{\epsilon+t\bmod2}
\]
for sufficiently large \(t\) uses the parity of the initial first trace and has no unaccounted phase offset. The independent basin verifier checks this exact clock after a burn-in longer than every proved depth bound.

### 3.6 Staircase transfer and counting: equations (5.1)–(5.8) and Theorem 5.1

The staircase/path correspondence runs from \((0,b)\) to \((a,0)\), hence counts \(\binom{a+b}{a}\) ideals. For a fixed \(1\le r<m\), the four transfer masks—empty, even-only, odd-only, and mixed—record contacts with the barrier \(i+j=r\). The start and endpoint are off this barrier because \(r<m\le a,b\), so no endpoint convention is hidden.

The recurrence \(F_{i,j}^{(r)}\) correctly takes its predecessor from west or north and unions in the parity bit exactly when the arrival vertex lies on the barrier. The barrier translation is exact:

- \(\nu(I)\ge r\) iff \(h_i\ge r-i\) for every relevant \(i\);
- equality \(h_i=r-i\) records a first-diagonal monomial and contributes its \(i\bmod2\) bit.

Consequently,
\[
\begin{aligned}
|\mathcal B(\mathfrak m)|&=1+A_1^M=2,\\
|\mathcal B(\mathfrak m^r)|&=A_r^M,\qquad 2\le r<m,\\
|\mathcal B(\{C_r^0,C_r^1\})|&=A_r^E+A_r^O,\\
|\mathcal B(\mathfrak m^m)|&=\binom{a+b}{a}-\binom{a+b}{m-1}.
\end{aligned}
\]
For \(m=1\), the separate sole-basin formula is used.

The reflection/ballot count is correct. Paths avoiding the barrier give the required \(\binom{a+b}{m-1}\) complement, and differencing successive barrier thresholds yields
\[
A_r^E+A_r^O+A_r^M
=\binom{a+b}{r}-\binom{a+b}{r-1}.
\]
The layers telescope with the unit and terminal cases to \(\binom{a+b}{a}\), so the basin formulas partition the entire state space.

The claimed \(O(abm)\) arithmetic cost follows from running the \(O(ab)\) four-mask dynamic program for each \(r<m\); \(O(ab)\) storage is attainable by reusing the table between levels. The worked \((a,b)=(5,7)\) basin totals
\[
2,10,9,45,38,116,90,185,297
\]
sum to \(792=\binom{12}{5}\), and the reported even/odd checker-phase splits sum to their cycle-basin totals.

## 4. Boundary audit

| Boundary | Result |
|---|---|
| \(a=1\) or \(b=1\) | The special strip dynamics and sole-basin statement are explicit and agree with literal quotient arithmetic. |
| Square \(a=b\) | The one-source band disappears; the square depth formula and its \(m=1,2\) exceptions are correct. |
| Nonsquare \(a\ne b\) | The one-source band has length \(m\) and gives the sharp depth \(m\). |
| \(m=1\) | No checker level exists; all ideals enter \(\mathfrak m\). |
| \(m=2\) | The only checker level is \(r=1\); the square maximum depth is \(1\). |
| \(r=1\) | The unit ideal is separated before the first-trace partition; the fixed-basin size is \(2\). |
| \(r=m-1\) | The last checker/power layer is included exactly once. |
| \(r=m\) | It is terminal rather than a checker layer; the ballot complement formula applies. |
| \(I=0\) | \(\nu(0)=\infty\), placing zero in the terminal basin. |
| \(I=R\) | \(\nu(R)=0\), and \(T(R)=\mathfrak m\). |
| Empty/full/checker diagonal words | All source and length-one exceptions agree between the proofs and exhaustive verifier. |
| Transposition \(a\leftrightarrow b\) | Counts are preserved, with the expected parity-label swap for checker phases. |

No off-by-one, missing empty case, or duplicated basin was found.

## 5. Verifier and canonical-transcript audit

I ran both verifier sources freshly with bytecode generation disabled and compared stdout byte-for-byte with the frozen canonical files.

### 5.1 Core verifier

| Item | Result |
|---|---|
| Source | code/verify_alg_cross_colon.py |
| Source SHA-256 | 950953523155868efec1491e69038b1d30c33249b1df2daa7881c74012242cbf |
| Frozen output | code/ALG_CROSS_COLON_CANONICAL.txt |
| Output SHA-256 | b924e05c5e9ac71a25fb668d5bc2033f6ab58c325c7c73642a4dd0b096d67deb |
| Fresh status | PASS |
| Byte comparison | Exact match |
| Assertions | 1,469,669 |

The implementation derives literal multiplication and colons in the quotient grid, separately implements the staircase and diagonal updates, and compares all three representations. It exhausts every path word of lengths \(1,\ldots,14\) for all four source types and every monomial ideal for \(1\le a,b\le9\), totaling 184,736 ideals across 81 rectangles.

The advertised assertion count is reproducible from the code:

- path assertions: \(11\sum_{n=1}^{14}2^n+4\cdot14=360{,}482\);
- per-ideal rectangle assertions: \(6\cdot184{,}736=1{,}108{,}416\);
- rectangle/family assertions: \(771\);
- total: \(360{,}482+1{,}108{,}416+771=1{,}469{,}669\).

The checks cover literal/staircase/diagonal equality, state closure, the fixed and checker recurrent classification, absence of other cycles, all depth values, sharp maxima, and the boundary witnesses.

### 5.2 Basin verifier

| Item | Result |
|---|---|
| Source | code/verify_alg_cross_colon_basins.py |
| Source SHA-256 | 51ca13655933b869ce8e4b12c868d550a107496c013136e2e5fa18ad9b481f22 |
| Frozen output | code/ALG_CROSS_COLON_BASINS_CANONICAL.txt |
| Output SHA-256 | bdfd3e041b9f641101436c40918adbba59fd14b1f1381d77fa943ce00c0c76ff |
| Fresh status | PASS |
| Byte comparison | Exact match |
| Assertions | 265,987 |

This program does not import the core verifier. It reimplements the quotient-grid arithmetic and independently compares actual functional-graph attractors with the first-trace classification. It exhausts all 48,602 monomial ideals for \(1\le a,b\le8\), checks the transfer counts against enumeration, verifies the exact checker phase, then checks transfer/reflection/layer identities and transposition behavior through \(1\le a,b\le30\).

The count also reconciles internally:

- small-rectangle block: 219,775;
- large transfer grid: 46,198;
- final \((5,7)\) example evaluation: 14;
- total: \(219{,}775+46{,}198+14=265{,}987\).

The fact that the two check functions alone account for 265,973 assertions is not a mismatch: the program’s final example call deliberately contributes the remaining 14 before printing the frozen total.

### 5.3 Combined ceiling

\[
1{,}469{,}669+265{,}987=\boxed{1{,}735{,}656}.
\]

Both canonical files are therefore genuine transcripts of the supplied sources, and the strengthened combined assertion claim is exact. Exhaustive finite-grid testing does not replace the proofs outside those grids; the paper and support files appropriately use it as an independent control rather than as a universal proof.

## 6. Isolated four-stage LaTeX build

I copied only main.tex and references.bib into a fresh temporary directory and ran:

1. pdflatex;
2. bibtex;
3. pdflatex;
4. pdflatex.

All four stages exited successfully. The final log contains no LaTeX, class, or package warnings; no undefined citations or references; no rerun request; no overfull or underfull boxes; and no errors. BibTeX reports no warning or error and resolves all nine bibliography entries. The isolated PDF is 293,617 bytes, has five pages, and has SHA-256

    3dd3316a0abbc504a65c6214bc52d4a439a4e16f8290ca655b7fcece2b501f81

which exactly matches main.pdf and both archived round PDFs.

## 7. Five-page visual and PDF audit

I rendered and inspected every PDF page at high resolution.

| Page | Content checked | Result |
|---:|---|---|
| 1 | Anonymous title and abstract; scope/claim boundary; operator; start of staircase formalism | Clean; no clipping, collision, malformed equation, or identity leak |
| 2 | Proposition 2.1; literal and diagonal rules; source-band table; Lemma 3.1; checker definition | Clean and readable |
| 3 | Theorem 3.2 and proof; basin invariants; Theorem 4.1 and proof | Clean and readable |
| 4 | Staircase transfer; mask recurrence; Theorem 5.1; reflection argument; complexity; example lead-in | Clean and readable |
| 5 | Table 1; computational controls; conclusion; all nine references | Clean and readable |

Table 1 floats to the top of page 5 after its page-4 discussion; the reference resolves and the placement is not ambiguous. There are no blank pages, clipped margins, overlapping objects, broken glyphs, orphaned display fragments, or unreadably small table cells.

Technical PDF checks:

- A4, portrait, five pages, PDF 1.5, unencrypted;
- no embedded files, JavaScript, signatures, forms, or raster images;
- Title, Author, Subject, and Keywords metadata fields are blank;
- no metadata stream or custom metadata;
- no creation/modification dates, filesystem paths, usernames, email addresses, affiliations, ORCID identifiers, TODO markers, or draft markers found;
- all 23 reported font subsets are embedded and have Unicode mappings;
- all nine citation keys resolve to nine bibliography items.

The PDF is anonymous at both visible and metadata levels.

## 8. Ownership, novelty ceiling, and internal-project firewall

### 8.1 Direct-owner search

Exact and near-exact searches for the operator \(x(I:y)+y(I:x)\), “cross-colon” monomial-ideal dynamics, iteration, attractors, and basin classifications returned no direct owner of this exact map or theorem package in the bounded search performed for this review. The nearest located literature concerns broader monomial dynamical systems, general basin-cylinder algebra, or static/power colon ideals. For example, Austin and Dinwoodie’s [Monomials and Basin Cylinders for Network Dynamics](https://doi.org/10.1137/140975929) is methodologically adjacent but does not own this cross-colon scheduler.

This is a **bounded non-hit, not proof of novelty**. Search-index incompleteness, unpublished work, different terminology, and very recent literature remain uncontrolled. Therefore the external HOLD remains mandatory.

### 8.2 Zero-credit owner subtraction

The paper correctly assigns no novelty credit for standard ingredients:

- monomial ideals as upper sets and staircase/path encodings;
- quotient-ring colon arithmetic;
- Boolean path dynamics, fixed points, cycles, and generic basin/depth language;
- ballot/reflection counts and elementary dynamic programming;
- generic rowmotion/toggle terminology.

The creditable claim ceiling is the synthesis specific to this scheduler: the exact local rule including quotient-boundary sources, the full recurrent classification, the sharp square/nonsquare entrance depths, the first-trace basin theorem with phase, and the exact transfer/reflection counts.

### 8.3 Explicit P107/P104 firewall

The repaired support files state the internal distinctions explicitly, and direct inspection confirms them:

- **P107** studies \(I\mapsto\operatorname{Ann}(I)^r\) on ideals of \(\mathbb Z/N\mathbb Z\), reduced by CRT valuations and a clipped reflection. It does not contain P124’s bivariate truncated monomial grid, cross-colon operator, diagonal source scheduler, checker cycles, or basin transfer.
- **P104** studies a random \(2\times2\) contraction cocycle and its spectral/folded fluctuations. Any shared “monomial” or “toggle” vocabulary is generic; it has no ideal lattice, colon operation, OR path map, or basin enumeration.

Generic cycles, depth, basins, ideals, toggles, or monomials do not constitute ownership of P124’s operator or theorem package. Conversely, the internal firewall does not establish external novelty; it only prevents inappropriate intra-corpus credit leakage.

## 9. Final hostile disposition

### Actionable findings

None.

### Gate

- **Internal correctness:** GO.
- **Proof boundary coverage:** GO.
- **Verifier reproducibility and canonical bytes:** GO.
- **Combined 1,735,656-assertion accounting:** GO.
- **Isolated build and five-page PDF:** GO.
- **Fonts, references, metadata, and anonymity:** GO.
- **Review-A repair closure:** GO.
- **Internal P107/P104 ownership firewall:** GO.
- **External direct-owner/novelty clearance:** HOLD.

**Final decision: GO internally; do not lift the external HOLD until an independent, dated prior-art search clears the exact operator and theorem package.**
