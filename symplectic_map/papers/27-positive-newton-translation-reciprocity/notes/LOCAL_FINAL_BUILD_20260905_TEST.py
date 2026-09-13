"""Pure-memory regression tests; no build/evidence path is opened."""
import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch
import io
import subprocess
import signal

SCRIPT = Path(__file__).with_name('LOCAL_FINAL_BUILD_20260905.py')
spec = importlib.util.spec_from_file_location('local_build', SCRIPT)
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)


def synthetic_text():
    first = '\n'.join((build.TITLE, 'Anonymous', 'Abstract') + build.HEADINGS +
        build.CLAUSES + build.BOUNDARIES + ('P1 P2 P3 Q1 Q2 Q3', build.CONCLUSION))
    pages = [first] + ['Synthetic proof-content fixture. ' * 8 for _ in range(23)]
    pages += ['References\n' + '\n'.join('[%d] Synthetic reference.' % i for i in range(1, 21))]
    return ('\f'.join(pages) + '\f').encode()


class ContractTests(unittest.TestCase):
    def test_normal_diagnostic_header(self):
        body = b'BATCH07_REFERENCE_START_PAGE=25\nOutput written on main.pdf (26 pages, 123 bytes).\n'
        for prefix in (b'file:line:error style messages enabled.\n', b' file:line:error style messages enabled.\n'):
            self.assertEqual(build.log_check(prefix + body, 123)['proof_pages'], 24)
        with self.assertRaises(build.Stop):
            build.log_check(b'file:line:error style messages enabled. REAL ERROR\n' + body, 123)

    def test_recorder_dot_spelling(self):
        data = b'PWD /synthetic/r0\nINPUT main.tex\nINPUT ./math_commands.tex\nINPUT ./main.aux\nOUTPUT main.aux\nOUTPUT main.log\nOUTPUT main.pdf\n'
        build.recorder_check(data, Path('/synthetic/r0'), set(), 3)
        for bad in (b'../main.aux', b'./../main.aux', b'././main.aux'):
            with self.assertRaises(build.Stop):
                build.recorder_check(data.replace(b'INPUT ./main.aux', b'INPUT ' + bad), Path('/synthetic/r0'), set(), 3)

    def test_no_known_proof_anchor_after_references(self):
        for token in build.HEADINGS + build.CLAUSES + build.BOUNDARIES + (build.CONCLUSION,):
            data = synthetic_text() + (token + ' Synthetic extra proof.\f').encode()
            with self.assertRaises(build.Stop):
                build.text_check(data, {'total_pages': 26, 'reference_page': 25})

    def fake_command(self, outcomes, signaling_error=None):
        class FakeProcess:
            pid = 123456
            returncode = None
            stdout = io.BytesIO()
            stderr = io.BytesIO()
            def communicate(self, timeout):
                outcome = outcomes.pop(0)
                if isinstance(outcome, BaseException):
                    raise outcome
                self.returncode = outcome
                return b'captured', b''
            def wait(self, timeout):
                if self.returncode is None:
                    raise subprocess.TimeoutExpired('synthetic', timeout)
                return self.returncode
        proc = FakeProcess()
        writes = {}
        with patch.object(build.subprocess, 'Popen', return_value=proc), \
             patch.object(build, 'write_new', side_effect=lambda p, d, *args: writes.__setitem__(p.name, d)), \
             patch.object(build.os, 'killpg', side_effect=signaling_error) as kill:
            try:
                build.run_command(Path('/synthetic'), 'TEST', ('synthetic',), Path('/synthetic'), {})
                caught = None
            except BaseException as exc:
                caught = exc
        self.assertTrue(proc.stdout.closed and proc.stderr.closed)
        return caught, writes, kill.call_args_list

    def test_child_cancellation_cleanup(self):
        caught, writes, signals = self.fake_command([KeyboardInterrupt(), -15])
        self.assertIsInstance(caught, KeyboardInterrupt)
        self.assertEqual(signals[0].args, (123456, signal.SIGTERM))
        self.assertEqual(writes['TEST.status'], b'-15\n')

    def test_child_exited_group_race(self):
        caught, writes, signals = self.fake_command([KeyboardInterrupt(), 0], ProcessLookupError())
        self.assertIsInstance(caught, KeyboardInterrupt)
        self.assertEqual(writes['TEST.status'], b'0\n')

    def test_child_timeout_escalation(self):
        timeout = subprocess.TimeoutExpired('synthetic', 190)
        caught, writes, signals = self.fake_command([timeout, timeout, -9])
        self.assertIsInstance(caught, subprocess.TimeoutExpired)
        self.assertEqual([call.args[1] for call in signals], [signal.SIGTERM, signal.SIGKILL])
        self.assertEqual(writes['TEST.status'], b'-9\n')

    def test_unreaped_child_is_hold(self):
        timeout = subprocess.TimeoutExpired('synthetic', 190)
        caught, writes, signals = self.fake_command([timeout, timeout, timeout])
        self.assertIsInstance(caught, build.ChildUnreaped)
        self.assertEqual(writes['TEST.status'], b'UNKNOWN\n')

    def test_child_success(self):
        caught, writes, signals = self.fake_command([0])
        self.assertIsNone(caught)
        self.assertEqual(signals, [])
        self.assertEqual(writes['TEST.stdout'], b'captured')

    def test_synthetic_text_positive(self):
        data = synthetic_text()
        self.assertEqual(build.text_check(data, {'total_pages': 25, 'reference_page': 25}), build.sha(data))

    def test_text_missing_requirements(self):
        for token in (build.TITLE, 'Anonymous', 'Abstract', *build.HEADINGS,
                      *build.CLAUSES, 'Q3', build.CONCLUSION):
            with self.subTest(token=token):
                data = synthetic_text().replace(token.encode(), b'MISSING')
                with self.assertRaises(build.Stop):
                    build.text_check(data, {'total_pages': 25, 'reference_page': 25})

    def test_text_bad_reference_counts(self):
        for old, new in ((b'[20]', b'[21]'), (b'[20]', b'[19]'), (b'[20]', b'20.'),
                         (b'References\n', b'Bibliography\n')):
            with self.subTest(new=new):
                with self.assertRaises(build.Stop):
                    build.text_check(synthetic_text().replace(old, new), {'total_pages': 25, 'reference_page': 25})

    def test_text_internal_tokens(self):
        for token in (*build.PROVENANCE, 'private@example.org', '??', '[?]', '[VERIFY]', '\ufffd'):
            with self.subTest(token=token):
                data = synthetic_text().replace(b'Abstract', ('Abstract ' + token).encode())
                with self.assertRaises(build.Stop):
                    build.text_check(data, {'total_pages': 25, 'reference_page': 25})

    def test_reference_page_drift(self):
        with self.assertRaises(build.Stop):
            build.text_check(synthetic_text(), {'total_pages': 25, 'reference_page': 24})

    def test_blank_proof_page(self):
        data = synthetic_text().split(b'\f')
        data[7] = b'8\n'
        with self.assertRaises(build.Stop):
            build.text_check(b'\f'.join(data), {'total_pages': 25, 'reference_page': 25})

    def test_log_boundaries(self):
        for proof in (24, 25, 26, 27, 28):
            log = ('BATCH07_REFERENCE_START_PAGE=%d\nOutput written on main.pdf (%d pages, 123 bytes).\n' % (proof + 1, proof + 2)).encode()
            self.assertEqual(build.log_check(log, 123)['proof_pages'], proof)

    def test_warning_not_hidden(self):
        log = b'BATCH07_REFERENCE_START_PAGE=25\nUnderfull \\hbox (badness 1000) in paragraph at lines 1--2\nOutput written on main.pdf (26 pages, 123 bytes).\n'
        report = build.log_check(log, 123)
        self.assertEqual(report['warnings'], [{'line': 2, 'text': log.decode().splitlines()[1]}])

    def test_exact_env(self):
        env = build.publication_env(Path('/synthetic/r0'))
        self.assertEqual(len(env), 11)
        self.assertEqual(list(env), sorted(env))
        self.assertNotIn('HOME', env)
        self.assertEqual(env['SOURCE_DATE_EPOCH'], '0')

    def test_citations_pure_mock(self):
        keys = sorted(build.KEYS)
        files = {
            'main.tex': ('\\cite{' + ','.join(keys) + '}').encode(),
            'references.bib': '\n'.join('@article{%s, title={Synthetic}}' % key for key in keys).encode(),
            'main.aux': ('\\citation{' + ','.join(keys) + '}').encode(),
            'main.bbl': '\n'.join('\\bibitem{%s} Synthetic' % key for key in keys).encode(),
            'main.blg': b'The style file: plain.bst\nDatabase file #1: references.bib\nand the built_in function-call counts, 0 in all, are:\nwarning$ -- 0\n',
        }
        def fake_read(path, *args):
            return files[path.name]
        with patch.object(build, 'read_file', side_effect=fake_read):
            build.citation_check(Path('/synthetic'))
            files['main.bbl'] += ('\n\\bibitem{%s} Duplicate' % keys[0]).encode()
            with self.assertRaises(build.Stop):
                build.citation_check(Path('/synthetic'))


    def test_bib_zero_counter_only(self):
        good = 'The style file: plain.bst\nDatabase file #1: references.bib\nand the built_in function-call counts, 2 in all, are:\nwarning$ -- 0\nwrite$ -- 2\n'
        build.bib_log_check(good)
        cases = [good.replace('warning$ -- 0', bad) for bad in
                 ('warning$ -- 1', 'warning$ -- 00', ' warning$ -- 0', 'warning$ -- 0 REAL WARNING',
                  'warning$ -- 0\nwarning$ -- 0', '')]
        cases += ['Warning--missing entry\n' + good, 'Error: malformed entry\n' + good,
                  'undefined\n' + good, good + 'diagnostic after counters\n',
                  good.replace('and the built_in function-call counts, 2 in all, are:\n', '')]
        for case in cases:
            with self.subTest(case=case):
                with self.assertRaises(build.Stop):
                    build.bib_log_check(case)

    def test_raw_boundaries_literal_and_wrapped(self):
        counts = {'total_pages': 25, 'reference_page': 25}
        data = synthetic_text()
        self.assertEqual(len(build.boundary_text_check(data, counts)['boundary_labels']), 7)
        for label, variant in build.BOUNDARY_WRAPS.items():
            data = data.replace(label.encode(), variant.replace(' ', '\n').encode())
        self.assertEqual(len(build.boundary_text_check(data, counts)['boundary_labels']), 7)

    def test_raw_boundaries_missing_duplicate_order_or_after_refs(self):
        counts = {'total_pages': 25, 'reference_page': 25}
        data = synthetic_text()
        cases = []
        for label in build.BOUNDARIES:
            cases += [data.replace(label.encode(), b'MISSING'),
                      data.replace(label.encode(), (label + '\n' + label).encode()),
                      data.replace(label.encode(), b'MOVED').replace(b'References\n', ('References\n' + label + '\n').encode()),
                      data.replace(b'References\n', ('References\n' + label + '\n').encode())]
        cases += [data.replace(b'Positive coordinates', b'Literal reflected label').replace(b'Literal reflected label\nPositive', b'Positive coordinates\nPositive'),
                  data.replace(b'8 Boundaries and conclusion', b'MISSING SECTION'),
                  data.replace(b'References\n', b'Bibliography\n'),
                  data.replace(b'Positive coordinates', b'Positive coo- dinates'),
                  data.replace(b'Positive-support cancellation control', b'Positivesupport cancellation control')]
        for case in cases:
            with self.subTest(case=case[:80]):
                with self.assertRaises(build.Stop):
                    build.boundary_text_check(case, counts)


if __name__ == '__main__':
    unittest.main(verbosity=2)

