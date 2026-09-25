# Independent internal review — integral braid residue owner

Candidate ID: ANG-20260920-BRF01.
Date: 2026-09-20.
Status: OWNED REFACTORIZATION CLOCK; COMPOSITE PRIMITIVES AND MISSING ODD-PRIME TIMES — STOP / FORK.

## 1. Scope, bindings and actual checkpoints

The ARS raw-card, manuscript-comparison and final adverse checkpoints
were completed for the exact full source, partial rule and retained-lag
owner. No old clock, periodic theorem or analytic result was transferred.
Only this report was written; no numerical run or external source
lookup was performed.

Exact SHA-256 bindings:

- Original version-1 candidate-card.md, read before the manuscript:
  c6a64634a95a0cbcae762b80450deeec84768a6ab84c450fd11a56ac3dddc3d0.
- Initial manuscript, fully read at checkpoint 2, 306 lines:
  afbe09586ffbbd5d5ef66c94077fc75a4b7590a6fcedc3ca633812637e49ac0f.
- Final manuscript, after targeted corrections, 307 lines:
  574c7c45d48ee1899c4e913fe697d4d5150932738ec219089cadfb7e988c1929.

The first decisive composite-packet finding and then the complete raw
branch/clock/periodic conclusions were sent before any 292 manuscript
access. The author independently drafted the paper. Its additional
odd-prime multiplicity corollary and exact FEEDBACK-OFF fixed-seed count
were explicitly checked at the manuscript stage, not misrepresented
as previously blind raw findings.

A bounded auxiliary received only the raw card to examine FEEDBACK-OFF
and UNIT-INDEX controls. Its conclusions arrived before the raw checkpoint
was completed and were checked against the formulas before integration.
It did not provide the main periodic classification or read the manuscript.
The main and auxiliary reviewers inherit the same model and shared
research context. This is not external peer review, cross-model checking,
formal verification or an independent-error guarantee.
The author's separate historical/scout comparisons were not independently
reaudited here; they do not support the exact proofs reviewed below.

## 2. Checkpoint 1 — raw branch and clock audit

Both three-letter matrix products have upper entries d=a+c, u,
and au at positions (1,2), (2,3), and (1,3). Thus the refactorization
identity is exact; it is not a global invariant of successive macrosteps.
Writing g=gcd(a,c), the two integrality tests are equivalent to
(d/g)|(b+j). Each root has exactly g admissible digits among d,
so the partial domain is clopen but neither empty nor full in that fibre.

For a target root (A,B,C), put U=A+C. Every actual predecessor has

    a=BC/U, c=BA/U, b=U-j, 0<=j<min(B,U),

with a,c positive integers. For each such branch, terminal seeds (v,w)
have unique source seeds (j+B(w-v),v). This is onto the entire target
fibre, with no recurrent restriction. Immediate T-predecessors exist
exactly when those outer ratios are integral. For example root (1,1,1)
has no T-predecessor, but its digit 1 is admissible; its digit 0
states are terminal. Partiality and non-surjectivity remain genuine.

The inverse seed map factors as the unimodular joint-Haar shear
(v,w)->(w-v,v), scaling the first coordinate by B, then translation.
Its Borel IMAGE factor is 1/B. Finite inverse prefixes therefore have
factor 1/D. A beta-to-alpha branch pair has J=D_beta/D_alpha and
c=log D_alpha-log D_beta, with the frozen sign.

Equal-lag presentations extend both prefixes by the same actual suffix;
its index cancels. Composition aligns the middle prefixes only to a
length already defined in the longer arrow, never beyond a terminal
point without evidence. Full inverse-branch charts give the Hausdorff
étale topology and a continuous cocycle on all points. Full support
also rules out a different continuous version confined to null points.
The real extension and translation retain every object and real phase.
No coarse Hausdorffness or embedded-circle theorem follows automatically.

## 3. Checkpoint 1 — full periodic and packet audit

The root sum changes by exactly j>=0, so every digit on any periodic
trajectory is zero. On the zero-digit integrality root domain I,
R(a,b,c)=(bc/d,d,ba/d) preserves I and satisfies R²=id.
Its fixed roots are exactly (a,2a,a); all other roots in I have
least root period two. Moreover b,d>=2 on I.

It remains necessary to exclude seed periods larger than root periods.
The zero-digit inverse seed matrix is B_d=[[-d,d],[1,0]]. Over two
steps P=B_d B_b has trace db+d+b and determinant db. Its characteristic
polynomial is positive at 0 and negative at 1, with positive leading
coefficient, so its roots lie in (0,1) and (1,infinity).
No positive power has eigenvalue one. A putative full period m also
gives period 2m and (P^m-I)v=0. Its nonzero integer determinant and
adjugate, together with integer-multiplication injectivity on K, force
v=0. K is not assumed to be an integral domain.
Conversely every root in I with zero seeds is genuinely periodic.

Thus packets are in bijection with the least R-cycles in I, including
every actual finite preimage. Fixed cores have full time group
log(2a) Z; other cycles have log(bd) Z. Source isotropy is ell Z,
where ell=1 or 2; its clock is injective. Extension fixed-object
isotropy is trivial. Outside eventual periodic basins, source isotropy
and positive time returns are absent. Equal lengths do not merge packets.

The retained fixed core (2,4,2,0,0) already gives a primitive log 4
packet distinct from the second traversal of (1,2,1,0,0).
This was reported as the early decisive STOP, not repaired afterward.
The same short classification shows only log 2 can be a prime primitive
time: every two-cycle exponent bd is composite, while 2a is prime only
at a=1. No numerical census or unbounded orbit search was needed.

## 4. Checkpoint 2 — manuscript, corollaries and corrections

The full initial paper agrees with the raw derivation. Its uniform
even-period seed argument correctly handles all profinite states.
The parametrization (a,b,c)=(g alpha,k s,g gamma), s=alpha+gamma,
gcd(alpha,gamma)=1, is exact, and R swaps (g,k,alpha,gamma) with
(k,g,gamma,alpha). For odd prime p, g k s²=p² forces s=p and
g=k=1. The p-1 coprime positive ordered pairs of sum p are unequal
and pair under swapping. This verifies exactly (p-1)/2 primitive
packets of time 2 log p, not repetitions of an absent log-p packet.
This is a direct corollary of the frozen full classification.

FEEDBACK-OFF retains the decisive zero-seed family under its own
branch IMAGE law. At fixed root (a,2a,a), fixed-seed equations give
x=y=j with 0<=j<d; hence exactly d distinct fixed packets, each
with least time log d. This does not classify higher-period control
seeds. UNIT-INDEX has a unimodular seed automorphism, its own J=1
and c=0. Its time groups are all {0}; source isotropy can remain
nontrivial and then also remains as extension isotropy.

Two minor wording corrections were requested and verified at the
final hash. Section 2 now retains all terminal STATES, not purportedly
terminal entire main root fibres. Section 5 makes finite preimage
levels relative to each fixed core cycle and fixed depth; the union
over infinitely many cores need not be finite. UNIT-INDEX's terminal
root fibres are legitimate and were correctly left unchanged.
No mathematical result or frozen rule was changed.

## 5. Checkpoint 3 — adverse scope and verdict

The arithmetic identity and joint clock are real positive owner results.
They do not imply prime-exclusive primitives or unique naturalness.
The unwanted composite packet is not resolved by equal-time identification,
retiming, selecting prime roots or deleting null/nonreturning states.
The paper preserves the complete ledger and makes none of those repairs.

**Verdict: no outstanding blocking issue or requested correction.**
STOP target promotion / FORK for this exact candidate. The short full
classification is justified by the precommitted identities, not a new
search after failure. Do not generalize this negative result to every
refactorization architecture. Coarse packet topology is unaudited;
naturalness remains OPEN; T3 is NOT SUPPLIED / NOT PURSUED.
Classical A0/A1/A2 are NOT APPLICABLE, formal coordinates UNASSIGNED,
and Route B NOT INVOKED. Earlier candidates and 241/242 remain unchanged.
