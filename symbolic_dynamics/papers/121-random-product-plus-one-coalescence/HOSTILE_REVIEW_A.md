# Hostile Review A — P121

## Review identity and provisional verdict

Role: independent nonauthor Reviewer A. I reconstructed the manuscript from
the complete author package and did not consult any later or prospective
Review B.

**Provisional verdict: `STOP/REWRITE`. External status remains `HOLD`.**

The mathematical derivations tested below are largely coherent, including
the Riccati signs, normalized pole residues, Sturm--Pringsheim induction,
first-moment dominant-pole analysis, marked-antichain coefficients, and the
explicit `r>=2` claim ceiling. The current contribution and owner boundary,
however, fail a direct-owner test. Disanto, Fuchs, Paningbatan, and Rosenberg
study the same uniformly ranked ordered binary-tree history statistic. If
their number of root configurations is `R_n`, then the paper's variable is
literally `X_n=R_n+1`. Their published recurrence, exact law recursion,
antichain correspondence, Riccati mean, identical dominant pole, and
second-moment analysis are not generic background; they are direct temporal
ownership. The manuscript does not cite this source.

## Package and independence boundary

Reviewed:

- `main.tex`, `main.pdf`, and `main_round0_original.pdf`;
- `references.bib`;
- `README.md`, `PAPER_PLAN.md`, `NARRATIVE_REPORT.md`,
  `CLAIMS_EVIDENCE.md`, `CONTROL_RESULTS.md`, and `BUILD.md`;
- `code/verify.py`, `code/verify.out`, and
  `code/marked_antichain_coefficients.tsv`.

No manuscript, bibliography, verifier, support document, PDF, shared ledger,
or Git state was modified.

## Independent reconstruction of the mathematics

1. Every active separator is an undeleted original boundary. Uniform choice
   among active separators therefore gives a uniform permutation of the
   `n-1` labels. Conditional on the last label `i`, the two relative side
   orders are independent and uniform, yielding
   `X_n =d 1+X_i X'_(n-i)` with uniform `i`.
2. On the full ordered evaluation tree, let `P_T(s)` mark antichains of
   internal vertices, including the empty antichain. Root inclusion gives the
   monomial `s`; root exclusion independently selects antichains in both
   subtrees. Hence `P_T=s+P_LP_R` and `P_T(1)` obeys the product-plus-one
   evaluation.
3. Uniform splitting gives
   `a_n(s)=s+(n-1)^(-1) sum_i a_i(s)a_(n-i)(s)`, so
   `A_z=A^2+s/(1-z)^2`. With `w=1-z`, the proposed `Y` satisfies
   `Y_ww+sY/w^2=0`, `Y(1)=Y_w(1)=1`. Because `d/dz=-d/dw`,
   `A=Y_w/Y` has the correct Riccati sign. The `s=1/4` formula is the
   removable coalescence of the two Euler exponents.
4. Expanding `(1+ab)^r` gives
   `F_r'=sum_(k<=r) binom(r,k)F_k^2`. Separating `F_r^2` and writing
   `F_r=-U_r'/U_r` gives `U_r''+G_rU_r=0` with the stated initial data.
5. If the previous level has residue one at `rho_(r-1)`, then
   `G_r(x)=r/(rho_(r-1)-x)^2+O((rho_(r-1)-x)^(-1))`. Comparison with an
   oscillatory Euler equation of coefficient `c>1/4` forces a positive zero
   before `rho_(r-1)`. A first zero is simple, so the new logarithmic
   derivative has residue one. Positivity and Pringsheim exclude a smaller
   complex radius; Cauchy--Hadamard yields only the limsup.
6. At `r=1`, the Euler solution has zeros determined by the cosine factor.
   On `|z|<1`, `w=1-z` lies in the right half-plane and the principal log is
   single-valued. The first zero is
   `rho=1-exp(-2*pi/(3*sqrt(3)))`; the next zero and the logarithmic branch
   point are farther away. Subtracting the normalized pole gives the stated
   coefficient asymptotic with leading constant one.
7. Since `xy+1>=x+y`, with equality iff one factor is one, equality at every
   recursive split forces a planar comb. There are `2^(n-2)` endpoint-choice
   deletion orders among `(n-1)!`, giving the minimum mass.

This chain did not reveal a theorem-level counterexample. It does reveal an
exact change of variables to a published statistic, addressed next.

## Severity-ranked findings

### CRITICAL

#### C1. A direct owner contains the same random variable up to `+1`

The missing direct source is:

> Filippo Disanto, Michael Fuchs, Ariel R. Paningbatan, and Noah A. Rosenberg,
> “The distributions under two species-tree models of the number of root
> ancestral configurations for matching gene trees and species trees,”
> *Annals of Applied Probability* 32 (2022), 4426--4458,
> [DOI 10.1214/22-AAP1791](https://doi.org/10.1214/22-AAP1791);
> [arXiv:2006.09106](https://arxiv.org/abs/2006.09106).

For a uniformly selected ordered unlabeled history with `n` leaves, their
Proposition 3.5 (numbering in the published version) uses a uniform split and
states

```text
R_1=0,
R_n =d (R_I+1)(R'_(n-I)+1).
```

It also gives the exact divisor-based distribution recursion. Set

```text
X_n := R_n+1.
```

Then, object for object,

```text
X_1=1,
X_n =d 1+X_I X'_(n-I),
```

which is Theorem 2.1 and Equation (2.3) of the present manuscript. The same
source identifies root configurations with antichains of the pruned
internal-node tree. It derives the Riccati equation and closed trigonometric
generating function for the mean, locates the same pole
`rho=1-exp(-2*pi/(3*sqrt(3)))`, obtains the same exponential constant
`1.42538682...`, and develops a Riccati/linearized second-moment and variance
analysis. The [authors' primary PDF](https://rosenberglab.stanford.edu/papers/DisantoEtAl2022-AAP.pdf)
makes these overlaps explicit.

This is not cured by the current general citations to BSTs, forest ideals,
or antichains. The current assertions that the residual includes the finite
law, antichain interpretation, and elementary mean are materially false as
an ownership subtraction.

**Required action.** Stop the current paper narrative. Add the direct owner,
prove `X_n=R_n+1` explicitly, and assign zero contribution credit claim by
claim to:

- the uniform-history split model;
- the complete finite distribution recursion;
- the unmarked antichain/root-configuration interpretation;
- the first-moment Riccati equation and its closed form;
- the dominant pole, exponential mean, and leading normalization; and
- the order-two moment/variance Riccati neighborhood.

Only after that subtraction may the remaining candidates—cardinality marking,
the all-order hierarchy, the all-`r` strict radius ladder, and the exact comb
mass—be independently owner-gated and evaluated for paper-scale sufficiency.

### MAJOR (mathematics)

None established. In particular:

- the sign in `A=Y_w/Y` is correct because `partial_z=-partial_w`;
- the first positive zero of each `U_r` is simple by ODE uniqueness;
- Pringsheim is used only to exclude a smaller radius, not to claim a unique
  dominant complex singularity;
- the first-moment zero classification does justify an annulus beyond `rho`;
  and
- the manuscript consistently stops at a coefficient limsup for `r>=2`.

The absence of a mathematical counterexample does not mitigate C1.

### MAJOR (owner/scope)

#### O1. The contribution list must be recomputed after direct subtraction

The abstract, Introduction items (i)--(iv), ownership section, README,
planning documents, and claims/evidence map all treat the exact law and mean
as part of the residual conjunction. After C1, those items are prior results
in shifted notation. Moreover, the direct owner already treats the second
moment more strongly than this manuscript's generic `r>=2` limsup ceiling.

**Required repair.** Rewrite rather than append one citation. A defensible
new contribution statement would need to say, at minimum:

1. the merge process is an encoding of the published root-configuration
   variable plus one;
2. the finite law and first-moment analysis are reproduced only to establish
   notation and receive zero credit;
3. the marked cardinality transform is compared literally with prior
   antichain-polynomial work;
4. the strict all-order radius ladder is isolated from the already analyzed
   first and second moments; and
5. the comb atom is checked against caterpillar/root-configuration extremal
   literature.

A bounded 2025--2026 search did not expose a later direct owner for the
all-order ladder, but that no-hit is bounded and cannot rescue the claims
already owned in 2022.

### MINOR

#### m1. Cite a precise Sturm comparison theorem or expand the interval step

The inference from the oscillatory Euler comparison solution to a zero of
`U_r` before `rho_(r-1)` is correct in outline, but compressed. State the
comparison theorem with the direction of the coefficient inequality, then
argue on two consecutive comparison zeros near the singular endpoint. This
will prevent a reader from having to reconstruct which solution's zeros
interlace.

#### m2. Keep the `r>=2` ceiling exactly as written if a rewrite proceeds

The current text correctly does **not** infer
`E[X_n^r]~rho_r^(-n)` from one positive local pole. It explicitly allows
other singularities on the convergence circle. Do not weaken this safeguard
during condensation. The direct owner's stronger order-two analysis should
be credited separately; it does not license full asymptotics at all orders.

#### m3. Make the shifted-owner convention visible in every coefficient table

If the table remains, label that its value at `s=1` is one plus the published
root-configuration count. Otherwise a reader can mistake exact agreement
with the old variable for independent corroboration.

## Fresh verification and build audit

### Canonical verifier

Commands run from the paper directory:

```bash
cmp -s <(PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py) code/verify.out
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
wc -c code/verify.out
```

Results:

- fresh run: `PASS`;
- exact assertions: `139,589`;
- exhaustive deletion histories through `n=9`;
- finite laws through `n=12` and raw moments through order six;
- moment and marked coefficient identities through `n=60`;
- coefficient artifact parsed and exactly matched through `n=12`;
- byte comparison exit status: `0`;
- canonical transcript: `528` bytes.

The code is deterministic, standard-library-only, and uses exact integer and
`Fraction` arithmetic. Its internal lanes genuinely compare literal adjacent
mergers, Cartesian evaluation, split-law DP, marked polynomial recursion,
moment recursion, and the committed TSV. It does not and cannot test the
Sturm/singularity or owner claims.

### Isolated build and PDF inspection

I copied `main.tex` and `references.bib` to a fresh `/tmp` directory and ran:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Results:

- six A4 pages, `385106` bytes, PDF 1.5;
- isolated PDF byte-for-byte equal to the stored `main.pdf`;
- no settled LaTeX/BibTeX warning, undefined reference/citation, box warning,
  or rerun request;
- 30 font rows, all embedded, subset, and Unicode mapped;
- empty Author metadata, no form, no JavaScript, and no encryption; and
- all six rendered pages visually inspected with no clipping, collision,
  displaced float, missing glyph, or unreadable formula.

Presentation quality is technically strong. It does not offset the direct
owner failure.

## Focused theorem stress tests

### Riccati linearization and marked transform

Direct differentiation confirms both logarithmic-derivative signs. The
initial conditions for `Y` follow from
`beta_++beta_-=1` and `beta_+-beta_-=delta`. The `s=0` specialization gives
`A=(1-z)^(-1)`, and the coefficient table agrees with exact histories. No
formula error was found.

### Strict pole ladder and Pringsheim step

The induction uses only the positive real pole of the preceding moment. The
coefficient `binom(r,r-1)=r` gives the required inverse-square forcing with
coefficient greater than `1/4`. At the new first zero, all lower moments are
analytic because `rho_r<rho_(r-1)`. A positive pole gives radius at most
`rho_r`; Pringsheim plus the zero-free positive interval gives radius at
least `rho_r`. This proves a radius and limsup, not uniqueness on the circle.

### First-moment dominant pole

Within `|z|<1`, the principal logarithm has no branch ambiguity and cosine
zeros force positive real `w`. The `k=-1` zero is the unique singularity of
modulus `rho`; `k<=-2`, `k>=0`, and `z=1` are farther away. The normalized
logarithmic-derivative pole contributes coefficient `rho^(-n)` to
`[z^(n-1)]M`. The calculation is correct but directly owned under `R_n=X_n-1`.

### Claim ceiling at `r>=2`

The abstract, theorem, remark, controls, and support documents agree: one
positive simple pole and the exact exponential limsup are claimed, while a
unique dominant complex singularity and full coefficient asymptotic are not.
There is no hidden overclaim in the current wording.

## Mandatory rewrite checklist

1. Add and read the direct Disanto--Fuchs--Paningbatan--Rosenberg source.
2. State and prove the exact identification `X_n=R_n+1`.
3. Apply theorem-by-theorem zero credit to the finite law, unmarked
   antichains, mean Riccati/closed form/pole, and second-moment neighborhood.
4. Re-run an owner gate specifically on the marked-cardinality OGF, all-`r`
   strict ladder, and minimum-mass formula.
5. Rewrite the abstract, title framing, introduction, conclusion, README,
   claim map, narrative, and plan around only the surviving residual.
6. Add a precise Sturm comparison citation or expanded argument.
7. Preserve the `r>=2` ceiling and external `HOLD`.

Until items 1--5 are complete and the residual is shown to be paper-scale,
the correct internal decision is `STOP/REWRITE`, not
`GO_INTERNAL_AFTER_REPAIR`.
