# Paper28 successor source: independent mathematical delta review

Date: 2026-09-05.
Decision: `SOURCE_SUCCESSOR_REVIEW_PASS`.
Proof status for the final reviewed additions: `PROVABLE AS STATED`.

## Bound inputs and scope

- Final candidate: `paper-successor-20260905/main.tex`, 84,983 bytes,
  1,855 LF bytes, SHA-256
  `7beb4f783cd370dc4b0d9d1e9178e3e48ce1ef9ed1497e0e9883b10739d4a1f9`.
- Frozen baseline: `paper/main.tex`, 73,733 bytes, 1,605 LF bytes,
  SHA-256 `bdc7a1edc06b3f8cfc75c6b47a8c24180883d24eef878c70d857588d19f1762e`.
- The complete source diff has precisely three insertion blocks, in
  Sections 3.2, 5.3 and 6.4. The final delta is 11,250 bytes and 250 LF bytes.
  The original text is not deleted or rewritten. Exact text comparisons
  preserve the eight section headings, 32 subsection headings, and sequence
  of theorem-like environments. The preamble, main theorem, citations and
  existing result environments are outside the insertion blocks and unchanged.
  Ten equation labels are added; a static scan finds no duplicate labels.

This is a complete review of those additions and their necessary local
dependencies, not a reopening of the frozen manuscript's entire prior R2
review. The reviewer read both requested skills, `proof-writer` and
`paper-write`, and used their assumption, proof-gap and claim-boundary checks.
The bounded review request governs the output: only this review document is
authored, with no source rewriting, template change or additional review loop.
No compiler, scientific program, live dependency access or old-build access
was used. Numerical expressions below were independently derived by hand
from the displayed definitions, not accepted from the author's arithmetic or
successor-note summary.

## Claim, assumptions and dependency map

The additions claim (i) an explicit finite inequality certificate and robust
rational/integer seed construction for the existing strict selector cone,
(ii) explicit leading-form recursions for the existing chambered
coefficient-uniform degree lift, and (iii) an exact worked decoder and
product-order check for the existing three-phase fixture. They do not claim
an enlarged main theorem, a new universality result from the fixture, or a
page-count/build acceptance result.

The cone argument uses nonempty finite integral supports, selected elements
belonging to those supports, equal totals on each side, a permutation $P$,
and the existing strict V-max/W-min residual convention. The leading-form
argument additionally uses the stated characteristic-zero field, nonzero
displayed coefficients, exponent coordinates at least two, positive initial
weights and the strict first-carry chamber. The decoder uses the incidence
construction, integer base $\lambda>1$, positive integral digits below that
base, and the stated marked phase, length, permutation and dictionary data.

The dependencies are local and explicit:

1. The pulled-back cone and W sign reversal determine the rows of $G$;
   finite row bounds and homogeneity determine the certificate.
2. The shear composition and strict selectors/carries determine the unique
   top-degree support term; the fixed weighted polynomial-ring domain
   property determines its nonzero leading form.
3. The fixture's occurrence sets determine its supports and digits; the
   ordered rank-one product identity determines its prefixes and monodromy;
   integer base expansion determines the decoder.

## Proof verification: Section 3.2

**Step 1 — row orientation and count.** A pulled-back V comparison is
$(\alpha_j-\gamma)^{\mathsf T}P^jx>0$, whereas a W-min comparison is
$(\eta-\beta_j)^{\mathsf T}P^jx>0$. The coordinate rows enforce $x_i>0$.
With all phase repetitions retained, there are exactly
$r+\ell(|E_V|-1+|E_W|-1)$ rows. Thus the displayed $Gx>0$ is exactly the
existing cone, not its closure or a reversed W-max cone.

**Step 2 — uniform perturbation margin.** For a strict seed $x$, finitely
many positive row evaluations give $\delta(x)>0$. The coordinate rows
ensure $N_G\geq r>0$ and $L_G\geq1$. For each row, the elementary bound
$$
 |G_h(v-x)|\leq\|G_h\|_1\|v-x\|_\infty
 \leq L_G\|v-x\|_\infty<\delta(x)/2
$$
implies $(Gv)_h>\delta(x)/2$. The inequality directions and strict final
bound are correct. This controls the specified selector inequalities and
positivity, not a momentum carry or a canonical distance to the fan walls.

**Step 3 — rational rounding.** An integer $N>L_G/\delta(x)$ exists.
Coordinatewise nearest-grid rounding gives error at most $1/(2N)$, strictly
less than the margin radius. Either choice at a rounding tie satisfies that
bound. Hence $v$ is positive and strict, and $Nv$ is a positive integer
seed. There is no missing separate positivity assumption on the rounding.
The statement supplies existence from an interior seed, not an efficient
algorithm for discovering a seed or a bound on witness size.

**Step 4 — certificate and degeneracies.** Scaling $x$ by $1/\delta(x)$
gives $Gz\geq\mathbf1$; conversely any such $z$ is strict. For rational
$z$, clearing positive common denominators makes the inequalities exact
integer comparisons. In fact the rounded integer seed above also has
integral positive row values, hence values at least one. No margin is
defined or used when the cone is empty. A singleton support contributes no
competitor row; if both sides are singletons, $G$ consists of coordinate
rows and all arguments still apply. Wall points do not satisfy the strict
certificate argument.

## Proof verification: Section 5.3

**Step 1 — one fixed ring.** Work in
$\mathbb{k}[X_i,Y_i:i\in I]$ with the original weights $(u_0,m_0)$.
Finite support gives a maximum weighted degree even for real, nondiscrete
weights. If nonzero polynomials have leading forms $L$ and $J$, every term
using a lower-weight component has weight strictly below the sum of their
degrees. Their top-weight product is $LJ\ne0$, since this polynomial ring
is a domain. Thus the leading form of the product is $LJ$. This justification
does not assume algebraic independence of the leading forms.

**Step 2 — V shear.** Substituting the coordinate polynomials of $F^n$ into
$p+\nabla V(q)$ gives exactly the displayed formula for
$\widetilde h_{n,i}$. The derivative product indexed by $\alpha$ has
degree $\alpha^{\mathsf T}u_n-(u_n)_i$. Its selected-minus-competitor
difference is $(\alpha_n-\gamma)^{\mathsf T}u_n>0$; the common derivative
subtraction does not change the comparison. The carried polynomial has
degree $(m_n)_i<(A_{\alpha_n}u_n)_i$. Therefore the displayed selected
product, with scalar $\xi_{a_n}(\alpha_n)_i$, is precisely
$\widetilde J_{n,i}$.

**Step 3 — W shear.** Put $v_n=A_{\alpha_n}u_n$. The position polynomial
before permutation is $f_{n,i}+\partial_iW(\widetilde h_n)$. The selected
W derivative degree is $\beta_n^{\mathsf T}v_n-(v_n)_i$.
The inherited W sign reversal makes selected-minus-competitor degree
positive, and the carry theorem gives
$(u_n)_i<(B_{\beta_n}v_n)_i$. These are two distinct exclusions: a support
competitor cannot reach the maximum, and the position carry cannot reach
it either. They yield exactly the displayed $\widetilde L_{n,i}$ product
with scalar $\zeta_{b_n}(\beta_n)_i$.

**Step 4 — permutation, induction and scope.** From $Pe_j=e_{Pj}$,
$(Pz)_i=z_{P^{-1}i}$, giving both final index recursions in the text;
the star is fixed. At depth zero the leading forms are $X_i,Y_i$.
Every derivative exponent is nonnegative, every derivative scalar is
nonzero by characteristic zero and the stated nonzero coefficients, and
every selected product remains nonzero by the preceding domain argument.
This closes induction for every $n\geq0$ and every allowed coefficient
tuple, including coefficients of different signs. Singleton competitor
families cause no problem. Ties, zero coefficients, positive characteristic
derivative vanishing, or failure of the carry chamber are not silently
included. The calculation is of actual weighted leading forms in this
fixed ring, not ordinary total degree or a varying weight assignment.

## Proof verification: Section 6.4

**Step 1 — independently reconstruct the fixture.** The occurrence sets are
$S_A=\{0,2\}$, $S_B=\{1\}$, $T_X=\{0,1\}$ and $T_Y=\{2\}$.
Putting $\rho=2,K=1$ into the incidence definition gives, in the stated
coordinate order,
$$
 \alpha_A=(3,2,3,3),\quad\alpha_B=(2,3,2,4),\quad
 \beta_X=(2,2,3,4),\quad\beta_Y=(3,3,2,3).
$$
Their totals are $11$, so $c=10\alpha-\beta$ and $\lambda=100$.
The selected digit rows are independently recovered as
$(28,18,27,26)$, $(18,28,17,36)$ and $(27,17,28,27)$.

**Step 2 — rotations, prefixes and matrix.** The row action is
$(v_0,v_1,v_2,v_\star)P=(v_1,v_2,v_0,v_\star)$, the opposite index shift
to the column spike. Consequently the three rotated rows are exactly
$(28,18,27,26)$, $(28,17,18,36)$ and $(28,27,17,27)$.
Using $R_{s+1}^{\mathsf T}=100R_s^{\mathsf T}+c_s^{\mathsf T}P^s$ gives
$$
 R_2^{\mathsf T}=(2828,1817,2718,2636),\qquad
 R_3^{\mathsf T}=(282828,181727,271817,263627).
$$
The successive row sums are $99$, $9999$ and $999999$. Since $P^3=I$,
each displayed entry of the manuscript's four-by-four matrix is checked by
adding the appropriate identity entry to this common row; all 16 entries
are consistent.

**Step 3 — all coordinate digits and side information.** In base $100$ the
four coordinates of $R_3$ have digit strings $28|28|28$, $18|17|27$,
$27|18|17$ and $26|36|27$. Grouping by place yields the three rotated
rows above. Applying $P^{-1}$ to the second and $P^{-2}$ to the third
recovers the original three digit rows. Only the support dictionary then
identifies the exponent pairs, and its literal names give
$((A,X),(B,X),(A,Y))$. The repeated $A$ is matched to one support, not
split into two labels.

For general length, set $k=\ell-1-j$. Division of the integer $r_i$ by
$\lambda^k$ and then reduction modulo $\lambda$ gives
$$
 d_{j,i}=\left\lfloor r_i/\lambda^k\right\rfloor
       -\lambda\left\lfloor r_i/\lambda^{k+1}\right\rfloor.
$$
This is the manuscript's formula, including both endpoint phases.
Integrality is important: $1\leq d_{j,i}\leq\lambda-1$ implies
$0<r_i\leq\lambda^\ell-1$. All required integrality comes from the
incidence construction, so it is not an added hypothesis. Neither unknown
length/permutation nor arbitrary input matrices are claimed to be inferred
by the formula.

**Step 4 — scalar and reversed-product checks.** The scalar forcing is
$10\cdot14-13=127$. Independently,
$$
 R_3^{\mathsf T}u_0=999999+282828=1282827
 =127(10000+100+1).
$$
This agrees with $t_3$, but does not recover the digit row. For the reversed
literal product, $c_0^{\mathsf T}P^2=(27,28,18,26)$, so
$$
 10000(27,17,28,27)+100(28,17,18,36)+(27,28,18,26)
 =(272827,171728,281818,273626).
$$
Its sum is also $999999$. Thus both rank-one updates have eigenvalues
$100^3,1,1,1$, while their ordered digits differ. This is a valid
product-order/spectral-information check; it need not assert that the
reversed literal product is the original map's admissible selector orbit.
The finite fixture is not used to prove the universal construction theorem.

## Correction resolved and substantive value

The first reviewed version allowed optional row deduplication immediately
before equating $N_G$ to the unreduced row count. The reviewer identified
that genuine counting ambiguity and requested only a local clarification.
The final bound version explicitly retains repeated rows in $G$ and defines
the displayed count before removal. That repair was read and verified;
it changes no scientific assumption or conclusion. No other unresolved
mathematical defect was found in the three additions.

The additions are substantive exposition and proof detail: Section 3.2
turns an existence statement into finite inequalities and a justified
rounding certificate; Section 5.3 makes the fixed-ring induction and the two
different noncancellation arguments explicit; Section 6.4 makes the entire
decoder, its rotation convention and its information losses independently
checkable. These are not merely repeated conclusions or typographic
padding, but neither are they represented as additional headline theorems.

## Open risks and handoff boundary

No mathematical delta blocker remains for the exact final hash above.
The frozen baseline remains unchanged. This reviewer made no manuscript,
macro, bibliography, validator or build modification. Publication pagination,
rendered equation/reference correctness, validator behavior, hermetic build
execution and PDF acceptance were not tested here and remain separate
authorized checks. This source PASS is not a build/PDF PASS or a Route A/B
evaluation, and does not relax any existing acceptance predicate.
