# C87 source audit

| source | SHA-256 | role |
|---|---|---|
| C73 evidence | `e91c8e6dcf1de5362b1a052ada83eb758b2c2d75520c1e8bdbd37ab055c725e5` | 25 minimal generating edges and first-order baseline |
| C73 manifest | `a50b5707d36f8b94b463e6c5fc4b5b7f6d6df7eb5e87d70bfc82d2b1a653cd8d` | predecessor binding |
| C76 evidence | `42e7783b2652666b84ea7f82b65d2421d98064ee5d5011ab94033aa18c051a94` | faithful label action and generators |
| C76 manifest | `55725664005113ae993b54197ff4fbd97bde347ce49aa69ea0c228372ba289d5` | predecessor binding |
| C78 evidence | `728d6462b337e3b22fe267ae9388da476a0f6409cc64a17ca659f53f1a8126ae` | independent pivot-plus-direction-block criterion |
| C78 manifest | `955b5ce23bf811d7377c0e41afd8d7dbc384a467790647e04cf0dadc98347c60` | predecessor binding |
| C81 evidence | `c3cc35f45e1c8f7c9d4ecaecca820bf9dbc4db1c6a5769c20c75bad21f32fd9f` | effective-orbit quotient consistency |
| C81 manifest | `ff3028fd68817795b08ff24332ef44de4cf520ccba543f053fbd78140ac1b512` | predecessor binding |
| C82 evidence | `6fc49cad02956f463b1e37d017506f437edce6717414da74770ad94913ccefa1` | Boolean-predicate and support-count consistency |
| C82 manifest | `5934de3a933e559e941fc636860db2f9f5ceca181acd9d4915396e9facdc8f8b` | predecessor binding |

Every producer/checker run rehashes all ten raw source files before accepting
them.  The producer constructs the Boolean truth table only from C73's 25
minimal edges.  The independent checker instead reconstructs it from C78's
four direction blocks and pivot.  Both separately reconstruct C76's five
effective permutations.

The C75 ambient lift has order 11520, but its order-six factor fixes every
label.  C87 therefore quotients labels and unordered pairs by the faithful
1920-element image, not by counting the nonfaithful lift as 11520 distinct
label permutations.  The order-six kernel remains explicit in every receipt.

All cited sources are local, hash-bound computational authorities.  The paper
contains no external bibliographic citations.
