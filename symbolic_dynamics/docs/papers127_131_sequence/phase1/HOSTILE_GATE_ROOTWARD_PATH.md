# Hostile gate: rootward active-pile coalescence on a path

**Gate date:** 2026-08-31  
**Candidate:** stochastic scout `S02`  
**Internal verdict:** `GO_INTERNAL`  
**External verdict:** `HOLD_EXTERNAL`  
**Paper assignment:** none at this gate

## Bottom line

`S02` survives the hostile gate. Its promotion no longer rests on a fitted
full-start mean. The exact residual is a general-initial-state theorem:

$$
\mathbb E[T_{\{0=s_0<s_1<\cdots<s_r\}}]
=\sum_{i=1}^{r}h(s_{i-1},s_i),
$$

where

$$
h(a,a)=0,\quad h(0,b)=b,\quad
h(a,b)=\frac12+\frac{h(a-1,b)+h(a,b-1)}2.
$$

Poissonization, ordered graphical interfaces, the jump-count compensator,
and a two-path first-event calculation prove the identity. For full
occupancy, the adjacent interface evaluation yields the exact
double-factorial mean and its `n^(3/2)` asymptotic. The acyclic PGF recurrence
and exact support interval are independent second outputs.

The proof package is
`../proof_spikes/ROOTWARD_PATH_PROOF_REPORT.md`. The scouting ledger and exact
program are in `../scouting/stochastic/`.

## Severity ledger

| Severity | Count | Disposition |
|---|---:|---|
| Critical | 0 | No correctness or internal-collision blocker remains for the stated promotion theorem. |
| Major | 2 | External ownership remains unresolved; the observed maximum-endpoint probability is excluded until its separate ballot proof is written. |
| Minor | 2 | Scheduler wording and set-versus-multiplicity boundaries must remain explicit; no tree extension may be implied. |

## Hostile checks

| Gate | Result | Evidence |
|---|---|---|
| Literal kernel frozen | PASS | State is an occupied set on a finite rooted path; select a nonroot occupied site uniformly, move it one step toward zero, and erase multiplicity on collision. |
| Almost-sure absorption | PASS | `Phi(S)=sum(S)` decreases by at least one at every effective update. |
| All-parameter main theorem | PASS | The interface-additive expectation holds for every finite rooted initial set, not only full occupancy. |
| Second output | PASS | Exact finite PGF recursion and `supp(T_S)={max(S),...,sum(S)}`; full-start minimum mass follows. |
| Proof closure | PASS | Graphical interface identity plus compensator/Tonelli; pair mean recurrence; ballot evaluation of adjacent interfaces. No interface independence is assumed. |
| Boundary cases | PASS | `{0}` gives zero; `{0,b}` gives deterministic `b`; root clock, collision multiplicity, active scheduler, and path-only scope are stated. |
| Exact pilot | PASS | 4,095 rooted subsets through `n=12` compare the Bellman mean with the independently computed interface sum; adjacent values pass through `m=12`; full PGFs pass through `n=10`. |
| Stable canonical output | PASS | Fresh run on 2026-08-31 matched `PILOT_CANONICAL.txt` byte for byte; the full 26-system run reports 9,225,587 exact assertions. |
| P1--P126 collision ceiling | PASS WITH SUBTRACTION | P114 rooted peeling, P117 exclusions, P121 adjacent coalescence, and P126 refinement machinery receive zero credit. The residual clock, geometry, theorem, and observable are distinct. |
| Direct-owner gate | HOLD | A bounded primary-source search found broad coalescing-walk owners but no statement of the same one-way active-pile kernel plus general interface-additive jump count. A non-hit is not novelty. |

## Exact evidence freeze

```text
systems=26
promoted=S02
root-containing initial states checked=4095
all nonempty subset states audited=8178
exact assertions=9225587
fresh canonical byte match=PASS
```

```text
8b4db213207189cfd476e6b3d94dfd31c2b7e084aec33ab80bb2563d4d1470d0  scouting/stochastic/code/pilot_exact.py
d62932222b246f93584376d90f59223e4004c10e8c39e915b6681e7022ac2020  scouting/stochastic/code/PILOT_CANONICAL.txt
```

## Owner and collision subtraction

The owner screen used primary technical sources on 2026-08-31, including
Kanade--Mallmann-Trenn--Sauerwald
([DOI 10.1145/3576900](https://doi.org/10.1145/3576900)),
Cooper--Elsässer--Ono--Radzik
([DOI 10.1137/120900368](https://doi.org/10.1137/120900368)), and Ermakov
([DOI 10.1016/S0304-4149(97)00077-X](https://doi.org/10.1016/S0304-4149(97)00077-X)).
General coalescing-walk time, meeting/hitting comparisons, graphical
constructions, one-dimensional coalescence, and simple-walk reductions all
receive zero contribution credit.

The internal ceiling is equally strict:

- P121 owns generic adjacent coalescence and its random-BST/Yule deletion
  history. None of that machinery is a claimed contribution here.
- P114 owns synchronous deterministic rooted peeling, not this asynchronous
  active-pile hitting law.
- P117's pointer-doubling and word-eroder exclusions killed `S03` and cap the
  failed word candidates.
- P126 owns length-increasing balanced refinement, the opposite temporal
  silhouette.

After subtraction, the surviving residual is the active-pile embedded chain,
the general rooted-state interface sum, its pure-death triangular kernel, and
the full-start exact corollary.

## Controlled issues

1. **External owner risk (major).** Coalescing-particle literature is broad.
   An independent expert must repeat the kernel-level and theorem-level owner
   search before any external novelty assertion.
2. **Maximum endpoint mass (major).** The exact pilot verifies
   `P(T=binom(n,2))=2^{-binom(n-1,2)}` through `n=10`, but the promotion does
   not rely on it. Keep it labelled computational until the noncollision
   ballot proof is complete.
3. **Scheduler boundary (minor).** “Uniform” must always say uniform among
   currently occupied nonroot sites. A geometric-site lazy scheduler is a
   different discrete-time law.
4. **Extension boundary (minor).** Set occupancy, deterministic rootward
   motion, and the path carrier are essential. Multiplicity, unbiased walks,
   or rooted trees require new gates.

## Rejected alternatives

- `S01` is stopped: its periodic terminal-size law is PD(1/3,0), the target
  distribution is owned, and no literal cyclic-word reduction was proved.
- `S03` is killed by the P117 pointer-doubling firewall despite its correct
  `(n+1)^(n-1)` census.
- `S25` is killed after reproducing PD(1/2,0) behind another adjacent
  deletion wrapper.
- `S26` is killed: exact height-three greedy-matching fractions did not yield
  an all-height residual beyond random-greedy/RSA ownership.

These failures cannot be counted toward a batch quota and do not weaken the
single-survivor decision.

## Decision

**GO_INTERNAL** for `S02` on the theorem contract proved in the proof-spike
report. This authorizes the next internal drafting/selection stage, not a
paper number or an external novelty claim. External status remains
**`HOLD_EXTERNAL`** until independent owner review clears the literal kernel
and general interface theorem.
