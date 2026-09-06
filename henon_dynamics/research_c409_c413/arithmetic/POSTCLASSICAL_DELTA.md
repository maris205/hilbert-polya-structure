# Classical deduction and the remaining wild theorem

2026-09-06. This file corrects an initially too-broad novelty emphasis
after the bounded search located Baril Boudreau–Holmes–Nguyen (BHN),
*Adelic perturbation of rational functions and applications*,
[arXiv:2307.07910v1](https://arxiv.org/pdf/2307.07910v1), 16 July 2023,
published as *Mathematische Annalen* 392 (2025), 2253–2275,
[DOI 10.1007/s00208-025-03155-0](https://doi.org/10.1007/s00208-025-03155-0).
The theorem locators below refer to the original preprint actually read.
The publisher's metadata and abstract were verified; its full final text
was not obtained. That version limitation is retained, not concealed.

## 1. The no-wild FAD conclusion is already a classical deduction

Consider a genuine positive-entropy FAD system with every $t_{p,n}=0$.
Write
$$
f_n=A_n g(n),\qquad
A_n=|\det(A^n-I)|c^n,\qquad
g(n)=r_n\prod_{p\in S}p^{-s_{p,n}v_p(n)}.
$$
The following is a deduction from existing theorems, not an additional
result of the candidate.

1. BCH Proposition 10.2.1 gives $c\in\mathbb Z_{>0}$ and rational
   $r_n,p^{s_{p,n}}$ in this no-wild case. Hence $g(n)\in\mathbb Q$.
   Periodicity and $v_p(n)=O(\log n)$ give $h(g(n))=O(\log n)$.
2. Let $W$ be a common period and put
   $d_k=W\prod_{p\in S}p^k$. On every residue class modulo $d_k$
   avoiding zero modulo $p^k$ for each $p\in S$, all valuations and
   periodic data are fixed; therefore $g$ is constant on that class.
   The proportion of excluded classes is at most
   $\sum_{p\in S}p^{-k}\to0$.
3. These facts are precisely BHN Definition 2.11(P1)–(P3), with constant
   constituent polynomials. The finitely many initial indices and the
   value at zero do not affect the definition or a natural boundary.
4. The generating function of $A_n$ is rational. Its normalized
   dominant factor is strictly positive at every positive integer, by
   BCH Lemma 10.3.10(ii), or by pairing the unit-circle roots as
   $\prod_j(2-\eta_j^n-\eta_j^{-n})$. It is therefore stable in BHN's
   sense: its dominant part vanishes identically on no progression.
5. BHN Theorem 2.14 applies. If any $s_{p,n}$ is active, BCH
   Proposition 11.3.3 excludes a rational fixed-count generating
   function. Thus its entropy circle is a natural boundary; the usual
   logarithmic-derivative argument transfers this to the dynamical
   zeta function.

Consequently **removing hyperbolicity only in the no-wild FAD case
cannot be admitted as a new theorem here**. In particular, the already
settled abelian-variety question in BHN Theorem 1.2 and finite-place
solenoid question in BHN Theorem 4.6/Remark 4.7 are classical scope.

## 2. The new proof genuinely crosses the height obstruction

In `REALIZED_EXAMPLE.md`, the normalized distortion is
$$
g(n)=p^{-p^{v_p(n)}}.
$$
For $n=p^a$, its absolute logarithmic Weil height is exactly
$$
h(g(p^a))=p^a\log p=n\log p.
$$
Thus BHN Definition 2.11(P2), $h(g(n))=o(n)$, fails. Local constancy on
a density tending to one of congruence classes still holds, but it does
not supply the missing height condition. Moving the factor $p^n$ into
the perturbation instead gives height $(n-1)\log p$ at integers
coprime to $p$, and likewise does not make this a direct application.

The candidate supplies an unconditional analytic argument for these
coefficients, including finitely many primes, periodic wild exponents,
and multiple archimedean dominant phases. Its mechanism is not a new
single-phase Pólya–Carlson criterion. It is the exact active-fibre
condition, construction of a finite atomic coefficient measure after
torsion aggregation, and a conductor-grid proof that its nonzero atoms
are dense.

The same proof admits arbitrary complex phase coefficients and
nonnegative real exponents without any algebraicity or Weil-height
assumption. This broader analytic scope should support the genuinely
wild theorem, not be used to hide that the no-wild dynamical conclusion
is already known.

## 3. What is and is not claimed after deduction

Permitted author-side candidate delta:

- an exact rationality/natural-boundary classification for the stated
  complex finite-phase, finite-adelic radial coefficients;
- its phase-safe dense-atom proof, with a rational cancellation control;
- the nonhyperbolic wild FAD conclusion and an actual Salem-torus ×
  additive-system example, not covered by the inspected BHN hypotheses.

Not a new claim:

- BC2018 Question 5.6 or BMW2014's finite-place conjecture, both already
  addressed by BHN;
- no-wild FAD natural boundaries, by the deduction above;
- the existence of single-prime wild natural boundaries;
- elementary Fourier expansions, Haar orthogonality, or extraction of
  atomic masses from radial limits;
- any new fixed-point formula for the factors of the example;
- a Riemann-zeta or Hilbert–Pólya conclusion.

An independent reviewer must still decide whether the remaining
theorem package clears the project's substance and ownership threshold.
Neither the author proof nor this deduction grants admission. A later
source or final-book version can further reduce the candidate's
novelty; the mathematical statement alone does not certify priority.
