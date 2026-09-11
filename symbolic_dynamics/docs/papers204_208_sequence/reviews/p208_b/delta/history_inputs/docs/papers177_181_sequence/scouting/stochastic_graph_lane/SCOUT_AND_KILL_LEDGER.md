# Stochastic, graph, matrix, and lattice scout ledger

**Audit date:** 2026-09-03 UTC  
**External lifecycle:** `HOLD_EXTERNAL`  
**Counting rule:** a row is one literal update/kernel, not a parameter value.
Internal conjugacies and proof-transfer kills remain counted as tested
literals but receive no promotion credit.

The executable probes **nine** fresh literal systems and makes **811,549**
exact assertions.  It is deliberately a wide falsification lane: only one row
is recommended as a theorem spike, one is retained as a theorem-complete
reserve, and seven are killed.

## Exact ledger

| ID | carrier and literal update | exact early signal | owner/collision decision |
|---|---|---|---|
| `RHT` | subsets of the (2^d-1) points of (PG(d-1,2)); toggle a uniformly sampled projective hyperplane | for (d=2,3,4), all Fourier characters give exactly four eigenvalues (±1,±1/(2^d-1)); the carrier splits into (2^{2^d-d-2}) classes, each a simple random walk on a crown graph; every history through time three matches the closed nonzero-sum formula | **`RECOMMEND_THEOREM_SPIKE / OWNER_AMBER`.**  The disjoint-crown conjugacy, every-target kernel, and global lifted multiplicities form a closed package.  Simplex codes, crown spectra, and finite-abelian Fourier theory are zero credit; P145 is the strict internal neighbour. |
| `LFS` | subsets of a represented finite point configuration; intersect with the kernel of a fresh uniform linear form | all sources/targets for binary ranks (d\le3) and all histories through (t=3) match a rank inclusion--exclusion formula; Boolean zeta functions diagonalize the kernel with eigenvalue (q^{-r(C)}) | **`THEOREM_COMPLETE_RESERVE / R7_RISK`.**  The every-target matroid lift is real, but `R7` already records iid hyperplane intersection on the subspace lattice, while semilattice spectra and Tutte/characteristic evaluations are direct background. |
| `ZSI` | graphs on ([n]); retain an edge under a fresh (\mathbb F_q)-colouring exactly when its endpoint colours sum to zero, (q) odd | all graphs for ((n,q)=(3,3),(4,3),(3,5)) satisfy (\Pr(F\text{ survives})=q^{b(F)-v(F)}), with (b(F)) the number of bipartite nontrivial components; every two-step endpoint matches inclusion--exclusion | **`KILL_INTERNAL_P158_TRANSFER`.**  The odd-cycle constraint is attractive, but history words are paired by the involution (x\mapsto-x); P158 already owns complementary-history graph intersection, component fibres, absorption, and the same meet-walk architecture. |
| `DPC` | labelled simple graphs; join two vertices iff their old degree parities agree | through (n=6), the image has size (2^{n-1}) for odd (n), (2^{n-2}) for even (n), and every fibre is uniform; odd orders retract in one step, even orders collapse to (K_n) in two | **`KILL_INTERNAL_P159_P127`.**  The complete theorem is just the odd-degree incidence map followed by a two-clique encoder.  P159 already owns the strict incidence-rank inverse, and P127 owns parity feedback. |
| `CDS` | (M_n(\mathbb F_q)); (A\mapsto A\operatorname{diag}(a_{11},\ldots,a_{nn})) | each column obeys ((d,b)\mapsto(d^2,db)); all iterates, image sizes, target fibres, recurrent core, and fixed-iterate census factor by columns and pass at ((n,q)=(2,2),(2,3),(2,5),(3,2)) | **`KILL_INTERNAL_P102_P175`.**  After the ratio (b/d), this is scalar squaring with zero-diagonal hairs, exactly P102's temporal engine; using the current diagonal on the full matrix carrier is too close to P175 to supply a second axis. |
| `RSS` | (M_n(\mathbb F_q)); scale each row by its old row sum | the row map has the same iterate and fibre histograms as `CDS` in every exact box | **`KILL_EXACT_CONJUGATE_CDS`.**  A linear coordinate change taking the row sum to the distinguished coordinate conjugates each row to ((d,b)\mapsto(d^2,db)).  It adds a literal test but no independent mechanism. |
| `RSI` | graphs; intersect with the star at a fresh uniform vertex | from (K_n), one distinct centre leaves a star, exactly two leave their connecting edge, and three leave empty; all histories through (n=7,t=5) match (n^t-n-\binom n2(2^t-2)) for absorption | **`KILL_MASK_MEET_THIN`.**  The three-distinct-centres clock and (1,2^t-2) fibres are elementary occupancy on top of the random-mask meet engine already spent by P158/P170. |
| `RSG` | graphs; union with the star at a fresh uniform vertex | every noncomplete endpoint records the exact set of sampled centres and has fibre (k!S(t,k)); completion occurs at (n-1) distinct centres | **`KILL_COUPON_OCCUPANCY`.**  This is a coupon collector encoded by star complements; Stirling occupancy is also newly occupied by P172 and supplies the whole theorem. |
| `TCP` | graphs; simultaneously delete every edge lying in a triangle | exhaustive graphs through (n=6) verify an idempotent projection onto the triangle-free graphs; image counts are (7,41,388,5789) and maximum fibres (2,12,187,6115) | **`KILL_RETRACTION_NO_INVERSE`.**  Triangle-edge pruning is complete after one round, while target fibres are the coupled problem of adding triangle-covered edges.  No independent scalable axis appears. |

## Funnel

```text
9 fresh literal systems
  1 recommended theorem spike: RHT
  1 theorem-complete reserve: LFS
  2 exact but internally transferred: ZSI, DPC
  5 shallow, conjugate, owner-dense, or occupied-engine kills
```

The two exact-but-killed rows are intentionally not promoted to inflate the
batch.  `RHT` is the lane's only proposed allocation input; even it remains
`HOLD_EXTERNAL` pending the batch-level owner and five-way diversity gates.

