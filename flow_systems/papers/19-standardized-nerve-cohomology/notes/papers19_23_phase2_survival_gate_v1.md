# Papers 19--23 Phase-2 source and survival gate v1

Date: **2026-08-24 (Asia/Shanghai)**

Status: **PHASE 2 COMPLETE — TWO LIVE RESEARCH LANES, THREE MERGE/NOTE DISPOSITIONS**

User authority consumed by this gate: bounded Phase-2 bibliography, source
verification, nearest-prior subtraction, owner correction, and feasibility
screening for the five frozen slots.  This gate does not authorize Phase-3
proof work, manuscript composition, Route advancement, submission, release,
or Git action.

Post-gate receipt: the user subsequently and explicitly confirmed continuation
into the bounded Phase-3 proof round.  The resulting proof/Route gate is
[`papers19_23_phase3_proof_route_gate_v1.md`](papers19_23_phase3_proof_route_gate_v1.md).

## 1. Search and evidence policy

All five screens used the ARS deep-research/source-verification workflow:

1. record search date, surfaces, exact query families, and inclusion/
   exclusion criteria;
2. prefer primary papers, official full text, authoritative monographs, and
   maintained mathematical references;
3. inspect theorem statements and nearby proof text rather than infer from a
   title or abstract;
4. separate exact-owner evidence from adjacent precedents;
5. treat zero search hits as bounded search silence, not a novelty theorem;
6. retain conditional hypotheses, owner boundaries, and Route nonclaims.

The project-level reports are:

- [P19 source/routine screen](phase2_source_routine_screen.md);
- [P20 arithmetic/source screen](../../20-wieferich-ulm-separation/notes/phase2_arithmetic_source_screen.md);
- [P21 effective-Chebotarev screen](../../21-effective-exact-order-witnesses/notes/phase2_effective_chebotarev_screen.md);
- [P22 source/site screen](../../22-fppf-verschiebung-lifts/notes/phase2_source_site_screen.md);
- [P23 trace-weight screen](../../23-normal-trace-return-erasure/notes/phase2_trace_weight_source_screen.md).

## 2. Portfolio outcome

| Slot | Phase-2 mathematical result | Standalone disposition | Binding next gate |
|---|---|---|---|
| P19 | conditional on the exact author-complex comparison, `H^0=R^Q`, `H^1=R^Q`, and `H^n=0` for every `n>=2`; unnormalized degeneracies add no classes | **MERGE INTO P12** | exact author-complex/cup/`J*` proof before any theorem amendment |
| P20 | every fixed finite `kappa` pattern has an exact product relative-prime density; every fixed finite projection has positive-density infinite fibres | **MERGE INTO P15 / TECHNICAL COROLLARY** | obtain the 2023 near-neighbor full text before any novelty sentence |
| P21 | exact-condition density `(r-1)/r^(m+1)`; selected-class density `r^(-(m+1))`; correct unconditional and ERH/GRH black-box least-prime bounds | **LIVE, REVISE** | compute relative Artin conductors for `E/Q(zeta_r)` and prove a genuine improvement |
| P22 | exact Deninger fppf owner recovered; first obstruction is `u_*e=V_N^*e` in sheaf `Ext^1` | **LIVE, REVISE** | compute the actual kernel/extension and decide `N=2` |
| P23 | all normal semifinite tracial weights are central-density weights; full circle-translation invariance selects a scalar Haar weight (FNS at positive scale) and implies nonzero-return erasure | **TECHNICAL NOTE / PREFER MERGE INTO P8** | converse needs extra common-domain hypotheses; no packet transfer |

This is not a failure of the five-project search.  It is the intended
selection outcome: three projects were stopped from becoming inflated
standalone papers before composition cost was incurred.

## 3. Exact theorem-shape receipts

### P19

For

```text
G_std = coproduct_(q in Q) ((R/LZ) rtimes R),
```

transitive reduction, `cd(Z)=1`, exactness of arbitrary products, and the
normalized/unnormalized comparison would yield

```text
H_cnv^n(G_std;R) ~= product_(q in Q) H^n(Z;R).
```

The exact comparison to the author-defined complex, the cup convention, and
higher `J*` remain local proof tasks.  The conditional conclusion is useful
closure for P12 but is too close to classical theory for a separate P19
manuscript.

### P20

For fixed finite prime-coordinate set `S` and fixed
`a in N_0^S`, the primes outside `S` with `kappa_r(p)=a_r` for every `r in S`
have relative prime density

```text
product_(r in S) delta_r(a_r),

delta_2(k)=2^(-(k+1)),
delta_r(k)=(r-1)/r^(k+1)       for odd r.
```

The odd local class count is prior art in Keller--Richstein; CRT and
fixed-modulus PNT-AP supply the product.  The exact Paper-15 packaging is a
technical corollary.  It proves every fixed finite projection noninjective,
not that every conceivable finite symbolic proof of global injectivity is
impossible.

### P21

For

```text
E=Q(zeta_(r^(m+1)),p^(1/r)),
n=[E:Q]=r^(m+1)(r-1),
```

each admissible cyclotomic component gives one target class of density
`r^(-(m+1))`.  Their disjoint union has exact-condition density
`(r-1)/r^(m+1)` (also `2^(-(m+1))` when `r=2`).  A single selected class is
enough for the least-prime bounds.  With

```text
B=n((m+2)log r+2log p),
```

verified general theorems give

```text
ell <= exp(310B)                         unconditionally,
ell <= (4B+2.5n+5)^2                     under the stated ERH/GRH.
```

These are correct but generic.  Standalone survival depends on replacing the
full-discriminant input by an explicitly computed relative conductor for
`E/Q(zeta_r)`.

### P22

On a fixed small absolute `NoethAffSch_fppf`, write

```text
e: 0 -> K -> underline Z(O)^sharp -> W_rat(O)^sharp -> 0.
```

An additive lift inducing `u:K->K` exists exactly when

```text
u_*e = V_N^*e                 in Ext^1(W_rat(O)^sharp,K).
```

This is the correct general precheck, not the missing arithmetic solution.
The first nontrivial proof test is `N=2`; if the actual `K,e,V_2^*e` remain
uncomputed, the project stops.

### P23

For

```text
M=L^infinity(T,m) bar-tensor B(H),
```

every normal semifinite tracial weight is

```text
psi_h(x)=integral h(theta)Tr(x(theta))dm(theta).
```

Invariance under all center translations is equivalent to `h` being a.e.
constant, hence to a scalar multiple of the Haar trace (FNS at positive
scale).  Paper 8's frozen Fourier formula then erases every nonzero return.
The reverse implication is not claimed for arbitrary semifinite weights
without additional common-domain hypotheses.  The classification is
classical; the exact P8 corollary is a short note, not an independent full
paper.

## 4. Fast Phase-3 order, if separately authorized

The speed-optimal proof order is:

1. **P21 conductor kill test:** compute local conductors at `p,r`; continue
   only if the relative bound genuinely improves the black box.
2. **P22 `N=2` kernel/extension reconnaissance in parallel:** continue only
   if `K,e,V_2^*e` can be computed, not merely named.
3. **P23 short proof package:** only if a technical note is desired; otherwise
   queue it as a P8 amendment.
4. **P19 and P20 merge packets:** preserve the exact results for future P12/
   P15 revisions; do not reopen those manuscripts silently.

P21 has the fastest quantitative theorem test.  P22 has the largest novelty
upside but also the higher algebraic risk.

## 5. Route and publication boundary

No project acquired a dynamics/clock/orbit/determinant tuple or a single
Hilbert-space/operator/domain owner.  The Route-A/Route-B conclusions in the
Phase-1 lock remain unchanged.  None of these Phase-2 results authorizes a
manuscript, runtime claim, publication, or release.

```text
PHASE2_BOUNDED_SOURCE_SCREEN=COMPLETE
P20_MAXIMUM_PRIOR=INCOMPLETE_2023_FULL_TEXT_REQUIRED
P19_EXACT_AUTHOR_COMPLEX_THEOREM=PARTIAL
P23_RETURN_ERASURE_CONVERSE=NOT_PROVED
LIVE_STANDALONE_CANDIDATES=P21,P22
MERGE_OR_TECHNICAL_NOTE=P19,P20,P23
FIVE_STANDALONE_MANUSCRIPTS=FALSE
PHASE3_PROOF_AUTHORITY=GRANTED_SUBSEQUENTLY_AND_CONSUMED
ROUTE_ADVANCEMENT=NONE
```
