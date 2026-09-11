# A01 theorem package — parity pushforward by a fresh random map

**Provisional gate:** `RESERVE_OWNER_DENSE / HOLD_EXTERNAL`  
For a fresh uniform endomap `f:[n]->[n]`, define

```text
D_f(A)={y in [n]: abs(f^(-1)(y) intersect A) is odd}.     (0)
```

Equivalently, push the indicator of `A` through the functional matrix of `f`
over `F_2`.  The map is resampled independently at each epoch.

## 1. Every-target Krawtchouk formula

Fix `abs A=a` and a labelled target `B` of size `b`.  Define

```text
K_b(k)=sum_l (-1)^l binom(b,l)binom(n-b,k-l).              (1)
```

Fourier inversion on `F_2^n` gives the number of restrictions `f|A` with
`D_f(A)=B`:

```text
N_n(a,b)=2^(-n) sum_(k=0)^n K_b(k)(n-2k)^a.              (2)
```

Thus

```text
P(A,B)=N_n(a,b)/n^a,                                     (3)
Q_ab=binom(n,b)N_n(a,b)/n^a.                             (4)
```

The apparent denominator in (2) always cancels because it is Fourier
inversion of an integer fibre.  The verifier checks integrality, every row,
and every full-map source/target through `n=5`.

Since all rows from `a`-sets are identical, for every `t>=1`,

```text
P^t(A,B)=(Q^t)_(a,b)/binom(n,b).                          (5)
```

At `t=0`, the actual identity kernel must be used; (5) is intentionally not
extended to time zero.

## 2. Occupied-image mark

Let `R=abs f(A)` be the number of occupied values before even multiplicities
cancel.  For a fixed parity endpoint `B` and `r>=b`, the exact marked fibre is

```text
M_n(a,b;r)
 = binom(n-b,r-b) a![z^a]
   (sinh z)^b (cosh z-1)^(r-b).                           (6)
```

The `b` endpoint boxes have positive odd occupancy; the other `r-b` occupied
boxes have positive even occupancy.  Formula (6) is checked against every
literal map through `n=5`, and

```text
sum_r M_n(a,b;r)=N_n(a,b).                               (7)
```

This mark is the only plausible second axis.  If an owner/value gate judges
it to be merely classical occupancy conditioned on parity, the candidate must
remain killed.

## 3. Recurrence, size spectrum, and absorption

Every reachable size satisfies

```text
b<=a,        b congruent to a (mod 2).                    (8)
```

The diagonal of the size chain is

```text
mu_a=(n)_a/n^a.                                          (9)
```

Here `mu_0=mu_1=1`, and
`mu_(a+1)/mu_a=(n-a)/n<1` for `a>=1`.  Hence the size
quotient has two semisimple recurrent eigenvalues `1` and the distinct
transient eigenvalues `mu_2,...,mu_n`.

Ordering the full `2^n` subset kernel by size, its same-size diagonal block is
the constant matrix with entry `a!/n^a`.  Therefore the complete algebraic
eigenvalue multiset is

```text
1,1,mu_2,...,mu_n,
and 0 with multiplicity 2^n-(n+1).                        (10)
```

No full zero-eigenvalue Jordan form is claimed.

Parity chooses the terminal class.  From an even nonzero size the chain
reaches empty almost surely; from an odd size it reaches the recurrent class
of all singletons almost surely.  Conditional on a singleton, the next
singleton is uniform, so that recurrent class has the uniform stationary law.
For `epsilon=a mod 2`,

```text
Pr_a(tau<=t)=(Q^t)_(a,epsilon),                           (11)
E_a tau=[1+sum_(b<a)Q_ab E_b]/(1-Q_aa),   E_0=E_1=0.     (12)
```

## 4. Boundaries

- `n=1`: empty and the singleton class are already recurrent; every hitting
  time in (12) is zero.
- `n=2`: the full set is even, with transitions to size zero and two each of
  probability `1/2`; hence its mean terminal time is `2`.
- `a=0`: the empty restriction has parity image empty and occupied mark zero.
- `a=1`: the output is always one uniformly chosen singleton, never empty.

## 5. Owner subtraction and decision threshold

Random mappings as labelled balls into boxes, odd/even occupancy extraction,
Fourier inversion on the Boolean cube, and Krawtchouk polynomials all receive
zero contribution credit.  Flajolet--Odlyzko and standard occupancy theory own
the random-map framework; Diaconis--Griffiths own broad multinomial/Krawtchouk
Markov-chain technology.  The spectrum and absorption recurrences are direct
consequences of (2)--(4).

The bounded search did not locate the iterated literal kernel (0), but that is
not novelty evidence.  This candidate should advance only if an independent
gate finds that the conjunction of the labelled all-time law (5), the marked
fibre (6), and the two terminal classes carries value beyond its classical
ingredients.  Current disposition remains reserve, below `S01` and `G05`.
