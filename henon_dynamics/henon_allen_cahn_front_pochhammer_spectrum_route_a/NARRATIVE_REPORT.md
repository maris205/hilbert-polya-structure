# C231 narrative report

For equal wells the Allen--Cahn flow is a gradient system.  The only monotone
heteroclinic between (-1) and (+1) is a translate of

\[
U_\epsilon(\xi)=\tanh\!\left(\frac{\xi}{\sqrt2\,\epsilon}\right),
\qquad c=0.
\]

The first integral gives equipartition and the exact interfacial energy
(2\sqrt2/(3\epsilon)).  Linearization is a factorized Pöschl--Teller
operator: translation is the simple zero mode, the shape mode has eigenvalue
(-3/(2\epsilon^2)), and the essential spectrum starts at
(-2/\epsilon^2) on the real line.  The epsilon-to-zero and epsilon-to-infinity
faces are singular scalings, not additional finite-width fronts.

This is a substantial physical/dynamical closure, but a heteroclinic is not a
primitive periodic-orbit owner.  Route A is therefore retained as a rigorous
negative result under `NO_BAD_EULER_OR_ROOT_NUMBER`.
