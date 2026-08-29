# C233 hostile audit

The mutation suite attacks source/evaluator locks, route and scope claims,
rate/mode/kernel/trace cells, and nested/top-level schema.  Repaired-hash
mutations must fail semantic checks; a stale-hash mutation must fail byte
integrity.  Counts are frozen in the release manifest.
