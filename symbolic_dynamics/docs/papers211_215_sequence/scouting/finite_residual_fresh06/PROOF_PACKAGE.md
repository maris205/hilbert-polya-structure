# Negative proof package: the already-owned four-digit Kaprekar entrance

Author: /root/round211_fresh_residual_scout. Date: 2026-09-09 UTC.
This reconstructs ONE EXISTING SOURCE MAP, not a new literal nomination.
No scientific execution, code implementation, paper number or admission.

## Claim and status

The candidate-gate goal is NOT CURRENTLY JUSTIFIED: zero fresh two-axis
survivors remain. The elementary statements below are PROVABLE AS STATED.
The odd-base temporal conclusion uses the explicitly attributed source theorem
identified below; its sharp raw-state lift and the boundary counting are author
deductions. They carry no novelty or independent-review certification.

## Assumptions and notation

For an integer $b\ge2$, use all padded four-digit strings
$S_b=\{0,\ldots,b-1\}^4$, equivalently the integers $0,\ldots,b^4-1$.
Sort an input into $a_1\ge a_2\ge a_3\ge a_4$. The EXISTING Kaprekar update
$F_b$ returns the padded base-$b$ expansion of the descending integer minus
the ascending integer. Its value is nonnegative and below $b^4$, so this
is an autonomous self-map of the finite carrier. Leading zeros are retained.

Put
$$\delta(a)=(u,v)=(a_1-a_4,a_2-a_3),\qquad
Q_b=\{(u,v):0\le v\le u<b\}.$$
Define $e_b:Q_b\to S_b$ as the padded expansion of
$$D_b(u,v)=(b^3-1)u+(b^2-b)v.$$
Every pair is realized, for example by the sorted string $(u,v,0,0)$.
Write $K_b=\delta\circ e_b$; this is the source's difference-state update.
The zero pair is included here to handle constant strings explicitly.

## Strategy and dependencies

1. Subtraction and a congruence identify the exact output coding.
2. Classifying repeated digits counts every sorting fibre.
3. A quadratic inequality evaluates the unique odd-base fibre maximum.
4. The direct primary theorem for $K_b$ supplies its recurrent core.
   Injective output coding then proves the raw-state recurrent set and sharp
   clock. This is a source-theorem lift, not a new temporal mechanism.

## Proof

### 1. Exact coding; this is not a full-carrier conjugacy

Expanding descending minus ascending gives $F_b=e_b\circ\delta$.
If $D_b(u,v)=D_b(u',v')$, division by $b-1$ and reduction modulo $b$
give $u\equiv u'\pmod b$. Since both lie in $[0,b-1]$, they are equal;
the remaining equation gives $v=v'$. Thus $e_b$ is injective.

Consequently
$$F_b^t=e_b\circ K_b^{t-1}\circ\delta\quad(t\ge1),\qquad
F_b\circ e_b=e_b\circ K_b.$$
In particular, the first image has exactly $b(b+1)/2$ states.
The map $\delta$ is many-to-one: these identities are not a conjugacy
between all $b^4$ raw states and $Q_b$.

### 2. Complete one-step inverse and its elementary evaluation

A target outside $e_b(Q_b)$ has no source. For a target $e_b(u,v)$,
injectivity says its fibre is exactly $\delta^{-1}(u,v)$.

For $u=0$ there are the $b$ constant strings. For $u>0$, every sorted source
has one and only one description
$$(m+u,m+t+v,m+t,m),\qquad
0\le m\le b-1-u,\quad 0\le t\le u-v.$$
Different sorted tuples have disjoint sets of permutations. It follows that
$$
|\delta^{-1}(u,v)|=
\begin{cases}
b,&u=v=0,\\
(b-u)(12u-4),&u>0,\ v=0,\\
6(b-u),&u=v>0,\\
24(b-u)(u-v),&0<v<u.
\end{cases}
$$

To check every branch, when $v=0$ the two endpoints $t=0,u$ each have
three equal digits and hence four permutations; the other $u-1$ choices
each have exactly one equal pair and hence twelve. This gives
$8+12(u-1)=12u-4$ for each $m$, also valid at $u=1$.
When $v=u>0$, only $t=0$ is possible; two equal pairs give six permutations.
When $0<v<u$, the two distinct endpoints of the $t$ interval each give
twelve permutations, while the $u-v-1$ interior choices give twenty-four.
The sum is $24(u-v)$. This last count needs no exclusion of $u+v=b$.

The interior polynomial and its permutation proof are already present
under the stated type-(a) conditions in Devlin–Zeng, Lemma 2.
The displayed extension across the other equality cases is elementary
case completion, not a claimed new independent inverse engine.

### 3. Sharp one-step maximum for odd bases

Suppose now that $b\ge5$ is odd. In the interior branch, the largest value
at fixed $u$ occurs only at $v=1$. Completing the square gives
$$(b-u)(u-1)=\frac{(b-1)^2}{4}
-\left(u-\frac{b+1}{2}\right)^2.$$
The unique interior maximizer is therefore
$$(u,v)=\left(\frac{b+1}{2},1\right),$$
with fibre size $6(b-1)^2$.

For the zero-inner-gap branch,
$$(b-u)(12u-4)\le 3b^2-4<6(b-1)^2.$$
The last inequality is equivalent to $3(b-2)^2-2>0$, true for $b\ge5$.
The diagonal branch is at most $6(b-1)$, and the constant branch has size
$b$; both are strictly smaller. Empty fibres cannot maximize.
Thus the unique maximizing raw target is
$$e_b\left(\frac{b+1}{2},1\right).$$
This is optimization of the preceding old counting polynomial, not a
separate deep extremal mechanism. No all-time extremal theorem is asserted.

### 4. Source-owned core and the exact raw-state clock

For odd $b>3$, put
$$T_b=\{(u,v):b>u>v>0,\ u,v\text{ odd}\}.$$
The direct primary result of Chen–Ono–Schwartz–Thakur
(Theorem 1.1, proved by Lemma 2.1, Lemma 3.1 and Proposition 3.2)
states that $K_b^3(Q_b\setminus\{(0,0)\})\subseteq T_b$ and that $K_b$
on $T_b$ is conjugate, by
$$(u,v)\longmapsto
 \left\{\left[\frac{u+v}{2}\right],\left[\frac{u-v}{2}\right]\right\},$$
to doubling on unordered distinct nonzero residue classes modulo $b$,
where a class is identified with its negative. The relevant source proofs
were read; no formal prover was executed here.

Because $b$ is odd, doubling is invertible on these projective classes.
Thus every state in $T_b$ is recurrent. Conversely a recurrent nonzero
difference state must lie in $T_b$, since its third iterate does and a
finite cycle is invariant under taking third iterates. The only remaining
difference cycle is the zero pair. (The source theorem also keeps the
nonzero difference carrier invariant.)

The raw recurrent set is exactly
$$\{0000\}\ \cup\ e_b(T_b).$$
Indeed, the intertwining identity makes $e_b(T_b)$ recurrent.
A raw recurrent state lies in the first image, hence is $e_b(q)$.
Its periodicity and injectivity imply periodicity of $q$ under $K_b$.
This proves the reverse inclusion, including the zero case.

The raw map reaches this recurrent set in at most four steps: for
nonconstant $x$, use $F_b^4(x)=e_bK_b^3\delta(x)$; every constant string
maps to $0000$ in one step.

This four-step bound is sharp for EVERY odd $b\ge5$. Set
$$q_0=\left(\frac{b+1}{2},0\right).$$
The subtraction rule gives
$$
q_0\longmapsto
\left(\frac{b-1}{2},\frac{b-1}{2}\right)
\longmapsto (2,0)
\longmapsto (b-2,1)\in T_b.
$$
The first three displayed pairs are outside $T_b$. Choose the raw string
$x=((b+1)/2,0,0,0)$, which has difference pair $q_0$.
For $j=1,2,3$, its $j$th image is $e_b(K_b^{j-1}q_0)$, outside the
raw recurrent set by injectivity. The initial state is also nonrecurrent
because its difference pair is nonrecurrent. Its fourth image is recurrent.
Hence the maximum raw-state transient is exactly four.

This separates the difference-state three-step theorem from the padded
digit-state four-step consequence. They must not be labelled the same clock.

## Open risks and disposition

No new literal was proposed: this is the ordinary source-owned map with
its ordinary state coding, also explicitly excluded in the current older
arithmetic intake. The temporal engine is directly owned. The inverse
interior engine is directly owned; its boundary extension and maximum are
elementary. There is no admissible residual two-axis paper contract.

No new all-base cycle census, all-time inverse formula, general digit-length
classification, formal-verification acceptance or global novelty conclusion
is claimed. No pilot or numerical check supports these deductions.

