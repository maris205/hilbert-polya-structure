# Paper 44 preauthority candidate: q-adic finite-size boundary laws

## Proposed identity

- Proposed candidate: `SD-C46` (provisional label only)
- Proposed paper position: `Paper 44`
- Working title: **q-adic Finite-Size Boundary Spectra of Multiplicative
  Shifts of Finite Type**
- Status: `TMP_ONLY_PREAUTHORITY_CANDIDATE / NOT AN AUTHORITY ARTIFACT`
- Active superseding Phase-2 input seal:
  `/tmp/p44_48_phase2/SHA256SUMS.txt`, SHA-256
  `d035310ac046981abe7a37a033b1354e3d8da3f53f33d631786ed80f40b90181`
- Active Phase-2 verification before candidate freeze: `PASS 10/10`
- Superseded Phase-2 seal `db00401b...` is chronology only and is not an
  accepted input.

Stage-3 normalization correction: an earlier Phase-2 prose line described a
residue bracket only as a multiple of $\xi/(1-\xi)$. The exact Abelian
coefficient is $-1/(1-\xi)$. The former proportional wording is superseded;
the nonvanishing and natural-boundary conclusions are unchanged.

This directory is a disposable research candidate. It authorizes no authority
write, registry entry, Route record, root README edit, mirror write, Git
operation, novelty statement, priority statement, or claimed experimental
result.

## Frozen mathematical output

Let $q\ge 2$ and let $A$ be a primitive zero-one matrix. For the
multiplicative shift

$$
X_A^{(q)}=\{x:A_{x_n,x_{qn}}=1\text{ for every }n\ge1\},
$$

let $Z(N)$ count admissible prefixes on $\{1,\ldots,N\}$. Put

$$
W_0=1,\qquad W_\ell=\mathbf 1^T A^{\ell-1}\mathbf 1\quad(\ell\ge1),
\qquad c_v=\log\frac{W_{v+1}}{W_v}.
$$

The proved candidate package is

$$
\log Z(N)-\log Z(N-1)=c_{\nu_q(N)},
$$

$$
\log Z(N)-hN
=-\sum_{v\ge1}(d_v-d_{v-1})
  \frac{N\bmod q^v}{q^v},
$$

where $d_v=c_v-\log\rho(A)$ and

$$
h=\sum_{v\ge0}\frac{q-1}{q^{v+1}}c_v.
$$

The remainder extends continuously to $\mathbb Z_q$, and its image is the
complete accumulation set. In the binary golden-mean case the image is a
strongly separated Cantor set of Hausdorff and box dimension

$$
\frac{\log 2}{2\log\varphi}.
$$

The ordinary generating function of the bounded remainder has nonzero radial
pole-type coefficients at every primitive dyadic root of unity and therefore
has the unit circle as a natural boundary.

## Ownership ceiling

The multiplicative-SFT object, multiplicative-chain product, Fibonacci word
counts,
leading entropy, and leading dimensions are prior-owned and receive zero
novelty credit. Boundary-complexity and surface-entropy terminology is also
prior-owned. The only eligible research delta is the exact order-one
$q$-adic remainder, its complete accumulation image, the golden boundary
Cantor geometry, and the secondary radial-singularity corollary.

Ordinary Minkowski-content nonexistence is not included. The exact theorem
controls integer/dyadic cutoffs, not every continuous covering scale.

## Proof status

`LOCAL PROOF COMPLETE / PROVABLE AS STATED` for the scoped theorem in
`PROOF_PACKAGE.md`. This is a preauthority proof classification, not a
claimed published or experimentally validated result.

The following stronger or differently typed statements are not justified:

- reducible or periodic $A$ under the same theorem without a new case split;
- ordinary Minkowski-content nonexistence;
- a meromorphic-pole description of the full boundary function;
- an Artin--Mazur, Fredholm, or transfer-operator interpretation of the
  ordinary generating function;
- any external priority claim inferred from a bounded negative search.

## Package map

- `RAW_INPUT_MANIFEST.json`: neutral result-free source configurations that
  both evaluators must expand independently
- `RESEARCH_QUESTION_BRIEF.md`: exact question, answer, and non-goals
- `SOURCE_LOCK.md`: frozen object, assumptions, and ownership boundary
- `LITERATURE_NOVELTY_AUDIT.md`: primary-source and internal collision audit
- `OBJECT_MARKER_OPERATOR_CONTRACT.md`: type, cutoff, marker, and ownership locks
- `DERIVATION_PACKAGE.md`: normalized formula chain
- `PROOF_PACKAGE.md`: theorem-grade proof with dependency map
- `THEOREM_FALSIFIERS.md`: decisive falsifiers and literal mutations
- `EXACT_WITNESS_LEDGER.md`: exact integer and algebraic controls
- `METHODOLOGY_BLUEPRINT.md`: evidence and independence workflow
- `EXPERIMENT_PLAN.md`: claim-driven deterministic validation plan
- `EXPERIMENT_TRACKER.md`: execution ledger with no fabricated outcomes
- `SELECTION_AND_PROVENANCE.md`: retrospective Phase-2 chronology
- `ROUTE_EXPECTATION.yaml`: conservative preauthority Route expectation
- `ROUTE_RECORD_CENSUS.md`: confirms that no Route run/result is claimed
- `DA_HANDOFF.md`: independent-review instructions
- `SHA256SUMS.txt`: C-sorted, newline-terminated, self-excluding manifest

All artifact paths in `ROUTE_EXPECTATION.yaml` are relative to this directory.
