# LY4: useful full-parameter helpers, no complete atlas

2026-09-08 UTC. Decision: **FULL CONTRACT NOT CLOSED; ZERO ADMISSIONS**.
The full ordinary signed-integral classification for every integer
parameter remains exactly the question in [FROZEN_CONTRACT.md](FROZEN_CONTRACT.md).
No paper, PDF, C-number or formal Route-A evaluation is produced.

## Mathematical outcome

[PROOF_PACKAGE.md](PROOF_PACKAGE.md) proves two uniform auxiliary
statements and an infinite falsifier, all with the original native clock:

- If a nonzero integer cycle avoids $-1$ and has least period greater
  than two, its two classical alternating 2-integrals are nonzero
  **integers**. The new argument uses p-adic diameters on the two parities.
- If $a\ne1$, every ordinary integer cycle meeting $-1$ is a rotation
  of $(-1,b,-1,1-a-b)$, with both varying entries nonzero. Exact least
  periods one, two or four are distinguished, including the degenerate
  Möbius cases.
- For every $M\geq5$, parameter $a=M$ admits the ordinary least-six
  word $(-M,M-1,1,-2,1,M-1)$, which avoids $-1$ and has height $M$.

The last family disproves the frozen naive finite-core hypothesis and
every raised height constant with the same exclusions. It does not
rule out a new core theorem after classifying further unbounded families.
The first two lemmas do not classify all remaining alternating-parameter
Lyness channels. The original full question is therefore not weakened
to these helpers for admission. Their novelty is not claimed.

## One frozen mathematical execution, no rerun

Before creating and executing the script, the contract froze the
alphabet $V=\{-8,\ldots,-1,1,\ldots,8\}$, the exact four-state
successor, all retained edges and cycle extraction without a period cap.
It also froze the specific height-four hypothesis to falsify.

Actual command, from repository root
`/root/autodl-tmp/hilbert-polya-structure`:

```sh
python3 -B henon_dynamics/research_c419_c423/continuation_round4/third_order_lyness/core_falsifier.py
```

The one execution returned exit code **0**, Python **3.12.3**, optimization
mode **0**; its result timestamp is **2026-09-08T02:35:53.970015+00:00**.
Recorded elapsed script time is **0.04612024128437042 seconds**. The
finite result has **65,536 states**, **20,800 retained edges**, and
**363 oriented cycles** (only rotations merged):

| Least period | Number of finite-alphabet cycles |
| --- | ---: |
| 1 | 16 |
| 2 | 120 |
| 3 | 14 |
| 4 | 120 |
| 5 | 1 |
| 6 | 84 |
| 8 | 8 |

These are not all-height counts or a universal period theorem. The
script tested each reported word against the original recurrence,
all possible smaller shifts, and the four-state parameter invariant,
using explicit exceptions. The counterexamples are preserved in the
full output. That producer-side validation is not an independent
reconstruction of the finite graph.

The output was exclusively created, not overwritten. The later
read-only `sha256sum` check confirmed the same bytes:

- [core_falsifier.py](core_falsifier.py):
  `62fdbd8aa099ce8b9d0fc8a069a086c26a30f32d18ce6c8b5493d84de9a80773`.
- [FINITE_ALPHABET_RESULT.json](FINITE_ALPHABET_RESULT.json):
  `a4250ab11dd4f85afa3e57064bdf0298b0e7239d86b5835ef7015a922fa0bfab`.

No second mathematical execution, alphabet enlargement, parameter
rectangle or old run was performed. Hash checking, source reading,
static code review and documentation checks do not add mathematical
executions or turn the result into a full theorem.

## Ownership, independent check and exact gap

[SOURCE_AUDIT.md](SOURCE_AUDIT.md) records all thirteen actual new
queries, precise primary reading, failed PDF retrievals and the
deducted classical 2-integral/order-eight/elliptic mechanisms.
The finite-type coefficient shortcut was rejected on its actual
source hypotheses, not on a vague integrability analogy.

The separately authored [helper review](INDEPENDENT_HELPER_REVIEW.md)
checks the new proof steps and statically inspects the script. Its
actual final scope and findings are recorded there; it is not a
rerun, independent graph reconstruction, full-contract admission or
human peer-review certificate.

To close the original question, one still needs a complete uniform
arithmetic exhaustion of all remaining no-$-1$ channels, exceptional
parameters and ordinary-domain cases, with exact native least periods.
The current lemmas do not supply that step. No additional mathematical
program is authorized solely by naming the gap. Keep the existing
M1/AS2/IR1 admissions at **3/5**, with **0 new manuscripts**.

Source-system progress does not establish target Euler factors, root
numbers, automorphy, target zeros or a Hilbert–Pólya realization.
`NO_BAD_EULER_OR_ROOT_NUMBER` is unchanged.
