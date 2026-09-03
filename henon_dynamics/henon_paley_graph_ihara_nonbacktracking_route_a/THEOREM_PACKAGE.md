# Proof Package

## Claim

Let `q` be an odd prime power with `q=1 mod 4`, let `F_q` be the field of `q`
elements, and let `chi` be its quadratic character, extended by `chi(0)=0`.
The Paley graph `P(q)` has vertex set `F_q` and an undirected edge between
distinct `x,y` when `chi(x-y)=1`.  Put

```text
k=(q-1)/2,  m=qk/2,
r=(-1+sqrt(q))/2,  s=(-1-sqrt(q))/2.
```

On directed edges define the Hashimoto matrix by

```text
B[(x,y),(y,z)]=1 exactly when z is adjacent to y and z is not x.
```

Then:

1. `P(q)` is connected and strongly regular with parameters
   `(q,k,(q-5)/4,(q-1)/4)`.
2. Its adjacency spectrum is `k` once and `r,s` each `(q-1)/2` times.  In
   particular it obeys the source Ramanujan bound
   `max(|r|,|s|)<=2 sqrt(k-1)`.
3. With oriented prime cycles identified only up to cyclic shift,

```text
det(I-uB)
 = (1-u^2)^(m-q)
   (1-ku+(k-1)u^2)
   (1-ru+(k-1)u^2)^k
   (1-su+(k-1)u^2)^k.
```

   Thus the full algebraic spectrum of `B` consists of the roots of
   `z^2-lambda*z+(k-1)` for every adjacency eigenvalue `lambda`, with its
   multiplicity, together with `+1` and `-1` each `m-q` additional times.
4. If `N_n=Tr(B^n)` and `pi_n` is the number of oriented primitive
   nonbacktracking cycles of length `n`, modulo cyclic shift but not reversal,
   then

```text
N_n = sum_{d|n} d*pi_d,
pi_n = (1/n) sum_{d|n} mu(d) N_(n/d),
Z_Ihara(u)=exp(sum_{n>=1} N_n u^n/n)=det(I-uB)^(-1).
```

5. At `q=5`, the graph is `C_5`, `m-q=0`, and exactly two oriented primitive
   cycles occur at length five.

## Status

PROVABLE AS STATED.

## Assumptions and conventions

- `q` is an odd prime power, not merely an odd integer.
- The congruence `q=1 mod 4` makes `chi(-1)=1`, hence adjacency is undirected.
- A prime cycle retains orientation; reversing it normally gives another
  prime cycle.
- `Z_Ihara` is the source graph zeta.  No target Euler factor is named.

## Proof strategy and dependency map

1. Character sums give regularity, common-neighbor counts, and the adjacency
   eigenvalues.
2. A tail/head incidence calculation proves the Bass determinant without
   assuming its conclusion.
3. Factor substitution supplies the complete `B` spectrum.
4. The trace counts based closed directed nonbacktracking walks; grouping
   repetitions of prime cycles gives Möbius inversion and the Euler product in
   the source graph sense.
5. `q=5` is evaluated separately.

## Proof

### 1. Graph geometry

Because `chi(-1)=1`, `chi(x-y)=chi(y-x)`, so the graph is undirected.  Each
vertex has the `k=(q-1)/2` nonzero squares as increments.  We defer
connectedness to the character diagonalization below: it will show that the
degree eigenvalue has multiplicity one, which is equivalent to connectedness
for a regular undirected graph.

For `a` nonzero, translate two vertices to `0,a`.  Writing the indicator of a
nonzero square as

```text
J(t)=(1+chi(t)-delta_0(t))/2,
```

and using `sum_t chi(t)chi(t-a)=-1`, direct expansion gives

```text
sum_t J(t)J(t-a)=(q-3-2chi(a))/4.
```

It is `(q-5)/4` when `a` is a square and `(q-1)/4` otherwise.  This proves the
strongly regular parameters.

### 2. Adjacency spectrum

Fix a nontrivial additive character `psi` of the prime field `F_p`, and set
`psi_b(x)=psi(Tr_(F_q/F_p)(bx))`.  Convolution by the nonzero squares
diagonalizes adjacency.  The trivial character has eigenvalue `k`.  For `b`
nonzero,

```text
lambda_b = ( -1 + chi(b) G )/2,
G=sum_t chi(t)psi(Tr_(F_q/F_p)(t)),  G^2=chi(-1)q=q.
```

Changing the initial nontrivial additive character can exchange the signs of
`G` but cannot change the multiset.  Exactly half of nonzero `b` have each
quadratic-character sign.  Hence the two nontrivial eigenvalues are `r,s`,
both with multiplicity `k`.  The multiplicity-one degree eigenvalue proves
connectedness.  Finally

```text
max(|r|,|s|)=(sqrt(q)+1)/2 <= 2 sqrt(k-1)=sqrt(2(q-3)).
```

After squaring, this is `2 sqrt(q)<=7q-25`.  The right-minus-left side is
increasing for `q>=5` and equals `10-2 sqrt(5)>0` at five.  This proves the
Ramanujan inequality for the source graph only.

### 3. Bass elimination

Let `E^or` be the `2m` directed edges.  Let `S,T` be the tail and head
incidence matrices from vertices to directed edges, and let `J` reverse an
edge.  With the displayed transition convention,

```text
B=T^t S-J,  J^2=I,  SJ=T,  ST^t=A,  SS^t=kI.
```

For formal `u`, factor

```text
I-uB=(I+uJ)[I-u(I+uJ)^(-1)T^tS].
```

Since `(I+uJ)^(-1)=(I-uJ)/(1-u^2)`, the determinant lemma
`det(I-XY)=det(I-YX)` reduces the second determinant to `q` dimensions.
Multiplying that reduced matrix by `1-u^2` and inserting the four incidence
identities yields `I-uA+(k-1)u^2I`.  The reversal matrix is a direct sum of
`m` swaps, hence `det(I+uJ)=(1-u^2)^m`.  Cancelling the denominator gives

```text
det(I-uB)=(1-u^2)^(m-q) det(I-uA+(k-1)u^2I).
```

Substitution of the adjacency spectrum proves the asserted factorization.
Its total degree is `2(m-q)+2q=2m`, so it accounts for every algebraic
eigenvalue of `B`, including multiplicity.  Reading reciprocal roots gives the
stated complete spectrum.

### 4. Primitive cycles and zeta

The diagonal entry `(B^n)_(e,e)` counts length-`n` legal paths beginning and
ending at the same directed edge.  Such a path is closed, nonbacktracking,
and has no tail because the final transition into `e` is also legal.  A prime
cycle of length `d|n` has exactly `d` possible based directed edges in its
`n/d`-fold repetition.  Consequently `N_n=sum_(d|n)d*pi_d`.  Ordinary Möbius
inversion proves the formula for `pi_n`.  Finally the formal identity
`-log det(I-uB)=sum_(n>=1)Tr(B^n)u^n/n` proves the source zeta identity and its
prime-cycle product.  This is a finite algebraic identity, not a target
arithmetic Euler product.

### 5. The smallest field

For `q=5`, the nonzero squares are `{1,4}` and `P(5)=C_5`.  Here `k=2`,
`m=5`, so the excess exponent is zero.  A nonbacktracking walk on a cycle must
retain its initial orientation.  The clockwise and counterclockwise circuits
are therefore the two oriented prime cycles of length five, and there are no
shorter ones.  This proves the boundary assertion.  Therefore all parts of
the claim follow.  QED.

## Route-A boundary

The quadratic character is intrinsic source arithmetic, but the field-size
parameter is not a rational-prime primitive orbit and path length is not a
logarithmic-prime roof.  Therefore A0 is weak, while the exact primitive-cycle
layer passes A1 analytically.  A2 and A3 stop: a source Ihara determinant is
not a target determinant or divisor.  The adjacency matrix is a natural
self-adjoint source operator, but it is only an A4 formal hint.

## Open risks

- Different polynomial models of an extension field relabel vertices; the
  theorem is field-isomorphism invariant, while finite evidence locks one
  canonical polynomial model.
- The word `Ramanujan` may describe the source graph bound only.  It cannot be
  used as an RH claim about another zeta function.
