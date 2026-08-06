# Route A Suspension Audit

## Outcome

The energy-dependent **entrance-to-exit scattering** route survives at the
classical level.  The stronger claim that the same physical Poincaré section
can be compensated by a half-order pulse with uniform adapted \(C^1\) bounds
is obstructed by a scale mismatch.  The quantum clause remains conditional on
a uniform variable-metric/two-parameter calculus.

## Exact implicit suspension

Use flow-box coordinates \((\tau,I,z)\) with

\[
 \omega=d\tau\wedge dI+\omega_z.
\]

Let \(k_E(\tau,z)\) be a compactly supported energy-dependent Hamiltonian
isotopy on the transverse variables.  Define the autonomous Hamiltonian \(K\)
implicitly by

\[
 I=K-k_K(\tau,z),
 \qquad \sup|\partial_E k_E|<1.
\]

The implicit-function theorem gives

\[
 \partial_IK=(1-\partial_Ek_E)^{-1}>0.
\]

On \(K=E\), division of the transverse Hamilton equation by
\(\dot\tau=\partial_IK\) cancels the same factor and yields exactly

\[
 \frac{dz}{d\tau}=X_{k_E}(z),
 \qquad I=E-k_E(\tau,z).
\]

Thus an energy-dependent transverse Hénon isotopy can be realized exactly as
an autonomous entrance-to-exit scattering map.  For

\[
 T(E)\asymp\sqrt{\frac{\log E}{E}},\qquad
 k_E(\tau,z)=T(E)^{-1}\widehat k(\tau/T(E),z),
\]

one has

\[
 \partial_Ek_E=O((E\log E)^{-1/2}),
\]

so the implicit construction is valid at high energy.

## Positive classical density

On the section \(q_1=0,p_1>0\), choose a bulk with

\[
 |q_2|\le cR_E,\qquad |p_2|\le c\sqrt E,
 \qquad R_E\asymp\sqrt{\log E}.
\]

Its flux area is a fixed proportion of
\(R_E\sqrt E\).  A collar of duration
\(T(E)\asymp R_E/\sqrt E\) has monotone \(q_1\) and exact symplectic flow-box
coordinates.  Fixed-template cells, a bulk cutoff, and deletion of boundary
cells preserve positive flux density.  If the pulse occupies a fixed
proportion of each collar time, its active microcanonical density is also
positive.

This proves a classical scattering statement.  The physical return after
the collar is generally \(P_{0,E}\circ H_a\), not \(H_a\) itself.

## Obstruction to the former same-section A9 claim

In canonical adapted section variables

\[
 X=q_2/\sqrt{T(E)},\qquad Y=\sqrt{T(E)}p_2,
\]

the bulk diameter is

\[
 M_E\asymp\sqrt{R_E\sqrt E}
 \asymp(E\log E)^{1/4}.
\]

The no-go statement requires a density hypothesis, not merely nonidentity on
one positive-measure set.  A sufficient hypothesis is that, for every fixed
\(C\),

\[
 \frac{\bigl|\{Z\in B_E:|P_{0,E}(Z)-Z|\le C\}\bigr|}{|B_E|}
 \longrightarrow0,
\]

where \(B_E\) is the normalized bulk.  One route to this hypothesis is local
uniform convergence away from an \(o(1)\) grazing set to a piecewise analytic
twist return whose fixed set has area zero; that fixed-set lemma must be
proved separately for the chosen return.

For a fixed-cell Hénon template, \(H_{\rm cell}\) has \(O(1)\) adapted
displacement.  A pulse

\[
 k_E=T(E)^{-1}\widehat k(\tau/T(E),X,Y),
 \qquad \|\nabla_{X,Y}\widehat k\|\le C,
\]

acts for unit normalized time and can likewise displace adapted points by
only \(O(1)\).  If \(P_{0,E}\circ S_E=H_{\rm cell}\) on the active cells, all
active points must therefore lie in an \(O(1)\)-near-fixed set of
\(P_{0,E}\).  The density hypothesis makes that set asymptotically negligible,
contradicting positive active density.  Equivalently, a typical exact
compensator needs an \(\Omega(M_E)\) adapted displacement/gradient budget.
Consequently the former combination

\[
 \text{same physical section}
 +\text{exact Hénon return}
 +\text{positive density}
 +\text{half-order amplitude}
 +\text{uniform adapted }C^1
\]

is false under the stated near-fixed-density hypothesis.  The obstruction
does not apply if the adapted \(C^1\) norm is allowed to grow with energy.

## Remaining quantum bridge

A natural phase-space metric is

\[
 g=T(I)^{-2}d\tau^2+T(I)^2dI^2+dz^2.
\]

The scale also matches a two-parameter calculus with

\[
 h_E=E^{-1},\qquad \widetilde h_E=(\log E)^{-1},\qquad
 (h_E/\widetilde h_E)^{-1/2}=T(E)^{-1}.
\]

This is a design match, not yet a theorem.  A complete quantum statement
still needs: a uniform canonical atlas, admissibility/temperateness of the
metric, uniform chart/FIO symbol bounds, locally finite summation, Egorov and
product remainders, and positive-density bookkeeping after all cutoffs.

## Literature boundary

Existing Hamiltonian-suspension, fragmentation, Weyl--Hörmander,
anti-Wick/Gabor, and two-parameter semiclassical results provide local pieces.
The project literature audit found no primary theorem that already combines
an infinite locally finite positive-density flow-box lattice, the critical
scale \(T(E)\), uniform Hénon compensation, and global quantization.  This
should be stated as a search result, not as an absolute nonexistence claim.
