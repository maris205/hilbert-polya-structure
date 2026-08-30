# C249 source and scope audit

**Locks.** Source baseline
`3ff451e904f8f063e88c40ef87f4697a6586b1a5`; route evaluator v0.2.0 authority
SHA `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`;
fixed epoch `1788048000`; date `2026-08-30`; scope
`NO_BAD_EULER_OR_ROOT_NUMBER`.

**Primary references.** A. Liénard, “Étude des oscillations entretenues,”
*Revue Générale de l'Électricité* 23 (1928), 901--912, Gallica scan
([source](https://gallica.bnf.fr/ark:/12148/bpt6k5671115f)); N. Levinson and
O. K. Smith, “A general equation for relaxation oscillations,” *Duke Math.
J.* 9 (1942), 382--403, DOI
[10.1215/S0012-7094-42-00928-1](https://doi.org/10.1215/S0012-7094-42-00928-1);
and S. H. Strogatz, *Nonlinear Dynamics and Chaos*, 2nd ed. (2015).
These sources motivate the classical theorem; all receipt values are
recomputed locally from the frozen vector field.

**Collision audit.** C227 is a three-dimensional Lorenz stability atlas and
stops at local equilibrium/Hopf conditions; C232 is a conservative Duffing
separatrix; C178 is a harmonic strobe; C237 is stochastic Kramers dynamics;
and C245 is hybrid integrate-and-fire.  C249 instead freezes a smooth
polynomial Liénard damping law and closes its global sign/boundary and
Floquet story.  This is workspace bookkeeping, not a literature-priority
claim.

**Evidence boundary.** The eight analytic parameter rows separate \(\mu<0\),
\(\mu=0\), and \(\mu>0\).  Five positive rows are DOP853 return-map probes;
they are explicitly marked finite and not an all-state census.  The checker
reintegrates them, while SymPy handles identities independently.  No finite
fit is used to infer an asymptotic period coefficient.

**Forbidden claims.** All nine scope flags are false and Route B is disabled.
The package contains no prime/zero table, arithmetic local datum, Euler
factor, root number, automorphy theorem, target divisor/functional equation,
target determinant, or Hilbert--Pólya operator.
