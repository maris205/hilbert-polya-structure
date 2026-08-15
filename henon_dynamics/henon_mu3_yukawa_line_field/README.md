# HCS-C56: the twenty-seven-line field of the fourth Hénon Yukawa surface

Status: **DOCS_FINAL_NO_MORE_EDITS; project RELEASE_FROZEN against exact
PREFREEZE_CODE_RESULTS_PASS machine evidence.**

HCS-C56 starts from the fixed cubic surface over $\mathbf Q$ released by
HCS-C55 and studies a different arithmetic object: its Fano scheme of lines.
The terminal theorem is that this line scheme is one connected finite
étale point of degree $27$, that the Galois closure of its residue field has
group $W(E_6)$ of order $51840$, and that the surface has geometric/arithmetic
Picard ranks $7/1$ and no $\mathbf Q$-line.

The prefreeze producer/checker pair now certifies the large Gröbner, modular,
and Weyl-group calculations.  The written argument supplies the global
clopen scheme bridge, the subgroup implication, and the
Hochschild--Serre torsion/rank bridge.  This exact code/results prefreeze
evidence package underlies the project `RELEASE_FROZEN`, whose implementation
commit is `b32402f1dd276a2684d3e849dae26150ebb595e1`.

## Upstream object and frozen status contract

The upstream geometric input is the HCS-C55 primitive integral Yukawa cubic
$Y_H$ in its released rational tangent basis.  Its zero locus

$$
Y=V(Y_H)\subset \mathbf P^3_{\mathbf Q}
$$

is already proved smooth and geometrically irreducible by HCS-C55.

The C55 status is deliberately stratified and C56 must preserve that contract:

- C55 Route status is `RELEASE_FROZEN`;
- C55 documentation status is `DOCS_FINAL_NO_MORE_EDITS`;
- C55 machine `code_results_status` and the certificate's `artifact_status`
  intentionally remain `RELEASE_CANDIDATE`.

The last two values are not a pending-state defect.  The C56 importer
verifies this exact combination, the committed C55 object identity, the C55
checker, and the canonical 20-row primitive coefficient array.  It must not
replace the frozen contract by a rule that every upstream status leaf say
“final.”

## Target theorem, current gate

| Result | Written implication | Instance evidence now |
|---|---|---|
| $F_1(Y)$ finite étale of degree $27$ | total-rank/simple-zero sources plus exact smoothness | PASS |
| $F_1(Y)=\operatorname{Spec}(E)$ with $[E:\mathbf Q]=27$ | exact chart map, direct remainders, clopen bridge, irreducibility sieve | PASS |
| $\operatorname{Gal}(K/\mathbf Q)=W(E_6)$, $[K:\mathbf Q]=51840$ | transitivity, order-five Frobenius, Coxeter parity, and Elsenhans–Jahnel Lemma 8 | PASS |
| $\rho(Y_{\overline{\mathbf Q}})=7$, $\rho(Y/\mathbf Q)=1$ | machine fixed rank one plus written Hochschild–Serre rank bridge | PASS |
| no $\mathbf Q$-line; $27\mid[L:\mathbf Q]$ whenever a finite $L$ defines a line | $F_1(Y)=\operatorname{Spec}(E)$ and the tower law | PASS |

## Documentation package

- `THEOREM_PACKAGE.md` gives the exact prefreeze theorem and all claim
  boundaries.
- `DERIVATION_PACKAGE.md` derives the scheme, irreducibility, Galois, Picard,
  and line-degree implications step by step.
- `PROOF_PACKAGE.md` provides a proof-writer feasibility classification and a
  complete proof from independently certified exact inputs.
- `SOURCE_AUDIT.md` records primary-source locators and the bounded neighbor
  search.
- `RESEARCH_QUESTION.md` freezes the object, falsifiers, scope, and success
  criterion.
- `METHODOLOGY_BLUEPRINT.md` separates cited theorems, written deductions,
  instance computation, and adversarial verification.
- `EXPERIMENT_PLAN.md` and `EXPERIMENT_TRACKER.md` define the exact execution
  phases and current gate state.
- `IMPLEMENTATION_CHECKLIST.md` lists every source, scheme, arithmetic,
  Galois, integrity, and release obligation.
- `INTEGRITY_REPORT.md` records the frozen-release provenance boundary.
- `NARRATIVE_REPORT.md` gives the research interpretation with the scope
  firewalls intact.
- `PAPER_PLAN.md` tracks the frozen source and official build artifacts.
- `route_a_evaluation.yaml` records the exact prefreeze machine tuple and
  official documentation hashes.  The implementation commit is bound exactly;
  the provenance commit remains null/external, and the release-wide
  full-project successor is recorded and verified externally.

The full paper source and bibliography are frozen.  The fresh isolated audit,
controlled bootstrap, official final build, log/font/text/visual audit, and
compilation report all pass.

## Provenance state

The exact scoped/code-results and release-wide integrity identities are:

| field | value |
|---|---|
| C56 payload SHA-256 | `5b17c9ed7bea60680556af70297199b653d51188bb30ce59f7c2c6bfbc94f661` |
| C56 canonical schema SHA-256 | `ef26d7204a38e28aaf00eed8188b31d34d590c9c8a19924f1d0798e40b052d5f` |
| C56 schema-file SHA-256 | `adab34998a944c8a4af8db774e511f0453839ea6a6e14e9437ffc259be3da504` |
| C56 certificate SHA-256 | `26739ce5aedb4a3467645f9c1b2036d4d3eec9ce4d0dbce23d67ea7b67e5fbc4` |
| C56 independent-check SHA-256 | `4ccfb09139a4bfa812ea9c57ff8b65a6a8e603dbdb00e245355a4563386489a9` |
| C56 scoped 12-entry manifest SHA-256 | `20d29af97128e766bb5e59bf6f82f8401c6ed62f279371b031febcefd5d99b4a` |
| semantic gates / rebound / tests | `10/10`; `2684/2684`; `15/15` |
| C56 producer/checker/test direct release fields | bound by scoped manifest; otherwise `null` |
| C56 implementation commit | `b32402f1dd276a2684d3e849dae26150ebb595e1` |
| C56 provenance commit | `null`; external/not separately promoted |
| paper-source SHA-256 | `5db4cfd2650485001d00fc2f52681d4cfaf8e739f4924b331df7ccc06a851cb3` |
| paper PDF SHA-256 | `750c1da7366701495fa3bf1f37014000d56fcb59a556f896224a5611b622a923` |
| paper log SHA-256 | `9f2845fdc37011aa259085810595703819741844be0d0ff15cdfc78c94e41a07` |
| extracted-text SHA-256 | `217ca51b1b0b4e6637f3d8405f23671aa89775d30e37ac964cb0684b548c2856` |
| compilation-report SHA-256 | `fd7c17d5121d4661b4fb385e2ab420882cfced172f9c5098c4152d68c6d5a3c8` |
| project/docs status | `RELEASE_FROZEN`; `DOCS_FINAL_NO_MORE_EDITS` |
| full-project manifest successor | root `FULL_PROJECT_HASHES.sha256`; 46 entries, self-excluding, verified separately; digest external-only |

Temporary architecture and reconnaissance files are chronology only.  No
`/tmp` path or digest is release evidence.

## Non-negotiable firewalls

1. $E$ is the degree-$27$ residue field of one line.  It is not the Galois
   closure.  $K$ is the splitting field/normal closure in which all lines are
   defined.
2. “Odd” means outside the index-two subgroup
   $U\subset W(E_6)$, equivalently odd Coxeter/reflection determinant.  The
   permutation of the 27 lines has ordinary sign $+1$ for every element of
   $W(E_6)$, so an $S_{27}$ sign test cannot distinguish $U$.
3. Smoothness and the classical count of 27 lines do not imply connectedness
   or full $W(E_6)$.  Irreducibility and the odd-class exclusion are separate
   exact gates.
4. A main-chart computation is not allowed to assume that all lines lie in
   that chart.  The proof first constructs a degree-$27$ closed subscheme and
   compares it with the globally known degree-$27$ finite étale scheme;
   complementary-chart unit ideals are an independent replay guard.
5. The Picard conclusion is a rank statement.  Hochschild–Serre gives a
   torsion cokernel, not an unqualified integral equality
   $\operatorname{Pic}(Y)=\operatorname{Pic}(Y_{\overline{\mathbf Q}})^{G_{\mathbf Q}}$.
6. No rational line implies neither absence of rational points nor
   irrationality, a Hasse-principle failure, or a Brauer–Manin obstruction.
7. No line-field calculation proves a motive, a polarized VHS isomorphism, an
   honest Calabi–Yau threefold, automorphy, or any dynamical/RH claim.
8. The bounded literature search is a gap signal only, never a proof of global
   novelty.
