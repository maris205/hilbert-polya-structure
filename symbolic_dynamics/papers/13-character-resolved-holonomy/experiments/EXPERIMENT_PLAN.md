# SD-C15 Experiment Plan

## E1 -- exact charged path census

Enumerate closed base words for small finite atom graphs.  Record path length,
cross-edge count, total `Z` charge, pure/mixed status, and coefficient.  The
primary `+1/+1` cocycle must have no charge-zero mixed word.  The inverse
`+1/-1` control must first leak at length two.

## E2 -- character-resolved Fredholm family

Build `L_s(exp(i theta))` at every frozen inventory, cutoff, source point, and
character.  Compare direct determinants with trace-power reconstruction and
with the two-atom closed formula.  Report the full character range and Fourier
coefficient residuals; do not retain only an attractive character.

## E3 -- gauge and reparameterization controls

For vertex potentials `psi_n=n` and `psi_n=log p_n`, assign edge phase
`exp(i theta(psi_target-psi_source))` and verify unitary similarity.  For the
roof twist verify `p^(-s) exp(i theta log p)=p^(-(s-i theta))`.  These are
structural null controls, not candidate successes.

## E4 -- adversarial specificity

Repeat the resolved response on composite, shuffled, and seeded random
inventories and on 32 positive integer charge fields.  A response shared by
these controls is `PROVES_TOO_MUCH` even when its amplitude is large.

## Required outputs

- machine-readable summary JSON;
- exact path census CSV;
- determinant/Fourier audit CSV;
- gauge/reparameterization CSV;
- inventory and charge control CSV;
- unit tests and SHA-256 ledger;
- an experiment report separating exact identities from numerical
  observations.
