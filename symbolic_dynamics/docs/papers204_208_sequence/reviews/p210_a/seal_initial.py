"""Seal only this completed initial review; no root/author mutation."""
import hashlib,json,pathlib
D=pathlib.Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
seal=D/'SHA256SUMS'
assert not seal.exists(),'never overwrite initial or accepted seal'
required=['REPORT.md','SOURCE_AND_PROOF.md','REPLAY_LOG.md','BUILD_REPORT.md','verify.py','CANONICAL.json','PARAMETERS.json','INPUT_PINS.sha256','FINDINGS.json','DELTA.md','AUDIT_READ_ROLES.json','ARTIFACT_ROLES.md']
assert all((D/p).is_file() for p in required)
assert json.loads((D/'FINDINGS.json').read_text())['census']['total_open']==0
assert 'NOT_YET_ACCEPTED_DELTA' in (D/'DELTA.md').read_text()
files=sorted(p for p in D.rglob('*') if p.is_file() and p!=seal)
rows=[sha(p)+'  '+str(p.relative_to(D)) for p in files]
seal.write_text('\n'.join(rows)+'\n')
for row in rows:
 h,name=row.split('  ',1)
 assert sha(D/name)==h
assert set(files)=={p for p in D.rglob('*') if p.is_file() and p!=seal}
print(json.dumps({'status':'SEALED_INITIAL_REVIEW_PENDING_ROOT_RESPONSE','payloads':len(files),'physical_files':len(files)+1,
 'seal_sha256':sha(seal),'input_pins':494,'verifier_sha256':sha(D/'verify.py'),'parameters_sha256':sha(D/'PARAMETERS.json'),
 'canonical_sha256':sha(D/'CANONICAL.json'),'canonical_bytes':(D/'CANONICAL.json').stat().st_size,
 'selected_children':{name:{'payloads':len(json.loads((D/name/'PAYLOADS.json').read_text())),'payload_inventory_sha256':sha(D/name/'PAYLOADS.json'),
                          'report_sha256':sha(D/name/'REPORT.json')} for name in ['produce01','pair01','pair02','build01','build02']},
 'selected_native_parents':['execution/pair02','execution/build02','execution/compare_author02','execution/build_pdf_cmp02'],
 'delta_accepted':False,'finding_census':json.loads((D/'FINDINGS.json').read_text())['census']},sort_keys=True,indent=2))
