# Object, cutoff, marker, and operator contract

## Typed objects

| Name | Type | Owner | Equality permissions |
|---|---|---|---|
| $q$ | `MultiplicativeChainRadix` | source definition | integer, $q\ge2$ |
| $A$ | `PrimitiveZeroOneAdjacency` | ordinary SFT input | matrix equality only |
| $X_A^{(q)}$ | `OneSidedMultiplicativeSFT` | source system | same $q,A$ only |
| $N$ | `PositivePrefixCutoff` | finite-size census | not orbit time |
| $W_\ell$ | `OrdinarySFTWordCount` | $A$-chains | positive integer |
| $Z(N)$ | `MultiplicativePrefixCount` | $X_A^{(q)}$ | positive integer |
| $h$ | `LeadingPrefixEntropy` | prior-owned asymptotic | real scalar |
| $E(N)$ | `OrderOnePrefixRemainder` | finite cutoff | real scalar |
| $x$ | `qAdicBoundaryState` | $\mathbb Z_q$ | inverse-limit equality |
| $E_{A,q}(x)$ | `RealBoundaryValue` | boundary map | real equality only |
| $\gamma_k$ | `GoldenBoundaryDigitCoefficient` | golden control | fixed indexing |
| $z$ | `OrdinaryCutoffGeneratingMarker` | $G(z)$ | marks prefix size $N$ |
| $\xi$ | `DyadicRootOfUnity` | radial control | complex boundary point |

## Chain contract

Every positive integer has a unique form $n=q^v i$ with $q\nmid i$. For a
fixed cutoff $N$, the sets

$$
\{i,qi,\ldots,q^{\ell_i-1}i\},
\qquad q\nmid i,
$$

partition $\{1,\ldots,N\}$. Constraints occur only between consecutive
vertices of one such chain. This justifies the exact product of $W_{\ell_i}$.

No statement identifies these chains with periodic orbits, rational primes,
or independent dynamical components of an additive shift.

## Prefix and increment contract

$Z(N)$ counts assignments on $\{1,\ldots,N\}$. Adding $N$ extends the chain
rooted at $N/q^{\nu_q(N)}$ from length $\nu_q(N)$ to
$\nu_q(N)+1$. Therefore

$$
\frac{Z(N)}{Z(N-1)}=\frac{W_{\nu_q(N)+1}}{W_{\nu_q(N)}}.
$$

Changing the prefix to $\{0,\ldots,N-1\}$, changing $qn$ to $n+q$, or
allowing a constraint whose second endpoint exceeds $N$ changes this formula
and is a source mutation.

## q-adic residue contract

For each $v\ge1$, the function

$$
r_v(x)=x\bmod q^v\in\{0,\ldots,q^v-1\}
$$

is locally constant on $\mathbb Z_q$. The real series

$$
-\sum_{v\ge1}(d_v-d_{v-1})\frac{r_v(x)}{q^v}
$$

is not a $q$-adic numerical series: $r_v(x)/q^v$ is evaluated in
$\mathbb R$ after the inverse-limit coordinate is selected.

## Accumulation contract

`Acc` always means subsequential limits along $N\to\infty`. It is not the
closure of the finite set of values at bounded $N$. For every
$x\in\mathbb Z_q$, the explicit representatives

$$
N_j=(x\bmod q^j)+q^j
$$

tend to infinity and converge to $x$ in $\mathbb Z_q$.

## Dimension firewall

The following are different typed quantities:

| Quantity | Object | Ownership/status |
|---|---|---|
| leading Minkowski/Hausdorff dimension | original multiplicative shift | prior-owned |
| $\dim_HE(\mathbb Z_2)$ | real image of the finite-size boundary map | proved candidate theorem |
| ordinary Minkowski content | continuous real covering scales | not claimed |
| dyadic normalized prefix content | integer/dyadic cutoff sequence | exact accumulation theorem |

An equality between the first and second dimensions is neither asserted nor
expected.

## Generating-marker contract

Define $E(0)=0$ and

$$
G(z)=\sum_{N\ge0}E(N)z^N.
$$

Here $z^N$ marks a finite prefix cutoff. It does not mark a periodic orbit,
return time, roof length, prime norm, or transfer-operator iterate.

Consequently:

- $G$ is not an Artin--Mazur zeta function;
- $G$ is not a Fredholm determinant or trace logarithm;
- no operator is defined or owned by this package;
- the root-of-unity calculation concerns radial boundary behavior of an
  ordinary generating function only.

## Boundary-singularity contract

At a primitive dyadic root $\xi$ the proved statement is

$$
\lim_{r\uparrow1}(1-r)G(r\xi)\ne0.
$$

This is a nonzero Abelian/radial pole-type coefficient. Since such points are
dense, they are not isolated singularities of a meromorphic continuation.
The package therefore avoids the phrase "the full function has a meromorphic
pole at every dyadic root."

## Firewall verdicts

| Proposed identification | Verdict | Reason |
|---|---|---|
| $N$ is orbit period | `TYPE_ERROR` | $N$ is a prefix cutoff |
| $G$ is Artin--Mazur zeta | `OWNER_ERROR` | coefficients are remainders, not fixed counts |
| $E(\mathbb Z_2)$ is the original shift | `TYPE_ERROR` | it is a real image of a boundary map |
| dyadic content equals ordinary Minkowski content | `SCALE_ERROR` | continuous scales were not analyzed |
| a radial singularity is an isolated pole | `ANALYTIC_ERROR` | singular points are dense |
| a finite cutoff proves the full Cantor theorem | `QUANTIFIER_ERROR` | all levels and tails are required |
| reducible $A$ is covered automatically | `ASSUMPTION_ERROR` | PF gap proof uses primitivity |

