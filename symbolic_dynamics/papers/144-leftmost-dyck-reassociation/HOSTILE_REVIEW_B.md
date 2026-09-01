# Hostile Review B — independent round-2 audit

**Paper:** *Leftmost Reassociation of Dyck Components: Exact Transient
Layers and Terminal Depth Fibres*
**Review date:** 2026-09-01 UTC
**Reviewer posture:** independent hostile round 2; the reviewer did not author
the manuscript and did not perform the round-1 repair
**Review scope:** theorem correctness, source/owner honesty, round-1 closure,
canonical controls, bibliography, isolated build, and round-0/round-1 PDF
provenance and visual integrity

## Verdict and severity count

**ACCEPT** for the internal round-2 gate.

External status remains **HOLD_EXTERNAL**.  This acceptance is a correctness
and artifact-integrity decision only.  It is not novelty, priority, ownership,
posting, submission, or circulation clearance.

| Severity | Count |
|---|---:|
| Critical | 0 |
| Major | 0 |
| Minor | 1 |

The round-1 major finding is closed.  The Pallo/Chapoton neighbourhood and the
ordered-plane-tree carrier are now exposed and conservatively subtracted.  The
formal theorem survives a definition-level reconstruction, the canonical
verifier replay is byte-identical, and a build from only `main.tex` and
`references.bib` reproduces the checked-in current PDF byte for byte.

The one minor issue is an abstract-level missing range on the iterate
description.  The displayed lemma, endpoint proof, and fixed-after-entry
definition already make the full orbit correct, so this does not block
acceptance.

## Materials independently examined

I read the following in full:

- `main.tex` and `references.bib`;
- `HOSTILE_REVIEW_A.md` and `IMPROVEMENT_LOG.md`;
- `README.md`, `PAPER_PLAN.md`, `NARRATIVE_REPORT.md`,
  `CLAIMS_EVIDENCE.md`, `SOURCE_VERIFICATION.md`, `CONTROL_RESULTS.md`, and
  `BUILD.md`;
- `verify_p144.py` and the complete frozen `verification_output.txt`;
- the settled auxiliary bibliography/build records `main.bbl`, `main.blg`,
  and the warning-relevant portions of `main.log`;
- all five rendered pages of `main_round0_original.pdf` and all six rendered
  pages of `main_round1.pdf`; because `main_round1.pdf` and `main.pdf` are
  byte-identical, this is also a page-by-page inspection of the current PDF.

No manuscript, bibliography, support document, verifier, transcript, or PDF
was modified.  This review file is the only paper-directory output of round 2.

Current hashes relevant to the audit are:

| Artifact | SHA-256 |
|---|---|
| `main.tex` | `c1991a40333a9b4de8645c3af3f1b0fe3e1ca3fcc30884e84a4af6611d61b657` |
| `references.bib` | `31a99d316771dca9180cf999decbcaa62171110d08f4c504191d03b1649617e0` |
| `HOSTILE_REVIEW_A.md` | `192696d8bc5c950cb2330d185d8dab4286df608828feee3222d86745f6a0cb5c` |
| `IMPROVEMENT_LOG.md` | `cdd6a824bffabcb30132b8c6f1d20148534a52db8e35ad1ff9dfe9d6011f194c` |
| `verify_p144.py` | `4e8e0762bf45c110f47ae99bcd394b226c4e7680fb6c9278c6624a9994052560` |
| `verification_output.txt` | `c9f7c02c4dcbe598ad4b0b8ed260256bd808987d7369cf8a300ef1f8ca046294` |
| `main_round0_original.pdf` | `f30d0145385d226ac66b75c280db956672f714d27e1e3c65169e37273c8baf26` |
| `main_round1.pdf` | `24a483f852b5c2fd29e5acf8ccc19aafe218928d7b5efb247a640444e1ef050c` |
| `main.pdf` | `24a483f852b5c2fd29e5acf8ccc19aafe218928d7b5efb247a640444e1ef050c` |

## Severity-ranked finding

### MINOR-1 — The abstract omits the active-time range in its iterate sentence

The abstract says that after `t` updates the first component has absorbed
`C_2,...,C_(t+1)` without restricting `t`.  Literally, that indexing is only
defined during the transient range

```text
0 <= t <= k-1.
```

For `t >= k-1`, all original components have already been absorbed and the
endpoint is fixed.  The mathematically uniform statement is obtained either by
adding the displayed range or by replacing `t` with `min(t,k-1)` in the
closed-orbit indexing.

This is not a theorem defect.  Lemma 3.1 states the correct range, Corollary
3.2 proves that the time-`k-1` endpoint is fixed, and together those statements
determine every iterate for every `t >= 0`.  The introduction's phrase “a
closed formula for every iterate” and the ownership section's “all-time
iterate” are therefore substantively supported; only the abstract's standalone
wording is missing the cap.

**Suggested nonblocking correction:** write “for `0 <= t <= k-1`, after `t`
updates...” and add that the endpoint is fixed thereafter.  No formula,
proof, bibliography, or verifier change is required.

## Round-1 closure audit

### Review-A MAJOR-1 — direct rotation neighbourhood and tree carrier: CLOSED

The requested repair was not handled by citation padding alone.  The current
package now contains all of the following:

1. verified primary records for Pallo (2006), Pallo (2003), Chapoton (2020),
   and Stanley's Catalan carrier;
2. a literal comparison among `Phi_n`, Pallo's deterministic leftmost
   left-rotation, and the comb/height-zero Tamari cover family;
3. an invariant that separates the Pallo and P144 functional graphs for
   `n >= 3`;
4. the explicit ordered-plane-tree root-child graft and its suffix-lift
   inverse;
5. a bounded, query-level source-search log that says expressly that a non-hit
   is not priority or novelty evidence;
6. synchronized subtraction language in the manuscript, claims ledger,
   narrative, plan, README, source ledger, and build record.

The retained residual is correspondingly narrow: it is only the conjunction,
for this literal selector, of the complete temporal law and the target/depth
unique-source assertion.  The map, scheduler idea, comb cover, tree carrier,
clock statistic, component census, and coefficient extraction are not claimed
separately.

### Review-A MINOR-1 — planned versus delivered length: CLOSED

`PAPER_PLAN.md` now targets 5--6 pages including references.  The current
artifact has 6 A4 pages.  `README.md`, `BUILD.md`, `IMPROVEMENT_LOG.md`, and
the actual PDF agree.

## Primary-source and ownership audit

### Pallo (2006): direct deterministic precedent — PASS

The official University of Szeged repository record and PDF are:

- <https://acta.bibl.u-szeged.hu/12796/>
- <https://acta.bibl.u-szeged.hu/12796/1/Pallo_2006_ActaCybernetica.pdf>

The article's pp. 802--803 support the roles assigned in the manuscript:

- p. 802 defines a unique leftmost eligible left-rotation away from the
  terminal tree;
- p. 802 defines the resulting directed leftmost-rotation graph and its unique
  path distance;
- p. 803 identifies a greatest element, a rooted tree structure, and a grading.

After adjoining a self-loop at the otherwise terminal greatest element,
Pallo's deterministic successor has one fixed state.  P144 has
`Cat_(n-1)` fixed paths, so for `n >= 3` fixed-point count alone excludes
equality and any functional-graph conjugacy, including one induced by mirror
or reversal.  The small cases `n=1,2` do not supply that separating invariant;
the source ledger and narrative correctly state the separation with the
`n>=3` qualifier.  The manuscript uses Pallo as a scheduler precedent, not as
an owner of the literal `Phi_n` rule or the target-fibre theorem.  This is
honest.

### Pallo (2003) and Chapoton (2020): comb/height-zero covers — PASS

The official Elsevier record for Pallo (2003) is
<https://www.sciencedirect.com/science/article/abs/pii/S0020019003002837>.
Its metadata, DOI, pages, and abstract support the right-arm-restricted
rotation role.  The source ledger is transparent that the round-1 check used
the official metadata/abstract and relied on Chapoton for the explicit comb
order attribution; it does not pretend that the full paywalled article was
used to verify the P144 dynamics.

Chapoton's official journal record and open primary PDF are:

- <https://alco.centre-mersenne.org/articles/10.5802/alco.98/>
- <https://alco.centre-mersenne.org/item/10.5802/alco.98.pdf>

Section 1.2, printed p. 438, identifies the comb order (also called the
left-arm rotation order under its convention), cites Pallo (2003), and states
that its covers are exactly the Tamari covers whose slid Dyck subpath is at
height zero.

The P144 edge has exactly this form.  At a nonfixed path

```text
P = U A D C_2 C_3 ... C_k,
```

the operation exchanges the ground-return `D` with the following primitive
subpath `C_2`:

```text
U A D C_2 ...  ->  U A C_2 D ... .
```

Thus the slid subpath begins at height zero, and choosing the first primitive
boundary is precisely choosing the leftmost available ground-level cover.
Chapoton supplies the cover-family equivalence; P144 supplies the repeated
selector and its inverse dynamics.  The current credit split says exactly
that and no more.

### Stanley and the ordered-plane-tree subtraction — PASS

The official Cambridge excerpt is
<https://assets.cambridge.org/97811070/75092/excerpt/9781107075092_excerpt.pdf>.
Stanley's Theorem 1.5.1 lists the standard Catalan carriers including plane
trees, binary trees, ballot sequences, and Dyck paths.  The package does not
claim that Stanley states P144's graft/lift dynamics.  It uses Stanley for the
standard carrier and performs the following immediate translation itself.

Under the usual contour convention, a plane tree whose root children are
`T_1,...,T_k` has Dyck word

```text
C_1 C_2 ... C_k,
```

where each `C_i=U A_i D` is the excursion around `T_i`.  Replacing

```text
U A_1 D C_2
```

by

```text
U A_1 C_2 D
```

makes the root of `T_2` the child visited after all pre-existing children of
the root of `T_1`; it is therefore appended as the rightmost child of that
root.  Root degree falls by one.  Reversing `d` updates lifts the last `d`
children of the terminal root's unique child, preserving order, to root
level.  This confirms both the direction (“rightmost”) and the suffix
orientation (“last `d`”).

The manuscript then assigns this entire carrier, graft/lift rewriting, and
root-degree clock zero standalone credit.  This is conservative and honest.
The bounded grafting/FCNS search is not used to infer novelty, and the package
continues to say that no owner of the residual conjunction has been
established.

## Definition-level mathematical attack

### 1. Domain, well-definedness, and `n=0/1` — PASS

The stated domain is `n >= 1`, and the abstract begins with a nonempty Dyck
path.  This exclusion is necessary: at `n=0` the empty Dyck path has no first
primitive factor `C_1=UAD`, so the literal rule as written is not defined.
No displayed theorem, fixed-count formula, or generating function silently
includes `n=0`; the bivariate series begins at `n>=1`.

At `n=1`, the only path is `UD`.  It has one primitive factor, is fixed and
recurrent, has depth zero, and is counted by `Cat_0=1`.  For the only target
`T=UD`, the interior is empty, so `r=0`, `P_0=UD`,
`B_T(u)=1`, and the maximum fibre size is `1=n`.  The deepest-state statement
also degenerates correctly: `(UD)^1` is the unique depth-zero path.

### 2. Literal move and complete orbit — PASS

Write `C_1=UAD`.  Since both `A` and `C_2` are Dyck words, `AC_2` is Dyck and
`UAC_2D` is primitive.  Hence the image remains in `D_n` and its primitive
factorisation is the merged first word followed by `C_3,...,C_k`.

Inductively, for `0<=t<=k-1`,

```text
Phi^t(P) = U A C_2 ... C_(t+1) D C_(t+2) ... C_k.
```

At time `t`, the displayed first word is primitive and the untouched suffix
contains exactly `k-t-1` primitive factors.  The induction therefore uses the
literal selector at every step and does not assume the desired factor clock.
At `t=k-1` the suffix is empty and the result is primitive, hence fixed.  For
all larger times the same endpoint repeats.  This is a complete all-time
orbit law despite MINOR-1's missing range in the abstract summary.

### 3. Clock, recurrence, and unique deepest path — PASS

Every nonfixed step changes the factor count from `k` to `k-1`; it cannot
produce a nontrivial cycle.  Fixed and recurrent states are exactly the
primitive paths, and deleting their outer `U,D` gives a bijection with
`D_(n-1)`.  Thus the fixed count is `Cat_(n-1)`.

The first fixed time is exactly `k-1`, not merely at most `k-1`, because the
state has at least two primitive factors at every earlier time.  Since every
factor has positive semilength, `k<=n`.  Equality requires every factor to
have semilength one, and `UD` is the only such primitive factor.  Hence the
unique maximum-depth state is `(UD)^n`, with depth `n-1`.

### 4. Temporal layer formula — PASS

One primitive component has semilength series `R(z)=zC(z)`.  Exactly `k`
components therefore contribute

```text
[z^n] R(z)^k = [z^(n-k)] C(z)^k.
```

For `m=n-k>=1`, Lagrange inversion from `W=z(1+W)^2`, `C=1+W`, gives

```text
[z^m] C(z)^k
  = (k/m) binom(2m+k-1,m-1)
  = k/(2m+k) binom(2m+k,m).
```

Substitution yields

```text
k/(2n-k) binom(2n-k,n).
```

The only point at which the displayed Lagrange expression would divide by
zero is `m=0`, equivalently `n=k`; the manuscript handles it separately and
gets one, as does the closed formula.  No denominator, symmetry, or
off-by-one error was found.

### 5. Target/depth unique source — PASS

Fix `T=UQD`, with the unique primitive factorisation
`Q=Q_1...Q_r`.  For `0<=d<=r`, the proposed source

```text
P_d = (U Q_1 ... Q_(r-d) D) Q_(r-d+1) ... Q_r
```

has one primitive first factor and `d` primitive suffix factors.  Its depth is
therefore `d`, and the endpoint formula absorbs exactly that suffix to recover
`T`.

For uniqueness, let a source at depth `d` have factorisation

```text
P = B_1 ... B_(d+1),    B_1=UAD.
```

Endpoint equality gives

```text
Q = A B_2 ... B_(d+1).
```

The factorisation of the Dyck word `A` ends at returns of `Q`, while every
`B_i` for `i>=2` is one primitive factor.  Uniqueness of primitive
factorisation therefore forces `B_2,...,B_(d+1)` to be the last `d` factors of
`Q` and `A` to be the preceding prefix.  It also forces `d<=r`.  Thus there is
exactly one source at each depth `0,...,r` and none elsewhere.

The edge cases are correct:

- `r=0`: only `T=UD` and depth zero occur;
- `d=0`: `P_0=T`;
- `d=r`: `P_r=(UD)Q_1...Q_r`;
- `n=1`: all three conditions coincide in the unique state `UD`.

The fibre polynomial is consequently `1+u+...+u^r`.  Since `Q` has
semilength `n-1`, one has `r<=n-1`; equality forces every factor of `Q` to be
`UD`.  This proves both size `n` and uniqueness of the maximum target
`U(UD)^(n-1)D`.

## Canonical verifier audit

The paper-local verifier was read before replay.  Its main independence
features are real:

- `phi` is implemented by moving the down-step at the first return across the
  word ending at the second return;
- `predicted_iterate` is constructed separately from the initial primitive
  factor list;
- basins and depths are obtained by forward iteration of the functional graph;
- the target/depth formula is then compared with those accumulated basin
  counters;
- layer counts use exact integer binomial arithmetic;
- no sampling, floating point, randomized hashing, or external package is
  used.

I reran the canonical command from the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 \
  papers/144-leftmost-dyck-reassociation/verify_p144.py \
  > /tmp/p144-review-b-verifier.txt
cmp /tmp/p144-review-b-verifier.txt \
  papers/144-leftmost-dyck-reassociation/verification_output.txt
```

`cmp` returned zero.  The replay ends with:

```text
TOTAL_STATES=290511
TOTAL_FIXED_TARGETS=82500
TOTAL_ASSERTIONS=6005502
STATUS=PASS
```

This is exhaustive finite counterexample pressure for `n=1..12`.  It is not
used as a replacement for the all-parameter proofs or as owner evidence.

## Isolated TeX/BibTeX build and bibliography audit

I created a new temporary directory, copied only `main.tex` and
`references.bib`, and ran:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

A further settled `pdflatex` pass reproduced the previous temporary PDF byte
for byte.  The isolated PDF is also byte-identical to both checked-in
`main.pdf` and `main_round1.pdf`, with SHA-256

```text
24a483f852b5c2fd29e5acf8ccc19aafe218928d7b5efb247a640444e1ef050c
```

The settled logs contain zero undefined citations, undefined references,
multiply defined labels, overfull boxes, underfull boxes, LaTeX warnings, or
BibTeX warnings.  There are seven bibliography records and seven distinct
citation keys in the manuscript; all resolve and all are printed.

The current PDF has 6 A4 pages, 328,154 bytes, blank title/author metadata, no
encryption, form, or JavaScript, and all 22 font rows are embedded and
subsetted.

## PDF provenance and page-by-page visual audit

### Provenance chain — PASS

- `HOSTILE_REVIEW_A.md` recorded the pre-repair `main.pdf` and
  `main_round0_original.pdf` as byte-identical at hash
  `f30d0145385d226ac66b75c280db956672f714d27e1e3c65169e37273c8baf26`.
- The current `main_round0_original.pdf` still has exactly that hash and is a
  distinct 5-page artifact.
- `IMPROVEMENT_LOG.md` and `BUILD.md` record the post-repair hash
  `24a483...e050c` for `main.pdf` and `main_round1.pdf`.
- Fresh comparison confirms that `main.pdf` and `main_round1.pdf` are
  byte-identical, while `main_round0_original.pdf` is different.
- Fresh isolated compilation from the current source produces the post-repair
  hash exactly.

Thus the package supports the claimed chain: a preserved round-0 PDF, a
distinct source/citation remediation, and a frozen round-1 PDF identical to
the current reproducible manuscript.  Suppressed volatile PDF metadata makes
the hashes stable; the package does not misuse the hashes as an external
timestamp or priority certificate.

### Round-0 pages — PASS

1. Title, abstract, initial four-source introduction, and the beginning of the
   literal definition are legible and within the page box.
2. The map, theorem, and first part of the clock proof are intact; displayed
   equations and proof boxes do not collide.
3. The clock conclusion and complete layer calculation are legible; there is
   no clipping at the page break.
4. The target-fibre proof and control table are fully visible and aligned.
5. The old ownership boundary and four references are readable; hyperlinks
   wrap within the text block.

### Round-1/current pages — PASS

1. The expanded abstract and Pallo/Chapoton comparison fit cleanly; the
   subject-classification footnote remains readable.
2. The ordered-tree graft display, definitions, and full theorem are legible;
   no equation number or theorem line is clipped.
3. The clock proof and first part of the Lagrange calculation have clean page
   breaks and proof boxes.
4. The layer conclusion, target-fibre theorem, boundary cases, and suffix-lift
   paragraph are intact.
5. The control table, ownership subtraction, and first reference fit without
   collision or margin overflow.
6. All remaining references and DOI/URL lines are readable and stay inside
   the page box.

No blank required-content page, malformed glyph, rasterization defect,
clipping, collision, illegible formula, broken table, or visibly unresolved
reference was found in either frozen PDF.

## Residual claim and release boundary

After the verified source subtraction, the remaining statement is genuinely
thin: for one literal ground-level selector, the paper combines its complete
transient orbit with a target-indexed inverse statement that has one specified
source at each feasible depth.  The fibre polynomial and maximum target are
only consequences.  The paper does not claim that the conjunction is absent
from all literature, and the bounded search cannot justify such a claim.

Accordingly:

- the mathematical and round-2 artifact gate is **ACCEPT**;
- the single abstract-range wording issue is **Minor** and nonblocking;
- the package remains **OWNER-THIN**;
- external release remains **HOLD_EXTERNAL**.
