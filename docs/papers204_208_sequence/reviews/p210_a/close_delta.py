"""Complete exact initial preservation/native closure and one-time final seal."""
import gzip, hashlib, json, pathlib, sys
D=pathlib.Path(__file__).resolve().parent
H=D/'history/initial_before_delta'
INITIAL='e60d352a6520dd5f56b01035912ce753bb1a669c7368ce0a999ff56a72ff966d'
RESPONSE='829acdc6048f1aa9b9dcbe0d1195bb935c3ea8ed84154dc2b2abc24ef2a17b66'
LEDGER='12e944d1d83cd582c2815f929b531d5f16538d6b4af81d68c7447fe7e3a8b634'
MODE=sys.argv[1]
assert MODE in ('seal','check')
assert sys.flags.isolated and sys.flags.no_site and sys.flags.dont_write_bytecode and not sys.flags.optimize
CHECKS=0
def need(ok,why):
    global CHECKS
    CHECKS+=1
    if not ok: raise AssertionError(why)
def raw(p): return pathlib.Path(p).read_bytes()
def sha(p): return hashlib.sha256(raw(p)).hexdigest()
def obj(p): return json.loads(raw(p))
def rows(p):
    result={}
    for line in raw(p).decode().splitlines():
        digest,rel=line.split('  ',1)
        need(len(digest)==64 and rel not in result and not pathlib.Path(rel).is_absolute() and '..' not in pathlib.Path(rel).parts,'strict nonself row')
        result[rel]=digest
    return result
need(sha(H/'SHA256SUMS')==INITIAL,'physical initial seal')
old=rows(H/'SHA256SUMS')
need(len(old)==484,'all484 initial payloads')
for rel,digest in old.items():
    path=H/'DELTA.md' if rel=='DELTA.md' else D/rel
    need(sha(path)==digest,'original byte preservation '+rel)
changed=[rel for rel,digest in old.items() if sha(D/rel)!=digest]
need(changed==['DELTA.md'],'only initial delta payload changed in place')
projection={('history/initial_before_delta/DELTA.md' if rel=='DELTA.md' else rel):digest for rel,digest in old.items()}
projection['history/initial_before_delta/SHA256SUMS']=INITIAL
need(rows(D/'INITIAL_PRESERVED_PINS.sha256')==projection,'full exact485 initial role projection')
before=raw(D/'DELTA_INPUTS_BEFORE.json.gz')
after=raw(D/'DELTA_INPUTS_AFTER.json.gz')
need(before==after and hashlib.sha256(before).hexdigest()==LEDGER,'complete byte-identical before/after keys')
need(len(json.loads(gzip.decompress(before)))==119881,'full known input count')
initial_findings=obj(D/'FINDINGS.json')
current=obj(D/'CURRENT_FINDINGS.json')
need(current['findings']==initial_findings['findings'] and current['census']==initial_findings['census'],'all initial finding details and census retained')
need(current['census']['total_open']==0 and current['census']['Major']['resolved']==1,'zero open with one resolved Major')
need(current['verdict']=='ACCEPTED_EXACT_NO_CHANGE_DELTA' and current['response_sha256']==RESPONSE,'precise accepted same-A response')
commands=('delta_preserve_delta01','delta_preserve_seal01','delta_cmp_initial_delta01','delta_cmp_initial_seal01',
          'delta_before01','delta_after01','delta_initial_preservation01','delta_frozen_inputs01',
          'delta_paper_manifest01','delta_round0_manifest01','delta_full_keys_cmp01',
          'delta_root_raw1_cmp01','delta_root_raw2_cmp01','delta_selected_pdf_cmp01')
records=[]
for name in commands:
    base=D/'execution'/name
    attempt,result=obj(base/'ATTEMPT.json'),obj(base/'RESULT.json')
    need(result['native_returncode']==0,'actual native success '+name)
    need(set(attempt['environment']) <= {'PATH','LANG','LC_ALL','LC_CTYPE','TZ'},'whitelist-only cleared launcher '+name)
    streams={}
    for channel in ('stdout','stderr'):
        need(sha(base/channel)==result[channel+'_sha256'],'complete original raw stream '+name)
        streams[channel]={'bytes':len(raw(base/channel)),'sha256':sha(base/channel)}
    need(streams['stderr']['bytes']==0,'no hidden command failure '+name)
    records.append({'name':name,'argv':attempt['argv'],'cwd':attempt['cwd'],'native_returncode':0,'streams':streams})
for name,count in (('delta_initial_preservation01',485),('delta_frozen_inputs01',494),('delta_paper_manifest01',987),('delta_round0_manifest01',493)):
    lines=raw(D/'execution'/name/'stdout').decode().splitlines()
    need(len(lines)==count and all(line.endswith(': OK') for line in lines),'full native manifest output '+name)
for name in ('delta_preserve_delta01','delta_preserve_seal01','delta_cmp_initial_delta01','delta_cmp_initial_seal01',
             'delta_full_keys_cmp01','delta_root_raw1_cmp01','delta_root_raw2_cmp01','delta_selected_pdf_cmp01'):
    need(not raw(D/'execution'/name/'stdout'),'complete silent native copy/cmp '+name)
for name,status,checks in (('delta_before01','PASS_SAME_A_DELTA_BEFORE',250531),('delta_after01','PASS_SAME_A_DELTA_AFTER',250533)):
    result=obj(D/'execution'/name/'stdout')
    need(result['status']==status and result['checks']==checks and result['input_paths_reread']==119881,'actual exact delta result '+name)
    need(result['ledger_sha256']==LEDGER and result['science_executions']==result['tex_builds']==result['new_views']==0,'no new science/build/view '+name)
summary={'schema':'p210-a-delta-native-closure-v1','reviewer':'/root/p210_a_reviewer',
         'status':'PASS_EXACT_ACCEPTED_NO_CHANGE_DELTA_NATIVE_AND_INITIAL_PRESERVATION',
         'response_sha256':RESPONSE,'initial_payloads_preserved':484,'initial_unchanged_in_place':483,
         'initial_seal_sha256':INITIAL,'initial_delta_path':'history/initial_before_delta/DELTA.md',
         'initial_seal_path':'history/initial_before_delta/SHA256SUMS','actual_safe_parent_native_commands':records,
         'before_checks':250531,'after_checks':250533,'unchanged_complete_key_count':119881,
         'complete_before_after_ledger_sha256':LEDGER,'current_census':current['census'],
         'science_runs':0,'builds':0,'new_views':0,'original_gates_reused':True,
         'root_final_gate':'not performed by reviewer; required before physical Round1/B',
         'historical_losses_recovered':False,'external_status':'OWNER_AMBER / HOLD_EXTERNAL'}
if MODE=='seal':
    need(sha(D/'SHA256SUMS')==INITIAL,'original seal still in place before replacement')
    need(not (D/'DELTA_CLOSURE.json').exists(),'new-only closure record')
    (D/'DELTA_CLOSURE.json').write_text(json.dumps(summary,sort_keys=True,indent=2)+'\n')
    current_files=sorted(p for p in D.rglob('*') if p.is_file() and p != D/'SHA256SUMS')
    need(all(not p.is_symlink() for p in current_files),'physical owned payloads')
    (D/'SHA256SUMS').write_text(''.join(sha(p)+'  '+str(p.relative_to(D))+'\n' for p in current_files))
else:
    need(obj(D/'DELTA_CLOSURE.json')==summary,'complete closure result unchanged')
sealed=rows(D/'SHA256SUMS')
need(set(sealed)=={str(p.relative_to(D)) for p in D.rglob('*') if p.is_file() and p != D/'SHA256SUMS'},'complete final nonself membership')
for rel,digest in sealed.items(): need(sha(D/rel)==digest,'complete final payload '+rel)
print(json.dumps({'status':'PASS_FINAL_A_DELTA_SEAL' if MODE=='seal' else 'PASS_READONLY_FINAL_A_DELTA_CLOSURE',
                  'checks':CHECKS,'payloads':len(sealed),'physical_files':len(sealed)+1,
                  'manifest_sha256':sha(D/'SHA256SUMS'),'delta_sha256':sha(D/'DELTA.md'),
                  'current_findings_sha256':sha(D/'CURRENT_FINDINGS.json'),'closure_sha256':sha(D/'DELTA_CLOSURE.json'),
                  'initial_preserved':484,'native_commands':len(records),'complete_before_after_keys':119881,
                  'zero_open':True,'resolved_major':1,'new_science_build_views':0},sort_keys=True))
