"""Own bounded diagnostic recorder; uses only preserved runtime infrastructure.

The original mathematical pair is never rerun here. Parent/startup tracing
is not asserted. Every subprocess has no inherited environment and complete
actual streams, command record, sampled maps, input before/after and failures.
"""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import sys
import traceback

W=Path('/root/autodl-tmp/symbolic_dynamics')
B=W/'docs/papers204_208_sequence/reviews/p209_b'
F=W/'papers/209-ordered-fibre-threading/frozen_round1'
A=W/'docs/papers204_208_sequence/reviews/p209_a'
ENV={'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}

def main():
    assert sys.argv[1:] in (['reconcile','auxiliary_01'],['artifacts','artifact_audit_03'])
    mode,label=sys.argv[1:]
    out=B/label
    assert not out.exists()
    assert sys.flags.isolated and sys.flags.no_site and sys.flags.optimize==0 and sys.dont_write_bytecode
    assert dict(os.environ)==ENV and Path.cwd()==W
    assert sys.pycache_prefix==str(out/'never_created_parent_cache') and not Path(sys.pycache_prefix).exists()
    out.mkdir()
    spec=importlib.util.spec_from_file_location('runtime_infrastructure',B/'record_review.py')
    rec=importlib.util.module_from_spec(spec); spec.loader.exec_module(rec)
    files=[Path(p) for p in json.loads((B/'review_pair_01/ALL_INPUTS_INCLUDING_CAPSULES_BEFORE.json').read_bytes())]
    files += [B/'review_pair_01/ALL_INPUTS_INCLUDING_CAPSULES_BEFORE.json',B/'record_auxiliary_v3.py',B/'record_review.py',B/'reconcile.py',A/'CANONICAL.json',F/'CANONICAL.json',B/'CANONICAL.json',F/'main.pdf',B/'review_build_01/cold_build/main.pdf']
    if mode=='artifacts':
        files += [B/'audit_artifacts_v3.py']
    for name in ['record_auxiliary_v3.py','record_review.py', 'reconcile.py' if mode=='reconcile' else 'audit_artifacts_v3.py']:
        shutil.copyfile(B/name,out/name)
        files.append(out/name)
    before=rec.pins(files)
    assert all('error' not in v for v in before.values())
    rec.save(out/'INPUTS_BEFORE.json',before)
    rec.save(out/'ATTEMPT.json',rec.observation('AUXILIARY_ENTRY'))
    problem=None
    try:
        if mode=='reconcile':
            cache=out/'never_created_child_cache'
            argv=['/usr/bin/python3.10','-I','-S','-B','-X','pycache_prefix='+str(cache),str(B/'reconcile.py'),str(out)]
            rec.command(argv,out,out,'reconcile',ENV)
            for tag,left,right in [('author_projection_cmp','author_projection.json','B_to_author_projection.json'),('A_projection_cmp','A_projection.json','B_to_A_projection.json')]:
                rec.command(['/usr/bin/cmp','--',str(out/left),str(out/right)],out,out,tag,ENV)
        else:
            cache=out/'never_created_child_cache'
            argv=['/usr/bin/python3.10','-I','-S','-B','-X','pycache_prefix='+str(cache),str(B/'audit_artifacts_v3.py'),str(out)]
            rec.command(argv,out,out,'artifact_check',ENV)
        rec.command(['/usr/bin/cmp','--',str(F/'main.pdf'),str(B/'review_build_01/cold_build/main.pdf')],out,out,'pdf_cmp',ENV)
        assert not cache.exists()
    except BaseException:
        problem=traceback.format_exc()
    after=rec.pins(before)
    rec.save(out/'INPUTS_AFTER.json',after)
    rec.save(out/'ALL_COMMAND_RECORDS.json',rec.COMMAND_RECORDS)
    result={'status':'PASS' if problem is None and before==after else 'FAIL_PRESERVED','failure':problem,'inputs':len(before),'inputs_unchanged':before==after,'commands':len(rec.COMMAND_RECORDS),'parent_limit':'No startup/continuous/grandchild trace; isolated explicit non-inherited environment, sampled direct-child maps. Underlying pair runtime files checked before and after.'}
    rec.save(out/'RECEIPT.json',result)
    seal=rec.manifest(out)
    print(json.dumps({**result,'seal':seal},sort_keys=True))
    return int(result['status']!='PASS')

if __name__=='__main__': raise SystemExit(main())
