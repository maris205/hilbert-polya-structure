# Fresh55 — all-parameter desk proofs

These are author deductions, not a manuscript, numerical test or accepted
candidate gate. Scope and prior-mechanism deductions are in [DESK.md](DESK.md).

## 1. Carrier and valuation

Fix a prime power q and m>=2. Put R=F_q[t]/(t^m), I=tR, and define

    F:I² -> I²,       F(x,y)=(y,x(t+y)).

Both coordinates remain in I. For z in R, let v(z) be its least nonzero
coefficient degree, with v(0)=m. Then v(zw)=min(m,v(z)+v(w)), and
|t^r R|=q^(m-r) for 0<=r<=m. If z is in t²R, then v(t+z)=1.

Given (x,y), set x_0=x, x_1=y and

    x_(n+2)=x_n(t+x_(n+1)).

Then F^n(x,y)=(x_n,x_(n+1)). All x_n lie in I, and x_n lies in t²R for
every n>=2, because its defining two factors both belong to I. Consequently
v(t+x_n)=1 for every n>=2. Only the initial factor t+y can have extra
cancellation; it is not assumed to have valuation one.

## 2. Exact hitting time

Let a=v(x), b=v(y). The first time tau with F^tau(x,y)=(0,0) is

    tau=max{2(m-b),2(m-a)-1}.                         (T)

Proof when b>=2. Since v(t+y)=1 and all later multiplier valuations are one,
induction gives, for all k>=0,

    v(x_(2k))   = min(m,a+k),
    v(x_(2k+1)) = min(m,b+k).

The last potentially nonzero even-indexed term is x_(2(m-a-1)) when a<m;
the last potentially nonzero odd-indexed term is x_(2(m-b-1)+1) when b<m.
The state becomes zero one position after the last nonzero term. Thus the
even chain contributes 2(m-a)-1 to tau and the odd chain 2(m-b), taking
zero when a chain is identically zero. If a=b=m the maximum in (T) is zero.
These statements also directly cover exactly one initially zero coordinate.

Proof when b=1. The first even successor x_2 may undergo cancellation, but
for k>=1 induction still gives

    v(x_(2k)) >= min(m,a+k).

On the odd chain there is no such cancellation: x_2 and every later adjacent
even term lie in t²R, so for all k>=0

    v(x_(2k+1)) = min(m,1+k).

In particular x_(2m-3) is nonzero and both x_(2m-2), x_(2m-1) vanish.
Hence tau=2m-2. Since a>=1, 2(m-a)-1<=2m-3, exactly as (T) asserts.
This includes m=2: x_1 is nonzero and x_2=x_3=0. This proves (T).

Every state reaches zero and zero is fixed, so it is the unique recurrent
state, with period one. Formula (T) shows that the maximum depth is 2m-2
and occurs exactly on v(y)=1. No coordinatewise exact-increment claim was
needed in the cancellation branch.

For clarity, the challenged example (x,y)=(t,-t) has x_2=0 and, for k>=1,

    F^(2k)(t,-t)   = (0,-t^(k+1)),
    F^(2k+1)(t,-t) = (-t^(k+1),0),

with powers interpreted modulo t^m. Its first zero state is 2m-2. The initial
question whether cancellation refuted (T) was resolved by this full-state
calculation, not by changing the carrier from I to t²R.

## 3. Exact depth census

For an integer 0<=h<=2m-2, formula (T) is equivalent to

    a >= m-ceil(h/2),       b >= m-floor(h/2).

Both right-hand thresholds lie between 1 and m. The independent ideal
cardinalities therefore give

    #{(x,y):tau(x,y)<=h}
      = q^ceil(h/2) q^floor(h/2) = q^h.

There is one depth-zero state, and subtraction gives (q-1)q^(h-1) states
at depth h>=1. In particular the complete depth polynomial is

    1 + (q-1) sum_(h=1)^(2m-2) q^(h-1) z^h.

This is a nilpotent full-state clock/depth distribution, not an orbit
enumeration run. It also yields q^(2m-2) total states as required.

## 4. Complete one-step fibres

Fix a target (u,w) in I². A predecessor must have y=u and must solve

    (t+u)x=w,             x in I.                    (E)

Put d=min(v(t+u),m-1). If d<=m-2, write t+u=t^d e with e a unit of R.
Multiplication by t+u maps I onto t^(d+1)R and its kernel in I is
t^(m-d)R, of size q^d. Thus (E) is solvable exactly for w in t^(d+1)R;
given any one solution x_0, all predecessors are precisely

    {(x_0+k,u): k in t^(m-d)R}.

For instance, if w=t^(d+1)w_0, one may choose x_0=t e^-1 w_0, with any
lift of w_0; the resulting ambiguity is just the displayed kernel.

If d=m-1, then (t+u)I=0, whether v(t+u)=m-1 or t+u=0. Equation (E)
therefore is solvable exactly when w=0; all q^(m-1) values x in I solve it.
This is again the coset of t^(m-d)R=I. Hence the stated image criterion
and q^d fibre count are uniform, including this saturated case.

For 1<=d<=m-2, translation u -> t+u permutes I, and exactly
(q-1)q^(m-d-1) choices of u have v(t+u)=d. Each such u admits
q^(m-d-1) possible w. Thus the number of q^d-element fibres is

    (q-1)q^(2(m-d-1)).

In the saturated case t+u in t^(m-1)R gives exactly the q elements
u=-t+c t^(m-1), c in F_q, each admitting only w=0. These are exactly
the largest-fibre targets. Summing the nonempty-target counts proves

    |image F|=q+(q-1) sum_(j=1)^(m-2) q^(2j).

The carrier minus this number is the zero-fibre census. For m=2 the middle
range is empty, all q nonempty fibres have q elements, and F(x,y)=(y,0).

## 5. Explicit old-primitive and linear controls

On the same I² define M(a,b)=(b,ab), P(x,y)=(x,y+t), Q(u,w)=(u-t,w).
All three maps are well-defined; P and Q are bijections. Direct substitution
gives F=Q M P. This transports every one-step fibre and image census from
ordinary multiplication. Since Q is not P^-1, this calculation does not
transport F^n to M^n and is not a dynamical-conjugacy proof. The old MFR
literal was defined on fields; a different carrier is disclosed here.

The linear control L(x,y)=(y,tx) has the two valuation chains in the b>=2
proof for every a,b, and therefore exactly (T) and the same depth census.
At m=2, the literal maps F and L coincide because xy=0 in R.

At m>=3, F has nonempty fibres of size q (the d=1 row has a positive
number of targets) and q^(m-1), which are unequal. For any endomorphism
phi of a finite group, a nonempty fibre is a coset of ker(phi), so all
nonempty fibres have the same size. A bijective dynamical conjugacy
preserves fibre sizes. Thus F is not conjugate to any finite-group
endomorphism, and in particular not to L or any finite linear map.
This does not rule out all nonlinear old literals, factors, or extensions.

## 6. Provenance and unresolved gate

The scout derived Sections 1–4 and the linear/nonuniform-fibre controls.
Root challenged and then clarified the cancellation branch. The independent
collision-search process supplied the explicit P/Q subtraction, which the
scout has checked algebraically. Those participants are proof-familiar and
are not presented as noncontributor gate reviewers.

No code in this package has been executed to test these mathematical claims.
No finite examples, measured counts or field enumeration are being used as
proof. Independent candidate/value review and unresolved old-literal/factor
clearance remain open; the present deductions alone do not authorize entry.
