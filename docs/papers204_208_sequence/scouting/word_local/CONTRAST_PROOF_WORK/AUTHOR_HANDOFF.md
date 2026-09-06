# MNC author handoff — mathematical package closed

2026-09-06 UTC. **PROVABLE AS STATED / AWAIT_INDEPENDENT_CANDIDATE_GATE**.
No paper number, source/owner clearance, manuscript review or admission.
MNC and MDE count as at most one contrast-family candidate. HOLD_EXTERNAL.

## Deliverable

`PROOF_PACKAGE.md` contains all-$n$ deductions for the literal ternary
cyclic rule $F_i=\min(|x_i-x_{i-1}|,|x_i-x_{i+1}|)$, $n\ge3$:

- $F^4=F^3$, exact colored singleton-pulse fixed set, no nonfixed cycles;
  sharp entrance two at $n=3,4$ and three at every $n\ge5$.
- A complete target-resolved inverse-set decoder with evaluated edge-word
  weights. This is a **zero-credit generic static construction**.
- Unique maximum target $0^n$ at every $n\ge4$, value
  $2^n+(-1)^n+4\cos(n\pi/3)$; at $n=3$ the unique maximum target is
  $111$, with its six sources explicitly identified. The zero-fibre count
  alone is zero-credit; the case-complete all-target comparison is the
  residual presented to the gate.

`SOURCE_BOUNDARY.md` gives the actual primary reading scope and complete
generic adapters, including ECA 36, Jen's endpoint recurrences and
maximal-probability discussion, and the general cyclic preimage-network
algorithm. Read scopes there denote only the specified sections of the
downloaded full PDFs, not an assertion that every page was read. Searches
and failed direct adapters do not certify novelty. The separate reviewer
may legitimately kill the proposed residual as routine or duplicated.

Main author: `batch197_lzk_gate`. Root independently contributed the
distance-word lemma and is a mathematical co-contributor. Neither may
provide an independent MNC manuscript review. No other author's verifier,
historical checker, canonical data or runtime imports enter `verify_mnc.py`.
The root distance proof was read only after the corresponding author
derivation existed; it is disclosed and pinned as proof context.

## Actual verification and bounds

The initially generated `CANONICAL.json` is complete stdout, 9,733 bytes.
Two **new** complete executions of `verify_mnc.py` were run by
`python3 -B replay_author.py author_pair_01`. The harness does not import
the producer. Both child exits and both actual `cmp` exits were zero;
each run executed **356,509 assertions**, and all five pinned inputs
were unchanged before/after. Exact commands, Python/runtime settings,
input hashes, byte counts and exits are in `author_pair_01/receipt.json`.
Both full raw stdout files and all empty stderr/comparator streams remain
present. These are author checks, not independent review evidence.

| Scope | Exact coverage |
|---|---|
| Full labeled cyclic sources, targets, distance words | $n=3,\ldots,9$, matching the predeclared intake cutoff |
| Complete inverse source sets, not just cardinalities | Every target at $n=3,\ldots,7$ |
| Relaxed singleton sets | Every binary mask at $n=3,\ldots,9$ |
| Endpoint-color block matrices | Every local source block of lengths $2,\ldots,8$ |
| Universal radius-four identity pressure | All $3^9$ local nine-symbol windows; not a larger cyclic pilot |
| Deducted ECA 36 local identity | All $2^7$ local binary seven-symbol windows |
| Scalar inequalities and explicit witnesses only | Lengths $4,\ldots,64$, not full cyclic state boxes |

Finite checks pressure the proof but do not establish its all-$n$
quantifiers. Every full-box fibre distribution, height histogram,
maximizer list, rule table, endpoint matrix and labeled fibre-vector hash
is in the canonical. In particular the maxima for lengths three through
nine are $6,15,33,69,129,255,507$; these observations are backed by the
separate all-length strictness proof, not extrapolated.

## Integrity and next obligation

`INPUT_PINS.sha256` is workspace-root-relative and covers this package's
scientific files plus the read-only intake/root proof/source context.
`MANIFEST.sha256` is package-relative and covers every nonself package
file, including inputs, complete execution outputs and downloaded sources.
Neither manifest claims to hash itself. The gate should pin these originals
before reading and write only to its distinct gate directory. Root performs
its own actual replay and source inspection before any admission decision.
