# C67 source audit

The producer binds exact source bytes:

| input | SHA-256 |
|---|---|
| C64 mark evidence | `7c4673e46f2b97ac03d4e331c762a47286058c36ea243fb20fc39543dd699212` |
| C64 prefreeze manifest | `eb1d6a55cb81ccfc9b3041879cb913367a514f5c4cba50872d8b286c0ac095b6` |
| C66 mark-SNF evidence | `ce74edeec04b245637e5b12165a7fcdeb42475b0dead7373b1bcf3e37f22beb1` |
| C66 prefreeze manifest | `aa9a750fd87cfd09948167e0af93145823dff7d34c7bdb1ed13d1a8df493c626` |

The C64 matrix digest is
`4e57d980e774e14709d60feac0fff5af831b6496409d248f398a8a3e2796c307`.
Schema IDs, prefreeze statuses, matrix shape, determinant, and the literal
`NO_BAD_EULER_OR_ROOT_NUMBER` are checked before inversion. C66 is used only
for its already certified upstream SNF compatibility.
