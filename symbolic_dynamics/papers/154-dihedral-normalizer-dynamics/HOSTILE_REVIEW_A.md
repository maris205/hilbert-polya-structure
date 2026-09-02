# P154 independent hostile review A

**Review date:** 2026-09-02 UTC.  
**Reviewer relation:** independent internal reader; did not author P154.  
**Protocol:** `docs/papers152_156_sequence/HOSTILE_REVIEW_PROTOCOL.md`.  
**External state:** `HOLD_EXTERNAL`. No manuscript content was sent to an
external model or service.

## Verdict

**REVISE — 0 Critical / 0 Major / 3 Minor.**

The owner-subtracted theorem package survives the hostile read. I found no
counterexample to the forest, every-time fibre, signature, or collision
theorems; no direct owner of the retained conjunction in the frozen primary-
source record; no verifier/transcript inconsistency; and no anonymity or PDF
integrity failure. The required changes are local but real: make two state/time
domains literal in the theorem statement, reconcile one cited author's
conflicting name metadata, and add the final LaTeX pass that the clean build
actually needs for a warning-free settled log.

This is a raw review. I did not edit `main.tex`, `references.bib`, `verify.py`,
either transcript, either PDF, `SHA256SUMS`, or any author ledger.

## 1. Package and theorem-ceiling comparison

I read `GDN_FREEZE_CONTRACT.md`, `FINAL_THEOREM_CONTRACTS.md`, both focused
GDN audits, the GDN owner-search record and collision firewall, `main.tex`, all
paper-local Markdown ledgers, `references.bib`, `verify.py`, both frozen
transcripts, the TeX/BibTeX build artifacts, and the five-page Round-0 PDF.

| Frozen interface | Manuscript interface | Hostile result |
|---|---|---|
| complete subgroup carrier and one-step normalizer rule | Theorem 1(i), equations (1)--(2), Section 2 | PASS; visibly assigned zero contribution credit |
| exact parity-halving iterates and binary inverse forest | Theorem 1(i)--(ii), equations (3)--(4) | PASS, subject only to the explicit-domain repair m1 |
| every positive-time image | Theorem 1(iii), equation (5) | PASS for every `t>=1`, including stabilization |
| every-target, every-time fibres | Theorem 1(iii), equations (6)--(7), Section 3 | PASS, including zero fibres and source-mass closure; target-domain wording joins m1 |
| iff unlabelled-graph signature | Theorem 1(iv), equations (8), (13) | PASS; necessity covers `m=1` and separates `a=0` from `a=1` |
| explicit 33/35 non-identifiability and common two-power lifts | Theorem 1(iv), equation (14) | PASS; an actual commuting 52-state bijection is supplied |
| owner-zero-credit and portfolio firewall | Sections 1 and 5, Table 1 | PASS, subject to citation-metadata repair m2 |

The zeta expression is correctly labelled generic bookkeeping and supplies no
standalone paper value. The manuscript does not exceed the frozen ceiling or
turn a bounded source non-hit into a novelty or priority claim.

## 2. Independent theorem rederivation and proof attacks

### 2.1 Carrier, one-step rule, and iteration

For a subgroup outside the cyclic rotation group, its rotation intersection
is the unique `R_d=<r^d>` and any contained reflection fixes one residue
`j mod d`; hence the displayed `R_d` and `H_(d,j)` keys are disjoint and
exhaustive. Their count is `tau(n)+sigma(n)`.

Every `R_d` is normal. Conjugation by `r^u` carries `r^j s` to
`r^(j+2u)s`, so a rotation normalizes `H_(d,j)` exactly when `d|2u`.
Conjugation by `r^u s` gives the companion condition `d|2(u-j)`. Both cosets
therefore form

~~~text
H_(d/gcd(d,2), j mod (d/gcd(d,2))).
~~~

This also handles `d=1`, and no division by a potentially zero quantity is
present. Writing `d=2^k e` then removes exactly one factor of two per step and
proves equation (3) for every admissible state and every nonnegative time.
The algebra is correct; the theorem statement simply leaves `t`, `k`, and
`j` implicit, which is the local defect m1.

### 2.2 Forest and all-time fibres

Fix an odd divisor `e|m` and a residue `j_0 mod e`. At level `k`, the exact
vertices above the root `H_(e,j_0)` are

~~~text
H_(2^k e, j_0 + ell e),       0 <= ell < 2^k.
~~~

Reduction modulo `2^(k-1)e` pairs these vertices into two children over each
parent. This proves a full binary transient tree of height `a` at each of the
`sigma(m)` fixed roots. Separately, all `tau(n)` rotation states are depth-one
leaves at `H_(1,0)` only. The depth polynomial and fixed-iterate census follow
without an omitted component.

For a positive-level target, the time-`t` source set is explicitly

~~~text
{H_(2^(k+t)e, j + ell 2^k e) : 0 <= ell < 2^t},
~~~

when `k+t<=a`, and is empty otherwise. This gives equation (6), including its
zero branch. For a root, levels `0,...,min(t,a)` contribute respectively
`1,2,...,2^min(t,a)` sources; every rotation contributes at every positive
time only to the distinguished root. Thus equation (7) is exactly

~~~text
2^(min(t,a)+1)-1 + tau(n) 1_((e,j)=(1,0)).
~~~

Summing these pointwise fibres recovers `sigma(n)+tau(n)` for every `t>=1`.
The image contains precisely the levels `0,...,max(a-t,0)`, proving equation
(5). No saturation or equality case is missing.

Small hostile boundary boxes make the two mechanisms transparent:

| `n` | boundary | independently recovered graph |
|---:|---|---|
| 3 | `a=0` | four fixed roots; two rotation leaves only at the distinguished root |
| 6 | `a=1` | four roots, two dihedral leaves per root, and four extra rotation leaves at the distinguished root |
| 4 | `m=1`, `a=2` | one seven-vertex binary tree plus three rotation leaves; ten vertices total |
| 8 | `m=1`, `a=3` | one fifteen-vertex binary tree plus four rotation leaves; nineteen vertices total |

### 2.3 Signature necessity, including `m=1` and `a=0/1`

A directed graph isomorphism preserves fixed vertices, so it first recovers
`sigma(m)`. Let `L` be the maximum transient tail. If `L>=2`, rotations
cannot create that depth and `a=L`.

If `L=1`, then `a` is zero or one. In either case `n>=3` forces `m>1`, hence
there is a nondistinguished fixed root. For `a=0`, every such root has only
its self-loop as an incoming edge; for `a=1`, every root also has exactly two
dihedral leaf predecessors. This graph-internal property distinguishes the
two cases without using the excluded parameters `n=1,2`.

If `m=1`, then `n>=3` forces `a>=2`, so the preceding maximum-tail argument
already recovers `a`; no comparison with a nonexistent second root is needed.
After `a` and `sigma(m)` are known, the graph's vertex count gives

~~~text
tau(n) = |V| - sigma(m)(2^(a+1)-1).
~~~

For example, `n=4` gives `10-1*(8-1)=3`, exactly `tau(4)`. This closes the
necessity direction in the single-root case. Conversely, equal signatures
let one match the distinguished roots, all remaining roots, every binary
position, and the extra rotation leaves; the map commutes level by level.
Both directions of the iff statement therefore hold.

### 2.4 The 33/35 commuting bijection

Both parameters are odd, with `sigma=48` and `tau=4`. Hence all 48 dihedral
states are fixed. Map the distinguished root to the distinguished root, match
the remaining 47 dihedral keys in the stated lexicographic order, and map

~~~text
R_1 -> R_1,  R_3 -> R_5,  R_11 -> R_7,  R_33 -> R_35.
~~~

The first 48 states commute because both updates fix them; the last four
commute because every rotation maps to the distinguished root. The domain and
codomain each have 52 states, so this is a bijection, not a count-only
argument. Multiplication by `2^b` preserves the three signature coordinates:
`a=b`, `sigma(odd)=48`, and `tau=4(b+1)`. The sufficiency construction then
provides every lifted conjugacy.

## 3. Owner and source attack

### Direct ownership receiving zero credit

- Cavior and Conrad own the cyclic/dihedral subgroup coordinates and counts.
- Frenkel owns the odd self-normalizing/even doubled-normalizer rule in an
  equivalent dihedral parameterization.
- Shelash/Ameen, Ahmad, and Obaid give the complete one-step subgroup-
  normalizer cases, including rotation subgroups and parity halving.

The paper places all of that material on the input side of the dependency
diagram and does not use it as residual contribution value.

### Nearby ownership and standard tools

Shelash--Ashrafi's two-adic Wielandt-length calculation is appropriately
treated as nearby ownership of the halving-clock intuition, not as an owner of
the pointwise functional graph. Generic finite-map zeta bookkeeping, divisor
sums, rooted-tree counting, and normalizer-tower vocabulary also receive no
separation credit.

### Residual and bounded non-hit

The surviving conjunction is the complete iterated forest, every positive-
time target fibre, the iff unlabelled-graph signature, and arithmetic order
non-identifiability. The frozen primary/author-hosted source record contains no
direct statement of that conjunction. This is only a bounded non-hit; the
paper says so explicitly. In accordance with the review instruction, I used
the frozen primary-source audit and did not send the manuscript to a live
bibliographic, model, or other external service. The internal records expose
one author-name discrepancy that must be resolved in m2.

## 4. Portfolio-collision attack

- **P142 reserve:** divisors and two-adic halving overlap, but P154's literal
  carrier is every subgroup and its arrow is the ambient normalizer. Its
  residual iff graph signature and 33/35 collision are absent from the
  divisor-only gcd reserve.
- **P91/P135:** finite-group vocabulary overlaps, but there is no relation
  shift, centralizer partition, spectrum, or wreath-product mechanism here.
- **P153:** both maps have finite branches, images, fibres, and periodic data.
  P153 has factorial arms entering a translating field cycle; P154 has
  parity-halving binary forests entering fixed roots.
- **P152:** the apparent binary silhouette is only superficial. P152 is a
  stochastic reflected Bellman chain on a triangular book, not a deterministic
  subgroup inflation map.
- **P155/P156:** their carriers change permutation rank and their inverse
  obstructions are right-to-left minima or Ferrers matchings. Neither the
  literal map nor the proof engine transfers to P154.

The paper passes the portfolio gate because it leads with the subgroup-
normalizer forest and arithmetic graph inverse, not with generic graph,
fibre, divisor, or binary-tree language.

## 5. Independent verifier and transcript replay

I cold-ran the verifier in a scrubbed process:

~~~bash
env -i PATH=/usr/bin:/bin PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 \
  /usr/bin/python3 verify.py
~~~

Fresh stdout was byte-identical to both `CANONICAL.txt` and
`verification_output.txt`, with transcript SHA-256
`25ab2e157715ddce077402e8f9383a7d52c261401d6579035eb43e8e945e9219`.
It ended with:

~~~text
PROFILE_SHA256 6eed12ce0c63f2d20f734ac1fa67634ce445140372dfc53e779a389de023b782
TOTAL boxes=44 iso_pairs=4 assertions=29590
VERDICT PASS_EXACT_REPLAY
~~~

The 44 boxes materialize each displayed subgroup as an element set, establish
key uniqueness, compute each normalizer by ambient conjugation, and check
depths, fixed roots, images, source mass, and every target through `a+3`.

The computation does **not** brute-force all subsets to prove subgroup
completeness; prove an all-`n` quantifier; prove ownership or novelty; or
authorize release. Its expected image/fibre formulas are theorem-coded. The
four isomorphic-pair checks use `predicted_next`, rather than recomputing the
literal normalizer inside that lane, although 33, 35, 66, and 70 occur
separately among the literal boxes and the manuscript proves the commuting
map. The verifier also does not scan unequal signatures for necessity. Those
interfaces rest on the deductive arguments in Sections 2.1--2.4 above, not on
29,590 bounded assertions.

## 6. Source-only build, PDF, manifest, and anonymity

A fresh temporary directory containing only `main.tex` and `references.bib`
completed the documented LaTeX/BibTeX sequence. The resulting PDF was already
byte-identical to the package PDF:

~~~text
pages=5
bytes=374722
SHA256=45901bc68e404cd387c48c848b87ce98d24ead5d60c9ec52b7d584fcb34e60f3
~~~

However, after exactly the four commands printed in `BUILD.md`, the clean
`main.log` still contained `Label(s) may have changed. Rerun to get
cross-references right.` One additional `pdflatex` pass removed that message;
the PDF hash did not change. This reproducibility-documentation mismatch is
m3, not a manuscript or PDF failure.

I rasterized and inspected all five pages. The theorem, dependency display,
equations, ownership table, transcript excerpt, and all five references are
legible and within bounds. There is no clipping, overlap, unresolved marker,
or corrupt glyph. All 26 font rows are embedded, subsetted, and Unicode
mapped. PDF title, author, subject, and keywords are blank; dates are absent;
the file is A4, unencrypted, and has no form or JavaScript. Visible authorship
is `Anonymous`, and text scans found no workspace path, email, affiliation,
ORCID, acknowledgement, or corresponding-author marker.

`main.pdf` and `main_round0_original.pdf` are byte-identical. Before this raw
review file was created, all 15 frozen entries in `SHA256SUMS` passed. The
manifest was not edited.

## 7. Findings and required repairs

### m1 — Minor: theorem formulas (3) and (6) leave admissible domains implicit

**Evidence Anchor:** text: Theorem 1(i), `main.tex` lines 112--116, "where
\(e\mid m\)"; Theorem 1(iii), lines 136--143, "For \(k\geq1\)".

**Confidence:** 5/5; direct quantifier audit of the displayed theorem.

Equation (3) uses `t` without saying `t>=0` and does not state
`0<=k<=a` or the residue range for `j`. Equation (6) similarly writes a
target `H_(2^k e,j)` after saying only `k>=1`, even though an actual carrier
target requires `1<=k<=a`, `e|m`, and `0<=j<2^k e`. The surrounding carrier
definition and proof make the intended domains recoverable, so no formula is
false; the all-parameter theorem should not leave them inferential.

**Required repair.** In Theorem 1(i), quantify equation (3) for `t>=0`,
`0<=k<=a`, `e|m`, and `0<=j<2^k e`. Before equation (6), quantify every
positive-level carrier target by `1<=k<=a`, `e|m`, and the same residue
range. Keep the zero-fibre condition `k+t>a` unchanged.

### m2 — Minor: the direct-owner citation has unresolved author-name metadata

**Evidence Anchor:** text: `references.bib` entry `ShelashEtAl2023`, "Hader
Baqer Shelash"; GDN owner-search log lines 63--68, "Hayder Baqer Ameen (the
PDF header uses the surname Shelash)".

**Confidence:** 5/5 for the internal metadata conflict; the repair deliberately
requires resolution against the authoritative record rather than guessing a
preferred form.

The bibliography and rendered reference use `Hader Baqer Shelash`, while the
frozen owner audit identifies the same DOI under `Hayder Baqer Ameen` and
notes a different surname in the PDF header. `SOURCE_VERIFICATION.md` says
publisher PDF and DOI metadata were checked but does not resolve or even
record this discrepancy. The owner subtraction remains substantively valid,
but the primary direct-owner citation is not metadata-clean.

**Required repair.** Recheck the DOI/publisher bibliographic record and the
article's own author line; use one authoritative citation form consistently in
`references.bib`, and record any Ameen/Shelash and Hader/Hayder variant in
`SOURCE_VERIFICATION.md` so the identity choice is auditable. Do not weaken
the zero-credit assignment while making this repair.

### m3 — Minor: the documented clean build stops one pass before a settled log

**Evidence Anchor:** text: `BUILD.md` lines 9--12, "pdflatex ... bibtex ...
pdflatex ... pdflatex"; clean source-only replay, "Label(s) may have changed.
Rerun to get cross-references right."

**Confidence:** 5/5; reproduced in an isolated source-only directory and
cleared by exactly one additional pass.

The documented sequence generates the correct byte-identical PDF, but its
last log still requests a rerun. The package's stored settled log reflects a
later pass, so `BUILD.md` does not quite reproduce the claimed warning-free
build state.

**Required repair.** Add one final `pdflatex -interaction=nonstopmode
-halt-on-error main.tex` command, or instruct the reader to continue until
cross-references settle. Update `FINAL_QA.md` to record the actual pass count.
The extra pass should leave the PDF hash unchanged in this environment.

## 8. Decision

The central theorem, owner subtraction, collision firewall, exact replay, and
Round-0 PDF all pass. No Critical or Major repair is required. Internal
acceptance is withheld until m1--m3 are closed in source/artifacts, documented
in `IMPROVEMENT_LOG.md`, and followed by `main_round1.pdf` as required by the
protocol.

**Verdict: REVISE — 0 Critical / 0 Major / 3 Minor / HOLD_EXTERNAL.**
