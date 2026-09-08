# Fifth continuation: arithmetic frontier outcome

Date: 2026-09-08 UTC. Author status: internal AI-assisted scout. The coordinator's
separate [helper review](INDEPENDENT_HELPER_REVIEW.md) passes the stated auxiliary
proofs only, with no mandatory mathematical correction and no admission.
**Three mechanisms screened, two deep attempts, zero admissions proposed.**
The original full contracts are preserved. This lane
does not change the batch's admission count, create a C number, or claim that
the five-contract objective is complete.

## 1. Frozen comparison and decisions

| Contract | Distinct mechanism and full target | Actual result | Full-contract disposition |
| --- | --- | --- | --- |
| AF5-G | Reversible arithmetic monodromy: exact coordinate-field Galois action for every least period over $\mathbb Q(t)$, including within-period block relations | Generic binary dihedral coding proved; at period four, $G_4$ has order 8 while the reversible centralizer has order 16 | Maximal-centralizer formula **refuted**; full all-period replacement remains **NOT CURRENTLY JUSTIFIED** |
| AF5-C | Cyclotomic integral rigidity: terminating exact atlas of all cyclotomic periodic points for every $c\in\mathbb Z$, with no degree/conductor/period cutoff | Integrality, explicit bounded house, absence of periodic curves and source-dependent finiteness proved | Effective period/conductor exhaustion not established; **NOT CURRENTLY JUSTIFIED** |
| AF5-D | Effective dynamical Mordell–Lang: terminating computation of an arbitrary nonperiodic Hénon orbit's curve-hit set | Existing qualitative DML identified; no effective last-hit bound extracted | **SHALLOW-STOPPED**, not a third deep attempt |

These are three mechanisms, not three parameter variants being sold as three
papers. AF5-G concerns generic coordinate splitting fields and group actions;
AF5-C concerns an infinite-degree arithmetic field and effective torsion
control; AF5-D concerns effective orbit chronology. No rational-Hénon
all-parameter or DH1/DH2 contract has been renamed or reopened.

All use native iterate time, ordinary polynomial-automorphism domains, and
distinct geometric points. Zeros are allowed. Full objects, observables,
classical deductions, decisive tests and stop rules are in
[FROZEN_CONTRACTS.md](FROZEN_CONTRACTS.md).

## 2. The decisive Galois obstruction

For $F_t(x,y)=(y,y^2+t-x)$ let

$$s^2=-t,\quad\alpha^2=s(s+2),\quad\beta^2=s(s-2).$$

The exact-period-four scalar cycles are the rotations of

$$ (s,s,-s,-s),\quad(s,\alpha,s,-\alpha),
\quad(-s,\beta,-s,-\beta). $$

Their complete coordinate field is $\mathbb Q(t)(s,\alpha,\beta)$.
The two radicand classes are independent over $\mathbb Q(s)$, and the
involution $s\mapsto-s$ exchanges them. Hence the group is $D_4$ of order 8.
The reversible centralizer is $C_2\times(C_2\wr S_2)$ of order 16.
Its apparently independent first-cycle half-turn is impossible over the
other two cycles' coordinate field, which already contains $s$.

Equivalently, the actual group satisfies one diagonal relation: the first
cycle's half-turn parity equals the swap parity of the other two cycles.
This is a complete analytic counterexample, with square-class and exhaustive
period-four proofs in [PROOF_PACKAGE.md, §3](PROOF_PACKAGE.md#3-a-decisive-exact-period-four-field-relation).
There is no factorization table or numerical specialization behind it.

The general binary coding in §2 fixes the dihedral set but does not give
an all-period Galois lower bound. A future full theorem would still need exact
groups and all within-period intersection relations. The period-four
parameterization territory is already owned by
[Endler–Gallas (2002)](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.65.036231);
the exact group formula was not independently source-verified from that
paper's body. Neither this bounded calculation nor its uncertain novelty
is proposed as an independent slot.

## 3. Cyclotomic consequence and exact remaining gap

For each integer $c$, every periodic coordinate is an algebraic integer of
house at most $1+\sqrt{1+|c|}$. A pole-order argument rules out periodic
algebraic curves for $F_c$. Using
[Ji–Xie–Zhang v2, Theorem 1.8](https://arxiv.org/html/2511.13443v2),
the cyclotomic periodic set is non-dense; its invariant Zariski closure cannot
have a curve component, so it is finite. This is a source-dependent
qualitative consequence, not our independent research increment.

The missing result is explicit, effective exhaustion for every $c$.
Finiteness does not tell an enumeration when to stop; bounded house without
degree does not give Northcott finiteness. No proof here bounds the necessary
conductors and periods or supplies an equivalent terminating alternative.
Low-period cyclotomic examples and fixed-parameter tables were deliberately
not promoted to the full atlas. Full details are in
[PROOF_PACKAGE.md, §4](PROOF_PACKAGE.md#4-cyclotomic-finiteness-with-the-effective-gap-exposed).

The external theorem is from the inspected 20 January 2026 preprint version;
the original discovery used v1's numbering and the frozen contract records
the correction. No peer-review certification is implied.

## 4. Ownership and plausible arithmetic relevance

P60 already owns mixed reflection closures, associated degree/count helpers
and finite irreducibility checks for a conjugate of $F_{-6}$. Generic-$t$
reducedness does not settle its fixed-parameter gap. C34 owns a fixed-period
Maxwell–Hill wreath construction, not the present all-coordinate splitting
field. Reversibility, anti-integrable coding, Kummer theory, qualitative DML
and cyclotomic non-density are deducted as source/classical inputs.

AF5-G would have intrinsic arithmetic content through Galois permutations
and splitting behavior if its full theorem were closed; AF5-C would give
effective arithmetic-field restrictions if its atlas were closed. These are
plausible source-side arithmetic directions, not established bridges to any
target zeta function. None identifies target Euler factors, root numbers,
automorphy or a Hilbert–Pólya realization. No source-to-target A2 claim or
formal A-grade is made. `NO_BAD_EULER_OR_ROOT_NUMBER` remains in force.

## 5. Actual execution, limitations and handoff

- Search: 10 search-bearing calls, 33 query strings, including 4 explicit
  183-day recency filters; complete chronological ledger and exact source
  locators in [SOURCE_AUDIT.md](SOURCE_AUDIT.md).
- Mathematical executions: **0**; old reruns, GPU jobs, paid APIs, conductor
  sweeps and high-degree censuses: **0**. Shell reads and document checks are
  administrative only. There is no mathematical CPU receipt because no such
  job was launched.
- Access limits: Zotero/Obsidian unavailable; named local library/helper
  fallback paths unavailable; Endler–Gallas and Bedford–Smillie body access
  did not verify the targeted original formulas/theorem number. No entire
  paper-corpus read or universal novelty search is claimed.
- Scout writes: only four Markdown artifacts, with `apply_patch`; the
  coordinator independently added `INDEPENDENT_HELPER_REVIEW.md`.
  No globals, other streams, manuscripts, PDFs, formal evaluations or Git
  history changed; inherited dirty/untracked work preserved.
- Skills influenced the work by enforcing source deduction, pre-computation
  contract freezing, explicit proof gaps, and retention of the full question.
  Current-team review is internal AI-assisted review, not external peer review.

The bounded lane is complete as a research checkpoint, not as a solved full
contract. The coordinator has directly reviewed the n=4 field relation and
finite-set deduction; **zero additional admissions** should be retained unless
a separate full substantive theorem is actually supplied. No new permission is needed
to read or adjudicate these artifacts; further research would be a new bounded
continuation, not an unreported extension of this one.
