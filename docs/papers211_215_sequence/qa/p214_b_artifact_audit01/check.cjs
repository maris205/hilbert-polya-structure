'use strict';

const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');

const W = '/root/autodl-tmp/symbolic_dynamics';
const R = W + '/docs/papers211_215_sequence/reviews/p214_b/build02';
const P = W + '/docs/papers211_215_sequence/qa/p214_b_build_preparation02';
const B = W + '/docs/papers211_215_sequence/qa/p214_b_build_binding02';
const F = W + '/papers/214-nilpotent-bilinear-clock/frozen_round1';
const L = W + '/papers/214-nilpotent-bilinear-clock';
const BUILD01 = W + '/docs/papers211_215_sequence/reviews/p214_b/build01';
const sourceNames = [
  'main.tex', 'math_commands.tex', 'references.bib',
  'sections/0_abstract.tex', 'sections/1_setup.tex',
  'sections/2_clock.tex', 'sections/3_fibres.tex',
  'sections/4_controls.tex', 'sections/5_scope.tex'
];
const products = [
  'main.aux', 'main.bbl', 'main.blg', 'main.log',
  'main.fls', 'main.out', 'main.toc', 'main.pdf'
];
const commandRoles = [
  'pass1', 'bibtex', 'pass2', 'pass3', 'pdfinfo', 'pdffonts',
  'pdftotext', 'final_diagnostics',
  ...Array.from({length: 7}, (_, i) => 'page-' + String(i + 1).padStart(4, '0'))
];
const passRoles = ['pass1', 'bibtex', 'pass2', 'pass3'];
let checks = 0;
function need(value, label) {
  checks++;
  if (!value) throw new Error(label);
}
function read(file) { return fs.readFileSync(file); }
function text(file) {
  const body = read(file);
  const decoded = body.toString('utf8');
  need(Buffer.from(decoded, 'utf8').equals(body), 'lossless UTF-8 ' + file);
  return decoded;
}
function digest(body) {
  return crypto.createHash('sha256').update(body).digest('hex');
}
function sha(file) { return digest(read(file)); }
function same(left, right, label) {
  need(read(left).equals(read(right)), 'RAW equality ' + label);
}
function rows(file) {
  const value = text(file);
  need(value.endsWith('\n') && !value.includes('\r'), 'LF manifest ' + file);
  const parsed = value.slice(0, -1).split('\n').map((line) => {
    const match = /^([0-9a-f]{64})  (.+)$/.exec(line);
    need(match, 'manifest syntax ' + line);
    return {sha256: match[1], path: match[2]};
  });
  need(new Set(parsed.map((row) => row.path)).size === parsed.length,
    'unique manifest paths ' + file);
  return parsed;
}

const inventory = [];
const directories = [];
function walk(directory, relative = '') {
  const stat = fs.lstatSync(directory);
  need(stat.isDirectory() && !stat.isSymbolicLink(), 'ordinary directory ' + relative);
  directories.push(relative);
  for (const entry of fs.readdirSync(directory, {withFileTypes: true})
    .sort((a, b) => a.name.localeCompare(b.name))) {
    const rel = relative + entry.name;
    const full = directory + '/' + entry.name;
    need(!entry.isSymbolicLink(), 'no symlink ' + rel);
    if (entry.isDirectory()) {
      walk(full, rel + '/');
    } else {
      need(entry.isFile(), 'regular file ' + rel);
      const body = read(full);
      inventory.push({path: rel, bytes: body.length, sha256: digest(body)});
    }
  }
}
walk(R);
need(inventory.length === 171, 'exact 171 files');
need(new Set(inventory.map((item) => item.path)).size === 171, 'unique output members');
const expectedDirectories = [
  '', 'pages/', 'pass_artifacts/', 'raw/', 'source_only/', 'source_only/sections/',
  ...passRoles.flatMap((role) => [
    'pass_artifacts/' + role + '.before/',
    'pass_artifacts/' + role + '.after/'
  ])
].sort();
need(JSON.stringify(directories.slice().sort()) === JSON.stringify(expectedDirectories),
  'exact 14-directory shape');
const names = new Set(inventory.map((item) => item.path));
const item = (name) => {
  need(names.has(name), 'recorded artifact ' + name);
  return inventory.find((entry) => entry.path === name);
};

need(text(R + '/controller.exit') === '0\n', 'controller zero');
need(read(R + '/controller.stdout.raw').length === 0, 'controller stdout empty');
for (const role of commandRoles) {
  need(text(R + '/raw/' + role + '.supervisor_exit') === '0\n', role + ' zero');
  need(read(R + '/raw/' + role + '.stderr.raw').length === 0, role + ' stderr empty');
  const request = text(R + '/raw/' + role + '.request.txt');
  need(request.startsWith('cwd=' + R + '/source_only\n'), role + ' cwd');
  need(request.includes('supervisor_argv=/usr/bin/timeout '), role + ' timeout request');
}
for (const role of passRoles) {
  need(read(R + '/raw/' + role + '.sources.stderr').length === 0,
    role + ' source stderr empty');
}
const stderrFiles = inventory.filter((entry) => entry.path.includes('stderr'));
need(stderrFiles.length === 28, 'exact 28 stderr files');
for (const entry of stderrFiles) need(entry.bytes === 0, 'empty stderr ' + entry.path);

const sourceManifest = rows(R + '/SOURCE_EXPECTED.sha256');
const runtimeManifest = rows(R + '/RUNTIME_EXPECTED.sha256');
const scienceManifest = rows(R + '/SCIENCE_AND_HISTORY_INPUTS.sha256');
need(sourceManifest.length === 9, 'nine source rows');
need(runtimeManifest.length === 223, '223 runtime rows');
need(scienceManifest.length === 7, 'seven science/history rows');
same(R + '/SOURCE_EXPECTED.sha256', P + '/SOURCE_EXPECTED.sha256', 'captured source manifest');
same(R + '/RUNTIME_EXPECTED.sha256',
  W + '/docs/papers211_215_sequence/qa/p214_a_build_binding02/RUNTIME_INPUTS.sha256',
  'captured runtime manifest');
same(R + '/SCIENCE_AND_HISTORY_INPUTS.sha256',
  P + '/SCIENCE_AND_HISTORY_INPUTS.sha256', 'captured science manifest');
for (const row of sourceManifest) {
  need(sourceNames.includes(row.path), 'known source ' + row.path);
  need(sha(R + '/source_only/' + row.path) === row.sha256, 'cold source ' + row.path);
  need(sha(F + '/' + row.path) === row.sha256, 'Round1 source ' + row.path);
}
for (const row of runtimeManifest) {
  need(path.isAbsolute(row.path), 'absolute runtime path');
  need(sha(row.path) === row.sha256, 'current runtime content ' + row.path);
}
for (const row of scienceManifest) {
  need(!path.isAbsolute(row.path), 'workspace-relative science path');
  need(sha(W + '/' + row.path) === row.sha256, 'science/history content ' + row.path);
}
const sourceOK = sourceManifest.map((row) => row.path + ': OK\n').join('');
for (const role of ['source.before', 'source.after', 'cold_source.initial', 'cold_source.final']) {
  need(text(R + '/' + role + '.stdout') === sourceOK, role + ' complete output');
  need(read(R + '/' + role + '.stderr').length === 0, role + ' empty stderr');
}
const runtimeOK = runtimeManifest.map((row) => row.path + ': OK\n').join('');
need(text(R + '/runtime.before.stdout') === runtimeOK, 'runtime before complete');
need(text(R + '/runtime.after.stdout') === runtimeOK, 'runtime after complete');
const scienceOK = scienceManifest.map((row) => row.path + ': OK\n').join('');
need(text(R + '/science.before.stdout') === scienceOK, 'science before complete');
need(text(R + '/science.after.stdout') === scienceOK, 'science after complete');

const requestRows = rows(R + '/REQUEST_AND_BINDING.sha256');
need(requestRows.length === 3, 'three request/binding rows');
for (const row of requestRows) need(sha(row.path) === row.sha256,
  'request/binding content ' + row.path);
const actual = JSON.parse(text(B + '/ACTUAL_NATIVE.json'));
need(actual.exit_code === 0 && actual.chunk_id === '1e9d7d', 'actual granted build02');
need(actual.output_files_observed_postrun === 171 && actual.output_symlinks_observed_postrun === 0,
  'actual postrun inventory');
need(actual.pdf_sha256_observed_postrun ===
  'a1f95a79c607436ea062f136be50c208b5505ef79568d2df5e73f4ed83a5eed8',
  'actual postrun PDF identity');
need(text(BUILD01 + '/controller.exit') === '1\n', 'build01 remains HOLD exit 1');

for (const role of passRoles) {
  for (const when of ['before', 'after']) {
    const base = R + '/pass_artifacts/' + role + '.' + when;
    const present = fs.existsSync(base + '/PRESENT.sha256') ? rows(base + '/PRESENT.sha256') : [];
    const absent = text(base + '/ABSENT.txt').trim().split('\n').filter(Boolean);
    const partition = [...present.map((row) => row.path), ...absent].sort();
    need(JSON.stringify(partition) === JSON.stringify(products.slice().sort()),
      'snapshot product partition ' + role + '.' + when);
    for (const row of present) need(sha(base + '/' + row.path) === row.sha256,
      'snapshot body ' + role + '.' + when + '/' + row.path);
  }
}
same(R + '/pass_artifacts/pass1.after/main.aux',
  R + '/pass_artifacts/bibtex.before/main.aux', 'pass1 to bibtex AUX');
for (const name of ['main.aux', 'main.bbl', 'main.blg', 'main.fls', 'main.log', 'main.pdf']) {
  same(R + '/pass_artifacts/bibtex.after/' + name,
    R + '/pass_artifacts/pass2.before/' + name, 'bibtex to pass2 ' + name);
  same(R + '/pass_artifacts/pass2.after/' + name,
    R + '/pass_artifacts/pass3.before/' + name, 'pass2 to pass3 ' + name);
  same(R + '/pass_artifacts/pass3.after/' + name,
    R + '/source_only/' + name, 'pass3 final ' + name);
}

const finalProducts = rows(R + '/FINAL_PRODUCTS.sha256');
need(finalProducts.length === 6, 'six final products');
for (const row of finalProducts) need(sha(R + '/source_only/' + row.path) === row.sha256,
  'final product ' + row.path);
need(text(R + '/raw/final_diagnostics.stdout.raw') ===
  'main.log:3: file:line:error style messages enabled.\n', 'sole configuration diagnostic');
need(!/Overfull|Underfull|undefined|Missing character|Warning|^!/m.test(
  text(R + '/raw/final_diagnostics.stdout.raw')), 'no adverse final diagnostic');

const flsInputs = text(R + '/source_only/main.fls').split('\n')
  .filter((line) => line.startsWith('INPUT ')).map((line) => line.slice(6));
need(flsInputs.length === 243, '243 ordered FLS inputs');
const absoluteFls = [...new Set(flsInputs.filter(path.isAbsolute))];
need(absoluteFls.length === 58, '58 unique absolute FLS inputs');
const runtimeByPath = new Map(runtimeManifest.map((row) => [row.path, row.sha256]));
for (const file of absoluteFls) need(runtimeByPath.has(file), 'bound FLS input ' + file);

const fonts = text(R + '/raw/pdffonts.stdout.raw').trim().split('\n').slice(2);
need(fonts.length === 15, '15 fonts');
for (const line of fonts) need(/ yes yes yes\s+\d+\s+0$/.test(line), 'font flags ' + line);
need(text(R + '/PAGE_COUNT.txt') === '7\n', 'seven pages');
const pageRows = rows(R + '/PAGES.sha256');
need(pageRows.length === 7, 'seven page pins');
for (let index = 0; index < 7; index++) {
  const name = 'pages/page-' + String(index + 1).padStart(4, '0') + '.png';
  const row = pageRows[index];
  need(row.path === R + '/' + name, 'ordered page path ' + name);
  need(sha(row.path) === row.sha256, 'page hash ' + name);
  const png = read(row.path);
  need(png.readUInt32BE(16) === 1241 && png.readUInt32BE(20) === 1754,
    'page dimensions ' + name);
}
const pdf = R + '/source_only/main.pdf';
need(read(pdf).length === 191549, 'PDF bytes');
need(sha(pdf) === 'a1f95a79c607436ea062f136be50c208b5505ef79568d2df5e73f4ed83a5eed8',
  'PDF hash');
same(pdf, L + '/main.pdf', 'build02 PDF equals current live PDF');
same(pdf, F + '/main.pdf', 'build02 PDF equals frozen Round1 PDF');
const extracted = text(R + '/raw/pdftotext.stdout.raw');
for (const phrase of [
  'A cancellation-safe clock for nilpotent bilinear', 'The exact clock',
  'Complete one-step fibres', 'Multiplication and linear controls',
  '5,271 states', '10,646 records', 'Alexander Bors', 'El Houcein El Abdalaoui'
]) need(extracted.includes(phrase), 'extracted phrase ' + phrase);
const bbl = text(R + '/source_only/main.bbl');
need(bbl.includes('Bors2017') && bbl.includes('ElAbdalaouiEtAl2016'),
  'both bibliography keys');
need(text(R + '/STATUS.txt') ===
  'CAPTURED_PENDING_B_ARTIFACT_DATA_AND_ACTUAL_ALL_PAGE_RECEPTION\n', 'captured status');

const stableInventory = inventory.slice().sort((a, b) => a.path.localeCompare(b.path));
const result = {
  schema: 'P214_B_BUILD02_ARTIFACT_AUDIT_V1',
  status: 'PASS_CURRENT_ARTIFACT_ZERO_FINDINGS',
  reviewer: '/root/p212_round2_terminal_finish',
  checks,
  files: inventory.length,
  symlinks: 0,
  directories: directories.length,
  total_bytes: inventory.reduce((sum, entry) => sum + entry.bytes, 0),
  inventory_sha256: digest(Buffer.from(JSON.stringify(stableInventory) + '\n')),
  controller_exit: 0,
  supervised_zero_exits: commandRoles.length,
  empty_stderr_files: stderrFiles.length,
  source_rows: sourceManifest.length,
  science_history_rows: scienceManifest.length,
  runtime_rows: runtimeManifest.length,
  ordered_fls_inputs: flsInputs.length,
  unique_absolute_fls_inputs: absoluteFls.length,
  fonts: fonts.length,
  pages: pageRows.length,
  pdf_bytes: read(pdf).length,
  pdf_sha256: sha(pdf),
  pdf_raw_equal_live_and_round1: true,
  build01_credit_used: false,
  diagnostic_interpretation:
    'The sole 52-byte line enables file:line:error formatting; it is configuration text.',
  current_findings: [],
  current_open_census: {Critical: 0, Major: 0, Minor: 0}
};
process.stdout.write(JSON.stringify(result) + '\n');
