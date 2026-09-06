# MNC: temporal law, complete inverse and sharp global fibre maximum

2026-09-06 UTC. Main proof author: `batch197_lzk_gate`; root independently
contributed the evaluated distance-word lemma in
[MNC_DISTANCE_DECODER.md](../MNC_DISTANCE_DECODER.md), which was read in
full and agrees with Step 3's independent derivation. Both are mathematical
contributors and cannot provide an independent MNC manuscript review.
This is contributor work, not an independent review. MNC and MDE belong to one contrast family;
no second family seat, candidate admission, paper number or release.

## Claim

For a labeled cyclic word $x\in\{0,1,2\}^n$, $n\ge3$, put
$$F(x)_i=\min\{|x_i-x_{i-1}|,|x_i-x_{i+1}|\}.$$
All subscripts are modulo $n$ and updates are synchronous. Then:

1. $F^4=F^3$. The fixed states are $0^n$ and words whose positive symbols
   are singleton pulses, each labeled 1 or 2, separated by at least two
   zeros. Every recurrent state is fixed. The sharp entrance is two for
   $n=3,4$, and three for every $n\ge5$.
2. Step 3 below is a complete labeled inverse-set decoder for every target,
   with explicit edge-word weights; it is not merely an image criterion.
3. Let $c_0=2,c_1=1,c_{t+2}=c_{t+1}-c_t$, and set
   $$Z_n=2^n+(-1)^n+2c_n
       =2^n+(-1)^n+4\cos(n\pi/3).$$
   For every $n\ge4$, $0^n$ is the **unique** maximum-fibre target, with
   fibre size $Z_n$. For $n=3$, the **unique** maximum target is $111$,
   with exactly six sources, the permutations of $012$.

## Status

**PROVABLE AS STATED.** All-parameter deductions appear below. Finite
checks pressure the implementation and small boundary cases; they are
not the justification for extending the statements to arbitrary $n$.
The source/value assessment is separate and not a consequence of this
proof status. In particular the binary ECA36 restriction, run languages,
proper cycle colorings and generic transfer/trace methods are prior tools.

## Assumptions and notation

- The alphabet is exactly $\{0,1,2\}$ and the metric is ordinary absolute
  difference, not cyclic color distance.
- Neighbors are distinct, because $n\ge3$. Positions remain labeled;
  rotations are not quotiented or multiplied back into inverse counts.
- A run is a maximal cyclic constant source block. A source position is
  a singleton iff both neighbors have different source values.
- A positive target block is a maximal consecutive block of nonzero
  target coordinates; it need not be a constant run.
- Matrices use color order $0,1,2$. The trace counts closed labeled walks,
  without identifying cyclic shifts of a walk.
- The formal sequence values at index zero used in trace recurrences are
  algebraic initial conditions, not claims about the excluded empty cycle.

## Strategy and dependency map

1. Equal source edges force adjacent target zeros. This gives permanent
   zero blocks and a two-step reduction of the remaining positive blocks.
2. Classify the first images at lengths three and four and give witnesses
   at every larger length to make the temporal bound sharp.
3. Decode via absolute edge differences and closed color walks. This
   general static representation is fully deducted for originality.
4. Evaluate the zero fibre through matchings and proper cycle colorings.
5. For a mixed target, forget its positive magnitudes but retain the exact
   source-singleton set. Commuting color-symmetric block matrices give an
   exact relaxed count and a strict uniform upper bound.
6. Bound all-positive targets containing 2 by a forced source triple;
   count the all-one target through two short types of run tile. Together
   these cases exhaust all targets and prove the unique maximizer.

## Proof

### Step 1. Paired zeros, positive blocks and the eventual fixed set

For any source $x$, an output $F(x)_i=0$ holds exactly when $x_i$ equals
at least one neighbor. An equal source edge produces zero at both of its
endpoints. Therefore **every zero in an image has a zero neighbor**.
Once two adjacent zeros occur, both stay zero forever: their mutual
contrast is zero. Consequently all image-zero positions are permanent.

Let $y=F(x)$ contain a zero. Its positive blocks are bounded by permanent
zeros, and each separating zero block has length at least two. A singleton
positive block, whether 1 or 2, is fixed because its two contrasts to zero
equal its own value. Consider a positive block of length at least two.
All its source values in $y$ belong to $\{1,2\}$. At each interior site
both adjacent differences are 0 or 1. At a boundary site the difference
to the inside neighbor is 0 or 1, so the minimum is at most one even if
the outside difference is two. Thus the whole block becomes binary after
one update. At that update the singleton 2 blocks remain isolated and
separated from the binary blocks by permanent zero blocks.

Put $z=F(y)$. As an image, $z$ still has a zero neighbor at every zero.
In a binary positive block of $z$, a singleton 1 stays 1; a block of at
least two consecutive ones becomes all zero, because every site in it
has an equal neighbor. The isolated 2 blocks remain fixed. After this
update all positive symbols are singleton pulses separated by at least
two zeros, and such a word is fixed by the literal rule.

If $y$ has no zero, it uses only values 1 and 2, so $z=F(y)$ is entirely
binary. If $z$ is constant, its next image is $0^n$. Otherwise its zeros
have zero neighbors, and the preceding binary-block argument shows that
$F(z)$ consists of isolated ones separated by at least two zeros. Thus
$F^3(x)$ is fixed in this case too. This proves $F^4=F^3$.

Conversely any fixed state is itself an image. If it has a zero, the
positive-block analysis forbids a positive block of length at least two:
such a block would have to be binary already, then vanish. Its positive
symbols are therefore isolated pulses, with zero blocks of length at
least two. A zero-free fixed word would first have to be binary, hence
all one, but all one maps to all zero. This gives the asserted complete
fixed set. A recurrent state of a finite map with $F^4=F^3$ must lie in
the fixed image of $F^3$, so there are no nontrivial recurrent cycles.

### Step 2. The small first images and all-length sharp witnesses

For $n=3$, a source is constant, has a repeated pair plus a singleton,
or has three distinct values. The first case gives $000$. In the second,
the repeated positions give zero and the singleton gives the distance
between the two values, namely 1 or 2. In the third case the three
source values are $0,1,2$, and every local minimum contrast is one.
Thus the first image is exactly
$$\{000,111\}\cup\operatorname{Rot}(001)\cup\operatorname{Rot}(002).$$
All of these are fixed except $111$, which maps to $000$. The source
$012\to111\to000$ proves sharp entrance two.

For $n=4$, an image with zeros has a zero block of length two, three or
four; two distinct zero blocks would already occupy all four positions.
A length-three zero block leaves a singleton positive pulse, already
fixed. For a length-two zero block, rotate its positions to 0 and 1.
The source has form $(a,a,b,c)$. Positivity of the other two outputs
forces $a,b,c$ pairwise distinct; hence both positive outputs equal one.
The target is a rotation of $0011$, whose next image is zero.

For a zero-free four-letter image, the source is a proper coloring of
the cycle. If an output is 2 at site $i$, then the source triple centered
there is $020$ or $202$. The remaining source site, adjacent to the two
equal extreme neighbors of that triple, is either the other extreme or
1. In the former case the source alternates 0 and 2 and the target is
$2222$. In the latter case direct distances give a single output 2 and
three outputs 1. If no output is 2, the target is $1111$.
Consequently the zero-free possibilities are precisely $1111$, $2222$
and the rotations of $2111$. Both constants map to zero; $2111$ maps
to $1000$, a fixed pulse. Thus every source at $n=4$ is fixed by time
two. The source $0012\to0011\to0000$ attains two.

At $n=5$ use the explicit orbit
$$01102\longmapsto10012\longmapsto10011\longmapsto00000.$$
The middle positive block wraps around the origin; its lengths are
three, first $121$ and then $111$. None of the first three displayed
states is fixed. At every $n\ge6$ use
$$0^{n-4}1102\longmapsto0^{n-2}12
\longmapsto0^{n-2}11\longmapsto0^n.$$
The initial zero run has length at least two, so the first coordinate
also maps to zero, unlike the explicitly separated $n=5$ case. These
orbits attain three and finish the sharp entrance law.

### Step 3. Full arbitrary-target inverse decoder and explicit weights

For $x$ define $d_i=|x_i-x_{i+1}|$. Then
$$F(x)_i=\min(d_{i-1},d_i).$$
For a prescribed target $b$, let
$$\mathcal D(b)=\{d\in\{0,1,2\}^n:
                  \min(d_{i-1},d_i)=b_i\text{ for every }i\}.$$
Equivalently, $d_i\ge\max(b_i,b_{i+1})$ for each edge, and every vertex
has at least one incident edge with difference exactly $b_i$.
The color transition matrices are
$$R_0=I_3,\qquad
R_1=\begin{pmatrix}0&1&0\\1&0&1\\0&1&0\end{pmatrix},\qquad
R_2=\begin{pmatrix}0&0&1\\0&0&0\\1&0&0\end{pmatrix}.$$

Choose $d\in\mathcal D(b)$, choose an initial color, then every successive
color so that $(R_{d_i})_{x_i,x_{i+1}}=1$, including the final closing
edge. The resulting word has target $b$. Conversely every source uniquely
recovers both its edge word and its color walk. This proves a labeled
bijection, with no rotational multiplicity, and gives
$$|F^{-1}(b)|=\sum_{d\in\mathcal D(b)}w(d),\qquad
w(d)=\operatorname{tr}(R_{d_0}\cdots R_{d_{n-1}}).\tag{1}$$

The weight can be evaluated without matrix multiplication. Let $u$ be
the number of edges labeled 1 and $v$ the number labeled 2. Then:

- If $u=v=0$, $w(d)=3$.
- If $u=0<v$, $w(d)=2$ when $v$ is even and $w(d)=0$ when $v$ is odd.
- If $u$ is odd, $w(d)=0$.
- If $u=2k>0$ and $v=0$, $w(d)=2^{k+1}$.
- If $u=2k>0$ and $v>0$, $w(d)=2^k$ exactly when between every two
  cyclically consecutive edges labeled 2 there are an even number of
  edges labeled 1; otherwise $w(d)=0$. Zero edges do not affect this test.

Here is a proof including the last case. The color-reflection-invariant
subspace consists of vectors $(a,b,a)$; on it $R_1$ and $R_2$ act as
$$U=\begin{pmatrix}0&1\\2&0\end{pmatrix},\qquad
P=\begin{pmatrix}1&0\\0&0\end{pmatrix}.$$
On the complementary line spanned by $(1,0,-1)$ they act as 0 and $-1$.
Thus any occurrence of $R_1$ kills that latter contribution. We have
$U^2=2I_2$ and $PU^{2j}P=2^jP$, whereas $PU^{2j+1}P=0$.
If there is a $P$, cut the trace at one such factor; the even-gap test
and product $2^k$ follow. If there is no $P$, the trace of $U^{2k}$ is
$2^{k+1}$ and the trace of an odd power is zero. With no $U$, the direct
traces of $I_3$ or $R_2^v$ give the first two cases. This proves all of (1).
It is a standard finite-walk/static decoder, not an originality claim.

### Step 4. The zero fibre and its classical matching formula

A source of $0^n$ has no singleton run: every source vertex has an equal
neighbor. Let $D$ be its set of nonconstant source edges. The condition
is exactly that $D$ is a matching in the labeled cycle, since consecutive
nonconstant edges would create a singleton. If $|D|=k$, equality edges
contract to a cycle of $k$ color blocks, counted by
$$\operatorname{tr}Q^k=2^k+2(-1)^k,\qquad
Q=\begin{pmatrix}0&1&1\\1&0&1\\1&1&0\end{pmatrix}.$$
This formula includes $k=0$ as three constants and $k=1$ as zero sources;
the matrix trace, not an informal one-vertex simple graph, defines those
two boundary cases. It also counts the two-block cycle correctly.

Write $I(C_n;t)=\sum_{D\text{ matching}}t^{|D|}$. Then
$$|F^{-1}(0^n)|=I(C_n;2)+2I(C_n;-1).\tag{2}$$
Matchings of a cycle are independent sets of its edge-cycle. The ordinary
two-state independent-set transfer
$H(t)=\begin{pmatrix}1&t\\1&0\end{pmatrix}$ gives
$I(C_n;t)=\operatorname{tr}H(t)^n$ for $n\ge3$, by retaining whether
the preceding edge is selected. Its characteristic equation is
$z^2-z-t=0$. At $t=2$ the roots are 2 and $-1$, so the first term in
(2) is $2^n+(-1)^n$. At $t=-1$, traces satisfy the $c_n$ recurrence
in the claim, with the periodic sequence
$$c_n: 2,1,-1,-2,-1,1,2,1,\ldots.$$
Thus (2) equals $Z_n$ and $Z_n\ge2^n-5$. All of this zero-fibre
language, matching correspondence and recurrence is explicitly deducted
as classical static enumeration.

### Step 5. Exact relaxed singleton-set count for every mixed target

Suppose $b$ has both zero and positive entries. If a zero block has
length one, its fibre is empty by Step 1. Otherwise write the lengths
of its $r\ge1$ zero blocks as $\ell_1,\ldots,\ell_r\ge2$ and let
$K\ge1$ be the total number of positive entries. Thus
$n=K+\sum_j\ell_j$. Relax the target constraints by prescribing only
which source vertices are singletons, forgetting whether a positive
minimum contrast is 1 or 2. This relaxation contains every source of $b$.

Across every edge incident to a prescribed singleton the two colors
must differ. A positive block of length $k$ therefore contributes $k+1$
consecutive $Q$ transitions. Inside a zero block of length $\ell$, the
first and last internal edges must be equal-color edges, since the
outside edges meet positive target positions and are already different.
For $\ell=2$, these first and last internal edges are one and the same
edge, forced equal. For $\ell=3$, both internal edges are forced equal.
For $\ell\ge4$, the remaining $\ell-3$ internal edges may be different
only on a matching; each such edge contributes $Q$, and equal edges
contribute $I_3$.

Consequently the exact endpoint-color matrix of a zero block is
$$B_2=B_3=I_3,\qquad B_\ell=B_{\ell-1}+QB_{\ell-2}
\quad(\ell\ge4).\tag{3}$$
The recurrence is the path-matching decomposition according to the last
available internal edge. All these matrices are polynomials in $Q$,
so they commute with $Q$ and with one another. Therefore the exact
number of sources in the relaxed class is
$$S(b)=\operatorname{tr}\left(Q^{K+r}\prod_{j=1}^rB_{\ell_j}\right)
      =2^{K+r}\prod_{j=1}^r a_{\ell_j}
        +2(-1)^{K+r}\prod_{j=1}^r e_{\ell_j}.\tag{4}$$
Here $a_2=a_3=e_2=e_3=1$,
$$a_\ell=a_{\ell-1}+2a_{\ell-2}
       =\frac{2^{\ell-1}+(-1)^\ell}{3},\qquad
e_\ell=e_{\ell-1}-e_{\ell-2}.$$
The scalar $a_\ell$ is the eigenvalue of $B_\ell$ on constant vectors;
$e_\ell$ is its eigenvalue on the two-dimensional sum-zero subspace.
This follows from the eigenvalues $2,-1,-1$ of $Q$ and proves (4),
including $r=1$ and the original cyclic closing condition. The product
does not forget labeled source choices: it counts them by the successive
endpoint colors before taking the trace.

For every $\ell\ge2$,
$$a_\ell\le2^{\ell-2},\qquad |e_\ell|\le1.$$
The first follows by induction from the two initial values and (3)'s
scalar recurrence; the second follows from the repeating six values
$1,1,0,-1,-1,0$ beginning at $\ell=2$. Equation (4) now gives
$$|F^{-1}(b)|\le S(b)
\le2^{K+r+\sum_j(\ell_j-2)}+2
=2^{n-r}+2\le2^{n-1}+2.\tag{5}$$
For every $n\ge4$,
$$2^{n-1}+2<2^n-5\le Z_n,$$
because $2^{n-1}\ge8>7$. In particular the explicit relaxed bounds
at $n=4,5$ are 10 and 18, below $Z_4=15$ and $Z_5=33$.
Thus **every mixed target has strictly fewer sources than the zero target**.
This comparison, unlike (2) alone, treats all mixed singleton placements.

### Step 6. All-positive targets and complete equality exclusion

Suppose $b$ has no zero. Every source is then a proper three-coloring of
$C_n$. If some $b_i=2$, its centered source triple is either $020$ or
$202$. Once that triple is selected, the remaining $n-3$ vertices can
be revealed along the complementary path with at most two color choices
at each step; closing the path can only reduce the choices. Therefore
$$|F^{-1}(b)|\le2\cdot2^{n-3}=2^{n-2}<Z_n\quad(n\ge4).\tag{6}$$
For the last inequality, $Z_n\ge2^n-5$ and
$2^n-5-2^{n-2}=3\cdot2^{n-2}-5>0$ at $n\ge4$.

It remains to consider $b=1^n$. Its sources are proper colorings avoiding
the triples $020,202$. They must contain a color 1: otherwise properness
forces a cyclic 0/2 alternation, which contains one of the forbidden
triples. Between consecutive occurrences of 1 there are therefore either
one extreme color ($0$ or $2$), or two different extreme colors ($02$
or $20$). These give two tile types, of total lengths two and three,
respectively, and each type has two color choices.

For a label-preserving count, use states $s,a_0,a_2,b_0,b_2$. A color-1
position has state $s$; an extreme immediately following a 1 has state
$a_0$ or $a_2$; an extreme following an extreme has state $b_0$ or $b_2$.
The directed transitions are
$$s\to a_0,a_2;\quad a_0\to s,b_2;\quad a_2\to s,b_0;
\quad b_0,b_2\to s.$$
Every allowed source has exactly one such cyclic state lift and vice
versa. The adjacency matrix on the color-symmetric subspace reduces to
$$T=\begin{pmatrix}0&2&0\\1&0&1\\1&0&0\end{pmatrix}.$$
On the antisymmetric subspace its matrix is
$\begin{pmatrix}0&-1\\0&0\end{pmatrix}$, whose positive powers have
trace zero. Hence
$$|F^{-1}(1^n)|=t_n:=\operatorname{tr}T^n\quad(n\ge3).$$
Since the characteristic polynomial is $z^3-2z-2$,
$$t_0=3,\quad t_1=0,\quad t_2=4,\qquad
t_n=2t_{n-2}+2t_{n-3}\quad(n\ge3).\tag{7}$$
In particular $t_3=6,t_4=8,t_5=20,t_6=28$. For $n=4,5,6$ these
values satisfy $t_n\le(3/4)2^n$. Induction using (7), whose two lower
indices are at least four when $n\ge7$, gives
$$t_n\le\frac34\bigl(2^{n-1}+2^{n-2}\bigr)
        =\frac9{16}2^n<\frac34 2^n.$$
Thus the bound holds for every $n\ge4$. At $n=4$,
$t_4=8<Z_4=15$ directly. For $n\ge5$,
$t_n\le(3/4)2^n<2^n-5\le Z_n$, since $2^{n-2}\ge8>5$.
This eliminates every all-positive target.

Steps 4–6 exhaust zero, mixed and all-positive targets. Every nonzero
target is strict for $n\ge4$, so $0^n$ is the unique maximizer. At
$n=3$, Step 2's complete first-image classification gives fibre three
at $000$, four at each rotation of $001$, two at each rotation of $002$,
and six at $111$. These counts partition $27=3+3\cdot4+3\cdot2+6$.
Therefore $111$ is the unique three-letter maximizer, with the six
permutations of $012$ as its full source set. This proves all claims. $\square$

## Corrections or missing assumptions

No claim of two independent MNC/MDE systems is made. This proof concerns
only MNC and the stated ternary cyclic carrier. It neither promotes the
candidate nor extends its formulas to larger alphabets, noncyclic finite
boundaries, asynchronous updates, or an all-time inverse formula.

## Open risks

The all-target decoder, zero-fibre enumeration and all-one constrained
language have direct classical representations. Those are zero-credit
ingredients, not three new axes. The remaining source/value question is
whether an earlier complete adapter already supplies the mixed singleton
class optimization together with all-positive exclusion, and whether the
ternary temporal reduction is a direct old system wrapper. The binary
restriction is ECA36, whose second-iterate stabilization is already prior.
An independent candidate gate must assess the exact conjunction after
these deductions; this author proof does not certify novelty. No external
upload, contact or release is authorized. HOLD_EXTERNAL.
