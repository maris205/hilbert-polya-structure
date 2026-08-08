# HCS-C21 exact code

This directory contains the exact certificate producer, a deliberately
non-importing independent checker, and fail-closed regression tests.

From the project directory:

```bash
python code/c21_producer.py --output results/c21_certificate.json
python code/c21_independent_check.py \
  --certificate results/c21_certificate.json \
  --output results/c21_independent_check.json
python -m unittest discover -s code -p 'test_c21.py' -v
```

`c21_producer.py` reconstructs the published period-six cubic factors and
then certifies the new ordered-cover geometry.  All arithmetic is exact.  It
computes polynomial identities, Gröbner reductions, discriminants, the
twelve-state group action, projective branch/genus data, the rotation fixed
field, the $H^1$-character, half-orbit controls, and the scoped period-seven
comparison.

`c21_independent_check.py` imports neither the producer nor predecessor
project code.  It uses resultant discriminants, a different root-ideal order,
fresh projective singularity and infinity calculations, fresh permutation
enumeration, and fresh recurrence generation.  It also binds the exact
certificate bytes and three source dependencies by SHA-256.

`test_c21.py` exercises full independent recomputation and deliberate
tampering of the candidate identity, source formula, ordered cover, genus,
rotation fixed field, $\tau$-character, cross-period shadow, chronology
threshold, and clock-separation flag.

The symbolic code retains the historical internal variable `r` for the
radical $r^2=A-3$.  Documentation calls it $\eta$; the Frobenius clock is
$r_F$.  The certificate records this notation separation explicitly.
