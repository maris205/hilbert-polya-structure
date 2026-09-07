"""Documentary-only command recorder; no finite-map producer is included."""
import argparse
import hashlib
import json
import pathlib
import re
import shutil
import subprocess
import sys

ROOT = pathlib.Path('/root/autodl-tmp/symbolic_dynamics')
HERE = pathlib.Path(__file__).resolve().parent
BATCH = 'docs/papers204_208_sequence/'
RECENT = tuple(BATCH + 'scouting/finite_systems_' + x + '/' for x in
               ('twenty_sixth', 'twenty_seventh', 'twenty_eighth'))
BAD_DIRS = {'order_geometry_tenth', 'order_geometry_tenth_desk',
            'finite_systems_nineteenth', 'ofs_gate', 'fth_gate'}

def allowed(path):
    p = pathlib.PurePosixPath(path)
    low = str(p).lower()
    if any(x.lower() in BAD_DIRS for x in p.parts):
        return False
    if re.search(r'p208|p209|ofs|fth', p.name, re.I):
        return False
    if any(re.match(r'(?:papers)?(?:208|209)(?:\D|$)', x, re.I) for x in p.parts):
        return False
    if low.startswith(BATCH) and not any(low.startswith(x) for x in RECENT):
        return False
    if low.startswith(BATCH) and len(p.parts) != 5:
        return False
    if any(x in low for x in ('frozen_round', '/snapshots/', '/historical_copies/',
                             '/source_capsule', '/runs/', '/runtime/', '/qa/',
                             '/controls/', '/sources/', '/__pycache__/',
                             '/history/', '/commands/', '/execution/', '/evidence/')):
        return False
    return p.suffix.lower() in {'.md', '.tex', '.py', '.bib', '.txt'}

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def run(label, argv, paths=None):
    out = HERE / 'evidence' / label
    out.mkdir(parents=True, exist_ok=False)
    if paths is not None:
        (out/'paths.json').write_text(json.dumps(paths, indent=2)+'\n')
        (out/'before.sha256').write_text(''.join(digest(ROOT/p)+'  '+p+'\n' for p in paths))
    proc = subprocess.run(argv, cwd=ROOT, capture_output=True)
    (out/'stdout').write_bytes(proc.stdout)
    (out/'stderr').write_bytes(proc.stderr)
    if paths is not None:
        (out/'after.sha256').write_text(''.join(digest(ROOT/p)+'  '+p+'\n' for p in paths))
    (out/'receipt.json').write_text(json.dumps({'kind':'documentary', 'cwd':str(ROOT),
       'argv':argv,'exit':proc.returncode,'stdout_sha256':digest(out/'stdout'),
       'stderr_sha256':digest(out/'stderr')},indent=2)+'\n')
    return proc

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('mode', choices=['discover','search','read','seal'])
    ap.add_argument('label', nargs='?')
    ap.add_argument('arg', nargs='*')
    a=ap.parse_args()
    if a.mode=='discover':
        argv=['rg','--files','--hidden','papers','docs']
        proc=run('01_path_discovery_corrected',argv)
        paths=sorted(p for p in proc.stdout.decode().splitlines() if allowed(p))
        (HERE/'corrected_discovery_paths.json').write_text(json.dumps(paths,indent=2)+'\n')
        (HERE/'corrected_discovery_pins.sha256').write_text(''.join(digest(ROOT/p)+'  '+p+'\n' for p in paths))
        print(json.dumps({'included':len(paths),'recent':[p for p in paths if p.startswith(BATCH)]},indent=2))
    elif a.mode=='search':
        paths=json.loads((HERE/'corrected_discovery_paths.json').read_text())
        proc=run(a.label,['rg','-n','-i','--',a.arg[0],*paths],paths)
        print(proc.stdout.decode(),end='')
        print('documentary_exit='+str(proc.returncode),file=sys.stderr)
    elif a.mode=='read':
        paths=a.arg
        if not all(allowed(p) for p in paths):
            raise ValueError('ineligible path')
        for i,p in enumerate(paths):
            proc=run(a.label+'_'+str(i),['sed','-n','1,$p',p],[p])
            snap=HERE/'snapshots'/p
            snap.parent.mkdir(parents=True,exist_ok=True)
            shutil.copyfile(ROOT/p,snap)
            print('READ_SCOPE '+p)
            print(proc.stdout.decode(),end='')
    else:
        paths=sorted(p for p in HERE.rglob('*') if p.is_file() and p.name!='SHA256SUMS')
        (HERE/'SHA256SUMS').write_text(''.join(digest(p)+'  '+str(p.relative_to(HERE))+'\n' for p in paths))
        print('sealed_payloads='+str(len(paths)))

if __name__=='__main__':
    main()
