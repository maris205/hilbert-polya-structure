# Final frozen theorem contracts — P147–P151

These are claim ceilings after the P1–P146 collision firewall and the closest
primary-owner subtraction.  A manuscript may narrow a statement after hostile
review but may not silently broaden it.  Exact enumeration is counterexample
pressure only.  Every paper is anonymous and remains `HOLD_EXTERNAL`.

## P147 — simultaneous adjacent-run consolidation

Let `Comp(n)` be the positive integer compositions of `n`.  In each maximal
constant run `s^r`, replace all `r` copies simultaneously by the single part
`rs`; call the resulting self-map `A_n`.

1. Prove that total weight is preserved and that the number of parts strictly
   decreases off the fixed set.  The fixed points are exactly the Carlitz
   compositions (adjacent parts unequal).  Their classical enumeration is
   background and receives zero contribution credit.
2. Prove the pointwise dependency-chain upper bound and the sharp all-size
   clock

   ```text
   max_{alpha in Comp(n)} tau(alpha)=floor(log_2 n).
   ```

   Supply an explicit depth-achieving composition for every `n`, not only for
   powers of two.
3. For a target `beta=(b_1,...,b_k)`, prove the complete length-refined
   one-step fibre polynomial

   ```text
   Phi_beta(u)=sum u^(sum_i b_i/s_i),
   ```

   where the sum ranges over divisors `s_i|b_i` with
   `s_i != s_(i+1)`.  Thus `[u^ell]Phi_beta` counts exactly the predecessors
   with `ell` parts, `Phi_beta(1)` is the full indegree, and nonvanishing is
   the exact image test.
4. Ordinary run-length encoding, maximal-run statistics, locally restricted
   compositions, and Carlitz generating functions are zero-credit inputs.
   The residual is the literal weight-preserving iteration, sharp every-`n`
   clock, and divisor-path every-target inverse.

## P148 — even-level contraction of plane rooted trees

Let `PT_{<=N}` be the finite disjoint union of plane rooted trees with at most
`N` vertices.  For a tree `T`, delete every odd-depth vertex, promote its
ordered child block to its parent, and recurse from every retained even-depth
vertex; call the result `E(T)`.  The one-vertex tree is fixed.

1. Prove that `E^k(T)` retains exactly the original vertices whose depths are
   divisible by `2^k`, with ancestry and contour order induced from `T`.
   Hence

   ```text
   h(E(T))=floor(h(T)/2),
   tau(T)=ceil(log_2(h(T)+1)),
   max_{|T|=n} tau(T)=ceil(log_2 n),
   ```

   with paths as equality witnesses.  The singleton is the unique fixed
   point.
2. If a target `U` has `m` vertices and `I(U)` internal vertices, prove the
   source-size-refined every-target fibre identity

   ```text
   sum_{E(T)=U} y^(|T|-m)=y^I(U)/(1-y)^(2m-1).
   ```

   Equivalently, among sources of exact size `n`, the fibre has size

   ```text
   binom(n-m-I(U)+2m-2, 2m-2)
   ```

   when `n-m>=I(U)`, and is empty otherwise.
3. Deduce the exact image condition `m+I(U)<=n` for sources of size `n`, and
   derive the algebraic image generating function from the local plane-tree
   specification.  The manuscript must distinguish an exact-size source
   layer from the finite self-map carrier `PT_{<=N}`.
4. **Post-freeze owner amendment:** Soo--Khoussainov--Linz
   outward-contraction directly owns the unordered rooted one-step shadow.
   That rule, its partition-tree interpretation, and bare height compression,
   together with Catalan carrier counts, generic ordered-tree contraction,
   even/odd level statistics, and Horton/leaf pruning, are zero-credit inputs.
   Iterating the unordered owner also makes the unordered all-rank depth and
   clock consequences cheap, so they are not scored alone.  The residual is
   only the conjunction of the plane-order every-target size-refined inverse,
   its exact-layer image criterion, and the algebraic image series.

## P149 — standardized endpoint-peak extraction

Let `S_{<=N}=disjoint_union_{1<=m<=N} S_m`.  Give both endpoints the fictitious
neighbour value zero.  Read all local-maximum values from left to right and
standardize that nonempty word; this defines `P:S_{<=N}->S_{<=N}`.

1. Prove for every `n,k>=1` the exact iterate image

   ```text
   P^k(S_n)=disjoint_union_{1<=m<=ceil(n/2^k)} S_m,
   |P^k(S_n)|=sum_{m<=ceil(n/2^k)} m!.
   ```

   Both inclusions must be proved.  Construct an explicit right section at
   every rank by alternating high values in the target order with small
   valleys and appending the unused low values in decreasing order.
2. Prove the pointwise packing upper bound and the sharp clock

   ```text
   max_{pi in S_n} tau(pi)=ceil(log_2 n),
   ```

   with a recursively lifted equality witness for every `n`.  The singleton
   is the unique recurrent state.
3. Give the complete one-step target multiplicity.  Sum over comparison words
   whose endpoint-inclusive peak positions have the target length; for each
   word count linear extensions of the associated zigzag poset after adjoining
   the order relations that impose the target's standardized peak-value
   order.  Prove that this sum is exactly `|P^{-1}(sigma) cap S_n|`.
4. Ji's exact two-zero static exterior-peak statistic, Fu's one-sided exterior
   peaks, ordinary peak/pinnacle sets, admissible pinnacle orderings, static
   enumeration, and generic zigzag-poset technology receive zero credit.  The
   residual is the repeated extraction, all-rank image/right-section theorem,
   sharp logarithmic clock, and target-resolved multiplicity.

## P150 — zero-totalized Lyness dynamics over odd finite fields

For every finite field `F_q` of odd order, put `inv0(0)=0` and
`inv0(x)=x^{-1}` for `x!=0`.  Study the literal all-affine self-map

```text
L(x,y)=(y,(1+y)inv0(x))
```

on `F_q^2`.  Let `r_q` be the number of roots in `F_q` of
`a^2-a-1`.

1. Partition the whole affine plane, disjointly and pointwise, into the
   generic Lyness locus, the two coordinate axes, and three exceptional tail
   layers.  Prove the temporal polynomial

   ```text
   (q^2-3q+5)+(q-1)z+(q-2)z^2+(q-2)z^3.
   ```

   In particular the maximum tail is exactly three for every odd `q`.
2. Prove the complete recurrent/cycle census: `q^2-3q+5` recurrent points,
   `1+r_q` fixed points, exactly two 2-cycles, `(q-3)/2` 4-cycles, and

   ```text
   ((q-2)(q-3)-r_q)/5
   ```

   5-cycles.  State the corresponding dynamical zeta factorization.
3. Prove the every-target fibre law: the fibre has size `q` at `(-1,0)`,
   size zero at `(-1,v)` for `v!=0`, and size one everywhere else.  Deduce
   `|im L|=q^2-q+1` and identify the whole singular in-tree.
4. Lyness's original cycle observation, classical five-periodicity on its
   birational domain, QRT/cluster interpretations, Kanki's distinct extended-
   space/almost-good-reduction singularity convention, and generic finite-
   field rational-map methods receive zero credit.  The residual is the zero-
   totalized all-affine boundary completion and its complete tail/cycle/fibre
   graph.

## P151 — leaf-marked first passage on unequal finite spiders

Join `r>=2` paths of positive integer edge lengths
`ell_1,...,ell_r` at a common centre.  Start simple random walk at the centre,
make all leaves absorbing, and record the absorbing leaf `I` and first-passage
time `T`.

1. Define

   ```text
   P_0=0, P_1=1, P_2=2,
   P_l=2P_(l-1)-z^2 P_(l-2),
   P=product_j P_(ell_j),
   D=rP-z^2 sum_i P_(ell_i-1) product_(j!=i)P_(ell_j).
   ```

   Prove by an excursion renewal at the centre the complete leaf-marked
   transform

   ```text
   F_i(z)=E[z^T 1_{I=i}]
         =z^ell_i product_(j!=i)P_(ell_j)(z)/D(z).
   ```

   Include the parity support and the first atom
   `Pr(T=ell_i,I=i)=1/(r 2^(ell_i-1))`.
2. With `H=sum_i ell_i^{-1}`, `L=sum_i ell_i`, and
   `C=sum_i ell_i^3`, derive

   ```text
   Pr(I=i)=ell_i^{-1}/H,
   E[T]=L/H,
   Var(T)=(C-2L)/(3H)+L^2/(3H^2).
   ```

   The endpoint and mean formulas are prior background and receive zero
   contribution credit; they are used to establish the residual results.
3. For fixed `(r,L)`, write `L=qr+s`, `0<=s<r`, and prove

   ```text
   L/(r-1+1/(L-r+1)) <= E[T]
   <= L/((r-s)/q+s/(q+1)).
   ```

   Characterize equality exactly: the lower class is a permutation of
   `(L-r+1,1,...,1)`, while the upper class consists of balanced arms.
4. Prove the precise inverse boundary.  The labelled endpoint vector recovers
   the primitive positive integer ratios `d_i` of the arm lengths but is
   invariant under a common dilation.  Adding the mean recovers the unique
   scale through

   ```text
   c^2=E[T](sum_i 1/d_i)/(sum_i d_i).
   ```

   Do not generalize this to unknown topology or unknown transition kernels.
5. Generic gambler's ruin, absorbing-chain resolvents, Chebyshev continuants,
   Pearce's general-tree endpoint/mean formulas, Sericola's generic time/place
   law and moments, Chen's general-tree hitting-time generating functions, the
   published unequal-arm endpoint exercise, equal-arm star hitting laws, and
   general tree-tomography framing receive zero credit.  The residual is the
   explicit unequal-spider continuant factorization, compact variance, sharp
   fixed-mass extremizers, and the coarse-data geometry inverse.

## Freeze rule

The five systems are frozen for anonymous internal Stage 2 drafting.  A direct
owner of any residual conjunction reopens that slot.  No theorem, source
search, verifier, review, or build authorizes novelty, priority, submission,
public posting, specialist contact, or release; all external action remains
`HOLD_EXTERNAL`.
