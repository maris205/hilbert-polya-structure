# Independent raw review of P46 `PAPER_PLAN.md`

## Verdict

- **Overall score:** **6.4 / 10**
- **Decision:** **REVISE** (not `PLAN_READY`)
- **Review mode:** independent, read-only, paper-plan standard
- **Writer bytes changed:** none
- **Review date:** 2026-08-18 UTC

This review is bound to the following inputs:

- `PAPER_PLAN.md`: `e8387e286e562507b0c0f2cd6966b1d2b43878ff7aa5ef000e326b9b157798b1`
- `CLAIMS_EVIDENCE.md`: `afc808da15ae6343be7a32c4212e14b3c1caa0f2c1fb007edf3e34990720e58f`
- `evidence/SOURCE_VERIFICATION.md`: `af397dadf5c268ff9df1de1c45495819f88c0ba1db88be7fd35c0bd2f5d62862`
- protected `preauthority/PROOF_PACKAGE.md`: `c6d4a4578d59ca7d3a4a9e02fe88b68b705ec35a0eefcb47277bec6dafc75`

## Six-axis scorecard

| Axis | Score | Raw assessment |
|---|---:|---|
| Logical flow and one-story coherence | 8.0 | The `0,1/2,1` walls -> valuation blocks -> cycle solver story is strong and unusually coherent. |
| Claim--evidence alignment | 7.2 | The analytic/finite/governance firewall is strong, but the direct-sum domain and some “certified proof replay” language do not yet align with what is actually established. |
| Mathematical statement precision and legal domains | 4.2 | One critical domain defect, an incomplete even-cycle theorem, and missing determinant overlap consistency block release. |
| Source positioning and novelty boundary | 8.3 | Narrow ownership statements and the no-priority firewall are good; related-work synthesis and exact manuscript-use locations remain underplanned. |
| Section/page feasibility | 4.0 | Seven main sections, four appendices, three figures, two tables, and references do not have a section-level budget and are not credible in 14--18 A4 pages inclusive. |
| Front matter and figure plan | 6.7 | The title/contribution and hero schematic are promising, but there is no actual Abstract plan, no substantive Related Work plan, and no explicit Conclusion. |

## Critical issues

### C1. The direct-sum theorem is not defined on the advertised unbounded domain

**Where:** `PAPER_PLAN.md` lines 51--64 and the one-sentence contribution; `CLAIMS_EVIDENCE.md` C4; protected `PROOF_PACKAGE.md` Steps 4 and 8.

The plan first writes “Let `s in C` ... `H_s` on `ell^2(N)`” and then claims

```text
H_s ~= direct_sum_{k>=0} 2^(-ks) A_s unitarily.
```

without a domain restriction. For `Re(s)<=0`, a fixed column (already the column at vertex 1) is not in `ell^2`; thus the formal matrix does not even define the usual `c00 -> ell^2` operator. Calling it an unbounded operator on `ell^2`, and then asserting unitary direct-sum equivalence, requires a separately defined dense domain, closure, and proof that the valuation unitary maps the operator domains exactly. None is present. The support identity alone proves a matrix/block identity, not an equivalence of unbounded operators.

**Minimum safe repair:** do not open an unnecessary unbounded-operator problem. State:

> For `sigma>0`, the matrix defines a bounded compact operator `H_s`. If
> `W: direct_sum_{k>=0} ell^2(odd) -> ell^2(N)` maps the `k`th odd copy to
> the exact-valuation subspace, then
> `W^* H_s W = direct_sum_{k>=0} 2^(-ks) A_s` as bounded operators.
> For `sigma<=0`, the formal matrix admits no bounded realization with
> these matrix coefficients; no unbounded direct-sum equivalence is claimed.

This restriction loses none of the paper's trace or determinant results, which already live in `sigma>1/2`. If the authors insist on all-complex-`s` unbounded equivalence, that becomes a new theorem package and must define minimal/maximal domains, density, closability/closedness, and exact domain transport before writing may begin.

## Major issues

### M1. “Complete” even-cycle closure is promised but its explicit positivity interval is absent

**Where:** `PAPER_PLAN.md` lines 71--80 and 164--173; protected `PROOF_PACKAGE.md` Step 10.

Both documents say that positivity cuts out an “explicit finite open interval,” but neither gives it. This is the key constructive content of the even theorem and cannot be deferred as a phrase while the title and contribution claim completeness.

**Minimum repair:** put the formula in the main theorem and the section plan. With

```text
b_1 = 0,
b_i = sum_{j=1}^{i-1} (-1)^(i-1-j) q_j,
n_i = (-1)^(i-1) x + b_i,
```

and the even compatibility condition, define

```text
L(q) = max_{1<=i<=r, i odd} (-b_i),
U(q) = min_{1<=i<=r, i even} b_i.
```

Then the positive integer solutions are exactly

```text
x = n_1 in Z intersect (L(q), U(q)),
n_i = (-1)^(i-1)x + b_i.
```

The odd block is the subset with `x` odd (all vertices then have the same odd parity). State explicitly that the interval may be empty and, because its endpoints are integers, the unrestricted count is `max(0,U-L-1)`. This gives the advertised solver rather than merely promising one.

### M2. The complex-phase firewall is close but still not strong enough

**Where:** `PAPER_PLAN.md` lines 126--131; protected `PROOF_PACKAGE.md` Step 1.

The identity

```text
H_s = U_t H_sigma U_t
```

is a left-right unitary factorization, not unitary conjugacy or operator similarity. It preserves singular values, ideal membership, compactness, and corresponding norms. It does **not** preserve spectrum, powers, traces, or determinants. In particular, one cannot infer `Tr(H_s^r)` or `det_2(I-zH_s)` from the real operator by “phase removal,” because the middle factors do not cancel in powers.

The plan already forbids “unitary conjugacy” and nonreal self-adjointness, which is good, but it must add the positive rule:

> Phase removal is used only for singular-value/ideal assertions. Every trace,
> power, and determinant identity retains complex `s` and is derived instead
> from the exact valuation direct sum.

Prefer “two-sided unitary factorization” or “left-right unitary equivalence for singular values,” not the unqualified phrase “unitarily equivalent.”

### M3. The `det_2` product needs a complete legality and overlap-consistency paragraph

**Where:** `PAPER_PLAN.md` lines 65--70 and 154--162; `CLAIMS_EVIDENCE.md` C5; protected `PROOF_PACKAGE.md` Step 9.

The principal domain `sigma>1/2` is correct, and local uniform convergence of the factor product is plausible from square-summability of the block Hilbert--Schmidt norms. The plan nevertheless omits three local consistency statements that are needed to keep determinant types from drifting:

1. For `sigma>1/2`, `det_2(I-zH_s)` and every block factor are entire in `z`, and the product converges uniformly on compact `z`-sets.
2. The logarithmic trace expansion is only a near-zero identity on a specified zero-free disk (a sufficient bound is `|z| ||H_s|| < 1`), with the logarithm branch fixed at `z=0`; it is not globally equivalent to the entire product.
3. In the overlap `sigma>1`, explicitly reconcile the determinant types:

   ```text
   det_2(I-zH_s) = det(I-zH_s) exp(z Tr(H_s)),
   Tr(H_s) = 1/(1-2^(-s)).
   ```

   If the ordinary block product is stated, justify it by trace-norm summability and state
   `det(I-zH_s)=product_k det(I-z2^(-ks)A_s)` on this domain.

The specialized `det_2` direct-sum proof should appear in the main text at least as a proposition plus proof sketch; Appendix B may carry the uniform-on-compacts bound. “A short appendix-level lemma” is not a precise proof-placement decision.

### M4. The paper has no executable Abstract, Related Work, or Conclusion plan

**Where:** the planned section architecture in `PAPER_PLAN.md` lines 113--190.

There is no Abstract subsection with the result/domain/evidence sentence sequence required by the paper-plan standard. “Introduction/related work” appears only in the citation plan, not in the section architecture. Section 7 promises to “close with non-goals” but is not an explicit conclusion.

**Minimum repair:** add all three:

- **Abstract (about 180--220 words):** exact operator, the three strict walls, the bounded-domain valuation theorem, ordered-label cycle solver, and one finite-replay sentence explicitly marked diagnostic/reproducibility evidence. Do not use “first,” “novel,” or “unitarily equivalent” without its domain.
- **Related-work synthesis (0.75--1.0 page):** organize by (i) classical Hankel/Schatten theory, (ii) lacunary Schur/folding machinery, and (iii) finite powers-of-two determinant/labeling problems. For each family, state both what is borrowed and what is a different mathematical object. This can be a dedicated section or a clearly budgeted Introduction subsection.
- **Conclusion (0.4--0.6 page):** restate only the proved package, limitations, and the precise next mathematical question. Either rename Section 7 to include Conclusion or add an eighth main section.

### M5. The 14--18-page inclusive budget is not credible and has no per-section accounting

**Where:** `PAPER_PLAN.md` lines 18--21 and all section/figure/appendix plans.

Seven main sections, four proof/reproducibility appendices, three figures, two tables, and references cannot be assessed against a single 14--18 page interval without per-section estimates. The current plan simultaneously asks for mathematical completeness and four appendices, so the low end is especially implausible.

**Minimum repair:** choose one explicit accounting model and make the numbers sum. A realistic starting allocation is:

| Component | Pages |
|---|---:|
| Abstract/front matter | 0.4 |
| 1. Introduction + synthesized related work | 2.0 |
| 2. Source/operator setup | 1.5 |
| 3. Boundedness/compactness | 1.5 |
| 4. `S_2`/`S_1` walls | 2.5 |
| 5. Valuation, traces, determinants | 2.3 |
| 6. Cycle calculus | 2.0 |
| 7. Replay/limitations | 1.0 |
| Conclusion | 0.5 |
| References | 1.3--1.7 |
| Appendices A--D | 5.5--6.5 |

This totals roughly 20--22 pages including references and appendices. To retain an 18-page hard cap, merge Figures 1 and 2, compress the replay ledger to one table, move reproducibility hashes to a machine-readable supplement, and cap the main text around 11 pages. The next plan must state whether appendices/references count and give a sum that matches the announced target.

### M6. The release gate and proof-evidence language are internally inconsistent

**Where:** `PAPER_PLAN.md` hard gate 1, lines 242--246; `CLAIMS_EVIDENCE.md` C1--C6.

Hard gate 1 is marked `[complete]` while saying the independent post-output audit is “in progress.” An in-progress audit is not a completed gate. Separately, statuses such as “Certified proof replay” risk suggesting that an automated proof audit established the infinite theorem, despite the otherwise good evidence firewall.

**Minimum repair:** mark the independent audit gate `IN_PROGRESS` until an exact PASS receipt exists, or split it into two gates (State-A integrity complete; independent post-output audit pending). Replace “Certified proof replay” with language such as “proof-contract checks passed; the infinite theorem remains proof-owned and is established only by the manuscript proof.” Do not block plan editing on the audit, but do block paper-write/freeze if that is the intended governance rule.

## Minor issues

### m1. Two internal file references are stale

`PAPER_PLAN.md` names `CLAIMS_EVIDENCE_DRAFT.md` and `SOURCE_VERIFICATION_DRAFT.md`; the reviewed files are `CLAIMS_EVIDENCE.md` and `evidence/SOURCE_VERIFICATION.md`. Correct both before downstream automation reads the wrong path.

### m2. The working title can still be mistaken for an orbit/quotient theorem

“Complete Cyclic Closure” is defensible only with the current scope firewall, but a skim reader may read it as primitive-orbit enumeration modulo rotation. Prefer “Complete Ordered-Label Cycle Solver” or put “for fixed ordered dyadic labels” in the subtitle/abstract. Keep the explicit statement that primitive reduction and cyclic base-point quotienting are separate.

### m3. Distinguish a Dirichlet-weighted Hankel matrix from a classical Hankel operator

For `s != 0`, the entries are not a function of `m+n` alone; the object is a diagonal Dirichlet weighting of the powers-of-two Hankel support. State this early so the Peller context is not read as a direct application of a classical Hankel classification theorem.

### m4. State the cycle-length conventions locally

The trace theorem uses `r>=2`, while the cycle solver in the proof package permits `r>=1` because loops are retained. Put these distinct ranges in the theorem and examples; do not let `r>=2` leak from determinant notation into the cycle statement.

### m5. Tighten the source-use map, without changing the good no-priority boundary

The source/novelty discipline is one of the plan's strengths: Peller/Simon are standard infrastructure, Fournier--Wagner ownership is preserved, Guo/Alekseyev are explicitly different finite objects, and bounded search absence is not priority evidence. Before drafting, add the exact section/proposition/passages supporting each standard imported fact and retain the rule that the specialized `det_2` block argument is reproduced. No new priority language is warranted.

### m6. Clarify the hero figure's “impossible edge” encoding

Draw a cross-valuation pair as a crossed-out candidate/non-edge, not as a highlighted edge, so the schematic does not visually contradict the support lemma. The proposed self-contained caption and grayscale/vector checks are otherwise good.

## What is already strong

1. The paper has a genuine one-story structure: sharp ideal walls, exact valuation self-similarity, then ordered-label closure on the same dyadic support.
2. Endpoint ownership is appropriately analytic. The plan does not infer `sigma=0`, `1/2`, or `1` from finite cutoffs.
3. The finite replay is carefully typed as implementation evidence rather than proof or novelty.
4. The source firewall is unusually disciplined: no priority claim, narrow ownership, and explicit separation of finite Hankel determinants/finite labeling from the present infinite weighted operator.
5. The figure/table plan is concrete, vector-first, and mostly source-bound.
6. The primitive-orbit and cyclic-basepoint nonclaims are already explicit and should be preserved.

## Minimum patch set for `PLAN_READY`

The same-reviewer recheck can return `PLAN_READY` only if all of the following are visible in the revised plan (and, where applicable, the claims matrix):

1. The operator direct sum is restricted to `Re(s)>0`, or a complete unbounded-domain theorem is supplied. The first option is strongly recommended.
2. The complex-phase paragraph states exactly what left-right factorization preserves and explicitly excludes traces, determinants, spectra, and powers.
3. The even-cycle theorem contains the displayed `b_i`, `L`, `U`, solution-set, and odd-parity formulas.
4. The `det_2` section separates the entire locally-uniform product, the near-zero logarithmic expansion, and the `Re(s)>1` ordinary-determinant overlap identity.
5. Abstract, synthesized Related Work, and Conclusion plans are present.
6. Every main section and appendix has a page estimate; the sum matches the declared inclusive/exclusive budget.
7. The independent audit gate is no longer both complete and in progress, and proof-audit wording cannot be read as machine certification of an infinite theorem.
8. The two stale filenames are corrected.
9. The no-priority, no-all-`S_p`, no-Hilbert--Polya, and no-primitive-quotient firewalls remain intact.

Until these conditions hold, the plan is coherent enough to revise but not safe enough to authorize paper writing.
