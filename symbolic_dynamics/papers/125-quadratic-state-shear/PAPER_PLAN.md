# P125 paper plan

Status: **IMPLEMENTED ROUND-TWO PLAN / GO_INTERNAL / EXTERNAL HOLD**.

## Central question

For a nonsingular quadratic space `(V,Q)` over `F_2`, what is the complete
finite dynamics of the basis-free, orthogonal-equivariant nonbijective map

```text
(x,y) -> (y, x + Q(x)y)?
```

The paper must answer this pointwise and globally for both Witt signs, without
claiming ownership of static quadratic-form counts, transvections,
Yang--Baxter maps, or formal zeta conversion.

## Section contract

1. **Map and residual question.** Define the map, `N`, and the Gauss/Witt sign
   `S`; separate it from transvection actions and bijective/nonbijective
   Yang--Baxter maps; include the P99/P103/P106/P109/P118 firewall.
2. **Pointwise clock.** Prove polar invariance and the three-bit quotient;
   display the complete matrix-word/landing table for all eight quotient
   rows to classify every depth, period, and shortening; record the
   plus/minus plane boundary; give explicit failures of both Yang--Baxter
   relations.
3. **Fibres, images, layers.** Solve the inverse equation, count the `0/1/2`
   fibres by a product code, derive the eight pair counts by a self-contained
   Walsh transform, then identify the image tower setwise and count all depth
   layers.
4. **Components and zeta.** Use reverse fibres as a complementary engine for
   the trees attached to the forward-classified cycles; prove the six-shape
   list, component counts, cycle formulas, and routine zeta product.
5. **Controls and release boundary.** State the exact exhaustive coverage,
   bounded owner non-hit, substantial owner risk, and external HOLD.

## Claims-to-proof skeleton

| Claim | Engine | Boundary |
|---|---|---|
| quotient and period ceiling | polarization plus the explicit eight-row matrix-word/landing table | every pointwise shortening is displayed |
| exact fibres | direct solution of `v=x+Q(x)u` | candidates are proved distinct |
| fibre histogram | independent singular/nonsingular product code | uses only `S^2=N` |
| pair census | three-character Walsh expansion | static counts receive zero credit |
| image tower | fibre-type table plus pointwise fates | equality is setwise, not only numerical |
| layers | transient quotient rows plus pair census | minus plane `m=1` has no depth two |
| six shapes | reverse fibres attached to forward cycles; rotation-only directed-cycle control | called complementary, not logically independent |
| cycles/zeta | component inventory and standard cycle product | zeta bookkeeping receives zero credit |

## Owner and collision ceiling

- Fulton and Hall--Shpectorov: characteristic-two quadratic/orthogonal count
  region; exact counts are reproved.
- Sjostrand: transvection orbit machinery; fixed-centre invertible linear maps
  differ from the state-gated nonbijective pair map.
- Etingof--Schedler--Soloviev and Catino--Colazzo--Stefanelli: bijective and
  nonbijective Yang--Baxter pair maps; the present map fails both defining
  relations.
- Internal P106 is the closest temporal silhouette.  P99 owns a genuine
  unipotent shear, P103 and P109 own other exact finite algebraic functional
  graphs, and P118 spends the quotient/fibre/basin/zeta package architecture.

Allowed residual language is limited to the complete functional graph of the
literal map.  No first-occurrence, novelty, priority, or external-release
claim is permitted.
