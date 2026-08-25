# C159 proof package

## Theorem 1: recurrent mixing and dense periodic points

Let `t_s` be binary digit-sum parity, `S={s:t_s=1}`, and let `X_S` be the
binary S-gap shift.  Its renewal code is `C={10^s:s in S}`.  Since `1,2` lie
in `S`, the code contains words of lengths two and three.

For a block containing a one, separately complete its left and right partial
zero gaps to the nearest code boundaries; the two completions are admissible
because the original block occurs in the shift.  An all-zero
block of any prescribed length instead lies inside `10^(2^k)`, because
`t_(2^k)=1`.  Given two boundary-aligned extensions, code words of lengths
two and three fill every sufficiently large connector length.  Therefore
`X_S` is topologically mixing.  Repeating any finite code concatenation gives
a periodic point in its cylinder; repeating `10^(2^k)` handles cylinders
around the all-zero point.  Periodic points are dense.

A recurrent transitive point can be made without an inference shortcut.
Enumerate the admissible blocks.  Inductively form a boundary-aligned block
that contains the preceding block twice and the next enumerated block once,
using length-two/three code fillers.  A centered subsequential limit contains
every admissible block and returns to every cylinder determined by an earlier
nested block.  Its orbit is dense and the point is recurrent.

## Theorem 2: exact renewal zeta and entropy

Put

```text
T(z)=sum_(s>=0) t_s z^s,             F(z)=zT(z),
P(z)=product_(j>=0)(1-z^(2^j)).
```

Expanding the product chooses each binary power at most once, so the
coefficient of `z^s` is `(-1)^(t_s)`.  Hence

```text
P(z)=1/(1-z)-2T(z),   T(z)=(1/(1-z)-P(z))/2.                 (1)
```

Every nonzero periodic point has a unique circular parse at its ones.  In
`-log(1-F)=sum_(q>=1)F^q/q`, division by `q` removes the `q` possible marked
code boundaries in a cyclic codeword list; converting boundary marks to the
`n` possible shift origins gives the coefficient `Fix(sigma^n)/n`.  Hence the renewal
part is `(1-F)^(-1)`; the all-zero fixed point gives the extra factor
`(1-z)^(-1)`.  Thus

```text
zeta_X(z)=1/((1-z)(1-F(z)))
         =2/(2-3z+z(1-z)P(z)).                              (2)
```

The positive series `F(r)` increases from zero to infinity on `0<r<1`.
There is a unique `R` with `F(R)=1`, and renewal-word growth gives
`h_top=-log R`.  Exact rational tail bounds certify

```text
0.67633710444063914 < R < 0.67633710444063915.
```

## Theorem 3: unit-circle natural boundary

Let `omega` be a root of unity of order `2^m`.  For `0<r<1`, split the
product at `m`.  The finite prefix has modulus at most `2^m`, while every
tail factor is `1-r^(2^j)` and lies in `[0,1]`.  In particular,

```text
|P(r omega)| <= 2^m (1-r^(2^m)) -> 0.                       (3)
```

Dyadic roots are dense on the unit circle.  If `P` had a meromorphic
continuation across an open arc, (3) prevents any dyadic root in the arc from
being a pole; each is instead a zero or removable zero.  Their accumulation
inside the continuation domain would force the continuation to vanish
identically, contradicting `P(0)=1`.  Thus `P` has no meromorphic continuation
across any arc.

Equation (2) defines a meromorphic continuation of the Artin--Mazur zeta in
the open unit disk.  If it crossed an arc, choose a smaller subarc avoiding
`z=1`; then

```text
P(z)=(2/zeta_X(z)-2+3z)/(z(1-z))
```

would continue meromorphically across that subarc, a contradiction.  Hence
the unit circle is a natural boundary for this source meromorphic
continuation.

## Boundary

The strict tuple is

```text
(A1_WEAK,A2_FAIL,A3_PARTIAL_ANALYTIC_STRUCTURE,A4_FAIL).
```

`A2_FAIL` is deliberate: an exact source zeta is not a target divisor test.
The A3 promotion records only the proved source continuation/natural boundary
and explicitly does not claim a target global-structure comparison.  Route B
remains unauthorized.
