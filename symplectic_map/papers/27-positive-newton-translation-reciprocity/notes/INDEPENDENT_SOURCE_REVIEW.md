# Independent source review (R3) - Paper 27

Authorization: B07-E0112.  Candidate: positive_newton_translation_reciprocity_v5.
This is a fresh source-trio review after the disqualified R2 attempt.  The
review was performed under the exact whitelist in the authorization.  I used
only direct reads and the permitted byte/line/mode commands; no directory
listing, search, compiler, bibliography tool, shell escape, generated output,
build root, cache, PDF, or external effect was used.

## Ledger binding and frozen manifest

The first 350357 bytes of BATCH_07_STATUS.md hash to
789d289dc317d3d392d94b0673fed2bdaaf257f7d9b0e5dd0946589c81313091.
This is the parent prefix required by E0112; no status byte after that prefix
was read.  The frozen source-trio manifest stated in the ledger is the
34-row, 4831-framing-byte, 34-LF aggregate
534d947b818c129f34467d10c4b04554e6da3215a0b5fa89dd4488772df34801, serialized
with path<TAB>bytes<TAB>LF<TAB>644<TAB>1<TAB>sha256<TAB>LF semantics (the final
separator is LF, not a literal TAB).  BATCH_07_STATUS.md is excluded from
that self-excluding aggregate.  The authorized paper directory census records
exactly main.tex, math_commands.tex, and references.bib, with no section file,
figure asset, code, data, auxiliary output, cache, build root, PDF, or release
copy.

## Physical source and review-input census

All rows below are regular files, mode 0644, link count one, UTF-8, LF-only,
without BOM, CR, or NUL.  The final two bytes were checked directly; each row
has exactly one terminal LF.

| path | bytes | LF | terminal bytes | SHA-256 |
|---|---:|---:|---|---|
| paper/main.tex | 33811 | 829 | 7d 0a | ba9879a7084821b18c3e76166706d90d99bc4cb8e0bb1cb09d04a23f3a007f18 |
| paper/math_commands.tex | 601 | 17 | 7d 0a | 34fdee026ed49adf9d7ad2d3b3c2d397549f29fd9f896fe5d54e046456e30957 |
| paper/references.bib | 6607 | 217 | 7d 0a | 4ec09da4d7be513d2cf11811515975e1f3c35b53ae9d84cbda6748cb39cbd23b |
| notes/PUBLICATION_LOCK.md | 7996 | 148 | 4e 0a | 7eb6ad779a00c4f56f4b5bea5fc56f22ebe55ee9b80af9924d18c70d4ff834aa |
| notes/PUBLICATION_SCOPE.md | 7055 | 137 | 4e 0a | 2651dd8df815872300c020f3c243a94115c9c38c80e9d1d00fc0052ec9f23a40 |
| PAPER_PLAN.md | 18412 | 249 | 44 0a | 61be9c2849d37ba6def1e3dc43a96fcd895d0d9b36500166ff08bfe164d79ca4 |
| notes/PROOF_PACKAGE.md | 19921 | 527 | 4e 0a | c583d2cedcd97bef8410172bed967dfe99bcaf9caa69595c305bbf36ccd51fd1 |
| notes/SOURCE_LOCK.md | 9328 | 177 | 4e 0a | ab63ffebbc62149daa0db70f4378cd59604c4c24c201b70036e96f831b9560c6 |
| notes/CITATION_VERIFICATION.md | 9366 | 61 | 44 0a | 1a54b62d83cd6861679f851ec509854d6ed83eb046d5b6db7343b6e96aa9c26b |

The source rows match the locked manifest values.  The 34-row aggregate is
therefore frozen before this review artifact is added.

## Anonymous trio and source structure

The article is completely embedded in main.tex and has the neutral
Anonymous author block, empty date, relative math_commands input, and a
relative references bibliography command.  math_commands.tex contains only
notation macros and no theorem, process, or provenance text.  The
bibliography is the only other manuscript source file.  The source has an
abstract followed by exactly these eight body sections, in order:

1. Introduction and contribution boundary.
2. Related work and claim-level collision positioning.
3. Typed setup, strict cells, and omnibus theorem.
4. Positive-face survival and degree transport proofs.
5. Translation, wall monotonicity, and affine tail proofs.
6. Reflected inverse reciprocity and its span criterion.
7. Local lower-ideal lemma and exact fixture.
8. Boundaries, limitations, reproducibility, and conclusion.

No stale section include, external figure, data dependency, custom package,
or generated artifact is present in the frozen source census.  The two boxed
diagrams are native symbolic text and introduce no data or asset dependency.

## Theorem and proof census

The source states the characteristic-zero field, r >= 3, finite nonempty
collected supports in Z_{>=2}^r, nonzero coefficients, positive integer pair
seeds, disjoint algebraically independent incoming leading blocks, and the
correct typed split between the u-only cone and the w-dependent pair cell.
Certified strict edges carry unique selectors, positive source and target
carries, and the printed target/reflection certificates.  Finite branches may
stop at a tie, failed carry, empty cell, or missing certificate; the global
selector bound and tail are explicitly restricted to infinite certified strict
branches.

The following proof obligations are all visible in the main text.

* Symplectic Jacobians and the W-first, V-second inverse order, including
  nonzero subtraction signs.
* The grouped positive-face Hessian determinant, its generic secondary
  minimizer witness, the exact coefficient
  c_{alpha_0}^r (-1)^r (1-|alpha_0|) product_i alpha_{0i}, and the
  characteristic-zero Jacobian criterion plus injective substitution.  The
  argument is uniform over every nonzero coefficient choice in the locked
  support class and distinguishes a tied auxiliary face certificate from a
  strict vertex selector.
* The typed leading action (u,w) -> (B_beta A_alpha u,A_alpha u), with
  strict fresh-block carries preventing old-block cancellation.
* The exact identities v = h_V(u) 1 - u and
  u' = h_W(v) 1 - v = u + delta 1, delta = h_W(v)-h_V(u) > 0, and
  delta integral and at least one on an integer strict branch.
* The increasing envelope g(t), invariant equal-total walls, single-crossing
  unequal-total walls, the d_V+d_W-2 selector-change bound on an infinite
  certified branch, and the global-origin affine tail
  t_(n+1) = lambda t_n + mu with
  lambda = (|alpha|-1)(|beta|-1) and
  mu = ((|beta|-1) alpha - beta) dot u_0.
* Coordinate-reversal identities, the W-then-V reflected inverse phase, and
  necessity and sufficiency of the two restricted matrix identities on U_e
  and V_e.  The full-matrix upgrade is limited to full observable spans and
  reflected score/carry/target certificates are required.
* The four normalized projections and selected-minus-new margins in the
  one-edge, one-step lower-ideal lemma, including the explicit denial of
  target-core inclusion, multi-edge stability, and all-iterate stability.

## Exact fixture and boundaries

Section 7 prints the asymmetric r=3 supports and labels, all A and B
matrices, products C_21 and C_22, the C1-to-C2 target and carry forms, the C2
self-loop forms, source and reflected gaps, the weighted and baseline seeds,
independent seed and full-span determinant checks, and the reflected path.
The positive and reflected pair cells are written explicitly.  Section 8
keeps the cancellation fixture outside the headline class and separately
records the missing-reflection, tie, failed-carry, empty-cell, proper-span,
and support-boundary limitations.  It lists the anti-claims against arbitrary
support extension, global reversors or conjugacy, dynamical-degree/entropy
conclusions, scalar/Perron upgrades, non-fixed same-seed reciprocity, and
multi-edge or all-iterate perturbation stability.

## Citation, anonymity, and computational firewall

All twenty bibliography records correspond to the verified S01-S20 package;
each key is cited in the related-work synthesis and no uncited entry remains.
The bounded public screen date is preserved as 2026-08-29 UTC, with no first,
unique, exhaustive, or priority wording.  Citations are contextual only and
are not used as proof of the theorem.  Bibliography fields contain no event
IDs, paths, hashes, reviewer names, candidate IDs, or process notes.

The three manuscript files contain no identity, affiliation,
acknowledgement, internal event ID, filesystem path, hash, reviewer name,
repository or governance language, or provenance breadcrumb.  Public
arXiv/DOI URLs in bibliography records are ordinary first-party citations,
not private workflow URLs.  The article explicitly disclaims empirical
results, numerical fits, CAS certificates, code, data, scans, GPU runs, and
hidden computational evidence; the fixture is literal symbolic arithmetic.

## Disposition

The physical census, frozen-manifest binding, source-only structure, theorem
quantifiers and formulas, fixture arithmetic, citation closure, anonymity
firewall, and no-external-effect boundary have zero findings.  This review
creates no authority beyond the authorized review artifact; a later build or
source mutation would require its own ledger gate and fresh review.

BATCH07_PAPER27_SOURCE_PASS
