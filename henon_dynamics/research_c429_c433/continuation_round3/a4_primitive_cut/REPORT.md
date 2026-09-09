# Round 3 A4 — primitive cut discriminants

2026-09-09 UTC. Frozen before substantial proof or mathematical execution. Exclusive author `/root/c429_a4_witt_local_data`; first-pass and Round 2 artifacts are read-only.

## Frozen mechanism and original target

For every odd prime $p$ and $e\geq1$, let $n=p^e$. Retain the E4-reviewed Round 2 definitions of primitive cycle necklaces, complement inertia $\iota$, the primitive branch polynomial $D(c)=\Delta_{n,n}(c)$, and its collision set $\mathcal K_{p,n}$. The original target is still **(CUT)**: every nonempty proper $\iota$-stable necklace set has a crossing primitive edge whose branch value is isolated on reduction. This implies global quotient transitivity, but is not equivalent to it.

The one mechanism to test is a **primitive discriminant budget versus a finite-edge cut bound**. For a complement-stable subset $S$, form over a branch splitting field

$$
H_S(c)=\prod_{\alpha\text{ labels an edge crossing }S}(c-\alpha),\qquad
J_S(c)=D(c)/H_S(c),
$$

after making $D$ monic by an odd-prime unit. First derive an exact algebraic condition for all roots of $H_S$ to lie in $\mathcal K_{p,n}$, then determine whether discriminant/resultant valuations impose a genuinely stronger obstruction than the already known total collision bound. The descent of $H_S$ to the ground DVR must be proved if used; a set of edges defined by necklaces is not automatically a $p$-adic Galois-stable set of branch roots.

Success is a uniform proof or refutation of (CUT), with its actual primitive collision labels. An auxiliary identity without a stronger uniform constraint will be labeled auxiliary and the proposed mechanism will be declared insufficient. The satellite polynomial $\Delta_{n,1}$ is excluded as a proxy for primitive collisions. One native tick remains $f_c(x)=x^2+c$.

## Accepted inputs and method boundary

The complete Round 2 report and its E4 review are accepted: generic quotient rank, exact component formula, infinity complementation, and the conditional surviving-edge specialization interface are not reopened as new claims. Primary sources will be checked for primitive discriminant bounds and graph resilience before asserting an increment. Relevant batch, proof-writer and research-lit instructions apply.

No mathematical program, isolated finite-period enumeration, old rerun, manuscript/PDF, formal evaluation, shared-file/Git write or external-model upload is allocated. A proposed execution would require a separate discriminating question and resource allocation from the coordinator.

## Status at freeze

**NOT CURRENTLY JUSTIFIED.** No new stronger bound or uniform theorem is claimed. `NO_BAD_EULER_OR_ROOT_NUMBER` remains unchanged.

## Outcome after the bounded attack

The original uniform (CUT) and the original global quotient assertion remain **NOT CURRENTLY JUSTIFIED**. No counterexample to either is established. The selected **total primitive-collision budget versus arbitrary-deletion resilience mechanism is refuted on an infinite native wild subfamily**, not merely left unchecked:

$$
\boxed{n=3^e,\ e\geq2:\quad
|\mathcal K_{3,n}|\geq 2n>\lambda_n,
\qquad v_3\operatorname{disc}\Delta_{n,n}\geq2n-1.}
\tag{NB}
$$

Here $\lambda_n$ is the minimum number of finite primitive edges crossing a nonempty proper complement-stable necklace subset. In particular, neither resilience after any $|\mathcal K_{3,n}|$ finite-edge deletions nor the source criterion requiring resilience after any $2v_3\operatorname{disc}\Delta_{n,n}$ deletions can hold for these periods. The actual colliding edges need not contain a minimum cut. Thus (NB) does **not** refute (CUT), and it does not imply reducibility or bad reduction.

This is an auxiliary mechanism-exclusion result, not a paper admission. It uses the actual primitive polynomial, an actual quadratic-family specialization, and a uniform proof. No isolated-period enumeration or mathematical program was performed.

## 1. Notation, assumptions and dependency map

For the algebraic identity below, $p$ is odd, $n=p^e$, and $D(c)$ is $\Delta_{n,n}(c)$ scaled to be monic over $\mathbb Z_p$. Its leading coefficient is a power of $2$, so the scaling does not change any valuation discussed here. Let $h=\deg D$ and $d=v_p\operatorname{disc}D$, with $v_p(p)=1$. Characteristic-zero simplicity of the primitive branch values is an imported input. All their roots are integral at odd primes.

Let $L/\mathbb Q_p$ be a finite field splitting $D$, $\mathcal O_L$ its valuation ring, and $\kappa$ its residue field. Use one fixed compatible sheet labeling as in Round 2. For a nonempty proper complement-stable necklace subset $S$, let $E(S)$ denote its crossing primitive branch labels. The monic polynomials $H=H_S$ and $J=J_S$ are in $\mathcal O_L[c]$; their coefficients are not assumed to lie in $\mathbb Z_p$.

For the uniform exclusion theorem only, specialize to $p=3$, $n=3^e\geq9$, and define

$$m=n/3,\qquad N=2^n-2^m,\qquad r=N/n,\qquad b=\frac{2^n+1}{3n}.$$

The accepted generic quotient has degree $r$ and complement inertia consists of $r/2$ pairs. Let $M$ denote the multiplicity of $c=-2$ in $D(c)\bmod3$. The residue field used for geometric point counts is $k=\overline{\mathbb F}_3$.

The proof dependencies are:

1. Exact cut algebra: rootwise derivative vanishing, discriminant and resultant identities.
2. Actual Chebyshev fiber: its $n$-cycles reduce to at most $r/2+(b+1)/2$ quotient points.
3. Trace-form corank plus mixed-characteristic discriminant conservation: $M\geq r/2-(b+1)/2$.
4. An elementary all-level inequality: $M\geq2n$.
5. A graph average-degree bound: $\lambda_n<2n$.
6. Hensel separation of the $c=-2$ branch cluster: $d\geq M-1$.

Inputs 2 and 3 build on source-owned Chebyshev descriptions and discriminant conservation; no new ownership is claimed for those ingredients. The all-level combination (NB) is the result being submitted for independent checking.

## 2. The exact algebraic condition for an isolating cut

**Lemma 1 (cut support, with descent caveat).** The following conditions are equivalent:

$$
E(S)\subseteq\mathcal K_{p,n};
\qquad v_p(D'(\alpha))>0\text{ for every root }\alpha\text{ of }H;
\qquad
\operatorname{rad}(\overline H)\mid\gcd(\overline D,\overline {D'}).
\tag{CS}
$$

Bars mean coefficient reduction to $\kappa$, and $\operatorname{rad}$ is the product of distinct monic irreducible factors. Furthermore,

$$
\begin{aligned}
\operatorname{disc}D&=\operatorname{disc}H\,\operatorname{disc}J\,
\operatorname{Res}(H,J)^2,\\
\prod_{H(\alpha)=0}D'(\alpha)
&=(-1)^{\deg H(\deg H-1)/2}\operatorname{disc}H\,\operatorname{Res}(H,J),\\
d&=v_p\operatorname{disc}H+v_p\operatorname{disc}J+2v_p\operatorname{Res}(H,J).
\end{aligned}
\tag{DR}
$$

**Proof.** For a root $\alpha$ of the monic separable polynomial $D$,

$$D'(\alpha)=\prod_{\beta\ne\alpha}(\alpha-\beta).$$

Every factor is integral. Its valuation is positive exactly when at least one distinct root has the same residue. This proves the first equivalence. Evaluation commutes with reduction, so the derivative vanishes at every root of $\overline H$ exactly when its squarefree support divides the displayed gcd. Factoring all pairwise root differences into the within-$H$, within-$J$ and between-factor pairs gives the first identity in (DR). For a root of $H$, $D'(\alpha)=H'(\alpha)J(\alpha)$; taking its product gives the second identity. Taking normalized valuations gives the third. $\square$

This is an exact reformulation, not a new obstruction by itself. In particular, the *product* in (DR) having positive valuation means only that at least one crossing label collides; (CS) requires all of them. Also, individual positive valuations may be fractional in $L$. A necklace-defined $S$ need not make $H$ descend to $\mathbb Z_p[c]$, so no integer-valued per-root charge or Galois norm shortcut may be inserted.

For comparison, the generic source-owned count bound is

$$|\mathcal K_{p,n}|\leq2d.\tag{CB}$$

One proof useful for checking its scope is as follows. If the reduction of $D$ has $t$ distinct geometric roots, then the trace pairing of $\overline{\mathbb F}_p[c]/\overline D$ has rank at most $t$: its nilradical is in the pairing radical. A discriminant matrix over the completed maximal unramified extension of $\mathbb Z_p$ therefore has valuation at least $h-t$. Each residue cluster of size $a\geq2$ contributes $a$ to the collision count and $a-1$ to $h-t$, and $a\leq2(a-1)$. This proves (CB), without referring to any edge incidence. For a general monic polynomial the factor $2$ cannot be reduced: $(c-a)^2-p$ has two colliding roots and discriminant valuation one. This control polynomial is not a quadratic-family counterexample.

The remaining sections establish a stronger actual-family constraint. Its direction is unfavorable to the budget mechanism: the true primitive collision count itself exceeds a graph cut size.

## 3. Actual quotient-fiber loss at the Chebyshev parameter

**Lemma 2 (a uniform fiber bound).** Let $t$ be the number of geometric closed points in the special fiber of the integral quotient model $Y_0(n)$ over $c=-2$. For $n=3^e\geq9$,

$$t\leq\frac r2+\frac{b+1}{2}.\tag{F}$$

**Proof, Step 1: characteristic-zero periodic points.** The identity

$$f_{-2}(z+z^{-1})=z^2+z^{-2}$$

identifies the roots of $\Phi_n(x,-2)$ with the following two disjoint sets, each taken modulo $z\sim z^{-1}$:

$$
U_-:=\mu_{2^n-1}\setminus\mu_{2^m-1},\qquad
U_+:=\mu_{2^n+1}\setminus\mu_{2^m+1}.
$$

To check the exclusions, every proper divisor of $n$ divides $m$, so points of period properly dividing $n$ are exactly those of period dividing $m$. The cross-sign intersections contain only $1$: writing $a=2^m$, one has $\gcd(a^3-1,a+1)=\gcd(a^3+1,a-1)=1$ since these integers are odd. Within each set inversion is fixed-point-free, because $1$ is excluded and $-1$ belongs to none of the odd-order groups. Thus each contributes $N/2$ distinct $x$-values. Their union has $N=\deg_x\Phi_n$ values and consists of exact period-$n$ points. Squaring induces the native iteration; each of the two types contains $r/2$ cycles.

**Step 2: reduction of the minus type.** Since $n$ is odd, $3\nmid2^n-1$. Reduction is injective on $\mu_{2^n-1}$. The identity $z+z^{-1}=w+w^{-1}$ implies $w=z$ or $z^{-1}$ over every field, so reduction remains injective on its inversion classes. Squaring acts by the same finite permutation before and after reduction. Therefore the minus type still gives exactly $r/2$ native $n$-orbits in the special point set.

**Step 3: reduction of the plus type.** One has

$$v_3(2^{3^e}+1)=e+1.$$

For completeness, start with $v_3(2+1)=1$. If $A\equiv-1\pmod3$, then $A^3+1=(A+1)(A^2-A+1)$ and, writing $A=-1+3q$, the second factor is $3(1-3q+3q^2)$ of valuation one. Induction proves the assertion. Thus $b=(2^n+1)/3^{e+1}=(2^n+1)/(3n)$ is an odd integer prime to $3$. Reduction of the plus roots is contained in $\mu_b$. Its inversion quotient has $(b+1)/2$ elements, hence at most that many distinct $x$-values or native orbits. This is only an upper bound; it does not assume that these residual orbits retain period $n$.

**Step 4: passing to the integral quotient.** Put $R=W(k)$ and $A=R[c,x]/\Phi_n$. The quotient ring is $A^{C_n}$. The map $\operatorname{Spec}A\to\operatorname{Spec}A^{C_n}$ is integral and surjective, and remains surjective after taking the fiber over $(3,c+2)$. Every orbit of geometric point-cover roots maps to one quotient point. Thus the number of quotient points is at most the number of such orbits. Every special point-cover root is the reduction of one of the displayed characteristic-zero roots: $\Phi_n(x,-2)$ is monic, splits into integral roots after a finite extension, and its reduction is the product of their reductions with multiplicities. Combining Steps 2 and 3 proves (F).

No assertion that cyclic invariants commute with arbitrary nonflat reduction is used. Surjectivity and constancy on orbits suffice for this upper bound. The quotient model here is the source's normal integral model, not the normalization of its special fiber. $\square$

## 4. Primitive branch multiplicity and the discriminant lower bound

**Lemma 3 (trace-form bound on the actual primitive cluster).** With the above notation,

$$
M\geq r-t\geq\frac r2-\frac{b+1}{2},
\qquad d\geq M-1.
\tag{PM}
$$

**Proof, Step 1: identify the correct local model.** Complete the quotient over $R[c]$ at $(3,c+2)$, writing $u=c+2$. Its ring $B$ is a normal finite flat $R[[u]]$-algebra of rank $r$; its special fiber $B_k$ is reduced and generically separable over $k[[u]]$. These are the accepted odd-characteristic quotient-model inputs. The normality is of the two-dimensional integral model and does not assert normality of $B_k$. Flatness can also be checked here from normality: a finite normal algebra over the regular local ring $R[[u]]$ is Cohen--Macaulay in dimension two and hence free as a module over that ring.

The finite characteristic-zero ramification of the quotient consists exactly of the simple primitive branch values, each contributing one to the trace discriminant degree. The ones contained in this formal disk are precisely those reducing to $c=-2$. Mixed-characteristic discriminant conservation therefore gives

$$\operatorname{ord}_u\operatorname{disc}(B_k/k[[u]])=M.$$

This is the source's Proposition 5.3 together with the primitive-branch identification in Lemma 10.6, with reducedness and generic separability retained. It is not a formula for the discriminant of the normalization of $B_k$.

**Step 2: take a trace-form corank.** The $k$-algebra $C=B_k/uB_k$ has dimension $r$ and exactly $t$ geometric maximal ideals. Its reduced quotient is $k^t$. For any nilpotent $a\in C$ and any $b\in C$, multiplication by $ab$ is nilpotent and therefore has trace zero. The nilradical is consequently in the radical of the trace pairing, so its rank is at most $t$. Reducing a trace matrix for $B_k$ modulo $u$ gives this pairing. Smith normal form over the DVR $k[[u]]$ then gives discriminant valuation at least $r-t$. This and Lemma 2 prove the first inequalities in (PM). Possible wild trace degeneracy only strengthens them.

**Step 3: transfer the cluster size to $d$.** Hensel factorization over $\mathbb Z_3$ gives

$$D=D_{-2}E,\qquad\overline D_{-2}=(c+2)^M,\qquad\overline E(-2)\ne0,$$

with both factors monic and their resultant a $3$-adic unit. The order $\mathbb Z_3[c]/D_{-2}$ is free of rank $M$, and its reduction has one geometric point. The same trace-rank argument, now for its reduction modulo $3$, proves $v_3\operatorname{disc}D_{-2}\geq M-1$. The product discriminant identity and nonnegative valuation of $\operatorname{disc}E$ give $d\geq M-1$. $\square$

**Lemma 4 (all-level size comparison).** For every integer $n\geq9$ of the form $3^e$,

$$\frac r2-\frac{b+1}{2}=\frac{2^{n+1}-3\cdot2^{n/3}-1-3n}{6n}\geq2n.$$

**Proof.** Write $A=2^n$ and $B_0=2^{n/3}$. Since $n-n/3\geq6$, $B_0\leq A/64$. Also

$$2^n\geq\frac{512}{81}n^2\quad(n\geq9):$$

there is equality at $n=9$, and the ratio $2^n/n^2$ increases with integer $n\geq3$ because $2n^2>(n+1)^2$. Therefore

$$
\begin{aligned}
2A-3B_0-1-3n-12n^2
&\geq\frac{125}{64}A-1-3n-12n^2\\
&\geq\frac{28}{81}n^2-3n-1\\
&=\frac{(n-9)(28n+9)}{81}\geq0.
\end{aligned}
$$

Dividing by $6n$ proves the claim. This boundary arithmetic is part of a uniform inequality, not a finite-period factorization or enumeration. $\square$

It follows that $M\geq2n\geq18$. All $M$ characteristic-zero primitive roots in this residue cluster belong to $\mathcal K_{3,n}$, so $|\mathcal K_{3,n}|\geq M\geq2n$. Lemma 3 also gives $d\geq2n-1$.

## 5. The graph cannot tolerate that many arbitrary deletions

**Lemma 5 (minimum cut upper bound).** For $n=3^e\geq9$,

$$\lambda_n<2n.$$

**Proof.** Contract every complement pair in the characteristic-zero graph. There are $q=r/2\geq2$ vertices in the resulting multigraph. Retain the finite edges, with their multiplicities; loops never cross a cut. Cuts in this multigraph are exactly the complement-stable cuts in the original graph. Its number of nonloop edges is at most $h=\deg D$. A vertex of minimum nonloop degree gives

$$\lambda_n\leq\frac{2h}{q}=\frac{4h}{r}.$$

The multiplier polynomial satisfies $\deg_c\delta_n(1,c)=N/2$. One can check this from the accepted infinity expansions: with $c=-t^{-2}$ every native multiplier has a nonzero leading term of order $t^{-n}$; their product over $r$ cycles has order $t^{-nr}=t^{-N}$. Thus the polynomial in $c$ has degree $N/2$. The factorization

$$\delta_n(1,c)=\Delta_{n,n}(c)\prod_{d_0\mid n,\ d_0<n}\Delta_{n,d_0}(c)$$

has a positive-degree satellite factor, for example $\Delta_{n,1}$ has degree $\varphi(n)>0$. Therefore $h<N/2=nr/2$, proving $\lambda_n<2n$. This use of the satellite is only a characteristic-zero degree subtraction, not a proxy for any primitive collision. $\square$

Combining Lemmas 3--5 proves (NB). Since $|\mathcal K_{3,n}|>\lambda_n$, there exists a set of at most $|\mathcal K_{3,n}|$ finite edges whose deletion disconnects the graph. Consequently the hypothesis of connectivity after *any* that many deletions is false. The same follows for the larger $2d$ allowance. No claim is made that this disconnecting edge set consists of actual colliding labels.

## 6. Source subtraction and exact remaining gap

The source used is Doyle--Krieger--Obus--Pries--Rubinstein-Salzedo--West, *Reduction of dynatomic curves*, published in *Ergodic Theory and Dynamical Systems*. The [primary accepted manuscript](https://api.repository.cam.ac.uk/server/api/core/bitstreams/17388c5b-06f8-4235-afed-8ae9a331c5f3/content) supplies the quotient model and specialization machinery (§§5--6, 8), the two-edge graph theorem (Theorem 9.1), and the conditional $2d$-deletion criterion (Proposition 8.6). These are source-owned inputs, not contributions here. Its [arXiv v2](https://arxiv.org/html/1703.04172v2) gives the Chebyshev point description (Lemma 10.3) and the primitive multiplicity interpretation (Lemma 10.6); the $2d$ statement is numbered Remark 8.6 there. Its detailed prime-period ramification formulas are not used for composite $3^e$. Targeted source searches did not locate the uniform comparison (NB); this absence is not a novelty certificate.

The previous-round primary-source exclusions remain in force: Bousch's characteristic-zero theorem, the corrected Morton distinct-root criteria, and LRL's small-cycle theorem do not establish the missing wild quotient transitivity. No source result on smoothness for individual periods is promoted to an all-$e$ statement.

The exact remaining arithmetic-combinatorial gap is still the incidence condition (CS): show that **no** complement-stable necklace cut has all its crossing labels in the actual collision set, or establish connecting monodromy from the colliding clusters themselves. A sharper *upper bound on total collision count alone*, combined with resilience after arbitrary deletions, cannot close this gap uniformly because (NB) already excludes it for every $3^e\geq9$. Incidence or cluster monodromy is essential to any continuation of this particular bridge. Other methods of quotient irreducibility remain possible.

## 7. Verification and disposition

The original (CUT)/(GQ) retains status **NOT CURRENTLY JUSTIFIED**. The cut identity and mechanism-exclusion theorem (NB) have complete proofs above and are handed to an independent reviewer; neither is presented as reviewed before that check. The proof-writer skill led to the explicit split between the original target, the proven weaker output and the exact gap. Research-lit enforced primary-source subtraction and the distinction between prime-period formulas and the composite levels here.

No mathematical execution, old rerun, isolated-period enumeration, manuscript/PDF build, formal evaluation, shared-file modification, Git operation or external-model upload occurred. Only this allocated report was edited. No paper admission is requested. `NO_BAD_EULER_OR_ROOT_NUMBER` is unchanged.
