# Paper 41 Phase-1 preauthority package

Proposed candidate: `SD-C43` (identifier supplied by the commissioning task;
authority allocation remains an integrator decision).

Working title: **Rooted Clocks Do Not Make Cycles: Exact Non-Descent in the
Knauf Binary Recursion**.

Status: `CORRECTED_INPUTS_FROZEN_FOR_INDEPENDENT_DA`, not authority, not a
preregistered experiment, not a Paper-41 repository integration.  The
corrected package bytes are frozen before independent DA only.

## Outcome first

The retrospective Boolean rule in `SELECTION_AND_PROVENANCE.md` returns the
unique Session-4 card `SD-C06`.  The rule was constructed after the six cards,
their results, and the exact witnesses were known.  “Independent” means only
independent of P39 ranking and P40 authorization; this package claims no
prospective, outcome-independent, or priority-bearing selection.  The
source-owned positive result is kept intact:

\[
  \lim_{k\to\infty} Z_k(s)
  =\sum_{n\ge 1}\varphi(n)n^{-s}
  =\frac{\zeta(s-1)}{\zeta(s)},\qquad \Re s>2.
\]

The new, deliberately narrow target is not another assertion that a partition
function is not automatically a determinant.  It is an exact non-descent
theorem for the frozen rooted clock

\[
 h(w)=\mathbf 1^{\mathsf T}M_w e_1,
 \quad
 L=\begin{pmatrix}1&1\\0&1\end{pmatrix},\quad
 R=\begin{pmatrix}1&0\\1&1\end{pmatrix}.
\]

Four source-local witnesses settle the smallest historical test:

1. the direct-limit identification `w ~ w0` is not a right congruence for
   appending `1`: `epsilon ~ 0`, but `h(1)=2` and `h(01)=3`;
2. the clock does not descend to binary necklaces:
   `h(01)=3 != 2=h(10)`;
3. temporal powers fail for that clock: `h(11)=3 != 4=h(1)^2`;
4. the added Liouville phase is neither cyclic nor a repetition character:
   `lambda(h(001))=+1 != -1=lambda(h(010))`, while
   `lambda(h(11))=-1 != (+1)=lambda(h(1))^2`.

Thus the exact rooted `h`-object supplies neither the canonical
primitive/repetition ledger requested by the `SD-C06` Route card nor an
endogenous scalar orbit sign.  Replacing `h` by a matrix trace or expanding
the state space is a changed object and does not repair `SD-C06` in place.

Expected strict Route tuple:

```text
(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_FAIL,
 A2_FAIL,
 A3_PARTIAL_ANALYTIC_STRUCTURE,
 A4_FAIL)

overall: ROUTE_A_REJECTED
route_b_invocation_allowed: false
```

## Package map

- `RESEARCH_QUESTION_BRIEF.md` — FINER question and bounded claim.
- `METHODOLOGY_BLUEPRINT.md` — evidence hierarchy and DA workflow.
- `SELECTION_AND_PROVENANCE.md` — retrospective six-card selector and the
  P39/P40 governance-independence firewall.
- `SOURCE_LOCK.md` — exact source bytes, admissible operations, and forbidden
  substitutions.
- `OBJECT_MARKER_OPERATOR_CONTRACT.md` — typed object, marker, operator, and
  determinant ledger.
- `DERIVATION_PACKAGE.md` — formula derivation with dimensions and domains.
- `PROOF_PACKAGE.md` — theorem statements and complete finite-witness proofs.
- `THEOREM_FALSIFIERS.md` — theorem-by-theorem defeat conditions.
- `LITERATURE_NOVELTY_AUDIT.md` — primary-source collision matrix and search
  log through 2026-08-17.
- `ROUTE_RECORD_CENSUS.md` — audit of all 42 integrated Route YAML records
  through terminal Paper 39, plus the separately sealed Paper-40 research
  record.
- `ROUTE_EXPECTATION.yaml` — retrospective corrected strict Route expectation
  for independent preauthority review.
- `DA_HANDOFF.md` — independent devil's-advocate questions and acceptance
  gates.
- `SOURCE_HASHES.sha256` — portable `repo:`/`dependency:` source-ID hashes;
  resolution is fixed by `SOURCE_LOCK.md` and has no sealed host path.
- `RESEARCH_LOCK.json`, `SHA256SUMS.txt` — self-excluding package seals.

## Authority boundary

The portable package namespace is
`papers/41-knauf-rooted-clock-non-descent/preauthority` relative to the
`symbolic_dynamics` root; its staging location is deliberately not sealed.
No authority tree, mirror, Git state, root README, paper manifest, or
candidate registry was modified.  This package cannot rank or authorize
itself; an independent DA and the root integrator must act before any
authority write.  The selection narrative is retrospective; only the final
corrected input bytes, not the selector or witness discovery, precede
independent DA.
