# Independent check of the minimal trace-selection theorem

Date: 2026-09-06.

## 1. Input and scope

The actual complete input was read and its hash verified:

- PAPER29_MINIMAL_TRACE_SELECTION_PROOF_V1_20260906.md;
- 438 lines;
- SHA256 e726963204552f5ac2b6afa8c05bdf3d224ece19a24337eed018f420cff4fb1c.

This is a bounded independent check of the new selection theorem,
including its exact coefficient and full period-vector quantifiers.
It does not merely endorse the earlier informal construction.
The independently accepted parent jet statements are used as inputs,
not reopened. No other reviewer's conclusions are used.

Only this new report is written. The author proof and all earlier
files remain unchanged.

## 2. Claim, assumptions and status

**Mathematical status: PROVABLE AS STATED.**

No extra hypothesis, corrected period restriction, or smaller type of
coefficient domain is needed. The prefactor in equation (7), the row
transformation determinant, the uniform singular-value profile and
the observation-count statement are correct.

The checked assumptions are precisely:

- fixed $k\ge6$ with $6\mid k$, and $d=k-3$;
- independently prescribed positive periods for all $k$ row labels;
- the stated nonempty supports and their unique all-plus markers;
- the normalized row $\kappa_p=(n_p\rho_p)^{-1}d_u\rho_p$;
- differentiation in $u$ at fixed nonzero $\epsilon$;
- constants depending on $k$, not on any of the prescribed periods.

Work is over $\mathbb C$. Write $a_p=1$ if $n_p=1$ and
$a_p=1-1/n_p$ otherwise, so $a_p\in[1/2,1]$.
The conclusion is a fixed product neighborhood in $(\epsilon,u)$,
not a shrinking region $u=\epsilon v$.
Correctness is separate from novelty, scientific value, page fit,
or candidate PASS; none of those decisions is assigned here.

## 3. Dependencies and proof map

The accepted parent proof supplies actual simple periodic branches,
the exact-period interpretation of primitive macro words, nonzero
traces and period-uniform holomorphic second-order jets.

The new proof steps requiring examination are:

1. Support separation at macro boundaries.
2. Binary polarization with independent occupation fractions.
3. Uniformly invertible output elimination and its determinant.
4. The complementary Fourier minor and the all-active resonant sum.
5. The exact prefactor and a fixed coefficient neighborhood for all
   period vectors.

All five steps close as written. Sections 4--9 below give the
independent checks.

## 4. Words, periods and correlation averages

The supports are $A=\{1,\ldots,d\}$, the $d$ singletons, and
$\{1,2\},\{2,3\}$. Since $d\ge3$, these are $k$ distinct nonempty
sets. For each row, $b_i$ denotes the indicator of its support.
For period at least two, the all-plus block is a unique
marker. Thus each macro word is primitive; period one needs no
separate repetition argument.

Different supports have different unions of negative phase labels.
A macro shift preserves that union. This proves disjointness when
periods coincide; different exact periods also cannot describe one
cycle. Simplicity and trace nonvanishing are inherited on one common
parent domain.

The inactive phases $k-2,k-1,0$ form three consecutive plus phases.
An adjacent or distance-two pair can therefore contain two active
phases only within one macro block. In that case the two negative
indicators occur together in the pattern blocks and together
vanish in the marker. Their joint occupation is $a_p$, not $a_p^2$.
If only one endpoint is active, the other sign is always plus.
This verifies the exact average
$$
1-2a_p(b_i+b_j)+4a_pb_ib_j
$$
for every relevant correlation, including period two and the
macro-boundary pairs. No equality among different $a_p$ is used.

## 5. Binary jet and independent occupations

Use the author notation
$$
\ell_i=-2\,\mathrm dh_i,\qquad
f_1=4\,\mathrm dE_1,\qquad f_2=4\,\mathrm dE_2,
$$
and let $m_i$ be the single-negative second-order covector.
Substitution of the preceding averages in the accepted jet gives
$$
\kappa_p=g+a_p\left[
\epsilon\sum_i b_i\ell_i+
\epsilon^2\left(\sum_i b_i m_i+q_{B_p}\right)\right]
+O(\epsilon^3),
$$
where
$$
q_B=4\sum_{i=1}^{d-1}b_ib_{i+1}\,\mathrm dE_i
   +4\sum_{i=1}^{d-2}b_ib_{i+2}\,\mathrm dD_{i+1}.
$$
The common $g$ is a polynomial jet, not an assertion that traces
of different actual return periods coincide. The stable-eigenvalue
terms remain in the accepted uniformly bounded remainder.

Weighting by $w_p=1/a_p$ leaves a common coefficient $w_p g$.
Set
$$
x_0=w_0-\sum_iw_i,\quad
x_\alpha=w_\alpha-w_1-w_2,\quad
x_\beta=w_\beta-w_2-w_3.
$$
The stronger separate inequalities
$$
x_0\le2-d<0,\qquad x_\alpha\le0,\qquad x_\beta\le0
$$
are valid on the entire cube $w_p\in[1,2]$. In particular
$$
\Gamma=x_0+x_\alpha+x_\beta\le2-d\le-1,\qquad
\Gamma/x_0\ge1.
$$
All denominators used in the proof are consequently uniformly
separated from zero.

## 6. Output transformation and exact determinant

Let $r_p=w_p\kappa_p$. The author's transformation is
$$
C=(r_0-\sum_i r_i)/x_0,\qquad U_i=r_i-w_iC,
$$
$$
V_\alpha=r_\alpha-r_1-r_2-x_\alpha C,\qquad
V_\beta=r_\beta-r_2-r_3-x_\beta C.
$$
Using original $r_i$, rather than the later $U_i$, in the last two
formulas is essential and is correctly specified in the input.
Direct substitution gives
$$
C=g+\epsilon^2q_A/x_0+O(\epsilon^3),
$$
$$
U_i=\epsilon\ell_i+
\epsilon^2(m_i-w_iq_A/x_0)+O(\epsilon^3),
$$
$$
V_\alpha=\epsilon^2(f_1-x_\alpha q_A/x_0)+O(\epsilon^3),
\quad
V_\beta=\epsilon^2(f_2-x_\beta q_A/x_0)+O(\epsilon^3).
$$
The zero coefficients vanish as functions on the whole $u$-domain.
Thus the last rows are jointly holomorphically divisible by
$\epsilon^2$, not merely small along $u=0$.

The determinant of the transformation from $K$ is exactly
$$
\boxed{\det T(a)=\frac1{x_0\prod_p a_p}.}
$$
One valid sequential realization is: weight all original rows;
subtract the original singles from the three compound rows;
divide the first compound row by $x_0$; then subtract its appropriate
multiples from the other rows. All operations except the weighting
and single division have determinant one, and the row order stays
$0,1,\ldots,d,\alpha,\beta$.

The explicit inverse in the author proof is valid. Both $T$ and
$T^{-1}$ are uniformly bounded on the occupation cube. These are
period-dependent but parameter-independent output operations.

## 7. Complementary minor and resonant identities

At zero,
$$
g_0=-\mathbf1^T/2,\qquad \ell_i=e_i^TL_1,\qquad
L_1=I-S-S^{-1},
$$
where $S$ is cyclic phase shift. The constant row and the $d$
consecutive rows $\ell_1,\ldots,\ell_d$ vanish on the two resonant
Fourier modes. Their nonconstant nonresonant minor has entries
$$
\bigl(1-2\cos(2\pi\nu/k)\bigr)k^{-1/2}\zeta_\nu^i.
$$
Here $\zeta_\nu=e^{2\pi i\nu/k}$.
Factoring the nonzero eigenvalues and one $\zeta_\nu$ from each
column leaves a Vandermonde matrix with exponents $0,\ldots,d-1$.
The nodes are distinct, so the first $k-2$ rows span the full
annihilator of the resonant subspace $R$.

For $z\in R$,
$$
f_1z=\tfrac12(z_1+z_2),\quad
f_2z=\tfrac12(z_2+z_3),\quad
4\,\mathrm dD_j(0)z=-3z_j.
$$
The two $f$ rows restrict independently to $R$. Their Fourier
column factors contain $1+e^{\pm i\pi/3}\ne0$, and the remaining
two-row determinant contains
$e^{-i\pi/3}-e^{i\pi/3}\ne0$.

The all-active quadratic term is, on $R$,
$$
q_Az=\tfrac12(z_1+z_d)-2\sum_{i=2}^{d-1}z_i.
$$
Since $d\equiv3\pmod6$, six-periodicity and zero sum over six
consecutive positions give $z_d=z_3$ and the interior sum $z_2$.
Using $z_1+z_3=z_2$ yields
$$
\boxed{q_A|_R=-f_1|_R-f_2|_R.}
$$
The minus sign in this identity is correct, including $k=6$.

Consequently the last two limiting rows, modulo the span of the
first $k-2$, differ from $(f_1,f_2)$ by a rank-one row update of
determinant $\Gamma/x_0$. The author's formula
$$
\det M(0,0)=\Delta_k\,\Gamma/x_0
$$
therefore has neither a missing sign nor a missing occupation factor.

## 8. Additional exact evaluation of the defined constant

The rational determinant defining $\Delta_k$ is already explicit
and its nonvanishing is proved by the preceding Fourier argument.
No change to that definition is needed. It can additionally be
evaluated in closed form:
$$
\boxed{\Delta_k=-3/8.}
$$

Here is an independent direct check of its sign and normalization.
In its last column, indexed $k-1$, only the first row is nonzero.
Expansion there reduces it to $(-1)^k/2$ times the determinant
with rows $\ell_1,\ldots,\ell_d,f_1,f_2$ on coordinates
$z_0,\ldots,z_{d+1}$.

Change these coordinates to
$$
(r_1,\ldots,r_d,z_0,z_1),\qquad
r_i=z_i-z_{i-1}-z_{i+1}.
$$
This transformation has determinant $(-1)^d$: moving the two
initial-coordinate rows to the front contributes no sign, and
the remaining triangular diagonal consists of $d$ entries $-1$.
On the subspace $r_1=\cdots=r_d=0$, writing $z_0=a,z_1=b$ gives
$z_2=b-a$, $z_3=-a$, $z_4=-b$. The last two outputs are
$$
f_1z=b-a/2,\qquad f_2z=b/2-a,
$$
whose determinant in $(a,b)$ is $3/4$. Thus
$$
\Delta_k=\frac{(-1)^k}{2}(-1)^d\frac34=-\frac38,
$$
because $d=k-3$. This evaluates the already defined constant; it
does not add a new hypothesis or amend the V1 theorem.

## 9. Uniform product domain, singular values and prefactor

With the analytic row scales
$$
\Lambda_\epsilon=\operatorname{diag}
(1,\underbrace{\epsilon,\ldots,\epsilon}_{d},
\epsilon^2,\epsilon^2),
$$
the matrix $M=\Lambda_\epsilon^{-1}T(a)K$ extends jointly
holomorphically across $\epsilon=0$ on a fixed parent $u$-domain.
The inherited remainder bounds stay uniform after the bounded
occupation operations and the indicated divisions.

The limiting determinant is bounded away from zero uniformly
on the occupation cube, since $\Gamma/x_0\ge1$ and
$\Delta_k\ne0$. Its entries are bounded there, so the cofactor
formula gives a uniform inverse bound. Its dependence on periods
at this boundary is only through $a$, while the actual analytic
remainders are uniformly bounded over all period vectors.
Hence one fixed $\eta$ and $\epsilon_0$ work for every vector;
there is no exchange with a countable intersection of unrelated
neighborhoods.

Both factors in
$$
K=T(a)^{-1}\Lambda_\epsilon M
$$
are boundedly invertible apart from the displayed row scales.
This proves the whole singular-value profile, not just its
determinant or smallest singular value.

The determinant calculation is now exact:
$$
\begin{aligned}
\det K(\epsilon,0)
&=\bigl(x_0\prod_p a_p\bigr)\epsilon^{k+1}
  \left(\Delta_k\Gamma/x_0+O_k(\epsilon)\right)\\
&=\Delta_k\left(\prod_p a_p\right)\Gamma(w)
  \epsilon^{k+1}+O_k(\epsilon^{k+2}).
\end{aligned}
$$
All multipliers of the remainder are bounded uniformly in the
periods. The asserted prefactor in (7) is therefore correct.
With the optional evaluation above, it is
$-\frac38(\prod_p a_p)\Gamma(w)$.

## 10. Boundaries, minimality and unresolved issues

The optimal-order statement is correctly tied to the inherited
universal obstruction at $u=0$ in this normalization. It does not
assert that every selection has this order at every coefficient
point. The observation-count minimum is a different, elementary
dimension statement: fewer than $k$ scalar observations cannot
have a rank-$k$ differential. The construction attains that count.

The output operations do not change parameter coordinates or add
observed traces. The normalizations by $n_p\rho_p$, and the later
row scalings by powers of $\epsilon$, must not be suppressed in a
conditioning interpretation. Raw trace and original-$c$ derivatives
have the additional factors already stated in V1.

Changing the selected cycles does not invalidate the frozen boundary
theorem for the old selection. The new full-rank finite selection
rules out a common kernel of all marked spectral observations on
this domain, but says nothing about a global unmarked quotient,
conjugacy reconstruction or full-spectrum behavior elsewhere.

No mathematical defect or missing lemma remains open in the actual
V1 theorem. Its claims survive unchanged.

## 11. Net additional proof volume

This is genuinely stronger than the prior selected-word result:
it uses exactly $k$ raw observations, permits their periods to vary
independently, and works on one fixed coefficient neighborhood.
The new proof load is the boundary-safe support choice, occupation
elimination, and the nonvanishing three-row certificate after
polarization. The Vandermonde check and closed evaluation of
$\Delta_k$ are short parts of that same argument.

Once the accepted parent second jet is cited, the net additional
proof naturally occupies approximately 3--5 substantive English
pages, including a precise statement and its scope guards.
The source's 438 Markdown lines, 2,147 whitespace-delimited words
including mathematical tokens, and 26 numbered displays are not a
compiled page count. Repeating the parent contractions, the whole
first-jet theory or the old boundary proof would not increase
the net new mathematical content.

This report does not decide the value or page fit of any eventual
combined manuscript and does not assign candidate PASS.

Final mathematical status: **PROVABLE AS STATED**.
