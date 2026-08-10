# HCS-C26 research question

## Primary question

For the exact countable AGY return family frozen in HCS-C25, can replacing
the real `C_b^1` or normalized `L^2` base by a point-evaluative holomorphic
function space make the **unsmoothed infinite-dimensional oscillator twist**
compact or determinant class?

The candidate operator is

\[
(\mathcal L_sF)(x)
=\sum_{\gamma\in\Gamma}
  w_{s,\gamma}(x)U_\gamma F(h_\gamma x),
\qquad
w_{s,\gamma}=e^{-sr_\gamma}j_\gamma,
\]

where the inverse branches, chronological symplectic matrices, and coherent
metaplectic lifts are exactly those of HCS-C25.  No transition-matrix average
or Hermite cutoff is permitted.

## Falsifiable target

Prove or refute the following statement.

> If a Banach space `X` of `L^2(R^2)`-valued functions contains bounded
> constant functions, has bounded evaluation at one real interior point,
> and realizes the displayed transfer formula pointwise as a bounded
> operator, then `L_s` is noncompact throughout the AGY source half-plane
> `Re(s)>-sigma_0`.

The statement is deliberately conditional only on the function-space
operations needed to form an exact slice.  It does not assume a
branch-supported holomorphic localizer.

## Stronger optional question

Can one also prove, on one common complex neighborhood of the AGY section,
that the **scalar** countable transfer operator is nuclear or trace class?
If so, HCS-C26 would yield a sharp same-domain dichotomy:

\[
\text{scalar holomorphic determinant exists},
\qquad
\text{literal infinite oscillator determinant does not}.
\]

This stronger half is accepted only if a uniform complex domain, a common
logarithm branch, compact containment of every inverse branch, and
countable nuclear-norm summability are all proved.  Real Hilbert-metric
contraction alone is not treated as a proof of those complex statements.

## Scope

- **In scope:** point-evaluative vector-valued holomorphic spaces; exact
  evaluation and fibre slices; the full countable branch family; explicit
  lower bounds from the certified length-128 branch; scalar nuclearity only
  if all complex-domain gates close.
- **Out of scope:** arbitrary distribution spaces with no bounded slice,
  informal Weil characters as ordinary traces, ad hoc heat factors,
  chronological averaging, and claims about Riemann-zero agreement.
- **Decision rule:** if the point-evaluation obstruction is proved, close
  the holomorphic/no-localizer escape for the literal oscillator model and
  move to a genuinely different fibre, preferably a finite Weil
  representation over `F_q`.

## FINER assessment

| Criterion | Score (1--5) | Reason |
|---|---:|---|
| Feasible | 5 | C24 supplies the atomic essential-norm theorem and C25 supplies the exact AGY coefficients and injectivity. |
| Interesting | 5 | This is the precise operator-space escape left open by C25. |
| Novel in this program | 4 | The atomic theorem is not new, but its no-localizer evaluation application to the source-locked AGY family is. |
| Ethical / reproducible | 5 | The proof uses public sources and exact, independently replayed integer/rational data. |
| Relevant | 5 | It decides whether ordinary holomorphic nuclearization can rescue the proposed Hilbert--Pólya transfer operator. |

Mean score: **4.8 / 5**.
