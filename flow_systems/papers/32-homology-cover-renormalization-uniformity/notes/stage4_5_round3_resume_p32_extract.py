"""Read-only paragraph/query preparation, not an integrity validator."""
import hashlib
import json
import re
from pathlib import Path

draft = Path(__file__).with_name("stage4_prime_revision_round4.tex")
raw = draft.read_bytes()
text = raw.decode("utf-8")
excluded = set("B0001 B0002 B0003 B0004 B0005 B0008 B0009 B0010 B0012 B0015 B0022 B0023 B0027 B0031 B0035 B0038 B0042 B0043 B0048 B0051 B0052 B0054 B0056 B0059 B0063 B0065 B0070 B0075 B0080 B0085 B0087 B0088 B0089 B0093 B0097 B0103 B0108 B0113 B0114 B0117 B0120 B0126 B0129 B0130".split())
paragraphs = []
for match in re.finditer(r"<!--block:(B\d+)-->\n(.*?)(?=<!--block:|\Z)", text, re.S):
    block_id, body = match.group(1, 2)
    if block_id in excluded:
        continue
    runs = re.findall(r"[A-Za-z][A-Za-z0-9,;:'\"() —–\-\n]*", body)
    runs = [run for run in runs if len(run.split()) >= 8]
    fragment = " ".join(max(runs, key=lambda x: len(x.split())).split()[:10]) if runs else ""
    if block_id == "B0007":
        fragment = "只有在未來自足推導局部因子後"
    paragraphs.append({"block_id": block_id, "draft_start_byte": len(text[:match.start(2)].encode()), "draft_end_byte": len(text[:match.end(2)].encode()), "query_fragment": fragment, "query": '"' + fragment + '"'})
print(json.dumps({"draft_path": str(draft), "draft_raw_sha256": hashlib.sha256(raw).hexdigest(), "excluded_structural_blocks": sorted(excluded), "paragraphs": paragraphs}, ensure_ascii=False))
