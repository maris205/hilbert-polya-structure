# HCS-C84 minimum-repair matroid and basis-exchange atlas

C84 upgrades C79's witness multiplicities to a maskwise structural theorem.
For every deletion set `D`, the minimum restoration witnesses are exactly the
bases of a direct sum of loops, an optional pivot coloop, and the rank
`max(0,t(D)-2)` truncation of the partition matroid on the fully deleted
direction blocks.

Independent C75 point-set closure enumeration verifies this statement and
basis exchange for all `65536` deletion sets.  The ten `(rho,W)` cells collapse
to five unlabeled exchange graphs:

| graph | deletion-set count | vertices | edges | diameter | degree spectrum |
|---|---:|---:|---:|---:|---|
| `K1` | 60800 | 1 | 0 | 0 | `{0:1}` |
| `K4` | 3968 | 4 | 6 | 1 | `{3:4}` |
| `K7` | 384 | 7 | 21 | 1 | `{6:7}` |
| `K8` | 256 | 8 | 28 | 1 | `{7:8}` |
| `L(K_{1,1,2,5})` | 128 | 25 | 128 | 2 | `{9:10,10:10,13:4,14:1}` |

For `D=L`, the 25 bases are exactly C76's 25 full-core-minimal triples.  Their
exchange graph has radius 2 and unordered pair-distance counts `{1:128,2:172}`.
Across all masks the package checks `198912` ordered basis-exchange obligations.

The canonical evidence SHA-256 is
`9c3b20c703b680a391ad1834c0f55cabaf27bfed14cee2099b0c3afa1eb259ca`.
The complete file binding is recorded in
[C84_PREFREEZE_MANIFEST.json](C84_PREFREEZE_MANIFEST.json).

This is a finite named-support theorem only.  It makes no arithmetic/local,
Euler-factor, root-number, automorphy, full Burnside/table-of-marks, or
Hilbert--Polya claim.  Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.
