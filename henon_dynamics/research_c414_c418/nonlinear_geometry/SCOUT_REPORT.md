# Nonlinear geometry scout: one proof-stage prospect, no admission yet

Date: 2026-09-07. Scope: the authorized C414–C418 batch only.
This report freezes three screened questions, not three paper numbers.
**Outcome: NG2 is worth a bounded all-family proof attempt; NG1 and NG3
are rejected at the present gate. Zero complete theorems are admitted here.**

Only this directory was written. Prior batches remain unchanged. There was
no manuscript, formal Route A evaluation, API/GPU job, external contact or
Git mutation. `NO_BAD_EULER_OR_ROOT_NUMBER` applies: none of the observations
below supplies a target Euler factor, root number, automorphy, target zero
divisor or Hilbert–Pólya operator. The coordinator's function-field height
lane was deliberately not duplicated.

## NG2 — complete rational cycle structure in all odd degrees

### Frozen object and success condition

For every odd integer $d=2k+1\ge3$, define, without an implicit sign change,

\[
s_d(Y)=\sum_{j=0}^{k}(-1)^{k-j}
 \frac{Y\prod_{i=1}^{j}(Y^2-i^2)}{(2j+1)!},
\qquad h_d(x,y)=(y,-x+s_d(y)).
\]

The domain is **all of $\mathbb Q^2$** and one clock tick is one application
of $h_d$. The observable is $N_n(d)=\#\operatorname{Fix}(h_d^n|\mathbb Q^2)$.
Let $C_n(d)$ count primitive cycles modulo cyclic rotation, without merging
the reverse cycle. The requested source zeta convention is

\[
 Z_d(u)=\exp\!\left(\sum_{n\ge1}N_n(d)u^n/n\right)
       =\prod_{n\ge1}(1-u^n)^{-C_n(d)}.
\]

Success means a **proved, finite, symbolic description of every $C_n(d)$**
for all odd $d\ge3$, including small degrees, boundary cycles, coincident
periods and escape. A degree-by-degree functional graph algorithm, a fitted
quadratic count, or the bare rationality of each finite-cycle zeta does not
meet this condition. This is one family contract; its residue classes are
not separate papers.

### Ownership subtraction

The polynomial family and its compression mechanism belong to
Kim–Krieger–Postolache–Szeto. Their Corollary 4.3 gives an integer escape box;
Theorem 5.1 proves a long cycle for $d\equiv1\pmod6$. The exact-count
remark and parts of §5.1 are explicitly computational. None of those
existing results is proposed as our new theorem.
[Primary v2 text](https://arxiv.org/html/2412.01668v2)

The proposed increment is the **entire cycle graph and its all-degree
multiplicities**, with a correct exhaustive boundary analysis. It differs
materially from C412's degree-two monic integral-coefficient classification:
here degrees grow, coefficients have factorial denominators, integer-valued
compression fills a growing two-dimensional region, and cycle lengths grow
with the degree. Merely extending a cubic parameter table was screened out;
no full-coefficient cubic proof mechanism was found in that preliminary
alternative.

Repository collisions were checked at C412's source audit and plan, the
previous nonlinear source ledger, and targeted `2412.01668`/`discrete sine`
matches across the Hénon and symbolic trees. Located uses treat this family
as related work, not an all-degree cycle classification. This is bounded
repository evidence, not a worldwide priority certificate.

### Native arithmetic mechanism and cheap decisive results

There is a direct integrality check independent of a parameter census.
For $|y|_p>1$, the $j$-th summand's norm is

\[
 |y|_p^{2j+1}|(2j+1)!|_p^{-1}.
\]

These norms strictly increase with $j$. Consequently

\[
 |s_d(y)|_p=|y|_p^d|d!|_p^{-1}>|y|_p.
\]

At a maximal $p$-adic coordinate of a periodic orbit, this contradicts
$y_{i+1}+y_{i-1}=s_d(y_i)$. Thus a rational periodic orbit is integral.
This short local observation is a feasibility input, not the paper's
proposed contribution.

Put $R=(d+1)/2$. On integer arguments $[-R,R]$, the polynomial is a
six-periodic sequence with a degree-dependent sign. There are only two
additional integer coordinate layers before the published escape bound
$(d+5)/2=R+2$. The useful route is therefore a symbolic bulk/boundary
decomposition: residue classes in the bulk; finitely many affine return
rules at the boundary; and a proof that these account for every point.
The difficult step is exhaustiveness and cycle closure for arbitrary $d$,
not evaluation of the polynomial.

The exact checker [feasibility.py](feasibility.py) evaluates each polynomial
in two ways (factorial products and generalized-binomial values), enumerates
only the explicitly selected boxes below, and independently checks every
edge and disjointness of every reported cycle. Its counts mean cycles in
the checked box. Identification with all rational periodic points uses the
escape statement, not merely the finite run.

| Selected degree $d$ | Periodic points in the checked box | Longest observed cycle |
|---:|---:|---:|
| 3 | 31 | 10 |
| 5 | 69 | 14 |
| 7 | 115 | 22 |
| 9 | 119 | 20 |
| 11 | 157 | 20 |
| 13 | 271 | 38 |
| 19 | 499 | 54 |
| 25 | 799 | 70 |
| 31 | 1171 | 86 |
| 67 | 4915 | 182 |

These ten selected degrees are a decisive feasibility/source check, not an
exhaustive parameter census and not a proof by numerical agreement.

For $d=6m+1$, the selected $m=1,2,3,4,5,11$ suggest this particularly
concrete **unproved** symbolic target:

| Primitive period | Observed multiplicity formula |
|---:|---:|
| 1 | 1 |
| 3 | 2 if $m$ is odd, otherwise 0 |
| 4 | $m(m+1)$ |
| 5 | 2 if $m$ is even, otherwise 0 |
| 6 | 2 if $m$ is odd, otherwise 3 |
| 10 | 1 if $m$ is odd, otherwise 0 |
| 12 | $m(m+1)$ |
| 16 | 2 |
| 20 | $m(m-1)$ |
| 36 | $m-1$ |
| $16m+6$ | 1 |

Summing these proposed multiplicities gives $d^2+6d+24$, consistent with
the selected degrees only. The $d\equiv3,5\pmod6$ symbolic classifications
have **not** been derived. Their small-degree exceptions are already
visible; they must not be suppressed by an asymptotic statement.

### Source inconsistency that must not be hidden

The accessed v2 exact-count formula cannot be used as a target theorem.
For $d=13$, its Theorem 4.4 implies at least $15^2=225$ periodic points,
whereas the later numerical remark gives 153. Our exact box calculation
gives 271. The conflicting statements also appear in the PDF text, so this
is not explained by the HTML transcription alone.
[PDF, printed pp. 14–15](https://arxiv.org/pdf/2412.01668v2)

This is an identified conflict in the accessed version, not a claim that
the authors' complete work is false or that no corrected version exists.
No journal final text was located in the bounded search. Correcting that
number alone would be insufficient for admission: the retained question
is the full all-degree graph.

### Decision and replacement boundary

`PROMISING_ALL_FAMILY_PROOF_ATTEMPT / NOT_ADMITTED`.

Next decisive task: replace all sampled formulas by finitely many proved
affine bulk/boundary return rules; establish the three odd residue classes
and every exceptional degree; then seek independent proof/source review.
Stop this contract if only the already known long-cycle existence result,
the finite-box algorithm, a numerical correction, or an unclosed boundary
case remains. No manuscript or paper number is justified yet.

## NG1 — rational-denominator conservative quadratic family

Frozen question: classify all periodic orbits of
$H_c(x,y)=(y,y^2+c-x)$, for **all** $c\in\mathbb Q\setminus\mathbb Z$,
on all of $\mathbb Q^2$, under ordinary iteration. The observable and cycle
conventions are the $N_n,C_n,Z(u)$ conventions above. The intended new
increment would have to be a complete rational-parameter period and point
classification, not a necessary denominator condition.

Here is the decisive local calculation. If $|c|_p>1$, let
$M=\max_i|x_i|_p$ on a periodic recurrence
$x_{i-1}+x_{i+1}=x_i^2+c$. Dominance at a maximal coordinate excludes both
$M^2>|c|_p$ and $M^2<|c|_p$, so $M^2=|c|_p$. If any coordinate has
smaller norm, its recurrence has right-hand norm $M^2>M$, another
contradiction. Thus every coordinate has norm $|c|_p^{1/2}$. At good primes
the maximal-norm argument gives integral coordinates.

Consequently, write $c=a/q^2$, with $q\ge2$, $(a,q)=1$. Every periodic
coordinate has exact denominator $q$, so $x_i=z_i/q$ and

\[
 q(z_{i-1}+z_{i+1})=z_i^2+a,
 \qquad z_i^2\equiv-a\pmod q.
\]

The square denominator and local escape mechanism have direct classical
precedent in Ingram's Lemma 7.2 for the opposite Jacobian sign. The sign
distinction matters for the global periodic classification, but the short
local adaptation is not a substantial new mechanism.
[Ingram, §7](https://arxiv.org/pdf/1111.3609)

The missing step is a uniform global closure across unbounded $q$: the
congruence does not bound the cyclic words or their heights uniformly, and
the C412 finite-symbol argument cannot be transferred with its integer
spacing unchanged. The adjacent uniformity questions are explicitly
conjectural in the 2024 arithmetic problem list; this is a difficulty
boundary, not an assertion that that list states our exact sign-restricted
problem verbatim.
[Problem list, §11](https://amj.math.stonybrook.edu/html-articles/Files-2015-2024/23-70/index.html)

`REJECT_CURRENTLY_NO_GLOBAL_CLOSURE`. No denominator table was computed.
Resurrection requires a new global proof mechanism, not another prime-power
denominator subfamily or the necessary congruence above.

## NG3 — character-surface alternatives and tropical denominators

Frozen broad question: on the full integral-parameter character-surface
family

\[
 S_{A,B,C,D}:x^2+y^2+z^2+xyz=Ax+By+Cz+D,
 \qquad A,B,C,D\in\mathbb Z,
\]

classify rational periodic points for each loxodromic Vieta word, under
iteration of that **one fixed word**. The generators, with this sign
convention, are
$s_x(x,y,z)=(A-yz-x,y,z)$, and cyclic analogues using $B,C$.
The observable would be the exact native fixed-point counts, not a
full-group orbit count or an arbitrarily switched word.

The natural feasibility mechanism is nonarchimedean valuation dynamics
followed by an archimedean finite core. But the central tropical mechanism
already has substantial direct ownership: Jang's Theorem A(b) linearizes
the skeleton for nonnegative parameter valuations. A standalone
restatement of that result, or of its immediate hyperbolic no-return
consequences on the nonzero linear model, is not a new paper.
[Jang v2, Theorem A](https://arxiv.org/html/2306.11357v2)

This does **not** establish that all rational periodic classifications for
all words are already known: lifting from the skeleton and controlling the
finite core are additional mathematical tasks. The present scout has not
provided a uniform, complete, non-classical core classification. For the
Fibonacci word at integral points, that core is already C413. For general
words, invoking canonical heights or equidistribution does not produce an
explicit classification. Abboud's actual rigidity theorem concerns common
periodic sets under specific parameter assumptions, a different quantifier.
[Abboud v4, Theorem A](https://arxiv.org/html/2401.05762v4)

The finite-field fixed-word route also collides with the earlier
`research_c399_c403/nonlinear_reserves/RESERVE_SCOUT.md`: swapping in another
hyperbolic word does not solve its already identified long-orbit obstacle.

`REJECT_NO_SEPARATED_COMPLETE_INCREMENT`. No new character-surface census
was run. A future candidate must name and solve a genuinely different full
arithmetic core problem, not rename a classical tropical model or multiply
the previous trace-map clock.

## Handoff

The coordinator may take NG2 into a bounded proof-development gate, with
the exact polynomial and clock above frozen. There is presently one
prospect and **zero** additional admitted papers. The source audit is
[SOURCE_AUDIT.md](SOURCE_AUDIT.md); reproducible checks are limited to
[feasibility.py](feasibility.py). Internal scouting is not external or human
peer review. Missing target A1/A2 evidence remains missing.
