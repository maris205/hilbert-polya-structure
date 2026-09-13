# Paper30: disposition of the arbitrary-support torus cohomology screen

Date: 2026-09-06. Status: `BOUNDED_SCREEN_CLOSED_WITH_GLOBAL_PROOF_OPEN`.
This is a proof-stage disposition, not a candidate rejection by scores,
a Route decision, a publication lock or a completed paper.

## Actual result

The two new proof packages have passed independent mathematical checking,
and root has fully read both final reports. No formula, hypothesis or
quantifier repair is required. The original arbitrary-support rigidity
question remains unproved; the checked auxiliary results do not supply it.

For $F_\kappa=A\circ S_\kappa$ with the fixed cat matrix and sine shear,
the completed results are:

| Result | Exact status |
| --- | --- |
| All formal sums on actual periodic branches at the linear parameter vanish if and only if a primitive exists in $\mathcal T[[t]]$ | Unconditional, independently checked |
| The primitive is unique modulo $\mathbb C[[t]]$ | Unconditional, independently checked |
| Formal fixed-support rigidity implies a finite nonzero analytic periodic minor for each support, and a countable exceptional parameter set for all supports together | Independently checked conditional implication; its rigidity hypothesis is still OPEN |
| For a fixed-support target and the same formal primitive: either coordinate projection is finite if and only if total support is finite, if and only if the target belongs to $\mathcal B[[t]]$ | Unconditional equivalence for such a solution, independently checked; it does not force any of its four properties to hold |
| A formal primitive with infinite support can have a finite pullback | Exact checked example; its difference target has infinite support, so it is not a counterexample to the original problem |

Here $t=\pi\kappa$, $\mathcal T$ is the finite Fourier space,
$\mathcal B=\{f(q)-f(q-p)\}$, and each coefficient of a primitive in
$\mathcal T[[t]]$ is finite without a uniform support assumption.
The coordinate projections are in $u=e^{2\pi i(q-p)},v=e^{2\pi iq}$.
“A finite projection” means bounded in both directions, not a one-sided
degree bound and not a bound on finitely many parameter orders.

## Exact unresolved obligation

For every fixed finite support space $V$, it remains to prove or disprove
$$
G\in V[[t]],\ H\in\mathcal T[[t]],\ (F_{t/\pi}^*-1)H=G
\quad\Longrightarrow\quad P_u(H)\text{ is finite}.
$$
By the checked equivalence, $P_v(H)$ can replace $P_u(H)$ here.
The projection identities only transmit finite support from one direction
to the other. They do not create an initial bound. A hypothetical
counterexample must have both projections infinite, but none has been
constructed. The earlier fixed-target third-order failure is not such
a counterexample either.

The all-support question at every fixed small nonzero real parameter also
remains OPEN. Formal convergence is not proved, and a countable generic
exceptional set, even under the missing hypothesis, can be dense.

## Bound completed inputs

| Input | Lines | SHA256 |
| --- | ---: | --- |
| [Formal periodic interface](PAPER30_TORUS_FORMAL_PERIODIC_INTERFACE_PROOF_20260906.md) | 332 | `16f063f3a7b6b75168b327a59090d9365c9a65e294b69d4865b0e1940d7b1da7` |
| [Interface independent check](PAPER30_TORUS_FORMAL_PERIODIC_INTERFACE_INDEPENDENT_CHECK_20260906.md) | 309 | `587e483c9adb04ac479a5abd5fd769a63e8249a1681c4cb64d5923a521636930` |
| [Support equivalence reduction](PAPER30_TORUS_FIXED_SUPPORT_FORMAL_GLOBAL_PROBE_20260906.md) | 321 | `3ffc7c26fd2a4393c33070b4ffcaf4382f2a4efb16a50e8d57fdcc209bfaa7f2` |
| [Support independent check](PAPER30_TORUS_SUPPORT_REDUCTION_INDEPENDENT_CHECK_20260906.md) | 298 | `e584dbb886bad2585f71438f2478ebd6a813c05c1a0292ae47204fe68fe53fff` |
| [All-support primary-source screen](PAPER30_TORUS_ALL_SUPPORT_PRIOR_PROBE_20260906.md) | 139 | `561021bdf3693622fbcbe24bcfa01a7fc5892f918fef692f3711b6615e23aafc` |

Root fully read all five final files. The support review initially met a
temporary model-capacity error and was reassigned with the identical
input. That service error is neither a proof failure nor a mathematical
review. The final report above is the completed independent check.
The configured GPT-5.4 reviewer MCP remained unavailable; reports disclose
actual secondary-agent xhigh checking, not cross-model or human review.

## Prior deductions

The literature screen did not locate a direct proof or counterexample to
the precise nonlinear fixed-parameter, generic-parameter or unrestricted
formal-support assertions. This is a bounded non-hit, not novelty PASS.
The linear Fourier orbit-sum mechanism is established prior work, and
Lyubich's circle expansion theorem already gives a genuine finite-Fourier
primitive result in a different setting. Analytic Livšic regularity does
not imply finite Fourier support. Finite-dimensional analytic minors and
countable generic exclusions are general tools, not new principal claims.

Root directly checked the additive version in de la Llave--Windsor,
[Theorem 3.1 and Remark 3.2](https://arxiv.org/pdf/0711.3229), Lyubich's
[Corollary 4.9 and Theorem 4.10](https://www.impan.pl/shop/en/publication/transaction/download/product/88685),
and the scope and Fourier recurrence of Dehghan-Nezhad--El Kacimi Alaoui's
[Theorem 5.1](https://www.jstage.jst.go.jp/article/jmath/59/4/59_4_1105/_pdf/-char/en).
No assertion of having read every page of all three papers is made.

## Disposition and continuation

Retain these short proofs and checks. Do not reopen the unchanged
seven-dimensional test, third-order example, or projection reduction
without a genuinely new global argument. Do not use their number as
evidence of a 22–30-page substantive paper. There is no manuscript,
candidate score, capacity exception or new completed-paper count here.

The user's latest continuation is retained. A separately bounded question
now being screened concerns the small-coupling Ruelle spectrum of the
same sine-shear torus family, motivated by a newly derived frequency-edge
inequality. That is a different spectral question, not an extension of
the unresolved cohomology result and not a selected project. Its exact
model and Fourier method already have strong Faure--Roy precedent; the
new claims must be checked before any proposal of independent value.

Batch07 remains 3/5 locally accepted; Paper30 is unselected and Paper31
has not started. All old proofs, failures and accepted artifacts are
preserved. The 22–30-page requirement and all original candidate gates
remain unchanged. No experiment, build, external write or Route A/B
evaluation was performed in this screen.
