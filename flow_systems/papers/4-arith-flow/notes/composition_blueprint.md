# Composition Blueprint — Paper 4

Date: 2026-08-13  
Candidate: `FF-FROB-SUSP-P1-F2`  
Status: proof-complete composition plan; not a manuscript

## 1. Proposed paper identity

**Working title**

> One Clock, One Characteristic: A Frobenius-Suspension Positive Control for
> Arithmetic Flow Zeta Functions

**Short title**

> Frobenius Suspension and the One-Clock Boundary

**Central thesis**

The constant-roof suspension of Frobenius on the discretized geometric points
of \(\mathbb P^1/\mathbb F_2\) realizes its native Hasse--Weil zeta exactly,
including primitive objects, repetition coefficients, and norm weights; the
same proof also shows why a fixed finite-field clock cannot realize rational
primes across characteristics, while the obvious disjoint-prime repair is a
universal target compiler and fails Route A at its arithmetic entry gate.

**Paper type**

- theorem-and-obstruction paper;
- exact positive control plus exact negative transfer boundary;
- no Hilbert--Polya claim;
- no Route-B invocation;
- no numerical discovery claim.

**Recommended length**

Approximately 7,000--9,000 words, excluding appendices and bibliography.

## 2. Abstract logic

The English and Chinese abstracts should follow the same five-sentence logic.

1. State the methodological problem: exact Euler-product matching is meaningful
   only when primitive objects and clocks emerge from a frozen arithmetic
   dynamics.
2. Define the positive control: square Frobenius on
   \(\mathbb P^1(\overline{\mathbb F}_2)\) with the disclosed discrete topology
   and roof \(\log2\).
3. State the exact theorem: closed points, primitive Frobenius cycles, and
   primitive suspension orbits coincide, with period
   \(\deg(x)\log2=\log N(x)\), and the orbit zeta equals
   \(1/((1-2^{-s})(1-2^{1-s}))\) for \(\Re s>1\), followed by meromorphic
   continuation.
4. State the boundary theorem: a fixed \(Q=\ell^f\) clock intersects only the
   \(\ell\)-prime-power clock; disjoint \(\log p\) circles are exact but
   target-encoded.
5. Give the calibrated conclusion: native Route A succeeds as a finite-field
   control, the Riemann target is rejected, and the next construction must
   couple residue characteristics in one non-disjoint phase space.

Avoid saying that the finite-field result provides evidence for RH.  Avoid
calling the orbit zeta a trace-class determinant.

## 3. Recommended section architecture

### 1. Introduction: why a positive control is needed

- Motivate the three interfaces that an arithmetic flow must keep on the same
  object: arithmetic source, primitive-orbit ledger, and zeta/determinant.
- Explain that the paper asks for a case where all three interfaces close
  exactly before testing characteristic-zero transfer.
- State the main positive theorem and the two negative boundary theorems.
- Place the result in Route A: exact native calibration, rejected Riemann
  candidate, Route B false.
- List contributions without novelty inflation: the classical identities are
  known; the contribution is their source-locked flow synthesis and adversarial
  separation.

### 2. Sources, conventions, and candidate lock

- Fix arithmetic Frobenius \(F(a)=a^2\), not geometric Frobenius.
- Disclose the discrete topology as `MODELING_CHOICE`.
- Define the mapping torus, vertical flow, primitive-orbit convention, and
  unweighted zeta.
- State allowed and forbidden inputs.
- Explain why inverse Frobenius changes orientation but not the frozen zeta.
- Cite `DEL74`/`DEL-EN` for the closed-point dictionary, `AM65` for fixed-point
  zeta, `PP90` for suspension conventions, and the Stacks/Milne sources only for
  supporting definitions and convergence checks.

### 3. From irreducible polynomials to primitive flow circles

- Prove that monic irreducible \(f\in\mathbb F_2[T]\) of degree \(d\) gives a
  Frobenius cycle of exact length \(d\).
- Add the point at infinity and record \(a_1=3\).
- Derive \(N_n=2^n+1=\sum_{d\mid n}d a_d\).
- Prove the mapping-torus circle decomposition.
- State precisely what is canonical: the closed point identifies the cycle and
  its suspension orbit canonically; a coordinate on the circle depends on a
  choice of root/base point.
- Prove least period, completeness, and local finiteness.
- Audit Hausdorffness, local compactness, second countability, and noncompactness.

### 4. Exact orbit zeta and endogenous weights

- Derive the Artin--Mazur/orbit/Hasse--Weil identity as formal power series.
- Specialize to \(\mathbb P^1/\mathbb F_2\).
- Separate primitive factors from repeated traversals.
- Derive \(1/r\) from \(-\log(1-u)\).
- Derive \(\log N(x)\) from \(-d/ds\).
- State explicitly what is absent: half-shift, sign, complex phase, stability
  denominator, and a nontrivial transverse monodromy.

### 5. Convergence, continuation, and the imaginary clock

- Prove absolute convergence exactly for \(\Re s>1\).
- Give the rational continuation and native functional relation.
- Exhibit imaginary periodicity \(2\pi i/\log2\) and the two pole lattices.
- Distinguish three determinant notions:
  1. primitive-orbit Euler product;
  2. Artin--Mazur fixed-point zeta;
  3. etale-cohomological Frobenius determinant.
- Say that equality of the scalar functions does not construct an operator
  equivalence between the circle flow and etale cohomology.

### 6. One clock cannot cross characteristics

- State and prove \(n\log Q=r\log p\Rightarrow p=\ell\) for
  \(Q=\ell^f\).
- Give the primitive corollary \(n\log Q=\log p\Rightarrow Q=p\) and
  \(f=n=1\).
- Explain why changing the variety over fixed \(\mathbb F_Q\) does not change
  the period lattice.
- Use Dirichlet-series uniqueness to contrast the finite-field imaginary period
  with the rational Euler product, without zero data.
- Conclude A0/A2 failure for the Riemann target.

### 7. The exact repair that proves too much

- Prove the arbitrary-length circle-compiler theorem first.
- Specialize to \(L_p=\log p\) only afterward.
- Explain the information-flow failure: target primitive labels and target
  roofs precede dynamics.
- Show that coordinate-free indexing by
  \(|\operatorname{Spec}\mathbb Z|\) does not remove the circularity.
- Add the same-cycle-type permutation control for all-points-periodic
  permutations: matching every finite cycle count determines the bare
  suspension.  Explicitly exclude additional infinite orbits, which the
  finite cycle counts would not see.  The topology alone still cannot recover
  algebraic/cohomological provenance.
- Assign `STOP_SCOPED / PROVES_TOO_MUCH`.

### 8. Dual Route-A assessment

- Present native and Riemann-target columns side by side.
- Native: A0 analytic, A1 analytic, A2 analytic orbit determinant, A3 controlled
  continuation, A4 fail.
- Riemann: A0 fail, A1 exact but wrong-support, A2 fail, A3 fail, A4 fail.
- Add a third compact row for the tautological `Spec Z` control.
- State `route_b_invocation_allowed: false` in text, not only metadata.

### 9. Deterministic controls

- Describe polynomial representation and the Frobenius/Rabin irreducibility
  test.
- Report finite degree counts and fixed-point reconstruction.
- Report formal-series coefficient equality.
- Show the repetition/derivative ledger.
- Treat convergence and periodicity outputs as regression controls, not
  evidence upgrading exact proofs.
- Give reproduction command and artifact hashes.

### 10. Discussion and next construction

- Retain the finite-field model as the clean positive structural prior.
- Accept the hostile objection that discretization turns the flow into an orbit
  ledger in geometric dress.
- Explain what remains valuable: all normalization decisions are visible and
  exact, so the control reveals what a successful characteristic-zero object
  must additionally supply.
- State the next theorem obligation: a single coupled non-disjoint phase space
  across residue characteristics with an emergent norm clock.

### 11. Limitations and conclusion

- Discrete topology is imposed.
- Flow components are neutral circles.
- No trace-class flow operator is constructed.
- No natural Weil compression or quantum lift is supplied.
- Native cohomological continuation is not a Riemann bridge.
- End with the positive/negative two-sentence result, not speculation.

### Appendices

- Appendix A: finite-field polynomial arithmetic and irreducibility criterion.
- Appendix B: formal Euler-product coefficient proof.
- Appendix C: complete Route-A machine-readable evaluation if the main text
  uses only a compact table.
- Appendix D: artifact manifest and software environment.

## 4. Main theorem package

### Theorem A — Frobenius-suspension orbit dictionary

For the frozen candidate,

\[
  |\mathbb P^1_{\mathbb F_2}|
  \longleftrightarrow
  \{\text{primitive Frobenius cycles}\}
  \longleftrightarrow
  \mathcal P(M_F)
\]

is a bijection, and \(\ell_x=\deg(x)\log2\).  Every flow point is periodic and
the primitive-orbit ledger is locally finite.

### Theorem B — exact native zeta

As a formal identity, and analytically for \(\Re s>1\),

\[
  \zeta_{\rm orb}(s)=Z(\mathbb P^1,2^{-s})
  =\frac1{(1-2^{-s})(1-2^{1-s})}.
\]

The rational expression gives meromorphic continuation.  The \(1/r\) and
\(\log N(x)\) weights are endogenous.

### Theorem C — one-clock obstruction

If \(Q=\ell^f\) and \(n\log Q=r\log p\), then \(p=\ell\).  Thus no fixed
finite-field clock produces rational-prime periods across characteristics.

### Theorem D — arbitrary Euler-product compiler

Every countable locally finite positive length multiset is the primitive length
multiset of a disjoint union of translation circles.  Hence the exact
disjoint-prime realization of \(\zeta\) is not generative evidence.

## 5. Claim ledger

| ID | Claim | Status | Proof/source | Manuscript use |
|---|---|---|---|---|
| C1 | closed points are Frobenius cycles | `PROVED` | `DEL74` §1.4 + Proof Audit §3 | theorem premise |
| C2 | affine closed points correspond to monic irreducibles | `PROVED` | direct finite-field proof | constructive ledger |
| C3 | cycle size equals residue degree | `PROVED` | direct proof + `DEL74` | Theorem A |
| C4 | suspension component is one circle of period \(d\log2\) | `PROVED` | direct quotient map | Theorem A |
| C5 | quotient is LCH, Hausdorff, second countable, noncompact | `PROVED` after `MODELING_CHOICE` | direct topology proof | scope disclosure |
| C6 | orbit, Artin--Mazur, and Hasse--Weil zetas agree | `PROVED` | formal divisor reindexing | Theorem B |
| C7 | P1 zeta is \(1/((1-z)(1-2z))\) | `PROVED` | point-count exponential | Theorem B |
| C8 | \(1/r\) and \(\log N(x)\) are endogenous | `PROVED` | expansion and differentiation | normalization result |
| C9 | absolute convergence is exactly \(\Re s>1\) | `PROVED` | positive-series comparison | analytic boundary |
| C10 | finite-field determinant is imaginary-periodic | `PROVED` | rational dependence on \(2^{-s}\) | Riemann incompatibility |
| C11 | one clock sees only its characteristic | `PROVED` | unique factorization | Theorem C |
| C12 | disjoint circles compile any length product | `PROVED` | componentwise flow theorem | Theorem D |
| C13 | circle flow supplies a cohomological operator bridge | `NOT_TESTABLE` | no operator map | forbidden promotion |
| C14 | construction supplies Riemann gamma/sign/half-weight | `REFUTED` for frozen object | source lock | Riemann rejection |
| C15 | natural quantum lift exists | `NOT_TESTABLE` | absent structure | A4/Route-B boundary |

## 6. Source-to-claim map

| Source key | Claims it may support | Claims it must not be used to support |
|---|---|---|
| `AM65` | fixed-point zeta definition; finite-field power-map example | transfer operator for this LCH flow |
| `DEL74` / `DEL-EN` | closed-point product; Frobenius dictionary; cohomological determinant; native FE | operator conjugacy to circle translation; Riemann transfer |
| `PP90` | standard suspension convention and roof-sum period | compact/hyperbolic hypotheses for the frozen countable-discrete base |
| `STACKS-01TF` | finite residue extensions | dynamical conclusions |
| `STACKS-03SL` | arithmetic/geometric Frobenius convention | phase or orientation amplitude |
| `MILNE13` | independent point-count/product/convergence check | novelty or quantum claims |

The direct topology proof is required because `PP90` does not by itself cover
the frozen noncompact countable-discrete base.

## 7. Figures and tables

### Figure 1 — three-way native dictionary

One horizontal diagram:

```text
irreducible f / closed point x
          <-> Frobenius root cycle of size d
          <-> suspension circle of circumference d log 2
```

Annotate `intrinsic arithmetic`, `discrete-topology modeling choice`, and
`vertical clock` separately.

### Figure 2 — the Route-A fork

Use one source node, `FF-FROB-SUSP-P1-F2`, with two target branches:

```text
native Hasse--Weil target -> exact A0--A3 calibration
Riemann target            -> one-clock support failure at A0/A2
```

Add the disjoint-circle repair below the failed branch and mark it
`exact product / A0_FAIL / PROVES_TOO_MUCH`.

### Figure 3 — clock lattices

Display \((\log Q)\mathbb N\) as one lattice and
\((\log p)\mathbb N\) for several symbolic \(p\).  Mark the theorem that an
intersection equality \(n\log Q=r\log p\) requires the same characteristic.
This should be schematic and not data-driven.

### Required tables

1. candidate lock and topology choices;
2. exact closed-point/fixed-point ledger for small degrees;
3. weight provenance (`primitive factor`, `log expansion`, `s derivative`);
4. native/Riemann/compiler Route-A comparison;
5. limitations and evidence labels;
6. reproducibility artifacts and hashes.

## 8. Equation order

Introduce equations in this dependency order:

1. mapping-torus quotient and vertical flow;
2. fixed-point ledger \(N_n=\sum_{d\mid n}d a_d\);
3. circle decomposition and \(\ell_x=\deg(x)\log2\);
4. Artin--Mazur exponential;
5. primitive Euler product;
6. \(\mathbb P^1\) rational expression;
7. logarithmic and derivative expansions;
8. convergence series;
9. imaginary periodicity;
10. one-clock Diophantine equality;
11. arbitrary circle compiler.

This order keeps every normalization derived before it is interpreted.

## 9. Artifact integration

The paper should cite these local artifacts by relative path:

- `notes/research_protocol.md` — preregistered obligations and controls;
- `notes/source_audit.md` — primary-source verification;
- `notes/candidate_lock.md` — frozen object and target split;
- `notes/proof_audit.md` — independent theorem audit;
- `code/frobenius_suspension_controls.py` — deterministic implementation;
- `code/test_frobenius_suspension_controls.py` — regression suite;
- `experiments/reproduce.sh` — one-command reproduction;
- `results/frobenius_suspension_manifest.json` — parameters and hashes.

The finite tables may appear in the paper, but the paper must not argue from
finite agreement to the theorem.  Proofs precede experiments.

## 10. Mandatory phrasing boundaries

Use:

- “exact native finite-field positive control”;
- “orbit-zeta identity”;
- “cohomological determinant with the same arithmetic source”;
- “disclosed discrete-topology modeling choice”;
- “one-clock obstruction”;
- “target-encoded universal Euler-product compiler.”

Do not use:

- “Hilbert--Polya realization”;
- “quantization of Frobenius suspension”;
- “trace formula of the circle flow” unless a trace operator is separately
  defined;
- “evidence for the Riemann hypothesis”;
- “emergent primes” for the disjoint-circle control;
- “canonical homeomorphism” when a coordinate on each circle depends on a
  chosen point of its Frobenius cycle;
- “absolute convergence after continuation.”

## 11. Declarations and limitations block

The final paper should include:

- no external funding unless project metadata later says otherwise;
- no conflicts of interest;
- no human/animal subjects;
- no external dataset;
- code and generated tables in the repository;
- AI-assistance disclosure consistent with the project convention;
- limitations: imposed topology, disconnected neutral flow, no flow-operator
  determinant, no natural Weil compression, no quantum lift, no Riemann claim.

## 12. Final quality gate before drafting

Drafting may begin only if all answers below remain “yes.”

1. Are native and Riemann targets named in every Route-A verdict?
2. Is the discrete topology called a modeling choice?
3. Is the exact identity first proved formally and only then assigned a
   convergence half-plane?
4. Are \(1/r\) and \(\log N(x)\) derived rather than inserted?
5. Is the cohomological determinant kept distinct from a flow transfer
   operator?
6. Is imaginary periodicity treated as a finite-field clock fingerprint?
7. Does the disjoint-prime construction fail A0 despite exact zeta matching?
8. Are all finite computations described as deterministic regression controls?
9. Are Riemann zeros absent from code, prose evidence, and parameter choices?
10. Is Route B explicitly false?

Current result: all ten gates pass.
