# P204 root disposition after actual Review A

2026-09-05 UTC. **REJECTED_IN_REVIEW_A / MATH_VALID / SEAT_REOPENED**.
The numbered draft, original candidate acceptance, Round0 freeze and all
passing/failed production evidence remain preserved. There is no accepted
A delta, Round1, B review, Round2 or internally completed paper.

Root read the complete actual Review A report, reconstructed proof/source
record, finding census, unaccepted delta and build/replay reports. The
decisive full-parameter suffix inversion-code double count is valid:

    D_(r,m)(A) = binom(r+m,m) β_m(A−1),

where β counts ordinary permutations with that exact descent set. Completing
the block after subtracting one supplies r! arbitrary prefix codes; counting
the corresponding permutation suffix by its labels and order gives the same
r! times the right side. Cancelling proves the identity for every parameter.
The mask was already supplied by the temporal decoder, so the retained
contract lacks the required independent inverse contribution after this
explicit subtraction. The valid feedback theorem remains mathematical
progress, but does not fill a paper seat under the fixed two-axis gate.

Root also directly opened the primary author paper
[Descent polynomials](https://users.math.msu.edu/users/bsagan/Papers/Old/dp.pdf),
dated 12 November 2017, and read its exact-descent definition, Proposition
2.1 and Theorem 2.3 with proof on printed pages 2–5. The latter explicitly
records and credits MacMahon's evaluated exact-set formula. No full-paper
or original-1915-book read is claimed. The new suffix adapter is the
reviewer's deduction from the classical code, not a verbatim source theorem.

Permutation complementation also confirms that fibre cardinalities do not
depend on the post-collapse phase. Target/source identities do distinguish
phases, and the original numerical offset example is correct. The rejection
is not a false mathematical-error claim or a wording-only repair request.

## Actual root verification

- Complete Round0 input pins: 23/23 OK (including its 22-entry manifest).
- Review A nonself manifest: 46/46 OK.
- Two fresh physical `python -B reviews/p204_a/verify.py` executions,
  with full stdout initially captured at `/tmp/p204_a_root_replay_1.stdout`
  and `/tmp/p204_a_root_replay_2.stdout`, both exited zero. These actual
  files were physically copied without byte changes to the durable
  `qa/rejection_replays/p204/run1.stdout` and `run2.stdout`; both hashes
  were checked again at those paths.
- Both actual `cmp` commands against `reviews/p204_a/CANONICAL.json`
  exited zero. Each run had 1,755,236 assertions; each complete output hash
  is `f09ce8357277001f3df6e0df116e81204dc19e59111f656fba06d81d420738e6`.
- Pinned standalone verifier:
  `a6ea7483dc80e6c3db6bb09343c8301d4c87a4bfc69c47d95110a5ba0014fa39`.

The rejected paper keeps its one critical **open value** finding. It is not
changed to resolved merely because root accepts the rejection. Zero
mathematical/evidence defects is not zero total findings. Root changes only
live lifecycle/index text, not the reviewed scientific inputs or package.
The next possible paper number is P205, but no replacement is pre-admitted.
All external action stays `HOLD_EXTERNAL`.
