# Reproduce and verify the import

The import is reproducible from the pinned source commit; no generated
artefact needs to be substituted or rebuilt for the file comparison below.

## Obtain the pinned source

```bash
git clone git@github.com:maris205/prime_dynamics_theory.git /tmp/prime_dynamics_theory_rh_source
git -C /tmp/prime_dynamics_theory_rh_source checkout --detach 02d51d372e9c95ffc2ed36727829363a32cec030
```

Set the paths for a read-only comparison:

```bash
source_repo=/tmp/prime_dynamics_theory_rh_source
zeta_root=/root/autodl-tmp/hilbert-polya-structure/zeta_mvp0
```

## Verify the RH paper tree

The following `rsync` is a checksum-based dry run.  It should print no file
changes when the source checkout and import are identical.

```bash
git -C "$source_repo" ls-files -z -- 'papers/RH-*' \
  | rsync -nrc --from0 --files-from=- "$source_repo/" "$zeta_root/"
```

Verify the root-document selections without changing either tree:

```bash
cmp -s "$source_repo/RH_HANDOFF.md" "$zeta_root/PRIME_DYNAMICS_RH_HANDOFF.md"
sed -n '1,9p' "$source_repo/README.md" \
  | cmp -s - "$zeta_root/PRIME_DYNAMICS_RH_README_SECTION.md"
sed -n '55,174p' "$source_repo/AGENTS.md" \
  | cmp -s - "$zeta_root/PRIME_DYNAMICS_RH_WORKFLOW.md"
```

Each command exits with status `0` on a byte-identical comparison.  Historical
absolute paths inside source records are intentionally retained; they are not
rewritten by this import.
