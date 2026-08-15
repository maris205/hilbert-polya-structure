# HCS-C56 integrity report

Status: **DOCS_FINAL_NO_MORE_EDITS; official documentation integrity PASS for
the project RELEASE_FROZEN.**

This report describes the integrity boundary of the frozen project release.
It binds independently checked prefreeze code/results evidence, the written
proof boundary, the official documentation build, and implementation commit
`b32402f1dd276a2684d3e849dae26150ebb595e1`.  A separate self-excluding
full-project manifest provides release-wide integrity without replacing the
scoped machine identity; the provenance commit remains null/external.

## 1. Owned scope

The documentation lane may create or edit only:

- the root HCS-C56 formal and planning documents;
- the paper subtree drafted after the exact handoff;
- the root route_a_evaluation.yaml record.

It does not create or alter code, results, top-level registries, codex_prompt,
commits, or remote publication.  It records the root-supplied implementation
commit but does not invent a separate provenance commit.  The existence of an
unreviewed file outside the owned scope is not evidence for any theorem premise.

## 2. Current integrity state

| Layer | State | What has been checked |
|---|---|---|
| research question | LOCKED | object, scope, falsifiers, and success criterion |
| theorem package | PREFREEZE PASS | C56-EXACT-0 through C56-EXACT-4 are certified |
| proof package | PREFREEZE PASS | global-scheme, irreducibility, Galois, Picard, and field-degree deductions |
| primary sources | PASS AT CITATION LEVEL | exact named locators and claim boundaries |
| bounded neighbor search | COMPLETE FOR STATED QUERIES | supports only a bounded-search statement |
| machine payload | PREFREEZE PASS | canonical exact instance payload |
| independent machine check | PASS | all 10 semantic gates independently derived |
| semantic mutation audit | PASS | 2684/2684 rebound cases and 15/15 tests |
| paper source | ISOLATED PREFREEZE PASS | clean fresh-copy compile; live source bytes and mtimes unchanged |
| official compilation | PASS | 19-page PDF; zero warnings; fonts/text/visuals clean |
| release provenance | RELEASE_FROZEN | implementation commit bound; scoped identity and documentation hashes retained; 46-entry full manifest verified separately; provenance commit null/external |

## 3. Upstream integrity contract

The only upstream mathematical object is the exact C55 primitive Yukawa
cubic surface. Its release contract has three deliberately different layers:

- the C55 Route is RELEASE_FROZEN;
- C55 documentation is DOCS_FINAL_NO_MORE_EDITS;
- C55 code/results and certificate artifact statuses remain
  RELEASE_CANDIDATE by design.

The C56 importer validates this exact combination from committed objects,
replays the C55 checker, and reconstructs the ordered primitive 20-row cubic.
The source-lock gate passes; this does not alter the intentionally layered C55
statuses.

## 4. Source integrity

The source audit uses primary or authoritative mathematical sources for the
claims on which the proof depends:

1. Kass--Wickelgren for the Grassmann-bundle line section, total rank 27,
   simple zeros, and separability roles;
2. Elsenhans--Jahnel for the \(W(E_6)\) containment, the index-two subgroup,
   the parity warning, and the transitivity/order-five criterion;
3. the Hochschild--Serre low-degree exact sequence, via the exact locator in
   SOURCE_AUDIT.md, for the rank-only Picard descent step.

Each citation is narrower than the desired instance theorem. None supplies
the C56 eliminant, modular factors, Weyl enumeration, or fixed-rank
calculation.  Those are internal exact obligations certified by the current
producer/checker rather than by the literature.

Temporary downloads, architecture notes, reconnaissance scripts, and hostile
review files are chronology only. Their paths and digests are intentionally
absent from the release fields.

## 5. Theorem-integrity checks

The formal package enforces the following dependency separations:

- the classical total of 27 and the simple-zero statement are distinct
  inputs;
- the chart morphism first lands in the open \(F_1(Y)\cap U_{01}\);
- finite étaleness makes that open open-and-closed before it is treated as a
  global closed subscheme;
- equal rank proves global equality only after the closed-immersion step;
- modular factorization proves irreducibility only through complete factors,
  squarefreeness, and the subset-sum intersection;
- irreducibility makes the line action transitive but does not alone prove
  full \(W(E_6)\);
- the target Frobenius class excludes \(U\) by Coxeter determinant, never by
  ordinary \(S_{27}\) sign;
- \(E\) is the degree-27 residue field, whereas \(K\) is its normal closure;
- Hochschild--Serre is used for equality of ranks, not integral Picard-group
  equality.

## 6. Claim-boundary integrity

The exact prefreeze C56 claims concern only:

- the complete line scheme;
- its degree-27 connected residue field;
- the full \(W(E_6)\) normal closure;
- geometric and arithmetic Picard ranks;
- nonexistence of a rational line and divisibility of line-definition field
  degrees;
- invariance under rational projective coordinate change and common scaling.

The package does not infer a rational point, rationality, stable rationality,
a Hasse or Brauer--Manin statement, a zeta or \(L\)-function statement, a
motive, a VHS, a Calabi--Yau realization, or a generic-family theorem.

## 7. Current provenance fields

| Identifier | Value |
|---|---|
| payload SHA-256 | `5b17c9ed7bea60680556af70297199b653d51188bb30ce59f7c2c6bfbc94f661` |
| canonical schema SHA-256 | `ef26d7204a38e28aaf00eed8188b31d34d590c9c8a19924f1d0798e40b052d5f` |
| schema-file SHA-256 | `adab34998a944c8a4af8db774e511f0453839ea6a6e14e9437ffc259be3da504` |
| certificate SHA-256 | `26739ce5aedb4a3467645f9c1b2036d4d3eec9ce4d0dbce23d67ea7b67e5fbc4` |
| independent-check SHA-256 | `4ccfb09139a4bfa812ea9c57ff8b65a6a8e603dbdb00e245355a4563386489a9` |
| scoped 12-entry code/results manifest SHA-256 | `20d29af97128e766bb5e59bf6f82f8401c6ed62f279371b031febcefd5d99b4a` |
| semantic gates / rebound / tests | `10/10`; `2684/2684`; `15/15` |
| producer SHA-256 | null; bound by scoped manifest |
| checker SHA-256 | null; bound by scoped manifest |
| tests SHA-256 | null; bound by scoped manifest |
| implementation commit | `b32402f1dd276a2684d3e849dae26150ebb595e1` |
| provenance commit | null; external/not separately promoted |
| full-project manifest successor | root `FULL_PROJECT_HASHES.sha256`; 46 entries, self-excluding, verified separately; digest external-only |
| paper-source SHA-256 | `5db4cfd2650485001d00fc2f52681d4cfaf8e739f4924b331df7ccc06a851cb3` |
| paper PDF SHA-256 | `750c1da7366701495fa3bf1f37014000d56fcb59a556f896224a5611b622a923` |
| paper log SHA-256 | `9f2845fdc37011aa259085810595703819741844be0d0ff15cdfc78c94e41a07` |
| extracted-text SHA-256 | `217ca51b1b0b4e6637f3d8405f23671aa89775d30e37ac964cb0684b548c2856` |
| compilation-report SHA-256 | `fd7c17d5121d4661b4fb385e2ab420882cfced172f9c5098c4152d68c6d5a3c8` |
| Route-record external SHA-256 | null |

Null in the provenance-commit and Route-self-hash rows means not separately
promoted under the external-only policy.  The full-project manifest digest is
likewise external-only to avoid a self-reference cycle.  Neither policy permits
a temporary calculation to replace the scoped prefreeze identity, the exact
implementation commit, or official documentation artifacts.

## 8. Completed integrity audits

The following prefreeze integrity audits pass:

1. the committed C55 rebind and status contract;
2. producer/checker independence and complete payload agreement;
3. semantic coverage of every scalar leaf under rebound mutation;
4. rollback atomicity and read-only nonmutation;
5. exact theorem/source wording after numerical backfill.

The official paper log/reference/destination/font/text/visual review also
passes.  Scoped provenance uses its 12-entry manifest; paper/report hashes are
recorded above; Route and report self-digests remain external-only.  The root
46-entry self-excluding full-project manifest is verified separately, and
implementation commit `b32402f1dd276a2684d3e849dae26150ebb595e1` is bound.
The provenance commit remains null/external.  This closes the documentation
lane at `DOCS_FINAL_NO_MORE_EDITS` and the project at `RELEASE_FROZEN` while
leaving the machine evidence at `PREFREEZE_CODE_RESULTS_PASS`.
