#!/usr/bin/env python3
"""SOURCE-ONLY terminal dependency derivation contract; no operational discovery.

This file is deliberately non-executable as a selector. Root reads all five
fresh sources and the entire actual original lock, rechecks its full current
host/configuration key, and writes a separately owned root-bound derived lock.

Exact derivation, independently enforced by build_p211.binding_inputs:
  retain every original key/value, including sources, entries, selector specs,
  reasons, queries, query commands, all ldd inputs and relative absence roles;
  replace schema, status and code_observations with the exact terminal roles;
  add terminal_derivation naming original 570037-byte lock and four allowed
  changed fields. Never learn or extend the key from a failed terminal build.

A changed source, host candidate, optional class config, library, module,
font/config member, or non-FLS input requires a new scoped root decision and
fresh inspected selector; this source has no such discovery fallback.
No program in this preparation package has been invoked.
"""

if __name__ == '__main__':
    raise SystemExit('SOURCE_ONLY_NO_DISCOVERY_AUTHORIZATION: root-owned exact binding required')
