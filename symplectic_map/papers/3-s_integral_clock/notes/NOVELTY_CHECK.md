# Novelty Check — `s_integral_clock`

Search boundary: sources checked through **2026-08-13**.

## Verdict

`ABANDON AS A STANDALONE THEOREM / KEEP ONLY AS A SUPPORTING OBSTRUCTION LEMMA`

The proposed statement is mathematically correct in the form

- \(A\in \mathrm{Sp}(2d,\mathbb Z)\) and \(\lambda\in \mathbb Q\) an eigenvalue \(\implies \lambda=\pm 1\);
- \(A\in \mathrm{Sp}(2d,\mathbb Z[S^{-1}])\) and \(\lambda\in \mathbb Q\) an eigenvalue \(\implies \lambda\) is an \(S\)-unit, so \(\lambda=\pm\prod_{\ell\in S}\ell^{n_\ell}\);
- hence a rational prime eigenvalue \(p>1\) forces \(p\in S\).

But the novelty is weak. The integral case is an immediate corollary of standard symplectic reciprocity/palindromicity plus the rational-root theorem. The \(S\)-integral case is the same observation rewritten in valuation language: if \(\lambda\) and \(\lambda^{-1}\) are both integral outside \(S\), then \(\lambda\) is an \(S\)-unit. The finite-state/noncommutative cocycle packaging does not materially deepen the theorem, because each periodic monodromy is still just a single matrix in the same arithmetic group.

My best estimate is:

- as a standalone paper theorem: **novelty 2.5/10**;
- as an internal certificate/no-go lemma inside a broader paper: **useful and defensible**;
- as a publishable short note: **unlikely**, unless strengthened substantially beyond rational eigenvalues.

## Proposed method

Use periodic monodromies of a finite-state symplectic cocycle with branch matrices in \(\mathrm{Sp}(2d,\mathbb Z[S^{-1}])\) (or more generally \(\mathrm{Sp}(2d,\mathcal O_{K,S})\)) as an arithmetic “eigenvalue clock.” The target claim is that exact rational-prime multipliers cannot appear unless the prime already lies in the finite localization set \(S\), with the integral case \(S=\varnothing\) excluding all rational primes \(>1\).

## Core claims and novelty assessment

| Claim | Assessment | Why |
|---|---|---|
| 1. For \(A\in \mathrm{Sp}(2d,\mathbb Z)\), every rational eigenvalue is \(\pm 1\). | **LOW novelty** | Elementary consequence of monic palindromic characteristic polynomial with constant term \(1\), hence rational roots are \(\pm1\). |
| 2. For \(A\in \mathrm{Sp}(2d,\mathbb Z[S^{-1}])\), every rational eigenvalue is an \(S\)-unit. | **LOW novelty** | Same proof after replacing the rational-root step by “\(\lambda\) and \(\lambda^{-1}\) are integral outside \(S\)”. Standard localization arithmetic. |
| 3. Therefore a periodic monodromy in a finite-state symplectic cocycle cannot have prime eigenvalue \(p>1\) unless \(p\in S\). | **LOW–MEDIUM novelty** | New only as packaging for your dynamical program; the proof does not use noncommutativity in a deep way. |
| 4. The theorem is sharp: diagonal blocks \(\mathrm{diag}(q,q^{-1})\) with \(q\) an \(S\)-unit realize all allowed rational eigenvalues. | **LOW novelty** | Explicit positive controls are immediate. |
| 5. The obstruction is only about exact rational eigenvalues, not spectral radius or singular values. | **Important scope point, not a novelty claim** | Stronger versions are false. Integral symplectic matrices can have irrational algebraic-unit spectral radii \(>1\). |

## Why the theorem is probably viewed as “known/elementary”

The closest standard facts already in the literature are enough to make the main statement feel like a one-paragraph corollary:

1. integral symplectic characteristic polynomials are palindromic / self-reciprocal;
2. reciprocal symmetry forces \(\lambda^{-1}\) to be an eigenvalue whenever \(\lambda\) is;
3. for integral coefficients, rational roots of a monic polynomial with constant term \(1\) are \(\pm1\);
4. for \(S\)-integers, an element of \(K^\times\) that is integral outside \(S\) together with its inverse is exactly an \(S\)-unit.

So the “matrix cocycle” extension sounds broader than Paper 1’s scalar obstruction, but mathematically it bypasses the difficult noncommutative part: once a periodic word is fixed, the entire problem collapses to a single arithmetic symplectic matrix.

That is the biggest novelty risk. A reviewer can say:

> this is not really a theorem about noncommutative products; it is an elementary arithmetic property of one resulting matrix.

## Closest prior work

| Reference | Year | Overlap | What it already gives | Delta from your claim |
|---|---:|---|---|---|
| Qingjie Yang, *Decomposability of symplectic matrices over principal ideal domain*, J. Number Theory 149, 139–152, DOI: [10.1016/j.jnt.2014.10.015](https://doi.org/10.1016/j.jnt.2014.10.015) | 2015 | **High** | Search snippet states: every integral symplectic characteristic polynomial is palindromic, and conversely every monic palindromic polynomial of even degree occurs. | Your integral claim is a rational-root corollary of this spectral structure. |
| R. Ackermann, *Achievable spectral radii of symplectic Perron-Frobenius matrices*, New York J. Math. 17 (2011), 683–697, abstract: <https://nyjm.albany.edu/j/2011/17-29.html> | 2011 | **High** | Every algebraic unit appears as an eigenvalue of some integral symplectic matrix; many Perron units appear as spectral radii. | Shows immediately that any stronger “no large eigenvalue / no large spectral radius” reading is false. |
| Disheng Xu, *Density of positive Lyapunov exponents for symplectic cocycles*, JEMS 21 (2019), 3143–3190, DOI: [10.4171/JEMS/899](https://doi.org/10.4171/JEMS/899) | 2019 | **Medium** | Finite-valued and continuous \(\mathrm{Sp}(2d,\mathbb R)\)-cocycles are already established objects of study. | Adjacent cocycle context, but no arithmetic rational-eigenvalue obstruction. |
| Xianzhe Li and Li Wu, *The fibered rotation number for ergodic symplectic cocycles and its applications: I. Gap labelling theorem*, Math. Z. 311 (2025), article 53, DOI: [10.1007/s00209-025-03860-1](https://doi.org/10.1007/s00209-025-03860-1) | 2025 | **Medium** | Current symplectic-cocycle literature remains active, but in rotation-number / spectral-theory directions. | Confirms the area is alive, but not in your arithmetic-\(S\)-unit direction. |
| Pär Kurlberg, Alina Ostafe, Zeev Rudnick, Igor E. Shparlinski, *On Quantum Ergodicity for Higher Dimensional Cat Maps*, Commun. Math. Phys. 406 (2025), article 174, DOI: [10.1007/s00220-025-05350-1](https://doi.org/10.1007/s00220-025-05350-1) | 2025 | **Low–Medium** | Cat maps remain a canonical \(\mathrm{Sp}(2g,\mathbb Z)\) control family. | Good negative-control context; does not supply prime-eigenvalue arithmetic. |
| Brian Conrad, *The lattice of S-integers* (course note), <https://math.stanford.edu/~conrad/676Page/handouts/Sintlattice.pdf> | undated note | **Background** | Characterizes \(\mathcal O_{K,S}^\times\) as elements with absolute value \(1\) outside \(S\). | Supplies the exact arithmetic language needed for the \(S\)-integral extension. |

## Exact theorem scope

### Safe theorem statement over \(\mathbb Q\)

Let \(S\) be a finite set of rational primes and let \(A\in \mathrm{Sp}(2d,\mathbb Z[S^{-1}])\).

If \(\lambda\in \mathbb Q\) is an eigenvalue of \(A\), then \(\lambda^{-1}\) is also an eigenvalue, and both \(\lambda,\lambda^{-1}\) are integral outside \(S\). Therefore \(\lambda\in \mathbb Z[S^{-1}]^\times\), so

\[
\lambda=\pm\prod_{\ell\in S}\ell^{n_\ell},\qquad n_\ell\in\mathbb Z.
\]

In particular, if \(\lambda=p>1\) is a rational prime, then \(p\in S\).

For \(S=\varnothing\), this reduces to \(\lambda=\pm1\).

### Safe theorem statement over a number field

Let \(K\) be a number field, \(S\) a finite set of places containing the archimedean ones, and \(A\in \mathrm{Sp}(2d,\mathcal O_{K,S})\).

If \(\lambda\in K\) is an eigenvalue of \(A\), then \(\lambda\in \mathcal O_{K,S}^\times\).

This is the correct number-field generalization. If you want to state a conclusion for a rational prime \(p\in \mathbb Z\subset K\), you must say carefully that **every prime of \(K\) above \(p\)** must lie in \(S\). If you instead work with \(\mathbb Z[S^{-1}]\), then the cleaner conclusion is simply \(p\in S\).

## Sharp controls and counterexamples

### Strict negative controls

- Any hyperbolic cat map \(A\in \mathrm{SL}(2,\mathbb Z)=\mathrm{Sp}(2,\mathbb Z)\) is a negative control for exact rational-prime eigenvalues.
- Example: Arnold’s cat map

\[
A=\begin{pmatrix}1&1\\1&2\end{pmatrix}
\]

has eigenvalues \(\frac{3\pm\sqrt5}{2}\), not rational.

- More generally, your repository’s existing cat-map observation is correct: in dimension \(2\), a prime unstable eigenvalue \(p\) would force trace \(p+p^{-1}\notin\mathbb Z\).

### Sharp planted positives

For any \(S\)-unit \(q\in \mathbb Z[S^{-1}]^\times\),

\[
\operatorname{diag}(q,q^{-1})\in \mathrm{Sp}(2,\mathbb Z[S^{-1}])
\]

has rational eigenvalue \(q\). In higher dimension, add identity symplectic blocks.

So the statement is exact: **allowed rational eigenvalues are precisely rational \(S\)-units**.

### Why spectral radius is the wrong object

This is the most important scope warning.

Ackermann’s 2011 paper shows that every algebraic unit occurs as an eigenvalue of some integral symplectic matrix, and many Perron units occur as spectral radii of integral symplectic Perron-Frobenius matrices. Therefore:

- the obstruction does **not** control spectral radius;
- it does **not** imply “large multipliers are impossible”;
- it only excludes **exact rational** eigenvalues not supported by \(S\).

### Why singular values are also outside scope

Singular values of a symplectic matrix also occur in reciprocal pairs, but they are eigenvalues of \(A^{\!*}A\), not roots of the characteristic polynomial of \(A\). The rational-root argument does not apply.

For the cat map \(A=\begin{pmatrix}1&1\\1&2\end{pmatrix}\), the eigenvalues are \(\frac{3\pm\sqrt5}{2}\), while the singular values are

\[
\sqrt{\frac{7\pm 3\sqrt5}{2}},
\]

again reciprocal, but governed by a different polynomial.

So the safe title is about **rational eigenvalues of periodic monodromies**, not spectral radii, Lyapunov exponents, or singular values.

## What is actually new relative to Paper 1?

Only a narrow point:

- Paper 1 / the scalar-clock obstruction works by finite \(\mathbb Q\)-rank of locally constant scalar logs.
- This candidate replaces scalar clocks by periodic monodromy eigenvalues of matrix-valued symplectic cocycles.

But the price is that the matrix theorem becomes much more elementary than it first appears. It does not use:

- noncommutativity of the branch matrices in any serious way;
- fine cocycle dynamics;
- multiplicative independence of many local generators;
- or symplectic geometry beyond reciprocal pairing.

So the “extension” is real, but not deep enough to anchor a paper by itself.

## Query log: three variants per claim

### Claim 1 — integral symplectic matrices cannot have rational prime eigenvalue

Queries used:

1. `integral symplectic matrix rational eigenvalue`
2. `Sp(2n,Z) rational eigenvalue`
3. `2024 2025 2026 symplectic matrix reciprocal eigenvalues rational`

Relevant outcomes:

- Yang 2015 via search snippets and citations around palindromic characteristic polynomials and realizability.
- 2026 spectral-type papers on symplectic matrices still treat palindromicity/reciprocity as standard structure.

Assessment:

- I found no paper advertising your exact corollary as a standalone theorem.
- That absence does **not** help novelty much, because the result looks like folklore.

### Claim 2 — \(S\)-integral version

Queries used:

1. `S-integer symplectic matrix eigenvalue`
2. `S-unit symplectic matrix eigenvalue`
3. `2024 2025 2026 S-unit symplectic matrix`

Relevant outcomes:

- No direct overlap.
- Results returned were mostly unrelated \(p\)-adic symplectic geometry or generic \(S\)-unit literature.
- Conrad’s note gives the needed arithmetic background on \(\mathcal O_{K,S}\) and \(\mathcal O_{K,S}^\times\).

Assessment:

- The exact formulation is not a visible named topic.
- But again, that seems to be because it is too elementary, not because it is a hidden open direction.

### Claim 3 — finite-state / finite-valued symplectic cocycle setting

Queries used:

1. `finite valued symplectic cocycle`
2. `periodic symplectic cocycle eigenvalues`
3. `2024 2025 2026 symplectic cocycle periodic eigenvalues`

Relevant outcomes:

- Xu 2015/2019 on finite-valued symplectic cocycles and Lyapunov exponents.
- Li–Wu 2025 on rotation numbers for ergodic symplectic cocycles.
- 2025–2026 quasi-periodic / Hermitian-symplectic cocycle papers in spectral theory.

Assessment:

- The cocycle context is standard and active.
- I found no direct precedent for your exact rational-\(S\)-unit obstruction in that context.
- But the reason appears to be that the cocycle version is immediate from the one-matrix statement.

### Claim 4 — cat maps, reciprocal-polynomial/spectral-radius boundary, 2024–2026

Queries used:

1. `cat map Sp(2g,Z) 2025`
2. `spectral radius integral symplectic matrix algebraic unit`
3. `2024 2025 2026 reciprocal polynomial symplectic matrix spectral radius`

Relevant outcomes:

- Kurlberg–Ostafe–Rudnick–Shparlinski 2025 confirms cat maps remain canonical \(\mathrm{Sp}(2g,\mathbb Z)\) controls.
- Ackermann 2011 shows algebraic units and Perron units do appear as eigenvalues/spectral radii of integral symplectic matrices.
- Liechti 2024 studies minimal spectral radii of skew-reciprocal integer matrices, confirming this spectral territory is active but differently focused.

Assessment:

- This search strongly supports your intended negative controls.
- It also strongly warns against overclaiming on spectral radius.

## Publishability assessment

### As a theorem note

Weak.

The proof is too short and too reducible to known facts. A referee in arithmetic dynamics, algebraic groups, or linear algebra is likely to regard it as an exercise-level corollary.

### As a certificate inside a larger paper

Reasonable.

If your paper’s real contribution is a broader obstruction program for “prime clocks” in symplectic dynamics, then this lemma is useful as:

- a design filter,
- a sharp negative control,
- a matrix-valued analogue of the scalar finite-rank obstruction,
- and a clean reason not to use cat maps or integral finite alphabets for exact rational-prime multipliers.

### What would make it stronger

One of the following would be needed:

1. a genuinely dynamical theorem where the cocycle structure matters, not just the resulting monodromy matrix;
2. a classification/realization theorem inside a nontrivial restricted family of cocycles, not just arbitrary diagonal block controls;
3. an extension from exact rational eigenvalues to a richer arithmetic invariant that still survives matrix noncommutativity;
4. a consequence for a concrete symplectic model family that is not already obvious from the arithmetic group containing its monodromies.

## Recommendation

### If the question is “Should this become Paper 2/3 on its own?”

**No.**

Abandon that plan.

### If the question is “Should we keep the theorem?”

**Yes, but only as a lemma.**

Use it as:

- `S-integral rational-eigenvalue obstruction for periodic symplectic monodromies`, or
- `elementary arithmetic obstruction for exact prime eigenvalue clocks`.

### Safest positioning

Do **not** sell it as:

- a deep theorem about noncommutative symplectic products,
- a spectral-radius obstruction,
- a Lyapunov-spectrum obstruction,
- or a new arithmetic-dynamics classification theorem.

Do sell it as:

- an elementary but sharp obstruction certificate;
- a matrix-valued extension of the repository’s earlier scalar clock filters;
- a way to rule out exact rational-prime multipliers in integral / \(S\)-integral finite-state symplectic constructions before spending time on them.

## Primary references checked

1. Qingjie Yang, *Decomposability of symplectic matrices over principal ideal domain*, J. Number Theory 149 (2015), 139–152. DOI: <https://doi.org/10.1016/j.jnt.2014.10.015>
2. R. Ackermann, *Achievable spectral radii of symplectic Perron-Frobenius matrices*, New York J. Math. 17 (2011), 683–697. Abstract page: <https://nyjm.albany.edu/j/2011/17-29.html>
3. Disheng Xu, *Density of positive Lyapunov exponents for symplectic cocycles*, J. Eur. Math. Soc. 21 (2019), 3143–3190. DOI: <https://doi.org/10.4171/JEMS/899>
4. Xianzhe Li and Li Wu, *The fibered rotation number for ergodic symplectic cocycles and its applications: I. Gap labelling theorem*, Math. Z. 311 (2025), article 53. DOI: <https://doi.org/10.1007/s00209-025-03860-1>
5. Pär Kurlberg, Alina Ostafe, Zeev Rudnick, Igor E. Shparlinski, *On Quantum Ergodicity for Higher Dimensional Cat Maps*, Commun. Math. Phys. 406 (2025), article 174. DOI: <https://doi.org/10.1007/s00220-025-05350-1>
6. Brian Conrad, *The lattice of S-integers* (course note), <https://math.stanford.edu/~conrad/676Page/handouts/Sintlattice.pdf>
7. Livio Liechti, *On the minimal spectral radii of skew-reciprocal integer matrices*, New York J. Math. 30 (2024), 307–322. Abstract page: <https://nyjm.albany.edu/j/2024/30-11.html>

## Bottom line in one sentence

The statement is correct and sharp, but it is too elementary to carry a paper: keep it as a rigorously sourced obstruction lemma, not as the headline novelty claim.
