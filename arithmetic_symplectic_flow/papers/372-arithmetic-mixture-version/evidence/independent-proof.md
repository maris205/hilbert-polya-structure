# 372 — Independent raw-card derivation

Owner `ANG-SCREEN-20260922-AMV01`; result: **STOP at prescribed full-point version admission**.
MAIN has a complete measured source but no admitted full real-clock extension.

## 1. Exact input and method

Read only `candidate-card.md`, all 98 lines, including the CP1 clarification.
SHA256 `0a13ed2c9e66084f1cc856c20a299aa7830cceb6bfd4ee401d1ddf5384cdf07b`.
Its preserved original 89-line SHA is
`2a68f215f31c8cbe16c1f32511c19d0a3c0d5eff7390b9776e270305c3092a37`.
Numerators below are mu(I_a([x|N])), fixing N+1 bits, not N bits of ax.
No root paper, peer proof, scout, other new package or external source was read.
Method: exact divisibility, nonnegative sums, likelihood inequalities and actual
groupoid arrows; no numerical search, auxiliary agent, network, Git or PDF.
ARS instructions and earlier shared binary/clock history are retained. This is
raw-card-separated, not blind/model-independent/external peer review; **NOT_CALIBRATED**.
Served model identity and effective reasoning setting are not independently known.

## 2. Arithmetic weights and the entire measured source

Put L_1=1 and L_n=lcm(1,...,n). Haar gives h(rK)=1/r by the r residue cosets.
Then {b=d}=L_(d-1)K minus L_d K and

    w_d=1/L_(d-1)-1/L_d.

Every nonzero q has finite b: divisibility by all positive integers forces
every p-adic coordinate to be zero. The only remaining point is 0, of Haar
mass zero since h(L_n K)=1/L_n ->0. Thus sum_(d>=2)w_d=1 telescopically.
An integer d increases the lcm exactly when d=p^a is a prime power: otherwise
each maximal prime-power factor is <d and already divides L_(d-1).
At d=p^a, L_d=p L_(d-1), so w_d=(p-1)/(p L_(d-1))>0.
Consequently D is all prime powers, infinite and unbounded (already 2^a).
In particular w_2=1/2, w_3=1/3, w_4=1/12; no alphabet was selected in advance.
Writing p_d=1/d, the countable sum mu=sum_D w_d nu_(p_d) is a probability.
Every binary cylinder of length N and s ones has probability

    Z_N(s)=sum_D w_d p_d^s(1-p_d)^(N-s)>0.

Hence its topological support is ALL X. Each component is shift-invariant,
so mu is too. The actual maps are T:X->X, I_a:X->[a], with T I_a=id and
I_a T=id on [a]. Each I_a has proper image [a]; T is onto.
Every singleton is null: each component's cylinder masses tend to zero,
and dominated summation over d preserves that limit. All points remain.
No mixing label is a source point.
For distinct coordinates, Cov(X_i,X_j)=Var_w(p_d)>0 because w_2,w_3>0;
thus this full-support stationary law is not a product law. No irreducibility,
finite-order property, arithmetic naturalness or factor of an older owner follows.

## 3. Prescribed ratios: exact failure and the measure-identity distinction

For s=s_N(x), define the positive posterior probability
Q_N(d|x)=w_d p_d^s(1-p_d)^(N-s)/Z_N(s). The exact ratios are

    j_(1,N)(x)=sum_D p_d Q_N(d|x),   j_(0,N)(x)=1-j_(1,N)(x).

At x=0^infinity, fix 0<epsilon<1/2 and choose e in D with p_e<epsilon.
The posterior mass of {p_d>=epsilon} is bounded by

    w_e^(-1) [(1-epsilon)/(1-p_e)]^N ->0.

Therefore 0<=j_(1,N)<=epsilon+(1/2)Q_N{p>=epsilon}, proving j_1=0 and j_0=1.
This is an all-N analytic bound at the retained null path, not an a.e. replacement.
It violates strict positivity and decisively stops the specified full version.
At x=1^infinity, the posterior outside d=2 is at most
((1-w_2)/w_2)(2/3)^N, since all other p_d<=1/3. Thus both limits are 1/2.

For completeness, on paths with frequency q=p_e>0 the same ratios tend to
p_e and 1-p_e. Indeed f_q(p)=q log p+(1-q)log(1-p) is strictly maximized at q.
For |p-q|>=epsilon, f_(s_N/N)(p)-f_(s_N/N)(q)<=-delta eventually, uniformly
over p in (0,1/2]; near zero it tends to minus infinity uniformly for s_N/N
near q. Division by the e term bounds outside posterior mass by w_e^(-1)e^(-N delta).
Inside the epsilon interval the posterior mean differs from q by at most epsilon.
Under nu_q the frequency is q a.s.: expansion gives E(S_N-Nq)^4=O(N^2),
and summable Markov bounds show that deviations >epsilon N occur only finitely often.
Thus disjoint Borel sets E_d={frequency=p_d} satisfy nu_(p_d)(E_d)=1,
mu(E_d)=w_d and mu(union E_d)=1. Define r_1=p_d on E_d, r_0=1-p_d,
and, only as a measure-identity representative, r_0=r_1=1/2 off their union.
For every Borel E, componentwise prefixing and nonnegative summation give

    mu(I_a E)=sum_D w_d p_d^a(1-p_d)^(1-a) nu_(p_d)(E)=integral_E r_a dmu.

The component prefix identity holds on cylinders and extends to all Borel
sets by uniqueness of finite measures on their generating cylinder algebra.
This establishes the every-Borel identity and the a.e. cylinder limits, without
substituting r for the frozen j at null paths. No alternative extension is built.
The result excludes this prescription, not all positive Borel representatives.

## 4. Complete source ledger despite failed clock admission

Every arrow is exactly (z,k,y), k=m-n, T^m z=T^n y; inverse is (y,-k,z),
and composition adds k. Prefix replacement v w ->u w has domain [v], image
[u], lag |u|-|v| and inverse u w ->v w. These charts exhaust all arrows.
Equal triples, not free histories, are identified. All incoming at y are
z=u T^n y, with every finite u and n>=0; all actual allowed lags are retained.
The full source lag kernel is {(z,0,y):T^N z=T^N y for some N>=0}.
Unequal shift equality at y is equivalent to eventual periodicity. If its
tail has least period l, any shift difference is divisible by l, and every
multiple of l is realized beyond the preperiod. Thus ENTIRE source isotropy
is lZ; for a non-eventually-periodic y it is {0}. Periodic tail orbits are
exactly primitive binary necklaces, with all finite incoming prefixes/rotations.
Each aperiodic orbit is the full prefix-shift saturation of any of its points.
MAIN's c, ker c, its intersection with ker lag, extension isotropy, H,
physical phases/primitive times/repetitions are **NOT DEFINED**, not zero.
No source necklace or lag is converted into physical time after admission fails.

## 5. SINGLE: complete independently measured control

On the full binary source with fair Bernoulli law, every prescribed ratio is
1/2 at every point and every N. Every-Borel prefix IMAGE is 1/2. For all
actual triples, c(z,k,y)=k log2; the inverse sign and cocycle identity hold.
The full extension sends (y,h) to (z,h+c); height translation h+t descends
to its orbit SET. The following phases classify that set and its full returns.
Full clock kernel, lag kernel and their intersection are the synchronized
lag-zero relation in section 4. Source isotropy is the entire lZ on least
period-l tails and {0} otherwise. Its image H is l log2 Z or {0}; extension
isotropy is always trivial, since c is injective on each source isotropy.
For a core eta of least period l and x=u T^j eta, 0<=j<l, the actual arrow
(x,|u|-j,eta) gives phase h-(|u|-j)log2 modulo l log2. These incoming states
exhaust its source orbit; different representations differ by full H.
For an aperiodic anchor a, the unique actual arrow (x,k,a) gives real phase
h-k log2. All prefixes of all shifts are included, with no null paths removed.
Every primitive necklace gives one physical circle of least time l log2;
powers give only repetitions. Distinct necklaces cannot share an eventual tail.
If P_l counts primitive length-l words, 2^n=sum_(l|n)P_l, so exactly P_l/l
packets have least time l log2. In particular two distinct constants give log2.

## 6. TWO-COMPONENT: exact oscillation, complete failed-owner ledger

Its own law is a full-support stationary probability, not a product, with
the same full source, inverse charts, incoming, lag kernel and ENTIRE source
isotropy of section 4. Set N_0=0, L_j=j(N_(j-1)+1), N_j=N_(j-1)+L_j.
Concatenate blocks of L_j zeros for odd j and L_j ones for even j. This is
one exact path, with increasingly dominant blocks; no cutoff search is used.
For s ones in an N-prefix, the likelihood ratio of p=1/2 to p=1/3 is
R_N=(3/2)^s(3/4)^(N-s). Put alpha=log(3/2)>0, beta=log(3/4)<0.
At odd block ends, log R<=N_(j-1)alpha+L_j beta ->-infinity; at even ends,
log R>=N_(j-1)beta+L_j alpha ->+infinity, directly from L_j=j(N_(j-1)+1).
Equal priors give posterior theta=R/(1+R) and its OWN
j_(1,N)=theta/2+(1-theta)/3, j_(0,N)=1-j_(1,N).
Thus along odd/even ends j_1 tends respectively to 1/3 and 1/2, and j_0 to
2/3 and 1/2. Both prescribed limits fail to exist at this retained path.
Constant-zero limits instead are (j_1,j_0)=(1/3,2/3), and constant-one limits
are (1/2,1/2): the oscillation witness is not a hidden zero-branch argument.
Every-Borel derivatives exist by the two disjoint frequency sets exactly as
above; this does not repair the prescribed version. Source fields remain
fully defined; c/clock kernels/extension/H/physical packets/phases/repetitions
are NOT DEFINED for this failed control, not inherited from SINGLE or zero.

## 7. RETAINED-INDEX: full positive clocks on every label fibre

Y=D times X is a distinct carrier with all d retained. The probability
sum_D w_d delta_d times nu_(1/d) is shift-invariant and has full support.
Both prefix inverses have ALL Y as domain and images D times [a]. Fixing d
in every cylinder cancels w_d: j_1=1/d and j_0=(d-1)/d at every point.
Every-Borel IMAGE follows by splitting into d-fibres and component prefixing.
All arrows are (d,z,k,y); no arrow changes d. Section 4 gives their full
source ledger fibrewise. Write A_d=log d, B_d=log(d/(d-1)), both positive.
For an arrow witnessed by prefixes u,v, set s=#1(u)-#1(v), t=#0(u)-#0(v).
These signed differences are invariant under extending both witnesses by
the same tail segment, and k=s+t. With W_d(u)=#1(u)A_d+#0(u)B_d,

    c_d=W_d(u)-W_d(v)=s A_d+t B_d=k log d-t log(d-1),   J_d=exp(-c_d).

The formula proves every prefix-replacement IMAGE, inverse and composition.
For d=2, ker c=ker lag={k=0}. For d>2, c=0 implies d^k=(d-1)^t;
coprimality and prime valuations force k=t=0, hence s=0, and conversely.
For d>2 the FULL clock kernel has s=t=0, lag kernel has s+t=0, and their
intersection is the clock kernel (also for d=2). This includes all arrows,
not only isotropy, and the extra balanced-prefix condition is not omitted.
Use the same full extension and height-translation rule as SINGLE, with c_d.
For a primitive period word v of length l, with a ones and b zeros, let
C_d(v)=a A_d+b B_d>0. ENTIRE source isotropy lZ maps nl to n C_d(v),
so H=C_d(v)Z and extension isotropy is trivial. For aperiodic tails both
source and extension isotropy are trivial and H={0}.
For x=u T^j eta with periodic core eta, relative phase is
h-W_d(u)+W_d(eta|j) modulo C_d(eta); the actual arrow has witnesses |u|,j.
For an aperiodic anchor a and x=u T^n a, phase is h-W_d(u)+W_d(a|n) in R.
Witness independence follows from the cocycle; all incoming were exhausted above.
For EVERY d and EVERY primitive binary necklace v there is exactly one circle
of least time C_d(v); its r-fold return is r C_d(v), and powers are not new
primitives. All heights, rotations and finite prefixes remain. Distinct labels
or necklaces never merge, even when C_d(v) agrees. This classifies ALL packets,
including the two constant words of times B_d and A_d in every label fibre.

## 8. Closure and limits

The arithmetic mixture and full source are established; admission fails on
the precommitted zero path. All three own controls have complete admitted or
explicitly NOT DEFINED ledgers. Their periods are not MAIN periods. No proof
of all-prime coverage, naturalness, or a universal nonatomic/version no-go is
claimed. No post-hoc roof, path deletion or retained-index repair of MAIN occurs.
Classical A0/A1/A2 NOT APPLICABLE; T3 NOT AUDITED; formal UNASSIGNED; B NOT INVOKED.
Portfolio: stop this frozen screen at its decisive gate; any changed measured
owner/version needs a fresh card. No additional research direction is opened here.
EOF — raw-card derivation complete; freeze for root's read and later review.
