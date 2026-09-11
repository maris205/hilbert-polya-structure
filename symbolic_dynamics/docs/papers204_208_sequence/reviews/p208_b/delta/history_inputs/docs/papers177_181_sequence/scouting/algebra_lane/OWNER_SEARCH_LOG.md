# Bounded owner search log

**Search snapshot:** 2026-09-03 UTC.  
**Lifecycle:** `HOLD_EXTERNAL`.

## Method and semantic limit

The search used exact literals, exact formula fragments, carrier/update
descriptions, and mechanism terms.  It checked the local P1--P176 corpus
first, then searched publisher/DOI records, arXiv abstracts, and author-hosted
primary manuscripts.  Representative queries included:

- `\"f(x+f(0))-f(x)\" finite field` and the same expression without spaces;
- `matrix map \"A+I\" \"det A\" dynamics finite field`;
- finite-field matrix cycle index with prescribed/forbidden eigenvalues;
- `self-power map x to x^x modulo prime dynamics`;
- arithmetic \(p\)-derivation / Fermat quotient operator;
- the two quadratic-extension literals; and
- iteration of multiplicative-order and factorial-return maps.

No search engine is exhaustive.  A nonhit below means only “not located in
this bounded pass.”  It never means novel, first, publishable, or externally
cleared.

## SFD: state-selected finite differences

### Located owner boundary

Erhard Aichinger and Jakob Moosbauer, [*Chevalley--Warning type results on
abelian groups*](https://doi.org/10.1016/j.jalgebra.2020.10.033), `Journal of
Algebra` 569 (2021), 30--66, define functional degree by powers of the
augmentation ideal, identify \(\Delta_a=\tau_a-1\) as a forward-difference
operator, and discuss nilpotency indices for \(p\)-group algebras.  The
publisher metadata, authors, volume, pages, and DOI were checked.

This source owns the algebra used to say that products of \(p\) differences
vanish on \(\mathbb F_p^{\mathbb F_p}\), as well as the augmentation-ideal
filtration itself.  Those facts receive zero contribution credit.

### Literal-query result

The exact update

\[
f\longmapsto\bigl(x\longmapsto f(x+f(0))-f(x)\bigr)
\]

was not located in the bounded exact-phrase/formula pass.  More importantly,
the located functional-degree source does not iterate a direction selected
by the current function value, recover nonzero direction words from an
orbit, or enumerate anchored inverse lifts.

**Owner status:** `OWNER_THIN / NOT CLEARED`.  The permitted residual is only
the state-selected orbit/fibre/Jordan conjunction, never finite-difference
nilpotence by itself.

## SST: singularity-stopped scalar translation

### Directly owned enumerative input

The following primary sources establish a dense owner boundary.

- Joseph P. S. Kung, [*The cycle structure of a linear transformation over a
  finite field*](https://doi.org/10.1016/0024-3795(81)90227-5), `Linear
  Algebra and its Applications` 36 (1981), 141--155, develops the finite
  linear cycle index.
- Richard Stong, [*Some asymptotic results on finite vector
  spaces*](https://doi.org/10.1016/0196-8858(88)90012-7), `Advances in
  Applied Mathematics` 9 (1988), 167--199, extends the matrix cycle-index
  formulation.
- Kent Morrison, [*Eigenvalues of Random Matrices over Finite
  Fields*](https://aimath.org/~morrison/Research/ERMFF.pdf) (1999
  manuscript), states the \(M_n(q)\) factorization by rational-canonical
  primary components.
- Kent Morrison, [*Matrices over \(\mathbb F_q\) With No Eigenvalues of 0 or
  1*](https://aimath.org/~morrison/Research/mnev01.pdf) (2004 note), gives
  explicitly the forbidden-linear-factor generating function and attributes
  its cycle index to Kung and Stong.
- Jason Fulman, [*Cycle indices for the finite classical
  groups*](https://doi.org/10.1515/jgth.1999.017), `Journal of Group Theory`
  2 (1999), 251--289, and [*Random matrix theory over finite fields: a
  survey*](https://arxiv.org/abs/math/0003195), record the broader cycle-index
  technology.

These sources own the local series
\(L_q(u)=\prod_{j\ge1}(1-u/q^j)^{-1}\), factor independence for selected
linear polynomials, and prescribed/forbidden eigenvalue coefficients.
Consequently formula (M6) in `THEOREM_SPIKES.md` is a specialization and
receives zero contribution credit.

### Literal-query result

The exact stopped update \(A\mapsto A+I\) for invertible \(A\), with singular
\(A\) fixed, was not located in the bounded literal pass.  That nonhit is not
decisive: P166 already supplies the internal state-gated translation-orbit
proof shell.  Only the gap-marked conjunction remains, which is why SST is a
reserve rather than a recommendation.

**Owner status:** `ENUMERATOR_DIRECT / LITERAL_NONHIT / INTERNAL_TRANSFER`.

## Direct-owner kills

### Self-power residues

Pär Kurlberg, Florian Luca, and Igor Shparlinski,
[*On the fixed points of the map \(x\mapsto x^x\) modulo a
prime*](https://doi.org/10.4310/MRL.2015.v22.n1.a8), `Mathematical Research
Letters` 22 (2015), 141--168, studies the literal map and its finite dynamical
fixed points.

Joshua Holden, Pamela A. Richardson, and Margaret M. Robinson,
[*Counting Fixed Points and Rooted Closed Walks of the Singular Map
\(x\mapsto x^{x^n}\) Modulo Powers of a
Prime*](https://doi.org/10.1134/S2070046620010021), `p-Adic Numbers,
Ultrametric Analysis and Applications` 12 (2020), 12--28, extends the same
self-power family to fixed points and rooted closed walks.

Thus `C07/SPR` is a literal owner hit, not merely a nearby-topic hit.

### Arithmetic \(p\)-derivation

Alexandru Buium, Claire C. Ralph, and Santiago R. Simanca,
[*Arithmetic differential operators on
\(\mathbb Z_p\)*](https://doi.org/10.1016/j.jnt.2010.07.011), `Journal of
Number Theory` 131 (2011), 96--105, explicitly takes the Fermat quotient
operator as the arithmetic derivative.  This directly owns the defining
operator in `C08/APD`; iterating its finite two-digit truncation did not yield
a uniform residual.

### General finite-field functional-graph boundary

José Alves Oliveira and Fabio Enrique Brochero Martínez,
[*Dynamics of polynomial maps over finite
fields*](https://arxiv.org/abs/2201.00954), `Designs, Codes and
Cryptography` 92 (2024), 1113--1125, develops complete functional graphs for
an index-controlled class \(x^nh(x^{(q-1)/m})\).  Related quadratic-extension
work includes Fabio E. Brochero Martínez and Hugo R. Teixeira,
[*On the functional graph of
\(c(X^{q+1}+aX^2)\)*](https://arxiv.org/abs/2111.11132).

Neither abstract is recorded as a literal owner of `C03/UCT` or `C09/FRD`.
They instead show that norm/cyclotomic quotients over quadratic extensions
are a dense active owner region.  Since both candidates reduce immediately
to such a quotient and leave no uniform independent clock, they are killed
without making a direct-ownership claim.

## Nonhits that do not rescue weak candidates

- No direct source for \(x\mapsto\operatorname {ord}_p(x)\) as an iterated
  self-map was located.  `C10/MOR` still fails because only the first
  Euler-\(\varphi\) fibre is uniform; the subsequent divisor dynamics varies
  with \(p\).
- No direct source for the conventionally totalized
  \(x\mapsto x!\pmod p\) functional graph was located.  `C11/FAC` still fails
  the internal P153 factorial firewall and the all-prime theorem test.
- No literal source for `C03/UCT`, `C05/ZMI`, or `C09/FRD` was claimed.
  Their kills are based on shallow or transferred mechanisms, so no novelty
  inference is needed.

## Final owner disposition

| Candidate | Owner conclusion |
|---|---|
| `SFD` | augmentation/difference input directly owned; literal feedback update not located; `OWNER_THIN / HOLD_EXTERNAL` |
| `SST` | cycle-index enumerator directly owned and forward shell transfers internally; reserve only |
| `SPR` | literal direct owner |
| `APD` | defining operator direct owner |
| `UCT/FRD` | dense quadratic-extension functional-graph region; no direct claim, killed on residual weakness |
| `MOR/FAC` | bounded nonhit only; killed independently of novelty |
