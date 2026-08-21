# Frozen theorem contract

## Input lock and status

This Stage-2 package treats `/tmp/p49_53_phase1` as a read-only input.  Its
`SHA256SUMS.txt` has SHA-256

```text
7fd51d53d077e3d7e0af905eda6bf2d15ee9aa64d6459bf3dcfa1dc282d97ec8
```

and every entry in that manifest was rehashed before the Stage-2 tests ran.
The per-file values are frozen in `evidence/input_hashes.json`.  Nothing in
this directory is an authority, publication, manuscript, or priority claim.

## Frozen objects

Fix an integer `p >= 3`.  For every nonzero integer `m`, put

```text
nu_p(m) = max { e >= 0 : p^e divides m }.
```

For composite `p`, this is the **p-divisibility exponent**, not a `p`-adic
valuation.  The argument never applies `nu_p` to zero: `(p-1)k+1 != 0` for
every integer `k` because `p-1 >= 2`.

A frozen directive is a bi-infinite periodic sequence `u=(u_n)_{n in Z}`
over a finite alphabet `A` satisfying all of the following.

1. `A={u_0,...,u_{h-1}}`, where `h` is the least period of `u`.
2. `h >= 2`.
3. `u_n != u_{n+1}` for every `n`, including the cyclic pair
   `u_{h-1} != u_0`.

Define

```text
L_p(k)       = (p-1)k+1,
x_{p,u}(k)   = u_{nu_p(L_p(k))},                 k in Z,
X_{p,u}      = closure { sigma^t x_{p,u} : t in Z },
T_{p,u}      = (X_{p,u}, sigma, x_{p,u}).
```

The distinguished point is part of the object.  A morphism
`F:T_{p,u}->T_{p,v}` is a continuous **onto** shift-commuting map with
`F(x_{p,u})=x_{p,v}`.  Source and target always have the same frozen base
`p`.

For `N>=1`, set

```text
r_N = 1+p+...+p^(N-1) = (p^N-1)/(p-1).
```

`Per_q(x)` denotes the positions whose letters are `q`-periodic along the
whole arithmetic progression.  For constructiveness, the essential period
of a finite block is used in the Hosseini--Yassawi sense: the least common
period of all positions in that block, not the ordinary overlap period of an
isolated finite word.

## Theorem A: exact skeleton and constructiveness split

For every integer `p>=3` and every frozen directive `u`:

1. `x_{p,u}` is an aperiodic normal simple Toeplitz sequence.
2. Its exact skeleton is

   ```text
   Per_{p^N}(x_{p,u}) = Z \ (r_N+p^N Z)             (N>=1).
   ```

3. Every `p^N` is essential; `(p^N)_{N>=1}` is a period structure.
4. Let `B_N=x_{p,u}[0,p^N-1]`.  The period structure is constructive in
   the precise Hosseini--Yassawi sense exactly when `p` is prime:

   ```text
   p prime     => essential-period(B_N)=p^(N+1) for every N>=1;
   p composite => essential-period(B_N)<p^(N+1) for every N>=1.
   ```

   More precisely, if `ell` is any prime divisor of a composite `p`, then
   `ell*p^N` is a common period of all positions of `B_N` and is strictly
   smaller than `p^(N+1)`.

Thus the all-integer-base essential-period statement is retained, while the
word **constructive** is restricted to the prime-base lane.

## Theorem B: high centers and pointed factor rigidity

For `c_n=r_n`, every nonzero integer offset `j` and every
`n>nu_p(j)` satisfy

```text
nu_p(L_p(c_n+j))
 = nu_p(p^n+(p-1)j)
 = nu_p(j).
```

For frozen source and target directives `u` and `v` at the same base `p`,
the following are equivalent.

1. A pointed factor map `F:T_{p,u}->T_{p,v}` exists.
2. There is a surjective letter map `lambda:A->B` such that
   `v_n=lambda(u_n)` for every `n in Z`.

When these conditions hold, both `lambda` and `F` are unique and

```text
F(z)(k)=lambda(z(k))                 (z in X_{p,u}, k in Z).
```

In particular, pointed conjugacy is exactly bijective directive-letter
relabeling, with no phase shift.

## Theorem C: quotient preorder, poset, and graph counts

For a frozen directive `u` on `A`, let `G_u` be the finite simple graph with
vertex set `A` and edge set

```text
{ {u_i,u_{i+1}} : i in Z/hZ }.
```

A set partition `P` of `A` is **admissible** exactly when every block is an
independent set of `G_u`.  Equivalently, it does not merge any cyclically
adjacent directive letters.  The quotient directive uses all of its block
letters, is cyclic-neighbor-distinct, and automatically has least period at
least two; it is always reduced to that least period.

Fixing `T_{p,u}`, its pointed factor targets inside the frozen same-base
family, modulo pointed conjugacy, are in bijection with admissible
partitions of `A`.  An arrow from the target represented by `P` to the one
represented by `Q` exists exactly when `P` refines `Q`, and that arrow is
unique.  With actual relabeled target objects retained this slice is a thin
category, hence a preorder.  After identifying pointedly conjugate targets,
it is precisely the refinement poset of admissible partitions.  No lattice
claim is made.

Writing `S_{G_u}(k)` for the number of partitions of `V(G_u)` into exactly
`k` nonempty independent blocks gives the following fixed-source,
pointed-conjugacy-class corollaries:

```text
# k-letter targets                  = S_{G_u}(k),
minimum target-alphabet size        = chi(G_u),
a binary target exists              iff G_u is bipartite,
P_{G_u}(q)                          = sum_k S_{G_u}(k) (q)_k.
```

Here `(q)_k=q(q-1)...(q-k+1)` and `P_G` is the chromatic polynomial.  The
binary equivalence uses that `G_u` has at least one edge, so `chi(G_u)>=2`.
These statements count target classes, not labeled letter maps.

## Explicit nonclaims and kill conditions

The contract makes no assertion about:

- factor maps between different bases;
- nonpointed factor maps, shifts of the distinguished target, or maps over a
  nonzero odometer element;
- arbitrary simple Toeplitz systems outside the affine divisibility family;
- classification of all factors outside the frozen target family;
- absolute novelty or priority;
- a lattice structure on admissible partitions.

An exact earlier theorem with the same object class, pointed quantifiers,
all-radius collapse to the unique letter quotient, and the resulting
partition classification is a collision and stops further publication work.
A context-dependent pointed map within this frozen family is a mathematical
counterexample and also stops the project.

## Proof status

Under these assumptions, Theorems A--C are **PROVABLE AS STATED**.  The
remaining gate is independent proof/source/implementation audit, not an
unfilled mathematical step.
