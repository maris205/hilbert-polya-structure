# Theorem package

Let `T²=R²/(Lx Z⊕Ly Z)`, `A=LxLy`, and use

`ω_B=dx∧dp_x+dy∧dp_y+B dx∧dy`, `H_cl=|p|²/2`.

For `B≠0`, put `J(u,v)=(-v,u)`. The exact lift of the flow is

`p(t)=R_{Bt}p0`, `c=q+Jp/B`, `q(t)=c-JR_{Bt}p0/B`.

## Main theorem

1. On every shell `E>0`, all trajectories have least phase-space period `2π/|B|`. The fixed set is empty at other times and is the whole energy shell at return times; because the return derivative is the identity, the returns are maximally clean. The orbit quotient is a two-torus.
2. A Hermitian line bundle with curvature `-iB dx∧dy` exists exactly when `N=BA/(2π)` is an integer. Its degree is `N`; flat holonomies exhaust the curvature-preserving twists.
3. If `N≠0`, the physical Bochner Hamiltonian has levels `E_n=|B|(n+1/2)`, each of multiplicity `|N|`, independently of flat holonomy.
4. Put `M=|N|` and `σ=sgn N`. For lifts `U,V` of the fixed positively oriented division vectors `(Lx/M,0),(0,Ly/M)`, every level carries a basis in which `Ue_j=e_{j+1}`, `Ve_j=exp(-2πiσj/M)e_j`, `U^M=V^M=I`, and `UV=exp(2πiσ/M)VU`. It is irreducible for `M>1`.
5. `Tr exp(-βH_B)=M exp(-β|B|/2)/(1-exp(-β|B|))` and `ζ_H(s)=M|B|^{-s}ζ(s,1/2)=M|B|^{-s}(2^s-1)ζ(s)`.
6. `ζ_H(0)=0`, `ζ'_H(0)=-(M/2)log 2`, and `det_ζ H_B=2^{M/2}`.
7. The least scalar revival is `2π/|B|` and equals `-I`; the least identity revival is `4π/|B|`.
8. The theorem separates `E=0`, both signs of `B`, `|N|=1`, nonintegral flux, and `B=0` instead of continuing regular formulas through them. At `B=0`, `q(t)=q_0+tp` closes exactly when `p_xt∈L_xZ` and `p_yt∈L_yZ` for some `t>0`; nonaxial closure is equivalent to `p_yL_x/(p_xL_y)∈Q`, axial nonzero motion closes, and zero velocity is stationary with no positive least period.

The proof uses explicit cyclotron integration, Chern–Weil plus a constructive cocycle, ladder algebra and genus-one Riemann–Roch, the finite Heisenberg commutator, geometric/Hurwitz summation, and adjacent spectral phase ratios. Full proofs are in `paper/main.tex` and `paper/main.pdf`.
