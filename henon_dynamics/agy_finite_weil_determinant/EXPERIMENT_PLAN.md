# HCS-C27 experiment plan

## Decision target

Test the finite-Weil fibre proposed at the end of C26.  The experiment must
separate three questions that earlier projects could not separate:

- existence of an ordinary determinant for the target fibre;
- sensitivity of exact character and local-factor data to noncommutative
  chronology;
- coherence of the resulting arithmetic across primes and orbits.

## Frozen inputs

- C24 periodic-orbit certificate, SHA-256
  `4b4fe5943262137eeeb3eda4de887725a0663402a1f39f8cc43e089bcc91e778`;
- C25 pathwise symplectic trivialization, SHA-256
  `a35cee22714abbb9dc9aadcc165720d1ff77aff3b7f29071f53a1b451760bd12`;
- C26 scalar holomorphic AGY certificate, SHA-256
  `1c0289b9b47e65e0603ea001be7cce263aea13d58c66e4609eac88edf8f7ce4a`;
- odd primes only, with
  \(\psi_p(a)=\exp(2\pi i a/p)\);
- the full \(p^2\)-dimensional finite Weil representation.

## Claims and falsifiers

| Gate | Pass condition | Immediate falsifier |
|---|---|---|
| Fixed-prime Fredholm gate | finite tensor extension of C26 is trace class on the same common domain | an infinite or unbounded fibre multiplicity enters the branch sum |
| Character gate | Thomas's exact character agrees with independent finite-field replay | phase convention or quotient discriminant fails a generator/control identity |
| Chronology gate | a noncyclic three-return order changes a genuine local factor for at least one frozen prime | only AB/BA cyclic signals or averaged-matrix artefacts appear |
| Full-tower gate | power characters are computed through a complete group period when an all-power claim is made | a finite power window is promoted to a theorem |
| Arithmetic gate | many source-locked branches concentrate in a small reproducible set of quadratic square classes | Legendre signatures fragment orbit by orbit |
| Hilbert--Pólya gate | the prime family admits an intrinsic, convergent, same-clock global assembly | the modulus remains external or requires an ad hoc product/measure |

## Computations

1. Compute \(k=\dim\ker(g-I)\) and the quotient-form discriminant
   \(d_g\) over \(\mathbb F_p\).
2. Store
   \(\Theta_p(g)\) exactly in the basis \((1,G_p)\),
   \(G_p^2=(\frac{-1}{p})p\).
3. Recover \(\det(I-T\rho_p(g))\) from
   \(\Theta_p(g^r)\) by Newton identities for \(p=3,5,7\).
4. Scan the C26 three-return forward/reverse pair for every odd
   \(p\le97\) and \(1\le r\le24\), then close any universal claim by a
   complete period computation.
5. Verify the C24-P076/P082 integral symplectic conjugacy and infer the
   all-prime/all-power class-function collapse.
6. Enumerate every first return to the C26 base of length at most 12,
   sandwich it by the frozen positive prefix, and compute the Legendre
   signature over all odd primes at most 97.

## Scope

The 150-branch arithmetic scan is finite evidence.  The fixed-prime trace
class theorem and the integral symplectic conjugacy collapse are exact.  No
product over primes, limit \(p\to\infty\), Riemann-zero comparison, or Route-B
claim is authorized.
