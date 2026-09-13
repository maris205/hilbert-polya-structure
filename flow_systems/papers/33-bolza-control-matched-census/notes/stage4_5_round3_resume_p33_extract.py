"""Read-only audit preparation; never runs an official validator or writes artifacts."""
import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
notes_dir = Path(__file__).parent
draft_path = notes_dir / 'stage4_prime_revision_round3.tex'
raw = draft_path.read_bytes()
draft = raw.decode('utf-8')
blocks = []
for match in re.finditer(r'<!--block:(B\d+)-->\n(.*?)(?=<!--block:|\Z)', draft, re.S):
    body = match.group(2)
    left = len(body) - len(body.lstrip())
    right = len(body.rstrip())
    a, b = match.start(2) + left, match.start(2) + right
    blocks.append({'block_id': match.group(1), 'text': draft[a:b],
                   'start_char': a, 'end_char': b,
                   'draft_span': {'start_byte': len(draft[:a].encode()), 'end_byte': len(draft[:b].encode())}})

excluded = set('B0001 B0002 B0003 B0004 B0005 B0006 B0008 B0009 B0011 B0012 B0013 B0016 B0021 B0023 B0024 B0028 B0031 B0035 B0038 B0039 B0042 B0046 B0048 B0049 B0054 B0056 B0060 B0063 B0065 B0068 B0075 B0076 B0078 B0080 B0083 B0085 B0086 B0089 B0092 B0094 B0096 B0097 B0099 B0101 B0104 B0111 B0114 B0118 B0125 B0126'.split())
paragraphs = [b for b in blocks if b['block_id'] not in excluded]
old = json.loads((notes_dir / 'stage4_5_round3_p33_semantic_working_audit.json').read_text())
queries = old['completed_work']['D1']['submitted_queries']
queried = {q['id'] for q in queries}
patch_names = ['stage4_revision_patch_round1.json', 'stage4_prime_revision_patch_round6_exact_confirmation.json', 'stage4_5_round2_correction_patch.json']
base_names = ['stage3_revision_base.tex', 'stage4_revision_round1.tex', 'stage4_prime_revision_round2.tex']
operations = []
changed = set()
for round_no, (patch_name, base_name) in enumerate(zip(patch_names, base_names), 1):
    patch = json.loads((notes_dir / patch_name).read_text())
    old_blocks = dict(re.findall(r'<!--block:(B\d+)-->\n(.*?)(?=<!--block:|\Z)', (notes_dir / base_name).read_text(), re.S))
    for ordinal, op in enumerate(patch['ops'], 1):
        target = op.get('block_id')
        new_text = op['new_text']
        if op['op'] == 'insert_after':
            target = op.get('new_block_id') or ('B0127' if round_no == 1 and ordinal == 1 else 'B0128')
        changed.add(target)
        operations.append({'revision_round': round_no, 'op_ordinal': ordinal, 'op': op['op'], 'target_block_id': target,
                           'patch_path': str(notes_dir / patch_name), 'base_path': str(notes_dir / base_name),
                           'operation_record': op, 'old_text': old_blocks.get(op.get('block_id'), '') if op['op'] == 'replace_block' else None,
                           'new_text': new_text})

coverage_path = Path('/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.28/skills/academic-research-suite/ars/scripts/claim_registry_coverage.py')
spec = importlib.util.spec_from_file_location('p33_readonly_coverage_lexical', coverage_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
sentences = []
for sentence in module._sentences(draft):
    containing = next((b for b in blocks if b['start_char'] <= sentence['start_char'] < b['end_char']), None)
    kinds = module._candidate_kinds(sentence['text'])
    if not containing or (containing['block_id'] in excluded and not kinds):
        continue
    text = sentence['text']
    if not kinds and (text.startswith(('%', '\\cite', '<!--')) or text in ('\\[', '\\]', '\\end{itemize}', '\\end{enumerate}')):
        continue
    sentences.append({'block_id': containing['block_id'], 'line': sentence['line'], 'claim_text': text,
                      'draft_span': {'start_byte': len(draft[:sentence['start_char']].encode()), 'end_byte': len(draft[:sentence['end_char']].encode())},
                      'lexical_kinds': kinds, 'lexical_triggers': module._candidate_triggers(text)})

semantic_sentences = []
for block in paragraphs:
    text = block['text']
    if block['block_id'] == 'B0010':
        segments = [(0, len(text))]
    else:
        masked = re.sub(r'%[^\n]*|\\citep\{[^}]*\}', lambda m: ' ' * len(m.group()), text)
        splits = list(re.finditer(r'(?<=[.!?。！？])\s+', masked))
        starts = [0] + [m.end() for m in splits]
        ends = [m.start() for m in splits] + [len(text)]
        segments = list(zip(starts, ends))
    for a, b in segments:
        segment = text[a:b]
        left = len(segment) - len(segment.lstrip())
        right = len(segment.rstrip())
        if right <= left:
            continue
        a, b = a + left, a + right
        absolute_a, absolute_b = block['start_char'] + a, block['start_char'] + b
        semantic_sentences.append({'block_id': block['block_id'], 'claim_text': text[a:b],
                                   'draft_span': {'start_byte': len(draft[:absolute_a].encode()), 'end_byte': len(draft[:absolute_b].encode())}})

result = {'draft_path': str(draft_path), 'draft_sha256': hashlib.sha256(raw).hexdigest(),
          'blocks': blocks, 'paragraphs': paragraphs, 'excluded_structural_blocks': sorted(excluded),
          'queries': queries, 'D_counts': {'paragraph_denominator': len(paragraphs),
          'sampled_paragraphs': len([b for b in paragraphs if b['block_id'] in queried]),
          'changed_block_count': len(changed), 'missing_changed': sorted(changed - queried)},
          'changed_blocks': sorted(changed), 'operations': operations, 'sentences': sentences,
          'semantic_sentences': semantic_sentences}
print(json.dumps(result, ensure_ascii=False))
