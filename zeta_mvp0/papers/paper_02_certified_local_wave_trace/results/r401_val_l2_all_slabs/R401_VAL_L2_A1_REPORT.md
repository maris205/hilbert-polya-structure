# R401-VAL-L2-A1 All-Slab Production Report

Protocol: `R401-VAL-L2-A1`  
Run configuration: `f2d3eef4a76f18246c15789e32fe597266e3fe855c5e9a8bd2b5c3e67dfdf70d`  
Archive generation: `a658e754000ea29aa0f2289aa03f45b565e216c96584fb3de6d494f9c27c95e0`

## Purpose

This held-out production run extends the accepted six-tree implementation
smoke to every one of the 51 parameter slabs protected by the L1 branch
certificate, independently at 128-bit and 256-bit precision. Its licensed
task is to exclude reduced roots from the eight-shell decomposition of

\[
B_{\mathrm{loc}}\setminus\operatorname{int}P_j
\]

for every slab and every frozen parameter value in that slab. The producer
only archived proof objects; scientific acceptance came from the separately
frozen checker.

## Frozen run design

| Item | Frozen value |
|---|---:|
| Slabs | 51 |
| Precisions | 128 and 256 bits |
| Trees | 102 |
| Initial shell roots | 816 |
| Workers | 24 |
| Concurrent nodes per tree | 1 |
| Per-node timeout | 7,200 seconds |
| Per-tree depth cap | 48 |
| Per-tree node cap | 20,000 |
| Global scientific budget | `null` |
| Scheduling rule | deterministic round-robin barrier batches |

The evaluator was built from CAPD commit
`731079217a9254ea2948d742df2b170895effe7f` with MPFR/GMP and
directed-rounding flags. Every node ran in a separate process, and commits
followed canonical `(precision, slab, depth, node_id)` order.

## Production archive

| Precision | Trees | Evaluated nodes | `ENERGY_EXCLUDED` | `RETURN_EXCLUDED` | Internal `SPLIT` | Terminal leaves | Maximum depth |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 128 | 51 | 28,054 | 1,731 | 12,500 | 13,823 | 14,231 | 38 |
| 256 | 51 | 24,736 | 1,637 | 10,935 | 12,164 | 12,572 | 32 |
| Total | 102 | 52,790 | 3,368 | 23,435 | 25,987 | 26,803 | 38 |

At each precision, the number of terminal leaves minus the number of internal
split nodes is 408, exactly the number of eight-shell roots for 51 slabs. All
102 frontiers are empty. No tree reached either frozen resource cap, and all
52,790 archived stderr transcripts are empty.

## Independent replay

The independent checker reopened the 102 strict tree payloads, rehashed every
manifest-bound artifact, reconstructed the exact-rational shell cover and
binary split DAG, and replayed every archived exclusion proof. It also rebound
the accepted L1 five-object release chain and recomputed the canonical
tree-manifest root and archive generation digest.

The replay completed 158,782 checks with zero failures. It found no unresolved
leaf, blocking classification, root candidate, invalid evaluator result,
timeout, precision-domain disagreement, or exhausted tree budget.

## Provenance digest table

| Artifact or digest | SHA-256 |
|---|---|
| Main freeze | `c64d7b3cb7d6cfef403edfe35b7459ba5291608104aea4653ae8c0feec710cf2` |
| Machine freeze | `b9291716b859da9651a2549832581cf85b1852b725bcf285539dea47eb7cbef4` |
| Run configuration | `f2d3eef4a76f18246c15789e32fe597266e3fe855c5e9a8bd2b5c3e67dfdf70d` |
| Evaluator source | `8eabb022f92c712805c401fb07e2b741e4af4e927bc43702c95125b2a4338bd2` |
| Evaluator binary | `b768de84247cd847a3c1b518ec08a7bcfc766e31c20c01bcdd0c75b06d319d53` |
| Checker source | `a03ba2e352e28db434b036f70c9d78a2f04852104a4247393315d28e06775c66` |
| Aggregate summary | `769f06671d23a16be4b8a4cedead3d25370423d0fee2484342c83a0fef61ecfe` |
| Aggregate manifest | `c2e06c4cb7abdac56c157f334c9949441de97bfad84fedee893992d87bf253b2` |
| Independent checker | `a3663435de931c30769038deffbc7cc05fe6f6613c5da638c77301396695c707` |
| Postcheck object | `54a2aa4efbf27d4018c5b1ad313a2fc32f2423e9529e9a7b2fbe6890ffa2450a` |
| Ordered tree-manifest root | `240c81a09d4ffd327fb1f3ba660d6df32c8bb300a3bf62f1481d0c9d3e37605c` |
| Archive generation | `a658e754000ea29aa0f2289aa03f45b565e216c96584fb3de6d494f9c27c95e0` |

## Acceptance declaration

Status: PASS_LOCAL_COMPLEMENT_ALL_SLABS
milestone_status = PASS_LOCAL_COMPLEMENT_ALL_SLABS
theorem_status = PASS_LOCAL_COMPLEMENT_ALL_SLABS
final_status = null
Claim boundary: local P_+=0 reduced-chart result only; no energy-shell/global, trace-formula, Hilbert-Polya, zeta-zero, or RH promotion

## Mathematical consequence

For the exact local box

\[
B_{\mathrm{loc}}=[-0.02,0.02]\times[0.12,0.17]\times[-0.08,0.08]\times[0.64,0.69],
\]

the new complement certificate proves, for every \(j=0,\ldots,50\) and every
\(\epsilon\in E_j\),

\[
Z(F_\epsilon)\cap\bigl(B_{\mathrm{loc}}\setminus\operatorname{int}P_j\bigr)
=\varnothing.
\]

Combining that exclusion with the previously accepted L1
existence-and-uniqueness result inside \(P_j\) gives the pointwise
reduced-chart statement

\[
Z(F_\epsilon)\cap B_{\mathrm{loc}}=\{x_j(\epsilon)\}.
\]

## Scope limitations

The result is confined to the frozen reduced \(P_+=0\) chart and the exact
parameter interval covered by the 51 slabs. It is not a phase or flow-box
cover of a complete periodic orbit, a full-energy-shell or global-phase-space
uniqueness theorem, continuation outside the slabs, a primitive-period
theorem, exclusion of every shorter return, an event-projected determinant
estimate, or a new quantitative trace-domain margin. It does not yield a
trace formula, an arithmetic-prime theorem, a Hilbert--Polya operator, a
Riemann-zero reconstruction, RH, or any implication toward RH.
