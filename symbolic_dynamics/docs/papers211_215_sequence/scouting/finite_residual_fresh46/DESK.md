# Fresh46 — coupled quadratic and requested frequency comparison

2026-09-11 UTC. Author `/root/current_round_independent_scout`.
**NO_CANDIDATE_HANDOFF / NO_PILOT / HOLD_EXTERNAL.**
One coupled-ring direction was fixed for subtraction. Root then supplied
one optional frequency-word lead, checked separately below. Neither has
an independently cleared temporal-plus-inverse residual. These are not two
admissions or two source-cleared new systems. Root contributed the initial
frequency inverse and cascade sketches; subsequent factor/clock deductions
below are this scout's author work, not independent review of root.

## 1. Coupled quadratic over powers of two

For k>=1, on $(\mathbb Z/2^k\mathbb Z)^2$, consider

$$F(x,y)=(x(1+y),y(1+x)).$$

This is finite, autonomous and noninjective: (0,0) and (-1,-1) have the
same zero image. The two coordinates genuinely couple before reduction.
However put $D(u,v)=(u(1+v),v(1-u))$ and $C(x,y)=(-y,x)$. Directly

$$D(C(x,y))=(-y(1+x),x(1+y))=C(F(x,y)).$$

C is invertible over every residue ring, so $F=C^{-1}DC$ with no division
or exceptional characteristic. The actual old DLV paragraph in
`docs/papers147_151_sequence/scouting/algebraic_replacement/SCOUT.md`,
lines305–330, was read (74934b). It specifies D over finite fields and
its invariant-sum quadratic foliation. A new modulus does not create a
new polynomial coupling; it changes the arithmetic of the old foliation.

More precisely, $d=x-y$ is invariant. In coordinates $(d,t)=(x-y,y)$,

$$F:(d,t)\longmapsto(d,t^2+(d+1)t).\tag{1}$$

This proves an exact disjoint-union reduction to scalar quadratics. It is
not a claim that the finite-field dynamics and the 2-power quotient dynamics
have the same functional graph.

### Evaluated inverse, but a classical scalar mechanism

For any target (X,Y), set d=X-Y and a=d+1 in the residue ring. Its
sources correspond bijectively to solutions of

$$t^2+at=Y;\qquad (x,y)=(t+d,t).$$

If d is even, a is odd. Every output of the scalar polynomial is even.
For an even target there is one root of each parity: at modulus2 both
parities solve the equation, and from modulus $2^j$ to $2^{j+1}$ the
two possible lifts differ in output by $2^j(2t+a)$, nonzero at that bit.
Thus exactly one lift survives in each parity at every level. The fibre
is therefore2 for even Y and0 for odd Y.

If d is odd, choose any h satisfying 2h=a. Translation t->t+h gives
the square congruence $u^2=w$, where $w=Y+h^2$. Its exact number of
solutions $R_k(w)$ is

$$R_k(0)=2^{\lfloor k/2\rfloor}.$$

For nonzero w, an odd valuation gives zero roots. If $v_2(w)=2s<k$,
write $m=k-2s$ and let z be the odd residue $w/2^{2s}$ modulo $2^m$.
Then

$$R_k(w)=2^s r_m(z),\qquad
r_m(z)=\begin{cases}
1&m=1,\\
2&m=2,\ z\equiv1\pmod4,\\
4&m\ge3,\ z\equiv1\pmod8,\\
0&\text{otherwise}.
\end{cases}\tag{2}$$

Indeed roots must have valuation s; writing u=2^s v leaves $2^s$
independent lifts of each odd unit root modulo $2^m$. For m>=3,
odd squares are1 modulo8. Conversely each such residue is a square:
inductively, adding $2^{m-1}$ to an odd root changes its square by
$2^m$ modulo $2^{m+1}$, so roots can be lifted to either next target
bit. The square homomorphism on odd units has kernel of size4, since
$(v-1)(v+1)=0$ modulo $2^m$ forces $v\equiv1$ or -1 modulo
$2^{m-1}$; hence each square has4 roots. The m=1,2 cases are direct.
The zero formula follows from $v_2(u)\ge\lceil k/2\rceil$.
These arguments prove (2), including k=1, without execution.

Consequently the maximum fibre of F is2 at k=1 and
$2^{\lceil k/2\rceil}$ at k>=2. For even k, zero in the square branch
attains it; for odd k>=3, take $v_2(w)=k-3$ with odd part1 modulo8.
Such square-branch targets exist by taking d=-1, so a=h=0.
The bound follows by maximizing the explicit cases in (2) together with
the even-d bound2. This is evaluated inverse arithmetic, not a new coupled
inverse mechanism.

### Direct temporal ownership and honest stopping point

Fan and Liao, *On minimal decomposition of p-adic polynomial dynamical
systems*, Advances in Mathematics228 (2011),2116–2144,
[primary HTML](https://arxiv.org/html/1010.5583), was directly read in
its introduction and Section6's classification setup, Theorem6.2 and the
statement opening of Theorem6.3. It explicitly studies arbitrary quadratic
maps on $\mathbb Z_2$, including $t^2+bt$ with odd b. Its introduction
also explains induced finite-quotient cycles and lifting. Thus the scalar
temporal family and lifting mechanism are direct prior work. No full-paper
proof audit or ready-made finite-k cycle table is claimed here; the source's
infinite-adic periodic-point theorem must not be mistaken for a bound of2
on all finite-quotient periods. No formula from its rendered general affine
normalization is needed for (1).

After (1) and this primary subtraction, no separate new global temporal
theorem has been identified. The square-root inverse does not repair that
deficit. Status: **reduction/inverse PROVABLE AS STATED; fresh two-axis
temporal contract NOT CURRENTLY JUSTIFIED**. No pilot or larger cutoff.

## 2. Root's own-value-frequency lead: exact EQC factor

Let n>=1, q>=n, and on $[q]^n$ let
$W(x)_i=|\{j:x_j=x_i\}|$. Write pi(x) for its equality partition.
For a labelled partition P, let L(P) assign each position its block size;
let E(P) merge all blocks of equal size. Then directly

$$W=L\pi,\qquad \pi L=E,\qquad
W^{t+1}=LE^t\pi.\tag{3}$$

The complete actual old EQC report
`docs/papers147_151_sequence/scouting/root/SCOUT.md` was read (c6fdee).
It defines precisely E, gives the logarithmic upper bound, powers-of-two
sharp cascades, distinct-size fixed partitions and divisor-injection fibres.
The complete `phase1/OWNER_AUDIT_EQC.md` was also read (28d1b6): its
status is KILL_UNRESOLVED_DIRECT_OWNER, not a source-cleared theorem claim.

Here is the exact word/partition clock relation, not an all-n sharpness
claim. If P=pi(x) has positive EQC depth tau, some blocks merge at its
last step. The resulting word at time tau labels such a merged block by
its former constituent size, strictly smaller than its new size. It is
not fixed. At time tau+1, (3) labels every final block by its own size,
and distinct final sizes make it fixed. Before tau its partition is not
fixed, so neither is the word. Thus $h_W(x)=\tau+1$ when tau>0.
If tau=0, depth is0 when x=L(P), and1 otherwise. There are no other
periodic words because their equality partitions coarsen and stabilize.
For n>=2, q>=n this gives $H_W(n,q)=H_E(n)+1$; n=1 has depth maximum0
at q=1 and1 at q>1. The as-yet-unevaluated all-n extremum H_E is not
replaced by a sharp floor-log assertion. In particular the power-of-two
witness is only a sharpness statement on that subsequence.

Root's proposed inverse formula is valid by the following independent
counting explanation. Targets using values outside [n] have zero fibre.
For other targets let n_k be the number of positions with value k.
Necessarily k divides n_k. Partition those positions into b_k=n_k/k
unlabelled source blocks of size k, then assign all B=sum b_k blocks
distinct source symbols. Conversely every such choice is a unique source.
Thus, with (q)_B the falling factorial,

$$|W^{-1}(y)|=(q)_B\prod_{k=1}^n
\frac{n_k!}{(k!)^{b_k}b_k!},\tag{4}$$

or zero if any divisibility fails. Empty groups contribute1. This is
static equal-block splitting plus symbol injection; (3) shows the temporal
part is old EQC with one final label update, not a new coupled engine.
No all-target inverse extremum or exact all-n H_E was proved here.

The old MPD gate was additionally read in full (afeddf), but its rule
discards part values and lists multiplicities; it is **not** E or W.
Its direct OEIS temporal owners must not be misassigned to this lead.
The Eliahou–Erickson2013 publisher search record again supplied only an
abstract about a related fixed-n partition system; the correct article
body returned403. A guessed wrong PII had previously failed, and an
OpenProblemGarden route also failed. No full-source resolution of the old
EQC concern occurred, and lack of access supplies no novelty clearance.

## Scope and handoff

Both ideas were desk-compared before any candidate gate or execution.
Project research/literature/proof skills enforced source subtraction and
the distinction between proved inverse formulas and uncleared temporal
claims. All deductions above are author work; root's frequency contributions
remain disclosed. Only this DESK.md was created. No science execution,
cutoff enlargement, helper import, environment audit, children, Git,
central/count edit, admission, external upload or contact. **Stop with no
candidate handoff and no pilot request.**
