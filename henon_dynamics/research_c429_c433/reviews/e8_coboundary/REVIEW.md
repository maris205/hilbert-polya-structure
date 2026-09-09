# E8 nonauthor audit: A1 Frobenius module and coefficient descent

2026-09-09 UTC. Independent current-team internal mathematical review by
`/root/c429_e8_coboundary_review`, not an author of the A1 artifacts and not
human peer review. Assigned write ownership: this review directory only.

## Verdict and exact scope

**PASS for the three auxiliary claims in A1's proof supplement, with zero
mathematical must-fixes. ORIGINAL PC424-L REMAINS UNCLOSED.** The free-module
description is structural information about an unknown space, not a computation
of that space, a proof of its vanishing, or a complete defect classification.
The report states these limitations correctly. No independent-paper admission
or target-arithmetic conclusion follows from this review.

The unchanged [original contract](../../../research_c424_c428/positive_characteristic/FROZEN_CONTRACTS.md)
is PC424-L, beginning at line 52: for every odd prime $p$, every
$c\in k=\overline{\mathbb F}_p$, and every $h\in k[x]$, determine whether

$$
K_c:=\{h:\sum_{a\in O}h(a)=0\text{ for every ordinary primitive }f_c\text{-orbit }O\}
=B_c:=\{Q\circ f_c-Q:Q\in k[x]\},\qquad f_c=x^2+c,
$$

or give the full uniform alternative defect/obstruction required there. The
domain is all of $\mathbb A^2(k)$ for
$T_{c,h}(x,y)=(f_c(x),y+h(x))$, one application of $T_{c,h}$ is one native
tick, and each distinct point in an ordinary primitive base orbit is counted
once, also for periods divisible by $p$. Nothing below replaces those
quantifiers by prime periods, one finite field, bounded degree, or scheme
lengths.

Reviewed primary lane artifacts:

- [A1 REPORT](../../lanes/a1_periodic_coboundary/REPORT.md), all 237 lines.
- [A1 PROOF_SUPPLEMENT](../../lanes/a1_periodic_coboundary/PROOF_SUPPLEMENT.md),
  all 221 lines.
- [A3 REPORT](../../lanes/a3_wild_tower/REPORT.md), all 143 final-readback lines, only for
  the fixed-germ/new-contact interface; this is not a separate full A3 review.

The accepted auxiliary statements, with $V=k\oplus xk[x^2]$ and
$N_c=K_c\cap V$, are precisely:

1. $K_c/B_c\simeq N_c$, compatibly with full polynomial Frobenius, and
   $N_c$ is a free **left** module over
   $R=k[\mathcal F; a\mapsto a^p]$, where $\mathcal Fv=v^p$.
2. A nonzero $N_c$ has countably infinite $k$-dimension. If it contains an
   element of degree $D$, then for $M\ge D$ its degree-$M$ slice has
   dimension at least $1+\lfloor\log_p(M/D)\rfloor$. The supplement's
   more precise sum over occupied degree chains is also correct.
3. If $c\in\mathbb F_q$, every slice
   $W_D=N_c\cap k[x]_{\le D}$ is defined over $\mathbb F_q$: it has a
   $k$-basis consisting of polynomials in $\mathbb F_q[x]$. Equivalently,
   $W_D=k\otimes_{\mathbb F_q}(W_D\cap\mathbb F_q[x])$ under the natural
   map. This is the precise meaning of coefficient descent, not the claim
   that the entire $k$-space is finite-dimensional over $\mathbb F_q$.

## 1. Polynomial normal form and both Frobenius operations

The actual [initial proof](../../../research_c424_c428/positive_characteristic/PROOF_PACKAGE.md),
Steps 1, 4 and 5, was read, not merely its current summary.

For $j\ge1$, $\Delta x^j=(x^2+c)^j-x^j$ is monic of degree $2j$.
Removing the largest positive even exponent of a polynomial creates only
smaller exponents. Iterating terminates and leaves a constant plus odd
positive powers. If $\Delta Q$ is also in $V$ and $Q$ is nonconstant,
its degree is positive even, whereas a nonzero member of $V$ has degree
zero or positive odd. Thus $B_c\cap V=0$ and $k[x]=B_c\oplus V$ as
vector spaces. The kernel of $\Delta$ is exactly the constants; the
normal representative is unique even though its transfer is only unique
modulo constants. No ring decomposition is asserted.

Telescoping gives $B_c\subseteq K_c$. Consequently normal reduction of
$K_c$ stays inside $K_c$, proving $K_c/B_c\simeq N_c$.

Full polynomial Frobenius is well-defined on the quotient: for every
$Q\in k[x]$,

$$
(\Delta Q)^p=\Delta(Q^p).
$$

This identity does not require $c\in\mathbb F_p$. Both $B_c$ and $V$
are preserved by full $p$th power; preservation of $V$ uses oddness of
$p$. If $\pi:k[x]\to V$ denotes normal projection, uniqueness gives

$$\pi(h^p)=\pi(h)^p.$$

Hence the displayed quotient isomorphism is also an isomorphism of the
claimed left skew modules. The supplement does not explicitly display
this projection identity, but its ingredients prove it without another
assumption. This is clarification, not an open proof obligation.

For ordinary cycle sums, $S_{h^p}(O)=S_h(O)^p$, so $K_c$ is preserved
by full Frobenius. The fixed-point equation $x^2-x+c=0$ has at least
one root in $k$, even at $c=1/4$. Its ordinary orbit has exactly one
point. Thus a constant polynomial $\beta\in K_c$ must satisfy
$\beta=0$. A double fixed-point scheme still supplies this one-point
ordinary test; no multiplicity or division by a period is used.

The imported stronger saturation statement is sound too: if
$h^p=\Delta Q$, differentiation yields
$2xQ'(x^2+c)-Q'(x)=0$. If $Q'\ne0$ has degree $m$, the degrees
$2m+1$ and $m$ cannot cancel because $2\ne0$. Thus $Q'=0$;
perfection supplies $Q=R^p$, and Frobenius injectivity gives
$h=\Delta R$. **Perfection is used in this backward saturation step;
the new forward degree-chain argument does not need it.**

## 2. Free left module, infinite pivots and filtered dimension

Supplement §2 supplies a direct proof, without relying on an unverified
structure theorem for noncommutative principal ideal rings. The relevant
ring convention is left coefficients:

$$
\Bigl(\sum_{r=0}^{s}a_r\mathcal F^r\Bigr)v
=\sum_{r=0}^{s}a_rv^{p^r},\qquad
\mathcal F a=a^p\mathcal F.
$$

Semilinearity, not $k$-linearity of $\mathcal F$, is exactly the required
compatibility. Composition of these operations realizes multiplication
in this skew-polynomial ring.

Every possible nonzero degree in $N_c$ is positive odd. Partition it
uniquely as $jp^e$, where $j$ is positive odd and $p\nmid j$. For an
occupied chain let $e_j$ be its first occupied exponent, put
$d_j=jp^{e_j}$, and choose a monic $v_j\in N_c$ of degree $d_j$.
Forward stability occupies every later degree $d_jp^r$. There is no
assertion that every $j$ occurs or that $e_j=0$.

The degrees of $v_j^{p^r}$ are pairwise distinct across all pairs
$(j,r)$. For $w\in N_c$ of degree $jp^e$, minimality gives $e\ge e_j$;
subtracting its leading coefficient times $v_j^{p^{e-e_j}}$ lowers the
degree and stays in $N_c$. Repetition stops, and any terminal constant
is zero by the fixed-point argument. Thus these powers span.

Each linear combination and each module relation is finite. In a
nontrivial such combination the unique largest leading degree cannot
cancel. This proves independence and hence

$$N_c=\bigoplus_{j\in J_c}R v_j.$$

The proof remains valid if $J_c$ is infinite: spanning reduces one
polynomial through finitely many lower degrees, and independence only
examines finite relations. It never requires Frobenius surjectivity on
$N_c$, extraction of coefficient roots during cancellation, or a finite
list of pivots. For $J_c=\varnothing$ the same proof gives $N_c=0$.

There can be no cancellation of a basis element above a degree cutoff
against another element. Consequently the basis elements of degree at
most $M$ form a basis of that slice and give exactly

$$
\dim_kW_M=
\sum_{\substack{j\in J_c\\d_j\le M}}
\left(1+\left\lfloor\log_p\frac{M}{d_j}\right\rfloor\right).
$$

The sum is finite; at $M=0$ it is empty, with no logarithm evaluated at
zero. Any nonzero $v$ of degree $D$ independently gives the advertised
logarithmic lower bound through the powers $v^{p^r}$. The upper cardinal
bound is countable since $N_c\subset k[x]$.

The valid consequence is
$\dim_k(K_c/B_c)<\infty\Rightarrow K_c=B_c$. A nonzero rank-one free
$R$-module is already infinite-dimensional over $k$. A1 REPORT
§D and supplement §3 explicitly avoid the illicit substitutions
“finite skew-module rank”, “every slice is finite”, or “finite-field
interpolation” for global finite $k$-dimension.

## 3. Descent of finite slices with infinitely many cycle constraints

For this claim only, assume $c\in\mathbb F_q$. Coefficient Frobenius
$h\mapsto h^{[q]}$ leaves exponents unchanged; it is not the full power
$h\mapsto h^q$. It preserves degree and the normal support.

Because the $q$-power map is a bijection of $k$ and commutes with $f_c$,
both it and its inverse send an ordinary primitive cycle to one of the
same exact length. Evaluation gives the supplement's exact identity

$$S_{h^{[q]}}(O)=S_h(O^{q^{-1}})^q.$$

Thus coefficient Frobenius and its inverse preserve $K_c$, $N_c$ and
$W_D$. This is equality of the resulting subspace, not just a guessed
one-sided inclusion.

Although $W_D$ is defined by infinitely many orbit equations, it is a
subspace of the finite-dimensional coefficient space $k^{D+1}$. It
therefore has a finite reduced row-echelon basis. With column order
$1,x,\ldots,x^D$ fixed, entrywise $q$th power preserves zeros, leading
ones, pivot locations and row-echelon order. Its row space is again
$W_D$. Uniqueness forces the entire matrix to be fixed, so every entry
lies in $\mathbb F_q$. The empty matrix handles $W_D=0$.

This argument needs neither an orbit cutoff nor an effective enumeration
of all constraints. Such a cutoff does not follow from it. Similarly,
it does not bound the degrees of finite fields containing detecting
cycles. If $W_D$ contains an element of exact degree $D$, at least one
descended basis element has that degree, since a span of lower-degree
elements cannot produce it. In particular, the monic chain generators
can be chosen over $\mathbb F_q$ exactly as claimed in supplement §4.

A1 REPORT §C's separate descent of each finite-field interpolation
system is also valid: its linear equations are over $\mathbb F_q$, so
consistency over $\mathbb F_{q^r}$ implies consistency over $\mathbb F_q$.
Its degree allowance still grows with $q^r$ and gives no global transfer.

## 4. Imported prime-period contact inequality: derivation checked

The full actual [R2 proof](../../../research_c424_c428/continuation_round2/positive_characteristic/PROOF_PACKAGE.md)
and [R3 proof](../../../research_c424_c428/continuation_round3/positive_characteristic/PROOF_PACKAGE.md)
were read. The strict inequality and prime-period localization in A1
REPORT's handoff are correct, with the following exact dependencies.

R2 Steps 1–2 identify the full cyclic algebra with
$A_n=k[x]/(f_c^{\circ n}-x)$ and prove its squarefree-monomial basis.
The binary-support proof detects any normal degree-$D$ trace whenever
$n>2\lfloor\log_2D\rfloor$. Its weight argument controls all terms
involving $c$; its circular-window separation uses both the zeroth and
highest binary digit of odd $D$. No reducedness assumption is hidden.

If $v\in N_c\setminus\{0\}$, ordinary-cycle vanishing gives
$\operatorname{rad}(F_n)\mid H_n(v)$ at every $n$, where
$F_n=f_c^{\circ n}-x$ and $H_n(v)=\sum_{i<n}v\circ f_c^{\circ i}$.
The converse uses $n$ equal to each primitive period, so does not divide
by a potentially zero scalar.

Let $M_n$ be the maximum root multiplicity of $F_n$ and let
$q_n=p^{\lceil\log_pM_n\rceil}$. Then
$M_n\le q_n<pM_n$ also when $M_n=1$. Rootwise vanishing makes
$H_n(v)^{q_n}$ divisible by $F_n$. But
$H_n(v)^{q_n}=H_n(v^{q_n})$ and $\deg v^{q_n}=Dq_n$, still odd.
The contrapositive of the binary-support criterion therefore yields

$$
Dq_n\ge2^{\lceil n/2\rceil},\qquad
M_n>\frac{2^{\lceil n/2\rceil}}{pD}.
$$

This proves the strict inequality; replacing the strict bound
$q_n<pM_n$ by a weak one would unnecessarily lose it.

For fixed $(p,c)$, exclude $p$ and those primes equal to the
multiplicative order of a nonzero fixed-point multiplier different from $1$.
There are at most two such multipliers. At every remaining prime
$\ell$, fixed points consume total root multiplicity exactly two in
$F_\ell$: either two simple roots, or the unique point at $c=1/4$
with germ $t+t^2$ and multiplicity two under prime-to-$p$ iteration.

For a sufficiently large odd remaining prime, the lower bound is at
least two. A root of maximal multiplicity must therefore have exact
ordinary period $\ell$, multiplier one, and the same multiplicity at
all its $\ell$ orbit points by local conjugacy through noncritical
one-step maps. Thus

$$
\frac{2^{(\ell+1)/2}}{pD}<e_\ell\le\frac{2^\ell-2}{\ell}.
$$

The threshold depends on $(p,c,D)$; this is not a universal prime cutoff.
Different primes require different primitive cycles. The displayed
upper bound is much too large to contradict the lower bound.

The monomial control $K_0=B_0$ in A1 REPORT §A is also a correct short
imported consequence: $\operatorname{ord}_{\mathbb F_p^*}(2)>1$, so
$x^{2^\ell}-x$ is squarefree at all sufficiently large prime $\ell$;
R2 then converts the nonzero trace class to an ordinary-point witness.
R2's stated Jacobian counterexample is algebraically valid and prevents
using derivative annihilation alone as ordinary vanishing.

## 5. R6 algebraic descent has no missing conclusion once its premise holds

The full [R6 proof](../../../research_c424_c428/continuation_round6/positive_characteristic/PROOF_AND_GAPS.md)
and its [frozen question](../../../research_c424_c428/continuation_round6/positive_characteristic/FROZEN_QUESTION.md)
were read. The imported theorem requires a genuine compatible field
embedding extending $x\mapsto f(x)$ and fixing $k$, together with an
element algebraic over $k(x)$ satisfying $\sigma u-u=h$.

The proof's successive implications are valid: the stable finite extension
$E=k(x,u)$ of $k(x)$ has $[E:\sigma E]=\deg f>1$; invariants of every positive
iterate are constants; in the separable case the minimal polynomial
satisfies $P^\sigma(T+h)=P(T)$; expansion at $u$ produces constant
coefficients and a finite additive translation Galois group. Its subgroup
polynomial gives a nonzero additive-polynomial relation
$A(h)=\Delta b$ without dividing by a possibly wild extension degree.
Finite-pole propagation makes rational $b$ polynomial. The normal
complement is stable under additive polynomials when $\gcd(\deg f,p)=1$,
excluding nonconstant normal residuals; invariance under $\sigma^p$
excludes the constant residual. Raising an arbitrary algebraic transfer
to an appropriate $p$th power handles the inseparable case and then
descends the original transfer by invariance.

This supports A1's use of R6 as a complete conditional input. It does
not produce the compatible finite algebraic object from cycle data.
Neither the new free module nor coefficient descent supplies that
premise. No auxiliary theorem in the supplement depends on assuming it.

## 6. A3's fixed germ does not control the new primitive contacts

The specific classical input to A3 is

$$
\operatorname{ord}_t((t+t^2)^{\circ p^j}-t)
=1+\frac{p^{j+1}-1}{p-1}\qquad(j\ge0, p\text{ odd}).
$$

Primary-source verification: Lindahl–Rivera-Letelier,
[Definition 3.4 and Proposition 4.4, including its odd-prime proof](https://arxiv.org/html/1311.4478v3#S4.SS2),
were inspected. The coefficients $a_1=1,a_2=0$ meet the stated
minimal-ramification criterion, and the definition gives the formula.
This is source-owned fixed-germ information, not a new primitive-period
contact bound.

The source's Theorem C also owns the unique small cycle and optimal slope
used by A3; the final A3 readback explicitly subtracts those conclusions.

For the A1 interface, the missing quantities instead are
$\operatorname{ord}_t(g_{\ell,a}(t)-t)$ for
$g_{\ell,a}(t)=f_c^{\circ\ell}(a+t)-a$, where $a$ moves through
new exact-prime-period multiplier-one cycles. Their coefficients and
initial contact orders are not identified with those of $t+t^2$.
Even a full formula for the $p$-power iterates of each fixed germ would
need independent control of these starting contacts.

A3's deformation at $c=1/4-s^2/4$ isolates one cluster specializing to
one fixed point and native periods $p^e$. It neither quantifies over
all primitive prime-$\ell$ cycles of a fixed $f_c$ nor bounds the
initial contacts above. The statement that it cannot presently close
A1 is therefore an inference from the mismatched hypotheses and
quantifiers, not a universal impossibility theorem. No cross-lane
upper bound is silently imported.

## 7. Source subtraction, must-fixes and the remaining lemma

| Material | Already owned input | Residual A1 contribution / limitation |
| --- | --- | --- |
| Normal form, telescoping, functional graphs, Frobenius saturation | Initial PC424-L proof, Steps 1–5 | These are not new A1 results |
| Binary-support trace detection, nilradical criterion, Jacobian failure | R2 proof, Steps 1–5 | No reduced ordinary detection follows automatically |
| Exponential contact lower bound on new prime cycles | R2 Step 4 and R3 Proposition | Imported necessary condition, not an A1 theorem |
| Algebraic-to-polynomial transfer descent | Complete R6 theorem | Existence of a compatible algebraic transfer remains missing |
| Minimal ramification of $t+t^2$ | Lindahl–Rivera-Letelier Proposition 4.4 | One germ's wild tower is not global contact control |
| Chainwise free-module basis and slice descent | Current A1 supplement | Elementary structural deductions; no claimed global novelty or substantial full-question closure |

**Mathematical must-fixes: none.** The displayed projection identity and
the precise base-change interpretation of a “basis over $\mathbb F_q$”
above clarify the existing statements; they do not require a change to
the accepted supplement. No author file was edited.

The exact direct remaining lemma is still:

$$
\forall p\text{ odd}\quad\forall c\in\overline{\mathbb F}_p\quad
\forall\,0\ne v\in k\oplus xk[x^2],\quad
\exists\text{ ordinary primitive }O\text{ with }S_v(O)\ne0.
$$

Equivalent or sufficient completion targets include, with their actual
unproved premises kept explicit:

- Prove $\dim_k(K_c/B_c)<\infty$ for every fixed $(p,c)$; no uniform
  numerical dimension bound is needed, but each entire quotient must be
  finite-dimensional.
- Construct, for every $h\in K_c$, a compatible finite algebraic transfer
  over $k(x)$; then the already proved R6 theorem applies.
- Prove for every fixed $(p,c)$ that the maximal initial contact
  $E_\ell^{\mathrm{new}}$ among exact-prime-period points satisfies
  $\liminf_{\ell\to\infty,\ \ell\text{ prime}}E_\ell^{\mathrm{new}}/2^{\ell/2}=0$
  after the finite R3 exclusions. This suffices by the strict lower bound.

A1's dual invariant-functional density formulation is also an exact
algebraic double-annihilator reformulation, not a density theorem.
None of these obligations has been proved by the reviewed artifacts.
A2's finite-graph/Bézout extraction is outside this review's ownership
and is not certified or rejected here.

## 8. Evidence and execution receipt

The actual initial, R2, R3 and R6 proof passages were independently
checked as above. The external check was bounded to the cited primary
ramification paper; Veech, Manes–Thompson and Garton comparison entries
in A1 REPORT were read as the author's bounded-access disclosures, not
independently reverified or used as proof inputs here. No worldwide
novelty, venue, retraction or human-read clearance is claimed.

Reviewed lane-byte identities at readback:

```text
A1 REPORT.md
39da241592b078da5edafcb9e983500f98212a4b90f2c1f1ceb3d58d26058c35
A1 PROOF_SUPPLEMENT.md
bcf1aaaaa6804889cf4cbcaac69ea584ac109970065ba7f2e6b0e89778257ffc
A3 REPORT.md (interface scope only)
71d31585ce8672755e19b384c7ed91d4c00ba50a638a1af7c14e0749dbc1a096
```

The repository batch skill preserved the frozen question and source
subtraction; research-review supplied the internal critical-review
discipline; proof-writer supplied the exact-claim/proof-gap distinction.
Their older external-model examples were not executed. The ARS router
was inspected but no ARS panel/report workflow is claimed.

Mathematical programs, old reruns, builds, Git operations, evaluator
mutations, shared-index changes, extra agents and external-model/API
manuscript uploads: **0**. Only this review file was written. Read/search
calls and byte-identity hashes are not mathematical experiments.
`NO_BAD_EULER_OR_ROOT_NUMBER` remains in force.
