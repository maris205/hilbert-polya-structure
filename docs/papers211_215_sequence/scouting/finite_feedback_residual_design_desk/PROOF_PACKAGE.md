# Proof package — support-count remainder feedback

2026-09-08 UTC. Author and proof contributor:
/root/round211_rational_scout.
One new local literal, F1/SCRF. No scientific program was run.

## Claim and status

**PROVABLE AS STATED:** the finite autonomous map below has only fixed
recurrent states; its exact worst entrance time is
$H(n,M)=\min(n,M)$; all equality sources and their number are explicit.
Every target has a disjoint explicit inverse decoder and finite product
sum. The image has an explicit support/maximum criterion. Zero is the
unique target with maximum one-step fibre.

**NOT CURRENTLY JUSTIFIED:** that these mathematically separate deductions
leave two independent research contributions after the existing
support-budget, quotient-decoding and monotone-injection mechanisms are
deducted. This package closes as an author negative design desk,
not an admission or independent review.

## Assumptions and notation

Fix integers $n\ge1$ and $M\ge0$, and let
$$X_{n,M}=\{0,\ldots,M\}^n.$$
Write $[n]=\{1,\ldots,n\}$. Coordinates are labelled and never deleted
or relabelled. Put
$$K(x)=\{i:x_i>0\},\qquad k(x)=|K(x)|.$$
The literal update is
$$
F(x)=
\begin{cases}
0^n,&k(x)=0,\\
(x_i\bmod k(x))_{i=1}^n,&k(x)>0.
\end{cases}
\tag{1}
$$
The remainder is the ordinary integer in
$\{0,\ldots,k(x)-1\}$. In particular a singleton positive coordinate is
reduced modulo one to zero; it is not protected by a guard. All updates
are simultaneous and use the original support count.

Write $h(x)=\min\{t\ge0:F^{t+1}(x)=F^t(x)\}$. The arguments below prove
this set is nonempty and that it is the first entrance into the recurrent
set. Let $H(n,M)=\max_{x\in X_{n,M}}h(x)$.

For a target $y$, write
$$Y=K(y),\qquad s=|Y|,\qquad m=\max_i y_i,$$
so $m=0$ at the zero vector. For $k\ge1$, set
$$B_k=\lfloor M/k\rfloor,\qquad
 A_i(k)=1+\lfloor(M-y_i)/k\rfloor\quad(i\in Y).$$
Only $k>m$ will occur in the inverse sum. Empty products equal one.
The factor $B_k^0=1$, including $B_k=0$, counts an empty tuple of choices.

## Proof strategy and dependency map

1. Remainders preserve old zero coordinates. An unchanged support count
   after a step forces the output to be fixed. Induction gives the
   support deadline.
2. Equality in that deadline forces support to fall by exactly one at
   each step. The first remainder vector must contain every positive
   residue once. This gives the exact joint box deadline and all its
   attaining sources.
3. For a target, fix the original support count and select which old
   zero-target coordinates were positive. Independent bounded quotient
   choices give every source exactly once.
4. Keep the quotient vector while changing its multiplier from the
   old support count to the quotient's support count. This injects each
   target fibre into the zero fibre. A missing single-coordinate source
   makes the comparison strict.

Steps 3–4 do not use the clock proof or its equality sources.
Steps 1–2 do not use any inverse count. Logical separation is not a
claim of separate research value.

## Proof

### Step 1. Closure, fixed points and recurrence

For every positive integer $k$ and nonnegative integer $a$,
$0\le a\bmod k\le a$. Therefore (1) maps $X_{n,M}$ to itself,
preserves every old zero, and never increases any coordinate.

Suppose $k(x)=k>0$. Then $F(x)=x$ precisely when every positive entry of
$x$ is smaller than $k$:
$$F(x)=x\quad\Longleftrightarrow\quad \max_i x_i<k. \tag{2}$$
Indeed values smaller than $k$ are unchanged by remainder, whereas a
value at least $k$ strictly decreases. The zero vector is fixed by
definition.

If $y=F(x)$ and $k(y)=k(x)=k>0$, every positive entry of $y$ lies in
$\{1,\ldots,k-1\}$, so (2) makes $y$ fixed. Consequently before the
last nonfixed step every support count strictly decreases. This proves
finite termination and rules out cycles of length greater than one.

The complete recurrent set is therefore exactly (2) together with zero.
Its size, as a static check on conventions, is
$$
1+\sum_{k=1}^n\binom nk\,\min(M,k-1)^k .
\tag{3}
$$
Choose its positive labels and then choose each positive value in
$\{1,\ldots,\min(M,k-1)\}$. This elementary fixed census is not a
third contribution axis.

### Step 2. Statewise support deadline

We prove $h(x)\le k(x)$ by induction on $k(x)$.
At $k(x)=0$ the state is fixed. At $k(x)=1$ it maps to zero in one step,
so $h(x)=1$.

For $k=k(x)\ge2$, a fixed state has height zero. For a nonfixed state,
put $y=F(x)$ and $\ell=k(y)$.
If $\ell=k$, Step 1 makes $y$ fixed and $h(x)=1\le k$.
If $\ell<k$, induction gives
$$h(x)=1+h(y)\le1+\ell\le k. \tag{4}$$
Thus the bound holds for every state.

If $k(x)>M$, each positive entry is at most $M<k(x)$, so $x$ is already
fixed. Any positive-height state consequently has $k(x)\le M$ as well
as $k(x)\le n$. Equation (4) gives
$$H(n,M)\le \min(n,M). \tag{5}$$

### Step 3. Every state attaining its support deadline

For $k(x)=k>0$, the following are equivalent:
$$
h(x)=k
\quad\Longleftrightarrow\quad
\{x_i\bmod k:i\in K(x)\}
 \text{ is the multiset }\{0,1,\ldots,k-1\}.
\tag{6}
$$
The statement is about multiplicities, not only the set of residues.

For $k=1$, both conditions hold for every positive source: its sole
residue is zero and its height is one.

Assume the equivalence established for smaller positive support.
If $h(x)=k\ge2$, the unchanged-support case in Step 2 is impossible.
Equality in (4) forces $\ell=k-1$ and $h(y)=k-1$.
By induction the positive entries of $y$ form a complete residue system
modulo $k-1$. They are also in $\{1,\ldots,k-1\}$, because $y=F(x)$.
There is only one representative of each residue modulo $k-1$ in that
interval: the zero residue is represented by $k-1$, and each positive
residue by itself. Thus $y$ has positive multiset
$\{1,\ldots,k-1\}$, while exactly one formerly positive coordinate
became zero. This is the right side of (6).

Conversely, that residue multiset gives an output with positive entries
$\{1,\ldots,k-1\}$. Repeated use of (1) successively removes the current
largest value:
$$
\{1,\ldots,k-1\}\longmapsto
\{1,\ldots,k-2\}\longmapsto\cdots
\longmapsto\{1\}\longmapsto\varnothing .
\tag{7}
$$
The coordinate labels stay fixed throughout; the displayed multisets
only describe their positive values. Each step in (7) changes the
state. Hence the output height is $k-1$ and $h(x)=k$.
This completes the induction.

### Step 4. Sharp joint deadline and all global equality sources

Put $H=\min(n,M)$. If $M=0$, the carrier is the singleton zero vector
and $H(n,0)=0$. Now suppose $M\ge1$, so $H\ge1$.

Choose $H$ coordinate labels and place $1,\ldots,H$ on them.
All other coordinates are zero. Its support is $H$ and its residues
modulo $H$ are complete, so (6) gives height $H$. Together with (5),
$$\boxed{H(n,M)=\min(n,M).} \tag{8}$$

Every source of height $H$ has support exactly $H$.
If $H=n$ this follows from $h(x)\le k(x)\le n$.
If $H=M<n$, a support larger than $H=M$ is fixed, while a support
smaller than $H$ has insufficient height. Thus (6) is also the complete
global equality classification.

Write $M=qH+r$ with $q\ge1$ and $0\le r<H$. Among positive values at
most $M$, the zero residue modulo $H$ has $q$ representatives; residues
$1,\ldots,r$ have $q+1$ each; the other residues have $q$ each.
The exact number of global height maximizers is therefore
$$
\boxed{\frac{n!}{(n-H)!}\,q^{H-r}(q+1)^r.}
\tag{9}
$$
Choose the $H$ labels, assign the $H$ distinct residues bijectively to
those labels, and choose one positive representative of each.
For $M=0$ the unique state is the unique height maximizer instead;
division by $H=0$ is never used. For $n=1$ and $M\ge1$, (8)–(9) give
height one and $M$ maximizers, namely every positive scalar.

### Step 5. Every-target inverse decoder and fibre formula

The zero source contributes exactly $\mathbf1_{\{y=0^n\}}$.
Every other source has a unique positive support count $k$.
Since its remainders lie below $k$, its target must satisfy $k>m$,
and preservation of zero coordinates gives $k\ge s$.

Fix an integer
$$\max(1,s,m+1)\le k\le n.$$
Choose a subset $J\subseteq[n]\setminus Y$ of size $k-s$.
Its elements are precisely the positive source coordinates whose
target is zero. Then choose source values as follows:
$$
\begin{array}{ll}
i\in Y:& x_i=y_i+kq_i,\quad
       0\le q_i\le\lfloor(M-y_i)/k\rfloor,\\
i\in J:& x_i=kq_i,\quad1\le q_i\le B_k,\\
i\notin Y\cup J:&x_i=0 .
\end{array}
\tag{10}
$$
Every such choice lies in the box, has exactly $k$ positive entries,
and reduces to $y$ under (1). Conversely any nonzero preimage gives
exactly this $k$, the set $J$, and its coordinate quotients.
Thus the construction is exhaustive and disjoint, including across
different $k$.

Counting its independent choices gives
$$
\boxed{
|F^{-1}(y)|=
\mathbf1_{\{y=0^n\}}+
\sum_{k=\max(1,s,m+1)}^n
 \binom{n-s}{k-s}B_k^{\,k-s}
 \prod_{i\in Y}A_i(k).
}
\tag{11}
$$
An empty sum is zero. At $k=s$ there are no positive zero-target
coordinates to choose, so the factor $B_k^0=1$ is necessary even
when $k>M$. Such a term is the fixed source $x=y$ when its entries
are below $s$ and $M< s$; it must not be dropped by an unjustified
global cutoff $k\le M$.

In particular
$$
\boxed{
|F^{-1}(0^n)|=
1+\sum_{k=1}^n\binom nk\lfloor M/k\rfloor^k .
}
\tag{12}
$$
Terms with $k>M$ vanish, but no such truncation is needed.

### Step 6. Exact image criterion

Let $B=\min(n,M)$. Zero is in the image. For every nonzero $y$,
$$
\boxed{
y\in F(X_{n,M})
\quad\Longleftrightarrow\quad
m<s\ \text{or}\ m<B .
}
\tag{13}
$$

For necessity, take a source counted by (10).
If $k=s$, then $m<k=s$.
If $k>s$, at least one coordinate in $J$ is a positive multiple
of $k$ bounded by $M$, so $k\le M$. Along with $k\le n$ and
$m<k$, this gives $m<B$.

For sufficiency, if $m<s$, equation (2) makes $y$ its own source.
Otherwise $m\ge s$ and $m<B$. Set $k=m+1$.
Then $s<k\le\min(n,M)$. Keep each positive target entry unchanged,
choose any $k-s$ of the remaining labels and put the value $k$ on
them, and put zero elsewhere. This is an explicit source in (10).
These two cases prove (13), including empty fibres.

### Step 7. Cross-modulus quotient injection

Fix a nonzero target $y$ and a source $x\in F^{-1}(y)$.
Let $k=k(x)$ and set
$$q_i=\lfloor x_i/k\rfloor,\qquad x_i=y_i+kq_i.$$
Let $\ell=|\{i:q_i>0\}|\le k$, and define
$$\Phi_y(x)=z,\qquad
 z_i=\begin{cases}\ell q_i,&\ell>0,\\0,&\ell=0.\end{cases}
\tag{14}$$
If $\ell>0$, the support of $z$ has size $\ell$ and every positive
entry is a multiple of $\ell$, hence $F(z)=0^n$.
Also
$$0\le z_i=\ell q_i\le kq_i\le x_i\le M.$$
If $\ell=0$, the same conclusions hold because $z=0^n$.
Thus (14) sends the fibre over $y$ into the fibre over zero.

It is injective. Recover $\ell$ as the support size of $z$.
For $\ell>0$, recover $q_i=z_i/\ell$; for $\ell=0$ recover $q=0^n$.
Every coordinate of $Y$ was positive in $x$, and a coordinate outside
$Y$ was positive precisely when its quotient is positive. Therefore
the original support count is recovered as
$$k=s+|\{i\notin Y:q_i>0\}|.$$
Finally recover each $x_i=y_i+kq_i$. A fixed target with zero quotient
is included in this reconstruction; its $k=s$ is not lost.
This proves injectivity without the clock theorem or fibre formula.

### Step 8. Strictness and unique maximizing target

A nonzero target requires $M\ge1$. Choose any label $j\in Y$ and
consider $z=M e_j$, where $e_j$ is the $j$-th coordinate unit vector.
It has singleton support, so $F(z)=0^n$.

If this $z$ lay in the image of (14), its quotient vector would be
$q=M e_j$ and the recovered old support count would be $k=s$.
The recovered source coordinate would then be
$$x_j=y_j+sM>M,$$
contradicting the box bound. Thus this particular zero-predecessor is
missing from the injection's image. Since both fibres are finite,
$$|F^{-1}(y)|<|F^{-1}(0^n)|\qquad(y\ne0^n). \tag{15}$$
For $M=0$, zero is the sole target and is therefore the unique
maximizer as well. Equation (12) evaluates the unique maximum in
every case. No exception is needed at $n=1$: all scalars map to zero.

## Corrections, boundaries and proof audit

No corrective change of the initial literal or of the stated theorems was
needed during this desk. No finite test, enumeration, symbolic software
evaluation, author verifier or new runtime was executed. The proofs above
are author deductions only. The examples below are hand deductions from
the definitions, not observed pilot data.

At $n=2,M=1$, this rule fixes exactly $(0,0)$ and $(1,1)$.
The actually inspected old SPR rule fixes exactly
$(0,0),(1,0),(0,1)$, because it protects support at most one and maps
$(1,1)$ to zero. Different fixed-point counts rule out a conjugacy
between those two maps on that same parameter box. This does not prove
global novelty or exclude every possible old parameter transformation.

The temporal quantity is entrance into the fixed set, not universal
extinction at zero: positive fixed vectors in (2) generally exist.
Formula (11) permits empty fibres and retains the $k=s>M$ identity term.
Formula (9) does not use division at $H=0$.
The injection changes the multiplier but preserves quotients; it does
not assert that the two dynamical maps are conjugate.

## Open risks and author value disposition

There is no identified open algebraic gap in (1)–(15), but no independent
review or scientific pressure test has occurred. All statements remain
subject to root original-evidence reception.

The deadline is a support budget with an immediate fixed output whenever
that budget does not decrease. Its equality pattern is the complete
residue staircase exposed by equality in that same budget. It does not
supply a separate survivor geometry or a nontrivial recurrent phase.
The inverse decoder is a one-parameter occupancy/product count.
The quotient compression in (14) is more specific than simply holding a
pivot fixed, but is still a bounded monotone quotient injection; the
actual CPRM proof already uses quotient-preserving lowering to compare
all targets with an extremal target, and the actual SPR gate rejects
unadorned quotient/occupancy inverses as a second contribution.

Accordingly this is **NO_PROMOTION_VALUE** at the author design desk.
It is not a mathematical impossibility claim, an independent gate,
or a statement that the new literal is an exact old SPR/CPRM slice.
A broader source/priority determination is not complete. No second
literal or experimental extension is justified merely to fill the cap.
