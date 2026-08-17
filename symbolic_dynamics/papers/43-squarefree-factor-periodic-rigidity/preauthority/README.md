# Paper 43 Phase-1 preauthority package

## Proposed identity

- Proposed candidate: `SD-C45`
- Historical parent: `SD-C02`
- Working title: **Factors Cannot Resurrect Cycles: Proximal Periodic-Ledger
  Rigidity of the Squarefree Admissible Shift**
- Status: `INPUTS_FROZEN_FOR_INDEPENDENT_DA`
- Authority status: no authority write, registry edit, manifest edit, mirror
  write, or Git operation is authorized by this package.

## Exact outcome

Let

\[
X_{\rm sf}=\left\{x\in\{0,1\}^{\mathbb Z}:
\operatorname{supp}(x)\bmod p^2\ne \mathbb Z/p^2\mathbb Z
\text{ for every rational prime }p\right\}
\]

with the two-sided left shift \(\sigma\). If

\[
\pi:(X_{\rm sf},\sigma)\twoheadrightarrow(Y,S)
\]

is any continuous surjective equivariant map to a compact metrizable
\(\mathbb Z\)-system, then \(Y\) has exactly one periodic point, namely
\(\pi(0^{\mathbb Z})\). Consequently, for every \(m\ge 1\),

\[
\#\operatorname{Fix}(S^m)=1,
\qquad
\zeta_{\rm AM,Y}(z)=\frac{1}{1-z},
\qquad
D_{\rm AM,Y}(z)=1-z.
\]

The mechanism is exact and short:

1. distinct prime-square missing residues and the Chinese remainder theorem
   make \(X_{\rm sf}\) proximal;
2. continuous factors of proximal compact systems are proximal;
3. a proximal system containing a fixed point has no other periodic point.

This closes the factor loophole for this particular source. It is not the
false general claim that factors of arbitrary aperiodic systems are
aperiodic.

The infinite exclusion family is essential. For any finite prime set
\(P_0\), put \(Q=\prod_{p\in P_0}p^2\) and let \(x_n=1\) exactly when
\(n\equiv1\pmod Q\). This nonzero \(Q\)-periodic point occupies only residue
one modulo every \(p^2\), so it satisfies every constraint in \(P_0\).
Therefore no finite prime-square approximant has the full periodic-collapse
or proximality conclusion.

## Route consequence

The strict expected Route-A v0.2 tuple is

```text
(A0_FAIL, A1_FAIL, A2_ANALYTIC_DETERMINANT, A3_FAIL, A4_FAIL)
overall = ROUTE_A_REJECTED
route_b_invocation_allowed = false
```

The determinant is exact only for a singleton primitive fixed-orbit ledger.
It carries no rational-prime primitive species, completed divisor, or
same-ledger Hilbert--Polya operator.

## Novelty warning

The source, its proximality, and the elementary permanence facts receive zero
novelty credit. The only possible contribution is a very narrow typed closure
inside this program: the source-specific factor theorem is joined explicitly
to the Artin--Mazur ledger, marker, determinant owner, repairs, and Route
falsifiers. The literature audit therefore recommends this package only as an
internal exact closure, not as a standalone novelty claim.

## Package map

- `RESEARCH_QUESTION_BRIEF.md`: scoped question and answer
- `METHODOLOGY_BLUEPRINT.md`: evidence and audit workflow
- `SELECTION_AND_PROVENANCE.md`: retrospective selector and chronology limits
- `SOURCE_LOCK.md`: frozen source and factor class
- `OBJECT_MARKER_OPERATOR_CONTRACT.md`: type and ownership firewalls
- `DERIVATION_PACKAGE.md`: formula chain and repair analysis
- `PROOF_PACKAGE.md`: theorem-grade proofs
- `THEOREM_FALSIFIERS.md`: decisive refutations and stop rules
- `EXACT_WITNESS_LEDGER.md`: exact controls and recomputation targets
- `LITERATURE_NOVELTY_AUDIT.md`: primary-source collision audit
- `ROUTE_EXPECTATION.yaml`: live Route-A v0.2 expectation
- `ROUTE_RECORD_CENSUS.md`: predecessor and authority census
- `DA_HANDOFF.md`: independent-review instructions
- `SOURCE_HASHES.sha256`: portable source/dependency seals
- `RESEARCH_LOCK.json`: immutable research-input seal
- `SHA256SUMS.txt`: sorted, self-excluding package manifest

The intended portable integration namespace is
`papers/43-squarefree-factor-periodic-rigidity/preauthority`.
