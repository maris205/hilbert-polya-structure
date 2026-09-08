# Round-two integral-return scout report

2026-09-07. Same C419–C423 batch; no C-number, manuscript or formal
evaluation is produced. M1 and AS2 remain admitted and untouched.

## Outcome

IR1, the original all-parameter NG1 integer periodicity question, now has
a complete computer-assisted classification candidate. It is not a new
question carved out of the old unresolved section, and it is not a larger
coordinate census. Independent review remains the admission gate.
The conditional replacement slot IR2 was not instantiated.

For every integer `a`, all ordinary integral periodic orbits of
`T_a(x,y,z)=(y,z,yz+a-x)` have least period in
`{1,2,3,4,5,6,8,9,12}`. `IR1_CLASSIFICATION.md` gives an explicit
disjoint parametrization, every native first-return length, every
invariant level, and finite square-test formulas for the cycle count
on each `K_a=k`. It consequently gives all ordinary fixed-point counts
and the rational native-clock zeta product on each level.

Two terminal cycles are not in the parameterized families:

- `a=-13`: `(-4,-2,-3,-3,-2)`, least period 5, level `k=-64`.
- `a=-2`: `(-2,-1,0,0,-1,-2,0,-1,0)`, least period 9, level `k=-1`.

The contribution is the complete exclusion of *every other* orbit, not
these two words by themselves. All unforced C413 content and the already
known all-parameter F4 channel are explicitly deducted.

## Why the old recurrent-core gap is closed

The decisive identity is
`d_(i+1)+d_(i-1)=(x_(i+1)+1)d_i`, for `d_i=x_(i+2)-x_i`.
It removes the forcing parameter from the linear difference equation.
Integrality and a global difference maximum give five possible centers.
Their complete signed case split proves that every orbit with `D>100`
is in an explicit periodic channel. Independently, a coordinate with
`|x+1|>3D` forces the four-step channel. Thus every remaining orbit has
`D<=100` and `|x+1|<=3D`, uniformly in parameter, level and period.

The exact finite algorithm enumerates all normalized extremal phases,
not a three-coordinate/large-parameter Cartesian box. Necessary neighbor
bounds leave 74,866 seeds. Injectivity proves that each iteration must
either return to the start or violate a proved residual bound; there is
no period cutoff. The first and only run took about 0.83 seconds and
certified all exits and returns. The native reversal orientations are
restored explicitly, not silently quotiented out.

The original parameter-dependent height-lemma approach was superseded
before mathematical computation; it was not run as an additional census.
The decisive stronger gate was appended to `FROZEN_CONTRACTS.md` before
the complete finite certification. The original stop boundary—no
unclassified recurrent SCC and no arbitrary instruction to search a
larger box—has therefore been met at the candidate-theorem level.

## Evidence and independent-review scope

| Artifact | Role |
| --- | --- |
| `FROZEN_CONTRACTS.md` | Original question, stronger pre-computation gate and stop rules |
| `IR1_PROOF.md` | Full scalar/difference proof, all five centers, reversal and finite-core coverage |
| `IR1_CLASSIFICATION.md` | Complete disjoint words, least returns, level counts and zeta |
| `certify_ir1_core.py` | Exact integer finite certification with no parameter/period cutoff |
| `IR1_CORE_SUMMARY.json` | Original seed counts, exits, family counts, two exceptions and digests |
| `IR1_CORE_CYCLES.jsonl` | Every oriented terminal cycle from the completed finite certification |
| `SOURCE_AUDIT.md` | Primary-source applicability, current checks and explicit ownership deductions |

The first-run raw outputs and code have not been rewritten or rerun for
another PASS. A harmless sign typo in the proof's height lemma was
identified by the coordinator and corrected: with `e=d_1=-d_(-1)`,
both neighboring values are `m+e`. Neither the conclusion nor the code
used the mistaken sign. A separate nonauthor hand audit of Sections 1–4
requested explicit reversal closure, now included in Section 3.6 and
rechecked by that reviewer: W1 is CLOSED and the scoped analytic verdict
is PASS in `../integral_return_review/REVIEW_LEMMAS.md`. The coordinator
also independently checked 10 families across 55 symbolic phases, the
full-space invariant and level-count discriminants. These are distinct
from the still-separate full independent finite reconstruction; neither
is misrepresented as a rerun or approval of the author's finite core.

## Source subtraction and assessment

Cantat–Loray contains the same ambient cubic family after a sign change,
but the inspected bounded-orbit theorems quantify the whole group.
Roberts' unforced escape theory, Baragar/Markoff–Hurwitz descent/counting,
and C413's complete `a=0` classification are deducted. Fresh primary
2024–2026 checks concern other observables or arithmetic domains.
No inspected source supplies the exact all-`a` single-map classification;
this is a bounded collision finding, not a first-priority claim.

The candidate is ready for independent admission review as one complete
question. It should not be split into a five-cycle question, nine-cycle
question, forced-four-line question or period-bound question to increase
the batch count. If the analytic proof or finite certificate fails review,
that same IR1 question must be repaired or rejected rather than relabeled.

## Scope safeguards

Writes were confined to this new `integral_return` directory. No old
first-pass file, AS2 proof, sealed reserve, manuscript, C-number,
evaluation, Git state, paid service or GPU job was changed.
The research-lit/source-verification workflow kept literature claims
separate from the newly derived proof; proof-writer required the complete
signed case split and explicit finite-certification assumptions.

Source arithmetic is distinct from target arithmetic.
`NO_BAD_EULER_OR_ROOT_NUMBER` is unconditional. There is no finite global
all-level fixed count—F4 is unbounded across levels—and no arithmetic
Euler-factor or root-number claim hiding inside the per-level dynamical
zeta product.
