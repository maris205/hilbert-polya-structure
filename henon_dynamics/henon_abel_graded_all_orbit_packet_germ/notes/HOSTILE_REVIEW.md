# Hostile review

## Round 1: mathematical interface audit

### Finding 1: conjugate-height scope was implicit

The first draft bounded complex fixed points but did not explicitly explain
why every embedding of the trace field is represented by such a conjugate
fixed point.

**Resolution:** the proof now extends each trace-field embedding to the
residue field of the geometric fixed point before applying the monic fixed
equations.

### Finding 2: signed and positive multipliers needed separation

The packet uses the signed multiplier, while pressure uses its positive
unstable modulus.

**Resolution:** the source section now defines
\(\Lambda_\gamma=|\lambda_\gamma|>1\) explicitly and keeps
\(\lambda_\gamma\) in the cyclotomic packet.

### Finding 3: primitive-divisor localization skipped one implication

The first draft said that a primitive divisor belongs to the \(n\)th
cyclotomic factor without spelling out why it cannot divide a proper-divisor
factor.

**Resolution:** the final proof gives the contradiction
\(p_n\mid N(\Phi_d(L_4))\Rightarrow p_n\mid\Delta_d\) for \(d<n\).

### Finding 4: abstract line overflow

The half-plane formula exceeded the text box.

**Resolution:** it is now a display equation.  Round-one PDF compilation has
no unresolved reference or citation.

## Round 2: adversarial claim and reproducibility audit

### Attack 1: delete the \(2^m\) degree cost

This produces the tempting threshold
\(\log\varphi/(h_-\log J_*)\), but the true ratio still contains \(2\) and
is greater than one.

**Verdict:** rejected by the independent checker and unit tests.

### Attack 2: set \(u=1\) after proving the germ

Flatters' theorem forces coefficient norm at least \(\log2\) for every
\(n>12\) on one orbit.

**Verdict:** refuted.  The final proof adds the Banach-valued
Cauchy--Hadamard calculation and proves radius exactly one.

### Attack 3: promote continuous pushforward to an isomorphism

The map is norm one and packetwise isometric, but P50 supplies a
30-dimensional finite kernel.

**Verdict:** rejected.  Continuity is retained; injectivity remains false.

### Attack 4: trust dependency hashes written by the producer

The first checker counted the lock rows but did not reread the source files.

**Resolution:** the independent checker now recomputes all eight file hashes
from disk without importing the producer.

### Attack 5: promote the germ to a determinant or Hilbert--Pólya object

There is no transfer operator, determinant identity, continuation, zero law,
or self-adjoint realization.

**Verdict:** rejected by the schema, tests, paper conclusion, and Route-A
record.

## Final review verdict

**PASS WITH SCOPED CLAIMS.**  The all-orbit germ and exact one-orbit boundary
obstruction are supported.  The paper does not support a zeta value at
\(u=1\), a von-Mangoldt law, a determinant, or an operator.
