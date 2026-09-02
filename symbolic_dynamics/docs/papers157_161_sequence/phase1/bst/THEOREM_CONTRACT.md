# Frozen theorem contract — binary-projective Steiner triangle collapse

External status: **HOLD_EXTERNAL**.  Selection status:
**PASS_FOCUSED / NUMBERING NOT YET FROZEN**.  This is a theorem contract, not
a novelty, priority, or release claim.

Let `r>=2`, let `V=F_2^r`, put `P=V\{0}` and `N=2^r-1`, and define the
Steiner quasigroup operation

```text
x star y = x       if x=y,
             x+y   if x!=y.
```

On ordered triples in `P^3`, set

```text
S(a,b,c)=(b star c,c star a,a star b).
```

The paper must prove the following conjunction.

1. **Complete functional graph.**  Diagonal triples and three-distinct
   triples satisfying `a+b+c=0` are fixed.  Every exactly-two-equal triple
   has exact period three.  Every three-distinct triple with `a+b+c!=0`
   has depth one and maps to a fixed block.
2. **Sharp census.**  There are `N^2` fixed points, `N(N-1)` strict
   three-cycles, and `N(N-1)(N-3)` depth-one points.  Hence the periodic
   locus, and also the one-step image, has size `4N^2-3N`.  The maximum tail
   is zero for `r=2` and one for `r>=3`.
3. **Every-target fibre theorem.**  A target has exactly one predecessor if
   it is diagonal or exactly-two-equal, exactly `N-2` predecessors if it is
   a three-distinct block, and no predecessor if it is a nonblock.  For a
   block `(x,y,z)`, the `N-2` sources must be parametrized explicitly as

   ```text
   (a,b,c)=(t,t+z,t+y),  t in V\{0,y,z}.
   ```

4. **Iterates and zeta.**  The image stabilizes after one step and

   ```text
   zeta_S(q)=(1-q)^(-N^2)(1-q^3)^(-N(N-1)).
   ```

The Steiner-quasigroup identities, the point-line Steiner triple system of
`PG(r-1,2)`, elementary characteristic-two algebra, and generic zeta
conversion receive zero contribution credit.  The retained residual is the
complete four-stratum functional graph together with the target-resolved
`1/(N-2)/0` inverse law.
