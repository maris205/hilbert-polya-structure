# HCS-P71: Relative Lind counterterm

For the full two-shift reverse action, the source Lind zeta is

    (1-2t^2)^(-1/2) exp((2t+3t^2)/(1-2t^2)).

At u=1-sqrt(2)t, its logarithm has pole coefficient 1/sqrt(2)+3/4 and
logarithmic branch coefficient -1/2. P70's odd orbit-resolved packet accounts
for only 1/sqrt(2). Therefore

    u^(1/2) exp(-3/(4u)) zeta_flip(t)/Z_orb(t,1)

extends holomorphically and nonvanishingly across u=0 as a local branch germ.
The coefficients 3/4 and 1/2 are unique among counterterms
u^beta exp(-c/u).

**Status:** source formula verified; local relative extension and uniqueness
PROVED; global determinant and arithmetic trace OPEN; Route B not authorized.
Reproduce with bash code/run_c71.sh and see paper/paper.pdf.
