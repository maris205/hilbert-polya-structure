# 411 — card-only independent raw derivation

Candidate: ANG-20260923-DSS01. Date: 2026-09-23.
Batch NONLINEAR-LIFT-20260923-M; internal shared-history NOT_CALIBRATED.
Root reported reading the entire CP1 report and explicitly released the frozen mathematical contract.
Sole current scientific input: candidate-card.md, complete lines 1–95 through actual EOF, reread after release.
candidate-card.md: 95 lines; SHA256 c399cf94479cedf0699a5a9500a0a2650492c06c141c31c9de117362bddbbd40
Frozen scope-review.md: 81 lines; SHA256 3ad55dd8951731fabe9e63f8e63654ab2640fd85b786b1dea7d0a93de5c9868e
No current author paper, README, ledger, peer, sibling or old scientific file was read.
Prior shared project history remains exposed; this is independent card-only work, not blind, external, human or cross-model verification.
The completely read ARS instructions and relevant workflow/role/runtime references remain retained, not represented as freshly reread here.
AI supplies the derivation and internal checking. No scientific code, numerical experiment, literature search, helper agent, Git action or higher-period census was used.

## 1. Whole sources and exact source-checked inverse atlas

Every owner retains all $X=\operatorname{Sym}_2(\mathbb R)$, $A=\begin{pmatrix}x&y\\y&z\end{pmatrix}$, with $\mu=dx\,dy\,dz$.
Let $m=\lfloor x\rfloor$, $n=\lfloor\det A\rfloor$ and $D=\{\det A\ne0,\operatorname{tr}A\ne0,m\ne0,m\mid n\}$.
MAIN uses $q=n/m$ and $T(A)=A^2-qI$ on D.
G uses $D_G=\{\det A\ne0,\operatorname{tr}A\ne0\}$ and $q_G=\lfloor n/m\rfloor$ for $m\ne0$, $q_G=0$ for $m=0$.
Q uses $D$ and $T_Q(A)=A^2$; S uses $D$ and $T_S(A)=A-qI$.
These are Borel domains and Borel partial maps: each integer readout is Borel and each quotient branch is polynomial.
Every failed permission remains a terminal with identity and actual incoming, not an absorbing loop.

Fix an integer branch value k for MAIN or G and a target B.
If a real symmetric legal A satisfies $A^2=B+kI$, then $A$ commutes with B and $A^2$ is positive definite because $\det A\ne0$.
For distinct eigenvalues $\beta_+>\beta_-$ of B this forces both $\beta_\pm+k>0$ and, with their orthogonal projectors,
\[
A=\epsilon_+\sqrt{\beta_++k}\,P_+
 +\epsilon_-\sqrt{\beta_-+k}\,P_-,\qquad \epsilon_\pm\in\{1,-1\}.
\]
Commutation and the one-dimensional eigenspaces prove exhaustion of all such roots, not just construction of some roots.
If $B=\beta I$, put $\lambda=\beta+k$.
For $\lambda<0$ no real symmetric square root exists; for $\lambda=0$ every such root is zero and fails determinant permission.
For $\lambda>0$, the eigenvalues of a symmetric root are each $\pm\sqrt\lambda$.
Mixed signs give trace zero and fail the frozen source condition, for EVERY orthogonal choice of eigendirections.
Equal signs give exactly $A=\pm\sqrt\lambda I$. Thus the omitted scalar-target continuum is illegal for the stated reason, not silently deleted.

For every enumerated root, retain it iff its own complete source permission holds and its own quotient is k.
Then $A^2-kI=B$ is the actual forward identity; conversely any actual predecessor supplies exactly such k and root.
This is an untruncated all-integer-k atlas. A source repeated by equivalent chart descriptions is identified, not a new arrow.
Different k cannot name the same actual source at the same target, since its owned quotient is unique.
Targets need not possess a next forward step.
Q uses this square-root construction ONLY at k=0, followed by its own D check; its readout q is not a second inverse label.
S enumerates all $A=B+kI$, $k\in\mathbb Z$, retaining precisely the own source checks and $q(A)=k$.
Substitution proves both inverse identities and exhaustion for S as well.
Every target has at most countably many predecessors in each owner; global injectivity is NOT asserted.

## 2. Complete analytic charts, agreement and every-Borel IMAGE

For same-sign square roots put $C=B+kI>0$.
The positive square-root matrix has the explicit formula
\[
C^{1/2}=\frac{C+\sqrt{\det C}\,I}
 {\sqrt{\operatorname{tr}C+2\sqrt{\det C}}}.
\]
Cayley–Hamilton verifies its square, and its positive eigenvalues identify it as the positive root.
All radicands and the denominator are positive on the positive-definite cone, so this formula and its negative are real analytic there.
In particular these charts extend through EVERY admitted scalar target, not merely through the simple-spectrum locus.
For mixed-sign roots use the open set where $C>0$ and B has distinct eigenvalues.
Writing $\delta=\sqrt{(B_{11}-B_{22})^2+4B_{12}^2}>0$ gives analytic eigenvalues $(\operatorname{tr}B\pm\delta)/2$ and analytic projectors $P_+=(B-\beta_-I)/\delta$, $P_-=(\beta_+I-B)/\delta$.
The two mixed-sign formulas are therefore analytic on that open set.
Their reconstructed traces cannot vanish: opposite signs would cancel only if the two shifted eigenvalues were equal.
Together these four charts per integer k cover all admitted square roots; no scalar mixed-sign chart is missing from the legal source.
Q requires only the four k=0 charts. S has the entire analytic translations $B\mapsto B+kI$.

On a fixed square branch, differentiating $F_k(A)=A^2-kI$ in the real coordinates gives
\[
DF_k(A)=
\begin{pmatrix}
2x&2y&0\\
y&x+z&y\\
0&2y&2z
\end{pmatrix},\qquad
\det_{\mathbb R^3}DF_k(A)=4(xz-y^2)(x+z).
\]
It is nonzero at EVERY legal source, including integer-floor cuts.
Hence every stated inverse chart has invertible derivative and is a diffeomorphism onto its image on its ambient open chart.
Injectivity on a fixed inverse chart also follows directly from $F_k\theta(B)=B$.
Its actual inverse domain is the Borel subset selected by the reconstructed source checks.
On it the prescribed all-point inverse density is
\[
J_{\rm MAIN}=J_G=J_Q=
\frac{1}{4|\det A\,\operatorname{tr}A|},\qquad A=\theta(B).
\]
This formula is evaluated at that owner's actual predecessor, not summed over branches.
For S the analytic translation has $J_S=1$ at every actual target.
All these values are finite and strictly positive, on null cuts and scalar cuts as well as interior points.

Descriptions that yield the same actual source have the same branch k and the same local inverse of its nonsingular polynomial map.
Thus their derivatives agree; alternatively the displayed determinant formula gives the same value immediately.
For every Borel subset E of any actual inverse domain, change of variables on the ambient analytic chart proves
\[
\mu(\theta(E))=\int_E J(B)\,d\mu(B).
\]
Restrictions with zero Lebesgue measure are included. The explicit analytic rule specifies the point version there; IMAGE alone does not uniquely choose arbitrary null values.
No measure, coordinate count, source restriction or null-point clock has been substituted.
Define the owned positive forward factor and legal-step clock by
\[
d_O(A)=4|\det A\,\operatorname{tr}A|\quad(O={\rm MAIN},G,Q),
\qquad d_S(A)=1,\qquad \kappa_O(A)=\log d_O(A).
\]
This is precisely $-\log J_O(T_OA)$. No step clock is assigned outside the source domain.

## 3. All actual finite histories, kernels and isotropy

All constructions in this section use each owner's own domain and untruncated atlas.
Put $R_j(A)=\prod_{i<j}d_O(T_O^iA)$ on legal histories, $R_0=1$ and $S_j=\log R_j$.
The actual arrow set is the frozen set
\[
G_O=\{(A,r-s,B):T_O^rA=T_O^sB,\ r,s\ge0,\ \text{both histories legal}\}.
\]
It is Borel by countably many legal-iterate equality sets and has countable source/range fibres by the inverse atlas.
Source is B and range is A. Equal triples are identified, while integer lag remains.
For two presentations of the same triple, the indices differ by a common integer.
Their longer legal common tail contributes the same factors to numerator and denominator, proving descent of
\[
c(A,r-s,B)=\log\frac{R_r(A)}{R_s(B)}.
\]
Alignment on the longer existing middle history proves composition and additivity without extending a terminal beyond its lifetime.
Inversion negates c. The finite inverse-history density is $R_r^{-1}$, and the source-to-range branch-pair density is $R_s(B)/R_r(A)=e^{-c}$.
The chain rule and every-Borel change of variables prove these statements on all actual history restrictions, with the same compatible point versions.

The COMPLETE kernels are
\[
\begin{aligned}
\ker\ell&=\{(A,0,B):\exists r\text{ legal},\ T_O^rA=T_O^rB\},\\
\ker c&=\{(A,r-s,B)\in G_O:R_r(A)=R_s(B)\},\\
\ker\ell\cap\ker c
 &=\{(A,0,B):\exists r\text{ legal},\ T_O^rA=T_O^rB,\ R_r(A)=R_r(B)\}.
\end{aligned}
\]
They are presentation independent by descent; no unit-kernel assertion is borrowed from a different partial map.
For example take $A=\operatorname{diag}(1,1/2)$ and $-A$.
Both have n=0, m=1 or -1, legal determinant/trace, and quotient zero for MAIN/G; Q ignores that quotient.
Their square images coincide and their factors are both 3.
Thus $(A,0,-A)$ is an actual nonunit arrow in BOTH kernels and their intersection for MAIN, G and Q.
This one-step coincidence is not a closed primitive of time log(3).
For S, c is identically zero on its entire groupoid, so $\ker c=G_S$ and the intersection equals its full lag kernel.

For a deterministic partial map, nonzero self-lag is equivalent to an eventually periodic legal tail.
Indeed two equal distinct-time iterates produce such a tail, and a legal cycle supplies all its repeated self-lags.
If the least eventual source period is r, the entire source isotropy is $r\mathbb Z$.
Let $C=\sum_{i=0}^{r-1}\kappa_O(T_O^iu)$ on its least periodic core.
Preperiodic sums cancel, and every multiple of r is realized after reaching the cycle; hence the ENTIRE $H_A=C\mathbb Z$.
At a state without an eventually periodic tail, source isotropy and H are zero.

The full extension keeps every $(A,h)\in X\times\mathbb R$ and sends $(B,h)$ to $(A,h+c)$.
Its kernels lift the preceding full kernels with every height.
At an eventual period-r state its isotropy is $\{kr:kC=0\}$: all $r\mathbb Z$ when C=0 and trivial otherwise.
Non-eventually-periodic states have trivial extension isotropy.
The complete phase set over a source class is $\mathbb R/H_A$, because two transports to a reference point differ exactly by a self-arrow clock.
Height translation on the orbit SET has stabilizer H; if C is nonzero, the primitive is $|C|$ and repetitions are $k|C|$, $k\ge1$.
If H=0 there is no positive time, even when ineffective source/extension isotropy survives; phases form a free real line.
Equal times never identify different source classes. No quotient topology or positive-roof suspension is claimed.

At arbitrary A, all incoming arrows are obtained by choosing every legal r, then every length-s actual inverse history from $T_O^rA$.
Its start B gives $(A,r-s,B)$, with source height $h-c(A,r-s,B)$ for target height h.
This exhausts incoming arrows by their definition, with no depth or integer cutoff; terminal A permits r=0 and retains all such predecessors.

## 4. COMPLETE fixed sets of MAIN and G for every integer quotient

At a fixed point with actual integer quotient q,
\[
A^2-A=qI.
\]
Each eigenvalue solves $t^2-t-q=0$, so $1+4q\ge0$ and integer q must be nonnegative.
For q=0, invertibility leaves only $A=I$; MAIN and G both actually read q=1 there, so it is not their fixed point.
For q>=1 put $a_q=(1+\sqrt{1+4q})/2$, $b_q=(1-\sqrt{1+4q})/2$.
Every symmetric solution is scalar at one of these roots, or has both eigenvalues and therefore trace 1 and determinant -q.
This spectral dichotomy includes all orthogonal orientations, not only diagonal representatives.

For a scalar $A=tI$, m=floor(t) and $n=\lfloor t^2\rfloor=q+m$.
MAIN fixedness requires $qm=q+m$, equivalently $(q-1)m=q$.
There is no q=1 solution; for q>=2 the integer $m=1+1/(q-1)$ forces q=2,m=2.
Of its two algebraic roots, only t=2 has that floor.
Thus MAIN's only scalar fixed point is $2I$.
For G and a negative scalar root, m<0 gives $\lfloor1+q/m\rfloor\le0$, inconsistent with q>=1.
For a positive root, m>=1 and fixedness requires $\lfloor q/m\rfloor=q-1$.
If m=1 this is impossible. If m>=2 then $q-1\le q/m\le q/2$, forcing q<=2.
The q=1 positive root lies strictly between 1 and 2 and has m=1, already excluded; q=2 gives t=2,m=2 and is admitted.
So G separately has the same sole scalar fixed point. Its m=0 rule cannot add a scalar fixed point: none of these nonzero algebraic roots has that floor.

For a mixed-eigenvalue solution, n=-q is an exact integer.
MAIN's equation $n/m=q$ forces m=-1.
For G, m=0 gives q_G=0, m>0 gives a negative q_G, and m=-h<0 gives $q_G=\lfloor q/h\rfloor$.
Equality to positive q forces h=1 and is then satisfied. Thus G also requires exactly m=-1.
Consequently BOTH COMPLETE fixed sets, separately source-checked, are
\[
\operatorname{Fix}(T_{\rm MAIN})=\operatorname{Fix}(T_G)
=\{2I\}\ \cup\ \bigcup_{q=1}^{\infty}\mathcal F_q,
\]
where
\[
\mathcal F_q=
\left\{\begin{pmatrix}x&y\\y&1-x\end{pmatrix}:
-1\le x<0,\quad y^2=q+x-x^2\right\}.
\]
The requirement that y be real is part of this formula; equivalently
\[
\max(-1,b_q)\le x<0,\qquad y=\pm\sqrt{q+x-x^2},
\]
with the two signs representing just one matrix where y=0.
Conversely every displayed matrix has trace 1, determinant -q, m=-1 and its required own quotient q.
Cayley–Hamilton gives $A^2-A=qI$, proving actual fixedness and exhaustion.
No q cutoff is present. Each $\mathcal F_q$ contains a continuum, for example along $-1/2<x<-1/4$ where the radicand is positive.
All orientations satisfying the actual source permission remain; no conjugacy class is collapsed.

## 5. COMPLETE fixed sets of Q and S

For Q, symmetric fixedness $A^2=A$ and nonzero determinant force $A=I$.
It satisfies its OWN source gate m=n=1, so $\operatorname{Fix}(T_Q)=\{I\}$.
Its quotient readout is 1 but that integer does not index its quotient-free inverse.
For S, fixedness is equivalent to its OWN q=0.
Since m is nonzero on D, this is exactly n=0; with nonzero determinant the full fixed set is
\[
\operatorname{Fix}(T_S)
=\{A:0<\det A<1,\ \operatorname{tr}A\ne0,\ \lfloor x\rfloor\ne0\}.
\]
Every such source is legal because its nonzero signed m divides zero; conversely every S fixed point is in this set.
The trace condition is retained as frozen, whether or not it is redundant here.
No point on a failed determinant or floor permission becomes an absorbing fixed point.
S has clock zero on EVERY legal step, not merely at these fixed points.
Hence its H is zero everywhere and it has no positive time packet; all possible source isotropy remains in the extension.
This is not a claim that S has no source cycles.

## 6. Entire fixed-core basins, all incoming, clocks and packet multiplicity

For any owner define the fully explicit predecessor set $\mathcal P_O(B)$ by Section 1's all-integer spectral/translation formulas AND own source tests.
Set $\mathcal P_O^0(B)=\{B\}$, $\mathcal P_O^{j+1}(B)=\bigcup_{C\in\mathcal P_O^j(B)}\mathcal P_O(C)$.
For each actual fixed core B the ENTIRE source class is exactly
\[
\mathcal B_O(B)=\bigcup_{j\ge0}\mathcal P_O^j(B).
\]
One inclusion follows by forward iteration; for the other, any common-future arrow with a fixed endpoint forces the other endpoint to reach that fixed point.
This is an exact untruncated set prescription for every incoming state, with only the already explicit integer and source checks; no additional unexplained branch selection remains.
Each such basin is countable, although there are continuum many distinct fixed cores.
Two distinct fixed cores cannot share a source class, since their forward histories remain their distinct fixed values.

Let $d(A)$ be the first hitting time of B from $A\in\mathcal B_O(B)$, let $K=\kappa_O(B)$, and put
\[
\eta(A)=S_{d(A)}(A),\qquad v(A)=\eta(A)-d(A)K.
\]
For any A,C in that basin and EVERY integer j, $(A,j,C)$ is an actual arrow: choose sufficiently long meeting times after both have reached B.
Extending any other presentation to those meeting times proves the full formula
\[
c(A,j,C)=v(A)-v(C)+jK.
\]
Thus all source isotropy is Z, entire H is $K\mathbb Z$, and extension isotropy is Z if K=0 and trivial if K differs from zero.
At target $(B,h)$ all incoming arrows from A have source height $h+v(A)-jK$.
The reference phase of $(A,h)$ is $h-\eta(A)$ modulo $K\mathbb Z$, equivalently $h-v(A)$; when K=0 this is an ordinary real height.
The basin lag kernel consists of all $(A,0,C)$; its clock-kernel intersection imposes $v(A)=v(C)$.
The full clock kernel in this basin imposes $v(A)-v(C)+jK=0$.
These formulas retain every incoming point, phase, zero-clock arrow and integer lag.

MAIN and G have, from their own derivatives,
\[
K(2I)=\log64,\qquad K(B)=\log(4q)\quad(B\in\mathcal F_q).
\]
All are positive; each actual fixed matrix supplies ONE full phase circle and ONE primitive packet of that time, with positive integer repetitions.
For each q there are continuum many distinct such source packets; identical eigenvalues or times do not identify them.
Their incoming basins and phases are exactly the all-integer formulas above, using MAIN and G's DIFFERENT permissions.

For clarity, the scalar-core basin can be evaluated completely in both owners.
Any predecessor of a scalar target is scalar, by the scalar-root proof.
For a MAIN predecessor $tI$ of $2I$, write $t^2=2+k$ with integer k and m=floor(t).
Its permission and quotient equation give $k(m-1)=2$.
The integer possibilities k=1,-1,2,-2, with their actual root floors and nonzero conditions, leave only $t=2,-1$.
A predecessor of $-I$ would have $t^2=k-1>0$ and $k(m-1)=-1$, impossible for the resulting integer k>=2.
For G a predecessor of $2I$ has $t=\pm\sqrt a$, integer a>=1, and quotient k=a-2.
A negative root gives negative q_G, so a<2 and only t=-1 survives.
A positive root has m>=1. The m=1 equation $\lfloor a/m\rfloor=a-2$ is impossible; m>=2 forces $a-2\le a/2$, hence a<=4 and $a\ge m^2\ge4$, leaving t=2.
A G predecessor of $-I$ would require $\lfloor a/m\rfloor=a+1$, impossible for positive m, while negative m gives a negative quotient.
Thus EACH scalar fixed core $2I$ has full basin $\{2I,-I\}$.
The entrance factor at -I is 8, so its one-step clock is log(8), but the ENTIRE isotropy image at either basin point is log(64)Z.
The entrance half-clock is not a smaller self-return: here $v(2I)=0$ and $v(-I)=\log8-\log64=-\log8$.

For Q, predecessors of I are exactly I and -I; both pass Q's own source gate.
There is no real symmetric square root of -I, so its fixed-core basin is exactly $\{I,-I\}$.
Q's factor at both points is 8, hence K=log(8), v=0 at both, entire H=log(8)Z, trivial extension isotropy and one full phase circle.
Its cross-point lag-zero arrows also have zero clock; none is discarded.

For S, the preceding general basin formulas specialize to K=0 and v=0.
They can also be specified entirely on an integer translate set for each fixed B.
Write $\delta=\det B$, $t=\operatorname{tr}B$, $m_0=\lfloor B_{11}\rfloor$ and $A_k=B+kI$, k an arbitrary integer.
Then $\det A_k=\delta+kt+k^2$, $\operatorname{tr}A_k=t+2k$, and its divisor floor is $m_0+k$.
At legal $A_k$, define $q_k=\lfloor\delta+kt+k^2\rfloor/(m_0+k)$ with the OWN nonzero and divisibility tests.
The actual update is $A_k\mapsto A_{k-q_k}$.
The complete basin is precisely the indices whose finite legal iteration $k\mapsto k-q_k$ reaches zero; every possible predecessor must be an integer translate by the S inverse formula.
All integer lags occur between any two points of this basin, all clocks are zero, source and extension isotropy are Z, and phases are the full free real line.
These fixed continua therefore contribute no positive packet; they are not deleted for that reason.

## 7. Exact lineage and decisive bounded result

For the frozen integers N>=2 and 1<d<N, the matrix
\[
A=\begin{pmatrix}d&1\\1&(N+1)/d\end{pmatrix}
\]
has determinant N, positive trace, and readouts m=d,n=N.
Its MAIN source permission is exactly d divides N; the real matrix then undergoes its actual square and quotient translation.
This proves the stated proper-divisor interface without replacing X by this zero-measure family or importing a prime table.
The next matrix supplies new readouts; strong naturalness and arbitrary-encoding risks remain OPEN.

MAIN has the legal fixed core $2I$, with its proved entire H=log(64)Z.
Its primitive multiplier 64 is composite, so its positive primitive time is not log of an ordinary integer prime.
This ONE actual full packet already violates the necessary target and decides STOP / FORK.
Independently the complete families $\mathcal F_q$ have primitive multiplier 4q, also composite for every q>=1, with their full continuum multiplicities retained.
No claim is needed about higher-period existence, prime support elsewhere or ultimate coverage; those remain unclassified.
G and Q have their own wrong-time fixed packets, while S has its own zero-clock full owner. These controls do not replace the MAIN counterexample.

T0 and the specified same-transport analytic IMAGE clock are established for all four owners, including scalar and floor cuts.
T2's necessary MAIN prime-time target FAILS; stronger naturalness is OPEN.
Classical NOT APPLICABLE; T3 NOT AUDITED; formal UNASSIGNED; Route B NOT INVOKED.
The decision is this frozen object's STOP / FORK, not a theorem against all symmetric-matrix arithmetic constructions.
The decisive MAIN result was sent to root before this report was written.
Raw now freezes for root's full read; no author-surface access occurs before a separate PAPER UNLOCK.

EOF — exact card-only independent raw; complete fixed window, no higher-period census.
