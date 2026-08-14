# HCS-C54 integrity report

Status: **DOCS_FINAL_NO_MORE_EDITS against the persistent scoped code/results
RELEASE_CANDIDATE and 44-entry full-project inventory; implementation-commit
provenance remains pending**.

## Mathematical red team

- “Full” is defined as full projective monomial stabilization of the
  homogeneous ideal.  No full-PGL automorphism theorem is stated.
- The ideal-to-equation-line lemma is explicit; the group enumeration does not
  assume that an ideal stabilizer already preserves the cubic line.
- The edge recurrence is solved symbolically.  Finite row scans are mutation
  guards rather than the all-\(n\) proof.
- The universal equation/group theorem is separated from packet-admissibility.
  Smooth rational packet data are inherited only for \(n=2,3,4\); every
  \(n\ge5\) packet statement is conditional.
- HCS-C53 is not credited with semisimplicity.  Theorem C fixes \(\ell\) and
  takes semisimplifications after restriction; traces, characteristic
  polynomials, ranks, and purity are unchanged.
- The rational group is a nonconstant finite etale group scheme of rank
  \(6n\) with two rational geometric elements.  The other elements are not
  claimed as individual rational maps.
- The Reynolds coefficient is \(1/(6n)\), and quadratic transfer is \(1/2\).
  These denominators are not merged.
- The ordinary-realization theorem begins with a trace identity but proves the
  same if-and-only-if classification for the complete split-local logarithm.
- Weight-zero and weight-one rails are separated before taking ranks.  The
  integral total rank \(84\) at \(n=3\) is recorded as an invalid proof route.
- The exact Cayley action includes \(\det M_g/\det A_g\).  Character
  multiplicities are written as coefficients such as \(2\varepsilon\), never
  as ambiguous tensor powers.
- The coefficient-field orbit block \(U_1,U_2,U_4\) retains multiplicity
  pair \((3,4)\).
- The common \(G_3\)-character theorem is first over \(K\).  A common rational
  group-scheme formulation requires the \(M_3\)-twisted Fermat form.
- Restriction on virtual rational classes is not called injective.  Kernel
  classes restrict to zero and cannot modify \(K\)-side rank or isotypic data.
- The inert identity is explicit and generally nonsquare.  No global root,
  continuation, functional equation, automorphy, or RH is inferred.

## Primary-source integrity

The source audit records exact locators where relied upon and verified
metadata or historical context elsewhere:

- Brünjes, arXiv:math/0301186, Proposition 3.8,
  Lemma/Definition 4.3, Theorem 4.6, and Example 4.7;
- Deligne, *Weil II*, §1.2, especially (1.2.2) and (1.2.5)(i),
  DOI 10.1007/BF02684780;
- Serre, PMIHES 54, §2.1, Theorem 1,
  DOI 10.1007/BF02698692;
- Brauer--Nesbitt, DOI 10.2307/1968918, as historical background for the
  internally stated characteristic-zero semisimple trace-rigidity lemma; no
  exact theorem-number locator is claimed;
- Nagel, Proposition 2.16,
  DOI 10.1016/S0019-3577(97)83353-8;
- Favero--Iliev--Katzarkov, §5.4 and equation (8),
  DOI 10.4310/PAMQ.2014.v10.n1.a1;
- Weil, DOI 10.1090/S0002-9947-1952-0051263-0.

No source is cited for a claim it does not make.  The novelty conclusion is
search-bounded and records databases, date, queries, and nearest primary work.

The upstream HCS-C53 source lock is read from committed git object
`9d509d3b3826b7bfbdb38ed9fe4dac9297f5dbdf`.  The checker verifies the
committed Route digest
`ae508e6e41523559f014f6fbcd0c4c199229f221fe6ac915a75cd27b02e73719`
and its exact implementation/certificate/payload/check/manifest tuple.  The
full tuple is recorded in `SOURCE_AUDIT.md`; mutable working-tree bytes are not
accepted as dependency provenance.

## Project-local release-candidate evidence

The immutable release-candidate replay passes 36 of 36 semantic checks.  The
test suite passes 93 of 93 unit tests, including all targeted hostile
mutations and the exhaustive rebound sweep of 198 semantic leaves.  The
certificate inventory has 1,078 scalar leaves: 198 semantic, 876
exact-derived, and four allowlisted history leaves.  The scoped
release-candidate hashes are:

    payload               f068d5e11ea8e6245e04bd3a30e77140267f835c4e07412ce2009c7fb04ceae1
    certificate           780cc9f249e836d3fa5b51a00fd2cdb9af0eac595d929cd1be4d728df1921846
    independent check     160b3a9d11354b41404642a3dd22d6e43f2ce576126acb21eb0133e552fc0c0a
    schema                4cee6c2252d5743ca3c5fee40ec98fbc945223312d2196fb63a43730281deedf
    code/results manifest 62f67e6d4929496974020febab3bc0e2cff45ed153b0cef51937031863d866ba

The displayed manifest hash is the digest of the persistent
`results/CODE_RESULTS_HASHES.sha256`.  Its 11 entries are exactly seven
release code files and four release result files; both manifest files are
excluded from that scope.  The 44-entry full-project inventory includes the
scoped manifest.  Only the implementation commit remains a later provenance
stage.  Temporary or unpackaged reconnaissance remains historical only and is
not a theorem input or reproducibility source.

## Compiled manuscript

The single final clean build passes and freezes a 14-page A4 PDF of 454270
bytes.  Its SHA-256 digest is
`34a0de185f16c93746ade889db2921f362906a2859b3d9786f65009224fa88b5`.
The compilation report SHA-256 digest is
`e0a2809a7d8a3aa58789e3db6d291429615b364f9cf9ebda2b6b82d8732436d2`.

The stabilized LaTeX log contains zero warnings, undefined citations,
undefined references, overfull boxes, underfull boxes, or rerun requests.
All 26 fonts are embedded, subsetted, and Unicode-mapped; no Type 3 font
occurs.  Text extraction succeeds, and representative pages 1, 11, 12, and 14
pass visual inspection.  All five scoped release-candidate hashes are
legible and extract exactly once.  Full details and the immutable build/log
digests are in `paper/COMPILATION_REPORT.md`.

## Current formal/paper source hygiene

The final source-only audit covers all 30 root-formal and paper Markdown,
YAML, TeX, and BibTeX files, totaling 157796 bytes.  It finds:

- zero CR, NUL, or ASCII control bytes other than line feed;
- zero bare quad or qquad tokens and zero bare occurrences of the audited
  TeX command vocabulary inside math;
- balanced inline/display math delimiters and LaTeX begin/end sequences;
- no trailing whitespace or missing final line feed;
- a clean no-index diff check, which explicitly covers the new untracked
  project files;
- 52 unique paper labels, 36 resolved references, 14 resolved citations,
  no unused bibliography key, and a valid Route YAML parse.

The audit was rerun after the compilation report and every final metadata
backfill; it is the documentation-freeze gate.

## Release gates

- [x] project-local release-candidate producer and independent checker,
  36/36;
- [x] 93/93 unit tests, including every targeted hostile mutation and the
  exhaustive 198-leaf semantic rebound sweep;
- [x] duplicate-key and unknown-envelope rejection;
- [x] rollback-atomic exception tests at the local write stages, with no
  power-loss or durability claim;
- [x] deterministic immutable release-candidate replay;
- [x] persistent release-candidate manifest for exactly 11 code/results
  entries, excluding both manifests from its own scope, and locked tuple;
- [x] 44-entry full-project inventory including the scoped manifest;
- [x] release-candidate promotion;
- [x] promoted RC hash insertion into exact-replay prose without theorem
  drift;
- [x] LaTeX compilation and PDF audit;
- [x] final full formal/paper raw-byte and TeX-token gate;
- [ ] implementation-commit provenance backfill after the documentation
  freeze.

## Workspace boundary

The scoped-manifest repair changes only HCS-C54 code/results, root Markdown,
paper sources/PDF/report, and the byte-identical root/archive Route-A record.
It does not modify top-level registries or the user-owned
henon_dynamics/codex_prompt.md file.
