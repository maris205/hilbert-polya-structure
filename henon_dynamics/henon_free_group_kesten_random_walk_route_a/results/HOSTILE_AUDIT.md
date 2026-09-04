# Hostile audit

The hostile lane performs 74 attacks.  It recomputes the self-excluding JSON payload hash after semantic changes, so rejection cannot rely on a stale digest alone.

Direct semantic attacks cover identity/date/epoch/source/scope; evaluator authority and hash; YAML relative path and digests; model normalization; spectral, return, and escape contracts; collision and nonclaim language; source identifiers; Route-A tuple/overall/Route-B lock; firewall flags; every evidence section; and the finite-evidence boundary.

For each of the six row sections, separate attacks add an unowned nested key, omit a row, and duplicate a row.  Parser attacks cover duplicate and nonfinite JSON, JSON root type, YAML duplicate/anchor/alias/merge/non-string keys, implicit timestamp spelling, scalar type changes, unknown keys, and YAML root type.  Result: `74/74 PASS`.
