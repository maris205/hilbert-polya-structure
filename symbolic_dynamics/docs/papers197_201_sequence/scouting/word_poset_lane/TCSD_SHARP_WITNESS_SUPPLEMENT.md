# Exact junction calculation for the TCSD sharp witnesses

2026-09-05 UTC. Author proof supplement, not a change to the map or a paper
review. Use this explicit calculation in place of an unexplained
"four-phase junction calculation" in the manuscript.

Write Alt_l(s)=(s,−s,s,…), with s∈{−1,1}. In the following witness
arguments l>=2. This qualification avoids applying the old contract's
informal (2.7) to the single letter s, which is not recurrent at n=1.
That boundary already has its separate theorem H_1=1.

For r>=1 the literal, unrotated equality is

$$D(0^r\operatorname{Alt}_l(s))
 =0^{r-1}\operatorname{Alt}_{l+1}(s).$$

The signs at both junctions give the first and last letters of the new
alternating block. For even n, a fully alternating word is mapped to its
negative, hence lies in the core. For odd n=2m+1, m>=1, all four phases of
the one-zero witness are

$$\begin{aligned}
w=0\operatorname{Alt}_{2m}(s),\qquad
Dw&=\operatorname{Alt}_{2m+1}(s),\\
D^2w&=\operatorname{Alt}_{2m}(-s)0,\\
D^3w&=\operatorname{Alt}_{2m}(s)(-s),\\
D^4w&=\operatorname{Alt}_{2m-1}(-s)0s=\rho^2w.
\end{aligned}$$

Here juxtaposition is concatenation; the last two letters of D^3w agree.
These formulas include m=1 without an empty strict block.

Every earlier phase in the sharp trajectory is outside the core. For
x=0^r Alt_l(s), n=r+l, the following coordinates exhibit inequality:

- If r>=4, (D^4x)_(r−4)=s while (rho²x)_(r−4)=0.
- If r=3, D³x is fully alternating, so (D^4x)_0=−s whereas
  (rho²x)_0=0.
- If r=2, D²x is fully alternating. At coordinate n−2, D^4x has a
  nonzero sign, whereas (rho²x)_(n−2)=0. This holds for either parity of n.
- If r=1 and n is even, D⁴x is the negative fully alternating word,
  nonzero at n−2, while (rho²x)_(n−2)=0.

Thus a^(n−1)b, a≠b, first enters at n−1 for even n and at n−2 for odd
n>=3. This is a first-entry proof, not merely a trajectory reaching a
known recurrent endpoint. The separate longest-run argument supplies the
matching upper bound on every other word.
