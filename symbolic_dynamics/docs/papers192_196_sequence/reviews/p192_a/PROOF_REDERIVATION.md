# P192 Review-A proof rederivation

This derivation starts from the frozen permutation product and literal
least-index map.  The history-set conjecture is not used.

## 1. Product order and local Hurwitz algebra

Multiplication is standard function composition: in `sigma rho`, `rho` acts
first.  For transpositions `x,y`, the paper's move is

```text
H(x,y)=(y,yxy).
```

The new pair has product `y(yxy)=xy`, since `y^2=e`.  Thus each update
preserves the ordered product under exactly the stated convention.  Direct
image-permutation multiplication confirms that

```text
(1,2)(2,3)...(n-1,n)=(1 2 ... n),
```

whereas the reversed factor order gives the inverse cycle for `n>=3`.

Adjacent equal factors cannot occur in a length-`n-1` factorization of an
`n`-cycle: equal adjacent transpositions cancel, leaving only `n-3` factors,
but an `n`-cycle has transposition length `n-1` because one transposition
changes the number of permutation cycles by exactly one.

## 2. Strictly advancing scheduler

At an active position write the distinct factors as `(a,b),(a,c)`, with
`a<b,c` and `b!=c`.  Conjugating swaps endpoint `a` with `c`, so

```text
H((a,b),(a,c))=((a,c),(b,c)).
```

After normalization, the two lower endpoints are `a,min(b,c)`, and the second
is strictly larger than `a`.  The collision at `i` has disappeared.  Factors
strictly before `i` are unchanged.  The only earlier comparison touching a
changed factor is at `i-1`, but position `i` retains lower endpoint `a`, so
that comparison is unchanged.  Since `i` was the least old collision, the
next selected index, if any, is greater than `i`.

Consequently update histories are strictly increasing subsets of
`{1,...,n-2}`.  Every state reaches a fixed point in at most `n-2` nontrivial
updates, and no nontrivial recurrent orbit can exist.

For `n>=3`, let

```text
w_n=((1,n),(1,2),(2,3),...,(n-2,n-1)).
```

The first move creates `(1,2),(2,n)`.  Inductively the moving factor `(j,n)`
meets `(j,j+1)` and becomes `(j,j+1),(j+1,n)`.  Hence the history is exactly
`1,...,n-2` and the terminal state is the canonical chain.  Since the chain
has product `c_n` and Hurwitz moves preserve product, the witness lies in the
carrier.  For `n=2`, the carrier consists of the one-factor word `((1,2))`,
which is fixed and realizes the sharp bound zero.

## 3. Fixed census by Pollak normalization

Put `N=n-1`.  The classical lower-endpoint map identifies the carrier with
parking functions of length `N` under the frozen orientation.  The stopping
rule says that a state is fixed exactly when adjacent letters in this parking
word are unequal.

In Pollak's circular model, take `N` preferences on `N+1` cyclic spots.  Among
all such words, adjacent entries are unequal in

```text
(N+1) N^(N-1)
```

ways: the first entry is arbitrary and each later entry avoids exactly its
predecessor.  Common translation modulo `N+1` is free and preserves those
inequalities.  Circular parking is translation equivariant and leaves one
spot empty, so every translation orbit has exactly one representative whose
empty spot is the distinguished last spot.  No car in that representative
can prefer the empty spot; deleting it gives an ordinary parking function,
and the ordinary parking procedure reverses this normalization.  Dividing by
`N+1` gives

```text
N^(N-1)=(n-1)^(n-2).
```

The argument includes `N=1`: two circular one-letter words form one
translation orbit and yield the single ordinary parking function.

## 4. Exact inverse atlas

Fix a target `y=(sigma_1,...,sigma_(n-1))`.  If a nonself source is selected
at `i`, it is uniquely determined because

```text
H_i^(-1)(u,v)=(uvu,u).
```

Write `u=sigma_i=(a,b)` with `a<b`.  The two inverse-source factors have the
same lower endpoint exactly when `v=sigma_(i+1)` contains `b` and its other
endpoint `c` satisfies `c>a`.  Indeed, conjugation by `(a,b)` changes the
endpoint `b` of `v` into `a`, producing `(a,c)`; it has lower endpoint `a`
precisely under that inequality.  Conversely, for the inverse conjugate to
contain `a`, a noncoincident `v` must contain `b`.  The coincident case is
excluded by minimality.

The inverse changes the lower endpoint at target position `i` from `a` to the
same `a`, and changes no earlier factor.  Therefore the source has no earlier
collision exactly when the target has none.  If `j(y)` is the first target
collision, the scheduler selects this reconstructed source at `i` exactly
when `i<j(y)`.  This proves necessity and sufficiency of reverse
admissibility.  Distinct counted indices cannot give the same source, because
the source's least collision recovers its index.

A self-source occurs precisely when the target is fixed: a nontrivial
Hurwitz update could equal its source only with coincident adjacent factors,
which the carrier forbids.  Adding that self-source gives the displayed
indegree formula, including the sentinel and `n=2` cases.

## 5. Maximum fibre and uniqueness

A fixed target has at most one self-source and one inverse source at each of
the `n-2` adjacent positions, so its indegree is at most `n-1`.  A nonfixed
target has no self-source and fewer eligible positions.  The canonical chain
is fixed and every position is reverse-admissible, so its indegree is `n-1`.

If a target attains equality, it is fixed and every position is admissible.
Write `sigma_i=(a_i,b_i)` with `a_i<b_i`.  Admissibility at `i` makes both
endpoints of `sigma_(i+1)` larger than `a_i`, so

```text
a_1<a_2<...<a_(n-1).
```

This lower word is a parking function.  Strict positivity gives `a_i>=i`,
while the parking inequalities give `a_i<=i`; hence `a_i=i`.  The classical
lower-endpoint bijection has one factorization over this word, and the
canonical chain is such a factorization.  It is therefore the unique
maximizer.

## 6. Conjecture quarantine

Nothing above counts complete history masks.  Finite reconstruction happens
to produce the displayed binomial depth rows through the checked range, but
this supplies neither an all-`n` Prüfer-compatible bijection nor a theorem.
The history-set formula, its summed depth formula, the claimed general unique
deepest state, and any basin formula remain conjectural and are not inputs to
Sections 1--5.

## 7. Independent finite reconstruction

`verify_review_a_p192.py` enumerates every length-`n-1` word of transpositions
through `n=6`, multiplies it literally, and retains only product `c_n`.  It
does not generate a Hurwitz orbit or invoke a tree code.  Separately it
enumerates ordinary parking functions through `n=8` and circular translation
orbits through `n=7`.  Every literal edge and target source set is compared
with the theorems.  Two runs are byte equal to `CANONICAL.txt`.

Conclusion: the proved mathematics is sound.  The source, boundary, and
four source, boundary, and companion-QA findings in `HOSTILE_REVIEW_A.md`
were repaired exactly and
accepted on recheck.  The Review-A disposition is `ACCEPTED_REPAIR`, with
zero open findings and the binding external state
`OWNER_RED_AMBER / HOLD_EXTERNAL`.
