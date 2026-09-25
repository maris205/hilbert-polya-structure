# 470 GMR01 — card-only independent mathematical derivation

Candidate ANG-20260925-GMR01; batch SYMBOLIC-RETURN-20260925-Y, round1/5.
Input: candidate-card.md, original111 lines, personally reread1–111 through EOF after DISTINCT RAW RELEASE.
Input SHA256: 6dee0423864ea121b7b475c302e1f3dd7fa06f4c9e5c953ab7e53bdc771b0f50.
CP1 scope-review.md remains frozen:77 lines, SHA256 22663d6bcdf540003b1e0f33c40644c3e83c14908f9d8838a5f4d84747426916.
Only that card is new scientific input. No current author paper/README/ledger, peer/helper result, old proof or appended Outcome was read.
Prior shared465 and earlier gcd-owner history remain exposed as recorded in CP1; no old result is imported as a lemma.
Inherited same-model internal work is NOT_CALIBRATED, not blind, human, external or cross-family verification. No helper was used.
Method: exact affine change of variables, integer inequalities and unrestricted finite-history arguments; no scientific code, numerical census, network, Git, PDF or extra return gate.

## 1. All four original owners and complete inverse domains

Keep Y=Z×R² with its original counting×Lebesgue2 measure mu. For every integer pair define
Gamma(m,n)=gcd(|m|,|n|), except Gamma(0,0)=1, and q(n)=Gamma(n,n)=max(1,|n|).
Introduce coefficients only as notation for the frozen maps:

| U | d_U(m,n) | b_U(m,n) |
| --- | --- | --- |
| M | Gamma(m,n) | m |
| C | 1 | m |
| K | Gamma(m,n) | 0 |
| R | q(n) | n |

Then T_U(m,x,y)=(n,y,(x+b_U(m,n))/d_U(m,n)), where n=floor(x).
All d are positive integers, so these are total Borel maps on the entire Y; no states, signs, axes or integer faces are removed.
For each m,n in Z let
I^U_{m,n}=[(n+b_U(m,n))/d_U(m,n),(n+1+b_U(m,n))/d_U(m,n)),
Omega^U_{m,n}={n}×R×I^U_{m,n}, and theta^U_{m,n}(n,u,v)=(m,d_U(m,n)v-b_U(m,n),u).
These Borel domains are the full actual domains, not just sufficient subdomains: their defining inequality is exactly floor(theta_x)=n.
Substitution gives T_U theta^U_{m,n}=identity there. Conversely every source has one m and one n=floor(x), and solving its two affine output equations gives precisely this theta.
Thus every target's complete predecessor set is {theta^U_{m,n}(n,u,v):m in Z, v in I^U_{m,n}}.
It is empty exactly when v belongs to none of these intervals; this is an exact all-integer membership test, not a cutoff.
Different m give genuinely different source objects. Half-open endpoints are assigned exactly once by their actual floor rule.
For C, every target has exactly one predecessor: m=floor(v)-n, x=v-m, y=u. Thus T_C is a Borel bijection.
For R, I^R_{m,n}=[2n/q(n),(2n+1)/q(n)) is independent of m: each target has either all integer old memories as predecessors or none.
This infinite R multiplicity is retained, not quotiented or used to renormalize measure. Having no predecessor is not being terminal: every source still has its prescribed forward image.

## 2. Full-point IMAGE and signed clocks

On each fixed counting component the inverse continuous derivative is [[0,d],[1,0]], of determinant -d.
The actual restriction is the restriction of that global affine diffeomorphism of R²; hence the assigned EVERY-point inverse Jacobian is J_theta=d_U(m,n), positive and finite, including both source/target cut assignments.
For every Borel E contained in Omega^U_{m,n}, affine change of variables and counting mass one on each component give
mu(theta E)=d_U(m,n) mu(E)=integral_E J_theta dmu, also when the values are infinite.
This proves the original-measure IMAGE law, with no fitted density or null-point repair. It is a branch law, not an assertion of global invariant probability or a sum of all incoming densities.
The full forward continuous determinant on the same source cell is -1/d; consequently the prescribed step clock is
kappa_U(m,x,y)=-log d_U(m,floor(x)).
It is nonpositive, may vanish, and is defined on every source. In particular C has identically zero clock; no positive roof is introduced.

## 3. Actual histories, IMAGE, full kernels and return groups

For each owner use its own d and T, and set Q_0=1, Q_r(z)=product_(0<=j<r) d(T^j z), S_r(z)=-log Q_r(z).
Here d(m,x,y) means d_U(m,floor(x)); every Q_r is a positive integer and every forward iterate exists.
The actual groupoid consists of (z,k,w) with witnesses r,s>=0, k=r-s and T^r z=T^s w; its units are (z,0,z).
Its inverse and composition are (z,k,w)^-1=(w,-k,z) and (z,k,w)(w,l,v)=(z,k+l,v).
Witnesses of the same triple differ by extending both histories by the same number of steps. The added sums start at their common endpoint, so they cancel.
Therefore c(z,k,w)=S_r(z)-S_s(w)=log(Q_s(w)/Q_r(z)) is well defined. Aligning two middle histories and using S_(a+b)(z)=S_a(z)+S_b(T^a z) proves additivity.
The forward arrow (Tz,-1,z) has c=-kappa(z)=log d(z); this fixes the direction independently of the sign of a physical period.
All meeting relations are Borel. A countable enumeration of witnesses gives a Borel c on the actual triple space; the countable inverse atlas gives countable source/range fibres.

Fix any two finite branch itineraries to a common future. Each restricted iterate is injective between fixed counting components and is an affine germ with forward Jacobian 1/Q_r.
For the history-pair map w->z, the Jacobian is Q_r(z)/Q_s(w)=exp(-c(z,k,w)).
Applying the same affine change-of-variables argument on the common-future domain proves EVERY-Borel history-pair IMAGE, including assigned faces.
Countable branch restrictions cover all actual finite histories; equality of triples does not change the assigned ratio because c has already descended.
No derivative of a floor function, topological étale claim or regular quotient is needed.

For exact incoming enumeration define P_0(t)={t} and P_(j+1)(t)=union_(v in P_j(t)) {theta^U_{m,n}(v):m in Z, v in Omega^U_{m,n}}.
In each union n is the actual first coordinate of v. Induction, using the complete one-step atlas, proves P_j(t)={z:T^j z=t} for every j, including empty sets.
ALL arrows with range t are (t,r-s,w), r,s>=0, w in P_s(T^r t); their inverses give all arrows with source t.
A compatible infinite ancestry is exactly v_0=t, v_(j+1)=theta^U_{m_j,n_j}(v_j) with every actual domain test satisfied. This equivalence follows step by step in both directions.
No assertion that every finite ancestry extends indefinitely, no free-word substitution and no added limit states is made.

For an actual arrow (z,k,w), the all-source kernels have exact membership tests:
ker(lag): k=0, with an equal-depth meeting T^r z=T^r w;
ker(c): a meeting T^r z=T^s w with r-s=k and Q_r(z)=Q_s(w);
ker(lag,c): k=0 and the product equality at the same equal-depth witness.
Different witnesses with a fixed lag cannot change these tests. These unrestricted tests include every memory component and depth.
For C, c=0 everywhere, so ker(c)=G_C; bijectivity makes ker(lag)=ker(lag,c) exactly the units.

A source has nonzero isotropy iff T^r z=T^s z for some r>s, equivalently its forward orbit eventually enters a legal finite cycle.
If that cycle has least period p and D=product of its p positive integer d-values, then I_z=pZ and
c(z,kp,z)=-k log D, ENTIRE H_z=(log D)Z.
To prove exhaustiveness, every return lag is divisible by p, all such multiples occur after entry, and the transient sums cancel. Otherwise I_z=H_z={0}.
Extension isotropy is the kernel of that clock map: all pZ when D=1, and only the unit when D>1; it is also trivial in the non-eventually-periodic case.
This is a structural criterion for every source, not a search or classification of higher cycles.

The extension keeps all (z,h) in Y×R. Two such points are in the same extension orbit exactly when an actual triple has c=h_z-h_w.
For a source class choose a reference a and an arrow a->z with clock b_z. The phase [h-b_z] in R/H_a is independent of that choice and is a complete extension-orbit test over the class.
Height translation has stabilizer H_a. If D>1, its primitive is log D and its positive repetitions are j log D, j>=1. If H=0, translation is free and gives no positive primitive, even when source isotropy is nontrivial.
The full height-action kernel on the orbit set is intersection_(z in Y) H_z. The zero-clock fixed sources proved below make that global kernel zero for each of the four owners.

## 4. Exhaustive GLOBAL fixed states

At any fixed state, the first two coordinates force m=n=floor(x) and y=x. Put q=q(m).
For M, the last equation is (q-1)x=m with x in [m,m+1).
If m=0, it is an identity and gives A_t=(0,t,t), 0<=t<1. If m=1 or -1, it is inconsistent.
If m>=2, its unique possible root is x=m/(m-1). For m=2 this is x=2 and is legal; for m>=3 it is at most3/2<m and is illegal.
If m=-k<=-2, the possible root is x=-k/(k-1). For k=2 this is x=-2 and is legal; for k>=3 it is at least-3/2>-2>=m+1 and is illegal.
Thus Fix(M)={A_t:0<=t<1} union {P_+,P_-}, where P_+=(2,2,2), P_-=(-2,-2,-2).
All possible integer memories have been exhausted; in particular the two integer left endpoints are retained and the half-open upper faces are not moved.

For C, the last equation is x=x+m, hence m=0 and Fix(C)={A_t:0<=t<1}.
For K, it is (q-1)x=0. If |m|<=1, q=1 and every x in its actual cell is allowed; if |m|>=2, x=0 contradicts floor(x)=m.
Thus Fix(K)={B_t=(floor(t),t,t):-1<=t<2}. This includes t=-1,0,1 in their proper cells, but excludes t=2.
For R, a fixed state again has m=n, so its scalar equation is exactly (q-1)x=m. The own-map substitution gives Fix(R)={A_t:0<=t<1} union {P_+,P_-}.
This equality of fixed lists does not identify their incoming basins or groupoids.

## 5. Complete core basins and their clock normal forms

For ANY of the fixed cores a just listed, define its own B_U(a)=union_(N>=0) P_N^U(a).
This is exactly its full source class: a common future with a is a, and every finite entrant shares that future. Distinct fixed cores have disjoint classes.
Let C_a=kappa_U(a), and for z in this basin choose any entry depth N and define beta_a(z)=S_N(z)-N C_a.
This is independent of N, since every subsequent step stays at a with clock C_a.
For every pair z,w in B_U(a) and EVERY k in Z, choose sufficiently large r,s with r-s=k after both entries. They meet at a, giving all such triples.
Conversely all arrows meeting the class stay there, so
G_U|_(B_U(a))=B_U(a)×Z×B_U(a), c(z,k,w)=beta_a(z)-beta_a(w)+k C_a.
The lag kernel has k=0, the clock kernel has beta_a(z)-beta_a(w)+k C_a=0, and the joint kernel has both.
At every entrant source isotropy is Z, entire H=C_a Z, and extension isotropy is Z if C_a=0 and trivial otherwise.
All phases are [h-beta_a(z)] in R/(C_a Z). For C_a!=0 the entire basin gives ONE closed physical packet of primitive |C_a| and all positive integer repetitions.
For C_a=0 it gives a free real translation orbit, retaining every zero-clock source repetition and every real phase, but no positive closed packet.

### MAIN and content-OFF: every fixed basin is a singleton

For a target A_t, 0<=t<1, a MAIN predecessor with old memory m has x=Gamma(m,0)t-m in [0,1).
For m>0 this equals m(t-1)<0; for m<0 it is |m|(t+1)>=1; only m=0 is admissible and reconstructs A_t.
For target P_e=(2e,2e,2e), e in {1,-1}, Gamma(m,2e) is1 or2 and the reconstructed x is an integer.
The required cell [2e,2e+1) therefore forces x=2e and m=2e(g-1).
The possibility g=1 would give m=0 but Gamma(0,2e)=2, a contradiction; g=2 gives exactly m=2e and reconstructs P_e.
Thus every MAIN fixed core has itself as its unique immediate predecessor, and induction gives B_M(a)={a} at every depth.
C's global bijectivity likewise makes each B_C(A_t)={A_t}.
The complete finite arrows of each such class are (a,k,a), k in Z; the only compatible infinite ancestry is the constant core sequence.
For M, C_(A_t)=0 and C_(P_e)=-log2; all beta are zero. For C every core clock is zero.
In particular each P_e has entire H=log2·Z, trivial extension isotropy and phase h modulo log2. Its lag, clock and joint kernels are all just the unit.
At each zero core the lag/joint kernels are the unit, but the entire source isotropy Z lies in the clock kernel and survives in the extension.

### Additive-memory-OFF: all fixed families and unrestricted incoming

For each -1<=t<2 use a=B_t and the explicit K recursion of Section3 with
theta^K_(m,n)(n,u,v)=(m,Gamma(m,n)v,u), domain n<=Gamma(m,n)v<n+1, over ALL m in Z at EVERY depth.
Together with B_K(B_t)=union_N P_N^K(B_t), the proved induction is an exact full-source membership characterization, not a finite tree or a selected set of entrants.
Its compatible infinite histories are precisely the domain-tested sequences in Section3; the fixed core itself always provides a constant one.
Every such core has d=1 and C_a=0, so beta_a(z)=-log Q_N(z) for any entry depth; Q_N is unchanged by further fixed steps.
The Section5 normal form supplies every kernel and phase: c=beta_a(z)-beta_a(w), entire H=0, source and extension isotropy Z, and real phase h+log Q_N(z).
Distinct t give disjoint full source classes; the continuum of fixed cores is not collapsed or promoted to positive physical multiplicity.
There are no positive packets from K's complete fixed set. This does not assert a globally empty positive ledger for K's unclassified higher cycles.

### Delayed-memory-OFF: explicit full basins, including old memories

For 0<=t<1, P_1^R(A_t)={(m,t,t):m in Z}. A predecessor of (a,t,t) would require 2a<=q(a)t<2a+1.
For a>0 this requires t>=2; for a<0 the right endpoint is negative while q(a)t>=0; only a=0 is possible.
Thus P_j^R(A_t)=P_1^R(A_t) for every j>=1 and B_R(A_t)=Z×{(t,t)}. All these entrants have d=1, beta=0 and entire H=0.
Its source/extension isotropy is Z, its clock kernel is the whole restricted groupoid, its joint kernel equals its lag kernel, and all real phases h remain.

The two positive-core basins are exactly
B_R(P_+)={(m,a,b):m in Z, a,b positive integers},
B_R(P_-)={(m,a,b):m in Z, a,b negative integers}.
Necessity: inverse reconstruction from an integer continuous target preserves integer coordinates. Also f(x)=(x+floor(x))/q(floor(x)) has precisely the sign of x, including f(x)=0 iff x=0, so a finite entrant into P_+ or P_- must have both continuous signs equal to that core's sign.
Sufficiency: for integers a,b of common sign e, the exact first three iterates are (a,b,2e), (b,2e,2e), (2e,2e,2e).
Thus every stated source enters the core without restricting its old memory m. Its full three-step Q is 2|ab|, so C_a=-log2 and beta(m,a,b)=log(4/|ab|).
Section5 gives c=beta(z)-beta(w)-k log2, entire H=log2·Z, trivial extension isotropy, and all phases [h-log(4/|ab|)] modulo log2.
Each sign basin is one full closed packet, primitive log2, with all integer repetitions; the signs are different source classes.
There are no omitted arbitrarily deep entrants: the inverse necessity proof and the uniform three-step entry prove the displayed basins equal the unrestricted recursion.
In every R fixed basin all sources enter its core in at most three steps. Therefore any compatible infinite ancestry must be the constant core sequence: its j-th state equals T^3 of its (j+3)-rd state. Noncore entrants have no such infinite ancestry, although all allowed finite histories remain.

## 6. Physical ledger, controls and frozen stop

MAIN's entire fixed ledger contains a continuum of distinct zero-clock source cores and EXACTLY two positive closed packets from fixed cores, both of primitive log2.
P_+ and P_- cannot meet under any histories because they are different fixed states; no sign symmetry or equal time identifies them in the actual groupoid or extension.
Their own complete basins are singletons, so neither an omitted incoming arrow nor a selected subgroup can reduce that primitive or merge the packets.
This proves positive-ledger nonemptiness and refutes the necessary at-most-one-packet-per-prime condition at the ordinary prime2. The decisive defect is duplicate multiplicity, not a demonstrated nonprime primitive.
The MAIN conclusion is therefore DUPLICATE PRIME-2 FIXED PACKETS — STOP / FORK, without changing any source, clock or phase convention.

Own-control ledger: C has H=0 globally because its entire clock is zero; K's complete fixed families have H=0, with higher returns unclassified; R has the same two positive fixed times but its own larger basins and offsets, plus its own zero family.
M and R agreeing on fixed equations cannot prove delayed-memory necessity, exactly as predeclared. No control's global statement is transferred to another owner.
Current gcd division is active at MAIN's positive cores, but those equal current/previous digits are not a proper-divisor N>D recurrence and establish no strong arithmetic naturalness.
Global prime-only purity at unclassified higher cycles, all-prime coverage, further packet uniqueness, strong naturalness and PROVES_TOO_MUCH are not decided or repaired by this short gate.
No new period search is needed or performed: a necessary target condition has already failed on the complete fixed ledger.
Same-object ownership remains intact. Classical NOT APPLICABLE; arithmetic T1 NOT PASSED; T3 NOT AUDITED; formal coordinates UNASSIGNED; Route B NOT INVOKED. No475.

EOF — card-only raw derivation, to freeze after full self-read; HOLD for root FULL-read and DISTINCT PAPER UNLOCK.
