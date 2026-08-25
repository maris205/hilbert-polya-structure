# C139 proof package

## Claim and status

**Status: PROVABLE AS STATED.**  For the frozen forward binary coding, the
four-block marker roof below has the stated exact determinant and all-period
primitive product; it separates a primitive pair that no roof depending on at
most three forward symbols can separate by periodic sums; it remains
noninjective on primitive orbits.

## Assumptions and notation

Let `Sigma={0,1}^Z` with left shift `sigma`.  Put

```text
tau_00=1, tau_01=sqrt(2), tau_10=sqrt(3), tau_11=sqrt(6), eta=sqrt(5),
r(x)=tau_(x0,x1)+eta*1_[x0x1x2x3=0011].
```

The suspension identifies `(x,t+r(x))` with `(sigma(x),t)`.  For a cyclic
word `w`, `N_ab(w)` and `N_0011(w)` count occurrences at every cyclic starting
coordinate.  Set

```text
ell(w)=N00+sqrt(2)N01+sqrt(3)N10+sqrt(6)N11+sqrt(5)N0011.
```

Rows and columns of `M_139` are ordered as
`000,001,010,011,100,101,110,111`.

## Dependency map

1. The determinant uses the explicit eight-state matrix and a one-entry
   cofactor computation around `y=1`.
2. The all-period product uses the cyclic-word/path bijection, the formal
   log-determinant identity, and unique primitive roots.
3. Clock-sector separation uses rational independence of the five displayed
   radicals.
4. Minimal forward memory uses equality of cyclic block-count vectors through
   width three.
5. The residual obstruction is an explicit primitive, nonrotation pair.

## Theorem 1: exact eight-state determinant

For `d in {0,1}`, give `abc -> bcd` weight
`x_ab y^(1_[abcd=0011])`.  Explicitly,

```text
M_139 =
[x00 x00  0    0    0    0    0    0  ]
[ 0   0  x00 x00y  0    0    0    0  ]
[ 0   0   0    0   x01 x01   0    0  ]
[ 0   0   0    0    0    0  x01 x01 ]
[x10 x10  0    0    0    0    0    0  ]
[ 0   0  x10 x10   0    0    0    0  ]
[ 0   0   0    0   x11 x11   0    0  ]
[ 0   0   0    0    0    0  x11 x11 ].
```

Then

```text
Delta_139(x,y)=det(I-M_139)
 =1-x00-x11-x01*x10+x00*x11
  +(1-y)*x00*x01*x10*x11.                         (1)
```

**Proof.**  Only entry `(001,011)` depends on `y`, so the determinant is
affine in `y`.  At `y=1`, a closed path in the three-block presentation is
bijective with a closed path in the two-state edge presentation: a cyclic
binary word sends its coordinate `j` to state
`w_j w_(j+1) w_(j+2)`, and the first symbol recovers the word.  Therefore the
two matrices have equal traces in every positive power.  Applying
`-log det(I-A)=sum_(n>=1) Tr(A^n)/n` in the formal degree completion, whose
constant term is zero on both sides, gives

```text
det(I-M_139(x,1))=1-x00-x11+x00*x11-x01*x10.      (2)
```

For completeness, differentiate the determinant with respect to `y`.  The
derivative of `(I-M)_(001,011)` is `-x00`.  Write
`a=x00,b=x01,c=x10,d=x11`.  Deleting row `001` and column `011` from
`I-M(x,1)` gives the cofactor minor

```text
[(1-a) -a   0   0   0   0    0  ]
[  0    0   1  -b  -b   0    0  ]
[  0    0   0   0   0  -b   -b  ]
[ -c   -c   0   1   0   0    0  ]
[  0    0  -c   0   1   0    0  ]
[  0    0   0  -d  -d   1    0  ]
[  0    0   0   0   0  -d  (1-d)].
```

Only the first and fourth rows meet the first two columns.  Laplace expansion
in those columns gives the factor
`det([[(1-a),-a],[-c,-c]])=-c` times

```text
Q=[[1,-b,-b,0,0], [0,0,0,-b,-b], [-c,0,1,0,0],
   [0,-d,-d,1,0], [0,0,0,-d,1-d]].
```

Replace the third row of `Q` by that row plus `c` times the first.  Expanding
the first column and then the resulting second row gives `det(Q)=-bd`: the two
nonzero contributions are `-b^2*c*d` and `-bd*(1-bc)`.  Hence the cofactor is
`(-c)(-bd)=bcd=x01*x10*x11`, and
`partial_y Delta=-x00*x01*x10*x11`.  Integrating from `y=1` and using (2)
proves (1).  The producer also evaluates the full eight-by-eight Leibniz sum;
the independent SymPy reconstruction obtains the same seven monomials.  ∎

## Theorem 2: all-period trace and primitive product

For every `n>=1`,

```text
Tr(M_139(x,y)^n)
 = sum_(rooted cyclic binary words w, |w|=n)
   y^N0011(w) product_ab x_ab^Nab(w).              (3)
```

Consequently, in the total-transition-degree completion,

```text
Delta_139(x,y)
 = product_[gamma primitive]
   (1-y^N0011(gamma) product_ab x_ab^Nab(gamma)).  (4)
```

**Proof.**  A term in a diagonal entry of `M^n` is a closed state path.
Overlapping consecutive three-block states determine exactly one rooted cyclic
binary word; conversely the cyclic word supplies exactly that path.  The
product of transition weights records each directed edge and each `0011`
start once, proving (3).

The formal matrix has entries of positive transition degree, so

```text
-log det(I-M)=sum_(n>=1) Tr(M^n)/n.
```

Every rooted periodic word is a unique repetition `gamma^k` of a primitive
necklace, and a primitive necklace of length `m` contributes its `m` rooted
rotations to period `mk`.  Its total logarithmic contribution is therefore
`sum_(k>=1) q_gamma^k/k=-log(1-q_gamma)`, with
`q_gamma=y^N0011 product x_ab^Nab`.  Only finitely many necklaces occur in
each total degree, so regrouping is coefficientwise finite.  Exponentiation
proves (4) without a period cutoff.  ∎

After `x_ab=z exp(-s tau_ab)` and `y=exp(-sqrt(5)s)`, (4) becomes

```text
Delta_139(z,s)=product_gamma
 (1-z^|gamma| exp(-s ell(gamma))).                 (5)
```

For any specialization at which the entrywise absolute-value matrix has
spectral radius below one, the trace logarithm converges absolutely; (5) then
follows analytically from the already proved formal identity.

## Lemma 3: rational independence of the clock basis

The numbers `1,sqrt(2),sqrt(3),sqrt(6),sqrt(5)` are linearly independent over
`Q`.

**Proof.**  The first four form the standard basis of the biquadratic field
`K=Q(sqrt(2),sqrt(3))`: applying the four independent sign changes to a
rational relation and summing with the appropriate signs isolates every
coefficient.  It remains to show `sqrt(5)` is not in `K`.  If it were, each of
the four automorphisms of `K` would send it to a root of `X^2-5`, hence to
`+sqrt(5)` or `-sqrt(5)`.  Its orbit would have size at most two, so a
nonidentity automorphism would fix it.  The three nonidentity fixed fields are
`Q(sqrt(2))`, `Q(sqrt(3))`, and `Q(sqrt(6))`.  But if
`sqrt(5)=a+b sqrt(m)` with rational `a,b` and `m in {2,3,6}`, squaring gives
`2ab=0`; `b=0` would make `sqrt(5)` rational, while `a=0` would require
`m b^2=5`, impossible for rational `b` in all three cases.  Therefore
`sqrt(5) notin K`, proving independence.  ∎

It follows immediately that equal suspension lengths imply equal full
five-component feature vectors.  This is feature-sector injectivity, not
orbit injectivity.

## Theorem 4: minimal forward-memory separation

The primitive words

```text
w =001011,       w'=001101
```

have common cyclic block counts

```text
k=1: (3,3),
k=2: (1,2,2,1),
k=3: (0,1,1,1,1,1,1,0),
```

in lexicographic block order, but `N_0011(w)=0` and `N_0011(w')=1`.
Therefore every forward locally constant roof depending on at most three
consecutive symbols gives them the same periodic sum, whereas the frozen roof
gives `ell(w')-ell(w)=sqrt(5)`.

**Proof.**  If a roof depends on `k` forward symbols through values
`phi(a_0...a_(k-1))`, its periodic sum is the dot product of `phi` with the
cyclic `k`-block count vector.  The displayed vectors, obtained by listing the
six cyclic starts, agree for `k=1,2,3`; hence every such dot product agrees.
The edge counts also agree, while direct listing of the four-block starts
finds zero versus one occurrence of `0011`.  The radical-basis lemma makes the
resulting difference exactly nonzero.  A nontrivial period of a length-six
word must divide six and hence be `1`, `2`, or `3`; direct comparison with the
corresponding repeated prefix excludes all three for each word.  Both are
primitive.  Their different cyclic marker counts also exclude one being a
rotation of the other, so this is a genuine two-orbit witness.  ∎

This minimality is relative to the frozen forward binary coding.  No
cohomology-invariant or recoding-invariant minimality is claimed.

## Proposition 5: retained obstruction and nonlattice control

The primitive nonrotation words `0101111` and `0110111` both have feature
vector `(0,2,2,3,0)`.  Hence the new clock is not orbit injective.  They occur
at period seven; exhaustive replay verifies that period seven is the first
collision in this frozen feature map, but that finite minimal-period statement
is a sentinel result rather than the proof of any infinite claim.

The fixed cycles `[0]` and `[1]` have lengths `1` and `sqrt(6)`, so no positive
number generates both lengths over the integers; the roof is nonlattice.  If
the specialized finite exponential polynomial at fixed `z=1` had an imaginary period `iT`,
its distinct `e^{-s}` and `e^{-sqrt(6)s}` coefficients would force
`e^{-iT}=e^{-iT sqrt(6)}=1`, contradicting irrationality unless `T=0`.

## Route-A conclusion and open risks

The exact result advances clock resolution while proving its next internal
obstruction.  It supplies no target divisor, target functional equation,
Gamma factor, counting law, arithmetic/local data, natural self-adjoint or
unitary lift, Hilbert--Polya operator, or Route-B authorization.  Conservative
verdict: `(A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`, overall
`ROUTE_A_EXPLORATORY`.
