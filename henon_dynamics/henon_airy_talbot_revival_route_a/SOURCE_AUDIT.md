# Source and claim audit

## Frozen sources

- B. Pelloni and D. A. Smith, *Revivals, or the Talbot effect, for the Airy
  equation*, Studies in Applied Mathematics 153 (2024), e12699, DOI
  `10.1111/sapm.12699`.
- L. Boulton, G. Farmakis, and B. Pelloni, *Beyond periodic revivals for
  linear dispersive PDEs*, Proceedings of the Royal Society A 477 (2021),
  20210241, DOI `10.1098/rspa.2021.0241`.

Publisher metadata and the original/repository records were checked.  They
support Airy-revival and boundary-condition context.  The exact strobe order,
valuation fixed-space law, state-period theorem, and operator boundary are
re-derived in this artifact; no literature-priority claim is made.

## Evidence boundary

The JSON contains exact modular hashes and 90-decimal finite DFT values.
The checker reconstructs phases, coefficients, inverses, Parseval, and fixed
strides without importing producer functions.  SymPy separately proves the
cubic periodicity and finite-character laws.  Sampling through `q=96` is a
regression oracle, not an all-modulus proof.

No target prime or zero table, arithmetic local datum, Euler factor, root
number, automorphy statement, target divisor/counting law/functional
equation, target determinant, Hilbert--Pólya operator, or Route-B input is
present.  Scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.
