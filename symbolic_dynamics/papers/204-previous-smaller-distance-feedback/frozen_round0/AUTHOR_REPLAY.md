# P204 author execution receipt

2026-09-05 UTC; root; Python 3.12.3, standard library only, `-B`, no random
input, imported pilot, external data, network or model call. From the workspace:

```sh
python -B papers/204-previous-smaller-distance-feedback/verify.py > papers/204-previous-smaller-distance-feedback/author_replay/run1.stdout
python -B papers/204-previous-smaller-distance-feedback/verify.py > papers/204-previous-smaller-distance-feedback/author_replay/run2.stdout
cmp papers/204-previous-smaller-distance-feedback/author_replay/run1.stdout papers/204-previous-smaller-distance-feedback/CANONICAL.json
cmp papers/204-previous-smaller-distance-feedback/author_replay/run2.stdout papers/204-previous-smaller-distance-feedback/CANONICAL.json
```

Both physical interpreter executions and both raw byte comparisons exited
zero (actual shell session 29476). The complete stdout files remain at the
paths above; neither output is a normalized or truncated summary.
Each contains 485,578 successful finite assertions, including 184,932
every-target checks. All-size results are proved in the manuscript.

- `verify.py`: `26b2cc657d7e9bc6775e5f03a55362366a4645bdd464821c0c134f1e5cfde3d4`.
- Canonical and each stdout: `f56457c4c44f8a07802ea11567cdc4c35e860dde3c9c91d38e59a478ec3f9fed`.

This is the admitted author's replay pair, not an independent paper review.
Reuse is conditional on unchanged code, parameters, dependencies, runtime
settings and canonical bytes; final batch checks must verify that key.
