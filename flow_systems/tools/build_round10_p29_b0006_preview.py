#!/usr/bin/env python3
"""Build only the authorized P29 B0006 Round-5 notes preview.

Derived from the retained exact-patch preview builder. No patch application or
official integrity validator is run. Only whole block-marker lines are removed
from a temporary byte-for-byte formatting copy. Logs survive a failed attempt;
a failed PDF is never published. The receipt is printed as apply_patch input
for the orchestrator to preserve, not written by this program.
"""

import datetime
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import runpy
import shutil
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
PAPER = 'papers/29-bianchi-ideal-owner-refinement'
NOTES = ROOT / PAPER / 'notes'
JOB = 'stage4_prime_revision_round5'
APPLICATION = 'BATCH_ROUND10_P29_B0006_APPLICATION_RECEIPT.json'
AUTHORITY = 'BATCH_ROUND10_P29_B0006_EXACT_AUTHORIZATION_RECEIPT.json'
REQUEST = 'BATCH_ROUND10_P29_B0006_EXACT_PATCH_APPROVAL_REQUEST.json'
REQUEST_SHA = '87407696aba59cad12c8c0737c69caad2cb6797cea6c9d024fd313206c639d96'
PATCH_SHA = 'f9ece4cb8ba64c6270b63443bdef09240b5648e3d745dcf2131218e643629362'
DRAFT_SHA = '4f43bdbdfcfc3e1a784e1d1641b39cf3c818faa2ef8f5ac8ce613deab4d1726a'
DRAFT_BYTES = 63707
LOCK = 'BATCH_ROUND10_STAGE4_5_ROUND2_INPUT_LOCK.json'
LOCK_SHA = '11875bf33e0318997c385d0d89bde3a7987bb9166b18967994ccb3ca5ac44bb0'
BOUNDARY_HELPER = 'tools/finalize_round10_stage4_5_round2.py'
BOUNDARY_HELPER_SHA = '7396dad339f2cf25b89de32941e95ebcf31c04d42ec0c2f02a661fd8985f732d'
PREDECESSOR_BUILDER = 'tools/build_round10_exact_patch_previews.py'
PREDECESSOR_BUILDER_SHA = 'b7f2052d5fac684457acfdadc580c5b4bd5b893708b17135b1bc74c7cc3f3f0f'
PAPER_BINDINGS = (
    'successor', 'approved_patch', 'apply_report', 'revision_evidence_bundle',
    'block_manifest', 'integrity_authorization',
)
ENVIRONMENT = {'LC_ALL': 'C', 'TZ': 'UTC', 'SOURCE_DATE_EPOCH': '1788134400'}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def workspace_file(relative):
    require(isinstance(relative, str), 'artifact path must be a string')
    parts = relative.split('/')
    require(relative and not PurePosixPath(relative).is_absolute()
            and all(part not in ('', '.', '..') for part in parts),
            'noncanonical workspace artifact path: ' + relative)
    target = ROOT
    for part in parts:
        target = target / part
        require(not target.is_symlink(), 'symlink artifact path: ' + relative)
    require(target.is_file(), 'missing or nonregular artifact: ' + relative)
    return target


def desc(path):
    relative = path.relative_to(ROOT).as_posix()
    raw = workspace_file(relative).read_bytes()
    return {'path': relative, 'sha256': sha(raw), 'bytes': len(raw)}


def verify(row):
    require(isinstance(row, dict) and set(row) == {'path', 'sha256', 'bytes'},
            'expected an exact path/SHA/bytes artifact descriptor')
    require(desc(ROOT / row['path']) == row, 'artifact binding mismatch: ' + row['path'])


def load(row):
    verify(row)
    return json.loads((ROOT / row['path']).read_bytes())


def emit_receipt(receipt, receipt_path):
    print('*** Begin Patch\n*** Add File: ' + str(receipt_path))
    for line in (json.dumps(receipt, ensure_ascii=False, indent=2,
                            sort_keys=True) + '\n').splitlines():
        print('+' + line)
    print('*** End Patch')


def main(paper_id):
    require(paper_id == 'P29', 'this builder accepts only P29')
    pdf_path = NOTES / (JOB + '.pdf')
    log_path = NOTES / (JOB + '.build.log')
    transcript_path = NOTES / (JOB + '.build.transcript.log')
    receipt_path = NOTES / (JOB + '_build_receipt.json')
    # A collision is not a new attempt: preserve the existing run in place.
    for target in (pdf_path, log_path, transcript_path, receipt_path):
        require(not target.exists() and not target.is_symlink(),
                'refusing overwrite: ' + str(target))
    require(NOTES.is_dir() and not NOTES.is_symlink(), 'unsafe/missing P29 notes directory')

    application_desc = authority_desc = request_desc = bibliography = None
    predecessor_desc = helper_desc = None
    paper = {}
    frozen, records, transcript, failures = {}, [], [], []
    before = after = compile_dir = boundary_replay = None
    compile_sha = page_count = page_size = pdf_text_sha = None
    latex_log = b''
    diagnostics = {key: None for key in (
        'undefined_citations', 'undefined_references', 'missing_glyphs',
        'fatal_errors', 'overfull_hboxes',
    )}

    def fail(code, detail):
        failures.append({'code': code, 'detail': str(detail)})
        transcript.append('\n' + code + ': ' + str(detail) + '\n')

    def freeze(row):
        verify(row)
        require(row['path'] not in frozen or frozen[row['path']] == row,
                'conflicting descriptors: ' + row['path'])
        frozen[row['path']] = dict(row)

    def command(argv, env, timeout):
        try:
            result = subprocess.run(argv, cwd=compile_dir, env=env,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                    timeout=timeout)
            output, code = result.stdout, result.returncode
            error_output = result.stderr
        except subprocess.TimeoutExpired as exc:
            output = exc.stdout or b''
            error_output = (exc.stderr or b'') + b'\nCOMMAND TIMEOUT\n'
            code = 124
        except OSError as exc:
            output = b''
            error_output = (type(exc).__name__ + ': ' + str(exc) + '\n').encode('utf-8')
            code = 127
        records.append({'argv': argv, 'exit_code': code})
        transcript.extend(['$ ' + ' '.join(argv) + '\n',
                           output.decode('utf-8', errors='replace'),
                           error_output.decode('utf-8', errors='replace'), '\n'])
        return code, output

    try:
        application_desc = desc(ROOT / APPLICATION)
        application = load(application_desc)
        require(application.get('paper_id') == 'P29', 'application is not P29-only')
        authority_desc = application['authority']
        require(authority_desc['path'] == AUTHORITY, 'wrong current authority path')
        authority = load(authority_desc)
        request_desc = authority['confirmed_request']
        require(request_desc['path'] == REQUEST and request_desc['sha256'] == REQUEST_SHA,
                'current authority does not bind the approved B0006 request')
        request = load(request_desc)
        require(isinstance(application['paper'], dict), 'application paper must be an object')
        paper = application['paper']
        if 'paper_id' in paper:
            require(paper['paper_id'] == 'P29', 'nested paper identity mismatch')
        for key in PAPER_BINDINGS:
            require(paper[key]['path'].startswith(PAPER + '/notes/'),
                    'non-P29 notes input: ' + key)
            freeze(paper[key])
        require(paper['successor'] == {
            'path': PAPER + '/notes/' + JOB + '.tex',
            'sha256': DRAFT_SHA, 'bytes': DRAFT_BYTES,
        }, 'round5 successor differs from the approved expected bytes')
        require(paper['successor']['path'] == request['named_successor'],
                'request/application successor path mismatch')
        require(paper['apply_report']['path'] == PAPER + '/notes/' + JOB + '.tex.apply-report.json'
                and paper['block_manifest']['path'] == PAPER + '/notes/' + JOB + '.block-manifest.json',
                'application contains a non-round5 apply report or block manifest')
        require(paper['approved_patch'] == request['patch']
                and paper['approved_patch']['sha256'] == PATCH_SHA,
                'request/application exact patch mismatch')
        require(paper['revision_evidence_bundle']['path'] == request['named_successor_bundle'],
                'request/application revision bundle path mismatch')
        applied = load(paper['apply_report'])
        require(applied.get('patch_digest') == PATCH_SHA
                and applied.get('output_path') == str(ROOT / paper['successor']['path'])
                and applied.get('output_draft_hash') == DRAFT_SHA[:12]
                and applied.get('revision_round') == 5,
                'apply report does not bind the approved round5 patch/output')
        bundle = load(paper['revision_evidence_bundle'])
        require(bundle.get('final_draft') == {
            'path': 'notes/' + JOB + '.tex', 'sha256': DRAFT_SHA,
        } and len(bundle.get('rounds', [])) == 5
                and bundle['rounds'][-1].get('revision_round') == 5
                and bundle['rounds'][-1].get('kind') == 'integrity_correction',
                'revision bundle does not end at the exact round5 integrity correction')
        lock_desc = desc(ROOT / LOCK)
        require(lock_desc['sha256'] == LOCK_SHA, 'protected input lock changed')
        lock = load(lock_desc)
        locked_papers = [row for row in lock['papers'] if row['paper_id'] == 'P29']
        require(len(locked_papers) == 1, 'P29 lock population mismatch')
        bibliography = application['bibliography']
        require(bibliography == locked_papers[0]['audit_bibliography'],
                'P29 bibliography differs from its unchanged locked input')
        freeze(bibliography)
        predecessor_desc = desc(ROOT / PREDECESSOR_BUILDER)
        helper_desc = desc(ROOT / BOUNDARY_HELPER)
        require(predecessor_desc['sha256'] == PREDECESSOR_BUILDER_SHA,
                'retained predecessor builder changed')
        require(helper_desc['sha256'] == BOUNDARY_HELPER_SHA,
                'read-only protected-boundary helper changed')
        for row in (application_desc, authority_desc, request_desc, lock_desc,
                    predecessor_desc, helper_desc, desc(Path(__file__).resolve())):
            freeze(row)
        helpers = runpy.run_path(str(ROOT / BOUNDARY_HELPER),
                                 run_name='p29_b0006_read_only_boundary_helpers')
        boundary_replay = helpers['protected_boundary_replay']
        before = boundary_replay()
        require(before['locked_file_bindings_replayed'] == 119
                and len(before['science_trees']) == 15,
                'protected-boundary population mismatch')

        original = (ROOT / paper['successor']['path']).read_bytes()
        # Byte regex avoids universal-newline or Unicode normalization.
        marker_free = re.sub(rb'(?m)^<!--block:B[0-9]+-->(?:\r?\n|$)', b'', original)
        compile_sha = sha(marker_free)
        compile_dir = Path(tempfile.mkdtemp(prefix='round10-p29-b0006-round5-'))
        (compile_dir / 'manuscript.tex').write_bytes(marker_free)
        shutil.copyfile(ROOT / bibliography['path'], compile_dir / 'references.bib')
        env = os.environ.copy()
        env.update(ENVIRONMENT)
        latex = ['/usr/bin/lualatex', '-no-shell-escape', '-interaction=nonstopmode',
                 '-halt-on-error', '-jobname=' + JOB, 'manuscript.tex']
        for argv in (latex, ['/usr/bin/bibtex', JOB], latex, latex):
            code, _ = command(argv, env, 120)
            if code:
                fail('COMPILER_COMMAND_FAILED', 'exit ' + str(code))
                break
        temp_log = compile_dir / (JOB + '.log')
        latex_log = temp_log.read_bytes() if temp_log.is_file() else b''
        log_text = latex_log.decode('utf-8', errors='replace')
        diagnostics = {
            'undefined_citations': len(re.findall(r"Citation [`'][^\n]+ undefined|There were undefined citations", log_text, re.I)),
            'undefined_references': len(re.findall(r"Reference [`'][^\n]+ undefined|There were undefined references", log_text, re.I)),
            'missing_glyphs': log_text.count('Missing character:'),
            'fatal_errors': len(re.findall(r'Fatal error|Emergency stop', log_text, re.I)),
            'overfull_hboxes': log_text.count('Overfull \\hbox'),
        }
        if not latex_log:
            fail('MISSING_FINAL_LATEX_LOG', str(temp_log))
        if any(diagnostics.values()):
            fail('NON_CLEAN_FINAL_LATEX_LOG', diagnostics)
        temp_pdf = compile_dir / (JOB + '.pdf')
        if not temp_pdf.is_file() or temp_pdf.stat().st_size == 0:
            fail('MISSING_PDF', str(temp_pdf))
        if not failures:
            for argv in (['/usr/bin/pdfinfo', str(temp_pdf)],
                         ['/usr/bin/pdftotext', str(temp_pdf), '-']):
                code, output = command(argv, env, 60)
                if code:
                    fail('PDF_READBACK_FAILED', 'exit ' + str(code))
                    break
                text = output.decode('utf-8', errors='replace')
                if argv[0].endswith('pdfinfo'):
                    count = re.search(r'^Pages:\s+(\d+)', text, re.M)
                    size = re.search(r'^Page size:\s+(.+)$', text, re.M)
                    page_count = int(count.group(1)) if count else None
                    page_size = size.group(1) if size else None
                    if not page_count or not page_size:
                        fail('PDF_PAGE_INFORMATION_UNAVAILABLE', text)
                        break
                else:
                    pdf_text_sha = sha(output)
                    if not text.strip():
                        fail('EMPTY_PDF_TEXT', str(temp_pdf))
    except Exception as exc:
        fail('INPUT_OR_BUILD_EXCEPTION', type(exc).__name__ + ': ' + str(exc))
    finally:
        # Every accepted input is compared again, including authority and code.
        for row in frozen.values():
            try:
                verify(row)
            except Exception as exc:
                fail('INPUT_BINDING_DRIFT', exc)
        if before is not None and boundary_replay is not None:
            try:
                after = boundary_replay()
                require(before == after, 'protected boundary drift during preview')
            except Exception as exc:
                fail('PROTECTED_BOUNDARY_FAILURE', exc)
        if compile_dir is not None:
            temp_log = compile_dir / (JOB + '.log')
            if temp_log.is_file():
                latex_log = temp_log.read_bytes()

    # Exclusive writes preserve every previous attempt; never publish a failed PDF.
    log_desc = transcript_desc = preview_desc = None
    try:
        with log_path.open('xb') as handle:
            handle.write(latex_log)
        log_desc = desc(log_path)
        with transcript_path.open('xb') as handle:
            handle.write(''.join(transcript).encode('utf-8'))
        transcript_desc = desc(transcript_path)
        if not failures:
            with temp_pdf.open('rb') as source, pdf_path.open('xb') as target:
                shutil.copyfileobj(source, target)
            preview_desc = desc(pdf_path)
    except Exception as exc:
        fail('ARTIFACT_PUBLICATION_FAILED', type(exc).__name__ + ': ' + str(exc))

    receipt = {
        'schema_version': 'round10-exact-patch-isolated-preview-build/1.0',
        'paper_id': 'P29',
        'built_at_utc': datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z'),
        'status': 'FAIL' if failures else 'PASS_CLEAN',
        'failure_reason': failures[0]['code'] if failures else None,
        'failure_details': failures,
        'authority': authority_desc,
        'confirmed_request': request_desc,
        'application_receipt': application_desc,
        'builder': desc(Path(__file__).resolve()),
        'predecessor_builder': predecessor_desc,
        'protected_boundary_helper': helper_desc,
        'input_draft': paper.get('successor'),
        'approved_patch': paper.get('approved_patch'),
        'official_apply_report': paper.get('apply_report'),
        'bibliography': bibliography,
        'revision_evidence_bundle': paper.get('revision_evidence_bundle'),
        'commands': records,
        'diagnostics': diagnostics,
        'pages': page_count,
        'page_size': page_size,
        'pdf_readback_text_sha256': pdf_text_sha,
        'preview': preview_desc,
        'final_latex_log': log_desc,
        'transcript': transcript_desc,
        'temporary_compile_directory': str(compile_dir) if compile_dir else None,
        'temporary_files_retained': compile_dir is not None,
        'compile_source_sha256': compile_sha,
        'marker_stripping': 'Only whole ARS block-marker lines removed in temporary formatting copy; all other source bytes unchanged.',
        'citation_style': 'natbib[numbers,sort&compress] + plainnat numeric',
        'environment_overrides': ENVIRONMENT,
        'protected_snapshot_unchanged': before is not None and after is not None and before == after,
        'protected_locked_bindings': after['locked_file_bindings_replayed'] if after is not None else None,
        'canonical_or_scientific_mutations': False,
        'stage4_5_round3_run': False,
        'stage5_or_stage6_run': False,
        'classification': 'P29_B0006_NOTES_SIDE_ROUND5_CORRECTION_PREVIEW_NOT_FINAL_MANUSCRIPT',
        'receipt_persistence': 'Printed apply_patch payload; orchestrator must preserve these actual bytes even on build failure.',
    }
    emit_receipt(receipt, receipt_path)
    return 1 if failures else 0


if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] != 'P29':
        raise SystemExit('usage: build_round10_p29_b0006_preview.py P29')
    try:
        raise SystemExit(main(sys.argv[1]))
    except (OSError, RuntimeError) as exc:
        # No-clobber refusal preserves the already existing attempt unchanged.
        print('P29 PREVIEW PRECONDITION REFUSED: ' + str(exc), file=sys.stderr)
        raise SystemExit(2)
