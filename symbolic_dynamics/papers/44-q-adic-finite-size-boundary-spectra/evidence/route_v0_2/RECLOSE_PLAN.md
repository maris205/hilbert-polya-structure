# Paper 44 canonical Route-A v0.2 acyclic reclose plan

Status: `HOLD_FOR_ROOT_INSTALL`.

This package is a fresh Route-A v0.2 evaluation of the unchanged `SD-C46`
object.  It is not a rewrite or downgrade of the historical v0.3 record at
`outputs/evaluations/route_a/SD-C46/2026-08-18.yaml`.

## Frozen science source

The source/proof/evaluator/mutation artifacts remain byte-identical to science
commit `b0e41ac3d6bd30618421d1b76122c3e9e04d070b`.  The fresh card therefore keeps
that value as `source_commit`.  No theorem, experiment, LaTeX, bibliography,
figure, or PDF byte is changed.

## H1 prime: static code only

The first new commit contains the renderer, both validators, the hostile
mutation runner, this plan, the publication-reclose code/contract changes, and
the separately root-owned tracked Phase-1/Phase-2 sequence packets.  It must
not contain the final v0.2 card or any validation receipt.  Its commit is the
evaluation-code provenance anchor supplied as the required `code_commit`
input to the renderer and both validators.

Canonical skill section 2 requires `code_commit` as an evaluation input, while
section 8 omits that key from the exact output schema and section 10 requires
the exact schema to be returned.  The canonical card therefore does not add a
top-level `code_commit` extension.  The primary, independent, and mutation
receipts record the H1-prime code commit instead.  The four executables bound
by that receipt field are:

```text
code/route/render_route_v0_2.py
code/route/validate_route_v0_2.py
code/route/audit_route_v0_2_independent.py
code/tests/run_route_v0_2_mutations.py
```

The synthetic commit used in `/tmp` is test-only.  Root must rerun the renderer
with the real H1-prime commit after all static paths, including the sequence
packets, have been staged and committed.

Both the renderer and primary validator execute
`git merge-base --is-ancestor <science-H1> <code-H1-prime>` and reject every
nonzero result before accepting matching code blobs.  The fixed hostile suite
also requires an orphan root commit containing exactly the same four code
blobs and no other paths; renderer, primary, and independent consumers must
all reject that unrelated-code-root fixture.  This makes code-byte equality
insufficient without science ancestry.

## H2 prime: derived records and seals only

Starting from clean H1 prime, render the append-only card at
`evaluations/route_a/SD-C46/2026-08-19.yaml`.  Run the primary and independent
validators and the hostile mutation suite, then install their canonical
stdout as:

```text
evidence/route_v0_2/PRIMARY_AUDIT.json
evidence/route_v0_2/INDEPENDENT_AUDIT.json
evidence/route_v0_2/MUTATION_RESULTS.json
```

The renderer and independent validator require that these four derived paths
are absent from H1 prime.  This prevents a card from claiming the commit that
already contains the card itself.

The mutation receipt covers 25 cases and 54 consumer invocations: the prior
24 card/physical mutations plus the three-consumer unrelated-code-root
provenance case, with one byte-exact renderer positive control and two
canonical-PASS validator positive controls.  The accounting is three positive
and 51 rejection invocations.  Its disposable Git
repository must contain both the real descendant H1 prime and a freshly built
four-blob orphan fixture; the orphan commit is never installed.

After the three receipts pass, update the project README, rebuild the writer
overlay manifest and publication seal with the current published overlay as
the predecessor, replay the publication smoke/auditor in a disposable root,
and regenerate `outputs/PAPER_MANIFEST.sha256`.  Commit only those derived
records, README registration, manifests, and seal as H2 prime.  The frozen
`PUBLICATION_SMOKE_EVIDENCE.json` remains byte-identical and is not restaged.

The publication protocol's out-of-band `--expected-stage1-commit` is a
different provenance domain from the Route evaluator's code H1 prime.  It
continues to be the historical science H1
`b0e41ac3d6bd30618421d1b76122c3e9e04d070b`, because the frozen State-B route
record under `outputs/evaluations/` binds that value in all three publication
route fields.  Supplying the newer evaluator-code H1 prime to the publication
auditor must reject with `ROUTE_STAGE1_COMMIT_MISMATCH`.

## Reachability and final checks

Final review must directly prove:

1. science source commit is an ancestor of H1 prime;
2. the card keeps the science source commit, while H1 prime is the exact
   `code_commit` in all three evaluation receipts;
3. H1 prime is an ancestor of H2 prime and H2 prime is reachable from `main`;
4. the old v0.3 record remains tracked and byte-identical;
5. authority and mirror trees are byte-identical;
6. the final PDF remains SHA-256
   `3ee4b7662f9d5f8fdd6a410461c7c8094cb5c2782fbbb486603f56b9841cb66d`;
7. the direct State-B publication auditor passes with historical science H1 as
   `--expected-stage1-commit`, while both v0.2 validators pass with the newer
   evaluator-code H1 prime as `--code-commit`.

No push is part of this disposable candidate.
