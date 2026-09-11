"""Read-only science boundary; generated files are documentary audit receipts."""
import hashlib
import json
import pathlib
import re
import subprocess
import sys

W = pathlib.Path('/root/autodl-tmp/symbolic_dynamics')
B = pathlib.Path(__file__).resolve().parent
CURRENT = 'docs/papers204_208_sequence/'
RECENT = tuple(CURRENT+'scouting/finite_systems_'+v+'/' for v in
               ['twenty_sixth','twenty_seventh','twenty_eighth'])
OUT = B/'final_documentary_audit'
CHECKS = 0

def check(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def dump(p, obj):
    p.write_text(json.dumps(obj, indent=2, sort_keys=True)+'\n')

def banned_science(path):
    p=pathlib.PurePosixPath(path)
    parts=[x.lower() for x in p.parts]
    return (bool(re.search('p208|p209|ofs|fth',p.name,re.I))
            or bool(set(parts)&{'order_geometry_tenth','order_geometry_tenth_desk',
                   'finite_systems_nineteenth','ofs_gate','fth_gate'})
            or any(re.match(r'(?:papers)?(?:208|209)(?:\D|$)',x) for x in parts)
            or (path.startswith(CURRENT) and not
                any(path.startswith(r) and len(p.parts)==5 for r in RECENT)))

def eligible(path):
    if banned_science(path):
        return False
    low=path.lower()
    if any(x in low for x in ['frozen_round','/snapshots/','/historical_copies/',
       '/source_capsule','/runs/','/runtime/','/qa/','/controls/','/sources/',
       '/__pycache__/','/history/','/commands/','/execution/','/evidence/']):
        return False
    return pathlib.PurePosixPath(path).suffix.lower() in ['.md','.tex','.py','.bib','.txt']

def cmd(label, argv):
    dest=OUT/label
    dest.mkdir()
    proc=subprocess.run(argv,cwd=W,capture_output=True)
    (dest/'stdout').write_bytes(proc.stdout)
    (dest/'stderr').write_bytes(proc.stderr)
    dump(dest/'receipt.json',{'kind':'documentary','argv':argv,'cwd':str(W),
         'exit':proc.returncode,'stdout_sha256':sha(dest/'stdout'),
         'stderr_sha256':sha(dest/'stderr')})
    check(proc.returncode==0, ('command',label,proc.returncode))
    return proc.stdout

def main():
    OUT.mkdir(exist_ok=False)
    own_before=sha(pathlib.Path(__file__))
    flags=[]
    for glob in ['!docs/papers204_208_sequence/**','!**/*p208*','!**/*p209*',
        '!**/*ofs*','!**/*fth*','!papers/208-*/**','!papers/209-*/**',
        '!**/order_geometry_tenth/**','!**/order_geometry_tenth_desk/**',
        '!**/finite_systems_nineteenth/**','!**/OFS_GATE/**','!**/FTH_GATE/**']:
        flags.extend(['--iglob',glob])
    broad=cmd('strict_discovery_old',['rg','--files','--hidden',*flags,'papers','docs'])
    recent_flags=['--maxdepth','1','--iglob','!**/*p208*','--iglob','!**/*p209*',
                  '--iglob','!**/*ofs*','--iglob','!**/*fth*']
    recent=cmd('strict_discovery_recent',['rg','--files','--hidden',*recent_flags,
                                        *[r.rstrip('/') for r in RECENT]])
    metadata=broad.decode().splitlines()+recent.decode().splitlines()
    check(all(not banned_science(p) for p in metadata),'strict raw metadata exclusions')
    final_paths=sorted(p for p in metadata if eligible(p))
    old_paths=json.loads((B/'corrected_discovery_paths.json').read_text())
    first_paths=json.loads((B/'discovery_paths.json').read_text())
    check(all(eligible(p) for p in old_paths),'corrected content paths safe')
    check(len(old_paths)==len(set(old_paths)),'unique corrected content paths')
    dump(OUT/'strict_discovery_paths.json',final_paths)
    dump(OUT/'strict_vs_content_paths.json',{'strict_only':sorted(set(final_paths)-set(old_paths)),
                                            'content_only':sorted(set(old_paths)-set(final_paths))})
    (OUT/'strict_discovery_pins.sha256').write_text(''.join(sha(W/p)+'  '+p+'\n' for p in final_paths))
    dump(OUT/'initial_extra_hashed_paths.json',sorted(set(first_paths)-set(old_paths)))
    initial_metadata={}
    for label in ['00_path_discovery','01_path_discovery_corrected']:
        listed=(B/'evidence'/label/'stdout').read_text().splitlines()
        initial_metadata[label]={'total':len(listed),
             'excluded_metadata_rows':sum(banned_science(p) for p in listed)}
    dump(OUT/'initial_metadata_failure.json',initial_metadata)

    receipts=0
    pin_rows=0
    content_searches=0
    explicit_reads=[]
    for folder in sorted((B/'evidence').iterdir()):
        receipt=json.loads((folder/'receipt.json').read_text())
        receipts+=1
        check(sha(folder/'stdout')==receipt['stdout_sha256'],str(folder)+' stdout')
        check(sha(folder/'stderr')==receipt['stderr_sha256'],str(folder)+' stderr')
        check(receipt['exit']==0,str(folder)+' exit')
        check(receipt['cwd']==str(W),str(folder)+' cwd')
        pathsfile=folder/'paths.json'
        if pathsfile.exists():
            paths=json.loads(pathsfile.read_text())
            check(all(eligible(p) for p in paths),str(folder)+' read paths')
            if receipt['argv'][0]=='rg':
                content_searches+=1
                check(paths==old_paths,str(folder)+' complete search pathlist')
                check(receipt['argv'][5:]==paths,str(folder)+' exact rg argv paths')
            else:
                check(receipt['argv']==['sed','-n','1,$p',paths[0]],str(folder)+' exact read argv')
                explicit_reads.extend(paths)
            cmd('cmp_'+folder.name,['cmp','-s',str(folder/'before.sha256'),str(folder/'after.sha256')])
            for manifest in [folder/'before.sha256',folder/'after.sha256']:
                rows=manifest.read_text().splitlines()
                check(len(rows)==len(paths),str(manifest)+' full rows')
                for row,path in zip(rows,paths):
                    digest,rel=row.split('  ',1)
                    check(rel==path,str(manifest)+' pin path')
                    check(sha(W/rel)==digest,str(manifest)+' current pin '+rel)
                    pin_rows+=1
    for rel in explicit_reads:
        check(sha(B/'snapshots'/rel)==sha(W/rel),'snapshot '+rel)

    aliases={
      'STATE.md':('SYMBOLIC_DYNAMICS_STATE.before.md','4b376b2475e335858ef26780160ae9e7aaaebb790b59dc27f942b7b592bfde25'),
      'PIPELINE.md':('PIPELINE_STATE.before.md','aeb4ca0405cf7ae25f56c2f0973bf2ee26aaba9e51e7555747bbd46743d422c1'),
      'GIT_SYNC_RECEIPT.md':('GIT_SYNC_RECEIPT.before.md','2f6998d2986831fa8776e31e9d336497e6ab37b114d1b13ef94879f3e2271c24')}
    alias_base=W/'docs/papers204_208_sequence/qa/central_lifecycle_p209_round1_push'
    alias_report={}
    for local,(alias,digest) in aliases.items():
        check(sha(B/'controls'/local)==digest,'immutable control '+local)
        check(sha(alias_base/alias)==digest,'root lifecycle alias '+alias)
        cmd('cmp_control_'+local,['cmp','-s',str(B/'controls'/local),str(alias_base/alias)])
        alias_report[local]={'sha256':digest,'exact_alias':str((alias_base/alias).relative_to(W))}
    check(sha(pathlib.Path(__file__))==own_before,'audit source unchanged')
    dump(OUT/'REPORT.json',{'status':'PASS_DOCUMENTARY_ONLY','checks':CHECKS,
       'receipts':receipts,'pin_rows':pin_rows,'content_searches':content_searches,
       'corrected_content_paths':len(old_paths),'strict_discovery_paths':len(final_paths),
       'explicit_original_reads':explicit_reads,'initial_hash_inventory':len(first_paths),
       'extra_initial_hashed_paths':len(set(first_paths)-set(old_paths)),
       'controls':alias_report,'audit_source_sha256':own_before,
       'python_executable':sys.executable,'python_resolved':str(pathlib.Path(sys.executable).resolve()),
       'python_sha256':sha(pathlib.Path(sys.executable).resolve()),
       'scientific_executions':0})
    print(json.dumps({'status':'PASS_DOCUMENTARY_ONLY','checks':CHECKS,
        'pin_rows':pin_rows,'content_searches':content_searches,
        'strict_discovery_paths':len(final_paths),'scientific_executions':0},sort_keys=True))

if __name__=='__main__':
    main()
