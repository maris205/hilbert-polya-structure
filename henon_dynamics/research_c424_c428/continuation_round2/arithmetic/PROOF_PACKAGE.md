# Two-pole compatibility for every Laurent-parameter quadratic Hénon map

AI-generated author-side proof, 2026-09-08 UTC. This is the single frozen
AR2-1 question, not an admitted contract or a manuscript. The result below
is an exhaustive **parameterwise finite atlas**, with exact reconstruction
and edge guards. It does not purport to list all possible symbolic cycle
words or all irreducible parameter strata of the exceptional graphs.
Whether that remaining presentation/structure distinction leaves enough
independent substance for a paper is explicitly reserved for review.

## Frozen object and scope

Let `k` be any field of characteristic different from two, `t` transcendental
over `k`, `a in k*`, and `c in k[t,t^-1] \ k`. One ordinary tick is

\[
H_{a,c}(x,y)=(y,y^2+c-a x)
\]

on **all** of `k(t)^2`. We classify ordinary rational periodic points,
their exact least periods and all coexistence for each parameter. No sign
quotient, field extension, local completion or finite search cutoff replaces
this domain. All conclusions include positive characteristic other than two.

The one-pole subfamilies are C418, or C418 after `t -> 1/t`, and are deducted
in their entirety. The new work below concerns genuine poles at both zero
and infinity. The determinant is constant; rational-function determinants,
more than two parameter poles, constant parameters, and characteristic two
are outside this contract.

## Theorem: the full parameterwise atlas

Write the pole orders of `c` at infinity and zero as `M,N > 0`.

1. If either order is odd, or either of `-c_M,-c_-N` is not a square in
   `k*`, the periodic set is empty. Otherwise put `M=2m,N=2n`, choose the
   two leading square roots in `k`, and construct the unique polynomials

   \[
   U\in t k[t],\quad \deg U=m,\qquad
   V\in t^{-1}k[t^{-1}],\quad \operatorname{ord}_0(V)=-n
   \tag{1}
   \]

   such that `U^2+c` has no term of exponent greater than `m`, and
   `V^2+c` has no term of exponent less than `-n`. Their chosen leading
   coefficients determine them; changing a root changes only the sign
   of the corresponding polynomial. Every periodic coordinate has the
   unique form

   \[
   y_i=e_iU+d_iV+b_i,
   \qquad e_i,d_i\in\{1,-1\},\ b_i\in k.                 \tag{2}
   \]

2. If `UV` is nonconstant, all periodic coordinates, even in different
   coexisting cycles, have the same sign product `e_i d_i = kappa`.
   For each of the two choices `kappa = +/-1`, put `P_0=U+kappa V`
   and test the Laurent identity

   \[
   c+P_0^2=L P_0+D,\qquad L,D\in k.                       \tag{3}
   \]

   At most one choice can pass. If neither passes there are no periodic
   points. For a passing choice put `P=P_0-L/2` and `C_*=D+L^2/4`.
   The **entire** periodic set is precisely the inherited seven-row atlas
   below with this `P,C_*`. Thus this part is a Laurent base-change
   corollary of C418 after the global sign-compatibility argument.

3. If `UV` is constant, necessarily

   \[
   m=n,\quad U=u t^m,\quad V=v t^{-m},\quad r=uv\in k^*.
   \tag{4}
   \]

   There are no periodic points unless the following five-term identity
   holds for unique `alpha,beta,C in k`:

   \[
   c=-U^2-V^2+\alpha U+\beta V+C.                          \tag{5}
   \]

   When it holds, form the **64 labelled states and two edge guards**
   in the next section. The directed cycles of this explicitly defined
   graph give every periodic point, with no other points. Graph-cycle
   length is the ordinary least period. Distinct graph cycles have
   disjoint point labels, and all graph cycles are included simultaneously.

4. A cycle whose product `e_i d_i` is nonconstant can occur only if

   \[
   a\in\{1,-1,2,-2,1/2,-1/2\}.                           \tag{6}
   \]

   In addition, both `(alpha-beta)/2` and `(alpha+beta)/2` belong to

   \[
   S_a=\{\eta+a\theta:\eta,\theta\in\{-1,0,1\}\}.        \tag{7}
   \]

   These are necessary restrictions, **not** a claim that all six values
   or all 81 coefficient pairs admit a mixed cycle. The graph's exact
   guards are the necessary-and-sufficient test, including every small
   characteristic collision. No division by three or a prime census is
   used.

In every case there are at most 64 ordinary rational periodic points and
every least period is at most 64. This is a proved upper bound, not a claim
of sharpness. The single-pole and unmixed branches have the sharper
inherited bounds. Membership in the atlas uses only two square tests in
`k`, finite Laurent coefficient comparisons, and at most 64 explicitly
labelled states; there is no unresolved Diophantine equation or unknown
period cutoff in its parameterwise use.

### The explicit 64-state atlas for (5)

A state is

\[
 s=(e_{-1},e_0,e_1,e_2;d_0,d_1)\in\{1,-1\}^6.
\]

Define

\[
B_0=\frac{e_1+a e_{-1}-\alpha}{2e_0},\qquad
B_1=\frac{e_2+a e_0-\alpha}{2e_1},                       \tag{8}
\]

and label the state by the actual rational point

\[
E(s)=(e_0U+d_0V+B_0,\ e_1U+d_1V+B_1).                    \tag{9}
\]

Compute the three constants

\[
D_2=2d_1B_1+\beta-a d_0,\qquad
B_2=B_1^2+2e_1d_1r+C-a B_0,\qquad
E_3=2e_2B_2+\alpha-a e_1.                                \tag{10}
\]

There is an outgoing edge exactly when

\[
\boxed{D_2^2=1,\qquad E_3^2=1.}                         \tag{11}
\]

Its unique target is

\[
(e_0,e_1,e_2,E_3;d_1,D_2).                               \tag{12}
\]

Equations (8)--(12) are an explicit constant-size parameter atlas, not
the assertion that four local signs somehow determine the global orbits.
They provide all 64 actual point labels and every edge, in field arithmetic,
for each of the full five constant parameters `(a,alpha,beta,r,C)`, `ar!=0`.
The graph has indegree and outdegree at most one. Delete its noncyclic
vertices; each remaining component is one ordinary rational cycle, labelled
by (9), whose length is its exact least period. This is a finite exact
decision/reconstruction rule for **every** input field and parameter in (5).

If `A` is its 64 by 64 zero-one adjacency matrix, then for every `n>=1`,

\[
\#\operatorname{Fix}(H^n)(k(t))=\operatorname{tr}(A^n),\qquad
\zeta_{H,k(t)}(z)=\det(I-zA)^{-1}.                        \tag{13}
\]

No matrix experiment is needed for (13); noncyclic components have no
closed walks, and cyclic components are ordinary permutation cycles.

### Deducted pure-sign rows, including all overlaps

The following table belongs to C418. It holds whenever `c=-P^2+C_*`
and all coordinates under consideration have the form `+/-P + constant`.
Put `K_a=(a+1)^2/4`. A transition bit word `w` determines signs by
`sigma_(i+1)=sigma_i (-1)^w_i`, with initial sign `+1` or `-1`, and

\[
y_i=\sigma_i P+
\frac{(-1)^{w_i}+a(-1)^{w_{i-1}}}{2}.                     \tag{14}
\]

| Word | Condition | `C_*` | Ordinary cycles | Least period |
|---|---|---:|---:|---:|
| 0 | any `a!=0` | `K_a` | 2 | 1 |
| 1 | any `a!=0` | `-3K_a` | 1 | 2 |
| 01 | `a^2=1` | `K_a-1` | 1 | 4 |
| 001 | `a^2=-1` | `K_a` | 1 | 6 |
| 011 | `a=1` | `-1` | 2 | 3 |
| 00011 | `char k=3,a=-1` | `-1` | 2 | 5 |
| 0111 | `char k=3,a=-1` | `1` | 1 | 8 |

In the monomial-pair case (5), the pure-sign cycles with product `kappa`
exist precisely among these rows if `beta=kappa alpha`, with

\[
P_\kappa=U+\kappa V-\alpha/2,\qquad
C_\kappa=C+2\kappa r+\alpha^2/4.                         \tag{15}
\]

Add every applicable row, for each admissible `kappa`. Opposite products
give disjoint point sets. Pure and mixed cycles are likewise disjoint.
If `a` is outside (6), this inherited-row rule already gives the entire
periodic set. If `a` is in (6), use the graph as well, retaining only its
mixed cycles when adding to the pure rows; equivalently use the graph
alone, which already contains both kinds and never double-counts.

## Proof

### 1. Pole orders and the two principal parts

Write a periodic orbit as `(y_i,y_(i+1))`, so

\[
y_i^2+c=y_{i+1}+a y_{i-1}.                               \tag{16}
\]

At an irreducible polynomial prime other than `t`, if a coordinate has
a pole, choose its maximal order `h>0` around that finite orbit. Since
`c` is integral and `a` a unit there, the left side at a maximal coordinate
has pole order `2h`, while the right side has order at most `h`. This is
impossible. Therefore every coordinate belongs to `k[t,t^-1]`.

At infinity let `h` be the maximum pole order among the coordinates.
It is positive: if all coordinates were regular, (16) could not balance
the pole of `c`. At a coordinate of order `h`, comparing (16) forces
`M=2h`, with cancellation of the leading terms. A coordinate of smaller
order could not cancel that pole of `c`; hence every coordinate has order
`m=M/2`. The identical argument at zero gives the common order `n=N/2`.
This also proves the two leading-square obstructions. The orders depend
only on `c`, so these statements hold over all coexisting orbits, without
presupposing that the full periodic set is finite.

For each orbit, (16) implies that `y_i^2+c` has exponent at most `m`
and at least `-n`. Fix the leading coefficient of the positive principal
part of `y_i`. Descending from exponent `2m` to `m+1`, the coefficients
of its square uniquely determine the coefficients of `t^m,...,t`;
at each step the divisor is twice its nonzero leading coefficient.
Negative powers and the constant term cannot affect these equations.
This constructs `U`, and constructs `V` independently after `t -> 1/t`.
The only choices are their leading signs. It follows that every coordinate
has (2). The three functions `U,V,1` are linearly independent over `k`,
by their largest positive and smallest negative exponents. Consequently
the representation in (2) is unique.

### 2. Global sign mixing forces a Laurent unit

Take any two periodic coordinates, even from different orbits, of the
form `y=eU+dV+b` and `z=fU+gV+h`. Subtract their instances of (16).
The neighbors are in the span of `U,V,1`, so

\[
y^2-z^2\in\operatorname{span}_k\{U,V,1\}.
\]

Expanding their squares gives

\[
2(ed-fg)UV+2(eb-fh)U+2(db-gh)V+(b^2-h^2)
  \in\operatorname{span}_k\{U,V,1\}.                     \tag{17}
\]

If `ed!=fg`, the coefficient `2(ed-fg)` is `+4` or `-4`, hence nonzero.
Then `UV` lies in that span. But `UV` has largest exponent at most `m-1`
and smallest exponent at least `-n+1`. In an expression `UV=l U+j V+q`,
the coefficient of `t^m` forces `l=0`, and that of `t^-n` forces `j=0`.
Thus `UV=q in k*`.

This proves that nonconstant `UV` forbids even cross-orbit mixing. If
`UV` is constant, its two factors are Laurent units and (4) follows.
For an elementary verification, write the exponent intervals of `U,V`
as `[j,m]` and `[-n,-l]`, with `j,l>=1`. Their product has extreme
exponents `j-n` and `m-l`, which must both be zero. Combining `j<=m`
and `l<=n` gives `m=n=j=l`, so both factors are single monomials.

### 3. Exhaustion of the nonconstant-product branch

When `UV` is nonconstant and a periodic point exists, all coordinates
have common product `kappa`. Thus they are `e_i P_0+b_i`, where
`P_0=U+kappa V`. Substitute one coordinate into (16). Its neighbors
are linear combinations of `P_0,1`, so `c=-P_0^2+L P_0+D` for constants
`L,D`. Completion of the square gives (3) and its `P,C_*`.

Both choices of `kappa` cannot pass (3): subtract their identities to
express `4UV` as a linear combination of `U,V,1`, which the preceding
extreme-exponent argument would force to be constant. For a fixed
`kappa`, the constants `L,D` are unique because `P_0` is nonconstant.

After the completion, coefficient comparison in the independent functions
`P,1` gives exactly

\[
2\sigma_i b_i=\sigma_{i+1}+a\sigma_{i-1},\qquad
b_i^2+C_*=b_{i+1}+a b_{i-1}.                             \tag{18}
\]

C418's eight-state transition proof uses just (18), not any further
polynomial integrality. Its seven rows therefore apply verbatim to this
Laurent `P`. The full proof in C418 has been read; all seven rows and their
small-characteristic overlaps are deducted rather than claimed anew.
Conversely every reconstructed row satisfies (18) and therefore (16),
so no sufficiency or rationality condition is missing.

### 4. The monomial-pair reduction and exact graph

If `UV=r` is constant, substitute any (2) into (16). The square has
nonconstant terms `U^2+V^2+2 e_i b_i U+2 d_i b_i V`; the cross term
`2 e_i d_i r` is constant. Its neighbors are in the span of `U,V,1`.
This forces (5). Conversely, once (5) is given, comparing its three
independent coefficients reduces (16) exactly to

\[
\begin{aligned}
2e_i b_i+\alpha&=e_{i+1}+a e_{i-1},\\
2d_i b_i+\beta&=d_{i+1}+a d_{i-1},\\
b_i^2+2e_i d_i r+C&=b_{i+1}+a b_{i-1}.                  \tag{19}
\end{aligned}
\]

The first equations at indices zero and one give (8), so every actual
periodic point is labelled by a state (9).

All 64 labels are distinct. From each point, independence of `U,V,1`
recovers `e_0,d_0,e_1,d_1,B_0,B_1`. The first equation of (8) then
recovers `e_-1`, using `a!=0`, and the second recovers `e_2`. There are
no collisions in characteristic three or any other allowed characteristic.

Direct expansion of `H(E(s))` gives first coordinate
`e_1 U+d_1 V+B_1` and second coordinate `e_2 U+D_2 V+B_2`, with (10).
If (11) holds, these are exactly the label (9) for (12), since its two
offsets are `B_1,B_2`. Conversely, if `H(E(s))` is any label, comparing
the coefficients of `U,V,1` first recovers the target's `e_0,e_1,d_0,d_1`
and offsets, then its `e_-1,e_2`; it is necessarily (12). Thus (11)
is an if-and-only-if edge criterion, not a necessary test that might
admit spurious orbits.

The graph has outdegree at most one by construction. Its indegree is at
most one because labels are injective and `H` is invertible, with inverse
`H^-1(x,y)=((x^2+c-y)/a,x)`. Each directed cycle therefore maps bijectively
to an ordinary cycle of the same least period. Every periodic point was
proved to lie among the labels, so this graph exhausts the whole field
domain. The 64 bounds and the coexistence rule follow. Formula (13) is
then just the elementary closed-walk identity for a partial permutation.

### 5. The six-value mixed-determinant restriction

Let `w_i=e_i d_i`. Eliminate `b_i` between the first two equations of
(19), using `e_i^2=d_i^2=1`. The result is

\[
\frac{\alpha-w_i\beta}{2}
=e_{i+1}{\bf1}_{w_{i+1}\ne w_i}
 +a e_{i-1}{\bf1}_{w_{i-1}\ne w_i}.                      \tag{20}
\]

If the cycle is mixed, both signs of `w` occur, proving (7).

Suppose `a` lies outside the six-value set (6). The nine quantities
`eta+a theta`, for `eta,theta in {-1,0,1}`, are pairwise distinct.
Indeed, a collision with different pairs gives a nonzero equation
`a=-Delta eta/Delta theta`, where the two differences lie in
`{-2,-1,0,1,2}`. If one difference were zero, so would the other, since
`a!=0` and `char k!=2`. Otherwise the ratio is one of (6). This proof
also covers all allowed positive characteristics, including coincidences
between the six displayed field values.

For all indices with the same `w_i`, the left side of (20) is fixed,
so distinctness forces **each of the two summands' signed coefficients**
to be fixed separately. In a mixed cyclic word there is a transition
from `+` to `-` and one from `-` to `+`. Therefore among `+` indices
there is one with an opposite-sign successor and one with an opposite-sign
predecessor. Their fixed coefficients are nonzero, so *every* `+` index
has both neighbors of sign `-`. The identical reasoning holds at `-`
indices. Thus `w` alternates.

The first signed coefficient in (20) also says that all `e_i` with a
given `w_i` are equal: each is the successor of an index of the other
sign. Hence `e_i,d_i` are two-periodic. The first equation of (19) makes
`b_i`, and then `y_i`, two-periodic as well.

But a cycle of period dividing two cannot be mixed. If its two coordinate
values are `p,q`, subtracting (16) gives

\[
(p-q)(p+q+a+1)=0.
\]

If `p=q` the signs agree. Otherwise `p+q=-(a+1)` is constant, forcing
both principal-part signs of `p,q` to be opposite, so their products
still agree. This contradiction proves (6).

### 6. The pure branch inside the monomial case

For a cycle with `w_i=kappa`, equation (20) forces
`beta=kappa alpha`. With (15), direct expansion gives
`c=-P_kappa^2+C_kappa`. Also

`e_i U+d_i V+b_i = e_i P_kappa+(b_i+e_i alpha/2)`.

The equations for these shifted offsets are (18), and the inherited
seven-row atlas is necessary and sufficient. This also proves the
pure-versus-mixed decomposition claimed after (15).

## A mixed orbit that falsifies the inherited-only shortcut

Over any characteristic different from two, put

\[
a=1,\quad P=t+1+\frac1{4t},\quad A=t-\frac1{4t},\quad c=-P^2.
\]

Then `A^2=P^2-2P`, and the cyclic coordinate word

\[
(A,-P,-A,-P)                                             \tag{21}
\]

satisfies (16). At the `A` and `-A` positions, `y_i^2+c=-2P`, the sum
of the two neighbors. At the `-P` positions it is zero, again the sum
of the neighbors. The four ordinary pair states are distinct because
`A` is nonconstant and `2A!=0`; its least period is four.

Taking `U=t,V=-1/(4t)` gives
`alpha=-2,beta=2,r=-1/4,C=-3/2`, sign words
`e=(+,-,-,-),d=(+,+,-,+)` and offsets `(0,-1,0,-1)`.
Thus its products are not constant. The single frozen exact diagnostic
found precisely this witness and stopped after 11 linear systems; it
did not scan periods five or six. The proof above is independent of that
program. Formula (21) is a low-period rationalization witness, not itself
a novelty claim or an exhaustive result.

## Author-side status, exact residual and limits

**Author-side mathematical status:** the theorem as formulated here is
closed by the proof above. It is a parameterwise exhaustive 64-state atlas,
with the nonexceptional branch reduced to the explicit inherited table.
The mixed part is not yet flattened into a list of all possible least
periods, sharp maxima, or all algebraic parameter components. Those are
not silently claimed. If the admission standard requires that stronger
normal-form table as opposed to a uniform exact graph atlas, the candidate
does not yet meet that stronger standard.

**Candidate residual after subtraction:** the two-pole global unit
rigidity, the six-value necessary restriction for genuinely mixed cycles,
and the exact constant-size rational reconstruction over all allowed fields.
Classical pole escape, finiteness, the one-pole seven-row table, local
horseshoes, the low-period example, and finite-cycle zeta identities are
not residual novelty. Independent substantive proof/source review and the
coordinator's material-increment judgment are still required.

No theorem here implies a target Euler factor, root number, automorphy,
divisor matching, or a Hilbert--Pólya realization. The constraint
`NO_BAD_EULER_OR_ROOT_NUMBER` is unconditional.
