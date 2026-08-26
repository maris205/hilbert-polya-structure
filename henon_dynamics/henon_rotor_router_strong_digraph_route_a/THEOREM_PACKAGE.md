# Theorem package

## Frozen dynamics

Let \(G=(V,A)\) be a finite nonempty strongly connected directed multigraph. Parallel arcs and loops are allowed and every arc is distinguished. Fix a cyclic order of the outgoing arcs at each vertex. A rotor state selects one outgoing arc at each vertex; a chip occupies a vertex \(w\). One tick advances the rotor at \(w\) to its next arc and moves the chip along that newly selected arc.

A rotor configuration has one selected outgoing arc per vertex and hence a functional directed graph. A **unicycle state** is a rotor configuration with exactly one directed cycle and a chip on that cycle. These are precisely the recurrent states for the frozen permutation.

For \(v\in V\), let \(t_v\) be the number of directed spanning in-arborescences oriented toward \(v\). Equivalently, \(t_v\) is the \(v\)-cofactor of the row Laplacian \(D_{\rm out}-A\). Put

\[
M=\gcd_{v\in V}t_v,
\qquad
L=\frac1M\sum_{v\in V}d_v^+t_v.
\]

## Main theorem

For every frozen graph and every choice of rotor cyclic orders:

1. The recurrent unicycle permutation has exactly \(M\) orbits.
2. Every orbit has exact length \(L\).
3. On every orbit, the chip departs from vertex \(v\) exactly \(d_v^+t_v/M\) times.
4. Every distinguished outgoing arc from \(v\) is traversed exactly \(t_v/M\) times.
5. The total number of recurrent states is \(ML=\sum_vd_v^+t_v\).
6. Therefore
   \[
   \#\operatorname{Fix}(R^n)=\begin{cases}ML,&L\mid n,\\0,&L\nmid n,\end{cases}
   \quad
   \zeta_{\rm AM}(z)=(1-z^L)^{-M}.
   \]
7. On \(\ell^2\) of recurrent states, the permutation Koopman operator \(U\) satisfies
   \[
   \det(I-zU)=(1-z^L)^M,
   \]
   and every \(L\)-th root of unity occurs with multiplicity \(M\).

If \(G\) is Eulerian, the kernel relation forces all \(t_v\) to equal a common \(\tau\). Hence \(M=\tau\), \(L=|A|\), there are \(\tau\) recurrent orbits, and each orbit traverses every distinguished arc exactly once.

## Proof

The classical rotor-router orbit theorem identifies unicycles as the recurrent phase. Pham's Theorem 1 supplies the exact common orbit length \(L\) and the exact orbit count \(M\) for this same advance-then-move model, including loops and multiple arcs. Consider one complete orbit and let \(x_v\) be the number of full rotor turns at \(v\). Each outgoing arc from \(v\) is then used exactly \(x_v\) times, so the chip departs \(v\) exactly \(d_v^+x_v\) times. Equality of arrivals and departures at every vertex gives

\[
(D_{\rm out}-A)^T x=0.
\]

Strong connectivity makes this kernel one-dimensional with a positive primitive integer generator. By the directed matrix-tree theorem, the cofactor vector \(t=(t_v)\) lies in the same kernel. Its primitive reduction is \(t/M\), so \(x=q(t/M)\) for a positive integer \(q\). Flow balance alone does not determine \(q\). Pham's exact length gives
\[
L=\sum_vd_v^+x_v=qM^{-1}\sum_vd_v^+t_v=qL,
\]
hence \(q=1\). This proves the arc frequencies and vertex visits independently of the cyclic orders. In Pham's proof, primitivity comes from deleting the chosen basepoint's outgoing arcs, using chip addition on the remaining acyclic rotors, and computing the deleted Laplacian row class to have order \(t_v/M\) in the quotient by the other row classes. That source mechanism is imported here; it is not replaced by a balance-only assertion.

For the state count, take a unicycle state with chip \(v\) and delete the selected rotor arc out of \(v\). What remains is an in-arborescence toward \(v\); conversely, an in-arborescence toward \(v\) together with a chosen outgoing arc at \(v\) reconstructs a unique unicycle state with chip on the unique cycle. Thus there are \(d_v^+t_v\) such states at \(v\), and \(\sum_vd_v^+t_v=ML\) in total. Division by Pham's exact length recovers \(M\) orbits.

The fixed-count formula follows from the disjoint union of \(M\) cycles of length \(L\). Exponentiating its logarithmic series gives the zeta, while the characteristic polynomial of a length-\(L\) cyclic permutation is \(1-z^L\); taking \(M\) copies proves the determinant and spectrum. In the Eulerian case the all-ones vector lies in the positive Laplacian kernel, so uniqueness makes \(t_v\) constant and the specialization follows.

## Operator and reversal boundary

The finite permutation Koopman operator is a natural unitary quantization of this frozen recurrent system, so A4 earns `A4_NATURAL_QUANTIZATION`. Abstract cycle reversal exists after choosing a basepoint on each orbit, but those basepoints are not selected by the source graph. Therefore no source-canonical time-reversal involution is claimed.

## Route-A consequence

The strict tuple is

\[
(\texttt{A0_FAIL},\texttt{A1_WEAK},\texttt{A2_FAIL},\texttt{A3_FAIL},\texttt{A4_NATURAL_QUANTIZATION}).
\]

A0 fails because arborescences and rotor cycles supply no rational-prime labels or prime-power weights. A1 is weak: orbit completeness is exact, but there are no intrinsic arithmetic labels or target amplitudes. A2 and A3 fail because the zeta is a finite-cycle polynomial reciprocal with no authorized target divisor, functional equation, or Weil compression. A0 failure forces `ROUTE_A_REJECTED` even though A4 is natural.
