# Exact-evidence plan

## Purpose

The executable layer checks indexing, normalization, finite-state balance
identities, and release integrity. It is not the proof of positive recurrence,
necessity, or the process-level external-departure theorem.

## Frozen panel

- Twelve rational networks: three each in dimensions \(1,2,3,4\).
- Positive rational external rates at every node.
- Routing panels include zero routing, feedback, tandem routing, cycles,
  self-routing, and nodes with no direct exit.
- Each panel carries a rational power-contraction certificate for
  \(\rho(P)<1\).
- Service rates are rational and strictly exceed the exact traffic rates.

## Exact receipts

- network_rows: 12 traffic, load, normalization, and routing certificates.
- balance_rows: every state in \(\{0,1,2,3\}^d\), hence
  \(3(4+4^2+4^3+4^4)=1,020\) exact global-balance rows.
- reverse_network_rows: 12 complete reversed parameter systems.
- reverse_jump_rows: 84 visible external-arrival, external-departure, and
  routed-service identities. They deliberately omit state-preserving phantom
  self-routing marks and allow zero reverse exogenous rates.
- boundary_rows: 6 named faces.

The producer solves traffic equations by exact Gauss--Jordan elimination. The
checker independently uses Cramer's rule, reconstructs every coordinate set,
and recomputes all rows. A separate SymPy lane checks symbolic traffic,
reverse-rate, global-balance, and one-node-feedback identities. Replay uses two
isolated temporary directories. Hostile tests repair outer payload hashes
after semantic corruption and attack strict JSON/YAML parsing.

## Acceptance gates

1. Producer, independent checker, SymPy lane, byte replay, and every hostile
   mutation pass under ordinary Python.
2. Each Python lane explicitly refuses both -O and -OO.
3. The evaluation YAML is bound by raw-byte and canonical semantic hashes.
4. Three substantively increasing PDF rounds are reproduced byte-for-byte in
   two fresh directories per round under the fixed epoch.
5. Settled logs have no warning, overfull/underfull box, undefined item,
   rerun request, or missing glyph; every font is embedded and subset.
6. The manifest closes exactly 27 payload files and 28 physical files including
   its self-excluded ledger.
