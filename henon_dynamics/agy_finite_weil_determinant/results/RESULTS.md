# HCS-C27 results

## Fixed-prime determinant: pass

For each fixed odd prime p, the finite-Weil-twisted AGY operator is trace
class on `A²(Omega) tensor C^(p²)` throughout the C26 half-plane. Finite
unitary tensoring multiplies branch trace norms by p² and preserves locally
uniform summability. The ordinary determinant `D_p(s,u)` is jointly
holomorphic.

A periodic word has the exact trace atom:

```text
Theta_p(g_word) * lambda_word^(-(s+1)) / chi_word'(lambda_word).
```

## Exact character and arithmetic law

Thomas's formula computes every character from the fixed-space dimension and
the quotient-form discriminant. Values are stored exactly as `a + b G_p`.
At good primes, the trace is the Legendre symbol of `det(g-I)` modulo p.

The character is never zero, is not multiplicative, and must be evaluated on
the complete chronological product. Repetitions use `Theta_p(g^r)`.

## Positive chronology signal

For the C26 three-return forward/noncyclic-reverse pair:

| p | forward | reverse | full fibre polynomials |
|---:|---:|---:|---|
| 3 | 1 | G_3 | different |
| 5 | -1 | 1 | different |
| 7 | -1 | -G_7 | different |

The degree-p² polynomials were reconstructed from all p² traces by Newton
identities. The AB/BA two-return null control is equal at every prime, as
trace cyclicity requires.

Across 24 odd primes p ≤ 97 and 24 powers, 328 of 576 characters differ and
248 agree. The apparent 24-power null windows at p=83 and p=89 are certified
to end at their first differences r=41 and r=30, respectively; only p=43 is
promoted using a complete period.

## Complete p=43 fibre-polynomial collision

The C26 forward and reverse matrices both have order 925 modulo 43. Their
Weil characters agree over the complete period, so their finite-fibre
polynomials `det(I - T rho_43(g))` are equal for all repetitions.

Their base characteristic polynomials modulo 43 are different:

```text
[1, 33, 9, 33, 1]
[1, 11, 13, 11, 1]
```

This is a collision of the finite Weil fibre only. The scalar Perron atoms
remain different.

## All-prime/all-power class-function obstruction

C24-P076 and P082 are distinct primitive labeled cycles with noncyclic orders
of the same three central returns. Their base-trivialized matrices A and B
obey `B X = X A`, `X^T J24 X = J24`, and `det X = 1` for the explicit
integral matrix stored in the certificate. Hence every class character has
the same value on all repetitions, over every prime.

These C24 controls have the same homological characteristic and Perron data;
they are not asserted to be C26 AGY operator branches.

## Singular-prime refinement

C24-P014 and P016 have the same characteristic polynomial and
`det(I-g)=3`. At p=3, their exact characters are `-G_3` and `+G_3`. The
singular quotient discriminant therefore contains information beyond the
common characteristic polynomial.

## Arithmetic fragmentation

The bounded source-locked census contains 150 branches of the form
`gamma_star + bridge + gamma_star`, where the bridge is a first return of
length at most 12. It finds:

```text
150 distinct integer discriminants
150 distinct characteristic polynomials
150 distinct Legendre signatures over odd primes <= 97
```

This is exact finite evidence, not an all-length theorem. It rejects the first
hypothesis of a small common conductor and favors orbit-dependent quadratic
fields.

## Research verdict

The finite Weil door is genuinely open at every fixed odd prime. The current
construction does not open the global Hilbert–Pólya door: p is external,
class-function fibres are provably non-separating, and the bounded census
suggests rather than proves conductor fragmentation. The next large test must
derive an intrinsic adelic trace/measure or pivot to a new dynamical form.
