# Source lock — Paper 28 / SD-C30

Lock time: 2026-08-14 UTC

The manuscript is locked to the following read-only research artifacts:

| Artifact | SHA-256 |
|---|---|
| /tmp/paper28_research_package.md | 68df371e9c8b9a76638b7fdde643d42ba31c84ce13c02ffdb95367986bdff924 |
| /tmp/paper28_chiral_incidence.py | e29553c5a04cb31393b6ef8f93d2718285bac52d956cffc04d4c8d53fc6cc737 |
| /tmp/paper28_chiral_incidence_results.json | 118ae2e85e4ce8d403673f1d00725520c7137a3a032bb9201cda186a61cb5cfb |

The research package underwent a Markdown delimiter repair before this lock. The final post-repair hash is recorded above; mathematical content, prototype, and result JSON remain unchanged.

## Frozen scientific claims

1. \(T_s\in\mathcal S_q\) iff \(\sum_{p}p^{-q\Re s}<\infty\); for prime atoms this is equivalent to \(q\Re s>1\).
2. The reflected block
   \[
   \mathcal B_s=\begin{pmatrix}0&T_s\\T_{1-s}^{\sharp}&0\end{pmatrix}
   \]
   belongs to \(\mathcal S_q\) precisely on \(1/q<\Re s<1-1/q\). The first nonempty integer-order strip is \(q=3\).
3. On \(s=1/2+it\), \(\mathcal B_s\) is compact self-adjoint but is a \(t\)-dependent family, not a fixed Hilbert–Pólya operator.
4. The exact native Gram coefficients are
   \[
   G_{pp}=C_\eta(1+p^{-2\eta}),\qquad
   G_{pq}=C_\eta\frac{(pq)^{-2\eta}}
   {(1+p^{-2\eta})(1+q^{-2\eta})}.
   \]
5. \(\det_3\) deletes powers \(1,2\); odd block traces vanish; power \(4\) is first visible. The frequency \(2\log(q/p)\) in \(\operatorname{Tr}\mathcal B_{1/2+it}^{4}\) has positive coefficient \(4G_{pq}^2/(pq)\).
6. Native spectral motion is exact but generic across non-arithmetic controls.
7. Every positive common orthogonalizing metric has an atom-diagonal conjugate \(Z^*GZ\), hence collapses the active family to independent coordinate atoms and erases \(t\)-motion.

## Marker ownership firewall

The main critical-line theorem is the arithmetic specialization \(u=1\).
One may formally retain the inherited digit marker by defining

\[
T_s(u)=\sum_p u^{\ell(p)}p^{-s}q_p,
\]

but the \(r\)-th atom power carries \(u^{r\ell(p)}\), not
\(u^{\ell(p)}\). No argument may silently drop this repetition factor.
Moreover, \(|u|<1\) changes the coefficient decay and therefore the
Schatten threshold; it is a different regularized object, not analytic
continuation of the \(u=1\) critical theorem.

## Frozen route and scope

    (A0_STRUCTURAL_ARITHMETIC_RELATION,
     A1_FAIL,
     A2_ANALYTIC_DETERMINANT,
     A3_FAIL,
     A4_FAIL)

- Decision: REJECTED
- Route B: false
- Target-zero fields: NA
- No target-zero locations, labels, or statistics may enter the manuscript.
- No claim may identify the auxiliary \(z\)-zeros of a regularized determinant with zeta zeros.
- No numerical cutoff trace may be described as the infinite \(\operatorname{Tr}\mathcal B^2\).

## Writer authority

The writer may create or edit only narrative, proof, derivation, literature, planning, figure, LaTeX, bibliography, and compilation-audit files in this paper directory. It may not modify code/, results/, experiments/, docs/evaluations/, any manifest, the repository README, or Git state.
