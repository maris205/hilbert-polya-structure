# Hostile Review A — P144, *Leftmost Reassociation of Dyck Components*

**Review date:** 2026-09-01 UTC
**Round:** independent hostile round 1
**Scope:** mathematical correctness, ownership boundary, exact-control
reproducibility, TeX/PDF/bibliography integrity
**Verdict:** **REVISE**
**External status:** retain **HOLD_EXTERNAL**

## Severity summary

| Severity | Count | Disposition |
|---|---:|---|
| Critical | 0 | No false theorem or failed artifact was found. |
| Major | 1 | The ownership gate omits the closest leftmost-rotation literature and the simpler plane-tree carrier on which the residual mechanism becomes root grafting. |
| Minor | 1 | The frozen paper plan targets 7--9 pages, while the delivered manuscript and build record contain 5 pages. |

The formal theorem package survived the hostile mathematical audit.  The
revision verdict is therefore not a response to a counterexample.  It is an
ownership-blocking verdict: the paper's claimed residual is precisely the part
for which the current four-source search is least adequate.

## Major finding

### MAJOR-1 — The residual ownership search misses the direct
leftmost-rotation neighbourhood and an ownership-compressing tree model

The manuscript assigns the Tamari cover, primitive decomposition, Catalan
enumeration, and component census zero credit, then retains as its residual
the deterministic repeated-leftmost scheduler together with its clock and
targetwise fibres.  `SOURCE_VERIFICATION.md`, however, checks only four broad
background sources.  It does not inspect either of the following primary
sources, even though they lie directly on the retained boundary:

- Jean Marcel Pallo, “Rotational tree structures on binary trees and
  triangulations,” *Acta Cybernetica* 17(4) (2006), 799--810.  The
  [official journal-repository record](https://acta.bibl.u-szeged.hu/12796/)
  and [official PDF](https://acta.bibl.u-szeged.hu/12796/1/Pallo_2006_ActaCybernetica.pdf)
  define a uniquely selected leftmost left-rotation, its directed tree, a
  grading, and rotation distance; see especially article pp. 802--803.
- Frédéric Chapoton, “Some properties of a new partial order on Dyck paths,”
  *Algebraic Combinatorics* 3(2) (2020), 433--463,
  [DOI 10.5802/alco.98](https://alco.centre-mersenne.org/articles/10.5802/alco.98/).
  Section 1.2, especially p. 438, identifies comb/left-arm rotations with
  precisely the Tamari covers whose moved Dyck subpath is at height zero.

These sources do **not** by themselves prove that Pallo's functional graph is
identical to the present one.  Indeed, a first separating invariant is already
visible: Pallo's graph is described with a unique greatest root, whereas
`Phi_n` has `Cat_(n-1)` fixed targets.  That distinction prevents an
unsupported declaration of literal ownership, but it makes an explicit
bijection-level comparison mandatory.  A source called “leftmost rotation”
that already gives a unique scheduler, a tree structure, a rank, and a distance
cannot be absent from an owner check whose proposed residual is a deterministic
leftmost rotation, clock, and basin tree.

There is a second, representation-level compression that the manuscript does
not expose.  Under the standard contour bijection from Dyck paths to ordered
rooted plane trees, the primitive factors are the excursions through the
root's ordered children.  If those children are `T_1,T_2,...,T_k`, then the
literal update is simply

```text
(T_1,T_2,T_3,...,T_k)
    -> (T_1 with T_2 appended as its rightmost child, T_3,...,T_k).
```

Thus the clock is root degree minus one.  For a fixed target, the inverse
depth-`d` source is obtained by lifting the last `d` children of its unique
root child to become root-level siblings.  This is exactly the suffix-cut
fibre formula in tree language.  The observation is mathematically benign,
but ownership-severe: it shows that the entire orbit and fibre package is a
canonical ordered-tree graft/lift operation, whereas the current owner search
is confined to Dyck-factor and generic Tamari terminology.

#### Why this is major

After the manuscript's own zero-credit deductions, almost no residual remains
outside the scheduler and its suffix-cut inverse atlas.  The omitted sources
and omitted tree carrier target that residual rather than peripheral context.
`HOLD_EXTERNAL` and the absence of a novelty claim are appropriate safeguards,
but they do not make the ownership ledger complete enough for acceptance of
the frozen framing.

#### Exact required fixes

1. Add Pallo (2006) and Chapoton (2020) to the verified-source ledger and
   bibliography using the primary records above.  Record the inspected
   sections/pages and assign only the roles that the texts actually support.
2. Give an explicit local comparison between `Phi_n`, Pallo's uniquely
   selected leftmost rotation, and the ground-level comb/Tamari covers.  State
   whether the rules are equal, mirror/reversal conjugate, restrictions of one
   another, or genuinely different.  Preserve a concrete separating invariant
   such as the fixed-root count if they are different.
3. Add the ordered-plane-tree conjugacy.  State explicitly that one update
   grafts the second root child onto the first as its rightmost child, and that
   terminal inverse fibres lift a suffix of children.  Re-audit the literature
   under the terms “ordered/plane forest grafting,” “rightmost-child graft,”
   “root rotation,” “comb order,” and “first-child/next-sibling encoding.”
4. Make the owner search reproducible: record databases or official
   repositories, exact queries, search date, bounds, inspected hits, and the
   non-hit limitation.  A bounded non-hit must remain explicitly non-novelty
   evidence.
5. Synchronize `SOURCE_VERIFICATION.md`, `CLAIMS_EVIDENCE.md`,
   `NARRATIVE_REPORT.md`, `PAPER_PLAN.md`, `README.md`, the ownership section of
   `main.tex`, and `references.bib`.  If the comparison assigns the scheduler,
   rank/clock, or tree structure to prior work, subtract that credit and
   reassess whether the targetwise depth-refined suffix-lift statement alone
   supports a paper.  Do not relax `HOLD_EXTERNAL` during this reassessment.

#### Acceptance test for MAJOR-1

The revision must let a reader recover, without guessing, a commutative or
separating comparison between the three literal moves (P144, Pallo, and the
height-zero comb cover), and it must show the plane-tree graft/lift model.  The
source ledger must then state exactly which pieces remain unowned after those
comparisons.  Merely adding two citations to a paragraph is insufficient.

## Mathematical attack report

No correction is required to the frozen formulas on the evidence inspected.
The following points were attacked independently of the verifier.

### 1. Well-definedness of the leftmost merge — PASS

The positive returns to height zero give a unique primitive factorisation
`P=C_1...C_k`.  Writing `C_1=UAD` is unique.  For `k>=2`, both `A` and `C_2`
are Dyck words, so `A C_2` is Dyck and `U A C_2 D` is primitive.  Its suffix
`C_3...C_k` is unchanged.  Hence the displayed image lies in `D_n`, and the
first-return selector is unambiguous.  The cases `k=1` and `n=1` are explicitly
covered.

### 2. Closed orbit, exact clock, and fixed/recurrent set — PASS

Induction gives, for `0<=t<=k-1`,

```text
Phi^t(P) = U A C_2 ... C_(t+1) D C_(t+2) ... C_k.
```

The first displayed block remains primitive because its interior is a
concatenation of Dyck words.  Therefore the primitive-factor count is exactly
`k-t`, not merely bounded by it.  Each nonfixed step drops the count by one,
`tau(P)=k-1`, and a nontrivial cycle is impossible.  Fixed and recurrent paths
are exactly the primitive paths.  Deleting their outer `U,D` gives the claimed
`Cat_(n-1)` count.

### 3. Ballot layer formula and boundary — PASS

One primitive factor has generating function `R(z)=z C(z)`, so exactly `k`
factors contribute

```text
[z^n] R(z)^k = [z^(n-k)] C(z)^k.
```

With `m=n-k`, Lagrange inversion yields

```text
[z^m] C(z)^k = k/(2m+k) * binom(2m+k,m)
```

for `m>=1`; substitution gives
`k/(2n-k) binom(2n-k,n)`.  The manuscript separately handles `m=0`
(`n=k`), where the coefficient and displayed formula are both one.  No
off-by-one or denominator failure was found.

### 4. Unique deepest state — PASS

Every primitive factor has positive semilength, so `k<=n`.  Equality requires
all `n` factors to have semilength one, and the only such primitive factor is
`UD`.  Thus depth is at most `n-1`, with equality only at `(UD)^n`.  This also
handles `n=1`, where the unique state has depth zero.

### 5. Fixed-target inverse fibre and uniqueness — PASS

For `T=UQD` with `Q=Q_1...Q_r`, the proposed depth-`d` word has one primitive
first factor and `d` primitive suffix factors, hence depth `d`; its endpoint is
`T`.  Conversely, if

```text
P=B_1...B_(d+1),  B_1=UAD,  E(P)=T,
```

then `Q=A B_2...B_(d+1)`.  Since `A` is a Dyck word and every later `B_i` is
primitive, uniqueness of primitive factorisation forces `A` to be the prefix
`Q_1...Q_(r-d)` and the later factors to be the final `d` factors of `Q`.
This proves both source uniqueness and the exclusion of depths outside
`0,...,r`.  The edge cases `r=0`, `d=0`, and `d=r` all agree with the formula.
Consequently the fibre polynomial and its unique size-`n` maximizer also
follow as stated.

## Reproducibility and artifact audit

### Exact verifier — PASS

The frozen command was rerun from the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 \
  papers/144-leftmost-dyck-reassociation/verify_p144.py \
  > /tmp/p144_review_replay.txt
cmp /tmp/p144_review_replay.txt \
  papers/144-leftmost-dyck-reassociation/verification_output.txt
```

`cmp` returned exit code 0.  The replay exhausts semilengths `1..12`,
290,511 states, and 82,500 fixed targets; it terminates with

```text
TOTAL_ASSERTIONS=6005502
STATUS=PASS
```

The literal `phi` implementation moves the closing step using the first two
return positions.  `predicted_iterate` instead rebuilds the claimed iterate
from the initial factor list.  Basin profiles are accumulated by exhaustive
forward iteration, and the observed `Counter` at every fixed target is then
compared with the independently constructed depth source.  This is adequate
finite counterexample pressure, with no random or floating-point component.

Hashes at review time were:

```text
verify_p144.py          4e8e0762bf45c110f47ae99bcd394b226c4e7680fb6c9278c6624a9994052560
verification_output.txt c9f7c02c4dcbe598ad4b0b8ed260256bd808987d7369cf8a300ef1f8ca046294
```

### TeX, bibliography, and PDF — PASS

A fresh isolated build from only `main.tex` and `references.bib`, using
`pdflatex`, `bibtex`, `pdflatex`, `pdflatex`, completed successfully.  The
settled logs contain no undefined reference/citation, multiply defined label,
box, LaTeX, or BibTeX warning.  All four bibliography entries are cited.

The rebuilt PDF is byte-identical to the checked-in `main.pdf`.  The PDF has
5 A4 pages, blank author/title metadata, no encryption, forms, or JavaScript,
and all 22 reported font rows are embedded.  Visual inspection of every page
found no clipping, collision, unreadable table, or malformed reference.
`main.pdf` and `main_round0_original.pdf` are also byte-identical, both with

```text
f30d0145385d226ac66b75c280db956672f714d27e1e3c65169e37273c8baf26
```

## Minor finding

### MINOR-1 — Planning artifact and delivered length disagree

`PAPER_PLAN.md` records a target of 7--9 pages including references, while
`README.md`, `BUILD.md`, `pdfinfo`, and the actual PDF all report 5 pages.  No
content is missing from the frozen theorem contract, so this is not a demand
for padding.  After the ownership revision, change the plan to the actual
short-note length (or explain the intentional variance) and keep all artifact
counts synchronized.

## Final verdict

**REVISE.**  The map is well defined; the exact clock, recurrent/fixed set,
ballot layers, unique deepest state, full targetwise inverse fibres, and sharp
fibre maximum are all proved correctly and survive exhaustive exact replay.
The build is clean and reproducible.  Acceptance is blocked only by the major
ownership gap: the current residual framing has not been tested against the
closest leftmost-rotation sources or against the standard ordered-plane-tree
graft/lift representation that compresses the mechanism.  Retain
**HOLD_EXTERNAL** until MAJOR-1 is resolved and independently rechecked.
