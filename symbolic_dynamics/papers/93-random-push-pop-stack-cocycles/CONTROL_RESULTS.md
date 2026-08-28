# Control Results

Command:

```text
python3 code/verify_push_pop.py
```

Recorded output:

```text
Random push--pop stack cocycle exact controls
J=M and I=M-S checked for every direction word through t=15
definition-level labeled maps checked for b=2 through t=9
image cylinders and constant fibre degrees checked for (b,t)=(2,10),(3,7)
ballot first-passage formula checked for b=2,3,5 through t=18
endpoint laws and ballot sums checked for p=0,1 through t=20
critical and supercritical change-of-measure identities checked through t=40 and t=35
symmetric I and J distributions checked through t=40
diagnostic subcritical-limit: value=2.000000000000, target=2.000000000000
diagnostic critical-linear-slope: value=0.170416666667, target=0.166666666667
diagnostic supercritical-prefactor: value=2.500000000000, target=2.500000000000
diagnostic symmetric-prefactor: value=1.500000000000, target=1.500000000000
diagnostic symmetric-Emax/sqrt(t): value=0.773382771825, target=0.797884560803
ALL DISCRETE EXACT CONTROLS PASSED (265,861 assertions; 5 floating diagnostics)
```

## Exact assertion ledger

- **196,605** running-maximum identities: all `65,535` direction words of
  lengths `0<=t<=15`, with `J=M`, `I=M-S`, and `I-J=-S` checked separately.
- **59,048** labelled-map assertions: all `29,524` words over
  `{D,C_0,C_1}` of lengths `0<=t<=9`, each checked against direct symbolic
  composition and against the length normal form.
- **8,188** binary image/fibre assertions: all direction words through
  `t=10`, with image size, output length, cylinder prefix, and constant
  fibre multiplicity checked separately.
- **1,020** ternary image/fibre assertions: the same four checks through
  `t=7`.
- **285** exact ballot comparisons: `b=2,3,5`, five rational probabilities,
  and `0<=t<=18`.
- **252** endpoint comparisons: for `b=2,3,5`, both `p=0,1`, and
  `0<=t<=20`, direct propagation is checked both against the finite ballot
  sum and against `A_t(0)=1` or `A_t(1)=b^t`.
- **123** exact critical-tilt comparisons: `b=2,3,5` and `0<=t<=40`.
- **234** exact supercritical checks: six rational `(b,p)` cases through
  `t=35`, including threshold and stationary-prefactor algebra.
- **24** subcritical-limit and critical-slope algebra checks.
- **82** symmetric finite-law checks: equality of the `I_t` and `J_t`
  histograms and total mass for `0<=t<=40`.

Total: **265,861 integer/rational assertions**.

## Evidence boundary

The five floating diagnostics are deliberately excluded from the exact
count.  They show the expected direction of convergence at `t=400`; they do
not prove an asymptotic constant.  The manuscript proves those constants by
geometric summation, first-hit change of measure, and convergence of a
dominated reflected birth--death chain.
