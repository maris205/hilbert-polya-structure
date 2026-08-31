# P133 hostile review — Round B

**Manuscript:** *Source Phases and Target Fibres for Totient--Complement
Dynamics on Squarefree Divisors*  
**Review date:** 2026-09-01 UTC  
**Reviewer role:** second independent reviewer; no participation in the draft
or in Round-A review  
**Calibration:** `NOT_CALIBRATED`; `criteria_binding_unavailable`, so this
report makes no venue-fit claim  
**External status:** `HOLD_EXTERNAL`  
**Verdict:** **`GO_INTERNAL`** — the Round-A repair is closed and the complete
mathematical, executable, source/PDF, and presentation gates pass.

Severity summary: **CRITICAL 0; MAJOR 0; MINOR 0**.

## 1. Frozen Round-B snapshot

I reviewed the repaired package without modifying `main.tex`, bibliography,
code, canonical output, or any PDF.  The reviewed hashes are:

| artifact | SHA-256 |
|---|---|
| `main.tex` | `3f62efbd5a23a5a0a811e92f4f975ba643cd4262b958c6c6ab0804920f602835` |
| `references.bib` | `3311a309139704fb8712bb152895ce5dec7e0ddbe087d44e4a20504976b83e2d` |
| `code/verify.py` | `841ed6f77091e0d0e6721c24dc334891f8bc3b54701717153da49ecbb391262a` |
| `code/verification_output.txt` | `1c90aea14a3c45d084ec9cd6d86e951d3508494d94fa04afa6bd6ec12692b99d` |
| `main.pdf` | `bbb869d485230bc0165bbe49ff43929de61700c1e0acc960a541b64b23651d7b` |
| `main_round0_original.pdf` | `bbb869d485230bc0165bbe49ff43929de61700c1e0acc960a541b64b23651d7b` |
| `main_round1.pdf` | `bbb869d485230bc0165bbe49ff43929de61700c1e0acc960a541b64b23651d7b` |

The three PDF hashes are identical and fresh pairwise `cmp` checks returned
zero.  This is the required support-only Round-1 history: no theorem source,
code, or rendered-paper drift is hidden behind the ledger repair.

Fresh raw execution of `code/verify.py` matched the canonical stdout byte for
byte (`cmp=0`).  It again covered 226 states, every one of the 226 targets,
and 4,774 exact assertions, with integer/tuple arithmetic and no sampling.

A fresh isolated four-stage build from only `main.tex` and
`references.bib` produced a PDF byte-identical to `main.pdf`.  The artifact
has three A4 pages and 346,509 bytes.  The settled build has no undefined
reference/citation, bad box, or actionable warning.  All 28 font rows are
embedded, subsetted, and Unicode-mapped.  The PDF is unencrypted, its
Title/Subject/Keywords/Author metadata fields are blank, and the visible
byline is `Anonymous`.

I rasterized and inspected all three pages, not merely the first page.  No
clipping, overlap, malformed glyph, orphaned table material, bad link box, or
bibliography defect is visible.  Text extraction is searchable and contains
no leaked tool/debug tokens.

## 2. Closure of `P133-A-m1`

Round A found one stale proof-object ledger.  Both repaired ledgers now point
to objects that actually exist in the unchanged manuscript:

| claim | repaired locator | Round-B check |
|---|---|---|
| C1 support conjugacy | Proposition 2.1 | exact |
| C2 complete source-phase decoder | equations (6)--(7), Lemma 3.1, completeness paragraph after Proposition 3.3 | exact |
| C3 recurrent census | Lemma 3.1 and census paragraph after Proposition 3.3 | exact |
| C4 entry bound | Lemma 3.2 and Proposition 3.3 | exact |
| C5 every-target fibre | Theorem 1.1(iv) and Section 4 derivation | exact |

`CLAIMS_EVIDENCE.md` and `PAPER_PLAN.md` agree with one another and with the
source.  No nonexistent theorem, lemma, proposition, or corollary remains in
these locators.  The improvement log accurately describes the change as
support-only.  **`P133-A-m1` is closed.**

## 3. Independent hostile reconstruction

### 3.1 Arithmetic support and actual coordinate law

For squarefree `n`, a prime `p` enters the literal output from `n/d` exactly
when `p` is absent from the source support.  If it is present, the only
remaining route is `p | (q-1)` for some present `q`; `q=p` cannot contribute.
Thus the actual divisor map is statewise, not just statistically, conjugate
to

```text
F(S) = (P \ S) union N(S).
```

With `x_p=1[p in S]` and `y_p=1-x_p`, its exact coordinate law is
`y_p(t+1)=(1-y_p(t)) A_p(t)`, where `A_p` is the product of parent `y` bits.
The edge strictly lowers primes, so the topological induction is legitimate
on every finite induced graph, including disconnected graphs.

### 3.2 Source phases, uniqueness, and census

Every source toggles.  For a nonsource, one parent already guarantees
`A_p^0 A_p^1=0`, because each parent phase pair has product zero.  The three
possible pairs `(A_p^0,A_p^1)=(0,0),(1,0),(0,1)` uniquely solve the two phase
equations as `(y_p^0,y_p^1)=(A_p^1,A_p^0)`.  Processing vertices in
topological order therefore gives one and only one extension of arbitrary
source bits.

The decoder keeps its source assignment, so it is injective.  Every nonempty
finite DAG has a source and that source toggles, excluding fixed points.  The
later entry argument proves completeness, leaving exactly `2^s` recurrent
states and `2^(s-1)` exact two-cycles.  The singleton case has `s=1` and
obeys the same count.

### 3.3 Two-step erasure and the `h+1` interface

Consecutive values satisfy `y_p(t)y_p(t+1)=0`.  At a nonsource this makes
`A_p(t)A_p(t+1)=0`, and direct substitution gives the exact erasure identity
`y_p(t+2)=A_p(t+1)`.  Assuming all parents are two-periodic from their stated
levels, the products at `t+1` and `t-1` coincide once
`t>=delta(p)+1`; hence the child is two-periodic from that time.  At time
`h+1` every coordinate satisfies the same two-step relation simultaneously,
so the whole state is already recurrent, not merely approaching a periodic
word coordinatewise.

There is no source-phase indexing gap at this boundary: take the actual
source coordinates at time `h+1` as phase zero.  Topological uniqueness then
forces the entire state and its successor to equal the two decoder phases.
For `h=0` the actual tail is zero, safely below the claimed upper bound one;
using the maximum component height also handles disconnected graphs.

### 3.4 Every-target fibre

An output zero at `p` is exactly the event that source bit `p` is one while
all its parents are zero.  Requiring events for a set `U` forces `U` to one
and `Par(U)` to zero.  The intersection is empty precisely when these two
sets overlap; otherwise exactly `|P|-|U|-|Par(U)|` bits remain free.
Inclusion--exclusion over target-one positions gives the displayed formula
with `U=Z union T`.  The derivation makes no image assumption, so a target
outside the image correctly receives zero rather than falling outside the
theorem's domain.

I also tried the strongest small boundary attacks suggested by the formulas:
a singleton source, a chain whose entry times differ by level, multiple
sources feeding one child, and disconnected components of unequal height.
None breaks the decoder, simultaneous `h+1` entry, or fibre count; all are
within the paper-local exact controls.

## 4. Code-to-paper consistency

The verifier implements the literal integer update separately from the
support law, tests both decoder phases, recurrent census, and the entry
bound, and compares the inclusion--exclusion formula with literal fibres for
every target in every advertised box.  Its reported totals agree across
`main.tex`, `CONTROL_RESULTS.md`, the canonical transcript, and the fresh
run.  Enumeration is consistently labelled as falsification rather than as
proof of an all-parameter statement.

## 5. Citations, ownership, and contribution boundary

The bibliography records and their uses are consistent: Ford--Konyagin--Luca
is cited only for prime-chain/Pratt geometry; Veliz-Cuba et al. and
Aracena--Cabrera-Crot--Salinas are cited for AND--NOT/signed Boolean-network
background.  Each entry is cited, and no citation is made to carry the new
decoder, entry, or fibre theorem.

I cross-checked the title/author/year/venue-or-arXiv identifiers against the
primary records for
[Ford--Konyagin--Luca](https://doi.org/10.1007/s00039-010-0089-0),
[Veliz-Cuba et al.](https://arxiv.org/abs/1211.5633), and
[Aracena--Cabrera-Crot--Salinas](https://doi.org/10.1093/bioinformatics/btaa922).
The bibliography data and the manuscript's limited attribution roles agree
with those records.

The manuscript explicitly removes contribution credit for Euler
factorization, prime-chain height, signed-Boolean formalism, generic DAG
propagation, inclusion--exclusion, and finite-map cycle conversion.  The
residual claim is limited to their conjunction for the literal displayed
totient--complement map.  The bounded owner non-hit is correctly kept from
becoming novelty or priority evidence.

## 6. Findings and verdict

### Critical

None.

### Major

None.

### Minor

None.  In particular, the only Round-A minor is fully closed.

**Round-B verdict: `GO_INTERNAL / HOLD_EXTERNAL`.**  The package is coherent,
reproducible, anonymous, and internally ready.  This verdict does not lift
the explicit external-release hold and makes no unbounded novelty claim.
