# R8 full nonauthor review: the critical quadratic atom

2026-09-10 UTC. Reviewer: E5. This is the allocated full mathematical
review, not a contract admission or a general MS6 closure.

## 1. Exact reviewed version and verdict

The entire actual author report was read and independently checked:

- `continuation_round8/a2_critical_atom/REPORT.md`, 526 lines;
- SHA256: `e3fcd6eef80df88ed1d0b5b4633e6d6e1003582bf0b4022c86303df166f278c3`.

The accepted R7 atom reduction was read as a separate input/interface:

- `continuation_round7/a1_balanced_divisor_detection/REPORT.md`, 379 lines;
- SHA256: `59f79d718d85e0c2b4bbaea2e8d78416b5cb48e52927fe044605fb5847bc6e8f`.

Both hashes were checked against the files, not copied as unverified
author claims. No E2 assessment was read or requested before completing
the full independent findings recorded here. The author formula was
available; every coefficient and logical interface below was checked
directly, without using another review as evidence.

**Verdict: PROVABLE AS STATED.** For every odd prime $p$, over
$k=\overline{\mathbf F}_p$, the native map $f(x)=x^2-1$ and atom
$g(x)=(x-1)/(x+1)$ have infinitely many distinct ordinary primitive
cycles avoiding $\{0,1,-1\}$ with product different from $1$.
The stronger prime-period assertion in author Section 1 is also valid.

There are **zero unresolved mathematical or source-applicability
must-fixes** in this frozen version. No author repair was requested.
The earlier false quartic shortcut was already withdrawn before this
version and remains withdrawn; it is not an input to this verdict.

The integration with the separately accepted R7 theorem is valid at
the single-quadratic-atom level, as detailed in Section 10 below.
Neither result supplies the missing general rational-function MS6
implication. Root integration/admission decisions are not made here.

## 2. Individual cycles, native periods, and the quotient basis

The cycle product calculation is exact for distinct orbit points.
For an ordinary cycle $O$ avoiding $0,1,-1$, set
$A=\prod_Ox$, $B=\prod_O(x+1)$, and $C=\prod_O(x-1)$.
All three factors are nonzero. Permuting points by $f$ gives

$$BC=\prod_Of(x)=A,\qquad
B=\prod_O(f(x)+1)=\prod_Ox^2=A^2.$$

Therefore $C=A^{-1}$ and $\prod_Og=A^{-3}$. This proves both
directions of goodness $\Longleftrightarrow A^3=1$, without an
aggregate over different cycles or a scheme multiplicity convention.
The return multiplier of an $n$-cycle is $2^nA$ by the chain rule.

In every odd characteristic, $0$ and $-1$ are distinct and form a
two-cycle. The point $1$ maps to $0$ and is not itself periodic.
Thus every cycle of odd least period avoids all three points. This
includes the least-period-one points, although the proof disposes of
those separately using $K$.

For every integer $n\ge3$, let

$$\mathcal A_n=k[X_0,\ldots,X_{n-1}]/(X_i^2-X_{i+1}-1),$$

with cyclic indices, and put $E=f^{\circ n}(x)$, $F=E-x$,
$N=2^n$, $P=\prod_iX_i$, $K=X_1-X_0$, and
$M=X_1\cdots X_{n-1}$.
Sending $X_i$ to $f^{\circ i}(x)$ gives the claimed isomorphism
$\mathcal A_n\simeq k[x]/F$. The relations recursively determine
all variables from $X_0$ and give exactly $f^{\circ n}(X_0)=X_0$.

Replacing any $X_i^2$ by $X_{i+1}+1$ decreases total degree, so the
squarefree monomials span. Their images are monic polynomials of
degrees $\sum_i\epsilon_i2^i$, which are exactly the distinct integers
from $0$ through $N-1$. Since $F$ is monic of degree $N$, these images
are independent modulo $F$. Hence they are genuinely a basis, and
all later coefficient functionals are unambiguous. This argument
does not require a squarefree $F$ or a confluent chosen reduction order.

## 3. Ordinary roots, possible wild multiplicities, and fixed points

The ordinary-root lemma is valid without a separability assumption.
If $F=(x-\alpha)^eV$ and $V(\alpha)\ne0$, differentiation gives
$\operatorname{ord}_\alpha F'\ge e-1$. If $p\mid e$, the leading
derivative term disappears and the order can only increase. If a
polynomial $H$ vanishes at every distinct root, then
$\operatorname{ord}_\alpha(F'H)\ge e$ for every root. Thus
$F\mid F'H$. The assertion also makes sense if the derivative is zero;
no division by $F'$ is made.

For prime $n\ge3$, every root of $F$ is a periodic point of least
period $1$ or $n$. If every ordinary $n$-cycle were good, then at a
least-period-$n$ root the preceding product identity gives $P^3=1$.
At a fixed point, $K=f(x)-x$ vanishes. Consequently
$H=K(P^3-1)$ vanishes at every distinct root of $F$.

The chain rule gives $F'=NP-1$ under the quotient identification.
The necessary identity is therefore exactly

$$D_n=(NP-1)K(P^3-1)=0\quad\text{in }\mathcal A_n.$$

In particular, $K$ need not kill a fixed-point local algebra by itself:
it only has to vanish at the underlying point, and $F'$ supplies the
remaining multiplicity. This is why a parabolic fixed point, a
multiple exact-period root, or multiplicity divisible by $p$ causes
no missing case. The original product still uses each orbit point once.
The argument also covers the hypothetical absence of exact $n$-cycles:
the goodness assumption would be vacuous, and the same necessary
identity would follow and be contradicted below.

## 4. Independent check of the coefficients through degree three

The square-carry identity in author (5.1) is correct:

$$X_iP=X_i+\sum_{r=1}^n\prod_{j\notin I_i(r)}X_j.$$

Choosing the constant term at the first square ends a carry; continuing
through $r$ consecutive sites gives the indicated complement. After
a complete circuit the remaining term is $X_i$. For $n\ge3$ the
only terms of squarefree degree $n-1$ are the complements for $r=1$.
It follows that

$$[M]K=0,\qquad [M]KP=-1,\qquad [M](X_1P)=0.$$

Multiplication of the defining relations gives the valid identity
$P^2=\prod_i(X_i+1)$. Put $R_j=\prod_{\ell=j}^{n-1}(X_\ell+1)$.
For $i\ge2$, the recursion
$X_iR_i=R_i+X_{i+1}R_{i+1}$ ends in $X_{n-1}R_{n-1}=R_{n-1}+X_0$.
Direct expansion and the first two relations also give

$$K(X_0+1)(X_1+1)=X_0X_2-X_1-1.$$

These identities yield the squarefree expression

$$KP^2=\sum_{j=2}^{n-1}X_0R_j+X_1+1-R_1,$$

whose $M$ coefficient is $-1$. This includes $n=3$.

For the cubic term, both auxiliary coefficient claims were checked:

$$[M](X_0PR_j)=1\quad(2\le j\le n-1),\qquad [M](PR_1)=1.$$

For the first, replacing the initial $X_0^2$ gives
$(X_1+1)MR_j$. In each expanded monomial all exponents at indices
$1,\ldots,n-1$ are $1$ or $2$, and there is no $X_0$.
The all-constant choice supplies $M$ once. Every other monomial has
a first doubled index $s$. Ordered reduction removes $X_s$ and
cannot create it again. The incoming carry increases an exponent by
at most one, so the last reduction introduces at most $X_0$, not
$X_0^2$; a second circuit cannot repair the missing factor. Such a
monomial therefore contributes zero to $M$.

For the second, under the one-variable isomorphism, $P$ is monic odd
of degree $N-1$ and $M$ monic even of degree $N-2$. Every other basis
element has degree at most $N-3$. It follows that $[M]U$ is exactly
the $x^{N-2}$ coefficient of the remainder of $U$ modulo $F$; the
one higher basis element $P$ has zero coefficient at this even power.

Now $PR_1$ is monic odd of degree $2N-3$, and $E$ is monic even
of degree $N$. In the division $PR_1=EV+W$, both $V$ and $W$ are
odd by uniqueness of division and parity. The polynomial $V$ is
monic of degree $N-3$. The remainder modulo $E-x$ is $xV+W$,
which has degree below $N$ and coefficient $1$ at $x^{N-2}$.
Odd characteristic is used legitimately in the parity argument.

Multiplying the displayed expression for $KP^2$ by $P$ therefore gives

$$[M]KP^3=(n-2)-1=n-3.$$

The count is an integer subsequently reduced in $k$; there is no
assumption that $n-2$ or $n-3$ is nonzero in the field.

## 5. The coefficient functional and all cyclic carries

Let $L(U)=[P]U$. The identity $[M]U=L(X_0U)$ holds on each
squarefree basis element. Degree at most $n-2$ cannot reach $P$;
among degree-$n-1$ elements only $M$ reaches $P$; and $X_0P$ has
no $P$ term by the square-carry formula. Thus it holds for all $U$.

The formal-looking extractor in author (6.2) is a legitimate finite
coefficient operation. For a monomial $H=\prod_iX_i^{m_i}$ of total
degree $d$, select an exponent $r_i\le q_i$ in
$(X_{i+1}+1)^{q_i}$. To obtain the requested power $X_i^{-1}$ one
must have $m_i=2q_i+1-r_{i-1}$. Summing gives

$$d-n=2Q-R\ge Q,\qquad Q=\sum_iq_i,\quad R=\sum_ir_i.$$

Thus the contributing nonnegative $q_i$ lie in a finite set for each
input polynomial. There is no implicit analytic convergence or
uncontrolled infinite trace.

To verify annihilation of the ideal, multiply the extractor by
$X_i^2-X_{i+1}-1$. Its geometric series telescopes, leaving $1$
in place of the $i$th factor. This cancellation is valid coefficient
by coefficient using the preceding finiteness bound. All remaining
factors, including any polynomial multiplier, have nonnegative powers
of $X_i$: negative powers occur only in the denominators indexed by
other variables. Hence the coefficient of $X_i^{-1}$ is zero.

The extractor is $1$ on $P$, because the bound forces all $q_i=0$,
and is zero on every lower-degree squarefree monomial. It therefore
descends to the quotient and equals $L$ exactly.

For $H=\prod_ih_i(X_i)$, write $h_j=[X^j]h$, with zero coefficients
outside the degree range. The exponent condition yields

$$T_h(r,s)=\sum_{q\ge s}\binom qs h_{2q+1-r},\qquad
L(H)=\sum_{r_0,\ldots,r_{n-1}\ge0}
\prod_iT_{h_i}(r_{i-1},r_i).$$

The same finiteness argument justifies this regrouping. A product
of finite matrices describes the sum once the contributing index
range is bounded. The cyclic closure $r_{-1}=r_{n-1}$ is retained,
so this method includes closed carries rather than silently discarding
them. The next bounds were checked before using the small matrices.

## 6. Independent quartic reconstruction and the decisive coefficient

Use $h(X)=(X+1)^2$, so the valid quartic identity is
$P^4=\prod_ih(X_i)$. Consequently

$$[M]KP^4=L\left(X_0X_1\prod_ih(X_i)\right)
-L\left(X_0^2\prod_ih(X_i)\right).$$

A nonzero local summand satisfies
$2r_i\le r_{i-1}+\deg h_i-1$, directly from its degree range and
$q_i\ge r_i$.

In the first term there are two adjacent degree-three sites, at $0,1$,
and all remaining sites have degree two. A cyclic maximum at least
$3$ contradicts $2R\le R+2$. If the maximum were $2$, it could
not be output by a degree-two site. Site $0$ cannot output $2$
after the degree-two site at $n-1$, and site $1$ consequently cannot
do so either. Here $n\ge3$ is essential and sufficient. All indices
are therefore $0$ or $1$.

Direct evaluation of the binomial formula gives

$$T_h=\begin{pmatrix}2&0\\2&1\end{pmatrix}=T,
\qquad T_{Xh}=\begin{pmatrix}2&1\\2&2\end{pmatrix}=S.$$

Their powers and product are

$$T^r=\begin{pmatrix}2^r&0\\2(2^r-1)&1\end{pmatrix},\qquad
S^2=\begin{pmatrix}6&4\\8&6\end{pmatrix}.$$

Thus the first functional equals
$\operatorname{tr}(S^2T^{n-2})=14\cdot2^{n-2}-2$.
The formula for $T^r$ includes $r=0$ and involves no eigenvalue division.

In the second term only site $0$ has degree four. Indices cannot
increase along the degree-two sites. Hence a maximum $R$ can be
taken at $0$, and the preceding index is at most $(R+1)/2$.
The degree-four inequality gives $2R\le(R+1)/2+3$, or $R\le2$.
After site $0$ every index is at most $1$. It is therefore enough,
without omitting any summand, to use indices $0,1,2$ and matrices

$$\widetilde T=\begin{pmatrix}2&0&0\\2&1&0\\2&2&0\end{pmatrix},
\qquad U=T_{X^2h}=\begin{pmatrix}2&2&0\\2&3&1\\2&4&2\end{pmatrix}.$$

Every displayed entry follows from the same binomial formula, including
the row and column corresponding to $2$. For $r\ge1$,

$$\widetilde T^r=
\begin{pmatrix}2^r&0&0\\2(2^r-1)&1&0\\3\cdot2^r-4&2&0\end{pmatrix}.$$

If $a=2^r$, the diagonal contributions to $U\widetilde T^r$ are
$6a-4$, $5$, and $0$. Therefore the second functional is
$\operatorname{tr}(U\widetilde T^{n-1})=6\cdot2^{n-1}+1$.
Subtracting the two traces gives exactly

$$[M]KP^4=2^{n-1}-3.$$

Combining this with the independently checked lower coefficients,

$$\begin{aligned}
[M]D_n
&=N(2^{n-1}-3)-(n-3)+N\\
&=2^{2n-1}-2^{n+1}-n+3\\
&=\frac{(2^n-2)^2}{2}+1-n.
\end{aligned}$$

All matrix entries and identities can be formed over the integers and
then reduced to characteristic $p$. The only displayed denominator
is $2$, invertible for every allowed $p$. Neither primality of $n$
nor $n\not\equiv0\pmod p$ is needed in this coefficient calculation.
In particular, no small-$n$ exception beyond $n\ge3$ was found.

## 7. Prime periods and the characteristic-three boundary

If prime $n\ne p$ satisfies $n\equiv1\pmod{p-1}$ and
$n\not\equiv1\pmod p$, Fermat's theorem gives $2^n=2$ in
$\mathbf F_p$. The decisive coefficient becomes $1-n\ne0$.
Since $p-1$ is even, these prime periods are odd and at least three.
Nonvanishing contradicts the necessary identity in Section 3 and
produces a bad ordinary cycle of least period exactly $n$.

The separate characteristic-three argument is also correct and
slightly stronger. In a field of characteristic three, $P^3=1$
at a point is equivalent to $P=1$. For any odd prime $n$, including
$n=3$, goodness would imply that $K(P-1)$ vanishes at all ordinary
roots. Since $2^n=-1$, its derivative annihilator is

$$K(-P-1)(P-1)=K(1-P^2).$$

Its $M$ coefficient is $0-(-1)=1$, contradicting vanishing. This
uses neither division by three nor a separability hypothesis and
establishes a bad cycle at every odd prime period in characteristic
three. The uniform proof does not depend on this extra check.

## 8. The elementary prime-period lemma, including all exclusions

The lemma asserting infinitely many suitable primes is valid; it is
not an unproved appeal to primes in an arbitrary progression.
Set $m=p-1\ge2$. The elementary cyclotomic facts used are
$\deg\Phi_m=\varphi(m)$, monicity, $\Phi_m(0)=1$, and
$T^m-1=\prod_{d\mid m}\Phi_d(T)$.
Since $m$ is even, $\varphi(m)\le m/2$.

Modulo $p$, each of $\Phi_m$ and $\Phi_m-1$ is nonzero and monic
of degree $\varphi(m)\ge1$. Their zero sets together contain at
most $2\varphi(m)\le p-1$ elements, so there is a residue $t$ for
which $\Phi_m(t)$ is neither zero nor one. Also $t\ne0$.

Assume the desired primes other than $p$ form a finite set $S$.
The CRT conditions

$$A\equiv0\pmod{m\prod_{q\in S}q},\qquad A\equiv t\pmod p$$

are compatible because $p$ divides neither $m$ nor any $q\in S$.
They admit arbitrarily large positive $A$. Monicity permits choosing
$A$ so that $V=\Phi_m(A)>1$.

Every prime factor $q$ of $V$ avoids $A$, since $\Phi_m(0)=1$;
therefore it avoids $m$ and $S$, all of whose prime factors divide
$A$. It avoids $p$ because $\Phi_m(t)\ne0$.
As $q\nmid m$, the reduction of $T^m-1$ modulo $q$ is squarefree,
so its cyclotomic factors have disjoint root sets. The nonzero
residue of $A$ is a root of $\Phi_m$ and hence has order exactly
$m$: any proper order dividing $m$ would make it a root of a
different factor in $T^d-1$. Thus $m\mid q-1$.

If every prime factor of $V$ were one modulo $p$, then their product,
with all multiplicities, would give $V\equiv1\pmod p$. But
$V\equiv\Phi_m(t)\not\equiv1$. Hence some prime factor also has
$q\not\equiv1\pmod p$, is different from $p$, and is outside $S$.
This is the required contradiction. It includes $p=3$, $m=2$;
for example the existence step there can take $t=1$, since
$\Phi_2(1)=2\pmod3$. No exceptional characteristic was discarded.

Combining the lemma with Section 7 gives infinitely many distinct
least periods and hence infinitely many distinct bad cycles. Their
odd periods ensure the required avoidance. All periods throughout
refer to one application of $f$, not to a replacement return map.

## 9. Repairs, source scope, and the withdrawn shortcut

No repair was needed in the final 526-line proof. The review checked
the full frozen statement, not just finitely many characteristics or
a finite collection of periods.
It did not infer existence from a nonzero divisor or from the fact
that elements of $k^*$ are roots of unity.

The provisional formula $P^4=\prod_i(X_i+2)$ is false in odd
characteristic and remains explicitly rejected. The actual identity is

$$P^4=\prod_i(X_i+1)^2
=\prod_i(X_{i+1}+2X_i+2).$$

The checked functional and traces retain these cross terms. The
withdrawn coefficient $2^{n+1}-n+3$ plays no role. This withdrawal
was author-self-initiated before the frozen proof; it is not represented
as a repair discovered or implemented by this review.

The residual theorem is self-contained apart from elementary algebra,
Fermat's theorem, the CRT, and the stated basic cyclotomic identities.
No external theorem on multiplier rigidity, finite multiplier spectra,
transversality, or periodic-point separability is imported. The
cyclotomic properties and elementary counting are classical inputs,
not a novelty claim. No primary-source query was needed or performed
for this full proof review, and no worldwide novelty assessment is
asserted. The R7 report is the separately accepted contextual input
for the following corollary, not an indispensable input to the R8 proof.

## 10. Exact atom-family corollary and what remains open

The accepted R7 input says: for every odd $p$, every $c\in k$, and
every $a\in k^\times$, with $f=x^2+c$ and
$g_a=(x-a)/(x+a)$, the cofinite good-cycle condition implies
$c=-1$ and $a\in\{1,-1\}$. Equivalently, every other parameter
in that single-atom family already has infinitely many bad ordinary
primitive cycles avoiding $\{a,-a\}$.

The R8 theorem closes $c=-1,a=1$. At $a=-1$, the atom is precisely
the reciprocal of the $a=1$ atom, so on every permitted cycle its
product is the reciprocal as well. A product different from $1$
remains different from $1$ after inversion.
The same infinitely many cycles therefore close $c=-1,a=-1$.
This establishes the advertised full single-quadratic-atom conclusion
when composed with the accepted R7 theorem. The extra avoidance of
$0$ in R8 only strengthens what the atom-family interface requires.

This composition does not claim prime-length bad cycles for every
noncritical R7 parameter: that stronger assertion has only been
proved here for the residual map. Nor does it imply the general
norm-one rational-function lemma, combinations of several atoms,
arbitrary degrees, or the general MS6 transfer/existence statement.
The separately established non-torsion of an individual atom is not
being promoted into such a missing implication.

## 11. Audit summary and handoff

The quotient basis, individual product, repeated-root annihilator,
fixed-point cancellation, cubic term, full quartic functional/traces,
prime-period lemma, characteristic-three branch, infinite-cycle
quantifier, and exact accepted-R7 interface all pass this independent
mathematical review. There are no open must-fixes in the frozen R8
author version and no requested author edits.

Only this allocated new review file was written. No mathematical
program, old checker, parameter census, numerical experiment, nested
agent, external model/API, GPU job, Git operation, manuscript/PDF,
or author/old/shared-file edit was used. All mathematical reconstructions
above were by hand. File reads and hashes are provenance checks, not
computational evidence for the theorem. No E2 assessment was used.

Final mathematical status: **PROVABLE AS STATED**, zero unresolved
mathematical/source-applicability must-fixes. General MS6 remains
outside this proved scope; contract admission remains with the root.
