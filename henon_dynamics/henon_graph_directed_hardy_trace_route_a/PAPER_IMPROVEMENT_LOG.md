# C124 paper improvement log

No external reviewer, model score, acceptance estimate, or novelty judgement was
used. The two passes below were internal claim/evidence and presentation audits,
followed by deterministic recompilation.

## Round 0

Artifact: `paper/main_round0_original.pdf`

SHA-256: `569abf553c9284f725c6ad8536ceb316ae7e2c82ab161f4568997e36f59271b2`

The manuscript already stated the joint primitive-orbit/Hardy/Fredholm theorem,
the exact `012` cycle, the translation control, and the strict Route-A boundary.
The main weakness was that trace class was justified too compactly; the source
of summability was not visible enough on the page.

## Round 1

Artifact: `paper/main_round1.pdf`

SHA-256: `51b0434d4bccf05cd98eaf0f05acfe8340a982780a14d6ba182b2e46580ae05e`

Added the explicit restriction ratio `rho=85/96`, total-degree multiplicity
`m+1`, and the summable majorant `sum_(m>=0) (m+1) rho^m`. This binds the
trace-class claim to the same rational geometry used for strong separation.

## Round 2

Artifacts: `paper/main_round2.pdf`, `paper/main.pdf`

SHA-256: `72b54fd5a91c8d23b4a2939fa1a57728ae488a37c47e7e2f67ad87edc127a9a1`

Added the normal-convergence argument for the Fredholm lattice product and
strengthened the negative-control wording: translation blindness persists even
within the strongly separated class. The final text retains the exact A2 fail
condition and does not promote an internal analytic determinant to a target
match.

All three versions are two pages. The final isolated builds are byte-identical,
all fonts are embedded, and the final logs contain no warning, overfull or
underfull box, or undefined reference.
