# Cross-hostile review B — P106

Date: 29 August 2026.  Reviewer role: second independent reviewer, separate
from the author and review A.  External circulation remains **HOLD**.

## Verdict

**Internal PASS after the recorded repairs.**  Unresolved CRITICAL: 0.
Unresolved mathematical MAJOR: 0.  The polarity, orbit, square-law, path,
and zeta formulas all survive independent reconstruction.  Before the
freeze there were 2 source/ownership MAJOR findings and 2 MINOR findings;
all are repaired and independently replayed below.

## Independent formula attack

1. **Polarity and orbit shape.**  Symmetry of the undirected adjacency
   relation gives `A subset F^2(A)`.  Antitonicity applied first to this
   inclusion and then extensivity applied to `F(A)` give both inclusions in
   `F^3(A)=F(A)`.  Consequently `im F=Fix(F^2)`, every positive odd iterate
   is `F`, every positive even iterate is `F^2`, preperiod is at most one,
   and periods are only one or two.  Open neighborhoods are essential and
   are stated explicitly.
2. **Fixed and periodic counts.**  `F(A)=A` is equivalent to `A` being both
   independent and dominating, hence a maximal independent set.  On the
   closed configurations `F` is an involution.  Thus the fixed sequence is
   `m(G)` on odd times and `c(G)` on even times, with `(c-m)/2` two-cycles;
   direct summation gives exactly the displayed zeta factors.
3. **Bipartite square law.**  For `A=P union Q`, the update is
   `(P,Q)->(beta(Q),alpha(P))`, so closure separates as
   `(beta alpha(P), alpha beta(Q))`.  The two one-sided closed systems have
   equal size `r`, because `alpha,beta` restrict to inverse
   anti-isomorphisms.  Closed full configurations number `r^2`, whereas
   fixed pairs number `r`.  Hence `c(G)=m(G)^2`, including isolated vertices
   and empty color sides.
4. **Path endpoint recurrence.**  Conditioning on vertex one gives the
   disjoint branches `m_(n-2)` and `m_(n-3)` with
   `m_0=m_1=1,m_2=2`.  The rational generating function and the specialized
   zeta formula follow without an omitted small-`n` endpoint.

## Repaired findings confirmed by review B

- **MAJOR, repaired — false bibliographic identity.**  The earlier
  `Richard2018` DOI did not belong to the cited conjunctive-network work.
  The frozen source now cites Aracena--Richard--Salinas, *JCSS* 88 (2017),
  145--163, DOI `10.1016/j.jcss.2017.03.016`, and the evidence ledger names
  the same owner.
- **MAJOR, repaired — missing direct path owner.**  The Padovan recurrence
  is now explicitly labeled classical and assigned to
  Euler--Oleksik--Skupie\'n (2013), DOI `10.7151/dmgt.1707`, Remark 2.2.
- **MINOR, repaired — visible TeX token.**  Both stray `qquad` tokens in the
  path display are now `\qquad`; extracted text and page rendering confirm
  the repair.
- **MINOR, repaired — non-evidentiary verifier work.**  A redundant inner
  loop computed iterates but made no assertion.  It was removed; the later
  independent odd/even fixed-count lane remains intact, and the registered
  output is unchanged.

## Owner and collision boundary

Gadouleau--Kutner study the same MIS Boolean local rule and its known fixed
points, with emphasis on sequential schedules.  Formal concept analysis owns
the antitone Galois-closure machinery.  The manuscript subtracts both and
claims only the displayed synchronous functional-graph/zeta conjunction.
This is a **direct-system collision**, even though the exact cubic-collapse,
two-cycle, and zeta package was not found in the checked source.  The owner
risk is therefore materially higher than for a merely analogous graph model.

Internally, P68 also uses bipartite graph structure, P80 gives graph-based
finite zeta formulas, and P75 is graph/language based.  P106 differs in its
Boolean phase space, antitone update, closure count, and MIS fixed-point
parameter.  These distinctions avoid literal theorem duplication but do not
reduce the external direct-system owner gate.

## Control independence and mechanical replay

The exact program implements the update twice: once by integer bitsets and
once by literal set/relation operations.  It exhausts every simple graph
through six vertices, every bipartite graph through `3+3`, every path state
through 17 vertices, and separate `K_2/K_3` sentinels.  A fresh run reproduced
the stored output byte for byte and reported **6,462,317 assertions**.

The exact sequence `pdflatex -> bibtex -> pdflatex -> pdflatex` exited zero.
Final `main.log`/`main.blg` scans found no substantive warning, undefined
citation/reference, multiply-defined label, overfull/underfull box, or error.
The PDF has 4 A4 pages and 299,003 bytes.  All 23 font entries are embedded,
subsetted, and Unicode-mapped; layout text extraction recovered 13,379 bytes.
All four rendered pages were visually inspected with no clipping, collision,
malformed display, or orphaned heading.

## Residual risk

- **Direct-owner risk: high.**  The exact network and its fixed-point
  interpretation already have a direct adjacent owner; classical polarity
  makes the remaining synchronous laws short consequences.
- **Mathematical risk: low.**  All finite-dynamical identities and endpoints
  are exact and independently controlled.
- **Release status: HOLD.**  Specialist priority review is mandatory; no
  absolute novelty or priority language is authorized.
