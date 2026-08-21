# HCS-C80 subgroup-threshold repair atlas

Let (Q=mathbb Z/9oplusmathbb Z/3oplusmathbb Z/2) and let (L) be the
frozen sixteen-label named support inherited from C78.  For a retained support
(Asubseteq L), write (Phi(A)) for its generated subgroup.  For every one
of the twenty actual subgroup rows (Hle Q), define the containment threshold

\[
 \tau_H(D)=\min\{|R|:R\subseteq D,
        H\subseteq\Phi((L\setminus D)\cup R)\}.
\]

This is deliberately different from C78's exact-closure repair distance
\(ρ(D)\): C80 only requires containment of a target subgroup, and the target
\(H=Q\) therefore satisfies \(τ_Q=ρ\).  The paper enumerates all
\(2^{16}=65536\) deletion masks and publishes, for every subgroup row, the
threshold distribution and the deleted-cardinality generating table.  It also
publishes the per-mask twenty-component profile, so no target row is inferred
from an abstract isomorphism class.

The scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`.
