# Source audit and literal deductions

Milestone: SOURCE_AUTHORING_ONLY, 2026-09-09 UTC.
The bibliography uses three verified published records. Actual public-source
requests and provider reference identifiers are preserved in
PRIMARY_ACCESS.json, without copying third-party papers or abstract bodies.
No new broad priority survey, global nonownership claim or fake cross-model
review is asserted.

## Published entries and claim-level scope

### boccara2002

Nino Boccara and Henryk Fukś, “Number-conserving cellular automaton rules,”
Fundamenta Informaticae 52(1–3), 1–13 (2002), DOI
[10.3233/FUN-2002-521-302](https://journals.sagepub.com/doi/abs/10.3233/FUN-2002-521-302).
Publisher metadata and [the authors' arXiv record](https://arxiv.org/abs/adap-org/9905004)
verify the title/authors and publication record. The source body read was
[the arXiv PDF](https://arxiv.org/pdf/adap-org/9905004), particularly
Theorem 2.1 and its elementary proof (returned lines 91–127).
It supports only the finite-alphabet local conservation characterization
used as background in §1. No terminal or inverse formula is attributed
to it. The displayed PDF header's 2024 template year is not taken as
publication metadata. The preprint versions are 1999 and 2000.
The BibTeX entry was manually formatted from the verified metadata;
the attempted DBLP .bib access failed, and is not represented as a
successful machine-retrieved BibTeX entry.

### nishinari1998

The full published record is verified in
[Waseda's author-institution entry](https://waseda.elsevierpure.com/en/publications/analytical-properties-of-ultradiscrete-burgers-equation-and-rule-/)
and [Takahashi's works list](https://hakotama.jp/laboratory/jworks.html).
Actual institution-supplied BibTeX fields identify Katsuhiro Nishinari,
Daisuke Takahashi, Journal of Physics A: Mathematical and General 31(24),
5439–5450 (1998), DOI 10.1088/0305-4470/31/24/006.

The [author-hosted PDF](https://hakotama.jp/laboratory/works/public/98nt.pdf)
has a September 11, 2001 front date. That file version does not change
the verified 1998 publication year. Section II, especially equations
(16) and (21), supplies the current min(M,sender,L−receiver) and its
current-unbounded version. The present receiver-mass current is a literal
difference only. No Cole–Hopf transfer, arbitrary-conjugacy exclusion,
full solution comparison or full-paper proof audit is asserted.
The DOI redirect attempt failed; the institution record and author body
supply the actual successful evidence.

### fukuda2023

The published title is “Generalized discrete and ultradiscrete Burgers
equations derived through the correlated random walk,” not the title of
the earlier preprint. [Shibaura's author-institution record](https://shibaura.elsevierpure.com/en/publications/generalized-discrete-and-ultradiscrete-burgers-equations-derived-/)
provides actual BibTeX fields: Akiko Fukuda, Etsuo Segawa, Sennosuke Watanabe,
Journal of Difference Equations and Applications 29(1), 84–101 (2023),
DOI 10.1080/10236198.2023.2172969.

The examined source formulation is
[arXiv 2104.14009v2](https://arxiv.org/html/2104.14009v2),
whose preprint title is “A variant of the discrete Burgers equation derived
from the correlated random walk and its ultradiscretization.” The arXiv record dates v2 to November 5,
2021. The read equations (15)–(17) include receiver vacancy and an additional
evolving variable. §1 explicitly labels that detailed comparison as the
examined preprint formulation; it does not assign those equation numbers
to the inaccessible published body. The institution abstract supports the
general correlated-random-walk description. Publisher full/abstract/PDF
opens and a Crossref API attempt failed. No publisher-body full read or
successful API BibTeX retrieval is claimed.

## Internal literal collisions deducted

These are repository evidence comparisons, not published bibliography.

- UUC: the entire author PROOF_PACKAGE.md in scouting/transport_lane was
  read. Its current is the binary uphill indicator
  1{0<x_i<=x_(i+1)}, not min(x_i,x_(i+1)). Its conservation, immutable
  zeros, energy convergence and generic current-word feasibility inverse
  are deducted. The present evaluated interval atlas is not claimed new
  merely because it partitions local equations.
- MNA: the entire author MNA_PROOF.md in
  docs/papers204_208_sequence/scouting/finite_systems_fortieth was read
  (the actual path is pinned in SOURCE_INPUTS.sha256). It merges
  maximal weakly increasing runs of a positive composition into their
  sums, changing its number of parts. Generic run boundaries and transfer
  counting are deducted; its triangular delayed-merger clock and
  refinement threshold are not reused as P213's mechanisms.
- P211: only its setup/introduction was read for comparison. It acts on
  nondecreasing selfmaps of a finite chain, via kernel/image ceiling
  retractions; it does not act over a finite field. The original fresh07
  source paragraph's “finite-field” wording is a preserved historical
  error, superseded by fresh07_source_erratum01/ERRATUM.md and the
  accepted same-reviewer fresh07_gate_delta01 amendment.
- P212: only its declared closed-pointer-orbit reversal setup was read
  for comparison. It is not the literal conservative integer flow here.
  No whole-manuscript review or proof contribution to P211/P212 is claimed.

The UUC/MNA scope is the actual original proof bodies, not a title-only
difference. A literal distinction is not a proof that no encoding or
conjugacy exists. Root reception and the candidate gate accepted only
GO_NARROW, not global priority, an originality score or venue suitability.

## Archive and process boundaries

The full candidate proof, source/collision record, independent gate report,
gate source check, source-label erratum, accepted delta and root reception
were read. The original OPEN wording remains historical; only the named
accepted label amendment closes it. Candidate science has not been
rerun or copied into a new output. SOURCE_INPUTS.sha256 pins the exact
documentary inputs used, not the entire archive or executable dependency
closure.

The paper-plan/paper-write cross-model MCP provider is unavailable. No
cross-model outline/manuscript review is fabricated. The same author wrote
the fresh07 proof and pilot and this new P213 source; see AUTHORSHIP.md.
Two distinct actual nonauthor manuscript reviews and their complete
artifact roles remain mandatory after the execution/build gates.

## Later title-label correction, with the original source preserved

The complete v2 preprint title above incorporates only the already accepted
[root erratum](../../docs/papers211_215_sequence/qa/p213_source_title_erratum01/ERRATUM.md),
its [same-auditor acceptance](../../docs/papers211_215_sequence/qa/p213_source_parameter_title_delta01/DELTA_ACCEPTANCE.md),
and [root combination receipt](../../docs/papers211_215_sequence/qa/p213_source_parameter_root01/RECEPTION.md).
The frozen 2026-09-09 original and its source seal remain historical inputs;
this later representation does not change the published BibTeX, manuscript
introduction, theorem, verifier, parameters or scientific output. It is not a
new primary-source retrieval, manuscript review or execution authorization.
