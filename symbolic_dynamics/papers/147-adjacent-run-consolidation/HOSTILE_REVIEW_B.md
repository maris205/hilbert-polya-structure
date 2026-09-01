# Independent hostile review B — P147

**Manuscript:** *Adjacent-Run Consolidation of Integer Compositions: A Sharp
Logarithmic Clock and Divisor-Path Fibres*  
**Reviewer role:** independent; this reviewer authored neither the manuscript
nor hostile review A.  
**External status:** `HOLD_EXTERNAL`.  
**Verdict:** **ACCEPT** — 0 Critical, 0 Major, 0 Minor findings.

The repaired package closes all four findings in hostile review A.  I
rederived the theorem independently after the repairs, cold-replayed the
falsifier, rebuilt the paper in isolation, and inspected every current PDF
page.  I found no surviving theorem, source-boundary, transcript, or artifact
defect.

## 1. Closure of review-A findings

| finding | status | review-B check |
|---|---|---|
| **A1 — doubling-ancestry selector** | **CLOSED** | The proof now defines `alpha^(j)=A_n^j(alpha)` for every `0<=j<=t`, handles `t=0`, proves the one-step ancestry claim, and recursively selects nontrivially produced parts `w_1,...,w_t`.  The equal-input run producing `w_j` gives `w_j>=2w_(j-1)`, while `w_1>=2` and `w_t<=n`; hence `2^t<=n`.  No index or existence step remains implicit. |
| **A2 — target typing** | **CLOSED** | Both the definition of `Phi_beta` and Theorem 1(3) now require `beta in Comp(n)`.  The summation explicitly uses positive divisors `s_i in Z_(>0)`, and the claims/control ledgers state that comparison is within the same exact-total layer. |
| **A3 — every-size witness orbit** | **CLOSED** | The appended-remainder branch now displays every state for `0<=j<t`; the half-remainder branch displays the states through the terminal triple `(r,r,r)`.  The bases `n=1`, `n=2`, and the exceptional half-remainder case `n=3` are explicit. |
| **A4 — owner ledger** | **CLOSED** | The Knopfmacher--Prodinger copy is correctly described as UCSD-hosted and DOI `10.1006/eujc.1998.0216` is present.  Bevan--Threlfall (2025) and Hopkins--Tangboonduangjit (2026) are screened, cited, and subtracted as different random-growth and static-restriction objects.  The paper retains the bounded-non-hit disclaimer and assigns no credit to the literal rule alone. |

## 2. Fresh theorem-interface attack

### Self-map, fixed set, and termination

Each output part is the product of the value and length of one maximal equal
run, so the total remains `n`.  A state is unchanged exactly when every run
has length one, equivalently when adjacent parts differ.  Every nonfixed
update strictly decreases the number of parts, which proves termination and
rules out every nontrivial cycle.  The one-part and `n=1` boundaries are
consistent.

### Pointwise upper clock

The repaired ancestry argument is valid.  Two equal adjacent parts in
`alpha^(j)` are outputs of two consecutive maximal runs in `alpha^(j-1)`.
Those preceding runs cannot both be singleton runs, because their equal
unchanged values would make them one maximal run.  Hence one equal input was
created by a nontrivial collapse.  Following such an input backward at every
generation yields a chain whose weight at least doubles at each update.  If
an orbit has depth `t`, one final part therefore has weight at least `2^t`
and at most the total `n`, proving
`t<=floor(log_2 n)` pointwise.

### Sharp witness for every total

For `C_t=(1,1,2,...,2^(t-1))`, after `j<t` updates the active prefix is
`(2^j,2^j)` followed by the remaining larger powers, so its depth is exactly
`t`.  If the remainder `r=n-2^t` is appended and is not `2^(t-1)`, the fixed
right boundary cannot merge with the cascade.  If `r=2^(t-1)`, prepending it
creates exactly the final triple `(r,r,r)` after `t-1` updates and the last
collapse after update `t`.  The separately stated `n=1,2,3` cases remove all
empty-range ambiguity.  As an additional independent check, I implemented
the map with a separate group-by routine and replayed the declared witness
for every `1<=n<=100000`; all weights and exact depths matched.

### Complete length-refined fibre

If a source run maps to target part `b_i`, its base `s_i` is a positive
divisor of `b_i` and its length is `b_i/s_i`.  Consecutive source runs are
maximal exactly when adjacent bases differ.  Conversely, expanding every
admissible divisor choice into `b_i/s_i` copies of `s_i` reconstructs a
unique source, and the adjacent inequality makes the expanded blocks exactly
its maximal runs.  These constructions are inverse and preserve the stated
source-length exponent.  I separately checked the boundary fibres
`Phi_(2)=u+u^2`, `Phi_(1,1)=0`, `Phi_(2,2)=2u^3`, plus mixed repeated and
nonrepeated targets; all agree with literal consolidation.

### Classical fixed-class formula and credit boundary

With the empty composition included, the equations
`C_j=x^j(C-C_j)` imply the displayed Carlitz generating function.  The note
correctly labels this static census as zero credit.  Primary records confirm
that the two newly added neighbours concern, respectively, random weak-
composition evolution and static Arndt--Carlitz restrictions.  A renewed
formula/terminology search did not locate the exact iterative
clock-plus-target-inverse conjunction.  This remains only a bounded non-hit,
not novelty, priority, or freedom-to-operate evidence.

## 3. Verifier and transcript audit

The cold command

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p147.py | cmp - verification_output.txt
```

returned success with a byte-identical transcript.  The run reports all
262,143 positive compositions of totals `1..18`, every target in each exact-
total layer, 50,190 nonempty image targets, maximum one-step fibre 59, and
2,690,869 assertions.  Literal orbit evaluation is separate from the
Carlitz dynamic program and divisor-path dynamic program.  The checks include
strict descent, weight preservation, cycle exclusion, the fixed criterion,
every pointwise clock bound, exact maximum and witness depth, and the full
source-length fibre counter for every target, including empty fibres.  The
code is deterministic, integer-only, standard-library-only, and performs no
runtime network access.  Its finite range is correctly described as
falsification pressure rather than proof.

## 4. Build, PDF, and visual audit

An isolated

```text
pdflatex -> bibtex -> pdflatex -> pdflatex
```

build under the documented deterministic environment reproduced the current
PDF byte for byte.  The repaired `main.pdf` and `main_round1.pdf` are both
four A4 pages, 338,052 bytes, with SHA-256
`1d9c5ceb72891e1c509ebeb8adfdb23d110958f129ea7ae32d3c9d427253ce20`.
The historical round-0 artifact remains distinct and unchanged at SHA-256
`c21bc9029f7dd697a623f489d446fcfa9329bd96f1bb6ea34e9c363a545a6aa3`.
The settled log has no unresolved citation/reference, rerun request, bad box,
or multiply defined label, and all reported fonts are embedded.

All four current pages were rasterized and inspected.  The repaired ancestry
proof and witness displays are legible; equations, theorem numbering, links,
declarations, and bibliography remain within the page bounds; no clipping,
collision, blank page, corrupt glyph, unresolved marker, or identifying PDF
metadata was found.  Source and extracted PDF text agree, independently of
the stronger byte-identical build check.

`BUILD.md` intentionally leaves creation of `main_round2.pdf` and the final
post-review hash record to the subsequent author/final-QA gate.  That
historical-copy step is not a manuscript defect and was outside this
reviewer's write authority.

## 5. Decision

P147 passes review B on its frozen residual: the simultaneous
weight-preserving consolidation map, the sharp all-size logarithmic clock,
and the complete target-resolved length-refined divisor-path inverse.  All
Carlitz enumeration, run statistics, random composition evolution, and
static adjacent-restriction results remain expressly subtracted.

The verdict is **ACCEPT**, but external status remains **`HOLD_EXTERNAL`**.
This review authorizes no posting, contact, submission, Git action, or
release.
