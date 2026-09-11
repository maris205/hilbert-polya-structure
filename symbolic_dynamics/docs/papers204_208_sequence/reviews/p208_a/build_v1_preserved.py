"""Independent reviewer cold source build; no author manuscript edits."""
from pathlib import Path
import hashlib, json, os, re, runpy, shutil, sys, time

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
OUT=ROOT/'docs/papers204_208_sequence/reviews/p208_a'
FREEZE=ROOT/'papers/208-original-snapshot-triangulation-sweeps/frozen_round0'
shared=runpy.run_path(str(OUT/'record.py'))
sha,dump,pins,command=[shared[n] for n in ('sha','dump','pins','command')]
ENV={'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC',
     'SOURCE_DATE_EPOCH':'1788652800','FORCE_SOURCE_DATE':'1','openin_any':'p','openout_any':'p'}
TEX_ROOTS=['/usr/share/texlive/texmf-dist/tex','/usr/share/texlive/texmf-dist/fonts',
           '/usr/share/texlive/texmf-dist/web2c','/usr/share/texlive/texmf-dist/bibtex',
           '/usr/share/texmf','/var/lib/texmf','/etc/texmf','/usr/local/share/texmf',
           '/root/texmf','/root/.texlive2021/texmf-config','/root/.texlive2021/texmf-var']
TOOLS=['/usr/bin/pdflatex','/usr/bin/bibtex','/usr/bin/kpsewhich','/usr/bin/pdfinfo',
       '/usr/bin/pdffonts','/usr/bin/pdftotext','/usr/bin/pdftoppm','/usr/bin/ldd','/usr/bin/cmp']

def main():
    label=sys.argv[1];dest=OUT/label;dest.mkdir();cold=dest/'source_only';cold.mkdir()
    shutil.copyfile(__file__,dest/'build_preserved.py')
    shutil.copyfile(OUT/'record.py',dest/'record_preserved.py')
    sources=[FREEZE/'main.tex',FREEZE/'math_commands.tex',FREEZE/'references.bib',*sorted((FREEZE/'sections').glob('*.tex'))]
    before=pins(sources+[Path(__file__),OUT/'record.py',FREEZE/'SHA256SUMS',FREEZE/'main.pdf'])
    dump(dest/'INPUTS_BEFORE.json',before)
    for p in sources:
        q=cold/p.relative_to(FREEZE);q.parent.mkdir(exist_ok=True,parents=True);shutil.copyfile(p,q)
    initial={str(p.relative_to(cold)):sha(p) for p in cold.rglob('*') if p.is_file()}
    assert len(initial)==11 and all(not p.endswith(('.aux','.pdf','.bbl')) for p in initial)
    dump(dest/'SOURCE_ONLY_INITIAL.json',initial)
    runtime=[]
    for root in TEX_ROOTS:
        if Path(root).exists():runtime.extend(p.resolve() for p in Path(root).rglob('*') if p.is_file())
    inventory=pins(runtime);dump(dest/'TEX_INVENTORY_BEFORE.json',inventory)
    recorder_modules=[Path(m.__file__).resolve() for m in tuple(sys.modules.values()) if getattr(m,'__file__',None) and Path(m.__file__).is_file()]
    toolpins=pins(TOOLS+[sys.executable,__file__,OUT/'record.py',*recorder_modules]);dump(dest/'TOOLS_BEFORE.json',toolpins)
    linked=[]
    for i,t in enumerate(TOOLS[:-2]+[sys.executable]):
        command(['/usr/bin/ldd',str(Path(t).resolve())],cold,ENV,dest/('ldd%02d'%i))
        raw=(dest/('ldd%02d.stdout'%i)).read_text();assert 'not found' not in raw
        linked.extend(token for token in raw.split() if token.startswith('/') and Path(token).is_file())
    libs=pins(linked);dump(dest/'LIBRARIES_BEFORE.json',libs)
    command(['/usr/bin/pdflatex','--version'],cold,ENV,dest/'engine_version')
    command(['/usr/bin/bibtex','--version'],cold,ENV,dest/'bibtex_version')
    command(['/usr/bin/kpsewhich','-var-value=TEXMF'],cold,ENV,dest/'texmf_roots')
    consumed={}
    for i in range(1,4):
        command(['/usr/bin/pdflatex','-no-shell-escape','-recorder','-interaction=nonstopmode','-halt-on-error','main.tex'],cold,ENV,dest/('tex%d'%i))
        for ext in ('log','fls','aux'):
            shutil.copyfile(cold/('main.'+ext),dest/('pass%d.'%i+ext))
        for line in (cold/'main.fls').read_text().splitlines():
            if line.startswith('INPUT '):
                p=Path(line[6:]);p=p if p.is_absolute() else cold/p;p=p.resolve()
                if p.is_file() and not p.is_relative_to(cold):
                    assert inventory.get(str(p))==sha(p),('unrecorded TeX resource',str(p))
                    consumed[str(p)]=sha(p)
        if i==1:
            command(['/usr/bin/kpsewhich','plainnat.bst'],cold,ENV,dest/'bst')
            bst=Path((dest/'bst.stdout').read_text().strip()).resolve()
            assert inventory[str(bst)]==sha(bst);consumed[str(bst)]=sha(bst)
            command(['/usr/bin/bibtex','main'],cold,ENV,dest/'bibtex')
            shutil.copyfile(cold/'main.bbl',dest/'generated.bbl')
            shutil.copyfile(cold/'main.blg',dest/'generated.blg')
    command(['/usr/bin/pdfinfo','main.pdf'],cold,ENV,dest/'pdfinfo')
    command(['/usr/bin/pdffonts','main.pdf'],cold,ENV,dest/'pdffonts')
    command(['/usr/bin/pdftotext','-layout','main.pdf',str(dest/'main.txt')],cold,ENV,dest/'pdftotext')
    pages=dest/'pages';pages.mkdir()
    command(['/usr/bin/pdftoppm','-png','-r','120','main.pdf',str(pages/'page')],cold,ENV,dest/'render')
    command(['/usr/bin/cmp',str(cold/'main.pdf'),str(FREEZE/'main.pdf')],cold,ENV,dest/'frozen_pdf_cmp')
    log=(cold/'main.log').read_text();warnings={k:re.findall(r'^.*'+v+r'.*$',log,re.M) for k,v in [('undefined','undefined'),('overfull','Overfull'),('underfull','Underfull'),('warnings','Warning')]}
    assert not warnings['undefined'] and not warnings['overfull']
    assert warnings['underfull']==['Underfull \\hbox (badness 5681) in paragraph at lines 9--13']
    fonts=[s.split()[-5:] for s in (dest/'pdffonts.stdout').read_text().splitlines()[2:] if s.strip()]
    assert len(fonts)==27 and all(f[0]=='yes' for f in fonts)
    assert re.search(r'^Pages:\s+7$',(dest/'pdfinfo.stdout').read_text(),re.M)
    assert len(list(pages.glob('*.png')))==7
    after=pins(before);dump(dest/'INPUTS_AFTER.json',after);assert before==after
    dump(dest/'TOOLS_AFTER.json',pins(toolpins));assert pins(toolpins)==toolpins
    dump(dest/'LIBRARIES_AFTER.json',pins(libs));assert pins(libs)==libs
    dump(dest/'CONSUMED_TEX_BEFORE.json',consumed);dump(dest/'CONSUMED_TEX_AFTER.json',pins(consumed));assert pins(consumed)==consumed
    assert initial=={rel:sha(cold/rel) for rel in initial}
    dump(dest/'RECEIPT.json',dict(status='PASS_BUILT_NOT_YET_VIEWED',pages=7,fonts_embedded=27,warnings=warnings,
        pdf_sha256=sha(cold/'main.pdf'),source_files=11,tex_inventory_count=len(inventory),consumed_tex_count=len(consumed),
        source_only_initial=initial,limitations='Pinned consumed TeX resources and actual tool/libraries; not a hermetic historic OS; actual viewing is separate.'))
    print('PASS source-only build, seven pages, actual badness 5681 retained; not yet viewed.')

if __name__=='__main__':main()
