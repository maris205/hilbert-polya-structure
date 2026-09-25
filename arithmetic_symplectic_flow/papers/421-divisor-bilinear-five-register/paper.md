# Divisor bilinear feedback: owned clocks and an empty short-return window

Candidate ID: `ANG-20260923-DBF01`. Paper421; 2026-09-23.
Batch `QUOTIENT-FEEDBACK-20260923-O`, round2/5.
Outcome: `OWNED BILINEAR IMAGE CLOCK; FROZEN SHORT-RETURN WINDOW EMPTY — BOUNDED OPEN / FORK`.

Contract: [candidate card](candidate-card.md), original99 lines including the
pre-analysis clarification, fully read before proof.
Scope: four complete inverse/IMAGE/history owners; fixed states in
\(W=C_+\cup C_-\) and all four length-two words with BOTH endpoints in \(W\).
No global fixed-set or higher-period census is claimed.
T3 NOT AUDITED; classical NOT APPLICABLE; formal UNASSIGNED; Route B NOT INVOKED.
AI-assisted derivation/drafting; shared-history NOT_CALIBRATED.

## Abstract

A current bilinear observable and a current integer divisor digit determine
a five-register rational transport. Its full real carrier admits a countable
actual inverse atlas and a prescribed finite positive IMAGE density at every
legal branch point, including floor faces. The same owner supplies the signed
clock, retained-lag groupoid and height action. We classify the entire frozen
one/two-step window for MAIN and its three controls: all fixed sets and all
four two-step word sets are empty there. This establishes neither global
absence of positive returns nor a prime-period obstruction for MAIN. The
planned discriminating window is exhausted, so the candidate remains bounded
OPEN and the search forks without tuning its source or clock.

## 1. Exact arithmetic source and four owners

Each owner has its own \(X=\mathbb R^5\), ordinary Borel structure and
\(\mu=\mathrm{Leb}_5\). At \(z=(a,b,c,d,e)\), set
\[
 N(z)=ac+bd,\quad m=\lfloor e\rfloor,\quad n=\lfloor N(z)\rfloor.
 \tag{1}
\]
MAIN is legal precisely when \(m\ne0,m\mid n,c\ne0,e+qc\ne0\), where
\(q=n/m\), and
\[
 Tz=(b,c,d,e,N(z)/(e+qc)).
 \tag{2}
\]
G replaces permission by \(q_G=\lfloor n/m\rfloor\) for \(m\ne0\), and
\(q_G=0\) for \(m=0\). Its only restrictions are \(c\ne0,e+q_Gc\ne0\);
its numerator remains \(N\). Q retains MAIN arithmetic permission, requires
\(c\ne0,e\ne0\), and has last output \(N/e\). B retains MAIN permission
and geometric domain but has last output \(ac/(e+qc)\).

All signs, zero coordinates, units, \(n=0\), half-open floor faces and
failed sources remain. The complement of each own domain is terminal for
its next step, not an absorbing extension or a deleted subset. Every point
has its identity history; every actual predecessor is retained. A terminal
next-step clock is NOT DEFINED, never silently zero.

The [prior-work](../../docs/prior_work/README.md) interface is exact:
for integers \(N_0\ge2\), \(1<d_0<N_0\), the seed
\((N_0-1,1,1,1,d_0)\) has \(N=N_0,m=d_0,n=N_0\).
If \(d_0\mid N_0\), then \(c=1\) and \(e+qc=d_0+N_0/d_0>0\);
otherwise the arithmetic permission fails. Thus MAIN legality on this
interface is equivalent to the original proper-divisor test.
The quotient changes actual transport and the shifting coordinates enter
future reads. This is a stated geometric deformation of divisibility
admissibility, not a conjugacy to a prior symbolic system or a claim of
natural prime periods. No prime table, zero data, chosen centre or roof is used.

## 2. Complete actual inverse atlases and incoming

Write a target \(y=(u,v,w,s,t)\). For MAIN enumerate every integer
\(m\ne0,n\) with \(m\mid n\), put \(q=n/m\), and set
\[
 K=s+qv,\quad A_q=(Kt-uw)/v,\quad
 \theta_{m,n}(y)=(A_q,u,v,w,s).
 \tag{3}
\]
Its exact target domain \(E_{m,n}\) is
\[
 v\ne0,\quad K\ne0,\quad
 \lfloor s\rfloor=m,\quad \lfloor A_qv+uw\rfloor=n.
 \tag{4}
\]
The frozen own-source and forward-equality tests are included: (4) implies
them, since the reconstructed \(c=v,e=s,N=A_qv+uw=Kt\).
Conversely a genuine predecessor has precisely this \(m,n,q,A_q\).
No target-next-step restriction occurs.

For G enumerate ALL \(m,n\in\mathbb Z\), use its own \(q_G(m,n)\)
in (3), and impose (4) with that \(q_G\). These are exactly its own
source tests; MAIN divisibility must not be inserted in G.
For B enumerate MAIN's legal \(m,n\), replace \(A_q\) by
\[
 A^B_q=Kt/v,\qquad
 E^B_{m,n}=\{vK\ne0,\ \lfloor s\rfloor=m,\
                  \lfloor A^B_qv+uw\rfloor=n\}.
 \tag{5}
\]
Here the floor observable still includes \(uw\), although the transported
numerator does not. Substitution gives \(A^B_qv/K=t\); the converse
recovers every B predecessor from its own actual digits.

Q has the SINGLE candidate
\[
 A^Q=(st-uw)/v,\quad \theta_Q(y)=(A^Q,u,v,w,s);
 \quad v s\ne0,\quad m=\lfloor s\rfloor\ne0,\quad
 m\mid\lfloor A^Qv+uw\rfloor .
 \tag{6}
\]
The same substitutions prove both inverse identities. No quotient index
duplicates this candidate; Q is globally injective on its partial domain.

All domains above are Borel. Each branch is injective: applying its own
forward formula recovers the target. Every predecessor must have the four
last source coordinates \((u,v,w,s)\); solving its final output yields
(3), (5) or (6), proving completeness. An actual source fixes both floors
uniquely even when several integer labels share a quotient. Thus there are
no artificial label copies, and all remaining inverse multiplicity is actual.
The enumeration is countable and untruncated. In particular \(v=0\) targets
have no predecessors, but targets on other null or terminal sets are still
tested by the complete atlas; \(t=0\) is not an exclusion.

For each owner define \(P(y)\) as ALL passing inverse points and
\[
 P^0(y)=\{y\},\qquad
 P^{j+1}(y)=\bigcup_{x\in P^j(y)}P(x).
 \tag{7}
\]
Induction using the two inverse identities proves that \(P^j(y)\) is
exactly the set of legal \(j\)-step predecessors. It includes all depths,
all labels and all sources outside the test window. No continuity across
floor faces or locally compact groupoid assertion is required.

## 3. Every-Borel IMAGE and the fixed pointwise version

In each inverse, the last four source coordinates are \((u,v,w,s)\).
Expansion along those four rows leaves the derivative of the first
coordinate with respect to \(t\). Consequently
\[
 J_{T,\theta}=J_{G,\theta}=J_{B,\theta}=|K/v|,
 \qquad J_{Q,\theta}=|s/v|.
 \tag{8}
\]
This calculation uses each owner's actual first coordinate separately:
\(\partial_t A_q=K/v\), \(\partial_t A^B_q=K/v\), and
\(\partial_t A^Q=s/v\). G uses its own \(q_G\).
All values are finite and strictly positive on their own exact domains.

For fixed \(q\), the displayed rational expression and its inverse are
smooth on \(vK\ne0\), respectively \(c(e+qc)\ne0\); Q uses \(vs\ne0\)
and \(ce\ne0\). The substitutions above exhibit inverse diffeomorphisms
on these geometric open sets, before any digit restriction. The usual
change-of-variables theorem applied to their Borel subsets therefore gives
\[
 \mu(\theta E)=\int_E J_\theta\,d\mu
 \quad\text{for EVERY Borel }E\subseteq E_\theta .
 \tag{9}
\]
This includes arbitrary null Borel subsets. Equation (8) prescribes the
analytic-extension value at every assigned floor face; it is not a claim
that measure alone fixes a unique version at null points, nor a claim of
a global derivative across arithmetic cuts.

At a legal source put
\[
 \lambda_T(z)=\left|\frac c{e+qc}\right|,\quad
 \lambda_G(z)=\left|\frac c{e+q_Gc}\right|,\quad
 \lambda_B(z)=\left|\frac c{e+qc}\right|,\quad
 \lambda_Q(z)=|c/e|,\qquad \kappa_O=\log\lambda_O .
 \tag{10}
\]
Indeed \(v=c,s=e\) at its own target, so each \(\lambda\) is exactly
\(J_{\theta_z}(T_Oz)^{-1}\). The matching expressions for MAIN and B do
not identify their transports, histories or returns. These clocks may
have either sign or vanish; none is relabelled as a positive roof.

## 4. Entire history, kernels, isotropy and real phases

Fix any one owner \(O\) and write \(T,\lambda,\kappa\) for its own data.
For each legal history set
\[
 M_j(z)=\prod_{i=0}^{j-1}\lambda(T^iz),\quad
 S_j(z)=\log M_j(z),\qquad M_0=1,\ S_0=0.
 \tag{11}
\]
All factors are finite positive; no logarithm of a terminal-step value is
taken. The countable Borel groupoid is the set of actual triples
\[
 G=\{(z,r-s,w):T^rz=T^sw,\ r,s\ge0\text{ legal}\},
 \quad c(z,r-s,w)=\log\frac{M_r(z)}{M_s(w)}.
 \tag{12}
\]
Range is \(z\), source is \(w\); equal triples are identified.
Two presentations of the same triple differ by adding the same number
of steps to both ends. Their common-tail products cancel, proving descent.
For composition, align the two histories at the common middle point:
if one middle exponent is smaller, extend that equality using only the
longer already legal middle history. The resulting equality has the sum
of the two lags, and the middle products cancel. This proves closure,
the cocycle identity and inverse rule \(c(g^{-1})=-c(g)\), without
inventing continuation past a terminal.

In particular the forward arrow \((Tz,-1,z)\) has \(c=-\kappa(z)\).
On every actual history bisection the IMAGE density of the arrow
\(w\mapsto z\) is \(M_s(w)/M_r(z)=e^{-c}\), by repeated (9).
The Borel structure is inherited from \(X\times\mathbb Z\times X\);
the countable inverse atlases supply its actual branches.

The complete kernels, with the actual \(\lambda_O\) in (10), are
\[
 \begin{aligned}
 \ker\ell&=\{(z,0,w):T^rz=T^rw\text{ for some legal }r\},\\
 \ker c&=\{(z,r-s,w)\in G:M_r(z)=M_s(w)\},\\
 \ker\ell\cap\ker c
 &=\{(z,0,w):T^rz=T^rw,\ M_r(z)=M_r(w)
                    \text{ for some legal }r\}.
 \end{aligned} \tag{13}
\]
These are exact product tests, not restrictions to a chosen periodic sector.
For Q, injectivity and backward cancellation give
\(\ker\ell=G^{(0)}\), hence also \(\ker\ell\cap\ker c=G^{(0)}\).
No such cancellation is presumed for the other owners.

Nonzero source isotropy occurs exactly when the legal future is eventually
periodic: a nonzero-lag equality is an actual repetition, and conversely
each repetition gives such an equality. If the eventual core has least
source period \(p\), let
\[
 C=\sum_{i=0}^{p-1}\kappa(T^iF).
 \quad G_z^z=p\mathbb Z,\quad
 c(z,kp,z)=kC,\quad H_z=C\mathbb Z .
 \tag{14}
\]
To see that these are ENTIRE groups, every eventual repetition lag is
a multiple of the least period, every such multiple is legal, and the
finite entrance products cancel. A non-eventually-periodic or
finite-terminal future has \(G_z^z=\{0\}\) and \(H_z=\{0\}\).

The extension keeps ALL \((z,h)\in X\times\mathbb R\), with
\((w,h)\mapsto(z,h+c)\). On its orbit SET, the action
\(\rho^t[z,h]=[z,h+t]\) is defined for all real \(t\), since height
translation commutes with every extension arrow.
The extension groupoid isotropy at an eventually periodic source
is \(\{kp:kC=0\}\); the height-action stabilizer is the ENTIRE \(H_z\).
If \(C\ne0\), the positive primitive is \(|C|\), with repetitions
\(k|C|\) and trivial extension isotropy. If \(C=0\), the source
\(p\mathbb Z\) survives in extension isotropy but gives no positive time.
Non-eventually-periodic sources also give no positive stabilizer.

For a source packet choose any base \(b\) and actual arrow \(g_z:z\to b\).
Its phase is \(h+c(g_z)\) modulo \(H_b\); changing the arrow changes this
by a loop in \(H_b\), exactly the necessary identification. If
\(T^az=T^ib\), that phase is \(h+S_i(b)-S_a(z)\).
For a fixed base it is \(h-S_a(z)\). For a periodic core \(\mathcal C\),
its entire source packet is \(\bigcup_{F\in\mathcal C,j\ge0}P^j(F)\):
tail equivalence to the core is precisely eventual arrival at it.
All phases \(\mathbb R/H_b\) remain, and distinct packets are not merged
when their clocks coincide. No manifold or Hausdorff orbit quotient is claimed.

Useful complete control-clock consequences require no period census.
Along any periodic core write its cyclic register sequence as
\((a_i,a_{i+1},\ldots,a_{i+4})\); every \(a_i\ne0\), since each becomes
a legal third coordinate. For Q,
\(\prod_i\lambda_Q=\prod_i|a_{i+2}/a_{i+4}|=1\).
For B, its actual update gives
\(\lambda_B(T^iF)=|a_{i+5}/a_i|\), so its cycle product is also one.
Thus \(H_z=\{0\}\) for EVERY Q and B source, including preperiodic
and terminal sources; periodic source isotropy is not removed.
This does not make their step clocks or all arrows zero-clock.
For MAIN/G the exact general cycle formula is
\[
 C=-\sum_{i=0}^{p-1}\log|1+q_i c_i/e_i|,
 \tag{15}
\]
because the product of \(c_i/e_i\) cancels around the register cycle.
Existence and classification of those cores outside the frozen probe are OPEN.

## 5. Complete fixed and two-step window audit

The frozen cells are
\(C_\pm=\{z:\lfloor e\rfloor=\pm1,\lfloor ac+bd\rfloor=2\}\)
and \(W=C_+\cup C_-\); BOTH endpoints of a tested two-step word lie in \(W\).
Let \(I_+=[1,2)\), \(I_-=[-1,0)\), \(k_+=3,k_-=-1\).
The first four output coordinates are identical shifts in all four owners.
Therefore every actual \(T^2z=z\) with both endpoints in \(W\) must be
\[
 z=(u,v,u,v,u),\quad Tz=(v,u,v,u,v),\quad
 u\in I_\epsilon,\ v\in I_\delta,\quad
 2\le L:=u^2+v^2<3.
 \tag{16}
\]
Conversely the own last-coordinate equations below, together with (16),
are sufficient for a two-step closed word. Here \(u,v\ne0\); the successive
\(m\) values are \(1\) or \(-1\) according to \(\epsilon,\delta\), and
\(n=2\), so MAIN/Q/B permission holds.
MAIN/G/B denominators are \(k_\epsilon u,k_\delta v\ne0\);
Q denominators are \(u,v\ne0\). Thus this reduction discards no legal
boundary solution and imports no domain from another owner.

MAIN and G separately have \(q=2\) on \(C_+\), \(q=-2\) on \(C_-\).
Their closure equations are
\[
 L=k_\epsilon uv=k_\delta uv.
 \tag{17}
\]
For \(++\), \(L=3uv\ge3\), contrary to \(L<3\).
For \(+-\), the first expression \(3uv\) is negative; for \(-+\),
the second expression is negative. For \(--\), \(L=-uv<0\).
Thus each of the four words is empty for EACH of MAIN and G.

For Q, every word requires \(L=uv\), whereas
\(u^2-uv+v^2=(u-v/2)^2+3v^2/4>0\); none closes.
For B, the two equations are
\[
 v=u/k_\epsilon,\qquad u=v/k_\delta.
 \tag{18}
\]
Since \(u\ne0\), the product \(k_\epsilon k_\delta\) must be one.
Its values for \(++,+-,-+,--\) are \(9,-3,-3,1\).
The remaining \(--\) possibility requires \(v=-u\), impossible when
both are negative. Its allowed corner \(u=v=-1\) is included and fails.

The fixed-state check can also be recorded directly. A fixed point must
be \(z=(t,t,t,t,t)\). Its exact window cuts give
\(t\in[1,\sqrt{3/2})\) in \(C_+\), and \(t=-1\) in \(C_-\).
All these candidates meet the corresponding source-domain conditions.
The respective last outputs are \(2t/k_\epsilon\) for MAIN/G,
\(2t\) for Q, and \(t/k_\epsilon\) for B. None equals the nonzero \(t\).

| Owner | Fixed set in \(C_+\) | Fixed set in \(C_-\) | \(++,+-,-+,--\) |
| --- | --- | --- | --- |
| MAIN | empty | empty | all empty |
| G | empty | empty | all empty |
| Q | empty | empty | all empty |
| B | empty | empty | all empty |

This includes fixed points as possible two-step repetitions before excluding
them; no source-period-two packet was created from a repeated fixed point.
There is no period-one/two core satisfying this window test, hence no such
core's incoming basin or phase packet. Equation (7) still supplies all incoming
to every full-source target; it is not replaced by a window-restricted inverse.

## 6. Decision, reproducibility and limitations

The full source, every-Borel IMAGE and prescribed all-point signed clock
are established on the same owner. The divisor-symbolic interface is exact.
The geometric-clock component is therefore owned, but arithmetic T1 is
NOT PASSED and strong naturalness/PROVES_TOO_MUCH remain OPEN.
The complete frozen short-return window is empty for all four owners.
It provides neither a wrong-prime MAIN primitive nor a positive prime packet.
Accordingly it does NOT establish a global T2 failure or success.
Nonemptiness, prime purity, uniqueness and all-prime coverage for MAIN remain
unproved. Under the precommitted bounded stop, the decision is OPEN / FORK,
not permission to enlarge the window or alter the denominator.

Inputs are the 99-line frozen card and exact real/integer arithmetic.
Methods are direct inverse substitution, rational differentiation,
change of variables, history-product cancellation and the inequalities in
(16)--(18). There was no scientific code, numerical orbit table, external
literature search, operator, Route evaluation, PDF or Git action.
[Claim ledger](claim-ledger.md) and [overview](README.md) are the author surfaces.
No claim or clock is transferred from a control or another candidate.

Before freeze the source author read only
[292 card](../292-integral-braid-residue-flow/candidate-card.md) lines1--65 and
[400 card](../400-nonlinear-exchange-return/candidate-card.md) lines1--57.
Both were non-EOF definition prefixes; heading navigation exposed appended
outcome titles, not bodies. No old total or hash was measured.
The author has shared prior proposal/proof history, including292 and416;
this is not blind discovery or a global novelty/nonconjugacy claim.
A bounded card-only author helper, `dss_g_fixed_author`, supplied the G/Q/B
window algebra. The main author checked it and integrated it; that helper
was not an independent reviewer. No reviewer/raw/evidence/peer science was
read while producing these author files. Root owns card integration/review.

AI agents supplied source design, mathematical derivation, drafting and
author-side checking; the workflow separately uses AI internal review.
This is NOT_CALIBRATED, with no human or external verification certified.
Human authorship/contributions, funding and conflicts were not supplied;
none is invented. No human participants or personal data are involved.
Data availability: all scientific inputs and exact proofs are in the linked
Markdown package; there is no hidden empirical dataset.
