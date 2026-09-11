# Two-map source-only proof and value boundary

Author: /root/round211_fresh_residual_scout, 2026-09-09 UTC.
Status of the deductions below: PROVABLE AS STATED.
Status of a paper-scale, source-subtracted two-axis contract: NOT CURRENTLY JUSTIFIED.
These are author deductions, not an independent review, pilot observation or novelty certificate.

## 1. Q2F: a directly owned quadratic family

For every m>=1, let R_m=Z/2^m Z and Q_m(x)=x+x^2. Put v(0)=m and use the truncated 2-adic valuation otherwise.

### Proposition Q1: full graph, all-step fibres and cycle census

The even residues are exactly the recurrent set. Q_m is a permutation on them, every odd residue has entry time one, and every recurrent vertex has one odd leaf in addition to its recurrent predecessor. Every target y and every k>=1 satisfy
\[
 |Q_m^{-k}(y)|=\begin{cases}2,&y\text{ even},\\0,&y\text{ odd}.\end{cases}
\]
Zero is fixed. On the nonzero even shell v(x)=s, 1<=s<=m-1, every point has period
\[
 \ell_{m,s}=2^{\max(m-2s,0)}.
\]
That shell has 2^{m-s-1}/ell_{m,s} cycles. These statements also cover m=1, with no nonzero even shell.

Proof. The product x(x+1) is always even. For two inputs of the same parity,
\[
 Q(a)-Q(b)=(a-b)(a+b+1),
\]
and the second factor is odd. Thus each parity class maps injectively, hence bijectively, onto the even class. This proves recurrence, the height-one leaves and the one-step fibres. On the even class every iterate is bijective, so the same two-source count holds for all positive k.

For a nonzero even integer lift x of valuation s, Q(x)-x=x^2 has valuation 2s. Every even orbit point z has Q'(z)=1+2z=1 modulo 4. Suppose g=Q^{2^r} and d=g(x)-x has valuation 2s+r. The chain rule gives g'(x)=1 modulo 4. Exact polynomial expansion gives
\[
 g(g(x))-x=d(1+g'(x))+d^2 B
\]
with an integer B. The first summand has valuation 2s+r+1; the second has strictly larger valuation since v(d)>=2. Induction therefore gives
\[
 v_2(Q^{2^r}(x)-x)=2s+r.
\]
Reduction modulo 2^m shows that a power-of-two iterate fixes x for the first time at r=max(m-2s,0). The minimal period divides that power of two, and no smaller power of two fixes x. This proves the period formula. Divisibility counting gives the shell size and hence the cycle count. Each parity branch bijection assigns precisely one odd leaf to each recurrent vertex. All assertions follow. Square.

Source subtraction. Fan--Liao, Theorem 6.2 and its full proof, treats the exact polynomial over Z_2 and explicitly tracks its finite-quotient cycle lifts. The finite period formula above is a direct consequence/rederivation of that decomposition, not a new theorem credited against it. The inverse is the elementary odd-cofactor parity bijection, with no surviving independent mechanism. Decision: KILL_DIRECT_OWNER_AND_CONSTANT_FIBRES.

This is not the old Artin--Schreier map over F_(2^m). Already at carrier size four, Q modulo four has two fixed points (0,2), while a^2+a=a over F_4 implies a=0, giving one. Thus those two finite maps are not conjugate. Nor is this P157's cubic 3x^2-2x^3; the cubic's generic valuation/Taylor lifting receives no new credit here.

## 2. SDT: synchronous Dijkstra token-ring literal

Let n>=3, q>=n, L=n-1 and X=(Z/q Z)^n, with coordinates indexed 0,...,L. All right-hand sides below use the old state:
\[
 F(x)_0=x_0+[x_0=x_L]\pmod q,\qquad F(x)_i=x_{i-1}\quad(1<=i<=L).
\]
This is a total finite deterministic self-map, with no scheduler coordinate or external input.

For the orbit starting at x, write h_t=F^t(x)_0 and delta_t=h_{t+1}-h_t in {0,1}; the subtraction uses its actual increment, not an arbitrary representative. For 0<=j<L, the head sees the as-yet-unreplaced initial coordinate x_{L-j}. Therefore
\[
 \delta_j=[h_j=x_{L-j}],\qquad h_j=x_0+\sum_{a<j}\delta_a \pmod q.       \tag{H}
\]
For a fixed initial head a and fixed word w=(delta_0,...,delta_{L-1}), each 1 fixes its consulted coordinate, and each 0 permits exactly q-1 distinct alternatives, independently. Consequently its initial-state fibre has weight
\[
 W(w)=(q-1)^{L-|w|}.                                                \tag{W}
\]
This is a weighted coding/quotient of all initial states, not a full-carrier conjugacy: those free alternatives are genuinely discarded.

### Proposition S1: exact reduced map and recurrent structure

Let Y consist of targets y with every difference y_i-y_{i+1} in {0,1}. Such a target is uniquely coded by its head h=y_0 and its chronological difference word
\[
 w_j=y_{L-j-1}-y_{L-j}\in\{0,1\},\quad0<=j<L.
\]
Then F^L(X)=Y. On Y the map is exactly
\[
 (h,w)\longmapsto(h+[w=0^L],\,g(w)),\qquad
 g(w)=(w_1,\ldots,w_{L-1},[w=0^L]).                                \tag{G}
\]
Its recurrent set C consists exactly of the q(L+1)=qn states with |w|<=1 and forms one cycle of length nq. The maximum recurrent-entry time on X is
\[
 T=2L-1=2n-3.
\]
The maximizing sources are exactly those for which delta_{L-2}=delta_{L-1}=1 in (H), and they number q^{n-2}.

Proof. Copying gives F^L(x)=(h_L,h_{L-1},...,h_0). Conversely (H) constructs a source for every a and every binary word, proving the image assertion and the target coding. For y in Y, the difference y_0-y_L is the sum of its L bits. Because 0<=|w|<=L<q, equality modulo q holds exactly when w is zero. The next copy step shifts the history and appends that equality indicator, giving (G).

Until all old ones disappear, g only shifts and appends zeros. A word with at least two ones becomes a one-one word when its second rightmost one falls off. The words of weight at most one form the cycle
\[
 0^L\to e_{L-1}\to e_{L-2}\to\cdots\to e_0\to0^L
\]
of length n. The head increases once during each turn of this word cycle, so the full qn states form one nq-cycle. Every word reaches it within L-1 further steps. Since every recurrent state belongs to every iterate image, no recurrent point outside Y has been missed.

If the initial history word has at least two ones and its second rightmost one is at position r, its entry time is exactly L+r+1: it is still nonrecurrent at time L, and afterwards at least two old ones survive through step r. If the word has at most one one, entry is at most L. Since L>=2, the maximum T>L is therefore attained exactly when its last two bits are both one. The weighted count of these sources is
\[
 q\sum_{p\in\{0,1\}^{L-2}}(q-1)^{L-2-|p|}
 =q\,q^{L-2}=q^{n-2}.
\]
An explicit witness is x_0=0, x_i=L-i for 1<=i<=L: (H) makes all its first L head increments one. This proves sharpness without a finite run. Square.

### Proposition S2: every-target k-step inverse atlas

Write N_k(y)=|F^{-k}(y)|. For 0<=k<=L,
\[
 N_k(y)=
 \begin{cases}
 (q-1)^{\,|\{0<=i<k:y_i=y_{i+1}\}|},
   &y_i-y_{i+1}\in\{0,1\}\text{ for every }i<k,\\
 0,&\text{otherwise}.
 \end{cases}                                                       \tag{I1}
\]
The k=0 condition is empty and gives one for every target. In particular,
|F^k(X)|=q^{n-k}2^k in this range. The maximum fibre is (q-1)^k, attained exactly at the q^{n-k} targets whose first k+1 coordinates agree.

For k=L+u, 1<=u<=L-1, N_k(y)=0 outside Y. For y in Y with word v, the following disjoint cases give every fibre:
\[
 N_{L+u}(y)=
 \begin{cases}
 q^u(q-1)^{L-u-|v|},
       &v\ne0,\quad v_{L-u}=\cdots=v_{L-1}=0,\\
 q^{u-1}(q-1)^{L-u},&v=0,\\
 (q-1)^L,&v=e_{L-u},\\
 q^r(q-1)^{L-1-r},&
       v=e_j,\ L-u<j<=L-1,\quad r=j+u-L-1,\\
 0,&\text{otherwise}.
 \end{cases}                                                       \tag{I2}
\]
(The two single-one rows can be grouped as one case with r=-1 separated.) For k=T+a, a>=0, only C can have nonempty fibres, and
\[
 N_{T+a}(y)=N_T(F_C^{-a}(y)),\qquad y\in C.                          \tag{I3}
\]
Here F_C is the explicitly given single-cycle permutation. Since each count in (I2) is independent of the head, the eventual count profile has period n, although the state cycle has length nq.

Proof. For k<=L, a preimage must have
x_0,...,x_{L-k}=y_k,...,y_L. The first k target differences prescribe exactly the k head increments. The k lost tail coordinates are distinct from these fixed coordinates. Each required increment one fixes one of them, and each zero allows q-1 alternatives. This proves (I1), including its image size and equality case.

For larger k, use the weighted coding (W) at time L. Given a target head and a history word mapping to v under g^u, the initial head is uniquely determined; the discarded-coordinate multiplicity remains W. If an old one survives, then v is nonzero with final u zeros; any prefix of u old bits may precede the surviving suffix. Summing its weights multiplies by q^u and yields the first row.

For v=0 the last original one must be at position u-1. Its earlier u-1 bits are arbitrary, and its later L-u bits are zero. This yields the second row. A newly injected one appears at position j>=L-u. If the original word was zero, it lies at j=L-u and contributes (q-1)^L. Otherwise the last original one was at r=j+u-L-1 in 0,...,u-2. Its r earlier bits are arbitrary and all L-1-r later bits are zero, giving the fourth row. No second newly injected one can occur in u<=L-1<n steps. These alternatives are exhaustive and disjoint, proving (I2). Finally F^T(X)=C and F_C is bijective, so each recurrent target has one possible predecessor in C at distance a; this proves (I3). Square.

This is an evaluated all-time, all-target count, not just a transfer-matrix restatement. It does not by itself specify every preimage-tree isomorphism or all correlations between branches.

### Proposition S3: exact recurrent-depth distribution

Let tau(x) be recurrent-entry time and A_t=|{x:tau(x)<=t}|. Then
\[
 A_0=qn,\qquad
 A_t=q\bigl[(n-t)(q-1)^t+t(q-1)^{t-1}\bigr]\quad(1<=t<=L),           \tag{D1}
\]
and
\[
 A_{L+u}=q^{u+1}(q-1)^{L-u-1}(q+L-u-1)
           \quad(0<=u<=L-1).                                      \tag{D2}
\]
The formulas agree at t=L. A_t=q^n for t>=T, and the exact depth-t count is A_t-A_{t-1}, with A_{-1}=0.

Proof. Since C is forward invariant, A_t is the sum of N_t(y) over y in C. Each recurrent target is either constant or has one unit difference at one of the L positions, with q head choices. Among its n word phases, t phases place that unit difference in the first t target differences, while n-t do not. Formula (I1) therefore gives (D1).

At time L+u, a history word yields a recurrent state precisely when the surviving original suffix of length L-u has weight at most one. Its arbitrary u-bit prefix has total weight q^u, while that suffix contributes
\[
 (q-1)^{L-u}+(L-u)(q-1)^{L-u-1}.
\]
Multiplying also by q head choices gives (D2). At u=L-1 it equals q^n, and the last shell is q^n-q^{L-1}(q^2-1)=q^{n-2}, agreeing with S1. Square.

### Exact source and value boundary

These S1--S3 proofs are the scout author's deductions from the literal, not claims that they were read in a primary source. The root agent asked whether an all-target/depth residual survived, but did not author these proofs.

All three results factor through (H), (W), (G): a finite head-delay history, independently discarded alternatives, and a shift that injects a one only at the zero word. Counting uses only the binomial identity sum_p(q-1)^{r-|p|}=q^r. Thus the complete inverse/depth axis does not provide a materially independent mechanism beyond the temporal reduction. Classical ownership of the local Dijkstra rule further removes literal novelty. Decision: KILL_VALUE_WEIGHTED_HEAD_HISTORY. No pilot is requested; increasing cutoffs cannot fix this value failure.

The first source comparison suggested that an n-step synchronous legitimacy bound might be compatible with a 2n-3 recurrent-entry bound. That suggestion is WITHDRAWN for this literal. The distinction exists pointwise, but does not explain the worst-case discrepancy. Under the natural Dijkstra privileges, the hand witness at n=q=4 is
\[
 (0,2,1,0)\to(1,0,2,1)\to(2,1,0,2)\to(3,2,1,0)
 \to(3,3,2,1)\to(3,3,3,2).
\]
At time four, normal machines 2 and 3 are both privileged. At time five, the state is recurrent and has one privilege. Hence this example is neither legitimate nor recurrent by time n. The displayed substitutions are symbolic hand deductions, not a software execution or a proof that a specified published theorem is false. The exact source qualification is in SOURCES_AND_SUBTRACTION.md.
