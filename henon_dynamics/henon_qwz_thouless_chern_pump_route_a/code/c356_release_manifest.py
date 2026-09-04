#!/usr/bin/env python3
"""Deterministic 27-payload release gate for HCS-C356."""
from __future__ import annotations
import argparse, hashlib, json, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; MAN=ROOT/'C356_RELEASE_MANIFEST.json'; EV=ROOT/'results/c356_qwz_evidence.json'; TEX=ROOT/'paper/main.tex'; MAIN=ROOT/'paper/main.pdf'; COMPILE_REPORT=ROOT/'paper/COMPILE_REPORT.md'
YML=ROOT/'evaluations/route_a/HCS-C356/2026-09-03.yaml'; RAW='65ca3b4edca93782ccf74b735a103dc1728c3f9ed33b74259c666a9becf1775c'; SEM='38b482ef987c719deda54769345e813b350a8103ba24e03277729292977a2b17'
SOURCE='140c8714b74de666d56f441ddfb712026955901a'; SCOPE='NO_BAD_EULER_OR_ROOT_NUMBER'; EPOCH=1788393600
ROUNDS=[ROOT/'paper/main_round0_original.pdf',ROOT/'paper/main_round1.pdf',ROOT/'paper/main_round2.pdf']
WARN=re.compile(r'(?:LaTeX|Package [^:\n]+) Warning:|warning  \(pdf backend\)|Overfull|Underfull|undefined (?:references|citations)|Rerun to get|Missing character')
EXPECTED={'EXPERIMENT_PLAN.md','NARRATIVE_REPORT.md','PAPER_IMPROVEMENT_LOG.md','PAPER_PLAN.md','README.md','RESEARCH_QUESTION.md','SOURCE_AUDIT.md','THEOREM_PACKAGE.md','code/README.md','code/c356_release_manifest.py','code/c356_qwz_checker.py','code/c356_qwz_mutation.py','code/c356_qwz_producer.py','code/c356_qwz_replay.py','code/c356_qwz_sympy_crosscheck.py','evaluations/route_a/HCS-C356/2026-09-03.yaml','paper/COMPILE_REPORT.md','paper/README.md','paper/main.pdf','paper/main.tex','paper/main_round0_original.pdf','paper/main_round1.pdf','paper/main_round2.pdf','results/HOSTILE_AUDIT.md','results/RESULTS.md','results/TEST_REPORT.md','results/c356_qwz_evidence.json'}
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
def lane(name):
 env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',TZ='UTC'); cmd=[sys.executable,'-B',str(ROOT/'code'/name)]
 with tempfile.TemporaryDirectory(prefix='c356-lane-') as d:
  if name=='c356_qwz_producer.py': cmd+=['--output',str(Path(d)/'evidence.json')]
  return subprocess.check_output(cmd,env=env,text=True).strip()
def optimized(name):
 env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',TZ='UTC')
 for flag in ('-O','-OO'):
  cmd=[sys.executable,flag,'-B',str(ROOT/'code'/name)]
  with tempfile.TemporaryDirectory(prefix='c356-opt-') as d:
   if name=='c356_qwz_producer.py': cmd+=['--output',str(Path(d)/'x.json')]
   p=subprocess.run(cmd,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
  if p.returncode==0 or 'refuses optimized Python' not in p.stdout: raise AssertionError(f'optimized execution not refused: {flag} {name}')
def fresh(round_number):
 with tempfile.TemporaryDirectory(prefix=f'c356-build-{round_number}-') as d:
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
 with tempfile.TemporaryDirectory(prefix='c356-raster-') as d:
  for page in range(1,np+1):
   pre=Path(d)/f'p{page}'; subprocess.run(['pdftoppm','-f',str(page),'-l',str(page),'-r','72','-png',str(p),str(pre)],check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
   ims=list(Path(d).glob(f'p{page}-*.png'))
   if len(ims)!=1 or ims[0].stat().st_size<1000: raise AssertionError('raster failure')
   sizes.append(ims[0].stat().st_size)
 return txt,sizes
def build_pdfs():
 for i,p in enumerate(ROUNDS):
  a=fresh(i); b=fresh(i)
  if a!=b: raise AssertionError('nondeterministic PDF')
  p.write_bytes(a)
 MAIN.write_bytes(ROUNDS[2].read_bytes())
def payload_hash():
 x=strict_json(EV); claimed=x.pop('payload_sha256'); got=hashlib.sha256(canonical(x)).hexdigest()
 if claimed!=got: raise AssertionError('stale evidence payload hash')
 return claimed
def make_manifest(outputs):
 src=TEX.read_text()
 for token in (r'G(m)=2\min',r'\operatorname{sgn}(m+2)',r'K H_m(k,\tau)K=H_m(k,-\tau)','no exact finite-driving-rate quantization','Dirac-monopole sphere','magnetic spectrum','Route B remains locked'):
  if token not in src: raise AssertionError(f'missing theorem token: {token}')
 if re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]',src) or re.search(r'(?<!\\)qquad',src): raise AssertionError('TeX hygiene failure')
 files={str(p.relative_to(ROOT)):p for p in ROOT.rglob('*') if p.is_file() and p!=MAN}
 if set(files)!=EXPECTED or len(files)!=27: raise AssertionError(f'ledger mismatch missing={sorted(EXPECTED-set(files))} extra={sorted(set(files)-EXPECTED)}')
 if sha(YML)!=RAW: raise AssertionError('YAML raw drift')
 report=COMPILE_REPORT.read_text()
 for p in ROUNDS:
  if sha(p) not in report: raise AssertionError(f'compile report lacks current PDF digest: {p.name}')
 checker=(ROOT/'code/c356_qwz_checker.py').read_text()
 if re.search(r'(?:from|import)\s+[^\n]*c356_qwz_producer',checker): raise AssertionError('checker imports producer')
 tokens=('exact bloch-gap owner','analytic dirac-degree owner','adiabatic scope and route firewall'); pdf=[]
 for i,p in enumerate(ROUNDS):
  np=pages(p); txt,ras=text_and_raster(p,np)
  if tokens[i] not in txt: raise AssertionError(f'round token missing {i}')
  if i==2 and ('finite driving rate' not in txt or 'route b remains locked' not in txt): raise AssertionError('final scope sentinel')
  pdf.append({'round':i,'path':str(p.relative_to(ROOT)),'sha256':sha(p),'bytes':p.stat().st_size,'pages':np,'font_rows':fonts(p),'raster_bytes':ras})
 if len({x['sha256'] for x in pdf})!=3 or MAIN.read_bytes()!=ROUNDS[2].read_bytes(): raise AssertionError('revision PDF closure')
 e=strict_json(EV)
 if e['source_commit']!=SOURCE or e['scope_literal']!=SCOPE or e['route_a']!={'tuple':['A0_FAIL','A1_FAIL','A2_FAIL','A3_FAIL','A4_NATURAL_QUANTIZATION'],'overall':'ROUTE_A_REJECTED','route_b_invocation_allowed':False}: raise AssertionError('evidence metadata drift')
 return {'schema':'hcs-release-manifest-v1','candidate_id':'HCS-C356','obstruction_id':'HEN-O340','source_commit':SOURCE,'fixed_epoch':EPOCH,'scope_literal':SCOPE,'evaluator_authority':'flow_systems/skills/route-a-evaluator.md','evaluator_version':'0.2.0','evaluator_authority_sha256':'6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c','payload_file_count':27,'physical_file_count':28,'evaluation_raw_sha256':RAW,'evaluation_semantic_sha256':SEM,'evidence_sha256':sha(EV),'evidence_payload_sha256':payload_hash(),'release_lanes':{'producer':'PASS','independent_checker':'PASS','sympy_crosscheck':'PASS','isolated_byte_replay':'PASS','hostile_mutation':'PASS','optimized_mode_refusal':'PASS','deterministic_pdf_rebuild':'PASS','payload_membership':'PASS'},'pdf_rounds':pdf,'main_pdf_sha256':sha(MAIN),'files':{n:sha(p) for n,p in sorted(files.items())}}
def main():
 if sys.flags.optimize: raise RuntimeError('C356 release refuses optimized Python')
 ap=argparse.ArgumentParser(); ap.add_argument('--write',action='store_true'); ap.add_argument('--build-pdfs',action='store_true'); a=ap.parse_args()
 lanes=[('c356_qwz_producer.py','C356_PRODUCER_PASS'),('c356_qwz_checker.py','C356 independent QWZ checker: PASS'),('c356_qwz_sympy_crosscheck.py','C356 SymPy cross-check: PASS'),('c356_qwz_replay.py','C356 byte replay: PASS'),('c356_qwz_mutation.py','C356 hostile mutation suite: PASS')]; outputs={}
 for name,sentinel in lanes:
  out=lane(name)
  if sentinel not in out: raise AssertionError(f'lane sentinel missing {name}')
  outputs[name]=out; optimized(name)
 if a.build_pdfs: build_pdfs()
 for i,p in enumerate(ROUNDS):
  first=fresh(i); second=fresh(i)
  if first!=second or first!=p.read_bytes(): raise AssertionError(f'stale/nondeterministic round {i}')
 manifest=make_manifest(outputs); raw=json.dumps(manifest,sort_keys=True,indent=2,ensure_ascii=False)+'\n'
 if a.write: MAN.write_text(raw)
 elif not MAN.exists() or MAN.read_text()!=raw: raise AssertionError('manifest missing or stale')
 bad=[p for p in ROOT.rglob('*') if p.is_file() and (p.suffix in {'.aux','.log','.out','.toc','.pyc'} or '__pycache__' in p.parts)]
 if bad: raise AssertionError(f'forbidden sidecars: {bad}')
 print(f'C356_RELEASE_PASS {sha(EV)} {sha(MAIN)} {sha(MAN)}')
if __name__=='__main__': main()
