#!/usr/bin/env python3
"""Recover only two exact old documentary texts; stdout only, no file mutation."""
from hashlib import sha256
import json
from pathlib import Path
import sys

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
SCOUT=ROOT/'docs/papers204_208_sequence/scouting/finite_systems_thirty_fifth'
EXPECTED_INITIAL='01dded327a041789a4a0c81f9b69b2f7d8c6d26c22f9c30b57dcb375d7c0ac48'
EXPECTED_FINAL='81660274d7cc677c7fac2b917fe2f5b6d8c2d5c18ccd68ffde5b6f85306be81a'
EXPECTED_OLD={
 'REPORT.md':'a5e5ad74f7e135b7e8c9d3d281b67a04b7a2f1d6ce19f1afb4e17a09d780cb42',
 'SOURCE_AND_HISTORY.md':'a7f4a2a485687075b882f9f88e643ef50675ff326b192cf38b45f31bff44f409',
}
assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode and not sys.flags.optimize
assert Path.cwd()==ROOT

input_names=['MANIFEST.initial_before_audit_failure.sha256','MANIFEST.sha256','REPORT.md','SOURCE_AND_HISTORY.md']
inputs={}
for name in input_names:
    p=SCOUT/name
    assert p.is_file() and not p.is_symlink() and p.resolve()==p
    raw=p.read_bytes()
    assert raw.endswith(b'\n')
    inputs[name]={'original_path':str(p),'sha256':sha256(raw).hexdigest(),
                  'bytes':len(raw),'text':raw.decode()}
assert inputs[input_names[0]]['sha256']==EXPECTED_INITIAL
assert inputs[input_names[1]]['sha256']==EXPECTED_FINAL

def read_manifest(name):
    pairs=[line.split('  ',1) for line in inputs[name]['text'].splitlines()]
    assert len({n for h,n in pairs})==len(pairs)
    return {n:h for h,n in pairs}
initial=read_manifest(input_names[0])
final=read_manifest(input_names[1])
assert len(initial)==27 and len(final)==31
for name,digest in EXPECTED_OLD.items():
    assert initial[name]==digest and inputs[name]['sha256']==final[name]

# @ stands only for a Markdown backtick in these fixed documented literals.
new_phrase=('named [v2 script](search_originals_v2.py) changes only three literal\n'
            'tool-path occurrences on two lines to the actually resolved bundled @rg@ binary.\n').replace('@',chr(96))
old_phrase=('named [v2 script](search_originals_v2.py) changes only the two literal\n'
            'tool-path occurrences to the actually resolved bundled @rg@ binary.\n').replace('@',chr(96))
added_source=('\nThe first closure auditor incorrectly checked for two path occurrences,\n'
 'confusing two changed lines with three occurrences, and stopped. Its\n'
 'original source, initial manifest and both actual failure invocations are\n'
 'retained in @audit_closure.py@, @MANIFEST.initial_before_audit_failure.sha256@\n'
 'and @CLOSURE_AUDIT.failed.actual.json@. The separately named\n'
 '@audit_closure_v2.py@ corrects only that literal count from two to three.\n'
 'The final manifest covers all failed and corrected provenance. This was\n'
 'a documentary assertion error, not a numerical test or mathematical finding.\n').replace('@',chr(96))
added_report=('The initial auditor stopped on an incorrect count of changed path strings;\n'
 'its source, initial manifest and actual failures are retained. The separate\n'
 'v2 auditor corrects exactly that count and is used for the final check.\n')
source=inputs['SOURCE_AND_HISTORY.md']['text']
report=inputs['REPORT.md']['text']
assert source.count(new_phrase)==1 and source.count(added_source)==1
assert report.count(added_report)==1
reconstructed={
 'SOURCE_AND_HISTORY.md':source.replace(new_phrase,old_phrase).replace(added_source,''),
 'REPORT.md':report.replace(added_report,''),
}
outputs={}
for name,text in reconstructed.items():
    raw=text.encode()
    digest=sha256(raw).hexdigest()
    assert digest==EXPECTED_OLD[name],(name,digest)
    outputs[name]={'restored_historical_role':name,
                   'physical_reconstruction_path':'reconstructed_initial/'+name,
                   'sha256':digest,'bytes':len(raw),'text':text}
for name,row in inputs.items():
    assert sha256((SCOUT/name).read_bytes()).hexdigest()==row['sha256']
print(json.dumps({'schema':'scout35-two-initial-document-reconstruction-v1',
                  'status':'LATER_RECONSTRUCTION_FROM_ACTUAL_HISTORY_AND_MATCHING_OLD_PIN',
                  'method':'Reverse the exact two-document hunks of the actual documentary correction; require both complete historical manifest digests.',
                  'input_manifest_count':27,'sealed_final_payload_count':31,
                  'inputs_before_and_after_unchanged':True,'inputs':inputs,
                  'reconstructed_initial_documents':outputs,
                  'source_of_delta':'The actual original two-document apply_patch correction, preserved as ORIGINAL_DOCUMENT_EDIT.patch. Unrelated hunks from that edit operation are intentionally outside this two-document recovery.',
                  'boundary':'These two files did not exist as preserved physical pre-edit snapshots in the sealed31 package. They are later verified reconstructions. No sealed source, code, proof, manifest, central index or Git was modified; no old checker or science ran.'},
                 indent=2,sort_keys=True))
