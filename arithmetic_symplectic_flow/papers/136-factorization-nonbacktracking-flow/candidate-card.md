# Broadened carrier card — ANG-20260914-FAC01

**Version:** 1, 2026-09-14; frozen before audit.  
**Initial status:** BROADENED HYPOTHESIS — T0--T3 OPEN.

For every integer n>=2 let Gamma_n be the undirected SIMPLE graph whose
vertices are all ordered finite words (a_1,...,a_k), each a_i>=2, with product
n. Two vertices are adjacent exactly when one replaces one entry ab by
the adjacent pair (a,b), a,b>=2, or reverses such a replacement. There are no
self-loops or labelled parallel edges. Let Gamma be the disjoint union of
these graphs for every n>=2.

Let X be all bi-infinite nonbacktracking oriented-edge paths in Gamma.
For directed edges e_t require terminal(e_t)=initial(e_{t+1}) and
e_{t+1} not equal to the reverse of e_t. The action is shift sigma.
Use the discrete directed-edge alphabet and its product topology restricted
to X. The transformation groupoid X crossed with Z is the specified
broadened owner. No constant paths at isolated vertices are inserted.

| Field | Frozen specification |
| --- | --- |
| Lineage | divisibility-based prime/composite recognition -> ordered factor refinement as symbolic admissibility -> reversible edge-path shift/groupoid |
| Arithmetic data | integer multiplication, all n>=2 together; no chosen prime component or prime table |
| Proposed prime mechanism | whether multiplicative indecomposability gives prime packets in this same path action; OPEN |
| Roof / flow | unit roof; suspension (X x [0,1])/(z,1)~(sigma z,0), same positive clock |
| Primitive / repetition | least shift period; cyclic phases identified; reverse orientation retained as distinct unless already a shift; repeated traversal r times has length r times primitive length |
| Analytic proposal | ordinary unweighted primitive product if defined; T3 OPEN, no operator supplied |
| Controls | prime and small-composite components; backtracking versus reduced paths; nonprime graph cycles; all-component ownership |
| Classical symplectic fields | NOT APPLICABLE |
| Stop | direct prime packet test first; no determinant work if primes lack paths |
| Route | no classical coordinates; Route B NOT INVOKED |

The graph relation is not itself a deterministic base map. Only the specified
edge shift owns time and returns. Replacing paths by vertex stasis or adding
loops/roofs would change the candidate.

## Audit outcome — 2026-09-14

The frozen version-1 definitions above are unchanged.

**Current status:** STOP — PRIME-PRODUCT COMPONENTS HAVE NO PATHS.

- T0: established for this locally compact symbolic transformation groupoid
  and its complete unit-roof suspension; classical symplectic fields remain
  NOT APPLICABLE.
- T1: multiplication intrinsically identifies prime products by an isolated
  factorization vertex. The proposed conversion of that indecomposability
  into a packet of the frozen path action fails: X_p is empty for every prime p.
  The unit clock is owned but supplies no prime-dependent length law.
- T2: least-period and repetition conventions are coherent on the same
  suspension. Prime-product packets are absent. As an exact contrast,
  Gamma_8 is a four-cycle and yields two oriented primitive packets of length 4.
- T3: NOT EVALUATED after the direct prime-packet stop; no determinant or
  global orbit product is asserted.
- Decision: stop this candidate; portfolio fork. No formal Route coordinate
  was evaluated; Route B NOT INVOKED.

Prime entries can occur inside factor words of a composite-product packet.
This does not contradict X_p being empty and is not an independently proved
dictionary between primes and packets. See [paper.md](paper.md) and
[claim-ledger.md](claim-ledger.md).
