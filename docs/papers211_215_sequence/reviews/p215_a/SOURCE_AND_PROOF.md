# P215 manuscript Review A: source and proof audit

2026-09-11 UTC. Complete physical Round0 manuscript, proof package, source
audit, source records, verifier design and author verifier were read.

The reflection identity is correct. After zero differences are removed, the
first positive input run produces no output run; each negative run produces
one nonempty positive output run; each later positive run begins above zero
and produces one nonempty negative run even if it subsequently saturates.
The separators prevent merging. Hence exactly one sign run disappears per
update, including plateau and saturation cases. This proves the pointwise
clock, unique recurrence, sharp height and full alternating equality set,
with `n=0` and `q=0` correctly separated.

For a target beginning with zero, the source running maximum can change only
at target-zero positions and is constant between them. Nondecreasing record
heights above the prefix block barriers give every source uniquely. The
converse checks both prior blocks and strict within-block inequalities. The
reverse-complement ceiling sequence is nondecreasing. In the recurrence,
first violation cannot occur at `m` because the ambient count already bounds
the last coordinate by `c_m`; for `i<m`, valid prefix and suffix concatenate
without an omitted boundary. Empty prefixes and empty words are explicit.
The image, maximum fibre and uniqueness proof are strict for `n,q>0`, while
singleton cases are handled separately.

The two bibliography records match the stated metadata and are used narrowly:
classical drawdown background and classical barrier enumeration. No stochastic
theorem, priority, arbitrary-poset extension, all-time inverse or universal
no-factor statement is inferred. Author lookup limitations remain disclosed.

Independent `verify.py` uses reverse BFS over the complete functional graph,
not per-source author orbit walks. Its inverse is a coordinate automaton over
the current record maximum, not the author's zero-block height enumeration.
It separately evaluates the displayed first-violation recurrence. Fixed box:
`0<=n<=6`, `0<=q<=4`, 35 carriers and 26,219 states. It has not been parsed,
imported, compiled or executed.

Current examined census: Critical 0, Major 0, Minor 0. All execution, build,
final verdict and freeze gates remain pending. OWNER_AMBER / HOLD_EXTERNAL.
