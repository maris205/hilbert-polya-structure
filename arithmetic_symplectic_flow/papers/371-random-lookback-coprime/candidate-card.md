# Frozen candidate — Random-lookback coprime conditional histories

Candidate `ANG-20260922-RLC01`; batch `MEASURED-HISTORY-20260922-E`, round2/5.
Date2026-09-22. Status `CONTRACT FROZEN; CONDITIONAL HISTORY OWNER OPEN`.

## 1. Full source, arithmetic interface and design constants

A={2,3,...}, X=A^N0 with all histories, coordinates recent to distant past,
discrete product topology/Borel. Freeze rho(a)=1/[a(a-1)],
Z(b)=sum_(a>=2,gcd(a,b)=1)rho(a), K_b(a)=rho(a)1_(gcd(a,b)=1)/Z(b).
Prove normalization/positive denominators. No prime alphabet or table.
For every x and every a prescribe

    q_a(x)=rho(a)/2 + (1/2)sum_(r>=1)2^-r K_(x_(r-1))(a).

The exact lineage is full-history common-divisor exclusion -> randomly
select one arbitrarily remote witness -> actual coprime conditional sampling
with explicit renewal/reset softening. Hard exclusion of367 is NOT retained:
this is a NEW probabilistic deformation, not a conjugacy or inherited theorem.
rho, reset1/2 and geometric lookback are fixed designs, not uniquely forced
by prime periods. Strong naturalness OPEN; no selected histories or roofs.

## 2. Explicit probability, not an unspecified stationary g-measure

On an auxiliary product noise space, at EACH integer t take independent
B_t in{0,1} fair, L_t>=1 with P(L_t=r)=2^-r, U_t uniform[0,1).
For a probability P on A define Q_P(u)=min{a>=2:sum_(j=2)^a P(j)>u}.
To define Y_t, follow decreasing ancestors: at s with B_s=1 go to s-L_s;
at B_s=0 stop, set Y_s=Q_rho(U_s), and recursively along the finite chain
set Y_v=Q_(K_(Y_(v-L_v)))(U_v). If the chain NEVER stops set Y_t=2.
This exception convention defines the noise output everywhere; prove its
probability and compatibility, do not silently omit it.
Freeze mu=Law(Y_0,Y_-1,Y_-2,...). Prove measurability, stationarity,
full support, atom status and the conditional law on the entire output past.
Noise variables construct mu ONLY; they are not an alternative physical
owner, extra arrows or retained dynamical coordinates later forgotten.
Source is ALL X, not just a conull output image; every null periodic and
exceptional history remains in X with the same all-point q prescription.

## 3. All actual branches, version, kernels and physical time

T is the full left shift. ALL inverse branches I_a(x)=ax have domain X
and image[a], for EVERY a>=2. Prove every-Borel IMAGE
mu(I_a E)=integral_E q_a(x)dmu(x), positive finite all-point versions,
their continuity/regularity, and consistency rather than fitting null cycles.
For u=a_0...a_(m-1), define
q_u(x)=product_(j<m)q_(a_j)(a_(j+1)...a_(m-1)x), q_empty=1.
All prefix replacements vx->ux have proposed IMAGE q_u(x)/q_v(x).
Actual G consists of triples(z,m-n,y), T^m z=T^n y, source y range z;
equal triples identified, lag kept. Put kappa(z)=-log q_(z_0)(Tz),
A_m=sum_(i<m)kappa(T^i z), c=A_m(z)-A_n(y).
Prove every history IMAGE, witness independence and composition. Retain ALL
X times R with arrows(y,h)->(z,h+c); time is height translation of its
orbit SET, no assumed manifold, invariant flow measure or external roof.
Determine FULL clock/lag kernels and intersection, ENTIRE source/extension
isotropy, H, all incoming/phase, primitive words up to rotation and repeats.
Give formulas for ALL constant and two-letter periodic words, not a finite
numerical sample. Fixed tests include2^infinity and(2,3)^infinity.

Target gate in this normalization: each positive primitive must have least
time log p for a prime p, with at most one packet per prime; coverage further
OPEN. Wrong time or duplicate prime packet stops promotion after completing
owner/control evidence. No reset/lag/rho retuning, selected subset or clock
rescaling. Explain any real nonproduct/infinite-memory property proved;
do not infer it merely from the noise construction or long-lookback notation.

## 4. Three own controls

Each reconstructs its OWN noise-output law, with full X, ALL prefix branches,
all-point q, actual lag, IMAGE, real extension and complete ledger as above.

ARITHMETIC-OFF: replace every K_b by rho, retain reset and lookback.
NEAREST-ONLY: retain coprime K and reset but set every L_t=1, giving
q_a^near(x)=rho(a)/2+K_(x_0)(a)/2; own never-reset convention2.
SHARED-DIVISOR: retain reset/lookback but replace K_b by
K_b^sh(a)=rho(a)1_(gcd(a,b)>1)/Z_sh(b),
Z_sh(b)=sum_(gcd(a,b)>1)rho(a). Prove these denominators independently.
For each: complete construction, full kernels/incoming/isotropy, general
periodic-word formula and constant/two-letter tests; do not import MAIN's
law or wrongly claim source-word length is physical time.

## 5. Provenance / scope

Definition scout read065 short card1–11 and369 card1–94 including outcome,
not their papers/proofs/reviews; it authored367 earlier. It supplied the
definitions without computations, IMAGE or cycle results. Root has prior
365–369 results and anticipates an arithmetic-softening/constant-history
test, not blind discovery. No claim before CP1 release. Targeted old-card
reads are not novelty evidence; no external literature or scientific numerics.
ARS CP1, separate raw derivation, CP2/CP3; shared-history NOT_CALIBRATED.
Classical A0/A1/A2 NOT APPLICABLE; T3 NOT AUDITED; formal UNASSIGNED;
B NOT INVOKED. Markdown only, no Git/external mutation, five rounds only.

EOF — complete output-history law and full conditional-prefix owner to audit.

## Appended outcome — original freeze preserved

Candidate `ANG-20260922-RLC01`; current status **STOP / FORK**.
A full-support stationary non-atomic law with genuinely infinite memory; every-Borel prefix IMAGE and continuous full-point clock.
The constant history 2^infinity is a primitive log4 packet, not a repeated log2 packet.
T0 and declared T1 established; T2 frozen prime-time target FAIL.
All primitive symbol necklaces, kernels, eventual-periodic isotropy, incoming histories and height phases are retained.
Strong naturalness OPEN; T3 NOT AUDITED; classical NOT APPLICABLE;
formal UNASSIGNED; B NOT INVOKED. See [paper](paper.md),
[claims](claim-ledger.md) and [review](evidence/review.md).
