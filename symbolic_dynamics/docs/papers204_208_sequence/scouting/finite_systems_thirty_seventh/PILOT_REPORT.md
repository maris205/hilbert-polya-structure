# Complete fixed-box SMV result — no temporal extrapolation

One actual original pilot, exit0, empty stderr, 124,629 checks, 5,408
states and all 5,408 targets. The [actual receipt](pilot_run/receipt.json)
pins seven exact local/interpreter inputs before and after, unchanged.
Full canonical stdout is [pilot_run/stdout.raw](pilot_run/stdout.raw):
68,160 bytes, SHA256
`193c76c203510faaacabb5161ec0fb5c81e06a6a515ef20b42f42889e3f5e9b1`.
It includes every successor, every target fibre size, every state's depth
and eventual period, and all complete cycles and basin summaries.

| Prime | Full states | Image size | Maximum depth | Cycle length: number of cycles | Maximum-fibre targets |
|---:|---:|---:|---:|---|---:|
| 3 | 27 | 15 | 2 | 1:5, 2:3 | 1 |
| 5 | 125 | 65 | 4 | 1:5, 2:6 | 1 |
| 7 | 343 | 187 | 6 | 1:5, 2:9, 4:6 | 5 |
| 17 | 4913 | 2957 | 16 | 1:5, 2:24, 3:4, 4:6, 8:12 | 55 |

Every observed maximum fibre is five, agreeing with the prior deductive
proof. Zero is not the unique maximizer in all fields; the proof never
claimed uniqueness. The observed heights equal $p-1$ in these four boxes,
but no statement for other primes or extension fields follows.

The separate [archived-output analysis](commands/07_archived_pilot_analysis/stdout.raw)
ran with zero new successor evaluations and no extra fields. It found
48 recurrent points having three distinct squared coordinates at $p=17$.
Thus a proposed proof that all recurrent points collapse to equal squared
coordinates is already false. One completely explicit cycle, also retained
in the original canonical, is

$$\begin{aligned}
(0,5,9)&\to(11,12,8)\to(0,8,5)\to(6,9,12)\\
&\to(0,12,8)\to(11,5,9)\to(0,9,12)\to(6,8,5)\to(0,5,9)
\end{aligned}$$

over $\mathbb F_{17}$. Substitution into the original update verifies each
arrow; the eight displayed states are distinct. At its first state the
squared coordinates are $0,8,13$, so the cycle directly refutes that
collapse hypothesis without a general numerical inference.

The result-analysis workflow separates observation, interpretation and
implication: the data pass the static decoder but do not provide a complete
all-field recurrent classification or an entrance-time theorem. No baseline
improvement percentage, stochastic error bar or mean/std is appropriate:
these are exact complete finite carriers, not random trials.

There is no further experiment in this bounded lane. Do not add another
prime, infer a theorem from the height pattern, or label static success an
admission. The full-carrier temporal obligation and direct source ownership
of the static residual remain unresolved. **NO_PROMOTION.**
