# Frozen theorem contracts — P172–P176

These contracts fix what each short paper must prove uniformly.  A finite
verifier is required for every item, but computation alone cannot satisfy a
contract.  All five remain `HOLD_EXTERNAL`.

## P172 — Fresh-map self-image erosion

For fresh uniform `f:[n]->[n]`, iterate `A <- A intersect f(A)`.

1. Prove the target-and-image-size count
   `binom(n-a,k-b) k! S(a,k)` for every fixed `B subseteq A`.
2. Derive the cardinality quotient and every-time labelled kernel.
3. Give the full algebraic spectrum and prove that the equal top two
   quotient eigenvalues form a forced `J_2` for every `n>=2`.
4. Classify recurrence and give exact absorption CDF/mean formulas.
5. Retain arbitrary-epoch image-size marks through a polynomial quotient.

## P173 — Random quotient-leakage erosion

For fresh uniform `T in End(F_q^n)`, iterate
`U <- U intersect T^(-1)(U)`.

1. Identify the update with the kernel of a uniform map `U -> V/U`.
2. Count every fixed target both as quotient maps and as ambient
   endomorphisms.
3. Derive the dimension quotient and every-time labelled subspace kernel.
4. Give the full algebraic spectrum and the complete quotient Jordan form:
   one `J_2` for every complementary transient pair.
5. Separate the fixed states `0,V` and prove proper-state absorption at zero.

## P174 — Minimum-pivot Möbius feedback

On a fixed-size subset of `P^1(F_p)`, choose the least finite point `a` and
apply `x -> 1/(x-a)` projectively.

1. Prove the exact image of the first and second iterates and `M^4=M^2`.
2. Give all three depth layers with sharp counts.
3. Reduce the recurrent core to inversion and enumerate fixed points and
   2-cycles, including `p=2,k=2`.
4. Characterize every target fibre and its minimum-pivot marked polynomial.
5. Derive the positive-fibre distribution and unique maximum target.

## P175 — Diagonal-feedback commutator

On `M_n(F_q)`, set `Phi(A)=[diag(A),A]`.

1. Prove `Phi^2=0` and the resulting complete temporal graph.
2. Characterize reachable targets by zero diagonal and `q`-colourability of
   the undirected nonzero-support graph.
3. Express every target fibre as an occupation-weighted proper-colouring,
   equivalently a specified Potts-type sum.
4. Prove that zero is the unique target of maximum fibre.
5. Give image-size, fixed/preperiodic census, and all-time fibres.

## P176 — First-frequency rotation

For a binary word, rotate left by the multiplicity of its current first
symbol.

1. Decompose each pointed necklace into explicit `+/-k` Cayley components.
2. Determine all periods: `{1,2}` together with proper divisors `d>=3` of
   the word length.
3. Prove the sharp maximum tail `n-2` and exactly two deepest words for
   `n>=3`.
4. Give the complete every-target two-branch inverse and fibre histogram
   `0/1/2`.
5. Derive the fixed-word census by Möbius inversion.

P174 and P176 carry explicit amber kill switches.  Contract completion does
not upgrade those lifecycle decisions.
