# Fresh temporal replay receipt

Date: 2026-09-05 UTC. Working directory is the repository root.
Two separate completed Python processes ran:

```sh
python docs/papers197_201_sequence/reviews/mct_temporal_pressure_20260905/verify_mct_temporal.py > docs/papers197_201_sequence/reviews/mct_temporal_pressure_20260905/RUN1.txt
python docs/papers197_201_sequence/reviews/mct_temporal_pressure_20260905/verify_mct_temporal.py > docs/papers197_201_sequence/reviews/mct_temporal_pressure_20260905/RUN2.txt
```

Both exited zero. `cmp RUN1.txt RUN2.txt` and each comparison with
`CANONICAL.txt` exit zero. Each reports `assertions=225506`, `status=PASS`.
The proof contributor wrote this code, extending their own earlier
diagnostic probe; these runs do not constitute independent manuscript
reviews. The code tests no inverse formula and makes no candidate promotion.

Input pins are checked from repository root. Package `SHA256SUMS` is checked
from this directory and lists every top-level regular file except itself.
