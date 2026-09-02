# Executable certificate

All scripts use Python’s exact `Fraction` arithmetic for finite cells. The
producer and checker share no imports.

## Components

- `c285_gordon_newell_producer.py` solves rational traffic equations, emits
  all selected finite states, three `Z_N` routes, moments, flows, reversals,
  condensation cells and the canonical payload hash.
- `c285_gordon_newell_checker.py` rejects duplicate JSON keys, unknown or
  missing schema keys, inexact JSON types, Boolean-as-integer substitutions,
  and noncanonical rational strings; independently solves traffic equations, builds every
  Fraction row-generator, computes the full RREF left nullspace, and
  reconstructs every evidence cell.
- `c285_gordon_newell_sympy_crosscheck.py` proves 28 separate symbolic
  generating, Newton, Euler/covariance, global-balance, reversal and
  equal-weight identities.
- `c285_gordon_newell_replay.py` produces the receipt in two unrelated fresh
  paths, runs the independent checker on each, and requires byte identity
  with the archived receipt.
- `c285_gordon_newell_mutation.py` exercises 64 hostile trials, including 60
  repaired-hash semantic/schema/type attacks, a row-count-preserving
  condensation drop/replace, a stale payload hash, and raw top-level plus
  nested duplicate JSON keys.
- `c285_release_manifest.py` reruns all gates, validates the unique Route-A
  carrier, builds every revision twice from fresh directories, audits PDF
  logs/fonts/text/rendering, and writes the self-excluded release manifest.

## Semantics that must not be merged

Self-routing completions count in the directed event-flow matrix but create no
off-diagonal generator transition. At `N=0`, the state chain is a reversible
singleton regardless of `P`, so routing detailed balance is not inferred from
that face. A routing entry may be zero inside an irreducible matrix; a service
rate or canonical weight may not be zero inside the frozen theorem.

The finite evidence does not prove the all-network or thermodynamic theorem.
It is a deterministic falsification and release layer for the written proof.
