# Devil's advocate

## Strongest reasons this result could be misread

### Symmetry is not the Hilbert--P\'olya conclusion

The symbol has both reciprocal symmetry and critical-line unitarity. Those
properties are exact, but the certified off-line divisor proves that they
are insufficient. They do not imply self-adjointness of a generator whose
spectrum is the Riemann zero set.

### A fiber determinant is not a Fredholm determinant

The displayed \(2\times2\) determinant is pointwise in Mellin frequency.
The corresponding multiplier on the global non-atomic \(L^2\) space is not
compact. Calling it a Fredholm determinant would be false.

### One bad zero is enough, but it is not a global zero census

The certificate proves exactly one zero in one tiny disc. It neither counts
all strip zeros nor asserts that no other cancellations can occur elsewhere.
The local no-cancellation bounds are sufficient to reject the frozen
unrenormalized candidate.

### The numerical center is not the proof

The decimal center was discovered numerically. The release theorem instead
rests on rational disc data, complex-ball enclosures, an explicit global
second-derivative bound, and Rouch\'e's theorem. Moving or deleting the
stored decimal approximation does not change the logic once the disc is
frozen.

### Reference cancellation cannot be fitted afterward

An independently derived parent operator could in principle contain the
same factor. The certified natural linear parent does not. Introducing
a canonical product whose zeros are chosen from the H\'enon computation
would merely divide away the counterexample and is forbidden.

### The odd channel is not a rescue

The bad zero occurs in the even channel. The Riemann zeta function has the
trivial real-place parity, so dropping the even channel and retaining the
apparently safer odd one changes the target to a different archimedean
character.

### The homogeneous pivot could be trivial

The homogeneous cubic is attractive because its Mellin symbol is explicit
and strip-safe. But exact scaling homogeneity makes its ambient cocycle a
coboundary. Only a quotient anomaly or index could retain nontrivial H\'enon
content. If no such anomaly exists, the route closes rather than succeeds.

## Mutation-oriented checks

The release checker must reject at least the following alterations after a
payload rehash:

- move the disc onto the critical line;
- replace a strict lower bound by zero;
- reverse the Rouch\'e inequality;
- change the zero multiplicity;
- claim a cancellation by the odd or mirror channel;
- promote the formal symbol to a Fredholm determinant;
- promote the Route-A decision to success;
- add an unknown nested key or change an integer into a Boolean/float;
- modify a locked source digest;
- claim a global strip census or an RH proof.

## Honest status

The result is a strong negative theorem for a natural candidate and a useful
design constraint for later Hilbert--P\'olya searches. It is not evidence
against RH, and it is not a general theorem excluding all H\'enon systems.
