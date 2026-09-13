# Paper 27 publication-stage scope lock (author draft)

## Purpose and boundary

This record converts the independently reviewed proof plan into a bounded
publication-stage specification.  It does not itself create a paper tree or
assert submission readiness.  The maximum permitted effect remains a local,
anonymous artifact; upload, submission, hosting, repository push, external
message, and identity disclosure are forbidden.

The article is a proof-only theory paper titled *Diagonal-Translation
Rigidity and Phase Reciprocity in Positive Newton-Fan Hamiltonian Shears*.
Its target is 24--28 content pages through the end of the conclusion, with a
planned 25.7 pages.  References and an optional appendix are outside that
count.  The article must use the corrected scope from SOURCE_LOCK.md and the
eight-body-section plan in PAPER_PLAN.md.

## Exact anonymous source trio

The later source lock may create exactly this trio and no other manuscript
source path:

1. `papers/27-positive-newton-translation-reciprocity/paper/main.tex` — the
   complete anonymous article, including all eight body sections and the
   abstract.  It may include the other two files with relative `\input` or
   bibliography commands only if the final source review confirms the trio is
   exactly reproducible.
2. `papers/27-positive-newton-translation-reciprocity/paper/math_commands.tex`
   — notation macros only; no identity or provenance.
3. `papers/27-positive-newton-translation-reciprocity/paper/references.bib` —
   only verified records actually cited by main.tex.

To keep the trio exact, sections should be embedded in main.tex rather than
stored as additional `.tex` files.  No figure file, generated data, code,
experiment output, supplementary archive, or custom package is in scope.  A
symbolic diagram may be drawn with native LaTeX commands in main.tex; it may
not depend on an external asset.

## Content contract

The source must state and prove, with the certified-branch quantifiers, the
following four clauses.

* **Survival and transport.** For every certified strict edge with unique
  exposed selectors and positive carries, and for every nonzero coefficient
  choice in the stated characteristic-zero class with finite nonempty
  collected supports E_V,E_W contained in Z_{>=2}^r and r >= 3, grouped
  positive-face Hessian survival, the Jacobian criterion, injective
  substitution, and strict carries yield the forward phase map
  (u,w) -> (B_beta A_alpha u, A_alpha u), and the W-then-V reflected inverse
  phase with subtraction signs.
* **Diagonal translation and tail.** On every certified strict edge,
  v = h_V(u) 1 - u and u' = h_W(v) 1 - v = u + delta 1 with delta > 0.
  On every infinite certified strict branch, selectors change at most
  d_V + d_W - 2 times, followed by the global-origin affine recurrence
  t_(n+1) = lambda t_n + mu, where lambda = (|alpha|-1)(|beta|-1) and
  mu = ((|beta|-1) alpha - beta) dot u_0.
* **Reflection.** With coordinate reversal R and R_state(u,w)=(Rw,Ru),
  reflected inverse reciprocity is necessary and sufficient edgewise on the
  observable spans U_e,V_e, provided the reflected score, carry, and target
  certificates are present.  Full matrices are asserted only for full spans.
* **Local lower-ideal lemma.** Four normalized projections and strict
  selected-minus-new margins preserve one forward and one reflected inverse
  leading step on one strict pair core.  The result is not target-core,
  multi-edge, C1-to-C2, or all-iterate stability.

The exact r=3 asymmetric fixture, its matrices/products/gaps/seeds, and the
outside-class cancellation and missing-reflection boundaries must be printed
as witnesses and counterexamples, never as proofs of universal claims.

## Required article organization

The source must follow the eight sections and labels in PAPER_PLAN.md:

1. Introduction and contribution boundary.
2. Related work and claim-level collision positioning.
3. Typed setup, strict cells, and omnibus theorem.
4. Positive-face survival and degree transport proofs.
5. Translation, wall monotonicity, and affine tail proofs.
6. Reflected inverse reciprocity and its span criterion.
7. Local lower-ideal lemma and exact fixture.
8. Boundaries, limitations, reproducibility, and conclusion.

The abstract is unnumbered.  Every theorem-critical derivation appears in the
main body; an appendix may only repeat routine arithmetic already explained.
The related-work section must synthesize the verified S01--S20 records by
methodological family and must not claim priority or exhaustiveness.

## Citation and bibliography rules

The source may cite only records in CITATION_VERIFICATION.md or records
independently reverified at the source-review gate.  Every BibTeX entry must
have verified author, title, year, and venue/record identifier.  Uncited
entries are forbidden.  No entry may be generated from memory, and no citation
may be used as evidence for the Paper 27 theorem itself.  The bounded screen
date is 2026-08-29 UTC; wording must remain “bounded public screen” rather than
“first” or “唯一”.

## Anonymous metadata firewall

main.tex, math_commands.tex, and references.bib must contain none of the
following: author names, affiliations, acknowledgements, internal event IDs,
filesystem paths, hashes, reviewer names, process descriptions, source-lock
language, private URLs, or provenance breadcrumbs.  Use an anonymous author
block and neutral self-reference.  The source may say that the derivations are
symbolic and exact, but must not mention this repository or its governance
ledger.  The source must not contain empirical results, numerical fits, CAS
certificates, broad scans, GPU claims, or hidden computational assertions.

## Deterministic-source requirements

Before any build gate, the source reviewer must freeze raw bytes and verify
UTF-8/LF-only, one terminal LF, regular mode 0644, link one, no BOM/CR/NUL,
balanced braces, no stale section files, and no uncited bibliography entries.
The source trio is immutable after PASS.  A repair requires a separately named
revision, a new source manifest, and a fresh source reviewer.  Build roots,
compiler paths, environment pins, and cache checks belong to later build
authorizations and must not be simulated here.

## Scope review checklist

The independent publication-scope reviewer must return all-zero findings on:

- exact trio path and no-extra-file scope;
- 24--28 page target and eight-section crosswalk;
- theorem quantifiers, anti-claims, failure boundaries, and predecessor
  absorption;
- verified citation roles and bibliography discipline;
- symbolic-only figure policy and no empirical/CAS dependency;
- anonymous metadata/provenance firewall;
- deterministic-source and repair rules; and
- no external effect or downstream build authority before publication lock.

Only that PASS opens the publication lock.  Until then, no `paper/` directory,
source trio, bibliography, figure, build root, PDF, or release copy may exist.

BATCH07_PAPER27_PUBLICATION_SCOPE_FROZEN
