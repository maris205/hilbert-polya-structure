# Divisor commutator transfer: an owned volume clock with a composite fixed primitive

Candidate ID: `ANG-20260923-DCT01`. Paper 427; 2026-09-23.
Outcome: OWNED COMMUTATOR IMAGE CLOCK; COMPOSITE FIXED PRIMITIVE — STOP / FORK
Batch: `SYMMETRY-FEEDBACK-20260923-P`, round3/5.
Type: exact negative result for a partial Borel matrix/groupoid owner.
Classical NOT APPLICABLE; arithmetic T1 NOT PASSED; T3 NOT AUDITED;
formal UNASSIGNED; B NOT INVOKED. Internal review NOT_CALIBRATED.

## Abstract

The frozen eight-dimensional matrix-pair transport and both controls have
complete actual inverse atlases and positive, finite, all-point inverse
IMAGE versions for their own counting-times-Lebesgue measures. We derive
their full history cocycles, kernels, isotropy, height phases and conditional
cycle ledger. MAIN and the commutator-OFF control each have exactly one
fixed state, with exactly four states in its entire incoming class.
Its whole clock image is \((\log16)\mathbb Z\), not a selected subloop:
this nonempty composite primitive refutes the ordinary-prime requirement.
The index-OFF control has no fixed state. No higher-period census is made.

## 1. Frozen owner and claim boundary

The [card](candidate-card.md) fixes \(X=\mathbb N_0\times M_2(\mathbb R)^2\)
and \(\mu=\#\times d^4A\,d^4B\), a sigma-finite, non-probability reference
measure. No invariant-measure claim is made. Every owner uses this full
source, not a commuting, scalar, eigenvector or similarity quotient.
When \(n\ge1\) and \(g=\det_{\mathbb C}(A+iB)\ne0\), put
\[
 a=\operatorname{Arg}(g)/(2\pi)\in[0,1),\quad d=1+\lfloor na\rfloor.
\]
Only if \(d\mid n\) is \(q=n/d\) defined. Write
\(L_B=\alpha\mathrm{Id}_{M_2(\mathbb R)}+\beta\operatorname{ad}_B\),
where \(\operatorname{ad}_B(A)=BA-AB\). The three separate owners are

| Owner | \(\alpha,\beta\) | Actual map | Additional permission |
| --- | --- | --- | --- |
| MAIN | \(d,q\) | \((n,A,B)\mapsto(d+q,B,L_BA+I_2)\) | \(L_B\) invertible |
| C, commutator-OFF | \(d,0\) | \((n,A,B)\mapsto(d+q,B,dA+I_2)\) | None |
| S, index-OFF | \(1,q\) | \((n,A,B)\mapsto(d+q,B,L_BA+I_2)\) | Its own \(L_B\) invertible |

Here \(\mathrm{Id}\) is an operator, whereas \(I_2\) is the added matrix.
Operator determinants use the four original real matrix-entry coordinates.
All failed permissions, \(n=0\), \(g=0\) and appropriate singular-operator
states remain terminals, with identities and all incoming but no forward
step or step clock. An individual singular \(A\) or \(B\) is not excluded.
Units, cuts, signs and non-diagonalizable matrices remain. C does not
inherit MAIN's unused singularity test. A terminal identity is not a fixed
point of the partial map, and no absorbing loop is added.

The target requires a nonempty positive ledger, every primitive equal to
\(\log p\) for an ordinary integer prime, at most one packet per prime,
and ultimately all-prime coverage. One wrong MAIN primitive suffices to
stop; an empty control fixed set does not decide MAIN or higher periods.

## 2. Complete actual inverse and eight-dimensional IMAGE

For a target \((m,C_0,D_0)\), enumerate every positive integer pair
\(d+q=m\). Set \(n=dq\) and, for that owner's coefficients,
\[
 \Theta_{d,q}(m,C_0,D_0)
   =(dq,L_{C_0}^{-1}(D_0-I_2),C_0).                 \tag{1}
\]
C uses \(L_{C_0}=d\mathrm{Id}\). Retain exactly those targets for which
this operator exists and the reconstructed source has that very
\(g\), phase digit \(d\), divisibility permission, own regularity and
forward equality. No next-step permission of the target is imposed.
These are Borel conditions: determinants and inverse germs are continuous
on their regular open sets, and the specified Arg/floor readout is Borel.
For \(m<2\) there is no inverse pair; otherwise there are finitely many.

The first matrix output forces \(B=C_0\); invertibility then forces the
second reconstruction in (1). Thus both inverse identities hold and
every actual predecessor is listed, with no eigenbasis choice. Any actual
source determines its unique \(n,d,q\); equal actual sources are identified,
not multiplied by labels. Different branch target domains can overlap
because different actual predecessors can have the same target.

We now prove, rather than assume, the eight-dimensional determinant.
On the unrestricted regular open germ, set
\(K_A(H)=\beta(HA-AH)\). In the ordered four-entry blocks the forward
and inverse derivative matrices are respectively
\[
 \begin{pmatrix}0&I_4\\ L_B&K_A\end{pmatrix},
 \qquad
 D\Theta=
 \begin{pmatrix}-L_{C_0}^{-1}K_A&L_{C_0}^{-1}\\ I_4&0\end{pmatrix}.       \tag{2}
\]
Swapping two blocks of four rows has sign \((-1)^{16}=1\).
The resulting block triangular matrices give
\[
 J_{d,q}(m,C_0,D_0)=|\det_{\mathbb R^8}D\Theta|
       =|\det_{\mathbb R^4}L_{C_0}|^{-1}>0.             \tag{3}
\]
The mixing block \(K_A\) has not been dropped before taking the full
determinant. In particular, (3) is not a borrowed four-dimensional measure.

The displayed germs are smooth diffeomorphisms between the open sets
where \(L_B\), respectively \(L_{C_0}\), is invertible. Standard
change of variables, restricted to the Borel actual inverse domain,
therefore proves, for every Borel subset \(E\) of that domain,
\[
             \mu(\Theta_{d,q}E)=\int_E J_{d,q}\,d\mu.    \tag{4}
\]
Each branch changes one counting slice to one counting slice, so no
additional integer factor occurs. These countably many Borel charts cover
every legal step. Distinct-source images are disjoint; overlapping target
domains retain their separate predecessors and separate branch IMAGE laws.
There is no single unqualified Jacobian for a many-predecessor union.
Equation (3) assigns the frozen positive finite value at every actual
point, including phase cuts and null states; it is not an a.e. choice.
The measure identity alone fixes a derivative only a.e.; the card's smooth
inverse-germ prescription supplies this particular all-point version.
The readout is an admission test, not a function differentiated at a cut.

An explicit check also describes all zero step clocks. For
\(B=\left(\begin{smallmatrix}u&v\\w&t\end{smallmatrix}\right)\), the
four-entry matrix of \(\operatorname{ad}_B\) is
\[
 \begin{pmatrix}0&-w&v&0\\-v&u-t&0&v\\w&0&t-u&-w\\0&w&-v&0\end{pmatrix}.
\]
Expanding \(\det(\alpha I_4+\beta\operatorname{ad}_B)\) gives
\[
 \det L_B=\alpha^2(\alpha^2-\beta^2\Delta(B)),\qquad
 \Delta(B)=(u-t)^2+4vw.                                \tag{5}
\]
This entry formula includes repeated eigenvalues and non-diagonalizable
matrices. On a legal step, with its unique source-selected branch,
\(\kappa(z)=-\log J(Fz)=\log|\det L_B|\). Thus C has
\(\kappa_C=4\log d\); MAIN and S use their own (5), not C's clock.
Precisely \(|\det L_B|=1\) gives zero clock. Clocks may be signed or zero;
no positive roof or symplectic/invariant-volume assertion follows.

## 3. Full history, kernels, isotropy and phases

The following proof applies to each of the three actual partial maps.
Let \(S_0=0\), and let \(S_r(z)\) be the sum of the \(r\) legal step clocks.
Use all triples \(G=\{(z,r-s,w):F^rz=F^sw,\ r,s\ge0\}\), with actual
integer lag retained and equal triples identified. This is a Borel
groupoid; finite predecessor sets imply countable source/range fibres.
Composition adds lags, source is \(w\), range is \(z\), and
\[
                 c(z,r-s,w)=S_r(z)-S_s(w).             \tag{6}
\]
For two witnesses of the same lag, their iteration pairs differ by a
common integer shift. Using the larger pair adds the same legal sum
after their common meeting point to both sides, proving descent.
For composition, extend the two middle histories to their larger meeting
iterate; the two middle sums cancel. This proves additivity, including
terminal meetings. The forward arrow \((Fz,-1,z)\) has clock \(-\kappa(z)\).

The entire kernels, not just their isotropy restrictions, are
\[
 \begin{split}
 \ker\ell&=\{(z,0,w):F^rz=F^rw\text{ for some legal }r\},\\
 \ker c&=\{(z,r-s,w):F^rz=F^sw,\ S_r(z)=S_s(w)\},\\
 \ker\ell\cap\ker c
 &=\{(z,0,w):F^rz=F^rw,\ S_r(z)=S_r(w)\text{ for some }r\}.
 \end{split}                                                        \tag{7}
\]
The quantified witnesses in each line are legal. Extend on all
\(X\times\mathbb R\) by \((w,h)\mapsto(z,h+c)\). Height translation acts
on its orbit SET; no smooth or Hausdorff quotient is claimed.

A nonzero source isotropy lag is equivalent to eventual periodicity:
unequal equal iterates give a genuine cycle; conversely a cycle supplies
all its multiples. If the eventual cycle has least period \(r_0\) and
signed cycle sum \(C_0\), then exactly
\[
 G_z^z=r_0\mathbb Z,\qquad
 c(kr_0)=kC_0,\qquad H_z=C_0\mathbb Z.                  \tag{8}
\]
Indeed every sufficiently late equality on the least cycle has lag a
multiple of \(r_0\), and all such lags have legal witnesses. Tail sums
cancel, and moving the core cyclically preserves its complete cycle sum.
For a non-eventually-periodic state source isotropy is trivial and \(H_z=0\).
Extension isotropy is \(r_0\mathbb Z\) if \(C_0=0\), and trivial otherwise.
Thus a zero \(H\) never by itself erases ineffective source isotropy.
Here every \(H\) is cyclic; if nonzero its least positive generator is
\(L=|C_0|\), with repetitions \(kL\), not a chosen fraction of this sum.

For any chosen periodic core point \(p\), all incoming is exactly
\(\bigcup_{j\ge0}F^{-j}\{p\}\), using every branch of (1) at every level.
This includes every point of its cycle and every coalescing history.
If \(F^az=F^bp\), its height phase at \(p\) is
\[
               h+S_b(p)-S_a(z)\pmod {H_p}.             \tag{9}
\]
Changing the meeting witness changes this by an element of the whole \(H_p\).
For arbitrary non-eventually-periodic components the identical meeting formula with
any representative and \(H=0\) gives the full real phase. In all cases
the stabilizer of height translation is exactly \(H\): returning to the
same height-orbit class requires, and is supplied by, source isotropy.
Different source packets with equal \(L\) are not identified.

## 4. Complete fixed sets and entire incoming classes

A fixed state must have a legal step. Its register equations give
\(dq=d+q=n\), hence \((d-1)(q-1)=1\), so \(d=q=2,n=4\).
Its first matrix equation forces \(A=B\); only now does the commutator
vanish. MAIN and C then require \(A=2A+I_2\), giving exactly
\[
                         f=(4,-I_2,-I_2).             \tag{10}
\]
This is actual: \(g=2i\), \(a=1/4\), and \(1+\lfloor4a\rfloor=2\),
at the included lower sector cut. MAIN's \(L=2\mathrm{Id}\) is regular.
S instead requires \(A=A+I_2\), impossible. These arguments start from
all matrix entries, not a scalar section: S's full fixed set is empty.

We exhaust every incoming branch of (10) for MAIN and C. At each scalar
target, \(B=C_0\) is forced scalar, so MAIN's \(L=d\mathrm{Id}\) and
the unrestricted inverse uniquely forces scalar \(A\). No off-scalar
predecessor can be missing. At \(f\), the pairs \(d+q=4\) are:

| Pair | Reconstructed source | Exact phase admission |
| --- | --- | --- |
| \(1,3\) | \(z_3=(3,-2I_2,-I_2)\) | \(g=3+4i,\ 0<a<1/4\), actual \(d=1\) |
| \(2,2\) | \(f\) | \(a=1/4\), actual \(d=2\) |
| \(3,1\) | \((3,-(2/3)I_2,-I_2)\) | \(g=-5/9+(4/3)i,\ 1/4<a<1/2\), not \(d=3\) |

At \(z_3\), pair \((1,2)\) gives \(z_2=(2,-2I_2,-2I_2)\),
with \(g=8i,a=1/4\) and actual digit 1. Pair \((2,1)\) gives
\((2,-I_2,-2I_2)\), with \(g=-3+4i\), \(1/4<a<1/2\);
its actual digit is 1, so that branch is rejected.
At \(z_2\) the only pair is \((1,1)\), giving
\(z_1=(1,-3I_2,-2I_2)\), \(g=5+12i\ne0\), actual digit 1.
There is no positive pair summing to register 1. Thus the complete class is
\[
                    z_1\longmapsto z_2\longmapsto z_3
                         \longmapsto f\longmapsto f.    \tag{11}
\]
All retained operators are regular. Iterating this exhausted inverse list
adds no state, although the fixed loop permits arbitrarily long histories.
S has no fixed core; its possible higher cycles remain unclassified.

For MAIN and C, (3) gives \(\lambda=\kappa(f)=\log16\);
each of the three incoming steps has its own \(d=1\) scalar operator,
so its clock is zero. Let \(e(f)=0,e(z_3)=1,e(z_2)=2,e(z_1)=3\).
On this whole four-state class every integer lag is realized, and
\[
 G|_{\mathcal B}=\mathcal B\times\mathbb Z\times\mathcal B,\quad
 c(x,k,y)=(k-e(x)+e(y))\lambda,\quad
 H_x=\lambda\mathbb Z,\qquad \mathcal B=\{f,z_3,z_2,z_1\}.              \tag{12}
\]
Indeed sufficiently long histories have sums \((r-e(x))\lambda\).
Here \(\ker c\) means \(k=e(x)-e(y)\), \(\ker\ell\) means \(k=0\),
and their intersection consists exactly of the identities. Source
isotropy is \(\mathbb Z\), extension isotropy is trivial, and all phases
are \(h\bmod\lambda\mathbb Z\). There is one fixed-core packet per owner,
not four packets from the incoming points or extra packets from its phases.
Its least positive primitive is \(\log16\), and its repetitions are
\(k\log16\). No source isotropy supplies \(\log2\) or a shorter generator.

## 5. Arithmetic interface, controls and gate

For every \(n\ge1\), take the full card's witness
\(A=\operatorname{diag}(\cos\phi,1)\),
\(B=\operatorname{diag}(\sin\phi,0)\), \(0\le\phi<2\pi\).
Then \(g=e^{i\phi}\); sector
\([2\pi(d-1)/n,2\pi d/n)\) gives exactly digit \(d\).
Divisibility still decides arithmetic permission: prime registers have no
proper nonunit divisor, whereas a composite's proper divisors are available.
For a permitted \(d,q\), MAIN's witness determinant is
\(d^2(d^2-q^2\sin^2\phi)\), S's is \(1-q^2\sin^2\phi\), and C's is \(d^4\).
The extra forbidden angles are finite, so every sector for a permitted
divisor has regular witnesses. Particular singular witnesses remain terminals;
we do not infer regularity merely from a sector. This family establishes
the stated interface, never a replacement source or periodic selector.

The ledger retains current phase readout, divisor permission, actual
noncommutative geometry and regenerated readout in one object. C shows that
removing the commutator preserves this particular adverse fixed primitive;
S removes that fixed window, not necessarily all periodicity or positive times.
Cuts, null fixed states, unit tail steps, singular permissions and unbounded
history length are handled exactly, without a numerical cutoff.
Because 16 is composite, MAIN's actual primitive violates the EVERY-prime
condition even though the tested positive ledger is nonempty. This is a
decisive necessary-target STOP / FORK, without any higher-cycle inference.
T0 and inverse-clock ownership are proved; arithmetic T1 is NOT PASSED,
T2 has this explicit adverse packet, T3 NOT AUDITED. Strong naturalness
and PROVES_TOO_MUCH risks remain OPEN; classical NOT APPLICABLE,
formal UNASSIGNED, B NOT INVOKED. No roof, measure or clock-root repair.

## 6. Provenance, assistance and reproducibility

Exact inputs are the frozen 95-line [card](candidate-card.md), original SHA256
`04cc5ca8f9e03a1409a83855cfc682132db5704c0d7fc2be19d438dbfaf8657f`.
Definitions and conclusions are cross-indexed in the [claims](claim-ledger.md)
and [README](README.md). Proof uses exact algebra and change of variables;
no scientific numerical code, external search or higher census is used,
and no trace/transfer operator is proposed.
The author read the card, paper template and registry guidance; prior scoped
collision reads were 401 card1–107 and 415 card1–109, including their outcomes,
with hashes recorded in the frozen card. No 427 reviewer/raw/evidence was read.
Earlier author history and informal inverse/fixed-feasibility design algebra
are disclosed; this was not blind or sealed preregistration.
AI agents supplied mathematical derivation, drafting and internal checking;
no human or external verification is certified. Same-author helper
`/root/bilateral_transport_review/direct_controls` first saw only the
proposal text for domain wording, then only the frozen 427 card for the
disjoint C/S fixed-set and C-incoming derivation. The main author derived
the common eight-dimensional IMAGE/history and MAIN results and checked
the control calculation. The helper is not an independent reviewer.
The ARS workflow governs scope, provenance and disclosure, not mathematical
validity. Shared-history/same-model review is NOT_CALIBRATED.
Only this paper, README and claim ledger are author-owned; root owns card
append/integration and separate review. This result authorizes no 430,
publication, PDF, Git mutation or formal Route evaluation.

EOF — DCT01 author proof; decisive fixed gate complete, broader census not undertaken.
