#!/usr/bin/env python3
"""Prospective static check source. Not executed or imported in preparation.

This checks literal source text and AST shape only if root separately
authorizes diagnostics. It is not mathematical verification, a native build,
a complete dependency trace, a root-read receipt or a manuscript review.
"""
import ast
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
NAMES = ('build_core.py', 'prepare_build.py', 'build_p211.py',
         'launch_build.py', 'static_checks.py')


def main():
    findings = []
    for name in NAMES:
        raw = (HERE / name).read_bytes()
        tree = ast.parse(raw, filename=str(HERE / name))
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                assert node.func.attr not in ('unlink', 'rmdir', 'rmtree', 'rename'), name
                assert not (node.func.attr == 'replace' and
                            isinstance(node.func.value, ast.Name) and
                            node.func.value.id == 'os'), name
        findings.append({'file': name, 'ast_no_named_delete_or_rename': True})
    core = (HERE / 'build_core.py').read_text()
    inner = (HERE / 'build_p211.py').read_text()
    outer = (HERE / 'launch_build.py').read_text()
    assert "'HOME':" not in core and "'SOURCE_DATE_EPOCH': '1788825600'" in core
    assert "('pass1', TEX_COMMAND)" in core and "('pass3', TEX_COMMAND)" in core
    assert 'NO_NATIVE_HANDLE_UNKNOWN_LAUNCH' in core and 'incomplete_native(root)' in core
    assert "'cold_build_' + str(number)" in inner and 'number in (1, 2)' in inner
    assert "binding.get('enabled') is True" in inner
    assert 'host_candidate_extension' in inner and 'round2_files(binding)' in inner
    assert 'TERMINAL_BUILD_RECORDED_NOT_VIEWED_NOT_ACCEPTED' in inner
    assert 'TERMINAL_BUILD_CAPTURED_PENDING_ROOT_INSPECTION' in outer
    assert 'diagnostic_capture' not in outer
    print(json.dumps({'status': 'STATIC_TEXT_AST_ONLY_NOT_A_BUILD_OR_ACCEPTANCE',
                      'findings': findings, 'native_children': 0,
                      'scientific_executions': 0, 'tex_compilations': 0,
                      'actual_page_views': 0, 'acceptance': False}, sort_keys=True))


if __name__ == '__main__':
    main()
