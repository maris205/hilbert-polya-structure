# Fresh43 — valuation extension of ambient totient-gcd

2026-09-11 UTC. Author `/root/current_round_independent_scout`.
**ONE_EXTENSION_LITERAL / NO_PILOT_REQUEST / RESIDUAL_NOT_CLEARED.**
This is a substantive author desk, not independent acceptance or admission.

## Literal, claims and status

For a fixed positive integer N, on its finite divisor set define

$$T_N(d)=\gcd(N,\varphi(d)).$$

The squarefree restriction is exactly old A01, not a new candidate here.
This desk considers arbitrary prime-power exponents and explicitly retains
that old restriction in the subtraction. No graph-mex, recency-rank,
priority scheduler, or quotient/rotation construction is used.

**PROVABLE AS STATED:** the unique recurrent divisor is one; the maximum
entrance time is the largest sum of ambient prime exponents along a prime
chain within N. For two primes joined by a Pratt edge, the pointwise clock,
all target fibres and all fibre maximizers are given below.
**NOT CURRENTLY JUSTIFIED:** a materially new two-axis contribution after
the old Pratt-DAG and elementary capped-counter mechanisms are deducted.
No broad inverse theorem for arbitrary N is claimed.

## Notation, strategy and dependencies

Write $N=\prod_{p\in P}p^{a_p}$, $a_p\ge1$, and $d=\prod p^{e_p}$,
$0\le e_p\le a_p$. Set $c_{pq}=v_p(q-1)$ for distinct primes in P.
Draw an edge $q\to p$ exactly when $c_{pq}>0$; then $q>p$, so the graph
is acyclic. Depth is least time to reach a periodic state.

The proof uses (1) the elementary prime-power totient formula and CRT,
(2) monotonicity of the resulting exponent map and its maximal state,
(3) direct solution of a two-counter recurrence, and (4) disjoint scalar
inverse branches. There is no finite experiment among these dependencies.

## Proof

### 1. Exponent dynamics and exact global extinction

Counting units gives $\varphi(p^e)=p^{e-1}(p-1)$ for $e>0$;
$\varphi(1)=1$. CRT multiplies these factors over active primes. Hence

$$e'_p=\min\left(a_p,(e_p-1)^+
       +\sum_{q>p}c_{pq}\mathbf1_{e_q>0}\right).\tag{1}$$

This proves closure and coordinatewise monotonicity. If N>1, both one
and the smallest prime dividing N map to one, proving noninjectivity.
For N=1 the singleton map is fixed.

Define, in descending prime order,

$$h_p=a_p+\max_{q\to p}h_q,\qquad \max\varnothing=0.\tag{2}$$

Start (1) from the maximal exponent vector $e_p=a_p$. Inductively every
strictly larger prime q is positive exactly at times $0,\ldots,h_q-1$.
Let $M=\max_{q\to p}h_q$. If M>0, an incoming prime attaining M stays
positive throughout those M times, so p receives at least one unit each
step before M. Starting at its cap, p therefore stays exactly at its cap
through time M. At and after time M all incoming primes are zero; p then
decreases by one each step, becoming zero exactly at $M+a_p=h_p$.
If M=0 it simply decreases from its cap from the beginning. This proves
the induction, including primes with no incoming edges.

Every other initial vector is bounded above by this maximal trajectory,
so all states reach zero by $H=\max_p h_p$. The maximal trajectory
attains H, proving sharpness. Equation (2) evaluates H as the maximum
sum of $a_p$ over a directed path, with a singleton vertex allowed.
Set H=0 when P is empty. Zero exponents represent divisor one; since
every orbit reaches it, it is the only recurrent divisor.

### 2. Complete pointwise clock for two primes

Assume $N=p^a q^b$, $p<q$, $a,b\ge1$, and $c=v_p(q-1)\ge1$.
For state $(i,j)$, equation (1) becomes

$$j'=(j-1)^+,\qquad
i'=\min(a,(i-1)^++c\mathbf1_{j>0}).\tag{3}$$

If j=0, the exact depth is i. If j>0, there are exactly j steps with
positive upper counter. During them the lower counter, after its first
update, is positive. Its value at the end of these steps is

$$I=\min(a,\max(i,1)+j(c-1)).$$

For i>=1 this follows by adding c-1 and capping at each step. For i=0,
the first value is min(a,c), and the remaining j-1 additions give the
same displayed expression. The upper counter is then zero and the lower
one drains in I more steps. Thus the exact pointwise formula is

$$h(i,0)=i,\qquad
h(i,j)=j+\min(a,\max(i,1)+j(c-1))\quad(j>0).\tag{4}$$

In particular the sharp maximum is a+b, attained at (a,b), consistently
with (2). This is a complete two-prime clock, not just an upper bound.

### 3. Every two-prime target fibre, including saturation

For $0\le u\le a$, define

$$\alpha(u)=\begin{cases}2&u=0,\\1&1\le u<a,\\0&u=a.\end{cases}$$

This counts sources i with $(i-1)^+=u$. For the active-upper branch,
the count of sources with $\min(a,(i-1)^++c)=u$ is

$$\beta(u)=
\begin{cases}
2&c<a,\ u=c,\\
1&c<a,\ c<u<a,\\
c&c<a,\ u=a,\\
a+1&c\ge a,\ u=a,\\
0&\text{otherwise}.
\end{cases}$$

For example, in the saturation case c<a one needs $i\ge a-c+1$,
giving exactly c choices, not c+1. If c>=a, even i=0 saturates and
all a+1 sources qualify. These conditions prove the beta formula.

For every target $(u,v)$ in the full divisor carrier, equation (3) gives

$$|T_N^{-1}(p^u q^v)|=
\begin{cases}
\alpha(u)+\beta(u)&v=0,\\
\beta(u)&1\le v<b,\\
0&v=b.
\end{cases}\tag{5}$$

Indeed v=0 allows exactly the two disjoint upper sources j=0 and j=1;
positive v<b forces j=v+1; v=b has none. This proves necessity,
sufficiency and completeness, without an uneliminated source search.

All maxima follow explicitly. If c<a, target (c,0) has fibre3, each
(a,v) with 0<=v<b has fibre c, and every other target has at most2.
Thus the maximum is max(3,c): only (c,0) maximizes for c<3; both those
sets maximize for c=3; only the saturation targets maximize for c>3.
If c>=a, the maximum is a+1, attained at every (a,v), 0<=v<b;
the additional target (0,0) also maximizes exactly when a=1.
All these statements allow b=1, when the middle line of (5) is empty.

## Source and mechanism subtraction

The original `docs/papers132_136_sequence/scouting/algebraic/SCOUT.md`
lines52–100 were directly read (1af896). A01 is exactly this totient-gcd
formula on squarefree divisors and already identifies its Pratt-edge
image clock. A02 includes an extra N/d factor and is not our map; A04's
sigma replacement is a different support relation. Their recorded pilot
outputs were not rerun or used as proof premises.

Ford, Konyagin and Luca, *Prime chains and Pratt trees*, Geom. Funct.
Anal.20 (2010),1231–1258,
[primary HTML](https://arxiv.org/html/0904.0473), was read through its
opening definition and introduction, including the paragraph comparing
ordinary totient iteration. It owns prime chains and the iterated-totient
neighbourhood. Its ordinary, uncapped phi iteration is not (1); no cited
analytic theorem is used to prove (2). Version metadata says2010; the
HTML's isolated regenerated2026 date was not treated as publication date.

Pollack, *Two remarks on iterates of Euler's totient function*,
[author PDF](https://www.pollack-math.net/iterates.pdf), was read in the
opening through the Pratt-tree discussion. It concerns ordinary totient
iterates and their arithmetic statistics, not the target fibres (5).
The old UGA PDF address redirected to a home page; that redirect was not
claimed as a PDF read. The author's current PDF address then succeeded.

The exponent lift is not falsely called the same Boolean relation-image
map: capacities and active-prime multiplicities really change it. However,
its global clock is a weighted version of the already-used prime-chain
countdown, via an elementary feedforward counter argument. The complete
two-prime inverse is just two decrement/saturation branches. No separately
cleared, materially new mechanism remains in this bounded desk. This is
an author value judgment with explicit proofs, not a global novelty verdict
or a proved full-carrier conjugacy to an unspecified older counter system.

The narrow valuation/weighted-chain query 6ab4f9 had no matches under its
selected scouting paths and exclusions; the broader20f6f6 output was
truncated. Neither establishes archive exhaustion. A new broad inverse
theorem on interacting prime chains was not proved and is not replaced by
a formal support-sum decoder or larger numerical cutoff.

## Handoff boundary

The project research skill imposed direct-original subtraction and early
rejection; literature/proof skills supplied primary-read limits and complete
proof boundaries. One nonsquarefree extension was defined, zero pilots or
scientific executions occurred, and only this DESK.md was created. No helper
imports, environment/dependency audit, children, Git, central edit, numbering,
admission, upload or contact. **No pilot request; stop this bounded desk.**
