# 407 final internal review — CP2 and CP3

Candidate `ANG-20260923-DPR01`; batch `NONLINEAR-PACKET-20260923-L`, round 3/5.
Verdict: **CP2 PASS / CP3 PASS** for the bounded frozen-owner claims below; no required correction identified.
Outcome: **OWNED REASSEMBLY CLOCK; COMPOSITE FIXED PRIMITIVES — STOP / FORK**.
This is shared-history, inherited-model, internal **NOT_CALIBRATED** review, not blind or external peer review.

## Exact final surfaces and access

- Paper: `paper.md`, 267 lines, SHA256 `73b9efc026c43bf04a3bbddb605ff8e0a22f3be379ada616be2d552c5aa2995f`.
- Card: `candidate-card.md`, 116 lines, SHA256 `c14220823efbb9f99170b88900d15e919ffb3474716637636034fbc8882d4c4c`.
- README: `README.md`, 39 lines, SHA256 `85d183455558e5cf7295c7c2fe22307277ac1e8bc8f2a7d5c63c912813d164ca`.
- Ledger: `claim-ledger.md`, 31 lines, SHA256 `23c993f4e52b1a19443e1a33445dc16002f31a812525ed8c550acda703280234`.
- Frozen CP1: `scope-review.md`, 56 lines, SHA256 `ba0b1daa99dd6cb23b93b1a88ae24cf99ecfee449e9503a3d7766cf062a7b6ad`.
- Frozen raw: `independent-review-raw.md`, 255 lines, SHA256 `0098a53949485fcecd423fdcd372b6f455d81125200ef7766c16115447671592`.
- Original Card prefix, lines 1–105: SHA256 `52ad8cc8d271c49317cf7245aed09ef3d421d2245b3b091c0f6c5054c96b25a1`.

After root's separate PAPER UNLOCK, I read all four final surfaces completely through their actual EOFs and compared the complete frozen raw and CP1, both also reread through EOF.
Card lines 106–116 are the later outcome appendix, not an input to the already frozen card-only raw proof; the original 105-line prefix remains unchanged.
No other new scientific package, peer report, author-helper proof, or external source was read. Retained earlier task context and fully read ARS/stream instructions are disclosed, not treated as DPR01 evidence.
No scientific code, numerical experiment, auxiliary delegation, higher-period census, new carrier, or parameter change was used. Only this final evidence file is written.
ARS reviewer guidance informed the owner-by-owner checks, proof-versus-status separation, and exposure disclosure; no score or forced-defect quota was applied.

## CP2 — complete owners, measured clocks, and actual arrows

1. The full carrier remains `N_0×[0,1]²` with counting-times-area measure. The priorities at n=0, x=1, y=1, r=0 and illegal divisibility states are consistent. Terminals retain identities and actual incoming, not forward self-loops; s=0 is legal.
2. The own source cells (2) partition every legal domain. Each target rectangle is exactly `{m}×(0,1)×[1−1/d,1)`, with m=d+e for T/L/G and m=n for H. Formula (3) recovers both assigned floor digits and all own permissions, proving inverse completeness without a cutoff.
3. G keeps every n,d with q=floor(n/d), rather than being restricted to n=dq. H enumerates all d dividing its target memory and every e=1,…,q. L uses r=u. No control borrows MAIN's domain or derivative.
4. Independent differentiation confirms J_T=J_H=q^(−3)u^(1/q−1), J_L=q^(−2), and J_G=d/(nq²)u^(1/q−1). Each is positive finite at every actual inverse point; the analytic extension fixes lower-face values without deleting null states.
5. The actual memory branch is a singleton counting bijection, contributing factor one. Change of variables on the real analytic inverse proves (5) for every Borel subset of its half-open domain, not merely an almost-everywhere density statement.
6. The additional forward-image formulas are valid: each restricted forward image `F(A∩B_α)={z∈E_α:I_αz∈A}` is Borel; their countable union is `{N_A>0}`. Its measure counts a union once, whereas nonnegative summation gives `∫N_A=∫_A exp(κ)`. Overlapping target branches are not incorrectly treated as disjoint.
7. All signed step clocks in (7) and the stated zero-step loci follow from those own Jacobians. For G with q=1, zero requires n=d; for q>1 the stated root lies strictly in (0,1). Zero steps are not equated with zero cycle clocks.
8. Actual retained-lag triples, not inverse words, define the groupoid. Two witnesses for one triple differ by a common legal tail, so the clock descends. Composable histories align at the longer legal middle history without iterating beyond a terminal. The claimed finite-chart IMAGE ratios follow by chain rule.
9. Equations (9) give the full clock kernel, lag kernel, and intersection with their actual-meeting conditions; no converse is inferred from an isolated product equality. Distinct H branches with the same d,q and different e correctly demonstrate nonunit arrows in both kernels.
10. Nonzero source isotropy is exactly eventual repetition of a full state. Least source period k gives source isotropy kZ, entire H=ΛZ, and extension isotropy `{jk:jΛ=0}`. Non-eventually-periodic and terminal-ending histories have no nonzero isotropy. The physical object is the orbit SET of the full real extension, not a claimed smooth or measured suspension.

## CP2 — independent check of the author's additional cycle identity

For T/H/G, substituting `x=(d−1+r)/n` and `x_next=r^q` into (11) gives
`B·x_next/x=(nq²/d)r^(q−1)`, which equals the OWN step multiplier in all three cases.
This calculation does not assume n=dq for G. Positivity of x follows from every legal source condition, so the coordinate ratio telescopes on every legal history and cancels on every actual cycle.
Since r∈(0,1), `B=(q²/d)(1+(d−1)/r)≥q²≥1`; equality with one occurs exactly when d=q=1.
For T this implies n=dq=1; for G it implies n=q=floor(n/1)=1. Their next memory is d+e=2, excluding a cycle whose every factor equals one.
Thus every actual T/G cycle has positive clock. For L, zero cycle clock requires every q=1, but then n_next=n+1 at each step, also impossible on a cycle.
For H, equality at every step forces n=d=q=e=1; its legal map is the identity on exactly `U={(1,x,y):0<x<1,0≤y<1}`. Conversely every point of U is a zero-clock fixed core.
Hence H's zero-CYCLE cores are exactly U. This does not say that every point with H=0 lies in U: non-eventually-periodic points still have H=0 by (10).
These statements are direct identities and an equality-case argument, not a higher-period existence theorem or census. They extend the raw's conditional cycle ledger without changing its frozen content or scope.

## CP2 — full fixed sets, incoming, and physical packets

11. MAIN's register equation dq=d+e leaves exactly d=1,q≥2,e=q−1 or d=q=e=2. Solving its real equations gives precisely (13), including the full t interval and legal lower faces. Its clocks are 2log q and log(1+sqrt(17)), as independently obtained in the raw.
12. L's own first fixed equation rejects the d=1 alternative through r=0 and leaves exactly `(4,1/3,t)`, 1/2≤t<1, with its own log4 clock.
13. G's independent integer cases are exhaustive: d=1; d≥2,e<d giving q=e=1; or d≥2,e≥d forcing d=q=e=2. The middle case requires forbidden y=1. Equality with MAIN's fixed set therefore does not erase any G branch or identify the full owners.
14. H's equations (18) retain n=dq without imposing n=d+e. For q=1 only U survives. For q≥2 the divided scalar equation has a strictly increasing left side and nonincreasing right side with opposite endpoint inequalities, proving its unique root in (0,1).
15. The second H equation excludes q<d, gives all allowed t when q=d, and gives exactly `1≤j≤floor(q/d)−1` when q>d. The latter range is nonempty exactly at q≥2d. Formula (21) is complete and retains every s=0 endpoint; its positive clocks satisfy (22). U keeps source and extension Z but no positive primitive.
16. At an arbitrary target the untruncated inverse atlas gives every incoming branch, including incoming to terminal cuts. At fixed targets (23) is complete; G's additional j=0,…,a−1 enumerates every n=ab+j with floor(n/a)=b. H uses all a dividing m and all e, not the MAIN target-register condition.
17. Formula (24) correctly includes all b≥1 and the unit-memory predecessor of MAIN's bad fixed core. Each H point in U has only itself as predecessor. Recursive incoming sets perform all intermediate domain tests; the stated union over forward and backward histories is the entire source orbit.
18. Every fixed basin has source isotropy Z and entire H=κ(f)Z by prefix cancellation; distinct fixed cores cannot have meeting constant futures. Incoming histories create no smaller generator and no extra packet.
19. The arrow for forward arrival F^a z=f is `(f,−a,z)`, with clock −S_a(z). Thus the fixed phase h−S_a and the cycle phase h+S_j(f_0)−S_a have the correct signs. All real phases, ineffective isotropy, and integer repetitions are retained.
20. Exact fixed-set parameterizations count all cores, including interval families and any equal-time H coincidences. No merging or selected representative is used. The author need not add a classification of higher cycles or the raw's separate cardinality notation to justify these complete fixed-window multiplicities.
21. MAIN's actual `(2,1/4,0)` has own inverse J=1/4, source isotropy Z, and entire H=(log4)Z. The primitive is therefore log4, not a selected repetition. Since 4 is not an ordinary prime, this MAIN packet alone decisively fails the frozen necessary target; no control or empty-window argument is substituted.

## CP3 — final surfaces, integrity, and stop boundary

Paper, Card outcome, README, and Ledger agree on candidate ID, batch/round, full owner, all three independent controls, complete fixed gate, and STOP / FORK outcome.
The generic cycle positivity and H zero-cycle-sheet claims on the Ledger are supported by the independently checked identity, and explicitly not advertised as a higher-period census.
The full incoming/phase claims are supported by the complete atlas and recursive source-orbit argument, not by a finite displayed sample. Null boundaries, unit sheets, terminal objects, and non-fixed remainder histories stay in the owner.
The lineage is the stated proper-divisor strip rule and geometric digit write-back. Strong naturalness and arbitrary-encoding risks remain OPEN; the result is not a conservative or symplectic realization.
T0 owner is established; T2's necessary MAIN target fails. T3 stays NOT AUDITED, classical fields NOT APPLICABLE, formal Route UNASSIGNED, and Route B NOT INVOKED. No invariant probability, trace/zeta/operator, spectrum, or all-prime coverage result is claimed.
The four surfaces consistently disclose AI derivation/drafting, shared-history internal review, prior design mental algebra, and the same-author helper's draft/card exposure. That helper is expressly not the independent reviewer. These are disclosure checks, not independent certification of another agent's private access log.
No human or external peer verification is implied. The card's outcome appendix is treated as post-proof status, not preregistered evidence. The frozen raw and CP1 remain byte-preserved.
Local Markdown targets among the four surfaces are present. Counts and whole-file hashes above bind the reviewed versions; the original Card prefix hash is separately unchanged.
No must-fix issue remains within the authorized contract. Portfolio **STOP / FORK** follows from MAIN's wrong positive primitive, with same-object ownership intact; no further science or new candidate is authorized by this review.

EOF — CP2 PASS / CP3 PASS for the bound final surfaces; final internal review frozen after full self-read, then HOLD for root integration.
