# HCS-C163: open-Walsh phase equidistribution

C163 keeps the frozen C148/C153/C158 three-symbol open Walsh gate and clears
the phase gate left open by C158.  The algebraic obstruction

```text
c=2 cos(delta)=(sqrt(3)-sqrt(111))/6,
primitive_Z(c)=3c^4-19c^2+27,
minpoly_Q(c)=c^4-(19/3)c^2+9
```

shows that the monic rational minimal polynomial has a nonintegral
coefficient, so the phase cosine is not an algebraic integer and the ratio of
the two surviving one-site phases is not a root of unity.  The exact binomial
Fourier formula then proves that the
multiplicity-weighted full-cycle phase law converges to Haar measure.  At the
central-limit scale the log-modulus fluctuation and phase converge jointly to
`Normal(0,sigma^2) tensor Haar`, hence become asymptotically independent.

This is an unconditional all-register-length source theorem.  The finite
ledgers are implementation receipts, not its proof.  No dynamics pivot was
required.  The moved-hole control realizes the complementary order-four
finite-subgroup branch.

Scope remains `NO_BAD_EULER_OR_ROOT_NUMBER`; Route B is not authorized.

## Reproduce

```bash
python3 code/c163_phase_producer.py
python3 code/c163_phase_checker.py
python3 code/c163_sympy_crosscheck.py
python3 code/c163_replay.py
python3 code/c163_mutation.py
```

The release PDF is `paper/main.pdf`; the content-addressed ledger is
`C163_RELEASE_MANIFEST.json`.
