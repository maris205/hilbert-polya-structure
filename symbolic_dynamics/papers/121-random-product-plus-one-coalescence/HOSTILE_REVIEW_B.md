# Hostile Review B — P121 owner rewrite

Status: **independent nonauthor review / GO_INTERNAL / EXTERNAL HOLD**.

Scope: the current manuscript, support documents, exact verifier and
coefficient artifact, current and round-two PDFs, and the direct 2022 owner.
I did not consult the other hostile review.  This review tests the rewritten
paper from the rule upward and does not certify novelty, priority, or public
release.

## Verdict and severity

**GO_INTERNAL.  EXTERNAL HOLD.**

Severity count: **critical 0; major 0; minor 0**.

I found no false recurrence, sign error, missing boundary case, analytic gap,
or ownership overclaim at the paper's deliberately narrow internal ceiling.
The direct owner collision has been correctly absorbed rather than hidden:
the adjacent process is an encoding of the same Yule root-configuration
statistic after the exact shift `X=R+1`.  The claimed residual begins only
after the owned split/law, unmarked antichains, mean, and second-moment
analysis have been removed.

One provenance observation is nonblocking.  Section 2.4.4 of the 2022 owner
itself recalls the caterpillar extremum from an earlier Disanto--Rosenberg
paper.  P121 says only that the fact is "already recorded" in the 2022 paper
and assigns it zero credit, so the statement is accurate.  An eventual
external historical account could cite the earlier source directly, but no
priority claim is currently made and this is not an internal defect.

## 1. Literal process, uniform split, and objectwise owner shift — PASS

With `j` current blocks, there are exactly `j-1` surviving original
boundaries.  Selecting a current adjacent pair uniformly is therefore the
same as deleting a uniformly chosen surviving original boundary.  The full
boundary-deletion order is a uniform permutation of `1,...,n-1`.

The last-deleted boundary is the evaluation-tree root.  Conditional on it
being boundary `i`, the relative orders of the `i-1` left boundaries and
the `n-i-1` right boundaries are independent uniform permutations.  Hence

```text
X_1=1,
X_n =d 1 + X_I X'_(n-I),       I uniform on {1,...,n-1},
```

and the displayed finite-law recursion follows by conditioning on the two
side values.  The manuscript explicitly warns that reversing the deletion
order changes the Cartesian-tree convention; the orientation is fixed.

For a fixed ordered history `T`, the merger evaluation satisfies

```text
V(leaf)=1,
V(T)=1+V(T_L)V(T_R).
```

The root-configuration recurrence is

```text
R(leaf)=0,
R(T)=(R(T_L)+1)(R(T_R)+1).
```

Structural induction therefore gives `V(T)=R(T)+1` for every coupled
history, not merely equality in distribution.  This agrees exactly with
Proposition 3.5 of the direct owner after shifting the variable.

Primary source audit:
[Disanto--Fuchs--Paningbatan--Rosenberg, Annals of Applied Probability 32
(2022), DOI 10.1214/22-AAP1791](https://doi.org/10.1214/22-AAP1791).
Its Proposition 3.5 states `R_1=0`, the uniform split, independent side
copies, and the recursive finite distribution.  Its Section 3.2 gives the
nonempty-antichain correspondence.  P121 gives all of this zero
contribution credit.

## 2. Cardinality-marked antichains and closed transform — PASS

For the ancestry poset of internal vertices, an antichain either contains
the root and is exactly the root singleton, or excludes the root and is an
independent pair of subtree antichains.  Thus

```text
P_T(s)=s+P_L(s)P_R(s),       P_leaf(s)=1.
```

At `s=1`, `P_T(1)=R(T)+1=X(T)`; this specialization is owned.  Averaging
over the uniform split gives

```text
a_n(s)=s+(1/(n-1))*sum_(i=1)^(n-1) a_i(s)a_(n-i)(s).
```

Because `A(z,s)=sum_(n>=1) a_n(s)z^(n-1)`, multiplication by
`(n-1)z^(n-2)` produces

```text
A_z=A^2+s/(1-z)^2,       A(0,s)=1.
```

The forcing sign and power are correct: the constant `s` contributes
`s*sum_(n>=2)(n-1)z^(n-2)=s/(1-z)^2`.

For `w=1-z`, let `delta=sqrt(1-4s)` and
`beta_±=(1±delta)/2`.  The displayed

```text
Y=(beta_+ w^beta_+ - beta_- w^beta_-)/delta
```

satisfies `Y_ww+sY/w^2=0` together with `Y(1,s)=Y_w(1,s)=1`.
Since `d/dz=-d/dw`, the **positive** logarithmic derivative `A=Y_w/Y`
obeys `A_z=A^2+s/w^2` and has the right initial value.  The sign in the
closed form is therefore correct.  Differentiating `beta*w^beta` at
`beta=1/2` gives the stated removable value
`w^(1/2)(1+(log w)/2)` at `s=1/4`.  At `s=0`, `Y=w` and `A=1/w`, correctly
counting the unique empty antichain.  At `s=1`, the coefficients specialize
to the mean of `X_n`.

The direct 2022 paper counts nonempty antichains but does not state this
cardinality-marked bivariate transform.  P121 nevertheless labels the
focused search only a bounded non-hit and makes no novelty claim.

## 3. Arbitrary raw-moment hierarchy — PASS

Conditioning on the split and expanding

```text
(1+ab)^r=sum_(k=0)^r binom(r,k)a^k b^k
```

gives exactly

```text
(n-1)m_(r,n)
  =sum_(i=1)^(n-1) sum_(k=0)^r binom(r,k)m_(k,i)m_(k,n-i),
F_r'=sum_(k=0)^r binom(r,k)F_k^2,
F_r(0)=1.
```

No mixed `k,l` term is missing: each binomial summand contains the same
power `k` on the independent left and right values.  The `r=0` lane reduces
to `F_0'=F_0^2`, so `F_0=(1-z)^(-1)`.  The `r=1,2` cases are equivalent,
under `X=R+1`, to the owner's mean and second-moment/variance neighborhood
and are explicitly assigned zero credit.  The residual is the arbitrary-
order interface and its use from `r=3` onward.

## 4. Sturm comparison and strict pole-radius ladder — PASS

Writing

```text
F_r'=F_r^2+G_r,
G_r=sum_(k=0)^(r-1) binom(r,k)F_k^2,
F_r=-U_r'/U_r,
U_r''+G_r U_r=0,
U_r(0)=1, U_r'(0)=-1
```

is correct.  Assume the earlier radii and normalized poles.  At the positive
point `rho_(r-1)`, every `F_k` with `k<=r-2` is analytic because
`rho_(r-1)<rho_k`.  The only singular summand in `G_r` is
`binom(r,r-1)F_(r-1)^2`, hence

```text
G_r(x)=r/(rho_(r-1)-x)^2+O(1/(rho_(r-1)-x)).
```

Choose `1/4<c<r`.  Near the preceding pole, `G_r` dominates
`c/(rho_(r-1)-x)^2`.  Every nonzero solution of the comparison Euler
equation is log-oscillatory because `c>1/4`, with infinitely many zeros
approaching `rho_(r-1)`.  Sturm comparison therefore places a zero of
`U_r` between consecutive comparison zeros unless `U_r` has already
vanished.  Its first positive zero `rho_r` consequently satisfies
`0<rho_r<rho_(r-1)`.

Because `G_r` is analytic at `rho_r`, ODE uniqueness excludes a double zero
of `U_r`.  A simple zero gives

```text
-U_r'(z)/U_r(z)=1/(rho_r-z)+O(1),
```

so the residue normalization is exactly one, with the stated sign.

The radius argument also survives hostile scrutiny.  The coefficients
`E[X_n^r]` are strictly positive.  The pole at `rho_r` gives radius at most
`rho_r`.  If a complex zero or another singularity forced a smaller radius
`R`, Pringsheim would force a singularity at the positive point `R`.
However, `G_r` is analytic there and the definition of the first positive
zero gives `U_r(R) != 0`; the logarithmic derivative is analytic in a
neighborhood of `R`, a contradiction.  Therefore the complex convergence
radius is exactly `rho_r`.

Cauchy--Hadamard gives
`limsup m_(r,n)^(1/(n-1))=rho_r^(-1)`, and changing to exponent `1/n` does
not change the finite positive limit superior.  The proof does not exclude
other singularities on `|z|=rho_r`, so the manuscript correctly stops at a
limsup for `r>=3`; it does not claim coefficient equivalence or a unique
dominant pole.

As a numerical stress test independent of the stated finite horizon, I
extended the exact moment recurrence to `n=100`.  The inverse consecutive-
coefficient ratios for `r=1,...,6` were approximately

```text
0.701563940808, 0.488998631729, 0.339041094618,
0.234055263336, 0.161002584958, 0.110421185536,
```

strictly consistent with the proved cascade.  This is only a regression
check; the proof, not the computation, establishes the theorem.

## 5. Mean and second-moment ownership — PASS

The mean formula has the correct shifted normalization.  With
`F_1=sum E[X_n]z^(n-1)`, the Euler solution gives the positive simple pole

```text
rho_1=1-exp(-2*pi/(3*sqrt(3)))=0.7015639408...
```

and local form `1/(rho_1-z)`, hence leading coefficient
`E[X_n]~rho_1^(-n)`.  The owner derives the same mean growth for `R_n`; the
shift changes only analytic/lower-order terms.

The direct owner's Section 5.3 derives a Riccati equation for `E[R_n^2]`,
locates its unique simple dominant root near `0.4889986317`, and obtains the
order-two growth `2.0449954971...^n`.  Under `X=R+1`, adding
`2E[R_n]+1` does not alter that dominant radius.  P121 does not reclaim
this result and explicitly describes it as a stronger owned order-two base.

## 6. Minimum value and exact endpoint mass — PASS

For positive integers,

```text
xy+1-x-y=(x-1)(y-1)>=0,
```

with equality exactly when one factor is one.  Induction through the split
therefore gives `X_n>=n`.  Equality requires minimal values on both sides
and an endpoint split `i=1` or `i=n-1` at every internal step.  These are
exactly the planar comb histories.

There is one minimum history at `n=2`.  For every `n>=3`, the last boundary
can be the left or right endpoint and the remaining side must be a minimum
history, so `c_n=2c_(n-1)=2^(n-2)`.  Since all `(n-1)!` boundary orders are
equally likely,

```text
P(X_n=n)=2^(n-2)/(n-1)!.
```

The 2022 owner explicitly records that the maximally asymmetric
caterpillar minimizes the number of root configurations.  P121 assigns
that minimizer zero credit and retains only the exact uniform ordered-
history mass, without a priority claim.

## 7. Exact controls — PASS

I ran the paper-local standard-library verifier from scratch with bytecode
writing disabled.

- status: **PASS**;
- exact assertions: **139,589**;
- every boundary order through `n=9`;
- full laws, moments through order six, and minimum atoms through `n=12`;
- moment and marked coefficient identities through `n=60`;
- independent mean Euler-series coefficients through `n=60`;
- committed TSV parsed and exactly matched through `n=12`;
- fresh stdout: **536 bytes**, byte-identical to `code/verify.out`.

The verifier correctly labels the `r>=3` radius theorem and every ownership
statement noncomputational.  No infinite analytic claim is inferred from
finite enumeration.

## 8. Isolated build and seven-page inspection — PASS

In a fresh temporary copy I ran

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

All four stages returned zero.  The isolated PDF, repository `main.pdf`,
and `main_round2.pdf` are byte-identical:

```text
SHA-256 0b35ba9ba81e772e6fc50264c4ddf98c3a312bc2dd1429fa28a2576eee5f23af
```

Mechanical audit:

- **7 A4 pages**, **393,230 bytes**;
- zero genuine LaTeX/BibTeX warnings or errors, undefined references or
  citations, multiply-defined labels, box warnings, or rerun requests;
- bibliography closure: **9/9** cited entries;
- **30/30 fonts** embedded, subsetted, and Unicode-mapped;
- empty Author metadata; no creation/modification dates, forms, JavaScript,
  or encryption;
- no `??`, `[?]`, `[VERIFY]`, `TODO`, `FIXME`, or `internal draft` sentinel.

I rendered and inspected all seven pages at 144 dpi.  The long owner
paragraphs, marked transform, Sturm proof, mean formula, minimum proposition,
coefficient table, and bibliography are legible.  There is no clipping,
overlap, missing glyph, bad float placement, or unreadable equation.  The
seventh page is intentionally sparse because it contains the remainder of
the bibliography; this is not a defect.

## Required fixes and release boundary

No mathematical or mechanical fix is required for the next internal stage.
Verdict: **GO_INTERNAL**.

Public posting, submission, specialist contact, a novelty claim, a priority
claim, and any full `r>=3` coefficient asymptotic remain **HOLD**.
