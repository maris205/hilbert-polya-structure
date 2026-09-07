"""Preserve a completed documentary wrapper failure without rewriting it."""
import importlib.util
import json
from pathlib import Path

B=Path('/root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/reviews/p209_b')
out=B/'delta_check_01'
spec=importlib.util.spec_from_file_location('recording_only',B/'record_review.py')
rec=importlib.util.module_from_spec(spec);spec.loader.exec_module(rec)
assert not (out/'SHA256SUMS').exists()
child=json.loads((out/'documentary_child.command.json').read_bytes())
assert child['exit']==0 and child['process_outcome']=='COMPLETED'
failure=json.loads((out/'OUTER_FAILURE.actual.json').read_bytes())
assert failure['actual_exit_code']==1
before=json.loads((out/'INPUTS_BEFORE.json').read_bytes())
assert before==json.loads((out/'INPUTS_AFTER.json').read_bytes())==rec.pins(before)
rows=json.loads((out/'ALL_COMMAND_RECORDS.json').read_bytes())
assert len(rows)==8 and all(e['command']['exit']==0 for e in rows)
for row in [child]+[e['command'] for e in rows]:
    for name in ('stdout','stderr'):
        assert rec.byteinfo(out/row[name])==row[name+'_info']
rec.save(out/'CLOSURE_AFTER_FAILURE.json',{'status':'FAIL_PRESERVED_OUTER_WRAPPER_FILENAME_COLLISION',
    'actual_outer_exit':1,'actual_child_exit':0,'actual_comparison_exits':[0]*8,
    'wrapper_inputs_unchanged':len(before),'original_streams_and_records_unchanged':True,
    'source':rec.info(B/'seal_failed_delta_attempt.py'),
    'scope':'Later documentary preservation only, not successful original outer closure, delta acceptance, science/build/view or process-tree tracing.'})
print(json.dumps({'status':'FAIL_PRESERVED_OUTER_WRAPPER_FILENAME_COLLISION','seal':rec.manifest(out)},sort_keys=True))
