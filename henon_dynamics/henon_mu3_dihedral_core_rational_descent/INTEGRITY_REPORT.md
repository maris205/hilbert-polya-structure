# HCS-C53 integrity report

Status: **PASS; implementation provenance backfilled**

## Mathematical red team

- The family theorem is proved symbolically. The three quadratic edge
  classes and determinant row-permutation sign are written explicitly;
  the \(n=2,\ldots,10\) calculations are controls, not the all-\(n\)
  proof.
- Smoothness and motive extraction are restricted to certified
  \(n=2,3,4\). Rows \(n\ge5\) retain only an algebraic \(\Q\)-form.
- The C52 group has order 24. Reynolds averaging uses \(1/24\), while
  quadratic cycle transfer uses \(1/2\).
- The descended group is a nonconstant finite \'etale group scheme split
  by \(K\); twenty-four individual \(\Q\)-automorphisms are not claimed.
- Raw strict compatibility and integrality are separated. The monic
  factor is \(\chi_p(U)=\det(U-F_p)\); only afterward is
  \(P_p(T)=T^{10}\chi_p(T^{-1})\) placed in \(\Z[T]\).
- Every local formula uses geometric Frobenius with
  \(F_p\mid\Q_\ell(-1)=p\). Reciprocity is derived from the
  self-transpose idempotent, nondegenerate restricted pairing, and
  Frobenius similitude, without semisimplicity.
- Fourth-row exponent clearing is restricted to good split rational
  primes. The inert polynomial identity is explicit and no global
  half-root, continuation, or functional equation is inferred.
- One-prime irreducibility is a future criterion. Its conclusion is
  limited to rational projectors with nonzero proper cohomological image;
  phantom and coefficient-extension projectors remain open.
- No conic-bundle/Prym statement is imported without an independent
  flatness theorem.

## Exact code replay

A read-only default replay passes:

- 20/20 independent semantic gates;
- 63/63 targeted mutation tests;
- 42/42 full-project manifest entries.

Locked release-candidate hashes:

- certificate:
  f4325a5987933e2acf81656389d46701d82d38912c546d1e5996123f617f6e79;
- payload:
  8064224eda63fa9d890efd26ec9aa167c7cd9458662620be3135196a09494d41;
- independent check:
  0d38643ded626c2a5e1536c8a4df9c56ae98c4fda01e1d15660996ea8c495e67;
- pre-integration code/results manifest:
  b62f353d119d6c8565f513dad771a047a5e6343411d08ad2e91562fe84923480.

The \(p=7\) trace is labeled
PRE_C53_RECONNAISSANCE_REGRESSION_ANCHOR_UNCERTIFIED. The checker verifies
recorded arithmetic consistency but does not independently reconstruct the
fixed-locus point counts. No C52 provenance is asserted.

## Documentation and byte hygiene

The twelve theorem/research Markdown files plus Route-A YAML have:

- no CR bytes;
- no forbidden ASCII control bytes;
- no trailing-whitespace errors under git diff --check;
- a parseable Route-A YAML record;
- no raw lost-backslash qquad tokens;
- no uncertified auxiliary-geometry claim.

The ordered SHA-256 list of those 13 files, excluding this report, has
aggregate SHA-256

9fe74130f60c105e95e45aa559b762cdf95d74ec758484d05271b67c77f3b43d.

This is the final documentation aggregate; release-integration metadata must
record it without reopening these files.

## Paper and PDF

The paper-compile audit passes:

- 13 A4 pages and 430815 bytes;
- PDF SHA-256
  0fcae5c42fa5803749956bb62c56f0f25f0148aa1019704b2dc43dcc443a518f;
- zero undefined citations or references;
- zero LaTeX/package warnings and zero overfull/underfull boxes;
- all fonts embedded and subsetted, with no Type 3 fonts;
- successful text extraction; the changed replay page 11 was re-rendered
  and visually inspected, while the prior page 1, 7, 10, 12, and 13 audit
  remains valid;
- every section source referenced by main.tex;
- all eight bibliography entries cited.

The ordered SHA-256 list of the 16 stable paper sources/report/PDF files has
aggregate SHA-256

e59beee292830263189aaed6fe558a21e3ca5ec6ea5a5c57c12dd3f90b19f33e.

## Provenance and workspace

- C52 source implementation commit:
  208feef86365cd92ace8dad02904acff6623eeec.
- Frozen C52 certificate:
  a2b0b281bfb311f979c7ed65e441a184ebe338b05f5fec8a60768610965c9c94.
- C53 implementation commit:
  0a7f0fdb8290eab4aa92ed5ade432401c40c22cf.
- The user-owned untracked file henon_dynamics/codex_prompt.md was neither
  read for content nor modified, staged, or included in an artifact list.

The theorem documents, Route-A record, manuscript, compilation report, and
PDF are final against the release-candidate evidence tuple above.  The
certificate has status `RELEASE_CANDIDATE`; the implementation SHA is
backfilled into this report, the project README, and both Route-A records.
The default runner verifies the complete project manifest without changing
stable files.
