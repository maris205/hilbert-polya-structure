# HCS-C21 repository update

## Stage-1 and Stage-2 package

The new directory henon_chiral_chronology_threshold contains:

- a source-locked exact research question and experiment plan;
- a complete period-six ordered-cover derivation;
- a primary-source and novelty audit;
- a Stage-1 synthesis with contradiction inventory;
- an adversarial Checkpoint-2 PASS;
- an exact producer, non-importing independent checker, and fail-closed tests;
- compact JSON artifacts and SHA-256 bindings;
- a formal Route-A evaluation;
- a complete 17-page bilingual LaTeX manuscript and compiled PDF;
- an exact bibliography with primary-source locators and frozen repository
  links;
- a PDF compilation/font/visual-integrity report; and
- a two-round manuscript pressure review.

## Repository-wide updates

The following indexes now point to HCS-C21:

- henon_dynamics/README.md;
- docs/candidate_registry.md;
- docs/obstruction_registry.md;
- docs/related_programs/README.md; and
- the HCS-C19/C20 successor roadmap.

Reusable obstructions HEN-O44--HEN-O46 record the genus-one
chronology--cohomology collapse, period-one marker shadow, and
clock-divisibility theorem.

## Verification

From the project directory:

~~~bash
python -m pip install -r requirements.txt
python code/c21_producer.py --output results/c21_certificate.json
python code/c21_independent_check.py \
  --certificate results/c21_certificate.json \
  --output results/c21_independent_check.json
python -m unittest discover -s code -p 'test_c21.py' -v
sha256sum -c results/ARTIFACT_HASHES.sha256
~~~

Expected result:

- certificate SHA-256:
  `5386c95cbc65e6a4323cfcf230de6b41f353be909d197818f9c4fbf0a75a96fc`;
- independent report: PASS, 133 checks;
- tests: 14/14 PASS;
- hash ledger: all entries OK.

From `paper/`, the release manuscript builds with:

~~~bash
latexmk -lualatex -interaction=nonstopmode -halt-on-error main.tex
~~~

Expected PDF:

- pages: 17;
- SHA-256:
  `984ad0bc7cd0fe8840ce6a6f442dd377f930127e28836137ca814a2dd30847e1`;
- undefined references, missing glyphs, or overfull boxes: none;
- all fonts embedded.

## Release state

Before release, the Route-A record deliberately uses
`PENDING_RELEASE_COMMIT`.  The release sequence is:

1. commit the complete HCS-C21 source package;
2. replace pending provenance fields with the source commit;
3. create a provenance-only release commit;
4. create annotated tag hcs-c21-v1; and
5. push main and the tag through the configured SSH remote.
