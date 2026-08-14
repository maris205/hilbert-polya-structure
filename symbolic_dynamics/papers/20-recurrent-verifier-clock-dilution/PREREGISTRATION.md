# PREREGISTRATION — SD-C22

## Frozen question

Does closing the explicit SD-C21 prime-verification path into one recurrent
cycle per accepted input preserve both the exact Euler clock and an ordinary
whole-vertex Fredholm determinant?

## Claims and falsifiers

| ID | Preregistered claim | Status sought | Decisive falsifier |
|---|---|---|---|
| C1 | The contracted prime cycle has $\ell(p)=2+\sum_{d=2}^{\lfloor\sqrt p\rfloor}\lceil p/d\rceil$. | theorem | One reachable prime path has a different edge count. |
| C2 | $\ell(p)=\frac12p\log p+(\gamma-1)p+O(\sqrt p)$. | theorem | The exact formula or harmonic estimate fails. |
| C3 | Every nonnegative exact-clock allocation makes $L_\sigma$ noncompact for every $\sigma>0$. | theorem | One allocation has tail block norms tending to zero. |
| C4 | The accepted restriction lies in no finite Schatten class. | theorem | Its singular values have a finite $q$-sum for some $q>0$. |
| C5 | The unit circle lies in the essential approximate spectrum. | theorem | A unit-circle point lacks a singular Weyl sequence. |
| C6 | The raw factor is $1-z^{\ell(p)}p^{-s}$, while first return gives $1-zp^{-s}$. | theorem | Direct finite-block determinants disagree with either formula. |
| C7 | At $z=1$ the orbit product is $1/\zeta(s)$ on $\operatorname{Re}s>1$, but it is not the whole-operator Fredholm determinant. | theorem/boundary | The whole adjacency is trace class, or the product identity fails. |
| C8 | Acceptance-independent runtime padding produces the same obstruction for arbitrary decidable supports. | adversarial theorem | A padded infinite accepted support evades the clock-length criterion. |

## Frozen controls

1. Exact formula versus direct traversal for every prime through 4096.
2. Independent prime support used only after graph construction.
3. Composite paths checked for absence of closed walks.
4. Uniform and adversarial exact-clock allocations.
5. Dense exact determinants only for small cycle blocks.
6. Raw graph-step versus induced return-step markers at $z=1$ and $z=1/3$.
7. SD-C21 summable source roofs as the trace-class/wrong-clock control.
8. Acceptance-independent padded deciders for squares, powers of two,
   Fibonacci numbers, and a deterministic hash inventory.
9. Alphabet relabeling control.
10. No Riemann-zero or fitted target-root data.

## Evidence hierarchy

- Infinite statements: proved analytically.
- Finite exact arithmetic: deterministic certificate.
- Floating values: diagnostic illustrations only.
- Roof distribution: `MODELING_CHOICE`.
- Arithmetic origin: structural semiring relation, not analytic selectivity.

## Stopping rule

The candidate stops if exact Euler clock and recurrent full verification force
noncompactness on the frozen natural vertex space, even if a formal orbit
product or induced determinant survives. The stopping rule is met.

## Frozen verdict

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_PASS_ANALYTIC,
 A2_FAIL,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
ROUTE_B_LOCKED
```
