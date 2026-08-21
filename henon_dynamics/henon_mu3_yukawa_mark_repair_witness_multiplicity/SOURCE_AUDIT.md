# C79 source audit

The producer and independent checker bind these committed predecessor bytes:

| source | SHA-256 |
|---|---|
| C73 evidence | `e91c8e6dcf1de5362b1a052ada83eb758b2c2d75520c1e8bdbd37ab055c725e5` |
| C73 manifest | `a50b5707d36f8b94b463e6c5fc4b5b7f6d6df7eb5e87d70bfc82d2b1a653cd8d` |
| C75 evidence | `8beee17a227153e066907549df70c14a087b7de4141c3092d7cebd4a91541d98` |
| C75 manifest | `7ede3e35c3101d17c683d2da440037d5bd4e002266530b52b3d1cb36ed4c8fcb` |
| C76 evidence | `42e7783b2652666b84ea7f82b65d2421d98064ee5d5011ab94033aa18c051a94` |
| C76 manifest | `55725664005113ae993b54197ff4fbd97bde347ce49aa69ea0c228372ba289d5` |
| C77 evidence | `f7e2db84698ec61bf6283175368d2749d7f17ac77baeda37fd0a5cb8caf1c634` |
| C77 manifest | `bcc3273b481123f89ed5bf10c216bcae7a2ac3ff77685edcba976ea959e84dbc` |
| C78 evidence | `728d6462b337e3b22fe267ae9388da476a0f6409cc64a17ca659f53f1a8126ae` |
| C78 manifest | `955b5ce23bf811d7377c0e41afd8d7dbc384a467790647e04cf0dadc98347c60` |

The C79 receipt itself is not used as an upstream authority by its checker;
the checker reconstructs the closure from C75 and tests the receipt against
that reconstruction.
