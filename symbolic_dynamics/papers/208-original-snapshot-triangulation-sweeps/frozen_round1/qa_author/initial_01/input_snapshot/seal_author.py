#!/usr/bin/env python3
"""One-time explicit author-owned manifest; later root work is not absorbed.

Run only after AUTHOR_HANDOFF.md and actual pair/build receipts exist.
The emitted list fixes ownership at this author handoff; never rerun in place.
"""
import hashlib
import json
from pathlib import Path
import sys

BASE = Path(__file__).resolve().parent


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    assert sys.flags.optimize == 0 and sys.flags.isolated == 1 and sys.dont_write_bytecode
    destination = BASE / 'AUTHOR_MANIFEST.sha256'
    if destination.exists():
        raise SystemExit('author manifest already sealed; do not overwrite')
    pair = json.loads((BASE / 'qa_author/pair_01/RECEIPT.json').read_bytes())
    build_pair = json.loads((BASE / 'qa_build/stable_pair/RECEIPT.json').read_bytes())
    assert pair['status'] == 'AUTHOR_EXECUTION_PASS'
    assert pair['expected_producer_count'] == pair['actual_producer_count'] == 2
    assert build_pair['status'] == 'RAW_PDF_PAIR_PASS'
    assert (BASE / 'AUTHOR_HANDOFF.md').is_file()
    assert sha(BASE / 'main.pdf') == build_pair['pdf_sha256'][0]
    # Snapshot every current author-owned file as an explicit nonself set.
    paths = sorted(p for p in BASE.rglob('*') if p.is_file())
    assert all(not any(part.startswith('frozen_round') for part in p.relative_to(BASE).parts)
               for p in paths)
    before = {str(p.relative_to(BASE)): sha(p) for p in paths}
    with destination.open('x', encoding='utf-8') as f:
        for rel, digest in before.items():
            f.write(digest + '  ' + rel + '\n')
    for rel, digest in before.items():
        assert sha(BASE / rel) == digest
    print(json.dumps({'role': 'fixed_author_owned_handoff_set',
                      'files': len(before), 'manifest_sha256': sha(destination),
                      'status': 'AUTHOR_MANIFEST_PASS'}, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
