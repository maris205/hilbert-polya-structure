#!/usr/bin/env python3
"""Root's independent raw-capture and full reconstructed-current-map reception.

Reads existing evidence only. Does not import the receiver, replay science,
build, render, view, update lifecycle or declare paper/batch completion.
"""
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import sysconfig

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
CAP = QA / 'p210_terminal_root_reception_01'
PAPER = ROOT / 'papers/210-weakly-increasing-run-aggregation'
BUILD = PAPER / 'qa_final'
CHECKS = 0

def need(ok, label):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(label)

def dp(data):
    return dict(sha256=hashlib.sha256(data).hexdigest(), bytes=len(data))

def pin(path):
    digest = hashlib.sha256()
    size = 0
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            digest.update(block)
            size += len(block)
    return dict(sha256=digest.hexdigest(), bytes=size)

def read(path):
    return json.loads(Path(path).read_bytes())

def rich(path):
    p = Path(path)
    d = dict(exists=p.exists(), symlink=p.is_symlink(), link=str(p.readlink()) if p.is_symlink() else None,
             resolved=str(p.resolve()), is_file=p.is_file(), is_dir=p.is_dir())
    if d['is_file']:
        d.update(pin(p))
    return d

def absent(pid):
    try:
        os.killpg(pid, 0)
        return False
    except ProcessLookupError:
        return True

def package(base, digest, count):
    need(pin(base / 'SHA256SUMS')['sha256'] == digest, 'fixed package seal')
    expected = {}
    for line in (base / 'SHA256SUMS').read_text().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        need(match is not None, 'strict manifest row')
        sha, name = match.groups()
        p = base / name
        need(not Path(name).is_absolute() and '..' not in Path(name).parts and p.resolve() == p and name != 'SHA256SUMS' and name not in expected, 'contained unique payload')
        expected[name] = pin(p)
        need(expected[name]['sha256'] == sha, 'full manifest payload bytes')
    need(len(expected) == count and set(expected) == {p.relative_to(base).as_posix() for p in base.rglob('*') if p.is_file() and p != base / 'SHA256SUMS'}, 'complete nonself membership')
    return expected

def known_keys():
    # Independently enumerate the source-declared bounded original spelling.
    std = Path('/usr/lib/python3.10')
    runtime = {str(std)} | {'/usr/bin/' + n for n in ('pdflatex','bibtex','kpsewhich','pdfinfo','pdffonts','pdftotext','pdftoppm','ldd','cmp','env','python3.10')} | {'/bin/bash','/bin/sh'}
    for directory, folders, files in os.walk(std):
        folders[:] = [n for n in folders if n not in {'site-packages','dist-packages','__pycache__'}]
        runtime.update(str(Path(directory) / n) for n in files if not n.endswith(('.pyc','.pyo')))
    for name in ('/usr/lib/x86_64-linux-gnu','/usr/lib64','/usr/local/lib'):
        p = Path(name)
        runtime.add(name)
        candidates = p.glob('*') if name == '/usr/local/lib' else p.rglob('*')
        runtime.update(str(q) for q in candidates if q.is_file() and (q.name.endswith('.so') or '.so.' in q.name))
    roots = dict(tex=('/usr/share/texlive/texmf-dist','/usr/share/texmf','/var/lib/texmf','/etc/texmf','/usr/local/share/texmf','/root/texmf','/root/.texlive2021/texmf-config','/root/.texlive2021/texmf-var'), configuration=('/etc/ld.so.conf.d','/usr/share/fonts','/etc/fonts','/var/cache/fontconfig','/usr/share/fontconfig','/usr/lib/locale/C.utf8','/usr/lib/x86_64-linux-gnu/gconv','/usr/lib/gconv','/usr/share/poppler','/usr/local/share/fonts','/etc/xdg/fontconfig','/etc/profile.d','/root/.fonts','/root/.fontconfig','/root/.fonts.conf.d','/root/.config/fontconfig','/root/.cache/fontconfig','/root/.local/share/fonts'))
    groups = dict(runtime=runtime)
    for group, bases in roots.items():
        groups[group] = set(bases)
        for base in bases:
            if Path(base).is_dir():
                groups[group].update(str(p) for p in Path(base).rglob('*'))
    config = groups['configuration']
    config.update(('/etc/ld.so.cache','/etc/ld.so.conf','/etc/ld.so.preload','/etc/locale.conf','/etc/default/locale','/etc/nsswitch.conf','/etc/localtime','/etc/bash.bashrc','/etc/profile','/etc/passwd','/etc/group','/etc/fonts/local.conf','/usr/lib/locale/locale-archive','/root/.fonts.conf','/root/.config/fontconfig/fonts.conf','/usr/lib/python310.zip','/usr/bin/pyvenv.cfg','/usr/pyvenv.cfg'))
    config.update(str(Path(base) / name) for base in ('/usr/bin','/usr/lib') for name in ('python._pth','python3._pth','python310._pth','python3.10._pth'))
    config.update((sysconfig.get_makefile_filename(), sysconfig.get_config_h_filename()))
    for key in ('LDLIBRARY','INSTSONAME'):
        value = sysconfig.get_config_var(key)
        if value:
            config.add('/usr/lib/' + value + '._pth')
    ldd = Path('/usr/bin/ldd').read_text()
    loaders = re.search(r'^RTLDLIST="([^"]+)"', ldd, re.M)
    need(ldd.startswith('#!/bin/bash\n') and loaders is not None, 'literal loader rule')
    config.update(loaders.group(1).split())
    return groups

def main():
    result = read(CAP / 'RESULT.json')
    need(result['original_wait_exit_code'] == result['cleanup_wait_exit_code'] == 0 and result['child_reaped'] is True and result['process_group_absent'] is True and absent(result['pid']), 'actual original normal wait and now absent group')
    need(result['cleanup_events'] == [] and result['wait_error'] is None and result['timed_out'] is False and result['inputs_unchanged'] is True and result['inputs_before'] == result['inputs_after'], 'no cleanup-as-success or changed inputs')
    need(not os.path.lexists(CAP / 'unused_receiver_cache'), 'actual cache absent')
    attempt, spawn = read(CAP / 'ATTEMPT.json'), read(CAP / 'SPAWN.json')
    need(attempt['argv'] == result['argv'] and attempt['cwd'] == result['cwd'] == str(ROOT) and attempt['environment'] == result['environment'] and attempt['inputs_before'] == result['inputs_before'] and attempt['timeout_seconds'] == 600 and attempt['start_new_session'] is True and spawn['pid'] == spawn['process_group_id'] == result['pid'], 'complete recorder attempt and spawn binding')
    for path, expected in result['inputs_before'].items():
        need(pin(path) == expected, 'actual direct input bytes')
    payloads = package(CAP, '1037dc53ebff5fdd4ebfec909ce408c9c401589b9ac6a9e1993b6faacbf215e2', 6)
    raw = (CAP / 'ROOT_RECEPTION.json').read_bytes()
    need(dp(raw) == result['stdout'] == payloads['ROOT_RECEPTION.json'] and (CAP / 'stderr').read_bytes() == b'' and pin(CAP / 'stderr') == result['stderr'], 'complete raw dual-stream receipt')
    launch, completion = (read(QA / ('P210_TERMINAL_RECEIVER01_ROOT_' + name + '.actual.json')) for name in ('LAUNCH','COMPLETION'))
    need(launch['result']['session_id'] == completion['session_id'] == 91772 and launch['result']['chunk_id'] == '6dc338' and launch['result']['output'] == '' and 'exit_code' not in launch['result'] and completion['result']['chunk_id'] == '0317d6' and completion['result']['exit_code'] == 0 and 'session_id' not in completion['result'], 'actual root native chain')
    tool = json.loads(completion['result']['output'])
    need(tool == dict(current_path_keys=125499, original_input_count=1619, original_wait_exit_code=0, output=str(CAP), result=pin(CAP / 'RESULT.json'), seal=pin(CAP / 'SHA256SUMS'), status='PASS_ACTUAL_P210_TERMINAL_RECEPTION_CAPTURE', stderr=result['stderr'], stdout=result['stdout'], terminal_acceptance=False), 'entire actual tool stdout')
    doc = json.loads(raw)
    need(doc['status'] == 'PASS_P210_TERMINAL_BUILD_ORIGINAL_DOCUMENTS_ONLY' and doc['checks'] == 533864 and doc['root_acceptance'] is False and all(doc[k] == 0 for k in ('new_science_executions','new_builds','new_views','manuscript_reviews')), 'documentary scope')
    reconstruct = doc['current_key_reconstruction']
    ledger_path = BUILD / 'KNOWN_INPUTS_BEFORE.json.gz'
    need(reconstruct['known_ledger'] == str(ledger_path) and reconstruct['known_ledger_pin'] == pin(ledger_path), 'actual reconstruction ledger')
    body = gzip.decompress(ledger_path.read_bytes())
    before = json.loads(body)
    need(body == gzip.decompress((BUILD / 'KNOWN_INPUTS_AFTER.json.gz').read_bytes()), 'complete raw before-after ledger')
    keys = known_keys()
    need(set(before) == set(keys) == {'configuration','runtime','tex'} and all(set(before[k]) == keys[k] for k in keys), 'entire independently enumerated known membership before any extras union')
    known = {}
    for rows in before.values():
        for path, value in rows.items():
            need(path not in known or known[path] == value, 'consistent original-spelling duplicates')
            known[path] = value
    extra = reconstruct['extra_entries']
    need(len(known) == reconstruct['known_original_paths'] == 123595 and len(extra) == reconstruct['extra_count'] == 1904 and not set(known).intersection(extra), 'known and extras separately validated and disjoint')
    full = {**known, **extra}
    need(len(full) == reconstruct['complete_entries'] == doc['current_path_keys'] == 125499 and dp(json.dumps(full, sort_keys=True, separators=(',', ':')).encode()) == reconstruct['complete_map'], 'entire reconstructed rich map and canonical bytes')
    need(hashlib.sha256(json.dumps(sorted(full), separators=(',', ':')).encode()).hexdigest() == doc['current_path_keys_sha256'], 'whole actual key-set identity')
    for path, expected in full.items():
        need(rich(path) == expected, 'independent full rich path reread: ' + path)
    need(known_keys() == keys, 'known membership unchanged after full read')
    package(BUILD, doc['build_seal'], 222)
    views = read(QA / 'P210_TERMINAL_ROOT_VIEWS.actual.json')
    need(views['status'] == 'ROOT_ACTUALLY_VIEWED_ALL_SIX_FINAL_PAGES_PASS' and views['terminal_manifest_sha256'] == doc['build_seal'] and views['open_visual_findings'] == 0 and [p['page'] for p in views['pages']] == list(range(1,7)), 'separate six actually viewed pages')
    for page in views['pages']:
        need(page['actually_displayed_and_viewed'] is True and page['observation'] and pin(page['path']) == {k:page[k] for k in ('sha256','bytes')}, 'each original actual view binding')
    pdfs = [(BUILD / ('cold_build_' + str(n)) / 'main.pdf').read_bytes() for n in (1,2)]
    need(pdfs[0] == pdfs[1] == (PAPER / 'frozen_round2/main.pdf').read_bytes() and dp(pdfs[0])['sha256'] == views['pdf_sha256'], 'actual full PDF byte equality and view identity')
    print(json.dumps(dict(status='PASS_ROOT_P210_TERMINAL_CAPTURE_ORIGINAL_RECEPTION', checks=CHECKS, current_path_keys=len(full), known_original_paths=len(known), disjoint_extras=len(extra), reconstructed_current_map=reconstruct['complete_map'], receiver_raw=dp(raw), receiver_seal=pin(CAP/'SHA256SUMS'), native_session=91772, native_completion_chunk='0317d6', terminal_seal=pin(BUILD/'SHA256SUMS'), original_terminal_builds=2, original_actual_root_views=6, new_science_executions=0, new_builds=0, new_views=0, paper_completion=False, five_paper_completion=False), sort_keys=True))

if __name__ == '__main__':
    main()
