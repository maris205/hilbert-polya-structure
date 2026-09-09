# The excluded unicritical congruence: a Hasse-carry proof

2026-09-10 UTC. Same PC424-L continuation; current-team author proof.
The accepted R4 proof and every earlier artifact remain unchanged.

## Claim

Let $p$ be an odd prime, $k=\overline{\mathbf F}_p$, and let
$d\ge2$ satisfy $d\equiv1\pmod p$. For every $c\in k$, put

$$f(x)=x^d+c,\qquad \Delta Q=Q\circ f-Q,\qquad
B_f=\Delta k[x].$$

For each ordinary primitive $f$-orbit $O$, count every distinct point
once and put $S_h(O)=\sum_{a\in O}h(a)$. Then

$$K_f:=\{h\in k[x]:S_h(O)=0\text{ for every }O\}=B_f.\tag{T1}$$

There is also an exact finite certificate. Write

$$P=p^{v_p(d-1)},\qquad A=(d-1)/P,\qquad
\alpha=[A]\in k^\times.$$

For an integer $M\ge1$, define

$$m=\lfloor\log_d(PM)\rfloor,\qquad
n_M=7m+22,\qquad F_j=f^{\circ j}-x,\qquad
\widetilde H_j(h)=\sum_{i=0}^{j-1}h\circ f^{\circ i}.$$

Here $D^{[P]}$ denotes the $P$th Hasse derivative, namely the
coefficient of $z^P$ in a polynomial evaluated at $x+z$. For every
$h\in k[x]$ of degree at most $M$, including zero, the following
conditions are equivalent:

1. $h\in B_f$.
2. $F_j\mid D^{[P]}F_j\,\widetilde H_j(h)^P$ for both
   $j=n_M,n_M+1$.
3. $\widetilde H_j(h)$ vanishes at every ordinary root of $F_j$
   for both $j=n_M,n_M+1$.

Consequently a noncoboundary of degree at most $M$ has a detecting
ordinary primitive period at most $7\lfloor\log_d(PM)\rfloor+23$.
The two fixed polynomials have degree at most $d^{23}(PM)^7$.
This is an exact degree bound, not an optimized running-time claim.

## Status, assumptions, and source boundary

**PROVABLE AS STATED — author proof complete; nonauthor review pending.**

All parameters of the allocated excluded-congruence question are
retained. The native time step is one application of $f$. No assumption
about ordinary root multiplicities, prime-to-$p$ cycle lengths, or a
special value of $c$ is used. In particular, the proof does not invoke
a characteristic-zero bound on multiplier-one cycles.

The [accepted R4 package](../../continuation_round4/a2_unicritical_carry_extension/PROOF_PACKAGE.md)
supplies the polynomial normal form, full cyclic digit basis, and the
already recorded failure of the ordinary Jacobian test. Its carry proof
does not cover the present congruence class. The new mechanism below is
an explicit Hasse derivative with one marked transition, together with
a different target digit string and insertion identity. It is not a
new paper slot or a worldwide-priority assertion. All algebraic
identities used in this package are proved here or stated as the
accepted R4 normal-form input; no newly searched theorem is imported.

## Dependency map

1. The accepted degree-$d$ normal form reduces the question to a
   polynomial with leading exponent not divisible by $d$.
2. Hasse differentiation yields a necessary ordinary-root certificate
   regardless of multiplicity.
3. The first non-linear Taylor term of $f$ has degree $P$. The
   $P$th derivative of an iterate is a sum of marked background products.
4. A long $d-1$ digit block and a later zero block localize every
   source of an observable. An adaptive cut handles every wraparound.
5. Inserting one $d-1$ digit pairs the existing marked paths. The
   newly inserted mark contributes exactly $\alpha a_D^P$.
6. Two necessary Hasse certificates contradict that nonzero difference.
   Constants are excluded separately, yielding the finite certificate
   and the ordinary primitive-orbit theorem.

## Proof

### 1. Normal form and the full periodic algebra

Set

$$V_d=k\oplus\bigoplus_{\substack{r\ge1\\d\nmid r}}kx^r.$$

The R4 triangular argument gives

$$k[x]=B_f\oplus V_d,\qquad
h=\Delta Q+v,\quad v\in V_d,\quad\deg v\le\deg h.\tag{1}$$

For completeness, $\Delta x^t$ is monic of degree $dt$ for $t\ge1$.
Successively eliminating positive exponents divisible by $d$ terminates
without raising degree. A nonconstant $Q$ has
$\deg\Delta Q=d\deg Q$, whereas the positive leading exponent of
a nonzero element of $V_d$ is not divisible by $d$. Constants cannot
be nonzero coboundaries either. This proves both existence and
uniqueness of the normal part. Telescoping proves $B_f\subseteq K_f$.

For $n\ge1$, define

$$\mathcal A_n=k[X_0,\ldots,X_{n-1}]/
(X_i^d+c-X_{i+1}:i\bmod n).$$

Elimination identifies $\mathcal A_n$ with $k[x]/(F_n)$ by
$X_i\mapsto f^{\circ i}(x)$. Its dimension is $d^n$. The monomials

$$X^{\mathbf e}=\prod_{i=0}^{n-1}X_i^{e_i},\qquad 0\le e_i<d,
\tag{2}$$

are a basis: replacing $X_i^d$ by $X_{i+1}-c$ strictly decreases
total degree in each resulting term, so these $d^n$ monomials span.
Their number equals the dimension. This argument uses the full
possibly nonreduced algebra.

Write $H_n(w)=\sum_i w(X_i)$. Telescoping gives

$$H_n(\Delta Q)=0\quad\text{in }\mathcal A_n.\tag{3}$$

Since $\gcd(d,P)=1$, $d\nmid r$ implies $d\nmid Pr$.
Moreover, in characteristic $p$,

$$H_n(v)^P=H_n(v^P).\tag{4}$$

### 2. A multiplicity-safe Hasse certificate

Let $G,H\in k[x]$, with $G\ne0$, and suppose $H$ vanishes
at every ordinary root of $G$. For every integer $E\ge1$,

$$G\mid D^{[E]}G\,H^E.\tag{5}$$

Indeed, if $a$ has multiplicity $e$ in $G$, the Hasse product rule
applied to $G=(x-a)^eU$ shows that $D^{[E]}G$ has order at
least $\max(e-E,0)$ at $a$. The factor $H^E$ has order at
least $E$. Their product therefore has order at least $e$.
Factoring $G$ over $k$ proves (5), including when some Hasse
coefficients vanish or the derivative is zero.

For $h\in K_f$, any root of $F_n$ has primitive period $r\mid n$,
and $\widetilde H_n(h)(a)=(n/r)S_h(O_a)=0$. Thus (5) with
$E=P$ gives, for every $n$,

$$F_n\mid D^{[P]}F_n\,\widetilde H_n(h)^P.\tag{6}$$

No division by a cycle length occurs. In the later finite-certificate
argument, (6) is simply assumed at the two specified levels.

### 3. The exact marked-background formula

The integer $P$ satisfies $3\le P<d$, and
$\alpha=[(d-1)/P]\ne0$. Expanding

$$f(x+z)=(x+z)(x^P+z^P)^A+c$$

shows that there are no Taylor terms of degrees $2,\ldots,P-1$,
and that

$$f'(x)=x^{d-1},\qquad D^{[P]}f(x)=\alpha x^{d-P}.\tag{7}$$

These absent intermediate terms remain absent under composition.
If $g(x+z)=g(x)+a(x)z+b(x)z^P+O(z^{P+1})$, the coefficient
of $z^P$ in $f(g(x+z))$ is
$f'(g(x))b(x)+D^{[P]}f(g(x))a(x)^P$.
Induction therefore gives the following identity in $\mathcal A_n$:

$$J_n:=[D^{[P]}F_n]=\alpha\sum_{j=0}^{n-1}B_{n,j},\tag{8}$$

where

$$B_{n,j}=
\left(\prod_{a<j}X_a^{P(d-1)}\right)
X_j^{d-P}
\left(\prod_{a>j}X_a^{d-1}\right).\tag{9}$$

The term $-x$ has zero $P$th Hasse derivative because $P>1$.
The integer $j$ is the marked site. The background exponents are

$$b_a(j)=
\begin{cases}
P(d-1),&a<j,\\
d-P,&a=j,\\
d-1,&a>j.
\end{cases}\tag{10}$$

### 4. The target and the exact reduction paths

Fix $M\ge1$ and a normal polynomial $v\in V_d$ with positive
leading degree $D\le M$ and leading coefficient $a_D\ne0$.
For the rest of the coefficient argument set

$$m=\lfloor\log_d(PM)\rfloor,\qquad L=m+2.$$

Allow integers $s,n$ satisfying

$$s\ge4L+4,\qquad n\ge s+3L+4.\tag{11}$$

Let $T_{n,s,D}$ be the digit-basis monomial whose digits are:

- $d-P+1$ at site $0$;
- $d-1$ at sites $1,\ldots,s-1$;
- the base-$d$ digits of $PD-1$, padded through $m+1$ digits,
  at sites $s,\ldots,s+m$;
- zero at every later site.

All digits lie in $[0,d-1]$. The first digit after the long block
satisfies

$$e_s=(PD-1)\bmod d\le d-2,\tag{12}$$

because $d\nmid PD$. The target is equivalently the digit
monomial of the integer $PDd^s-P+1$, not an assertion that its
univariate representative in $k[x]/(F_n)$ is a pure power when
$c\ne0$.

We expand $B_{n,j}X_i^{Pr}$, where $1\le r\le D$, by the
relations $X_a^d=X_{a+1}-c$. Call $i$ the source. At a processed
site with incoming carry $t_a$, its exponent is
$b_a+t_a+Pr\mathbf 1_{a=i}$. Put

$$q_a=\left\lfloor\frac{b_a+t_a+Pr\mathbf1_{a=i}}d\right\rfloor,
\qquad e_a=(b_a+t_a+Pr\mathbf1_{a=i})\bmod d.$$

The expansion chooses $0\le t_{a+1}\le q_a$ and has weight

$$\binom{q_a}{t_{a+1}}(-c)^{q_a-t_{a+1}}.\tag{13}$$

Thus, on a legal closed circuit, with
$\kappa_a=q_a-t_{a+1}\ge0$,

$$e_a=b_a+t_a+Pr\mathbf1_{a=i}-dt_{a+1}-d\kappa_a.\tag{14}$$

Weights, including zero weights, are retained. The ensuing bounds
are inequalities for integer carries and exponents, not scalar
equalities modulo $p$.

### 5. Adaptive cuts and complete wraparound control

To justify the closed-circuit description before any source has been
localized, choose a cut $a\in[1,s-1]$ different from the source,
whose forward cyclic distance from the source is at least $L$.
Process the $n$ sites once in cyclic order starting at $a$.
At the cut first process its background without any incoming carry;
the carry from the last processed site is added to its retained digit
at the end.

Before processing the unique source, every incoming carry is at most
$P-1$. This follows from $b_u\le P(d-1)$ and from starting with
zero incoming carry. After $h\ge1$ steps from the source, the
carry satisfies

$$t\le P+\frac{Pr-1}{d^h}.\tag{15}$$

At the source its incoming carry was at most $P-1$, and each
subsequent nonsource step is bounded by
$t_{\rm next}\le(P(d-1)+t)/d$; these facts prove (15) by
induction. Since $d^{L-1}=d^{m+1}>PM-1$, the carry is at
most $P$ after $L-1$ steps and remains at most $P$ thereafter.

At the cut, its retained digit from the first processing is $d-P$
if it is a prefix or marked site, and $d-1$ if it is a suffix site.
The final incoming carry is at most $P$. If the cut is a suffix
site, the preceding site is a suffix or the marked site; its incoming
carry was at most $P$ and it was not the source. Its outgoing
carry is consequently at most one. Thus the final exponent at the
cut is at most $d$ in every case.

If this exponent is less than $d$, the first circuit already gives
a digit monomial. If it equals $d$, reducing the cut once leaves
its digit zero and sends a carry zero or one to the next site. All
other sites already have digits below $d$. A carry one can continue
only through a site currently having digit $d-1$, leaving zero
there. It either stops or makes one complete additional circuit;
on returning to the cut, it raises its zero digit to at most one
and stops. Every such branch has final cut digit at most one.

The desired cut digit is $d-1\ge3$. Therefore no overflowing
branch contributes the target. Every contributing branch is already
legal after one circuit. At its cut, adding the final incoming carry
does not change the initial quotient $q_a$, since the retained digit
plus this carry is still below $d$. Its initial binomial weight is
therefore exactly (13) with the final incoming carry included.
Consequently every target-producing branch gives the genuine cyclic
identities (13)--(14) at every site, including the cut.

Conversely, a cyclic path producing the target with this cut and
these legal quotients is recovered by the same one-circuit expansion;
the cut's quotient is the initial quotient. Hence no contributing
path or weight is lost by this description. This argument is about
individual expansion branches and does not assume coefficients avoid
cancellation.

### 6. Localization of every source

For a fixed marked site $j$ define the low-block baseline

$$\ell_a=
\begin{cases}P-1,&a\le j,\\0,&a>j.\end{cases}$$

At every site $a<n-1$ the background identity is

$$b_a+\ell_a=(d-1)+d\ell_{a+1}.\tag{16}$$

For a cyclic path put $u_a=t_a-\ell_a$. Equation (14) gives,
away from the last site,

$$e_a=d-1+u_a+Pr\mathbf1_{a=i}-du_{a+1}-d\kappa_a.\tag{17}$$

If there is no source at $a$ and $u_a\le0$, then
$du_{a+1}\le d-1$, since $e_a,\kappa_a\ge0$. The integer
$u_{a+1}$ is thus at most zero. Nonpositive excess cannot become
positive without passing the source.

At a nonsource site with incoming carry between zero and $P$, a
target digit $d-1$ forces $t_a=\ell_a$. This follows directly
by reducing each of the three backgrounds (10) modulo $d$ and
using $P<d$. A zero digit instead requires
$t_a=\ell_a+1$. In particular it is impossible if $u_a\le0$.

Put $b=s+m+1$, a zero target site. We claim that every contributing
source lies in

$$I_{n,s}=\{s-L,s-L+1,\ldots,b\}.\tag{18}$$

If $i\le s-L-1$, choose the adaptive cut $a=i+L$.
It belongs to $[1,s-1]$ and lies $L$ forward steps from $i$.
Section 5 applies. Its incoming carry is at most $P$ and its
target digit is $d-1$, so $u_a=0$. No source occurs in the
ordinary index interval $[a,b]$. Equation (17) keeps the excess
nonpositive up to $b$, contradicting its zero target digit.

If $i\ge b+1$, choose the cut $a=L$. Its forward cyclic
distance from $i$ is $n-i+L\ge L+1$, and it is a nonsource
site of the long block. The same argument starts with $u_a=0$
and reaches the zero site $b$ before the source, again a
contradiction. These two cases prove (18).

There is also no target contribution from $B_{n,j}$ without a
source. Use the cut $a=L$. The no-source carries satisfy the
same bounds, the overflowing-cut alternatives are excluded as
before, and $u_a=0$ cannot become positive before $b$.
Consequently constant terms of $v^P$ contribute zero to the
coefficient under study, regardless of the scalar $n$ in their trace.

### 7. A common cut for all remaining paths

Every source in (18) is positive, and

$$n-i\ge n-b\ge2L+5.$$

We may now process all contributing terms in the fixed order
$0,1,\ldots,n-1$. Site zero is not a source. Its retained first
digit is $d-P$, whether it is the marked site or a prefix site.
By (15), the final carry from site $n-1$ is at most one:
the source was sufficiently far back, and the last site is either
a suffix or the mark. Therefore the final exponent at site zero
is at most $d-P+1<d$. No second circuit occurs.

Producing the target forces the final carry to be exactly one.
Thus all contributing paths have the closed-circuit convention

$$t_0=t_n=1.\tag{19}$$

At site zero this convention gives the same quotient and binomial
weight as initially processing the background without an incoming
carry, because $d-P+1<d$. All paths and all weights are consequently
described by (13)--(14) with this one fixed cut. Before the source,
the carries after site zero are at most $P-1$.

### 8. Insertion pairs all existing marked paths

Define

$$C(n,s)=[T_{n,s,D}]\bigl(J_nH_n(v^P)\bigr).$$

Insert a new site at index $a=2L$, sending old indices through

$$\iota(u)=\begin{cases}u,&u<a,\\u+1,&u\ge a.\end{cases}$$

The new parameters are $(n+1,s+1)$, with the same $m,L,D$.
The target inserts a digit $d-1$ at $a$ and otherwise preserves
all old digits. Conditions (11) remain true. The source intervals
(18) are carried to one another by $\iota$, since their lower
endpoint $s-L\ge3L+4$ exceeds $a+1$. No source can occur
at the inserted site or either of its immediate neighbors.

First consider an old marked site $j$, mapped to $\iota(j)$.
At the insertion position, the target digit is $d-1$, the source
has not yet occurred, and the incoming carry is bounded by $P-1$.
It is therefore the low baseline: $P-1$ if the mark is ahead,
and zero if the mark is behind.

Insert a nonsource, unmarked site with the same baseline incoming
and outgoing carry. If the mark is ahead, its background is
$P(d-1)$, quotient $P-1$, and retained digit $d-1$.
If the mark is behind, its background is $d-1$, quotient zero,
and retained digit $d-1$. In both cases its weight is one.
Every old transition, source, and digit is otherwise unchanged.
The fixed-cut condition (19) is preserved.

Conversely, take a target-producing level-$(n+1)$ path whose mark
is not the inserted site. The inserted site and its successor are
both nonsources with target digit $d-1$, and the source is still
ahead. Their incoming carries are their respective low baselines.
Since the mark is not the inserted site, those two baselines are
equal. The transition at the inserted site therefore has weight
one and can be deleted. This recovers an old path. These operations
are mutual inverses, including when the mark is immediately before
or after the inserted site. They preserve the complete digit vector,
not only its support.

It follows that $C(n+1,s+1)-C(n,s)$ consists exactly of the
contributions whose mark is the new site $a$.

### 9. The new marked site isolates the leading coefficient

Write $N=n+1$, $S=s+1$ for this paragraph, and put the mark
at $a=2L$. Every possible source lies strictly after $a+1$ by
Section 6. At the mark the incoming carry is $P-1$, its exponent
is $(d-P)+(P-1)=d-1$, and its quotient is zero. Its outgoing
carry is thus zero and its weight is one.

All sites from the mark to the source have suffix background $d-1$.
Starting with carry zero, each nonsource has output digit $d-1$
and outgoing carry zero. Equation (12) now forces the source
index to satisfy $i\le S$; otherwise the smaller target digit
at $S$ would occur before any source.

The source term is $X_i^{Pr}$, $1\le r\le D$, and its
incoming carry is zero. Sum (14), multiplied by $d^{u-i}$,
over suffix sites $u=i,\ldots,N-1$. All backgrounds here are
$d-1$, and (19) gives the final carry one. We obtain the exact
integer identity

$$\sum_{u=i}^{N-1}e_ud^{u-i}
=Pr-1-\sum_{u=i}^{N-1}\kappa_ud^{u-i+1}.\tag{20}$$

For the specified target and $i\le S$, the left side is
$PDd^{S-i}-1$. Thus

$$Pr=PDd^{S-i}+\sum_{u=i}^{N-1}\kappa_ud^{u-i+1}.\tag{21}$$

All terms in the last sum are nonnegative integers. Because
$r\le D$ and $i\le S$, equality is possible only when
$i=S$, $r=D$, and every $\kappa_u=0$. The earlier long-block
sites also have their forced baseline transitions and weight one.
The remaining path exists: ordinary division of $PD-1$ in base
$d$ gives exactly the specified digits at $S,\ldots,S+m$,
after which the suffix carry is one. All its binomial weights
are one, since the outgoing carry equals the quotient at each
step. It is unique.

Including the scalar $\alpha$ from (8) and the coefficient
$a_D^P$ from $v^P$, Sections 8--9 prove

$$C(n+1,s+1)-C(n,s)=\alpha a_D^P\ne0.\tag{22}$$

This is the marked Hasse-carry identity. It does not require any
condition on $c$, and it has treated all marks, all sources,
constant branches, and wraparound branches.

### 10. The full theorem and the finite certificate

Fix $M$ and take $L=m+2$, $s=4L+4$, and
$n=s+3L+4=7m+22=n_M$. Suppose condition 2 in the Claim holds.
Replacing $h$ by its normal part $v$ preserves that condition,
by (3)--(4). In $\mathcal A_j$ the two conditions become

$$J_jH_j(v^P)=0,\qquad j=n,n+1.\tag{23}$$

If $v$ has positive leading degree $D$, both coefficients in
(22) are zero by (23), contradicting $\alpha a_D^P\ne0$.
Hence $v=a_0$ is constant.

At least one of $n,n+1$, say $j$, is not divisible by $p$.
The leading term in the univariate formula (8) is
$j\alpha x^{d^j-P}$: every marked term has that degree and
leading coefficient one, either by (7) and composition or by
summing its geometric-series exponents in (9). Thus
$D^{[P]}F_j\ne0$ and has degree less than $\deg F_j$.
For constant $v$, the divisibility condition is

$$F_j\mid ja_0^P D^{[P]}F_j.$$

Since $j\ne0$ in $k$, it forces $a_0=0$. Therefore condition
2 implies $h\in B_f$.

If $h=\Delta Q$, telescoping makes $\widetilde H_j(h)$
divisible by $F_j$ for every $j$, proving both conditions 2 and
3. Condition 3 implies 2 by (5). This proves all three finite
conditions equivalent. For $h\in K_f$, equation (6) supplies
condition 2 at the two required levels, proving (T1).

Finally, if $h\notin B_f$, condition 3 fails at a root $a$ of
one of $F_n,F_{n+1}$. If its primitive period is $r\mid j$,
then $\widetilde H_j(h)(a)=(j/r)S_h(O_a)\ne0$, so its
ordinary primitive sum is nonzero. This proves the period bound.
The degree estimate follows from

$$\deg F_j\le d^{n+1}=d^{7m+23}\le d^{23}(PM)^7.$$

Therefore the full excluded-congruence claim, with every allocated
prime, degree, parameter, and polynomial, follows. $\square$

## Verification and open review risks

The proof is by exact hand expansions, integer inequalities, and
weight-preserving finite bijections. No mathematical program was run.
Nonauthor internal review remains pending. The principal audit points
are the adaptive-cut bound and overflowing-cut exclusion in Section 5,
the nonpositive-excess localization in Section 6, and preservation of
all marked paths in Section 8. The statement does not depend on an
unproved global multiplicity estimate or on a fixed-point example.
The source-free monomial check is recorded separately in the report;
it is not being substituted for this all-$c$ proof.
