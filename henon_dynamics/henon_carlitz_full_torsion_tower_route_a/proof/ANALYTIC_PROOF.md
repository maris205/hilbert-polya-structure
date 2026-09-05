# C389: full Carlitz torsion, dynamics, and ramified towers

## Claim, status, and assumptions

Status: PROVABLE AS STATED. Let $q=p^e$ be any prime power, $A=\mathbb F_q[\theta]$, and $K=\mathbb F_q(\theta)$. The base field is exactly $K$, not an arbitrary extension. Define the additive polynomial $C_\theta(X)=\theta X+X^q$, put $C_c(X)=cX$ for $c\in\mathbb F_q$, and extend by addition and composition to $C:A\to A\{\tau\}$. Here $\tau(X)=X^q$ and $\tau c=c^q\tau$. For monic nonzero $a\in A$, write $\Lambda_a=\ker C_a\subset K^{\rm sep}$ and $L_a=K(\Lambda_a)$.

We prove, uniformly in $q,a,b$ and all monic irreducibles $P$ and levels $k\geq1$: the cyclic $A/a$ torsion module; exact annihilator strata and all multiplier preperiods and periods; fixed-point and native finite determinant formulas; primitive prime-power Eisenstein polynomials; full Galois groups and compatible inverse towers; finite-prime ramification, lower ramification groups and different exponents; and full composite-conductor Galois groups. This is a self-contained synthesis of classical Carlitz cyclotomic structure, not a claim of literature priority. The finite code audits identities and finite ring models; it does not prove infinite quantifiers.

No claim concerns target Euler factors, root numbers, automorphy, target zeros or functional equations, a Hilbert--Polya operator, or Route B. The scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Notation and dependency map

For monic $D$, let $\Phi(D)=|(A/D)^\times|$, with $\Phi(1)=1$. Write $v_P$ for the exponent of $P$ on $K$, normalized by $v_P(P)=1$. At level $P^k$, set $Q=q^{\deg P}$ and $e_k=(Q-1)Q^{k-1}$. The identity group in ramification formulas is denoted $\{1\}$; the identity polynomial of the ring action is $C_1(X)=X$.

Dependency order: ring construction and separability -> cyclic modules and exact dynamics -> critical reduction lemma -> Eisenstein irreducibility and full prime-power Galois groups -> local valuation and unramified-away lemma -> disjointness and all conductors -> compatible towers and ramification filtration. The only general field-theoretic tools used below are Eisenstein's criterion, the elementary Hensel lifting lemma for simple roots, and the local different formula for an explicitly justified monogenic extension. No class field theory or Carlitz exponential theorem is invoked.

## 1. Ring action and reduced torsion

For $a=\sum_{j=0}^d a_j\theta^j$, define $C_a=\sum_j a_jC_\theta^{\circ j}$. Constants from $\mathbb F_q$ commute with $C_\theta$, so expansion gives $C_{a+c}=C_a+C_c$, $C_{ac}=C_a\circ C_c=C_c\circ C_a$, and $C_1=X$. Induction on $j$ gives $\deg_X C_\theta^{\circ j}=q^j$ with leading coefficient one. Consequently $\deg_X C_a=q^{\deg a}$, with leading coefficient the leading coefficient of $a$, and $C_a'(X)=a(\theta)$. Nonzero $a$ has nonzero derivative in $K$; hence $C_a$ has precisely $q^{\deg a}$ distinct roots in $K^{\rm sep}$. The finite group scheme is reduced, and every geometric torsion root has multiplicity one. This is algebraic separability, not a Lyapunov stability assertion.

For a root $x$, the ideal $\operatorname{Ann}(x)=\{a:C_a(x)=0\}$ is principal. A point has exact annihilator $D$ when this ideal is $(D)$ with $D$ monic. For $x=0$ it is $(1)$.

## 2. Cyclicity, CRT, and all multiplier clocks

For $a=P^k$, the proper inclusion $\Lambda_{P^{k-1}}\subset\Lambda_{P^k}$ follows from their respective cardinalities $Q^{k-1}<Q^k$. Choose $\lambda_k$ in the difference. Its annihilator divides $P^k$ but not $P^{k-1}$, so it is $P^k$. The map $A/P^k\to\Lambda_{P^k}$, $r\mapsto C_r(\lambda_k)$, is injective, and equal cardinalities make it an isomorphism.

For coprime $u,v$, choose $r,s$ with $ru+sv=1$. If $x\in\Lambda_{uv}$, the decomposition

$$x=C_{sv}(x)+C_{ru}(x)$$

has summands in $\Lambda_u$ and $\Lambda_v$. Their intersection is zero by the same Bezout identity. Iteration gives $\Lambda_a=\bigoplus_{P^k\parallel a}\Lambda_{P^k}\cong A/a$. A generator can be obtained by summing generators of the primary summands. In $A/a$, exact-annihilator-$D$ points correspond to $(a/D)r$ with $r$ a unit modulo $D$. Thus their number is $\Phi(D)$ and $\sum_{D\mid a}\Phi(D)=q^{\deg a}$.

Fix any $b\in A$ and consider the finite map $T_b=C_b|_{\Lambda_a}$. If $x$ has annihilator $D$, then $C_c(C_bx)=0$ exactly when $D\mid cb$. The new annihilator is therefore $D/\gcd(D,b)$. Suppose $b\ne0$. Let

$$D_* = \prod_{P\nmid b}P^{v_P(D)},\qquad h_D=\max_{P\mid b}\left\lceil\frac{v_P(D)}{v_P(b)}\right\rceil,$$

where the maximum of an empty collection, and the terms with $v_P(D)=0$, are zero. After $j$ steps, the exponent at $P\mid b$ is $\max(v_P(D)-jv_P(b),0)$; the other exponents remain unchanged. A strictly decreasing annihilator cannot occur on a cycle. At step $h_D$ the remaining annihilator is $D_*$, on which $b$ is invertible. Hence the exact preperiod is $h_D$, and the exact eventual period is $\operatorname{ord}_{D_*}(b)$, with $\operatorname{ord}_1(b)=1$. The formula concerns the time clock of a chosen multiplier $b$, whereas conductor exponent $k$ is a tower depth, not that time clock.

For $b=0$, zero is fixed and every nonzero point has preperiod one and eventual period one. For $b=1$, every point is fixed. For $a=1$, the only point is zero for every $b$.

For all $n\geq1$, multiplication by $b^n-1$ on $A/a$ has a kernel of size

$$F_n(a,b)=q^{\deg\gcd(a,b^n-1)}.$$

Indeed, if $g=\gcd(a,b^n-1)$, cancellation of the coprime factors shows that precisely the multiples of $a/g$ lie in this kernel. Adopt $\gcd(a,0)=a$. This also handles $b=0$ and $b=1$. Exact primitive cycle populations are

$$O_n(a,b)=\frac1n\sum_{d\mid n}\mu(n/d)F_d(a,b).$$

They are nonnegative integers because each finite functional graph consists of directed cycles with rooted incoming trees. Möbius inversion of $F_n=\sum_{d\mid n}dO_d$ proves the formula.

Let $U_b$ be pullback on all complex-valued functions on $\Lambda_a$. The characteristic polynomial of its transpose (the point-map matrix) can be ordered by distance to a cycle; transient vertices give a nilpotent block, and a cycle of length $d$ gives a permutation block. Thus

$$\det(I-zU_b)=\prod_{d\geq1}(1-z^d)^{O_d},\qquad
\exp\!\left(\sum_{n\geq1}\frac{F_nz^n}{n}\right)=\det(I-zU_b)^{-1}.$$

The products are finite. Nonunit $b$ must not be called a permutation on all torsion. These are source-native finite determinants, already part of general finite-map theory; they do not provide a target A2 divisor.

## 3. Critical reduction lemma

For every monic irreducible $P$ of degree $d$, the coefficient reduction in $A/P=\mathbb F_Q$ satisfies

$$\overline{C_P}(X)=X^Q.$$

Proof: the polynomial is monic of degree $Q$, and its derivative is $\overline P=0$. Suppose it had a nonzero root $\gamma$ in an algebraic closure of $\mathbb F_Q$. The reduced ring action $a\mapsto\overline C_a$ is still a ring action, and the map $A\to\overline{\mathbb F_Q}$, $a\mapsto\overline C_a(\gamma)$, has an annihilator ideal containing $(P)$. This ideal is proper since $\overline C_1(\gamma)=\gamma\ne0$. Maximality of $(P)$ makes the annihilator exactly $(P)$, so this map has $Q$ distinct values. Commutation with $\overline C_P$ makes every such value a root of $\overline C_P$. A polynomial of degree $Q$ with zero derivative cannot have $Q$ distinct roots: in characteristic $p$ all its positive exponents are divisible by $p$, so each root has multiplicity at least $p$. This contradiction leaves zero as the only root. Monicity and degree give $X^Q$. The argument establishes the specific Carlitz reduction; it does not assume an arbitrary additive polynomial reduces to Frobenius.

## 4. Primitive polynomials and full prime-power Galois groups

Define

$$\Psi_P(X)=C_P(X)/X,\qquad
\Psi_{P^k}(X)=\Psi_P(C_{P^{k-1}}(X)).$$

The identity $C_P(Y)=Y\Psi_P(Y)$ shows

$$C_{P^k}(X)=C_{P^{k-1}}(X)\Psi_{P^k}(X).$$

Separability in generic characteristic here means the derivative $P^k$ is nonzero in $K$; the ambient field has characteristic $p$. The quotient roots are exactly $\Lambda_{P^k}\setminus\Lambda_{P^{k-1}}$, each simple. The degree is $e_k$. The reduction lemma gives $\overline\Psi_{P^k}=X^{e_k}$; its constant coefficient is precisely $P$, because $C_{P^{k-1}}(0)=0$. Every other nonleading coefficient is divisible by $P$. Consequently $\Psi_{P^k}$ is Eisenstein at $P$, hence irreducible over $K$.

For any primitive root $\lambda_k$, every $P^k$-torsion point is $C_r(\lambda_k)$, so $K(\lambda_k)$ is the full splitting field and is Galois. An automorphism sends $\lambda_k$ to $C_u(\lambda_k)$ for a unique $u\in(A/P^k)^\times$. Conversely irreducibility gives $[K(\lambda_k):K]=e_k=|(A/P^k)^\times|$. The injective homomorphism from the Galois group to this unit group is therefore bijective. This proves surjectivity, not merely a faithful action.

## 5. Local ownership, disjointness, and all conductors

Complete at $P$. An Eisenstein polynomial of degree $e_k$ produces an extension of degree $e_k$, residue degree one, ramification index $e_k$, and a uniformizer $\lambda_k$. For completeness, any extension valuation of a root must satisfy $v_P(\lambda_k)=1/e_k$: a nonpositive valuation leaves its monic leading term uniquely minimal; for a positive valuation every nonconstant nonleading term has valuation strictly greater than one, so cancellation requires $e_kv_P(\lambda_k)=1$. The fractional valuation forces ramification index at least $e_k$ and the polynomial degree bounds it above. The full global degree is already $e_k$, so $P$ has a unique place in $L_{P^k}$ and is totally ramified.

If a finite prime $R\ne P$, then $C_{P^k}$ has coefficients integral at $R$, is monic, and has derivative the unit $P^k$. Its reduction has distinct roots over an algebraic closure of the residue field. Those roots lie in some finite residue extension; pass to the corresponding unramified extension of the complete field $K_R$. Hensel's lemma lifts each simple residue root uniquely to a root there. The degree many roots exhaust the polynomial, so its splitting field embeds in an unramified extension. Thus $L_{P^k}/K$ is unramified at every such finite $R$.

Take distinct $P_1,\ldots,P_s$ with exponents $k_i$. Inductively the compositum of the first $s-1$ towers is unramified at $P_s$: after completion it lies in a compositum of unramified local extensions, whose residue extensions compose and remain unramified. Its intersection with $L_{P_s^{k_s}}$ is both unramified and totally ramified at $P_s$. A subfield of the latter extension has one place and local degree equal to its global degree, whereas an extension both unramified and totally ramified has degree one. The intersection is $K$. Since these are Galois extensions, the two fields are linearly disjoint. Induction gives degree $\prod_i\Phi(P_i^{k_i})$ and direct-product Galois group. The module CRT identifies the compositum with $L_a$ for $a=\prod_iP_i^{k_i}$ and identifies its Galois group with $(A/a)^\times$.

No assertion describes infinity ramification, the full maximal abelian extension, or all constant extensions. These need additional owners and are unnecessary for the finite-prime conclusions.

## 6. Compatible infinite towers and exact ramification filtration

Choose a primitive $\lambda_1$. Given primitive $\lambda_k$, choose a root of $C_P(X)=\lambda_k$ in $K^{\rm sep}$. It is killed by $C_{P^{k+1}}$ but not by $C_{P^k}$, since otherwise applying $C_{P^{k-1}}$ to $\lambda_k$ would give zero. Thus it is primitive and may be named $\lambda_{k+1}$. The field inclusions are compatible; an automorphism indexed by $u$ at level $k+1$ restricts to its reduction modulo $P^k$. Every unit class lifts to a unit class at the next level. Hence

$$\operatorname{Gal}\left(\bigcup_{k\geq1}L_{P^k}/K\right)
 =\varprojlim_k(A/P^k)^\times=A_P^\times.$$

Here $A_P=\varprojlim A/P^k$ is the completed local ring, with its inverse-limit topology. An automorphism of the union is determined by compatible restrictions; compatible restrictions glue on the union, which proves the displayed equality of profinite groups.

Normalize $v_{L_k}(\lambda_k)=1$. For $\sigma_u\ne1$, put $s=v_P(u-1)<k$, where any lift modulo $P^k$ gives the same $s$. Write $u-1=P^sv$ with $v$ a unit. Then

$$\sigma_u(\lambda_k)-\lambda_k=C_v(C_{P^s}(\lambda_k)).$$

This is primitive of level $k-s$. Its base valuation is $1/e_{k-s}$ by the already proved Eisenstein result, so its $L_k$ valuation is $e_k/e_{k-s}=Q^s$.

To justify computing ramification from this one element, the local integer ring is $\mathcal O_{K_P}[\lambda_k]$. Indeed $1,\lambda_k,\ldots,\lambda_k^{e_k-1}$ is a field basis. For $x=\sum_{j=0}^{e_k-1}a_j\lambda_k^j$, the nonzero summands have valuations $e_kv_P(a_j)+j$ distinct modulo $e_k$. The minimum is unique, so $x$ is integral exactly when all $a_j$ are integral. For every integral polynomial in $\lambda_k$, its difference under $\sigma$ is divisible by $\sigma(\lambda_k)-\lambda_k$, with an integral quotient. The minimum difference valuation over the full integer ring is therefore attained at $\lambda_k$. In the lower numbering $G_i=\{\sigma:v_{L_k}(\sigma x-x)\geq i+1\ \forall x\in\mathcal O_{L_k}\}$, this yields

$$G_0=(A/P^k)^\times,\qquad
G_i=1+P^s\pmod {P^k}\quad
(Q^{s-1}\leq i\leq Q^s-1,\ 1\leq s<k),$$

and $G_i=\{1\}$ for $i\geq Q^{k-1}$. For $k=1$ the intermediate ranges are empty. For $Q=2,k=1$, even $G_0$ is trivial, which agrees with the degree-one Eisenstein polynomial.

The different exponent is

$$d_k=\sum_{i\geq0}(|G_i|-1)
=(e_k-1)+\sum_{s=1}^{k-1}(Q^s-Q^{s-1})(Q^{k-s}-1)
=Q^{k-1}\bigl(k(Q-1)-1\bigr).$$

This also follows from the monogenic different formula $\mathfrak D=(\Psi'_{P^k}(\lambda_k))$. Differentiate $C_{P^k}=C_{P^{k-1}}\Psi_{P^k}$ at $\lambda_k$ to obtain $P^k=\lambda_1\Psi'_{P^k}(\lambda_k)$; therefore its normalized valuation is $ke_k-Q^{k-1}$. Both computations agree, including the tame first level and the $Q=2$ boundary.

## 7. Structural controls and target obstruction HEN-O373

The rank-zero parent action $a\mapsto aX$ has only zero torsion for nonzero $a$, so nonzero torsion is not an arbitrary label on scalar dynamics. Distinct-prime conductor $PQ$ yields a CRT product, whereas conductor $P^2$ has the principal-unit filtration and wild layer; their equal-size coincidences, if any, do not identify their ring actions. The neighboring rank-one action $C_\theta^{(u)}=\theta X+uX^q$ for $u\in K^\times$ is geometrically conjugate: choose $v$ with $uv^{q-1}=1$, and multiplication by $v$ conjugates it to the frozen action. That conjugacy need not be defined over $K$, so base-field Galois conclusions for arbitrary twists are not silently inherited.

The strict judgement is $(\mathrm{A0\_STRUCTURAL\_ARITHMETIC\_RELATION},\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},\mathrm{A3\_FAIL},\mathrm{A4\_FAIL})$, overall `ROUTE_A_EXPLORATORY`. There is an intrinsic function-field prime and ramification carrier, and exact source cycle clocks. Function-field irreducibles are not rational primes, no rational-prime logarithmic orbit clock is established, and none of the evaluator's six mandatory strong-A1 controls is completed. Finite native determinants do not identify the target divisor. No target completion, counting law, Weil compression, quantum construction, or Hilbert--Polya domain is supplied. Route B remains disabled.

## Open risks and evidence boundary

No open step remains in the stated source theorem. General finite-field ring calculations are only finite regressions; symbolic checks test displayed identities, not a proof assistant certification. Sources are credited as classical ownership. Infinity, maximal class field theory, numeric-specialization transfers, and target arithmetic are outside the theorem. Reviewer and executable receipts must be recorded only after their actual runs.
