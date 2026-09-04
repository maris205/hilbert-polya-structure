# P193 Review-A source and owner-collision audit

**Audit date:** 2026-09-04 UTC  
**Decision:** `PASS`; historical source revision installed and accepted; no
literal-map collision established.  
**Gate:** `OWNER_AMBER / HOLD_EXTERNAL`.

## Bibliography verification

The three frozen records resolve and their central metadata agree with
publisher/index records:

| Record | Checked metadata | Result |
|---|---|---|
| Bóna, *Combinatorics of Permutations*, 2nd ed. | CRC Press, 2012, DOI [10.1201/b12210](https://doi.org/10.1201/b12210) | PASS |
| Gale--Shapley, *College Admissions and the Stability of Marriage* | *American Mathematical Monthly* 69(1), 9--15 (1962), DOI [10.2307/2312726](https://doi.org/10.2307/2312726) | PASS |
| Stanley, *Enumerative Combinatorics*, Vol. 1, 2nd ed. | Cambridge University Press, print year 2011, DOI [10.1017/CBO9781139058520](https://doi.org/10.1017/CBO9781139058520) | PASS |

The citations support only direct-sum/permutation background and classical
matching stability.  They are not presented as owners of P193's theorem
package.

## Exact owner query and located neighbour

Queries combined `mutual best blocking pairs`, `blocking pair dynamics`,
`common master list`, `simultaneous exchange`, `sum-indecomposable first
minimum swap`, and `parallel permutation sorting operator`.

The significant hit is Schipper--Zhang,
[*Matching, Unanticipated Experiences, Divorce, Flirting, Rematching,
Etc*](https://arxiv.org/abs/2504.01280), arXiv:2504.01280 (2025).  It defines
mutual optimal/best blocking pairs and gives them priority in a decentralized
stochastic matching process.  It is not a literal P193 owner: its process
satisfies a selected pair sequentially/probabilistically, includes friction
and changing awareness/preferences, and does not derive P193's common-order
permutation block surgery, depth recurrence, or fibre product.  It does own
nearby terminology and process language.  Its original omission was finding
P193-A1; the repaired paper now cites and subtracts it.

The permutation/direct-sum queries returned standard indecomposable-class and
parallel-sorting neighbours, not the frozen P193 conjunction.  This bounded
result is not a novelty, priority, completeness, or freedom-to-operate claim.

## Internal P1--P191 subtraction

The live definitions of the nearest internal systems were reread.

| Prior system | Shared surface | Literal separation |
|---|---|---|
| P105 cycle-minimum pruning | permutation carrier, one absorber, `n-1` tail scale, fibres | modifies functional-cycle arrows; P193 swaps first/minimum entries inside one-line direct-sum blocks |
| P122 even record-block reversal | adaptive permutation blocks, sharp clock, target fibres | cuts at left-to-right maxima and reverses parity-selected blocks; P193 uses direct-sum cuts and exchanges all nontrivial blocks |
| P155 cycle-maximum extraction | cycle extrema and target fibres | rank-changing support extraction, not a fixed-rank position exchange |
| P156 weak-excedance extraction | permutation image/fibre analysis | rank-changing diagonal selection and standardization, not block surgery |
| P181 first-descent prefix reversal | inversion trigger and same carrier | one prefix reversal with a depth-two two-cycle core; P193 has parallel disjoint swaps, strict refinement, and one absorber |
| P191 prefix-divisibility cuts | block monotonicity and inverse grouping | composition cut/coarsening rule with divisibility data, not a permutation nomination map |

The manuscript's explicit `132` and `3412` negative controls agree with the
live P181 and P105 definitions.  No inspected internal map transfers both the
P193 update and its target product.  This establishes only the internal
firewall, not external novelty.

## Accepted disposition

P193-A1 is closed.  The repaired manuscript and source ledger keep all
matching/common-master and sequential/stochastic mutual-best dynamics
zero-credit, distinguish the fixed-order simultaneous map, and retain
`OWNER_AMBER / HOLD_EXTERNAL`.  Open source findings: `0`.
