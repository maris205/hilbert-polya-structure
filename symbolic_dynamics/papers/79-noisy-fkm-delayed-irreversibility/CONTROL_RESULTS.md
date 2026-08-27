# Deterministic control results

Command:

```bash
python3 code/verify_noisy_debruijn.py
```

Status: **PASS**.  The script reports **309 grouped assertions**:

- definition/de Bruijn: `55`;
- FKM witnesses: `10`;
- noisy local uniformity: `54`;
- exact reversal bounds: `36`;
- support/covariance: `18`;
- phase separation and drift: `24`;
- endpoints and small orders: `72`;
- entropy sandwiches: `40`.

All groups pass exactly.  The finite controls support, but do not replace,
the asymptotic recovery and information-theoretic proofs.
