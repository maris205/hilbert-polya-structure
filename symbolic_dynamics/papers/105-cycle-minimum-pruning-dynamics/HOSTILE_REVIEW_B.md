# Independent cross-hostile review B — P105

Audit date: 2026-08-29 UTC.  This pass reviewed the tree after independent
review A had frozen it.  It is a team-internal audit, not an external referee
report, and supplies no novelty, priority, or release endorsement.

Verdict: **GO for internal Stage 2 use / HOLD for external release**.
CRITICAL: 0.  Mathematical MAJOR: 0.  Repaired MINOR: 1.  One release-only
owner gate remains major.

## Independent theorem reconstruction

### Forward dynamics and time convention

Write each original cycle in its inherited orientation and order its labels
as `s_1<...<s_ell`.  One application removes exactly `s_1`, fixes it, and
reconnects its predecessor to its successor.  Induction on time therefore
leaves the inherited cycle on
`C\{s_1,...,s_min(t,ell-1)}` and fixes precisely those removed labels.
Nothing is standardized and different original cycles evolve in parallel.
Thus a length-`ell` cycle finishes at time `ell-1`, including `ell=1,2`, and
the whole permutation has depth `L(pi)-1`.

The number of fixed labels strictly increases at every nonidentity step and
never decreases.  Consequently the identity is the unique recurrent point,
every positive iterate fixes only it, least-period counts vanish beyond one,
and the formal Artin--Mazur zeta factor is exactly `(1-z)^(-1)`.

### Depth layers

Depth at most `t` is equivalent to every cycle length being at most `t+1`.
Adjacent subtraction gives `D_(n,t)=A_(n,t+1)-A_(n,t)`.  The restricted-cycle
EGF is the standard labelled SET-of-CYCLES construction.  Independently,
exposing the cycle containing label 1 gives
`binom(n-1,j-1)(j-1)!=(n-1)!/(n-j)!`, proving the recurrence without the EGF.
The endpoints are correct: an `n`-cycle gives `(n-1)!` deepest states; for
`n>=3`, the penultimate layer is one `(n-1)`-cycle plus a singleton, giving
`n(n-2)!`.

### One-step indegree and Garden-of-Eden condition

Every nontrivial output cycle `B_i` must come from one source cycle of length
`|B_i|+1`.  Its deleted source minimum is a fixed output label below
`b_i=min(B_i)`, and distinct output cycles require distinct fixed labels.
Order `b_1<...<b_r`.  Each of the previous `i-1` choices is automatically
below `b_i`, so among the `e_i` eligible fixed labels exactly
`e_i-i+1` remain.  This proves both the product and the sharp nonexistence
condition `e_i<i`; it is the nested/Ferrers form of Hall's condition, not an
independence heuristic.

For each matching, inserting the chosen minimum into one of the `ell_i`
directed edges of `B_i` gives exactly `ell_i` distinct source cycles.
Unmatched output fixed labels arise uniquely as source singletons or source
transpositions; an involution records exactly that singleton/pair partition.
The factors are therefore bijective and nonoverlapping.  Endpoint probes are
consistent: `(1 2)` in `S_2` is Garden-of-Eden, while `(1)(2 3)` has the two
ancestors `(1 2 3)` and `(1 3 2)`, and the identity fiber is `I_n`.

## Finding and implemented repair

### MINOR — trajectory evaluations were called graph edges

The manuscript and evidence ledger called `1,981,326` the number of
“nontrivial pruning edges.”  That counter is incremented while every starting
permutation is followed along its whole trajectory, so the same
functional-graph edge may be traversed many times.  A functional graph on
409,113 states cannot have 1,981,326 distinct outgoing edges.  The arithmetic
was genuine, but the label overstated what was counted.

The code/output key is now `literal_trajectory_steps`; the manuscript,
README, claims ledger, and control results say explicitly that these are
trajectory-step evaluations with repetitions across starting states.  The
assertion count and all theorem evidence remain unchanged.

## Owner and internal-collision audit

Publisher records verify the cited scopes and DOI metadata: Flajolet--Sedgewick
(`10.1017/CBO9780511801655`) and Stanley
(`10.1017/CBO9781139058520`) own standard labelled permutation enumeration;
Shepp--Lloyd (`10.1090/S0002-9947-1966-0195117-8`) own the ordered and longest
cycle laws; Pitman (`10.1007/b11601500`) owns nearby deletion-consistent
structures; and Artin--Mazur (`10.2307/1970384`) own the periodic-point zeta
construction.  None is presented as owner of the exact simultaneous labelled
surgery.  A bounded exact-map search found no direct owner, but search absence
is not novelty evidence.  Specialist review is still required.

The P100 firewall survives attack.  P100 changes arithmetic digit
coordinates and has digit-sum time.  P105 preserves the labelled set,
processes all permutation cycles in parallel, and has a threshold-matching
inverse graph.  Earlier finite-subset and permutation papers use different
phase spaces and do not contain this indegree mechanism.

## Post-repair controls and build

A fresh run is byte-identical to `CONTROL_OUTPUT.txt` after the descriptive
key repair:

```text
cycle-minimum pruning exact control: PASS
assertions=17219241
literal_permutations=409113
literal_trajectory_steps=1981326
fibre_formula_states=409113
restricted_cycle_recurrence=PASS n<=50
periodic_mobius_zeta=PASS periods<=60
```

All 409,113 literal output states through `S_9` still have their indegree
compared with the closed formula.  The four-stage build
`pdflatex -> bibtex -> pdflatex -> pdflatex` passed.  `main.pdf` has 5 A4
pages and 331,334 bytes; `pdftotext -layout` recovered 17,919 bytes.  The
final logs contain no LaTeX/package warning, undefined citation/reference,
multiply-defined label, overfull/underfull box, or error.  All 24 fonts are
embedded, subsetted, and Unicode mapped.  The modified final page was rendered
and visually inspected without clipping or malformed text.

## Disposition

- Theorems, endpoints, and one-step fiber bijection: **GO internally**.
- Exact controls: **GO after correcting the counter semantics**.
- Public release, submission, specialist contact, novelty, and priority
  language: **HOLD** pending the direct-owner gate and final artifact QA.
