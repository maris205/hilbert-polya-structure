# A Tree Has No Closed Geodesic

Paper 38 / Candidate `SD-C40`.

This paper tests the only affine successor authorized by Paper 37: the full
oriented-edge geodesic shift on the presentation-canonical Bass--Serre tree
of the original ascending HNN splitting

```text
BS(1,r) = <u,v | vuv^{-1}=u^r>,  r>=1,
```

with the canonical modular cocycle and no auxiliary representation.  It is a
new object and inherits neither the earlier Cayley-object credit nor the old
generator-step marker.

The result is terminal.  The literal full-tree primitive ledger is empty, and
the undamped Hashimoto operator is noncompact and not trace class.  For
`r>=2`, the tree action is faithful and its image is non-discrete.  For
`r=1`, the translation image is a discrete `Z`, but the original `Z^2` action
has kernel `<u>`, is non-proper, and fails the finite-stabilizer tree-lattice
hypotheses.  A separately typed positive-height group-conjugacy ledger exists
for `r>=2`, but it is the generic necklace product

```text
Z_{+,r}(z) = (1-z)/(1-rz),
```

not the full-tree Fredholm determinant.  At `r=1` it diverges.  Bass--Serre
translation length also collapses every `u^m` to zero, so the new tree-edge
clock is incompatible with the old marker.

## Frozen decision

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_FAIL,
 A2_FAIL,
 A3_FAIL,
 A4_FAIL)

overall: ROUTE_A_REJECTED
route_b_invocation_allowed: false
candidate: SD-C40
stop: STOP_BASS_SERRE_TREE_BRANCH
branch: CLOSE_ENTIRE_AFFINE_BRANCH
```

## Canonical authority integration

- Corrected evaluator assertions: `277/277`; scientific SHA-256
  `a9ffa66d826bcaf8eef0b00991aafa46cdbeaca7014430c68aacf070446adf24`.
- Fresh A/B and isolated cold C: `3/3` science, source-packet, and Route
  outputs byte-identical; the cold copy was removed.
- Integration tests: `44/44`; full integrity audit: `96/96`.
- Exact result set: `28` files; managed canonical text: `44` files.
- Immutable ledger: `42/42`, SHA-256
  `af2db7457808bcb956c284d28387bf74bfda59f329b688e9491b5ef38066d309`.
- Independent Route evaluation SHA-256:
  `984187abd5fced5e42c334763127ced28329fc4d9fbefe4d06b31427f509a434`.
- Fixed Route-A v0.2 YAML SHA-256:
  `32b2288b1397b084e73b4dd01d0bcc973f7326f963396463d532976e56d36a0c`.
- Experiment report SHA-256:
  `174b2ddf05fa41b5ddc06130fec14de628b51f410ec59dc905179a71f9eeb380`.
- Research lock SHA-256:
  `b338e75410116890e11b6d2d09a9d11c5c8e41fecd00a9c438997dde80435be3`.
- Corrected prototype lock and bridge SHA-256:
  `7a25ecee27974aa1f593f4793c7f44b8a940ad1b13f824f0a5f3c11669290c5b`
  and `25d95b5c0e06aac15bd673b1d6547cdef4e71277445b1e69356d05f7ebd6e657`.
- Corrected independent evaluator SHA-256:
  `0934d99fa05329d8146467e903b57f36e23588ce977354f3e948777c8ec5da13`.
- A second primary materialization changed no path: `changed_paths=[]`.

## Built manuscript

The final manuscript is 17 A4 pages and 517,244 bytes.  Its SHA-256 is
`61e731540f3546c0d2b728edfe124f5885d4a424cbf542d970ed02985a3117e9`.
The complete compile, font, citation, vector, and visual audits are recorded
in `COMPILATION_REPORT.md`.

## Ownership

Writer-owned files are `README.md`, `SOURCE_LOCK.md`, `PREREGISTRATION.md`,
the proof/derivation/literature/narrative/plan/round-two/figure documents,
`main.tex`, `math_commands.tex`, `references.bib`, `sections/`, `figures/`,
`main.pdf`, and `COMPILATION_REPORT.md`.

Independent experiment integration owns `code/`, `results/`, `experiments/`,
`evaluations/`, `docs/`, `EXPERIMENT_REPORT.md`, and Route ledgers.  The
repository root alone owns the future Stage-2 `PAPER_MANIFEST.sha256`, its
metadata-only seal, root README registration, Git operations, and mirror
synchronization.  This writer does not create or modify any of those paths.

## Frozen successor boundary

Paper 39 may only synthesize the affine-branch closure as a typed obstruction
DAG and return control to the pre-existing global Symbolic Dynamics registry.
It may not introduce another affine representation, quotient, local system,
cocycle, tree, damping, or marker.
