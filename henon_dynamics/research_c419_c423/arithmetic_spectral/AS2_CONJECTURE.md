# AS2 frozen conjecture — subsequently refuted

Frozen before a new commutator computation, 2026-09-07.
The full object and width-one basis are in [FROZEN_CONTRACTS.md](FROZEN_CONTRACTS.md).
No restricted level family has replaced the all-level question.

## Claim proposed for falsification

For trivial nebentypus, the family $\Phi_N(s)$ commutes for every pair
of regular parameters if and only if every primitive character $\chi$
whose conductor $q$ has $q^2\mid N$ satisfies $\chi^2=\overline{\chi}^2$.

A proposed equivalent elementary level condition is:

- $v_2(N)\le9$;
- $v_3(N)\le3$ and $v_5(N)\le3$;
- $v_p(N)\le1$ for every prime $p\ge7$.

This arithmetic equivalence itself needs verification and is not taken
as a premise. The source of the guess is that a nonreal $\chi^2$
may give a conjugate-character scattering block whose two off-diagonal
coefficients have a nonconstant ratio. Commutativity of all oldform
blocks is another unproved component, not an established fact.

## Status

The original conjecture is **REFUTED**, not merely unproved. Independent
review found a fixed-coordinate counterexample at $N=50$: a primitive
quartic character modulo $5$ has real square but takes the value $i$ at
the additional prime $2$. The resulting paired oldform block has a
nonzero commutator at $s=2,t=3$. The complete normalization proof and
exact diagnostic are recorded in [independent_review/](independent_review/).
The original proposed formula above is retained unchanged as a record of
what was tested; it must not be quoted as a theorem.

In particular, a fixed basis of character
oldform spans does not prove a fixed diagonalizing basis for the entire
matrix family. Young's basis changes depend on $s$. This is exactly
where the proposed sufficiency failed. The forty earlier principal-sector
checks remain valid checks of that sector only.

The separately stated [first repair](AS2_REPAIRED_CRITERION.md) was also
refuted, now by the commuting full level $N=100$. Its elementary arithmetic
equivalence remains correct, but its proposed analytic necessity was too
strong. The current parity-sensitive theorem has a complete proof and a
passed nonauthor review; see the [current proof index](AS2_PROOF_INDEX.md).
Neither failed analytic conjecture is erased or promoted retrospectively.

## Explicit boundaries

- The spectral parameter is not source time.
- A nonzero commutator would not establish an autonomous chronological
  dynamics, target Euler factor or Hilbert–Pólya realization.
- A small-level counterexample refutes the conjecture but does not
  complete the original all-level classification.
- Classical scattering formulas and their direct algebraic corollaries
  are fully deducted before deciding whether any residue is substantial.

## First decisive checks

Reconstruct the oldform block from independent incoming constant terms
at prime powers, and compare two exact regular parameters after removing
only the common scalar level-one scattering factor. Include even and
odd exponents, not just the symmetric prime-square case.
Separately check the primitive-character block from Young's
Proposition 4.2 and Theorems 6.1/7.1. Do not make an $s$-dependent
basis change and then mistake its commutator for the cusp commutator.
