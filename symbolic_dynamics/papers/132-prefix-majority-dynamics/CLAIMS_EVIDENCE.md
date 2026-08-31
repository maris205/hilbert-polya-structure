# Claims and evidence — P132

| claim | deductive evidence | exact falsifier |
|---|---|---|
| fixed words are the two displayed families | four-state balance table at heights `>=1,0,-1,<=-2` | all words through `n=16` |
| all recurrence is fixed and maximum depth is `ceil(log_2 n)` | fixed-prefix amplifier and doubling witness | complete functional graphs through `n=16`; witnesses through `n=511` |
| every target fibre has the excursion/meander product | forced crossings at `-1/0` and concatenation inverse | every one of 131,070 target cells through `n=16` |
| image size is `F_(n+2)` | admissible-run generating function | complete image sets through `n=16` |
| unique maximum is `1^n`, size central binomial | injective absolute-value map and missing all-up path | all targets through `n=16` |

The verifier performs 524,452 integer assertions.  Enumeration is
counterexample pressure only; the all-parameter claims are proved in
`main.tex`.
