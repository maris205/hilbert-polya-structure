# Route Record and Seal Census

## Read-only authority state

A fresh read-only replay on 2026-08-18 observed:

$$
\begin{aligned}
\text{authority commit}
&=6e5658649d2eab0fce077cbcdcc00070dd54095f,\\
\text{authority status}
&=\text{clean},\\
\text{writes by this task}&=0,\\
\text{mutating Git operations}&=0.
\end{aligned}
$$

## Integrated Route records

The canonical universe is every accepted Route evaluation YAML matching
papers/*/evaluations/route_a/SD-C*/*.yaml under the read-only authority
tree. Paths are repository-relative POSIX paths and are sorted with
LC_ALL=C.

| Quantity | Value |
|---|---|
| record count | 46 |
| C-sorted newline-terminated path-list SHA-256 | bc0be20cc32c7326a706bac960c9906f20fc976a4c451dcd4f0361d80f7ac078 |
| C-sorted path-order sha256sum-stream SHA-256 | a2eb6e16c698242a3af32ae400729ab26f23717caa8f2f0c5400993ba7bc940b |
| last path | papers/43-squarefree-factor-periodic-rigidity/evaluations/route_a/SD-C45/2026-08-17.yaml |
| last record SHA-256 | 1918b6abe3c2c56bc0bf32388d25b593e0d87645e18f47b063380586e42c62dc |

The second digest hashes the newline-terminated output of sha256sum applied
to each file in the first list's order from the authority repository root.

## Candidate boundary

Proposed Papers 44–48, including SD-C50, are not integrated Route records
and are not included in the count. ROUTE_EXPECTATION.yaml is an expectation,
not an accepted evaluation. It supplies no ranking or authorization.

The active Phase-2 parent manifest has SHA-256
d035310ac046981abe7a37a033b1354e3d8da3f53f33d631786ed80f40b90181.
That parent selects five preauthority theory units with firewalls; it does
not alter the integrated Route census.

## Replay recipe

From the authority repository root:

1. enumerate the canonical glob with find;
2. sort repository-relative paths under LC_ALL=C;
3. count newline-terminated paths and hash that list;
4. run sha256sum on each path in list order and hash the resulting stream;
5. verify the final path and its file digest;
6. verify Git status without writing.

Any change in commit, status, path universe, count, or digest requires a
fresh census before integration can be considered.

