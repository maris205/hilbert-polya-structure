"""Materialize already-observed view/provenance metadata; not a visual checker."""
import hashlib,json,pathlib
D=pathlib.Path(__file__).resolve().parent
R=D.parents[3]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(name,x):
 p=D/name
 assert not p.exists()
 p.write_text(json.dumps(x,sort_keys=True,indent=2)+'\n')
notes=[
 'Title and Anonymous attribution clear; abstract/math legible; old-part sample and three-operation comparison table fit without clipping; page continuation at bottom is readable.',
 'Clock section, both lemmas and sharp theorem are legible; all inequalities and displayed witness fit; continuation to page3 is coherent; no overlap at proof boxes.',
 'Witness ending and N1 boundary visible; unique-refinement lemma, full three-case scan and order-sensitive example render cleanly; all displayed conditions present.',
 'Complete encoding/inverse, reserved terminal T1 discussion and known-series corollary visible; start of fibre section and endpoint coefficient formula fit margins.',
 'Every-target product/transfer formula clear; limitations include original box/counts, Robbins93/94 caveat and external hold; references begin cleanly.',
 'Remaining six bibliography entries and wrapped URLs readable; no missing citation marker, clipped text or identifying author metadata; intentional whitespace below references.'
]
for run in ['build01','build02']:
 put('VIEW_'+run+'.actual.json',{'reviewer':'/root/p210_a_reviewer','role':'actual manual inspection after viewing all6 page images with view_image, not inferred from hashes',
  'pdf':str((D/run/'source/main.pdf').relative_to(R)),'pdf_sha256':sha(D/run/'source/main.pdf'),
  'pages':[{'page':i,'path':str((D/run/('page-'+str(i)+'.png')).relative_to(R)),
            'sha256':sha(D/run/('page-'+str(i)+'.png')),'actually_viewed':True,'observation':notes[i-1]} for i in range(1,7)],
  'status':'PASS','open_layout_findings':0,'boundary':'Review A page inspection, not root or terminal-batch inspection'})
keyfiles=['verify.py','PARAMETERS.json','CANONICAL.json','DESIGN_COMMITMENT.md','COMMITMENT_PINS.sha256',
 'INPUT_PINS.sha256','instrumentation/evidence.py','instrumentation/runtime_probe.py','record.py',
 'pair02/INPUTS_BEFORE.json','pair02/INPUTS_AFTER.json','pair02/CONTEXT.json','pair02/runtime_1.json','pair02/runtime_2.json',
 'pair02/REPORT.json','execution/pair02/ATTEMPT.json','execution/pair02/RESULT.json']
context=json.loads((D/'pair02/CONTEXT.json').read_bytes())
put('REPLAY_KEYS.json',{'schema':'p210-a-replay-keys-v1','interpreter':'/usr/bin/python3.10',
 'flags':['-I','-S','-B','-X','pycache_prefix=NEW_ABSOLUTE_ABSENT_PATH'],'unoptimized':True,
 'parameters':json.loads((D/'PARAMETERS.json').read_bytes()),'environment':context['environment'],
 'file_keys':{str((D/f).relative_to(R)):sha(D/f) for f in keyfiles},
 'complete_runtime_key_ledgers':['pair02/INPUTS_BEFORE.json','pair02/INPUTS_AFTER.json'],
 'runtime_input_count':2631,'scientific_output_bytes':703850,'scientific_checks_per_run':133978,
 'scientific_schema':'p210-review-a-cut-graph-v1','complete_box_states':4095,
 'root_direct_command_template':['/usr/bin/python3.10','-I','-S','-B','-X','pycache_prefix=NEW_ABSOLUTE_ABSENT_PATH',str(D/'verify.py'),str(D/'PARAMETERS.json')],
 'root_requirements':'Two fresh invocations, actual stdout rawcmp against canonical and each other, full code/data/parameter/canonical/environment/runtime prepost closure. Root runs are not A runs.',
 'probe_scope':'post-hook Python opens/imports/modules and before/after maps; broad pre/post stdlib/sharedlibrary/config/locale inventory; not an OS/startup trace'})
print(json.dumps({'status':'RECORDED_ACTUAL_OBSERVATIONS','views':12,'replay_key_paths':len(keyfiles)},sort_keys=True))
