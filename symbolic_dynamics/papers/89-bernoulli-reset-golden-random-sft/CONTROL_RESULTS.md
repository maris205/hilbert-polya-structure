# Control Results

Command:

```text
python3 code/verify_reset_golden.py
```

Recorded final output:

```text
Bernoulli-reset golden random-SFT controls
E A^k E = F_(k+2) E checked for 0 <= k <= 50
definition-level paths checked for 0 <= n <= 9
renewal factorization checked for 0 <= n <= 15
annealed identity checked at 3 rational p values for 0 <= n <= 16
sum_environment N_n for n=1..8: [5, 14, 38, 104, 284, 776, 2120, 5792]
p=0.10: h_q=0.447641693679066, h_a=0.452590731810424, sigma^2=0.011161475034958, terms=372
p=0.25: h_q=0.392429805909620, h_a=0.405465108108164, sigma^2=0.029582718016643, terms=140
p=0.50: h_q=0.285678394376291, h_a=0.311905358182436, sigma^2=0.057612583212541, terms=59
p=0.75: h_q=0.156807280840549, h_a=0.188226406459598, sigma^2=0.062358024158315, terms=30
p=0.90: h_q=0.066539324972977, h_a=0.087651818647215, sigma^2=0.037293341513176, terms=18
ALL DISCRETE EXACT CONTROLS PASSED (66,787 assertions; 10 floating diagnostics)
```

## Exact coverage

- **101** Fibonacci matrix assertions: `E A^k E` for `0<=k<=50` and the
  entrywise Fibonacci form of `A^k` for `1<=k<=50`.
- **1,023** definition-level comparisons: every environment of lengths
  `0<=n<=9`, with the matrix count compared to an independent enumeration of
  all `2^(n+1)` state paths.
- **65,535** renewal-factorization comparisons: every environment of lengths
  `0<=n<=15`.
- **102** exact annealed checks: normalization and expected path count for
  `p=1/5,1/2,4/5` and every `0<=n<=16`.
- **25** exact geometric/generating-function reductions for five rational
  reset probabilities.
- **1** exact aggregate environment ledger check.

Total: **66,787 integer/rational assertions**.  The ten additional checks
only test that five printed floating evaluations have a positive strict gap
and positive variance.  The strict inequalities and the CLT are established
symbolically in the manuscript, not by decimal evidence.

The first floating implementation of Binet's formula used an incorrect
parity sign.  The hostile audit caught and corrected it before this recorded
run.  That defect was isolated to diagnostics: the discrete matrix,
path-enumeration, factorization, and rational layers never used Binet's
formula.
