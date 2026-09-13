# Paper30 wild-cover first probe: independent mathematical check

Date: 2026-09-06. Reviewer identity: `/root/p30_wild_cover_check`, the independent subagent assigned this bounded check by `/root`; this is not an external referee or an external-model review. The runtime does not expose a separately verifiable model identifier, so none is asserted.

Input: [PAPER30_WILD_COVER_FIRST_PROBE_20260906.md](PAPER30_WILD_COVER_FIRST_PROBE_20260906.md), 202 lines, SHA256 `0a0db518aff8cba19ca56cff2d687c0e5ac6bbd5428efa3a1523706aa05c2e42`. The input was read completely and was not edited. Only this new report is owned by this reviewer. Workflow: complete reads of `docs/WORKFLOW.md` and the `proof-writer` skill, followed by direct proof and boundary-case checks; no numerical experiment.

## Claim

Check the input's ordinary versus deck-equivariant lift criterion, two Artin–Schreier reduction lemmas, exact bilinear eigenslice for $P=x^{q-1}+c$, and the connected degree-$q$ cover with its displayed automorphism. Check characteristic-two and odd-characteristic quantifiers. No full quotient classification, novelty assessment, capacity assessment, Route A/B evaluation, or manuscript acceptance is requested or supplied.

## Status

**PROVABLE AS STATED for the substantive lemmas, slice theorem, and degree-$q$ cover/lift claim.** No mathematical counterexample was found. One literal wording correction is needed: the input's lines 96–97 must not call the class for $a=0$ nontrivial. There are $q$ distinct slice classes, exactly $q-1$ of which are nonzero when $c\ne0$. This does not change the stated dimension or any construction.

| Checked item | Independent status | Scope or qualification |
| --- | --- | --- |
| Ordinary lift versus specified deck-equivariant lift | PROVED | Connected degree-$p$ cover; existence permits some $j\in\mathbb F_p^*$ satisfying the criterion, not necessarily $j=1$ |
| Lemma 1: rational primitive, polynomiality, $y$-degree obstruction | PROVED | Polynomial base $K[x,y]$; $a\ne0$ in the mixed term |
| Lemma 2: unique Frobenius-reduced representative | PROVED | Algebraically closed $K$ supplies roots and removes constants |
| Exact bilinear $j$-eigenclass criterion | PROVED | Only classes $[axy]$; $a\ne0$ for the restriction $j=-1$ |
| Root description and dimension of $E_c$ | PROVED | $c=0$: zero space; $c\ne0$: dimension $r$, including the zero class |
| Connected finite étale degree-$q$ cover | PROVED | $q=p^r>2$, $c\ne0$, hence $\alpha\ne0$ |
| Actual lift, polynomial inverse, deck inversion and square | PROVED | The square commutes with the whole displayed deck group |
| Character subcovers realize the slice | PROVED | $b=0$ is the zero character; nonzero characters have a marking distinction described below |
| Full invariant/finite-orbit classification in $Q_{\rm AS}$ | OPEN | Not implied by any checked result |

## Assumptions

- $K$ is algebraically closed of characteristic the prime $p>0$; $A=K[x,y]$ and $F=K(x,y)$.
- $H_P(x,y)=(P(x)-y,x)$, $\sigma=H_P^*$, and $\deg P\ge2$.
- $\wp(u)=u^p-u$; $Q_{\rm AS}=A/\wp(A)$ is an additive $\mathbb F_p$-vector space, not a $K$-vector-space quotient.
- In the selected family, $r$ is a positive integer, $q=p^r>2$, and $P=x^{q-1}+c$. The slice allows $c=0$, but the explicit cover assumes $c\ne0$.
- A lift is an automorphism over the specified base automorphism. Deck-equivariant means that it commutes with the fixed translations, not merely that it normalizes their group.

## Notation

$[g]$ denotes an Artin–Schreier class. For a degree-$p$ equation, $T_b(z)=z+b$ with $b\in\mathbb F_p$; for the degree-$q$ equation the same notation uses $b\in\mathbb F_q\subset K$. The set of bilinear classes is $B=\{[axy]:a\in K\}$. The eigenslice in question is $E_c=B\cap\ker(\sigma+1)$.

## Proof Strategy

Use pole orders and $y$-degrees to exclude concealed rational primitives, then reduce univariate Frobenius chains. Establish the lift criterion by the deck-group action. Compute the slice exactly, and prove the degree-$q$ cover's irreducibility using the valuation at $y=\infty$. Finally verify both the map and its inverse by substitution.

## Dependency Map

1. The rational-primitive obstruction ensures that a nonzero polynomial Artin–Schreier class gives a connected degree-$p$ cover.
2. The $y$-degree obstruction and univariate reduction give the exact bilinear eigenclass criterion and the root equation for $E_c$.
3. The degree-$q$ cover uses a separate valuation proof of irreducibility; finite étaleness alone does not imply connectedness.
4. The lift calculation uses only $t^q=\alpha$ and $\alpha c=-t$; trace-character calculations link this cover back to $E_c$.

## Proof

### Step 1. Polynomiality and the two reduction lemmas

Write a rational $u$ in lowest terms. If its denominator has an irreducible factor $\pi$, the associated valuation has $v_\pi(u)<0$. The two summands of $u^p-u$ then have unequal valuations $pv_\pi(u)<v_\pi(u)$, so $v_\pi(\wp(u))=pv_\pi(u)<0$. A polynomial has no such pole. Thus the denominator is a nonzero constant and $u\in A$.

For a polynomial $u$ with $s=\deg_y u>0$, its $p$th power has $y$-degree $ps>s$, with nonzero leading coefficient. Consequently $\deg_y\wp(u)=ps$. This excludes $y$-degree zero and one. Therefore $\wp(u)\in K[x]$ implies $u\in K[x]$, and $axy+f(x)$ cannot be a coboundary if $a\ne0$. Applied to $(a-a')xy$, this proves injectivity of $a\mapsto[axy]$. The same argument excludes rational primitives for these mixed polynomials.

Because $K$ is algebraically closed, Frobenius is bijective and every constant belongs to $\wp(K)$. For $m>0$,
$$
c x^{pm}-c^{1/p}x^m=\wp(c^{1/p}x^m).
$$
Eliminate the highest remaining positive exponent divisible by $p$, combining coefficients after each replacement. The offending highest exponent strictly decreases, so the process terminates. The resulting representative has zero constant and only positive exponents prime to $p$. A nonzero difference of two such representatives has highest exponent prime to $p$. It cannot equal $\wp(v)$ for nonconstant $v$, whose highest degree is $p\deg v$, and a constant $v$ cannot produce that difference. This proves uniqueness.

### Step 2. Ordinary lifts and the deck-equivariant criterion

For $[g]\ne0$, Step 1 excludes a root of $Z^p-Z-g$ in $F$. If $z$ is any root, all roots are $z+b$ with $b\in\mathbb F_p$. Thus $F(z)/F$ is a separable splitting extension whose Galois group injects into the additive group of order $p$. It is nontrivial, hence has order $p$. The polynomial is irreducible, and the monic quotient $A[z]/(z^p-z-g)$ embeds in this field, so the cover is integral and connected.

Its deck group consists of the $p$ translations. A lift $\Phi$ normalizes that group because it covers a base automorphism, and its conjugation has the form $\Phi T_b\Phi^{-1}=T_{jb}$ for one $j\in\mathbb F_p^*$. Let $h$ be its last-coordinate function. Then $h(z+b)-h(z)=jb$, so $h-jz$ is deck-invariant. The invariant ring is $A$: express a function uniquely as $\sum_{i=0}^{p-1}a_i z^i$; if its highest positive exponent is $d<p$, translation by $1$ gives a nonzero leading difference coefficient $d a_d$. Therefore an invariant function has no positive exponent. It follows that $h=jz+u$ with $u\in A$.

The defining equation now gives
$$
\sigma g=jg+\wp(u).
$$
Conversely this equality defines a lift with inverse obtained from $H_P^{-1}(x,y)=(y,P(y)-x)$ and fiber coordinate $j^{-1}(z-u\circ H_P^{-1})$. Thus an ordinary lift exists exactly when $\sigma[g]=j[g]$ for some $j\ne0$; a lift commuting with the specified translations exists exactly when $j=1$ is possible. For a nonzero class these conditions need not agree in odd characteristic. For $p=2$, $\mathbb F_2^* =\{1\}$, so they do agree for connected degree-two covers.

The symplectic statement also holds: $H_P^*(dx\wedge dy)=(P'(x)dx-dy)\wedge dx=dx\wedge dy$ in every characteristic.

### Step 3. Exact bilinear slice, and no more

For $a\ne0$ and $j\in\mathbb F_p^*$,
$$
\sigma(axy)-jaxy=axP(x)-(1+j)axy.
$$
Step 1 forces $1+j=0$ if this is a coboundary. With $j=-1$, Step 1 also says that being a coboundary in $A$ is equivalent to being a coboundary in $K[x]$. Lemma 2 of the input, proved above, tests this by the reduced form. For $P=x^{q-1}+c$, that form is $(a^{1/q}+ac)x$. Since Frobenius to the $r$th power is bijective,
$$
a^{1/q}+ac=0\quad\Longleftrightarrow\quad a+a^q c^q=0.
$$
This establishes precisely the stated $E_c$, including $a=0$. For $c=0$ only $a=0$ survives. For $c\ne0$, the polynomial $c^q X^q+X$ has degree $q$ and derivative $1$, hence $q$ distinct roots over $K$. Its root set is $\mathbb F_p$-linear. Injectivity from Step 1 then gives $\dim_{\mathbb F_p}E_c=r$ and exactly $q-1$ nonzero classes.

For $p=2$, $-1=1$ and every displayed class is $\sigma$-invariant. For odd $p$, every nonzero displayed class has exact period two under $\sigma$: equality with its negative would imply $2[axy]=0$, hence $[axy]=0$ in an $\mathbb F_p$-vector space. Thus these particular nonzero classes are not invariant under $H_P$, but they are invariant under $H_P^2$. This says nothing about invariant classes outside $B$.

### Step 4. Finite étaleness and connectedness of the degree-$q$ cover

Choose $t^{q-1}=-1/c$ and set $\alpha=t^q$. Algebraic closedness supplies $t$, and $c\ne0$ forces $t\ne0$; multiplying the defining equality gives $\alpha c=-t$. The ring
$$
R=A[z]/(z^q-z-\alpha xy)
$$
is free of rank $q$ over $A$ because the relation is monic. The relative derivative in $z$ is $-1$, a unit; the monogenic étale criterion proves that $\operatorname{Spec}R\to\operatorname{Spec}A$ is finite étale.

For connectedness take the discrete valuation of $F=K(x)(y)$ with $v(y)=-1$ and $v(K(x)^*)=0$. Let $L=F(z)$ for one root and extend the valuation to $L$, preserving its values on $F$. Since $v(\alpha xy)=-1$, the equation forces $v(z)<0$ and then $qv(z)=-1$. If $e$ is the ramification index, the value group is $(1/e)\mathbb Z$; containing $-1/q$ forces $q\mid e$. The valuation inequality $e\le[L:F]$ and the polynomial bound $[L:F]\le q$ give equality throughout. This proves irreducibility. The ring $R$ injects into $L$ by its monic normal forms, so $R$ is integral and the cover is connected.

All $q$ roots of $B^q-B$ lie in $K$ and form $\mathbb F_q$. The $q$ translations on $z$ are distinct deck automorphisms; a degree-$q$ field extension admits at most $q$ such automorphisms. They are the entire deck group. The valuation used above is at infinity, outside the affine base, so ramification there does not contradict affine étaleness.

### Step 5. The actual automorphism and characteristic quantifiers

Define $\widetilde H(x,y,z)=(x^{q-1}+c-y,x,-z+tx)$. In either parity of the characteristic,
$$
(-z+tx)^q-(-z+tx)=-(z^q-z)+\alpha x^q-tx
=\alpha x(x^{q-1}+c-y).
$$
It preserves $Y$. Its two-sided polynomial inverse is
$$
(x',y',z')\longmapsto(y',(y')^{q-1}+c-x',ty'-z').
$$
The inverse also preserves the equation: substitution gives $(ty'-z')^q-(ty'-z')=\alpha y'((y')^{q-1}+c-x')$. Thus no birational-to-regular inference is missing.

For every $b\in\mathbb F_q$, $\widetilde H T_b=T_{-b}\widetilde H$. Therefore $\widetilde H^2$ commutes with every deck translation. In fact its fiber coordinate is $z+t(P(x)-x-y)$, a pure base-dependent translation. In characteristic two, already $\widetilde H$ commutes with every deck translation. In odd characteristic it inverts every translation; for $b\ne0$, $T_{-b}\ne T_b$. These are statements about this cover and this lift, not a universal assertion about all $H_P^2$-invariant classes or all lifts of all covers.

### Step 6. Character subcovers and the marking convention

For $b\in\mathbb F_q$, let $w_b=\sum_{i=0}^{r-1}(bz)^{p^i}$. Telescoping gives
$$
\wp(w_b)=(bz)^q-bz=b\alpha xy.
$$
For $b\ne0$, Step 1 makes this a nonzero Artin–Schreier class and Step 2 makes its degree-$p$ cover connected. The deck action is
$$
T_d(w_b)-w_b=\operatorname{Tr}_{\mathbb F_q/\mathbb F_p}(bd).
$$
The trace polynomial has degree $p^{r-1}<q$ and is nonzero, so it cannot vanish at all $q$ elements. Its values lie in $\mathbb F_p$, and its nonzero $\mathbb F_p$-linear image is all of $\mathbb F_p$. Multiplication by nonzero $b$ is bijective. Consequently the pairing is nondegenerate, and the $q$ choices of $b$ give all additive characters, including the zero character.

Finally, $\alpha^q c^q+\alpha=(\alpha c)^q+\alpha=(-t)^q+\alpha=0$. Hence every element of $\alpha\mathbb F_q$ is a root of $c^q X^q+X$; both sets have $q$ elements, so they are equal. These character classes realize all of $E_c$ and no additional bilinear coefficients. For $b=0$, $w_b=0$ is the zero character, not a connected degree-$p$ intermediate cover. Distinct nonzero $b$ give distinct marked Artin–Schreier classes. If $b'=jb$ with $j\in\mathbb F_p^*$, however, $w_{b'}=jw_b$ generates the same intermediate field. Thus there are $(q-1)/(p-1)$ distinct degree-$p$ intermediate subcovers when the marking is forgotten, rather than $q-1$ in odd characteristic. The input does not assert the latter incorrect cover count. ∎

## Corrections or Missing Assumptions

1. Input lines 96–97: replace the unrestricted phrase “distinct nontrivial classes” by “$q$ distinct classes, of which the $q-1$ classes with $a\ne0$ are nontrivial.” This is a zero-element wording correction, not a weakening of the slice theorem.
2. Input lines 148–153: read “degree-$p$ character subcovers” for $b\ne0$; $b=0$ records the zero class. Preserve the marked/unmarked distinction above if cover counts are added later.
3. No extra hypotheses are needed for the principal claims. Algebraic closedness, $q>2$, and $c\ne0$ where explicitly assumed do real work. Over $K=\mathbb F_p$, for example, constants need not belong to $\wp(K)$, so the zero-constant normal form would fail. With $\alpha=0$, the displayed degree-$q$ equation would instead split into $q$ disconnected components. Neither case satisfies the relevant input assumptions.

## Open Risks

- No complete classification of $Q_{\rm AS}^{\sigma}$, $Q_{\rm AS}^{\sigma^2}$, or all finite-orbit classes has been proved. Exactness inside $B$ supplies no reduction of a general multivariate class to $B$ and no effective global degree bound. The full classification question remains **OPEN**.
- The elementary lift and slice results remain short results; they do not justify a 22–30-page paper, paper selection, or a capacity/novelty PASS. The two quantum-candidate assessments are outside this report's scope.
- [Stacks Project, §59.63](https://stacks.math.columbia.edu/tag/0A3J), accessed 2026-09-06, confirms the characteristic-$p$ Artin–Schreier exact sequence used as background. The arguments above are direct calculations and do not depend on a characteristic-zero Danielewski classification. No literature-completeness claim has been checked or promoted.

Disposition: preserve the author probe; record the checked short mathematical results and the two zero/marking qualifications. No Route A/B status or artifact acceptance is conferred.
