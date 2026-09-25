# Claim ledger — 423

Candidate ID: `ANG-AUDIT-20260923-FSC01`  
Date / type: 2026-09-23; fixed-stride conditional audit.  
Outcome: `FIXED-STRIDE PACKET TRANSPORT ESTABLISHED; RATIONAL PRIME-UNIQUE LEDGER STOP`

Input: [card](candidate-card.md), first83 lines, SHA-256 `67af700efafe77b4c26c969239019b23008f6f4a4b4dfaa3d5fd76cd2faa0ee1`. Proof: [paper](paper.md); handoff: [README](README.md). Parent T is TOTAL, stride k>=2 is fixed uniformly, and R keeps all X and mu.

| Claim | Evidence | Status / exact boundary |
| --- | --- | --- |
| FSC-01: R owns full Borel IMAGE inverse-chain product and integrated S^T_k clock | §4.1, Borel substitution | ESTABLISHED; all-point versions prescribed, no clock averaging |
| FSC-02: every incoming inverse word retained for each owner | §§3–4.1 | ESTABLISHED; R depth a is parent depth ka, no discarded source |
| FSC-03: both actual cocycles descend and are additive | §4.2 | ESTABLISHED; equal triples identified, integer lag retained |
| FSC-04: Psi(z,l,w)=(z,kl,w) injective with EXACT image parent lag in k Z and same clock | §4.2 | ESTABLISHED; totalness required, proper image if X nonempty |
| FSC-05: complete lag/clock/joint kernels and exact image identities | §4.3 | ESTABLISHED; nonunit lag-zero coalescences retained |
| FSC-06: parent eventual isotropy q Z, H=C Z; height phases R/H and zero-C ineffective isotropy | §5.1 | ESTABLISHED; signed/zero permitted, non-eventual H=0 retained |
| FSC-07: d=gcd(q,k) sampled packets with least q/d and ENTIRE H=((k/d)C) Z | §5.2 | ESTABLISHED; full eta-residue basin assignment, all incoming and reference invariance |
| FSC-08: every non-eventual parent packet splits into EXACTLY k sampled packets | §5.3 | ESTABLISHED; complete residue labels, kernels, all real phases, no coalescence loss |
| FSC-09: rational M>1 and M^a=p force a=1 and M=p | §5.4, coprime integer argument | ESTABLISHED; no corresponding irrational claim |
| FSC-10: under rational condition on EVERY nonzero parent cycle, joint nonempty prime-only unique target impossible | §5.4 | STOP; prime case forces k duplicates, no nonzero parent gives empty positive ledger |
| FSC-11: full A one log 3 -> one primitive log 9 | §6, independently measured parent/sample | Prime-only STOP; every nonzero source and phase retained |
| FSC-12: full B one least-3 log 2 -> three fixed log 2 packets | §6 | Uniqueness STOP; no label quotient |
| FSC-13: full C irrational sqrt(3) parent -> one log 3 sampled packet | §6 | Necessary target holds outside rational class; no arithmetic admission/all-prime claim |
| FSC-14: endogenous prime source, general acceleration no-go, operator or formal Route | No such construction/evaluation | NOT CLAIMED; arithmetic T1 NOT PASSED; T3 NOT AUDITED |

## Gates and decision

T0 CONDITIONAL FULL OWNERS / EXACT LAG IMAGE ESTABLISHED. OWN COMPOSED IMAGE CLOCK COMPONENT ESTABLISHED, explicitly ARITHMETIC T1 NOT PASSED. T2 COMPLETE CONDITIONAL PACKET SPLITTING / H / PHASES ESTABLISHED; rational k>=2 target STOP. Classical A0–A2 NOT APPLICABLE, formal UNASSIGNED, Route B NOT INVOKED.
Controls separate clock multiplication, primitive versus repetition, full packet splitting and the irrational-parent boundary; signed/zero sums are covered by the theorem. No arithmetic source exists for label randomization. PROVES_TOO_MUCH is bounded by C; strong naturalness remains OPEN. Future FORK requires fresh frozen assumptions, not deleting packets or dividing the clock. No new candidate is started.

## Evidence and integrity limits

Exact proofs; no scientific numerical run/code, finite cutoff/precision extrapolation, orbit census, literature/API, Git, PDF or publication. `sed`, `wc -l`, `sha256sum`, local-link and ID/Outcome checks concern artifacts only. Root owns card append and later CP2/CP3; author surfaces do not certify those gates.
Named AI author/helper tasks and access receipts are in the paper, including the declared pre-freeze 409/413 collision reads. No post-release reviewer/raw/peer or sibling manuscript inputs. Shared-history NOT_CALIBRATED; AI derivation/drafting/internal checking disclosed, no human/external verification certified. ARS bounded claim/evidence discipline, `criteria_binding_unavailable`, no venue readiness. Human authorship/funding/conflict declarations remain UNKNOWN where unsupplied.
