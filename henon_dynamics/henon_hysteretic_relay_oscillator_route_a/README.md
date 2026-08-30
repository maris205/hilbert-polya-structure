# HCS-C252 — two-threshold hysteretic relay oscillator (Route A)

This package freezes the guard-priority hybrid phase oscillator
\[\dot\theta=\sigma,\qquad \dot y=-\gamma y,\qquad -h\le\theta\le h.\]
At theta=h the mode switches from +1 to -1; at theta=-h it switches back.
The theorem-scale advance is an exact switching-section map: each leg lasts
2h, the full period is 4h, and y maps to exp(-4 gamma h)y. It gives a unique
attracting phase cycle for gamma>0, a neutral continuum for gamma=0, and a
direct no-Zeno bound. Equality guards and the h=0 face are explicit.

This is a source-local hybrid model, not a claim about every Filippov
selection. No target arithmetic, Euler factor, root number, automorphy,
target divisor, or Hilbert--Polya operator is used; Route B is disabled.
The final manuscript is paper/main.pdf.
