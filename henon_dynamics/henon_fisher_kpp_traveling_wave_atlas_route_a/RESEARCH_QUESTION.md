# HCS-C202 research question

For the Fisher--KPP equation

\[
u_t=D u_{xx}+r u(1-u),\qquad D,r>0,
\]

classify every real traveling speed without splitting the model into separate
papers.  With `z=x-c t`, determine exactly when the profile equation

\[
D U''+cU'+rU(1-U)=0
\]

has a positive unit-interval front, prove uniqueness up to translation, close
the reflected negative-speed family, identify the obstruction at every
subcritical or stationary speed, and record the three distinct leading-edge
asymptotic regimes.  The same package must decide whether any of this structure
advances Route A under `NO_BAD_EULER_OR_ROOT_NUMBER`.

The finite certificate is a regression oracle only.  It may test phase-plane
signs, algebraic tails, trapping identities, Hamiltonian levels and the
Ablowitz--Zeppetella profile, but it may not stand in for the continuous
heteroclinic existence proof.
