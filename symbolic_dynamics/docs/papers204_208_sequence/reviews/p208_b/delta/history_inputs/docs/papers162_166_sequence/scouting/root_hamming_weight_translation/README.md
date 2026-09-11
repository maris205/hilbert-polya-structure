# P166 focused scout: Hamming-weight translation dynamics

**Decision: `GREEN_OWNER_THIN / HOLD_EXTERNAL`.**  This is a theorem contract,
not a paper and not a novelty or priority claim.  The owner search was bounded.

## Literal system

For every integer `n >= 2`, let

```text
X_n = (Z/nZ)^n,
w(x) = #{r : x_r != 0},
T_n(x) = x + w(x) (1,...,1).
```

The apparent `n^n`-state dynamics reduces along each free diagonal-translation
orbit, but the reduction is not the result.  If

```text
c_i = #{r : x_r=i},                 sum_i c_i=n,
```

and phase `i` denotes `x-i(1,...,1)`, then the induced map is

```text
g_c(i)=i+c_i mod n.                 (1)
```

The results below classify (1), lift the classification with the correct
multinomial weights, and separately solve every one-step target fibre.

## Frozen strongest theorem contract

### A. Complete recurrent structure for every histogram

Every cycle of `g_c` is fixed or there is exactly one nontrivial cycle.  A
nontrivial cycle `C` uses all the mass:

```text
sum_{i in C} c_i=n.
```

Consequently `C` is the positive support of `c`, and `c_i` is the clockwise
gap from `i` to the next point of `C`.  Conversely every subset `C` of size
`ell >= 2`, with these gap labels and zero labels off `C`, produces the cycle
profile `1^(n-ell) ell^1`.  Thus all periods `1,...,n` occur and there is never
more than one nontrivial cycle on a diagonal orbit.

### B. Exact global period and depth census

Let `S(n,k)` be a Stirling number of the second kind and let `P_{n,ell}` be
the number of states of least period `ell`.  Then

```text
P_{n,1}   = 1+(n-1)^n,
P_{n,ell} = ell! S(n,ell),                 2 <= ell <= n.       (2)
```

Hence

```text
#Fix(T_n^k) = sum_{ell|k, ell<=n} P_{n,ell},
zeta_T(z)   = product_{ell=1}^n
              (1-z^ell)^(-P_{n,ell}/ell).
```

Let `D_{n,d}` count states of exact preperiod `d`.  The full depth census is

```text
D_{n,0} = (n-1)^n + sum_{k=1}^n k! S(n,k),                    (3)

D_{n,d} = d! sum_{s=d}^{n-1} binom(n,s) S(s,d)
                    (n-d-1)^(n-s),          1 <= d <= n-2,    (4)

D_{n,d} = 0,                               d >= n-1.          (5)
```

In particular the maximum preperiod is exactly `n-2`.  For `n>=3`, a
histogram attains that bound somewhere precisely when it has one zero at
`z`, one two at `e`, all other entries one, and `e != z-1 mod n`.  Phase
`z+1` always has depth `n-2`; phase `z+2` also does exactly when `e=z+1`.
There are `n(n-2)` sharp histograms, `n(n-1)` sharp histogram-phase pairs,
and

```text
D_{n,n-2}=(n-1)n!/2.                                      (6)
```

The boundary `n=2` is a permutation and has no transient points.

### C. Every-target one-step fibres and their global polynomial

For an arbitrary target `y`, put

```text
m_j(y)=#{r:y_r=j}.
```

Every candidate source is uniquely `y-k(1,...,1)`.  Therefore

```text
#T_n^{-1}(y)
 = 1_{m_0 in {0,n}} + sum_{k=1}^{n-1} 1_{m_k=n-k}.           (7)
```

Equation (7) is simultaneously the exact image criterion.  It includes the
all-zero, no-zero, and empty-fibre boundaries.  Moreover, with

```text
A_0(u,z)=exp(u)+(z-1)(1+u^n/n!),
A_k(u,z)=exp(u)+(z-1)u^(n-k)/(n-k)!,       1<=k<n,
```

the complete fibre-size distribution is

```text
F_n(z)=sum_{y in X_n} z^(#T_n^{-1}(y))
      =n![u^n] product_{k=0}^{n-1} A_k(u,z).                 (8)
```

For `n>=3`, if

```text
r=floor((sqrt(8n+1)-1)/2),
```

then the largest one-step fibre is `r+1`; equality means `m_0=0` and exactly
`r` positive indices `k` satisfy `m_k=n-k`.  For `n=2` every fibre is a
singleton.

The period/depth theorems and the target-fibre theorem are logically
independent: (2)--(6) follow from forward phase paths and multinomial lifts,
whereas (7)--(8) enumerate candidate shifts backwards from a prescribed
target.

## Exact evidence

[`verify_scout.py`](verify_scout.py) independently checks:

- every state of `X_n` for `2<=n<=7` (including composite `n=4,6`);
- all weak compositions of `n` into `n` parts through `n=10`;
- the phase reduction, complete cycle classification, period census, two
  independent forms of the depth census, sharp-tail equality structure,
  every target fibre, fibre polynomial, and sharp fibre maximum; and
- 3,200 deterministic random histogram tests at
  `n=11,12,16,20,31,48,64,80`.

Two fresh executions are byte-identical to
[`canonical_output.txt`](canonical_output.txt).  The transcript contains
`2,139,713` assertions.  Enumeration is falsification support; the
all-parameter proofs are in [`DERIVATION_PACKAGE.md`](DERIVATION_PACKAGE.md).

## Owner and collision boundary

The one-ball siteswap theorem directly owns the permutation/gap-vector slice
of (1), and Meyer--Pommersheim directly own the binary parity-complement map
that is exactly the isolated boundary `n=2`.  Hamming weight, diagonal cyclic
actions, Stirling/Fubini enumeration, circular parking arguments, and generic
finite-map zeta conversion receive zero contribution credit.  No located
source states the literal coupled family together with (4), (7), or (8).
The nearest internal systems and killed scouts are subtracted in
[`OWNER_COLLISION_GATE.md`](OWNER_COLLISION_GATE.md).

The surviving claim is only the exact conjunction A--C.  A direct owner for
that conjunction, or a hostile proof-transfer finding, changes this decision
to `KILL`.  External release remains prohibited.
