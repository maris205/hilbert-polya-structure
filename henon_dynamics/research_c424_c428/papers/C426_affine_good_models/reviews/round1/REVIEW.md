# C426 — first actual nonauthor manuscript review

2026-09-09 UTC. Reviewer: coordinator, not the GR5 proof or C426
manuscript author. Current-team internal review, not human peer review
or an external-model service. This review follows the actual first
PDF and is not a relabeling of the GR5 admission or outline reviews.

## Verdict

The complete accepted all-affine local/global classification has been
transferred into a readable, self-contained 10-page mathematical
manuscript. No critical/major mathematical, source-ownership or
evidence defect was found. Three minor presentation corrections below
are recommended before the second actual manuscript pass. They do not
change any theorem, quantified domain, proof or computation count.

**Mathematical must-fix: 0. Source/evidence must-fix: 0.**
Second manuscript review, formal evaluation and final reproducible
build/release checks remain open. No journal acceptance score or
submission-readiness certification is assigned.

## Actual inputs and reading scope

The reviewer read all ten editable manuscript inputs in full: main,
the bibliography, seven section files and the source-ownership table;
read the entire actual PDF text (an initially truncated middle range
was reread), and separately viewed all ten rendered PDF pages. The
README, entire manuscript SOURCE_AUDIT and BUILD_LEDGER were read.
The complete original GR5 contract, original source audit and
coordinator source comparison were reread; relevant original review
sections were checked as provenance, not substituted for this review.
The original full proof had already been read during admission; this
pass independently follows every typeset proof rather than rerunning
that admission procedure.

Frozen input PDF SHA256:
`85677da439f31f1c2faea804430c8f395a2aaa235a0d20696e0a97a8ca08ed38`.
The actual initial source archive is
`builds/initial_02/source.tar`, SHA256
`d027a620a4a330bfdcafb5bc6dd724f720604cb136609447ee757825764b6cec`.

| Input relative to `papers/C426_affine_good_models/` | SHA256 |
| --- | --- |
| `main.tex` | `f7cdb1decbbfb790bad87c63179714302db289ea18028c8dd38c6758a3e19712` |
| `references.bib` | `236b3e561c23da17df00d6dc9f5f1ffe51a6ec526f0bbc1a8bd70454e7c2ae68` |
| `sections/01_introduction.tex` | `3938336f24736c069f003d907b3d0c4d2aa2d51360dc61a282d342bb72a41a6d` |
| `sections/02_classification.tex` | `e1435da1871f79207d9a4c50441880e02046868b5af6a5fe09316b17b496d5dd` |
| `sections/03_local_rigidity.tex` | `4f613e8c9ac19c1e8606d1c0cb1e9350bd4fca47e1af14e058ec99d3356ed202` |
| `sections/04_local_test.tex` | `346740d7e24fffbd38aa840bf15d39a6b2a2926a92bd29a40350108a8792afa3` |
| `sections/05_global.tex` | `6e73beca2bd34c2991fcb4aabf3aa9850ebfd32b05569ce123c0bf306a881169` |
| `sections/06_examples.tex` | `4e91d529c53eda0b62ee022e28d7d5893311852df4f2b4862b977ab01e976c35` |
| `sections/07_scope.tex` | `7cccb15510622ef8f54d9da94bc7f645e8a65c355ec6fe3d572f1dca5117e583` |
| `tables/source_scope.tex` | `06d649e46b5bb1f162b1d0fbac231d302b9d9388db0483b6fb27a0fd1d67ebaa` |

## Substantive manuscript checks

1. **Theorem/definition alignment.** Definition 2.1 requires both
   coefficient integrality and degree preservation, plus geometric
   separation of the reduced indeterminacy sets. Theorem 2.2 covers
   arbitrary number fields, all nonzero Jacobians and degree at least
   two, with the full local/global affine group. Nonunits, fractional
   scale exponents and failed centre tests are genuinely rejected
   branches, not excluded hypotheses. No field extension is smuggled in.
2. **All-affine necessity, not a diagonal ansatz.** In Lemma 3.1,
   the pure monomial of a primitive row form remains a unit after
   taking its dth power, even when the residue characteristic divides
   d. The two primitive vector factors therefore identify the two
   actual geometric indeterminacy points. Their separation makes the
   row-direction matrix integral and invertible. Only then is the
   affine map reduced to two scalar directions. The forward and inverse
   linear coordinates force their ratio to be a unit and their centre
   difference integral at that scale. Every right composition used is
   authorized by the proved integral-conjugacy invariance.
3. **Scalar algebra and wild centres.** Equations (4.1)–(4.2)
   have the correct q=f-aY and the subtraction of the centre r.
   The d=2 subleading coefficient is explicitly q1=f1-a. The
   valuation of the subleading factor is e-k; this yields a complete
   O/dO list modulo sO. All coefficients, including the constant,
   are tested, so necessity of the candidate list is not confused
   with sufficiency. The Q2 example is checked directly: r=0 fails
   and r=1/2 gives Y²+Y.
4. **Uniqueness has a complete original-field proof.** A polynomial
   with integral coefficients and unit leading coefficient has bounded
   forward-orbit set exactly O in E: outside O the top term strictly
   dominates. Affine conjugacy with q makes the disc intrinsic. This
   is an auxiliary q-orbit argument, explicitly not a new clock for F.
5. **Finite and exact local arithmetic.** After a is globally a unit,
   only nonunit leading coefficients or denominators in q require
   individual tests. Outside that finite support s=1,r=0 works,
   including otherwise wild primes. Local uniformizers and residue
   representatives may be chosen in K without requiring a prime
   ideal to be globally principal.
6. **Centre patching includes new denominator primes.** Lemma 5.1
   uses CRT for every positive valuation of DI, not merely the original
   support. Places introduced by D are expressly included. Intersections
   of the local fractional ideals recover the asserted global coset.
7. **The obstruction is I², not I.** Exterior powers prove
   I²=(det A). The two-generator lemma and displayed matrix prove the
   converse with no PID assumption. Both inclusions in AR²=I⊕I are
   established by the explicit inverse. Local factorization proves
   regular good reduction, not only determinant integrality.
8. **All models and examples.** Equality of the local lattices and
   translations proves the whole global left coset. The fixed-field,
   fixed-degree criterion realizes every (d-1)-torsion ideal class using
   q=bY^d. In Q(sqrt(-5)), I²=(2), I is nonprincipal and the shown
   matrix has determinant 2. In Q(sqrt(-23)), alpha has norm 8,
   lies only over I and yields I³=(alpha); the norm form excludes
   principality of I and hence of I². The examples are full direct
   verifications, not numerical evidence for a generalization.
9. **Evidence and route scope.** All central arguments are in the
   PDF; internal notes are provenance only. The finite prescription
   is not described as an executed algorithm. Section 7 excludes
   nonaffine maps, compactification changes, Hénon products and field
   extensions. It neither computes nor promises target Euler factors,
   root numbers or a spectral realization.

## Fresh primary-source spot checks

Four primary endpoints were directly reopened during this manuscript
review, with targeted follow-up reads/finds and no new search query:

- [Kawaguchi publisher PDF](https://msp.org/ant/2013/7-5/ant-v7-n5-p08-s.pdf):
  title and metadata; Definition 4.1 and surrounding regular-reduction
  conditions read directly. Its three requirements agree with the
  manuscript's geometrically interpreted definition. This is not a
  fresh full-paper read.
- [Bruin–Molnar publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/3294C6C9B556A6D2D1EC553E168BAD5D/S1461157012001131a.pdf/minimal_models_for_rational_functions_in_a_dynamical_setting.pdf):
  Proposition 2.10 and Remark 2.11 were read directly; the named
  Example 6.4 endpoint and its statement were located. The one-dimensional
  rational-map scope is correctly distinguished. The full example had
  been read in the preceding source stage; no new full-example read is
  claimed here.
- [Petsche–Stout journal record](https://jtnb.centre-mersenne.org/articles/10.5802/jtnb.889/):
  the abstract explicitly concerns projective endomorphisms over a PID;
  volume 26 (2014), 813–823 and the separate 2015 online date were checked.
- [Allen–DeMark–Petsche v3](https://arxiv.org/html/1610.04271v3):
  standing odd-residue-characteristic scope and Theorem 11, including
  its full unit-ball equivalence proof, were read. The manuscript
  credits the quadratic unit-ball regime, not the present all-affine
  necessity or arbitrary-ideal sufficiency, to this result.

All five bibliography entries are cited. The internal reference is
clearly labeled unpublished AI-assisted notes. No missing central
reference, invented publication or out-of-scope theorem application
was found within these checks. This is not worldwide priority or
systematic retraction/venue/interest certification.

## Minor requested presentation corrections

| ID | Severity | Location and concrete correction |
| --- | --- | --- |
| P1 | Minor clarity | Abstract: replace `uses no mathematical computation` with `requires no computer-assisted certificate` (or equivalent). The article does contain explicit mathematical calculations; the intended distinction is zero program executions. |
| P2 | Minor typography | Introduction, prior-work paragraph: `arbitrary-class-` followed by a source newline and `group` renders as `arbitrary-class- group`. Write the natural phrase `statement for arbitrary class groups` and reflow the sentence. |
| P3 | Minor bibliography | Reference [3] renders `8 September 2026, 2026`. Remove the duplicated year by keeping `8 September` in the descriptive field and the single `year={2026}` field, or move the full date to a separate note. Preserve the true unpublished/internal label and exact source link. |

These are not proof gaps, and they do not justify mathematical reruns.
Preserve the genuine first source/PDF, apply the chosen small changes,
compile a real round-one revised PDF, and submit the actual revision
and diff for the second scheduled manuscript pass.

## PDF and build observations

All ten current rendered pages were visually read: formulas, the
single ownership table and references are legible, with no clipping or
overlap. The table naturally moves to page 2. The final engine/BibTeX
logs were checked for warnings, over/underfull boxes, undefined items
and TeX errors; no match. The true first build and its sole layout
correction remain recorded. Font and deterministic-release tests are
not promoted beyond the author ledger at this pass; final inputs still
need the prescribed two fresh builds and final read-only verification.

Reviewer actions: static source/PDF/log reading, ten page-image views,
hash/inventory reads, and the bounded primary web checks above.
Zero mathematical programs, zero old certificate reruns, zero external
uploads, and no manuscript-source edits were performed by this reviewer.
