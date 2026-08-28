# Source and provenance audit

The equation and its inverse-scattering context are attributed to
Zakharov–Shabat, *Exact theory of two-dimensional self-focusing and
one-dimensional self-modulation of waves in nonlinear media*, Soviet Physics
JETP 34 (1972), 62–69, [official JETP record](https://www.jetp.ras.ru/cgi-bin/dn/e_034_01_0062).
That page has no DOI; none is invented here.  The variational Hessian and VK
framework are attributed to Michael I. Weinstein, *Modulational Stability of
Ground States of Nonlinear Schrödinger Equations*, SIAM J. Math. Anal. 16
(1985), 472–491, DOI
[10.1137/0516034](https://doi.org/10.1137/0516034).

The exactly solvable potential/ladder attribution is limited to G. Pöschl and
E. Teller, *Bemerkungen zur Quantenmechanik des anharmonischen Oszillators*,
Zeitschrift für Physik 83 (1933), 143–151, DOI
[10.1007/BF01331132](https://doi.org/10.1007/BF01331132).  This citation is
used only for the historical solvable Pöschl–Teller potential and ladder
source; it does not assign the present NLS normalization or claim priority.

These sources establish historical ownership and context.  This package makes
no priority or literature-novelty claim.  The Pöschl–Teller factorization is
written out and independently checked rather than cited as a black box.

The producer emits exact rational-grid labels and high-precision values.  The
checker reproduces every formula without importing producer functions; SymPy
checks the profile ODE, integrals, kernels, factorization and action.  No finite
box eigenvalue is used to infer the continuum theorem.

No prime list, Riemann-zero list, fitted frequency, arithmetic local datum,
Euler factor, root number, automorphy datum, target divisor, or
Hilbert–Pólya operator enters the source, code, receipt or manuscript.
