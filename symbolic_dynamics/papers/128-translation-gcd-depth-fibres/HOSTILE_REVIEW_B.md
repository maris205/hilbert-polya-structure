# Hostile Review B — P128 translation–GCD depth fibres

**Role:** second independent nonauthor reviewer  
**Review date:** 2026-08-31 UTC  
**Object reviewed:** repaired round1 package in
`papers/128-translation-gcd-depth-fibres/`  
**External status:** **HOLD_EXTERNAL**

## Verdict

**GO_INTERNAL.**  I independently reconstructed the literal iterate, the
irreducible-orbit exponent dynamics, the fixed-cut transfer trace, the
all-depth formal orbit Euler product, and the exact and capped terminal
fibres.  I did not inherit Review A's conclusion.  No theorem counterexample,
missing boundary, ownership overclaim, or reproducibility defect remains in
round1.

All three Review-A re-entry conditions are genuinely closed.  The transfer
proof now fixes labelled coordinates and proves one closed state path per
labelled residual vector, with neither rotation quotienting nor recounting by
zeros.  The canonical verifier now literally builds truncated polynomial
matrices `M_t(y/(1-y))`, powers them, takes their traces, and compares every
coefficient in scope with a separate vector enumerator.  The infinite product
is consistently and correctly bounded as a **formal orbit Euler product**.

This is an internal mathematical/package decision only.  Generic orbit-fold
mechanics, the old P01 scout outputs, P110's order-dual mechanism, and the
Garefalakis–Reis fixed-irreducible theory remain zero credit.  A bounded owner
non-hit is not novelty clearance; posting, submission, priority language, and
external circulation remain **HOLD_EXTERNAL**.

## Severity summary

| severity | count | disposition |
|---|---:|---|
| CRITICAL | 0 | no false theorem or corrupted artifact |
| MAJOR | 0 | all round1 re-entry conditions close |
| MINOR | 0 | no manuscript or support repair required |

## 1. Independent reconstruction of the dynamics

Let `q=p^a`, let `sigma f(x)=f(x+1)`, and let

```text
T(f)=gcd(f,sigma f),             Q=T^(p-1).
```

Translation by one has order `p`, including over a proper extension
`F_(p^a)`.  Thus the acting subgroup is the prime-subfield copy of `F_p`, not
the full additive group of `F_q`.  Since translation commutes with monic gcd,
induction gives

```text
T^t(f)=gcd_(0<=j<=t) sigma^j f.
```

At `t=p-1` the gcd uses the complete order-`p` orbit, so `Q(f)` is invariant.
The invariant ring is exactly `F_q[x^p-x]`; its monic degree series is
`1/(1-qz^p)`.  This remains correct for `a>1`: replacing `p` by `q` would be a
different action.

On a nonfixed irreducible orbit

```text
P_0, P_1=sigma P_0, ..., P_(p-1)=sigma^(p-1)P_0,
```

write the exponents of `f` as `e=(e_0,...,e_(p-1))`.  Up to reversing the
cyclic indexing, the exponent after `t` steps is

```text
e_i^(t)=min_(0<=j<=t) e_(i+j).
```

At time `p-1` all coordinates equal `m=min_i e_i`.  For the unique residual
vector `c=e-m(1,...,1)`, one has `c_i>=0` and `min_i c_i=0`.  Every sliding
window of length `t+1` contains a zero exactly when `c` has no cyclic positive
run of length `t+1`; hence its local stabilization depth is the longest cyclic
positive run `lambda(c)`.  Fixed irreducibles have no residual coordinate.
The global depth is the maximum of these local depths, with the empty maximum
equal to zero, and is at most `p-1`.

This verifies the manuscript's window identity and Lemma 2.1 for arbitrary
multiplicities, not merely squarefree inputs.

## 2. Fixed-cut trace: one labelled path, no rotation recount

For `0<=t<=p-1`, set `u=y/(1-y)` and index states by `0,...,t`.  A zero
coordinate sends every state to 0 with weight 1; a positive coordinate sends
`i` to `i+1` with weight `u` when `i<t`.  These are exactly the entries of the
displayed `M_t(u)`.

Fix the cut at the labelled coordinates `0,...,p-1`.  For an admissible
support, the state before coordinate `j` is forced to be the length of the
positive run immediately preceding `j`.  The support contains a zero because
`min c_i=0`; using any zero to compute the states recovers this same cyclic
assignment.  It does not create another path.  Conversely, an all-positive
closed path is impossible because every transition would strictly increase
the state, and every other closed path recovers a unique labelled support.
The all-zero vector has its unique all-zero path.  Replacing each positive
support entry by an arbitrary positive height contributes one factor
`u=y+y^2+...`.

Therefore

```text
R_(p,t)(y)=tr(M_t(y/(1-y))^p)
```

counts each labelled normalized exponent vector exactly once.  The trace is
neither a necklace/rotation quotient nor a sum over choices of zero; there is
no missing or extra factor of `p`.  This is the precise point left implicit in
round0, and the repaired proof closes it.

The edge cases are also exact:

```text
R_(p,0)=1,
R_(p,p-1)=(1-y^p)/(1-y)^p.
```

For `t=0`, only the zero residual is allowed.  For `t=p-1`, all nonnegative
vectors except the all-positive ones are allowed, giving
`(1-y)^(-p)-(y/(1-y))^p`.

## 3. All-depth formal orbit Euler product

Every irreducible translation orbit has length 1 or `p`.  If `b_d` is the
number of fixed degree-`d` irreducibles and `N_d(q)` is the usual irreducible
count, then

```text
a_d=(N_d(q)-b_d)/p
```

is the number of nonfixed degree-`d` orbits.  On each such orbit the
decomposition `e=m1+c`, `min c=0`, is unique.  The common-minimum pieces,
together with all powers of fixed irreducibles, form one arbitrary invariant
monic polynomial.  They therefore contribute the single factor
`1/(1-qz^p)` and are not counted again in a residual factor.

Unique factorization and the maximum-of-local-depths rule then give

```text
H_(q,p,t)(z)
  = 1/(1-qz^p) product_(d>=1) R_(p,t)(z^d)^(a_d).
```

The wording **formal orbit Euler product** is mathematically important and is
now used consistently.  No analytic convergence is asserted or needed: in
the coefficient of `z^n`, only irreducible degrees `d<=n` can contribute.
“Orbit” here refers to translation orbits of irreducible factors; it is not a
dynamical zeta product and does not assert multiplicativity of `Q`.

The extreme thresholds close independently:

```text
H_(q,p,0)=1/(1-qz^p),
H_(q,p,p-1)=1/(1-qz).
```

Thus consecutive CDF differences count exact depth layers, degree zero
contains the unique state `1`, `p=2` has only depths 0 and 1, and genuine odd
characteristic is exercised without an unstated `p>2` assumption.

## 4. Unit fibre and the full target law

Valuation by valuation, `Q(f)` retains the whole exponent of a fixed
irreducible and the common minimum on each nonfixed orbit.  It is invariant
and divides `f`.  The residual `r=f/Q(f)` has no fixed irreducible factor and
minimum zero on every nonfixed orbit, so `Q(r)=1`.  Both factors are forced.

For invariant `h`, the window gcd gives only the restricted identity

```text
Q(hr)=h Q(r).
```

It follows that multiplication is a degree-preserving set bijection

```text
{invariant monic h} x Q^(-1)(1)  ->  {all monic f},
(h,r)                             ->  hr.
```

It is not a monoid quotient.  Dividing the all-monic series by the invariant
series yields

```text
U_(q,p)(z)=(1-qz^p)/(1-qz),

U_(q,p,n)=q^n                    for 0<=n<p,
            q^n-q^(n-p+1)       for n>=p.
```

For every invariant monic target `h` of degree `m`, the exact degree-`N`
fibre is `U_(q,p,N-m)` for `N>=m` and is empty for `N<m`.  With `L=D-m`, the
degree-capped fibre is empty for `L<0` and otherwise is

```text
(q^(L+1)-1)/(q-1)                         if 0<=L<p,
(q^(L+1)-1-q^(L-p+2)+q)/(q-1)             if L>=p.
```

The second expression is exactly the geometric prefix
`sum_(n=0)^L U_(q,p,n)`: it subtracts
`q sum_(j=0)^(L-p) q^j`.  The seam `L=p`, the unit target `m=0`, and targets
larger than the cap all behave correctly.  Since every value of `Q` is
invariant, every noninvariant monic target has an empty fibre.  Thus the
displayed invariant-target theorem plus this immediate image observation
covers the full monic codomain.

The nonmultiplicativity firewall is literal in every characteristic.  Put

```text
a=x,                    b=(x^p-x)/x.
```

Each factor misses a member of the full linear translation orbit, so
`Q(a)=Q(b)=1`; their product is the invariant polynomial `x^p-x`, hence
`Q(ab)=x^p-x`.  Calling `Q^(-1)(1)` the **unit fibre**, not a kernel, is
therefore necessary and is done consistently in round1.

## 5. Fixed irreducibles and owner subtraction

The standard irreducible count

```text
N_d(q)=(1/d) sum_(e|d) mu(e) q^(d/e)
```

and the displayed fixed count are correct.  If `m=p^v s` with `(s,p)=1`,
then

```text
b_d=0 unless d=pm,
b_(pm)=(p-1)/(pm) sum_(e|s) mu(s/e) q^(p^v e).
```

Reis's Theorem 2(c) writes the same sum with divisor `d|m`, `(d,p)=1`;
substituting `d=s/e` gives the manuscript's formula exactly.  The formula,
the fixed-irreducible classification, and the immediate orbit quotient
`a_d` are correctly treated as externally owned inputs, not residual
contributions.

Primary technical records checked on 2026-08-31:

- Theodoulos Garefalakis, *On the action of GL2(Fq) on irreducible
  polynomials over Fq*, DOI
  [10.1016/j.jpaa.2010.10.015](https://doi.org/10.1016/j.jpaa.2010.10.015).
- Lucas Reis, *The action of GL2(Fq) on irreducible polynomials over Fq,
  revisited*, [arXiv:1608.03915](https://arxiv.org/abs/1608.03915), DOI
  [10.1016/j.jpaa.2017.06.008](https://doi.org/10.1016/j.jpaa.2017.06.008).

The internal firewall also closes:

- `P01` is an old scouting handle, not an earlier paper number.  Its literal
  map, sliding-window iterate, order-`p` clock, invariant ring, fixed counts,
  and old finite depth tables receive zero credit.  The manuscript subtracts
  the substance explicitly; the support plan and hostile gate identify the
  `P01` provenance.  Reprinting the temporary scout handle in the article is
  not needed for an honest claim boundary.
- P110 owns the order-dual cyclic semilattice fold, invariant endpoint,
  finite clock, and recurrent/fixed mechanism.  Remark 1.1 names P110 and
  excludes those generic conclusions.  P128's surviving internal claim is
  only the polynomial-specific normalized-exponent census/formal product
  together with the target-refined graded fibres.
- Standard transfer matrices and shifted-gcd/shiftless-factorization
  interfaces are background, not novelty claims.

The manuscript makes no novelty or priority assertion.  The owner search is
bounded and cannot establish absence; this is why **HOLD_EXTERNAL** remains
mandatory even though the internal theorem package passes.

## 6. Round1 re-entry and verifier audit

I read the verifier rather than relying on its transcript.

### 6.1 Literal matrix control

`transfer_matrix_series` constructs a `(t+1)x(t+1)` matrix over
`Z[y]/(y^10)` with:

```text
M[i,0]=1,
M[i,i+1]=y+y^2+...+y^9       for i<t,
```

and zero elsewhere.  `power_polynomial_matrix` performs truncated polynomial
matrix multiplication, raises this literal matrix to the characteristic
`p`, and the function sums the diagonal.  `audit_transfer_matrix_formula`
constructs the comparison side with direct labelled residual-vector
enumeration; it does not reuse the matrix.  For

```text
(p,t)=(2,0),(2,1),(3,0),(3,1),(3,2)
```

it compares all coefficients of weights `0,...,9`, giving exactly **50**
matrix assertions.  Truncating each positive-height series at weight 9 is
coefficientwise exact through that cap.

### 6.2 Separate global-product control

The matrix test is local; I do not overstate it as the implementation of the
whole Euler product.  Separately, `depth_cdf_formula` builds the invariant
factor and multiplies the direct residual-vector series over the computed
irreducible-orbit counts, coefficientwise through each degree cap.
`audit_lane` compares those coefficients with literal translation–gcd state
enumeration.  It also checks the invariant image, quotient reconstruction,
unit-fibre coefficients, every invariant target at every exact input degree,
capped target fibres, nonmultiplicativity, irreducible totals, fixed counts,
orbit partitions, the sharp depth, and the terminal CDF boundary.

I fresh-ran from the paper directory:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py \
  > /tmp/p128-review-b-verification.txt
cmp -s /tmp/p128-review-b-verification.txt code/verification_output.txt
```

The byte comparison exited 0.  The stable run reports:

```text
F4: 5,461 states, D=6, lane assertions 52,712
F8: 4,681 states, D=4, lane assertions 47,488
F9: 7,381 states, D=4, lane assertions 80,190
transfer-matrix assertions: 50
field-construction assertions outside the lane totals: 13
TOTAL_ASSERTIONS=180453
```

The three state boxes total **17,523** states.  The `F9` lane exercises all
depths `0,1,2`.  Fresh and canonical stdout have the identical SHA-256

```text
3b5e5bbbe94ec7ed7e689ff6a2cfeb2dc04a1ebc1ce9686c44194518ac1b1204.
```

The verifier hash is

```text
1b58fb8f71ac74082fb0ed9131a555a2ed4b7716da035e731ee9e5da0ac4a2fe.
```

The canonical sentinels correctly state that finite enumeration is
falsification evidence rather than proof, old clock/fixed/depth results are
zero credit, and external release remains on hold.

## 7. Isolated build and four-page artifact audit

I copied only `main.tex` and `references.bib` to a fresh temporary directory
and ran the required isolated sequence:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

All four stages exited 0.  The settled log and bibliography log contain no
LaTeX/package warning, undefined citation/reference, rerun request, overfull
or underfull box, or error.  The isolated PDF is byte-identical to both the
current PDF and the frozen round1 PDF.

Artifact facts:

```text
main.tex SHA-256
  fa1c10facf18dbb215896da5d4e6b36af446ce60f85208c1a632159f4d0ee1c7
references.bib SHA-256
  32c4d786ead0bd833713fa1609a76abdd612829c7739ccf088d90a7d8079328c
main.pdf / main_round1.pdf / isolated PDF SHA-256
  f49d7c850e6c607130b96ff80f409ac642bae21ecae80203857262f831677439
current/round1 size
  386,639 bytes
main_round0_original.pdf SHA-256
  e2c063e17ce35249978a5729d27194c9223a893865b62ef11ce8f90c2435d667
round0 size
  362,516 bytes
```

The immutable round0 artifact is present and distinct; current and round1
are exactly identical.

`pdfinfo` reports 4 unrotated A4 pages, PDF 1.5, no encryption, forms,
JavaScript, metadata stream, user properties, or custom metadata.  Author,
title, subject, and keyword metadata are blank, and no creation/modification
dates are emitted.  The rendered byline and running heads say only
`ANONYMOUS`; no identity is exposed.  All 28 reported font entries are
embedded, subsetted, and Unicode-mapped.

I rasterized and inspected pages 1–4 individually.  There is no clipped text,
formula collision, missing glyph, bad line break, margin overflow, blank
page, broken hyperlink display, or orphaned bibliography.  The long fibre
formulas, transfer proof, limitations paragraph, and page-4 references are
all visibly intact.

## Final gate

**GO_INTERNAL / HOLD_EXTERNAL.**

The round1 theorem ceiling that survives owner subtraction is exactly:

1. the all-threshold formal orbit Euler product built from normalized
   irreducible-orbit exponent vectors; and
2. the graded unit-fibre split with exact and capped fibres over every
   invariant endpoint (and empty fibres over noninvariant targets).

No repair is required for internal freeze.  This verdict does not authorize
external posting, submission, priority claims, or circulation; specialist
owner review and explicit authorization remain prerequisites.
