# Research question

For the closed mass-action system

```text
Sdot=-beta*S*I,
Idot=beta*S*I-gamma*I,
Rdot=gamma*I,
```

with `beta,gamma>0`, classify every trajectory and all parameter boundaries in
one theorem.  The target is not a fitted epidemic curve: it is the full
dynamical atlas, including exact scaling, invariant phase curves, peak,
final-size branch, quadrature, sensitivities, equilibria, stability and
recurrence.

Then apply Route-A evaluator v0.2.0.  Can an exactly soluble biological flow
with a transcendental final-size equation supply a prime primitive-orbit layer,
dynamical Zeta, target analytic structure, or natural operator lift?

## Success criterion

The all-parameter proof must separate the infection-free boundary `I0=0` from
the positive-infection branch.  Two independent high-precision methods must
distinguish `W_0` (the forward limit when `I0>0`) from the upper `W_{-1}`
intersection.  No numerical ODE plot can replace those obligations.

## Safety and scope

This is an idealized model analysis, not medical or public-health guidance.
There are no human data and no claim of predictive validity for a real disease.
