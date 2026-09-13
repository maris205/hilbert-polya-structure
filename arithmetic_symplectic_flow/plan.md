# Round-2 Plan: Arithmetic Symplectic Suspension Flow

> **Plan status:** `ACTIVE DESIGN SPECIFICATION` (2026-09-13).
> **Scientific status:** no concrete candidate, result, Route-A tuple, or
> Route-B entry is created by this plan.

## 1. Mandate and scope

### Project mission

> Construct and audit one explicitly frozen suspension flow of a concrete
> symplectic map, with an endogenous arithmetic source, a single roof/clock,
> intrinsic primitive closed orbits and repetition law, and a transfer
> operator/dynamical determinant belonging to that same object; establish or
> refute A0 \(\rightarrow\) A1 \(\rightarrow\) A2 before any Riemann-zero
> matching, quantum-spectrum claim, or Route-B invocation.

This is a **candidate-engineering** programme. It deliberately does not choose
an existing Phase-I Session as a presumed winner, and it does not combine the
best-looking pieces of several prior objects into a retroactive candidate.

The plan gives the required order, evidence contracts, and documentation
standard for future authorized work. A new user instruction still determines
whether a mathematical proof, computation, literature search, paper draft, or
external action may be undertaken.

### Programme sources and their proper role

| Source | What it contributes | What it does not contribute |
| --- | --- | --- |
| [Updated visual roadmap](roadmap/rh_roadmap.png) | The Round-2 *Structural Synthesis* direction: arithmetic source \(\to\) symbolic structure \(\to\) geometric carrier \(\to\) closed-orbit/trace structure \(\to\) quantum spectrum. | A proof that any link is already closed. |
| [Phase-I status vocabulary](../p1_wiki/01-status-and-claim-vocabulary.md) | The distinction between source identity, workflow status, local result, and Route evaluation. | A transferable Route label. |
| [Phase-I cross-stream map](../p1_wiki/02-cross-stream-relationships.md) | Legitimate conceptual ancestry and warnings about object/evidence/process transfer. | A theorem dependency between Sessions. |
| [Flow conclusions](../p1_wiki/directions/flow_systems/conclusions.md) | Same-object ownership and clock-transfer failure lessons. | A positive A2 result for this project. |
| [Symplectic roadmap](../p1_wiki/directions/symplectic_map/roadmap.md) | The need for an endogenous \(p\leftrightarrow\gamma_p\), clock, and repetition mechanism. | A preselected map \(F\). |
| [Route A mirror](roadmap/route-a-evaluator.md) and [Route B mirror](roadmap/route-b-evaluator.md) | Frozen obligation references for eventual typed evaluations. | Automatic invocation, a live agent skill, or approval of a candidate. |

The two mirrored evaluator documents remain byte-preserved historical
references. Their source titles may say *Skill*, but in this directory they are
roadmap documents, not an instruction to auto-run an evaluation.

## 2. Why a new object is required

The Phase-I archive provides a stronger design constraint than a list of
systems to continue:

- Logistic Dynamics established a valuable same-object return/roof/nuclear
  transfer/Fredholm chain, but did not supply a natural arithmetic orbit source,
  target divisor structure, completed structure, or natural quantization for
  the Riemann target. It is a **seed/control**, not this project's main object.
- Hénon Dynamics supplied useful periodic and geometric material, but it did
  not form a strong A0--A2 candidate. It is a **bridge**: a future base map may
  be related to a Poincaré section or geometric ancestor only after that link is
  defined and checked.
- Symbolic Dynamics demonstrated that clean finite symbolic work is not, by
  itself, a geometric carrier, global analytic continuation, or operator
  realization. It supplies possible **intrinsic coding**, never a detachable
  symbolic clock.
- The bounded P24--P28 Flow end-state records positive arithmetic A2 `0/5` and
  Route-B invocation `0/5`. In particular, a unit-roof symbolic determinant
  cannot be credited to a distinct physical-roof flow. These counts apply only
  to that named five-form Flow batch.

Thus Round 2 is not a claim that Phase I failed wholesale. It is the practical
inference that the first new project must make object ownership explicit before
it spends effort on target matching or operator construction.

## 3. Object nomenclature and geometry gate

The working programme name is **Arithmetic Symplectic Suspension Flow**. A
future candidate must start from an exact tuple

\[
\mathcal C=
\bigl(M,\omega,F,\mathcal P,\tau,M_\tau,\varphi^t,\mu,\mathcal A\bigr),
\]

where \((M,\omega)\) is a specified symplectic phase space, \(F\) is one
specified \(C^r\) symplectomorphism with \(F^*\omega=\omega\),
\(\mathcal P\) is its fixed parameter/provenance record, \(\tau\) is one
fixed roof of stated regularity, \(\mu\) records the measure and normalization,
and \(\mathcal A\) names the proposed endogenous arithmetic mechanism. The
card must also certify a non-Zeno condition: for example \(\inf\tau>0\), or a
precise equivalent condition ensuring forward and backward accumulated return
time does not converge at finite time on the relevant domain.

The suspension must be defined, rather than only named:

\[
M_\tau=
\{(x,t):x\in M,\;0\le t\le\tau(x)\}/
\bigl((x,\tau(x))\sim(Fx,0)\bigr),
\]

with flow \(\varphi^t\) induced by translation in the \(t\)-coordinate. The
semi-open interval \(0\le t<\tau(x)\) is a representative convention, not the
set on which the endpoint gluing relation is first imposed.

### Non-negotiable geometric distinction

Do **not** infer a Hamiltonian flow merely from the word “symplectic.” If
\(M\) has dimension \(2n\), then its mapping torus has dimension \(2n+1\),
so it cannot itself be a symplectic manifold. The project must distinguish:

```text
symplectic base map F
        -> suspension / mapping-torus flow phi^t
        -> optional Hamiltonian, contact, extended-phase-space, or quantum lift.
```

A future paper may use the stronger term *Hamiltonian* only after it defines
the relevant realization, phase space, form/contact data, generator, and
ownership relation. Until then, the correctly scoped object is a suspension
flow **over a symplectic map**.

## 4. Candidate-card freeze: Phase P0

Before any new theorem claim, numerical run, source-expansion campaign, or
Route language, create a versioned candidate card in the first paper package.
It must answer every field below; an unknown field is recorded as `OPEN`, never
filled by analogy with a prior Session.

| Field | Required frozen content | Immediate stop/fork trigger |
| --- | --- | --- |
| `candidate_id` | Stable ID, date, responsible paper package, and parent/source relation. | Reusing an old ID after changing the object. |
| Symplectic base | Exact \((M,\omega)\), regularity, boundary/topology, and one \(C^r\) symplectomorphism \(F:M\to M\) with \(F^*\omega=\omega\). | “A family like Hénon/cat maps” without one exact member. |
| Parameters and provenance | Parameter domain, selection rule, allowed data, measure, normalizations. | Choosing a parameter after looking at Riemann-zero agreement. |
| Roof and flow | Explicit positive \(\tau\), regularity, \(M_\tau\), \(\varphi^t\), clock units, and a non-Zeno/completeness condition (for example \(\inf\tau>0\)). | Swapping a unit roof for a physical roof later. |
| Arithmetic source | Mechanism internal to \(\mathcal C\); permitted arithmetic inputs and why they are endogenous. | Hand-inserting prime tables, \(\log p\), von Mangoldt weights, or zero data. |
| Symbolic coding | Markov partition/coding/semiconjugacy hypothesis and its precise connection to \(F\) or \(\varphi^t\). | An unrelated standalone shift supplies the timing or determinant. |
| Orbits and repetitions | Primitive convention, orientation, multiplicity, degeneracies, monodromy, and repetition law. | Words, map points, and flow orbits are silently substituted for one another. |
| Analytic owner | Operator, function space, domain, weights, zeta/determinant convention, and analytic region. | Borrowing an analytic object from a calibrator. |
| Controls | Positive/negative controls, invariance checks, data split, and falsification thresholds. | No test distinguishes mechanism from fitted coincidence. |
| Future lift owner | Candidate Hilbert/contact/quantum object, if any; otherwise `DEFERRED`. | A self-adjoint-looking operator is used to rescue weak A0/A1/A2. |
| Route state | Exact evidence state for A0--A2; B is not invoked at this stage. | Inheriting a tuple from another object or Session. |

**P0 exit condition:** a reader can reconstruct the exact candidate from the
card and identify the owner of every object used below. If not, no A0/A1/A2
assessment begins.

## 5. The same-object ledger

The project has one central invariant. All rows below must name the same frozen
candidate \(\mathcal C\), or the candidate must be stopped/forked before
claiming progress.

| Item | Must be owned by the same construction |
| --- | --- |
| Arithmetic source | The frozen \(F,\tau,M_\tau,\varphi^t\) and its stated internal mechanism. |
| Symbolic coding | A coding derived from that base map/flow, with the relation stated. |
| Clock / roof / action | The exact \(\tau\) used to define the flow and closed-orbit lengths. |
| Primitive closed orbits and repetition | The suspension-flow orbit ledger and its specified convention. |
| Transfer operator | An operator defined for this object, its roof, and its stated function space. |
| Zeta / Fredholm determinant | The object induced by the same orbit ledger, clock, operator, and normalization. |
| Trace | The same geometric/analytic object and the same normalization. |
| Later quantum object | A distinct later obligation with a demonstrated owner relation; it cannot repair an earlier missing row. |

The literal anti-pattern is:

```text
symbolic clock + physical orbit + borrowed determinant + separate operator
```

Any of the following is a fail-closed ownership event: an orbit/determinant/
operator object change; substitution of a unit roof for a different physical
roof; a determinant inherited from a calibrator; or a numerical comparison that
uses a different normalization from the claimed object.

## 6. First technical target: A0 -> A1 -> A2

Round 2's first meaningful milestone is not RH, zero matching, or an operator.
It is the coexistence of **A0 + A1 + A2 in one natural candidate**. Each phase
may end with a positive result, a scoped negative result, `OPEN`, or
`NOT_TESTABLE`; all are useful when the object and evidence are preserved.

### P1 / A0 — Endogenous arithmetic relevance

**Question.** What part of the frozen candidate internally produces the
arithmetic structure? Can it generate a meaningful candidate relation such as

\[
p\longleftrightarrow\gamma_p,
\qquad
T_{\gamma_p}\approx\log p,
\]

without importing the right-hand side as a definition or fitting target?

**Required evidence.** A0 work must specify the mechanism, the derivation
path, which prime/power data are or are not involved, parameter provenance, and
at least three adversarial controls appropriate to the candidate. Suitable
control families include shuffled primes, density-matched random integers,
composites-only labels, randomized arithmetic labels, nearby parameters, and a
simpler nonarithmetic parent.

**Forbidden shortcuts.** Do not set \(T_p=\log p\) by hand, insert
von Mangoldt weights, tune/select parameters on Riemann zeros, use a separate
object per prime, or treat generic chaos/GUE-like statistics as arithmetic
origin.

**A0 exit.** The paper either gives a reproducible, endogenous mechanism that
survives controls, or records exactly why the proposed mechanism is external,
degenerate, or indistinguishable from a control. Neither outcome licenses A1
credit without an explicit P1 record.

### P2 / A1 — Primitive closed orbits and repetition law

**Question.** Does the same suspension flow own a natural, enumerable (or
otherwise rigorously characterized) primitive closed-orbit structure, including
repetitions?

For a base-map primitive point \(x\) of period \(n\), the target relation is

\[
T_\gamma=\sum_{j=0}^{n-1}\tau(F^j x),
\qquad
T_{\gamma^r}=rT_\gamma.
\]

The task is to prove, delimit, or refute that relation for the chosen object,
not to presume it from symbolic words. The orbit ledger must state primitivity,
orientation, cyclic identification, multiplicity, stability/monodromy,
degenerate or continuous families, enumeration coverage, and the relationship
between any coding and \(\varphi^t\).

**A1 stop condition.** An extension degree, symbolic repetition, or finite
periodic-point list is not automatically a prime-power law. If the claimed
closed orbit, clock, or multiplicity belongs to another carrier, return to P0
and fork or stop.

### P3 / A2 — Same-object dynamical zeta / Fredholm determinant

**Question.** Can the A1 orbit ledger define a stable analytic object belonging
to this exact roofed suspension? Its general starting point should state the
repetition convention explicitly, for example

\[
\log Z_\tau(s)=\sum_{\gamma\ \mathrm{primitive}}\sum_{r\geq1}
\frac{a_{\gamma,r}}{r}e^{-srT_\gamma}.
\]

Only when the specified weights have the needed multiplicative repetition law,
for example \(a_{\gamma,r}=w_\gamma^r\), may this be written as an Euler
product such as

\[
Z_\tau(s)=\prod_{\gamma\ \mathrm{primitive}}
\bigl(1-w_\gamma e^{-sT_\gamma}\bigr)^{-1},
\]

or

\[
D_\tau(s)=\det(I-\mathcal L_{s,\tau})?
\]

The candidate card must precommit whether the central object is \(Z\),
\(1/Z\), \(Z'/Z\), or a Fredholm determinant; define \(w_\gamma\), function
space, operator domain, normalization, convergence/analytic region, and how
the exact same \(\tau\) enters orbit length, trace, and determinant.

Any computation must report precision, orbit cutoff, completeness limits,
training/validation/sealed comparisons if target data are ever allowed,
extra/missing roots, root-count stability, cutoff drift, and precision drift.
At this stage, however, **Riemann-zero matching is out of scope**.

An owner-level analytic result at P3 is not automatically a formal Route-A A2
pass. The mirrored Route-A protocol also asks whether the zeros/divisor
structure matches the target beyond a fitted region. Because this Round-2 first
phase deliberately excludes target-zero matching, record any such result as a
same-object zeta/determinant result and leave its formal Route-A A2 state
`UNASSIGNED` / `NOT EVALUATED` unless a later, separately authorized evaluation
addresses the protocol's full evidence contract.

**A2 stop condition.** A unit-roof symbolic determinant does not become an A2
result for a different physical-roof suspension without a proof of identity.
An operator/determinant from a control or unrelated model is evidence about
that control/model only.

## 7. Controls, stop rules, and fork discipline

### Mandatory controls

Each future paper must state which of the following are applicable and why:

1. **Arithmetic controls:** shuffled labels, random/density-matched integers,
   composites-only or altered arithmetic labels.
2. **Geometric controls:** nearby parameter, non-symplectic/dissipative or
   simpler-parent comparison, altered roof where legitimate.
3. **Ownership controls:** same base map with a changed roof, same symbolic code
   with a different flow, and calibrator/operator separation.
4. **Robustness controls:** cutoff, precision, normalization, and enumeration
   completeness variations.
5. **`PROVES_TOO_MUCH` control:** test whether the alleged mechanism can encode
   arbitrary prescribed data with comparable ease.

### Immediate stop / fork events

Stop the current candidate rather than repair it rhetorically when any occurs:

- its exact base map, roof, object identity, or allowed data change;
- the arithmetic source is an external prime/zero selector;
- the physical flow no longer owns the clock, orbit ledger, analytic object, or
  claimed determinant;
- no specified control could distinguish the claimed mechanism from fitting;
- a later Hamiltonian/contact/quantum idea requires a new object not shown to
  inherit the earlier owner chain.

Archive a short Markdown paper record for every stop. A genuinely altered
construction gets a new candidate ID, a new paper package, and a fresh P0
card; prior results are then cited only as scoped antecedents.

## 8. Route B is explicitly deferred

Route B concerns operator definition/domain (B1), self-adjointness (B2), target
spectral type (B3), prime-power trace / Weil-form compatibility (B4), and a
completed-\(\Xi\) determinant/divisor identity (B5). It is not a shortcut
around weak arithmetic, orbit, or determinant ownership.

For this project:

```text
Current Route B state: NOT INVOKED.
Formal entry condition: a separately authorized candidate-specific evaluation
only after Route A reports ROUTE_A_SUCCESS_ROUTE_B_READY, rather than after
A0--A2 alone.
```

No current document may claim a self-adjoint Hilbert--Pólya operator, a required
spectral type, a prime-power/von-Mangoldt trace, Weil compatibility, a
completed-\(\Xi\) determinant identity, Riemann-zero identification, or RH.

Before Route-A readiness, a separately authorized *limited early audit* may
only examine a candidate's prospective Hilbert space/quantization coherence,
an obvious self-adjointness obstruction, or membership in a known exact
trace-formula framework. It must not issue a Route-B coordinate or verdict and
must not rescue a weak A0--A2 chain.

## 9. Markdown-only paper protocol

This project records every substantive conclusion—positive, negative,
inconclusive, theorem-level, computational, or methodological—in a Markdown
paper package under `papers/`. See [papers/README.md](papers/README.md) and
[papers/paper-template.md](papers/paper-template.md).

Minimum package layout after a candidate is frozen:

```text
papers/NNN-short-slug/
  README.md                 # stable status card and navigation
  paper.md                  # complete Markdown paper; authoritative prose
  candidate-card.md         # P0 identity/ownership record
  claim-ledger.md           # scoped claims and evidence states
  evidence/README.md        # provenance / reproducibility index when needed
```

Do not generate PDF or LaTeX for this Round-2 workspace unless the user later
asks for that different deliverable. A clean Markdown file, a completed paper
package, or a passing local check is not Route credit or a mathematical proof.

After any substantive update:

1. update the relevant paper and candidate card first;
2. append a concise result/boundary entry to [readme.md](readme.md);
3. retain failed controls and negative results rather than overwriting them;
4. verify local Markdown links, source identities, and any stated computation;
5. state explicitly what remains open and whether the object was forked.

## 10. Current nonclaims

At plan creation, this project does **not** claim any of the following:

- a concrete Arithmetic Symplectic Suspension Flow candidate;
- A0, A1, A2, A3, or A4 passage;
- a transferable result or Route credit from Logistic, Hénon, Symplectic,
  Symbolic, or Flow work;
- natural Markov coding, Hamiltonian realization, trace formula, determinant,
  or quantization for a presently unspecified map;
- a Route-B operator, self-adjointness, spectral identification, prime-power
  trace, Weil compatibility, completed-\(\Xi\) identity, RH, or a Riemann-zero
  match.

The first deliverable is therefore a fully specified P0 candidate card, not a
success narrative. A rigorously scoped obstruction or no-go result is an equally
valid outcome if it sharpens the next candidate choice.

## 11. Agent working order

For any authorized future task in this directory:

1. read [AGENTS.md](AGENTS.md), this plan, [readme.md](readme.md), and the
   relevant paper package;
2. open [roadmap/README.md](roadmap/README.md) before interpreting Route A/B;
3. verify the current candidate ID and every same-object ledger row;
4. perform only the work authorized by the current user request;
5. record the result with its object, evidence class, controls, and boundary;
6. stop or fork at the first ownership violation.

The full Phase-I wiki is a reference library, especially its
[agent start page](../p1_wiki/00-agent-start.md), but it does not supersede
this project's frozen candidate card or create permission to resume stopped
work in another stream.
