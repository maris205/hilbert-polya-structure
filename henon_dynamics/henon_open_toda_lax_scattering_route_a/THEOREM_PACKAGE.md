# Theorem package: finite open Toda Lax flow and scattering

## Frozen convention

For \(N\ge2\), \(q,p\in\mathbb R^N\), set
\[
 H(q,p)=\frac12\sum_{j=1}^N p_j^2+
 \sum_{j=1}^{N-1}e^{q_j-q_{j+1}}.
\]
The endpoint convention is \(e^{q_0-q_1}=e^{q_N-q_{N+1}}=0\), so
\[
 \dot q_j=p_j,\qquad
 \dot p_j=e^{q_{j-1}-q_j}-e^{q_j-q_{j+1}}.
\]

Introduce Flaschka variables
\[
 a_j=\tfrac12e^{(q_j-q_{j+1})/2}>0,\qquad b_j=-\tfrac12p_j,
\]
and the real symmetric Jacobi matrix \(L\) and skew matrix \(B\)
\[
 L_{jj}=b_j,\quad L_{j,j+1}=L_{j+1,j}=a_j,\qquad
 B_{j,j+1}=a_j,\quad B_{j+1,j}=-a_j.
\]
Then \(\dot L=[B,L]\), equivalently
\[
 \dot a_j=a_j(b_{j+1}-b_j),\qquad
 \dot b_j=2(a_j^2-a_{j-1}^2),\quad a_0=a_N=0.
\]

## Theorem 1 — global Hamiltonian/Lax closure

Every finite \((q(0),p(0))\) has a solution for all \(t\in\mathbb R\).  The
positive edges satisfy \(a_j(t)>0\) at every finite time, \(L(t)\) is an
isospectral deformation, and
\[
 I_k=\frac1k\operatorname{tr}L^k,\quad 1\le k\le N,
 \qquad H=4I_2,\qquad \sum_jp_j=-2\operatorname{tr}L
\]
are constant.

*Proof.*  The displayed Hamilton equations give the Flaschka system and direct
matrix multiplication gives the commutator.  Since \(B^T=-B\),
\[
\frac d{dt}\operatorname{tr}L^k=k\operatorname{tr}(L^{k-1}[B,L])=0.
\]
In particular \(\operatorname{tr}L^2\) bounds every \(a_j,b_j\); the smooth
finite-dimensional vector field is therefore complete.  The scalar equation
\(\dot a_j=a_j(b_{j+1}-b_j)\) gives
\[
a_j(t)=a_j(0)\exp\!\left(\int_0^t(b_{j+1}-b_j)\,ds\right)>0,
\]
so no finite-time edge collision occurs.  Reconstructing
\(q_j-q_{j+1}=2\log(2a_j)\) and \(p_j=-2b_j\) closes the Hamiltonian statement;
the common position is the free center-of-mass coordinate.

## Theorem 2 — simple spectrum and sorting scattering

An irreducible real symmetric Jacobi matrix (\(a_j>0\)) has \(N\) simple real
eigenvalues.  Write them in decreasing order
\[
\lambda_1>\lambda_2>\cdots>\lambda_N.
\]
The open Toda solution obeys the Moser sorting limits
\[
 b_j(t)\longrightarrow\lambda_j\quad(t\to+\infty),\qquad
 b_j(t)\longrightarrow\lambda_{N+1-j}\quad(t\to-\infty).
\]
Consequently \(p_j=-2b_j\) are asymptotically ordered at the two ends and
\[
 q_j(t)=-2\lambda_jt+c_j^+ +o(1),\quad t\to+\infty,
\]
with the reversed eigenvalue order at \(t\to-\infty\).  The norming weights
\[
 \rho_k(t)=|v_1(\lambda_k,t)|^2,\qquad
 \rho_k>0,\quad\sum_k\rho_k=1,
\]
linearize the flow:
\[
 \rho_k(t)=\frac{\rho_k(0)e^{2\lambda_kt}}
 {\sum_\ell\rho_\ell(0)e^{2\lambda_\ell t}},\qquad
 b_1(t)=\sum_k\lambda_k\rho_k(t).
\]

*Proof sketch.*  The three-term eigenvector recurrence proves simplicity: an
eigenvector with first component zero has every component zero.  The Weyl
function \(m(z)=e_1^T(zI-L)^{-1}e_1=\sum_k\rho_k/(z-\lambda_k)\) has positive
residues and determines the Jacobi matrix by continued-fraction inversion.
Differentiating \(v_t=Bv\) at the first component gives
\[
\dot\rho_k=2(\lambda_k-b_1)\rho_k,
\]
which integrates to the displayed softmax formula.  The largest (respectively
smallest) exponent dominates at \(+\infty\) (respectively \(-\infty\)); the
continued-fraction reconstruction yields the full diagonal sorting limits and
the integrated position asymptotics.  This is a scattering theorem, not a
periodic-orbit statement.

An explicit all-$N$ reconstruction makes the asymptotics quantitative.  Put
$r_k(t)=\rho_k(0)e^{2\lambda_k t}$, $\tau_0=1$, and

\[
 \tau_j(t)=\sum_{|S|=j}\left(\prod_{k\in S}r_k(t)\right)
 \Delta(\lambda_S)^2,\qquad
 a_j=\frac{\sqrt{\tau_{j-1}\tau_{j+1}}}{\tau_j},\qquad
 b_j=\frac12\partial_t\log\frac{\tau_j}{\tau_{j-1}}.
\]

This Cauchy--Binet/Hankel formula is exact on the simple-spectrum chamber;
dominance of the top or bottom subsets gives (without finite-time fitting) the
two sorting limits.

## Theorem 3 — exact \(N=2\) ledger and action-angle boundary

For \(N=2\), let
\[
 d=\sqrt{(b_1(0)-b_2(0))^2+4a_1(0)^2},\quad
 \alpha=\operatorname{artanh}\frac{b_1(0)-b_2(0)}d.
\]
Then
\[
 a_1(t)=\frac d2\operatorname{sech}(dt+\alpha),\qquad
 b_{1,2}(t)=\frac{b_1(0)+b_2(0)\pm d\tanh(dt+\alpha)}2.
\]
The eigenvalues are \((b_1+b_2\pm d)/2\), and the edge tends to zero only at
the scattering ends.

On the simple-spectrum regular set, the ordered eigenvalues and positive
norming simplex \(\{\rho_k>0:\sum_k\rho_k=1\}\) are global inverse-scattering
coordinates.  After fixing center-of-mass action, logarithmic norming variables
give local canonical action-angle coordinates.  The uncompactified positive
open-chain leaf is noncompact (a scattering chamber), not a real compact
Liouville torus.  An \((N-1)\)-torus is obtained only by adjoining complex
norming phases/compactifying the isospectral manifold; this extension is not
used as a target operator here.  Concretely, nonzero complex residues are
quotiented by their common \(\mathbb C^\times\) gauge; fixing their moduli
leaves the phase fiber \((S^1)^N/S^1\simeq\mathbb T^{N-1}\) above each simple
spectrum.  This local phase torus is distinct from the real positive
scattering chamber.

## Degenerate boundary and Route-A decision

At a boundary edge \(a_j=0\), \(L\) splits into blocks.  Repeated roots can then
occur; the receipt uses \(N=3\), \(a_1=a_2=0\), \(b=(0,0,1)\), whose polynomial
is \(x^2(x-1)\).  This singular face is excluded from the regular action-angle
chart.  The finite characteristic polynomial \(\det(\lambda I-L)\) is a
source-local invariant, not a dynamical zeta or Fredholm determinant.

The strict Route-A tuple is
\[
 (\texttt{A0\_FAIL},\texttt{A1\_FAIL},\texttt{A2\_FAIL},
 \texttt{A3\_FAIL},\texttt{A4\_FORMAL\_HINT}),
\]
with ROUTE_A_REJECTED and route_b_invocation_allowed=false: there is no
arithmetic owner, primitive periodic repetition law, target divisor, or natural
Hilbert--Polya lift.  The positive result is the Hamiltonian/Lax/scattering
theorem itself.
