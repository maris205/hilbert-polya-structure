# C80 hostile mutation audit

The harness mutates schema, status, scope, predecessor hashes, target order
metadata, profile masks and thresholds, the full-core distribution/table, a
gate flag, and a nonclaim flag.  The independent checker rejects all 13/13
mutations.
