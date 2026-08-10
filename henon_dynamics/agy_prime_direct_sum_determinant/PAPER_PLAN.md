# Paper plan: sharp prime--Schatten thresholds

## One-sentence contribution

For the source-locked finite-Weil Rauzy--AGY transfer operators, the local
Schatten norms have the sharp size
\(\|\mathcal L_{s,p}\|_{S_q}\asymp p^{2/q}\), so a prime-weighted block
sum has an ordinary Fredholm determinant exactly beyond the prime harmonic
wall, while the two weight-free alternatives are either noncompact or have
the trivial normalized determinant germ.

## Frozen title and object

**Working title:** *Sharp Prime--Schatten Thresholds for Finite-Weil
Rauzy--AGY Transfer Operators*

The paper studies

\[
\mathcal L_{s,p}
=\sum_{\gamma\in\Gamma}K_{s,\gamma}\otimes\rho_p(g_\gamma)
\quad\text{on}\quad
\mathcal H_p=A^2(\Omega)\widehat\otimes\mathbb C^{p^2}
\]

and its prime-graded block sum

\[
\mathfrak L_{s,z}
=\bigoplus_{p\ \mathrm{odd}}p^{-z}\mathcal L_{s,p}.
\]

The object is called a **prime-graded Dirichlet--Fredholm family**.  It is
not called an adelic Weil representation: a direct sum of residue-field
fibres is not the restricted tensor product of local-field oscillator
representations.

## Claims--evidence matrix

| Claim | Status | Evidence or proof mechanism | Boundary |
|---|---|---|---|
| For fixed integral symplectic \(h\), \(p^{-2}\Theta_p(h)\to\mathbf1_{h=I}\) | theorem | rank stability modulo \(p\) and Thomas's character formula | pointwise in fixed \(h\); no uniformity over a growing word set |
| \(\|\mathcal L_{s,p}\|_{S_q}\asymp p^{2/q}\) for \(1\le q<\infty\), locally uniformly in \(s\) | theorem | C26 upper majorant; constant/evaluation compression, C25 injectivity, normalized trace, and Schatten duality for the lower bound | applies to the declared full finite-Weil fibre |
| \(\oplus_pc_p\mathcal L_{s,p}\in S_q\iff\sum_pp^2|c_p|^q<\infty\) | theorem | exact direct-sum Schatten norm and the local two-sided bound | block-diagonal scalar place weights only |
| \(\mathfrak L_{s,z}\in S_q\iff q\Re z>3\) | theorem | convergence criterion for the prime zeta series; \(\sum_p1/p\) at equality | ordinary determinant corresponds to \(q=1\) |
| \(\mathfrak D(s,z,u)=\prod_p\mathcal D_p(s,up^{-z})\) is an ordinary determinant for \(\Re z>3\) | theorem | locally uniform trace-norm convergence | the new variable \(z\) is external to the AGY roof |
| \(\exp[p^{-2}\operatorname{Log}_0\mathcal D_p]\to1\) for the normalized positive-AGY germ | theorem | C25 free positive monoid, C27 absolute word traces, dominated convergence | branch fixed at \(u=0\) on a common compact-uniform disc only; large-\(p\) limit, not a prime product |
| Dimension-normalized MARKED assembly can fail at a rational fixed plane | exact control | C24-P073 has \(\dim\ker(g-I)=2\) and \(\Theta_p(g)=p\) for every odd \(p\) | P073 is a C24 full-Rauzy control, not a C26 induced branch |
| Arithmetic coefficients are orbit-dependent quadratic prime series | theorem plus finite evidence | good-prime Legendre law and finite bad-prime correction; C27 conductor census | no common character, automorphic representation, or functional equation |

## Paper architecture

1. **Introduction.** State the sharp threshold, the honest determinant, and
   the canonicality trilemma on the first page.
2. **Source-locked setting and related constructions.** Freeze the AGY
   branch grammar, chronology, analytic hypotheses, and finite-Weil
   normalization; distinguish residue-field direct sums from adelic Weil
   representations.
3. **Normalized finite-Weil character limit.** Prove the rank-stability
   lemma and convergence to the regular character.
4. **Sharp local Schatten theorem.** Give the complete compression proof,
   including compact-set uniformity and the C25 injectivity input.
5. **Prime-graded determinant and exact phase diagram.** Prove the general
   weighted `iff`, the \(q\Re z>3\) wall, joint holomorphy, product formula,
   and chronological trace expansion.
6. **Normalized-trace collapse.** Prove vanishing of all positive moments
   and convergence of the normalized determinant germ to one.
7. **Arithmetic structure and fixed-plane control.** Derive quadratic prime
   series and present P073 with its strict C24 scope.
8. **Interpretation and limitations.** Explain the external prime clock,
   absence of an adelic/automorphic or Hilbert--Pólya conclusion, and the
   path-groupoid or genuine local-field pivots.
9. **Appendices.** Source-lock proof details, regularized determinant
   hierarchy, P073 exact minor computation, and reproducibility statement.

## Proof-order requirements

- State all analytic hypotheses before the sharp theorem.
- Use \(1\le q<\infty\) for Schatten membership and treat compactness
  separately; do not hide the \(q=\infty\) convention.
- In the lower bound, first prove the normalized compressed trace converges
  locally uniformly in \(s\).  Only then apply Schatten duality.
- Quote C25 exactly: the full labeled fixed-start Rauzy matrix decodes the
  edge word, and concatenations of first-return words form a free monoid.
- Repetitions use \(\Theta_p(g_w^r)\), never \(\Theta_p(g_w)^r\).
- Keep operator scaling \(p^{-2}\mathcal L_{s,p}\) distinct from normalized
  trace \(p^{-2}\operatorname{Tr}\).

## Required scope language

- `proved`: sharp Schatten bounds, direct-sum threshold, ordinary determinant
  on \(\Re z>3\), regular-character limit, normalized positive-monoid
  collapse, and P073's all-odd-prime character formula.
- `exact finite certificate`: the 146-cycle C24 census and the frozen source
  hashes.
- `finite evidence`: C27's bounded conductor fragmentation census.
- `open`: exclusion of fixed planes from the full C26 induced language,
  continuation toward \(z=0\), and any nontrivial based/groupoid trace.

## Intended conclusion

C28 supplies a rigorous global analytic object, but only after adding the
prime norm as a second grading.  Within the declared direct-sum and
normalized-trace constructions there is no nontrivial, undamped, one-clock
ordinary determinant.  The next structural move must add genuine inverse
holonomy through a based path groupoid or replace residue-field fibres by a
true local-field/automorphic architecture.
