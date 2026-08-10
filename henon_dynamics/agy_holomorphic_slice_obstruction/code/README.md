# Exact C26 code

This directory implements the exact application witness for the conditional
AGY holomorphic point-evaluation-slice obstruction.  It deliberately does
not construct a holomorphic transfer space and does not reprove either the
C24 discrete-metaplectic-atom theorem or the C25 all-length Rauzy decoder.

`c26_producer.py` independently reconstructs the literal Rauzy class from
`1234/4321`, obtains seven states and fourteen directed edges, identifies the
frozen AGY state 4 (`1342/4321`), and follows

```text
eta        = tbttbtbb
gamma_star = t^64 eta^8.
```

It preserves the convention

```text
B_word = B_last ... B_first,
R_word = B_word^T.
```

For the exact point

```text
x0 = normalize(R_gamma_star * 1),
```

the producer computes `S=1^T R x0`, directly differentiates the projective
map in three affine simplex coordinates, and verifies

```text
J_gamma_star(x0) = S^(-4).
```

The same exact `P=R_gamma_star` is then used as the fixed positive prefix in
the countable AGY branch grammar.  The producer derives, without sampling,

```text
coordinate hull margin delta = 14783/1642663,
max Birkhoff cross ratio     = 12206150825/12121793906,
q <= tanh(log(theta)/4)      = 0.001733750497636432...
```

and records the positive-prefix complex-cone lemma as the theorem basis for
one common complex projective domain, a right-half-plane normalizer, and the
principal logarithm.  The normalized complex dimension is three; the
Jacobian exponent remains four.

The producer also checks the scalar periodic trace reduction for one-, two-,
and three-return words.  The two-return word uses the genuine base-state
bridge `bttbtbb` and records both the forward Rauzy order and the reversed
operator-factor order forced by the inverse projective action.  Since AB and
BA have the same characteristic polynomial, spectral chronology is tested
separately by a three-return word using the additional bridge `bbb`; its
noncyclic reversal has a different reciprocal characteristic polynomial.
For
`A_word=B_word^T`, characteristic polynomial `chi_A`, and Perron root
`lambda`, it records

```text
periodic weight              = lambda^(-(4+s)),
det_C(I-Dp_A)                = chi_A'(lambda)/lambda^3,
scalar periodic trace atom   = lambda^(-(s+1))/chi_A'(lambda).
```

The two examples verify the specialization at high precision.  The general
identity rests on Perron eigenline splitting, not on those examples.

It then records the conditional point-evaluation factorization

```text
ev_x0 L_s iota_const
  = sum_gamma w_(s,gamma)(x0) U_gamma
```

and the exact single-term floor supplied by `gamma_star` after the external
C24/C25 inputs are invoked:

```text
||ev_x0 L_s iota_const||_ess >= S^(-(sigma+4)),
s = sigma + i*t.
```

For the ambient candidate space the quantitative conclusion is

```text
||L_s||_ess >= S^(-(sigma+4))/(C_eval*C_const).
```

The bounded constant embedding, bounded evaluation, and bounded literal
transfer operator are explicit assumptions on a proposed function space.
They are not inferred from the finite arithmetic certificate.

`c26_independent_check.py` does not import the producer.  It separately
reconstructs the graph, word, matrices, finite `gamma_star` decoder replay,
point, normalizer, direct Jacobian, exact `sigma=0,1` coefficient floors,
the positive-prefix cone constants, three exact characteristic polynomials,
Perron roots, a finite-difference projective denominator, the noncyclic
three-return reversal polynomial, and the optional
length-20 sentinel.  The checker also enforces that the C24 and C25 theorems
remain external dependencies.

`test_c26.py` rejects:

- right-multiplied chronology and confusion of `B` with `B^T`;
- a Jacobian exponent other than four;
- transposed or nonpositive complex-cone prefixes;
- complex dimension four in place of projective dimension three;
- a fitted/nonprincipal logarithm or a sampling-based domain claim;
- reversed two-return order, false spectral promotion of cyclic AB/BA, the
  three-return noncyclic reversal, and failure to cancel the `lambda^3`
  factor;
- mutations of the word, base state, point, or normalizer;
- omission of the bounded-constants or bounded-evaluation assumptions;
- promotion of a finite cutoff to an all-length proof;
- ignoring projected-matrix collisions or averaging metaplectic signs;
- averaged chronology, oscillator truncation, and related scope mutations.

The length-20 first-return replay is a mutation sentinel based at the
original state 2.  It is not an enumeration of AGY branches, a completeness
claim, or the proof of the all-length decoder theorem.

Run the complete release with:

```bash
./code/run_c26.sh
```

The command regenerates both JSON artifacts, executes all mutation tests,
writes the SHA-256 manifest, and checks every listed artifact.
