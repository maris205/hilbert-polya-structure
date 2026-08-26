# C170 theorem package

## Assumptions and conventions

Fix \(N\ge1\) and \(\varepsilon_0,\ldots,\varepsilon_{N-1}\in\{\pm1\}\). On \(X_N=\mathbb Z/N\mathbb Z\times\{\pm1\}\), let
\[
T(j,s)=(j+1,\varepsilon_j s),\qquad \eta=\prod_{j=0}^{N-1}\varepsilon_j.
\]
Counting measure defines \(\ell^2(X_N)\), and \(U_Tf=f\circ T^{-1}\); determinant formulas are unchanged by choosing the inverse permutation convention.

## Classification theorem

For every \(N\) and every marker word:

1. \(T^N(j,s)=(j,\eta s)\).
2. If \(\eta=+1\), all \(2N\) states have exact period \(N\) and form two \(N\)-cycles.
3. If \(\eta=-1\), all states have exact period \(2N\) and form one \(2N\)-cycle.
4. With \(L=N\) for \(\eta=+1\) and \(L=2N\) for \(\eta=-1\),
\[
#\operatorname{Fix}(T^n)=\begin{cases}2N,&L\mid n,\\0,&L\nmid n.\end{cases}
\]
Writing \(c=2N/L\),
\[
\zeta_T(z)=(1-z^L)^{-c},\qquad
\det(I-zU_T)=(1-z^L)^c.
\]
The spectrum consists of every \(L\)-th root of unity with multiplicity \(c\).
5. There is an explicit involutive reversor \(R\) and \(\Theta f=\overline{f\circ R}\) satisfies \(\Theta U_T\Theta=U_T^{-1}\).
6. \(U_T\) is self-adjoint exactly when \(L\le2\).

## Proof

During one circuit, the position returns and the spin accumulates every marker once, proving \(T^N(j,s)=(j,\eta s)\). Any return time must be divisible by \(N\), because the position advances by one. If \(\eta=+1\), the first possible return \(N\) works. If \(\eta=-1\), time \(N\) flips the spin and time \(2N\) is the first return. Since \(|X_N|=2N\), division by the common least period gives respectively two and one cycles. The fixed-count law follows immediately.

For a permutation whose cycle lengths are all \(L\), each cycle contributes \((1-z^L)^{-1}\) to the Artin--Mazur zeta and \(1-z^L\) to \(\det(I-zU_T)\). The cyclic permutation matrix has the \(L\)-th roots of unity once each; \(c\) cycles give multiplicity \(c\). A unitary permutation is self-adjoint exactly when its cycles have length at most two, proving the boundary.

For reversal, set \(g_0=1\), \(g_j=\prod_{r<j}\varepsilon_r\), and \(q=g_js\). In \((j,q)\) coordinates, the map advances \(j\), leaves \(q\) unchanged away from the wrap, and changes \(q\) to \(\eta q\) at the wrap. If \(\eta=+1\), reflect \(j\mapsto-j\) separately on each \(q\)-cycle. If \(\eta=-1\), unfold by \(\psi(j,+1)=j\), \(\psi(j,-1)=N+j\); the map becomes \(t\mapsto t+1\) on \(\mathbb Z/(2N)\mathbb Z\), reversed by \(t\mapsto-t\). Pulling either reflection back through the gauge yields an explicit involution with \(RTR=T^{-1}\), and complex conjugation supplies the stated antiunitary.

## Edge cases and evidence status

For \(N=1,\eta=+1\), the map is the identity on two states. For \(N=1,\eta=-1\), it is one transposition. Both obey every formula. All theorem statements are `PROVED`. Exhaustive enumeration through \(N=10\) is only a regression sentinel.

## Route-A decision

The v0.2 tuple is `(A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)`, overall `ROUTE_A_REJECTED`, Route B false. The paper remains exact theorem progress, but A0 failure rejects it as a primary Hilbert--Pólya candidate. The primitive cycles are intrinsic and completely classified, yet the family is a finite, exactly reducible kinetic toy model with no proved arithmetic semantics or target comparison.
