# P129 — Rootward active-pile coalescence on a path

Status: **GO_INTERNAL / ANONYMOUS ROUND-2 FREEZE / HOLD_EXTERNAL**.

The literal chain selects an occupied nonroot site uniformly, moves its pile
one edge toward root zero, and coalesces on contact. The main theorem applies
to every rooted initial set:

$$
\mathbb E[T_{\{0=s_0<\cdots<s_r\}}]
=\sum_{i=1}^{r}h(s_{i-1},s_i),
$$

where `h` is the meeting-time mean of two ordered rate-one pure-death paths.
The full-state corollary is the double-factorial sum with leading term
`4/(3 sqrt(pi)) n^(3/2)`. The manuscript also proves the complete support
from every rooted state and the full-state minimum-time mass. The observed
maximum-time endpoint mass remains explicitly `PILOT_ONLY` and is not a
manuscript claim.

Key frozen files:

- `main.tex`, `sections/*.tex`, `math_commands.tex`, `references.bib` —
  anonymous source;
- `main.pdf`, `main_round1.pdf`, `main_round2.pdf` — byte-identical repaired
  PDF and support-only Review-B sign-off;
- `main_round0_original.pdf` — immutable pre-review snapshot;
- `code/verify.py`, `code/verification_output.txt` — paper-local exact
  verifier and canonical transcript;
- `PAPER_PLAN.md`, `NARRATIVE_REPORT.md`, `CLAIMS_EVIDENCE.md`,
  `CONTROL_RESULTS.md`, and `BUILD.md` — planning and evidence package;
- `HOSTILE_REVIEW_A.md`, `HOSTILE_REVIEW_B.md`, `HOSTILE_REVIEW.md`, and
  `IMPROVEMENT_LOG.md` — two independent reviews, consolidated verdict, and
  their exact repair map;
- `FINAL_QA.md`, `SHA256SUMS` — terminal paper-local audit and integrity
  manifest for the frozen round-two package.

Generic coalescing random walks, voter duality, graphical constructions,
meeting/hitting-time comparisons, ballot identities, and one-dimensional
first-passage reductions receive zero contribution credit.  Assiotis's
birth--death coalescing flows, Hitczenko--Wesołowski's active-count/jump
bridge, and Śniady--Urbán's interval-label/coalescence-pattern machinery are
cited as direct zero-credit neighbors.  The internal firewall distinguishes
P114, P117's odd-run boundary eroder, P121's separator-driven BST/Yule
process, and P126.  The verifier executes 506,663 exact assertions: means
through `n=14`, complete laws through `n=11`, and pair/ballot checks through
80.  The owner search is bounded; no novelty, priority, posting, submission,
or external-release decision is made.
