# P197 Review B proof package

## Claim and status

**PROVABLE AS STATED.** The target is frozen Round 1, with its explicit
small-length qualifications and external hold unchanged. No all-time inverse,
efficient fixed-dimension depth formula, complete list of occurring divisors,
or external novelty theorem is added.

## Assumptions and notation

There are $n\ge1$ labelled cyclic positions and levels $-1,0,1$. The
synchronous map is $D(x)_i=\operatorname{sgn}(x_{i+1}-x_i)$; $\rho$ is left
shift. An open comparison operation $\delta$ shortens a word by one.
The tail $\tau$ is first entrance into the periodic set. For a nonconstant
word, $R$ is the largest cyclic constant-run length. Define
$K_n=\{x:D^4x=\rho^2x\}$. Fibonacci and Lucas indexing is as in the paper.

## Strategy and dependency map

1. Exhaustive local identities plus **backward constant-interval ancestry**
   prove all-size entrance, independently of finite cyclic graphs.
2. Invertibility on the entered language and explicit junction phases prove
   exact recurrence, sharp tails and the period divisor bound.
3. Labelled overlap windows prove depth/fixed traces. A different full
   polynomial certificate uses SCC blocks and Bareiss interpolation.
4. **Equality quotients and extremal-level sets**, followed by independent
   sets on paths/cycles, give an independent combinatorial inverse proof.
5. Global Fibonacci comparisons, not strictness of each merge, identify
   every maximum and its exceptional small ties.

## 1. Local identities and backward interval ancestry

On all 96 length-six words without equal neighbours,
$\delta^5(w)=\delta(w_2w_3)$. On all 1,344 length-seven words without a
constant triple, $\delta^6(w)=\delta^2(w_2w_3w_4)$. The reviewer reproduces
the unrestricted finite domains by successive sorted-pair comparisons, not
the radix-3 lookup used for cyclic graphs. It also verifies every orbit size,
extension count and output of the manuscript's eight representative rows.
Negation changes both sides' signs, and reversal changes them by the same
parity factor. Thus the finite certificate is complete. Since an arbitrary
cyclic window is one of these open words, repeated wrapping when $n$ is
shorter than the window causes no omission.

Here is a backward version of the attraction argument. In any image under
$D$, a constant nonzero interval of length three would require four strictly
ordered old levels, impossible in a three-level alphabet. Consequently
every constant image interval of length at least three is zero. Its inverse
ancestry is a constant interval longer by one. If $D^t x$ has a constant
triple, tracing this implication backwards through $t$ updates produces an
old constant interval of length at least $t+3$. This argument is applied only
until the word is constant; a constant cyclic image is necessarily zero,
since a strict increase or decrease around a cycle is impossible.

For $R\ge2$, after $R-2$ steps there can be no constant triple, unless zero
has already been reached. The second local identity then puts the state in
$K_n$ within two more steps. For $R=1$, use the first identity and one step.
Thus $\tau\le R$ for nonconstant inputs. Every constant goes to zero in
one step, with zero already fixed.

## 2. Recurrent set, exact first entry, and sharp witnesses

$D$ commutes with $\rho$. Hence $K_n$ is invariant, and on it
$\rho^{-2}D^3$ is a two-sided inverse of $D$. Every point of this finite
set is periodic. Since all states enter it, there are no periodic states
outside it, proving the exact clock in the manuscript. On the core,
$D^{4n/\gcd(n,2)}=\mathrm{id}$, so least periods divide that number;
the argument does not say that every divisor is realized.

For $x=0^{n-1}1$, the first output is $0^{n-2}(1,-1)$. If a phase has the
form $0^r\operatorname{Alt}_\ell(s)$ with $r\ge1$ and $\ell\ge2$, all
interior zero comparisons vanish, while the boundary to the alternating
part starts with $s$. Alternation and the final comparison back to zero
then give $0^{r-1}\operatorname{Alt}_{\ell+1}(s)$ exactly.

At even length the first fully alternating phase is in the core. At odd
length the phase with one zero is already in the core: for $n=2m+1$ and
$w=0\operatorname{Alt}_{2m}(s)$, the successive forms printed in the
manuscript give $D^4w=\rho^2w$, including $m=1$.
Earlier junctions are not core states. For $r\ge4$, coordinate $r-4$ of
$D^4$ is $s$ while that of the two-shift is zero. For $r=3$, coordinate
zero gives $-s$ versus zero. For $r=2$, coordinate $n-2$ gives a nonzero
letter versus zero after the fully alternating intermediate; this works in
both parity cases. For $r=1$ at even length, coordinate $n-2$ again
separates the two. These are exact local phase checks, not an inference from
a plotted orbit. They prove first entry at $n-1$ in even length and $n-2$
in odd length at least three. Directly checking $001$ and $01$ supplies
the stated small witnesses; arbitrary choices of the exceptional two values
are not asserted to be sharp there.

All nonconstant words other than a one-exception word have $R\le n-2$.
The preceding entrance bound and the explicit one-exception phases prove
the global upper bound in odd length as well as the lower bound. Even
length follows from $R\le n-1$. At $n=1$ the two nonzero states each enter
zero in one step. All tail boundaries therefore agree with the theorem.

## 3. Traces and a different characteristic-polynomial certificate

The vertex at labelled site $i$ of a closed overlap walk is the word
starting at $i$ of the specified window length. Overlap forces every later
window, and closing the walk forces periodic continuation. Conversely a
labelled cyclic word provides exactly one such walk with its site-zero
start. This is valid for every relative ordering of cycle length and window
length. No quotient by rotations is taken.

The allowed $A_t$ edges state precisely
$D^{t+4}x=\rho^2D^t x$, so the trace is the depth CDF. The $C_p$ edges
state $D^p x=x$. Dividing least-period point counts by $p$ and applying
divisor Möbius inversion gives the cycle formula. The verifier separately
multiplies sparse integer overlap matrices for $t=0,1,2$ through length six
and $p=1,2,3,4$ through length eight, including repeated-window cases.

For $A_0$, the independently constructed graph has 81 vertices and 165
edges. Boolean transitive closure divides it into 42 singleton components
without a loop, one singleton loop, and one 38-vertex strongly connected
component $B$. Ordering components topologically makes $zI-A_0$ block
triangular, hence

$$\det(zI-A_0)=z^{42}(z-1)\det(zI-B).$$

For each of the 39 distinct integers $z=0,1,\ldots,38$, fraction-free
Bareiss elimination computes the latter determinant exactly, checking every
division for zero remainder. The results equal

$$z^{32}(z^3-z^2-2z-1)(z^3+z^2+2z+1).$$

Both polynomials have degree at most 38. Agreement at 39 distinct points
therefore proves polynomial identity over the rationals, including every
coefficient and all zero roots. This proves the full degree-81 formula;
it is neither short-recurrence fitting, the author's Newton calculation,
nor Review A's Berkowitz implementation. The trace of every positive power
of a nilpotent block is zero. The seven nonzero eigenvalues therefore give
the stated seven-term recurrence for $R_n$ from $n\ge8$, with the seven
initial values independently computed from full graphs.

## 4. Every inverse source through an equality quotient

Fix a target $y$. Contract each cyclic zero edge, whose old endpoint levels
must agree. Every positive strict edge directs an inequality from its left
class to its right class, and every negative edge reverses it. A strict
self-edge makes the fibre empty. On the resulting directed quotient, an
assignment of levels $-1,0,1$ is equivalent to the following data:

- a low-level set contained in the directed source vertices;
- a disjoint high-level set contained in the directed sink vertices;
- all remaining vertices at middle level, with no edge between two of them.

Necessity follows because a low vertex cannot have an incoming strict edge,
a high vertex cannot have an outgoing strict edge, and equal middle levels
cannot satisfy a strict edge. Conversely those conditions make every edge
increase strictly: low-to-middle/high and middle-to-high are its only
possibilities. Each labelled source determines these sets uniquely and
lifting quotient levels uniquely restores every old coordinate. This gives
a full source-set reconstruction, independently tested against graph
incoming sets for every target through $n=6$.

If all target edges are zero there is one equality class and three sources.
Otherwise delete the zero edges to obtain the strict cyclic skeleton. One
sign only is impossible, and three consecutive equal signs require four
levels, also impossible. A doubled positive run forces its three old
levels to be $-1,0,1$; a doubled negative run forces $1,0,-1$.
These fixed endpoints separate the remaining alternating segments.

Consider $g$ singleton runs between successive doubled runs. If $g=0$ or
$g=1$, the anchors force a unique assignment. If $g\ge2$, there are
$g-1$ interior extrema. An interior valley is either $-1$ or zero, and an
interior peak is either zero or $1$. The only forbidden adjacent choice is
zero at both endpoints. Thus choosing the zero extrema is exactly choosing
an independent set of a path on $g-1$ vertices. Its count is $F_{g+1}$,
by conditioning on whether the first vertex is chosen. Different anchored
gaps are independent, so the fibre is the product of these factors. All
factors are positive, proving the image criterion's converse, not only its
necessity.

Without any doubled run, the skeleton alternates and has even length $r$.
The same zero-extremum bijection now gives independent sets of the cyclic
graph on $r$ vertices. Its count is $F_{r-1}+F_{r+1}=L_r$. At $r=2$ the
two opposite strict comparisons impose the same inequality twice; its
three assignments still agree with $L_2=3$. Finally, the trace of the
three comparison matrices merely enumerates these same closed level
assignments, so the manuscript's trace formula agrees with this independent
combinatorial reconstruction for every target, including absent ones.

## 5. Strict optimization and all equality cases

Let $q>0$ be the number of doubled runs. The total number of sign runs is
even, giving $q\equiv r\pmod2$ and $r=2q+\sum g_j$. The addition identity

$$F_aF_b\le F_{a+b-1}\qquad(a,b\ge1)$$

successively bounds the gap product by $F_{r-2q+1}$. If $r$ is even,
$q\ge2$, so this is at most $F_{r-3}<L_r$. If $r$ is odd, $q=1$ gives
exactly $F_{r-1}$ and $q\ge3$ gives at most $F_{r-5}<F_{r-1}$. All indices
used here are nonnegative because a realizable skeleton has the required
number of strict edges. Individual merge inequalities may be equalities;
the strict final comparisons are what exclude extra global maximizers.

For even $n\ge4$, the full alternating skeleton gives $L_n$, strictly
larger than every shorter or doubled skeleton and the all-zero value three.
There are exactly two such targets. For odd $n\ge5$, the largest even
skeleton length is $n-1$; its value $L_{n-1}$ strictly beats $F_{n-1}$
and every shorter length. One zero can be placed at any of $n$ labelled
positions and either alternating orientation is allowed, giving exactly
$2n$ targets. At $n=2,3$, the zero target also has fibre three and creates
respectively three and seven maximizers. At $n=1$, zero alone is in the
image and has fibre three. No other equality case survives.

## Independent finite graph logic and remaining risks

The verifier extracts the recurrent set as the image of $D^{3^n}$ by binary
lifting. This is valid for any map on $3^n$ states and does not presume the
core theorem or period bound. Lifted first entrance then determines tails;
only afterwards are the theorem's core and period conditions compared.
All 797,160 source states and the same number of target words at $n\le12$
are checked. Actual source-set reconstruction is limited to $n\le6$;
all target counts and all equality targets are checked through $n=12$.
Finite checks are not extrapolated beyond these ranges. The all-size
claims rest on the deductions above.

No correction or extra assumption is required. Higher-block, time-iterate,
and other uninspected owner encodings remain open; a valid mathematical
package and a bounded source non-hit do not prove novelty.
