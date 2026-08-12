# R300-P1 Independent Proof Review

**Reviewed:** 2026-08-06  
**Target:** `R300_P1_UNIFORM_REMAINDER_PROOF.md`  
**Final verdict:** `ACCEPT`  
**External Codex MCP:** unavailable; two independent subagent proof audits were
used as the documented fallback, with no fabricated numerical review score.

## Theorem reviewed

For fixed \(a>-1\) and \(h>0\), with

\[
L=\log\frac1{2\pi t},
\]

the proof asserts

\[
\Theta_a(t)-\Theta_0(t)
=-\frac{t^2}{48\pi}\bigl(I_a(t)-I_0(t)\bigr)
+O_{a,h}(tL^4).
\]

Together with the exact carrier identity, this gives

\[
\Theta_a(t)-\Theta_0(t)
=-\frac{a^2}{24\pi}
\left[L^2+\bigl(2(1-\gamma)+4\pi r_a^2\bigr)L+\kappa_a\right]
+O_{a,h}(tL^4).
\]

## Audit A: deterministic geometry and power count

Verdict: `ACCEPT WITH MINOR CLARIFICATIONS`.

The reviewer independently verified:

- the exact displaced Hénon coordinate;
- normalized derivative bounds through fourth order;
- weighted derivative-product integrals without an extra factor of \(L\);
- the main-region \(O(L^4)\) fourth-derivative integral;
- the moving cutoff \(\sigma_*=L+8\log L\);
- the incomplete-Gamma tail;
- Brownian covariance factors \(1/12\) and \(1/6\);
- the sign and coefficient \(-t^2/(48\pi)\);
- the Gamma moments and final coefficient \(-a^2/(24\pi)\).

Requested clarifications were implemented: \(\delta\) is frozen before
constants are named; the tail uses

\[
\alpha_L=C_a(\delta/L+\delta^2/L^2),
\qquad
p_L=\frac{1+\alpha_L}{1-\alpha_L},
\]

and includes the Jacobian \((1-\alpha_L)^{-1}\).

## Audit B: adversarial Brownian proof review

Initial verdict: `REVISE`, not `REJECT`.

The reviewer found one local rigor gap: the original draft estimated the
bad-event second derivative at \(\theta=0\) but had not explicitly justified
passing two derivatives through the bad-event expectation.  The proof was
repaired by showing, for fixed \(z,t,\theta_0\),

\[
\sup_{|\theta|\le\theta_0}|f_a''(\theta,z,B)|
\le C_{a,z,\theta_0}(1+M)^{10}.
\]

The bridge maximum \(M\) has Gaussian tails, so this is an integrable
neighborhood dominator.  The revised equations (25a)--(25b) establish the
required dominated differentiation.  The reviewer re-opened the repaired
file and returned the final verdict `ACCEPT`.

The same audit independently confirmed the direction of pathwise Jensen,
the avoidance of a small-probability-times-infinite-volume error, the fourth
derivative formula, all \(h,t,\pi\) factors, and the cutoff integration by
parts.

## Claim boundary

The accepted theorem proves a nonzero analytic relative spectral invariant
for one fixed Hénon warp.  It does not prove a rational-prime trace law,
identify individual zeta zeros, prove positive-measure classical chaos, or
select \(a=1.02\) as arithmetically unique.

