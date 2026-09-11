#!/usr/bin/env python3
"""Check two reconstructed documents and the exact forward delta, never old code."""
from hashlib import sha256
import json
from pathlib import Path
import sys

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
BASE=ROOT/'docs/papers204_208_sequence/qa/scout35_initial_document_recovery'
SCOUT=ROOT/'docs/papers204_208_sequence/scouting/finite_systems_thirty_fifth'
assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode and not sys.flags.optimize
assert Path.cwd()==ROOT
receipt=json.loads((BASE/'RECONSTRUCTION.actual.json').read_text())
assert receipt['status']=='LATER_RECONSTRUCTION_FROM_ACTUAL_HISTORY_AND_MATCHING_OLD_PIN'
inputs=receipt['inputs']
before={}
for name,row in inputs.items():
    current=(SCOUT/name).read_bytes()
    capture=(BASE/'inputs'/name).read_bytes()
    assert current==capture==row['text'].encode()
    assert sha256(current).hexdigest()==row['sha256']
    before[name]=current

documents={}
for name,row in receipt['reconstructed_initial_documents'].items():
    raw=(BASE/row['physical_reconstruction_path']).read_bytes()
    assert raw==row['text'].encode()
    assert len(raw)==row['bytes'] and sha256(raw).hexdigest()==row['sha256']
    documents[name]=raw.decode()

lines=(BASE/'ORIGINAL_DOCUMENT_EDIT.patch').read_text().splitlines(keepends=True)
assert lines[0]=='*** Begin Patch\n' and lines[-1]=='*** End Patch\n'
target=None
hunks=[]
old=[]
new=[]
def finish_hunk():
    if old or new:
        assert target is not None
        hunks.append((target,''.join(old),''.join(new)))
        old.clear()
        new.clear()
for line in lines[1:-1]:
    if line.startswith('*** Update File: '):
        finish_hunk()
        path=line[len('*** Update File: '):].rstrip('\n')
        assert path.startswith('docs/papers204_208_sequence/scouting/finite_systems_thirty_fifth/')
        target=path.rsplit('/',1)[1]
        assert target in documents
    elif line=='@@\n':
        finish_hunk()
    elif line.startswith(' '):
        old.append(line[1:]); new.append(line[1:])
    elif line.startswith('-'):
        old.append(line[1:])
    elif line.startswith('+'):
        new.append(line[1:])
    else:
        raise AssertionError('unexpected patch syntax')
finish_hunk()
assert len(hunks)==3
for name,old_text,new_text in hunks:
    assert old_text and documents[name].count(old_text)==1
    documents[name]=documents[name].replace(old_text,new_text)
for name,text in documents.items():
    assert text.encode()==before[name]
for name,raw in before.items():
    assert (SCOUT/name).read_bytes()==raw
print(json.dumps({'schema':'scout35-physical-reconstruction-check-v1',
                  'status':receipt['status'],'physical_reconstructed_files':2,
                  'captured_current_inputs_byte_equal':4,'historical_forward_hunks_applied_in_memory':3,
                  'complete_forward_delta_reaches_both_exact_current_documents':True,
                  'source_inputs_unchanged':True,
                  'recovered_pins':{n:{k:r[k] for k in ('sha256','bytes','physical_reconstruction_path')}
                                    for n,r in receipt['reconstructed_initial_documents'].items()},
                  'boundary':'Documentary check only. Historical patch applied only to in-memory reconstructed strings. No old checker, producer, protected source, central file or Git operation.'},
                 indent=2,sort_keys=True))
