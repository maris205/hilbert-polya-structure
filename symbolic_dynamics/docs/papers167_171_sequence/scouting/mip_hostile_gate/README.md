# MIP independent hostile gate

This directory is the isolated pre-paper gate for the self-map

```text
M(f)(i)=min {j:f(j)=i}, with M(f)(i)=i when i is absent,
```

on all endofunctions `[n]^[n]`.

## Decision

`GREEN_OWNER_THIN / ELIGIBLE_FOR_INTERNAL_PAPER_SLOT / HOLD_EXTERNAL`.

The theorem package passed without correction.  The gate does not make a
worldwide novelty or priority claim.

## Files

- `HOSTILE_GATE.md`: decision, claim matrix, exact results, and limits;
- `PROOF_REDERIVATION.md`: self-contained derivation from the literal map;
- `OWNER_SEARCH.md`: bounded primary-source search and owner subtraction;
- `INTERNAL_COLLISION_AUDIT.md`: complete P1--P166 range audit and focused
  near-neighbor comparisons;
- `verify_mip_gate.py`: independent standard-library falsifier;
- `CANONICAL.json`: frozen deterministic stdout;
- `REPLAY_LOG.md`: two byte-identical final replays; and
- `SHA256SUMS`: local integrity manifest.

## Reproduce

From this directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_mip_gate.py > /tmp/mip_gate.json
cmp -s CANONICAL.json /tmp/mip_gate.json
```

Expected terminal facts:

```text
assertions:       12,603,676
verifier SHA-256: acb630523348a26f90a37aac45d9e17e33db13addfe0fc7aab1c71e9f4ab56e0
stdout SHA-256:   d566ede8a559273ec25757c7dcf7dd6f8bbd7ef15cc855f2a38a974a2d4f5b8f
```
