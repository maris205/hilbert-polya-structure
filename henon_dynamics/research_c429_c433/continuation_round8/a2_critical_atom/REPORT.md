# R8: a hand proof for the critical quadratic atom

2026-09-10 UTC. One cyclic multiplier-algebra mechanism.

## 1. Frozen exact claim and status

For every odd prime $p$, put $k=\overline{\mathbf F}_p$ and

$$f(x)=x^2-1,\qquad g(x)=(x-1)/(x+1).$$

**Claim.** There are infinitely many distinct ordinary primitive
$f$-cycles $O\subset k$ avoiding $\{0,1,-1\}$ for which

$$\prod_{x\in O}g(x)\ne1.$$

The native clock is one application of $f$. An ordinary primitive
cycle is the set of distinct points in one orbit of least period
$n$, and its product uses each point once, without scheme multiplicity.
Every odd prime remains in scope. This is the exact allocated residual
atom question, not a replacement for general MS6 and not an admission.

**Author proof status: PROVABLE AS STATED.** The proof below is complete
as an author proof package; independent review is not presumed passed.
It proves more: for every prime $n\ne p$ satisfying

$$n\equiv1\pmod{p-1},\qquad n\not\equiv1\pmod p, \tag{1.1}$$

there is such a bad cycle of least period exactly $n$. Section 8
proves that this set of primes is infinite by an elementary argument.
All primes in (1.1) are odd, so $n\ge3$. Section 7 also gives a
separate characteristic-$3$ check for every odd prime native period.

## 2. Input subtraction, strategy, and dependency map

A1's complete 379-line
[R7 report](../../continuation_round7/a1_balanced_divisor_detection/REPORT.md)
was actually read, with SHA256
`59f79d718d85e0c2b4bbaea2e8d78416b5cb48e52927fe044605fb5847bc6e8f`.
Its all-parameter atom reduction was under E8 review at this task's
start; the root later reported that review accepted. The present proof
does not assume that reduction. It proves the stated residual question
directly, including the required cycle-product identity.

The mechanism was frozen before the coefficient proof: use the
individual orbit multiplier product in a cyclic coordinate algebra,
kill the fixed-point exception, and multiply by the derivative to
handle repeated fixed-scheme roots. The target was

$$D_n=(2^nP-1)(X_1-X_0)(P^3-1). \tag{2.1}$$

The proof does not use the already unsuccessful aggregate product
over all fixed points, nor infer anything from the automatic fact
that elements of $k^*$ are roots of unity.

Dependencies, in order:

1. The cycle identity in Section 3 translates a good individual
   cycle into $P^3=1$ at each point of that cycle.
2. The normal basis and repeated-root annihilator in Section 4
   show that goodness of every primitive $n$-cycle would force
   $D_n=0$ in the cyclic algebra, for prime $n\ge3$.
3. Sections 5 and 6 compute one exact normal-basis coefficient:
   $[X_1\cdots X_{n-1}]D_n=(2^n-2)^2/2+1-n$.
4. For primes in (1.1) this coefficient is $1-n\ne0$ in $k$.
5. The elementary cyclotomic argument in Section 8 gives infinitely
   many such prime native periods. Different least periods give
   distinct cycles.

The only assumptions are that $p$ is odd and the map and atom are
exactly those in Section 1. No separability of $f^{\circ n}(x)-x$,
multiplier rigidity theorem, return-map replacement, generic parameter,
finite-field degree cutoff, or Dirichlet theorem is assumed.

## 3. Exact product on an individual cycle

Let $O$ be an ordinary cycle avoiding $\{0,1,-1\}$, and define

$$A=\prod_{x\in O}x,\qquad
  B=\prod_{x\in O}(x+1),\qquad
  C=\prod_{x\in O}(x-1).$$

These are nonzero. Since $f$ permutes the points of $O$,

$$BC=\prod_{x\in O}f(x)=A,$$

and, using $f(x)+1=x^2$,

$$B=\prod_{x\in O}(f(x)+1)=A^2.$$

Consequently $C=A^{-1}$ and

$$\prod_{x\in O}g(x)=C/B=A^{-3}. \tag{3.1}$$

If $|O|=n$, its multiplier is $2^nA$, by the derivative chain rule.
Thus goodness is the exact equation $A^3=1$, not an aggregate
condition on the products of different cycles.

The points $0,-1$ form a two-cycle, and $1$ maps into that cycle
without belonging to it. Therefore no periodic point of odd least
period lies in $\{0,1,-1\}$.

## 4. Normal basis and the ordinary-root annihilator

Fix an integer $n\ge3$ and use indices modulo $n$. Write

$$\mathcal A_n=k[X_0,\ldots,X_{n-1}]/
 (X_i^2-X_{i+1}-1)_{i\bmod n},$$

$$E=f^{\circ n}(x),\quad F=E-x,\quad N=2^n,\quad
P=\prod_{i=0}^{n-1}X_i,\quad K=X_1-X_0,\quad
M=\prod_{i=1}^{n-1}X_i.$$

The assignment $X_i\mapsto f^{\circ i}(x)$ gives an isomorphism

$$\mathcal A_n\simeq k[x]/(F). \tag{4.1}$$

Indeed the relations determine every $X_i$ from $X_0$, and the last
relation is $f^{\circ n}(X_0)=X_0$; the reverse assignment sends
$x$ to $X_0$.

Every monomial reduces to a linear combination of squarefree monomials:
each replacement $X_i^2\mapsto X_{i+1}+1$ lowers total degree.
These $2^n$ squarefree monomials are linearly independent. Their images
under (4.1) are monic polynomials of pairwise distinct degrees
$\sum_i\epsilon_i2^i$, where $\epsilon_i\in\{0,1\}$; all these
degrees are less than $\deg F=N$. They therefore form the normal
basis. The notation $[M]U$ denotes the coefficient of $M$ in this basis.

**Ordinary-root lemma.** If a polynomial $H\in k[x]$ vanishes at
every distinct root of $F$, then $F$ divides $F'H$.

To prove it, let $\alpha$ have multiplicity $e\ge1$ in $F$.
Differentiating $F=(x-\alpha)^eV$, with $V(\alpha)\ne0$, shows
$\operatorname{ord}_\alpha F'\ge e-1$. This remains true when
$p$ divides $e$; then the order can be larger. Since
$\operatorname{ord}_\alpha H\ge1$, the product has order at least
$e$. Doing this at every distinct root proves the divisibility.

Now suppose $n\ge3$ is prime and every ordinary cycle of least
period $n$ is good. Every root $\alpha$ of $F$ has least period
$1$ or $n$. At a fixed point, $K(\alpha)=f(\alpha)-\alpha=0$.
At a point of least period $n$, the orbit avoids the three excluded
points, and (3.1) gives $P(\alpha)^3=1$. Thus

$$H=K(P^3-1)$$

vanishes at every distinct root, whether or not $F$ is squarefree.
The chain rule gives

$$F'=2^n\prod_{i=0}^{n-1}f^{\circ i}(x)-1=2^nP-1.$$

The ordinary-root lemma and (4.1) therefore imply

$$D_n=(2^nP-1)K(P^3-1)=0\quad\hbox{in }\mathcal A_n. \tag{4.2}$$

No multiplicity was inserted into the original cycle product.

## 5. First three normal coefficients, including the cubic term

All calculations in Sections 5 and 6 are finite hand calculations in
$\mathcal A_n$, valid for every integer $n\ge3$ and odd characteristic.

### 5.1. The coefficients of $K$, $KP$, and $KP^2$

For a cyclic consecutive interval $I_i(r)$ of length $r$ starting at
$i$, repeated use of the relations gives

$$X_iP=X_i+\sum_{r=1}^{n}\prod_{j\notin I_i(r)}X_j. \tag{5.1}$$

At each square, choosing the constant term ends the carry and gives
one displayed complement product; carrying all the way around the
cycle leaves the final $X_i$. This also proves (5.1) by successive
substitution. Only the $r=1$ term has degree $n-1$, since $n\ge3$.
It follows that

$$[M]K=0,\qquad [M]KP=-1. \tag{5.2}$$

The product of the defining relations, followed by cyclic reindexing,
gives

$$P^2=\prod_{i=0}^{n-1}(X_i+1). \tag{5.3}$$

For $2\le j\le n-1$ set

$$R_j=\prod_{\ell=j}^{n-1}(X_\ell+1),\qquad
R_1=\prod_{\ell=1}^{n-1}(X_\ell+1).$$

Successively reducing $X_iR_i$ from $i$ towards $n-1$ gives

$$X_iR_i=\sum_{j=i}^{n-1}R_j+X_0\qquad(2\le i\le n-1).$$

For example, the recursion is
$X_iR_i=R_i+X_{i+1}R_{i+1}$ until the last relation
$X_{n-1}^2=X_0+1$ closes it.
The direct two-variable calculation

$$K(X_0+1)(X_1+1)=X_0X_2-X_1-1$$

therefore yields the following expression already in normal form:

$$KP^2=
 \sum_{j=2}^{n-1}X_0R_j+X_1+1-R_1. \tag{5.4}$$

Here the only term contributing to $M$ is $-R_1$, so

$$[M]KP^2=-1. \tag{5.5}$$

### 5.2. The two auxiliary coefficients for the cubic term

For every $2\le j\le n-1$,

$$[M](X_0PR_j)=1. \tag{5.6}$$

To check it, first replace the initial $X_0^2$:

$$X_0PR_j=(X_1+1)\Bigl(\prod_{i=1}^{n-1}X_i\Bigr)R_j.$$

Expand this product. Each monomial has exponent $1$ or $2$ in each
$X_i$ for $i\ge1$, and has no $X_0$. The choice of the constant
term from $(X_1+1)$ and every factor of $R_j$ contributes $M$ once.
For any other choice, let $s$ be its first index with exponent $2$.
Reducing in order $X_1,X_2,\ldots,X_{n-1}$ removes $X_s$ when
$X_s^2$ is replaced. No later replacement creates $X_s$. During this
ordered reduction incoming exponents increase by at most one, so the
last replacement can create at most one $X_0$, never $X_0^2$; it
cannot restart a carry at $X_1$. Thus this monomial cannot contribute
to $M$. This proves (5.6).

The other coefficient is

$$[M](PR_1)=1. \tag{5.7}$$

Here is a parity proof that also handles characteristic cancellations.
Under (4.1), $P$ is odd of degree $N-1$, $M$ is even of degree $N-2$,
and every other basis monomial has degree at most $N-3$. Thus $[M]U$
equals the coefficient of $x^{N-2}$ in the degree-below-$N$ remainder
of $U$ modulo $F$: the only higher-degree basis element is $P$, and
its coefficient at this even power is zero.

The polynomial $U=PR_1$ is monic and odd of degree $2N-3$, while
$E=f^{\circ n}(x)$ is monic and even of degree $N$. Divide by $E$:

$$U=EV+W,\qquad \deg W<N.$$

Uniqueness of division and parity imply that $V,W$ are odd.
The quotient $V$ is monic of degree $N-3$. Modulo $F=E-x$,

$$U\equiv xV+W,$$

and the right side has degree below $N$. Its coefficient at
$x^{N-2}$ is $1$, coming from $xV$; the odd polynomial $W$ has
zero coefficient there. This proves (5.7).

### 5.3. The cubic coefficient

Multiply (5.4) by $P$ and extract $M$. Equations (5.1), (5.6),
and (5.7), together with $[M]P=0$, give

$$[M]KP^3=(n-2)\cdot1+0+0-1=n-3. \tag{5.8}$$

In particular, the count $n-2$ is taken in the integers and then
mapped to $k$; it is not assumed nonzero in characteristic $p$.

## 6. The quartic coefficient by a finite normal-form functional

This section computes the remaining coefficient without using the
false simplification $P^4=\prod_i(X_i+2)$.

### 6.1. Exact coefficient functional and its finite expansion

Let $L(U)=[P]U$ be the top normal-basis coefficient. The degree
reduction and (5.1) imply, for every $U\in\mathcal A_n$,

$$[M]U=L(X_0U). \tag{6.1}$$

Indeed basis elements of degree at most $n-2$ cannot contribute to
$P$ after multiplication by $X_0$. Among degree-$n-1$ basis elements,
only $M$ produces $P$; the others contain $X_0$ and their square
replacement lowers degree. The degree-$n$ element $P$ contributes
zero by (5.1).

For a polynomial $H$ define a coefficient extractor by expanding

$$\mathscr R(H)=
[X_0^{-1}\cdots X_{n-1}^{-1}]
 H\prod_{i=0}^{n-1}
 \left(\sum_{q_i\ge0}X_i^{-2q_i-2}(X_{i+1}+1)^{q_i}\right).
 \tag{6.2}$$

This is a finite coefficient calculation, not a convergence assumption.
For an input monomial of total degree $d$, a contributing term has

$$d-n=2\sum_iq_i-\sum_ir_i\ge\sum_iq_i,$$

where $r_i\le q_i$ is the power of $X_{i+1}$ selected from its
binomial. Therefore only finitely many nonnegative $q_i$ can contribute.

The extractor annihilates every multiple of
$X_i^2-X_{i+1}-1$: cancellation of its geometric series leaves no
negative power of $X_i$ anywhere in that product. Moreover it is $1$
on $P$ (all $q_i=0$) and $0$ on every lower-degree squarefree
monomial. Hence it descends to the quotient and equals $L$.

For $H=\prod_i h_i(X_i)$, write $h_{i,m}$ for the coefficient of
$X^m$ in $h_i(X)$, taking it to be zero outside its degree range.
The exponent condition in (6.2) is
$m_i=2q_i+1-r_{i-1}$. Define

$$T_h(r,s)=\sum_{q\ge s}\binom qs h_{2q+1-r}.
 \tag{6.3}$$

Summing the cyclic indices gives

$$L\Bigl(\prod_i h_i(X_i)\Bigr)
 =\sum_{r_0,\ldots,r_{n-1}\ge0}
   \prod_iT_{h_i}(r_{i-1},r_i),\qquad r_{-1}=r_{n-1}.
 \tag{6.4}$$

This is the trace of the indicated product of finite matrices once
the contributing index range is bounded. Formula (6.2) proves its
validity, including possible closed carries around the cyclic indices.

### 6.2. The two finite traces

Put $h(X)=(X+1)^2$. By (5.3), $P^4=\prod_i h(X_i)$, so (6.1) gives

$$[M]KP^4
 =L\Bigl(X_0X_1\prod_i h(X_i)\Bigr)
  -L\Bigl(X_0^2\prod_i h(X_i)\Bigr). \tag{6.5}$$

For the first term, the local polynomials at indices $0,1$ are $Xh$,
and all other local polynomials are $h$. A nonzero local term satisfies
$2r_i\le r_{i-1}+\deg h_i-1$.
All contributing cyclic indices are $0$ or $1$: a maximum at least
$3$ is incompatible with degree at most $3$; if the maximum is $2$,
no degree-$2$ site can output $2$, and the two adjacent degree-$3$
sites cannot start such an output after the degree-$2$ site preceding
index $0$. There is such a site because $n\ge3$.

On indices $0,1$, (6.3) gives

$$T=T_h=\begin{pmatrix}2&0\\2&1\end{pmatrix},\qquad
S=T_{Xh}=\begin{pmatrix}2&1\\2&2\end{pmatrix}.$$

Thus the first term in (6.5) is $\operatorname{tr}(S^2T^{n-2})$.
Direct multiplication gives, for $r\ge0$,

$$S^2=\begin{pmatrix}6&4\\8&6\end{pmatrix},\qquad
T^r=\begin{pmatrix}2^r&0\\2(2^r-1)&1\end{pmatrix},$$

and consequently

$$L\Bigl(X_0X_1\prod_i h(X_i)\Bigr)=14\cdot2^{n-2}-2. \tag{6.6}$$

For the second term in (6.5), only the polynomial at index $0$ has
degree $4$, namely $X^2h$. Every other site has degree $2$.
The inequality above shows that an index can never increase while
traversing the degree-$2$ sites, so the maximum occurs at index $0$.
If that maximum is $R$, the preceding index is at most $(R+1)/2$;
the degree-$4$ site then gives
$2R\le(R+1)/2+3$, hence $R\le2$.
All indices after the degree-$4$ site are at most $1$.
It is enough to use indices $0,1,2$ in (6.3):

$$\widetilde T=
 \begin{pmatrix}2&0&0\\2&1&0\\2&2&0\end{pmatrix},\qquad
U=T_{X^2h}=
 \begin{pmatrix}2&2&0\\2&3&1\\2&4&2\end{pmatrix}.$$

The second term is $\operatorname{tr}(U\widetilde T^{n-1})$.
For $r\ge1$, direct multiplication or induction yields

$$\widetilde T^r=
 \begin{pmatrix}
 2^r&0&0\\2(2^r-1)&1&0\\3\cdot2^r-4&2&0
 \end{pmatrix}.$$

Therefore

$$L\Bigl(X_0^2\prod_i h(X_i)\Bigr)
 =6\cdot2^{n-1}+1. \tag{6.7}$$

Subtracting (6.7) from (6.6) proves the corrected coefficient

$$[M]KP^4=2^{n-1}-3. \tag{6.8}$$

All binomial entries, powers, and traces were computed over the
integers and then reduced to $k$. No division by $n$, no matrix
diagonalization, and no condition on $n$ modulo $p$ occurs here.

### 6.3. The decisive coefficient

Expand (2.1) as

$$D_n=K(2^nP^4-P^3-2^nP+1).$$

Using (5.2), (5.8), and (6.8),

$$\begin{aligned}
[M]D_n
 &=2^n(2^{n-1}-3)-(n-3)+2^n\\
 &=2^{2n-1}-2^{n+1}-n+3\\
 &=\frac{(2^n-2)^2}{2}+1-n. \tag{6.9}
\end{aligned}$$

Division by $2$ is legitimate for precisely the odd characteristics
in the claim. If $n$ satisfies (1.1), Fermat's theorem gives
$2^n=2$ in $\mathbf F_p$, and hence

$$[M]D_n=1-n\ne0. \tag{6.10}$$

## 7. Independent short characteristic-$3$ check

When $p=3$, goodness of a primitive cycle gives $P^3=1$, which is
equivalent to $P=1$ in the field $k$. For any odd prime $n$, the
ordinary-root argument can therefore use $H=K(P-1)$ instead.
Since $2^n=-1$ in characteristic $3$, its annihilator is

$$K(2^nP-1)(P-1)=K(1-P^2).$$

By (5.2) and (5.5), its $M$ coefficient is $1$, so it is nonzero.
Thus there is a bad primitive cycle at every odd prime period in
characteristic $3$. This check is not needed for the uniform proof
through (6.10), but shows explicitly that the characteristic-$3$
branch is not hidden in a division by $3$ or a cube-root choice.

## 8. Infinitely many usable prime native periods

**Prime-period lemma.** For every odd prime $p$, there are infinitely
many primes $n\ne p$ with $n\equiv1\pmod{p-1}$ and
$n\not\equiv1\pmod p$.

Let $m=p-1\ge2$, and let $\Phi_m(T)\in\mathbf Z[T]$ be the
$m$th cyclotomic polynomial. We use its elementary defining properties:
it is monic of degree $\varphi(m)$, has constant term $1$ for $m>1$,
and $T^m-1=\prod_{d\mid m}\Phi_d(T)$.
Since $m$ is even, $\varphi(m)\le m/2$.

Over $\mathbf F_p$, each of $\Phi_m(T)$ and $\Phi_m(T)-1$ is a
nonzero polynomial of degree $\varphi(m)$. Together they have at
most $2\varphi(m)\le p-1$ roots. Hence some $t\in\mathbf F_p$
satisfies

$$\Phi_m(t)\notin\{0,1\}. \tag{8.1}$$

In particular $t\ne0$. Suppose only finitely many desired primes
other than $p$ exist, and call their set $S$. By the Chinese remainder
theorem choose arbitrarily large positive integers $A$ satisfying

$$A\equiv0\pmod{m\prod_{q\in S}q},\qquad A\equiv t\pmod p.$$

The moduli are coprime because no element of $S$ is $p$.
Choose $A$ large enough that the positive integer
$V=\Phi_m(A)$ exceeds $1$.
Every prime divisor $q$ of $V$ avoids $mA$: a prime dividing $A$
would see $\Phi_m(A)\equiv1$, and every prime dividing $m$ divides
$A$. It also avoids $p$ by (8.1), and avoids $S$ since all primes
in $S$ divide $A$.

For completeness, such a divisor $q$ satisfies $q\equiv1\pmod m$.
Modulo $q$, the polynomial $T^m-1$ is squarefree because $q\nmid m$.
Its cyclotomic factors therefore have no common root. The residue of
$A$ is a root of $\Phi_m$, so has multiplicative order exactly $m$:
an order that was a proper divisor $d$ of $m$ would make it a root
of $T^d-1$ and hence of a different cyclotomic factor. The order
divides $q-1$, proving the congruence.

If all prime divisors of $V$ were also $1$ modulo $p$, then $V$
itself would be $1$ modulo $p$, contrary to (8.1). At least one such
divisor therefore satisfies $q\not\equiv1\pmod p$. It is a new
prime of the desired kind outside $S$, a contradiction. This proves
the lemma. The argument includes $p=3$, for which $m=2$.

## 9. Completion of the exact claim

For each of the infinitely many primes $n$ supplied by Section 8,
suppose every primitive cycle of least period $n$ were good. Section 4
would give $D_n=0$ in $\mathcal A_n$, whereas (6.10) gives a nonzero
normal-basis coefficient. This contradiction proves the existence of
a bad ordinary primitive cycle of least period exactly $n$.

Because $n$ is odd, Section 3 ensures the cycle avoids
$\{0,1,-1\}$. Because least periods are different for different
chosen primes, these cycles are distinct. Formula (3.1) gives the
required product inequality. This proves the original claim for every
odd prime $p$, without a parameter restriction or a finite exception
in the characteristic. $\square$

## 10. Attempt ledger, source accounting, and remaining scope

The frozen test was always (2.1); no second mathematical mechanism
was opened. During hand exploration the author mistakenly replaced
$P^4$ by $\prod_i(X_i+2)$ and sent a provisional full-family
breakthrough message. That identity omits the cross term from squaring
$(X_i+1)$ and is false in odd characteristic. The message and its
claimed coefficient $2^{n+1}-n+3$ were explicitly withdrawn before
this proof was finalized. The root reported that no such conclusion
had been adopted. The correct identity used in Section 6 is

$$P^4=\prod_i(X_i+1)^2
     =\prod_i(X_{i+1}+2X_i+2),$$

and the replacement calculation (6.2)--(6.9) includes every cross
term and every cyclic carry. The characteristic-$3$ argument and
the cubic calculation did not depend on the withdrawn identity.

No primary-source query batch was used by this author task; the cap
was two. No external theorem about finite multiplier spectra is used.
The only source dependency is the read local R7 report as context;
the theorem above is proved independently of its larger reduction.
The root separately allocated independent coefficient reconstruction
to E2, and announced a later full proof review; neither review is
presumed passed in this author report.

No mathematical program, parameter census, numerical experiment,
nested agent, external model/API, Git operation, manuscript/PDF,
or old/shared-file edit was used. Only this allocated new report was
written. The finite matrices in Section 6 were evaluated by hand.

**Open risks and limits.** The author proof has no retained missing
lemma, but the nonreduced annihilator, cyclic coefficient extractor,
quartic trace, and prime-period lemma are explicit independent-review
targets. Combining this result with the separately accepted R7 atom
reduction is a root integration decision. This report does not prove
the general norm-one lemma for arbitrary rational functions, does not
close general MS6, and does not admit a fifth contract.
