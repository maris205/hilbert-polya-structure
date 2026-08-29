# Hostile-review resolution ledger — P115

Status: author revision after independent Reviews A and B. External release,
novelty, and priority remain **HOLD**. This ledger records repairs; it is not a
new review, final QA, owner certificate, or release authorization.

## Shared mathematics and claim-scope repairs

| Review issue | Resolution | Evidence in the revised package |
|---|---|---|
| “Complete/entire functional graph” outran the theorem package | **Applied by theorem, with calibrated surrounding language.** | Theorem 3.2 gives the explicit `F_p`-linear conjugacy `Psi C Psi^(-1)=sigma^(-1) x N`, where `N` is the product of finite index-chain shifts. It then identifies every weak component, cycle, attached rooted tree, per-root entry layer, and indegree type. The abstract/README/narrative now say “exact temporal and component” package rather than relying on an unsupported slogan. |
| Direction of the chain untwisting was unstated | **Applied and checked.** | For `j=u p^v`, `p` not dividing `u`, the manuscript defines `d_(u,v)=sigma^(-v)(c_(u p^v))`; the inverse is `c_(u p^v)=sigma^v(d_(u,v))`. Direct substitution gives `d'_(u,v)=d_(u,v+1)` and terminal zero. |
| Component sizes and attached-tree isomorphism were missing | **Applied.** | A Frobenius cycle of length `d` supports one component `O x V_+` of size `d q^n`; the sets `T_y={(sigma^(h(z))y,z)}` give the attached trees and their partition. The periodic theorem also records `A_d/d` such components. |
| Semilinearity was only implicit | **Applied.** | Equation (2.2) states both `C(lambda f+g)=sigma^(-1)(lambda)C(f)+C(g)` and its `t`-fold version immediately after the map definition; it explicitly says `F_p`-linear and generally not `F_q`-linear. |
| `Per(C)` was not defined | **Applied.** | The conventions section defines the periodic set together with `tau` and `Core`. |
| Route II was overstated as independent | **Applied.** | It is now called “Complementary route II”; the text says it starts from the already proved iterate formula and only recounts fibres and the CDF by rank--nullity. Supporting documents use the same calibration. |
| Recovery data could be misread as a short prefix | **Applied.** | Theorem 7.1 explicitly says `(F_m)_(m>=1)` is the full infinite fixed-count sequence and disclaims an unspecified preassigned finite prefix. |
| “Zero-residue” was ambiguous | **Applied.** | First use and support files now say “residue-class-zero Cartier section.” |
| Small-parameter and empty-set boundaries must survive revision | **Preserved.** | `t=0`, `n=0`, `a=1`, `p^t>n`, empty fibres, constants, `alpha=1`, and the excluded `alpha=p` endpoint remain explicit. The empty product `V_+` at `n=0` is also stated. |

## Owner-scope repairs

| Review issue | Resolution | Evidence in the revised package |
|---|---|---|
| Restriction of scalars puts the map in classical finite-linear dynamics | **Applied with zero credit.** | The definition and ownership section explicitly identify an ordinary finite `F_p`-linear endomorphism. Generic linearization, cyclic--nilpotent splitting, ranks/kernels, component products, and attached trees are subtracted. |
| Direct finite-linear owners were missing | **Applied.** | The manuscript and bibliography now cite and subtract Elspas (1959), Wang (1967), Hernández Toledo (2005), Panario--Reis (2019), while retaining Reis (2023). Bibliographic data and DOI strings were checked against primary publisher/DOI records. |
| A close modern Cartier-family owner was missing | **Applied.** | Jeong’s published 2018 paper on Cartier operators on compact discrete valuation rings is cited as a close family owner; Bridy and Cartier remain. No claim is made that Jeong owns or fails to own the exact bounded conjunction. |
| Contribution density after subtraction was too broad | **Applied.** | The residual paragraph is limited to the exact bounded Cartier specialization—closed coefficient, fibre, temporal, and component formulas—together with the lattice stabilization and parameter-recovery conjunction. Search absence is expressly non-probative. |

## Exact-control repairs

| Review issue | Resolution | Evidence |
|---|---|---|
| Graph-level assertions were absent | **Applied.** | `code/verify.py` now checks the forward/inverse coordinate change, statewise product conjugacy, component count and size, per-root layers, and tree cardinality in every literal finite-field lane, including `n=0`. |
| Raw assertion magnitude could be misconstrued | **Applied.** | Main text and control report call it a mechanical count of executed checks, not independent mathematical claims. The revised canonical terminus is `PASS: 2,259,162 exact assertions`. |
| Fresh run and byte comparison required | **Applied.** | Fresh stdout has 14 lines and 1,449 bytes, ends with `PASS: 2,259,162 exact assertions`, and is byte-for-byte identical to the stored canonical output. |
| Four-stage build, warning/font scan, and all-page visual audit required | **Applied.** | The four stages exited zero. The settled PDF has 7 A4 pages; final log and BibTeX scans have zero warnings/errors, box diagnostics, or undefined items; all 27 fonts are embedded/subsetted/Unicode-mapped; all 7 rendered pages passed visual inspection. |

## Remaining gate

No theorem-level defect reported by either reviewer remains open in the source
revision. The bounded bibliography repair does not establish novelty or owner
absence. A specialist direct-owner audit is still required before any external
use, and external release, novelty, and priority remain **HOLD**.
