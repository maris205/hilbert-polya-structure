# Independent audit of the logarithmic Dirichlet–Gram transfer

2026-09-06. Non-author review of `spectral/PROOF_DRAFT.md`, Sections 2–5,
and its `SCOUT_REPORT.md`. No author file was edited. This is not a formal
Route-A evaluation or an admission decision. The research-review and
proof-writer criteria are applied to a mathematical proof, with the current
independent team replacing unavailable older review-MCP defaults.

## 1. Outcome and boundaries

**No mathematical counterexample or substantive proof gap was found in
Sections 2–5, conditional on the explicitly stated input W.** The dyadic
approximation has the needed exponential-scale strength. The Laguerre
normalization is correct. The Loewner and threshold inequalities have the
correct direction, including the signed remainder.

The exact classical eigenvalue coefficient W remains an external source
gate; this review does not resolve the reported source discrepancy or claim
to have inspected Widom's original theorem. Section 6's arithmetic
L-function justification was outside the requested proof audit. The proof
in Sections 2–5 only needs the analytic germ assumed in Section 1.

On substance: this is **not merely positivity followed by a formal invocation
of W**. The explicit analytic-remainder lemma supplies a real missing step at
the square-root exponential scale. Conditional on its transfer statement not
already having a primary owner, it can support **one coherent, modest
source-spectral theorem**. The prime and residue-class examples, determinant
asymptotic and density-independence observation are consequences of that
theorem, not additional independent contributions. I would not reject the
draft as a bare restatement of W; I would still hold admission at the exact
ownership/source gate. A mathematically complete short proof is not itself
evidence of novelty.

## 2. Gram factorization and global analytic estimates

Write `q_j=w_j a_j^(-rho)` and `ell_j=log(a_j)>0` in this section only.
Then the columns of B are `sqrt(q_j) exp(-ell_j t)`, and

\[
\sum_j\|b_j\|_2^2
=\sum_j\frac{q_j}{2\ell_j}
=\int_0^\infty D(\rho+2t)\,dt.
\]

Tonelli applies because all summands are nonnegative. The local germ gives
an integrable logarithmic divergence at zero. If `t>=eta`,

\[
D(\rho+2t)
\le D(\rho+\eta)a_*^{-(2t-\eta)},
\]

so the tail is integrable. Thus B is Hilbert–Schmidt and `G=B*B` is positive
trace class. Integration of a pair of columns gives exactly the denominator
`log(a_i a_j)`, with no missing factor two.

The Dirichlet series is holomorphic in `Re(s)>rho`: positivity and real
convergence give absolute, locally uniform convergence in every smaller
right half-plane. For `Re(u)>=eta`,

\[
|D(\rho+u)|
\le D(\rho+\eta)a_*^{-(\Re u-\eta)}.
\]

Similarly `|E(u)|<=E(eta) exp(-(Re(u)-eta))`. Choosing one fixed
`0<d<=min(log(a_*),1)` yields the asserted half-plane estimate for R, with
constants depending on eta. The removable local germ stitches to the
right-half-plane definition. These estimates are global enough for the
later Taylor circles; no prime number theorem or unproved vertical-strip
bound is being inserted.

The model is itself positive trace class:

\[
E(t+s)=\int_1^\infty e^{-x t}e^{-x s}\,\frac{dx}{x},
\qquad
\operatorname{Tr}H_E=\int_0^\infty E(2t)\,dt=\frac12.
\]

Thus the continuous kernel identity `BB*=c H_E+H_R` is valid between bounded
operators. The actual remainder R is real on the positive axis, so `H_R` is
self-adjoint. The standalone analytic lemma need not impose reality because
it concerns singular values; reality is available at the transfer step.

## 3. The dyadic Taylor lemma survives a uniform-constant check

Let `0<h<r/5`. For the first interval `[0,h]`, the Taylor circle has center
`y+h/2` and radius h. If `0<=y<=2h`, it lies in `|u|<=7h/2<r`.
If `y>2h`, it lies in `Re(u)>=y-h/2>=3h/2`. The first set is compact;
the second uses one fixed half-plane bound. Enlarging a constant therefore
gives a uniform circle bound `C exp(-d' y)`.

For `[v,2v]`, `v>=h`, the circle centered at `y+3v/2` with radius v has
`Re(u)>=y+v/2>=h/2`. The same `C_(h/2)` works for every dyadic interval,
giving `C exp(-d(y+v/2))`. This uniformity is important and does hold.

On both interval types, the real Taylor ratio is at most one half. Cauchy's
estimate and a geometric-series sum give an error bounded by a constant
times `2^(-m)` times the displayed circle bound. The coefficient functions
are in `L²(dy)` because of their exponential y-decay. Each truncated
interval kernel has rank at most m; discontinuous interval cutoffs in x do
not affect that rank statement or square integrability.

For the first `K+1` intervals, the squared error estimate is

\[
\|\text{Taylor error}\|_{\mathrm{HS}}^2
\le C4^{-m}
\left(1+\sum_{k\ge1}2^{k-1}h e^{-d2^{k-1}h}\right)
\le C'4^{-m}.
\]

The tail `x>T=2^K h` has squared Hilbert–Schmidt norm bounded by
`C exp(-2dT)`. Consequently the total operator-norm error is at most

\[
C_1 2^{-m}+C_2e^{-d2^K h}.
\]

Choose, for sufficiently large L,

\[
m=\left\lceil\frac{L+C_3}{\log2}\right\rceil,
\qquad
K=\left\lceil\log_2\frac{L+C_4}{dh}\right\rceil,
\]

with fixed constants making both terms smaller than `exp(-L)/2`.
Then `m=O(L)`, `K=O(log L)` and the approximant rank is
`O(L log L)`. By approximation numbers/minimax,

\[
N_s(e^{-L};H_R)=O(L\log L)=o(L^2).
\]

The original proof's notation “`2^K h=O(L)` large enough” is correct, but
the explicit choice above would remove a possible stylistic ambiguity.
It is not a mathematical repair.

The author's warning about all-Schatten estimates is justified. For example,
a diagonal compact operator with singular values
`s_n=exp(-(log(n+1))²)` belongs to every `S_p`, `p>0`, whereas
`N_s(exp(-L))` grows on the scale `exp(sqrt(L))`, much faster than `L²`.
Thus replacing the proved lemma by an all-Schatten assertion would break the
transfer argument. This is a control example, not a counterexample to the
actual lemma.

## 4. Laguerre normalization and model comparison

With the draft's basis

\[
\ell_j(t)=\sqrt2e^{-t}L_j(2t),
\]

the Laplace transform is
`sqrt(2)(x-1)^j/(x+1)^(j+1)`. Hence, for `n=j+k`, the model matrix entry is

\[
\int_1^\infty
\frac{2}{x(x+1)^2}
\left(\frac{x-1}{x+1}\right)^n dx.
\]

For `v=(x-1)/(x+1)`, one has
`x=(1+v)/(1-v)` and `dx=2dv/(1-v)²`. The measure factor becomes

\[
\frac{2}{x(x+1)^2}dx=\frac{1-v}{1+v}\,dv.
\]

Therefore the stated weight `theta=(1-v)/(1+v)` is exact. An independent
normalization check is

\[
\sum_{j\ge0}J_\theta(j,j)
=\int_0^1\frac{\theta(v)}{1-v^2}\,dv
=\int_0^1\frac{dv}{(1+v)^2}=\frac12,
\]

matching the trace of `H_E` computed above.

For `ell(v)=-log v`, positivity of moment forms gives

\[
c_\delta J_{\mathrm{high}}\le J_\theta\le J_\ell,
\qquad
J_{\mathrm{high}}=J_\ell-J_{\mathrm{low}}\ge0.
\]

Indeed `-log v>=1-v>=theta(v)`, and the ratio `theta/ell` extends
continuously to `v=1` with value one half and has a positive minimum on
`[delta,1]`. The entries of `J_ell` are exactly `(j+k+1)^(-2)`.

If `P_m` is the first-m-coordinate projection, the approximant
`P_m J_low+J_low P_m-P_m J_low P_m` has rank at most `2m`; the residual
is the block with both indices at least m. The draft's entry bound gives
its Hilbert–Schmidt norm `O(delta^m)`. Thus `N_s(e^(-L);J_low)=O(L)`.

The fully explicit lower bound is

\[
N(t;J_\theta)
\ge N(t/c_\delta;J_{\mathrm{high}})
\ge N(2t/c_\delta;J_\ell)-N(t/c_\delta;J_{\mathrm{low}}).
\]

Together with `N(t;J_theta)<=N(t;J_ell)` and W, this proves the stated
model asymptotic. All threshold factors are fixed, so they shift L by a
constant rather than altering the quadratic leading term.

## 5. Signed perturbation and determinant

For compact self-adjoint A and E, intersect the subspaces where the
quadratic forms of A and `|E|` are at most t. On that intersection the
quadratic form of `A+E` is at most `2t`. This proves

\[
N_+(2t;A+E)\le N_+(t;A)+N_s(t;E).
\]

Applying the same fact to `A=(A+E)+(-E)` proves the reverse comparison
used in the draft. Positivity of E is not needed. Here `A=cH_E`,
`E=H_R`, and `A+E=BB*>=0`, so the two model comparisons and the
`o(L²)` error give the claimed positive-eigenvalue count. Monotone
inversion gives the square-root logarithmic eigenvalue law, including
multiplicities and with zero eigenvalues omitted as stipulated.

Set `M(t)=#{n:-log(lambda_n)<=t}`; changing `<` to `<=` affects neither
integral. The exact logistic identity and Tonelli give

\[
\log\det(I+e^LG)
=\int_{x_{\min}}^\infty\frac{M(t)}{1+e^{t-L}}\,dt.
\]

With `M(t)~a t²`, the unweighted integral from zero to L is
`aL³/3+o(L³)`. Both logistic corrections are `O(L²+1)` because
`M(t)=O(1+t²)` for nonnegative t. The fixed negative-t interval has
bounded length and bounded M, hence contributes `O(1)`. This justifies
the cubic coefficient `1/(6pi²)` and does not accidentally suppress the
contribution of finitely many large eigenvalues; their linear-in-L part
is already included in the integral over `[0,L]`.

## 6. Contribution audit: what is and is not new

The logical contribution inventory is:

1. **Classical/elementary input:** positive Gram factorization, trace class,
   nonzero-spectrum equivalence and basic minimax inequalities.
2. **Classical external input:** W for the square-Hankel matrix. Neither its
   coefficient nor its proof can be attributed to the draft.
3. **Candidate increment:** a uniform, explicitly proved
   `N_s(exp(-L);H_R)=O(L log L)` analytic localization statement, used to
   transfer the classical model law to discrete frequency/weight systems
   specified only by a holomorphic logarithmic Dirichlet germ.
4. **Consequences, not independent new theorems:** the Fredholm cubic law,
   prime/reduced-residue-class cases once their local germs are justified,
   and disappearance of c from the leading coefficient.

The argument addresses a whole quantified class, not just a table of
examples, and the remainder proof is stronger than the power-scale shortcut
that would otherwise leave a genuine gap. This is why I do not characterize
it as *only* a short formal corollary of W. Its technique is nevertheless
elementary analytic low-rank approximation; older general analytic-Hankel
or rational-approximation results could already imply exactly the required
transfer. That is the strongest ownership risk.

The class is not uniquely arithmetic. For example,

\[
a_j=e^j,\qquad w_j=e^{\rho j}/j
\]

gives `D(rho+u)=-log(1-exp(-u))=-log u+A(u)` near zero and

\[
G_{ij}=\frac1{\sqrt{ij}(i+j)}.
\]

It obeys the same conclusion. Scaling all weights also merely scales G,
which by itself explains why that amplitude is invisible at the leading
inverse-log scale. These controls support the stated source-universality
interpretation and rule out any added prime-specific spectral rigidity claim.
They do not invalidate the transfer theorem or its arithmetic applications.

## 7. Source scope and remaining admission gates

In addition to the two local drafts, this bounded review checked primary
abstract/metadata records for the multiplicative Hilbert matrix and for
Pushnitski–Yafaev's localization paper. The latter explicitly concerns the
**power scale** in its abstract. That does not establish the draft's
square-root exponential-scale transfer as an automatic consequence, but
neither does reading an abstract rule out a stronger relevant theorem.
[Pushnitski–Yafaev, arXiv 1508.04279v2](https://arxiv.org/abs/1508.04279).
Its DOI full-page fetch failed with HTTP 403; no complete proof read is
claimed. A few exact-phrase searches did not reveal an exact prime/germ
transfer owner; that limited negative result is not a novelty certificate.

Before admission, retain these distinct gates:

- Verify W with its exact coefficient and hypotheses against an adequate
  primary statement, resolving rather than suppressing the known discrepancy.
- Check existing exponential-scale analytic-Hankel localization and rational
  approximation results for the exact germ-to-Gram transfer. A match there
  would reduce the main contribution to an application.
- Audit the arithmetic germs separately; do not replace holomorphic local
  continuation by a density asymptotic.
- Keep all applications and the determinant inside this one contract. No
  target Euler factor, root number, target-zero operator or prime-orbit
  construction follows from this proof.

Only optional presentation additions are suggested: display the explicit
choice of m and K, the model trace `1/2`, and the reason the actual signed
remainder is self-adjoint. None is required to rescue a false step.
