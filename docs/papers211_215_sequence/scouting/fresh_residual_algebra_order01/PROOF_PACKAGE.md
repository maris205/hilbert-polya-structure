# Proof package — two rejected Laver-table desk literals

## Claim and status

The requested two-axis admission claim is `NOT CURRENTLY JUSTIFIED` for
either map. The limited propositions below are `PROVABLE AS STATED`, using
the explicit standard Laver-table facts listed next. They are deductions
for subtraction, not claims of novel Laver-table structure.

## Assumptions and notation

Fix $n\ge0$, put $N=2^n$, and let $A_n=\{1,\ldots,N\}$ with the classical
Laver operation $\triangleright_n$. The modular representative of zero is
always $N$. A theorem about $A_n$ is finite; no assertion about an infinite
limit or large cardinals is required.

The directly inspected basic properties are: left self-distributivity;
$p\triangleright_n1=p+1\pmod N$; row $N$ is the identity; the last column
is constant $N$; and a row $p$ has a power-of-two period $\pi_n(p)$ with
distinct increasing entries through its first occurrence of $N$.
For $p<N$ every entry is greater than $p$. Reduction modulo $2^m$ is an
operation homomorphism for $m\le n$. These are established background,
not new results of this desk; the source note gives exact locations.

Set $v_2(N)=n$ and use the ordinary integer valuation for $1\le x<N$.
For any finite map, the tail $h(x)$ is the least nonnegative iterate index
at which the orbit becomes recurrent. The two new desk definitions are

$$D_n:A_n\longrightarrow A_n,\qquad D_n(x)=x\triangleright_n x,$$

$$B_n:A_n^2\longrightarrow A_n^2,\qquad
B_n(a,b)=(a\triangleright_n b,a).$$

These carriers are total, finite and autonomous. The second definition is
an exact known positive-braid coloring rule, not an invented candidate.

## Strategy and dependency map

1. Row growth determines the recurrent set of each map.
2. The projective homomorphism plus a row-period bound gives a stronger,
   but not asserted sharp, diagonal clock.
3. Self-distributivity identifies the diagonal inverse question with an
   already-existing column multiplicity question.
4. For the pair map the output's second coordinate fixes the input's first;
   the first-coordinate equation is then exactly one row of the table.
5. These mechanisms do not produce two residual substantive axes.

## Proof 1: diagonal recurrence and a valuation bound

If $x<N$, row growth gives $D_n(x)>x$; while $D_n(N)=N$. Thus $N$ is the
only recurrent state, and every orbit reaches it. This already yields the
generic bound $h(x)\le N-x$.

For the stronger bound, take $x<N$ and $k=v_2(x)<n$. Reduce the operation
to $A_{k+1}$. The residue of $x$ is $p=2^k$. In that table the distinct
entries of row $p$ all lie in $\{p+1,\ldots,2^{k+1}\}$, a set of $2^k$
elements. Its period is therefore a power of two at most $2^k$, hence
divides $p$. The entry in column $p$ is consequently $2^{k+1}$, the zero
residue. The homomorphism property now gives

$$2^{k+1}\mid D_n(x).$$

Each nonterminal step raises the valuation by at least one. At valuation
$n$ the only element in the carrier is $N$. Therefore

$$h(x)\le n-v_2(x),\qquad D_n^n(x)=N\quad\hbox{for all }x\in A_n.$$

For $n=0$ the only state is already fixed and the bound is zero. For $n>0$
the argument makes no assertion that every step raises valuation by exactly
one. In particular, the primary table at $n=4$ has
$D_4(2)=12$ and $D_4(12)=16$: the valuation jumps from two to four on the
second step. Thus an exact pointwise equality with $n-v_2(x)$ is false.

## Proof 2: why the diagonal inverse is not solved

Let $s(p)=p+1\pmod N$ in the stated representatives. Self-distributivity
with the two right arguments equal to $1$ gives

$$p\triangleright_n2
=p\triangleright_n(1\triangleright_n1)
=(p\triangleright_n1)\triangleright_n(p\triangleright_n1)
=D_n(s(p)).$$

For $n=0$ interpret the displayed $2$ as its residue $1$; the identity
still holds. Since $s$ is a permutation, the target fibre of $D_n$ has
exactly the multiplicity of that target in the second column. This is a
change of the input variable, **not a conjugacy of the two dynamical maps**.
It supplies no evaluated all-target multiplicity formula by itself.

The condition $D_n(x)=N$ can also be written $\pi_n(x)\mid x$, because a
row first reaches $N$ precisely at its period. This still depends on the
table's full row-period data. The desk does not count that set uniformly
in $n$, identify the largest diagonal fibre, or classify every diagonal
target. Merely summing indicators of these conditions would restate the
inverse problem and is not admitted as a separate theorem axis.

## Proof 3: complete pair-map recurrent set

Let
$$R_n=\{(N,b):b\in A_n\}\cup\{(a,N):a\in A_n\}.$$
For every $b$, the known boundary row/column equations give

$$B_n(N,b)=(b,N),\qquad B_n(b,N)=(N,b).$$

Thus $(N,N)$ is fixed, and for each $b<N$ the two displayed states form
one two-cycle. These are $N-1$ distinct two-cycles and $2N-1$ recurrent
states in total.

If the state has not yet entered $R_n$, both coordinates are below $N$.
Writing its successive first coordinates as $a_t$, the update gives
$a_{t+1}=a_t\triangleright_n a_{t-1}>a_t$ whenever the current state is
interior. Therefore an orbit starting at $(a,b)$ in the interior reaches
$R_n$ within at most $N-a$ steps. It cannot contain an interior recurrent
state. This proves that the displayed boundary is exactly the recurrent
set, without a pilot or a sharp maximum-tail claim. For $n=0$ the same
description reduces to its one fixed state.

## Proof 4: pair-map fibres and unique maximum

For target $(u,v)$, the equation $B_n(a,b)=(u,v)$ first forces $a=v$;
the remaining condition is $v\triangleright_n b=u$. Let
$\operatorname{Row}_n(v)$ be the set of the $\pi_n(v)$ distinct values in
one row period. If $u$ is absent from that set, there is no predecessor.
If it is present, it occurs once per period and there are $N/\pi_n(v)$
periods across the $N$ input values. Hence

$$|B_n^{-1}(u,v)|=
\begin{cases}
N/\pi_n(v),&u\in\operatorname{Row}_n(v),\\
0,&u\notin\operatorname{Row}_n(v).
\end{cases}$$

For $n\ge1$, a fibre can have size $N$ only when $\pi_n(v)=1$. A constant
row must have value $N$, whereas its first value is $v+1$ if $v<N$.
Consequently $v=N-1$; conversely that row is indeed constant $N$.
The row $N$ has period $N>1$, so causes no additional equality case.
The unique maximizing target is therefore $(N,N-1)$ with fibre size $N$.
For $n=0$ the unique target $(1,1)$ has fibre size one instead.

The image size is $\sum_{v\in A_n}\pi_n(v)$, an exact expression in known
table data, not an evaluated all-$n$ image enumeration. This sum is not
advanced as another substantive axis.

## Subtraction and open risks

The row monotonicity, power-of-two periods and projective homomorphisms
are primary-source background. For $D_n$ they give a clean upper bound,
but a sharp full-carrier clock and separately evaluated all-target inverse
remain unproved. For $B_n$, the literal is directly published and both
deductions above are immediate uses of its table rows. A valid unique
inverse maximum does not restore residual temporal value.

No unrestricted shelf theorem is claimed: general shelves need not have
the Laver order or boundary laws. Nor is $B_n$ identified with the old
finite-group Hurwitz permutation: for $n\ge1$ it has an $N$-element fibre,
so it is not injective, unlike that group map. The shared coloring shell
receives no novelty credit. Both candidates close without promotion.
