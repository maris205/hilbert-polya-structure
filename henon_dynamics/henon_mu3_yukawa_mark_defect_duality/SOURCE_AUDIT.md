# C68 source audit

The producer binds exact bytes before any new calculation:

| Source | Role |
|---|---|
| C64 mark evidence | frozen 16-by-16 integer matrix `M` |
| C65 defect evidence | kernel vectors and saturation vectors `u_i` |
| C66 cokernel evidence | upstream Smith invariants |
| C67 coordinate evidence | predecessor-chain compatibility |

All sources carry the literal scope firewall `NO_BAD_EULER_OR_ROOT_NUMBER`.
The C68 claim is limited to finite integral lattices on this named 16-type
support.
