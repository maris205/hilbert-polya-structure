# Internal hostile review — P98

Audit date: 2026-08-29 UTC.
Disposition: **internal GO / external HOLD**.

Round 1 was an integrating proof audit by the primary authoring agent. Round
2 was an independent read-only rederivation by the completed P97 reviewer.
This is internal adversarial review, not external peer review.

## Round 1 — attack of the first complete draft

The first pass independently derived the global residue-class form from
window-sum telescoping and then attacked the polynomial route without using
that parametrization. It checked the recurrence orientation, the cyclic
kernel lemma, repeated-root multiplicities, all characteristic endpoints,
the exact order, Möbius integrality, and recovery.

Findings and implemented repairs:

1. The root argument had used separability implicitly. The proof now states
   that $p\nmid r_0n_0$ makes both reduced root polynomials separable before
   counting their common roots.
2. The pure $p$-power order endpoint could be misread by substituting the
   separately excluded case $r=1$. The proof now records that
   $r_0=1,r>1$ implies $p^a>1$, hence the least multiplicity-covering power is
   $p^{a+1}$.
3. The source and verifier were compared on prime and nonprime fields. The
   field order controls vector-space cardinality, while characteristic alone
   controls root multiplicity; no multiplication-table assumption leaked
   into the configuration lane.
4. General algebraic dynamics, finite linear networks, finite-field
   repeated roots, and Artin–Mazur zeta were positively assigned to the
   cited owners. Bounded search absence was not converted into priority
   language.

After the repairs, the stored program again passed **152,266 exact
assertions**.

## Round 2 — independent rederivation

The independent reviewer reconstructed the affine normal form, the shift on
$(a,d)$, the gcd-degree formula, the exact order, every endpoint, Möbius
inversion, zeta, and recovery from a blank derivation.

Verdict before minor clarification:

- **CRITICAL:** 0.
- **MAJOR:** 0.
- **MINOR:** 4.

All four minor findings were implemented:

1. The manuscript now fixes the companion orientation. With column state
   vectors, the literal shift matrix is the transpose of the
   multiplication-by-$z$ Frobenius companion, so every polynomial has the
   same rank on the two matrices.
2. The $r_0=1,r>1$ implication used in the exact-order proof is explicit.
3. The finite zeta product is expressly an identity of formal power series.
4. The manuscript now anchors its computational statement to the stored
   count of 152,266 assertions.

The reviewer reran the verifier and obtained output byte-for-byte identical
to **CONTROL_OUTPUT.txt**. All five citation keys resolved, the cited scopes
matched the ownership statements, and no claim depended on search absence.

## Residual risk and verdict

- **Mathematics:** low after two proof engines, independent rederivation, and
  full-state controls in six fields.
- **Scope:** low inside the equal-adjacent-block-sum family.
- **Literature/priority:** medium; an equivalent formula may use different
  algebraic-shift or sequential-network terminology.
- **Verdict:** GO for internal Route-A use; HOLD for public posting,
  submission, author contact, or absolute priority language.
