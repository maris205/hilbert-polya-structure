# 403 — Affine full-torus admission audit

Candidate ID: `ANG-AUDIT-20260922-ATA01`.  
Batch: `NONLINEAR-RETURN-20260922-K`, round 4/5, 2026-09-22.  
Outcome: `AFFINE PERIODIC ADMISSION ESTABLISHED; NONEMPTY PRIME-UNIQUE LEDGER STOP`

[Paper](paper.md) contains the exact proofs; [frozen card](candidate-card.md) specifies the complete owner; [claim ledger](claim-ledger.md) records the boundaries. This changed affine class is rederived independently, not credited with a predecessor's result.

## Two exact results

For affine monodromy `g(v)=Bv+beta` on the FULL torus, with nonsingular integer B, let `pi:T^n→T^n/(I−B)T^n`. Then g has a periodic point **exactly when pi(beta) is torsion**. The proof translates the shift to a torsion vector and uses an invariant finite torsion grid; it does not assume a fixed centre or an expanding spectrum. Fixed points require the stronger condition pi(beta)=0. Exact fixed/least-period predicates retain all finite and continuous degeneracies.

For a least base cycle of length ell, put Q=abs(det B). A least-r fibre cycle gives least full source period ell r and complete physical H=(r log Q)Z. If Q>1, its primitive multiplier is Q^r. Prime-only lengths would therefore force Q prime and r=1. Once a fixed point is established, the full translated (Q+1)-torsion grid supplies either another fixed packet at that prime or a longer cycle with composite multiplier. Thus a **nonempty** positive ledger cannot satisfy both prime-only primitive lengths and at most one packet per prime.

Q=1 contributes no positive period. Q>1 with no periodic fibre also contributes none. An empty ledger can satisfy the two conditions vacuously, but supplies no prime coverage. The torsion grid is a witness retained within the full carrier, never a selected replacement for it.

## Ownership and complete controls

Every actual fibre inverse and every base history is retained. A degree-d affine map has local forward Jacobian d and inverse-sheet IMAGE `m(I_j E)=m(E)/d`, whereas summing all sheets gives `m(F^(-1)E)=m(E)`. These distinct transport laws do not define interchangeable clocks. No base probability or smooth volume on all Y is supplied. General clock/lag kernels are given by full common-tail equalities and determinant-product conditions; they can contain nonunit arrows.

| Own full-carrier control | Complete periodic result | Physical consequence |
| --- | --- | --- |
| S: circle `2x+sqrt2` | After translation, periodic coordinates have odd rational denominator; eventual periodicity means rational. One fixed point and one exact-two cycle | One log-2 packet, but also a primitive log-4 packet and all exact-period families |
| R: T² `(2x,y+1/2)` | Eventual periodicity means rational x; least period is lcm(odd-denominator doubling period,2). No fixed points; exact-two set `{0,1/3,2/3}×T` | All primitive multipliers are composite; continuum many distinct packets at each occurring even period |
| I: T² `(2x,y+sqrt2)` | No periodic or eventually periodic point; fixed/exact-two sets empty | H={0} everywhere; positive ledger empty, not prime coverage |

All three own Haar measure, every inverse sheet and tau=log 2. Their clock kernel, lag kernel and intersection coincide with the complete dyadic merger relation (with equal second coordinate for R/I), not just units. Extension isotropy is trivial everywhere. The paper gives all source isotropy, entire H, incoming, real phases and repetitions; equal times never merge packets.

## Decision and scope

STOP the nonempty prime-unique ledger claim within this full affine-fibre architecture; retain the periodic-admission criterion. Conditional T0–T2 ownership and audit results are established, not arithmetic naturalness or candidate admission. Classical NOT APPLICABLE; T3 NOT AUDITED; formal UNASSIGNED; Route B NOT INVOKED. Nonlinear fibres and geometry-dependent base permission are outside the result. No novelty, operator or RH claim is made.

## Reproducibility and exposure

Frozen 74-line card SHA-256: `798ef503ad37a6204ab611af6ddea3263f10fffb7e426eefe560be2e54e6a380`. All proofs use exact flat-volume, lattice, affine and finite-grid arguments; no scientific numerical census, cutoff, fitting, prime/zero data, external source, PDF, Git mutation or publication is used.

Mechanical checks: `head -n 74 candidate-card.md | sha256sum`, `wc -l paper.md`, and local Node reads verifying IDs, identical Outcome strings and relative links. These establish file consistency, not theorem validity. The author read the complete card and instructions, not other new main/raw/peer material. Same-card and lemma-only helper work is author assistance, not independent review. Internal work is shared-history NOT_CALIBRATED; ARS claim discipline is disclosed in the paper. Root owns card integration and CP2/CP3; author completion does not declare those gates complete.
