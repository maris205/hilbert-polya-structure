"""B-owned source-only TeX build; full relevant input snapshots and observed maps.

Infrastructure design informed by author/A build recorders after science kernel
freeze. No mathematical implementation reused or executed by this recorder.
"""
from pathlib import Path
import hashlib
import json
import os
import re
import subprocess
import sys
import time

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
BASE=ROOT/'docs/papers204_208_sequence/reviews/p208_b'
FREEZE=ROOT/'papers/208-original-snapshot-triangulation-sweeps/frozen_round1'
OUT=BASE/'source_build'
ENV={'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC',
     'SOURCE_DATE_EPOCH':'1788652800','FORCE_SOURCE_DATE':'1','openin_any':'p','openout_any':'p'}
TOOLS=['/usr/bin/pdflatex','/usr/bin/bibtex','/usr/bin/kpsewhich','/usr/bin/pdfinfo',
       '/usr/bin/pdffonts','/usr/bin/pdftotext','/usr/bin/pdftoppm','/usr/bin/ldd','/usr/bin/cmp','/bin/bash']
TEX_ROOTS=['/usr/share/texlive/texmf-dist/tex','/usr/share/texlive/texmf-dist/fonts',
 '/usr/share/texlive/texmf-dist/web2c','/usr/share/texlive/texmf-dist/bibtex',
 '/usr/share/texmf','/var/lib/texmf','/etc/texmf','/usr/local/share/texmf','/root/texmf',
 '/root/.texlive2021/texmf-config','/root/.texlive2021/texmf-var']
CONFIG_ROOTS=['/etc/ld.so.conf.d','/etc/fonts','/usr/share/fonts','/var/cache/fontconfig',
 '/usr/share/fontconfig','/usr/lib/locale/C.utf8','/usr/share/poppler']
CONFIG_EXPLICIT=['/etc/ld.so.cache','/etc/ld.so.conf','/etc/ld.so.preload',
 '/root/miniconda3/pyvenv.cfg','/root/miniconda3/bin/pyvenv.cfg',
 '/root/miniconda3/bin/python._pth','/root/miniconda3/lib/python312.zip']
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dump(p,obj):
    with Path(p).open('x') as f:json.dump(obj,f,indent=2,sort_keys=True);f.write('\n')
def pins(paths):return {str(p):sha(p) for p in sorted(set(str(p) for p in paths))}
def inventory(roots):
    return pins(p.resolve() for root in roots if Path(root).exists() for p in Path(root).rglob('*') if p.is_file())
def absence():
    return {p:{'exists':Path(p).exists(),'sha256':sha(p) if Path(p).is_file() else None}
            for p in TEX_ROOTS+CONFIG_ROOTS+CONFIG_EXPLICIT}
def runtime():
    result={'version':sys.version,'flags':repr(sys.flags),'path':sys.path,
            'pycache_prefix':sys.pycache_prefix,'environment':dict(os.environ),'modules':{}}
    for name,m in sorted(sys.modules.items()):
        path=getattr(m,'__file__',None);spec=getattr(m,'__spec__',None)
        result['modules'][name]={'file':path,'origin':getattr(spec,'origin',None),
                                'sha256':sha(path) if path and Path(path).is_file() else None}
    raw=Path('/proc/self/maps').read_text();result['maps_raw']=raw
    result['map_files']=pins(line.split(None,5)[5] for line in raw.splitlines() if len(line.split(None,5))==6 and line.split(None,5)[5].startswith('/'))
    return result
COMMANDS=[]
OBSERVED={}
def command(name,args,cwd):
    snapshots=[];start=time.time()
    with (OUT/(name+'.stdout')).open('xb') as out, (OUT/(name+'.stderr')).open('xb') as err:
        p=subprocess.Popen(args,cwd=cwd,env=ENV,stdout=out,stderr=err)
        last=None
        while p.poll() is None:
            try:raw=Path(f'/proc/{p.pid}/maps').read_text()
            except (FileNotFoundError,ProcessLookupError,PermissionError):raw=''
            if raw and raw!=last:
                snapshots.append(raw);last=raw
                for line in raw.splitlines():
                    parts=line.split(None,5)
                    if len(parts)==6 and parts[5].startswith('/') and Path(parts[5]).is_file():
                        OBSERVED[parts[5]]=sha(parts[5])
            time.sleep(.005)
        code=p.wait()
    row={'argv':[str(x) for x in args],'cwd':str(cwd),'environment':ENV,'exit_code':code,
         'seconds':time.time()-start,'stdout_sha256':sha(OUT/(name+'.stdout')),
         'stderr_sha256':sha(OUT/(name+'.stderr')),'observed_map_snapshots':len(snapshots)}
    dump(OUT/(name+'.command.json'),row);dump(OUT/(name+'.maps.json'),snapshots)
    COMMANDS.append(row)
    assert code==0,(name,code)
    return (OUT/(name+'.stdout')).read_text(errors='replace')
def main():
    assert sys.flags.optimize==0 and sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode
    assert sys.pycache_prefix and not Path(sys.pycache_prefix).exists()
    OUT.mkdir(exist_ok=False);cold=OUT/'source_only';cold.mkdir()
    source_names=['main.tex','math_commands.tex','references.bib']+[str(p.relative_to(FREEZE)) for p in sorted((FREEZE/'sections').glob('*.tex'))]
    sourcepins=pins([FREEZE/n for n in source_names]+[FREEZE/'main.pdf',FREEZE/'SHA256SUMS',Path(__file__)])
    dump(OUT/'INPUTS_BEFORE.json',sourcepins)
    for n in source_names:
        dst=cold/n;dst.parent.mkdir(exist_ok=True,parents=True);dst.write_bytes((FREEZE/n).read_bytes())
    initial={str(p.relative_to(cold)):sha(p) for p in cold.rglob('*') if p.is_file()}
    assert len(initial)==11 and all(Path(p).suffix in ('.tex','.bib') for p in initial)
    dump(OUT/'SOURCE_ONLY_INITIAL.json',initial)
    texbefore=inventory(TEX_ROOTS);dump(OUT/'TEX_INVENTORY_BEFORE.json',texbefore)
    cfg=inventory(CONFIG_ROOTS);cfg.update(pins(p for p in CONFIG_EXPLICIT if Path(p).is_file()))
    dump(OUT/'CONFIG_BEFORE.json',cfg);absbefore=absence();dump(OUT/'CONFIG_ABSENCE_BEFORE.json',absbefore)
    parent=runtime();dump(OUT/'RECORDER_RUNTIME_BEFORE.json',parent)
    parentfiles=[i['file'] for i in parent['modules'].values() if i['sha256']]
    toolpins=pins([Path(p).resolve() for p in TOOLS]+[sys.executable,Path(__file__)]+parentfiles+list(parent['map_files']))
    dump(OUT/'TOOLS_BEFORE.json',toolpins)
    linked=set();aliases=set();ldd_targets=sorted(set(str(Path(p).resolve()) for p in TOOLS if p!='/usr/bin/ldd')|{str(Path(sys.executable).resolve())}|{p for p in parentfiles if p.endswith('.so')})
    for i,target in enumerate(ldd_targets):
        raw=command(f'ldd_{i:02d}',['/usr/bin/ldd',target],cold)
        assert 'not found' not in raw
        for token in raw.split():
            if token.startswith('/') and Path(token).is_file():
                aliases.add(token);linked.add(str(Path(token).resolve()))
    libpins=pins(linked);dump(OUT/'LIBRARIES_BEFORE.json',libpins)
    dump(OUT/'LIBRARY_ALIASES.json',{'raw_aliases':sorted(aliases),'resolved_files':sorted(linked)})
    command('engine_version',['/usr/bin/pdflatex','--version'],cold)
    command('bibtex_version',['/usr/bin/bibtex','--version'],cold)
    for var in ('TEXMF','TEXMFCNF','TEXMFHOME','TEXMFCONFIG','TEXMFVAR','TEXFORMATS'):
        command('kpse_'+var,['/usr/bin/kpsewhich','-var-value='+var],cold)
    consumed={};generated={}
    for i in range(1,4):
        command(f'tex_{i}',['/usr/bin/pdflatex','-no-shell-escape','-recorder','-interaction=nonstopmode','-halt-on-error','main.tex'],cold)
        for ext in ('fls','log','aux','out'):
            if (cold/('main.'+ext)).exists():(OUT/(f'pass_{i}.'+ext)).write_bytes((cold/('main.'+ext)).read_bytes())
        for line in (cold/'main.fls').read_text().splitlines():
            if line.startswith('INPUT '):
                p=Path(line[6:]);p=(p if p.is_absolute() else cold/p).resolve()
                if p.is_file():
                    if p.is_relative_to(cold):generated.setdefault(str(p.relative_to(cold)),[]).append({'pass':i,'sha256':sha(p)})
                    else:
                        assert texbefore.get(str(p))==sha(p),('missing consumed TeX input',str(p))
                        consumed[str(p)]=sha(p)
        if i==1:
            bst=Path(command('bst',['/usr/bin/kpsewhich','plainnat.bst'],cold).strip()).resolve()
            assert texbefore[str(bst)]==sha(bst);consumed[str(bst)]=sha(bst)
            command('bibtex',['/usr/bin/bibtex','main'],cold)
            for ext in ('bbl','blg'):(OUT/('bibliography.'+ext)).write_bytes((cold/('main.'+ext)).read_bytes())
    info=command('pdfinfo',['/usr/bin/pdfinfo','main.pdf'],cold)
    fonts=command('pdffonts',['/usr/bin/pdffonts','main.pdf'],cold)
    command('pdftotext',['/usr/bin/pdftotext','-layout','main.pdf',str(OUT/'main.txt')],cold)
    pages=OUT/'pages';pages.mkdir()
    command('render',['/usr/bin/pdftoppm','-png','-r','120','main.pdf',str(pages/'page')],cold)
    command('cmp_frozen',['/usr/bin/cmp','-s',str(cold/'main.pdf'),str(FREEZE/'main.pdf')],cold)
    log=(cold/'main.log').read_text();text=(OUT/'main.txt').read_text()
    warnings={name:re.findall(r'^.*'+pattern+r'.*$',log,re.M) for name,pattern in
              [('undefined','undefined'),('overfull','Overfull'),('underfull','Underfull'),('warning','Warning')]}
    assert not warnings['undefined'] and not warnings['overfull']
    assert '??' not in text and '[VERIFY]' not in text and '[?]' not in text
    pagecount=int(re.search(r'^Pages:\s+(\d+)',info,re.M)[1]);assert pagecount==7
    tails=[line.split()[-5:] for line in fonts.splitlines()[2:] if line.strip()]
    assert len(tails)==27 and all(t[0]=='yes' for t in tails)
    assert len(list(pages.glob('*.png')))==7
    dump(OUT/'FONT_EMBEDDING.json',{'tail_fields_emb_sub_uni_obj_gen':tails,'all_embedded':True})
    after=pins(sourcepins);dump(OUT/'INPUTS_AFTER.json',after);assert after==sourcepins
    texafter=inventory(TEX_ROOTS);dump(OUT/'TEX_INVENTORY_AFTER.json',texafter);assert texafter==texbefore
    cfgafter=inventory(CONFIG_ROOTS);cfgafter.update(pins(p for p in CONFIG_EXPLICIT if Path(p).is_file()))
    dump(OUT/'CONFIG_AFTER.json',cfgafter);assert cfgafter==cfg
    dump(OUT/'CONFIG_ABSENCE_AFTER.json',absence());assert absence()==absbefore
    dump(OUT/'TOOLS_AFTER.json',pins(toolpins));assert pins(toolpins)==toolpins
    dump(OUT/'LIBRARIES_AFTER.json',pins(libpins));assert pins(libpins)==libpins
    dump(OUT/'CONSUMED_TEX_INPUTS.json',consumed);dump(OUT/'GENERATED_INPUT_CHAIN.json',generated)
    dump(OUT/'RECORDER_RUNTIME_AFTER.json',runtime())
    allpins={**toolpins,**libpins,**cfg,**texbefore}
    observed={str(Path(p).resolve()):h for p,h in OBSERVED.items()}
    missing={p:h for p,h in observed.items() if p not in allpins or allpins[p]!=h}
    dump(OUT/'OBSERVED_RUNTIME_MAP_COVERAGE.json',{'observed':observed,'missing':missing})
    assert not missing,missing
    assert initial=={p:sha(cold/p) for p in initial}
    dump(OUT/'RECEIPT.json',{'status':'PASS_BUILT_RENDERED_NOT_YET_VIEWED','source_files':len(initial),
        'source_only':True,'pages':pagecount,'embedded_fonts':len(tails),'warnings':warnings,
        'pdf_sha256':sha(cold/'main.pdf'),'all_command_exits_zero':all(c['exit_code']==0 for c in COMMANDS),
        'tex_inventory_files':len(texbefore),'consumed_tex_files':len(consumed),'config_files':len(cfg),
        'raw_library_aliases':len(aliases),'resolved_library_files':len(linked),
        'observed_runtime_map_files':len(observed),'commands':COMMANDS,
        'limitations':'Actual .fls, bibliography style, full pre/post TeX/resource/config inventories, resolved ldd closure and every observed process map are covered. Process-map sampling is not a syscall trace or a hermetic historical OS claim. Actual visual review is separate.'})
    print(json.dumps({'status':'PASS_BUILT_RENDERED_NOT_YET_VIEWED','pages':pagecount,'warnings':warnings,'pdf':sha(cold/'main.pdf')},sort_keys=True))
if __name__=='__main__':main()
