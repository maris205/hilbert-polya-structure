# Paper 06 Literature Audit

## Search boundary

This was a focused primary-source search, not an exhaustive systematic
review. It covered symbolic zeta/determinant formulas, intrinsic Markov and
(g)-measures, transfer-operator twists, central/local limit theorems for
shifts, and nearby same-cocycle trace constructions. The search did not look
for a precedent by matching a Riemann-zero computation, because zero data are
forbidden at this stage.

## Established ingredients

- Bowen–Lanford (1970) supplies the finite-state symbolic determinant
  background; Ruelle (1976) supplies the broader transfer/zeta analytic
  framework.
- Parry (1964) supplies intrinsic maximal-entropy Markov chains for
  finite-state shifts.
- Keane (1972) and Walters (1975) supply the normalized \(g\)-measure/Ruelle
  operator setting.
- Parry–Pollicott (1990), especially the CLT and twisted-operator chapters,
  is the closest conceptual collision: one analytic transfer family encodes
  a cocycle and its Gaussian Hessian while remaining tied to periodic-orbit
  zeta data.
- Lalley (1986), Coelho–Parry (1990), and Aaronson–Denker (2001) support the
  central/local limit and uniform-density machinery used in the Mellin step.

These sources validate the ingredients. None by itself supplies the
tensor-prime full-shift monoid or the exact SD-C08 package.

## Scoped synthesis claim

The claim made in Paper06 is deliberately narrow: within this finite search,
we did not find the specific conjunction

1. primes as tensor atoms of the monoidal full-shift source;
2. the unique minimal atom \(F_2\) as the canonical scalar standard sector;
3. the identity
   \(\operatorname{tr}(e^{zQ/2}K_2e^{zQ/2})^r=(\cosh z)^r\), used at both
   \(z=0\) and \(z=iu/\sqrt r\);
4. the resulting Euler/Gamma Mellin–Fredholm factorization; and
5. the universal one-sided chiral no-motion theorem, valid for every bounded
   coupling without a mass-commutation assumption.

This is a synthesis/selection claim, not a “first ever” priority claim.
Absence from a finite search cannot establish universal novelty.

## Specificity warning from the literature

Symbolic CLTs are broad. Therefore the convergence to a Gaussian and its
Mellin Gamma factor is not selective on its own. Paper06 adds source-level
selection (\(F_2\) is the unique least tensor atom), representation-level
selection (its centered sector is one-dimensional and multiplicity one), and
radial \(q>2\) controls. Biased binary and arbitrary scalar-observable
controls still succeed after normalization; this remains an explicit
`PROVES_TOO_MUCH` limitation.

## Bibliographic reliability

The manuscript bibliography uses primary records and verified identifiers
for the claims it cites. Broader interval-map, geometric, or operator-family
analogies are not developed here because Symbolic Dynamics is the only
primary system family. Such directions belong only in the stage's
`ROUND2_CLUE` ledger.
