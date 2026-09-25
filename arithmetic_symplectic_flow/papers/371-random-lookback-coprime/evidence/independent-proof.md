# Independent raw-card proof — random-lookback coprime histories

Candidate `ANG-20260922-RLC01`; 2026-09-22; round 2/5.
Author `/root/algebraic_henon_author`; internal AI, `NOT_CALIBRATED`.
Sole scientific input: [card](../candidate-card.md), all 94 lines through EOF,
SHA-256 `3f11f7cd57dbf8717d0d8e2db29f7bf32bc76b2fd4267592633563aa00e3c037`,
verified at CP1 and fully reread after root's explicit mathematical release.
No author paper, peer/scout proof, other new science, web or numerical experiment.
Previously fully read ARS instructions reused; shared history and the disclosed
anticipated test preclude blindness or discovery-priority claims.

## 1. Four separately constructed probability owners

Write d(a)=a(a-1), rho(a)=1/d(a). Telescoping proves sum_(a>=2)rho(a)=1.
Z(b)>=rho(b+1)>0 by coprimality, while Z(b)<=1-rho(b)<1.
Independently, S(b):=Z_sh(b)>=rho(b)>0 and S(b)<=1-rho(b+1)<1.
Partitioning by gcd gives S(b)=1-Z(b). Thus K and K^sh are probability
kernels on the entire countable alphabet, with all prescribed denominators valid.

The following construction proof is quantified over FOUR separate noise laws:
MAIN uses H=K and lag law lambda_r=2^-r; OFF uses H_b=rho with that lag;
NEAR uses H=K and lambda_1=1; SHARED uses H=K^sh and lambda_r=2^-r.
Each uses its OWN independent two-sided reset, lag and uniform noise, its OWN
fallback 2, and produces its OWN mu^alpha and q^alpha. No law is imported.
The fair-reset and uniform variables remain as specified for all four owners.

Quantiles exist for every u<1 because each cumulative probability tends to one;
their dependence on the countable parent symbol and u is Borel. An ancestral
chain strictly decreases its time indices. Expose the new node's noise only
when reached; it has not previously been queried and its reset bit is still
independent fair. Hence the probability of n successive continuations is 2^-n.
The never-reset event has probability zero. Taking the countable union over
all integer starting times gives a single null exception set.

Every finite-chain event is Borel, and the finite recursive quantile output is
Borel there; assigning 2 on the Borel never-reset event defines Y_t everywhere.
On the common conull set all chains terminate. A parent's own chain is precisely
the child's remaining suffix, so all recursive equations hold simultaneously.
They are NOT asserted on never-reset samples: the fallback is an output
definition there, not a solution of the original sampling recursion.
The algorithm, including fallback, commutes with integer translation of the
noise. The resulting two-sided process is stationary, and its past law mu^alpha
is a probability on FULL X. Noise never becomes an extra physical coordinate.

## 2. Conditional law, all-point regularity, support and atom status

For each owner let F_-1 be the sigma algebra of all noise at times <=-1.
Every Y_-r is F_-1-measurable; time-zero reset, lag and uniform are independent
of F_-1. The a.s. recursion and the quantile distribution give

    P(Y_0=a | F_-1)=rho(a)/2 + (1/2)sum_r lambda_r H_(Y_-r)(a).

This right side is measurable in the entire OUTPUT past, so the tower property
proves q_a^alpha(x)=rho(a)/2+(1/2)sum_r lambda_r H_(x_(r-1))(a)
as the conditional law given that past. Nonnegative summation
shows sum_a q_a^alpha(x)=1 at every x, with the uniform-in-history bounds

    0<rho(a)/2 <= q_a^alpha(x) <= (1+rho(a))/2 <= 3/4.              (1)

For geometric lookback, agreement of the first N past symbols gives
|q_a(x)-q_a(y)|<=2^(-N-1), since each kernel value lies in [0,1]. Thus every
q_a is continuous; its log is continuous as well by the positive lower bound.
NEAR is constant on first-symbol cylinders; OFF is constant on all X.
In particular kappa(z)=-log q_(z_0)(Tz) is continuous and >=log(4/3).

Stationarity gives the past vector (Y_-1,Y_-2,...) the same law mu^alpha.
Consequently for EVERY Borel E subset X, the conditional identity proves

    mu^alpha(I_a E)=integral_E q_a^alpha dmu^alpha.                 (2)

Iterating gives every finite word u the cylinder bounds
product_j[rho(u_j)/2] <= mu^alpha([u]) <= (3/4)^|u|.
Every nonempty basic cylinder therefore has positive mass: full support.
Shrinking cylinders around any single history show it has mass zero, so each
mu^alpha is nonatomic. All null periodic and exceptional histories stay in X.
The explicit q is an all-point version of (2), not conditioning on singleton
events. Full support makes it the UNIQUE continuous version of the a.e.
conditional function: continuous disagreement would contain a positive-mass open set.

## 3. Actual dependence, not an inference from noise notation

For MAIN, K_2(2)=0 whereas K_3(2)>0. Keeping every coordinate except a
chosen arbitrarily remote coordinate r-1 fixed, replacing its 2 by 3 changes
q_2 by the nonzero quantity 2^(-r-1)K_3(2). For SHARED the corresponding
kernel values are K^sh_2(2)>0 and K^sh_3(2)=0, again a nonzero change.
If either law had finite Markov order N, its conditional q_2 would be a.e.
constant on each length-N cylinder. Continuity and full support force that
constancy everywhere on the cylinder, contradicting the remote change for r>N.
Thus both laws are genuinely infinite-memory and nonproduct.
NEAR has order at most one, and the same K_2/K_3 contrast proves it is not
order zero or product. OFF has Y_t=Q_rho(U_t) on the common conull set,
independently for all t; hence its own law is exactly rho^N_0, not MAIN's law.

## 4. All histories, cocycle and FULL kernels, for each own measure

Fix any one of the four owners in this section; every q and mu refers to it.
All I_a are actual Borel/homeomorphic prefix inverses on ALL X, with disjoint
images [a] covering X. Repeated use of (2) and its nonnegative-function form gives
mu(I_u E)=integral_E q_u dmu, with exactly the frozen product q_u, on EVERY
Borel E. For replacement vx->ux, its IMAGE at vx is q_u(x)/q_v(x).
Indeed both image masses integrate their respective q_u,q_v against the SAME
tail measure; division is by the strictly positive function q_v, never by a
null set's mass. All functions are positive continuous pointwise versions.

The countably many prefix charts cover exactly the stated actual-lag groupoid.
For z=ux, y=vx, c=log[q_v(x)/q_u(x)]. Two witnesses for the same triple
extend their shifts by the same number; the common-tail kappa sums cancel.
Aligning intermediate shifts in a composition proves cocycle additivity and
inverse sign. Thus these clocks belong to the very IMAGE identities just proved.
Exact full arrow-set descriptions, including non-isotropy arrows, are

    ker c = union_(u,v) { (ux,|u|-|v|,vx): q_u(x)=q_v(x) };
    ker lag = union_(|u|=|v|) { (ux,0,vx): x in X };
    their intersection imposes BOTH the length and q-product equalities.       (3)

Here q_u is the explicit finite product of the specified convergent kernel
series, so (3) supplies all tails and all finite words, not a periodic-only
description. No equality of the two kernels is assumed. For example OFF has
q_4=q_23=1/12, giving nonzero-lag zero-clock arrows, whereas its equal-length
prefixes 2 and 3 give a nonzero clock on lag zero.

## 5. Entire isotropy, incoming histories and primitive packets

These structural statements apply to EACH own clock from section 4. A source
has nonzero isotropy iff unequal shifts of it agree, equivalently its tail is
eventually periodic. The isotropy lags form a subgroup of Z; its least positive
element is the least eventual word period ell. Thus isotropy is ell Z, or
{0} for a non-eventually-periodic source. If w is its primitive cyclic core,
put L(w)=sum_(i<ell) kappa(T^i w^infinity). Cancelling a finite preperiod yields

    c on isotropy k*ell = k L(w),   L(w)>=ell log(4/3)>0.

Hence H=L(w)Z for that source; otherwise H=0. Extension isotropy is trivial
at EVERY source and height, since only lag zero has zero isotropy clock.
All incoming and tail histories are exactly u T^n z, for all finite u and
n>=0, with the actual witness lags retained. No alphabet, tail or phase is removed.
Over a source orbit, choose a reference f and an actual arrow g:f->z. The
full phase is h-c(g) modulo H_f; choices differ by precisely H_f. Thus each
aperiodic-tail orbit gives a physical line, each periodic one gives R/L(w)Z.
Only orbit SETS are asserted, not a manifold or invariant physical measure.

Two periodic source orbits agree iff their primitive cores are cyclic rotations:
aligning infinite tails proves necessity and constructs the converse arrows.
Therefore ALL primitive necklaces over A, one packet per necklace, are the
complete positive ledger. Repeated words give times k L(w) of that SAME packet.
Different necklaces with equal time are distinct packets, not merged by value.
All these countable periodic source orbits are null but remain in the owner.

## 6. Exact general-word formulas and all constant/two-letter tests

For a word w of length ell, indices below are cyclic. For the geometric-lag
owners, define W_r=2^-r/(1-2^-ell), 1<=r<=ell. Their exact one-position factor is

    C_i(w)=rho(w_i)/2 + (1/2)sum_(r=1)^ell W_r H_(w_(i+r))(w_i).

For NEAR instead C_i=rho(w_i)/2+K_(w_(i+1))(w_i)/2; for OFF it is rho(w_i).
For EVERY word, L(w)=-log product_i C_i(w). It is the least positive time
when w is primitive; otherwise it is the indicated repetition's time. This
computes the whole periodic ledger separately with H=K or H=K^sh, as appropriate.

For ALL a,b>=2 put I=1_(gcd(a,b)=1), J=1-I. The following table gives the
constant-word least time and a factor f(a,b) such that the two-letter traversal
time is log[d(a)d(b)/(f(a,b)f(b,a))]:

| Own owner | Constant a^infinity: least time | f(a,b) |
| --- | --- | --- |
| MAIN | log[2d(a)] | 1/2+I/[3Z(b)] |
| OFF | log d(a) | 1 |
| NEAR | log[2d(a)] | 1/2+I/[2Z(b)] |
| SHARED | log[2d(a)S(a)/(1+S(a))] | 1/2+J/[3S(b)]+1/[6S(a)] |

To derive this, the geometric odd/even lookback masses are 2/3 and 1/3.
Thus C_a=rho(a)/2+H_b(a)/3+H_a(a)/6, and analogously for b.
Coprime kernels have H_a(a)=0; shared-divisor kernels have H_a(a)=rho(a)/S(a).
The nearest and OFF formulas follow directly from their OWN conditional laws.
For a!=b the two-letter word is primitive; ab and ba are one packet. For
a=b the table gives exactly twice the constant time, not another primitive.

In particular write z_2=Z(2), z_3=Z(3), s_2=S(2), s_3=S(3). The fixed tests are

| Own owner | 2^infinity | (2,3)^infinity least time |
| --- | --- | --- |
| MAIN | log4 | log[12/((1/2+1/(3z_3))(1/2+1/(3z_2)))] |
| OFF | log2 | log12 |
| NEAR | log4 | log[12/((1/2+1/(2z_3))(1/2+1/(2z_2)))] |
| SHARED | log[4s_2/(1+s_2)] | log[12/((1/2+1/(6s_2))(1/2+1/(6s_3)))] |

These are exact expressions, not numerical estimates. If desired the fixed
denominators have closed forms: summing rho over even integers gives
s_2=integral_0^1 1/(1+x) dx=log2, while summing over multiples of three gives
s_3=integral_0^1 x/(1+x+x^2) dx=(log3)/2-pi/(6 sqrt3); z_j=1-s_j.
The integral identities follow by summing the nonnegative integral expansion
rho(a)=integral_0^1 x^(a-2)(1-x) dx, so no numerical data are involved.

## 7. Gate and proof boundary

MAIN's constants ALL have composite integer index 2a(a-1); already 2^infinity
has least time log4, not log p for a prime. STOP promotion of MAIN.
NEAR has the same counterexample. OFF has constant 3 of time log6, despite
its constant 2 having time log2. For SHARED, 1/2<s_2<1 gives
1<4s_2/(1+s_2)<2, so its constant-2 positive time is below log2 and cannot
equal log p. These decisions do not depend on assigning primality to the other
exact two-letter expressions. All owner/control obligations above remain proved.
Genuine nonproduct infinite memory is established for MAIN, but does not repair
its clock mismatch. Full prime coverage is not claimed; no retuning or deletion.
Strong naturalness OPEN; T3 NOT AUDITED; classical NOT APPLICABLE; formal
UNASSIGNED; B NOT INVOKED. No external novelty claim or additional research.
