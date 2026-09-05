# Internal mathematical review of the harmonic delta-comb admission proof

Date: 2026-09-05. Reviewer: current-team agent build_c382, independently
checking the proof authored by build_c383. This is not external, human,
blind or journal peer review. The reviewer knew the scout contract, then
read the actual entire 13-step author proof, not only its summary.

Reviewed file:
[delta-comb PROOF_PACKAGE.md](../delta_comb/PROOF_PACKAGE.md).
SHA256 at review:
7a63727caee39ba2926e2fe93dd249df17ea9ec4ba5ddf7b760432f02898b0af.
No file in the delta-comb author's directory was changed by this reviewer.

## Verdict

No blocking mathematical issue found in the stated fixed-positive-finite
coupling contract. The common domain, uniform exponential comparator,
min--max error transfer, heat/zeta constants, Schatten threshold and
inclusive endpoint counting all survive the checks below.

This is mathematical admission support only. It does not establish
publication novelty, validate the subsequently prepared numerical script,
or release a paper. In particular the proposed finite-coupling asymptotic
still needs its bounded ownership audit and coordinator adjudication.

## 1. Common form domain and closedness

The estimate on each cell is valid for the absolutely continuous Sobolev
representative. Integrating the fundamental-theorem bound for $|f|^2$
gives exactly the author's factor $2$, with no inverse-cell-length loss
after $(y-x_{n-1})/\ell_n\le1$. Summing only finitely many cells before
taking limits avoids subtraction of infinities. The two nonnegative
partial expressions differ by a uniform finite bound; consequently one
is finite if and only if the other is finite.

The harmonic inequalities have the correct direction:
$h_n-\log n$ decreases to $\gamma$, whereas
$h_n-\log(n+1)$ increases to it. They imply the global bound
$|n-\exp(x/\pi-\gamma)|\le1$ on the $n$th cell, including the separately
treated first cell. Thus the coefficient
$C=\kappa e^{-\gamma}/\pi$ and the additive error $\kappa/\pi$ are correct.

For fixed $\kappa>0$, Young's inequality yields
$$
Q_{1-\varepsilon,C}-d_\varepsilon\|\cdot\|^2
\le q_\kappa
\le Q_{1+\varepsilon,C}+d_\varepsilon\|\cdot\|^2,\qquad
d_\varepsilon=\kappa^2/\varepsilon+\kappa/\pi.
$$
At a fixed $\varepsilon=1/2$ these are genuine two-sided form-norm
comparisons. They prove closedness on the claimed weighted Sobolev domain,
not merely a bound on a preliminary test space.

The form-core argument is sufficient: cutoff convergence follows from the
tails of both $|f'|^2$ and $e^{x/\pi}|f|^2$, and smoothing is only performed
on a fixed finite interval where the weight is bounded. The delta jump
condition has the correct positive sign. Integration by parts contributes
$f'(x_n-)-f'(x_n+)$, which cancels $+\kappa f(x_n)$ in the form.
The form-core extension eliminates an unproved boundary term at infinity.

Compactness follows from local Rellich plus a uniform exponential tail.
The zero-kernel argument then gives a strictly positive ground energy.
The first-cell initial derivative and the subsequent jump propagation
prove simplicity for every finite coupling. No simplicity is incorrectly
assigned to the decoupled limit.

## 2. Uniform comparator: the essential moving-parameter gate

The exact scaling is consistent:
$$
x=2\pi y,\qquad
A_{a,C}=\frac a{4\pi^2}
\left(-\frac{d^2}{dy^2}+b^2e^{2y}\right),\qquad
b=2\pi\sqrt{C/a},\quad K=\frac{2\pi r}{\sqrt a}.
$$
For fixed $C>0$, allowing $a\in[1/2,3/2]$ places $b$ in one fixed
positive compact interval. In particular
$2K/b=2r/\sqrt C$, without a remaining $a$ in the logarithm.

I checked the cited special-function identities against the actual NIST
pages: [the Bessel series and decay definition](https://dlmf.nist.gov/10.25),
[the connection formula](https://dlmf.nist.gov/10.27.E4), and
[Gamma/digamma asymptotics](https://dlmf.nist.gov/5.11).
At imaginary order the connection formula indeed gives
$K_{iK}(b)=\pi\,\operatorname{Im}I_{-iK}(b)/\sinh(\pi K)$ with the
positive sign used by the author.

For the rising product in the $j$th Bessel-series term, every factor has
modulus at least $K$. Differentiation introduces at most $j/K$. Therefore
the stated estimates
$$
|S_b-1|\le e^{d_+/K}-1,\qquad
|S_b'|\le d_+K^{-2}e^{d_+/K}
$$
hold uniformly in the compact $b$ interval. The logarithm remains on a
single disk around $1$ after choosing one common $K_0$.

The Gamma branch on the right half-plane is applicable at $1+iK$.
Its phase derivative is $\operatorname{Re}\psi(1+iK)$, and the phase has
the stated positive large-$K$ derivative. Thus one root occurs at each
integer phase crossing above a common $K_0$. Below $K_0$, comparison with
the smallest $b$ bounds the number of roots uniformly; this closes a
potential hidden parameter-dependent integer-offset gap.

These steps prove a uniform $O_C(1)$ comparator count. They do not merely
assume that a fixed-parameter Bessel asymptotic is uniform. This is the
key reason the next step may use $a=1\pm1/k$.

## 3. Min--max direction and error size

The counting inequalities have the correct order:
$$
N_{A_{1+1/k,C}}(k^2-d_k)
\le N_\kappa(k^2)
\le N_{A_{1-1/k,C}}(k^2+d_k),\qquad
d_k=\kappa^2k+\kappa/\pi.
$$
For example $q_\kappa\le Q_{1+1/k,C}+d_k$ means that each comparator
eigenvalue at most $k^2-d_k$ forces a comb eigenvalue at most $k^2$;
this checks the potentially confusing left inequality directly.

The shifted frequency is $k+O_\kappa(1)$. For the comparator leading
function, differentiating gives
$$
\partial_r F=\frac2{\sqrt a}\log(2r/\sqrt C),\qquad
\partial_a F=-\frac r{a^{3/2}}[\log(2r/\sqrt C)-1].
$$
Thus the frequency displacement and the $1/k$ coefficient displacement
each cost $O_\kappa(\log k)$, not $O(1)$ and not $O(k)$.
Substitution of $C$ gives the claimed linear coefficient
$\log(4\pi/\kappa)+\gamma-2$.

The estimates are valid for all sufficiently large real $k$. Inclusive
thresholds are covered because the comparator phase floor only changes
the bounded counting error by one. No constant uniform in $\kappa$ has
been inferred.

## 4. Heat, spectral zeta and Schatten conclusions

Writing the count in the energy variable gives
$N(E)=\sqrt E\log E+C_\kappa\sqrt E+O_\kappa(\log(E+2))$.
Its heat transform is
$$
t^{-1/2}\Gamma(3/2)
[\log(1/t)+\psi(3/2)+C_\kappa].
$$
Using $\psi(3/2)=2-\gamma-2\log2$ gives
$\psi(3/2)+C_\kappa=\log(\pi/\kappa)$ exactly.
The remainder contributes $O_\kappa(\log(1/t))$ after $u=tE$;
the low-energy extension of the remainder is integrable.

For the zeta transform the rational contribution is
$$
\frac{s}{(s-1/2)^2}+\frac{sC_\kappa}{s-1/2}.
$$
Its principal part is
$\tfrac12(s-1/2)^{-2}+(1+C_\kappa/2)(s-1/2)^{-1}$.
The remainder integral and its differentiated integrands are uniformly
integrable on compact subsets of $\operatorname{Re}s>0$; the low-energy
term is entire because the ground energy is positive. The proof
correctly stops before $s=0$.

The positive Stieltjes integral at real $p$ yields the sharp
$p>1/2$ Schatten condition; at $p=1/2$ the integrand is proportional to
$(\log E)/E$ and diverges. The ordinary determinant follows from inverse
trace class. The Bessel function has not been substituted for the comb's
actual Fredholm determinant.

As a small independent algebra check, I differentiated the leading
comparator function and expanded the heat/zeta constants with SymPy.
The heat-constant difference was exactly zero and the zeta expansion gave
the two coefficients above. This supplements, rather than proves, the
analytic argument. No numerical spectrum lane was rerun.

## 5. Infinite coupling, norm resolvent and threshold direction

The limiting form domain is dense: finite sums of smooth functions
inside separate cells are dense in the direct-sum $L^2$ space.
Vanishing vertex values also imply membership in the finite-coupling
domain by the already proved sampling bound. The increasing closed-form
theorem therefore has the hypotheses the author needs.

The norm upgrade is valid. For
$0\le T_\kappa=R_\kappa-R_\infty\le R_{\kappa_0}$, the compact positive
upper operator supplies a finite-rank spectral projection with small tail.
Positivity bounds off-diagonal blocks by the geometric mean of the two
diagonal block bounds; strong convergence on the finite-dimensional head
then proves norm convergence. This is stronger than a bare appeal to
strong resolvent convergence and does rule out spectral leakage here.

Ordered endpoint eigenvalues increase from below. At a fixed inclusive
energy $E$, all endpoint modes $j\le N_\infty(E)$ are already counted for
every finite coupling; the next endpoint eigenvalue is strictly above $E$
and eventually excludes all subsequent modes. This proves eventual
equality even at square thresholds. The author correctly does not make
the corresponding claim for strict counting at a threshold.

The pair count for endpoint eigenvalues $m^2n^2$, the hyperbola
decomposition for real $k$, and the two unequal iterated limits are all
consistent. No uniform coupling threshold as $E\to\infty$ is supplied or
needed.

## Remaining boundaries and minor presentation note

No required repair was identified. One optional precision sentence would
be that continuous-parameter $\kappa\to\infty$ follows from the monotone
form theorem along an integer sequence and order squeezing in between;
the current monotone-family use is mathematically sufficient.

The finite-coupling remainder is $O_\kappa(\log k)$, so the old C398
bounded-remainder target obstruction cannot be imported. The endpoint
divisor zeta does not establish a finite-coupling arithmetic orbit owner.
The text maintains those boundaries.

This review does not check all subsequent source-audit claims, a future
sanity script, PDFs, release ledgers or target arithmetic controls.
No statement here is a certificate of literature novelty.
