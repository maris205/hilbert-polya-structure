# P214 claim, proof and source ledger

Date: 2026-09-11 UTC. Deductive status: `PROVABLE AS STATED`, matching the
root-admitted contract. Author execution, canonical, builds and manuscript
A/B reviews: `PENDING`. This ledger is not an execution receipt or PASS.

## Fixed assumptions and dependency map

Every mathematical claim below uses a prime power q, integer m>=2,
R=F_q[t]/(t^m), I=tR, full carrier I², F(x,y)=(y,x(t+y)), and v(0)=m.
The identity v(ab)=min(m,v(a)+v(b)) and |t^rR|=q^(m-r) are proved from
coefficients. No arbitrary finite-chain-ring generalization is implicit.

The temporal theorem depends on the recurrence representation and the
post-index-2 ideal inclusion. The depth census depends only on that theorem
and ideal sizes. The inverse theorem depends on multiplication image/kernel
ideals. Its distribution depends on translation and valuation-stratum counts.
Nonconjugacy depends on the resulting unequal positive fibres and an explicit
kernel-coset argument for finite groups. No proof relies on an executed check.

| ID | Exact claim and boundaries | Manuscript proof location | Evidence / source ownership |
| --- | --- | --- | --- |
| C1 | For a=v(x), b=v(y), tau=max{2(m-b),2(m-a)-1} | Section 2, clock theorem and two case proofs | Root-admitted author deduction; generic precision increase is known, exact cancellation-safe application is the temporal advance |
| C2 | Zero uniquely recurrent; height 2m-2, attained iff b=1 | Section 2, clock theorem | Consequence of C1, including zero coordinates and m=2; not separate novelty |
| C3 | Cumulative depth q^h for 0<=h<=2m-2; exact h>0 count (q-1)q^(h-1) | Section 2, census corollary | C1 plus ideal counts; same distribution as linear control, not a third axis |
| C4 | At (u,w), d=min(v(t+u),m-1); reachable iff w in t^(d+1)R; fibre {(x0+k,u):k in t^(m-d)R} | Section 3, fibre theorem | Full self-contained image/kernel proof; ordinary multiplication/annihilator mechanism, wholly deducted through QMP |
| C5 | Ordinary fibre q^d has (q-1)q^(2(m-d-1)) targets, 1<=d<=m-2; q saturated fibres have size q^(m-1) | Section 3, census corollary | Valuation-stratum evaluation of C4; not a new inverse method |
| C6 | Maximum targets exactly (-t+c t^(m-1),0); image q+(q-1) sum_(j=1)^(m-2) q^(2j) | Section 3, census corollary | C4/C5 and empty sum at m=2; all remaining targets have empty fibre |
| C7 | F=QMP, P(x,y)=(x,y+t), Q(u,w)=(u-t,w), M(a,b)=(b,ab) | Section 4, exact adapter | Direct identity; transfers one-step fibres, NOT iterate conjugacy |
| C8 | L(x,y)=(y,tx) has the same pointwise clock/census; F=L for m=2 | Section 4, comparison proposition | Explicit parity-chain formula; all numerical shape/linear-boundary novelty deducted |
| C9 | For m>=3, F is not bijectively conjugate to any finite-group endomorphism | Section 4, comparison proposition | C5 gives positive sizes q and q^(m-1); every endomorphism fibre is a kernel coset; excludes no arbitrary nonlinear factor |

## Source categories and allowed attribution

The primary bibliography verification will record actual metadata, passages,
retrieval and limits in `sources/`. Only finalized, actually cited entries
belong in `references.bib`; no placeholder or inferred bibliographic item is
allowed. The intended categories are:

1. Finite-group endomorphism dynamics: contextualizes structural constraints
   on maps with an algebraic linear/group representation. It does not
   linearize F or supply C1. The elementary constant-fibre fact is proved.
2. Fibonacci polynomial dynamics: its complex map (xy+c,x), after coordinate
   interchange at c=0, identifies the multiplication polynomial. Neither its
   complex carrier nor its constant c is identified with the present tx term.
3. Finite-commutative-ring linear systems, if retained: contextualizes module
   endomorphisms only; no source theorem is applied beyond its hypothesis.

The original internal MFR/WCF/fresh09 controls and bounded candidate-source
gate are explicitly recorded in the admission/scout packages. They remain
provenance rather than anonymous public bibliography entries. The paper's
algebraic identities make the corresponding deductions self-contained.

## Verifier claim mapping and mandatory negative controls

The fixed source must independently reconstruct literal orbits and full
predecessor lists before comparing them with formulas. Named checks must
cover C1–C9, all carrier/transition closure, exact predecessor sets (not just
counts), the saturated inverse branch, m=2 and characteristic-two cancellation.
F4 arithmetic must distinguish the field from arithmetic modulo four.

The parameter box has nine carriers and deductively 5271 states; no row or
count has been observed. OUTPUT_PLAN and OUTPUT_SCHEMA will define the full
ordered record stream, check census, failure behavior and future canonical
comparison. Hash checking of source files is not mathematical validation.

## Authorship and later gates

Main scout, root and `fresh55_local_ring_collision` are proof contributors.
New author verifier and bibliography contributors are recorded in README.
Candidate gate reviewer `p213_manuscript_review_b` was noncontributing for
the candidate gate; that gate is not manuscript Review A or B. No independent
manuscript review is claimed in this source package.
