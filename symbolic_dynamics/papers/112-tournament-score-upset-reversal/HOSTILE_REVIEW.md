# P112 hostile-review resolution ledger

Status: **VALID REPAIRS APPLIED / EXTERNAL DISSEMINATION HOLD**.

Inputs read in full: `HOSTILE_REVIEW_A.md` and `HOSTILE_REVIEW_B.md`.  Those
two review records were not edited.  This file records resolutions only; it
is not an independent final QA, novelty clearance, or release decision.

## Critical and mathematical repairs

| Review issue | Resolution | Evidence in repaired manuscript |
|---|---|---|
| Review A C1 / Review B m1: the central iterate display visibly contained two `Phi_C^{,t-1}` superscripts | **RESOLVED.** Both commas were removed.  Because the repair also inserted the local-fixed and incidence equations, the former equation (5) is now equation (7). | The rendered display reads `Phi_{C_1}^{t-1}(T_1) oplus ... oplus Phi_{C_k}^{t-1}(T_k)` with no comma; PDF text and all-page visual inspection agree. |
| `Phi_C` was undefined although only `Phi_n` had been introduced | **RESOLVED.** The map is now defined functorially on every finite label set `V`; `Phi_n=Phi_[n]`; `T[C]` and `Phi_C` are defined explicitly, and all `Phi_C` scores are internal to `C`. | Definition 2.1 and the paragraph immediately following equation (7). |
| Simultaneous application was implicit | **RESOLVED.** The definition says that every right-hand-side score is read from the unchanged input and every edge decision is then applied simultaneously. | Definition 2.1. |
| Energy aggregation shared endpoints and needed an incidence derivation | **RESOLVED.** The signed incidence formula for `delta_v` is displayed before the square expansion; summing it gives the exact linear term without pretending that reversals happen sequentially. | Equations (2) and (4), theorem 2.2 proof. |
| The local fixed criterion was only implicit | **RESOLVED.** `Phi_V(T)=T iff R(T)=emptyset` is a displayed part of the Lyapunov theorem and is invoked in the fixed-point theorem. | Equation (3), theorem 4.1 proof. |
| Recursive tree was defined before well-foundedness | **RESOLVED.** Before defining the tree, the manuscript proves that one score class implies a fixed tournament; hence a nonfixed node has at least two nonempty proper score classes and all children have strictly smaller order.  Fixed nodes are explicitly leaves with no children. | Text before corollary 3.2. |
| Exact `tau` recursion lacked the stabilization “if and only if” | **RESOLVED.** Restriction to the fixed labelled blocks now proves that two consecutive global iterates agree iff every restricted factor agrees.  Persistence after equality and strong induction on child order give both directions of `tau(T)=1+max_i tau(T[C_i])`.  The fixed case is separated, so no maximum over an empty set occurs. | Corollary 3.2 proof, equations (8)--(10). |
| `[0]` depended on ellipsis notation | **RESOLVED.** `[n]={i in Z:0<=i<n}` is explicit, so `[0]=emptyset` literally.  Orders zero and one are handled separately and have depth zero. | Opening of section 2 and corollaries 3.2/4.3. |
| Update display had a redundant inequality | **RESOLVED.** For distinct `u,v`, the rule is now the single logical disjunction “higher old score, or tied old score and retained old arc.” | Equation (1). |
| `r_0` and `f_0` conventions were conflated | **RESOLVED.** `r_0=0` is identified as the nonempty-block convention, whereas `f_0=1` counts the empty ordered sum. | Text before corollary 4.2. |
| The universal depth bound risked being read as sharp | **RESOLVED.** Every occurrence presents `tau<=n-1` as a universal, non-sharp bound.  The manuscript expressly does not determine the sharp global maximum or a complete transient enumerator. | Abstract, introduction, corollary 3.2, controls, and limits. |

## Scan-qualified six-vertex signal

The edge order and bit convention remain adjacent to the example.  The
program and prose now say exactly: scan orders increasingly, and within each
order scan numerical masks increasingly; mask `148` is the least
nonidempotent state in that specified scan through order six.  No unrestricted
“first witness,” analytic minimality, or sharp-depth claim remains.

The verifier function/output label was correspondingly changed from
`first_nonidempotent` to `least_nonidempotent_in_specified_scan`; the exact
orbit remains `148 -> 4 -> 0 -> 0`.

## Owner subtraction and scope repairs

The bibliography and prose now include and distinguish the following
primary/direct neighbors.  Each item receives **zero contribution credit**.

| Owner/source | Verified record | Subtracted subject |
|---|---|---|
| Landau | *Bulletin of Mathematical Biophysics* 15 (1953), DOI `10.1007/BF02476378` | score-sequence theorem |
| Moon | *Topics on Tournaments* (1968) | tournament terminology, regular tournaments, ordinal-sum and Ryser-lineage background |
| Rubinstein | *SIAM Journal on Applied Mathematics* 38 (1980), 108--111, DOI `10.1137/0138009` | static ranking by tournament points |
| Henriet | *Social Choice and Welfare* 2 (1985), 49--63, DOI `10.1007/BF00433767` | static Copeland choice |
| Bouyssou | *Social Choice and Welfare* 23 (2004), 249--273, DOI `10.1007/s00355-003-0250-x` | ranking by successive choice on shrinking sets |
| Linares Lejarraga--Bodanza | *Constitutional Political Economy* (2025), DOI `10.1007/s10602-025-09500-4` | current “Iterative Copeland from below” collective-choice usage |
| Ryser | “Matrices of zeros and ones in combinatorial mathematics,” in *Recent Advances in Matrix Theory* (1964), 103--124 | same-score-sequence triangle-reversal lineage |
| Thomassen | *Discrete Mathematics* 71 (1988), 73--86, DOI `10.1016/0012-365X(88)90031-3` | arc reversals in tournaments |
| Ghosh--Kuchlous--Mehra--Mukhopadhyay | ESA 2026, LIPIcs 388, article 156, DOI `10.4230/LIPIcs.ESA.2026.156` | verified contemporary score-sequence/cycle-reversal neighbor |
| McKay | *Combinatorica* 10 (1990), 367--377, DOI `10.1007/BF02128671` | regular-tournament enumeration |
| Monsuur | *European Journal of Operational Research* 164 (2005), DOI `10.1016/j.ejor.2003.09.032` | upset/backward-edge inconsistency language |
| Flajolet--Sedgewick | *Analytic Combinatorics* (2009), DOI `10.1017/CBO9780511801655` | generic labelled-sequence recurrence/EGF machinery |
| Artin--Mazur | *Annals of Mathematics* 81 (1965), DOI `10.2307/1970384` | periodic-point zeta definition and routine one-factor specialization |

The manuscript contains a mechanics table separating static ranking/choice,
successive deletion and recomputation, iterative collective choice,
score-preserving or controlled arc/cycle reversals, and the present rule.  It
records state/output, vertex deletion, arc changes, score timing,
sequential-versus-synchronous action, and tie retention.

After subtraction, the only residual scope is the exact finite-map
conjunction for the specified synchronous map: simultaneous incidence and
Lyapunov identity, permanent score-class factorization, recursive pointwise
depth with its universal upper bound, and map-specific fixed-set
identification.  Regular counts, the labelled recurrence/EGF, and zeta are
low/zero-credit corollaries.  A bounded search miss is not novelty or priority
evidence.  Owner clearance and external dissemination remain **HOLD**.

## Presentation and collateral repairs

- The printed internal draft date was removed with `\date{}`; deterministic
  PDF controls, T1 encoding, and Latin Modern remain active.
- The abstract, introduction, conclusion, README, paper plan, narrative,
  claims/evidence map, control report, build record, verifier label, and stored
  stdout were synchronized to the repaired claim and credit boundary.
- The internal P106 firewall remains explicit: different phase space, update,
  recurrent objects, and proof engines; shared generic vocabulary receives no
  credit.
- The two input hostile reviews remain intact.  No future review, final hash,
  batch QA, Git operation, external post, or submission action was performed.

## Fresh mechanical regression

Verifier command:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
```

Byte comparison command:

```bash
cmp -s code/verification_output.txt \
  <(PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py)
```

Result: **PASS**, **1,677,508 assertions**, **33,868 states**, and fresh stdout
byte-identical to the stored **781-byte** transcript.

Settled four-stage build:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Result: **PASS**, `main.pdf` has **8 A4 pages** and **332,780 bytes**; the
Conclusion and References begin on page 7.  Final LaTeX warnings, BibTeX
warnings, undefined references/citations, and overfull/underfull boxes are all
zero.  Bibliography closure is **13/13**.  PDF author metadata is empty, and
all **23/23** fonts are embedded, subsetted, and Unicode-mapped.  All eight
rendered pages were visually inspected; the corrected iterate formula,
mechanics table, and references are legible without clipping or overlap.

## Provisional disposition after repair

The two reviews found no theorem-level counterexample, and every actionable
mathematical/presentation repair has been implemented.  This supports an
internal repaired-manuscript mechanical pass only.  Novelty, priority,
ownership clearance, and external dissemination remain **HOLD**.
