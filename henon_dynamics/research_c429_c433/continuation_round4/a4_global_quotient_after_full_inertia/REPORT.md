# Round 4 A4 — the global quotient after full local inertia

2026-09-09 UTC. Frozen before substantial proof. Exclusive author `/root/c429_a4_witt_local_data`; all first-pass, Round 2 and Round 3 files remain read-only.

## Original full question and present inputs

For every odd prime $p$ and $e\geq1$, with $k=\overline{\mathbb F}_p$, $F=k(c)$, $n=p^e$ and $m=p^{e-1}$, classify the geometric irreducible components of the reduced native dynatomic curve

$$\Phi_n(x,c)=\frac{f_c^{\circ n}(x)-x}{f_c^{\circ m}(x)-x}=0,\qquad f_c(x)=x^2+c.$$

The intended irreducibility bridge is that the cycle quotient

$$B_n=(F[x]/\Phi_n)^{C_n},\qquad\dim_F B_n=(2^n-2^m)/n,$$

is a field. One application of $f_c$ remains one native tick. No restricted parameter family or finite-period check replaces this all-odd-$p$, all-$e$ question.

Accepted Round 2 supplies the quotient rank and component formula, not quotient transitivity. E4-reviewed Round 3 proves that scalar arbitrary-deletion budgets fail for every $n=3^e\geq9$; that mechanism is excluded from this round. A3's new `continuation_round3/a3_interlevel_contacts/FULL_LOCAL_INERTIA.md` was read in full. It supplies full $C_{p^e}$ inertia of the canonical small cycle, **conditional here until its independent final review closes**. This is A3's proof, not an A4 increment.

## One selected mechanism

Test **actual residue-cluster monodromy**, beginning with the Chebyshev specialization $c=-2$. The cyclotomic parametrization gives exact root reductions and native cycle incidence there; unlike a total discriminant allowance, a proved geometrically unibranch special germ yields a specific local inertia orbit. Determine whether these orbit identifications, compatibly transported and combined with surviving primitive transpositions and infinity complementation, connect all quotient sheets. A special point of large scheme-theoretic length is not assumed unibranch.

The source-first task is to check applicable odd-characteristic quotient-model, local normalization and specialization results, including whether any later irreducibility theorem already closes this wild case. The decisive success is a uniform quotient-transitivity theorem or a rigorous counterexample to the full question. A failed local-cluster bridge must report the precise missing unibranchness/incidence statement, not just restate a scalar budget. For $p\geq5$ dividing $n$, the absence of Chebyshev collisions is an explicit scope test to establish, not a reason to silently narrow the original question to $p=3$.

## Boundaries and status

**NOT CURRENTLY JUSTIFIED** for the full global assertion. No new quotient connectivity or component count is claimed at freeze. No mathematical census or program, old rerun, manuscript/PDF, external-model upload, shared-file or Git write is allocated. Only this report and a proof-only supplement if genuinely necessary may be written. `NO_BAD_EULER_OR_ROOT_NUMBER` remains unchanged.


## Outcome and dependency update

The selected Chebyshev-cluster bridge does not prove the original global question. Its failure is now an **actual incidence obstruction**, not the scalar deletion obstruction from Round 3: even granting arbitrary mixing inside every actual Chebyshev reduction class, adjoining infinity complementation leaves a specified pair of cycle sheets isolated when $p=3$ and $e\geq2$. When $p\geq5$, all these reduction classes are singletons and the same proposed generating mechanism gives only complement pairs.

This concerns a precisely defined subgroup/graph on characteristic-zero cycle sheets. It is **not** a counterexample to (CUT), (GQ), or geometric irreducibility in characteristic $p$: primitive inertia away from this one specialization can connect the displayed classes. No identification with the entire special-fiber monodromy group is claimed.

A3's independent final review has now been read in full:
[E6 full-local review](../../continuation_round3/reviews/e6_full_local_inertia/REVIEW.md), PASS with zero open mathematical/source must-fixes, binding the full-local proof to SHA-256 `0a4f4ff66b633de268d741142502c1b4244868b9eccd3eb040ae472e0b296250`. Its all-level local conclusion is therefore used below as reviewed input, not left conditional or re-proved here.

The source and proof audit produces three auxiliary outputs: the exact local-to-global consequence in §1, the complete Chebyshev reduction-class degrees in §2, and the explicitly labeled two-sheet obstruction in §3. Section 4 gives a concrete local smoothness condition and the remaining global transport/incidence gap. **PC424-D remains unresolved; no weakened paper is proposed.**

## 1. What full local inertia now proves globally

Write $A_n=F[x]/\Phi_n$ and $B_n=\prod_{j=1}^{s}F_j$, where $r_j=[F_j:F]$. For each quotient component, let $h_j\mid n$ be the native rotation image of the geometric Galois stabilizer of one of its cycles. The E4-reviewed Round 2 formula is

$$\#\operatorname{Irr}(\Phi_n)=\sum_{j=1}^{s}\frac{n}{h_j},\qquad
\sum_jr_j=\frac{2^n-2^m}{n},\qquad r_j\text{ even}.$$

The reviewed local theorem implies $h_{j_*}=n$ for the one quotient component receiving the canonical small cycle. Its point cover has one field factor, of degree $nr_{j_*}$ over $F$. This yields the exact all-level equivalence

$$\boxed{\Phi_{p^e}\text{ geometrically irreducible}\quad\Longleftrightarrow\quad B_{p^e}\text{ is a field}.}\tag{EQ}$$

Indeed irreducibility of $A_n$ implies that its invariant subalgebra is a field. Conversely, if $B_n$ is a field, then $s=1$ and the known full local rotation image forces the only summand $n/h_1$ to equal one. This is the application of the already reviewed component formula to A3's new input, not a new proof of either input.

Nothing here forces $s=1$. In particular, full local inertia does not control the other possible quotient components or imply that all the $h_j$ are full. The exact missing global obligation in (EQ) has not disappeared.

The local conclusion also descends from the tame coordinate $s$ to the native parameter $u=c-1/4$. The monic degree-$n$ local point factor over $k[[u]]$ becomes A3's irreducible degree-$n$ factor after $u=-s^2/4$ and the stated translation in $x$. A factorization over $k((u))$ would persist after this field extension, so none exists. The roots form one native cycle and its root field contains every iterate, hence is already cyclic Galois of degree $n$. This confirms that the local-to-global use respects the native parameter as well as the native clock.

## 2. The actual Chebyshev reduction classes

Use $N=2^n-2^m$ and $r=N/n$. At $c=-2$, the characteristic-zero native $n$-cycles split into two sets $\mathcal C_-$ and $\mathcal C_+$, each of size $r/2$. They arise respectively from

$$U_-:=\mu_{2^n-1}\setminus\mu_{2^m-1},\qquad
U_+:=\mu_{2^n+1}\setminus\mu_{2^m+1},$$

via $x=\zeta+\zeta^{-1}$, followed by the native action $\zeta\mapsto\zeta^2$. Inversion identifies exactly two roots in each displayed set. This is the source-owned Chebyshev parametrization, with the prime-power simplification justified in the reviewed Round 3 report. Fix a prime above $p$ for these roots of unity. A **reduction block** is the set of characteristic-zero cycles specializing to one geometric point of the integral cycle quotient over $c=-2\bmod p$.

### 2.1 Odd primes at least five

Since $2^{p^e}\equiv2\pmod p$, one has

$$2^n-1\equiv1\pmod p,\qquad 2^n+1\equiv3\pmod p.$$

For $p\geq5$, every root of unity in both types has order prime to $p$. Reduction preserves distinct roots, their inversion classes, and the squaring permutation. Consequently all $r$ quotient reduction blocks are singletons. The point fiber is étale over the parameter, and so is its free cyclic quotient. In particular, this specialization supplies no nontrivial quotient inertia at these wild periods. It cannot furnish a uniform bridge covering all odd primes.

### 2.2 Exact block degrees at the prime three

Let $n=3^e$, $m=3^{e-1}$ and set

$$b_j:=\frac{2^{3^j}+1}{3^{j+1}}\quad(j\geq0),\qquad b_0=1.$$

The valuation identity $v_3(2^{3^j}+1)=j+1$ was proved uniformly in Round 3. Thus $b_j$ is odd and prime to $3$, and $b_{j-1}\mid b_j$. Reduction of the plus type is described by $\xi\in\mu_{b_e}$ modulo inversion and squaring. Denote the native period of $\xi+\xi^{-1}$ by $d$.

**Proposition 1 (coarse quotient degrees, not assumed normalized ramification indices).** The complete list of reduction blocks and their sizes is:

| Residual type | Native residual period | Point-root multiplicity in $\overline{\Phi_n}(x,-2)$ | Number $\ell$ of characteristic-zero cycle sheets in its quotient block |
| --- | --- | --- | --- |
| Minus type | $n$ | $1$ | $1$ |
| Plus type, $\xi=1$ | $1$ | $n$ | $1$ |
| Plus type, $\xi\in\mu_{b_{e-1}}\setminus\{1\}$ | $d\mid m$ | $2n$ | $2d$ |
| Plus type, $\xi\in\mu_{b_e}\setminus\mu_{b_{e-1}}$ | $n$ | $3n$ | $3n$ |

Here the rows involving $\xi$ are indexed by inversion/squaring orbits, not by each individual root of unity. Empty rows contribute nothing. The formal integral quotient germ at that point is finite free of rank $\ell$ over $W(k)[[c+2]]$. Its special-fiber normalization may have several branches whose degrees sum to $\ell$; the table alone does not prove a single branch.

**Proof, Step 1: count point-root lifts.** Write a plus root as a product of a prime-to-$3$ root and a root in $\mu_{3n}$. The lower-period excluded group has prime-to-$3$ part $\mu_{b_{e-1}}$ and $3$-part $\mu_n$.

For a fixed $\xi\ne1$ in $\mu_{b_{e-1}}$, there are $3n-n=2n$ surviving lifts with this reduction. Pairing the lifts over $\xi$ and $\xi^{-1}$ by inversion gives $2n$ distinct $x$-roots reducing to $\xi+\xi^{-1}$. For $\xi\notin\mu_{b_{e-1}}$, no lift is excluded, giving $3n$ such $x$-roots. When $\xi=1$, inversion acts within $\mu_{3n}\setminus\mu_n$, whose $2n$ elements give exactly $n$ $x$-roots. The minus roots retain multiplicity one, as their orders are prime to $3$. Cross-type intersections cannot occur: the two prime-to-$3$ orders divide $2^n-1$ and $2^n+1$, whose gcd is one, and the minus type excludes $1$.

The reduction of the monic polynomial is the product of these reduced integral roots with multiplicity, so the counts are the asserted polynomial multiplicities, not a count inferred from a local Galois degree.

**Step 2: identify residual periods.** Every plus residual point has period dividing $n$. If its period divides $m$, then $\xi^{2^m}=\xi$ or $\xi^{-1}$. The first alternative forces $\xi=1$ because $\gcd(2^m-1,2^n+1)=1$. The second says $\xi\in\mu_{b_{e-1}}$. Conversely, elements of this subgroup have residual period dividing $m$. Since $n/m=3$ and all its proper divisors divide $m$, every element outside the subgroup has exact residual period $n$.

**Step 3: quotient points are exactly residual orbits.** Let $R=W(k)$, $A=R[c,x]/\Phi_n$ and $A_0=A^{C_n}$. Integrality gives surjectivity of $\operatorname{Spec}A\to\operatorname{Spec}A_0$, including after the closed parameter fiber. Distinct residual orbits cannot have the same quotient point: use the Chinese remainder theorem on the finite reduced point set to choose a function taking value zero on the first orbit and one on the second, lift it to $A$, and take its product over $C_n$. This invariant still has values zero and one and separates the two images. Hence quotient points correspond exactly to residual native orbits. This argument neither averages by $n$ nor asserts invariants commute with nonflat reduction.

If a residual orbit has $d$ points and each point receives $a$ characteristic-zero roots, then it receives $da/n$ characteristic-zero native cycles, because each such cycle has exactly $n$ roots and specializes into that orbit. Thus its block has size $\ell=da/n$, giving all four rows.

**Step 4: interpret the integral germ degree.** Complete the normal finite quotient over $(3,c+2)$ and split it into its local factors. Each factor is finite free over the regular local base $R[[c+2]]$, by the accepted integral-model facts. Evaluation at $c=-2$ is finite free of the same rank over $R$. Its geometric characteristic-zero points are the distinct native cycles specializing to the chosen quotient point. Thus its rank is exactly the block size $\ell$. After reduction, normalization can split it; only the sum of its normalized branch degrees is forced to be $\ell$. $\square$

In particular, the plus block at $\xi=1$ has rank one and the integral quotient germ there is just the base ring. This is the unique pure-$3$-power cycle, represented by a primitive $(3n)$th root of unity. Indeed the order of $2$ modulo $3^{e+1}$ divides $2\cdot3^e$ and is even; the proved valuation identity gives $v_3(2^{2\cdot3^j}-1)=j+1$, excluding every smaller candidate $2\cdot3^j$ with $j<e$. Its order is therefore $2n$, so squaring modulo inversion has one orbit of size $n$ on $\mu_{3n}\setminus\mu_n$. Its reduction is the parabolic fixed point $x=2$ at $c=-2\bmod3$, namely the same point as $x=1/2,c=1/4$. Full inertia of its *point* cover is compatible with this degree-one *cycle* quotient.

For reference, the number of plus reduction blocks is

$$q_e=1+\sum_{j=1}^{e}\frac{b_j-b_{j-1}}{2\cdot3^j}.\tag{QB}$$

The summand counts the residual plus cycles of exact native period $3^j$: the corresponding inversion classes in $\mu_{b_j}\setminus\mu_{b_{j-1}}$ number $(b_j-b_{j-1})/2$, and each orbit has $3^j$ elements. Formula (QB) counts reduction blocks, not global irreducible components. For $e\geq2$, $b_e>b_{e-1}$, so there is a block besides the pure-$3$-power block.


## 3. A specific two-sheet obstruction for the selected generating mechanism

Identify the characteristic-zero Chebyshev fiber with the infinity-coded sheet set by following the real parameter interval from $c<-2$ to $c=-2$. The periodic roots remain simple along this interval and at its endpoint. Their signs cannot change: the critical point zero is not periodic for any $c\leq-2$. Thus the infinity sign itinerary specializes to the signs of the real Chebyshev orbit.

For $x=\zeta+\zeta^{-1}$, differentiation of the Chebyshev identity gives

$$
(f_{-2}^{\circ n})'(x)
=2^n\frac{\zeta^{2^n}-\zeta^{-2^n}}{\zeta-\zeta^{-1}}
=\begin{cases}2^n,&\zeta\in U_-,\\-2^n,&\zeta\in U_+.\end{cases}
$$

The denominator is nonzero on both sets. The sign of this multiplier is the product of the $n$ itinerary signs. Infinity complementation flips that product because $n$ is odd. Hence the infinity involution $\iota$ bijects $\mathcal C_+$ with $\mathcal C_-$.

Let $\mathscr B_p$ be the actual Chebyshev reduction partition of the cycle sheets. To give the chosen mechanism every possible within-block connection, define

$$G_{\mathrm{Ch},p}:=\left\langle\iota,\ \operatorname{Sym}(B)\ (B\in\mathscr B_p)\right\rangle.$$

This is a maximal reconnection model for the selected reduction partition, not a claimed formula for the entire characteristic-$p$ geometric monodromy group. On the punctured mixed-characteristic formal neighborhood, the quotient algebra decomposes into the local factors of Proposition 1. Monodromy based at its characteristic-zero Chebyshev fiber preserves each such factor and hence every reduction block. Granting the full symmetric groups can only strengthen this within-block connecting power. Passing local actions to the special generic fiber would additionally require compatible transport, as discussed below.

**Proposition 2 (failure even with maximal within-block mixing).** If $p\geq5$, the orbits of $G_{\mathrm{Ch},p}$ are the $r/2$ complement pairs. If $p=3$ and $e\geq2$, this group has exactly $q_e$ orbits. One of them is the explicit proper two-sheet set

$$S_*:=\{C_*,\iota C_*\},\tag{PAIR}$$

where $C_*$ is the pure-$3$-power plus cycle. Thus this candidate generating mechanism is nontransitive for every wild pair except the classical rank-two case $(p,e)=(3,1)$.

**Proof.** For $p\geq5$ every reduction block is a singleton, so the only generator is $\iota$.

For $p=3$, every minus block is a singleton. Given a plus block $B$, its union $B\cup\iota(B)$ is invariant under $\iota$ and under every block permutation. It is one orbit: block permutations connect all its plus vertices and $\iota$ connects each of them to its minus partner. Different plus blocks give disjoint such orbits. Thus their number is $q_e$. The block $B=\{C_*\}$ is a singleton by Proposition 1, and its minus partner is also a singleton. Its orbit is precisely (PAIR), which is proper since there are other plus blocks for $e\geq2$. $\square$

The labels in (PAIR) can be given without a finite-period census. If $n=3^e$, the sign itinerary of $C_*$ is the native period-$n$ necklace represented by

$$\epsilon_j=\operatorname{sgn}\cos\!\left(\frac{2\pi\,2^j}{3^{e+1}}\right),\qquad0\leq j<n,$$

and $\iota C_*$ is its binary complement. None of these cosines is zero. The choice of a different primitive $(3n)$th root changes only the native cyclic representative, because $2$ generates the units modulo $3^{e+1}$.

This is a failure of the **Chebyshev-only** connection mechanism, even with optimistic local mixing. It does not show that every primitive edge crossing (PAIR) collides. Adding a suitable surviving primitive edge or a suitable other-cluster monodromy action can break it. The actual (CUT) question has therefore not been refuted.

## 4. Exact remaining local and global obligations

Even the nontrivial block degrees in Proposition 1 are not automatically inertia-orbit sizes after reduction. A concrete test is available for the new residual plus cycles of exact period $n$. Let $\xi\in\mu_{b_e}\setminus\mu_{b_{e-1}}$, $x=\xi+\xi^{-1}$, and set

$$D_j=(f_{-2}^{\circ j})'(x)
=2^j\frac{\xi^{2^j}-\xi^{-2^j}}{\xi-\xi^{-1}}.$$

All these quantities are nonzero. In characteristic three, $D_n=-2^n=1$, and the parameter derivative is exactly

$$\left.\partial_c(f_c^{\circ n}(x)-x)\right|_{c=-2}
=D_n\sum_{j=1}^{n}D_j^{-1}
=(\xi-\xi^{-1})\sum_{j=1}^{n}\frac{2^{-j}}{\xi^{2^j}-\xi^{-2^j}}.
\tag{TR}
$$

The first equality follows by differentiating the $n$ iterates with respect to $c$ and summing the contribution of the additive parameter at each step. Since the residual native period is $n$, the denominator $f_{-2}^{\circ m}(x)-x$ in the dynatomic quotient is nonzero. The $x$-derivative vanishes because $D_n=1$. The plane dynatomic germ is therefore smooth exactly when (TR) is nonzero. The constant cyclic group acts freely on this residual orbit, so the quotient's completed germ has the same smoothness test. Nonvanishing would give one normalized branch of degree $3n$; vanishing alone would not decide whether a singular germ is unibranch.

No uniform nonvanishing proof for (TR), no general normalization of the $2d$ blocks, and no actual primitive-label incidence statement crossing (PAIR) has been obtained. Moreover, even granting unibranchness of every Chebyshev block would leave Proposition 2's explicit obstruction: other branch actions are still required.

There is also a necessary labeling distinction. The reduction blocks above are concrete specializations of the characteristic-zero fiber at $c=-2$; infinity labels use the specified real path. The special characteristic-$p$ generic fiber lies over a different geometric base point. A claim that local actions and chosen primitive transpositions act on the *same* labeled set requires compatible étale/nearby-fiber transport. Arithmetic reduction of a root of unity is not, by itself, that transport theorem. This report does not infer that (PAIR) is invariant under the full special-fiber Galois group.

To close the selected global route, one must prove actual common-label connectivity after including additional primitive inertia: in particular a verified connection out of (PAIR), and then between the other classes. The exact Round 3 cut identity may be applied to the crossing-label polynomial for this specified necklace pair, but no new valuation statement about those labels is proved here. Scalar resilience has already been excluded and is not reintroduced.

## 5. Source audit and disposition

The [primary Doyle--Poonen paper, Remark 1.3 and §4](https://math.mit.edu/~poonen/papers/dyn_gonality.pdf) was checked at its actual theorem and proof passages. Its geometric irreducibility assertion concerns each already irreducible dynatomic component; its positive-characteristic argument deliberately avoids knowing whether the usual dynatomic factors are irreducible. It supplies no uniform (GQ) shortcut. Its finite-field component/gonality conclusions remain source-owned.

[Doyle et al., §§6, 8--10](https://arxiv.org/html/1703.04172v2) supplies the integral quotient model, the isolated-branch specialization theorem, symbolic labels and Chebyshev parametrization. The reviewed Round 2 and Round 3 reports already subtract these inputs. This round's prime-power block bookkeeping and maximal-reconnection obstruction are auxiliary applications, not a new irreducibility theorem. The source's prime-period ramification formulas are not applied to composite periods. Its displayed questions concerning higher-period good reduction are not treated as current impossibility results.

The Bousch/Morton/corrigendum scope boundaries from Round 2 remain unchanged. Recent targeted searches did not locate an applicable all-odd-$p$, all-$e$ quotient theorem; this is a search outcome, not a proof of literature-wide absence. Constant-derivative families $x^p\pm x+c$, fixed-number-field period computations, and arboreal preimage monodromy do not settle the quadratic cycle-quotient problem.

The proof-writer skill required the separation of (EQ), proved finite-fiber statements, the candidate-group obstruction, and unproved global connectivity. Research-lit and the repository batch skill prevented promoting source-owned geometry or this method-specific result to a new paper. Only this allocated report was written. No mathematical program, census, old rerun, external-model call, manuscript/PDF, shared-file or Git operation occurred. **Original global PC424-D: NOT CURRENTLY JUSTIFIED; paper admission: none.**
