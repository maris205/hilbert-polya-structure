# C78 code map

The release is split into independent gates:

- `c78_repair_distance_geometry.py` binds C73/C75/C76/C77 and produces the
  canonical exact certificate;
- `c78_repair_distance_geometry_checker.py` reconstructs the named closure,
  derives minimum repairs independently, and checks the bivariate identity;
- `c78_sympy_crosscheck.py` verifies the generating-function transformation;
- `c78_repair_distance_geometry_replay_checker.py` runs the checker in a
  clean process;
- `c78_mutation_test.py` applies semantic JSON mutations and requires every
  one to be rejected.

The convention is fixed: `D` is the deleted set, `A=L\\D` is retained,
`x` marks `|D|`, and `y` marks
`rho(D)=min{|R|: R subset D and Phi(A union R)=Q}`.  The structural check uses
the pivot `S9` and projective direction blocks
`[S1]`, `[S16]`, `[S7,S15]`, `[S3,S4,S8,S11,S12]`; six dummy labels contribute
the factor `(1+x)^6`.

Run from this directory with `python3`.  The canonical evidence is
`results/c78_repair_distance_geometry_evidence.json` and has SHA-256
`728d6462b337e3b22fe267ae9388da476a0f6409cc64a17ca659f53f1a8126ae`.
The committed C76 manifest authority is
`55725664005113ae993b54197ff4fbd97bde347ce49aa69ea0c228372ba289d5`, and the
committed C77 manifest authority is
`bcc3273b481123f89ed5bf10c216bcae7a2ac3ff77685edcba976ea959e84dbc`.
All scripts preserve the literal scope firewall
`NO_BAD_EULER_OR_ROOT_NUMBER`.
