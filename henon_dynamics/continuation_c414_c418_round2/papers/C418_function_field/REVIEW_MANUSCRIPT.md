# C418 independent manuscript review

Status: **PASS / CLOSED — bounded actual-manuscript mathematical and
citation review**.
Date: 7 September 2026.
Reviewer: the current team's nonauthor function-field proof/source
reviewer. This reviewer did not author the C418 TeX or its new equality
table. The work is AI-assisted internal review, not human peer review,
publication acceptance, worldwide novelty certification, or the final
release gate.

## 1. Actual artifact and review scope

The following were read in full:

- `main.tex` and all seven included substantive section files;
- `references.bib`, `CITATION_AUDIT.md`, and `AUTHOR_HANDOFF.md`;
- the actual nine-page `main.pdf` via complete text extraction, including
  the abstract, all three tables, equations, proofs and bibliography;
- the stable `../../function_field/PROOF_PACKAGE.md`, compared with this
  reviewer's prior complete proof review and affected-revision closure;
- `../../function_field/SOURCE_AUDIT.md` and the supplementary execution
  receipt, read as records of their stated evidence roles.

The first combined terminal output was truncated in presentation. The
missing source/receipt/hash material and PDF pages 1–3 were explicitly
read in smaller bounded calls; no completeness claim rests on truncated
output. The final proof step and its scope section were also read to EOF.

No author file was edited. No LaTeX build, graph enumeration, finite-field
sample, mathematical script, old-batch certificate, external model API,
or fresh literature search was run. PDF text extraction used stdout and
did not create a file in the author directory. The only new file written
by this reviewer is this report.

The reviewed frozen proof has SHA256
`a5f10ff4354adb0fa86ffdf6868b9f7c7658e2e95116a62d20142c0308be6ccb`.
The prior independent review, including the final Step 5 converse
clarification, has SHA256
`0880b910fade20f089a2fc710b115d6378d7c17c1a96e4388a17359792bf736c`.
The actual manuscript preserves the mathematical claims and all-field
proof of that pair. The new explicit coordinate table is checked below
independently of the author's statement that it was corrected.

## 2. Claims–evidence verdict

| Actual manuscript claim | Verification | Verdict |
|---|---|---|
| All fields k of characteristic not two, all a in k*, all nonconstant polynomial c, every point of k(t)^2 | Theorem 2.1, Lemmas 3.1–3.2 and Proposition 3.3 retain these exact quantifiers. No perfection, completion or global finite-set maximum is assumed. | PASS |
| Existence forces c=-P^2+C; C is unique and P unique up to sign | The degree-factorization and centered-square argument are in the body. The uniqueness proof retains both the C-D nonzero and zero cases. | PASS |
| Exact sixteen signed labels rather than an unrestricted horseshoe | Proposition 4.1 proves injectivity and both directions of the restricted-map description. | PASS |
| Exactly seven possible bit cycles over every allowed field | Section 5 gives the least-state cases directly from the complete edge table, including the characteristic-three equations. No sampled characteristic or characteristic-zero gcd replaces the proof. | PASS |
| Ordinary least periods and disjoint simultaneous rows | Lemma 5.1 restores the sign, proves leastness by label injectivity, and proves distinct bit cycles have disjoint point sets. | PASS |
| Full sharp 14/8/6 totals and a^4=1 restriction | Section 6 keeps all collisions and all determinant cases; Theorem 2.2 matches the proved equality conditions. | PASS |
| Explicit fourteen-point equality table | All three coordinate words satisfy the literal recurrence, have the declared least periods and represent mutually disjoint ordered-pair sets; see Section 4 of this review. | PASS |
| Native ordinary return formula and finite-cycle zeta | Corollary 6.1 is the direct divisibility formula for these same finite cycles, with no change of map, field or clock. | PASS |

No required mathematical repair was found. The manuscript does not
promote the supplementary nineteen-cycle computation into the proof of
the arbitrary-field classification.

## 3. Sensitive proof transitions rechecked

### Rational coordinates, common degree and normalization

At a finite polynomial prime, the maximal pole order M in one finite
orbit produces valuation -2M on the left of the recurrence and at least
-M on the right. The constancy and nonvanishing of a are used exactly
where needed. The inverse map makes the cyclic recurrence valid for
periods one and two as well.

At infinity, the maximum degree m is taken separately within one orbit.
The quadratic leading degree forces deg(c)=2m, and every coordinate in
that orbit has degree m. Since m=deg(c)/2 depends only on c, comparison
across two arbitrary cycles is legitimate without first assuming the
whole periodic set finite. The factorization
`(y-sigma P0)(y+sigma P0)` then leaves a constant offset, because the
second factor has degree m and 2 is nonzero.

Completion of the square is only a parameter normalization. If two
centered representations exist, `(P-Q)(P+Q)=C-D` first forces C=D,
then Q=±P in the integral domain k[t]. This covers arbitrary imperfect
or infinite constant fields. The abstract's phrase “P or -P plus a
constant” is correctly restricted by the later offset equations; it
does not assert that there are only two individually fixed translates.

### Bit constraint and exact signed graph

The offset equation is
`b_i=(a+1)/2-delta_i-a delta_{i-1}`. Squaring it and using binary
idempotence gives, at the unshifted index,
`K_a-C=a^2 delta_{i-2}+2a delta_{i-1} delta_i+delta_{i+1}`.
The manuscript's shifted equation (4.3) and all sixteen edge labels in
Table 2 follow. Outgoing labels differ by 1 and incoming labels by
a^2; both are nonzero in every allowed field.

For the signed label E(epsilon;u,v,w), the first leading coefficient
determines epsilon; the ratio of the two leading coefficients determines
v. Only after that does the first offset determine u, and the second
offset determine w. This order avoids the possible offset collision at
a=1. The manuscript also carries the precise converse added during the
frozen proof review: the leading coefficients of H(E) first determine
epsilon'=epsilon(-1)^v and v'=w, then the first offset gives u'=v
using a≠0, and the remaining equation is the graph edge with z=w'.
Thus the restricted graph is an if-and-only-if description, not merely
a sufficient construction.

### All-field exhaustion and period restoration

The minimum-state cases 000, 001, 010, 011 (both first edges), and the
remaining states exhaust the possible simple directed cycles. In both
exceptional cases the retained equations are `2a=1` and `a^2=1`.
Their combination implies 4=1, hence characteristic three and a=-1.
They are not discarded as inconsistent merely over characteristic zero.

The seven words have parity and ordinary lifts:

| Word | Bit length | Sign after one bit traversal | Ordinary cycles |
|---|---:|---:|---|
| 0 | 1 | + | two fixed points |
| 1 | 1 | - | one two-cycle |
| 01 | 2 | - | one four-cycle |
| 001 | 3 | - | one six-cycle |
| 011 | 3 | + | two three-cycles |
| 00011 | 5 | + | two five-cycles |
| 0111 | 4 | - | one eight-cycle |

Injectivity of the full signed label proves these are least periods.
In particular the two positive-phase lifts are not identified under
coordinate sign or rotation. These multiplicities exactly match Table 1.

## 4. Independent literal check of the new fourteen-point table

For characteristic three, a=-1 and c=-P^2-1, the coordinate recurrence is

```text
y_i^2-P^2-1 = y_{i+1}-y_{i-1}.
```

The table's four-word is

```text
(P+1, P-1, -P+1, -P-1).
```

Computing either side around that word gives the same vector

```text
(2P, -2P, -2P, 2P).
```

The positive five-word is

```text
(P+1, P, P, P-1, -P).
```

Both sides give

```text
(2P, -1, -1, -2P, -1).
```

At the last index the right side is `(P+1)-(P-1)=2`, which equals
-1 in characteristic three. This is the potentially easy-to-miss
wraparound identity, and it holds for the actual current table.

The second five-word is obtained by replacing P by -P while keeping
the same constant offsets:

```text
(-P+1, -P, -P, -P-1, P).
```

Its recurrence vector is `(-2P,-1,-1,2P,-1)`. This is not a claim
that every coordinate of the positive five-word is simply multiplied
by -1. Such a global negation would change the offsets and is not the
rule used in the manuscript.

For a direct disjointness check, the four-word projects to bit states
{101,010} and visits both phases. Each five-word projects to
{100,000,001,011,110}; these two five-cycles use complementary phases
over every one of those five states. The full signed labels are
injective, so the sets of ordered pairs are disjoint and have sizes
4,5,5. Repeated individual coordinates P or -P do not merge ordered
pairs. There are fourteen points, with least periods 4,5,5, exactly
as claimed. These checks were hand algebra on the written formulas;
no field-evaluation substitute or program was run.

## 5. Sharp coexistence check

For a not in {1,-1}, fixed-point and two-cycle parameters are distinct.
The only additional possibility is a^2=-1, which coexists with the two
fixed points at C=K_a, giving 8; otherwise the total is at most 2.

For a=1, the four possible `(C,point contribution)` pairs are
`(1,2),(-3,2),(0,4),(-1,6)`. In characteristic different from two
the only collision is -3=0 in characteristic three, giving 2+4=6.
It does not collide with the six-point two-three-cycle row.

For a=-1, C=0 gives two fixed points and one two-cycle, hence 4.
C=-1 gives the four-cycle and, only in characteristic three, the two
five-cycles, hence 14. The other exceptional characteristic-three
value C=1 gives one eight-cycle. Those three values are distinct.
This proves the unique fourteen-point equality locus and preserves
all lower-field totals. Outside characteristics two and three, a square
root of -1 gives the unique eight-point determinant condition; when
there is no such root the a=1,C=-1 locus attains six. Taking P=t
attains every asserted maximum over the stated field itself.

## 6. Source scope and manuscript exposition

The two actual bibliography entries are cited, and neither has invented
metadata. The manuscript and audit preserve the source boundaries already
checked in the proof review:

- Ingram's actual normalization is phi_alpha=(alpha y,x+f(y)); the
  displayed conjugacy L=(-ax,y) yields alpha=-a, so alpha=1 means
  the present a=-1. The citation distinguishes the 2014 journal record
  from the accessed arXiv:1111.3609v1 text and does not claim a newly
  read final journal proof. The quadratic routing is not silently replaced
  by the degree-at-least-three estimate.
- Allen–DeMark–Petsche's comparison retains completeness, local
  compactness, odd residue characteristic, the square condition and
  the horseshoe parameter region. J=(-y,-x) yields (-c,-a). The
  manuscript does not identify completion itineraries with k(t)-rational
  itineraries or extend their field hypotheses to arbitrary k.
- C412 is expressly an unpublished repository note, with its sign/offset
  mechanism deducted rather than claimed anew. The current theorem is
  self-contained and does not require an unpublished external proof step.
  The audit records a local locator without inventing a journal entry.
- The nineteen-cycle execution statement is supplementary and matches
  the coordinator's retained receipt. This review did not rerun, audit
  the source code of, or independently certify that execution. All-field
  mathematical validity rests on the displayed least-state proof.

The introduction states the result and ownership clearly, the exact
atlas is near the front, and all promised proof steps appear in the
body. Table 2 serves the exhaustion and Table 3 serves the sharp-locus
construction. The finite-cycle zeta is correctly presented as a corollary
of the same object, not an additional paper or a target arithmetic claim.
No substantive narrative repair is required for the present bounded
review. No external novelty or selected-venue assessment is made.

## 7. Read-only PDF and bibliography checks

The reviewer ran the following read-only commands from the C418 paper
directory (the complete extraction was followed by a bounded pages 1–3
read when a combined tool display truncated):

```sh
pdftotext -layout main.pdf -
pdftotext -f 1 -l 3 -layout main.pdf -
pdfinfo main.pdf
rg -n 'Warning|undefined|Overfull|Underfull|multiply defined|LaTeX Error|Fatal error' build_author/main.log build_author/main.blg
rg -n '\\cite|\\nocite|^@|TODO|FIXME|PLACEHOLDER|TBD' sections main.tex references.bib
```

The PDF extraction and metadata commands exited 0. The PDF is nine
letter-size pages, 341,957 bytes, unencrypted, with empty author metadata
and no JavaScript. Both bibliography items and all three tables appear
in the extracted text. The final log search had no matches (rg exit 1,
not a compilation failure). The citation search shows exactly the two
cited external keys, with no nocite expansion or unfinished placeholders.

The stable source and PDF hashes at review were:

```text
dade97cf4fbf9ddb22cd35d3766242d100b666eb1cbc81937c0d8ce7d8de7084  main.tex
1072ab97376e6af235818a5b6709145ccf8f5dd877ba4ddd9a13f6a391cff995  sections/1_introduction.tex
5acf2c7e22a428b7db896f1e2d18e153de8b10847ef99fa8af08904a01bba319  sections/2_atlas.tex
aba8abbd23791cbd65313b10af779e0009085b415c0aba1dd3b6b35cc702926a  sections/3_rigidity.tex
9e9ba15b02b6ebb5f3dd14dd2451976f3d4e7c83d10ccffb8fdb39c223faa85d  sections/4_graph.tex
3ff5268060984a44198bf41eea82715c28b57f7df168670a0972cc3a1814b70e  sections/5_exhaustion.tex
cefda173fc4768d59c76d2872df9ed208ec3e2687ff84cbce4ace8e21c8d6aa2  sections/6_bounds.tex
9de374757f3bebc856e1b1368a80282037ef548dc659a28d0fdd0bbf18f69017  sections/7_scope.tex
21284d37d84251e0530839c58c4194d2e4cac12cdd8ddf871b37da450ec6284b  references.bib
cb11f5eb464cb770b18a049a410bcd76e9269c277312532c2d47f2557104bc3d  CITATION_AUDIT.md
0c9d6c53a422b8a8733cfaab68afdc0b60daedec57c46468973e63e1d844ac6e  main.pdf
```

No new final visual check or deterministic build is claimed here.
The coordinator retains all-page visual inspection, two fresh final
builds, evaluation, sealing and Git. For the exact reviewed TeX/Bib/PDF
text, the required mathematical and citation corrections are **none**.
