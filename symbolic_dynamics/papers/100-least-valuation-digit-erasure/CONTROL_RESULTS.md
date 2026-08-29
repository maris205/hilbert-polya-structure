# Exact control results

Command:

~~~bash
python code/verify_digit_erasure.py
~~~

Stored output: **CONTROL_OUTPUT.txt**.

| prime | digits | states | maximum depth |
|---:|---:|---:|---:|
| 2 | 12 | 4,096 | 12 |
| 3 | 9 | 19,683 | 18 |
| 5 | 7 | 78,125 | 28 |
| 7 | 7 | 823,543 | 42 |
| 11 | 5 | 161,051 | 50 |

Exact totals:

- orbit states: **1,086,498**;
- single-step assertions: **45,232,302**;
- profile/fixed-data assertions: **620**;
- overall: **46,319,420**, all passing.

The script uses only integer arithmetic, exact rational moments, and the
Python standard library.
