# Claim ledger — 403 affine full-torus admission

Candidate ID: `ANG-AUDIT-20260922-ATA01`.  
Batch: `NONLINEAR-RETURN-20260922-K`, round 4/5, 2026-09-22.  
Outcome: `AFFINE PERIODIC ADMISSION ESTABLISHED; NONEMPTY PRIME-UNIQUE LEDGER STOP`

Input: [frozen card](candidate-card.md), original 74 lines SHA-256 `798ef503ad37a6204ab611af6ddea3263f10fffb7e426eefe560be2e54e6a380`. Full proof: [paper](paper.md); overview and mechanical checks: [README](README.md). Every substantive result is rederived for the changed affine class.

| Claim | Evidence state | Exact proof and limit |
| --- | --- | --- |
| Full fibre and all inverses | ESTABLISHED degree d=abs(det A), all d solutions per actual base inverse | Paper §2, lattice/coset construction; no fibre subset replaces the carrier |
| Pointwise volume owner | ESTABLISHED local forward Jacobian d and inverse Jacobian 1/d everywhere | §2; flat fibre only, no volume on the arbitrary base or all Y |
| Borel inverse-sheet IMAGE | ESTABLISHED m(I_j E)=m(E)/d for every sheet and Borel E | §2 equation (3); every cut boundary assigned |
| All-sheet versus injective transport | ESTABLISHED all-preimage Haar law and full image-multiplicity identity | §2 equations (3)–(4); arbitrary source IMAGE is not d times its measure |
| Affine-prefix composition and step sums | ESTABLISHED exact ordered B_k, beta_k, Q_k and S_k=log Q_k | §2 equations (5)–(6); all finite legal prefixes and all inverse solutions |
| Actual cocycle and kernels | ESTABLISHED witness independence, full clock kernel Q_k=Q_l, lag kernel k=l, intersection both | §3 equation (7); nonunit and terminal-history arrows retained |
| Full periods and entire H | ESTABLISHED least base ell plus least fibre r gives least full period ell r and H=(r log Q)Z | §3 equation (8); applies to all incoming eventual-periodic points |
| Extension isotropy and phases | ESTABLISHED trivial for Q>1, source isotropy retained for Q=1; R/H per complete source orbit | §3; other source isotropy trivial, H={0}; all heights and repetitions retained |
| Affine periodic admission | ESTABLISHED iff pi(beta) torsion in T^n/(I−B)T^n | §4 Theorem 1; finite-grid proof without a fixed centre or spectral restriction |
| Fixed centres and periodic degeneracies | ESTABLISHED fixed iff pi(beta)=0; exact fixed/least-period sets given | §4 equation (9); empty, finite and continuum fixed sets distinguished |
| Nonempty prime-unique ledger | IMPOSSIBLE in the frozen architecture | §5 Theorem 2; prime-only forces Q prime/r=1, then full (Q+1)-torsion witness violates length or uniqueness |
| Q=1 and no-periodic-fibre cases | NO positive packets from these cases | §§3–5; empty positive ledger remains vacuous, not prime coverage |
| S control | ESTABLISHED full rational/eventual criterion, fixed/exact-two sets and every least-period packet predicate | §§6–7; shifted doubling still supplies a composite primitive multiplier |
| R control | ESTABLISHED full rational/eventual criterion, even least periods and entire exact-two set | §§6–7; no fixed point, continuum composite-time packets |
| I control | ESTABLISHED all points non-eventually-periodic; fixed/exact-two sets empty | §§6–7; positive ledger empty while all inverse and kernel arrows remain |
| Control kernels / incoming / heights | ESTABLISHED complete dyadic merger kernels, all inverse sheets, isotropy and full H | §§6–7 equation (10); extension isotropy trivial everywhere, equal times do not merge packets |
| Arithmetic naturalness / lineage admission | NOT ESTABLISHED | No concrete arithmetic base supplied; controls use assigned coefficients |
| Nonlinear/feedback owners, novelty, RH | NOT CLAIMED | Outside the frozen affine, fibre-independent base-permission scope |

## Gates and decision

Conditional T0 verifies same-object fibre, inverse and actual-history ownership. T1 establishes its geometric clock, not an endogenous prime mechanism. T2 establishes the periodic-admission equivalence and the nonempty-ledger obstruction with complete controls. Classical NOT APPLICABLE; T3 NOT AUDITED; formal UNASSIGNED; Route B NOT INVOKED.

Decision: STOP a nonempty prime-only, unique-per-prime ledger claim for this architecture, retaining the exact affine admission criterion. The adverse Q=1, no-periodic-fibre and empty-ledger cases remain explicit. A changed nonlinear fibre or geometry-dependent permission rule needs a fresh frozen owner; no theorem or Route credit transfers automatically.

## Evidence and workflow limits

All methods are exact; no finite census is promoted to an infinite assertion. Mechanical hash/line/ID/Outcome/link checks concern file integrity. No target data, external reference, scientific numerics, PDF, Git mutation or external publication is used. Author helpers used only the same card or bounded lemma statements; no new main/raw/peer material was read. Helpers are not independent reviewers; shared-history internal work is NOT_CALIBRATED. ARS bounded claim/evidence discipline applies. Card integration and CP2/CP3 remain root-owned.
