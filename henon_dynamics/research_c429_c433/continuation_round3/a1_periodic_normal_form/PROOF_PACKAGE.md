# R3 A1: stabilized cyclic carry coefficients

2026-09-09 UTC. This is a continuation of the unchanged PC424-L question.
First-pass and Round-2 artifacts are read-only inputs. No mathematical
execution is allocated or has been run. The claim below records the new
coefficient mechanism identified during the hand investigation; it is not
a claim that an earlier freeze or independent check had already occurred.

## Claim

For every odd prime $p$, $k=\overline{\mathbb F}_p$, $c\in k$, and
$f(x)=x^2+c$, let $\Delta Q=Q\circ f-Q$ and

$$K_c=\left\{h\in k[x]:\sum_{a\in O}h(a)=0
\text{ for every ordinary primitive }f\text{-orbit }O\right\},
\qquad B_c=\Delta k[x].$$

The original claim is $K_c=B_c$, with a full defect classification
required if equality fails. Every primitive orbit point is counted once,
including periods divisible by $p$. No iterate is substituted for the
native one-step clock.

The new candidate coefficient lemma is the following. For an odd integer
$D\ge1$, put $m=\lfloor\log_2D\rfloor$ and let
$E_D\subseteq\{0,\ldots,m\}$ be its nonzero binary-digit positions.
In the full cyclic algebra

$$A_n=k[X_0,\ldots,X_{n-1}]/(X_i^2+c-X_{i+1}:i\bmod n),$$

write $P_E=\prod_{i\in E}X_i$, $P_{\rm all}=\prod_{i=0}^{n-1}X_i$,
and $H_n(v)=\sum_{i=0}^{n-1}v(X_i)$. The squarefree monomials $P_E$
are the imported basis. For
$v=a_0+\sum_{1\le d\le D,\ d\text{ odd}}a_dx^d$, define

$$C_n(v;E_D)=[P_{E_D}]\bigl(P_{\rm all}H_n(v)\bigr),$$

where the bracket extracts the coefficient in that basis. The precise
candidate stabilization statement is

$$C_{n+1}(v;E_D)=C_n(v;E_D)
\qquad\text{for every integer }n\ge3m+4. \tag{S}$$

The same target index set $E_D$ is used at both levels. This is an exact
equality in $k$, for every allowed $p,c,v$, not an asymptotic estimate.

## Status

**PROVABLE AS STATED — author proof complete, independent review pending.**
The proof below establishes (S) and derives the original unchanged claim.
This is an author proof claim, not independent acceptance, a completed
source-priority review, paper admission, or an evaluation.

## Source subtraction

- The [initial normal form](../../../research_c424_c428/positive_characteristic/PROOF_PACKAGE.md)
  gives $k[x]=B_c\oplus(k\oplus xk[x^2])$.
- The [old cyclic proof, Steps 1–2 and 5](../../../research_c424_c428/continuation_round2/positive_characteristic/PROOF_PACKAGE.md)
  already proves the squarefree basis, all-$c$ triangular detection
  $[P_{E_D}]H_n(v)=a_D$ for $n>2m$, and the implication from ordinary
  root vanishing to $(2^nP_{\rm all}-1)H_n(v)=0$ in $A_n$.
  None of these is a new result of this round. The Step-5 counterexample
  disproves a converse at one level, not the present adjacent-level
  coefficient mechanism.
- The [first-pass A1 report](../../lanes/a1_periodic_coboundary/REPORT.md)
  already treats $c=0$ using arbitrarily large squarefree levels.
  A new monomial-necklace proof or another all-$c$ full-scheme leading
  coefficient proof would duplicate those accepted inputs.
- The [E8-accepted dynamics algebra](../../continuation_round2/a1_frobenius_finiteness/PROOF_PACKAGE.md)
  is a different mechanism and is not re-proved here.

The new step is (S), proved by weighted carry paths in the existing
cyclic basis. Formal Böttcher coordinates motivated the investigation
but will not be evaluated at finite periodic points or used to discard
an uncontrolled infinite Laurent tail.

## Dependency map and cheap failure criterion

1. A single sequential circuit reduces $P_{\rm all}X_i^d$ for odd
   $d\le D$ to squarefree monomials: the final carry must be at most one.
2. A path producing the nonempty target $E_D\subseteq[0,m]$ must
   start at an index in $[-m,m+1]\pmod n$.
3. Inserting a zero site in the long complementary interval preserves
   all contributing paths, with transition weight exactly one.
4. This proves (S); the imported Jacobian and leading-coefficient
   identities at two consecutive periods then exclude every positive
   degree normal defect. Fixed points exclude a nonzero constant defect.

A failure of any path bound, index condition, final-carry condition or
insertion/deletion inverse invalidates (S) as presently argued. Merely
observing stabilization at finitely many levels would not prove it.

## Proof

### 1. Exact one-circuit reduction and its weights

In this section let $1\le d\le D$ be odd, put $L=m+1$, and suppose
$n\ge L$. Fix a source index $i\in\mathbb Z/n\mathbb Z$.
We give a complete weighted expansion of $P_{\rm all}X_i^d$ in the
imported squarefree basis, not in the reduced periodic-point algebra.

Start at $X_i$ and process the sites in the order
$i,i+1,\ldots,i+n-1$, once around the circle. The initial site has
exponent $d+1$, and every other site initially has exponent one.
Let $t_0=d$. At step $s\in\{0,\ldots,n-1\}$ the exponent at the
current site $X_{i+s}$ is $1+t_s$. Write

$$b_s=(1+t_s)\bmod 2,\qquad
r_s=\left\lfloor\frac{1+t_s}{2}\right\rfloor.
\tag{1}$$

Here $b_s$ is an integer in $\{0,1\}$. The defining relation gives
the exact polynomial identity

$$X_{i+s}^{\,1+t_s}
 =X_{i+s}^{\,b_s}(X_{i+s+1}-c)^{r_s}
 =\sum_{t_{s+1}=0}^{r_s}
   \binom{r_s}{t_{s+1}}(-c)^{r_s-t_{s+1}}
   X_{i+s}^{\,b_s}X_{i+s+1}^{\,t_{s+1}}.
\tag{2}$$

A path is any sequence $(t_0,\ldots,t_n)$ with $t_0=d$ and
$0\le t_{s+1}\le r_s$. Its weight is

$$w(t)=\prod_{s=0}^{n-1}
 \binom{r_s}{t_{s+1}}(-c)^{r_s-t_{s+1}}\in k.
\tag{3}$$

Integer binomial coefficients are mapped into $k$. Some weights may
be zero; the expansion includes those paths as well. All path sets
are finite.

For every path, induction using $t_{s+1}\le(1+t_s)/2$ proves

$$t_s\le1+\frac{d-1}{2^s}.
\tag{4}$$

Since $2^L>D-1$, equation (4) gives $t_L<2$, hence $t_L\le1$.
The states zero and one can never lead back to a larger state.
In particular, $t_n\le1$.

There is one cyclic-boundary point to check. At the initial site
$b_0=0$ because $d$ is odd. After processing the last site, its outgoing
factor $X_i^{t_n}$ therefore lands on an initial exponent zero.
Because $t_n\le1$, this requires no further reduction. Thus the final
squarefree monomial of the path has exponent $t_n$ at the source $i$,
and exponent $b_s$ at $i+s$ for $1\le s<n$:

$$E(t,i)=
\bigl(\{i\}\text{ if }t_n=1,\ \varnothing\text{ if }t_n=0\bigr)
\ \cup\ \{i+s:1\le s<n,\ b_s=1\}.
\tag{5}$$

The union is a union of index sets modulo $n$. Equations (2)–(5)
prove the exact expansion

$$P_{\rm all}X_i^d=\sum_t w(t)P_{E(t,i)}
\qquad\text{in }A_n.
\tag{6}$$

Every term on the right is squarefree. Consequently the coefficient
of any prescribed basis monomial is the sum of the weights of the
paths producing it. No choice of an unproved normal-form algorithm,
radicality assumption, or cancellation-free argument is being used.

For later use the two eventual states have these exact transitions:

| Incoming state | Output bit | Outgoing state | Weight |
| --- | --- | --- | --- |
| $0$ | $1$ | $0$ | $1$ |
| $1$ | $0$ | $1$ | $1$ |
| $1$ | $0$ | $0$ | $-c$ |

### 2. A source-index bound for any nonempty short target

Let $E$ be any nonempty subset of $\{0,\ldots,m\}$ and suppose
$n\ge L+1$. Consider a path in (6) with final support exactly $E$.
We claim that its source must satisfy

$$i\in
\left(\bigcup_{s=0}^{L-1}(E-s)\right)\cup(E+1)
\ \subseteq\ [-m,m+1]\pmod n.
\tag{7}$$

Here $E-s=\{e-s:e\in E\}$ and $E+1=\{e+1:e\in E\}$.
To prove the first inclusion, it suffices to consider a source
$i\notin E$ for which none of $i+1,\ldots,i+L-1$ lies in $E$.
Then $t_n=0$ by (5), and the first $L-1$ output bits away from
the source are zero.

If $t_L=0$, the transition table forces state zero for the rest of
the circuit. Since $n-1\ge L$, the last output bit is one, so
$i-1\in E$.

If $t_L=1$, the condition $t_n=0$ forces a transition from one to
zero at some step $s\in\{L,\ldots,n-1\}$. Before the first such
transition all output bits are zero; after it all subsequent output
bits are one. If it occurred only at the last step $s=n-1$, there
would be no subsequent one bits. Along with the assumed initial
zero bits and $t_n=0$, that would make $E$ empty. Hence the first
transition occurs at $s\le n-2$, and again the last output bit is
one. Therefore $i-1\in E$. This completes the first inclusion.

For the second inclusion in (7), use $E\subseteq[0,m]$ and
$L-1=m$. When $n\ge3m+4$, its integer interval representatives
give the concrete source set

$$I_n=\{0,\ldots,m+1\}\ \cup\ \{n-m,\ldots,n-1\}.
\tag{8}$$

The second set is empty when $m=0$. The two sets in (8) are
disjoint under the stated lower bound on $n$. The argument applies
to every odd $d\le D$, with the same $m,L,I_n$.

### 3. Insertion and deletion of a weight-one zero site

Keep $E\ne\varnothing$, $E\subseteq[0,m]$, and fix

$$n\ge3m+4,\qquad j=2m+2.
\tag{9}$$

Take a path producing $E$ at level $n$. Its source belongs to
$I_n$. In particular, neither $j$ nor $j+1$ is the source:
the lower source block ends at $m+1<j$, while the upper source
block begins at
$n-m\ge2m+4>j+1$. Both sites $j,j+1$ also lie outside $E$.

When the path reaches site $j$ in its cyclic source-dependent order,
at least $L$ sites have already been processed. Indeed, its forward
cyclic distance from the source is

$$j-i\ge m+1=L\quad(0\le i\le m+1),
$$

or

$$j+n-i\ge j+1\ge L\quad(n-m\le i\le n-1).
$$

Its incoming state at $j$ is therefore at most one, by (4).
Since the output at $j$ is zero, that state must be one.
Since the output at $j+1$ is also zero and $j+1$ is not the source,
the outgoing state at $j$ must also be one. Thus the transition
at $j$ is $1\to1$ and has weight one.

Insert a new site just after $j$, giving it output zero and transition
$1\to1$. Relabel the old sites by the order-preserving injection

$$\iota_n(r)=
\begin{cases}
r,&0\le r\le j,\\
r+1,&j+1\le r<n.
\end{cases}
\tag{10}$$

The target $E\subseteq[0,m]$ is unchanged, and the source becomes
$\iota_n(i)$. All old transitions occur in the same cyclic order.
The inserted transition has weight one, so the path weight is
unchanged. The initial carry is still $d$ and the final carry is
unchanged; in particular, the special final contribution at the
source in (5) is preserved. We have produced a path with target
$E$ at level $n+1$.

We now check surjectivity and the inverse, including the new source
position that appears in the longer orbit sum. Every path producing
$E$ at level $n+1$ has source in $I_{n+1}$. Hence its source is
neither $j+1$ nor $j+2$: the upper block begins at
$n+1-m\ge2m+5>j+2$. The sites $j+1,j+2$ are outside $E$.
The same distance estimate places site $j+1$ at least $L$ steps
after the source. Its incoming and outgoing states must therefore
both be one. Delete site $j+1$ and its weight-one transition, and
relabel all later indices down by one. This is a valid level-$n$
path with unchanged initial carry, final carry, target and weight.

Deletion reverses insertion and insertion reverses deletion.
The extra possible source $j+1$ in the level-$n+1$ sum produces no
target paths at all, by the source-index bound. Thus (10) defines
a weight-preserving bijection between *all pairs consisting of a
source and a path producing $E$*, at levels $n$ and $n+1$.
Together with (6), this proves

$$[P_E]\left(P_{\rm all}\sum_{i=0}^{n-1}X_i^d\right)
 =
[P_E]\left(P_{\rm all}\sum_{i=0}^{n}X_i^d\right)
\quad(n\ge3m+4),
\tag{11}$$

where the right side is computed in $A_{n+1}$.
The equality holds for each odd $d\le D$, not just the leading
monomial.

For a constant term $a_0$,
$P_{\rm all}H_n(a_0)=na_0P_{\rm all}$. Since
$E\subseteq[0,m]$ and $n\ge3m+4>m+1$, the target is not the full
index set. Its coefficient in this constant contribution is zero,
at both levels. Taking the linear combination in (11) therefore
proves (S), and in fact proves it for every nonempty
$E\subseteq[0,m]$ with the same bound.

### 4. Consecutive periods exclude a positive-degree normal defect

We now apply the newly proved stabilization lemma to the original
claim. The imported normal form decomposes any $h\in K_c$ uniquely
as $h=\Delta Q+v$, where $v\in k\oplus xk[x^2]$. Telescoping shows
$B_c\subseteq K_c$, so $v\in K_c$.

Suppose first that $v$ has positive odd degree $D$ and leading
coefficient $a_D\ne0$. Let $m,E_D$ have their meanings above.
For every $n$, ordinary-cycle vanishing implies

$$\bigl(2^nP_{\rm all}-1\bigr)H_n(v)=0\quad\text{in }A_n.
\tag{12}$$

This is precisely the accepted necessary Jacobian condition from
the old cyclic proof. Its use does not assume its false converse:
if $F_n=f^{\circ n}-x$ has a root of multiplicity $e$, the ordinary
vanishing of $H_n(v)$ gives order at least one there, and $F_n'$
has order at least $e-1$, also when $p\mid e$. Hence
$F_n\mid F_n'H_n(v)$. Under the imported cyclic presentation,
$F_n'=2^nP_{\rm all}-1$, which gives (12). This brief recall is to
identify the exact imported implication, not a new lemma.

For $n>2m$, the accepted all-parameter leading-binary-coefficient
lemma gives

$$[P_{E_D}]H_n(v)=a_D.
\tag{13}$$

Choose any $n\ge3m+4$. Equation (12), followed by (13), gives

$$2^nC_n(v;E_D)-a_D=0,\qquad
2^{n+1}C_{n+1}(v;E_D)-a_D=0.
\tag{14}$$

Equation (S) identifies the two $C$ values. Subtracting twice
the first identity in (14) from the second gives $a_D=0$,
contradicting the choice of the leading coefficient.
This argument divides neither by a period nor by a root multiplicity.
Both periods $n$ and $n+1$ are permitted even if one is divisible by $p$.

Therefore $v$ is constant. The polynomial $f(x)-x$ has a root over
$k$, and the primitive orbit consisting of that fixed point has
sum $v$. Since $v\in K_c$, this sum is zero. Thus $v=0$ and
$h=\Delta Q$. With the already noted reverse inclusion, we conclude

$$\boxed{K_c=B_c\quad
\text{for every odd }p,\ c\in\overline{\mathbb F}_p.}
\tag{15}$$

This is the original polynomial-coboundary assertion with all ordinary
primitive periods retained. $\square$

### 5. Same-theorem corollary: two explicit finite tests

The coordinator supplied the following consequence of the stabilization
proof. It belongs to the same PC424-L theorem, not a second paper question.

**Corollary.** Let $M\ge1$, $\deg h\le M$, and

$$n=3\lfloor\log_2 M\rfloor+4,\qquad
F_j=f^{\circ j}-x,\qquad
\widetilde H_j(h)=\sum_{s=0}^{j-1}h(f^{\circ s}(x)).
\tag{16}$$

Here $\widetilde H_j$ is the univariate polynomial representing $H_j$.
Then the following are equivalent:

1. $h\in B_c$.
2. $F_j\mid F_j'\widetilde H_j(h)$ for both $j=n,n+1$.
3. $\widetilde H_j(h)(a)=0$ for every ordinary root $a$ of $F_j$,
   for both $j=n,n+1$.

Consequently, every $h\notin B_c$ with $\deg h\le M$ has nonzero
sum on an ordinary primitive cycle whose length divides $n$ or $n+1$.
In particular one detecting primitive period is at most

$$3\lfloor\log_2 M\rfloor+5.
\tag{17}$$

**Proof.** Telescoping proves that condition 1 makes
$F_j\mid\widetilde H_j(h)$ for every $j$, so it implies both
conditions 2 and 3. The necessary Jacobian implication already recalled
in Section 4 proves that condition 3 implies condition 2.

Suppose condition 2 holds. The imported normal-form elimination only
lowers degrees, so $h=\Delta Q+v$ with $\deg v\le M$.
Telescoping shows that condition 2 is unchanged when $h$ is replaced
by $v$. If $v$ has positive odd degree $D\le M$, then
$n\ge3\lfloor\log_2D\rfloor+4$, and the two identities (14) hold
for these levels. The stabilization proof and the same subtraction
force the leading coefficient of $v$ to be zero, a contradiction.

Thus $v=a_0$ is constant. At level $j$ the polynomial in condition 2
becomes $j a_0F_j'$. Since $p$ is odd, $F_j'$ has nonzero leading
coefficient $2^j$ and degree $2^j-1<\deg F_j$. Therefore
$F_j\mid j a_0F_j'$ forces $j a_0=0$ in $k$. Applying this at
$j=n$ and $j=n+1$ and subtracting gives $a_0=0$. Hence $h\in B_c$,
proving the equivalences.

If $h\notin B_c$, condition 3 fails at some root $a$ of $F_j$ for
$j\in\{n,n+1\}$. Let $r\mid j$ be its ordinary primitive period
and let $O$ be its orbit. The nonzero value is
$\widetilde H_j(h)(a)=(j/r)\sum_{b\in O}h(b)$, so its primitive
sum is nonzero. This proves (17), without dividing in $k$.
$\square$

The ordinary-root tests in condition 3 are sums over the full $j$-step
return on every root, not merely tests on primitive cycles of exact
length $j$. Both finite iterate polynomials have degree at most
$2^{n+1}\le32M^3$. This is a proved finite certificate bound; no
finite test has been executed here.

## Verification boundary

The proof is entirely algebraic and uses no mathematical execution.
In particular, (S) is proved by an explicit finite weight-preserving
bijection, not by sampled coefficient agreement. Its new content is
stabilization after multiplication by $P_{\rm all}$; it does not
repackage the accepted leading-coefficient lemma for $H_n(v)$ alone.

There is no step requiring that a binary coefficient functional itself
descend to the reduced quotient. We use the full cyclic algebra and
the valid necessary implication (12), at two consecutive levels.
The old example where Jacobian annihilation fails to imply ordinary
vanishing at a single level is therefore consistent with this proof.

Formal Böttcher evaluation, Laurent-tail periodization, bounds on
multiple periodic roots, finite Frobenius dependence, and algebraic
transfer extraction are not invoked. If independently accepted, the
original equality implies the previously targeted finite Frobenius
dependence simply with $s=0$; no separate finiteness theorem is claimed.

## Open risks and review status

Independent author-proof checking and an independent derivation have
been allocated by the coordinator, but are pending at this file version.
In particular, the source-dependent insertion/deletion in Section 3
and the final carry at the source in (5) must pass those checks.
No original-contract acceptance, source-priority clearance, manuscript
admission, or new paper count is asserted here.

The mathematical proof imports only the explicitly linked accepted
normal-form, full-cycle-basis, leading-coefficient and Jacobian facts.
Broader literature/source collision review is a subsequent coordinator
gate, not something inferred from the success of the hand proof.
