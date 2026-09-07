#!/usr/bin/env python3
"""Extract fixed protected historical roles from sealed metadata, not current bodies."""
from collections import defaultdict
from hashlib import sha256
import json
from pathlib import Path
import sys
ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
S=ROOT/'docs/papers204_208_sequence/scouting/finite_systems_thirty_third'
assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode
lanes=('order_geometry_tenth','order_geometry_tenth_desk','finite_systems_twentieth')
roles=defaultdict(list)
digests=defaultdict(set)
physical=set()
refs=0
for group in ('commands','postcheck'):
    for d in sorted((S/group).iterdir()):
        for phase in ('inputs_before.json','inputs_after.json'):
            p=d/phase
            raw=p.read_bytes()
            data=json.loads(raw)
            for name, digest in data.items():
                absolute=str(ROOT/name)
                physical.add(absolute)
                if phase=='inputs_before.json':
                    refs+=1
                if any('/scouting/'+lane+'/' in name for lane in lanes):
                    digests[name].add(digest)
                    roles[name].append({'record_path':str(p.relative_to(S)),
                                        'record_sha256':sha256(raw).hexdigest(),
                                        'literal_key':name,'value':digest})
rows=[]
for name in sorted(roles):
    assert len(digests[name])==1
    rows.append({'historical_workspace_path':name,'sha256':next(iter(digests[name])),
                 'current_access':'SKIP_CURRENT_BODY_AND_HASH',
                 'reason':'Explicit conservative mixed/protected lane exclusion; root may separately verify these bytes.',
                 'archived_occurrences':roles[name]})
assert len(rows)==8
sets={n:json.loads((S/n).read_text()) for n in ('SELECTED_ORIGINALS.json','SELECTED_ORIGINALS_V2.json','SELECTED_ORIGINALS_FINAL.json','SELECTED_ORIGINALS_SCOPED.json')}
pairs=list(zip(list(sets)[:-1],list(sets)[1:]))
print(json.dumps({'schema':'scout33-protected-historical-role-contract-v1',
                  'status':'EXACT_ARCHIVED_ROLES_ONLY_NO_CURRENT_PROTECTED_READ',
                  'source_scout_seal':'e839102239f6d3936514c62419b447c7bfa48ec7cbbe5e854590a88de73c573e',
                  'protected_roles':rows,
                  'protected_distinct_paths':len(rows),
                  'protected_record_occurrences':sum(len(r['archived_occurrences']) for r in rows),
                  'historical_input_references_before':refs,
                  'historical_normalized_physical_names':len(physical),
                  'historical_normalized_permitted_names':len(physical)-8,
                  'selection_differences':[{'earlier':a,'later':b,'removed':sorted(set(sets[a])-set(sets[b])),'added':sorted(set(sets[b])-set(sets[a]))} for a,b in pairs],
                  'boundary':'All opened files are scout-owned archived JSON metadata. No path in protected_roles was opened or hashed.'},indent=2,sort_keys=True))
