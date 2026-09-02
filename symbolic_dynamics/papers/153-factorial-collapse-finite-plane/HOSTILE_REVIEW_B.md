# P153 independent hostile review B

**Review date:** 2026-09-02 UTC.  
**Reviewer relation:** fresh internal reader; did not author P153, implement its
Round-1 repairs, or perform Review A.  
**Protocol:** `docs/papers152_156_sequence/HOSTILE_REVIEW_PROTOCOL.md`.  
**External state:** `HOLD_EXTERNAL`.  No manuscript content was sent to an
external model, reviewer, or service.

## Verdict

**REVISE — 0 Critical / 0 Major / 2 Minor.**

The factorial-collapse graph and every-target inverse atlas survive a fresh
derivation in every stated parameter range.  The map is correctly treated as
an owned triangular-family specialization; the labelled arms, leaf sign,
temporal polynomial, `1/p/0` fibres, image and conservation laws,
identifiability boundary, fixed iterates, and zeta function are all correct.
The 18,942,551-assertion replay and source-only PDF reproduction pass exactly,
and every rendered page is visually sound.

Two local Round-1 defects remain.  First, Review A's `t=0` notation issue was
fixed in the corollary statement but the same interval-style root list remains
in its proof under a phrase that includes `t=0`.  Second, the settled and fresh
source-only logs contain a persistent pdfTeX font-expansion warning, contrary
to the Round-1 ledgers' claim of zero warnings.  Neither affects the theorem or
rendered PDF, so both are Minor; both must be repaired and recorded before
internal acceptance.

This is a raw review.  I did not edit any author source, verifier, transcript,
ledger, bibliography, PDF, or manifest.  This report is the only file added.

## 1. Frozen ceiling and claim-by-claim comparison

I cold-read `FINAL_THEOREM_CONTRACTS.md`, `FTC_FREEZE_CONTRACT.md`, the focused
FTC audit and owner log, Review A, `IMPROVEMENT_LOG.md`, `main.tex`,
`references.bib`, every paper-local Markdown ledger, `verify.py`, both frozen
transcripts, all retained PDFs and build products, and the Round-1 manifest.

| Frozen interface | Round-1 source | Review-B result |
|---|---|---|
| exact triangular-family inclusion and elementary factorial iterate receive zero credit | abstract and opening scope | PASS; literal construction and family membership are not claimed |
| `T^t(x,y)=(x+t,yP_t(x))`, time-`p` collapse, and saturation | Theorem 1(i), Lemma 2 | PASS as mathematics and mandatory input |
| one axis `p`-cycle and `p-1` disjoint labelled arms of depth `p` | Theorem 1(ii), Section 2 | PASS |
| leaf `v_(a,p)=(1,-a)` | Theorem 1(ii), Section 2 | PASS, including the Wilson sign |
| temporal polynomial with the collapse transition | Theorem 1(iii) | PASS |
| every-time, every-target `1/p/0` fibre atlas | Theorem 1(iv), equation (1), Section 3 | PASS for `t=0`, `0<t<p`, `t=p`, and `t>p` |
| image profile, target distribution, and both conservation identities | equations (2), (3), and (7) | PASS |
| exact pointwise coordinate-identifiability boundary | Theorem 1(iv), equation (8) | PASS |
| nested source observation partitions | Corollary 3 | STATEMENT PASS; proof repeats the repaired `t=0` notation defect (m1) |
| unique least-`p` cycle, fixed counts, and zeta | Theorem 1(v), Section 4 | PASS |
| odd-prime-only, formal/pointwise, ring counterexample, and owner/collision boundaries | Sections 2--4 and Limitations | PASS |

The corollary remains a direct reformulation of the frozen point-fibre atlas,
not a claim-ceiling enlargement.  Generic graph, image, and zeta language is
not assigned independent contribution value.

## 2. Fresh mathematical falsification

### 2.1 Iterate and complete-residue collapse

Induction gives

```text
T^t(x,y)=(x+t, y product_(j=0)^(t-1)(x+j)).
```

The monic degree-`p` product has the `p` distinct field elements as its roots,
so `P_p(X)=X^p-X` in `F_p[X]`.  This is not the zero polynomial; evaluating it
on `F_p` makes it vanish pointwise.  Hence `T^p(x,y)=(x,0)`, after which the
ordinate stays zero and the abscissa keeps translating.  This proves the
`t>=p` saturation without importing it from enumeration.

### 2.2 Labelled graph, depths, and equality cases

For an off-axis source, the first zero multiplier is the unique residue step
with `x+j=0`.  Counting that transition, its depth is the representative of
`1-x` in `{1,...,p}`; every off-axis state enters `(1,0)`.  At depth `s`, the
first coordinate is `1-s`.  Evolving through the preceding `s-1` nonzero
factors multiplies the ordinate by

```text
(-1)^(s-1)(s-1)!.
```

Labelling the resulting depth-one ordinate by `a` gives exactly

```text
v_(a,s)=(1-s, a/[(-1)^(s-1)(s-1)!]).
```

Substitution verifies every arrow, including `s=1`.  Distinct labels give
disjoint arms, and `(p-1)p` transient vertices exhaust the complement of the
axis.  For odd `p`, Wilson gives
`(-1)^(p-1)(p-1)!=-1`, so the leaf is `(1,-a)`.  There are `p-1` states at each
positive depth `1,...,p` and `p` recurrent axis states, giving
`p+(p-1)(z+...+z^p)` with the final collapse transition included.

### 2.3 Target fibres, images, inverse information, and boundaries

A time-`t` target `(u,v)` forces the source abscissa `x=u-t`.  The ordinate
equation is

```text
v=y C_t(u),   C_t(u)=product_(r=1)^t(u-r).
```

If the coefficient is nonzero, field division gives one source.  If it is
zero, `v=0` gives all `p` source ordinates and `v!=0` gives no source.  There
is no division in either zero case.

For `0<=t<=p`, the indexed root set is `{r:1<=r<=t}` in target-column
coordinates and has exactly `t` distinct members; at `t=0` it is empty and at
`t=p` it is all of `F_p`.  For `t>=p`, every later product retains a complete
residue system.  With `r_t=min(t,p)`, this gives

```text
N_1=p(p-r_t),  N_p=r_t,  N_0=r_t(p-1),
|im T^t|=p(p-r_t)+r_t.
```

Both `N_1+N_p+N_0=p^2` and `N_1+pN_p=p^2` hold.  The source abscissa is always
known from a feasible observation; the ordinate is known exactly in the
nonzero-coefficient case.  An impossible target is not mislabeled as an
ambiguous observation.  The source observation partitions are nested because
the roots of `P_t(x)` are the indexed set `{-j:0<=j<t}` before saturation.

The composite-ring warning is also valid: over `Z/4Z`, `(2,2)` collapses in
one step, and the target equation `2y=2` has the two solutions `1,3`.  Thus the
field inverse trichotomy is not silently extended to residue rings.

### 2.4 Periodic data

If `p` does not divide `n`, the first coordinate changes by a nonzero field
element, so there are no fixed points.  If `p` divides `n`, then `n>=p` and
collapse gives `T^n(x,y)=(x,0)`; exactly the `p` axis points are fixed.  They
form one orbit of least period `p`, while all other points are transient.
Therefore

```text
#Fix(T^n)=p 1_(p|n),
sum_(n>=1) #Fix(T^n) z^n/n = -log(1-z^p),
zeta_T(z)=1/(1-z^p).
```

No characteristic-three or cycle-multiplicity exception occurs.

## 3. Review-A closure

Review A returned 0 Critical / 0 Major / 2 Minor.

1. **`t=0` column notation: only partially closed.**  The corollary statement
   now uses `{-j:0<=j<t}` and explicitly says the family is empty at `t=0`.
   That source-level repair is correct.  Its proof, however, repeats the old
   interval-style list under a range that includes `t=0`; see m1.
2. **Missing declarations: fully closed.**  The Round-1 manuscript contains
   explicit Limitations, Data Availability, Ethics Statement, Author
   Contributions, Conflict of Interest, Funding, and External Status
   paragraphs.  `HOLD_EXTERNAL` is visible and no declaration exceeds the
   anonymous internal scope.

## 4. Owner-zero-credit and portfolio attacks

The decisive owner subtraction remains explicit.  After exchanging
coordinates to `(Y,X)=(y,x)`, the map becomes `(Y,X)->(YX,X+1)`, the
`g_0(X)=X`, `h_0=0`, `a=b=1` specialization of the
Ostafe--Shparlinski triangular family.  Construction, family membership,
generic degree-growth machinery, and the elementary product iterate therefore
receive zero contribution credit.  Ostafe's maximal-period systems, Maubach's
triangular automorphism/conjugacy work, and Konyagin et al.'s univariate
functional-graph framework are nearby or generic background, not owners of the
retained nonpermutation graph/fibre conjunction.  The bounded conjunction
non-hit is not promoted to novelty, priority, or ownership completeness.

The internal firewall also survives.  P99/P104 share only product/cocycle
notation; P150 is the closest graph/fibre/zeta interface but uses a rationally
totalized finite-plane map and a different identity; P152 is a stochastic
absorbing count chain; P154 is a subgroup-normalizer forest; and P155/P156 are
rank-changing permutation extractors.  P153's separating mechanism is the
progressive factorial zero schedule and its target-resolved column atlas, not
generic finite-map vocabulary.

## 5. Fresh replay and evidence semantics

From a scrubbed process I ran

```bash
env -i PATH="$PATH" LANG=C.UTF-8 PYTHONDONTWRITEBYTECODE=1 python3 verify.py
```

Fresh stdout was byte-identical to both `CANONICAL.txt` and
`verification_output.txt`, with transcript SHA-256

```text
fd900d9d0c1233a265834ce7efc25c43e2c9360a5cb3bbb5eaef4d125f67d6f9
```

and terminal profile

```text
PROFILE_SHA256 b44a7815c886a98409b5f56a0c26ce24f8644fa4f6b57a238d5a50d8a2d83810
TOTAL boxes=25 states=75993 assertions=18942551
VERDICT PASS_EXACT_REPLAY
```

The 25 boxes, 75,993 states, assertion total, profile digest, and manuscript
figures agree with every ledger.  The script independently pressures literal
trajectories, first-repeat graph shapes, indegrees, arm labels, every target
through `t=p+3`, and fixed sets through `3p`.  It does not prove the all-prime
quantifier, exhaust owners, establish novelty or priority, validate prime-power
or ring extensions, or authorize release.

## 6. Source-only build, PDF, manifest, and visual inspection

A fresh temporary directory containing only `main.tex` and `references.bib`
completed the declared sequence

```text
pdflatex -> bibtex -> pdflatex -> pdflatex.
```

Its PDF was byte-identical to both `main.pdf` and `main_round1.pdf`:

```text
pages=5
bytes=394720
SHA256=81e56c67a1029add2bc93aaf67add40cbc68016a82e8eb2a1b7025cad2d3bb7a
```

An additional settling pass left the PDF byte-identical but retained the
warning in m2.  The historical artifact remains unchanged:

```text
main_round0_original.pdf
bytes=393462
SHA256=8940cc2979406cd788e9a1c2ed23cb76422c50ff92fe99723608d0cfcb8dfd77
```

Before this report was added, `SHA256SUMS` excluded itself and covered exactly
all 23 other retained paper-local files; `sha256sum -c` passed 23/23.  The
manifest must be regenerated after this report and Round-2 artifacts are
frozen.  Its expected temporary omission of this newly added report is not
scored as an author defect.

The settled log has no unresolved citation/reference, rerun request,
overfull/underfull box, or build error, but it does contain the persistent
pdfTeX warning described in m2.  `pdfinfo` reports five A4 pages, no encryption,
no form, no JavaScript, no CreationDate or ModDate, and blank
title/author/subject/keyword metadata.  All 30 `pdffonts` rows are embedded,
subsetted, and Unicode mapped.  `pdftotext` contains no path, email address,
affiliation, ORCID, acknowledgement, corresponding-author marker, or
nonanonymous identity.

I freshly rasterized and inspected all five Round-1 pages.  The complete
theorem, dependency displays, labelled-arm derivation, progressive-collapse
table, repaired indexed set in the corollary statement, owner firewall,
transcript excerpt, declarations, and bibliography are legible and inside
page bounds.  No clipping, overlap, blank page, corrupt glyph, unresolved
marker, displaced float, or visible identity leak was found.

## 7. Findings and required repairs

### m1 — Minor: Review A's `t=0` notation defect remains in the corollary proof

**Evidence.**  The statement at `main.tex` lines 324--330 is repaired correctly:
it uses `x in {-j:0<=j<t}` and declares the family empty at `t=0`.  The proof at
lines 335--341 then says, without excluding time zero, that “Before time `p`,
the distinct roots of `P_t` are `0,-1,...,1-t`.”  Since “before time `p`”
includes `t=0`, this repeats the interval-style expression that Review A
identified as not literally empty.  The theorem and intended proof are clear,
but the Review-A repair is not complete everywhere in source.

**Required repair.**  Replace the proof's list by the indexed set
`{-j:0<=j<t}` (or split out `t=0` and quantify the displayed list only for
`1<=t<p`).  Record the closure in the improvement ledger and rebuild; do not
change the theorem ceiling or saturation clause.

### m2 — Minor: a persistent source-only pdfTeX warning contradicts the
Round-1 QA record

**Evidence.**  The retained `main.log` contains, at line 670,

```text
pdfTeX warning (font expansion): font should be expanded before its first use
```

The same warning appeared in the fresh source-only final pass and remained
after one additional settling pass, although that extra pass left the PDF
byte-identical.  This contradicts `FINAL_QA.md` lines 11--13 and
`IMPROVEMENT_LOG.md` lines 22--24, which report zero build/package warnings.
No overfull/underfull box or visible font defect occurs, so the issue is local
build hygiene/provenance rather than mathematical or rendering failure.

**Required repair.**  Correct the font-expansion initialization or microtype
configuration so the declared source-only sequence settles without this
warning, then rebuild and update the PDF digest and QA/build ledgers as needed.
Do not merely suppress the diagnostic while leaving its cause unaudited.  A
fresh final log must support the revised zero-warning claim.

## 8. Decision

The theorem, owner, portfolio, verifier, metadata, font embedding, anonymity,
and visual gates otherwise pass.  Internal acceptance is withheld until m1 and
m2 are repaired, documented, rebuilt, and followed by the mandatory Round-2
manifest freeze.

**Final Review-B verdict: REVISE — 0 Critical / 0 Major / 2 Minor /
HOLD_EXTERNAL.**
