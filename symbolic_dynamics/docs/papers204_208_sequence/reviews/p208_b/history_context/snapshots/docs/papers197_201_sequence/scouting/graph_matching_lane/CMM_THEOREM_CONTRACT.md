# CMM theorem contract: odd-cycle monomer matching

**Candidate status:** `PROVISIONAL_AMBER_HOSTILE_GATE`; `HOLD_EXTERNAL`.
The statements below are an internal theorem contract, not a novelty claim.

## 1. Literal map and conventions

Let `n=2m+1>=3`, label the vertices of the cycle `C_n` by
`0,1,...,n-1` clockwise, and write

```text
e_i={i,i+1 mod n}.
```

The carrier `M_n` is the set of all matchings.  A monomer is an unmatched
vertex.  Every state has an odd, nonzero number of monomers.

Define `F:M_n -> M_n` as follows.

1. If there are at least three monomers, let `a` be the least monomer in the
   ordinary label order and let `b` be the next monomer encountered clockwise
   from `a`.  Flip membership of every edge on the clockwise `a`--`b` arc.
2. If `a` is the unique monomer, flip `e_a` and `e_(a+1)`.  Equivalently, slide
   the first clockwise dimer into `a`, so the new monomer is `a+2 mod n`.

The two cases exhaust the carrier, so no tie or failure branch remains.  For
formal totality, an unreachable failure branch would hold.

## 2. Exact temporal theorem

If a matching has at least three monomers, the open arc between consecutive
monomers has no unmatched vertex.  Its internal vertices are therefore
perfectly matched.  The arc has odd length and its edge pattern is

```text
0,1,0,1,...,0.
```

Flipping the whole arc gives `1,0,1,0,...,1`, still a matching, and removes
exactly the two endpoint monomers.  Consequently

```text
|F(M)|=|M|+1
```

until `|M|=m`.  Every point has exact tail

```text
tau(M)=m-|M|.
```

The global maximum is `m`, attained uniquely by the empty matching.

At size `m`, the unique monomer advances by `+2`.  Since `gcd(2,n)=1`, the
`n` maximum matchings form one directed cycle of length `n`.  There are no
other recurrent states and no fixed points.

For `0<=r<=m`, the number of size-`r` matchings of `C_n` is

```text
n/(n-r) * binom(n-r,r).
```

Thus the complete depth polynomial is

```text
D_n(z)=sum_(r=0)^m [n/(n-r) binom(n-r,r)] z^(m-r).
```

The static matching formula is classical and receives zero contribution
credit; its role here is to make the functional-graph layer claim exact.

## 3. Every-target fibre theorem

Fix a target `Y` and let

```text
u=min {unmatched vertices of Y},
r=floor(u/2),
T_r=r(r+1)/2.
```

Then

```text
|F^(-1)(Y)| = T_r + 1_{|Y|=m}.                         (3.1)
```

Proof.  A noncore predecessor has two more monomers `a,b` than `Y`.  Because
`a` was the least source monomer and `b` was the next clockwise source
monomer, both satisfy

```text
0 <= a < b < u.
```

Conversely, all vertices with labels below `u` are matched in `Y`.  If `u` is
even they are tiled by `e_0,e_2,...,e_(u-2)`; if `u` is odd, vertex `0` uses
the wrap edge and the internal dimers are `e_1,e_3,...,e_(u-2)`.  In either
case there are exactly `r` consecutive dimers before `u`.  Reversing any
nonempty contiguous interval of these dimers creates one and only one source
whose selected monomers are the two interval endpoints.  There are
`1+2+...+r=T_r` choices.  If `Y` is maximum, it also has its unique predecessor
on the rotor cycle.  These sources are disjoint and exhaustive, proving (3.1).

Immediate consequences are:

- a nonmaximum target is in the first image exactly when `u>=2`;
- every maximum target is in the image;
- the unique largest fibre is the maximum matching whose monomer is `n-1`,
  and its size is

  ```text
  1+T_m=1+m(m+1)/2.
  ```

This is a complete target-indexed atlas, including all zero fibres and the
core/transient overlap boundary.

## 4. First-image census

For a nonmaximum target, `u>=2` exactly when vertices `0` and `1` are both
matched.  There are two disjoint possibilities.

- `e_0` is present; the remaining path contributes `F_(n-1)` matchings.
- Both `e_(n-1)` and `e_1` are present; the remaining path contributes
  `F_(n-3)` matchings.

Here `F_0=0,F_1=1`.  These two cases already include the supported maximum
targets with monomer at least two.  Adding the two maximum targets with
monomer `0` or `1`, which have rotor predecessors, gives

```text
|Im(F)|=F_(n-1)+F_(n-3)+2=L_(n-2)+2.                  (4.1)
```

The `n=3` boundary is included: the second summand is `F_0=0`, and the image
has size three.

## 5. Exact verification boundary

The dependency-free verifier exhausts every state for odd `3<=n<=21`.  It
checks closure, the point clock, all depth coefficients, the unique recurrent
cycle, the `+2` core motion, formula (3.1) at every target, (4.1), and the
unique fibre maximum.  The last box has 24,476 states.  No finite check is
used as a proof or novelty certificate.

## 6. Contribution subtraction and kill switches

Zero standalone credit is assigned to:

- Berge augmentation and the fact that an augmenting flip raises matching
  size by one;
- the matching numbers of a path or cycle and Fibonacci/Lucas identities;
- hard-core words, monomers/dimers, and alternating configurations;
- the rotation of the maximum-matching core;
- generic functional-graph, image, and fibre terminology.

The possible residual is only the conjunction

```text
least monomer + next-clockwise scheduler
  + one odd-cycle rotor
  + every-target triangular interval atlas.
```

Kill `CMM` if a source owns the literal update, if this conjunction is shown
to be a transparent recoding of Rule 184/GCM/another hard-core transducer, or
if hostile review decides that formula (3.1) is merely the same regular
preimage engine already subtracted for P90.  Do not promote it by citing only
the deficiency clock, Lucas image, or period `n`.

