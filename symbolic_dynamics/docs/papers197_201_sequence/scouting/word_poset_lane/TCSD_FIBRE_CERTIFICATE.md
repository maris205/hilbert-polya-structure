# TCSD fibre extremum certificate

This note expands the matrix-normal-form step behind Theorem B.  Transfer
matrices themselves are standard and receive zero contribution credit; the
purpose here is to make the extremum and all equality cases auditable.

Index the three levels increasingly and write

```text
U=M_+ = [[0,1,1],       L=M_-=U^T,
         [0,0,1],
         [0,0,0]].
```

Then

```text
U^2=E_(1,3),  L^2=E_(3,1),  U^3=L^3=0,              (F1)
UL = [[2,1,0],
      [1,1,0],
      [0,0,0]].                                      (F2)
```

Consequently

```text
(UL)^m[1:2,1:2]
  = [[F_(2m+1),F_(2m)],
     [F_(2m),  F_(2m-1)]],                          (F3)
tr((UL)^m)=L_(2m).
```

Here `F_0=0,F_1=1` and `L_0=2,L_1=1`.

Contract every equality edge of a target.  Unless all edges were equal, its
fibre is the trace of a cyclic word in `U,L`.  A run of three equal matrices
vanishes by (F1), so every nonempty fibre has sign-runs of length one or two.
Let `q` be the number of doubled runs.  The number of sign runs is even, so

```text
q == r (mod 2),                                      (F4)
```

where `r` is the strict-skeleton length.

Cut the cyclic product at every rank-one block `U^2` or `L^2`.  Equations
(F1)--(F3) express the resulting trace as a product of consecutive Fibonacci
entries, one for each alternating gap between marked blocks.  Merging two
marked gaps uses

```text
F_a F_b <= F_(a+b-1),                                (F5)
```

which follows immediately from the Fibonacci addition formula.  Repeating
(F5) removes doubled runs in pairs and never decreases the comparison upper
bound.  Equality tracking in (F5) shows that a maximum has the smallest `q`
allowed by (F4):

- if `r=2m`, then `q=0`; the skeleton is one of the two alternating words
  and (F3) gives `L_(2m)=L_r`;
- if `r=2m+1`, then `q=1`; the skeleton has exactly one doubled run, and the
  rank-one coefficient from (F3) is `F_(2m)=F_(r-1)` (for `r>=3`).

Any extra doubled-run pair makes one application of (F5) strict.  Hence the
only maximizing strict skeletons are the two alternating skeletons at even
`r`, and, for odd `r>=3`, the `2r` choices of the doubled-run location and
sign.  The zero-valued `r=1` boundary is handled separately below.

The boundary values are explicit: `r=0` is the all-equality target with fibre
three; `r=1` is unrealizable and has fibre zero; `r=2` has alternating fibre
three; `r=3` has maximum one.  For a target of total length `n`, inserted
equality edges only lower `r` and do not change the contracted trace.  Lucas
and Fibonacci monotonicity therefore give:

```text
max fibre = L_(2 floor(n/2)).                         (F6)
```

At even `n>=4` equality requires `r=n` and the two alternating targets.  At
odd `n>=5` it requires `r=n-1`, hence exactly one equality edge and `2n`
targets.  The all-equality fibre creates the additional ties at `n=2,3`
listed in the theorem contract.
