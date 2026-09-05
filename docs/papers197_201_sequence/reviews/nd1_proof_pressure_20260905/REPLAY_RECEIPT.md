# ND1 bounded replay receipt

Two distinct fresh processes executed:

```sh
python3 -B docs/papers197_201_sequence/reviews/nd1_proof_pressure_20260905/verify_nd1_pressure.py
```

Both exited zero. The actual captures were
/tmp/nd1-pressure.OxHlE2/run1.txt and run2.txt; cmp exited zero. Their exact
bytes are preserved in RUN1.txt and RUN2.txt and equal CANONICAL.txt.
Each run has 1,524,572 assertions and PASS_BOUNDED_CONTROL status.
Canonical SHA-256:
1f08b366aa78d866e767e8fe6f3b07fdf351cc263cc5896feb13c2e3e43bc4ae.

An earlier diagnostic process with the same code also passed, but the
two-run receipt counts only the two captured processes. The scopes are
all labelled graphs n=0..6 and every potential-decoder target n=0..4.
No larger graph box or author-verifier import was used. This transcript
does not prove all-size recurrence, a four-step bound, or the extremum.

PINNED_INPUTS.sha256 uses workspace-root-relative paths. SHA256SUMS is
nonself and uses paths relative to this archive. The archive contains no
paper review verdict, accepted delta, or promotion certificate.
