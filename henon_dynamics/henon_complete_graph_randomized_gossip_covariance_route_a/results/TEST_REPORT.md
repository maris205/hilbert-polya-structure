# Test report

Commands are run from the package root.

| Lane | Command | Result |
|---|---|---|
| producer | `PYTHONDONTWRITEBYTECODE=1 python -B code/c333_gossip_producer.py` | PASS; 56 spectral rows, 48 word rows, 2,966 leaves |
| independent checker | `PYTHONDONTWRITEBYTECODE=1 python -B code/c333_gossip_checker.py` | PASS; 1,392 checks |
| symbolic | `PYTHONDONTWRITEBYTECODE=1 python -B code/c333_gossip_sympy_crosscheck.py` | PASS; 350 exact identities |
| byte replay | `PYTHONDONTWRITEBYTECODE=1 python -B code/c333_gossip_replay.py` | PASS; two isolated outputs equal checked-in evidence |
| hostile mutation | `PYTHONDONTWRITEBYTECODE=1 python -B code/c333_gossip_mutation.py` | PASS; 140/140 attacks rejected |

Every Python entry point is also invoked with
`PYTHONDONTWRITEBYTECODE=1 python -O -B` and must fail
with its explicit optimized-execution refusal.  The release gate additionally
checks strict JSON/YAML parsing, evaluator authority, every gate's
`evidence_status`, raw and semantic YAML hashes, the canonical self-excluding
evidence payload hash, exact file closure, deterministic PDF rebuilds,
extracted text, rasterization, and embedded/subset fonts.

The checker imports no producer code.  It independently enumerates every
declared edge word and directly reconstructs the second-moment transfer.
