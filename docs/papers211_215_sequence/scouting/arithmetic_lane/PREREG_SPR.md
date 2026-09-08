# SPR sole finite pilot preregistration

Author/pre-run declaration: `/root/round211_arithmetic_scout`, 2026-09-08.
This file and the completed SPR proof precede every scientific invocation.
The lane uses exactly **one** invocation, never a rescue/replay/expanded box.

## Fixed scope

- Literal: labelled `{0,...,M}^n`; support <= 1 is fixed; otherwise every
  coordinate is replaced by its remainder modulo the second-smallest
  positive entry, counting multiplicities. No map variation is tested.
- All 35 boxes: `n = 1,2,3,4,5`, `M = 0,1,2,3,4,5,6`, in that order.
- Standard-library CPU only; subprocess wall limit 60 seconds, CPU soft
  limit 55 seconds, address-space limit 512 MiB; no external scientific
  dependency, randomness, network, GPU, fitting or optimized cutoff.
- On assertion failure, timeout, crash or receipt mismatch: preserve the
  failure and close/downgrade the claim. No second scientific invocation.

## Predeclared checks

1. Independently represented literal maps: positive-value sorting versus
   scanning a value histogram to locate its second positive occurrence.
2. Every state: image in carrier; fixed iff support <= 1; strict support
   loss otherwise; orbit traversal yields height and terminal fixed state.
3. Every state of height >= t: every largest partial sum dominates `c[t]`.
   Every eligible nonfixed predecessor also checks Lemma 1 of the proof.
4. Every box: observed maximum height equals the prewritten additive reverse
   recurrence threshold; an attaining tuple fits and has the stated height.
5. Every target, including empty fibres: brute incoming degree equals the
   full pivot/quotient formula; every actual source uniquely satisfies the
   stated inverse-case decoder. Total incoming degree equals carrier size.
6. Every box: full fibre histogram; unique zero maximum for n >= 2, M >= 1;
   exact stated maximum formula; identity boundary cases checked separately.

`c[t]` is constructed only as far as t <= 4 is needed for these boxes. There
is no numerical extrapolation of the sequence or a claim beyond the boxes.
The all-parameter theorem stands or falls on the separate proof.

## Output and evidence model

The child emits a complete compact canonical JSONL transcript: one row per
box with all height/fibre histograms, deterministic first maximum-height
witness, full maximum-fibre target list and SHA-256 commitment to the full
canonical per-state records. Each record contains `[x,T(x),h(x),indegree(x)]`
in lexicographic state order. Those records are retained in
`sole_pilot/state_records.jsonl.gz` with deterministic gzip timestamp zero;
thus the compact transcript does not stand in for missing enumerated data.
The final row pins imported module files and executable mappings visible
at that point. The wrapper retains complete native stdout/stderr and return
status, before/after explicit input hashes, executable pin, explicit child
environment, resource limits, output pins, time and command. The invocation
uses `-I -S -B`; no site customization or implicit current-directory import.

This is **not hermetic dependency closure**: frozen/builtin modules reside
in the pinned interpreter; interpreter transitive runtime files may be
read without remaining imported/mapped; dynamic loader/OS/kernel/CPU state,
tool-host execution and external network source acquisition are not fully
traced or pinned. `/proc/self/maps` and `sys.modules` are a disclosed bounded
runtime surface, not proof that no other input was accessed. Historical
proof/source files affect author interpretation, not numerical execution.
No strict scientific reuse, independent replication or independent review
is claimed. The script and wrapper are author code.

## Before-pilot source disposition

No exact old SPR literal was found in the bounded actual-original review.
CPRM preserves gcd and retains a divisor; P174 uses finite-field projective
Möbius inversion; the P210 partition clock uses insertion births. Brun
rank-selected remainder primitives and classical reverse-smallest-input
worst-case methods are known and receive no standalone novelty credit.
Lam--Shallit--Vanstone's full worst-case proof is not retrieved; that is an
explicit residual source/value-review question, not a cleared source.
SPR's proposed residuals are the changing-support weak-majorization theorem
and the all-target quotient decoder plus strict extremal fibre comparison.
This permits one pressure check, not admission or a paper number.
