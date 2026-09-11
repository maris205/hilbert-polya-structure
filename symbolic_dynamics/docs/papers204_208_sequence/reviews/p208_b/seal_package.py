"""Read-only package audit, then bounded complete directory-relative nonself seal.

No scientific implementation is imported or executed by this final auditor.
"""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys
import time
BASE=Path('/root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/reviews/p208_b')
ROOT=BASE.parents[3]
FREEZE=ROOT/'papers/208-original-snapshot-triangulation-sweeps/frozen_round1'
CHECKS=0
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text())
def check(value,label):
    global CHECKS
    CHECKS+=1
    if not value:raise AssertionError(label)
def dump(p,obj):
    with Path(p).open('x') as f:json.dump(obj,f,indent=2,sort_keys=True);f.write('\n')
def manifest(path,root,expected=None):
    lines=Path(path).read_text().splitlines();seen=set()
    for row in lines:
        h,p=row.split('  ',1)
        check(p not in seen,('duplicate',p));seen.add(p)
        check(sha(root/p)==h,('pin',p))
    if expected is not None:check(len(lines)==expected,'manifest count')
    return seen
def pinpairs(directory,stems):
    for stem in stems:
        before=read(directory/(stem+'_BEFORE.json'));after=read(directory/(stem+'_AFTER.json'))
        check(before==after,('beforeafter',str(directory),stem))
        for p,h in before.items():
            if isinstance(h,str):check(sha(p)==h,('live relevant pin',p))
def commands(directory):
    for p in sorted(directory.glob('*.command.json')):
        r=read(p);check(r['exit_code']==0,('actual command exit',str(p)))
        prefix=p.name[:-len('.command.json')]
        for stream in ('stdout','stderr'):
            if stream+'_sha256' in r:
                check(sha(directory/(prefix+'.'+stream))==r[stream+'_sha256'],('stream hash',str(p),stream))
def audit():
    check(sha(FREEZE/'SHA256SUMS')=='12dca26eeb68503737846c633170bd427101648c21a9e89ef710d9ddaef01ace','immutable round1 manifest')
    manifest(FREEZE/'SHA256SUMS',FREEZE,487)
    manifest(BASE/'INPUT_PINS.sha256',ROOT)
    initial=read(BASE/'INITIAL_PIN_RECORD.json')
    for p,h in initial['initial_files'].items():check(sha(BASE/p)==h,('prereading initial file',p))
    for row in initial['assignment_context'].values():check(sha(BASE/row['snapshot'])==row['before_sha256'],'assignment historical snapshot')
    a=(BASE/'initial_kernel.py').read_text().split("if __name__ == \"__main__\":")[0].rstrip()
    check((BASE/'verify.py').read_text().startswith(a),'initial kernel unchanged in final science')
    for p,row in read(BASE/'SOURCE_CONTEXT_PINS.json')['paths'].items():
        check(sha(p)==row['sha256']==sha(BASE/row['snapshot']),('source context',p))
    hist=BASE/'history_context'
    hb=read(hist/'SEARCH_INPUTS_BEFORE.json');ha=read(hist/'SEARCH_INPUTS_AFTER.json')
    check(hb==ha and len(hb)==1917,'complete machine search beforeafter')
    for p,h in hb.items():check(sha(ROOT/p)==h,('original searched file',p))
    for p in (hist/'snapshots').rglob('*'):
        if p.is_file():check(sha(p)==hb[str(p.relative_to(hist/'snapshots'))],'search snapshot')
    pair=BASE/'final_pair';receipt=read(pair/'RECEIPT.json')
    check(receipt['status']=='PASS' and receipt['comparisons']==[0,0,0],'final actual pair receipt')
    pinpairs(pair,['INPUTS','CONFIG'])
    canonical=read(BASE/'CANONICAL.json');canonical_sha=sha(BASE/'CANONICAL.json')
    check(canonical_sha=='f809344b8692df7883109000b9914f441f7260739241e7f486547aea15335d07','canonical identity')
    check(canonical['checks']==3144418 and canonical['total_states']==2055,'science declared checks/carrier')
    check([len(b['rows']) for b in canonical['polygons']]==[1,2,5,14,42,132,429,1430],'complete boxes')
    before=read(pair/'INPUTS_BEFORE.json')
    for number in (1,2):
        check(sha(pair/f'run_{number}.stdout')==canonical_sha,'raw final stdout')
        check((pair/f'run_{number}.stderr').read_bytes()==b'','empty producer stderr')
        r=read(pair/f'run_{number}.runtime.json');cover=read(pair/f'run_{number}.coverage.json')
        check(not cover['missing'] and len(cover['consumed'])==44,'consumed complete coverage')
        check(r['exit_status']==0 and r['cache_prefix_still_absent'],'actual source-only execution')
        check(not Path(r['before']['pycache_prefix']).exists(),'still no bytecode prefix')
        for p,h in cover['consumed'].items():check(before[p]==h==sha(p),'runtime source pin')
        for side in ('before','after'):
            for p,h in r[side]['maps']['files'].items():check(before[p]==h==sha(p),'all actual producer maps')
            for row in r[side]['modules'].values():
                if 'sha256' in row:check(before[row['file']]==row['sha256']==sha(row['file']),'actual module file')
    observed=read(pair/'RECORDER_AND_OBSERVED_MAP_COVERAGE.json')
    check(not observed['missing'],'all recorder and observed command maps covered')
    for p,h in observed['consumed_or_observed'].items():check(before[p]==h==sha(p),'recorder observed path')
    for p in (pair/'producer_snapshot').iterdir():check(sha(p)==sha(BASE/p.name),'producer snapshot current')
    commands(pair);commands(BASE/'payload_comparison')
    comp=read(BASE/'payload_comparison/compare.stdout')
    check(comp['status']=='PASS' and comp['checks']==266834,'actual full data comparator')
    check(comp['before']==comp['after'],'comparator beforeafter')
    for row in comp['before'].values():check(sha(row['path'])==row['sha256'],'comparator current payload')
    build=BASE/'source_build';br=read(build/'RECEIPT.json')
    check(br['pages']==7 and br['embedded_fonts']==27 and br['all_command_exits_zero'],'actual build receipt')
    pinpairs(build,['INPUTS','TOOLS','LIBRARIES','TEX_INVENTORY','CONFIG','CONFIG_ABSENCE'])
    inventory={}
    for stem in ('TOOLS','LIBRARIES','TEX_INVENTORY','CONFIG'):inventory.update(read(build/(stem+'_BEFORE.json')))
    for p,h in read(build/'CONSUMED_TEX_INPUTS.json').items():check(inventory[p]==h==sha(p),'actually consumed TeX resource')
    ob=read(build/'OBSERVED_RUNTIME_MAP_COVERAGE.json');check(not ob['missing'],'build maps coverage')
    for p,h in ob['observed'].items():check(inventory[p]==h==sha(p),'all observed build maps')
    for side in ('BEFORE','AFTER'):
        r=read(build/('RECORDER_RUNTIME_'+side+'.json'))
        for p,h in r['map_files'].items():check(inventory.get(str(Path(p).resolve()),inventory.get(p))==h==sha(p),'build recorder complete maps')
        for row in r['modules'].values():
            if row['sha256']:check(inventory.get(str(Path(row['file']).resolve()),inventory.get(row['file']))==row['sha256']==sha(row['file']),'build recorder source module')
    commands(build)
    check(sha(build/'source_only/main.pdf')==sha(FREEZE/'main.pdf')==br['pdf_sha256'],'final built PDF')
    sources=read(build/'SOURCE_ONLY_INITIAL.json');check(len(sources)==11,'eleven source-only files')
    for p,h in sources.items():check(sha(build/'source_only'/p)==h,'source-only input unchanged')
    pages=sorted((build/'pages').glob('*.png'));check(len(pages)==7,'seven final renderings')
    text=(BASE/'PAGE_VIEWS.md').read_text()
    for p in pages:check(p.name in text,'actual per-page view record')
    check(br['warnings']['underfull']==['Underfull \\hbox (badness 5681) in paragraph at lines 9--13'],'actual warning exact')
    check(not br['warnings']['undefined'] and not br['warnings']['overfull'] and not br['warnings']['warning'],'no unresolved reference/citation warning')
    f=read(BASE/'FINDINGS.json')
    check(f['census']['open']=={'critical':0,'major':0,'minor':0},'zero current open findings')
    check(not f['delta_accepted'] and not (BASE/'DELTA.md').exists(),'no fabricated delta')
    check(len(f['findings'])==2 and all(row['status']=='resolved' for row in f['findings']),'exact resolved evidence census')
    if (BASE/'SHA256SUMS').exists():
        referents=manifest(BASE/'SHA256SUMS',BASE)
        allfiles={str(p.relative_to(BASE)) for p in BASE.rglob('*') if p.is_file() and p!=BASE/'SHA256SUMS'}
        check(referents==allfiles,'complete directory-relative nonself seal')
    return {'status':'PASS','checks':CHECKS,'round1_referents':487,'final_pair_inputs':len(before),
       'canonical_sha256':canonical_sha,'pdf_sha256':br['pdf_sha256'],'viewed_pages':7,
       'live_runtime_resource_and_source_keys_unchanged':True,
       'limit':'Read-only audit of actual recorded executions and current bytes, not another mathematical run or new visual inspection.'}
def seal():
    out=BASE/'package_audit';out.mkdir(exist_ok=False)
    args=[sys.executable,'-I','-S','-B',str(Path(__file__)),'audit']
    env={'PATH':'/root/miniconda3/bin:/usr/bin:/bin','LANG':'C','LC_ALL':'C','TZ':'UTC'}
    start=time.time()
    with (out/'audit.stdout').open('xb') as stdout,(out/'audit.stderr').open('xb') as stderr:
        p=subprocess.run(args,cwd=ROOT,env=env,stdout=stdout,stderr=stderr)
    dump(out/'audit.command.json',{'argv':args,'cwd':str(ROOT),'environment':env,'exit_code':p.returncode,
         'seconds':time.time()-start,'stdout_sha256':sha(out/'audit.stdout'),'stderr_sha256':sha(out/'audit.stderr')})
    assert p.returncode==0,'preserved failed final artifact audit'
    result=read(out/'audit.stdout')
    count=sum(p.is_file() for p in BASE.rglob('*'))+1
    dump(BASE/'SEAL_RECEIPT.json',{'status':'SEALED_INITIAL_B','payload_count':count,
        'nonself_manifest':'SHA256SUMS','all_payload_files_included':True,
        'audit':result,'manifest_hash_location':'actual launcher stdout; not embedded circularly in its own referent',
        'delta_status':'No root response or acceptance yet.'})
    files=sorted(p for p in BASE.rglob('*') if p.is_file())
    assert len(files)==count and not (BASE/'SHA256SUMS').exists()
    with (BASE/'SHA256SUMS').open('x') as stream:
        for p in files:stream.write(sha(p)+'  '+str(p.relative_to(BASE))+'\n')
    referents=manifest(BASE/'SHA256SUMS',BASE,count)
    actual={str(p.relative_to(BASE)) for p in BASE.rglob('*') if p.is_file() and p!=BASE/'SHA256SUMS'}
    assert referents==actual
    print(json.dumps({'status':'PASS_SEALED_INITIAL_B','payloads':count,'manifest_sha256':sha(BASE/'SHA256SUMS'),
                      'audit':result},sort_keys=True))
if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1]=='audit':print(json.dumps(audit(),sort_keys=True))
    else:seal()
