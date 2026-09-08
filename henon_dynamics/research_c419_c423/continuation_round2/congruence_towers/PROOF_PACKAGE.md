# CT1 proof triage: qualitative rationality is a classical reconstruction

2026-09-07. Coordinator derivation; not independently reviewed, not admitted.

## Claim and status

The frozen claim asks for the complete ordinary period generating functions
of every polynomial automorphism $F$ of $\mathbb Z_p^d$, including an
effective finite construction. The status of that entire claim is
**NOT CURRENTLY JUSTIFIED**: no algorithmic representation or effective
procedure for arbitrary $p$-adic coefficients has been supplied.

The qualitative part is **PROVABLE AFTER WEAKENING** by the short reduction
below: finitely many prime-to-$p$ period parts occur and every
$C_{F,m}(u,v)$ is rational. The main analytic and rationality inputs are
existing theorems. This reduction is a substance-based rejection of CT1
as a new paper contract, not a counterexample to qualitative rationality.

## Assumptions and notation

Fix a prime $p$, an integer $d\ge1$, and mutually inverse polynomial maps
$F,F^{-1}$ with coefficients in $\mathbb Z_p$. Both maps preserve all
congruences, so $F_k$ is a permutation of $(\mathbb Z/p^k)^d$.
Write $\nu(x)=\min_i v_p(x_i)$, with $\nu(0)=\infty$.
The function $\mu_{\rm ar}$ below is the ordinary arithmetic Mobius function.
All cycles use one application of $F_k$ as one time step.

## Strategy and dependency map

1. Finite residue permutations and their affine return maps produce a
   common iterate that is sufficiently near identity on each residue ball.
2. Poonen's Theorem 1 interpolates that iterate by restricted analytic
   functions. This supplies a definable action of a compact procyclic group.
3. The condition that an ordinary period divides $e p^r$ becomes a
   subanalytic formula in the two integer parameters $k,r$.
4. Cluckers' fixed-$p$ rationality theorem for subanalytic equivalence
   relations, with its stated multivariable extension, counts residue
   classes satisfying the condition. Elementary Mobius inversion finishes.

The two external inputs are credited in [SOURCE_AUDIT.md](SOURCE_AUDIT.md).
No uniformity in varying $p$ and no nonsingularity of fixed loci is used.

## Derivation

### 1. Honest residue-ball normalization

Let $h$ be the order of the finite permutation $F_1$. For each residue
representative $b\in\{0,\ldots,p-1\}^d$, put

$$R_b(y)=\frac{F^h(b+py)-b}{p}.$$

This is an integral polynomial automorphism of $\mathbb Z_p^d$.
Its polynomial reduction modulo $p$ is affine, with invertible linear
part $D F^h(b)\bmod p$: terms of degree at least two acquire a factor $p$.
Let $\ell$ be a common multiple of the orders of these finitely many
affine permutations in $\operatorname{AGL}_d(\mathbb F_p)$.
Then $R_b^\ell$ is coefficientwise identity modulo $p$.
For $p=2$, its square is coefficientwise identity modulo $4$:
if $T=y+2H(y)$, then
$T^2-y=2H(y)+2H(y+2H(y))\equiv0\pmod4$.
Thus, with $M=h\ell$ for odd $p$, and $M=2h\ell$ for $p=2$,
Poonen's threshold holds on every ball for $F^M$.

This argument does not infer polynomial identity from equality as functions
on $\mathbb F_p^d$; the affine normalization is essential.

### 2. A compact ordinary-iterate action

Poonen gives a restricted analytic interpolation of each normalized return.
Returning to the original coordinates yields a finite piecewise restricted
analytic function $g(x,t)$ on $\mathbb Z_p^d\times\mathbb Z_p$ such that
$g(x,n)=F^{Mn}(x)$ for nonnegative integers $n$.
Density of those integers and continuity give
$g(g(x,t),u)=g(x,t+u)$ and $g(x,0)=x$.
They also show that every $g(\cdot,t)$ preserves congruences: approximate
$t$ by nonnegative integers and use congruence preservation by $F^{Mn}$.

On a finite congruence quotient this is a continuous action of
$\mathbb Z_p$, whose image is a finite $p$-group. Consequently, the order
of $F_k$ divides $M p^a$ for some $a$ depending on $k$. Write
$M=\eta p^s$ with $p\nmid\eta$. Every ordinary period has prime-to-$p$
part dividing $\eta$. No bound on $a$ is needed.

The ordinary powers of $F$ extend continuously to the procyclic group
$\varprojlim_a\mathbb Z/(M p^a)\cong\mathbb Z/\eta\times\mathbb Z_p$.
Explicitly, choose $0\le j<M$ with prescribed finite coordinate
$j\bmod\eta$ and $j\equiv t\pmod {p^s}$, and act by
$F^j g(x,(t-j)/M)$. The quotient $(t-j)/M$ is integral.
This follows first for dense ordinary integer powers and then by
continuity. If a residue point has ordinary period $m' p^{r'}$, its
stabilizer consists exactly of coordinates divisible by $m'$ in the
finite factor and by $p^{r'}$ in the $p$-adic factor.

### 3. A definable ordinary period-divisibility test

For a divisor $e\mid\eta$, $k\ge1$ and $r\ge0$, define $X_{e,k,r}$ by
the following formula on $x\in\mathbb Z_p^d$:

$$
\exists t\in\mathbb Z_p\quad v_p(t)=r,\quad
\bigvee_{\substack{0\le j<M\\j\equiv e\ (\mathrm{mod}\ \eta)}}
\left[v_p(t-j)\ge s\ \land\
\nu\!\left(F^j g\!\left(x,\frac{t-j}{M}\right)-x\right)\ge k\right].
$$

This is a subanalytic formula with integer parameters $k,r$ and a finite
disjunction. For a residue point of period $m'p^{r'}$, it holds exactly
when $m'\mid e$ and $r'\le r$. Indeed the finite and $p$-adic stabilizer
conditions just proved are independent, and an element of valuation $r$
exists for every $r\ge0$. Thus $X_{e,k,r}$ is a union of residue balls and
its number of classes modulo $p^k$ is

$$A_e(k,r)=\#\operatorname{Fix}(F_k^{e p^r}).$$

In particular the formula does not require the undefinable operation of
inserting a variable integer exponent $p^r$ into a polynomial iterate.

### 4. Existing rationality plus cycle inversion

Apply Cluckers' fixed-$p$ subanalytic equivalence-relation theorem to
congruence modulo $p^k$ on $X_{e,k,r}$. Its two-parameter version gives

$$\mathcal A_e(u,v)=\sum_{k\ge1,r\ge0}A_e(k,r)u^k v^r\in\mathbb Q(u,v).$$

If the definable domain is empty for some parameters, add one disjoint
tagged dummy equivalence class, apply the nonempty-domain formulation,
and subtract $u/((1-u)(1-v))$. This resolves that hypothesis explicitly.

Let $B_m(k,r)$ count points of exact ordinary period $m p^r$. For $m\mid\eta$,

$$B_m(k,r)=\sum_{e\mid m}\mu_{\rm ar}(m/e)
\left(A_e(k,r)-\mathbf1_{r\ge1}A_e(k,r-1)\right).$$

The subtraction isolates the exact $p$-power part, and divisor inversion
isolates the exact prime-to-$p$ part. Each cycle contains $m p^r$ points,
so the desired rational expression is

$$C_{F,m}(u,v)=\frac{1-v/p}{m}
\sum_{e\mid m}\mu_{\rm ar}(m/e)\mathcal A_e(u,v/p).$$

For $m\nmid\eta$ the answer is zero. Singular fixed loci, the identity map,
and $p=2$ were not excluded. This proves the qualitative subclaim.

## Effectivity boundary and decision

The argument supplies definable data, not a implemented finite-jet
algorithm for arbitrary $p$-adic coefficients. A fixed coefficient
precision cannot determine the answer: identity and translation by
$p^L$ agree modulo $p^L$, but have different ordinary periods at higher
levels. Exact coefficient access, symbolic input classes and effective
cell decomposition would need separate specifications.

Even a repaired effective formulation would need a genuinely new
algorithmic increment to merit a paper. The qualitative claim above is
already reconstructed from existing general theorems with a short
ordinary-clock encoding. We stop CT1 here, with no admission, paper
number, formal Route-A evaluation, large quotient census or PDF.

## Open risks

This derivation has not received nonauthor mathematical review. It is a
transparent reason for rejecting a candidate's proposed novelty, not a
certified new theorem package or an assertion of global priority.
