# CP9 independent nonauthor proof and source review

2026-09-08 UTC. Internal AI-assisted mathematical review by the AS1
spectral-probe lane, which did not author CP9 and did not supply its
period-two witness. The coordinator requested an adversarial review of
the actual frozen theorem, not a favorable author summary. This review
does not constitute journal peer review, a global-priority certificate,
a formal Route-A evaluation or a manuscript admission by itself.

## Verdict

**PASS for the complete frozen CP9 theorem, with its two explicitly
imported external theorems. No mandatory mathematical correction remains.**

The result retains every field of characteristic three, every starting
pair and the full set of geometric ordinary-preperiodicity parameters.
The proof does not silently reduce the contract to a special field,
fixed pair, bounded period, selected root of an equation or single
exceptional parameter.

**Substantive-increment recommendation: eligible as one complete
independent research contract**, subject to coordinator adjudication.
The new argument resolves the two surviving signs for the source's
explicit fixed-polynomial example. It is a short proof with substantial
borrowed input, but neither the hypothesis specialization alone nor the
borrowed height theorem alone gives the missing exclusion. The new
uniform two-cycle/escape witness is the decisive additional argument.
It does not classify all equal-weight binomials.

## Artifacts actually read and fixed review targets

All four author files were read completely. Their SHA-256 values at
review were:

| Artifact | SHA-256 |
| --- | --- |
| [FROZEN_QUESTION.md](../charp_alternatives/FROZEN_QUESTION.md) | `246d71869d98f1ed4829acef84b61d1983c98a85389fefbb6a8d4cf48dfe5736` |
| [PROOF_DRAFT.md](../charp_alternatives/PROOF_DRAFT.md) | `75cb7f6fe2abb7b77cc721b1354003c3416d34f5525823a6bb9806c38ebb73e4` |
| [SOURCE_LEDGER.md](../charp_alternatives/SOURCE_LEDGER.md) | `658e050f811a3d2dedaef4fc226f2eb1f2d2bec2bec0cad3de79b4518eb97a20` |
| [SCOUT_REPORT.md](../charp_alternatives/SCOUT_REPORT.md) | `9edf158a1b398055ffbd4543eca0911805c01e9933872f8c9295ac937a241fd0` |

The author ledger became available during this review and was then read
in full; no claim was made to have read it before it existed. Its other
source accesses and its 35 searches remain the author's receipts, not
the reviewer's own source work. This review independently reopened the
particular primary source carrying both proof dependencies.

The review also retains the round-nine plan, original batch boundaries,
current repository instructions and the four-contract entry state.
Neither the reviewer nor these findings alter a global admission file.

## Exact theorem under review

Let $L$ be any field of characteristic $3$, let $\overline L$ be an
algebraic closure, and put $k=\overline{\mathbb F}_3\subset\overline L$.
For $f(X)=X^4+X^6$ and $F_\lambda=f+\lambda$, the reviewed assertion is
$$
\#\{\lambda\in\overline L:
 a,b\text{ are preperiodic under }F_\lambda\}=\infty
\quad\Longleftrightarrow\quad
(a,b\in k)\ \text{or}\ f(a)=f(b),
$$
for every $a,b\in L$. Iteration is ordinary composition, starting at
time zero. The set counts geometric parameters, not scheme
multiplicities or Frobenius-substituted times.

## Primary-source applicability, independently verified

[Lee–Nam v2](https://arxiv.org/html/2509.15079v2) was directly read at
Setup 1.3, Theorems 1.2, 1.4, 1.5, Remark 1.6, Section 2 through
Theorem 2.1, and Section 4.3 through Remark 4.5. Theorem 1.5/4.4
applies to the equal-weight, nonadditive case and leaves differences
$0,\pm1$ here. Theorem 2.1 uses finite extensions of the perfect
closure of $k(t)$, monic $f$, degree at least two and $f(0)=0$;
infinitely many common preperiodic parameters imply equality of local
heights at every place and every completed-algebraic-closure parameter.
It does not require strict exponent-weight inequality. Remark 4.5
expressly leaves the two nonzero differences unresolved for this
polynomial. These are verified statement/hypothesis imports, not an
independent reconstruction of Ghioca–Hsia's original proof.

The [arXiv version record](https://arxiv.org/abs/2509.15079) currently
lists v2, dated 11 October 2025. [Nam's author publication list](https://sites.google.com/view/namgyeonghyeon/gyeonghyeon-nam)
still identifies this work as submitted; its separate JNT 278 (2026)
entry belongs to the orbit-intersection paper. This prevents a false
peer-review/publication attribution. Five bounded fresh searches found
no direct covering theorem; that is not global novelty clearance.

The specialization itself is checked arithmetically:
$$
4=3^0\cdot4,\quad6=3^1\cdot2,\quad
3^0(4-1)=3^1(2-1)=3,
$$
and both prime-to-three parts exceed one. The source's nonzero equation
reduces to $\epsilon^2=-4/2=1$ in characteristic three, whose roots
are exactly $\epsilon=1,-1$. Also $f$ is monic of degree six with
$f(0)=0$. No strict inequality is being smuggled into this specialization.

## Claim-by-claim adversarial audit

| Claim or possible failure | Decision | Check |
| --- | --- | --- |
| Constants give infinitely many common parameters | PASS | Any three constants lie in one finite field preserved by the map. |
| Equal first images suffice | PASS | Both marked orbits agree from time one; the fixed-point-parameter lemma is applied to the fixed marked point $a$. |
| One-point preperiodicity parameter set is infinite | PASS | A simple fixed-parameter root leaves an additional root at every prime return time; its least period equals that prime. |
| Nonconstant exceptional equation forces both points nonconstant | PASS | The constant field is algebraically closed inside $\overline L$. |
| Arbitrary $L$ reduces to the required one-variable function field | PASS | $b$ is algebraic over $k(a)$, and every preperiodic parameter is algebraic over that same field. |
| Passing to the perfect closure retains the whole infinite parameter set | PASS | The relative algebraic closure inside $\overline L$ contains all of it and is itself algebraically closed. |
| Pole valuation exists through perfection and the finite extension | PASS | The pole extends uniquely through the purely inseparable tower and extends to the finite algebraic field. Its sign on $a$ is retained. |
| The proposed first orbit is a genuine two-cycle | PASS | Its two points could coincide only for the constant $a=-1$. |
| All roots $b$ of the exceptional equation are handled | PASS | The first image depends only on $f(b)$, not on a root choice. |
| Both signs are excluded | PASS | Swap the two marked points; the common-parameter set is unchanged. |
| Escape domination and height normalization | PASS | The third image has modulus $C^6>C$; subsequent sixth powers give height $(\log C)/36$. |
| The height bridge applies at the constructed parameter | PASS | Its parameter quantifier is universal, not confined to the original infinite set or to fixed-point parameters. |

### 1. Sufficient directions and geometric parameter infinitude

When $a,b\in k$, every $\lambda\in k$ belongs to a finite extension
of $\mathbb F_3$ together with $a,b$. The resulting finite field is
preserved by $F_\lambda$, so both orbits are finite. The field $k$ is
infinite. This works even if the original $L$ is finite or does not
contain every constant, because the contract permits all
$\lambda\in\overline L$.

If $f(a)=f(b)$, then $F_\lambda(a)=F_\lambda(b)$ for every
parameter. Thus preperiodicity of the fixed marked point $a$ is
equivalent to that of $b$. No assertion about a parameter-dependent
tail being a fixed input to Lemma 1 is needed.

For nonconstant $a$, define $Q_n(T)=F_T^n(a)-a$. Induction on $n$
gives degree $6^{n-1}$ and leading coefficient one: the sixth power
of the previous monic iterate has strictly larger degree than its
fourth power or the added $T$. The unique fixed parameter is
$T_0=a-f(a)$. Since $f'(X)=X^3$, differentiating the iteration and
evaluating at $T_0$ gives
$$
D_1=1,\quad D_{n+1}=a^3D_n+1,
\quad Q_n'(T_0)=\sum_{j=0}^{n-1}a^{3j}.
$$
This polynomial in the transcendental $a$ is nonzero, including when
$n$ is divisible by three. The characteristic does not turn its
distinct monomials into equal terms. Hence $T_0$ is a simple root.

For every prime integer $\ell\ge2$, $Q_\ell$ has degree greater
than one and cannot have $T_0$ as its only geometric root: an algebraic
closure factors it into linear factors, whereas $T_0$ has multiplicity
one. Any other root makes $a$ periodic, with period dividing $\ell$
but not equal to one. Its least period therefore is $\ell$. A fixed
parameter cannot give the same point two distinct least periods, so
different primes supply different parameters. This is an infinite
geometric set, not an argument based only on growing multiplicities.

### 2. Arbitrary-field and parameter-transfer audit

After the imported reduction, only $f(b)-f(a)=0,1,-1$ must be treated.
If either point is constant under a nonzero difference, the other is
a root of a polynomial with coefficients in the algebraically closed
field $k$, hence is also constant. Thus every nonconstant exceptional
pair has both points transcendental over $k$.

Swapping $a,b$ when needed preserves the original simultaneous
preperiodicity set and permits $f(b)=f(a)+1$. This makes $b$
algebraic over $k(a)$ with degree at most six. The field
$$
K_0=\bigcup_{r\ge0}k(a^{1/3^r}),\qquad K=K_0(b)
$$
is therefore a finite extension of the perfect closure of the
rational function field $k(a)$. All these fields are taken inside
the given $\overline L$; one need not assume $k\subset L$.

For any parameter at which $a$ is preperiodic, some relation
$F_\lambda^n(a)=F_\lambda^m(a)$ holds with $n>m\ge0$.
For $m\ge1$, the two polynomials in the parameter have different
degrees $6^{n-1}>6^{m-1}$; for $m=0$, the right side is just $a$.
The relation is consequently a nonzero polynomial equation over
$k(a)$. Thus every one of the assumed infinitely many parameters is
algebraic over $k(a)$ and over $K$.

Let $\overline K$ be the elements of $\overline L$ algebraic over
$K$. It is an algebraic closure of $K$: roots in $\overline L$ of
polynomials over this subfield are algebraic over $K$ by transitivity.
All common parameters belong to it, so the field replacement retains
their infinitude. The assumption for the imported height theorem is
satisfied by any sequence of distinct such parameters, whose global
canonical heights are all zero by preperiodicity.

The ordinary pole valuation of $a$ on $k(a)$ extends through the
purely inseparable perfect-closure tower and then to $K$. Existence
of valuation extensions under algebraic field extension is the usual
valuation-extension theorem; no discrete value-group assertion is
needed. In fact $K_0$ is perfect, so its finite algebraic extension
$K$ is separable. Whatever positive normalization is used in the
source's product formula, $C=|a|_v$ remains greater than one.
Nonzero constants have absolute value one, since each has finite
multiplicative order. These facts justify every valuation property
used in the escape calculation.

### 3. Independent algebra check of the universal witness

The reviewer expanded the polynomial directly. In characteristic
three,
$$
(X+1)^4=X^4+X^3+X+1,\qquad
(X+1)^6=X^6- X^3+1,
$$
so $f(X+1)-f(X)=X-1$. Replacing $X$ by $X-1$ or expanding directly
gives $f(X-1)-f(X)=-X-1$. The even powers also give $f(-X)=f(X)$.

Set $\lambda_*=1-a-f(a)$. Using these identities,
$$
F_{\lambda_*}(a)=1-a,\qquad
F_{\lambda_*}(1-a)=f(a-1)+1-a-f(a)=-2a=a.
$$
The equality $1-a=a$ would imply $a=-1\in k$, excluded here, so
this is a genuine period-two orbit. There is no need to select an
unspecified root of a period-two equation.

For any $b$ satisfying $f(b)=f(a)+1$,
$$
F_{\lambda_*}(b)=-a-1,\qquad
F_{\lambda_*}(-a-1)=f(a+1)+1-a-f(a)=0,\qquad
F_{\lambda_*}(0)=\lambda_*.
$$
This computation covers every algebraic branch of $b$, including any
extension behavior not visible in a finite-field sample. It uses only
the value $f(b)$ and therefore does not assume a particular relation
between $a$ and $b$ themselves.

### 4. Escape and the contradiction

At the chosen pole, $|a|_v=C>1$. The distinct sizes of the terms show
$|f(a)|_v=C^6$ and $|\lambda_*|_v=C^6$. For any $z$ with
$|z|_v>C$, both inequalities
$$
|z|_v^6>|z|_v^4,\qquad |z|_v^6>C^6=|\lambda_*|_v
$$
are strict, so the nonarchimedean triangle law gives
$|F_{\lambda_*}(z)|_v=|z|_v^6$. The third image of $b$ already
has modulus $C^6>C$. Induction gives
$$
|F_{\lambda_*}^n(b)|_v=C^{6^{n-2}}\quad(n\ge3),\qquad
\widehat h_{v,\lambda_*}(b)=\frac{\log C}{36}.
$$
The two values in the orbit of $a$ are bounded, so its local canonical
height is zero directly from the limit definition. The parameter
$\lambda_*\in k(a)\subset K$ is allowed by the imported theorem's
universal parameter quantifier. It need not belong to the initial
infinite common-parameter set. Equality of the two local heights at
this parameter is contradicted. Swapping the starting points proves
the same impossibility for the other sign, completing necessity.

## Substantive increment, separately from mathematical correctness

The following is the reviewer's bounded contribution assessment, not a
global novelty assertion or journal recommendation.

1. **Complete quantified question.** The output is an if-and-only-if
   classification of all starting pairs over all characteristic-three
   fields for one fixed family. The single constructed parameter is
   only the contradiction witness, not a replacement for that outcome.
2. **External input deducted.** The reduction to three differences,
   universal height-function equality and the general local-height
   method are not new here. The constant and equal-image sufficient
   directions are also routine; the direct one-point lemma is a
   self-contained convenience, not another contribution.
3. **Actual surviving deduction.** The witness changes the test orbit
   from eventual fixed-point behavior to a two-cycle and simultaneously
   sends every remaining exceptional second point to zero and then
   into a forced escape region. This uniformly removes the two values
   that remained after the imported reduction. It is not obtained by
   satisfying the earlier strict inequality: the two weights here are
   equal. Nor is this family a monomial specialization; its derivative
   $X^3$ is nonzero although the degree-six monomial has zero derivative.
4. **Why short is not automatically insufficient.** The missing result
   is the full residual classification for the specific example, not a
   numerical example or a restatement of an already proved sufficient
   condition. Once the new witness is supplied, the proof is short
   because substantial prior results are being used transparently.
   Its role is a completion of that explicit case, not a new general
   equidistribution theory.
5. **Why this does not establish everything.** The argument does not
   settle the equal-weight binomial family, the colliding-orbits
   conjecture, a zeta boundary, or target arithmetic. Its independence
   from M1/AS2/IR1/P7 concerns the object and observable; it does not
   create any A2 bridge.

I therefore recommend that the coordinator may count **one** complete
CP9 contract under the batch's substantial-question gate, retaining this
precise source-dependent scope. Neither its two signs nor its two lemmas
should be split into additional papers. The coordinator's independent
substantive adjudication, subsequent paper planning and release gates
remain separate actions.

## Mandatory corrections and optional editorial clarifications

**Mandatory mathematical/source corrections: none identified.**

Optional clarifications for a later manuscript, not conditions for this
proof's PASS:

- Say explicitly that $a$ has least period two at $\lambda_*$ because
  coincidence of its two displayed points would make it constant.
- In the equal-image sufficient direction, say that Lemma 1 is applied
  to $a$, rather than describing its input as the parameter-dependent
  common tail.
- Preserve the distinction between an imported theorem stated and
  checked in Lee–Nam, and an independently read proof of the original
  Ghioca–Hsia height theorem. The latter was not performed here.

The current draft already states enough to justify all three points;
these are clarity suggestions, not hidden proof gaps.

## Exact review source/query and execution receipt

The available-tool inventory contained no Zotero or Obsidian tools.
Filename-filtered local PDF discovery found no relevant CP9 source;
the initial broader listing concerned the repository's unrelated root
paper stream and was not represented as source reading. The local
`literature/`, `tools/` and legacy arXiv-fetch directories were absent.
Primary web retrieval was the fallback; no PDF was downloaded.

The reviewer made exactly **five** fresh search submissions, in order,
without a tool-level domain or recency filter:

1. `"x^4+x^6" "preperiodic"`
2. `"Lee" "Nam" "simultaneously preperiodic" "2026"`
3. `"2509.15079" "period"`
4. `"On simultaneously preperiodic points for one-parameter families" "2026"`
5. `"preperiodic" "Remark 4.5" "3"`

Several returned broad or irrelevant locators. Aggregators and unrelated
PDF hits were not used as evidence. The actual independent primary
accesses were Lee–Nam's HTML with the sections listed above, its arXiv
abstract/version history, and Nam's current author page. Reopening/find
calls are not additional search submissions. No claim is made that the
other thirteen papers in the author's inventory were independently read
by this reviewer. No global citation-completeness or priority certificate
is inferred from either search count.

The `research-review` adversarial framework and `proof-writer` claim
checks were used. Repository/current-task instructions select this
current-team internal review instead of the legacy external-model API
examples. `research-lit` governs the local-first/primary-source routing;
ARS is restricted to source-status and applicability checking, not a
fresh full pipeline or an empirical evidence grade for a theorem.
No external review API, mathematical program, GPU, old accepted-proof
rerun, source download, Git write, manuscript build or author-file edit
was performed. All new writes are inside this `charp_review/` directory.

## Final disposition

- Exact frozen CP9 classification: **PASS**, explicit external theorem
  dependencies retained.
- Remaining mandatory issues: **none identified**.
- Complete-contract increment: **recommended eligible as one result**,
  not a global-novelty or publication-readiness certificate.
- Admission authority: coordinator; no registry or admission edited here.
