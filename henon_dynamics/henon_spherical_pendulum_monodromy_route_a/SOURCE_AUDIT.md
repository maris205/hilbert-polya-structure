# C244 source and scope audit

**Locks.** Source baseline
5f357e2d2b78604f6c286bfbd05da922e1d6791f; evaluator v0.2.0 authority
6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c;
fixed epoch 1788048000; date 2026-08-30; scope literal
NO_BAD_EULER_OR_ROOT_NUMBER.

**Primary sources.**

* R. H. Cushman and J. J. Duistermaat, “The quantum mechanical spherical
  pendulum,” *Bull. Amer. Math. Soc.* 19 (1988), DOI
  [10.1090/S0273-0979-1988-15705-9](https://doi.org/10.1090/S0273-0979-1988-15705-9).
* H. R. Dullin, “Semi-global symplectic invariants of the spherical
  pendulum,” *J. Differential Equations* 254 (2013), DOI
  [10.1016/j.jde.2013.01.018](https://doi.org/10.1016/j.jde.2013.01.018);
  preprint [arXiv:1108.4962](https://arxiv.org/abs/1108.4962).

The sources support the focus-focus and monodromy context.  Every numerical
receipt is recomputed locally from the displayed Hamiltonian; citations do not
import hidden data.

**Boundary audit.** The \((\theta,\phi)\) chart is not used at \(u=\pm1\).
Critical rows are never assigned a regular period.  The interior elliptic
double-root branch is kept separate from the isolated top focus value.  The
oriented cycle basis, positive loop, and matrix-column convention are
explicit.  The checker verifies the cubic, discriminant, root order, and all
three quadratures; the symbolic script returns to the original action
integral.

**Forbidden claims.** All nine scope flags are false.  There is no prime or
zero table, arithmetic local datum, Euler factor, root number, automorphy
claim, target divisor/function equation, target determinant, or
Hilbert--Pólya operator.  Route B is not invoked.
