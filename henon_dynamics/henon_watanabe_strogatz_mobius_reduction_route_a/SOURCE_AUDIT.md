# C189 source audit

## Frozen primary sources

1. S. Watanabe and S. H. Strogatz, “Constants of motion for superconducting
   Josephson arrays,” *Physica D* **74** (1994), 197--253,
   DOI [10.1016/0167-2789(94)90196-1](https://doi.org/10.1016/0167-2789(94)90196-1).
   Role: original constants-of-motion reduction for identical sinusoidally
   coupled phase systems.
2. S. A. Marvel, R. E. Mirollo, and S. H. Strogatz, “Identical phase
   oscillators with global sinusoidal coupling evolve by Möbius group
   action,” *Chaos* **19** (2009), 043104,
   DOI [10.1063/1.3247089](https://doi.org/10.1063/1.3247089),
   [arXiv:0904.1680](https://arxiv.org/abs/0904.1680).
   Role: explicit disk-automorphism/`PSU(1,1)` formulation and orbit geometry.
3. A. Pikovsky and M. Rosenblum, “Partially integrable dynamics of
   hierarchical populations of coupled oscillators,” *Physical Review
   Letters* **101** (2008), 264103,
   DOI [10.1103/PhysRevLett.101.264103](https://doi.org/10.1103/PhysRevLett.101.264103).
   Role: independent primary account of the partial-integrability boundary.

The reduction and its invariants are classical.  C189 claims no priority for
them.  Its package-level contribution is a convention-locked all-forcing
synthesis, collision-stratum theorem, constant-generator trichotomy,
executable exact audit, and Route-A stopping certificate.

## Convention lock

The common phase equation and circle coordinate are

\[
 \dot\theta_j=f(t)+\operatorname{Im}(H(t)e^{-i\theta_j}),
 \qquad z_j=e^{i\theta_j},
\]

so the Riccati equation is

\[
 \dot z_j=ifz_j+\frac12(H-\overline H z_j^2).
\]

With `J=diag(1,-1)`, the lifted generator is

\[
 A(t)=\frac12\begin{pmatrix}if&H\\ \overline H&-if\end{pmatrix},
 \qquad A^*J+JA=0.
\]

The projective action is

\[
 M(z)=\frac{az+b}{\overline b z+\overline a}
     =e^{i\psi}\frac{z+\alpha}{1+\overline\alpha z}.
\]

For constant `f=omega`, put
`Delta=omega^2-|H|^2`.  Elliptic means `Delta>0`; its projected
period is `2*pi/sqrt(Delta)`.  At `Delta=0`, the zero generator is the
identity and must not be mislabeled parabolic.

## Evidence and citation boundary

- The sources justify the classical owner and Möbius formulation.
- `THEOREM_PACKAGE.md` gives the complete proof in the frozen convention.
- Exact rational circle points, disk automorphisms, local Riccati jets, and
  constant generators test implementation conventions only.
- No finite census proves the all-parameter theorem.
- No external review, exhaustive literature novelty certification, target
  comparison, or acceptance claim is made.
