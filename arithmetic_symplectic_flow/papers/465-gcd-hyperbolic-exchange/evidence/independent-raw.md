# GHE01 — independent card-only raw derivation

Candidate `ANG-20260925-GHE01`; four full-plane measured-history owners M, G, E, S.
Result: M and S each have exactly one fixed core in W; G and E have none there.
MAIN's actual positive primitive at its core has exponential strictly between 4 and 5.
The frozen necessary prime target therefore fails on MAIN itself: STOP / FORK.

## 1. Inputs and isolation

Sole scientific input: original `candidate-card.md` lines 1–108, fully read through EOF;
SHA256 `fc7698d40f559138a7ec6cb49172dcdd28c5af125dc29a2719ca8eb58ca87a25`.
CP1 `scope-review.md`: 89 lines; SHA256
`61af0ea9fa2fb459e018c19844e6bad09fed6d1278dd8c77d8743a3fdb12c36f`.
Root fully read CP1 and issued a distinct card-only RAW release. No author manuscript,
README, ledger, current helper/peer proof, old proof or old Outcome was opened for this work.
Refreshed ARS/local instruction reads and inherited exposure are recorded in CP1.
Shared history and inherited model remain `NOT_CALIBRATED`, not blind/external verification.
No reviewer helper, scientific code, numerical solver, network, Git or PDF was used.
Only this raw is written. All identities and bounds below are exact analytic arguments.

## 2. Full sources and every actual inverse

Every owner keeps X=R², its usual Borel sets and original Lebesgue area mu.
For C_ab=[a,a+1)×[b,b+1), define g=Gamma(a,b)=gcd(|a|,|b|), except Gamma(0,0)=1.
The countable cells partition X, including every assigned integer face, and g≥1.
MAIN T_M=(cosh(y)/g,cosh(x)/g) and S T_S=(cosh(x)/g,cosh(y)/g)
use that actual source g and have legal source xy≠0. G has T_G=(cosh y,cosh x)
on xy≠0, with no arithmetic cell labels. E has T_E=(exp(y)/g,exp(x)/g) on ALL X.
All targets are finite and strictly positive. No target must itself be legal to be retained.
Axes and negative coordinates remain objects; E does not inherit a cosh critical guard.

For fixed g let O_g={(u,v):gu>1,gv>1}. For each cell and eps,eta in {−1,1}, use
 theta^M_ab,eps,eta(u,v)=(eps arcosh(gv),eta arcosh(gu)),
 theta^S_ab,eps,eta(u,v)=(eps arcosh(gu),eta arcosh(gv)),                     (1)
on their exact domains {Z in O_g:theta(Z) in C_ab}. These reconstructed coordinates
are nonzero and have the declared signs. For G use the M formula with g=1 on O_1,
four sign choices and no cell tests or redundant labels.
For E the branch is
 theta^E_ab(u,v)=(log(gv),log(gu)),
 domain {(u,v) in (0,infinity)²:theta^E_ab(u,v) in C_ab}.                   (2)
Zero reconstructed coordinates in (2) remain legal, including all appropriate cell faces.

Necessity: a legal source has its unique actual cell (except G, which needs none) and,
for cosh owners, two nonzero signs. Inverting the positive exponential or the even cosh
on each signed half-line gives exactly (1) or (2). Sufficiency: every listed candidate
has the required actual g, signs and source permission, and substitution returns Z.
Thus these are all predecessors. Repeated presentations of the same source are deduplicated;
genuinely different reconstructed sources are not. Every branch domain is Borel.
At a cosh threshold gu=1 or gv=1 the corresponding zero-coordinate source is illegal,
not an extra inverse branch; other cells must still undergo their own strict tests.
Targets outside the positive quadrant have no one-step preimages, not a deletion from X
and not a claim that their full history-groupoid incoming arrows are absent.

## 3. Original-area IMAGE and the frozen pointwise clocks

Each fixed-g cosh formula on a signed open quadrant is an analytic diffeomorphism
onto O_g, with (1) its inverse; each fixed-g exponential formula is an analytic
diffeomorphism R²→(0,infinity)². The cell restriction selects its actual Borel branch.
Differentiating these ambient inverse germs gives, at every actual branch point,
 J_M=J_S=g²/(sqrt((gu)²−1)*sqrt((gv)²−1)),
 J_G=1/(sqrt(u²−1)*sqrt(v²−1)),             J_E=1/(uv).                     (3)
The M/E exchange changes determinant sign but not its absolute value.
Every value in (3) is strictly positive and finite on its exact domain.
In particular E remains regular when a reconstructed source coordinate is zero.
For EVERY Borel A in a branch's actual domain, ambient change of variables restricts to
                       mu(theta(A))=integral_A J_theta dmu.              (4)
This includes null sets, assigned floor faces and infinite-area sets, with nonnegative
integrals possibly infinite. Borel images follow from the ambient homeomorphism.
No derivative of the whole discontinuous floor map across a cut is claimed, and no
pointwise completion is chosen after looking at periodic states.

Using the actual forward target in (3), the prescribed legal-source clocks are
 kappa_M(z)=kappa_S(z)=log(|sinh x*sinh y|/g(z)²),
 kappa_G(z)=log|sinh x*sinh y|,
 kappa_E(z)=x+y−2 log g(z).                                               (5)
These are own formulas, not a transfer of admission between owners. They are finite on
their legal sources and equal −log J_actual(Tz). Negative and zero values are retained.
Illegal cosh sources have no outgoing summand. Original area is not replaced by an
invariant density, and no positive suspension roof is inferred.

## 4. All finite and compatible infinite histories

For each owner U independently, put D_0=X and let D_r be its legal length-r domain.
Let S_r(z)=sum_(0≤i<r) kappa_U(T_U^i z), S_0=0, W_r(z)=exp S_r(z)>0.
The complete actual groupoid is
 G_U={(z,r−s,w):z in D_r,w in D_s,T_U^r z=T_U^s w},
 c_U(z,r−s,w)=S_r(z)−S_s(w), source w/range z.                            (6)
Equal actual triples only are identified. Two witnesses of the same triple differ by
equal extra depths; the added sums run from the same meeting point and cancel.
For composition align the two middle histories at the larger middle depth. The already
legal longer history supplies the continuation, and the middle sums cancel. Thus c
descends and adds; inversion negates it, all objects have units, and the forward arrow
(T_U z,−1,z) has clock −kappa_U(z). No terminal is padded with artificial iterates.
Countably many Borel legal-history equality sets, with witness-independent clock values,
give a Borel groupoid and Borel c. Integer lag is retained, not collapsed to endpoints.

On each actual fixed finite-history branch, the endpoint map is an own inverse iterate
after an own forward iterate. The all-point chain rule and (4) give its IMAGE density
                      W_s(w)/W_r(z)=exp(−c_U(z,r−s,w))                    (7)
for the arrow w→z, on EVERY Borel subset of its actual domain. Floor/sign histories
are retained as germ choices; witnesses of the same actual triple give the same (7).

Let P_0^U(t)={t}, and recursively let P_(j+1)^U(t) be every theta_alpha(v) with
v in P_j^U(t) and v in that own branch's actual domain from (1)–(2).
The inverse identities prove by induction
                    P_j^U(t)={z:T_U^j z=t legally}.                      (8)
All arrows incoming to t are exactly
 (t,r−j,z), with r,j≥0, t in D_r and z in P_j^U(T_U^r t).                 (9)
This is all depths, including terminal incoming with r=0. Reversing gives outgoing;
the endpoints of (9) are exactly the whole source class, not selected ancestors.

Every compatible infinite backward history from t is exactly a sequence v_0=t,v_1,...
such that at each j an actual branch alpha_j from (1)–(2) satisfies
 v_j in domain(theta_alpha_j), v_(j+1)=theta_alpha_j(v_j).                (10)
Equivalently, T_U(v_(j+1))=v_j at every j with every step legal. Necessity and sufficiency
follow from the complete one-step atlas, so (10) gives all such histories with exact
cell/sign tests and no index/depth cutoff. It does not assert every finite chain extends,
adjoin limit points, or allow free sign words whose reconstructed states fail the tests.
Infinite forward histories have precisely z in intersection_(r≥0) D_r and their unique
actual iterates. Neither kind of infinite history creates new source objects or arrows;
the arrows in (6) still have finite meeting witnesses.

The full kernels, for each own U, are
 ker lag={(z,0,w):T_U^r z=T_U^r w legally for some r},
 ker c={(z,r−s,w) in G_U:W_r(z)=W_s(w)},
 ker lag intersect ker c={(z,0,w):T_U^r z=T_U^r w,W_r(z)=W_r(w) for some legal r}. (11)
These are witness-independent exact tests; branching and zero clocks are not removed.
Two extended points (w,h) and (z,h') are in the same extension orbit exactly when some
actual triple (z,k,w) satisfies h'−h=c_U(z,k,w). This is an exact full-height orbit test.

If a state is not eventually on a legal cycle, nonzero source isotropy would imply equal
unequal-depth iterates and is impossible. Its source and extension isotropy are units, H=0.
If its eventual core has least period p and signed sum C, every and only isotropy lag kp
occurs, with clock kC, k in Z: extend histories after first entry and cancel their prefixes.
Thus ENTIRE H=CZ, including at every feeder. Extension isotropy is all pZ when C=0
and only units when C≠0. In each source class choose an anchor for description only and
an anchor-to-z arrow of clock b_z. All phases are h−b_z modulo H; a different arrow
changes b_z by H. Height translation on the orbit SET has stabilizer exactly H.
When C≠0 it has primitive |C| and all positive integer repeats; when C=0 there is no
positive primitive, despite retained source isotropy. Different equal-time classes stay distinct.

## 5. Exhaustive fixed sets in the frozen window

On W=[2,3)² the actual two floor digits are both 2, so g=2 for M, E and S.
Every point of W is in the own legal domain. For MAIN a fixed point must satisfy
                         2x=cosh y, 2y=cosh x.                            (12)
If x>y, strict increase of cosh on W gives 2x=cosh y<cosh x=2y, a contradiction;
the reverse inequality is equally impossible. Thus x=y is proved, not assumed.
Put F(t)=cosh t−2t. On [2,3), F'(t)=sinh t−2>0, since sinh 2>2.
The following exact bounds locate its unique root without a numerical solve.

For r=21/10, the positive cosh series tail starting at degree four has successive
ratios at most r²/30. Since r²<9/2,
 cosh r ≤1+r²/2+r^4/(24(1−r²/30))
         <641/200+135/136=1784/425<21/5=2r.                               (13)
For s=9/4, its first three positive terms give
 cosh s ≥1+s²/2+s^4/24=28257/6144>27648/6144=9/2=2s.                     (14)
Continuity and strict monotonicity give exactly one a in [2,3) with
                      cosh a=2a,        21/10<a<9/4.                    (15)
Consequently Fix(M) intersect W consists exactly of z_*=(a,a).
The strict monotonicity also excludes any further window root or lower boundary root;
the upper boundary 3 is excluded by W itself, not inserted as a missing source object.

G fixed equations in W again force x=y, now with cosh x=x. But
cosh t≥1+t²/2>t for t in W, so Fix(G) intersect W is EMPTY.
E fixed equations there are 2x=exp y and 2y=exp x; strict increase forces x=y.
For t in W, exp t≥1+t+t²/2>2t, so Fix(E) intersect W is EMPTY.
For S the separate equations are F(x)=F(y)=0. Uniqueness in (15) independently
gives Fix(S) intersect W={z_*}. This exhausts all four owners and off-diagonal cases.
No fixed-set statement outside W or higher-period census is needed or claimed.

## 6. Whole MAIN/S fixed packets, all incoming and the decisive primitive

For U=M and U=S separately, define B_U=union_(n≥0) P_n^U(z_*) using (8).
Because z_* is fixed, (9) shows B_U is exactly its entire full-X source class.
It includes every negative/cut/null predecessor permitted by that OWN atlas; no basin
representative is substituted. The compatible infinite histories are exactly (10),
and every member of such a history from z_* belongs to B_U at its corresponding depth.
These two basins are not identified between different owners merely because their cores coincide.

At z_* each own clock in (5) is
            L=log(sinh²(a)/4)=log(a²−1/4),
            104/25<exp L<77/16, hence 4<exp L<5 and L>0.                 (16)
Here cosh² a−sinh² a=1 and (15) give the identities and strict rational bounds.
In particular exp L is not an integer or an ordinary prime.

For z in B_U let nu(z) be its first-entry depth to z_* and A(z)=S_{nu(z)}(z),
and put beta(z)=A(z)−nu(z)L. Every pair z,w in B_U admits EVERY integer lag k:
choose s≥nu(w), r≥nu(z) with r−s=k and extend at the fixed core.
Conversely these are all actual triples on B_U. Their clocks are exactly
                 G_U restricted to B_U=B_U×Z×B_U,
                 c_U(z,k,w)=beta(z)−beta(w)+kL.                          (17)
This follows by writing S_r(z)=A(z)+(r−nu(z))L after entry. It is unchanged by any
earlier meeting witness. In particular all source isotropy is Z and its ENTIRE image
is LZ, even at feeders. No extra inverse label creates a smaller positive clock.

The packet's lag kernel is every (z,0,w); its clock kernel is precisely
beta(z)−beta(w)+kL=0; its joint kernel has k=0 and beta(z)=beta(w).
Extension isotropy is trivial because L>0. The actual zero-lag arrow z_*→z has clock
beta(z), giving the complete phase h−beta(z) modulo L. Thus each owner's whole basin,
with all phases retained, gives one physical periodic packet of primitive L, not one
per incoming state or per phase. All positive repeats jL, j≥1, remain.
G and E have no fixed packet in W, but keep their full-source ledgers from Section 4;
their possible outside-window or higher-period packets are not declared absent.

## 7. Decision and limitations

MAIN's frozen-window core is arithmetically active: its actual g is 2, not an external
label. Nevertheless (16)–(17) supply an owned actual nonprime primitive, so MAIN alone
triggers STOP / FORK. S supplies its own same-clock fixed control, not a transferred
MAIN verdict or a second MAIN packet. No rescaling, phase selection or source deletion is used.
The positive ledger is nonempty, but the required all-primitives prime support already fails.
No conclusion about full prime coverage, other windows, higher cycles, global basin equality
or a universal no-go is asserted. No parameter, inverse version, density or roof is repaired.
Strong naturalness and PROVES_TOO_MUCH remain separate open obligations. Classical fields
NOT APPLICABLE; arithmetic T1 NOT PASSED; T3 NOT AUDITED; formal UNASSIGNED; B NOT INVOKED.
The bounded gate stops here. No scientific numerics, extra gate or paper 470 is introduced.

EOF — card-only raw; full self-read before byte freeze, then HOLD for distinct PAPER UNLOCK.
