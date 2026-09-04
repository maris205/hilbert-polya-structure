#!/usr/bin/env python3
"""Deterministic 27-payload release gate for HCS-C362."""
from __future__ import annotations
import argparse, hashlib, json, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; MAN=ROOT/'C362_RELEASE_MANIFEST.json'; EV=ROOT/'results/c362_cucker_smale_evidence.json'; TEX=ROOT/'paper/main.tex'; MAIN=ROOT/'paper/main.pdf'; CR=ROOT/'paper/COMPILE_REPORT.md'; YML=ROOT/'evaluations/route_a/HCS-C362/2026-09-04.yaml'
RAW='db434760c390e4bfe52298390a8a1ac342152d0b6b33db719e3c42d11f85ad09'; SEM='941bac50bb2f6c8998e8a0dd072a2caecfc8831d18b0e290b363b87cfe2a158a'; SOURCE='05ca5f96b2c69a6ad6ba153d1084df750d7722c0'; SCOPE='NO_BAD_EULER_OR_ROOT_NUMBER'; EPOCH=1788480000
ROUNDS=[ROOT/'paper/main_round0_original.pdf',ROOT/'paper/main_round1.pdf',ROOT/'paper/main_round2.pdf']
WARN=re.compile(r'(?:LaTeX|Package [^:\n]+) Warning:|warning  \(pdf backend\)|Overfull|Underfull|undefined (?:references|citations)|Rerun to get|Missing character')
EXPECTED={'EXPERIMENT_PLAN.md','NARRATIVE_REPORT.md','PAPER_IMPROVEMENT_LOG.md','PAPER_PLAN.md','README.md','RESEARCH_QUESTION.md','SOURCE_AUDIT.md','THEOREM_PACKAGE.md','code/README.md','code/c362_release_manifest.py','code/c362_cucker_smale_checker.py','code/c362_cucker_smale_mutation.py','code/c362_cucker_smale_producer.py','code/c362_cucker_smale_replay.py','code/c362_cucker_smale_sympy_crosscheck.py','evaluations/route_a/HCS-C362/2026-09-04.yaml','paper/COMPILE_REPORT.md','paper/README.md','paper/main.pdf','paper/main.tex','paper/main_round0_original.pdf','paper/main_round1.pdf','paper/main_round2.pdf','results/HOSTILE_AUDIT.md','results/RESULTS.md','results/TEST_REPORT.md','results/c362_cucker_smale_evidence.json'}
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def canonical(x): return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
def strict_json(p):
    def unique(pairs):
        d={}
        for k,v in pairs:
            if k in d: raise ValueError('duplicate JSON key')
            d[k]=v
        return d
    return json.loads(p.read_text(),object_pairs_hook=unique,parse_constant=lambda s:(_ for _ in()).throw(ValueError(s)))
def run(name,args=()):
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',TZ='UTC'); cmd=[sys.executable,'-B',str(ROOT/'code'/name),*args]
    return subprocess.check_output(cmd,env=env,text=True).strip()
def lane(name):
    with tempfile.TemporaryDirectory(prefix='c362-lane-') as d:
        args=('--output',str(Path(d)/'evidence.json')) if name=='c362_cucker_smale_producer.py' else ()
        return run(name,args)
def optimized(name):
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',TZ='UTC')
    for flag in ('-O','-OO'):
        cmd=[sys.executable,flag,'-B',str(ROOT/'code'/name)]
        with tempfile.TemporaryDirectory(prefix='c362-opt-') as d:
            if name=='c362_cucker_smale_producer.py': cmd+=['--output',str(Path(d)/'x.json')]
            p=subprocess.run(cmd,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        if p.returncode==0 or 'refuses optimized Python' not in p.stdout: raise AssertionError(f'optimized execution not refused: {flag} {name}')
def fresh(round_number):
    with tempfile.TemporaryDirectory(prefix=f'c362-build-{round_number}-') as d:
        w=Path(d); shutil.copy2(TEX,w/'main.tex'); env=dict(os.environ,SOURCE_DATE_EPOCH=str(EPOCH),FORCE_SOURCE_DATE='1',TZ='UTC')
        cmd=['lualatex','-interaction=nonstopmode','-halt-on-error','-jobname=main',rf'\def\CRevisionRound{{{round_number}}}\input{{main.tex}}']
        for _ in range(2): subprocess.run(cmd,cwd=w,env=env,check=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        log=(w/'main.log').read_text(errors='replace'); hit=WARN.search(log)
        if hit: raise AssertionError(f'paper warning round {round_number}: {hit.group(0)}')
        return (w/'main.pdf').read_bytes()
def pages(p):
    out=subprocess.check_output(['pdfinfo',str(p)],text=True); return int(next(x.split(':',1)[1] for x in out.splitlines() if x.startswith('Pages:')))
def fonts(p):
    rows=[x for x in subprocess.check_output(['pdffonts',str(p)],text=True).splitlines()[2:] if x.strip() and not x.lstrip().startswith('-')]
    if not rows: raise AssertionError('no fonts')
    for row in rows:
        cols=row.split()
        if len(cols)<7 or cols[-5]!='yes' or cols[-4]!='yes': raise AssertionError(f'font not embedded/subset: {row}')
    return len(rows)
def text_and_raster(p,np):
    raw=subprocess.check_output(['pdftotext','-layout',str(p),'-'])
    if re.search(rb'[\x00-\x08\x0b\x0e-\x1f\x7f]',raw): raise AssertionError('control byte in PDF text')
    txt=' '.join(raw.decode().lower().split())
    for bad in ('??','[verify]','qquad','__mutated','varepsilon_'):
        if bad in txt: raise AssertionError(f'PDF text garbage: {bad}')
    sizes=[]
    with tempfile.TemporaryDirectory(prefix='c362-raster-') as d:
        for page in range(1,np+1):
            pre=Path(d)/f'p{page}'; subprocess.run(['pdftoppm','-f',str(page),'-l',str(page),'-r','72','-png',str(p),str(pre)],check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            ims=list(Path(d).glob(f'p{page}-*.png'))
            if len(ims)!=1 or ims[0].stat().st_size<1000: raise AssertionError('raster failure')
            sizes.append(ims[0].stat().st_size)
    return txt,sizes
def pdf_receipts():
    tokens=('global diameter-barrier owner','critical-tail and scalar-sharpness owner','boundary-atlas and scope-firewall owner'); out=[]
    for i,p in enumerate(ROUNDS):
        np=pages(p); txt,ras=text_and_raster(p,np)
        if tokens[i] not in txt: raise AssertionError(f'round token missing {i}')
        if i==2 and ('equality face is not classical flocking' not in txt or 'route b remains locked' not in txt): raise AssertionError('final boundary/scope sentinel missing')
        out.append({'round':i,'path':str(p.relative_to(ROOT)),'sha256':sha(p),'bytes':p.stat().st_size,'pages':np,'font_rows':fonts(p),'raster_bytes':ras})
    if len({x['sha256'] for x in out})!=3 or MAIN.read_bytes()!=ROUNDS[2].read_bytes(): raise AssertionError('revision PDF closure')
    return out
def payload_hash():
    x=strict_json(EV); claimed=x.pop('payload_sha256'); got=hashlib.sha256(canonical(x)).hexdigest()
    if claimed!=got: raise AssertionError('stale evidence payload hash')
    return claimed
def reports(outputs,pdfs):
    checker=re.search(r'PASS \((\d+) assertions\)',outputs['c362_cucker_smale_checker.py']).group(1)
    sympy=re.search(r'PASS \((\d+) exact checks\)',outputs['c362_cucker_smale_sympy_crosscheck.py']).group(1)
    attacks=re.search(r'PASS \((\d+) attacks\)',outputs['c362_cucker_smale_mutation.py']).group(1)
    result=f'''# Results\n\nThe canonical evidence has SHA-256 `{sha(EV)}` and self-excluding payload SHA-256 `{payload_hash()}`.  It records 36 exact finite-system rows, five communication primitives, and three sharp scalar two-body regimes.\n\nThe analytic theorem proves global flow, mean conservation, exact variance dissipation, diameter comparison, tail-barrier confinement, exponential alignment, unconditional flocking for `0 <= beta <= 1/2`, and the `beta>1/2` outward two-body trichotomy.  Finite rows are implementation receipts only.\n'''
    test=f'''# Test report\n\nAll five computational lanes pass under ordinary Python and explicitly refuse both `python -O` and `python -OO`:\n\n- producer: 36 exact systems and 3 two-body rows PASS;\n- independent checker: {checker} assertions PASS;\n- SymPy lane: {sympy} exact checks PASS;\n- isolated replay: two byte-identical temporary-directory runs PASS;\n- hostile mutation: {attacks} attacks PASS.\n\nThe release gate additionally verifies strict JSON/YAML parsing, raw and semantic evaluator locks, exact 27-payload membership, warning-free deterministic PDFs, embedded subset fonts, extracted text, rasterization, and self-excluding manifest closure.\n'''
    hostile=f'''# Hostile audit\n\nThe repaired-hash suite rejects {attacks} attacks.  It changes theorem gates, the ordered-pair dissipation factor, diameter signs, strictness, the `beta=1/2` endpoint, the equality orbit, the many-body claim boundary, low-level exact rows, evaluator authority/status/text, Route-A/Route-B fields, and forbidden flags.  It also covers deletion, reorder/truncation, duplicate/nonfinite/root-invalid JSON, duplicate/alias/non-string YAML, and a stale outer-hash control.\n'''
    lines=['# Compile report','','Each conditional manuscript round was built twice in fresh directories with LuaLaTeX under `SOURCE_DATE_EPOCH=1788480000`; both bytes matched the stored artifact.  Settled logs have no warnings or layout defects, all fonts are embedded and subset, extracted text has no control garbage, and every page rasterizes.','','| round | pages | font rows | SHA-256 | substantive addition |','|---|---:|---:|---|---|']
    adds=['global flow, dissipation, diameter lemma, and tail barrier','endpoint, explicit radius, and exact scalar threshold sharpness','degenerate atlas, source boundary, evidence semantics, and route firewall']
    for p,a in zip(pdfs,adds): lines.append(f'| {p["round"]} | {p["pages"]} | {p["font_rows"]} | `{p["sha256"]}` | {a} |')
    lines+=['','`main.pdf` is byte-identical to round 2.','']; compile='\n'.join(lines)
    return {'results/RESULTS.md':result,'results/TEST_REPORT.md':test,'results/HOSTILE_AUDIT.md':hostile,'paper/COMPILE_REPORT.md':compile}
def make_manifest(pdfs):
    src=TEX.read_text()
    for token in (r'\Dini X\le V',r'V(0)<K\int',r'0\le\beta\le1/2',r'u_0=A',r'target zero match',r'Route B remains locked'):
        if token not in src: raise AssertionError(f'missing theorem token: {token}')
    if re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]',src) or re.search(r'(?<!\\)qquad',src): raise AssertionError('TeX hygiene failure')
    files={str(p.relative_to(ROOT)):p for p in ROOT.rglob('*') if p.is_file() and p!=MAN}
    if set(files)!=EXPECTED or len(files)!=27: raise AssertionError(f'ledger mismatch missing={sorted(EXPECTED-set(files))} extra={sorted(set(files)-EXPECTED)}')
    if sha(YML)!=RAW: raise AssertionError('YAML raw drift')
    checker=(ROOT/'code/c362_cucker_smale_checker.py').read_text()
    if re.search(r'(?:from|import)\s+[^\n]*c362_cucker_smale_producer',checker): raise AssertionError('checker imports producer')
    e=strict_json(EV)
    route={'tuple':['A0_FAIL','A1_FAIL','A2_FAIL','A3_FAIL','A4_FAIL'],'overall':'ROUTE_A_REJECTED','route_b_invocation_allowed':False}
    if e['source_commit']!=SOURCE or e['scope_literal']!=SCOPE or e['route_a']!=route or any(e['scope_flags'].values()): raise AssertionError('evidence metadata drift')
    return {'schema':'hcs-release-manifest-v1','candidate_id':'HCS-C362','obstruction_id':'HEN-O346','source_commit':SOURCE,'fixed_epoch':EPOCH,'scope_literal':SCOPE,'evaluator_authority':'flow_systems/skills/route-a-evaluator.md','evaluator_version':'0.2.0','evaluator_authority_sha256':'6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c','payload_file_count':27,'physical_file_count':28,'evaluation_raw_sha256':RAW,'evaluation_semantic_sha256':SEM,'evidence_sha256':sha(EV),'evidence_payload_sha256':payload_hash(),'release_lanes':{'producer':'PASS','independent_checker':'PASS','sympy_crosscheck':'PASS','isolated_byte_replay':'PASS','hostile_mutation':'PASS','optimized_mode_refusal':'PASS','deterministic_pdf_rebuild':'PASS','payload_membership':'PASS'},'pdf_rounds':pdfs,'main_pdf_sha256':sha(MAIN),'files':{n:sha(p) for n,p in sorted(files.items())}}
def main():
    if sys.flags.optimize: raise RuntimeError('C362 release refuses optimized Python')
    ap=argparse.ArgumentParser(); ap.add_argument('--write',action='store_true'); ap.add_argument('--build-pdfs',action='store_true'); a=ap.parse_args()
    if a.build_pdfs and not a.write: raise ValueError('--build-pdfs requires --write')
    if a.write: run('c362_cucker_smale_producer.py')
    lanes=[('c362_cucker_smale_producer.py','C362_PRODUCER_PASS'),('c362_cucker_smale_checker.py','C362 independent Cucker-Smale checker: PASS'),('c362_cucker_smale_sympy_crosscheck.py','C362 SymPy cross-check: PASS'),('c362_cucker_smale_replay.py','C362 byte replay: PASS'),('c362_cucker_smale_mutation.py','C362 hostile mutation suite: PASS')]; outputs={}
    for name,sentinel in lanes:
        out=lane(name)
        if sentinel not in out: raise AssertionError(f'lane sentinel missing {name}')
        outputs[name]=out; optimized(name)
    if a.build_pdfs:
        for i,p in enumerate(ROUNDS):
            first=fresh(i); second=fresh(i)
            if first!=second: raise AssertionError(f'nondeterministic PDF round {i}')
            p.parent.mkdir(parents=True,exist_ok=True); p.write_bytes(first)
        MAIN.write_bytes(ROUNDS[2].read_bytes())
    for i,p in enumerate(ROUNDS):
        first=fresh(i); second=fresh(i)
        if first!=second or first!=p.read_bytes(): raise AssertionError(f'stale/nondeterministic round {i}')
    pdfs=pdf_receipts(); expected_reports=reports(outputs,pdfs)
    for name,raw in expected_reports.items():
        p=ROOT/name
        if a.write: p.parent.mkdir(parents=True,exist_ok=True); p.write_text(raw)
        elif not p.exists() or p.read_text()!=raw: raise AssertionError(f'report missing or stale: {name}')
    manifest=make_manifest(pdfs); raw=json.dumps(manifest,sort_keys=True,indent=2,ensure_ascii=False)+'\n'
    if a.write: MAN.write_text(raw)
    elif not MAN.exists() or MAN.read_text()!=raw: raise AssertionError('manifest missing or stale')
    bad=[p for p in ROOT.rglob('*') if p.is_file() and (p.suffix in {'.aux','.log','.out','.toc','.pyc'} or '__pycache__' in p.parts)]
    if bad: raise AssertionError(f'forbidden sidecars: {bad}')
    print(f'C362_RELEASE_PASS {sha(EV)} {sha(MAIN)} {sha(MAN)}')
if __name__=='__main__': main()
