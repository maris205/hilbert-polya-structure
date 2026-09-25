# 441 — card-only independent derivation

Candidate: ANG-20260923-DMF01. Review date: 2026-09-24.
Frozen session/batch: 2026-09-23, ADMISSION-CLOCK-20260923-S,440–444 only.
Root reported its full 97-line CP1 read and distinctly released raw mathematics.
Sole scientific input: original candidate-card.md lines 1–104, completely
reread after release through the original explicit EOF; no append was read.
candidate-card.md original prefix — 104 lines; SHA256 773843abf3378c2bb2351f57b9a1c559f5243eefb9ce0e5d05e85e97e36da687
Frozen scope-review.md — 97 lines; SHA256 cffab78b230d24c59912d02aea2c603344dc77042eb6bad67559bf1cd1547518
No author paper/README/ledger, peer, helper, sibling or old scientific file
was read. Design-algebra and prior-result exposure were disclosed in the
card; shared history remains exposed, not blind.
Retained ARS instructions govern this work, not claimed as freshly reread.
AI supplied exact derivation/checking; internal same-model NOT_CALIBRATED,
not human, external, cross-model or independent-of-shared-history validation.
No auxiliary agent, scientific code/numerics, network/literature, Git, PDF,
publication, expanded window or higher-period census was used.

## 1. Full owners and the exact arithmetic interface

Each owner separately retains all \(M_2(\mathbb R)\), its ordinary Borel
structure and original-entry Lebesgue4. Put
\[
C=\begin{pmatrix}1&0\\0&2\end{pmatrix},\quad
J=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
m=\lfloor A_{11}\rfloor,\ n=\lfloor A_{12}\rfloor,\quad K_q=C-qJ.
\]
MAIN uses \(m\ne0,m\mid n,q=n/m\), with
\(\det(A+C)\ne0,\det K_q\ne0\), and
\(T_{\rm M}(A)=(A+qJ)(A+C)^{-1}\) in that order.
G uses its own integer \(q_G=\lfloor n/m\rfloor\) for m nonzero and
q_G=0 otherwise, with only its own two geometric conditions and the same
fractional formula. L uses MAIN arithmetic permission but
\(T_L(A)=(A+qJ)C^{-1}\), without EITHER fractional geometric condition.
No owner requires A itself invertible.
All maps and domains are Borel by their fixed-label rational/affine formulas.
Every remaining state is terminal, retaining identities and all incoming,
not an absorbing loop or a point deleted from X.

For every integer q, \(\det K_q=2-q^2\ne0\): if |q|<=1 its square is
0 or 1, and otherwise its square is at least 4. The declared MAIN/G
condition is thus automatically satisfied by their actual integer exponents;
it is nevertheless retained as their specified geometric test.
At \(A_{N,d}=\begin{pmatrix}d&N\\0&1\end{pmatrix}\), actual readings are d,N.
If \(d\mid N\), q=N/d is an integer and
\(\det(A_{N,d}+C)=3(d+1)>0\), so BOTH geometric conditions hold.
Thus complete MAIN legality on the stated interface is exactly d|N,
not merely an assumed correspondence of arithmetic digits.
The actual quotient enters the numerator; the matrix output supplies
the next readouts. No invariant restriction to that interface is imposed.
This proves the stated lineage mechanism, not strong naturalness or prime
periodicity. No prime table, roof or fitted parameter has been inserted.

## 2. Complete actual inverse atlases, with matrix order retained

Fix any integer q and write \(M=A+C\). On \(\det M\ne0\),
\[
F_q(A)=(A+qJ)M^{-1}=I-K_qM^{-1}.
\]
Therefore \(B=F_q(A)\) satisfies \(I-B=K_qM^{-1}\), which is invertible.
Conversely, at EVERY real matrix B with \(\det(B-I)\ne0\), set
\[
\Theta_q(B)=(I-B)^{-1}K_q-C
           =(B-I)^{-1}(qJ-BC).
\]
The last equality follows from
\(qJ-BC=-K_q-(B-I)C\); no factors have been commuted.
Its reconstructed \(M=(I-B)^{-1}K_q\) is invertible, and substitution
gives \(F_q(\Theta_q B)=B\), as well as \(\Theta_q(F_q A)=A\).
Thus these are mutually inverse analytic diffeomorphisms between the
open sets \(\det(A+C)\ne0\) and \(\det(B-I)\ne0\).
This also proves that no actual fractional image with singular B-I was lost.
Singular A and singular B themselves are not excluded.

For MAIN enumerate ALL integer m!=0,n with m|n and q=n/m.
Restrict \(\Theta_q\) to targets whose reconstructed source passes
all own source/forward checks and the exact floor conditions
\(\lfloor(\Theta_q B)_{11}\rfloor=m,\lfloor(\Theta_q B)_{12}\rfloor=n\).
These conditions, the open target domain and the geometric tests define
a Borel actual target domain. They are necessary and sufficient for its
actual inverse branch by the two identities above.

For G enumerate ALL integer pairs m,n, use its OWN q_G and the same
reconstructed floor conditions, without MAIN divisibility or m!=0.
Both inverse identities and source checks hold with precisely that own
quotient, including m=0,q_G=0. Every actual G predecessor is recovered.
In either owner, an actual source uniquely fixes its two labels, so duplicate
actual sources are identified while distinct inverse points are retained.
The atlas is countable and every target has at most countably many inverses.

For L, fixed-q inverse is
\[
\Theta_q^L(B)=BC-qJ
\]
on the ENTIRE real matrix space. This affine map is the inverse of
\((A+qJ)C^{-1}\), again on the entire matrix space.
For every MAIN-admitted label retain exactly the reconstructed floor and
own arithmetic/forward checks. Neither det(A+C) nor det K_q is an L
condition. These Borel restrictions exhaust all actual L predecessors
by direct substitution, with no label/root/depth cutoff.
All inverse branches are injective restrictions of their analytic inverse
germs. A target need not have a next step in ANY owner.
No singular-source or target-next-step restriction was smuggled into L.

## 3. FULL four-dimensional IMAGE and every-point clocks

For a two-by-two U and V, the real determinant of \(H\mapsto UHV\)
on all four entries is \((\det U)^2(\det V)^2\): left multiplication acts
separately on two columns and right multiplication on two rows.
This computes the full determinant, not a selected matrix direction.

Differentiating the fixed-q inverse, with \(P=I-B\), gives
\[
D\Theta_q(B)[H]=P^{-1}HP^{-1}K_q,\qquad
J_q(B)=\frac{|\det K_q|^2}{|\det(I-B)|^4}>0 .
\]
It is finite at EVERY point of its open germ domain.
The forward derivative, equivalently obtained from \(I-K_qM^{-1}\), is
\[
DF_q(A)[H]=K_qM^{-1}HM^{-1},\qquad
d_q(A)=|\det_{\mathbb R^4}DF_q(A)|
      =\frac{|\det K_q|^2}{|\det(A+C)|^4}.
\]
Since \(\det(I-F_q(A))=\det K_q/\det(A+C)\), these two full-dimensional
formulas give \(J_q(F_qA)=1/d_q(A)\). Thus the declared geometry really
does ensure four-dimensional regularity at every admitted fractional source.

For L the inverse derivative is \(H\mapsto HC\), so its OWN full
four-dimensional determinant is \(J^L_q=(\det C)^2=4\).
The actual forward determinant is 1/4, everywhere on its own legal source.
This derivation does not import the fractional determinant or domain.

Every actual inverse is a Borel restriction of the corresponding open-set
analytic diffeomorphism (globally affine for L). Change of variables gives
\[
\mu(\theta E)=\int_E|\det D\theta|\,d\mu
\]
for EVERY Borel subset E of its actual target domain. The identity holds
also for unbounded or null sets, by nonnegative integration/restriction.
The fixed-label germ supplies the prescribed values at assigned floor faces;
no a.e.-only representative is repaired at an eventual periodic point.
Actual source labels are unique, so equivalent descriptions have the same J.
Different inverse sources over one target may have different densities.

Consequently the OWN clocks are
\[
\kappa_{\rm M/G}(A)
=2\log|2-q_O(A)^2|-4\log|\det(A+C)|,\qquad
\kappa_L(A)=-\log4 .
\]
They are finite at every legal source; a terminal has no next-step clock.
No positivity restriction, external roof or global time change is imposed.
Branchwise IMAGE does not assert global injectivity or whole-map measure
preservation for a potentially many-to-one map.

## 4. Full histories, kernels, isotropy and unrestricted incoming

For each owner let \(P_O(B)\) be ALL its actual inverse points from Section 2,
and set \(P_O^0(B)=\{B\}\),
\(P_O^{j+1}(B)=\bigcup_{A\in P_O^j(B)}P_O(A)\).
The inverse identities prove by induction that these are exactly the
legal j-step starts into B. All source labels and all depths remain.
This is exact countable inverse recursion, not a finite-basin claim.

Set \(d_O=e^{\kappa_O}\), \(M_r(A)=\prod_{i=0}^{r-1}d_O(T_O^iA)\),
\(M_0=1,S_r=\log M_r\) on finite legal histories. Define the full groupoid
\[
\mathscr G_O=\{(A,r-s,B):T_O^rA=T_O^sB,\ r,s\ge0
                                  \text{ with both histories legal}\}.
\]
Equal triples, not extra witness labels, are identified; source is B.
The equal-iterate relations are Borel and the full inverse atlas gives
countable source/range fibres. Inversion reverses endpoints and lag.
Composition aligns the two middle histories at the longer already legal
middle time; this proves closure and lag addition without extending a terminal.
For two witnesses of one triple, the longer adds the SAME legal common
tail to both ends. Its products cancel, proving that
\[
c_O(A,r-s,B)=S_r(A)-S_s(B)=\log(M_r(A)/M_s(B))
\]
is well-defined. The same middle-time cancellation proves additivity.
The forward arrow \((T_OA,-1,A)\) has value \(-\kappa_O(A)\).
Composition of actual branch charts gives source-to-range history IMAGE
density \(M_s(B)/M_r(A)=e^{-c_O}\); countable disjoint Borel restrictions
cover all actual history charts and their assigned null faces.

The COMPLETE kernels are
\[
\begin{aligned}
\ker\ell&=\{(A,0,B):T_O^rA=T_O^rB\text{ for some legal }r\},\\
\ker c&=\{(A,r-s,B)\in\mathscr G_O:M_r(A)=M_s(B)\},\\
\ker\ell\cap\ker c
 &=\{(A,0,B):T_O^rA=T_O^rB,\ M_r(A)=M_r(B)
                                      \text{ for some legal }r\}.
\end{aligned}
\]
No nonunit coalescence is deleted. For L specifically,
\(c_L=-\ell\log4\), so \(\ker c_L=\ker\ell_L\) and the joint kernel is
the same full equal-level relation, not asserted to consist only of units.

All incoming at range A are exactly
\[
(A,r-s,B),\quad r\text{ legal at }A,\quad s\ge0,\quad
B\in P_O^s(T_O^rA).
\]
At range height h the source height is \(h-c_O\). At a terminal only r=0
is allowed; all backward words, zero-depth identities and their sources stay.

A nonzero self-lag is equivalent to an eventually periodic legal future.
Repeated legal states force an indefinitely repeatable cycle; an eventual
least cycle of period p supplies all multiples of p. Advancing any other
equality to that core shows these are ALL self-lags.
If K is its once-around clock sum, then
\[
\mathscr G_{O,A}^{A}=p\mathbb Z,\qquad H_A=K\mathbb Z.
\]
Entrance sums cancel; non-eventually-periodic and finite-terminal histories
have trivial source isotropy and H=0. The full \(X\times\mathbb R\) extension
retains exactly \(\{kp:kK=0\}\) of the source isotropy at each height.
Transport to a reference b by any actual arrow \(g_A:A\to b\) gives phase
\(h+c(g_A)\bmod H_b\), independent of that choice modulo the WHOLE H.
Height translation on the orbit SET has stabilizer H; no nice quotient
or selector is needed. For K!=0 the primitive is |K| and repetitions are
its positive integer multiples. H=0 has all real phases and no positive time,
even if zero-clock source isotropy remains.

For L an eventual least p-cycle, IF present, has \(K=-p\log4\),
entire \(H=p\log4\,\mathbb Z\) and trivial extension isotropy.
This is a conditional consequence of its own constant clock, not a census
or existence assertion about L cycles outside the frozen fixed window.

## 5. EVERY fractional fixed matrix in W

Write \(A=\begin{pmatrix}a&b\\c&d\end{pmatrix}\).
On the full prescribed W, \(2\le a,b<3\), m=n=2.
Thus MAIN's actual quotient and G's actual floor quotient are both q=1.
The fixed equation, after multiplication on the RIGHT by A+C, is
\[
A^2+A(C-I)-J=0.
\]
Its four scalar equations, without any matrix ansatz, are
\[
a^2+bc=0,\qquad b(a+d+1)=1,\qquad
c(a+d)=1,\qquad bc+d^2+d=0 .
\]
Since b>0, the first gives \(c=-a^2/b\).
Put s=a+d. The second gives \(s=1/b-1\), and the third then forces
\(a^2=b^2/(b-1)\). Since a>0, this fixes the positive a, not a selected
root among additional admissible negative values.
Set \(u=\sqrt{b-1}\in[1,\sqrt2)\). All entries are now forced:
\[
b=u^2+1,\quad a=u+u^{-1},\quad
c=-1-u^{-2},\quad s=-u^2/(u^2+1),\quad d=s-a .
\]
The last scalar equation is \(s(s+1)-a(2s+1)=0\), equivalently
\[
P(u)=(u^2-1)(u^2+1)^2-u^3
     =u^6+u^4-u^3-u^2-1=0 .
\]
At u=1 it is -1, and at u=sqrt2 it is \(9-2\sqrt2>0\).
For u>=1,
\[
P'(u)=(6u^5-3u^2)+(4u^3-2u)>0,
\]
since the first bracket is at least \(3u^2>0\) and the second at least 2u.
The intermediate value theorem and strict increase give exactly one root
\(u_0\in(1,\sqrt2)\). These statements are exact, not numerical root finding.

Conversely the displayed entries at u_0 satisfy all four equations,
by reversing the substitutions. They lie in W:
\(2<b<3\), and \(2<a<\sqrt2+1/\sqrt2=3/\sqrt2<3\).
No lower-face point was lost, since u=1 fails the last equation; upper
faces are excluded as required, and c,d were unrestricted throughout.
There are no other matrix roots in W.

Every solution of this fixed equation also satisfies
\((A-I)(A+C)=J-C=-K_1\). Its right side is invertible, so both
A-I and A+C are invertible. Thus the unique root actually satisfies
all MAIN/G geometry, as well as their own arithmetic readings.
Let \(F=A(u_0)\). Then exactly
\[
\operatorname{Fix}(T_{\rm M})\cap W
=\operatorname{Fix}(T_G)\cap W=\{F\}.
\]
These are separate owned fixed cores; equality of the matrix does not
identify their unrestricted incoming packets.

## 6. L's complete fixed window and F's exact clock

For L, the actual quotient on W is also q=1. Its fixed equation is
\(AC=A+J\), or \(A(C-I)=J\).
The left first column is zero, whereas J's first column is (0,1)^T.
This is impossible for EVERY a,b,c,d. Hence
\(\operatorname{Fix}(T_L)\cap W=\varnothing\).
No fractional geometric guard was used in this complete L classification.
Its general full-source inverse/history ledger above remains, despite an
empty fixed window. No absence of all L cycles is concluded.

For the fractional core put u=u_0 and s=-u²/(u²+1). Since bc=-a²,
\(\det F=a(a+d)=as=-u\).
The actual denominator determinant is therefore
\[
R=\det(F+C)=\det F+2a+d+2
           =1+\frac1u+\frac1{u^2+1}>1 .
\]
Here \(\det K_1=1\). The FULL four-entry determinants and own core clock are
\[
d_{\rm M/G}(F)=R^{-4},\qquad
J_{\rm actual}(F)=R^4,\qquad K_*=\kappa_{\rm M/G}(F)=-4\log R<0 .
\]
The exponent four is the native full-dimensional IMAGE exponent, not a
normalization chosen to fit the arithmetic target.

## 7. Entire fixed-core packets, incoming and phases

For each fractional owner separately the EXACT full packet of F is
\[
\mathcal B_O(F)=\bigcup_{j\ge0}P_O^j(F).
\]
The preceding all-label inverse formulas and source checks specify every
term exactly; incoming is not restricted to W, q=1 or the fixed ansatz.
Every arrow relating a source to the constant future F is precisely eventual
entry to F. Thus the recursion proves equality to the WHOLE source packet,
not a selected invariant subset or finite-basin assertion.

For A in that basin let d(A) be first entry time,
\(\eta(A)=S_{d(A)}(A)\), and \(v(A)=\eta(A)-d(A)K_*\).
After entry \(S_r(A)=v(A)+rK_*\). Every pair of basin sources admits
EVERY integer lag k by comparing sufficiently late iterates at F, and
\[
c_O(A,k,B)=v(A)-v(B)+kK_* .
\]
This determines the full basin kernels: lag kernel k=0, clock kernel
\(v(A)-v(B)+kK_*=0\), and joint kernel \(k=0,v(A)=v(B)\).
Every basin source has source isotropy Z and ENTIRE \(H=K_*\mathbb Z\);
its extension isotropy is trivial. No entrance clock or alternate inverse
path can shrink the generator: its contribution cancels on each self-arrow.
The full phase is \(h-\eta(A)\bmod K_*\mathbb Z\), equivalently h-v(A).
At (F,h), ALL incoming source heights from A are \(h+v(A)-kK_*\).
Thus the whole physical packet has all phases
\(\mathbb R/(4\log R)\mathbb Z\), primitive \(4\log R=\log R^4\),
and positive repetitions \(j\,4\log R\). No phase is selected or merged
with a different source packet just because its length agrees.
L has no found fixed core in W; its unrestricted general incoming and
conditional cycle/phase statements in Section 4 fulfill its remaining ledger.

## 8. Exact integer-prime exclusion and decisive stop

It remains to decide whether R^4 is an ordinary integer prime, not to
approximate it. Put \(w=u-u^{-1}\). Dividing P(u)=0 by u³ gives
\[
(u-u^{-1})(u+u^{-1})^2=1,\qquad w^3+4w-1=0 .
\]
Also the fixed identity gives \(\det(F-I)\det(F+C)=1\), so
\(\det(F-I)=R^{-1}\). Using det F=-u and trace F=s yields
\[
R+R^{-1}=3-w.
\]
Consequently \(z=R+R^{-1}\) satisfies
\(z^3-9z^2+31z-38=0\). Multiplication by R³ gives the exact monic relation
\[
\Phi(R)=R^6-9R^5+34R^4-56R^3+34R^2-9R+1=0 .
\]
No irreducibility or approximate root isolation is needed for the next step.

Here is an elementary integer-exclusion argument with its algebraic proof.
Let E be the six-by-six integer coefficient matrix with ones on the
superdiagonal, zero other entries in the first five rows, and final row
\((-1,9,-34,56,-34,9)\). Its determinant is 1, by the unique nonzero
permutation using its first column and the first five rows.
The nonzero vector \((1,R,R^2,R^3,R^4,R^5)^T\) is an eigenvector
with eigenvalue R, exactly by \(\Phi(R)=0\). Thus R^4 is an eigenvalue
of E^4. The polynomial \(\det(tI-E^4)\) is monic with integer coefficients
and constant term \(\det(-E^4)=1\).
If its root R^4 were an integer N>1, substituting and reducing modulo N
would give \(1=0\pmod N\), impossible.
This finite coefficient-matrix argument is solely a proof of the algebraic
integer exclusion; it is not added to the candidate as an operator/trace owner.
Since R>1, it proves R^4 is NOT ANY integer, in particular not a prime.

MAIN has a genuine positive primitive \(\log R^4\) in its COMPLETE fixed
packet, with a proved noninteger exponent. Its mandatory ordinary-prime
purity therefore fails: STOP / FORK.
This is not a missing-positive-ledger argument, numerical observation,
selected loop or claim that a longer census could remove the wrong packet.
G separately retains its own same fixed matrix and wrong clock without
the arithmetic gate; it supplies no MAIN arithmetic credit.
L has its own complete clock/history law and empty fixed window, not a
replacement clock or proof that all its periodic data are absent.

The same full source, three own laws, native measure, point versions,
all inverse branches, retained lag, incoming, phases and repetitions remain.
Strong naturalness/PROVES_TOO_MUCH are not rescued by the nonlinear clock.
Changing the time exponent, measure, readout, window or selected direction
would require a new owner, not preserve this stopped candidate.
Arithmetic T1 NOT PASSED; T3 NOT AUDITED; classical NOT APPLICABLE;
formal Route UNASSIGNED; B NOT INVOKED.
Higher periods, outside-window fixed points and coverage are unclassified;
none can erase this retained necessary-target violation.
EOF — freeze after full self-read; HOLD for root's full read and DISTINCT PAPER UNLOCK.
