# Paper Configuration

- Candidate: `cat_centralizer_cyclic_torsor_v1`.
- Title: *A Centralizer-Quotient Audit for Cat-Map Torsion Shells* (the
  independently approved conservative title).
- Format: anonymous specialist mathematical note, 11 pt, single column; no
  venue, page-limit, acceptance, priority, or historical-first claim is made.
- Document date: 2026-08-15 terminal local finalization.
- Length: 15 pages including appendices, three figures, three tables, and 14
  references.
- Manuscript source: `paper/manuscript.tex`, SHA-256
  `65bd460ac888ff5527f4401696788034973c3f97a532ee8a34184ce05fae72a6`.
- Historical pre-review copy: `paper/paper_pre_review.pdf`, SHA-256
  `f685996c741c3e92d4eb18086f2a4e4d898ede10e8124a23991ada3579f8d378`;
  it is byte-identical to `paper/manuscript.pdf`.
- Independent Round-1 review: `paper/reviews/round1_review.md`, SHA-256
  `bb1bdfb379062d2fe11245568ca3f6a97845456004119d3954c17dd917828c24`,
  verdict `ACCEPT`, with `CRITICAL=0 / MAJOR=0 / MINOR=0` and no required
  manuscript change.
- Round-1 revision copy: `paper/paper_round1_revision.pdf`, SHA-256
  `f685996c741c3e92d4eb18086f2a4e4d898ede10e8124a23991ada3579f8d378`;
  it is byte-identical to both the frozen pre-review copy and current
  `paper/manuscript.pdf` because Round 1 requested no change.
- Independent Round-2 review: `paper/reviews/round2_review.md`, SHA-256
  `ca8ee460f0956eb2f653e837402888b9d88d4888ae04ea1ad76231b6764a79ae`,
  verdict `PASS -- MAY_FINALIZE`, with
  `CRITICAL=0 / MAJOR=0 / MINOR=0`.
- Final PDF: `paper/paper_final.pdf`, SHA-256
  `f685996c741c3e92d4eb18086f2a4e4d898ede10e8124a23991ada3579f8d378`;
  it is byte-identical to the independently approved Round-1 revision PDF.
- Build: `paper/build.sh` fixes `SOURCE_DATE_EPOCH`, `FORCE_SOURCE_DATE`,
  `TZ`, and `LC_ALL`, then uses
  `pdflatex -> bibtex -> pdflatex x3`.  Two isolated clean trees reproduced
  byte-identical PDF, LaTeX-log, BibTeX-log, bibliography, auxiliary, and
  outline artifacts.
- Bibliography: numerical `natbib`; the 14 cited keys are exactly the 14
  independently verified entries in `paper/references.bib`, with no missing
  or unused key.
- Figures: the three independently approved vector-PDF masters are included
  with their exact frozen captions and labels; their SVG and 300 dpi PNG
  companions remain in the asset package.
- Reader-facing novelty policy: the note is described only as a deliberately
  modest, low-novelty structural audit and assembly of known ingredients.  No
  numeric novelty score appears in the manuscript or terminal release
  metadata.
- Review state: `COMPLETE_LOCAL_FINAL_REVIEW_PASS`.  Independent Round 2
  authorized finalization of the exact unchanged source and approved PDF.
  Terminal finalization was mechanical and changed no manuscript source,
  scientific content, reference, figure, source lock, code, or result
  artifact.

## Scientific boundary

For the frozen standard cat matrix, the note proves the universal cyclic
basis, matrix commutant, full-centralizer torsor, cyclic-orbit cosets, full
coarse quotient, and symplectic norm-image quotient for every modulus.  It
keeps the cyclic locus separate from the complete shell, treats the
binary/inert/split/ramified prime strata and fixed reversor, derives composite
formulas by CRT, and reports the single nine-modulus registered audit only as
an exact implementation and falsification control.

The one-class full quotient contains the map being quotiented and therefore
has identity induced dynamics with native period one.  The specialization
`z=q^{-s}` and length `log q` are external modulus labels.  The same one-class
construction holds at composite moduli and uses all modulus-dependent local
commuters, so it supplies neither an intrinsic prime selector nor a native
modulus clock.  The symplectic quotient retains norm classes and still has
identity dynamics.

No new centralizer classification, Artin--Mazur/equivariant/orbifold/stacky/
groupoid zeta, Hecke theory, quantization, transfer or Fredholm determinant,
prime--zero correspondence, RH mechanism, or historical-priority result is
claimed.  Enriched quotient and Route-B mechanisms remain live but untested.

Scientific disposition:
`CENTRALIZER_CYCLIC_TORSOR_CERTIFIED /
A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC / ROUTE_B_NOT_OPENED`.

## Frozen authorities and asset release

- Source lock: `experiments/source_lock.json`, SHA-256
  `aa99218099f2e2c3e14367bfe75f9da881d8b204689c07c6fa963f9582b696e2`.
- Proof package: `notes/PROOF_PACKAGE.md`, SHA-256
  `2eafe71f32c452ff8a20a6818ccb43082e02b866db7353e26c36ff432f1b2a4c`.
- Independent source review: SHA-256
  `a551784d205d9ef52ce6a493ab66cb7295a4a9dadbeb8bb2353fc58e3011dff5`,
  verdict `SOURCE_PASS`.
- Reviewed execution tree: SHA-256
  `87b08f11fc67eae47bdf745f8286700376f3debc5ac3fd190075a5fa2632f436`.
- Independent code-review history: SHA-256
  `990b1762e2aea6c379288854cca918cc4bbe87b7ea7ccadef7458ecfcf6988f0`,
  preserving Round-1 rejection and final Round-2 `DEPLOYMENT_PASS`.
- Raw registered result: SHA-256
  `8dceb1b8a63db462c1fd55a242ea35de974f73b6c80da68517b91c9eebb214ff`.
- Independent result integrity: SHA-256
  `29264a8fd97d3acf4435ed807294bffcda0844a48728d8572083d92a3bcf5b58`,
  verdict `RESULT_PASS`.
- Strict result manifest: SHA-256
  `db1dda86ff8bf13fd307cbb1eb6ea6a8c3c0de531ea5b1cc28a58c7bb085b658`,
  status `PASS`.
- Paper plan and citation verification: SHA-256
  `972c13d2551e51bb2781bf7f177314812460c161af0ce1daa748eeff413cbe8a`
  and
  `b4596ed56aee5eb47314221bba681098e45011a3fdc9dafc201315e597a1bfc6`.
- Bibliography and figure manifest: SHA-256
  `1ccce7ade3079ca995f00058f4811bdd02a9062d8038b27be2f967f480fe8699`
  and
  `1a2c7de68772ddeb5c614d0ade89a48710e93a3e5a5ff4a393db5c6f3cd4c2ab`.
- Frozen 25-path asset tree: SHA-256
  `33b8e1d767221529ff2b97fddca0145b1f9724cae924c37afa2847ecfc2bc9d6`.
- Round-1 repair history and fresh Round-2 `ASSET_PASS`: SHA-256
  `97f971328996efae866356bdc2c4715a68fcb470dcbe64029d7758d1ec73256a`
  and
  `9277132df8400c550f108c9a71d466a1c3752bbf3c1be2ae39d565e932bc3e87`.
- Independent manuscript Round-1 review: SHA-256
  `bb1bdfb379062d2fe11245568ca3f6a97845456004119d3954c17dd917828c24`,
  verdict `ACCEPT`, finding inventory `0/0/0`.
- Round-1 no-change response and integrity record: SHA-256
  `b3c4d6ecea0d5bc165bcb50fbb240ffede2d44804cd32dd9b66d487b93d6d561`
  and
  `af4404f0606fdd2c8efc2c7d19eb1f89ed2b8298eaa26fc861faceb068c14364`.
- Independent manuscript Round-2 review: SHA-256
  `ca8ee460f0956eb2f653e837402888b9d88d4888ae04ea1ad76231b6764a79ae`,
  verdict `PASS -- MAY_FINALIZE`, finding inventory `0/0/0`.

No file under `code/`, `experiments/`, `results/`, `paper/figures/`, and no
frozen planning, citation, bibliography, manuscript-source, or scientific
artifact was changed or rerun during finalization.  Historical pre-review
lifecycle labels embedded in the frozen source and PDF remain reviewed
artifact history; this configuration and the terminal manifests are
authoritative for the current lifecycle state.  Terminal status:
`COMPLETE_LOCAL_FINAL_REVIEW_PASS`.
