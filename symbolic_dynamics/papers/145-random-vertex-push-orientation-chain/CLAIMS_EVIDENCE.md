# P145 claims--evidence ledger

**Status:** round 1 revised / anonymous / `HOLD_EXTERNAL`
**Ceiling:** the frozen P145 contract remains an absolute claim ceiling.

The revision incorporates a direct owner hit.  Vertex pushing, push
equivalence, the connected folded-hypercube identification and spectrum,
folded-hypercube bipartiteness and random-walk facts, finite-abelian Fourier
diagonalisation, and generic uniform stationarity/spectral moments receive
zero contribution credit.  No novelty or priority claim is made.

| ID | Exact statement | Formal support | Executable support | Credit/boundary | Status |
|---|---|---|---|---|---|
| `P145-B0` | The push orbit is a torsor for `F_2^V/<1_C>`; component all-push relations are all relations; orbit size is `2^(n-c)`. | Lemma 2.1, cut-map kernel. | Exact cut ranks, full kernels, constant fibres, and BFS orbits for every labelled graph through order five. | Established push framework/setup; not residual. | Proved; controls pass. |
| `P145-B1` | For a connected order-`s` component, pivot coordinates send the quotient generators to the coordinate vectors and all-ones vector of `F_2^(s-1)`. | Proposition 2.2 and equations (5)--(6). | Literal generator images for every `s=1..12`. | Direct identification with the standard Xu--Meng `FQ_(s-1)` presentation; zero credit. | Proved as bridge; owner subtracted. |
| `P145-R1` | The disconnected labelled kernel is the degree-weighted random-scan tensor sum, with isolate weight `m_1/n` and explicit `s=2` duplicate-generator convention. | Proposition 2.2, equation (7), and convention paragraph. | Literal labelled graph kernels through order five. | Narrow multi-component residual packaging only. | Proved; controls pass. |
| `P145-R2` | Eigenvalue `(n-2k)/n` has multiplicity `[x^k]M_G(x)`; the return formula and period boundary follow. | Theorem 3.1: owned single-factor spectrum plus weighted product multiplication and orthogonality. | Sign multiplicities, direct recurrence through time six, odd relations, and `-1` criterion on all graph controls. | Single-component spectrum, bipartiteness, folded-cube walk facts, and generic spectral moments are zero credit. | Proved; heavily owner-subtracted. |
| `P145-R3` | Given `n`, the spectrum including multiplicities recovers `Q_G`, and the deterministic descending divisibility algorithm using only `(n,Q_G)` returns all component orders. | Lemma 4.1 and Theorem 4.2: complete simple negative roots, strict nearest-root ordering, precise nearest-root collision exclusion, and isolate residual. | 28,628 public-input recoveries through total 30; 624,834 exact candidate division attempts and 144,024 successful peels. | Principal residual theorem; bounded owner-search non-hit is not novelty evidence. | Proved; genuine input-only control passes. |
| `P145-L1` | Known-`n` spectrum does not determine internal adjacency. | Proposition 5.1; factorisation depends only on component orders. | Independently constructed `P_4` and `K_4` edge sets, labelled transition matrices, and equal characteristic polynomial `z^8-z^6`. | Sharp positive limitation. | Proved; real witness passes. |
| `P145-L2` | An unmarked chain/spectrum contains no chosen starting orientation or affine push orbit. | Proposition 5.1; translation conjugates affine cut-space cosets. | Constructed disjoint affine `K_4` orbits and transition conjugacy. | Category distinction, not a substantive spectral target. | Proved; wording narrowed. |
| `P145-L3` | Without supplied `n`, component orders are not recoverable in general. | Proposition 5.1; every positive-order edgeless graph has the one-state identity kernel. | Literal edgeless kernels for orders 1--6 all have characteristic polynomial `z-1`. | Establishes necessity of the theorem's known-`n` hypothesis. | Proved; controls pass. |
| `P145-E1` | The revised verifier is deterministic exact arithmetic and its recovery decisions do not inspect the hidden partition. | `recover_component_orders(total, compressed)` source interface and exact division implementation. | Byte-identical canonical replay; 155,901 assertions. | Computation is counterexample pressure only. | Pass. |

## Downgraded and removed round-0 controls

- The old “factor peeling” loop was given the true partition.  It has been
  replaced by `recover_component_orders(n,Q)`, which scans candidate sizes
  from `n` downward and sees no ground-truth factors.
- The old “strict root order” and “no-smaller collision” checks were executable
  restatements of integer inequalities.  They have been removed.  The verifier
  now claims only exact squarefreeness of `E_s` through `s=30`; nearest-root
  order and collision exclusion are carried by the all-parameter proof.
- The old `P_4/K_4` control called the component formula twice.  The new
  witness constructs both adjacency sets and both Markov matrices before
  comparing exact characteristic polynomials.

Distinct `E_r,E_s` can share roots away from the larger factor's nearest root,
so no pairwise-coprimality claim is made.

## Release gate

The revised package remains an owner-thin internal record.  It makes no
novelty, priority, authorship, posting, submission, publicity, or
specialist-contact decision.  External status remains `HOLD_EXTERNAL`.
