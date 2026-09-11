# LNR independent candidate gate

2026-09-06 UTC. **MATH_VALID / HOLD_SOURCE / NO_ADMISSION**.
No paper number, reserve, manuscript review or global novelty claim.

## Reviewed claim and authorship

For $n\ge3$, $x\in\{0,1,2\}^n$ has labeled cyclic positions and
$F(x)_i=\mathbf1_{x_{i-1}<x_i}+\mathbf1_{x_{i+1}<x_i}$, synchronously.
Root authored `../LNR_TEMPORAL_PROOF.md`; `batch197_fosp_gate` authored
`../LNR_INVERSE_WORK/PROOF_PACKAGE.md` and is not an independent reviewer.
This assessor read both original proofs completely, the inverse author's
complete source-boundary note, and the bounded primary/internal sources
listed in [SOURCE_AUDIT.md](SOURCE_AUDIT.md). The final reviewed inputs are
pinned in [INPUT_PINS.sha256](INPUT_PINS.sha256).

The mathematical claims survive this audit:

- $F^4=F^3$; all recurrent points are fixed, with positive blocks
  $2,11,12,21,121$ separated by zeros, plus the all-zero word.
- Sharp maximal entrance is one at $n=3$ and three for every $n\ge4$.
- The eight positive-block kernels and zero-run-height decoder describe
  every labeled one-step inverse set.
- The maximum fibre is $L_{2\lfloor n/2\rfloor}$. For even $n$, only the
  two $(02)^{n/2}$ rotations attain it. For odd $n\ge5$, exactly the $2n$
  labeled targets with one doubled zero or one doubled peak ($11$) in the
  alternating template attain it. At $n=3$, the six rotations of $002,011$
  and $000$ attain three.

These are deductive proof assessments supported by finite tests, not
all-parameter conclusions inferred from those tests. **Source admission
does not follow**, because a direct earlier iterative local-rank paper
has not yet been compared at theorem level.

## Deductive temporal audit

Each image excludes neighboring twos: adjacent source sites cannot both
be strictly larger than one another. A zero persists under every update;
in an image a two also persists, since it has no neighboring two. The
all-one image would assign exactly one strict decreasing incident edge
per vertex. Summing gives all $n$ cycle edges strict, and outdegree one
forces a directed strict cycle, impossible for numeric heights. Hence the
remaining ones lie in runs bounded by fixed zeros/twos.

The author's run analysis exhausts lengths one, two and at least three.
Length-one runs immediately settle to 2, 0 or 1 according to bounds 00,
22 or mixed. For longer runs, interior ones vanish; surviving boundary
ones either form the stable isolated pair 11 or become twos in one further
step. Shared boundary sites do not invalidate this argument because they
are already permanent. Thus at most two further updates after the first
image suffice. The stated fixed language follows from the literal tests
for output 0/1/2, including exclusion of a zero-free fixed word.

For $n=3$, equality patterns of a three-vertex complete graph give only
the fixed first images described in the proof. For all $n\ge4$,
$0^{n-3}122\to0^{n-3}111\to0^{n-3}101\to0^{n-3}202$ has entrance three,
including $n=4$ where both ends touch the same single zero. There is no
unhandled small-cycle duplicate-neighbor case because $n\ge3$ is explicit.

## Deductive inverse/extremal audit

Two adjacent target zeros force equality of the source heights. Boundary
inequalities at a zero run must be checked also for singleton runs; the
author includes them. Every positive target site has positive source
height. An interior source one in a positive run would produce zero, so
all interior source letters are two. This forbids lengths at least five.
Checking the remaining endpoints yields the complete eight-word list.
There is no accidental division by rotations: the zero-run heights and
positive source strings reconstruct every original coordinate. For one
positive run, the two exterior heights are the same variable; the trace
enforces exactly that rather than treating them independently.

All displayed kernel entries were checked against the local source lists.
The inverse proof does not depend on the temporal theorem. The all-zero
target has exactly three constant sources; every zero-free target is
impossible because a source has a global minimum.

For the maximum, the entrywise replacements $D,D^T,C,E\le A$ are valid
inside a trace of nonnegative factors without any commutation assumption.
The analytic estimates use actual Schatten norms, not eigenvalue norms
for nonsymmetric products. The precise multifactor inequality follows
from Tropp's unitarily invariant two-factor theorem with
$t=r/s$, $p=s/(s-1)$, $q=s$, for $2\le s\le r$; all norm exponents are
at least one and both Hölder exponents exceed one. Trace is bounded by
the trace norm through the singular-value decomposition. Thus there is
no hidden restriction to positive semidefinite or commuting factors.

The nonzero eigenvalues of $A$ are $\lambda,\lambda^{-1}$;
$J$ has singular values $2,1,1$; $\|B\|_2=3$. For $r\ge2$,
$\sqrt6<\lambda<a_r$ makes any $J$ strict when there is no $B$.
With one $B$, the leading block gives
$\operatorname{tr}(BA^{r-1})=\operatorname{tr}A^r$ for $r\ge2$.
The exceptional $BJ$ case has trace four, and for $r\ge3$ the scalar
norm product $3\sqrt[3]{10}<\lambda^2$ handles any separated $B,J$ pair;
the argument does not illegitimately move these matrices together.

With $k\ge2$ copies of $B$, the author's strict comparison is uniform:
$(10/9)3^k<\lambda^{k+\lfloor k/2\rfloor}$ follows from the checked
bases $k=2,3$ and the increment-two multiplier $9<\lambda^3$.
The preceding factor $a_r^{r-k}/\lambda^{r-k}<10/9$ also holds for
$r=k$ because then its left side is one. Counting real target positions
gives $n\ge2r+k$. This proves the strict mixed-$B$ bound and does not
silently spend the longer dominated runs' extra length.

The equality analysis is complete precisely because equality forces
$n-2r\in\{0,1\}$ after the large cases are strict. Hence no long dominated
run fits. At zero excess all runs are singleton and any $J$ is strict.
At one excess the unique extra site lies in a zero run or in a length-two
positive run. The $B$ case gives the doubled-peak family; $D,D^T$ are
strict against $A^{r-1}$ because the latter's leading four entries are
positive. The separate $r=0,1$ trace list excludes small-run exceptions
for $n\ge4$ and proves all seven $n=3$ cases. A unique double run excludes
nontrivial rotational stabilizers, so the odd count really is $2n$.

## Independent representation and actual executions

[verify_gate.py](verify_gate.py) is newly written, self-contained and
standard-library only. It reads/imports no author code, old checker,
author canonical or external runtime data. The independent main inverse
engine enumerates cyclic edge-sign words and counts their three-color
realizations through strict upper/lower comparison matrices and the
identity. It then sums those counts by target. This is materially different
from generating counts by the author's positive-run kernels. The sign
representation was selected independently before reading the author's
closed source-boundary note; their generic sign-poset deduction is
compatible but no code was imported. It carries no novelty credit.

The direct source engine independently computes literal updates, complete
orbits and target buckets. For $n\le7$, a separate sign-coloring
backtracker reconstructs full source sets and checks their disjoint union
against each literal inverse bucket. As a third cross-check, all positive
run kernels are derived from literal local strings of lengths 1–7, then
their trace is compared against both main engines for every target.

Finite scope and actual successful assertion counts:

| Check | Scope / count |
|---|---|
| All literal sources, all targets, and all edge-sign words | $n=3,\ldots,11$; 265,707 of each |
| Full inverse source-set equality | Every target for $n=3,\ldots,7$; 3,267 target sets |
| Local positive-run kernel entries / absent words | Every positive word of lengths 1–7; 254 kernel comparisons |
| Mixed products from the eight derived kernels | 2–5 blocks, and 0–2 additional zero positions; 112,320 products-with-padding, each with upper and equality tests |
| Explicit sharp temporal witnesses | Every length 4–128 |
| Total | **3,157,633 assertions per full execution** |

Initial canonical production actually exited zero. Two **additional fresh**
complete child executions then finished; both child exits and both raw
`cmp` exits are zero, stderr is empty, and all six before/after scientific
input pins are unchanged. See [replays/RECEIPT.json](replays/RECEIPT.json)
and the two complete raw stdout files; the reproducible driver is
[record_replays.py](record_replays.py). Each output is 12,257 bytes with
SHA-256 `ebff1e816b557e3a1f960a0d7f12e66aae8706f2667b0d2ff07d38ca1d3fd1f6`.
The canonical includes full distributions, all maximizing labeled targets,
per-family assertion counts and hashes of full lexicographic target-count
vectors. It does not pretend to store every source set or establish an
unbounded theorem through enumeration.

The first package-manifest command accidentally included its own newly
opened output file. The actual check exited one with that sole self-hash
failure; all 25 other entries matched. That failed list is preserved as
`MANIFEST_WITH_SELF.failed.sha256`. The corrected final manifest excludes
only itself and includes the failed evidence. This packaging correction
does not change any scientific input, checker or canonical output.

## Findings and source-value disposition

| ID | Severity / state | Finding and required resolution |
|---|---|---|
| LNR-S1 | Admission-blocking / OPEN | Mukherjee 2011 explicitly claims iterative local-rank convergence, but the relevant theorem statement/proof remains unread. Retrieve a legitimate body and compare its literal neighborhood, ties, iteration, alphabet, stabilization bound and fixed states. Do not claim either complete ownership or a new three-step refinement from the preview. |

No mathematical error was found in the stated proofs. This does not mean
zero current findings: the source gate has the open item above.
[SOURCE_AUDIT.md](SOURCE_AUDIT.md) records the actual primary contexts,
failed retrievals and limits. The literal rank map is old; all-target
sign-poset reconstruction, transfer matrices, crown independent-set
fibres (including both odd adapters), Lucas values and Schatten–Hölder
are all deducted. The remaining arbitrary-target sharp comparison and
complete equality exclusion survive the *inspected* inverse adapters,
but this is not a global originality certificate and does not repair the
unresolved temporal axis.

The skill-directed external Codex-MCP cross-model step was not available;
the project-authorized current-model process-separated audit is disclosed
instead. It does not constitute specialist or external review.

## Handoff

Preserve this package and the author's proofs. Do not assign a number or
promote the candidate on these results. A source-body comparison can
reopen `LNR-S1`; unrelated scouting can continue independently. This is
**HOLD_SOURCE**, not `KILL_VALUE`, since an unseen owner theorem cannot
honestly be used as a complete killing adapter. `HOLD_EXTERNAL` remains.
