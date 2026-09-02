# Direct-owner and portfolio chains for LCP and PAE

**Search/audit date:** 2026-09-02 UTC  
**Mode:** bounded keyword-to-primary-source audit plus complete local contract
comparison  
**External state:** `HOLD_EXTERNAL`

Only generic queries were sent to search engines.  No draft, proof package, or
repository artifact was transmitted.  A bounded non-hit is never used as a
novelty or priority certificate.

## 1. LCP owner chain

### Query record

```text
plane tree delete leftmost child subtree iteration pruning ordered tree
ordered rooted tree pruning first child subtree generating function preimages
plane trees old path pruning inverse expansion operator
```

### External chain

1. Hackl, Heuberger, Kropf, and Prodinger,
   [*Fringe Analysis of Plane Trees Related to Cutting and Pruning*](https://arxiv.org/abs/1704.01095),
   Aequationes Mathematicae 92 (2018), DOI
   [10.1007/s00010-017-0529-0](https://doi.org/10.1007/s00010-017-0529-0).
   This directly owns repeated plane-tree pruning, leftmost old leaves and
   paths, and inverse expansion operators.  It does not appear to use the
   literal whole-first-subtree rule, so it owns inputs rather than supplying
   the decisive kill.
2. Chen, Deutsch, and Elizalde,
   [*Old and young leaves on plane trees*](https://arxiv.org/abs/math/0410127),
   owns the old/leftmost leaf statistic and its static enumeration.  It does
   not supply the LCP iterate or fibre.
3. The external outward-contraction owner already recorded by P148 owns the
   unordered one-step contraction shadow and generic ordered contraction is
   also cited there.  These sources remove generic contraction and
   expansion language; their exact scope is documented in P148.

### Internal direct chain

```text
LCP literal plane-tree map
  -> P148 exact same PT_(<=N) carrier and exact-source-layer convention
  -> P148 original-coordinate survival induction
  -> P148 local reversible inverse multiplied over target vertices
  -> P148 coefficient nonvanishing / minimum-source image condition
  -> KILL_PROOF_ENGINE_TRANSFER
```

P114 supplies the portfolio's parallel tree-peeling/height/fibre precedent.
P126 supplies the recursive all-iterate canonical-code and local-product-fibre
precedent.  Those two are supporting collisions.  P148 is decisive because
both its all-iterate induction and inverse scaffold migrate mechanically.

### Exact support boundary

The external search did not retrieve the literal equation
`L(T_1,...,T_k)=(L(T_2),...,L(T_k))`.  That non-hit does not matter: the gate
tests portfolio residual, not literal-name novelty.  After the internal P148
subtraction, changing depth divisibility to child-index threshold leaves no
new proof architecture.

## 2. PAE owner chain

### Query record

```text
permutation retain positions values same parity standardization
parity agreement permutation extraction
parity alternating permutations position value same parity
```

### External chain

1. Kebede and Rakotondrajao,
   [*Parity alternating permutations starting with an odd integer*](https://arxiv.org/abs/2101.09125),
   ECA 1:2 (2021), DOI
   [10.54550/ECA2021V1S2R16](https://doi.org/10.54550/ECA2021V1S2R16),
   directly owns the fixed class and its static enumeration/statistics.
2. Tanimoto,
   [*Combinatorial study on the group of parity alternating permutations*](https://arxiv.org/abs/0812.1839),
   is an earlier owner for parity-alternating permutations and their static
   group/statistic structure.

Neither external paper found in the bounded search defines the literal PAE
extraction map.  They nevertheless remove all fixed-class value.

### Internal direct chain

```text
PAE retain an absolute-predicate subword and standardize
  -> P149 identical selected-word/rank-varying interface and composed sections
  -> P156 selected positions + selected values + forced sigma assignment
  -> P156 target compatibility obstruction + minimum all-rank section
  -> P156 complement matching fibre + canonical inverse tower
  -> P155 target-dependent minimum scheduler + factorial support sum
  -> permanent parity/direction/standardization selector exclusion
  -> KILL_PERMANENT_SELECTOR_EXTRACTION
```

P156 is the decisive proof-engine owner.  In its notation, replacing the
Ferrers inequalities by odd/even colors turns the deficient complement board
into two complete bipartite blocks; every other step remains unchanged.  P155
independently occupies the two-order minimization, all-rank section, and
factorially weighted fibre silhouette.  P149 occupies the selected-subword
iteration and explicit-section silhouette.

### Exact support boundary

The PAE rank-eight obstruction---732 targets need excess four rather than two
---is verified and the threshold theorem is proved.  It is only a more
complicated target statistic inside an excluded architecture.  It does not
break the direct chain above.

## 3. Decision receipt

| candidate | literal direct external owner found? | decisive owner | gate |
|---|---:|---|---|
| LCP | no exact-rule hit | internal P148 proof engine | `KILL` |
| PAE | no exact-rule hit; fixed class directly owned | internal P156 plus permanent selector rule | `KILL` |

No numbering, drafting, freeze, release, or Git action is authorized by this
record.
