# Divisor-driven rational relaxation: composite fixed families and full translated packets

Candidate ID: `ANG-20260923-DRR01`. Paper 437; 2026-09-23.
Outcome: OWNED RATIONAL IMAGE CLOCK; COMPOSITE FIXED FAMILIES — STOP / FORK
Batch: `NONHOMOGENEOUS-FEEDBACK-20260923-R`, round3/5.
Type: exact full-source inverse/clock and negative arithmetic result.
Classical NOT APPLICABLE; arithmetic T1 NOT PASSED; T3 NOT AUDITED;
formal UNASSIGNED; B NOT INVOKED. Internal review NOT_CALIBRATED.

## Abstract

All three full three-dimensional owners admit complete actual inverse
atlases and positive finite all-point IMAGE clocks. MAIN's entire fixed
set comprises the origin line and positive-integer diagonal lines, with
singleton incoming per point. Each diagonal-\(j\) primitive is
\(2\log(1+j^2)\); its multiplier is a composite square. Distinct translates
are distinct full packets, also for every actual positive finite core.
The proof uses this owner's actual groupoid, no borrowed diffeomorphism
theorem, section or higher-cycle census. Denominator-OFF has zero clock globally.

## 1. Same-object ledger and full laws

The [frozen card](candidate-card.md) fixes full \(X=\mathbb R^3\), original
coordinates \((u,v,w)\), Borel sets and \(\mu=du\,dv\,dw\), sigma-finite
but not a probability or claimed invariant measure. Every source is legal;
signed axes, faces, units, null states and unbounded fibres remain.
Absence of an inverse is not a terminal. Write
\[
 n=\lfloor u\rfloor,\quad m=\lfloor v\rfloor,\quad
 d=\max(1,\gcd(|n|,|m|)),\qquad \gcd(0,0)=0.            \tag{1}
\]
Read \(d\) once at the ORIGINAL source for the full step. MAIN is
\[
 U=\frac{u+dv^2}{1+v^2},\qquad
 V=\frac{v+dU^2}{1+U^2},\qquad W=w+d(u^2-v^2).          \tag{2}
\]
The second sweep uses updated \(U\); the drift uses original \(u,v\).
D CONTENT-OFF uses the same formulas with constant \(d=1\), without a
gcd guard or redundant labels. N DENOMINATOR-OFF instead uses
\[
             U=u+dv^2,\quad V=v+dU^2,\quad
             W=w+d(u^2-v^2),                          \tag{3}
\]
with its own original-source (1). MAIN/N recompute (1) at their own output.
The positive denominators make (2) defined at every real source.
No owner is assumed globally injective; D will have a single global inverse.
\(w\) is a geometric source coordinate, distinct from extension height \(h\).

In cells \(u\in[n,n+1),v\in[m,m+1)\), \(1<m<n\), the current readout
satisfies \(m\mid n\) exactly when \(d=m\). The same content enters both
actual sweeps and the drift, and \(U,V\) supply the next readout.
This is the divisor-symbolic-to-geometry feedback interface on the full
source, not an independent integer seed or a prime oracle. The readout,
constant 1, sweep order and Lebesgue measure are designs; naturalness is OPEN.
The benchmark requires a nonempty positive ledger, every primitive
\(\log p\) for an ordinary integer prime, at most one packet per prime,
and ultimately all-prime coverage.

## 2. Complete inverses and the full three-dimensional IMAGE

For MAIN target \((U,V,W)\), enumerate EVERY integer \(d\ge1\), set
\[
 v=(1+U^2)V-dU^2,\quad
 u=(1+v^2)U-dv^2,\quad w=W-d(u^2-v^2),                 \tag{4}
\]
and admit exactly the reconstructed sources whose actual (1) equals \(d\)
and whose forward value is the target. D uses (4) only with \(d=1\),
without any content test. N uses every \(d\ge1\) with its own reconstruction
\[
            v=V-dU^2,\quad u=U-dv^2,\quad
            w=W-d(u^2-v^2),                           \tag{5}
\]
and its own actual-content/forward checks.
For fixed \(d\), solving the second sweep, then the first, then the drift
forces exactly (4) or (5). Substitution gives the reverse identity.
An actual source supplies its unique \(d\), proving exhaustion. No inverse
index or depth cutoff occurs; equal actual sources count once.
The actual branch domains are Borel because the reconstructions are
polynomial and (1) is Borel. Different labels cannot represent the same
admitted source with two different contents, but target domains may overlap.

For the FULL inverse derivative, factor (4) into three maps on \(\mathbb R^3\):
\[
 (U,V,W)\mapsto(U,v,W)\mapsto(u,v,W)\mapsto(u,v,w).
\]
Their full derivative matrices, at the appropriate intermediate points, are
\[
 \begin{pmatrix}1&0&0\\2U(V-d)&1+U^2&0\\0&0&1\end{pmatrix},\
 \begin{pmatrix}1+v^2&2v(U-d)&0\\0&1&0\\0&0&1\end{pmatrix},\
 \begin{pmatrix}1&0&0\\0&1&0\\-2du&2dv&1\end{pmatrix}.                  \tag{6}
\]
In particular the \(w\)-mixing row is retained. Multiplying determinants gives
\[
 J_{\mathrm{MAIN},d}=(1+U^2)(1+v_d^2),\qquad
 J_D=(1+U^2)(1+v_1^2),                               \tag{7}
\]
where \(v_d\) is (4)'s reconstructed coordinate, and D uses only \(d=1\).
For N, the analogous
first two matrices have off-diagonal entries \(-2dU,-2dv\) and unit
diagonal; the third matrix is unchanged. Thus its full \(J_{N,d}=1\).
Every value is finite and positive at every actual point.

Each of the three fixed-\(d\) factors is a global smooth diffeomorphism,
as is their composition. Change of variables restricted to every Borel
subset \(E\) of its actual inverse domain therefore proves
\[
                    \mu(\theta_d E)=\int_E J_d\,d\mu.  \tag{8}
\]
D has one unrestricted branch; MAIN/N have the complete countable atlases
above. Overlapping targets retain their distinct predecessors and branch
laws, not an unqualified multiplicity-free union Jacobian.
At floor faces one differentiates the displayed fixed-\(d\) smooth germ,
not the discontinuous readout. Measure identities alone fix derivatives
only a.e.; the frozen germ supplies the particular all-point version.
No density, atomic weight or null-set repair is used. N's branch IMAGE1
does not by itself assert global measure preservation of a many-to-one map.

With the unique source-selected branch, the own step clocks are
\[
 \kappa_O(z)=-\log\bigl((1+v^2)(1+U_O(z)^2)\bigr)
 \quad(O=\mathrm{MAIN},D),\qquad \kappa_N(z)=0.         \tag{9}
\]
The formula uses each owner's actual \(U_O\), not a pointwise equality
between the two owners' clocks. It is zero exactly when \(u=v=0\) and
strictly negative otherwise. Signed clocks
are not a positive suspension roof or a claimed symplectic structure.

## 3. Full actual histories, kernels, isotropy and phases

For each owner \(T\), take all actual triples
\(G=\{(z,r-s,y):T^rz=T^sy,\ r,s\ge0\}\), source \(y\), range \(z\).
Equal triples are equal arrows and integer lag is retained. Countably many
actual inverse branches give countable fibres; the maps and meeting
conditions are Borel. All forward iterates exist; a missing predecessor
does not remove its target object. Set \(S_0=0\) and use actual clock sums:
\[
                  c(z,r-s,y)=S_r(z)-S_s(y).            \tag{10}
\]
Two witnesses of the same lag differ by a common shift of both meeting
times; extending to the larger pair adds the same sum to each side.
This proves descent. In a composition, extend the middle histories to
their larger meeting time; their middle sums cancel. Hence \(c\) adds,
and the forward arrow \((Tz,-1,z)\) has clock \(-\kappa(z)\).

For MAIN/D define
\(P_r(z)=\prod_{i=0}^{r-1}(1+v_i^2)(1+u_{i+1}^2)\), \(P_0=1\),
along that owner's actual iterates; for N put \(P_r=1\).
Then \(S_r=-\log P_r\) and the full kernels are
\[
 \begin{split}
 \ker\ell&=\{(z,0,y):T^rz=T^ry\text{ for some }r\},\\
 \ker c&=\{(z,r-s,y):T^rz=T^sy,\ P_r(z)=P_s(y)\},\\
 \ker\ell\cap\ker c
 &=\{(z,0,y):T^rz=T^ry,\ P_r(z)=P_r(y)\text{ for some }r\}.
 \end{split}                                                        \tag{11}
\]
For N, \(\ker c=G_N\) and the joint kernel is its lag kernel.
These are all arrows satisfying the conditions, not only loops.

A nonzero isotropy lag is equivalent to eventual periodicity. If \(z\)
enters a least source cycle of period \(q\) with signed cycle sum \(C\),
then precisely
\[
       G_z^z=q\mathbb Z,\qquad c(kq)=kC,\qquad H_z=C\mathbb Z.         \tag{12}
\]
Unequal equal iterates produce such a cycle; on its least core all
meeting lags are multiples of \(q\). Tail sums cancel and yield (12).
For a non-eventually-periodic state source isotropy is trivial and \(H_z=0\).
On the full extension \(X\times\mathbb R_h\), arrows act by
\((y,h)\mapsto(z,h+c)\). Extension isotropy is \(q\mathbb Z\) when
\(C=0\), and trivial when \(C\ne0\); non-eventual states have none.
The stabilizer of physical height translation on its orbit SET is exactly
\(H_z\), since any height return is a source-isotropy arrow. No quotient
regularity is asserted. Only \(L=|C|>0\) defines a primitive, with repeats
\(kL\); \(H=0\) retains any ineffective source isotropy.

All predecessors are exactly §2's passing inverses. For a chosen periodic
core point \(p\), its entire source component is
\(\bigcup_{j\ge0}T^{-j}\{p\}\), with every actual branch at every depth.
For arbitrary points the full component is
\(\bigcup_{r,s\ge0}T^{-r}\{T^sz\}\). If \(T^az=T^bp\), the complete
height phase at \(p\) is
\[
                  h+S_b(p)-S_a(z)\pmod {H_p}.          \tag{13}
\]
For a non-eventual component the same meeting formula at any representative
has \(H=0\) and gives a real phase. Different witnesses differ exactly by
an element of the entire \(H\). Equal lengths never identify base packets.
N has \(c\equiv0,H_z=0\) globally, with phase \(h\) per source component;
any eventual-cycle source/extension isotropy remains as in (12).

## 4. Entire fixed sets and singleton full incoming

For MAIN, fixing the first two outputs in (2) gives
\[
                    v^2(u-d)=0,\qquad u^2(v-d)=0.      \tag{14}
\]
If either coordinate is zero both are zero; otherwise \(u=v=d\).
In both cases the drift vanishes. At the origin the actual readout is 1;
at \((j,j)\), \(j\ge1\) integer, it is exactly \(j\), including the
assigned integer faces. These exhaust all signed and off-axis solutions:
\[
 \operatorname{Fix}(\mathrm{MAIN})=
 \{(0,0,w):w\in\mathbb R\}\ \cup\
 \bigcup_{j\ge1}\{(j,j,w):w\in\mathbb R\}.               \tag{15}
\]
D's own constant-\(1\) equations (14) give only the origin line and
\((1,1,w)\). For N, fixedness first gives \(dv^2=0\), then \(du^2=0\);
its entire fixed set is only \((0,0,w)\). No gcd guard is imposed on D.

For MAIN target \((j,j,W)\), \(j\ge1\), an arbitrary inverse label \(d\)
in (4) reconstructs integers
\[
 v=j+j^2(j-d),\quad u=j+(j-d)v^2,\quad
 w=W-d(u^2-v^2).
\]
Since \(v\) is a multiple of \(j\),
\(\gcd(|u|,|v|)=\gcd(j,|v|)=j\), including possible zero or negative
reconstructions. Thus admission forces \(d=j\), which returns exactly
\((j,j,W)\). At the origin line every label reconstructs \((0,0,W)\),
but only actual content 1 passes. D's sole inverse returns each of its
fixed points to itself. N at \((0,0,W)\) likewise reconstructs it for
every formal label but admits only \(d=1\).
Hence EACH listed fixed point has itself as its only predecessor at every
depth and as its entire source component. No external incoming, hidden
off-diagonal branch or alternative lag can change its whole clock image.

Every fixed point has source isotropy \(\mathbb Z\). MAIN at \((j,j,w)\)
has \(\kappa=-2\log(1+j^2)\), so its ENTIRE \(H=L_j\mathbb Z\), where
\[
                 L_j=2\log(1+j^2)=\log((1+j^2)^2).     \tag{16}
\]
Extension isotropy is trivial; every phase \(h\bmod L_j\mathbb Z\) remains.
D's \((1,1,w)\) points have \(L=\log4\) with the same own ledger.
Every origin-line core has \(H=0\), retained source/extension \(\mathbb Z\)
and full real phase \(h\). Different \(w\)'s label distinct singleton
base classes, not phases of one packet. For \(j\ge1\), the multiplier in
(16) is composite; the source period is 1 and no loop supplies a smaller
generator such as \(\log(1+j^2)\). MAIN's \(j=1\) line is already an
actual nonempty family of primitive \(\log4\), not a repeated \(\log2\) packet.

## 5. Global translated-packet gate, proved for this actual owner

For each of MAIN/D/N, \(\alpha_t(u,v,w)=(u,v,w+t)\) preserves readouts,
all actual inverse-domain tests and Lebesgue measure, and
\(T\alpha_t=\alpha_tT\) at every point. Equations (4)–(7) show that inverse
branches translate in their third coordinate and that their \(J\)'s do
not change. Thus \(\kappa(\alpha_tz)=\kappa(z)\) and all sums are preserved.
The induced arrow action is
\((z,\ell,y)\mapsto(\alpha_tz,\ell,\alpha_ty)\), preserving \(c\), all
kernels and the entire isotropy images. Its height lift
\((z,h)\mapsto(\alpha_tz,h)\) respects the actual extension arrows and
commutes with physical \(h\)-translation. It is a different action from
that physical time; no source \(w\) is substituted for \(h\).

Let \(O\) be ANY actual finite least core, not just (15). Its translate
\(O_t=\alpha_tO\) has exactly the same least source period and cycle sum.
If \(O_t,O_s\) belonged to one full source component, a meeting of their
forward iterates would make the two deterministic cycles identical.
Equality of their finite nonempty sets of \(w\)-coordinates then gives
\(\max w(O)+t=\max w(O)+s\), hence \(t=s\).
Thus different translates belong to distinct FULL packets, not merely
different point representatives; adding all incoming cannot merge them.
If the core has \(C\ne0\), (12) supplies the same entire \(H=C\mathbb Z\)
and the same positive primitive for continuum many distinct packets, with
all height phases carried by the lift. Zero-clock cores instead retain
their ineffective isotropy and have no positive primitive.

This argument uses actual meeting arrows and finite cycles; it assumes
neither smoothness nor injectivity of the assembled MAIN/N maps, and does
not invoke 429's global-diffeomorphism theorem. It does not claim that all
translated NONPERIODIC source components must be distinct.
Consequently nonempty, prime-only and at-most-one-per-prime cannot jointly
hold for these translation-equivariant owners: absence of positive cores
fails nonemptiness; any positive core either has a wrong prime time or
has continuum copies of its prime time. This conditional global argument
is separate from the already proved MAIN/D fixed-core existence.

## 6. Decision, controls and disclosure

MAIN fails prime purity by its actual composite fixed families; its global
symmetry also prevents a nonempty prime-unique ledger. D independently
retains a \(\log4\) family; N independently has an empty positive ledger
because its entire clock is zero. These control conclusions are not
transferred clocks or excuses to discard fibres. No higher cycles were
classified. All inverse depths, source isotropy and phases remain.
T0/IMAGE ownership is established; arithmetic T1 NOT PASSED; T2 has the
explicit negative packet and global multiplicity gate; T3 NOT AUDITED.
Strong naturalness and PROVES_TOO_MUCH remain OPEN; classical NOT APPLICABLE,
formal UNASSIGNED, B NOT INVOKED. STOP / FORK, without quotient or repair.

Inputs are the frozen 96-line [card](candidate-card.md), SHA256
`7be673a1470edcf1351835bb53fa300874fce70f922393e4560593befaea60da`,
and the local paper template. See the [claims](claim-ledger.md) and
[README](README.md). Exact methods are algebra, all-point change of
variables and actual-history arguments, not scientific numerics.
Definition-stage reads were 430 summary1–110, 416 card1–104 and 429 card1–105,
all to EOF including outcomes; hashes are recorded in the card. Previous
author history and informal inverse/fixed-feasibility design algebra remain
disclosed, not blind/sealed preregistration. No current raw/scope/peer or
sibling manuscript was read; no external novelty/nonconjugacy claim is made.
AI agents supplied derivation, drafting and internal checking; no human/external
verification is certified. Same-author helper
`/root/bilateral_transport_review/direct_controls` read proposal
messages for wording, then only this card for D/N fixed/incoming/own-clock
derivation. The main author derived MAIN, common ownership and the global
packet gate, and checked the controls. This helper is not an independent reviewer.
ARS governs scope/disclosure, not validity; same-model/shared-history review
is NOT_CALIBRATED. Only paper/README/ledger are author-owned; root owns card
outcomes/integration. No scientific numeric code, outside lookup, old edit,
Git/PDF/publication or Route work.

EOF — DRR01 full fixed and global symmetry gate complete; no higher-cycle census.
