# Same-reviewer recheck of revised P46 paper plan

## Recheck identity

- **Round-0 raw review:** `/tmp/p46_plan_review_raw.md`
- **Revised `PAPER_PLAN.md`:** `a80d73345a18eb377aa93cee2b48e99c8e462be1bce7af289cda868a19b96f90`
- **Revised `CLAIMS_EVIDENCE.md`:** `465feb363273447ff79210a6a5138d9bf1807ced7f67e61565ed644756819d16`
- **Unchanged source verification:** `af397dadf5c268ff9df1de1c45495819f88c0ba1db88be7fd35c0bd2f5d62862`
- **Unchanged protected proof package:** `c6d4a4578d59ca7d3a4a9e02fe88b68b705ec35a0eefcb47277bec6dafc75`
- **Writer bytes changed by reviewer:** none

## Verdict

- **Score:** **8.2 / 10**
- **Decision:** **REVISE**
- **Critical:** **0**
- **Major:** **4**
- **Minor:** **3**

This is a substantial and good revision. The original critical direct-sum
claim is repaired, the even-cycle interval is now constructive, the page
budget is executable, and source ownership remains disciplined. `PLAN_READY`
is nevertheless reserved for zero Critical and zero Major issues, and four
narrow release blockers remain.

## Six-axis recheck

| Axis | Round 0 | Recheck | Assessment |
|---|---:|---:|---|
| Logical flow and one-story coherence | 8.0 | 8.8 | Strong section sequence and much better front-loading. |
| Claim--evidence alignment | 7.2 | 7.8 | Domains are mostly aligned, but machine-audit “Certified proof” wording remains. |
| Mathematical statement precision/legal domains | 4.2 | 7.3 | Direct sum and determinant overlap are repaired; phase-factorization domain and local log details remain. |
| Source positioning/novelty boundary | 8.3 | 8.9 | Dedicated synthesis and ownership subtraction are now explicit. |
| Section/page feasibility | 4.0 | 8.7 | The allocations sum exactly and the total is credible, though tight. |
| Front matter/figure plan | 6.7 | 7.8 | Abstract and Related Work now exist; explicit Conclusion still does not. |

## Round-0 issue disposition

| Round-0 item | Disposition |
|---|---|
| C1 unbounded-domain direct sum | **Resolved.** Restricted to bounded operators on `Re(s)>0`; no all-`s` unbounded equivalence. |
| M1 explicit even-cycle interval | **Resolved in substance.** `b_i`, `L`, `U`, integer interval, and odd filter are present. |
| M2 complex-phase firewall | **Partially resolved.** Preservation/non-preservation list is excellent; the stated finite-support operator domain is still invalid for `Re(s)<=0`. |
| M3 determinant legality/overlap | **Partially resolved.** Entire product and trace-class overlap are present; near-zero log branch/radius and a main-text proof sketch remain absent. |
| M4 Abstract/Related Work/Conclusion | **Partially resolved.** Abstract and Related Work are good; Conclusion remains only implicit. |
| M5 page feasibility | **Resolved.** Main 11.25 + references 1.25 + appendices 4.8 = 17.3 pages. |
| M6 release/proof-evidence language | **Partially resolved.** Release gate is fixed; “Certified proof replay” remains in C1--C3. |
| stale filenames | **Resolved.** |
| no-priority and primitive-quotient firewalls | **Preserved.** |

## Remaining Major issues

### R-M1. Phase factorization still claims an invalid finite-support operator identity for `Re(s)<=0`

Section 3 says to prove `H_s=U_tH_sigma U_t` “first on finitely supported
vectors.” For `sigma<=0`, even `H_s e_1` and `H_sigma e_1` are not in
`ell^2`; thus neither side is an `ell^2`-valued operator on `c00`. The new
sentence correctly limits the valuation direct sum, but this separate domain
statement still reintroduces the same formal-matrix/operator ambiguity.

**Minimum fix:** replace that sentence with both levels explicitly:

> Entrywise, and equivalently on every finite compression,
> `P_N H_s P_N = U_t P_N H_sigma P_N U_t`. On `sigma>0`, where the matrices
> define bounded operators, this passes to the bounded-operator identity
> `H_s=U_tH_sigma U_t`. Only singular-value properties transfer; spectra,
> powers, traces, and determinants do not.

For `sigma<=0`, say “the formal matrix has no bounded operator realization
with these coefficients,” not that it acts from `c00` into `ell^2`.

### R-M2. The determinant section still omits the near-zero logarithmic identity and a main-text proof sketch

The revised plan now gives the entire locally-uniform `det_2` product and the
correct `sigma>1` overlap identity. It does not plan the protected proof
package's logarithmic formula, its branch, or its legal neighborhood. It also
places the specialized proof entirely in Appendix B, despite the determinant
product being a headline contribution.

**Minimum fix:** add two Section-6 bullets:

1. State that, on the branch normalized by `log det_2(I)=0`, for the
   sufficient disk `|z| ||H_s|| < 1`,

   ```text
   log det_2(I-zH_s)
     = -sum_{r>=2} z^r/r * Tr(A_s^r)/(1-2^(-rs)).
   ```

   Explicitly distinguish this local logarithm from the entire factor
   product.
2. Put the proposition and a 3--5 line proof sketch in Section 6: the
   valuation unitary gives the block union, squared Hilbert--Schmidt norms
   are summable, and canonical factors converge normally on compact
   `z`-sets. Leave the detailed zero/eigenvalue bookkeeping and estimates in
   Appendix B.

### R-M3. There is still no explicit Conclusion plan

The revised plan adds an Abstract and a real Related Work section, but
Section 8 is still titled “Independent replay, ownership, and limitations”
and ends with non-goals. A limitations paragraph is not automatically a
conclusion, and the page-plan rubric explicitly required one.

**Minimum fix:** either rename it “Independent replay, limitations, and
conclusion” and reserve its final 0.35--0.45 page for a conclusion, or add a
short Section 9 while keeping the same total by reducing replay detail.
Specify: theorem restatement in different words, why the shared dyadic
support matters, one exact limitation, and one concrete next question. No
new claim or priority language belongs there.

### R-M4. The claims matrix still labels machine checks as proof certification

`CLAIMS_EVIDENCE.md` C1--C3 still say “Certified proof replay,” and C5 says
“Certified with evidence firewall.” This conflicts with the file's own
correct statement that every infinite theorem remains proof-owned. An audit
can certify that expected fields/checks passed; it cannot certify an
infinite mathematical proof.

**Minimum fix:** use a non-epistemic audit status, for example:

> Proof-contract checks replayed with PASS; finite diagnostics make no
> theorem inference. The infinite claim is established only by the analytic
> manuscript proof.

Likewise replace “matching obstruction certified” in the high-level table
with “proof audit records the matching-obstruction check as PASS.” “Certified
implementation replay” is acceptable only when it unmistakably refers to
the implementation, not theorem correctness; “exact implementation replay
matched” is safer.

## Remaining Minor issues

### R-m1. Put the even interval in the theorem ledger or cross-reference it exactly

The section plan now has the formula, but theorem item 6 still says only
“an explicit finite interval.” Either display `b_i,L,U` there or write
“the interval `(L(q),U(q))` defined in Theorem X.” Add that it may be empty
and optionally record `max(0,U-L-1)` for the unrestricted count.

### R-m2. The figure-plan row still says “an impossible cross-valuation edge”

The revised hero caption no longer makes this mistake, but the table row
does. Specify a crossed-out candidate pair/non-edge so the visual cannot be
read as contradicting valuation preservation.

### R-m3. Make the weighted-Hankel distinction explicit in Section 2 or 3

The Related Work boundaries are good, but add one sentence that for `s!=0`
the entries are not a function of `m+n` alone: the object is a diagonal
Dirichlet weighting of powers-of-two Hankel support. This prevents Peller's
classical setting from being read as a direct proof of the sharp walls.

## Recheck release rule

A minimal second patch can reach `PLAN_READY`; no new experiment, source, or
proof package is required. The next same-reviewer check needs only verify:

1. finite-compression versus bounded-operator phase domains;
2. local `log det_2` branch/disk and a main-text product proof sketch;
3. an explicit Conclusion allocation;
4. removal of theorem-certifying audit language.

All four must be resolved with zero new Critical/Major findings.
