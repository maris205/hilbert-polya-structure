# Evidence — ANG-20260915-LKC01

**Date:** 2026-09-15  
**Status:** STOP — BASIC GRADING CANCELS PRIME RETURNS; FULL ORDINARY SUPERTRACE UNDEFINED.

## Inputs and exact method

The [version-1 frozen card](../candidate-card.md) supplies all integers n>=2,
actual localizations, units, real translation, the basic two-degree de Rham
complex, normalized translation means and uniform Gaussian smoothing.
No candidate definition changed during the proof.

The [paper](../paper.md) contains all derivations. Proposition 1 proves
localization equality and the full return groups. Proposition 2
constructs the uniform-mean completion. Proposition 3 computes the
component trace by Fourier diagonalization and derives the Gaussian
transform through its differential equation. Proposition 4 uses the
unitary J and an infinite orthonormal family of constant channels.

There is no numerical experiment, arithmetic cutoff, precision claim,
prime table, zero dataset, external source-dependent theorem or installed
software dependency in these mathematical results. All limiting claims
are proved for the stated spaces, not inferred from finite checks.

## Bounded collision search

The read-only search command was:

~~~sh
rg -n -i 'Koszul|higher Euler|reduced exterior|transverse exterior|localization.*cohom|cohom.*localization' papers --glob '*.md'
~~~

It returned no matches before the new card was created. This local
keyword search does not establish global novelty or absence of related
ideas under other wording. The nearest same-carrier antecedent,
[146](../../146-localization-scaling-groupoid/paper.md), and the current
[156 frontier](../../156-multi-round-source-trace-frontier/paper.md) were
read directly; neither supplies an analytic trace owner for this contract.
The [prior-work guide](../../../docs/prior_work/README.md) supplies lineage
context, not a theorem dependency.

## Controls and limitations

The paper records repeated-label, mixed-support, distinct-component,
single-circle, paired-degree, finite-cutoff, full-direct-sum and arbitrary
circle-length controls. The scalar circle trace is not promoted to a
trace of the full carrier. The zero paired relative observable is
distinguished from the undefined ordinary supertrace. No alternative
degree weighting or analytic torsion is implemented.

The basic complex is an invariant-form representation of the full
groupoid, not all its cochains. Every component is present. This
distinction is essential to the negative result's scope.

## Independent review

The separately assigned [bounded model review](review.md) read the frozen
card before the full manuscript and then checked every proposition,
the scalar Gaussian/Dirac-comb normalization, unitary degree pairing,
full fixed-constant obstruction and negative-result boundaries.
No substantive or minor mathematical defect was identified. Its advance
knowledge of the task and shared model family are disclosed; it is not
human peer review, cross-model validation or formal verification.

## Artifact verification

On 2026-09-15 a read-only Node.js stdin script using fs/path recursively
read every Markdown file in this package. It resolved Markdown local
link targets relative to their source, skipped web/mail/fragment-only
links, and checked the four core files for the exact candidate ID and
common status. It also checked trailing whitespace while allowing
Markdown two-space line endings, and blank interruptions inside tables.

The initial complete-package run, including the independently written
review, reported 6 Markdown files, 26 local links, 4 core identity/status
checks, and 0 problems. Adding the two review navigation links did not
change mathematical inputs; the final scoped receipt follows below.

The separate command

~~~sh
git diff --check -- papers/158-localization-koszul-packet-audit
~~~

returned successfully without diagnostics. New untracked Markdown files
are not covered by Git's diff check, so the direct filesystem check was
used for the actual new contents. Artifact checks do not certify proofs.

Final direct-filesystem receipt after review navigation: 6 Markdown
files, 28 local links, 4 core identity/status checks, 0 problems. This
receipt adds no new mathematical claim or link target.
