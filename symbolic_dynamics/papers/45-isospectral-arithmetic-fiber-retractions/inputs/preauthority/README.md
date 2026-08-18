# Paper 45 preauthority theory/source candidate

## Proposed identity

- Provisional identifier: P45-ALLH-RETRACTIONS-PREAUTHORITY
- Working title: Paired Arithmetic Retractions with One Cyclic Ledger and
  Different Nonnormal Geometry
- Stage: result-free preauthority theory and source freeze
- Scientific gate inherited from Phase 2: GO_WITH_FIREWALL
- Authority status: this directory authorizes no repository, mirror,
  registry, Route-record, or Git write.

## Exact object

For every integer \(h\ge 2\), let \(\mathcal F_h\) be the positive
\(h\)-free integers and define

\[
\tau_h(n)=\prod_p p^{\min(v_p(n),h-1)},\qquad
\omega_h(n)=\prod_p p^{v_p(n)\bmod h}.
\]

For \(s\in\mathbb C\), \(\sigma=\Re s\), the two algebraic weighted
retractions on the standard basis of \(\ell^2(\mathbb N)\) are

\[
S_{h,s}e_n=n^{-s/2}e_{\tau_h(n)},\qquad
M_{h,s}e_n=n^{-s/2}e_{\omega_h(n)}.
\]

The saturated operator \(S_{h,s}\) extends boundedly, and is compact,
exactly when \(\sigma>0\). The modulo operator \(M_{h,s}\) does so exactly
when \(\sigma>1/h\). On their common bounded domain they have the same
simple nonzero eigenvalues \(m^{-s/2}\), \(m\in\mathcal F_h\), but their
singular values, similarity geometry, and fiber masses differ.

## Claimed paper-sized remainder

The package claims only the following residual arithmetic theorem after all
mandatory ownership subtraction:

1. a complete all-\(h\) paired classification of boundedness, compactness,
   Schatten membership of powers, legal traces and regularized
   determinants, and bounded similarity to normal;
2. the exact primorial maximal order of the saturated Riesz projections,
   two explicit singular-value Weyl laws with
   \(C_{h,1}=D_{h,1}=1\), and a separate self-commutator ideal wall,
   including the \(h=2\) endpoint argument and Euler-product control.

Generic weighted composition, rank-one fibers, oblique projections,
Gram/Schatten methods, regularized determinants, classical power-free-part
maps, Tauberian/PNT/Mertens tools, and the free-UFD construction receive
zero novelty credit.

## Frozen endpoint ledger

\[
\begin{aligned}
S_{h,s}\text{ bounded/compact}&\iff \sigma>0,\\
M_{h,s}\text{ bounded/compact}&\iff \sigma>1/h,\\
S_{h,s}^k\in\mathcal S_q&\iff k\sigma q>2,\\
M_{h,s}^k\in\mathcal S_q&\iff \sigma>1/h\ \text{and}\ k\sigma q>2,\\
[S_{h,s}^*,S_{h,s}]\in\mathcal S_q&\iff \sigma q>1,\\
[M_{h,s}^*,M_{h,s}]\in\mathcal S_q&\iff
\sigma>1/h\ \text{and}\ \sigma q>1.
\end{aligned}
\]

Here \(k\ge1\) and \(0<q<\infty\). Every inequality is strict. Common
power traces are asserted only when both operators exist boundedly and
\(k\sigma>2\).

## Proof and evaluation status

The corrected theorem is proved in PROOF_PACKAGE.md and has already passed a
separate Phase-2 hostile derivation audit. This package contains no claimed
experimental output. EXPERIMENT_PLAN.md preregisters two genuinely
independent evaluators, exact canonical comparison fields, and
type/endpoint/source/firewall mutation suites for a later authorized run.

## Package map

- RESEARCH_QUESTION_BRIEF.md: narrow question, answer, and non-goals
- SOURCE_LOCK.md: definitions, domains, source hashes, and evidence boundary
- LITERATURE_NOVELTY_AUDIT.md: external and P27--P30/P43 subtraction
- OBJECT_MARKER_OPERATOR_CONTRACT.md: type, fiber, trace, and determinant
  ownership
- PROOF_PACKAGE.md: theorem-grade derivation with strict endpoints
- THEOREM_FALSIFIERS.md: decisive mathematical and governance stop rules
- EXACT_WITNESS_LEDGER.md: preregistered exact witnesses, not run results
- METHODOLOGY_BLUEPRINT.md: claim/evidence and evaluator architecture
- EXPERIMENT_CONTRACT.json: typed neutral cases, exact 15-case infinite
  coverage/hash gate, 13-row raw serialization grid, evidence schemas, and
  transaction policy
- EXPERIMENT_CONTRACT_SCHEMA.json: strict Draft-2020-12 schemas for all
  outputs, canonical-string/RFC8785 Dirichlet-power envelopes, duplicate-key
  policy, exact A/B/P coverage, certified intervals, hashes, coverage
  evaluation, outcomes, and structured errors
- EXPERIMENT_PLAN.md: result-free implementation and mutation plan
- MUTATION_REGISTRY.json: executable atomic mutation/consumer/rejection
  contract
- MUTATION_REGISTRY_SCHEMA.json: strict schema for exact consumers,
  RFC6901 replacements, symbolic-AST/raw-parser/coverage mutations, typed
  filesystem operations, and survivor semantics
- SELECTION_AND_PROVENANCE.md: chronology, hashes, and anti-priority record
- ROUTE_EXPECTATION.yaml: conservative, unevaluated Route expectation
- SHA256SUMS.txt: sorted self-excluding package manifest

## Release boundary

The final unique Phase-2 parent seal is
d035310ac046981abe7a37a033b1354e3d8da3f53f33d631786ed80f40b90181.
It supersedes every earlier Phase-2 manifest candidate.
This preauthority package is a candidate for independent evaluation only.
It must not be treated as an authority artifact, completed experiment,
publication decision, priority claim, or Route result.
