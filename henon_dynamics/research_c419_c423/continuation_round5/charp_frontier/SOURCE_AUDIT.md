# Round 5 source and collision audit

Access date: 2026-09-08 UTC. Bounded source-first scout; not a systematic
review, worldwide novelty certificate, or assertion of current global
openness. Three contracts were frozen, at most two deepened. Broad search
leads rejected before the freeze do not become extra candidate contracts.

## Primary/authoritative text actually used

| ID | Source and version actually accessed | Exact reading scope | Permitted use and limit |
| --- | --- | --- | --- |
| S1 | Kenneth Allen, David DeMark, Clayton Petsche, *Non-Archimedean Hénon maps, attractors, and horseshoes*, [arXiv:1610.04271v3 PDF](https://arxiv.org/pdf/1610.04271v3), version 6 February 2018; the PDF body dates its revision 5 January 2018 | §1.1 including the ground field, equation (1), Julia definitions (3), parameter partition (4); Theorem 1(a,e); §5.5 Theorem 28 and its proof, printed pp.29–30; the adjacent proof-ending discussion was also returned | Direct CF2 coverage. Odd residue characteristic explicitly includes finite extensions of $\mathbb F_p((T))$. It supplies full filled-Julia coding, not merely a chosen subset. The arithmetic outside this parameter region, residue characteristic two, and other proposed attractors are not imported. Not all 31 pages were read. |
| S2 | Andrew Bridy, *Transcendence of the Artin–Mazur Zeta Function for Polynomial Maps of $\mathbb A^1(\overline{\mathbb F}_p)$*, [arXiv:1202.0362v2 PDF](https://arxiv.org/pdf/1202.0362v2), header 14 May 2012 | Abstract, definitions and motivating Frobenius example, ordinary-versus-multiplicity discussion, Theorems 1–2 on printed pp.1–3 | Owns the additive-polynomial transcendence mechanism in its stated scope. Theorem 2 in this version assumes odd $p$; it is not cited as a direct all-$p$ theorem for CF1 or for a nonlinear two-coordinate skew map. The present proof treats $p=2$ explicitly. No full-body reading or general plane-map classification is claimed. |
| S3 | Antonio Rojas-León, *On the number of rational points on curves over finite fields with many automorphisms*, [arXiv:1005.4078v2 PDF](https://arxiv.org/pdf/1005.4078v2), header 27 May 2010 | Abstract and §1 opening through the Kummer-family discussion on printed pp.1–2 | Primary research context for Artin–Schreier/Kummer point counting and the classical Weil error. Its sharper descent estimates and their additional hypotheses are not applied to arbitrary $a$. The literal CF1 dynamical formula is not attributed to this source. |
| S4 | Bjorn Poonen, *Rational points on varieties*, [author-hosted online text](https://math.mit.edu/~poonen/papers/Qpoints.pdf), copyright 2017, marked unofficial for incidental online use | §7.1 Theorem 7.1.1, §7.2 including Corollary 7.2.1, and §7.7.1 Theorem 7.7.1 with proof sketch; printed pp.205–206 and 222–223 | Authoritative theorem formulation for the fixed-curve estimate and geometric-irreducibility condition in CF1 Step 5. Smooth projective completion and bounded affine boundary are checked in the proof. The book is exposition, not the original owner of the Weil/Lang–Weil theorem. No reading of all 348 pages is claimed. |
| S5 | Benjamin Hutz, *Dynatomic cycles for morphisms of projective varieties*, [NYJM publisher PDF](https://nyjm.albany.edu/j/2010/16-8p.pdf), 2010 | Introduction/Definitions 1.1–1.2/Theorem 1.3; Theorem 2.4 and local-intersection setup; Proposition 2.18 and its displayed proof; Theorem 4.11/Corollary 4.12; §4.4 Theorem 4.13 and its proof | Owns the general formal-period/multiplier restrictions and Wehler periodic-point context. Multiplicity-one criterion is relevant to CF3. A fixed point's boundedness theorem away from characteristic-divisible times is not an all-points uniform wild-tower bound. The displayed Wehler Lefschetz number is not silently transported into an ordinary positive-characteristic count. Not all 35 pages or all effectivity arguments were audited. |

Poonen's explicit affine theorem formulation and Rojas-León's primary
curve context were both checked; this audit does not pretend that reading
an exposition is a fresh verification of Weil's original proof. An
attempt to access Lang–Weil's original [DOI](https://doi.org/10.2307/2372655)
returned an access error. No original-paper body coverage is claimed.

## Context-only retrieval and discarded isogeny lead

- Byszewski–Cornelissen–Houben, [arXiv:2209.00085v2](https://arxiv.org/html/2209.00085v2),
  *Dynamics of endomorphisms of algebraic groups*: official metadata,
  abstract and opening context were inspected. The accessed revision is
  19 April 2024, not a new 2026 manuscript. A guessed v3 HTML URL returned
  404 and was discarded. This round does not newly certify all of its
  176 pages or assert that CF1 is an algebraic-group endomorphism.
- Lau–Morrison–Orvis–Scullard–Zobernig,
  [arXiv:2509.15214v1 HTML](https://arxiv.org/html/2509.15214v1): metadata,
  introduction and framework overview were retrieved as a possible lead.
  The header gives 18 September 2025 whereas the returned HTML body gives
  24 August 2026. The old repository audit already owns this scout and
  records an odd-cycle sign defect with a PDF check. This round read that
  local audit, did not rerun its counterexample, did not re-audit the full
  primary formula, and excluded the lead before freezing three contracts.
  Its definitions/framework ownership is not a certification of every
  printed theorem or a new CF1–CF3 dependency.
- Other discovered abstracts, including recent isogeny publications and
  Markoff/curve results, were routing leads only. No abstract-only hit,
  search snippet, third-party summary, or unrelated paper supplies a
  theorem in the proof package.

## Repository comparisons actually made

Read-only `rg` searches used narrow topic/literal/version terms in the
Hénon markdown files, followed by direct reading of the relevant records.
This is a collision screen, not a proof audit of every historical paper.

| Local record and inspected part | Collision/subtraction |
| --- | --- |
| [C404 resonant proof](../../../continuation_c404_c408_round2/henon_resonance/PROOF_PACKAGE.md), entire contract/setup/count and §7 natural-boundary argument through §8 | C404's nonlinear degree lemma is different from CF1, but its characteristic-divisibility telescoping product and fractional radial-order argument are exactly the analytic mechanism reused here. Adding component cycles and a holomorphic Weil-error term is a short extension, not an independent analytic invention. |
| [NC2 frozen contract](../../continuation_round2/new_charp/FROZEN_CONTRACTS.md), NC2 section; [NC2 scout](../../continuation_round2/new_charp/SCOUT_REPORT.md), opening disposition and relevant boundary | NC2 was an additive orbit sum/trace-quadratic problem on separately indexed finite fields. CF1 instead counts geometric fixed points with a Kummer norm twist; it is not literally NC2, but classical skew-return reconstruction remains a serious increment ceiling. |
| [Earlier characteristic-p scout](../../positive_characteristic/SCOUT_REPORT.md), directed search hits and disposition; [admission decisions](../../ADMISSION_DECISIONS.md), relevant PC-D/PC-H/NC2 entries | Finite Drinfeld invariant factors and coefficient-twisted C404 counts are already screened and are not fresh routes here. No old experiment was rerun. |
| [Round 3 contracts](../../continuation_round3/positive_charp_new/FROZEN_CONTRACTS.md), entire file | Excludes simply resubmitting the one-variable $x^p+1/x$ question or matrix-isogeny Kummer quotient reconstruction. CF1's Kummer cover is a different literal object, not a reopening of that matrix question. |
| [NG3 frozen contract](../../nonlinear_geometry/FROZEN_CONTRACTS.md), NG3 and shared boundary; [NG3 source audit](../../nonlinear_geometry/SOURCE_AUDIT.md), directed K3/Hutz hits | The earlier target is all rational points of affine $W_k$ under one three-involution word. CF3 has a different compact family, geometric domain and ordinary multiplicity problem. Its two-involution Wehler framework remains classical. |
| [Old nonaffine isogeny audit](../../../research_c404_c408/nonaffine_charp/SOURCE_AUDIT.md), entire file; [scout](../../../research_c404_c408/nonaffine_charp/SCOUT_REPORT.md), opening and candidate A | Confirms the discarded isogeny lead was already examined, with the printed odd-cycle caveat. This exact old lane is not counted as a fresh fourth contract. |
| [Old nonaffine-charp audit](../../../continuation_c399_c403_round2/nonaffine_charp/SOURCE_AUDIT.md), entire file | Reconfirms that derivative-one rational formulas can conceal Lattès structure and that simple multiplicity obstructions do not settle all-period ordinary zetas. Its old formulas/checks are not rerun. |
| Hénon main README; connected algebraic $\mathbb Z^2$ resonance README; uniform affine horseshoe README | Broad ownership routing only: compact group-resonance and real affine horseshoe coding are not confused with the exact local-field scope of S1. S1 provides the decisive CF2 coverage. |

An initially guessed `research_c403_c418` directory did not exist; it was
not represented as searched successfully. Some broad `rg` output was
truncated; the decisive C404, NC2, NG3 and old-isogeny records above were
subsequently opened directly. An attempted old `SCOUT_REPORT.md` under
`continuation_c399_c403_round2/nonaffine_charp` did not exist; its actual
`SOURCE_AUDIT.md` was the record read there.

## Actual directed web queries

These exact public mathematical formulations were run. No workspace
manuscript, unpublished proof payload, credentials, or private data was
sent to web search. The number of queries is a receipt, not a novelty
guarantee.

1. `positive characteristic dynamical zeta functions periodic points 2024 2025 2026`
2. `positive characteristic algebraic dynamics zeta non dynamically affine skew product`
3. `"dynamical zeta" "Witt"`
4. `"finite fields" "skew product" "periodic points"`
5. `"positive characteristic" "dynamics on algebraic groups" zeta`
6. `"positive characteristic" "dynamical zeta" "skew"`
7. `"linearized" "polynomial" "Frobenius" "monodromy"`
8. `"periodic points" "Artin-Schreier-Witt"`
9. `"Henon" "positive characteristic" "horseshoe"`
10. `"Hénon" "non-Archimedean" "periodic"`
11. `"Dynamics of endomorphisms of algebraic groups and related systems"`
12. `"y^p" "x" "skew" "periodic" "finite"`
13. `"Non-Archimedean Hénon maps, attractors, and horseshoes"`
14. `"Non-Archimedean H'enon maps" arxiv`
15. `"Dynamics of endomorphisms of algebraic groups and related systems" arxiv`
16. `"Kummer" "dynamical zeta" "Frobenius"`
17. `"supersingular isogeny graphs" "zeta" 2025 2026`
18. `"Artin Mazur" "Newton" "positive characteristic"`
19. `"Kummer cover" "skew product" Frobenius`
20. `"positive characteristic" "periodic points" "Markov"`
21. `Wehler K3 surface positive characteristic automorphism periodic points fixed points multiplicity`
22. `K3 surface automorphism finite field ordinary periodic points Lefschetz wild fixed multiplicities`
23. `"Wehler" "periodic points" finite fields`
24. `"K3" "periodic points" "positive characteristic"`
25. `"automorphism" "periodic points" "multiplicities" "finite field" surfaces`
26. `Kummer curves finite fields Weil bound number rational points y^m=f(x) irreducible components`
27. `"Dynamically" "Kummer" "skew" zeta Frobenius`
28. `"y^p" "a(x)" "dynamical" "zeta"`
29. `Lang Weil Number of points varieties finite fields 1954 pdf`
30. `"Wehler" "Lefschetz" "Silverman" 22`
31. `"Bridy" "1202.0362"`

## Access limitations and substantive conclusion

Zotero/Obsidian tools were searched for and unavailable. Named local
paper-library/helper paths were absent, and no relevant candidate PDF
was identified by the local paper filename screen. Unrelated symbolic
PDFs were not substituted for a source corpus. Ordinary web discovery,
primary author preprints, a publisher PDF and the author's theorem text
were used instead. No automated scholar scrape, citation-score ranking,
paid API, new plugin install, GPU or mathematical CPU job was used.

CF2 is directly covered. CF1's literal theorem is proved locally, not
claimed found verbatim in a publication; the complete reduction is too
close to classical/owned tools for this lane's independent-slot gate.
CF3's full ordinary-zeta classification was not located in the sources
read and was not proved here. That bounded negative statement does not
assert global openness, impossibility or priority.

The source-first batch/research-lit/idea-creator/ARS workflow caused the
explicit version/hypothesis/ownership checks and rejection of the old
isogeny lead. Proof-writer caused full-claim versus helper separation.
This is author-stage internal AI-assisted source work. A separate
non-author CF1 mathematical review is being arranged by the coordinator;
it must not be represented as already completed by this audit.
