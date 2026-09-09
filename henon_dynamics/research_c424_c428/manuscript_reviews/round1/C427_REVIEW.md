# C427 actual-manuscript nonauthor review — round 1

Date: 2026-09-09 UTC. Reviewer: current-team agent
`round6_positive_characteristic`, not the author of the C427 manuscript.
This reviewer previously reviewed the R6 mathematical proof package; that
earlier review was treated as provenance, not as the present manuscript
review. The present assessment is based on the actual frozen LaTeX,
bibliography, rendered PDF, source record and retained build evidence.

## Decision

**Recommend PASS for manuscript-review round 1, with zero must-fix
findings.** One optional wording clarification is recorded below.

The accepted mathematical content has been migrated into a readable,
self-contained new n>=4 argument without weakening the all-input,
all-integer-point, native-clock, freely parametrized or exact-least-period
requirements. The n=3 theorem remains a clearly identified inherited
computer-assisted dependency. The level-height appendix includes the
degenerate directions instead of silently invoking a full Vieta-group
fundamental domain.

This is an internal nonauthor assessment, not human peer review, a formal
Route-A score, proof of global priority, journal acceptance, the second
manuscript pass, or final release/build sealing. The coordinator must
adjudicate this review and separately initiate the next required stage.

## Frozen object and actual reading

Paper directory: `papers/C427_vieta_semilinear/` relative to this batch.
The reviewed PDF is 13 pages, 346767 bytes, SHA256
`ff63cdac04d87d212e7c902ce61c56695587e3b12379e180bd6f9c3c3e4dd021`.
It equals `builds/initial_03/main.pdf` byte for byte.

I read all nine TeX files and the entire BibTeX file, the complete
extracted PDF text, and every separately rendered PDF page 1–13. I also
read the actual `README.md`, `PAPER_PLAN.md`, `SOURCE_AUDIT.md` and
`BUILD_LEDGER.md`, inspected the input manifest, final engine and
bibliography diagnostics, and checked the retained source archive.
The frozen manifest passed all ten file checks. Every one of its ten
entries was independently compared by SHA256 with the corresponding
member streamed from `builds/initial_03/source.tar`; all matched.
Fresh `pdftotext -layout main.pdf -` output also matched the retained
`builds/initial_03/main.txt` exactly.

| Record | SHA256 |
| --- | --- |
| `INPUT_MANIFEST.sha256` | `caed08ab3f6522ed74bbe2bece36556c1b81fed28f93714ca550c80e9b85e305` |
| `builds/initial_03/source.tar` | `35e78c9503e6f08c3f9ce2e3a2877a71d840f6636cc64344c2df507340862f83` |
| `README.md` | `4887ce9e98ae2c75d8efb74f4e585ac1a13c5afad9ce0825f3c0cc9691dd9d1c` |
| `PAPER_PLAN.md` | `2bd09b0153bbf25e7457960077a48997c8a7325e93588bbf52e885b32efdf66f` |
| `SOURCE_AUDIT.md` | `1abd7f6a6503ef9af184e152acc95734d4482a84fd1c594a98657673474f784f` |
| `BUILD_LEDGER.md` | `4c50be9d870b96ecdb0d395addfaf259d5072fb1b85f93f3349a1bbe14b7928f` |

The complete reviewed source identity is:

```text
b2692505b12faf8ff30598d1be3d7563170d078173b2474853d0948e35fdf184  main.tex
37da752a679690d585d27589205ccd5b863f1ff2a2fa503d74212b2e32f2312b  math_commands.tex
133829fcecde21b8be888891fa8a64a1efd6b91b92566d5377ec83952caa87d2  references.bib
2fe935b8b648a9ca110a660357de2245eb7ca2e45d4f7a77bb76dfccf01713d0  sections/00_abstract.tex
c04d9102e4e2191ac9d6a4ea7bae53938f1b4fe567772b8a4c023c146a86e8d8  sections/01_statement.tex
09fccd90fbeb980a43e5f629926a469102eb47ebc1e4b3424f6e1eacc49ca234  sections/02_blocks.tex
19ee5f474edd5928de53de34bbfd06dad6ac742a5d8b98e75219bf6076a4fcb6  sections/03_classical.tex
b1e23411589a52b562c5fb1bd73bcd2d413101fc13c9cf51d4b061d77c60d931  sections/04_atlas.tex
da61a16a96c6caf797de19c0dcbcd9c553921972c2a1092cccdccf9472a6ab00  sections/05_completion.tex
c357b5befb562bb4b1f5e5f3a973de364d6d979034cf1c2f70d87ce4b274cc30  sections/appendix_height.tex
```

## Mathematical and migration audit

### 1. Exact object and statement

Section 1, especially Theorem 1.1 and equations (1.1)–(1.4), preserves
the specified map, explicit integral inverse and invariant. The
coordinate substitution `t -> Q+a-t` proves invariance directly.
No smoothness, nonzero-coordinate or positive-coordinate qualification
has appeared during migration. One application of F remains one step.

The definition of a linear set explicitly leaves all nonnegative
parameters free; it does not conceal a residual invariant equation,
nonlinear integer equation or injectivity assumption. Overlap and
dependent directions are permitted. Deleting zero directions makes
every retained channel genuinely unbounded: fixing the other parameters
and increasing one parameter along a nonzero integer vector suffices.
The finite remainder and channels are defined for fixed `(n,a)` before
any level D is chosen. The polynomial-shear counterexample correctly
explains why a uniform period bound alone does not imply semilinearity.

### 2. New local rigidity, including mixed-zero words

I checked Lemmas 2.1–2.2 and Corollary 2.3 directly in
`sections/02_blocks.tex`, not merely against the earlier review.

- The product bound is local to one maximal nonzero block. A shifted
  window never imports the height of a different block through a zero.
  When the new external factor is zero, its required estimate is
  immediate; otherwise the shifted window stays inside the same block.
- For an internal maximum, a length-`n-1` window with that maximum
  strictly internal exists because `n-1 >= 3`. Both external absolute
  values become at most 2, giving the stated `|a|+4` contradiction.
  The zero-free and all-zero cases are also accounted for.
- A block of length `n-1` has product `-a`, hence cannot be large.
  For a longer block, the endpoint maximum forces the internal product
  to be a sign and every internal factor to be a unit. Reversal is used
  only to arrange this proof; it does not identify native oriented cycles.
- For length at least `n+1`, the nonzero next coordinate really forces
  `a != 0`, sign `+1` and value `2a`. The next window yields
  `2A(M-A) <= M+A+1`; the displayed contradiction is valid since
  `(2A-1)(A+4)-(2A^2+A+1)=6A-5>0` for `A>=1`.
- The length-n case leaves exactly the two asserted endpoint windows.
  A nonzero window with a large factor therefore has precisely one such
  factor and unit companions. Zero-containing products remain exactly
  zero even with several arbitrarily large other coordinates.

Thus the manuscript retains the essential new mixed-zero mechanism.
It neither assumes independence of successive blocks nor substitutes
one example of an unbounded family for exhaustiveness.

### 3. Classical period and cone constructions

In Section 3.1, the 2-adic near-identity proof tracks the minimum vector
valuation correctly. Doubling increases the finite valuation by exactly
one; an odd number of iterated displacements preserves it. Every
positive putative return time is covered. For an integral polynomial
automorphism, the return map on a residue ball has an integral inverse
and an affine coefficientwise reduction modulo 2. Its affine order
divides `E_n`; squaring `id+2V` is coefficientwise `id+4W`. It follows
that the original least period divides `2re`, hence the explicit `L_n`.
This proves a divisor bound without changing the native clock.

In Section 3.2, the homogenized cone is pointed and its normalized
section compact; vertex enumeration uses finite rational linear
systems, including lower-dimensional cases. Clearing denominators
produces a finite ray list. The integer remainder after flooring ray
coefficients lies in the displayed finite coordinate box. That box
therefore really supplies a finite generating set, with no empirical
cutoff. In the first-coordinate-one slice there is exactly one
first-coordinate-one generator and only first-coordinate-zero generators
besides it. Formula (3.3) consequently has genuinely free nonnegative
parameters. Slack variables, integer affine projection, the zero cone,
empty solutions and zero-variable cases are all covered.

These facts are correctly credited as classical tools, not separately
promoted as new results.

### 4. Complete tagging and exact least-period strata

I checked all rows of Table 2 and the two directions of Proposition 4.1
against the original recurrence. Every tag has exact magnitude and sign
semantics. A rejected zero-free window contradicts Corollary 2.3 for a
true periodic word; every retained product expression is its actual
product, not a relaxation. Requiring all L recurrence equations makes
the converse a real periodic native orbit. Retaining every phase and
working modulo L cause no missing-orbit or clock quotient.

For Section 4.2, imposing r-periodicity is supplemented by a finite
disjunction of explicit integer witnesses for failure of each proper
divisor. The signed inequality at a witness is equivalent to a genuine
coordinate inequality. All witness/sign choices are enumerated; each
branch is again a linear integer system. Thus no period-degeneracy
exception remains as a nonlinear condition on the final parameters.
The scalar word period equals the least state period because a length-n
state determines the full word, both forwards and backwards. Projection
to that state cannot accidentally relabel a shorter period.

Section 4.3 removes zero projected directions and collects singleton
outputs into an explicit finite `E_{n,a}`. Any surviving direction gives
an unbounded subset consisting entirely of points with the same exact
period. Same-period overlaps are harmless, while different period
strata cannot intersect. The stated finite remainder is uniform over
D, and every enumeration bound is determined by `(n,a)`. No final
unresolved polynomial locus, guessed finite core or executed all-input
atlas is substituted for the claimed terminating construction.

### 5. Inherited n=3 theorem and computational ownership

Section 5.1 is explicit at the theorem statement, the ownership table,
the proof and the limitations. I checked its use against the actual
C421 theorem section and complete `IR1_CLASSIFICATION.md` table.
The imported exact-period set is
`{1,2,3,4,5,6,8,9,12}`. Constant solutions form a finite set. The
alternating-pair relation is `(u-1)(v-1)=1-a`: it gives finite divisor
enumeration when `a != 1`, and two affine lines with the prescribed
orientation/period exclusions when `a=1`. The remaining parametric
words are affine with linear parameter restrictions or finite
exclusions; the two sporadic words are finite. Splitting integer rays
and taking consecutive triples gives exactly the required semilinear
format, with periods inherited from the table.

No new enumeration was performed or implied here. The C421 finite
certificate is not silently relabelled as computation-free by the new
n>=4 proof. Its dependency is important but is neither concealed nor
described as an external journal result.

### 6. Height appendix and finite-level counting

Appendix A, pages 12–13, supplies the full auxiliary proof. I checked
the adjacent native updates at an orbit maximum of the sum-height and
all branches `Q=0`, `|Q|>=3` including zero endpoint sum, `|Q|=1`, and
`|Q|=2` with small or large endpoints. In particular:

- the fork inequalities follow from the preceding and following
  native states, not from unrestricted generator minimality;
- for `Q=2`, the large same-sign branch with nonzero forcing gives the
  stated linear bound on the endpoint sum; at zero forcing the two
  endpoint updates are fixed;
- for `Q=-2`, the large opposite-sign branch forces `x+y=a/2` and
  both endpoint updates are fixed; odd a leaves no such integer branch;
- in the remaining fixed-endpoint directions, the next native update
  of `z_1` yields `(u-1)(v-1)<=A+2n-1`, while `|u-v|<=A/2` excludes
  unbounded endpoints;
- the final extra factor n is correctly retained because the chosen
  point maximizes sum-height, not every individual coordinate.

The radius `2n^2(|a|+|D|+n+2)` follows for the entire periodic orbit,
including singular levels and zeros. Section 5.2's finite-box graph
therefore has exactly the true native periodic cycles. It counts
distinct points rather than overlapping parameter representations.
The cycle-count identity and finite ordinary zeta product have their
proper source-dynamical meaning. The example `(0,a,0,t)` for n=4,
`a != 0`, has the displayed eight-word, invariant `t(t-a)` and exact
period eight, because its fourth iterate changes the first coordinate
and every proper divisor of eight divides four. It remains explicitly
illustrative, not the basis of the completeness theorem.

## Sources, attribution and reading boundaries

All six bibliography entries are used. I directly checked the relevant
primary records during this review: [Whang, arXiv v3](https://arxiv.org/abs/2305.13529v3),
[Hu–Tan–Zhang, arXiv v2](https://arxiv.org/abs/1501.06955v2),
[Ginsburg–Spanier, publisher PDF](https://msp.org/pjm/1966/16-2/pjm-v16-n2-p09-p.pdf),
[Maloni–Palesi–Tan, EMS record](https://ems.press/journals/ggd/articles/13338),
and [Shin, arXiv v2](https://arxiv.org/abs/2312.07890v2).
The Ginsburg–Spanier title/authors and initial effective-semilinearity
statements were inspected; the arXiv/EMS checks established the named
versions, metadata and stated scope. They are not represented as fresh
whole-paper proof reviews. The local C421 theorem and complete
classification were read as described above. No claim of a new Springer
journal-page read or fresh reading of every previously cited fork proof
is made.

The source audit's earlier primary reading is distinguished from new
opens and failed access. The full-group/unforced setting of
Markoff–Hurwitz antecedents is not used as a theorem for this one forced
native map. Classical period/semilinear theory is deducted from the
new-contribution claim. The retained single integrated contribution is
the mixed-block reduction and effective full periodic atlas. No
systematic worldwide-priority or retraction search is certified by this
bounded source check.

## Presentation, build evidence and reproducibility

All 13 actual page images are legible. I found no clipping, overlaps,
missing equation content or broken tables. The final short reference
page 11 is explained by the explicit appendix break and is not missing
material. The anonymous 11pt article has no selected venue quota.
All 19 font rows are embedded, subset Type 1 fonts with Unicode maps.
The PDF is unencrypted and has no JavaScript.

The final engine/BibTeX diagnostic check found no substantive warning,
undefined reference/citation, overfull/underfull box or TeX error. A
deliberately broad case-insensitive search also matches the installed
`infwarerr` package's descriptive text and BibTeX's `warning$ -- 0`
counter; neither is a warning. The source/PDF/archive equality checks
above validate the exact object reviewed, not an independent fresh
compilation. The three genuine initial builds are retained with the
documented layout-only changes and are not passed off as manuscript
reviews or the still-pending final fresh-build pair.

No source file, PDF, metadata record or prior mathematical evidence was
modified during this review. No unchanged mathematical program or
certificate was rerun. No external paid model or manuscript upload was
used. The only written artifact is this review file.

## Findings and disposition

Must-fix findings: **0**.

Optional O1 — magnitude wording in the abstract:
`sections/00_abstract.tex:11`, PDF page 1, says “a coordinate larger
than `|a|+4`.” Consider “a coordinate whose absolute value exceeds
`|a|+4`.” The current phrase is a true but weaker positive-coordinate
formulation; the full body correctly proves and uses the absolute-value
statement, with both signed large tags. This is an optional precision
improvement, not a mathematical gap or condition of the round-1 PASS.

The coordinator may accept that one-line clarification or record a
reasoned decision to retain the text. Any revised version must be
identified and sent through the separately assigned second actual
nonauthor manuscript pass. This review does not itself close that pass,
formal evaluation, final-build reproducibility or release gates.
