"""One-time scoped infrastructure adaptation, run after math commitment."""
from pathlib import Path
import difflib
import hashlib
import json
import shutil

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[3]
FREEZE = ROOT / 'papers/209-ordered-fibre-threading/frozen_round0'
assert hashlib.sha256((BASE / 'verify.py').read_bytes()).hexdigest() == '28fad641f3928907c9dca259b3360000f0c9063edee7005148ed9a5fc10779af'
assert hashlib.sha256((FREEZE / 'SHA256SUMS').read_bytes()).hexdigest() == '0f77871539b374027ab42910471cc74cefcd570e214a8242ac0a30c7a83e70ba'
snap = BASE / 'infrastructure_originals'
snap.mkdir()
pins = []
for name in ('record_author.py', 'launch_author.py', 'bootstrap.py'):
    shutil.copyfile(FREEZE / name, snap / name)
    pins.append(hashlib.sha256((FREEZE / name).read_bytes()).hexdigest() + '  ' + (FREEZE / name).relative_to(ROOT).as_posix())
(BASE / 'INFRASTRUCTURE_INPUT_PINS.sha256').write_text('\n'.join(pins) + '\n')
original = (snap / 'record_author.py').read_text()
adapted = original.replace('ROOT = PAPER.parents[1]', 'ROOT = PAPER.parents[3]\nFREEZE = ROOT / "papers/209-ordered-fibre-threading/frozen_round0"')
start, end = adapted.index('def science():'), adapted.index('\ndef runtime(mode):')
adapted = adapted[:start] + '''def science():
    check_manifest(FREEZE)
    require(info(FREEZE / "SHA256SUMS")["sha256"] == "0f77871539b374027ab42910471cc74cefcd570e214a8242ac0a30c7a83e70ba", "EXACT_ROUND0_SEAL")
    files = [p for p in FREEZE.rglob("*") if p.is_file()]
    files += [PAPER / n for n in ("verify.py", "bootstrap.py", "record_review.py", "launch_review.py", "PARAMETERS.json", "INDEPENDENCE_COMMITMENT.md", "COMMITMENT_PINS.sha256", "prepare_infrastructure.py", "INFRASTRUCTURE_INPUT_PINS.sha256", "ADAPTATION.diff", "INPUT_PINS.sha256")]
    files += [p for p in (PAPER / "infrastructure_originals").rglob("*") if p.is_file()]
    if (PAPER / "CANONICAL.json").is_file():
        files.append(PAPER / "CANONICAL.json")
    value = pins(files)
    REGISTERED_INPUTS.update(value)
    require(all("error" not in p for p in value.values()), "MISSING_SCIENTIFIC_INPUT")
    config = json.loads((PAPER / "PARAMETERS.json").read_bytes())
    require(config["n_values"] == list(range(6)) and config["total_states"] == 3414, "ORIGINAL_CUTOFF_CHANGED")
    return value

''' + adapted[end:]
start, end = adapted.index('        require(payload["status"]'), adapted.index('\n    except BaseException:', adapted.index('        require(payload["status"]'))
adapted = adapted[:start] + '''        require(payload["schema"] == "p209-review-a-independent-v1"
                and sum(b["state_count"] for b in payload["boxes"]) == 3414
                and [b["n"] for b in payload["boxes"]] == list(range(6))
                and all(len(b["records"]) == b["state_count"] for b in payload["boxes"]), "PRODUCER_PAYLOAD_SCOPE")
        details = {"checks": payload["checks"], "total_states": 3414,
                   "boxes": [{k: b[k] for k in ("n", "state_count", "partition_count", "maximum_fibre", "extremizer_ranks")}
                             for b in payload["boxes"]]}
''' + adapted[end:]
start, end = adapted.index('def build('), adapted.index('\ndef main():', adapted.index('def build('))
adapted = adapted[:start] + adapted[start:end].replace('PAPER / name', 'FREEZE / name').replace('PAPER / n', 'FREEZE / n').replace('PAPER / local', 'FREEZE / local') + adapted[end:]
adapted = adapted.replace('record_author.py', 'record_review.py').replace('author_(?:pair|build)', 'review_(?:pair|build)').replace('PASS_AUTHOR_', 'PASS_REVIEW_A_').replace('P209 author evidence only. No manuscript review, freeze or terminal acceptance.', 'P209 A actual verifier/build execution evidence; no review verdict, delta or terminal acceptance.')
(BASE / 'record_review.py').write_text(adapted)
diffs = [''.join(difflib.unified_diff(original.splitlines(True), adapted.splitlines(True), fromfile='frozen_round0/record_author.py', tofile='reviews/p209_a/record_review.py'))]
original = (snap / 'launch_author.py').read_text()
adapted = original.replace('ROOT = PAPER.parents[1]', 'ROOT = PAPER.parents[3]').replace('launch_author.py', 'launch_review.py').replace('record_author.py', 'record_review.py').replace('PASS_AUTHOR_', 'PASS_REVIEW_A_').replace('author_pair_N|author_build_N', 'review_pair_N|review_build_N').replace('prefix = "author_"', 'prefix = "review_"')
(BASE / 'launch_review.py').write_text(adapted)
diffs.append(''.join(difflib.unified_diff(original.splitlines(True), adapted.splitlines(True), fromfile='frozen_round0/launch_author.py', tofile='reviews/p209_a/launch_review.py')))
shutil.copyfile(snap / 'bootstrap.py', BASE / 'bootstrap.py')
(BASE / 'ADAPTATION.diff').write_text('\n'.join(diffs))
(BASE / 'PARAMETERS.json').write_text(json.dumps({'n_values': list(range(6)), 'total_states': 3414, 'mathematical_code_imports': []}, indent=2) + '\n')
files = sorted(p for p in FREEZE.rglob('*') if p.is_file())
assert len(files) == 1990
(BASE / 'INPUT_PINS.sha256').write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest() + '  ' + p.relative_to(ROOT).as_posix() + '\n' for p in files))
print(json.dumps({'status': 'PREPARED_NOT_EXECUTED', 'freeze_inputs': len(files), 'source_pins': pins, 'reviewer_math_sha256': hashlib.sha256((BASE / 'verify.py').read_bytes()).hexdigest()}, sort_keys=True))
