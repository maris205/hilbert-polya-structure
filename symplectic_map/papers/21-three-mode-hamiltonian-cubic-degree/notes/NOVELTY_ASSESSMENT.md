# Bounded novelty assessment

The two candidate reviews (R1
`d9362d3b07c38e2248494d2c0ec43209e7b0ce8fb089737326d61888b5d1d846`, corrected
record `6f455d8b40c873b8fc18568d95ed3e3b97de7528eddae911e83a00fe5214c132`; R2
`70592ffe85111cefde9e8fa872688958c22ad7cbe6bf4671151d9e5893aad387`) support a
bounded novelty statement: within the current Papers 12–20 corpus, no prior
paper uses this exact three-mode coupling, asymmetric pure-power placement,
selector margins, and (3\times3) exponent matrix together.

This is not a global literature-priority claim.  The assessment is a collision
screen and design justification.  Primary citation verification is separately
locked in `CITATION_VERIFICATION.md`; all comparisons must retain their stated
scope and terminology.

## Collision matrix: Papers 12–20

| Earlier paper | Main invariant/family | Why it is not Paper 21 |
|---|---|---|
| 12 | period-3 residue | no three-mode sextic coupling or (3\times3) cone |
| 13 | primitive-cycle cover | no asymmetric (q_1^g/p_3^g) placement |
| 14 | four-step torus escape | not an exact-gradient canonical pair |
| 15 | quartic trace fibers | no six-coordinate support recurrence |
| 16 | support-size torus escape | no corrected two-face selector proof |
| 17 | torus-coset decay | different potentials and matrix dimension |
| 18 | marked scalar-boundary ramification | no three-mode (A_g,B_g,C_g) family |
| 19 | translate/gcd obstruction | no present sextic coupling or mod-5 corollary |
| 20 | A4 two-mode shear matrix | no A6, cubic Perron family, or exact formula |

The table is an internal collision record, not a claim that the listed papers
are globally exhaustive or that Paper 21 has priority over uncited work.

## Differentiating signature

The candidate's identifying signature is the conjunction of five restrictions:

1. ambient space \mathbb A^6 with three (q)- and three (p)-coordinates;
2. exact-gradient shears, rather than arbitrary triangular substitutions;
3. a three-mode sextic coupling (q_1^2q_2^2q_3^2) paired with asymmetric pure powers
   (q_1^g) and (p_3^g);
4. a two-face selector feeding the displayed (3\times3) Perron matrix; and
5. a characteristic-zero semiring proof of exact, rather than asymptotic,
   degree.

The five-item conjunction is an internal identification signature.  The novelty
wording therefore says only “not collided within Papers 12–20 under this
conjunction,” never “new in the literature,” and makes no claim about what
would happen after removing any item.

## Review protocol

An independent reviewer must recompute the collision table from the local
records, verify the candidate-review hashes, and check that citations to
Blanc–van Santen and Shao–Sun are terminology/context only.  The reviewer must
also search the manuscript for prohibited global words and report exact line
locations if found.  A clean protocol yields `NOVELTY_SCREEN_PASS`; a collision
or unverifiable citation yields a bounded repair request rather than a novelty
claim.
