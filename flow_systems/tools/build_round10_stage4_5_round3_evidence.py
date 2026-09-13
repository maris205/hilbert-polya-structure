"""Append-only audit support: official EVR API execution; JSON stdout only.

Reads a named audit input and exact explicit source pointers, never ambient source
discovery. Does not modify manuscripts, evidence, or official library code.
Any first exception is reported with already-built rows and a nonzero exit;
the caller must retain it and obey the active stop condition, never repair/retry.
"""
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARS = Path('/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.28/skills/academic-research-suite/ars')

def pointer(value, ptr):
    for part in ptr.split('/')[1:]:
        part = part.replace('~1', '/').replace('~0', '~')
        value = value[int(part)] if isinstance(value, list) else value[part]
    return value

def main():
    rows, source_map, source_bindings = [], {}, []
    step = 'read_input'
    try:
        input_path = Path(sys.argv[1])
        input_raw = input_path.read_bytes()
        payload = json.loads(input_raw)
        spec = importlib.util.spec_from_file_location('round3_official_evidence_rows', ARS/'scripts/evidence_rows.py')
        evr = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(evr)
        first = int(sys.argv[2]) if len(sys.argv) > 2 else 0
        count = int(sys.argv[3]) if len(sys.argv) > 3 else len(payload['inputs'])
        selected_inputs = payload['inputs'][first:first+count]
        for index, selected in enumerate(selected_inputs, first):
            step = f'source_read:{index}'
            source_text, extracted = None, None
            template = selected['row']
            source_ref = selected['source_ref']
            if source_ref is not None:
                source_path = ROOT / source_ref['path']
                raw = source_path.read_bytes()
                source_text = pointer(json.loads(raw), source_ref['json_pointer'])
                if not isinstance(source_text, str) or source_text != source_ref['expected_text']:
                    raise ValueError('NEW_SOURCE_TARGET_TEXT_MISMATCH: '+str(source_path)+source_ref['json_pointer'])
                slug = template['source']['ref_slug']
                if slug in source_map and source_map[slug] != source_text:
                    raise ValueError('NEW_SOURCE_MAP_CONTENT_CONFLICT: '+slug)
                source_map[slug] = source_text
                template['source']['source_artifact_sha256'] = hashlib.sha256(raw).hexdigest()
                extracted = source_text
                binding = {'ref_slug':slug, 'path':source_ref['path'], 'json_pointer':source_ref['json_pointer'], 'artifact_sha256':hashlib.sha256(raw).hexdigest(), 'excerpt_sha256':hashlib.sha256(source_text.encode()).hexdigest()}
                if binding not in source_bindings:
                    source_bindings.append(binding)
            step = f'official_build:{index}'
            built = evr.build(template, source_text, extracted_text=extracted)
            step = f'official_validate:{index}'
            rows.append(evr.validate(built, source_text))
        step = 'tuple_and_claim_accounting'
        if len(rows) != len(selected_inputs):
            raise ValueError('SELECTED_TUPLE_COUNT_MISMATCH')
        print(json.dumps({'status':'COMPLETED', 'first_tuple_index':first, 'selected_tuple_count':len(selected_inputs), 'total_selected_tuples':len(payload['inputs']), 'input_sha256':hashlib.sha256(input_raw).hexdigest(), 'rows':rows, 'source_map':source_map, 'source_bindings':source_bindings},ensure_ascii=False))
        return 0
    except Exception as exc:
        print(json.dumps({'status':'STOP_FIRST_FAILURE', 'step':step, 'exception_type':type(exc).__name__, 'error':str(exc), 'already_built_rows':rows, 'source_map':source_map, 'source_bindings':source_bindings},ensure_ascii=False))
        return 1

if __name__ == '__main__':
    raise SystemExit(main())
