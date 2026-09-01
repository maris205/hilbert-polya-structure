# Claims and evidence ledger

**Gate:** the frozen theorem contract is the claim ceiling.  The manuscript is
anonymous, owner-thin, and **HOLD_EXTERNAL**.  Proof is the primary evidence;
exact enumeration is counterexample pressure only.  Round 1 further subtracts
deterministic leftmost scheduling, comb/height-zero covers, and the ordered-tree
graft/lift representation from standalone residual credit.

## Formal claim matrix

| ID | Claim | Proof locus in `main.tex` | Exact evidence | Status |
|---|---|---|---|---|
| C1 | If `P=C_1...C_k`, `C_1=UAD`, then `Phi^t(P)=UA C_2...C_(t+1)D C_(t+2)...C_k` for `0<=t<=k-1`. | Lemma “closed orbit” | `iterate-formula` for every state and every admissible `t`, `n<=12` | Proved as stated |
| C2 | Every nonfixed update reduces primitive-factor count by one; all recurrence is fixed and fixed paths are exactly primitive. | Closed-orbit lemma and recurrent corollary | `factor-drop`, `fixed-if-primitive`, `moves-if-composite`, `terminal-fixed` | Proved as stated |
| C3 | `tau(P)=k(P)-1`; the maximum is `n-1`, uniquely at `(UD)^n`. | Sharp-clock corollary | `pointwise-clock` for 290,511 paths and `unique-deepest` at every `n<=12` | Proved as stated |
| C4 | The fixed census is `Cat_(n-1)`. | Outer-step deletion bijection | Complete fixed census for every `n<=12` | Proved as stated; Catalan enumeration receives zero credit |
| C5 | The number of depth-`k-1` states is `k/(2n-k) binom(2n-k,n)`. | Temporal-layer theorem via `(zC(z))^k` and Lagrange inversion | Every layer at every `n<=12` | Proved as stated; ballot/Lagrange machinery receives zero credit |
| C6 | For fixed `T=UQD`, with `Q=Q_1...Q_r`, the displayed suffix-cut path is the unique source at every depth `d in [0,r]`. | Terminal fibre theorem, constructive direction and converse | Every fixed target and every feasible depth through `n=12` | Proved as stated |
| C7 | The terminal depth-fibre polynomial is `1+u+...+u^r`. | Immediate sum of C6 | Exact `Counter({d:1})` comparison for all 82,500 targets | Proved as stated |
| C8 | The unique largest terminal fibre has size `n` at `U(UD)^(n-1)D`. | Extremal corollary using `r<=n-1` | `maximum-fibre-size` and `unique-maximum-target` for every `n<=12` | Proved as stated |

## Boundary cases checked in proof and code

- `n=1`: the sole path `UD` is fixed, has depth zero, and is its own unique
  depth-zero basin source.
- `k=1`: the map is the identity and the closed-orbit formula has only `t=0`.
- `n=k`: the Lagrange coefficient has `m=n-k=0`; it is handled directly
  rather than by dividing by `m`.
- `r=0`: a fixed target with empty interior has fibre polynomial `1`.
- `d=0`: the target itself is the source.
- `d=r`: the first source component is `UD`, followed by all factors of the
  target interior.

## Evidence totals

The focused audit exhausts:

| Quantity | Count |
|---|---:|
| Semilengths | 12 (`1..12`) |
| Dyck states | 290,511 |
| Fixed targets | 82,500 |
| Exact assertions | 6,005,502 |
| Floating-point operations used for claims | 0 |
| Samples or random seeds | 0 |

The canonical transcript is `verification_output.txt`.  A valid replay must
compare byte for byte and terminate with `STATUS=PASS`.

## Zero-credit and nonclaim ledger

The following are used but not presented as residual contributions:

- first-return decomposition and unique primitive factorisation;
- Catalan enumeration of Dyck paths and primitive paths;
- the ballot/component count;
- the atomic Tamari reassociation;
- Pallo's deterministic leftmost-rotation precedent, rooted rotation tree,
  rank, and distance;
- the Pallo/Chapoton comb-order characterisation as precisely the Tamari covers
  moving a subpath at height zero;
- the standard contour bijection to rooted ordered plane trees;
- the representation of one update as grafting the second root child onto the
  first as its rightmost child, the root-degree-minus-one clock, and the inverse
  representation as lifting a suffix of children;
- the generic Lagrange-inversion and generating-function extraction steps.

The note does not claim a classification of Tamari schedules, general lattice
dynamics, literature priority, or external owner clearance.  Its residual
scope is only the conjunction, for the particular literal selector, of its
closed all-time iterate with the targetwise assertion that each feasible depth
has one specified source.  The clock, layers, graft/lift model, fibre
polynomial, and extremal target receive no standalone novelty or priority
claim.

## Round-1 owner allocation

| Interface | Direct source or representation | Allocation |
|---|---|---|
| deterministic leftmost rotation | Pallo (2006), pp. 802--803 | zero standalone credit; different map, separated by one terminal root versus `Cat_(n-1)` |
| ground-level cover | Pallo (2003); Chapoton (2020), Section 1.2, p. 438 | zero credit; every `Phi_n` edge is a comb cover selected at the leftmost ground return |
| plane-tree carrier | Stanley, Theorem 1.5.1 | zero credit for contour bijection, root-child graft, suffix lift, and root-degree clock |
| exact temporal/target-fibre package | direct proofs C1 and C6 | retained only as an owner-unresolved conjunction under `HOLD_EXTERNAL` |

## Traceability

- Literal implementation: `verify_p144.py::phi`
- Closed iterate: `verify_p144.py::predicted_iterate`
- Ballot layer: `verify_p144.py::ballot_layer`
- Constructive inverse: `verify_p144.py::source_at_depth`
- Full exhaustive loop: `verify_p144.py::audit_size`
- Frozen output: `verification_output.txt`
- Source roles and metadata: `SOURCE_VERIFICATION.md`
- Literal move/owner comparison: `SOURCE_VERIFICATION.md`, “Literal
  comparison of the three move descriptions”
