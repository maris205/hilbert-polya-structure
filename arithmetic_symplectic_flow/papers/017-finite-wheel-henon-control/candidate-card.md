# Candidate card — `ASFS-20260913-WHEEL01`, version 1

| Field | Frozen definition | Status |
| --- | --- | --- |
| Phase space | `M=T*(S^1 x R^2)` with canonical `omega=dtheta^dI+dx^dxi+dy^deta` | frozen |
| Wheel data | `P=30`; `w_j=1` iff `gcd(j,30)=1`, for `j=0,...,29` | frozen; externally supplied control |
| Parameter function | `a(theta)=sum_{j=0}^{29} w_j B_j(theta)`, where `B_j` are the fixed smooth periodic bump functions defined in paper §1 | frozen |
| Base map | `g(theta,x,y)=(theta+1/30, y, -x+a(theta)y^2)` | frozen |
| Symplectic map | `F=T*g` | frozen |
| Roof / flow | `tau=1`; mapping torus suspension of `F` | frozen |
| Arithmetic mechanism | periodic 30-wheel word only | frozen as adverse control |
| Orbit convention | primitive periodic points of `F`; zero covector over `(theta,0,0)` | frozen locally |
| Zeta/operator | `OPEN`; deliberately not attached | OPEN |
| Route state | A0 fails; no Route-A tuple; B not invoked | frozen |

The cotangent lift is symplectic by construction. The mapping torus is not
thereby asserted to be symplectic or Hamiltonian.
