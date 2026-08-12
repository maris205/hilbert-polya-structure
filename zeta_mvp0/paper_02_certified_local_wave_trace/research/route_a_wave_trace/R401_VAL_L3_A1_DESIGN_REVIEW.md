# R401-VAL-L3-A1 independent design review

Review date: 2026-08-09 UTC

Review scope: prospective all-slab implementation design only

Reviewed design: `R401_VAL_L3_A1_PREFREEZE_DESIGN.md`
Reviewed design SHA-256: `b711fbc61e10c9867058de38a1cd5d38bd69182c584890cbf5dcb69278143d62`

## 1. Independence and authority boundary

This is the independent read-only review of the prospective L3-A1 design.
The review compared the final design bytes against the accepted L2-A1
transaction, checker, freeze, and release architecture; the A4.16
phase-anchor derivation; and the accepted representative L3 S0 component and
composite evidence.

The reviewer did not modify the design, tracker, evaluator, scheduler,
checker, test, result, or release files during the review. No representative,
held-out, or all-slab evaluator was invoked. This record authorizes only the
next implementation-and-mock-testing stage described below. It is not a
formal pre-freeze review and is not a scientific result.

## 2. Blocker assessment

```text
P0 blockers = 0
P1 blockers = 0
P2 documentation notes = 3
```

No remaining design-level defect can currently promote an incomplete matrix,
mix the two components, bypass the provenance graph, convert a resource stop
into a theorem, or widen the A4.16 mathematical claim.

## 3. Accepted design properties

The reviewed bytes close the following design obligations.

1. The canonical experiment has exactly 102 composite cells in the order
   `128:S000..S050`, then `256:S000..S050`. Each cell contains one static
   phase-anchor obligation and one continuous branch-tube obligation, for 204
   component evaluations in total.
2. Static and branch archives have separate cell namespaces, aggregates,
   independent checkers, and write-once postchecks. Neither component can
   substitute for a missing partner. Only the composite checker owns
   `PASS_LOCAL_PHASE_TUBE_ALL_SLABS`.
3. The noncircular provenance graph binds the accepted L1 five-object chain,
   the accepted A4.15/L2-A1 five-object chain, the A4.16 derivation, the exact
   S0 compatibility object, formal code and contracts, machine evidence,
   pre-freeze tests and review, a last-generated main freeze, the sealed run
   configuration, both 102-cell archives, three checker/postcheck layers, the
   report, and a no-self-hash release object.
4. The static status vocabulary cannot report a scientific gate violation
   merely because an interval permits a bad value. Without a separately
   checked constrained existence witness on `K=1` in the slow tube, such a
   cell remains unresolved.
5. Branch stdout, stderr, record, and total-cell output are prospectively
   bounded and streamed into staging files. Output exhaustion, timeout, or a
   signal terminates the complete process group and produces a non-passing
   scheduler classification with no forged evaluator status.
6. Resume is derived from validated cell manifests. A manifest-less canonical
   directory is not a committed pass; corrupted or binding-incompatible
   generations are quarantined as complete recoverable units and are never
   mixed with a new generation.
7. Interrupted staging is confined to the exact operational sibling
   namespace, with a frozen naming grammar, the same `st_dev` as the
   authoritative target, and one active owner per cell. Hidden or extra paths
   beneath the authoritative root are rejected.
8. The read-only S0 compatibility object binds the exact six-cell matrix,
   static totals `84172/42074/42098/0`, 122300 independent checks, six branch
   raw replays, the 26-file branch role set, six composite cells, 18 composite
   bindings, zero failures, and the nine sealed component/control hashes. It
   cannot invoke an evaluator or modify an S0 byte.
9. Machine and resource admission prospectively bind the 32-CPU execution
   view, 60-GiB cgroup limit, Python/Arb chain, CAPD checkout/build, persistent
   binary, compiler and runtime libraries, peak-RSS calibration, sequential
   worker pools, and operational disk/memory barriers. Resource exhaustion is
   inconclusive rather than a negative theorem.
10. The complete mocked 102-static plus 102-branch test, fault injection,
    path/type/TOCTOU tests, compatibility replay, release tests, independent
    pre-freeze review, main freeze, initialize-only handshake, and later
    explicit production authorization all remain mandatory before held-out
    dispatch.

## 4. Mathematical and programme boundary

The prospective all-slab statement remains explicitly conditional: an
energy-one periodic candidate with period in `[0.64,0.69]` is identified with
the accepted branch modulo time translation only if its complete trajectory
stays in `r_minus < 0.06`. The separate branch obligation places the accepted
branch itself in `r_minus < 0.04`.

The design does not place arbitrary energy-shell candidates inside that tube.
It does not establish global orbit uniqueness, global tube routing, the
event-projected determinant, Taylor residual, `delta_tr`, `P0`, a trace
formula, a prime-orbit identity, a Hilbert--Polya operator, zeta-zero
reconstruction, RH, or an implication toward RH. The final programme status
remains null.

## 5. Non-blocking P2 notes

1. The supplemental tracker should mirror the design's new branch output
   caps and the 8-GiB memory reserve in its candidate-budget table.
2. After this review record is bound by the repository workflow, the planning
   tracker may mark the independent design review complete. This does not
   satisfy the later formal independent pre-freeze review gate.
3. The formal protocol and release contract must freeze the precise
   cross-precision rule---identical exact root domains and final verdicts,
   without requiring identical adaptive tree partitions---and an exact
   release role map and role count.

## 6. Decision

The design is sufficiently fail-closed and concrete to implement the formal
cell evaluators, transactional scheduler, independent component and composite
checkers, S0 adapter, release builder, and mocked/fault-test suite.

This decision is not `ACCEPT_FOR_FREEZE`. It does not authorize
representative resource calibration, representative evaluator reruns,
held-out execution, or all-slab production. The formal protocol and
contracts, implementation, complete tests, L3 machine freeze, formal
independent pre-freeze review, main freeze, initialize-only audit, and an
explicit later production instruction are still required.

Verdict: ACCEPT_FOR_IMPLEMENTATION_DESIGN
