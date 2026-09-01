# Hostile review B — repaired manuscript, round 2

## Verdict and severity count

**ACCEPT**

- Critical: **0**
- Major: **0**
- Minor: **0**

No required mathematical, ownership, bibliographic, build, or provenance fix remains from this review.  This verdict concerns internal correctness and reproducibility only; it does not override the manuscript's `HOLD_EXTERNAL` status and is not novelty or priority evidence.

## Review scope

I independently read `HOSTILE_REVIEW_A.md`, `IMPROVEMENT_LOG.md`, the current `main.tex`, all narrative/plan/evidence/source/control/build documents, `references.bib`, both verifier sources, both frozen transcripts, and the extracted text of the round-0 and current PDFs.  I reran both canonical programs, rebuilt from only the current TeX and bibliography in an isolated temporary directory, compared the resulting bytes, and visually inspected all four pages of the current PDF.  I also attacked the proofs directly, with special attention to non-antisymmetric preorders, collapsed quotient classes, labelled versus unlabelled embeddings, and closures in the inclusion--exclusion formula.

## Severity-ranked findings

### Critical findings (0)

None.  I found no false theorem, missing branch, invalid fibre bijection, corrupted canonical replay, or source/PDF mismatch.

### Major findings (0)

None.  All four substantive findings from round 1 are repaired and the repairs are actually present in the current PDF, not merely in auxiliary notes.

### Minor findings (0)

None.  The remaining differences among publisher date fields for the Schmidt book are not a manuscript error: Cambridge's own copyright/frontmatter page for ISBN 978-0-521-76268-7 says copyright 2011 and “First published 2011,” which supports the bibliography's year, even though some Cambridge Core chapter metadata expose a 2010 print-year field.

## Round-1 repair audit and owner locators

1. **Katona--Nagy DOI:** the current bibliography and printed reference use `10.1007/s11083-014-9342-8`.  The [official Springer record](https://doi.org/10.1007/s11083-014-9342-8) resolves to Gyula O. H. Katona and Dániel T. Nagy, “Incomparable Copies of a Poset in the Boolean Lattice,” *Order* 32 (2015), 419--427, and its abstract distinguishes weak from strong/induced embeddings.  The superseded DOI ending `9343-7` resolves to the different Dove--Griggs article “Packing Posets in the Boolean Lattice”; it no longer occurs in the repaired artifacts.

2. **Schmidt locator and direction:** the cited location is exact: *Relational Mathematics*, §4.4, Fig. 4.4.2, p.45.  There Schmidt's right residual \(Q/P\) relates a row of numerator \(Q\) to denominator rows of \(P\) that it **contains**.  Thus at \(P=Q=A\) the displayed direction is \(R_j(A)\subseteq R_i(A)\).  The manuscript's map is the converse direction, \(R_i(A)\subseteq R_j(A)\), so the sentence saying that the displayed orientation must be reversed is mathematically exact.  The [official Cambridge chapter record](https://doi.org/10.1017/CBO9780511778810.008) identifies §4.4's chapter and pp.35--48, while the [official Cambridge frontmatter](https://assets.cambridge.org/97805217/62687/frontmatter/9780521762687_frontmatter.pdf) verifies the cited edition, ISBN, and 2011 first-publication statement.

3. **Botts locator:** the [publisher article and PDF](https://doi.org/10.4153/CJM-1954-057-5) verify Truman Botts, *Canadian Journal of Mathematics* 6 (1954), 525--528.  Page 525 defines the family of upper sets and gives the principal-upper-set map \(K(x)\); pp.525--526 establish its order-embedding/representation property.  The manuscript uses this only to delimit the classical principal-upper-set/powerset representation viewpoint.  It does not attribute the present labelled-map fibre count to Botts.

4. **Labelled maps:** Theorem 1 and the inverse-atlas proof now consistently say “labelled induced order-embedding maps \(Q\hookrightarrow\mathcal B_n\)” and explicitly state that no quotient by \(\operatorname{Aut}(Q)\) is taken.  This is the correct object: the quotient classes of the fixed labelled target \(P\) remain distinguished, while equal elements inside one preorder class are forced to share a source row.

## Mathematical falsification audit

### Forward dynamics

- For every Boolean matrix \(A\), row-support inclusion is reflexive and transitive, so \(\mathcal T_n(A)\) is a preorder.  No antisymmetry is silently assumed.
- If \(P\) is a preorder, its \(i\)-th row is the principal upper set \(\uparrow i\).  The equivalence

  \[
  \uparrow i\subseteq\uparrow j \quad\Longleftrightarrow\quad j\le_P i
  \]

  remains valid when \(i\) and \(j\) belong to nontrivial equivalence classes.  Therefore \(\mathcal T_n(P)=P^{\mathsf T}\).
- It follows both that every preorder is hit, via \(\mathcal T_n(P^{\mathsf T})=P\), and that \(\mathcal T_n^3=\mathcal T_n\).  Every nonpreorder has tail exactly one because it is outside the image at time zero and in the image after one step.
- A preorder fixed by transpose is precisely a symmetric preorder, hence an equivalence relation.  All other preorders form strict transpose two-cycles.  Consequently the odd/even fixed-iterate counts \(B_n\) and \(q_n\), and the zeta factorization

  \[
  (1-z)^{-B_n}(1-z^2)^{-(q_n-B_n)/2},
  \]

  have the correct multiplicities.  In particular \(q_n-B_n\) is even because transpose partitions the nonfixed preorders into two-element orbits.

### Every-target fibre theorem

- Targets outside the preorders have empty fibres because every image is a preorder.
- For a preorder target \(P\), mutual comparability forces the corresponding source rows to be equal.  Conversely, equal source rows force mutual comparability in \(P=\mathcal T_n(A)\).  Hence the row assignment factors through the quotient poset \(Q=P/{\sim}\) and is injective on \(Q\).
- The relation \(q\le_Q r\) is equivalent to inclusion of the assigned source-row subsets.  Thus the factor map both preserves and reflects order: it is an induced order-embedding into the labelled Boolean lattice.  Conversely, expanding an embedding along the labelled quotient map reconstructs one and only one source matrix.  Class sizes introduce no multiplicity and poset automorphisms introduce no division.
- For the explicit count, an isotone map \(Q\to\mathcal B_n\) is equivalently an \(n\)-tuple of upper sets, giving \(J(Q)^n\).  For every missing order pair \((q,r)\in D_Q\), the bad event is \(f(q)\subseteq f(r)\).  Intersecting a set \(S\) of bad events is exactly isotonicity for the reflexive--transitive closure \(Q_S\), so ordinary indexed inclusion--exclusion gives

  \[
  \sum_{S\subseteq D_Q}(-1)^{|S|}J(Q_S)^n.
  \]

  This remains correct when \(Q_S\) ceases to be antisymmetric: upper sets of the resulting preorder are constant on its equivalence classes.  Duplicate or logically dependent bad events likewise do not invalidate indexed inclusion--exclusion.

I found no counterexample in any theorem branch.  As a noncanonical supplementary stress test, 100,000 seeded random Boolean matrices and 10,000 seeded random reflexive--transitive closures for \(1\le n\le10\) supplied 110,000 further assertions of \(\mathcal T^3=\mathcal T\) and \(\mathcal T(P)=P^{\mathsf T}\), all passing.

## Canonical reproducibility

From the paper directory I ran

```sh
PYTHONDONTWRITEBYTECODE=1 python3 verify_p143.py | cmp - verification_output.txt
PYTHONDONTWRITEBYTECODE=1 python3 verify_p143_embeddings.py | cmp - embedding_verification_output.txt
```

Both commands exited zero and reproduced their checked-in transcripts byte for byte.

- `verify_p143.py`: **265,050 assertions**.  It exhausts every Boolean matrix through \(n=4\), every target through \(n=4\), all forward-dynamics branches, fixed-iterate/zeta data, and the direct fibre versus inclusion--exclusion formula.
- `verify_p143_embeddings.py`: **13,238,845 assertions**.  Independently of the main verifier/formula, it compares direct source sets with labelled induced-embedding source sets for every target through \(n=4\), then tests all 219 labelled four-element posets in the \(\mathcal B_5\) lane.  Its frozen fingerprints include 14,835,086 embedding candidates, all 66,066 source matrices through \(n=4\), 10,450,918 isotone maps, and 863,040 induced maps.
- Canonical total: **13,503,895 assertions**.

The verifier and transcript hashes match the repaired control documents:

```text
verify_p143.py                      1d0335d78806b60500794cce6bdd197cea1e328f2a13cf0af28c406c449720fd
verification_output.txt             9643e4a8a069c58cdb1a9772a0ad341b85d844a43597b2c3e65450a4ba46938c
verify_p143_embeddings.py           383688827176cadffe68017ef0a9c77e57029049ba14902801af38c7d98eae7d
embedding_verification_output.txt   dabdbd7cb891838ef8049f79460c3e5213137f4ad1d62e7377bf3d61989a47fe
```

## Build, PDF inspection, and provenance

I copied only current `main.tex` and `references.bib` to an isolated `/tmp` directory and ran `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.  The settled logs contain no undefined references/citations, BibTeX warnings, overfull/underfull boxes, or rerun requests.  The isolated output is byte-identical to current `main.pdf`.

Relevant hashes are:

```text
main.tex                    13a4aa9f547e5bd0a09166895494abc232bff1c8300ad509ed1625c4a6f44a7b
references.bib              4ba072fc9aa629e7dcfeac6834612594b233c18c2007e732253a734acda31b82
main_round0_original.pdf     2cc73cb1f9cb0c673f86fc7a869cd8937b6aa0aa80a6a9d5a07fd50682567b6f
main_round1.pdf              240aac151d3f077854d1ceb8de1ed53f510f0c27cdde662314cd1fbadfb07efe
main.pdf                     240aac151d3f077854d1ceb8de1ed53f510f0c27cdde662314cd1fbadfb07efe
isolated main.pdf            240aac151d3f077854d1ceb8de1ed53f510f0c27cdde662314cd1fbadfb07efe
```

Thus the preserved round-0 PDF is genuinely distinct, while `main_round1.pdf`, current `main.pdf`, and a clean rebuild of current source are identical.  The text difference from round 0 contains exactly the documented repair classes: corrected DOI, Schmidt/Botts locators and orientation, labelled-map/no-automorphism wording, and the second-verifier report.

The current PDF is four A4 pages, unencrypted, has no JavaScript or forms, and all 25 reported fonts are embedded, subsetted, and Unicode-mapped.  Visual inspection of every page found no clipping, collision, malformed formula, broken reference, or table overflow.

## Ownership framing

The paper credits Schmidt for residual convention, Botts for the classical representation, and Katona--Nagy for induced-embedding terminology.  It does not present those ingredients as contributions.  The bounded owner search is explicitly labelled a non-hit rather than novelty/priority/clearance evidence, and the external status remains `HOLD_EXTERNAL`.  I found no owner-framing overclaim requiring repair.

## Required fixes

**None.**
