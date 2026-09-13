#!/usr/bin/env python3
"""Build one isolated notes-only preview from an officially applied exact patch.

Mechanical formatting only: strip block-marker lines in the temporary copy,
copy the approved bibliography, run four TeX passes, and preserve build logs.
Print a receipt as apply_patch input; a non-clean build exits 1 and must stop.
"""
import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import runpy
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'BATCH_ROUND10_STAGE4_5_ROUND2_EXACT_PATCH_'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def desc(path):
    raw = path.read_bytes()
    return {'path': str(path.relative_to(ROOT)), 'sha256': sha(raw), 'bytes': len(raw)}


def verify(row):
    assert desc(ROOT / row['path']) == row, row['path']


def main(paper_id):
    apply_path = ROOT / (PREFIX + 'APPLICATION_RECEIPT.json')
    apply = json.loads(apply_path.read_bytes())
    verify(apply['authority'])
    authority = json.loads((ROOT / apply['authority']['path']).read_bytes())
    verify(authority['confirmed_request'])
    assert authority['confirmed_request']['sha256'] == '759480e724b818c5068233134712a14a4736df116ca295578495912f3a86a42d'
    p = next(p for p in apply['papers'] if p['paper_id'] == paper_id)
    for key in ('successor', 'approved_patch', 'apply_report', 'revision_evidence_bundle', 'block_manifest', 'integrity_authorization'):
        verify(p[key])
    lock = json.loads((ROOT / 'BATCH_ROUND10_STAGE4_5_ROUND2_INPUT_LOCK.json').read_bytes())
    bib = apply['bib_successor'] if paper_id == 'P30' else next(p for p in lock['papers'] if p['paper_id'] == paper_id)['audit_bibliography']
    verify(bib)
    source = ROOT / p['successor']['path']
    notes, job = source.parent, source.stem
    pdf_path = source.with_suffix('.pdf')
    log_path = notes / (job + '.build.log')
    transcript_path = notes / (job + '.build.transcript.log')
    receipt_path = notes / (job + '_build_receipt.json')
    for path in (pdf_path, log_path, transcript_path, receipt_path):
        assert not path.exists(), f'refusing overwrite {path}'
    frozen = {d['path']: d for d in [p['successor'], p['approved_patch'], p['apply_report'], p['revision_evidence_bundle'], p['block_manifest'], p['integrity_authorization'], bib]}
    finalizer = runpy.run_path(str(ROOT / 'tools/finalize_round10_stage4_5_round2.py'), run_name='read_only_boundary_helpers')
    before = finalizer['protected_boundary_replay']()
    compile_dir = Path(tempfile.mkdtemp(prefix='round10-exact-'+paper_id.lower()+'-'))
    original = source.read_text()
    marker_free = re.sub(r'(?m)^<!--block:B\d+-->\r?\n?', '', original)
    # Temporary formatting copies only; the approved .tex/.bib stay untouched.
    (compile_dir / 'manuscript.tex').write_text(marker_free, encoding='utf-8')
    shutil.copyfile(ROOT / bib['path'], compile_dir / 'references.bib')
    env = os.environ.copy()
    env.update({'LC_ALL': 'C', 'TZ': 'UTC', 'SOURCE_DATE_EPOCH': '1788134400'})
    latex = ['/usr/bin/lualatex', '-no-shell-escape', '-interaction=nonstopmode', '-halt-on-error', '-jobname='+job, 'manuscript.tex']
    commands = [latex, ['/usr/bin/bibtex', job], latex, latex]
    records, transcript = [], []
    failure = None
    for command in commands:
        try:
            result = subprocess.run(command, cwd=compile_dir, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=120)
            output = result.stdout.decode('utf-8', errors='replace')
            code = result.returncode
        except subprocess.TimeoutExpired as exc:
            output = (exc.stdout or b'').decode('utf-8', errors='replace') + '\nBUILD TIMEOUT\n'
            code = 124
        records.append({'argv': command, 'exit_code': code})
        transcript.extend(['$ '+ ' '.join(command)+'\n', output, '\n'])
        if code != 0:
            failure = 'COMPILER_COMMAND_FAILED'
            break
    temp_log = compile_dir / (job+'.log')
    log = temp_log.read_text(errors='replace') if temp_log.exists() else ''
    diagnostics = {
        'undefined_citations': len(re.findall(r'Citation [`\'][^\n]+ undefined|There were undefined citations', log, re.I)),
        'undefined_references': len(re.findall(r'Reference [`\'][^\n]+ undefined|There were undefined references', log, re.I)),
        'missing_glyphs': log.count('Missing character:'),
        'fatal_errors': len(re.findall(r'Fatal error|Emergency stop', log, re.I)),
        'overfull_hboxes': log.count('Overfull \\hbox'),
    }
    if any(diagnostics.values()):
        failure = failure or 'NON_CLEAN_FINAL_LATEX_LOG'
    temp_pdf = compile_dir / (job+'.pdf')
    if not temp_pdf.is_file() or temp_pdf.stat().st_size == 0:
        failure = failure or 'MISSING_PDF'
    page_count, page_size, pdf_text_sha = None, None, None
    if not failure:
        for command in (['/usr/bin/pdfinfo', str(temp_pdf)], ['/usr/bin/pdftotext', str(temp_pdf), '-']):
            result = subprocess.run(command, cwd=compile_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60)
            records.append({'argv': command, 'exit_code': result.returncode})
            output = result.stdout.decode('utf-8', errors='replace')
            transcript.extend(['$ '+' '.join(command)+'\n', output, result.stderr.decode('utf-8', errors='replace'), '\n'])
            if result.returncode != 0:
                failure = 'PDF_READBACK_FAILED'
                break
            if command[0].endswith('pdfinfo'):
                match = re.search(r'^Pages:\s+(\d+)', output, re.M)
                page_count = int(match.group(1)) if match else None
                size = re.search(r'^Page size:\s+(.+)$', output, re.M)
                page_size = size.group(1) if size else None
                if not page_count:
                    failure = 'PDF_PAGE_COUNT_UNAVAILABLE'
            else:
                pdf_text_sha = sha(result.stdout)
                if not output.strip():
                    failure = 'EMPTY_PDF_TEXT'
    for d in frozen.values():
        verify(d)
    after = finalizer['protected_boundary_replay']()
    assert before == after, 'protected boundary drift during build'
    # Preserve real diagnostic logs even on failure; never publish a failed PDF.
    log_path.write_text(log, encoding='utf-8')
    transcript_path.write_text(''.join(transcript), encoding='utf-8')
    if not failure:
        shutil.copyfile(temp_pdf, pdf_path)
    receipt = {'schema_version': 'round10-exact-patch-isolated-preview-build/1.0', 'paper_id': paper_id, 'built_at_utc': datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z'), 'status': 'FAIL' if failure else 'PASS_CLEAN', 'failure_reason': failure, 'authority': apply['authority'], 'application_receipt': desc(apply_path), 'builder': desc(Path(__file__).resolve()), 'input_draft': p['successor'], 'bibliography': bib, 'revision_evidence_bundle': p['revision_evidence_bundle'], 'commands': records, 'diagnostics': diagnostics, 'pages': page_count, 'page_size': page_size, 'pdf_readback_text_sha256': pdf_text_sha, 'preview': desc(pdf_path) if not failure else None, 'final_latex_log': desc(log_path), 'transcript': desc(transcript_path), 'temporary_compile_directory': str(compile_dir), 'temporary_files_retained': True, 'compile_source_sha256': sha((compile_dir/'manuscript.tex').read_bytes()), 'marker_stripping': 'Only whole ARS block-marker lines removed in temporary formatting copy; all other source bytes unchanged.', 'citation_style': 'natbib[numbers,sort&compress] + plainnat numeric', 'environment_overrides': {'LC_ALL': 'C', 'TZ': 'UTC', 'SOURCE_DATE_EPOCH': '1788134400'}, 'protected_snapshot_unchanged': True, 'protected_locked_bindings': after['locked_file_bindings_replayed'], 'canonical_or_scientific_mutations': False, 'stage4_5_round3_run': False, 'stage5_or_stage6_run': False, 'classification': 'NOTES_SIDE_CORRECTION_PREVIEW_NOT_FINAL_MANUSCRIPT'}
    print('*** Begin Patch\n*** Add File: '+str(receipt_path))
    for line in (json.dumps(receipt, ensure_ascii=False, indent=2, sort_keys=True)+'\n').splitlines():
        print('+'+line)
    print('*** End Patch')
    return 1 if failure else 0


if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] not in ('P29', 'P30', 'P31', 'P32', 'P33'):
        raise SystemExit('usage: build_round10_exact_patch_previews.py P29|P30|P31|P32|P33')
    raise SystemExit(main(sys.argv[1]))
