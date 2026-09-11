# Proof package: three tail-distance desk rules

Author: `/root/round211_nonlinear_scout`. These are author deductions, not
independent reviews. All definitions are fixed in
[the intake](INTAKE_AND_DISPOSITION.md). No finite experiment is a dependency.

## Claim, assumptions, status and dependency map

**PROVABLE AS STATED:** closure; CEP0 idempotence and every-target inverse;
CEP1 image/core, complete rotation periods and every-target inverse; HDA's
pointwise tail-depth transform, exact entrance clock and fixed locus; HDA
fibres over every fixed target. Empty carriers and singleton components are
included with the conventions below.

**NOT CURRENTLY JUSTIFIED:** a new two-axis contribution after subtraction;
HDA's complete image or every-target inverse/extremal theorem; any priority,
admission or manuscript-acceptance statement.

Assumptions: finite labelled vertex set, simultaneous old-state evaluation,
and no quotient by graph isomorphism. Write $c(m)=1$ for $m=1$, and
$c(m)=m^{m-2}$ for $m\ge2$. This is the classical number of labelled trees on
a prescribed $m$-set with one prescribed root, oriented to that root. Rooting
at a prescribed label adds no factor. The usual Prüfer encoding removes the
least-labelled leaf and records its neighbour until two labels remain; its
reverse reconstructs a unique tree from every length-$m-2$ label word. This
gives $c(m)$ for $m\ge2$, including the empty code at $m=2$.

The dependency map is:

1. Finite functional-graph decomposition gives the cycle set, tail depth and
   unique first cycle entry.
2. CEP0 and CEP1 are decoded by that cycle set and disjoint entry basins.
3. HDA keeps every cycle arrow and sends a noncycle vertex to a proper old
   ancestor; its new depth is determined solely by its old depth.
4. HDA's fixed-target inverse is exactly a product of height-at-most-two
   rooted-tree counts; it does not prove the missing arbitrary-target claim.

Empty products are one, $0!=1$, and $0^0=1$ when used in finite sums.

## 1. CEP0: a projection with the complete classical inverse

For every $x$, $P_0(f)(x)=r_f(x)\in C_f$. If $x\in C_f$, then $d_f(x)=0$
and $P_0(f)(x)=x$. Consequently $P_0(f)$ is idempotent as a vertex map.
Conversely, if $g^2=g$, then every nonroot maps to a fixed point in one step,
so $P_0(g)=g$. The image and recurrent carrier of $P_0$ are therefore exactly
the idempotent endofunctions, and $P_0^2=P_0$ as operators.

For an idempotent target $g$, let $R=\operatorname{Fix}(g)$ and
$B_r=g^{-1}(r)$ for $r\in R$. Then

$$|P_0^{-1}(g)|=|R|!\prod_{r\in R}c(|B_r|).\tag{1}$$

For a nonidempotent target the fibre is zero. At $n=0$, (1) is one.

Proof of (1). In any predecessor $f$, the fixed vertices of $P_0(f)$ are
exactly $C_f$, since a noncycle vertex cannot equal its first cycle entry.
Hence $C_f=R$, and the restriction of $f$ to $R$ is an arbitrary permutation
$\sigma$. If $x\in B_r\setminus\{r\}$, the forward path from $x$ until its
first cyclic vertex must end at $r$ and must stay inside $B_r$: moving first
to another basin would change that first entry. The noncycle edges in $B_r$
therefore form a tree oriented to $r$, with no additional cycle. Conversely,
choose any permutation $\sigma$ on $R$ and independently choose such a tree
on each prescribed $B_r$. Set the root arrow to $\sigma(r)$ and retain the
oriented tree edges elsewhere. The resulting first entries are exactly $g$.
Each input recovers its permutation and its basin trees uniquely, giving the
bijection and formula. This entire decoder is classical static data.

The global maximum entrance time is zero at $n=0,1$ and one for $n\ge2$:
all images are fixed, and a transposition with every unused vertex fixed is
not itself idempotent. This is projection time, not an independent axis.

## 2. CEP1: height-one normalization and ordinary cycle rotation

Let $\mathcal Y_n$ be the set of functions whose noncycle vertices have depth
one, together with all permutations and the empty map. For every $f$, CEP1
keeps the restriction on $C_f$ and sends every noncycle vertex directly to
the cyclic successor of its first entry. Thus $P_1(f)\in\mathcal Y_n$ and
its cyclic vertex set is exactly $C_f$.

For $g\in\mathcal Y_n$, write $\sigma=g|_{C_g}$. CEP1 preserves all cycle
arrows; for every noncycle $x$, it replaces $g(x)$ by $\sigma(g(x))$.
This is a bijection on $\mathcal Y_n$, with inverse attachment motion by
$\sigma^{-1}$. It follows that image and recurrent carrier are exactly
$\mathcal Y_n$. The period of a labelled recurrent state is

$$\operatorname{per}_{P_1}(g)=
\operatorname{lcm}\{|C|:C\text{ is a vertex cycle carrying a noncycle vertex}\},
\tag{2}$$

with empty least common multiple one. To see exactness, choose a labelled
attached vertex on any participating cycle. Its head successively visits
all distinct labels of that cycle, so it returns precisely at multiples of
the cycle length. Independent components synchronize by the displayed LCM.
There is no identification of labelled attachment configurations by symmetry.

The entrance time is exactly zero for $H(f)\le1$ and one for $H(f)>1$.
The global maximum is therefore zero for $n\le2$ and one for $n\ge3$;
a loop-rooted chain on three labels witnesses the latter case.

For a target $g\in\mathcal Y_n$, define

$$B_r=\{r\}\cup\{x\notin C_g:g(x)=\sigma(r)\}\quad(r\in C_g).
\tag{3}$$

Then

$$|P_1^{-1}(g)|=\prod_{r\in C_g}c(|B_r|).\tag{4}$$

Targets outside $\mathcal Y_n$ have zero fibre. Proof: in any predecessor,
the cycle set and its arrows are exactly those of $g$, since CEP1 keeps cycle
arrows and creates no cyclic noncycle vertex. For a noncycle $x$, the equation
$g(x)=\sigma(r_f(x))$ forces the unique root entry
$r_f(x)=\sigma^{-1}(g(x))$. Thus its basin is exactly (3). Its internal tree
can be chosen arbitrarily, and the converse reconstruction is the same
disjoint-basin construction as in (1), now with the root permutation fixed.
There is no further source coupling to count. This proves (4).

Thus both its temporal and inverse mechanisms are standard normalization,
rotation and labelled-tree enumeration. A different literal from P209 does
not make rotation/LCM a new mechanism.

## 3. HDA: exact depth dynamics and the complete entrance clock

Set

$$a(d)=\left\lceil\frac{d+1}{2}\right\rceil,\qquad
q(d)=d-a(d)=\left\lfloor\frac{d-1}{2}\right\rfloor\quad(d\ge1),$$
$$\phi(d)=\lfloor\log_2(d+1)\rfloor\quad(d\ge0).$$

HDA retains the original cycles and every label. Off a cycle it replaces the
arrow by the old ancestor at depth $q(d)$, which is a nonnegative integer
strictly smaller than $d$. This proves closure and proves that no old
noncycle vertex becomes cyclic. It also proves that the first cycle entry
of every vertex is unchanged, since every jump stops at or before that entry.

For each vertex $x$ of old depth $d$, following its new arrows successively
changes old depth by $d\mapsto q(d)$ until zero. Let $L(0)=0$ and
$L(d)=1+L(q(d))$ for $d\ge1$. Since

$$q(d)+1=\left\lfloor\frac{d+1}{2}\right\rfloor,$$

induction gives $L(d)=\lfloor\log_2(d+1)\rfloor$: for $d\ge1$ the integer
$d+1$ is at least two, and dividing it by two with floor removes exactly one
from its binary logarithm floor. Hence the exact pointwise law is

$$d_{A(f)}(x)=\phi(d_f(x)).\tag{5}$$

This is not a numerical pattern. Every original path to a cycle supplies
the required ancestors at all intermediate depths. Reapplying (5) proves

$$d_{A^t(f)}(x)=\phi^{\circ t}(d_f(x)),\qquad
H(A^t(f))=\phi^{\circ t}(H(f)),\tag{6}$$

because $\phi$ is nondecreasing. For $d\ge2$, $\phi(d)<d$. At depths zero
and one the literal update changes no arrow. Conversely, a vertex of depth
$d\ge2$ is moved at least two old edges and reaches a different old ancestor
from its parent, so such a state is not fixed. Thus

$$\operatorname{Fix}(A)=\operatorname{Rec}(A)=\mathcal Y_n,$$
$$\tau_A(f)=\min\{t\ge0:\phi^{\circ t}(H(f))\le1\}.\tag{7}$$

Every nonfixed state reaches the fixed locus by strict height decrease,
which excludes nontrivial recurrent cycles. Equations (5)--(7) are a scalar
height factor with the exact terminal-level test, not a bijective coding of
whole functions. HDA's terminal state preserves the original cyclic arrows
and attaches every noncycle vertex to its original first cycle entry.

For an exact threshold form, set $b_0=1$ and

$$b_{t+1}=2^{b_t+1}-2.$$

For every integer $d\ge0$, $\phi(d)\le b_t$ iff $d\le b_{t+1}$. Induction
therefore gives $\tau_A(f)\le t$ iff $H(f)\le b_t$. The first thresholds
are $1,2,6,126$, followed by $2^{127}-2$. At $n\ge1$, the largest attainable
height is $n-1$, attained by a loop-rooted chain on all labels; consequently

$$\max_{f\in\mathcal X_n}\tau_A(f)=\min\{t:n-1\le b_t\}.\tag{8}$$

The empty carrier has maximum zero. The height-factor proof explains the
whole clock, but does not itself create the required independent inverse
mechanism. No sharper complexity claim follows from (8).

## 4. HDA fixed-target fibres: precisely the old height-two count

For $m\ge0$, let

$$M_m=\sum_{k=0}^{m}\binom{m}{k}k^{m-k}.\tag{9}$$

This counts labelled trees of height at most two on a prescribed root plus
$m$ other labels: choose the $k$ root children, and let every remaining
label choose its parent among those $k$. These are exactly the idempotent
functions on the $m$ nonroot labels under the bijection which makes each
root child a fixed point and leaves the depth-two parent pointers unchanged.
In particular $M_0=1$ with the stated convention.

For $g\in\mathcal Y_n$ and $r\in C_g$, let
$D_r=\{x\notin C_g:g(x)=r\}$ and $m_r=|D_r|$. Then

$$|A^{-1}(g)|=\prod_{r\in C_g}M_{m_r}.\tag{10}$$

Proof: HDA preserves every cycle arrow and first entry. Equation (5) says
the output has height at most one iff the input has height at most two.
For these inputs the output of a noncycle vertex is exactly its first entry,
so its input entry basin is $\{r\}\cup D_r$. Conversely any independent
height-at-most-two tree on these basins, with the fixed cyclic arrows of
$g$, maps to $g$. The choices recover uniquely, proving (10).

Formula (9) and this height-two tree interpretation occur explicitly in old
LLG's proof, Section 3, equations (6)--(9). A product over prescribed cycle
basins is not a new constrained inverse mechanism. The LLG all-target
compression injection is **not** transported: HDA has different lost edges.

## 5. Missing claim and an explicit failed compression attempt

For a general HDA target $g$, (5) forces every possible source depth $e(x)$
into the interval

$$2^{d_g(x)}-1\le e(x)\le 2^{d_g(x)+1}-2,$$

but this condition does not reconstruct parent arrows. Adding the equations
that a source path reach $g(x)$ after $a(e(x))$ edges merely restates the
predecessor constraints. It is not an evaluated inverse or support theorem.

One attempted transfer of the old height-two compression also fails. Let the
root be $0$, and use labels $1,2,3,4$. Let both trees have arrows
$1\to0$, $2\to1$, $3\to1$, and let $4\to2$ in the first tree and $4\to3$
in the second. Their HDA target is the same:

$$g=(0,0,0,0,1).$$

Both trees have depths $(0,1,2,2,3)$. Compressing every odd-depth nonroot
vertex to the root while retaining each even-depth parent produces the same
height-two tree in both cases, with parent vector $(0,0,1,1,0)$. Thus this
compression is not injective within the fixed target fibre: it loses the
choice of the depth-two parent of vertex $4$. This is a hand-checked symbolic
witness, not an executed pilot. It does not disprove every possible injection
or a maximal-fibre conjecture; it shows why that particular transfer cannot
be claimed.

The missing result is a genuinely constrained, evaluated inverse/image or
extremal theorem outside $\mathcal Y_n$, with an independent residual after
old mechanisms are deducted. No such result was obtained here. No general
maximal-fibre value is asserted. HDA therefore closes NO_PROMOTION, without
rescuing its missing axis by a larger experiment or by restricting its carrier
to the already-counted stable-target sector.
