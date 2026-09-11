"""Bounded documentary child recorder; original infrastructure only."""
import importlib.util
import json
import os
from pathlib import Path
import shutil
import sys
import traceback

W=Path('/root/autodl-tmp/symbolic_dynamics')
B=W/'docs/papers204_208_sequence/reviews/p209_b'
ENV={'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}


def main():
    mode,label=sys.argv[1:]
    assert (mode,label) in [('intake','delta_intake_01'),('check','delta_check_01')]
    script='delta_intake.py' if mode=='intake' else 'check_delta.py'
    out=B/label;assert not out.exists()
    assert sys.flags.isolated and sys.flags.no_site and sys.flags.optimize==0 and sys.dont_write_bytecode
    assert dict(os.environ)==ENV and Path.cwd()==W
    assert sys.pycache_prefix==str(out/'never_created_parent_cache') and not Path(sys.pycache_prefix).exists()
    out.mkdir()
    spec=importlib.util.spec_from_file_location('unchanged_recording_only',B/'record_review.py')
    rec=importlib.util.module_from_spec(spec);spec.loader.exec_module(rec)
    files=[Path(p) for p in json.loads((B/'review_pair_01/ALL_INPUTS_INCLUDING_CAPSULES_BEFORE.json').read_bytes())]
    files += [B/'review_pair_01/ALL_INPUTS_INCLUDING_CAPSULES_BEFORE.json',B/'record_review.py',B/'launch_delta.py',B/script]
    for name in ['record_review.py','launch_delta.py',script]:
        shutil.copyfile(B/name,out/name);files.append(out/name)
    before=rec.pins(files);assert all('error' not in v for v in before.values())
    rec.save(out/'INPUTS_BEFORE.json',before);rec.save(out/'ATTEMPT.json',rec.observation('DELTA_DOCUMENTARY_ENTRY'))
    problem=None
    try:
        cache=out/'never_created_child_cache'
        rec.command(['/usr/bin/python3.10','-I','-S','-B','-X','pycache_prefix='+str(cache),str(B/script),str(out)],out,out,'documentary_child',ENV)
        assert not cache.exists()
    except BaseException:
        problem=traceback.format_exc()
    after=rec.pins(before);rec.save(out/'INPUTS_AFTER.json',after)
    rec.save(out/'ALL_COMMAND_RECORDS.json',rec.COMMAND_RECORDS)
    result={'status':'PASS' if problem is None and before==after else 'FAIL_PRESERVED','failure':problem,
            'inputs':len(before),'inputs_unchanged':before==after,'commands':len(rec.COMMAND_RECORDS),
            'scope':'Documentary assessment only; no mathematical producer/build/render/view; no continuous/startup/grandchild trace or OS-hermeticity.'}
    rec.save(out/'RECEIPT.json',result);seal=rec.manifest(out)
    print(json.dumps({**result,'seal':seal},sort_keys=True))
    return int(result['status']!='PASS')


if __name__=='__main__':raise SystemExit(main())
