# Exact control results

Command:

~~~bash
python code/verify_equal_block_sum.py
~~~

Stored output: **CONTROL_OUTPUT.txt**.

Registered full-configuration lanes:

| field | characteristic | window | states | exact order |
|---:|---:|---:|---:|---:|
| 2 | 2 | 5 | 512 | 10 |
| 3 | 3 | 4 | 2,187 | 12 |
| 4 | 2 | 3 | 1,024 | 6 |
| 5 | 5 | 3 | 3,125 | 15 |
| 8 | 2 | 2 | 512 | 4 |
| 9 | 3 | 2 | 729 | 6 |

The independent polynomial/matrix lane covers characteristics 2, 3, 5, 7,
all $1\le r\le8$, and all $1\le n\le32$.

Result: **152,266 exact assertions; all pass.**

No floating-point comparisons, randomized trials, interpolated formulas, or
external algebra package are used.
