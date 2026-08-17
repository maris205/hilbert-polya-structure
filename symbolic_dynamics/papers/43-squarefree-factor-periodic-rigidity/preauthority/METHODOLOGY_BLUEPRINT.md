# Methodology blueprint

## Workflow contract

This Phase-1 package follows the academic-research, formula-derivation,
proof-writer, research-literature, and novelty-check contracts. Their concrete
effect is:

1. freeze the research question and factor category before proving it;
2. separate known source facts from newly assembled program consequences;
3. derive every formula from typed objects and explicit quantifiers;
4. state proof dependencies and edge cases;
5. search primary literature before assigning novelty;
6. expose controls that delete one hypothesis at a time;
7. freeze exact bytes before an independent adversarial decision.

No cross-model review transport was available during preparation. Independent
DA is therefore a required next stage, not an optional endorsement.

## Question decomposition

| Question | Evidence type | Required outcome |
|---|---|---|
| Is \(X_{\rm sf}\) compact and shift invariant? | direct topology proof | proved |
| Can two source points be made jointly zero on any finite window? | missing residues plus CRT | proved |
| Does proximality pass through \(\pi\)? | uniform continuity | proved |
| Can a proximal target contain a nontrivial periodic orbit? | finite-orbit separation | refuted |
| What is the target periodic ledger? | exact fixed-point count | singleton |
| What determinant does that ledger own? | Artin--Mazur definition | \(1-z\) |
| Can repetitions be retyped as rational primes? | primitive/repetition type audit | no |
| Is the result externally novel? | primary-source collision audit | at most minimal |

## Evidence labels

- `PROVED`: a complete proof is in `PROOF_PACKAGE.md`.
- `KNOWN_PRIMARY_SOURCE`: the result is already explicit in cited primary
  literature.
- `DIRECT_COROLLARY`: follows immediately from a proved or known result but is
  still proved locally for auditability.
- `MODELING_CHOICE`: fixed by the source card, not discovered.
- `STOP_SCOPED`: a repair changes an object, marker, observable, or category.
- `STOP_DUPLICATE`: an exact published collision would remove the bounded
  closure claim.

## Proof architecture

The proof is deliberately modular:

```text
prime-square admissibility
  -> one missing residue for each chosen prime and point
  -> pairwise-coprime CRT system for every finite window
  -> source proximality
  -> factor proximality
  -> unique periodic point in every factor
  -> exact fixed-point ledger
  -> Artin--Mazur zeta and inverse determinant
  -> rational-prime primitive-support obstruction
```

Each arrow has an independent falsifier. In particular, the final arithmetic
obstruction does not rely on zeros of any analytic function.

## Controls

### Positive controls

- Identity factor: retains the exact source theorem.
- One-point factor: has exactly one fixed point and determinant \(1-z\).
- Periodic-core matrix \(K=[1]\): realizes \(\det(I-zK)=1-z\) on the
  one-dimensional ledger only.

### Assumption-deletion controls

- For any finite prime set \(P_0\), set
  \(Q=\prod_{p\in P_0}p^2\) and
  \(x_n=\mathbf1_{n\equiv1\pmod Q}\). This is a nonzero periodic point whose
  support occupies only residue one modulo every selected \(p^2\). The
  modulus-four point \((0111)^{\mathbb Z}\) is an additional concrete control.
- Add an external periodic system by product: cycles appear, but this is an
  extension, not a factor repair of the frozen object.
- Forget continuity, equivariance, or surjectivity: the resulting map is
  outside the theorem.
- Replace Artin--Mazur counts with an aperiodic or measure zeta: this changes
  the observable.

## Literature protocol

The search used source-specific, theorem-specific, factor-specific, and recent
power-free-shift queries. Primary arXiv, publisher, DOI, and institutional
pages were preferred. The exact publication claims were checked against the
2025 revision of the most relevant recent factor paper. Failure to find an
exact collision is recorded only as a search result, never as proof of
novelty.

## Governance protocol

- Terminal Paper 39 is an existence and closure audit, not a ranking.
- Papers 40, 41, and 42 are collision and chronology boundaries only.
- The root commission fixes the remaining universe \(\{\mathrm{C02,C03,C05}\}\).
- The rule choosing C02 was constructed retrospectively after every card
  outcome and the present theorem were known.
- Only root governance may authorize an authority path or Route record.
