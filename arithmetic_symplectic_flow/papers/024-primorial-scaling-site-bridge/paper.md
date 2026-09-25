# Primorial coding in the scaling site

**Paper ID:** `024-primorial-scaling-site-bridge`  
**Candidate ID:** `ANG-20260914-SCS01`  
**Status:** `STOPPED AT T1 — T0 AND LINEAGE CODING ESTABLISHED; CANONICAL LANDING SCOPED FAIL; T3 NOT EVALUATED`

## Frozen object

The carrier is the Connes--Consani scaling site `S` and its adele-class
realization `X_Q`. It has an `N^times` multiplication action and an
`R_+^times` scaling action. No classical map or roof is added.

For Holt's gap recursion, write `P_k=p_k#`. R1 reads
`p_(k+1)=g_1+1` from `G(P_k)`, and R2--R3 produce
`P_(k+1)=p_(k+1)P_k`. Define

```text
j(G(P_k))=[P_k],       [P_k] --> [p_(k+1)P_k].
```

`[P_k]` is the finite supernatural/finite-adele coordinate. The update is a
carrier multiplication arrow; its label is read from the current sieve word.

## Exact limitation

The carrier owns `C_p=R_+^times/p^Z`, with period `log p` and local
repetitions `r log p`. The coded path advances under `N^times`.

There is a weaker same-carrier relation: `[P_k,1]=[1,P_k^(-1)]` in the
adele-class quotient, so coded stages lie on the free scaling orbit. This free
orbit is dense in every `C_p`. The discrete primorial sequence has a different,
decisive limit: `P_k^(-1)->0`, hence it tends to `[1,0]`. This is in the
`A_f x {0}` contribution, fixed by every scaling action. It cannot be a
nontrivial `C_p`; prime periodic data require a finite adele component that
vanishes at the selected prime, whereas the finite component here is `1`.

| Audit | Status | Limitation |
| --- | --- | --- |
| T0 carrier | established | nonclassical only |
| lineage coding | established | semigroup arrow, not return relation |
| T1 canonical sieve-to-`C_p` landing | scoped FAIL | canonical sequence lands at fixed `[1,0]`, not `C_p` |
| T2 `C_p`, `r log p` | carrier-local established | not attributed to coding |
| T3 | NOT EVALUATED | stop after T1 failure |
| Route A/B | NOT APPLICABLE / NOT INVOKED | prohibited |

**Decision:** `STOP AT T1; FORK`. The exact source-to-carrier coding remains a
useful lineage control, but its natural endpoint is incompatible with the
prime-orbit ledger. Do not pursue a trace/determinant for this candidate.

## Evidence index

- [Candidate card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Evidence and source lock](evidence/README.md)
- [Symbolic source control](../019-primorial-gap-recursion-control/paper.md)
- [Earlier scaling-site control](../005-adelic-scaling-a0-positive-control/paper.md)
