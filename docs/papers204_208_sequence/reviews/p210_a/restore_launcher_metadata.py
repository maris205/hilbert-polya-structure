"""One-time metadata reconstruction after disclosed sanitizer failure; no secrets."""
import hashlib,json,pathlib
D=pathlib.Path(__file__).resolve().parent
R=D.parents[3]
rel=str(D.relative_to(R))
base='/usr/bin/python3.10 -I -S -B -X'.split()
entries={
 'pair01':base+['pycache_prefix='+str(D/'absent_driver_pair01'),rel+'/instrumentation/evidence.py','pair','--paper',rel,'--out',rel+'/pair01'],
 'build01':base+['pycache_prefix='+str(D/'absent_driver_build01'),rel+'/instrumentation/evidence.py','build','--paper','papers/210-weakly-increasing-run-aggregation/frozen_round0','--out',rel+'/build01'],
 'compare_author01':base+['pycache_prefix='+str(D/'absent_compare01'),rel+'/compare_author.py'],
 'build_pdf_cmp':['/usr/bin/cmp',rel+'/build01/source/main.pdf','papers/210-weakly-increasing-run-aggregation/frozen_round0/main.pdf']}
rows=[]
for name,argv in entries.items():
 p=D/'execution'/name/'ATTEMPT.json'
 assert p.read_bytes()==b''
 v={'role':'RECONSTRUCTED_KNOWN_LAUNCH_METADATA_AFTER_SANITIZER_FAILURE_NOT_ORIGINAL_RECEIPT',
    'argv':argv,'cwd':str(R),'native_returncode_evidence':'RESULT.json',
    'reconstruction_basis':'actual native tool invocation; command and cwd known, original sensitive environment intentionally not recovered',
    'original_start_ns':1788787619979700744 if name=='pair01' else None,
    'start_time_scope':'pair01 recovered from actual sanitized tool stdout; other three unavailable, not inferred',
    'environment_scope':'original inherited platform fields removed; exact clean scientific/build child environment remains in capsule CONTEXT/commands records',
    'redacted_sensitive_key_names':['AutodlAutoPanelToken','AutoDLServiceURL','AutoDLService6006URL','AutoDLService6008URL','http_proxy','https_proxy'],
    'all_unneeded_launcher_fields_omitted':True,
    'sanitizer_failure':'Perl -i without correct input loop emptied all four ATTEMPT files; subsequent read failed native255; no child evidence or result changed'}
 p.write_text(json.dumps(v,sort_keys=True,indent=2)+'\n')
 rows.append({'path':str(p.relative_to(D)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
print(json.dumps({'status':'RECONSTRUCTED_LIMITED_NOT_ORIGINAL','records':rows},sort_keys=True,indent=2))
