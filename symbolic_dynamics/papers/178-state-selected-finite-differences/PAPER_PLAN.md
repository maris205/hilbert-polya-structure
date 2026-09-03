# P178 paper plan — state-selected finite differences

**Working title:** *State-Selected Finite Differences: Complete Fibres and
Jordan Blocks*  
**Type:** finite algebraic dynamics / enumerative proof note  
**Format:** anonymous deterministic `amsart`, A4, 10pt  
**Round:** Round 2 dual-review freeze  
**Settled target length:** 3 pages including references  
**External state:** `OWNER_THIN / HOLD_EXTERNAL`

## One-sentence contribution

The nonlinear map
\(f\mapsto(x\mapsto f(x+f(0))-f(x))\) on all
\(\mathbb F_p\)-valued functions has a complete image, fibre, depth, and
transition-Jordan atlas because each nonzero state-selected direction has a
unique reverse lift after anchoring at zero.

## Claims–evidence matrix

| Claim | Proof evidence | Exact pressure | Manuscript location |
|---|---|---|---|
| cyclic-difference flag has dimensions \(p-t\) | binomial basis and Pascal identity | modular ranks through \(p=19\) | equations (8)–(9), Section 2 |
| nonzero directions advance one flag layer | \(D_a=N U_a(N)\), \(U_a(0)=a\ne0\) | every nonzero \(a\) and layer through \(p=19\) | Lemma 2 |
| anchor gives one reverse lift | constant kernel plus evaluation at zero | direct direction-word census for \(p=2,3,5\); anchor ranks through \(p=19\) | Lemma 2, equation (10) |
| complete image tower and every-time fibres | unique lift for each nonzero direction word; mass conservation at zero | every state, target, and time for \(p=2,3,5\) | Theorem 1(i)–(ii), Section 2 |
| sharp rooted graph and depth shells | explicit binomial-basis witness; consecutive zero-fibre differences | all literal depths and indegrees for \(p=2,3,5\) | Theorem 1(iii), Section 3 |
| complete transition spectrum and Jordan blocks | rank-one recurrent projection plus nilpotent rank second differences | predicted block ranks at all checked primes | Theorem 1(iv), Section 3 |
| owner boundary is narrow | primary finite-difference and linear-FDS sources; A05/P164 subtraction | exact-literal bounded search log | Sections 1 and 4; `SOURCE_VERIFICATION.md` |

## Section and page budget

| Component | Content | Budget |
|---|---|---:|
| Title and abstract | literal map, strongest counts, owner boundary | 0.35 page |
| Section 1: feedback map and theorem | notation, literal distinction, full theorem | 0.80 page |
| Section 2: difference flag and anchored lifting | binomial basis, unit factor, inverse words, sharp witness | 0.85 page |
| Section 3: rooted graph and transition operator | depth shells, projection split, complete Jordan census, \(p=2\) boundary | 0.55 page |
| Section 4: controls, ownership, and limits | author-side exact audit, external/internal subtraction, prime-field limit | 0.30 page |
| References | two verified owner-boundary records | 0.15 page |
| **Total** | complete proof-only note | **3.00 pages** |

No appendix is planned: every proof needed by the theorem remains in the
main text.

## Section blueprint

### Abstract

- Open with the literal update.
- State the \(p\)-step clock and \(p^{p-t}\) image staircase.
- Give the nonzero fibre and full zero-Jordan multiplicities.
- End with exact zero-credit background and `HOLD_EXTERNAL`.

### 1. The feedback map and theorem

- Define \(\tau_a,D_a,N,J^t\) before the theorem.
- Explain why selecting \(f(0)\) at every epoch is not a fixed linear map.
- State the full temporal, inverse, graph, and operator result.
- Cite only verified background sources actually used.

### 2. The difference flag and anchored lifting

- Construct the binomial basis and prove the one-block difference flag.
- Isolate the unit factor \(D_a=N U_a(N)\).
- Prove the constant-kernel/zero-anchor lifting lemma.
- Count nonzero fibres by direction words and zero fibres by mass.
- Give the explicit sharp witness.

### 3. The rooted graph and transition operator

- Obtain immediate indegrees and depth shells.
- Split the transition operator using \(E=P^p\).
- Convert nilpotent ranks to exact block multiplicities.
- Display the \(p=2\) sentinel.

### 4. Exact controls, ownership, and limits

- Describe the direct-tuple exhaustive and modular-matrix author audit passes.
- Separate computation from proof.
- Subtract Aichinger–Moosbauer, linear-FDS background, A05, and P164.
- State the prime-field limitation and bounded-search semantics.

## Figure and table decision

Figure phase is complete with **Figure N/A**. The map's functional graph is
already specified by exact level and indegree formulas, so a generic rooted
tree would discard labels and communicate less than the theorem. No table is
needed; the \(p=2\) boundary fits in one remark. See `FIGURE_PLAN.md`.

## Citation plan

- Sections 1 and 4: Aichinger–Moosbauer for translation differences,
  augmentation powers, and functional-degree context.
- Sections 1 and 4: Hernández Toledo for fixed linear finite dynamical systems and
  nilpotent/bijective decomposition.
- No citation appears unless its primary record and claim use are logged in
  `SOURCE_VERIFICATION.md`.

## Author and Review-A gate

- [x] frozen theorem and dependency chain
- [x] claims–evidence matrix and page budget
- [x] no-figure phase documented
- [x] anonymous full LaTeX draft
- [x] standalone exact verifier
- [x] settled deterministic PDF and frozen Round-0 copy
- [x] final visual, citation, anonymity, and hash checks

The subsequent hostile review found only an evidence-provenance wording
issue.  That documentation repair is recorded in `IMPROVEMENT_LOG.md`; the
theorem source and PDF bytes are unchanged.
