# P185 Review A — Round1 Delta Acceptance Record

Review A is process-separated and is not claimed independent.  The reviewer
did not edit any file in `papers/185-prefix-diversity-delay/`.

## Bound objects

| Object | SHA-256 |
|---|---|
| Round0 `main.tex` | `a1fa39c5e83bba76af2100fdf27209414fdfb1c56bd7da36e6397c0a33657185` |
| Round0 `main_round0_original.pdf` | `45a2ce36879d17dafb42fd4a08c2afbc6213c8c140ffdee145f4e27f4c8a9129` |
| Round1 `main.tex` | `e17e073a15d839a3178bc5ed922227bd24cea41d4c6ceff4e6066090651da6f6` |
| Round1 `main_round1.pdf` | `fcd6257debd3a3e8744571a390296fe02566cc6655957011778400582bea03c3` |

## Exact delta inspection

- Round1 source lines 47–51 now restrict the image-size and depth-CDF
  summary to `1 <= t <= n-1` and describe the product as transient.
- Round1 source lines 214–217 declare the `t=n-1` empty product, the `t=0`
  identity fibres, and the `t>=n-1` stabilized image/fibres.
- Text-layer comparison of the frozen Round0 and Round1 PDFs showed only
  those requested prose additions/replacements; remaining diff hunks are
  deterministic line/page reflow caused by the added text.
- Mathematical changes beyond the requested boundary repair: **NO**.

## Acceptance conditions for P185-A-MI-01

- [x] The abstract attaches `1 <= t <= n-1` to the image-size and depth-CDF
      formulas.
- [x] The “all-time every-target fibres” claim is literally completed by
      the `t=0` identity fibres and the `t>=n-1` stabilized fibre statement.
- [x] The `t=n-1` empty-product convention is explicit.
- [x] No revised sentence extends `(n)_(n-t)` to negative indices or
      `2^(n-t-1)` beyond stabilization.
- [x] The formal pointwise iterate, transient image, clock, CDF, and local
      fibre formulas are otherwise unchanged.

## Reviewer rerun

- [x] Reviewer updated the verifier to bind only the supplied Round1 source
      and Round1 PDF hashes.
- [x] The verifier explicitly asserts presence of all three boundary repairs.
- [x] Two clean processes were run with `PYTHONDONTWRITEBYTECODE=1`.
- [x] Both runs matched `CANONICAL.txt` byte for byte.
- Exact assertion count: **2,104,528**.
- Formal counterexamples: **0**.
- Transition digest:
  `d5d5f26f18778d029aefc6dc9bf271afaf4ec6ded04029c495c0bbf0c153b918`.
- Round1 canonical transcript SHA-256:
  `c3faeaf7f0853a269400f0d4377aeab56d22e64bf607332d79b71d7742b9a34d`.
- Source/PDF binding: **PASS**.

## Delta disposition

- P185-A-MI-01: **ACCEPTED**.
- New Critical findings: **0**.
- New Major findings: **0**.
- New Minor findings: **0**.
- Final Review A disposition: **ACCEPT**.

Round1 closes the sole Round0 finding without altering the proved dynamical
package.
