# Narrative report

Continuous-time search on a complete graph is exactly solvable for a reason
that also makes convention errors easy to conceal: permutation symmetry
compresses the initialized dynamics to two dimensions while leaving two large
dark eigenspaces.  A success-only derivation can therefore obtain the right
clock and still omit most of the spectrum.

HCS-C323 keeps all sectors.  The marked and unmarked dark spaces have fixed
eigenvalues `-1` and `0`; the remaining bright block has discriminant
`Omega^2=(g-1)^2+4gM/N`.  Its exponential yields the exact marked-subspace
probability, not merely one marked amplitude.  The maximum defect factors as

\[
1-p_{\max}=
\frac{(1-M/N)(g-1)^2}{(g-1)^2+4gM/N},
\]

which turns resonance necessity into an identity: in the interior, perfect
search occurs exactly at `g=1`.

The same formula resolves scaling.  A fixed detuning destroys high-fidelity
search as the marked fraction vanishes, while `g=1+c sqrt(a)` retains the
nontrivial limiting peak `4/(c^2+4)`.  Finally, the adjacency convention is
closed exactly: with `g=gamma N`, the graph and rank-one-driver Hamiltonians
differ by `gamma I`, so probabilities agree but absolute eigenvalue ledgers
must record the scalar shift.

The theorem is a complete source-dynamics result, not an arithmetic bridge.
Its strict Route-A tuple ends at source-native natural quantization and leaves
Route B locked.
