# Control Results

Command:

```text
python3 code/verify_adjacent_product.py
```

Recorded release output:

```text
finite-field adjacent-product exact controls
q=2: L_0..L_9=[1, 2, 4, 7, 12, 21, 37, 65, 114, 200]
q=2: next fixed-nonzero probabilities=0, 1/4, 1/6, 1/5, 3/16, 5/26, 4/21, 13/68
q=2: age_mass=1.000000000000000, h_mu=0.484678454953871, h_top=0.562399148645924
q=3: L_0..L_6=[1, 3, 9, 23, 57, 143, 361]
q=3: next fixed-nonzero probabilities=0, 2/9, 2/15, 2/11, 10/63, 22/129, 14/85, 86/513
q=3: age_mass=1.000000000000000, h_mu=0.853898202937607, h_top=0.924806254398638
q=4: L_0..L_5=[1, 4, 16, 55, 184, 619]
q=4: next fixed-nonzero probabilities=0, 3/16, 3/28, 3/19, 21/160, 57/388, 30/217
q=4: age_mass=1.000000000000000, h_mu=1.134074691264723, h_top=1.216224572920358
q=5: L_0..L_4=[1, 5, 25, 109, 465]
q=5: next fixed-nonzero probabilities=0, 4/25, 4/45, 4/29, 36/325, 116/905
q=5: age_mass=1.000000000000000, h_mu=1.361005489603169, h_top=1.454951935105873
ALL EXACT CONTROLS PASSED
```

The run exhaustively compared map images, forbidden-language words, and
matrix fiber counts on every tested block.  It also checked the exact
generalized-Fibonacci context ratios, verified that consecutive ratios do not
stabilize, normalized the age law, and confirmed the numerical entropy gap.

The discrete exhaustive layer covers **24 block lengths**, **14,676 hidden
words**, and **4,258 candidate observed words**.  After the hostile review,
the context control checks every nonzero label pair rather than only
`a=b=1`: this gives **199 exact `(a,b,r)` conditional-probability checks**,
including 63 over the nonprime field `F_4`.  The entropy sums and Perron roots
printed above are floating-point diagnostics; the exact entropy formula and
strict gap are established symbolically in the manuscript.
