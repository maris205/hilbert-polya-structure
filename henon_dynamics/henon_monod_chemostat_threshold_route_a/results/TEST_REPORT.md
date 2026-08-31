# Test report

All gates pass:

- producer: 18 exact rows and five boundaries;
- independent checker: 244 assertions;
- fresh SymPy derivation: 14 identities;
- replay: two producer runs equal each other and the released bytes;
- hostile integrity: 28/28 independently rehashed mutations rejected;
- manuscripts: three pairwise-distinct revision hashes, and two independent
  fixed-epoch builds per revision agree byte for byte;
- final PDF: two pages, 20 embedded/subset fonts, clean settled log and visual
  inspection of both pages;
- scope: every forbidden-data flag is false, Route B is disabled, and the
  tuple is exactly `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`.

No numerical trajectory is used to prove global convergence.
