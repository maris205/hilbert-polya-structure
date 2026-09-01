# Paper plan: folded-hypercube products and component-order inversion

**Working title:** Uniform Vertex-Push Chains as Folded-Hypercube Products:
Component-Order Inversion
**Type:** anonymous rigorous mathematical short note
**Stage:** round-1 remediation
**Status:** `ROUND-2 INTERNAL ACCEPT / OWNER_REPAIRED / HOLD_EXTERNAL`
**Target length:** 5--7 A4 pages including references
**Residual sentence:** After assigning the folded-hypercube identification,
single-component spectrum, bipartiteness, random-walk facts, vertex pushing,
and generic Fourier machinery zero credit, record the labelled
multi-component weighted-product factorisation and prove an input-only
known-`n` inverse for its component orders.

## Claim--evidence--credit matrix

| Item | Formal object | Exact control | Credit status |
|---|---|---|---|
| Push orbit is `F_2^V/<1_C>` with size `2^(n-c)`. | Cut-map kernel lemma. | Every labelled graph through order five. | Setup; vertex pushing and equivalence are established, so no residual emphasis. |
| A connected order-`s` factor is `FQ_(s-1)`. | Pivot isomorphism `[a] -> (a_v+a_*)`; explicit generator images. | Quotient generator checks for `s=1..12`. | Direct folded-hypercube identification; zero credit. |
| Disconnected kernel is the degree-weighted random-scan tensor sum, including isolate loops and duplicate labels at `s=2`. | Exact kernel proposition. | Literal labelled transitions on all graphs through order five. | Multi-component assembly is retained only as a narrow residual packaging claim. |
| `M_G` gives the global transition multiplicities and return law. | Owned single-factor spectrum plus weighted tensor-sum multiplication and character orthogonality. | Exact sign multiplicities and return recurrences through time six. | Single-factor spectrum and generic spectral moment are zero credit; only the multi-factor packaging remains residual. |
| Period two iff all component orders are even. | Product parity/odd relation, with `s=1` loop. | Kernel-parity and `-1` tests on all graph controls. | Folded-hypercube bipartiteness is directly owned and zero credit. |
| Given `n`, `(n,Q_G)` recovers all component orders. | Complete negative-root lemma plus descending exact-divisibility algorithm. | The routine receives only `(n,Q)` for all 28,628 partitions through total 30; 624,834 candidate divisions and 144,024 successful peels. | Principal residual theorem; no novelty claim. |
| Internal adjacency is invisible; starting orientation is unmarked; unknown `n` fails generally. | Dependence only on orders, affine conjugacy, all-edgeless family. | Constructed `P_4/K_4` kernels, affine cosets, and six edgeless orders. | Sharp limitation, not a positive reconstruction claim. |

## Section structure

1. **Scope and owner subtraction.** Name all six verified sources, identify the
   direct folded-hypercube hit, and freeze the reduced residual.
2. **Quotient and folded-hypercube product.** Prove the cut quotient, pivot
   isomorphism, low-dimensional conventions, and weighted product kernel.
3. **Multi-component factorisation.** Import the owned single-factor spectrum,
   derive `M_G`, and record return/period as zero-credit consequences where
   appropriate.
4. **Known-order inverse.** Recover `Q_G`, prove the full nearest-root lemma,
   state the `(n,Q)` exact recovery algorithm, and prove it cannot accept a
   spurious size.
5. **Boundary and exact controls.** Give `P_4/K_4`, affine-orbit, and
   all-edgeless witnesses; report repaired controls and retain
   `HOLD_EXTERNAL`.

## Citation plan

- Pretzel and Klostermeyer: vertex-push and orientation framework.
- Terras: generic finite-group Fourier background.
- Xu--Meng: standard folded-hypercube Cayley presentation and complete
  single-component adjacency spectrum.
- Xu--Ma: folded-hypercube bipartiteness/cycle boundary.
- Chen--Li--Lin: direct folded-hypercube random-walk literature.

All six entries are verified in `SOURCE_VERIFICATION.md`; the inverse
owner-search non-hit is explicitly not novelty evidence.

## Display decision

No figure is planned.  The pivot map, weighted tensor sum, and descending
division algorithm carry the exact relationships.  A picture would not
resolve the duplicate-generator convention at `s=2` or strengthen the root
proof.  One compact control table remains useful.

## Workflow and release gate

Round 0 is preserved as `main_round0_original.pdf`.  This remediation produces
`main_round1.pdf`, updates all ledgers, and records changes in
`IMPROVEMENT_LOG.md`.  The task forbids a round-2 review and Git operations;
neither is performed.  External status remains `HOLD_EXTERNAL`.
