# P170 narrative report

## The map

Fix a labelled ground set `[n]`.  From a current subset `A`, sample a uniform
permutation `pi` and keep only those elements of `A` fixed by `pi`.  Independent
samples produce a monotone random chain.  Pathwise, the time-`t` state is the
initial set intersected with the common fixed set of all `t` sampled
permutations.

That identity makes the unmarked law transparent.  For an endpoint `B⊆A`,
all labels of `B` must be fixed at every epoch, while every label in `A\B`
must move at least once.  Inclusion--exclusion therefore gives

```text
K_t(A,B) = sum_j (-1)^j C(|A|-|B|,j) (n-|B|-j)!^t.
```

The only missing positive-time containment edge is from the full set to a
set missing exactly one label.  A permutation cannot move just one point.

## The repaired temporal boundary

Containment indicators diagonalize the one-step operator.  Rank `r` has
eigenvalue `(n-r)!/n!`; the last two ranks collide because `1!=0!`.  Setting
the endpoint to the empty set gives the complete absorption distribution,
its PGF, and its first two moments.

This collision matters at small `n`.  For `n=3`, both the two-label and the
three-label terms decay as `6^{-t}`.  They must be combined exactly:

```text
P(T>t) = a 3^{-t} - (C(a,2)-C(a,3)) 6^{-t}.
```

Consequently the usual first-two-distinct-scales expression begins only at
`n>=4`.  The note also isolates `n=1` (no absorption from the nonempty state)
and `n=2` (the same `2^{-t}` survival law for every nonempty source).

## The second axis: complete cycle-marked histories

The scalar kernel forgets how complicated the sampled permutations were.
To retain that information, weight a history by `u` to the sum of the cycle
counts of all sampled permutations.  If `s` labelled points are prescribed
fixed, the one-epoch cycle polynomial is

```text
R_(n,s)(u) = u^s product_(q=0)^(n-s-1) (u+q).
```

Endpoint inclusion--exclusion before setting `u=1` yields a polynomial for
every labelled endpoint.  Two uniform facts survive its alternating form.

- Every supported history has at least
  `t(b+1_[b<n])` cycles, and one cycle on the complement at every epoch
  attains the bound.
- If `d=a-b` labels disappear, their moved supports force total cycle
  deficit at least `ceil(d/2)`.  Transposition pairings, one three-cycle for
  odd `d>=3`, and an outside helper label for `d=1` attain the bound.

Thus the highest exponent is exactly `tn-ceil(d/2)`.  Differentiating the
same endpoint polynomial at one gives the exact conditional total-cycle
expectation.  These marked statistics cannot be reconstructed from the
unmarked history count alone.

## Ownership posture

The note does not assign contribution credit to common fixed points of random
permutations, rencontres/inclusion--exclusion calculations, Boolean
semilattice eigenbases, standard absorption transforms, or the rising-
factorial cycle polynomial.  Primary-source neighbourhoods own those pieces.
The bounded search did not locate the exact endpoint-conditioned marked
conjunction, but that non-hit is not priority evidence.  The manuscript
therefore stays `HOLD_EXTERNAL`.

## Exact pressure

The standalone author verifier regenerates uniform permutations literally,
multiplies labelled subset histories, and implements the formulas in a
separate path.  It checks exact integer coefficients, rational moments and
PGFs, support, degree endpoints, parity witnesses, the `n=3` repair, and the
Boolean-zeta basis.  Finite verification is treated only as counterexample
pressure; all uniform claims have proofs in `main.tex`.
