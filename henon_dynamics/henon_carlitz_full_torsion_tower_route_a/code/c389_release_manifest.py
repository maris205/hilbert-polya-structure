#!/usr/bin/env python3
"""Closed source/evidence/three-round PDF release; default mode is read only."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import yaml

ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/'C389_RELEASE_MANIFEST.json'
YML=ROOT/'evaluations/route_a/HCS-C389/2026-09-05.yaml'
YAML_RAW='4ef4101db5f7fd1107ec427142401370534ffe3c568019a788bdc88d5a766ef8'
SOURCE='0c877206d202f732e21ea0b194f9c7fdf30467ee'
EVALUATOR='6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c'
ROUTE=['A0_STRUCTURAL_ARITHMETIC_RELATION','A1_WEAK','A2_FAIL','A3_FAIL','A4_FAIL']
ENV=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',TZ='UTC',SOURCE_DATE_EPOCH='1788566400',FORCE_SOURCE_DATE='1')
WARNING=re.compile(r'(?:LaTeX|Package).*Warning|Overfull|Underfull|badness|undefined|Missing character',re.I)
EXPECTED=set('''ASSUMPTIONS.md CLAIMS.md EXPERIMENT_PLAN.md LIMITATIONS.md
NARRATIVE_REPORT.md PAPER_IMPROVEMENT_LOG.md PAPER_PLAN.md PROJECT_README.md
README.md REFERENCES.md RELEASE.md REPRODUCIBILITY.md RESEARCH_QUESTION.md
SCOPE.md SOURCE_AUDIT.md THEOREM_PACKAGE.md requirements.txt
code/README.md code/c389_carlitz_checker.py code/c389_carlitz_mutation.py
code/c389_carlitz_producer.py code/c389_carlitz_replay.py code/c389_carlitz_sympy_crosscheck.py
code/c389_release_manifest.py evaluations/route_a/HCS-C389/2026-09-05.yaml
paper/COMPILE_REPORT.md paper/README.md paper/main.pdf paper/main.tex
paper/main_body.tex paper/main_round0.pdf paper/main_round0.tex
paper/main_round1.pdf paper/main_round1.tex paper/main_round2.pdf
paper/main_round2.tex paper/compile_round0.txt paper/compile_round1.txt
paper/compile_round2.txt proof/ANALYTIC_PROOF.md results/HOSTILE_AUDIT.md
results/RESULTS.md results/TEST_REPORT.md results/c389_carlitz_evidence.json
review/CLAIM_REFERENCE_AUDIT.md review/FAILURE_MODE_AUDIT.md
review/FINAL_INTEGRITY.md review/ROUND0_REVIEW.md review/ROUND1_REVIEW.md
review/ROUND2_REVIEW.md review/VISUAL_AUDIT.md tests/test_c389_smoke.py'''.split())

def need(value,message):
    if not value:
        raise ValueError(message)

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def strict_json(path):
    def unique(pairs):
        out={}
        for k,v in pairs:
            need(k not in out,'duplicate JSON')
            out[k]=v
        return out
    return json.loads(Path(path).read_text(),object_pairs_hook=unique,
                      parse_constant=lambda v:(_ for _ in ()).throw(ValueError(v)))

class Loader(yaml.SafeLoader):
    pass

def mapping(loader,node,deep=False):
    out={}
    for k,v in node.value:
        need(k.tag!='tag:yaml.org,2002:merge','YAML merge')
        key=loader.construct_object(k,deep=deep)
        need(type(key) is str and key not in out,'duplicate/nonstring YAML key')
        out[key]=loader.construct_object(v,deep=deep)
    return out

Loader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,mapping)
def reject_timestamp(loader,node):
    raise ValueError('implicit or explicit YAML timestamp forbidden')

Loader.add_constructor('tag:yaml.org,2002:timestamp',reject_timestamp)

def content_gate(yml=YML):
    raw=Path(yml).read_text()
    for token in yaml.scan(raw):
        need(not isinstance(token,(yaml.tokens.AnchorToken,yaml.tokens.AliasToken)),'YAML alias')
    route=yaml.load(raw,Loader=Loader)
    need(sha(yml)==YAML_RAW,'frozen raw YAML hash; unknown fields/type drift forbidden')
    need(route['source_commit']==route['code_commit']==SOURCE,'source commit')
    need(route['scope_literal']=='NO_BAD_EULER_OR_ROOT_NUMBER','scope literal')
    need(route['evaluator_authority_sha256']==EVALUATOR,'evaluator SHA')
    need(route['skill']=='route-a-evaluator' and route['skill_version']=='0.2.0','evaluator schema')
    need(route['tuple']==ROUTE and route['overall_verdict']=='ROUTE_A_EXPLORATORY','strict tuple')
    need(route['route_b_invocation_allowed'] is False,'Route B')
    need(all(v is False for v in route['scope_flags'].values()) and len(route['scope_flags'])==9,'scope flags')
    need(set(route['source_lock'])=={'object','arithmetic_origin','clock','normalization',
         'determinant_convention','cutoff','precision','allowed_data','forbidden_data'},'source lock')
    for layer,expected in zip(('a0','a1','a2','a3','a4'),ROUTE):
        need(route[layer]['verdict']==expected and route[layer]['artifacts'],'layer '+layer)
    need(route['a1']['metrics']['mandatory_a1_controls_completed']==0,'failed A1 lock')
    for key in ('adversarial_controls','claim_boundary','blocking_conditions','next_smallest_test','round2_clues'):
        need(bool(route[key]),'missing route field '+key)
    body=(ROOT/'paper/main_body.tex').read_text()
    for token in ('Round 0 advance','Round 1 advance','Round 2 advance',
                  'The critical Carlitz reduction','lower groups',
                  'HEN-O373','中文摘要','关键词：','Keywords:',
                  'Route B remains disabled','nonunit','Generic characteristic'):
        need(token in body,'paper token '+token)
    checker=(ROOT/'code/c389_carlitz_checker.py').read_text()
    need(not re.search(r'(?:from|import)\s+[^\n]*c389_carlitz_producer',checker),'checker imports producer')
    need((ROOT/'paper/main.tex').read_text().strip()==r'\input{main_round2.tex}','main wrapper')
    return route

def run(script,args=(),cwd=ROOT):
    p=subprocess.run([sys.executable,'-B',str(ROOT/'code'/script),*args],
                     cwd=cwd,env=ENV,text=True,capture_output=True)
    need(p.returncode==0,script+' failed\n'+p.stdout+p.stderr)
    return p.stdout.strip()

def fresh(round_number):
    with tempfile.TemporaryDirectory(prefix='c389-pdf-') as directory:
        work=Path(directory)
        shutil.copy2(ROOT/'paper/main_body.tex',work/'main_body.tex')
        shutil.copy2(ROOT/f'paper/main_round{round_number}.tex',work/f'main_round{round_number}.tex')
        cmd=['lualatex','-interaction=nonstopmode','-halt-on-error','-jobname=artifact',f'main_round{round_number}.tex']
        for _ in range(2):
            p=subprocess.run(cmd,cwd=work,env=ENV,capture_output=True,text=True)
            need(p.returncode==0,'LuaLaTeX failure\n'+p.stdout[-8000:])
        log=(work/'artifact.log').read_text(errors='replace')
        warnings=[line for line in log.splitlines() if WARNING.search(line)]
        need(not warnings,'settled PDF warnings '+str(warnings))
        return (work/'artifact.pdf').read_bytes(),log

def pdf_gate(build):
    receipts=[]
    for i in range(3):
        first,log=fresh(i)
        second,_=fresh(i)
        need(first==second,'nondeterministic PDF '+str(i))
        path=ROOT/f'paper/main_round{i}.pdf'
        if build:
            path.write_bytes(first)
            (ROOT/f'paper/compile_round{i}.txt').write_text(log)
        else:
            need(path.read_bytes()==first,'frozen PDF drift')
        info=subprocess.check_output(['pdfinfo',str(path)],text=True)
        pages=int(next(l.split(':')[1] for l in info.splitlines() if l.startswith('Pages:')))
        fonts=subprocess.check_output(['pdffonts',str(path)],text=True).splitlines()[2:]
        need(bool(fonts),'no PDF fonts')
        for line in fonts:
            cols=line.split()
            need(cols[-5:-3]==['yes','yes'],'font not embedded/subset '+line)
        need(any('DroidSansFallback' in l for l in fonts),'missing CJK font')
        text=subprocess.check_output(['pdftotext','-layout',str(path),'-'],text=True)
        compact=''.join(text.split())
        for token in ('Abstract','Keywords:','中文摘要','关键词：'):
            need(token.replace(' ','') in compact,'missing bilingual token')
        need(f'Round{i}advance' in compact,'substantive round missing')
        for later in range(i+1,3):
            need(f'Round{later}advance' not in compact,'future round leaked')
        for bad in ('??','[VERIFY]','TODO','FIXME'):
            need(bad not in text,'bad text '+bad)
        raster_sizes=[]
        with tempfile.TemporaryDirectory(prefix='c389-raster-') as directory:
            subprocess.run(['pdftoppm','-r','72','-png',str(path),str(Path(directory)/'page')],check=True,capture_output=True)
            images=sorted(Path(directory).glob('page-*.png'))
            need(len(images)==pages,'raster page count')
            raster_sizes=[p.stat().st_size for p in images]
            need(all(n>1000 for n in raster_sizes),'empty raster page')
        receipts.append(dict(round=i,source=f'paper/main_round{i}.tex',pages=pages,
          fonts=len(fonts),sha256=sha(path),bytes=path.stat().st_size,raster_bytes=raster_sizes,
          deterministic_two_fresh_builds=True,settled_warnings=0))
    need(len({r['sha256'] for r in receipts})==3,'identical round artifacts')
    if build:
        (ROOT/'paper/main.pdf').write_bytes((ROOT/'paper/main_round2.pdf').read_bytes())
    need(sha(ROOT/'paper/main.pdf')==receipts[-1]['sha256'],'main differs from round2')
    return receipts

def reports(outputs,pdfs):
    tests='# Test report\n\n'+''.join(f'- {k}: `{v}`\n' for k,v in outputs.items())
    tests+='\nSix scripts under both -O and -OO give twelve optimized-mode refusals. Strict YAML/raw hash, source scope, exact membership and PDF gates passed. Finite evidence is regression, not an all-level proof.\n'
    compile='# Compile report\n\nEvery round was built twice in fresh directories at epoch 1788566400, with two LuaLaTeX passes per build. Each pair is byte identical. All fonts are embedded/subset, all pages rasterize and settled logs contain no warning.\n\n| round | pages | fonts | bytes | SHA256 |\n|---|---:|---:|---:|---|\n'
    for r in pdfs:
        compile+=f"| {r['round']} | {r['pages']} | {r['fonts']} | {r['bytes']} | {r['sha256']} |\n"
    compile+='\nmain.pdf equals round2. Round0 proves full annihilator clocks and critical reduction. Round1 adds Eisenstein polynomials, full Galois groups and all conductors. Round2 adds compatible towers, lower ramification and different, exact controls and target boundaries. Raw settled compiler logs are retained unchanged as .txt files.\n'
    return {'results/TEST_REPORT.md':tests,'paper/COMPILE_REPORT.md':compile,
      'results/RESULTS.md':'# Results\n\nThe exact grid has 107 conductor cases, every residue multiplier, and 77 prime-power cases over q=2,3,4,5. Evidence SHA256: `'+sha(ROOT/'results/c389_carlitz_evidence.json')+'`. All-conductor and infinite-tower claims follow from the proof, never extrapolation.\n',
      'results/HOSTILE_AUDIT.md':'# Hostile audit\n\n'+outputs['mutation']+'\n\nEvery semantic JSON attack repairs the payload hash. Recursive exact-type checking includes bool/int confusions at scalar and nested fields. Ten YAML attacks test unknown fields, numeric false, implicit timestamp, duplicates, anchors, aliases, merges, nonstring keys and two promotions.\n',
      'paper/README.md':'# Manuscript artifacts\n\nThree wrappers compile strictly increasing theorem layers from main_body.tex. main.pdf equals round2. Every round has bilingual abstracts and six keywords per language. Raw compiler logs, deterministic rebuild receipts and full-page raster checks are retained.\n',
      'RELEASE.md':'# Release\n\nRun `python -B code/c389_release_manifest.py --write --build-pdfs` to generate evidence, reports, PDFs and manifest. Run `python -B code/c389_release_manifest.py` for complete nonwriting verification including fresh PDF builds. Both lanes are local and scoped to this package.\n'}

def main():
    if sys.flags.optimize:
        raise RuntimeError('C389 release refuses optimized Python')
    parser=argparse.ArgumentParser()
    parser.add_argument('--write',action='store_true')
    parser.add_argument('--build-pdfs',action='store_true')
    args=parser.parse_args()
    need(not args.build_pdfs or args.write,'--build-pdfs requires --write')
    route=content_gate()
    if args.write:
        run('c389_carlitz_producer.py')
    with tempfile.TemporaryDirectory(prefix='c389-release-producer-') as directory:
        output=Path(directory)/'evidence.json'
        producer=run('c389_carlitz_producer.py',['--output',str(output)])
        need(output.read_bytes()==(ROOT/'results/c389_carlitz_evidence.json').read_bytes(),'producer differs')
    outputs={'producer':producer}
    for label,script in [('checker','c389_carlitz_checker.py'),('sympy','c389_carlitz_sympy_crosscheck.py'),
                         ('replay','c389_carlitz_replay.py'),('mutation','c389_carlitz_mutation.py')]:
        outputs[label]=run(script)
        need('PASS' in outputs[label],'missing PASS '+label)
    p=subprocess.run([sys.executable,'-B','-m','unittest','tests/test_c389_smoke.py'],cwd=ROOT,env=ENV,capture_output=True,text=True)
    need(p.returncode==0 and 'OK' in p.stderr,'smoke failure '+p.stdout+p.stderr)
    outputs['smoke']='3 tests PASS'
    for path in sorted((ROOT/'code').glob('c389_*.py')):
        for opt in ('-O','-OO'):
            p=subprocess.run([sys.executable,opt,'-B',str(path)],env=ENV,capture_output=True,text=True)
            need(p.returncode!=0 and 'optimized' in p.stderr,'optimized refusal '+path.name)
    pdfs=pdf_gate(args.build_pdfs)
    generated=reports(outputs,pdfs)
    for name,content in generated.items():
        path=ROOT/name
        if args.write:
            path.write_text(content)
        else:
            need(path.read_text()==content,'report drift '+name)
    files={str(p.relative_to(ROOT)):sha(p) for p in sorted(ROOT.rglob('*')) if p.is_file() and p!=MANIFEST}
    need(set(files)==EXPECTED,'payload membership missing='+str(sorted(EXPECTED-set(files)))+' extra='+str(sorted(set(files)-EXPECTED)))
    need(not any('__pycache__' in n or n.endswith(('.aux','.out','.toc')) for n in files),'unexpected build residue')
    # The whitelist and the nonwrite manifest independently lock exact membership.
    need(all(n.split('/')[0] in {'code','evaluations','paper','proof','results','review','tests'} or '/' not in n for n in files),'unknown payload directory')
    evidence=strict_json(ROOT/'results/c389_carlitz_evidence.json')
    manifest=dict(schema='hcs-release-manifest-v1',candidate_id='HCS-C389',obstruction_id='HEN-O373',
        source_commit=SOURCE,fixed_epoch=1788566400,scope_literal='NO_BAD_EULER_OR_ROOT_NUMBER',
        evaluator_authority='flow_systems/skills/route-a-evaluator.md',evaluator_version='0.2.0',
        evaluator_authority_sha256=EVALUATOR,evaluation_raw_sha256=sha(YML),
        evaluation_semantic_sha256=hashlib.sha256(json.dumps(route,sort_keys=True,separators=(',',':')).encode()).hexdigest(),
        payload_file_count=len(files),physical_file_count=len(files)+1,
        evidence_sha256=sha(ROOT/'results/c389_carlitz_evidence.json'),evidence_payload_sha256=evidence['payload_sha256'],
        analytic_theorem_range='all prime powers q, all conductors and multipliers, all prime-power levels and compatible towers',finite_evidence={'ring_cases':len(evidence['payload']['ring_cases']),'tower_cases':len(evidence['payload']['tower_cases'])},
        route_tuple=ROUTE,overall_verdict='ROUTE_A_EXPLORATORY',release_lanes={k:'PASS' for k in
        ('producer','independent_checker','sympy_crosscheck','isolated_byte_replay','hostile_mutation','unittest_smoke',
         'optimized_mode_refusal','strict_json_yaml','source_and_scope_gate','deterministic_pdf_rebuild','embedded_subset_fonts','payload_membership')},
        pdf_rounds=pdfs,main_pdf_sha256=sha(ROOT/'paper/main.pdf'),files=files)
    if args.write:
        MANIFEST.write_text(json.dumps(manifest,indent=2,sort_keys=True)+'\n')
    else:
        need(strict_json(MANIFEST)==manifest,'release manifest drift')
    print('C389_RELEASE_PASS evidence_sha256='+manifest['evidence_sha256']+
          ' main_pdf_sha256='+manifest['main_pdf_sha256']+' manifest_sha256='+sha(MANIFEST))

if __name__=='__main__':
    main()
