# Paper 32 — Projective Residue Recurrence Obstruction

**Title:** *Projective Residue Recurrence in Symbolic Dynamics: Universal
Modular Cycles and Cusp-Diamond Obstructions*

**Candidate:** SD-C34

Paper 31 closed terminal semiring verifiers: a completed accept/reject
computation may select prime cycles, but the whole recurrent operator is
noncompact or the verifier becomes transient, while first return changes the
clock.  Paper 32 therefore tests a nonterminal alternative.  Its states are
the projective residue lines
\(X_n=P^1(\mathbb Z/n\mathbb Z)\), every state carries the two modular
transitions
\[
 S[a:b]=[-b:a],\qquad R[a:b]=[-b:a+b],
\]
and the canonical cusps \(c_n=[1:0]_n\) are connected in both directions
between \(n\) and \(2n,3n\).

This construction satisfies the architectural requirements that defeated the
terminal branch: it has no accept/reject state, its marker-distinct recurrent
families share every state, different moduli share recurrent cusp states, and
the original uninduced graph-step operator is trace class on
\(\operatorname{Re}s>2\).  It nevertheless fails before weights are chosen.
The identities \(S^2=R^3=1\) hold projectively for every prime, prime power,
and mixed composite modulus.  Bidirectional cusp coupling also produces the
primitive nonbacktracking cycle
\[
 c_n\longrightarrow c_{2n}\longrightarrow c_{6n}
 \longrightarrow c_{3n}\longrightarrow c_n
\]
for every \(n\ge2\).  The top modulus \(6n\) is always composite.

The static equality
\[
 |P^1(\mathbb Z/n\mathbb Z)|=n+1
 \quad\Longleftrightarrow\quad n\text{ is prime}
\]
does separate fields from composite residue rings.  Using it to admit or
delete recurrent blocks is, however, exactly a completed primality gate and
is forbidden by the source lock.

The strict route record is

    (A0_STRUCTURAL_ARITHMETIC_RELATION,
     A1_FAIL,
     A2_ANALYTIC_DETERMINANT,
     A3_FAIL,
     A4_FAIL)

Decision: **ROUTE_A_REJECTED**.  Route B is locked.  Branch action:
**CLOSE_EUCLIDEAN_PROJECTIVE_RESIDUE_RECURRENCE_BRANCH**.  The negative
obstruction paper is `GO`; the prime-selective positive candidate is `STOP`.

## Writer-owned files

- `SOURCE_LOCK.md` — frozen research authority, source, theorem boundary, and
  writer limits
- `PREREGISTRATION.md` — candidate, information boundary, gates, and stop
  rules
- `PROOF_PACKAGE.md` — exact theorem statements and proofs
- `DERIVATION_PACKAGE.md` — source, cycle, trace-norm, and determinant
  derivations
- `LITERATURE_AUDIT.md` — primary-source matrix and bounded novelty statement
- `NARRATIVE_REPORT.md` — theorem-led interpretation and route decision
- `PAPER_PLAN.md` — claims/evidence map and manuscript architecture
- `ROUND2_CLUES.md` — branch closure consequences and Paper 33 obligation
- `FIGURE_SPEC.md` — pure-vector TikZ semantics and accessibility constraints
- `main.tex`, `math_commands.tex`, `sections/`, `figures/`, `references.bib`
  — modular manuscript source
- `main.pdf`, `COMPILATION_REPORT.md` — compiled manuscript and objective build
  audit

Experiment code, experiment plans, result ledgers, evaluator files, route
evaluation YAML, manifests, repository-level documentation, mirrors, and Git
state are integrator-owned and outside writer authority.

## Frozen research status

The infinite conclusions are theorem-backed and independent of a cutoff.  The
research prototype audits all 191 moduli from 2 through 192: 43 primes, 14
prime-power composites, and 134 mixed composites.  All 148 composites have
recurrent support; all 31 canonical cusp diamonds have composite top modulus;
48 of 48 random finite \(C_2*C_3\) actions reproduce the universal recurrence;
and 191 of 191 matched finite-semiring relabels transport the complete
addition/multiplication tables and projective graph exactly.

The canonical integration freeze independently passes 4,819,026 of
4,819,026 checks, including every entry of all matched addition and
multiplication tables and 56,318 projective edges.  All 13 deterministic
assertions pass; two fresh executions reproduce all 16 primary artifacts
byte for byte with aggregate SHA-256
`3cc4d3bddb5e771c5b2621110e9499b169359438d88608c36f8dc615ce73c727`;
and the final-tree integrity audit is `PASS`.  The canonical ledger SHA-256 is
`689a73a593f1791e6b2f49836b50cc2a11e5ddb1b91c46053af7aaa495ae4b8f`.
The result files remain integrator-owned; the writer records their frozen
counts and fingerprints without modifying them.
