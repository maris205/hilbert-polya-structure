# C241 compile report

Build contract: LuaLaTeX, fixed `SOURCE_DATE_EPOCH=1788048000`, and two
settled passes in each of two fresh directories for revision rounds 0, 1, and
2.  The round macro `\CRevisionRound` is set to 0, 1, and 2 respectively; the
three PDFs must have distinct hashes, while `main.pdf` equals round 2.

The final audit checks:

* no LaTeX errors, unresolved references, overfull boxes, or rerun warnings in
  settled logs;
* 2–6 PDF pages, embedded/subset fonts, and required text for the Lüroth map,
  countably infinite points, `Re(s)>1/2`, absolute product convergence,
  meromorphic continuation, `z=1`, and the A1/A2 route labels;
* no retained `.aux`, `.log`, `.out`, `.toc`, `.fls`, `.fdb_latexmk`, `.pyc`,
  `.tmp`, or `.synctex.gz` sidecars.

Hashes and page/font counts are filled from the release script after the
deterministic builds and are then fixed in the release ledger.

## Settled build receipt

| artifact | SHA256 | bytes |
|---|---|---:|
| `main_round0_original.pdf` | `5ef3d66f9ea3069980357b1fd59733d4187346d2ceff62538032701d18cb6f5e` | 312469 |
| `main_round1.pdf` | `e127da8b02e004eabfbfa4303d3b59181078dfda142b45ea169b23b1a041c0ab` | 313881 |
| `main_round2.pdf` | `682151b76d75ee6418543b399495a98b3fbaf44b333efafa5bb8fe66faf7f94c` | 317745 |
| `main.pdf` | `682151b76d75ee6418543b399495a98b3fbaf44b333efafa5bb8fe66faf7f94c` | 317745 |

The final PDF has 2 pages and 24 embedded/subset fonts.  Independent fresh
build pairs reproduced each round byte-for-byte; settled logs contained no
warnings, errors, unresolved references, or overfull boxes.
