# Source audit and attribution boundary

## Frozen primary sources

1. A. Kuniba, T. Takagi, and A. Takenouchi, *Bethe ansatz and inverse scattering transform in a periodic box-ball system*, Nuclear Physics B 747 (2006), 354--397, arXiv:math/0602481v2, <https://arxiv.org/abs/math/0602481>.  This is the authority for the commuting `T_l`, conserved soliton content, direct/inverse scattering map, angle variables, and linear translation vector `h_l=(min(j,l))`.
2. T. Takagi, *Level Set Structure of an Integrable Cellular Automaton*, SIGMA 6 (2010), 027, arXiv:0906.1410, <https://sigma-journal.com/2010/027/>.  This is the authority for internal symmetry `alpha_j|gcd(m_j,p_j)`, the component matrix `F_alpha`, torus decomposition, exact multiplicity, and the allowed `p_max=0` boundary.

Both bibliographic records and formula-bearing source texts were checked.  No claim is attributed to an inaccessible secondary summary.

## Prior-result boundary

The following are prior KTT/Takagi results and are not claimed novel here:

- the periodic combinatorial-`R` definition and commutativity of `T_l`;
- the action variable `m`, vacancy numbers `p_j`, and the angle-variable bijection;
- decomposition by internal symmetry into copies of `Z^H/F_alpha Z^H`;
- the matrix entries, component multiplicity formula, and translation vector.

The present package derives from that frozen theorem:

- an exact augmented-Smith formula for every individual `T_l` order in every component;
- fixed-point laws componentwise, levelwise, at fixed `(L,M)`, and over the full positive-weight space;
- exact primitive-cycle spectra, zeta factors, and finite Koopman determinants;
- deterministic independent-carrier, SymPy, replay, and mutation certificates.

No external peer review, acceptance prediction, or novelty-priority claim is made.

## Data and firewall audit

There is no training split and no fitted parameter.  The package uses no prime table, zero table, arithmetic local data, Euler factor, root number, automorphy input, or Route-B object.  The arithmetic-origin field is explicitly `none`; integer Smith calculations are not re-labelled as prime arithmetic.

Scope literal: `NO_BAD_EULER_OR_ROOT_NUMBER`.
