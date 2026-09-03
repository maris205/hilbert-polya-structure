# P171 paper plan — Boolean Gram closure

**Status:** implemented in `main.tex` at author Round 0.  
**Lifecycle:** `GREEN_OWNER_THIN / HOLD_EXTERNAL`.

## One-sentence spine

The Boolean-Gram self-map becomes repeated squaring after one step, so its
entire temporal graph is measured by component diameters, while its complete
one-step inverse is the ordered enumeration of loop-and-edge clique covers.

## Claim architecture

### A. Literal dynamics and exact clock

- Define the carrier and Boolean multiplication entrywise.
- Interpret `G=AA^T` as the labelled row-intersection relation with loops.
- Prove for every `t>=1` that
  `Gamma^t(A)=G^(2^(t-1))`.
- Use loop padding to show that `G^r_ij=1` exactly at graph distance at most
  `r` inside an active component.
- Deduce the endpoint and the exact source-dependent depth, retaining the
  special `D<=1` convention.

### B. Complete recurrence and sharpness

- Characterize fixed/recurrent states as partial equivalence relations:
  fully looped clique components and unlooped isolates.
- Count them by choosing the active set and partitioning it:
  `sum_k binom(n,k) Bell(k)=Bell(n+1)`.
- Deduce the zeta function, since all periodic points are fixed.
- Give the path-incidence source as a uniform sharp witness for
  `1+ceil(log2(n-1))`.
- Separate `n=1`, where both carrier states are already fixed.

### C. Independent all-target inverse axis

- A target must be symmetric and every edge endpoint must be looped.
- Treat each source column as a fully looped clique support of the target.
- Introduce loop singleton and unordered-edge atoms `E*(H)`.
- Apply inclusion--exclusion to missed atoms to obtain
  `sum_{S subset E*} (-1)^|S| c_H(S)^n`.
- Preserve labelled column order, repeats, and empty columns.
- Deduce the image criterion: at most `n` allowed nonempty cliques cover all
  loop/edge atoms.
- Show compatibility is not sufficient using looped `K_{2,3}` at `n=5`.

## Mandatory owner subtraction

The following do not carry the paper:

- Boolean multiplication or Gram/intersection interpretation;
- monotone Boolean powers or repeated-squaring transitive closure;
- connectivity, distance doubling, or partial equivalence relations;
- Bell enumeration and the formal zeta conversion;
- set-intersection representations and edge clique covers;
- exact or approximate symmetric Boolean matrix factorization;
- inclusion--exclusion.

Fitting's Boolean-power chain, Erdős--Goodman--Pósa's intersection-cover
equivalence, and Chen--Song--Tao--Zhang's `M=WW^T` factorization formulation
are cited next to the corresponding mechanisms.  The retained value is only
the exact joint finite-dynamics/fibre package for the literal self-map.

## Boundary and evidence plan

- `n=1`: height zero; zero and one are fixed.
- zero matrix: fixed; zero target fibre one.
- `D=0,1`: nonfixed sources have depth one.
- target with an unlooped incident edge: fibre zero.
- isolated loop: singleton atom and fibre `2^n-1` in the one-loop target.
- empty columns: allowed and used for padding a cover of size `<n`.
- repeated columns: allowed and distinguished only through their labelled
  positions.
- exhaustive source/codomain comparison through `n=4` and sharp path replay
  through `n=64`.

No external release action is authorized by this plan.

