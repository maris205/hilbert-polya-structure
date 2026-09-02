# Hostile Review A — rectangular-corner stripping atlas

**Review date:** 2026-09-02 UTC  
**Role:** independent internal non-author cold reader  
**Starting point:** frozen theorem contract and main_round0_original.pdf  
**External state:** HOLD_EXTERNAL

I then read main.tex, every paper-local ledger, references.bib, the author
verifier and its frozen transcript. I did not consult a prior review of this
replacement manuscript, edit an author file, run Git, or transmit manuscript
material to an external model or specialist. The only paper-local write is this
report. Reviewer-owned artifacts are under
docs/papers157_161_sequence/reviews/p160_rcs_a/.

## Verdict

**REVISE — 0 Critical / 2 Major / 0 Minor. HOLD_EXTERNAL.**

No displayed theorem was falsified. The all-time crop, clock, sharp height,
empty and nonempty fibres, shells, image threshold, mass identity, conjugation,
three probes, and worked example survive independent reconstruction. The two
Major findings are:

1. the every-weight proof gives an inadmissible unit-parts witness in
   \(\gamma\); and
2. the provenance boundary omits the direct classical generalized-Durfee-
   rectangle and \(m\)-Durfee-symbol chain, while Table 1 incorrectly leaves
   classical two-boundary factorization inside the scoped residual.

M1 is a real proof gap in a universally quantified headline claim, although a
one-line repair proves the unchanged conclusion. M2 is not a direct-owner kill:
no inspected source owns the full literal-dynamics-plus-prescribed-target
conjunction. It is nevertheless material because it changes what may receive
contribution credit.

## 1. Frozen-contract comparison

| Contract interface | Round-0 location | Result |
|---|---|---|
| positive \(a,b\); all \(t,N\geq0\); empty partition | Sections 1–2 | PASS |
| \(T_{a,b}^t(\lambda)=(\lambda_{at+1}-bt,\ldots)_+\) | Theorem 1, (5) | PASS |
| point clock and rectangle survival | Theorem 1, (6) | PASS |
| unique recurrent state and sharp capped height | Theorem 1, (7) | PASS |
| empty fibre \(E_{at,bt}\) and exact shells | Theorem 1, (8) | PASS |
| every nonempty target and two-factor fibre | Theorem 2, (9) | PASS |
| image iff \(M\leq N\), source at every weight | Theorem 2, (10) | FORMULA PASS / PROOF REVISE |
| coefficient formula and worked example | (12)–(13) | PASS |
| image size and global mass identity | (14)–(15) | PASS |
| conjugation and ordered three-probe recovery | (16)–(20) | PASS |
| no novelty, firstness, or owner-absence assertion | Sections 1 and 6 | PASS |
| complete zero-credit source boundary | Table 1 / source ledger | REVISE |

The manuscript stays inside the algebraic theorem ceiling and uses no forbidden
novelty language. The defects are proof support and contribution subtraction,
not a false display.

## 2. Fresh mathematical reconstruction

### 2.1 Iterates, clock, and \(t=0\)

For a Ferrers cell set \(D(\lambda)\), an \((h,w)\)-crop is

\[
C_{h,w}D(\lambda)
=\{(i-h,j-w):(i,j)\in D(\lambda),\ i>h,\ j>w\}.
\]

Coordinate windows compose additively:
\(C_{h_2,w_2}C_{h_1,w_1}=C_{h_1+h_2,w_1+w_2}\). Thus \(t\)
literal \((a,b)\)-crops equal one \((at,bt)\)-crop and yield (5). At
\(t=0\), the offsets vanish and the map is the identity, including on
\(\varnothing\).

The crop is nonempty exactly when its prospective northwest cell existed:

\[
\lambda_{at+1}\geq bt+1
\iff (at+1,bt+1)\in D(\lambda).
\]

This proves the clock. Every positive crop of a nonempty diagram loses its
northwest cell, so weight strictly decreases; \(\varnothing\) is the only
recurrent state.

### 2.2 Sharp height and \(N=0\)

Survival after rank \(t\) forces the rectangle
\([1,at+1]\times[1,bt+1]\), of area \((at+1)(bt+1)\). Conversely the
rectangular partition \((bt+1)^{at+1}\) realizes equality. Hence the maximum
entry time is the first \(t\) for which this area exceeds \(N\). At \(N=0\)
the first such time is \(0\), and the carrier contains only the already-empty
state.

### 2.3 Empty target, zero windows, and shells

For arbitrary \(h,w\geq0\), the empty condition is
\(\lambda_{h+1}\leq w\). Slice by \(k=\lambda_{h+1}\). At \(k=0\) one
gets partitions with at most \(h\) rows. For \(1\leq k\leq w\), removal of
the forced \((h+1)\times k\) rectangle leaves independently:

- a top excess partition with at most \(h\) rows; and
- a lower partition whose largest part is at most \(k\).

The slice is reversible and \(k\) is recovered from row \(h+1\), proving

\[
E_{h,w}(q)=\frac1{(q;q)_h}\sum_{k=0}^{w}
                 \frac{q^{k(h+1)}}{(q;q)_k}.
\]

The absorbed sets are nested, so consecutive differences are the exact shells
for \(t\geq1\). Boundary reductions are correct:

\[
E_{0,w}=\frac1{(q;q)_w},\qquad
E_{h,0}=\frac1{(q;q)_h},\qquad E_{0,0}=1.
\]

Only \(h=w=0\) occurs dynamically at \(t=0\), but the one-sided zero-window
checks rule out hidden convention errors.

### 2.4 Nonempty target and both inverse directions

For nonempty \(\mu=(\mu_1,\ldots,\mu_r)\), a source maps to \(\mu\) exactly
when

\[
\lambda_{h+j}=\mu_j+w\ (1\leq j\leq r),\qquad
\lambda_{h+r+1}\leq w.
\]

The first \(h\) rows have baseline \(\mu_1+w\); their excesses form
\(\gamma\) with at most \(h\) parts. Rows below the forced middle form
\(\beta\) with largest part at most \(w\). Padding \(\gamma\) to \(h\)
entries and concatenating the top block, the shifted \(\mu\)-block, and
\(\beta\) is a unique weakly decreasing source. Both joins are strict enough:
the first middle row equals the baseline, and its last row is at least
\(w+1>\beta_1\).

The forced mass is

\[
M_{h,w}(\mu)=|\mu|+h(\mu_1+w)+w\ell(\mu),
\]

and the two free series are \(1/(q;q)_h\) and \(1/(q;q)_w\). At
\(h=w=0\) both free pieces vanish and the unique source is \(\mu\). The
artificial \(h=0\) or \(w=0\) cases likewise reduce to one free factor.

### 2.5 Every exact weight: conclusion true, printed witness false

The minimum source uses \(\gamma=\beta=\varnothing\). For excess \(d\geq0\)
at positive time, either of the following is valid:

\[
\gamma=(d),\ \beta=\varnothing,
\qquad\text{or}\qquad
\gamma=\varnothing,\ \beta=(1^d),
\]

with the empty partition at \(d=0\). The first works because \(h\geq1\) and
\((d)\) has one part. The second works because \(w\geq1\) bounds part size,
not the length of \(\beta\). Hence the threshold and every-weight conclusions
are true.

Round 0 instead says to add arbitrarily many parts of size one to
\(\gamma\). That constructs \((1^d)\), which has \(d\) parts and violates the
already-stated bound \(\ell(\gamma)\leq h\) whenever \(d>h\). This explicit
witness therefore fails precisely in the unbounded range it is meant to prove.

### 2.6 Worked fibre and mass identity

For \((a,b,t,\mu)=(2,1,2,(3,1))\), \(h=4,w=2\), and

\[
M=4+4(3+2)+2\cdot2=28.
\]

Convolving \(1/(q;q)_4\) and \(1/(q;q)_2\) gives
\(1,2,5,9,17\) in excess degrees \(0,\ldots,4\), exactly as printed.

All fibres are disjoint and exhaust the source partitions, so coefficientwise
summation proves (15). At \(h=w=0\), its right side becomes
\(1+\sum_{\mu\ne\varnothing}q^{|\mu|}\), again
\(1/(q;q)_\infty\). Exhaustive mass checks through weight 30 pass for all
tested internal and one-sided-zero windows.

### 2.7 Conjugation and recovery

Transposing retained cells exchanges the two offsets, proving
\(T_{a,b}(\lambda)'=T_{b,a}(\lambda')\). Direct substitution gives

\[
m((1))=(a+1)(b+1),\quad
m((2))-m((1))=a+1,\quad
m((1,1))-m((1))=b+1.
\]

The row and column probes therefore recover the ordered pair. Independent
checks for \(1\leq a,b\leq7\) pass.

## 3. Findings

### Critical

None.

### Major

#### M1 — inadmissible \(\gamma\) in the every-weight proof

**Locations:** main.tex lines 224–228; PROOF_PACKAGE.md lines 117–123;
CLAIMS_EVIDENCE.md row B2.

**Required repair:** replace the false unit-parts-in-\(\gamma\) construction
everywhere by either \(\gamma=(d)\) or \(\beta=(1^d)\), explicitly including
\(d=0\). Make the same witness explicit in DERIVATION_PACKAGE.md. No theorem
formula, coefficient, example, or title needs to change.

#### M2 — generalized rectangles and classical two-boundary symbols omitted

**Locations:** main.tex lines 71–83 and Table 1; references.bib;
SOURCE_VERIFICATION.md; the phase-one owner ledger.

The source boundary is materially closer than Round 0 records:

- Gordon and Houten, “Notes on Plane Partitions II,” Journal of Combinatorial
  Theory 4 (1968), 81–99, are credited in the later primary literature with
  introducing the \(m\)-Durfee rectangle.
- George E. Andrews,
  [“Generalizations of the Durfee Square”](https://doi.org/10.1112/jlms/s2-3.3.563),
  Journal of the London Mathematical Society s2-3(3), 563–570 (1971), is the
  direct generalized-Durfee-rectangle source. Later primary work explicitly
  records arbitrary positive rational rectangle ratios and the associated
  rectangle-area/two-Pochhammer terms.
- Chen, Ji, and Zang,
  [“Proof of the Andrews–Dyson–Rhoades Conjecture on the spt-Crank”](https://arxiv.org/abs/1305.2116),
  Section 3, define the \(m\)-Durfee rectangle symbol as two boundary
  partitions around a maximal rectangle and give its area-plus-two-boundary
  mass decomposition.

These records do not state the full fixed RCS operator together with every
arbitrary prescribed southeast target, the separate empty branch, cap support,
and ordered recovery. Thus no Critical direct-owner kill is warranted.
However, generalized rectangles, the static two-boundary symbol, and the
factor \(q^{hw}/((q;q)_h(q;q)_w)\) are classical ingredients, not residual
contributions.

**Required repair:** inspect and directly cite Gordon–Houten, Andrews, and
Chen–Ji–Zang; add verified entries to references.bib and the source ledger.
Move generalized/rational-slope Durfee rectangles, static rectangle survival,
classical two-boundary symbols, and two-Pochhammer rectangle factorization to
the zero-credit column. Rewrite the residual so it begins only at the
integrated literal all-time crop and the **arbitrary-prescribed-target** atlas,
including its distinct empty branch, exact cap support, and ordered recovery.
Keep the bounded-non-hit and HOLD_EXTERNAL language.

### Minor

None.

## 4. Direct-owner and portfolio collision attack

Queries covered the literal row/column deletion, southeast remainder,
prescribed target/tail, generalized/successive/ambient Durfee rectangles, and
Durfee rectangle symbols. Barnes–Savage directly own the \(a=b=1\) local
deletion and Durfee decrement. The sources in M2 own more of the static
rectangle mechanism than Round 0 subtracts.

No inspected record contains the exact conjunction

\[
\text{fixed }T_{a,b}\text{ all-time dynamics}
+\text{ every prescribed target}
+\text{ separate empty branch}
+\text{ cap support and oriented recovery}.
\]

The outcome is BOUNDED_NONHIT, not novelty or owner clearance.

The P1–P161 title/keyword/occupancy scan found no internal same-map collision.
The closest occupied paper is P113, principal-hook partition dynamics: it uses
the same integer-partition/Ferrers carrier, but regroups diagonal hooks and
preserves weight on each \(\mathcal P(n)\). RCS deletes a global coordinate
window, strictly loses weight, and absorbs at \(\varnothing\). Their weight
behavior and recurrent loci exclude a literal conjugacy. P126 splits
compositions; P148 contracts parity levels of plane trees; P156 uses Ferrers
boards for permutation fibres; none transfers the RCS theorem. P157–P159 and
P161 have different arithmetic, stochastic-graph, parity-pruning, and affine-
geometry carriers. The retired BST P160 is historical negative evidence, not a
live collision.

The internal SYSTEM_COLLISION_FIREWALL should add P113 as the closest carrier
comparison; this documentation repair is bundled with M2 and is not a separate
Minor.

## 5. Exact controls

The author verifier was replayed three times. Each reports:

    RCS VERIFY parameters=((1, 1), (2, 1), (1, 3), (2, 2), (3, 2))
    EXHAUSTIVE source_weight<=32 target_weight<=9 times=0..5
    ASSERTIONS 3462895
    STATUS PASS

All replays match verification_output.txt byte for byte. Transcript SHA-256:
3e1b83ff586795fc80fc01882d545fff270f9106471145b39c0f0ca51bd3a778.

The independent reviewer verifier is
docs/papers157_161_sequence/reviews/p160_rcs_a/verify_p160_rcs_review_a.py.
It imports no author code and implements the update by literal Ferrers-cell
cropping. Separate routines test the row formula, bounded-product coefficients,
inverse reconstruction, valid every-weight witnesses, images, and mass.

Coverage is all 16 pairs \(1\leq a,b\leq4\), \(t=0,\ldots,5\), every source
through weight 30, named targets through weight 10, all caps through 30, probes
through \(a,b\leq7\), and 15 artificial/internal windows including
\((0,w)\), \((h,0)\), and \((0,0)\). It performs **7,332,616 exact
assertions**. Two cold runs match CANONICAL.txt byte for byte.

- reviewer verifier SHA-256:
  b886846853762cf13c755f7569f465bd6a5eab23d61765e0c687266c77569a49
- reviewer transcript SHA-256:
  971bcfccf205a590d08246f7266b73f38d088bfc79c571e92b209a936359ef9f

Computation is counterexample pressure and regression control only, not proof,
novelty evidence, or owner clearance.

## 6. Build, PDF, fonts, visual, and anonymity audit

Two fresh temporary directories received only main.tex and references.bib and
ran pdflatex, bibtex, pdflatex, pdflatex. Both settled PDFs are byte-identical
to each other, main.pdf, and main_round0_original.pdf:

- four A4 pages; 295,886 bytes;
- frozen Round-0 SHA-256:
  **2be90261ae3b636aa8db684597896f7e7d549363879936b3f6539877577f7d08**;
- settled passes have no unresolved citation/reference warning, rerun request,
  bad box, or error.

PDF title, author, subject, and keywords are blank. There is no custom metadata,
encryption, form, JavaScript, embedded file, machine path, email, ORCID, or
unresolved editorial marker. All 23 font rows are embedded, subsetted, and
Unicode mapped. The source author is Anonymous.

All four frozen pages were rasterized and inspected. The source table, theorem
statements, proofs, displayed formulas, worked coefficients, mass identity,
recovery equations, control section, and references are legible and unclipped.
No overlap, malformed glyph, missing rule, or broken equation was found. Page 4
has harmless whitespace after the two-item bibliography.

## 7. Round-1 repair list by file

1. **main.tex:** repair M1; add and subtract the M2 owner chain; revise Table 1
   and residual wording.
2. **references.bib:** add verified Gordon–Houten, Andrews, and Chen–Ji–Zang
   records actually cited by the text.
3. **PROOF_PACKAGE.md:** replace the invalid \(\gamma=(1^d)\) witness with a
   valid all-\(d\) construction.
4. **CLAIMS_EVIDENCE.md:** correct B2's evidence and move classical rectangle/
   two-boundary factorization to zero credit.
5. **DERIVATION_PACKAGE.md:** state the valid witness explicitly and sharpen
   the classical/residual boundary.
6. **SOURCE_VERIFICATION.md:** record the new primary-source inspection,
   metadata, exact owned interfaces, and bounded-nonhit limit.
7. **PAPER_PLAN.md, NARRATIVE_REPORT.md, README.md, SELF_QA.md:** propagate the
   corrected contribution boundary and witness; do not leave inconsistent
   “two-boundary residual” language.
8. **phase-one owner/collision ledgers:** add the M2 sources and the explicit
   P113 noncollision.
9. **Round-1 artifacts:** record every change in IMPROVEMENT_LOG.md, preserve
   main_round0_original.pdf, replay both exact-control lanes, perform two
   source-only builds, visually inspect all pages, and freeze main_round1.pdf.

Final disposition:
**REVISE / 0 Critical / 2 Major / 0 Minor / HOLD_EXTERNAL**.
An independent Review B is required after repair. This report authorizes no
posting, circulation, submission, author/specialist contact, novelty claim,
priority claim, or owner clearance.
