#!/usr/bin/env python3
"""ROOT-ONLY read-only documentary checker. Never imports/runs Scout33 science.
Preparation must not execute this file. Only subprocess: three /usr/bin/cmp
calls comparing already archived outputs. No compile, producer or web calls.
"""
import argparse
from collections import Counter, defaultdict
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import stat
import struct
import subprocess
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
REL = 'docs/papers204_208_sequence/scouting/finite_systems_thirty_third'
S = ROOT / REL
PREP = ROOT / 'docs/papers204_208_sequence/qa/scout33_root_check_preparation'
SELF_SEAL = 'PREPARATION_SHA256SUMS'
OLD_SEAL = '74004ca903c61efce6313781549b30c269c43794ce3d550a9f090c342d373d53'
FINAL_SEAL = 'e839102239f6d3936514c62419b447c7bfa48ec7cbbe5e854590a88de73c573e'
EMPTY = sha256(b'').hexdigest()
TOOLS = {Path('/usr/bin') / n for n in
         ('cmp', 'cp', 'curl', 'gcc', 'objdump', 'pdftotext', 'readelf', 'sha256sum', 'uname')}
PROTECTED = {
 'docs/papers204_208_sequence/scouting/finite_systems_twentieth/INTAKE.md': '0f52bca7e4754c52bbc8d6319534f4b253867a32801ee1947c74ae17bfb70dbc',
 'docs/papers204_208_sequence/scouting/finite_systems_twentieth/PROOF_AND_ADAPTERS.md': 'f748cb681f0f0e5c6cafb508e8b9ff97e0a6a91b0fc2211c310dbac53239784b',
 'docs/papers204_208_sequence/scouting/finite_systems_twentieth/SCOUT_REPORT.md': '1aacb48943f674cc232b5010280a01cd83e7596a1c659ae12fb67d3df4b8fa90',
 'docs/papers204_208_sequence/scouting/order_geometry_tenth/INTAKE.md': '7a0a9605e25efe82fdab5e2bbc8402761240288f27f150cd22cfb86500a51261',
 'docs/papers204_208_sequence/scouting/order_geometry_tenth/PROOF_AND_DISPOSITION.md': '912b262805a061f7ac175ae8f9506b77344c926cd8fe706ebe65e95a3dba342b',
 'docs/papers204_208_sequence/scouting/order_geometry_tenth/SCOUT_REPORT.md': '109b5a9a80a7653de38f9b6aa9fa7b26d29503b90973d07cb1523e45bb9b361f',
 'docs/papers204_208_sequence/scouting/order_geometry_tenth/SOURCE_AND_COLLISION_NOTES.md': '0e6cbb24ca689e8c46ed00f0d5f60566997fffd40e3de15c11a070517b36b0e1',
 'docs/papers204_208_sequence/scouting/order_geometry_tenth_desk/PROOF_AND_ADAPTER.md': '181f18e946fb2d526af67addb1f06e8bfff257d82ada054ba90069f9176daeb9',
}
CONTROL_ROWS = [
 ('SYMBOLIC_DYNAMICS_STATE.md', '94cc7fa657ecee1d4b3d18b26d05813b8b5e3979f127f62ea8e77bfaa82640e0', 'controls/SYMBOLIC_DYNAMICS_STATE.md'),
 ('docs/papers204_208_sequence/PIPELINE_STATE.md', 'a1ad9005e147bef705761f16ae861a52b392fc2020fa46af7bb86cce4f52e7bd', 'controls/PIPELINE_STATE.md'),
 ('docs/papers204_208_sequence/GIT_SYNC_RECEIPT.md', 'a67457d5fe6e860040ad5f72a51b839e0220b7b83af22188008c8a74850b1865', 'controls/GIT_SYNC_RECEIPT.md'),
]
SCIENCE_PINS = {
 'pilot.c': '2341a626df91f9205d077ea1d0565d59e4fbaf6cceaf760975ff281a7be7de5e',
 'pilot': '834a4ecc6f989340ad3f05b086a37efa6d7f9d4040fcef7f8e542a1a11f96a75',
 'INTAKE.md': '72bbd264f03c96f87b9db24731323938673095439e8df077a0e768fcb296b008',
 'CANONICAL.raw': '80e1d40a04b48f0bf4944f5c88b9013e06b871ed8bb7a4fb9d71c031dc2dd356',
}
checks = 0


def need(condition, label):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(label)


def safe_relative(name):
    return (isinstance(name, str) and name and not Path(name).is_absolute()
            and '\\' not in name and all(p not in ('', '.', '..') for p in name.split('/')))


def physical_census(base):
    files = set()
    for directory, dirs, names in os.walk(base, followlinks=False):
        for name in dirs + names:
            p = Path(directory) / name
            need(not p.is_symlink(), 'owned symlink forbidden: ' + str(p))
        for name in names:
            p = Path(directory) / name
            need(stat.S_ISREG(p.stat().st_mode), 'owned regular file: ' + str(p))
            files.add(str(p.relative_to(base)))
    return files


class ReadLedger:
    def __init__(self):
        self.allowed = {S/'SHA256SUMS', S/'FINAL_SHA256SUMS', PREP/SELF_SEAL}
        self.cache = {}
        self.before = {}
        self.after = {}
        self.reasons = defaultdict(set)

    def allow(self, paths):
        for p in paths:
            need(p.is_absolute() and '..' not in p.parts, 'absolute lexical allow path')
            need(str(p) not in {str(ROOT/n) for n in PROTECTED}, 'no protected current authorization')
            self.allowed.add(p)

    def one(self, p):
        need(p in self.allowed, 'current path explicitly authorized: ' + str(p))
        need(str(p) not in {str(ROOT/n) for n in PROTECTED}, 'protected read guard')
        need(p.is_file(), 'current regular-file referent exists: ' + str(p))
        resolved = p.resolve(strict=True)
        if p in TOOLS:
            need(str(resolved).startswith('/usr/'), 'fixed OS-tool symlink target')
        else:
            need(not p.is_symlink() and resolved == p, 'original lexical physical identity')
        raw = p.read_bytes()
        row = {'sha256': sha256(raw).hexdigest(), 'bytes': len(raw),
               'resolved_path': str(resolved)}
        return raw, row

    def read(self, p, reason):
        self.reasons[str(p)].add(reason)
        if p not in self.cache:
            raw, row = self.one(p)
            self.cache[p] = raw
            self.before[str(p)] = row
        return self.cache[p]

    def pin(self, p, digest, reason):
        raw = self.read(p, reason)
        need(sha256(raw).hexdigest() == digest, 'exact current pin: ' + str(p))
        return raw

    def second_pass(self):
        for name, expected in sorted(self.before.items()):
            raw, actual = self.one(Path(name))
            need(actual == expected and raw == self.cache[Path(name)],
                 'second full-byte read unchanged: ' + name)
            self.after[name] = actual
        need(set(self.after) == set(self.before), 'complete second physical-read coverage')


def read_json(ledger, path, reason):
    return json.loads(ledger.read(path, reason))


def manifest(ledger, base, filename, digest, expected_count=None):
    raw = ledger.pin(base/filename, digest, 'manifest authentication')
    need(raw.endswith(b'\n'), 'manifest final newline')
    result = {}
    for line in raw.decode('utf-8').splitlines():
        need(bool(re.fullmatch(r'[0-9a-f]{64}  .+', line)), 'manifest raw syntax')
        pin, name = line.split('  ', 1)
        need(safe_relative(name) and name not in result and name != filename,
             'manifest safe unique nonself name')
        result[name] = pin
    need(list(result) == sorted(result, key=Path), 'manifest recorded pathlib component order')
    if expected_count is not None:
        need(len(result) == expected_count, 'manifest count')
    ledger.allow(base/name for name in result)
    for name, pin in result.items():
        ledger.pin(base/name, pin, 'manifest payload')
    return result


def old_original(p):
    """Literal historical filename selector, never opens a discovered body."""
    parts = p.split('/')
    if REL in p:
        return False
    if any(re.search(r'review|qa|freez|froz|snapshot|source|runtime|history|historical|command|build|compile|copied|receipt|execution', s, re.I) for s in parts[:-1]):
        return False
    if any(re.search(r'(^|[^a-z0-9])(p?208|p?209|ofs|fth)([^a-z0-9]|$)', s, re.I)
           for s in parts[2:] if not re.fullmatch(r'papers[0-9]+_[0-9]+_sequence', s)):
        return False
    if re.match(r'papers/(208|209)-', p):
        return False
    if re.fullmatch(r'papers/[0-9]+-[^/]+/(main\.tex|sections/[^/]+\.tex|PROOF_PACKAGE\.md)', p):
        return True
    if re.fullmatch(r'docs/papers[0-9]+_[0-9]+_sequence/scouting/[^/]+/[^/]+\.md', p):
        return any(s in parts[-1] for s in ('PROOF','SCOUT_REPORT','KILL','CANDIDATE_LEDGER','INTAKE','DISPOSITION','COLLISION','THEOREM','DOSSIER'))
    return bool(re.fullmatch(r'docs/papers[0-9]+_[0-9]+_sequence/phase1/(CANDIDATE_POOL_AND_KILL_LEDGER|THEOREM_CONTRACTS|SYSTEM_COLLISION_FIREWALL)\.md', p))


def tier_original(p, tier):
    if not old_original(p):
        return False
    if tier >= 1:
        if (any('gate' in s.lower() for s in p.split('/')[2:-1])
            or 'TITLE' in p.rsplit('/',1)[1]
            or '/scouting/finite_systems_nineteenth/' in p):
            return False
    blocked = ()
    if tier >= 2:
        blocked += ('order_geometry_tenth','order_geometry_tenth_desk')
    if tier >= 3:
        blocked += ('finite_systems_twentieth',)
    return not any('/scouting/'+name+'/' in p for name in blocked)


def command_contract(selected, initial):
    P = lambda n: REL+'/'+n
    compiler = '/usr/bin/gcc'
    executable = str(S/'pilot')
    python = '/root/miniconda3/bin/python3'
    specs = {}

    def add(label, argv, inputs, cwd=ROOT, exit_code=0, group='commands'):
        specs[group+'/'+label] = {'argv': argv, 'inputs': sorted(set(inputs)),
                                  'cwd': str(cwd), 'exit': exit_code}

    discovery = ['rg','--files','papers','docs','-g','*.md','-g','*.tex']
    globs = ('**/reviews/**','**/qa/**','**/*froz*/**','**/*freez*/**','**/*snapshot*/**',
             '**/*source*/**','**/*runtime*/**','**/*history*/**','**/*historical*/**',
             '**/*commands*/**','**/*build*/**','**/*compile*/**','**/*copied*/**',
             '**/*receipts*/**','**/*execution*/**','papers/208-*/**','papers/209-*/**',
             '**/OFS*/**','**/FTH*/**')
    for glob in globs:
        discovery += ['-g','!'+glob]
    add('01_path_discovery', discovery, [P('SCOPE.md'),P('record.py')])
    for label, script, listname, extras in [
        ('02_actual_selected_paths','record_v2.py','SELECTED_ORIGINALS_V2.json',['record.py']),
        ('03_final_actual_paths','record_final.py','SELECTED_ORIGINALS_FINAL.json',['record_v2.py','record.py']),
        ('05_refined_actual_paths','record_scoped.py','SELECTED_ORIGINALS_SCOPED.json',['record_v2.py','record.py'])]:
        add(label,[python,'-I','-B',P(script),'verify_paths'],
            selected[listname]+[P(n) for n in [listname,script]+extras])
    patterns = [
        ('04_orientation_partition','SELECTED_ORIGINALS_FINAL.json','tournament|acyclic orientation|sink reversal|source reversal|sink.popp|click equivalence|rowmotion|Kreweras|Bulgarian|partition.*conjugat|chip.fir|rotor.router'),
        ('06_oriented_square','SELECTED_ORIGINALS_SCOPED.json','oriented graph|Boolean.*squar|squar.*Boolean|two.step.*path|length.two.*path|skew.*support|asymmetric.*part|asymmetr.*squar|walk.*squar|digraph.*power|power.*digraph'),
        ('23_cancellation_circulant','SELECTED_ORIGINALS_SCOPED.json','asymmetric.*part|asymmetric.*squar|two.step.*cancel|reciprocal.*cancel|digraph.*squar|circulant|1, ?2, ?4, ?8|sumset.*difference|sumset.*subtract')]
    for label, listname, pattern in patterns:
        add(label,['rg','-n','-i','--',pattern]+selected[listname],selected[listname])
    core=[P('INTAKE.md'),P('pilot.c')]
    add('07_compiler_version',[compiler,'--version'],[compiler])
    add('08_compile_static',[compiler,'-nostdlib','-static','-fno-stack-protector','-fno-builtin','-fno-pie','-no-pie','-O2','-Wall','-Wextra','-Werror','-Wl,--build-id=none','-o',P('pilot'),P('pilot.c')],core+[compiler])
    add('09_static_elf',['/usr/bin/readelf','-l','-d','-s',P('pilot')],core+[P('pilot'),'/usr/bin/readelf'])
    for label in ('10_pilot_a','11_pilot_b'):
        add(label,[executable],core+[P('pilot')])
    a,b,c=P('commands/10_pilot_a/stdout.raw'),P('commands/11_pilot_b/stdout.raw'),P('CANONICAL.raw')
    for label,x,y in [('12_raw_canonical_cmp',a,b),('15_run_a_raw_canonical_cmp',a,c),('16_run_b_raw_canonical_cmp',b,c)]:
        add(label,['/usr/bin/cmp',x,y],[x,y,'/usr/bin/cmp'])
    add('13_p171_original',['sed','-n','1,99999p','papers/171-boolean-gram-dynamics/main.tex'],['papers/171-boolean-gram-dynamics/main.tex'])
    add('14_preserve_raw_canonical',['/usr/bin/cp','-p',a,c],[a,'/usr/bin/cp'])
    add('17_disassembly',['/usr/bin/objdump','-d',P('pilot')],[P('pilot'),P('pilot.c'),'/usr/bin/objdump'])
    add('18_runtime_platform',['/usr/bin/uname','-srvm'],['/usr/bin/uname'])
    for num,name,url in [
        ('19','kutz_2004','https://people.mpi-inf.mpg.de/alumni/d1/2009/mkutz/diss/kutzdiss.pdf'),
        ('20','deschutter_1997','https://www.dcsc.tudelft.nl/~bdeschutter/pub/rep/97_67.pdf')]:
        pdf=P('sources/'+name+'.pdf')
        add(num+'_fetch_'+name,['/usr/bin/curl','-L','--fail','--max-time','45','-D',P('sources/'+name+'.headers'),'-o',pdf,url],['/usr/bin/curl'])
        add(num+'b_extract_'+name,['/usr/bin/pdftotext','-layout',pdf,P('sources/'+name+'.txt')],[pdf,'/usr/bin/pdftotext'])
    for label,span,name in [('21_kutz_primary_context','3491,3685p','kutz_2004'),('22_deschutter_primary_context','1,280p','deschutter_1997')]:
        path=P('sources/'+name+'.txt')
        add(label,['sed','-n',span,path],[path])
    closure_inputs=[P(name) for name in initial if not name.startswith('commands/24_documentary_closure/') and name!='HANDOFF.md']
    need(len(closure_inputs)==185,'original closure input role')
    add('24_documentary_closure',[python,'-I','-B',P('close.py')],closure_inputs)
    post_inputs=[str(S/name) for name in initial]+[str(S/'SHA256SUMS'),str(S/'postcheck.py'),str(S/'POSTCHECK_FAILURE_TRANSCRIPTION.md'),'/usr/bin/sha256sum']
    add('01_wrong_cwd_reproduction',['sha256sum','-c',P('SHA256SUMS')],post_inputs,exit_code=1,group='postcheck')
    add('02_correct_cwd',['sha256sum','-c','SHA256SUMS'],post_inputs,cwd=S,group='postcheck')
    need(len(specs)==28,'literal native command contract count')
    return specs


def canonical_consistency(raw):
    """Validates only the already printed transition table; no OTC update."""
    need(len(raw)==19667 and raw.endswith(b'\n'),'canonical exact raw extent')
    lines=raw.decode('ascii').splitlines()
    need(len(lines)==845,'complete canonical line count')
    need(lines[0]=='OTC original complete pilot v1; columns STATE n id target tail period cycle_min incoming','canonical header')
    cursor=1
    stats=[]
    structural=0
    total_states=0
    for n,count in ((1,1),(2,3),(3,27),(4,729)):
        rows=[]
        printed_cycles=[]
        for ident in range(count):
            tokens=lines[cursor].split(); cursor+=1
            need(len(tokens)==8 and tokens[0]=='STATE','canonical complete STATE grammar')
            row=tuple(map(int,tokens[1:]))
            dn,di,target,tail,period,rep,incoming=row
            need((dn,di)==(n,ident) and 0<=target<count and 0<=tail<count
                 and 1<=period<=count and 0<=rep<count and 0<=incoming<=count,
                 'complete labelled original-box row domain/order')
            rows.append(row)
            if tail==0 and ident==rep:
                tokens=lines[cursor].split(); cursor+=1
                need(tokens[0]=='CYCLE' and len(tokens)==3+period,'printed cycle grammar')
                vals=tuple(map(int,tokens[1:]))
                need(vals[:2]==(n,period),'printed cycle dimensions')
                printed_cycles.append(vals[2:])
        targets=[row[2] for row in rows]
        incoming=Counter(targets)
        tails=Counter()
        periods=Counter()
        expected_cycles=[]
        for ident,row in enumerate(rows):
            dn,di,target,tail,period,rep,parent_count=row
            need(parent_count==incoming[ident],'full printed incoming count')
            seen={}; orbit=[]; x=ident
            while x not in seen:
                seen[x]=len(orbit); orbit.append(x); x=targets[x]
                need(len(orbit)<=count,'printed functional graph orbit bound')
            split=seen[x]; cycle=orbit[split:]
            need((tail,period,rep)==(split,len(cycle),min(cycle)),'printed orbit descriptors agree with printed targets')
            if tail==0 and ident==rep:
                expected_cycles.append(tuple(cycle))
            tails[tail]+=1; periods[period]+=1
            structural+=1+tail+period
        need(printed_cycles==expected_cycles,'all printed cycles complete and ordered')
        summary=(n,count,len(incoming),tails[0],sum(t==i for i,t in enumerate(targets)),
                 max(tails),max(periods),max(incoming.values()))
        prefix='SUMMARY n states image recurrent fixed max_tail max_period max_fibre '
        need(lines[cursor].startswith(prefix),'summary complete grammar')
        need(tuple(map(int,lines[cursor][len(prefix):].split()))==summary,'all summary columns')
        cursor+=1
        need(lines[cursor]=='TAIL_HIST '+str(n)+''.join(' '+str(k)+':'+str(tails[k]) for k in range(max(tails)+1)),'full tail histogram')
        cursor+=1
        need(lines[cursor]=='PERIOD_HIST '+str(n)+''.join(' '+str(k)+':'+str(periods[k]) for k in sorted(periods)),'full period histogram')
        cursor+=1
        need(sum(incoming.values())==sum(tails.values())==sum(periods.values())==count,'three totals from complete printed table')
        structural+=3; total_states+=count
        stats.append({'n':n,'states':count,'summary':list(summary),'cycles':len(expected_cycles)})
    need(cursor==len(lines)-1 and lines[cursor]=='DONE states checks 760 2852','no extra or omitted canonical sections')
    need(total_states==760 and structural==2852,'recorded structural counter consistent with printed table')
    return {'scope':'Consistency of all archived rows only; no literal OTC update or scientific execution',
            'states':760,'lines':845,'recorded_checks_per_run':2852,'boxes':stats}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--expected-preparation-sha256',required=True)
    args=parser.parse_args()
    need(bool(re.fullmatch(r'[0-9a-f]{64}',args.expected_preparation_sha256)),'caller-fixed preparation seal')
    need(sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode
         and not sys.flags.optimize,'isolated no-site no-bytecode unoptimized execution')
    need(Path.cwd()==ROOT,'root checker cwd')
    ledger=ReadLedger()
    ledger.allow({Path(__file__).resolve()})
    ledger.read(Path(__file__).resolve(), 'actual root V2 adapter source')
    own=manifest(ledger,PREP,SELF_SEAL,args.expected_preparation_sha256)
    own_census=physical_census(PREP)
    need(own_census==set(own)|{SELF_SEAL},'complete preparation physical census')
    outer=manifest(ledger,S,'FINAL_SHA256SUMS',FINAL_SEAL,208)
    inner=manifest(ledger,S,'SHA256SUMS',OLD_SEAL,192)
    scout_census=physical_census(S)
    need(scout_census==set(outer)|{'FINAL_SHA256SUMS'} and len(scout_census)==209,
         'complete final scout physical census')
    need(set(inner)<set(outer) and all(outer[n]==h for n,h in inner.items())
         and outer['SHA256SUMS']==OLD_SEAL,'all initial192 payload bytes preserved at same physical names')

    names=['SELECTED_ORIGINALS.json','SELECTED_ORIGINALS_V2.json','SELECTED_ORIGINALS_FINAL.json','SELECTED_ORIGINALS_SCOPED.json']
    discovered=ledger.read(S/'commands/01_path_discovery/stdout.raw','complete archived filename discovery').decode().splitlines()
    need(len(discovered)==5110 and len(set(discovered))==5110
         and all(safe_relative(p) for p in discovered),'all discovery names, not their bodies')
    selected={}
    for tier,(name,count) in enumerate(zip(names,(1239,1227,1222,1219))):
        values=read_json(ledger,S/name,'complete original selection metadata')
        need(values==sorted(set(values)) and len(values)==count,'selection count/order')
        need(values==sorted(p for p in discovered if tier_original(p,tier)),
             'complete exact historical selector reconstruction')
        selected[name]=values
    scoped=set(selected[names[-1]])
    ledger.allow(ROOT/p for p in scoped)
    ledger.allow(TOOLS)

    protected_doc=read_json(ledger,PREP/'PROTECTED_HISTORICAL_ROLES.json','fixed protected archived-role contract')
    need({r['historical_workspace_path']:r['sha256'] for r in protected_doc['protected_roles']}==PROTECTED,
         'exact eight protected fixed path/hash roles')
    protected_occurrences=[]
    for row in protected_doc['protected_roles']:
        need(row['current_access']=='SKIP_CURRENT_BODY_AND_HASH','protected no-read policy')
        for occurrence in row['archived_occurrences']:
            raw=ledger.pin(S/occurrence['record_path'],occurrence['record_sha256'],'protected archived metadata only')
            need(json.loads(raw)[occurrence['literal_key']]==occurrence['value']==row['sha256'],
                 'protected archived literal role and value')
            protected_occurrences.append((occurrence['record_path'],occurrence['literal_key'],occurrence['value']))
    need(len(protected_occurrences)==28 and len(set(protected_occurrences))==28,'all fixed protected archived occurrences')

    alias_doc=read_json(ledger,S/'CONTROL_ALIASES.json','literal old-control aliases')
    actual_aliases=[(r['historical_workspace_path'],r['sha256'],r['local_copy']) for r in alias_doc['aliases']]
    need(actual_aliases==CONTROL_ROWS,'only three exact documented aliases')
    aliases={(name,pin):S/copy for name,pin,copy in CONTROL_ROWS}
    for name,pin,copy in CONTROL_ROWS:
        ledger.pin(S/copy,pin,'literal old-path plus old-hash control role')
    bootstrap=ledger.read(S/'BOOTSTRAP_TRANSCRIPTION.md','historical capture disclosure').decode()
    need('not native recorder' in bootstrap.lower(),'capture remains tool transcription')

    specs=command_contract(selected,inner)
    actual_dirs={str(p.parent.relative_to(S)) for group in ('commands','postcheck')
                 for p in (S/group).glob('*/receipt.json')}
    need(actual_dirs==set(specs),'complete command-package physical census')
    receipts={}
    all_roles=[]
    native_fields={'argv','cwd','exit','finished_epoch','input_count','label','recorder_sha256',
                   'started_epoch','stderr_sha256','stdout_sha256','unchanged'}
    expected_files={'receipt.json','inputs_before.json','inputs_after.json','pathset.json','stdout.raw','stderr.raw'}
    recorder=sha256(ledger.read(S/'record.py','native recorder source pin')).hexdigest()
    post_recorder=sha256(ledger.read(S/'postcheck.py','postcheck recorder source pin')).hexdigest()
    observed_protected=[]
    physical_inputs=set()
    for name,spec in specs.items():
        folder=S/name
        need({p.name for p in folder.iterdir()}==expected_files,'exact native command six-file census')
        rec=read_json(ledger,folder/'receipt.json','native command receipt')
        before=read_json(ledger,folder/'inputs_before.json','native full inputs before')
        after=read_json(ledger,folder/'inputs_after.json','native full inputs after')
        paths=read_json(ledger,folder/'pathset.json','native full pathset')
        is_post=name.startswith('postcheck/')
        need(set(rec)==native_fields|({'role','expected_exit'} if is_post else set()),'exact receipt schema')
        need(rec['label']==folder.name and rec['argv']==spec['argv'] and rec['cwd']==spec['cwd']
             and rec['exit']==spec['exit'],'exact archived command/cwd/exit contract')
        need(isinstance(rec['started_epoch'],(int,float)) and isinstance(rec['finished_epoch'],(int,float))
             and 0<rec['started_epoch']<=rec['finished_epoch'],'actual receipt timestamps')
        need(paths==sorted(set(paths))==sorted(before)==sorted(after)==spec['inputs'],
             'complete exact path/input-before/input-after roles')
        need(len(paths)==rec['input_count'] and before==after and rec['unchanged'] is True,
             'complete unchanged input maps including failed command')
        need(rec['recorder_sha256']==(post_recorder if is_post else recorder),'correct recorder version role')
        if is_post:
            need(rec['expected_exit']==spec['exit'] and rec['role']=='new_documentary_execution_not_original_tool_transcription',
                 'wrong-cwd reproduction is separate actual execution')
        for channel in ('stdout','stderr'):
            ledger.pin(folder/(channel+'.raw'),rec[channel+'_sha256'],'complete native raw '+channel)
        if name not in {'commands/19_fetch_kutz_2004','commands/20_fetch_deschutter_1997','postcheck/01_wrong_cwd_reproduction'}:
            need(rec['stderr_sha256']==EMPTY,'recorded blank stderr where actually expected')
        for phase,mapping in [('inputs_before.json',before),('inputs_after.json',after)]:
            for literal,pin in mapping.items():
                need(bool(re.fullmatch(r'[0-9a-f]{64}',pin)),'historical digest syntax')
                physical=ROOT/literal
                physical_inputs.add(str(physical))
                if literal in PROTECTED:
                    need(pin==PROTECTED[literal],'protected exact historical pin')
                    observed_protected.append((name+'/'+phase,literal,pin))
                    resolution='SKIP_CURRENT_PROTECTED_BODY_AND_HASH'
                else:
                    if (literal,pin) in aliases:
                        physical=aliases[(literal,pin)]
                        resolution='EXACT_DOCUMENTED_OLDPATH_OLDHASH_ALIAS'
                    else:
                        need(physical in ledger.allowed,'no unapproved current original path')
                        resolution='EXACT_PHYSICAL_INPUT'
                    ledger.pin(physical,pin,'archived '+name+'/'+phase+' input')
                all_roles.append({'record':name+'/'+phase,'literal_path':literal,'sha256':pin,
                                  'resolution':resolution,'physical_path':str(physical)})
        receipts[name]=rec
    need(sorted(observed_protected)==sorted(protected_occurrences),'exact fixed skip census, no extra skip')
    need(len(all_roles)==15912 and len(physical_inputs)==1431,'all before/after roles and normalized inputs')
    need(len({r['literal_path'] for r in all_roles})==1616,'all literal historical input names')
    ordered=sorted(receipts.items(),key=lambda item:item[1]['started_epoch'])
    need(all(a[1]['finished_epoch']<=b[1]['started_epoch'] for a,b in zip(ordered,ordered[1:])),
         'all preserved native commands completed in documented nonoverlapping order')

    for label,listname in [('02_actual_selected_paths',names[1]),('03_final_actual_paths',names[2]),('05_refined_actual_paths',names[3])]:
        rows=ledger.read(S/'commands'/label/'stdout.raw','complete actual-path output').decode().splitlines()
        need(rows[:-1]==selected[listname],'every actual-path output name')
        trailer=json.loads(rows[-1])
        need(trailer=={'actual_paths':len(selected[listname]),'all_valid':True},'actual-path verification trailer')
    for label in ('04_orientation_partition','06_oriented_square','23_cancellation_circulant'):
        rec=receipts['commands/'+label]
        lines=ledger.read(S/'commands'/label/'stdout.raw','complete historical search output').decode().splitlines()
        corpus=set(rec['argv'][5:])
        for line in lines:
            matched=re.fullmatch(r'([^:]+):([0-9]+):(.*)',line)
            need(matched is not None and matched[1] in corpus,'every archived rg match maps to its actual corpus')
            need(int(matched[2])>0,'search output positive original line')
            if matched[1] not in PROTECTED:
                original_lines=ledger.read(ROOT/matched[1],'matched original line byte role').decode().splitlines()
                need(int(matched[2])<=len(original_lines) and original_lines[int(matched[2])-1]==matched[3],
                     'every returned match agrees with pinned permitted original')
    for label,path,start,end in [
        ('13_p171_original',ROOT/'papers/171-boolean-gram-dynamics/main.tex',1,99999),
        ('21_kutz_primary_context',S/'sources/kutz_2004.txt',3491,3685),
        ('22_deschutter_primary_context',S/'sources/deschutter_1997.txt',1,280)]:
        full=ledger.read(path,'actual sed source extent')
        chunks=full.split(b'\n')
        physical_lines=[part+b'\n' for part in chunks[:-1]]
        if chunks[-1]:
            physical_lines.append(chunks[-1])
        expected=b''.join(physical_lines[start-1:end])
        need(ledger.read(S/'commands'/label/'stdout.raw','full actual extracted source output')==expected,
             'byte-exact historical sed output extent')
    for name in SCIENCE_PINS:
        ledger.pin(S/name,SCIENCE_PINS[name],'complete archived original scientific dependency')
    code=ledger.read(S/'pilot.c','source/declared box consistency').decode()
    need('for(unsigned n=1;n<=4;++n)' in code and 'static unsigned next[729]' in code,
         'pinned original source fixed parameter bounds')
    elf=ledger.read(S/'pilot','executed artifact metadata only')
    need(elf[:6]==b'\x7fELF\x02\x01' and struct.unpack_from('<H',elf,18)[0]==62,
         'preserved x86-64 little-endian ELF identity')
    phoff=struct.unpack_from('<Q',elf,32)[0]
    phsize,phnum=struct.unpack_from('<HH',elf,54)
    need(phsize>=56 and phoff+phsize*phnum<=len(elf),'complete ELF program headers')
    types=[struct.unpack_from('<I',elf,phoff+i*phsize)[0] for i in range(phnum)]
    need(2 not in types and 3 not in types,'no dynamic/interpreter program header in exact executed artifact')
    canonical=ledger.read(S/'CANONICAL.raw','complete canonical raw')
    need(canonical==ledger.read(S/'commands/10_pilot_a/stdout.raw','original run A raw')
         ==ledger.read(S/'commands/11_pilot_b/stdout.raw','original run B raw'),'full raw canonical equality')
    table=canonical_consistency(canonical)

    initial_order=list(inner)
    wrong_stdout=ledger.read(S/'postcheck/01_wrong_cwd_reproduction/stdout.raw','preserved native wrong-cwd stdout')
    wrong_stderr=ledger.read(S/'postcheck/01_wrong_cwd_reproduction/stderr.raw','preserved native wrong-cwd stderr')
    correct_stdout=ledger.read(S/'postcheck/02_correct_cwd/stdout.raw','preserved corrected-cwd stdout')
    need(wrong_stdout==''.join(n+': FAILED open or read\n' for n in initial_order).encode(),'all192 original wrong-cwd failure rows')
    need(correct_stdout==''.join(n+': OK\n' for n in initial_order).encode(),'all192 actual correct-cwd rows')
    need(wrong_stderr.count(b'No such file or directory')==192
         and b'192 listed files could not be read' in wrong_stderr,'complete wrong-cwd error census')
    transcription=ledger.read(S/'POSTCHECK_FAILURE_TRANSCRIPTION.md','initial actual tool failure transcription').decode()
    need('exit1' in transcription and 'truncated' in transcription and 'not a native receipt' in transcription,
         'first wrong-cwd failure remains a truncated tool transcription, not fabricated native raw')
    need(OLD_SEAL in transcription,'original seal fixed in first failure disclosure')
    old_closure=read_json(ledger,S/'commands/24_documentary_closure/stdout.raw','original documentary closure output')
    need(old_closure['completed_native_commands']==25 and old_closure['input_references']==7379
         and old_closure['distinct_current_input_paths']==1253
         and old_closure['refined_originals']==1219 and old_closure['canonical_lines']==845,
         'original closure retains its original scope/counts, not final scope')

    links=0
    for name in sorted(outer):
        if not name.endswith('.md') or name.startswith('controls/'):
            continue
        path=S/name
        for target in re.findall(r'\]\(([^)]+)\)',ledger.read(path,'scout local-link source').decode()):
            if target.startswith(('http://','https://','#')):
                continue
            literal=target.split('#',1)[0]
            if not literal:
                continue
            need(safe_relative(literal),'scout-owned local link syntax')
            resolved=path.parent/literal
            need(resolved in ledger.allowed and resolved.is_file(),'scout local link exact target')
            links+=1

    fresh_cmps=[]
    for left,right in [
        ('commands/10_pilot_a/stdout.raw','commands/11_pilot_b/stdout.raw'),
        ('commands/10_pilot_a/stdout.raw','CANONICAL.raw'),
        ('commands/11_pilot_b/stdout.raw','CANONICAL.raw')]:
        argv=['/usr/bin/cmp',str(S/left),str(S/right)]
        need(all(Path(p) in ledger.allowed for p in argv),'fresh comparator whitelist')
        r=subprocess.run(argv,cwd=ROOT,env={'PATH':'/usr/bin:/bin','LANG':'C','LC_ALL':'C','TZ':'UTC'},
                         stdin=subprocess.DEVNULL,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False)
        fresh_cmps.append({'argv':argv,'cwd':str(ROOT),'exit':r.returncode,
                           'stdout':r.stdout.decode('ascii'),'stderr':r.stderr.decode('utf-8'),
                           'scope':'Fresh raw comparison of existing outputs only, not producer execution'})
        need(r.returncode==0 and r.stdout==b'' and r.stderr==b'','fresh raw existing-output cmp')

    need(physical_census(S)==scout_census and physical_census(PREP)==own_census,'unchanged complete package path censuses')
    ledger.second_pass()
    permitted_historical={p for p in physical_inputs if p not in {str(ROOT/n) for n in PROTECTED}}
    need(len(permitted_historical)==1423 and permitted_historical<=set(ledger.before),
         'all1423 permitted normalized historical inputs read twice')
    need(not ({str(ROOT/n) for n in PROTECTED}&set(ledger.before)),'zero protected current-body reads')
    result={'schema':'scout33-root-documentary-check-v1',
            'status':'DOCUMENTARY_CHECK_COMPLETE_WITH_EIGHT_EXPLICIT_PROTECTED_CURRENT_HASH_SKIPS',
            'mathematical_acceptance':False,'scientific_producer_executions':0,
            'scout_final_seal':FINAL_SEAL,'scout_final_payloads':208,
            'scout_initial_seal':OLD_SEAL,'scout_initial_payloads':192,
            'physical_scout_files':209,'native_receipts':28,
            'historical_input_references_per_phase':7956,'historical_role_checks':15912,
            'normalized_historical_input_paths':1431,'permitted_historical_paths_twice':1423,
            'protected_current_bodies_not_read':protected_doc['protected_roles'],
            'control_aliases':[{'literal_old_path':n,'old_sha256':h,'physical_snapshot':str(S/c)}
                               for n,h,c in CONTROL_ROWS],
            'discovery_filename_count':5110,'selected_tier_counts':[1239,1227,1222,1219],
            'canonical_consistency_only':table,'local_links':links,
            'fresh_existing_output_raw_comparisons':fresh_cmps,
            'native_exit_census':dict(Counter(str(r['exit']) for r in receipts.values())),
            'wrong_cwd_failures':{'initial':'Tool transcription, exit1, original full raw not available',
                                  'reproduction':'Separate native full receipt, exit1',
                                  'corrected':'Separate native full receipt, exit0'},
            'current_read_path_count':len(ledger.before),
            'current_read_columns':['literal_current_path','resolved_path_if_different',
                                    'bytes_before','sha256_before','bytes_after','sha256_after'],
            'current_reads_twice':[[name,
                 before['resolved_path'] if before['resolved_path']!=name else '',
                 before['bytes'],before['sha256'],ledger.after[name]['bytes'],ledger.after[name]['sha256']]
                 for name,before in sorted(ledger.before.items())],
            'historical_roles_complete_canonical_sha256':sha256(json.dumps(all_roles,sort_keys=True,separators=(',',':')).encode()).hexdigest(),
            'historical_role_records':[{'directory':name,'input_count':rec['input_count'],
                 'before_record_sha256':sha256(ledger.cache[S/name/'inputs_before.json']).hexdigest(),
                 'after_record_sha256':sha256(ledger.cache[S/name/'inputs_after.json']).hexdigest()}
                 for name,rec in sorted(receipts.items())],
            'documentary_checks':checks,
            'boundary':'Root must separately handle the eight fixed protected current hashes and original mathematical/source/code acceptance. This checker never computes or runs OTC, fetches sources, imports scout code, changes any file or certifies a paper.'}
    print(json.dumps(result,sort_keys=True,separators=(',',':')))


if __name__=='__main__':
    main()
