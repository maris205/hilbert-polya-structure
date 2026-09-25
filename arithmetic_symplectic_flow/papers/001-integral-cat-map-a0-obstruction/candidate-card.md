# P0 candidate card — `ASFS-20260913-CAT01` v1.0

**Frozen on:** 2026-09-13  
**State:** `FROZEN FOR A0 AUDIT; STOPPED AT A0 AFTER AUDIT`

Let \(M=\mathbb R^2/\mathbb Z^2=\mathbb T^2\), with \(\omega=dx\wedge dy\), and let
\[
A=\begin{pmatrix}2&1\\1&1\end{pmatrix},\qquad F([v])=[Av].
\]
This is the entire parameter record: no parameter search, prime table, von Mangoldt weight, Riemann-zero data, or per-prime object is allowed. Let \(\mu\) be Haar probability and \(\tau(x)=1\). Define
\[
M_\tau=\{(x,t):x\in M,0\le t\le1\}/((x,1)\sim(Fx,0)),
\]
with translation suspension flow \(\varphi^u\). The half-open interval is only a representative convention. Since \(\inf\tau=1\), the non-Zeno condition holds. With \(J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}\), \(A^TJA=(\det A)J=J\), hence \(F^*\omega=\omega\). The mapping torus is three-dimensional and is not claimed symplectic or Hamiltonian.

| Item | Frozen owner / definition | State |
| --- | --- | --- |
| Phase space and base map | \((\mathbb T^2,dx\wedge dy)\), displayed \(F\) | `FROZEN` |
| Parameters / measure / units | no free parameters; Haar probability; return-time unit | `FROZEN` |
| Roof / flow | \(\tau\equiv1\), \(M_\tau\), \(\varphi^u\) | `FROZEN` |
| Proposed arithmetic source | integral lattice action and maps on \((\mathbb Z/N\mathbb Z)^2\), \(N\ge2\) | `FROZEN AS PROPOSAL` |
| Allowed data | \(A\), integral iterates, intrinsic lattice/congruence constructions only | `FROZEN` |
| Coding / orbit convention | not used before A0 | `OPEN` |
| Transfer, zeta, determinant | not constructed | `OPEN` |
| Controls | [paper.md](paper.md) | `FROZEN` |
| Future lift owner | none asserted | `DEFERRED` |
| Route state | A0 `SCOPED FAIL`; A1/A2 `NOT EVALUATED`; Route A `UNASSIGNED`; Route B `NOT INVOKED` | `FROZEN STATUS` |

Changing the matrix, roof, allowed data, or later owner creates a new candidate rather than repairing this one.
