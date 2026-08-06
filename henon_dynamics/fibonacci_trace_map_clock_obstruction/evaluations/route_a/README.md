# Route-A evaluation record migration

Route-A records are append-only. Historical YAML files remain in place for
provenance, but readers must use the authoritative mapping below rather than
selecting a record solely by directory name or lexicographic timestamp. The
workspace is not a Git worktree, so the authoritative records explicitly set
`source_commit: NOT_TESTABLE` and freeze provenance through their object locks
and artifact paths instead of inventing a commit hash.

| Candidate | Record | Status | Reason |
|---|---|---|---|
| HCS-C13 | `hcs_c13/20260806T000000Z.yaml` | Historical, non-authoritative | Uses evidence labels outside the Route-A 0.1.0 enumeration. |
| HCS-C13-AM | `hcs_c13/20260806T170000Z.yaml` | Superseded, non-authoritative | Stored under the wrong candidate directory and mixes evidence from separately scoped repair/obstruction candidates. |
| HCS-C13-AM | `hcs_c13_am/20260806T172500Z.yaml` | **Authoritative** | Freezes the unweighted ten-state Artin--Mazur object at `lambda=16`, the literal identity \(\operatorname{tr}(A_{10}^k)=d_k(E)\), source provenance, clocks, exact determinant convention, and no-data split. |
| HCS-C13R | `hcs_c13r/20260806T170000Z.yaml` | Superseded, non-authoritative | Earlier draft of the missing-input assessment. |
| HCS-C13R | `hcs_c13r/20260806T172500Z.yaml` | **Authoritative input gate** | Minimal `NOT_TESTABLE` record with no A1--A4 scores: no repair computation is authorized until the full operator tuple and data split are frozen. |

The candidate boundaries are strict. HCS-C13-AM is only the fixed unweighted
closed-orbit zeta. HCS-C13B (marked boundary paths), HCS-C13P
(dimension-independent bounded-degree passive-parameter repairs), and HCS-C13G
(zero-radius analytic-germ obstructions) are different mathematical claims and
their artifacts cannot be used as evidence
for HCS-C13-AM. HCS-C13R is an unspecified infinite-dimensional repair proposal,
not a continuation of HCS-C13-AM under a changed object definition.

Any future evaluation of HCS-C13B, HCS-C13P, or HCS-C13G must be appended under
its own normalized candidate directory with a fresh source lock. Existing files
must not be overwritten merely to make old schema or labels conform.
