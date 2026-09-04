# Proof package

## Claim

Fix the Hamilton quaternions

```text
S5={(1,±2,0,0),(1,0,±2,0),(1,0,0,±2)}.
```

For every prime `q>5`, `q=1 mod 4`, choose `iota^2=-1 mod q` and map
`a=(a0,a1,a2,a3)` to

```text
M_iota(a)=[[a0+iota*a1,a2+iota*a3],
           [-a2+iota*a3,a0-iota*a1]].
```

Take projective classes.  Let `X^{5,q}` be the LPS Cayley graph on the
group selected below, `A_q` its adjacency matrix, and `H_q` its oriented-edge
nonbacktracking matrix.

## Status

PROVABLE AS STATED

The connectedness and Ramanujan bound are explicitly cited LPS inputs.  The
generic determinant is the cited Bass--Hashimoto theorem.  The arithmetic
chamber closure, gauge statement, spectral mapping, trace and primitive
cycle consequences are proved below.

## Assumptions

- `q>5` is prime and `q=1 mod 4`.
- Projective determinant means its square class, which is independent of the
  scalar matrix representative.
- Prime oriented cycles are identified under cyclic shift but not reversal.

## Notation

- `chi_q=(5/q)` is the Legendre symbol.
- `G_q=PSL2(F_q)` if `chi_q=1`; `G_q=PGL2(F_q)` if `chi_q=-1`.
- `n_q=|G_q|`, `m_q=3n_q`, and the oriented-edge space has dimension
  `2m_q=6n_q`.
- `N_q(r)=Tr(H_q^r)`.
- `Pi_q(r)` is the number of prime oriented cycles of length `r`.

## Proof strategy

Use the quaternion norm to lock the six projective generators and their
inverse pairs.  Invoke the LPS congruence theorem once to identify the full
group and the adjacency bound.  Prove the two chamber geometries by the
projective determinant character.  Apply the Bass characteristic identity,
then read the complete Hashimoto spectrum and primitive cycles from its
quadratic factors.  Finish the prime-chamber density by reciprocity and the
prime number theorem for arithmetic progressions.

## Dependency map

1. The generator lemma uses only matrix multiplication and Hamilton norm.
2. The group and Ramanujan lemma uses the LPS theorem under the frozen prime
   hypotheses.
3. Chamber bipartiteness uses the determinant-square homomorphism;
   nonbipartiteness uses connectedness and simplicity of `PSL2(F_q)`.
4. The characteristic theorem uses the Bass--Hashimoto identity.
5. The trace, Möbius and spectral-circle statements use item 4 and the LPS
   adjacency bound.
6. The density statement uses quadratic reciprocity and the prime number
   theorem for arithmetic progressions.

## Main theorem

For every eligible prime `q` the following statements hold.

1. The six projective matrices are distinct, inverse-closed generators.
   Replacing `iota` by `-iota` conjugates every generator by the same
   projective matrix, so the graph and its dynamics are gauge independent.
2. The LPS graph is connected and six-regular.  If `chi_q=1`, then
   `G_q=PSL2(F_q)`, `n_q=q(q^2-1)/2`, and the graph is nonbipartite.  If
   `chi_q=-1`, then `G_q=PGL2(F_q)`, `n_q=q(q^2-1)`, and the graph is
   bipartite with the two determinant-square classes as equal parts.
3. The exact characteristic factorization is

   ```text
   det(t I-H_q)=(t^2-1)^(2n_q) det(t^2 I-t A_q+5I).
   ```

   Equivalently,

   ```text
   det(I-uH_q)=(1-u^2)^(2n_q)det(I-uA_q+5u^2I).
   ```

4. If `lambda` is an adjacency eigenvalue, the corresponding two Hashimoto
   roots solve `mu^2-lambda*mu+5=0`; the remaining roots are `+1` and `-1`,
   each with multiplicity `2n_q`.  The trivial eigenvalue `lambda=6`
   supplies `mu=5,1`.  The eigenvalue `lambda=-6`, hence `mu=-5,-1`, occurs
   exactly in the bipartite chamber.  Every other quadratic root satisfies
   `|mu|=sqrt(5)`.
5. `N_q(r)` counts closed, cyclically nonbacktracking oriented walks of
   length `r`, and

   ```text
   Pi_q(r)=(1/r) sum_{d|r} mobius(d) N_q(r/d).
   ```

   As a formal power series, hence as a rational function,

   ```text
   Z_q(u)=prod_[prime oriented C](1-u^length(C))^(-1)
         =exp(sum_{r>=1}N_q(r)u^r/r)
         =det(I-uH_q)^(-1).
   ```

6. Among eligible primes, the two chambers each have conditional natural
   density `1/2`: residues `q=1,9 mod 20` give `PSL2`, while residues
   `q=13,17 mod 20` give `PGL2`.

## Proof

### Step 1: generator and gauge lemma

Direct expansion gives

```text
det M_iota(a)=a0^2+a1^2+a2^2+a3^2.
```

Thus every frozen matrix has determinant five.  Quaternion conjugation
changes the unique `±2` coordinate's sign and satisfies
`M(a)M(conj(a))=5I`; in projective space the paired classes are inverses.
For `q>5`, no frozen matrix is scalar and no two are projectively equal:
their diagonal or off-diagonal difference would force `2=0`, `4=0`, or
`5=0 mod q`.  Hence the Cayley graph is simple and six-regular once the
group is generated.

Let `J=[[0,1],[-1,0]]`.  Entrywise multiplication verifies

```text
M_{-iota}(a)=J M_iota(a) J^(-1).
```

The two choices of square root therefore give conjugate generator sets and
isomorphic labeled dynamics.

### Step 2: arithmetic group and chambers

The LPS theorem for two distinct primes congruent to one modulo four,
specialized to quaternion prime five, proves connectedness, identifies the
generated group as `PSL2(F_q)` when five is a square and `PGL2(F_q)` when it
is not, and proves the Ramanujan adjacency bound.  The standard orders give
the stated values of `n_q`.

The determinant square class is well defined on `PGL2`, because multiplying
a representative by a scalar multiplies its determinant by a square.  In
the nonresidue chamber every generator has nonsquare determinant, so every
edge flips the character.  This is a bipartition.  Connectedness makes both
parts nonempty and right multiplication by any generator bijects them, so
they are equal.  In the residue chamber the group is `PSL2(F_q)`.  A
connected bipartite Cayley graph would make word-length parity a nontrivial
homomorphism from `PSL2(F_q)` to the group of order two; its kernel would
have index two.  For `q>=13`, `PSL2(F_q)` is nonabelian simple, so no such
homomorphism exists.  This proves nonbipartiteness.

### Step 3: determinant, traces and primitive cycles

For a finite graph without degree-one vertices, the Bass--Hashimoto theorem
states

```text
det(I-uH)=(1-u^2)^(m-n) det(I-uA+u^2(D-I)).
```

Here `D=6I` and `m=3n`, giving exponent `2n` and coefficient five.  Replacing
`u` by `1/t` and multiplying by `t^(6n)` yields the characteristic form.
Both sides have degree `6n`, so the displayed roots form the complete
Hashimoto spectrum, including multiplicities.

By the definition of `H`, a diagonal entry of `H^r` is one exactly for a
closed oriented-edge walk whose adjacent edges, including the last and
first, are never mutual reverses.  Summing the diagonal proves the trace
interpretation.  Every such closed walk is a unique repeat of a prime
oriented cycle.  Therefore

```text
N_q(r)=sum_{d|r} d Pi_q(d),
```

and Möbius inversion proves the formula.  Taking a formal logarithm of the
finite determinant, or grouping repeats of each prime cycle, proves the
three equal forms of `Z_q`.

### Step 4: Ramanujan spectral circle

The LPS theorem gives `|lambda|<=2sqrt(5)` for every adjacency eigenvalue
other than the trivial `6` and, in the bipartite case, `-6`.  If
`|lambda|<2sqrt(5)`, the roots of `mu^2-lambda*mu+5` are conjugate and their
product is five, so both have modulus `sqrt(5)`; equality gives the repeated
real roots `±sqrt(5)`.  The trivial quadratics factor as
`(mu-1)(mu-5)` and `(mu+1)(mu+5)`.  A connected regular graph has `-6` as
an adjacency eigenvalue exactly when it is bipartite.  Step 2 therefore
proves the claimed chamber dependence.

### Step 5: chamber density

Quadratic reciprocity has no sign correction for five, so `(5/q)=(q/5)`.
Eligible primes occupy the four reduced residue classes `1,9,13,17 mod 20`.
The first two are `±1 mod 5` and have symbol one; the last two are `±2 mod 5`
and have symbol minus one.  The prime number theorem for arithmetic
progressions gives each class natural density `1/8` among all primes, hence
density `1/4` after conditioning on `q=1 mod 4`.  Each pair therefore has
conditional density `1/2`.

This completes the proof. ∎

## Corrections or missing assumptions

- None.  The result explicitly separates package derivations from the LPS
  and Bass--Hashimoto source theorems.

## Open risks

- The theorem does not assemble the finite `q`-graphs into one autonomous
  global flow.
- The circle `|mu|=sqrt(5)` is a source graph-spectral statement, not a
  target critical-line or zero-correspondence claim.
- HCS-C329 retains the generic determinant-mechanism ownership.
- The exact primitive-cycle theorem is internal to each source graph.  It
  provides neither an orbit-level prime label nor `p <-> gamma_p`, prime-power,
  intrinsic `log p`/von Mangoldt, phase, or stability data.  The mandatory
  shuffled-period, random-weight, random-phase, and same-density-length
  controls are absent at the A1 orbit-correspondence layer.  Exact
  wrong-residue-prime, matched-composite, and cyclic chamber-label-shuffle
  tests are executed at A0 and do not fill that gap.  Strict evaluator v0.2
  therefore records `A1_WEAK` and overall `ROUTE_A_EXPLORATORY`.
