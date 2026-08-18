# Paper 44 authenticated State-B bridge commands

`SEAL_SHA256` and `STAGE1_H1` are out-of-band values.  The seal must be
lowercase hex64.  For this frozen Paper 44 publication, `STAGE1_H1` is the
historical science H1
`b0e41ac3d6bd30618421d1b76122c3e9e04d070b`, whose three values are recorded
in the State-B route under `outputs/evaluations/`.  It is not the later
Route-v0.2 evaluator-code H1 prime used by the new validators.
Never execute a controller directly from the mutable overlay before completing
the bootstrap below.  Before section 2, the operator must also hold exclusive
ownership or an external exclusive lease on `TARGET` for the entire command;
the built-in prewrite comparison is not a cross-process lock.

## 1. Generic-code bootstrap into a read-only controller

This step uses only the shell, GNU `sha256sum`, and an inline standard-library
JSON reader.  It verifies the raw seal hash, obtains the manifest hash from
that already authenticated seal, verifies the full writer manifest, then
copies and re-verifies the four operational programs in a private directory.

```bash
set -euo pipefail
umask 077
SOURCE=/tmp/paper44_stateb_publication_repair
TARGET=/tmp/disposable-paper44-full-root
FIXTURE=/tmp/current-stage1-paper44-fixture
SEAL_SHA256=<externally-approved-lowercase-seal-sha256>
STAGE1_H1=b0e41ac3d6bd30618421d1b76122c3e9e04d070b

[[ "$SEAL_SHA256" =~ ^[0-9a-f]{64}$ ]]
[[ "$STAGE1_H1" =~ ^[0-9a-f]{40}$ && "$STAGE1_H1" != 0000000000000000000000000000000000000000 ]]
CONTROLLER=$(mktemp -d /tmp/paper44-stateb-controller.XXXXXX)
chmod 700 "$CONTROLLER"
install -m 0444 "$SOURCE/evidence/publication_gate/PUBLICATION_OVERLAY_SEAL.json" "$CONTROLLER/PUBLICATION_OVERLAY_SEAL.json"
test "$(sha256sum -- "$CONTROLLER/PUBLICATION_OVERLAY_SEAL.json" | awk '{print $1}')" = "$SEAL_SHA256"
MANIFEST_SHA256=$(python -I -B - "$CONTROLLER/PUBLICATION_OVERLAY_SEAL.json" <<'PY'
import json, re, sys
with open(sys.argv[1], "rb") as handle:
    raw = handle.read()
value = json.loads(raw.decode("ascii"))
observed = value.get("writer_manifest_sha256")
if type(observed) is not str or re.fullmatch(r"[0-9a-f]{64}", observed) is None:
    raise SystemExit(2)
print(observed)
PY
)

install -m 0444 "$SOURCE/WRITER_MANIFEST.sha256" "$CONTROLLER/WRITER_MANIFEST.sha256"
test "$(sha256sum -- "$CONTROLLER/WRITER_MANIFEST.sha256" | awk '{print $1}')" = "$MANIFEST_SHA256"
(cd "$SOURCE" && sha256sum --strict -c "$CONTROLLER/WRITER_MANIFEST.sha256")

for NAME in publication_auditor.py publication_transaction.py stateb_bridge.py run_publication_smoke.py; do
  REL="evidence/publication_gate/$NAME"
  install -m 0444 "$SOURCE/$REL" "$CONTROLLER/$NAME"
  EXPECTED=$(awk -v path="$REL" '$2 == path {print $1}' "$CONTROLLER/WRITER_MANIFEST.sha256")
  test -n "$EXPECTED"
  test "$(sha256sum -- "$CONTROLLER/$NAME" | awk '{print $1}')" = "$EXPECTED"
done
chmod 0555 "$CONTROLLER"
```

The controller copies, not the source-overlay copies, are the executable trust
root for all remaining commands.  Each transaction still re-audits the source
against the external seal, closing the post-bootstrap source-race boundary.

## 2. Disposable audit, upgrade, and State-B transition

```bash
python -I -B "$CONTROLLER/publication_auditor.py" \
  --root "$SOURCE" --overlay-source "$SOURCE" --source-only \
  --expected-publication-seal-sha256 "$SEAL_SHA256" \
  --expected-stage1-commit "$STAGE1_H1"

python -I -B "$CONTROLLER/publication_transaction.py" \
  --source "$SOURCE" --target "$TARGET" \
  --expected-publication-seal-sha256 "$SEAL_SHA256" \
  --expected-stage1-commit "$STAGE1_H1" --relocated-disposable

python -I -B "$CONTROLLER/stateb_bridge.py" \
  --source "$SOURCE" --target "$TARGET" \
  --expected-publication-seal-sha256 "$SEAL_SHA256" \
  --expected-stage1-commit "$STAGE1_H1" --relocated-disposable

python -I -B "$CONTROLLER/publication_auditor.py" \
  --root "$TARGET" --overlay-source "$SOURCE" \
  --expected-publication-seal-sha256 "$SEAL_SHA256" \
  --expected-stage1-commit "$STAGE1_H1" --relocated-disposable
```

For the cold suite, point `FIXTURE` at a disposable copy of the current
Stage1-local predecessor root:

```bash
python -I -B "$CONTROLLER/run_publication_smoke.py" \
  --source "$SOURCE" --authority-fixture "$FIXTURE" \
  --expected-publication-seal-sha256 "$SEAL_SHA256" \
  --expected-stage1-commit "$STAGE1_H1"
```

Failure injection is permitted only with `--relocated-disposable` below
`/tmp`.  A later authorized non-disposable publication omits that switch and
uses the same authenticated controller; these commands do not authorize or
perform such a write.
