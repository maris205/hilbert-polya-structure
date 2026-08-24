# C123 — additive-noise Hénon moment dynamics

Freeze the iid two-branch affine Hénon system

\[
F_\sigma(x,y)=\left(\frac x2-\frac y4+\frac\sigma2,\frac x4\right),
\qquad \sigma\in\{-1,+1\},\quad \Pr(\sigma=\pm1)=\frac12.
\]

Every finite noise word defines a strict affine contraction.  The package
enumerates all 126 rooted words through length six, reduces the primitive
ones to 23 oriented necklaces, and reconstructs their unique periodic states
exactly.  It also builds the source-owned 15-dimensional Markov operator on
polynomials of total degree at most four and solves its stationary moments.
For a canonical length-`n` necklace row, `2^-n` is the probability of the
chosen rooted length-`n` block under the iid law.  It is not the necklace's
total mass and not an infinite periodic-orbit probability.

This is a finite random-dynamics prefix, not a complete random orbit atlas or
a global nuclear/Fredholm theorem.  It has no prime-like target
correspondence, target-divisor match, or analytic bridge; the degree-four
Markov determinant therefore does not earn an A2 prefix verdict.  The
canonical verdict is `A1_WEAK / A2_FAIL / A3_FAIL / A4_FAIL`, overall
`ROUTE_A_EXPLORATORY`.  The scope firewall is
`NO_BAD_EULER_OR_ROOT_NUMBER`.

## Reproduce

```bash
python3 code/c123_noise_producer.py
python3 code/c123_noise_checker.py
python3 code/c123_sympy_crosscheck.py
python3 code/c123_replay.py
python3 code/c123_mutation.py
python3 code/c123_release_manifest.py
```

Paper: [paper/main.pdf](paper/main.pdf).  Content ledger:
[C123_PREFREEZE_MANIFEST.json](C123_PREFREEZE_MANIFEST.json).
