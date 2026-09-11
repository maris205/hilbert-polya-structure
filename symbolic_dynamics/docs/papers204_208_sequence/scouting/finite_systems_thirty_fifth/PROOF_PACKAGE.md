# Scout35 proof package

## Claim

The desired admission claim is an all-$d$ classification of the full
temporal/recurrent structure of unsigned Boolean Fourier-support feedback,
with a genuinely separate full-target inverse or extremal mechanism after
classical deductions. A partial orbit family or an extremizer's location
alone is not this claim.

## Status

**NOT CURRENTLY JUSTIFIED.** No full-carrier temporal atlas or sharp height
has been proved. The complete narrower statements below are
**PROVABLE AS STATED**, but the original admission claim has not survived.

D1 is an exact historical duplicate by the identity adapter in the intake;
there is no proposed D1 theorem requiring a new proof.

## Assumptions

Let $d\ge0$ be an integer, let $V=\mathbb F_2^d$, and let $N=2^d$.
The dot product is the nondegenerate standard coordinate form over
$\mathbb F_2$. Each state is an arbitrary subset $A\subseteq V$.
Fourier sums and binomial coefficients are evaluated in the integers.

## Notation

Write $\chi_\xi(x)=(-1)^{\xi\cdot x}$,
$h_A(\xi)=\sum_{x\in A}\chi_\xi(x)$, and
$U(A)=\{\xi:h_A(\xi)\ne0\}$.
For comparison only, the old WZS map is
$$W_A(\xi)=\sum_{x\in V}(-1)^{1_A(x)+\xi\cdot x},
\qquad Z(A)=\{\xi:W_A(\xi)=0\}.$$
For a subspace $L\le V$ let
$L^\perp=\{\xi:\xi\cdot x=0\text{ for all }x\in L\}$.
For a target $B\subseteq V$ let $m(B)=|\{A:U(A)=B\}|$.

## Proof strategy

Use character cancellation to isolate the exact adapter, the boundary
orbits, and the classical subspace restriction. Use parity of integer
character sums to lower-bound the full-support fibre; compare every
other target to one balanced-character hyperplane. No finite enumeration
or empirical conjecture enters any proof.

## Dependency map

1. Pairing under a nonzero linear character gives the total character sum.
2. That sum and the signed-indicator identity give the exact old-map adapter.
3. Parity, translation and subspace cancellation give limited temporal facts.
4. One missing nonzero frequency forces equal counts in two halves of $V$.
5. The resulting central-binomial bound and odd-weight forcing locate the
   maximum-fibre target; dimensions zero and one are handled separately.
6. None of Steps 1--5 gives a global potential or exhausts arbitrary cycles.

## Proof

### Step 1: elementary character identities

At $\xi=0$ every summand is one, hence $h_A(0)=|A|$.
For nonzero $\xi$, choose $v\in V$ with $\xi\cdot v=1$.
Translation by $v$ pairs each $x$ with $x+v$, and their signs cancel.
Thus
$$\sum_{x\in V}\chi_\xi(x)=N1_{\xi=0}.$$
Since $(-1)^{1_A(x)}=1-2\,1_A(x)$, it follows that
$$W_A(\xi)=N1_{\xi=0}-2h_A(\xi).$$
For every nonzero $\xi$, membership in $U(A)$ is precisely nonmembership
in $Z(A)$. At zero, however,
$$0\in U(A)\iff A\ne\varnothing,\qquad
0\in Z(A)\iff |A|=N/2.$$
The second condition is impossible for $d=0$ because $|A|$ is integral.
The exact universal adapter is therefore
$$U(A)=\bigl((V\setminus Z(A))\setminus\{0\}\bigr)
\ \cup\
\begin{cases}\{0\},&A\ne\varnothing,\\
\varnothing,&A=\varnothing.
\end{cases}$$
It reduces to $U(A)=V\setminus Z(A)$ for nonempty unbalanced $A$,
but fails at the empty state and at nonempty balanced states. This is an
output adapter with an input-dependent zero-frequency correction; it is
not a proved conjugacy. No old WZS orbit census transfers through it.

### Step 2: symmetries and boundary trajectories

Changing variables $x=y+a$ gives
$$h_{A+a}(\xi)=\chi_\xi(a)\,h_A(\xi).$$
The multiplicative factor is always $1$ or $-1$, so $U(A+a)=U(A)$.
For nonzero $\xi$ the complement identity is
$h_{V\setminus A}(\xi)=-h_A(\xi)$.
When $A$ is nonempty and proper both zero-frequency coefficients are
positive, giving $U(V\setminus A)=U(A)$ in exactly this stated range.
For $A=\varnothing$ or $A=V$ the complement assertion is not used.

The direct evaluations are
$$U(\varnothing)=\varnothing,\qquad U(V)=\{0\},\qquad U(\{0\})=V.$$
For $d\ge1$ the latter two states are distinct and form a two-cycle.
When $d=0$, $V=\{0\}$; the empty and full states are two distinct fixed
states. If $|A|$ is odd, every $h_A(\xi)$ is a sum of an odd number of
signs, hence is an odd integer and cannot vanish. Consequently $U(A)=V$
for every odd-cardinality state in every dimension. This describes their
subsequent orbit but not the orbit of every even-cardinality state.

### Step 3: affine-subspace trajectories are a deducted family

For $A=a+L$, translation gives
$h_A(\xi)=\chi_\xi(a)\sum_{x\in L}\chi_\xi(x)$.
If $\xi\notin L^\perp$, choose $v\in L$ with $\xi\cdot v=1$;
pairing $x$ with $x+v$ cancels the sum over $L$.
If $\xi\in L^\perp$, all signs on $L$ are one. Thus
$$h_{a+L}(\xi)=|L|\,\chi_\xi(a)\,1_{\xi\in L^\perp},
\qquad U(a+L)=L^\perp.$$

The form on $V$ is nondegenerate: a vector orthogonal to every coordinate
basis vector has all coordinates zero. Every linear functional on $L$
extends to $V$ by extending a basis, and every functional on $V$ is a dot
product with a vector. It follows that the linear map $V\to L^*$ is
surjective and has kernel $L^\perp$, so
$\dim L^\perp=d-\dim L$. Inclusion $L\subseteq(L^\perp)^\perp$ and
equality of dimensions imply $(L^\perp)^\perp=L$. Hence
$$U^2(a+L)=L,\qquad U^3(a+L)=L^\perp.$$
The subspaces $L$ and $L^\perp$ are fixed exactly when equal, and otherwise
form a two-cycle. The affine initial state enters this family in one step.
This is the classical orthogonal-complement involution on an invariant
family and receives no new temporal credit. Exhaustion of all recurrent
states by this family has not been proved.

### Step 4: every competing fibre has a uniform upper bound

If $U(A)=\varnothing$, its zero-frequency coefficient vanishes, so
$|A|=0$ and $A=\varnothing$. Therefore $m(\varnothing)=1$.
Every nonempty output contains zero; thus $m(B)=0$ for nonempty $B$ not
containing zero.

Now let $d\ge1$ and let $B$ be nonempty, proper, and contain zero.
Choose $\xi\in V\setminus B$; it is nonzero.
A predecessor must have $h_A(\xi)=0$.
The two character halves
$H_+=\{x:\xi\cdot x=0\}$ and $H_-=\{x:\xi\cdot x=1\}$
both have size $N/2$, since translation by a vector with dot product one
is a bijection between them. The equation $h_A(\xi)=0$ is equivalent to
$|A\cap H_+|=|A\cap H_-|$. The number of subsets satisfying it is
$$\sum_{k=0}^{N/2}\binom{N/2}{k}^2=\binom{N}{N/2}.$$
To justify the equality, count $N/2$-element subsets of a disjoint union of
two $N/2$-element sets according to the number $k$ chosen from the first:
the second factor is $\binom{N/2}{N/2-k}=\binom{N/2}{k}$.
The empty set is included in this count but cannot map to nonempty $B$.
Thus every such target satisfies
$$m(B)\le\binom{N}{N/2}-1.$$
This is an upper bound, not an evaluation of its exact fibre.

### Step 5: exact location of the maximum fibre, not its value

For $d\ge1$, toggling one fixed element bijects the even- and odd-cardinality
subsets of $V$, so there are $2^{N-1}$ odd-cardinality subsets.
Step 2 implies
$$m(V)\ge2^{N-1}.$$
For $N\ge4$ even, write $N=2r$. The normalized central binomial numbers
$c_r=\binom{2r}{r}/4^r$ obey
$$\frac{c_{r+1}}{c_r}=\frac{2r+1}{2r+2}<1,\qquad c_2=\frac38.$$
The ratio follows by cancelling the factorial expressions.
Consequently $\binom{N}{N/2}\le3\cdot2^N/8<2^{N-1}$ for all such $N$.
Step 4 bounds every nonempty proper target strictly below $m(V)$;
the empty target has size one and is also strictly smaller.
Targets not containing zero have no predecessors.

For $d=1$, write $V=\{0,e\}$. The four exact transitions, obtained directly
from the two character sums, are
$$\varnothing\mapsto\varnothing,\quad
\{0\}\mapsto V,\quad\{e\}\mapsto V,\quad V\mapsto\{0\}.$$
The fibre sizes are therefore $1,1,0,2$ for targets
$\varnothing,\{0\},\{e\},V$. For $d=0$ both fixed states have one predecessor.

It follows that for every $d\ge1$, $V$ is the unique maximum-fibre target.
For $d=0$ both targets tie with fibre size one. This theorem identifies
every maximizer but does not give an all-$d$ formula for $m(V)$.

### Step 6: the remaining inverse and temporal obligations

For arbitrary $B$ the defining constraints
$$h_A(\xi)=0\quad(\xi\notin B),\qquad
h_A(\xi)\ne0\quad(\xi\in B)$$
are necessary and sufficient for membership in the fibre.
They are just intersections and exclusions of ordinary character
hyperplanes on $0$--$1$ vectors. Restating them supplies no new full-target
decoder or count. The bounds in Steps 4--5 cannot replace that missing
mechanism, and supply no bound on the transient length.

## Corrections or missing assumptions

No silently narrowed carrier is used: the admitted target remains the
entire power set in every dimension. The proved affine-subspace statement
is separately labelled as a weaker family result. There is no completed
lemma forcing arbitrary states into that family, no proof ruling out
other recurrent states, and no sharp global-height theorem.

## Open risks

The elementary extremizer-location result is an inverse-only residual
and is not claimed novel. The old WZS adapter is especially close.
The bounded source search does not prove absence of a direct prior owner.
No dedicated source/value gate, independent review, admission or paper
number follows from this package. **NO_PROMOTION / HOLD_EXTERNAL**.
