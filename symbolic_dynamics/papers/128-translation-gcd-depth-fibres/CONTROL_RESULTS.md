# Control results

## Fresh independent verifier

Run on 2026-08-31 UTC from the paper directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py \
  | tee /tmp/p128_verify_round1_fresh.txt
cmp -s /tmp/p128_verify_round1_fresh.txt code/verification_output.txt
```

Result: `cmp` status `0`.

```text
fields=F4,F8,F9
degree_caps=6,4,4
monic_states=17523
transfer_matrix_control=cases[p2:t0,p2:t1,p3:t0,p3:t1,p3:t2] weight_cap=9 assertions=50
TOTAL_ASSERTIONS=180453
```

| lane | states | invariant images | depth ceiling | selected terminal CDF | assertions |
|---|---:|---:|---:|---|---:|
| F4 | 5,461 | 85 | 1 | degree 6: `64,4096` | 52,712 |
| F8 | 4,681 | 73 | 1 | degree 4: `64,4096` | 47,488 |
| F9 | 7,381 | 10 | 2 | degree 4: `0,5904,6561` | 80,190 |

The global total also includes 13 field-construction assertions made before
lane counters begin and 50 transfer-matrix assertions, hence
`52,712+47,488+80,190+13+50=180,453`.

## What is checked

- explicit quotient-field axioms and irreducible bases;
- literal Horner shift and Euclidean polynomial gcd;
- literal iterate versus the consecutive-window gcd;
- terminal clock, invariance, divisibility, and quotient reconstruction;
- the nonmultiplicativity counterexample for `Q`;
- every unit-fibre coefficient in the boxes;
- every invariant target at every exact input degree and every capped sum;
- naive irreducible totals, Garefalakis/Reis fixed counts, and literal
  translation-orbit lengths;
- every depth-CDF coefficient versus an independently assembled formal orbit
  Euler product;
- every coefficient through weight 9 of the literally constructed truncated
  polynomial matrix trace `tr(M_t(y/(1-y))^p)` versus direct residual-vector
  enumeration, for `p=2,3` and every `t`;
- final CDF boundary `q^n`.

The extension fields are falsifiers only.  They neither prove the general
theorems nor support novelty or priority.

## Pinned hashes at round0

```text
660a85d36a5e0796cc01056f17cf782495a7fd256e8a77201bf10cec8dce0803  code/verify.py
303f25ecf334d396ecb9c510cc4496d2ce5877387ebcae3661b9ec683b353930  code/verification_output.txt
be420329b9b14f489536f808448e8c2729462310dac786abbf500a366bddabae  main.tex
32c4d786ead0bd833713fa1609a76abdd612829c7739ccf088d90a7d8079328c  references.bib
e2c063e17ce35249978a5729d27194c9223a893865b62ef11ce8f90c2435d667  main_round0_original.pdf
```

## Round1 verifier freeze

Review A's transfer-matrix repair adds exactly 50 assertions and leaves all
three literal extension-field lanes unchanged.

```text
1b58fb8f71ac74082fb0ed9131a555a2ed4b7716da035e731ee9e5da0ac4a2fe  code/verify.py
3b5e5bbbe94ec7ed7e689ff6a2cfeb2dc04a1ebc1ce9686c44194518ac1b1204  code/verification_output.txt
fa1c10facf18dbb215896da5d4e6b36af446ce60f85208c1a632159f4d0ee1c7  main.tex
32c4d786ead0bd833713fa1609a76abdd612829c7739ccf088d90a7d8079328c  references.bib
f49d7c850e6c607130b96ff80f409ac642bae21ecae80203857262f831677439  main.pdf
f49d7c850e6c607130b96ff80f409ac642bae21ecae80203857262f831677439  main_round1.pdf
```

## Scope sentinels

- old window/clock/fixed/depth outputs: zero credit;
- Garefalakis/Reis `b_(pm)` and its orbit quotient: zero credit;
- P110 order-dual orbit fold: zero credit;
- `Q^(-1)(1)`: unit fibre, not a kernel;
- bounded literature non-hit: not novelty clearance;
- release: `HOLD_EXTERNAL`.
