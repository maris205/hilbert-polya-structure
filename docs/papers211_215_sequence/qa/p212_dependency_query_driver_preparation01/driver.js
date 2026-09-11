'use strict';
// SOURCE ONLY. This file has NOT been executed, imported, checked as AST, or tested.
// Fresh implementation, not a transplant of an old builder/discovery controller.
// Default entry reads only its disabled companion, then refuses. An enabled
// external binding, received source and a PRE-startup native entry are separate gates.
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const childProcess = require('node:child_process');
const assert = require('node:assert/strict');
const ROOT = '/root/autodl-tmp/symbolic_dynamics';
const QA = ROOT + '/docs/papers211_215_sequence/qa';
const SELF = QA + '/p212_dependency_query_driver_preparation01/driver.js';
const QUERY_ROOT = QA + '/p212_build_dependency_query01';
const QUERY_CWD = QUERY_ROOT + '/query_cwd';
const BINDING_ROOT = QA + '/p212_build_dependency_binding01';
const ENV8 = {"PATH":"/usr/bin:/bin","LANG":"C.UTF-8","LC_ALL":"C.UTF-8","TZ":"UTC","SOURCE_DATE_EPOCH":"1788825600","FORCE_SOURCE_DATE":"1","openin_any":"p","openout_any":"p"};
const OLD_COMPANIONS = {
  "QUERY_FRONTIER.json": {
    "path": "docs/papers211_215_sequence/qa/p212_build_dependency_source_preparation01/QUERY_FRONTIER.json",
    "sha256": "762645257c2bea4f1d5c081de471cdee9eeb2b00dd312aab48d7dd4ed59cad1f"
  },
  "INTERFACE.disabled.json": {
    "path": "docs/papers211_215_sequence/qa/p212_build_dependency_source_preparation01/INTERFACE.disabled.json",
    "sha256": "2087003781dccd2bf4096031b903f0d2f9c5dfb833ae13407fd71af54dda10df"
  },
  "CAPTURE_CONTRACT.json": {
    "path": "docs/papers211_215_sequence/qa/p212_build_dependency_source_preparation01/CAPTURE_CONTRACT.json",
    "sha256": "6f6b122d844b778bdf5ed4a0a7ddb1ddd583136cbc77306a8f7f4f62abb1483b"
  },
  "SELECTOR_OBLIGATIONS.json": {
    "path": "docs/papers211_215_sequence/qa/p212_build_dependency_source_preparation01/SELECTOR_OBLIGATIONS.json",
    "sha256": "2f20ab8b0df5bb67ddea8610839655cd05128ae9192c567573bac2248400d960"
  }
};
// These complete fixed tuples are independent of later candidate JSON contents.
const SEEDS = [
  {
    "label": "class_article",
    "name": "article.cls",
    "program": "pdflatex",
    "engine": "pdftex",
    "role": "class source",
    "basis": "main.tex exact documentclass[10pt]{article}",
    "required": true
  },
  {
    "label": "package_01_geometry",
    "name": "geometry.sty",
    "program": "pdflatex",
    "engine": "pdftex",
    "role": "ordered direct package source",
    "basis": "main.tex package 1 options=[\"margin=0.85in\"]",
    "required": true
  },
  {
    "label": "package_02_amsmath",
    "name": "amsmath.sty",
    "program": "pdflatex",
    "engine": "pdftex",
    "role": "ordered direct package source",
    "basis": "main.tex package 2 options=[]",
    "required": true
  },
  {
    "label": "package_03_amssymb",
    "name": "amssymb.sty",
    "program": "pdflatex",
    "engine": "pdftex",
    "role": "ordered direct package source",
    "basis": "main.tex package 3 options=[]",
    "required": true
  },
  {
    "label": "package_04_amsthm",
    "name": "amsthm.sty",
    "program": "pdflatex",
    "engine": "pdftex",
    "role": "ordered direct package source",
    "basis": "main.tex package 4 options=[]",
    "required": true
  },
  {
    "label": "package_05_booktabs",
    "name": "booktabs.sty",
    "program": "pdflatex",
    "engine": "pdftex",
    "role": "ordered direct package source",
    "basis": "main.tex package 5 options=[]",
    "required": true
  },
  {
    "label": "package_06_array",
    "name": "array.sty",
    "program": "pdflatex",
    "engine": "pdftex",
    "role": "ordered direct package source",
    "basis": "main.tex package 6 options=[]",
    "required": true
  },
  {
    "label": "package_07_fontenc",
    "name": "fontenc.sty",
    "program": "pdflatex",
    "engine": "pdftex",
    "role": "ordered direct package source",
    "basis": "main.tex package 7 options=[\"T1\"]",
    "required": true
  },
  {
    "label": "package_08_hyperref",
    "name": "hyperref.sty",
    "program": "pdflatex",
    "engine": "pdftex",
    "role": "ordered direct package source",
    "basis": "main.tex package 8 options=[\"hidelinks\"]",
    "required": true
  },
  {
    "label": "style_plain",
    "name": "plain.bst",
    "program": "bibtex",
    "engine": "pdftex",
    "role": "BibTeX style source",
    "basis": "main.tex exact bibliographystyle{plain}; use BibTeX program search context",
    "required": true
  },
  {
    "label": "config_pdflatex_texmf",
    "name": "texmf.cnf",
    "program": "pdflatex",
    "engine": "pdftex",
    "role": "TeX search configuration candidate",
    "basis": "inherited query mechanism only; current whole body/search precedence remains to be received",
    "required": false
  },
  {
    "label": "config_bibtex_texmf",
    "name": "texmf.cnf",
    "program": "bibtex",
    "engine": "pdftex",
    "role": "BibTeX search configuration candidate",
    "basis": "separate effective BibTeX program context",
    "required": false
  },
  {
    "label": "format_pdflatex",
    "name": "pdflatex.fmt",
    "program": "pdflatex",
    "engine": "pdftex",
    "role": "opaque compiled-format dependency",
    "basis": "proposed pdflatex build; program/engine-specific lookup required by preserved old discovery failure",
    "required": true
  },
  {
    "label": "source_pdftexconfig",
    "name": "pdftexconfig.tex",
    "program": "pdflatex",
    "engine": "pdftex",
    "role": "format/configuration source candidate",
    "basis": "old explicit configuration seed, not assumed active or sufficient for new format",
    "required": false
  },
  {
    "label": "source_latex_kernel",
    "name": "latex.ltx",
    "program": "pdflatex",
    "engine": "pdftex",
    "role": "candidate kernel/NFSS source for manual semantics",
    "basis": "candidate explanatory body; equality to the dumped-format kernel is NOT established by current file presence",
    "required": false
  },
  {
    "label": "map_pdftex",
    "name": "pdftex.map",
    "program": "pdflatex",
    "engine": "pdftex",
    "role": "candidate map source",
    "basis": "old explicit map seed; actual map names/order must follow received configuration/source",
    "required": false
  },
  {
    "label": "config_fmtutil",
    "name": "fmtutil.cnf",
    "program": "pdflatex",
    "engine": "pdftex",
    "role": "format-construction configuration candidate",
    "basis": "historical explicit seed only; not permission to regenerate a format",
    "required": false
  },
  {
    "label": "config_updmap",
    "name": "updmap.cfg",
    "program": "pdflatex",
    "engine": "pdftex",
    "role": "font-map construction configuration candidate",
    "basis": "historical explicit seed only; not permission to regenerate maps",
    "required": false
  },
  {
    "label": "config_texfonts",
    "name": "texfonts.map",
    "program": "pdflatex",
    "engine": "pdftex",
    "role": "font-alias configuration candidate",
    "basis": "historical explicit seed only; actual use awaits source semantics",
    "required": false
  }
];
const VARIABLES = ['TEXMF','TEXMFCNF','TEXMFHOME','TEXMFCONFIG','TEXMFVAR',
  'TEXMFDBS','TEXINPUTS','BIBINPUTS','BSTINPUTS','shell_escape','openin_any','openout_any'];
const FLAGS = ['--no-mktex=tex','--no-mktex=fmt','--no-mktex=tfm','--no-mktex=pk'];
const LATER = 'LOOKUP_ONLY_AFTER_SEPARATE_OPTION_AND_RUNTIME_SOURCE_ACCEPTANCE';
const FORBIDDEN = {engine:false,bibtex:false,ldd:false,python:false,submitted_import:false,
  build:false,setup:false,science:false,recursive_discovery:false,lock:false,
  manuscript_review:false,visual_review:false,external:'HOLD_EXTERNAL'};
const EMPTY_CLOSURE = {class_configuration:null,ordered_package_graph:null,
  nfss_text_math_graph:null,metrics_virtual_fonts_maps_programs:null,
  dumped_format_provenance:null,configuration_databases:null,
  native_renderer_graph:null,actual_build_cwd_key:null,dependency_lock:null};
const STAT_KEYS = ['dev','ino','mode','nlink','uid','gid','rdev','size','blksize',
  'blocks','atimeNs','mtimeNs','ctimeNs','birthtimeNs'];
const IDENTITY_KEYS = ['dev','ino','mode','uid','gid','rdev'];
const RECEIPT_KEYS = ['plan_source','driver_source','prestartup','options','queries','body_scope'];
const INPUT_KEYS = ['path','role','kind','comparison','lstat','stat','resolved',
  'symlink_target','content','members'];
const BINDING_KEYS = ['schema','status','enabled','phase','receipts','controller',
  'driver_pin','inputs','phase_output','query_cwd','policy','option_acceptance',
  'query_inputs','body_requests','future_closure','forbidden'];
const POLICY = {timeout_ms:120000,max_native_stream_bytes:16777216,
  automatic_retry:false,automatic_intervention:false,
  argv_not_shell:true,raw_streams_separate:true,stdin:'/dev/null',
  owned_scope:'DETACHED_PROCESS_GROUP_SAMPLED_ONLY',
  broader_session_and_product_reception:'REQUIRED_SEPARATE_ROOT_RECEIPT',
  no_handle:'UNKNOWN_UNCLOSED_NO_FINAL_RAW_HASH_OR_SEAL',
  escaped_writer_scope:'UNKNOWN_NOT_CONTINUOUS_OR_OS_HERMETIC'};
const phases = ['contract','lookup','bodies'];
let binding, inputByPath, out, ownedUnsettled = false;
const createdFiles = [], createdDirs = [], bodyObservations = new Map();
function need(value, message) { assert.ok(value, message); }
function same(a, b, message) { assert.deepEqual(a, b, message); }
function keys(value, expected, label) {
  need(value !== null && typeof value === 'object' && !Array.isArray(value), label);
  same(Object.keys(value).sort(), [...expected].sort(), label + ' exact keys');
}
function absolute(p) {
  need(typeof p === 'string' && p.startsWith('/') && path.normalize(p) === p &&
    !/[\x00-\x1f\x7f]/.test(p), 'exact absolute path');
  return p;
}
function sha(bytes) { return crypto.createHash('sha256').update(bytes).digest('hex'); }
function pin(bytes) { return {bytes:bytes.length,sha256:sha(bytes)}; }
function pinShape(p) {
  keys(p,['bytes','sha256'],'pin');
  need(Number.isSafeInteger(p.bytes) && p.bytes >= 0,'pin bytes');
  need(typeof p.sha256 === 'string' && /^[a-f0-9]{64}$/.test(p.sha256),'pin digest');
}
function canonical(bytes) {
  const text = bytes.toString('utf8');
  need(Buffer.from(text,'utf8').equals(bytes),'JSON must be exact UTF-8');
  const value = JSON.parse(text);
  // Exact canonical re-encoding also rejects duplicate JSON member names.
  need(Buffer.from(JSON.stringify(value,null,2)+'\n').equals(bytes),
    'canonical JSON required; duplicate/hidden members or alternate bytes rejected');
  return value;
}
function write(rel, bytes) {
  need(typeof rel === 'string' && /^[A-Za-z0-9_./-]+$/.test(rel) &&
    !rel.split('/').some(x => x === '' || x === '.' || x === '..'),'output relative path');
  const full = out + '/' + rel;
  fs.writeFileSync(full,bytes,{flag:'wx',mode:0o600});
  createdFiles.push(rel);
}
function record(rel,value) { write(rel,Buffer.from(JSON.stringify(value,null,2)+'\n')); }
function mkdir(rel) {
  need(/^[A-Za-z0-9_-]+$/.test(rel),'flat child directory');
  fs.mkdirSync(out+'/'+rel,{mode:0o700});
  createdDirs.push(rel);
}
function stats(s) {
  return Object.fromEntries(STAT_KEYS.map(k => {
    need(typeof s[k] === 'bigint','integer stat field '+k);
    return [k,s[k].toString()];
  }));
}
function statShape(s) {
  keys(s,STAT_KEYS,'full integer stat');
  for (const v of Object.values(s)) need(typeof v === 'string' && /^-?[0-9]+$/.test(v),'integer string');
}
function comparable(s, how) {
  return Object.fromEntries((how === 'identity' ? IDENTITY_KEYS :
    STAT_KEYS.filter(k => k !== 'atimeNs')).map(k => [k,s[k]]));
}
function kindOf(s) {
  if(s.isSymbolicLink()) return 'symlink';
  if(s.isFile()) return 'file';
  if(s.isDirectory()) return 'directory';
  if(s.isCharacterDevice()) return 'character';
  return 'unsupported';
}
function assertMetadata(actual, expected, how, label) {
  same(comparable(actual,how),comparable(expected,how),label);
}
function descriptorShape(d) {
  keys(d,INPUT_KEYS,'input');
  absolute(d.path);
  need(['source','runtime','configuration','ancestor','cwd','receipt','query_result','body','device'].includes(d.role),'input role');
  need(['file','directory','symlink','absent','character'].includes(d.kind),'input kind');
  need(['stable','identity'].includes(d.comparison),'comparison');
  if(d.comparison === 'identity') need(d.kind === 'directory' && d.role === 'ancestor','identity only for ancestor directories');
  if(d.kind === 'absent') {
    same([d.lstat,d.stat,d.resolved,d.symlink_target,d.content,d.members],
      [null,null,null,null,null,null],'absence fields');
    return;
  }
  statShape(d.lstat); statShape(d.stat); absolute(d.resolved);
  need(d.symlink_target === null || typeof d.symlink_target === 'string','link target');
  if(d.kind === 'symlink') need(typeof d.symlink_target === 'string','symlink target required');
  else same(d.symlink_target,null,'not a symlink');
  if(d.content !== null) pinShape(d.content);
  if(d.kind === 'file' || (d.kind === 'symlink' && d.content !== null)) {
    if(d.content === null) need(d.role === 'body' && binding.phase === 'bodies','only approved first body may have unknown bytes');
  } else same(d.content,null,'nonfile content');
  need(d.members === null || Array.isArray(d.members),'members');
  if(d.members !== null) {
    need(d.kind === 'directory','membership directory');
    need(d.members.every(x=>typeof x === 'string' && x !== '' && x !== '.' && x !== '..' && !x.includes('/')),'member names');
    same(d.members,[...new Set(d.members)].sort(),'unique sorted membership names');
  }
}
function observeLink(p) {
  const d = inputByPath.get(p); need(d,'unbound alias/ancestor '+p);
  const s = fs.lstatSync(p,{bigint:true});
  same(kindOf(s),d.kind,'lexical kind '+p);
  assertMetadata(stats(s),d.lstat,d.comparison,'lexical metadata '+p);
  const target = s.isSymbolicLink() ? fs.readlinkSync(p) : null;
  same(target,d.symlink_target,'link text '+p);
  return {path:p,lstat:stats(s),symlink_target:target};
}
function resolveBound(p) {
  // Resolve only explicitly bound component spellings; never enumerate siblings.
  absolute(p);
  let parts=p.split('/').slice(1), done='/', hops=0;
  const chain=[observeLink('/')];
  while(parts.length) {
    const next=path.join(done,parts.shift()), observed=observeLink(next);
    chain.push(observed);
    if(observed.symlink_target !== null) {
      need(++hops <= 40,'bounded symlink chain');
      const rewritten=path.resolve(path.dirname(next),observed.symlink_target,...parts);
      parts=rewritten.split('/').slice(1); done='/';
    } else done=next;
  }
  return {resolved:done,chain};
}
function readPinned(p, expected) {
  const d = inputByPath.get(p);
  const receivedBody=d&&d.role==='body'&&binding.phase==='bodies'&&expected;
  need(d && (d.content !== null || receivedBody),'file must belong to full bound input key: '+p);
  if(expected&&d.content!==null) same(d.content,expected,'explicit required pin '+p);
  const requiredPin=expected??d.content; pinShape(requiredPin);
  const resolution=resolveBound(p);
  same(resolution.resolved,d.resolved,'resolved input '+p);
  const fd=fs.openSync(resolution.resolved,
    fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);
  try {
    const before=fs.fstatSync(fd,{bigint:true});
    need(before.isFile(),'regular input file');
    assertMetadata(stats(before),d.stat,'stable','read handle before '+p);
    const chunks=[],buffer=Buffer.alloc(1024*1024);
    let total=0;
    while(true) {
      const n=fs.readSync(fd,buffer,0,buffer.length,null); if(n===0) break;
      total+=n; need(total<=requiredPin.bytes,'bound input grew beyond complete expected size '+p);
      chunks.push(Buffer.from(buffer.subarray(0,n)));
    }
    same(total,requiredPin.bytes,'complete bound input byte count '+p);
    const bytes=Buffer.concat(chunks,total);
    const after=fs.fstatSync(fd,{bigint:true});
    assertMetadata(stats(after),stats(before),'stable','read handle after '+p);
    same(pin(bytes),requiredPin,'complete input body '+p);
    return bytes;
  } finally { fs.closeSync(fd); }
}
function snapshot() {
  const result=[];
  for(const d of binding.inputs) {
    if(d.kind === 'absent') {
      try {fs.lstatSync(d.path); throw new Error('expected absent '+d.path);}
      catch(e){need(e.code === 'ENOENT','absence exact ENOENT '+d.path);}
      // Its nearest present parent and complete aliases must still be bound.
      resolveBound(path.dirname(d.path));
      result.push({...d,observed_at:new Date().toISOString()}); continue;
    }
    const resolution=resolveBound(d.path);
    same(resolution.resolved,d.resolved,'resolved key '+d.path);
    const lst=fs.lstatSync(d.path,{bigint:true}), st=fs.statSync(d.path,{bigint:true});
    assertMetadata(stats(lst),d.lstat,d.comparison,'lstat key '+d.path);
    assertMetadata(stats(st),d.stat,d.comparison,'stat key '+d.path);
    let content=null, members=null;
    if(d.content !== null) content=pin(readPinned(d.path,d.content));
    if(d.members !== null) {
      members=fs.readdirSync(d.path).sort(); same(members,d.members,'finite membership '+d.path);
    }
    result.push({path:d.path,role:d.role,kind:d.kind,comparison:d.comparison,
      lstat:stats(lst),stat:stats(st),resolved:resolution.resolved,
      symlink_target:d.symlink_target,content,members,alias_chain:resolution.chain});
  }
  return result;
}
function stableKey(rows) {
  return rows.map(r => ({path:r.path,kind:r.kind,resolved:r.resolved,
    lstat:r.lstat===null?null:comparable(r.lstat,r.comparison),
    stat:r.stat===null?null:comparable(r.stat,r.comparison),
    symlink_target:r.symlink_target,content:r.content,members:r.members}));
}
function referenceShape(ref) {
  keys(ref,['path','pin'],'receipt ref'); absolute(ref.path); pinShape(ref.pin);
  need(ref.path.startsWith(ROOT+'/'),'receipt is workspace original');
}
function receiveRef(ref) { referenceShape(ref); readPinned(ref.path,ref.pin); }
function expectedCommands() {
  const result=[
    {label:'contract_help',phase:'CONTRACT_ONLY',argv:['/usr/bin/kpsewhich','--help'],expected_exit_codes:[0],result:null},
    {label:'contract_version',phase:'CONTRACT_ONLY',argv:['/usr/bin/kpsewhich','--version'],expected_exit_codes:[0],result:null}
  ];
  for(const seed of SEEDS) for(const mode of ['default','all'])
    result.push({label:seed.label+'_'+mode,phase:LATER,
      argv:['/usr/bin/kpsewhich','--progname='+seed.program,'--engine='+seed.engine,
        ...FLAGS,...(mode==='all'?['--all']:[]),seed.name],expected_exit_codes:[0,1],result:null});
  for(const name of VARIABLES)
    result.push({label:'var_'+name,phase:LATER,
      argv:['/usr/bin/kpsewhich','--progname='+(['BIBINPUTS','BSTINPUTS'].includes(name)?'bibtex':'pdflatex'),
        '--engine=pdftex',...FLAGS,'-var-value='+name],expected_exit_codes:[0,1],result:null});
  result.push({label:'expanded_TEXMF',phase:LATER,
    argv:['/usr/bin/kpsewhich','--progname=pdflatex','--engine=pdftex',...FLAGS,
      '-expand-path=$TEXMF'],expected_exit_codes:[0,1],result:null});
  same(result.length,53,'complete first frontier'); return result;
}
function oldCompanions() {
  const objects={};
  for(const [name,fixed] of Object.entries(OLD_COMPANIONS)) {
    const absolutePath=ROOT+'/'+fixed.path;
    const bytes=readPinned(absolutePath);
    same(sha(bytes),fixed.sha256,'immutable WHOLE companion, every field and byte '+name);
    objects[name]=canonical(bytes);
  }
  const f=objects['QUERY_FRONTIER.json'];
  same(f.initial_name_seeds,SEEDS,'all complete independent seed tuples');
  same(f.ordered_command_proposals,expectedCommands(),'all complete independent argv records');
  same(f.environment,ENV8,'exact ENV8'); same(f.command_cwd_proposal,QUERY_CWD,'cwd proposal');
  // Immutable byte identity above is deliberately stronger than selective schema
  // tests. Any companion change requires a new source receipt and new driver pin.
  return f;
}
function validateBinding(b, filename) {
  keys(b,BINDING_KEYS,'binding');
  same(b.schema,'p212-dependency-query-driver-binding-v1','binding schema');
  need(typeof b.enabled === 'boolean','enabled boolean');
  keys(b.receipts,RECEIPT_KEYS,'all separate receipt roles');
  keys(b.controller,['executable_spelling','executable_resolved','exec_argv','argv',
    'cwd','environment','umask','outer_entry_source','outer_request_record'],'controller');
  same(b.controller.environment,ENV8,'replacement controller ENV8');
  same(b.controller.cwd,ROOT,'controller cwd');
  same(b.controller.umask,0o077,'private capture umask');
  need(Array.isArray(b.controller.exec_argv),'exact Node options');
  same(b.query_cwd,QUERY_CWD,'exact initial query cwd');
  same(b.policy,POLICY,'complete fixed native policy');
  keys(b.option_acceptance,['accepted','installed_flags','one_name_default_all',
    'generators_disabled','variable_and_expand_semantics','unknown_generators',
    'format_contexts_received'],'all option semantics fields');
  same(b.option_acceptance.installed_flags,FLAGS,'requested flags');
  for(const k of ['accepted','one_name_default_all','generators_disabled',
    'variable_and_expand_semantics','unknown_generators','format_contexts_received'])
    need(typeof b.option_acceptance[k] === 'boolean','option boolean '+k);
  need(Array.isArray(b.inputs) && Array.isArray(b.query_inputs) &&
    Array.isArray(b.body_requests),'all finite arrays must exist');
  same(b.future_closure,EMPTY_CLOSURE,'no operational semantic closure or lock');
  same(b.forbidden,FORBIDDEN,'all forbidden roles, including HOLD_EXTERNAL');
  if(!b.enabled) {
    same(b.status,'DISABLED_SOURCE_ONLY','disabled status');
    same(b.phase,null,'no phase');
    same(b.driver_pin,null,'no enabled driver pin');
    same(b.phase_output,null,'no output observation');
    same(b.inputs,[],'no host inputs'); same(b.query_inputs,[],'no queries');
    same(b.body_requests,[],'no body authority');
    for(const k of RECEIPT_KEYS) same(b.receipts[k],null,'disabled receipt '+k);
    same(b.controller.executable_spelling,null); same(b.controller.executable_resolved,null);
    same(b.controller.argv,null); same(b.controller.exec_argv,[]);
    same(b.controller.outer_entry_source,null); same(b.controller.outer_request_record,null);
    for(const k of Object.keys(b.option_acceptance))
      if(k!=='installed_flags') same(b.option_acceptance[k],false,'disabled option '+k);
    throw new Error('HOLD_OPERATIONAL: disabled source-only interface; no child or host key read');
  }
  same(b.status,'ROOT_BOUND_ONE_PHASE_ONLY','active status');
  need(phases.includes(b.phase),'exact separate phase');
  same(filename,BINDING_ROOT+'/'+b.phase+'01/BINDING.json','immutable separate phase binding location');
  pinShape(b.driver_pin);
  absolute(b.controller.executable_spelling); absolute(b.controller.executable_resolved);
  need(Array.isArray(b.controller.argv),'exact argv');
  same(b.controller.argv,[b.controller.executable_resolved,SELF,filename],'controller argv');
  same(b.phase_output,QUERY_ROOT+'/'+b.phase+'01','exact new phase output');
  for(const k of ['plan_source','driver_source','prestartup']) referenceShape(b.receipts[k]);
  referenceShape(b.controller.outer_entry_source); referenceShape(b.controller.outer_request_record);
  if(b.phase==='contract') {
    for(const k of ['options','queries','body_scope']) same(b.receipts[k],null,'later gate absent');
    for(const k of Object.keys(b.option_acceptance))
      if(k!=='installed_flags') same(b.option_acceptance[k],false,'contract cannot accept its own options');
  } else {
    referenceShape(b.receipts.options);
    for(const k of ['accepted','one_name_default_all','generators_disabled',
      'variable_and_expand_semantics','format_contexts_received'])
      same(b.option_acceptance[k],true,'separate installed option acceptance');
    same(b.option_acceptance.unknown_generators,false,'unknown generators stop');
  }
  if(b.phase!=='bodies') {
    same(b.receipts.queries,null); same(b.receipts.body_scope,null);
    same(b.query_inputs,[]); same(b.body_requests,[]);
  } else {
    referenceShape(b.receipts.queries); referenceShape(b.receipts.body_scope);
    same(b.query_inputs.length,38,'all default/all result inputs');
  }
  need(b.inputs.length>0,'fresh complete finite input key required');
  for(const d of b.inputs) descriptorShape(d);
  inputByPath=new Map(b.inputs.map(d=>[d.path,d]));
  same(inputByPath.size,b.inputs.length,'duplicate input path is not deduplicated away');
  need(!inputByPath.has(b.phase_output),'own output is not an immutable absent key');
  need(b.inputs.every(d=>!d.path.startsWith(b.phase_output+'/')),'no preexisting output members');
  for(const p of ['/',SELF,b.controller.executable_spelling,b.controller.executable_resolved,
    '/dev/null',QUERY_CWD,QUERY_ROOT]) need(inputByPath.has(p),'mandatory input role '+p);
  same(inputByPath.get('/dev/null').kind,'character','bound null character device');
  same(inputByPath.get(QUERY_CWD).kind,'directory','actual query cwd');
  same(inputByPath.get(QUERY_CWD).members,[],'query cwd must be observed empty');
  const executable=b.phase==='bodies'?'/usr/bin/cmp':'/usr/bin/kpsewhich';
  need(inputByPath.has(executable) && inputByPath.get(executable).content!==null,
    'exact native executable alias bytes are separately bound');
  for(const d of b.inputs) {
    if(d.role==='body') need(b.phase==='bodies','no body reads in query phases');
    if(d.kind==='file' && d.role!=='body') need(d.content!==null,'full regular input pin required');
    if(d.kind==='symlink') {
      const resolved=inputByPath.get(d.resolved);
      need(resolved&&resolved.kind!=='symlink','resolved alias role explicitly present');
      same(resolved.stat,d.stat,'alias and referent stat binding');
      if(resolved.kind==='file'&&resolved.role!=='body')
        need(resolved.content!==null,'resolved regular alias referent has full bytes');
      if(d.content!==null) same(d.content,resolved.content,'alias content agrees with target');
    }
  }
}
function openOutput(rel) {
  const fd=fs.openSync(out+'/'+rel,fs.constants.O_WRONLY|fs.constants.O_CREAT|fs.constants.O_EXCL,0o600);
  createdFiles.push(rel); return fd;
}
function groupSample(pid) {
  try {
    process.kill(-pid,0);
    return {process_group_id:pid,exists:true,errno:null,members:null,
      census_scope:'GROUP_NONEMPTY_MEMBERS_NOT_ENUMERATED',
      sampled_at:new Date().toISOString()};
  } catch(e) {
    if(e.code==='ESRCH') return {process_group_id:pid,exists:false,errno:'ESRCH',members:[],
      census_scope:'EMPTY_OWNED_GROUP_AT_SAMPLE_ONLY',
      sampled_at:new Date().toISOString()};
    return {process_group_id:pid,exists:null,errno:e.code??String(e),members:null,
      census_scope:'UNKNOWN',sampled_at:new Date().toISOString()};
  }
}
async function nativeCapture(label,argv,allowed) {
  // No shell, PATH search, retry, kill, installation or generator helper.
  need(/^[A-Za-z0-9_]+$/.test(label),'native label');
  need(argv[0]==='/usr/bin/kpsewhich'||argv[0]==='/usr/bin/cmp','finite native tools only');
  mkdir(label);
  const before=snapshot();
  record(label+'/INPUTS_BEFORE.json',before);
  record(label+'/CONFIGURATION_BEFORE.json',{environment:process.env,cwd:process.cwd(),
    execPath:process.execPath,execArgv:process.execArgv,umask:process.umask(),
    child_environment:ENV8,child_cwd:QUERY_CWD,stdin:'/dev/null'});
  const outFd=openOutput(label+'/stdout.raw'), errFd=openOutput(label+'/stderr.raw');
  const eventFd=openOutput(label+'/EVENTS.jsonl');
  const nullResolution=resolveBound('/dev/null');
  const nullFd=fs.openSync(nullResolution.resolved,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW);
  const nullHandle=fs.fstatSync(nullFd,{bigint:true});
  need(nullHandle.isCharacterDevice(),'actual stdin read handle is character device');
  assertMetadata(stats(nullHandle),inputByPath.get('/dev/null').stat,'stable','null read handle');
  const attempt={schema:'p212-native-attempt-v1',label,argv,cwd:QUERY_CWD,environment:ENV8,
    deadline_unix_ms:Date.now()+POLICY.timeout_ms,timeout_ms:POLICY.timeout_ms,
    stdin:{lexical:'/dev/null',resolved:nullResolution.resolved,handle:stats(nullHandle)},
    detached_process_group_requested:true,pre_spawn_input_key:pin(Buffer.from(JSON.stringify(before,null,2)+'\n')),
    expected_native_exits:allowed,automatic_retry:false,automatic_intervention:false,
    wrapper_native_product_originals:'MUST_BE_RETAINED_BY_SEPARATE_PRESTARTED_ENTRY'};
  record(label+'/ATTEMPT.json',attempt);
  const events=[];
  function event(type,data) {
    const row={type,observed_at:new Date().toISOString(),...data};
    events.push(row); fs.writeSync(eventFd,JSON.stringify(row)+'\n'); fs.fsyncSync(eventFd);
  }
  let child, pid=null, spawnError=null, nativeExit=null, closeObserved=false, timedOut=false;
  const settled=await new Promise(resolve=>{
    let returned=false;
    const finish=value=>{if(!returned){returned=true;clearTimeout(timer);resolve(value);}};
    const timer=setTimeout(()=>{
      timedOut=true; event('DEADLINE',{pid,policy:'NO_AUTOMATIC_INTERVENTION'});
      finish(false);
    },POLICY.timeout_ms);
    try {
      child=childProcess.spawn(argv[0],argv.slice(1),{
        cwd:QUERY_CWD,env:ENV8,stdio:[nullFd,outFd,errFd],detached:true,shell:false
      });
      child.once('spawn',()=>{
        pid=child.pid; event('SPAWN',{pid,requested_process_group_id:pid,
          actual_product_session:'EXTERNAL_ENTRY_RECORD_NOT_SYNTHESIZED'});
      });
      child.once('error',e=>{
        spawnError={name:e.name,message:e.message,code:e.code??null};
        event('ERROR',{pid,error:spawnError});
      });
      child.once('exit',(code,signal)=>{
        nativeExit={code,signal}; event('EXIT',{pid,native_exit:nativeExit});
      });
      child.once('close',(code,signal)=>{
        closeObserved=true; event('CLOSE',{pid,code,signal}); finish(true);
      });
    } catch(e) {
      spawnError={name:e.name,message:e.message,code:e.code??null};
      event('SPAWN_THROW',{error:spawnError}); finish(false);
    }
  });
  // Close only controller-owned descriptors, never kill or clean the native child.
  for(const fd of [nullFd,outFd,errFd,eventFd]) fs.closeSync(fd);
  const group=pid===null?null:groupSample(pid);
  const closed=settled&&closeObserved&&pid!==null&&nativeExit!==null&&
    spawnError===null&&group!==null&&group.exists===false;
  if(!closed) {
    ownedUnsettled=true;
    if(child) child.unref();
    record(label+'/UNKNOWN_UNCLOSED.json',{label,argv,pid,spawn_error:spawnError,
      native_exit:nativeExit,close_observed:closeObserved,timed_out:timedOut,
      group_sample:group,events,interventions:[],
      stdout_final_hash:null,stderr_final_hash:null,manifest:null,
      next_action:'ROOT_OWNED_SESSION_SETTLEMENT_REQUIRED_NO_RETRY',
      broader_session_and_escaped_writer_scope:'UNKNOWN'});
    throw new Error('UNKNOWN_UNCLOSED '+label+'; no final stream hash or local seal');
  }
  for(const name of ['stdout.raw','stderr.raw'])
    need(fs.statSync(out+'/'+label+'/'+name).size<=POLICY.max_native_stream_bytes,
      'closed native stream exceeds finite memory bound; original remains, no truncation');
  const stdout=fs.readFileSync(out+'/'+label+'/stdout.raw');
  const stderr=fs.readFileSync(out+'/'+label+'/stderr.raw');
  const after=snapshot();
  record(label+'/INPUTS_AFTER.json',after);
  record(label+'/CONFIGURATION_AFTER.json',{environment:process.env,cwd:process.cwd(),
    execPath:process.execPath,execArgv:process.execArgv,umask:process.umask(),
    child_environment:ENV8,child_cwd:QUERY_CWD,stdin:'/dev/null'});
  same(stableKey(after),stableKey(before),'native declared comparable full-key projection '+label);
  const result={schema:'p212-native-group-capture-v1',label,argv,
    pid,native_exit:nativeExit,close_observed:true,group_sample:group,
    stdout:pin(stdout),stderr:pin(stderr),events,interventions:[],
    wrapper_outcome:'CHILD_CLOSE_OBSERVED_OWNED_GROUP_EMPTY_AT_SAMPLE',
    allowed_native_exit:allowed.includes(nativeExit.code)&&nativeExit.signal===null,
    complete_native_product_and_broader_session_reception:'PENDING_SEPARATE_ROOT_RECEPTION',
    continuous_race_or_escaped_writer_proof:false};
  record(label+'/RESULT.json',result);
  return {result,stdout,stderr};
}
function rawLines(bytes) {
  if(bytes.length===0) return [];
  const text=bytes.toString('utf8');
  need(Buffer.from(text).equals(bytes),'unambiguous UTF-8 paths required; raw remains preserved');
  const ended=text.endsWith('\n');
  const lines=text.split('\n'); if(ended) lines.pop();
  // Only separate LF delimiters. Do not trim, sort or deduplicate any spelling.
  return lines.map((line,index)=>({index,raw_line_hex:Buffer.from(line).toString('hex'),
    delimiter_hex:index<lines.length-1||ended?'0a':'',lexical_path:line}));
}
function interpretName(command,capture) {
  const seed=SEEDS.find(s=>command.label===s.label+'_default'||command.label===s.label+'_all');
  need(seed,'known name seed');
  need(capture.result.allowed_native_exit,'query exit outside exact contract');
  need(capture.stderr.length===0,'query diagnostics require root disposition before interpretation');
  const lines=rawLines(capture.stdout);
  if(capture.result.native_exit.code===1) need(lines.length===0,'exit 1 with path data is unresolved');
  if(seed.required) need(capture.result.native_exit.code===0&&lines.length>0,'required seed missing: HOLD');
  if(command.label.endsWith('_default')) need(lines.length<=1,'default result ambiguity');
  for(const line of lines) absolute(line.lexical_path);
  return {label:command.label,seed,lines,empty:lines.length===0,
    native_exit:capture.result.native_exit.code,consumption_claim:false};
}
function validateQueryInputs() {
  const commands=expectedCommands().slice(2,40), requests=[];
  same(binding.query_inputs.map(x=>x.label),commands.map(x=>x.label),'all 38 result contexts in order');
  for(let i=0;i<commands.length;i++) {
    const q=binding.query_inputs[i], c=commands[i];
    keys(q,['label','stdout','stderr','result'],'query input');
    for(const k of ['stdout','stderr','result']) referenceShape(q[k]);
    const stdout=readPinned(q.stdout.path,q.stdout.pin),stderr=readPinned(q.stderr.path,q.stderr.pin);
    const result=canonical(readPinned(q.result.path,q.result.pin));
    // Query reception supplies the complete historical-native validation; these
    // checks additionally bind every body authorization to the exact raw bytes.
    keys(result,['schema','label','argv','pid','native_exit','close_observed',
      'group_sample','stdout','stderr','events','interventions','wrapper_outcome',
      'allowed_native_exit','complete_native_product_and_broader_session_reception',
      'continuous_race_or_escaped_writer_proof'],'whole generated query-result schema');
    keys(result.native_exit,['code','signal'],'native exit');
    keys(result.group_sample,['process_group_id','exists','errno','members',
      'census_scope','sampled_at'],'owned group sample');
    need(Number.isSafeInteger(result.pid)&&result.pid>0,'actual positive native pid');
    need([0,1].includes(result.native_exit.code)&&result.native_exit.signal===null,'query native exit');
    same(result.allowed_native_exit,true);
    same(result.group_sample.process_group_id,result.pid);
    same(result.group_sample.errno,'ESRCH'); same(result.group_sample.members,[]);
    same(result.group_sample.census_scope,'EMPTY_OWNED_GROUP_AT_SAMPLE_ONLY');
    need(typeof result.group_sample.sampled_at==='string','actual group sample time');
    same(result.wrapper_outcome,'CHILD_CLOSE_OBSERVED_OWNED_GROUP_EMPTY_AT_SAMPLE');
    same(result.complete_native_product_and_broader_session_reception,'PENDING_SEPARATE_ROOT_RECEPTION');
    same(result.continuous_race_or_escaped_writer_proof,false);
    same(result.interventions,[]);
    need(Array.isArray(result.events),'complete native event array');
    same(result.events.map(e=>e.type),['SPAWN','EXIT','CLOSE'],'complete accepted event sequence');
    for(const e of result.events) {
      const fields=e.type==='SPAWN'?['type','observed_at','pid','requested_process_group_id','actual_product_session']:
        e.type==='EXIT'?['type','observed_at','pid','native_exit']:['type','observed_at','pid','code','signal'];
      keys(e,fields,'event exact fields'); same(e.pid,result.pid);
      need(typeof e.observed_at==='string','event actual timestamp');
      if(e.type==='SPAWN') {
        same(e.requested_process_group_id,result.pid);
        same(e.actual_product_session,'EXTERNAL_ENTRY_RECORD_NOT_SYNTHESIZED');
      } else if(e.type==='EXIT') same(e.native_exit,result.native_exit);
      else {same(e.code,result.native_exit.code);same(e.signal,result.native_exit.signal);}
    }
    same(result.schema,'p212-native-group-capture-v1');
    same(result.label,c.label); same(result.argv,c.argv);
    same(result.stdout,pin(stdout)); same(result.stderr,pin(stderr));
    same(result.close_observed,true); same(result.group_sample.exists,false);
    const interpreted=interpretName(c,{result,stdout,stderr});
    for(const line of interpreted.lines) requests.push({query_label:c.label,
      raw_line_index:line.index,raw_line_hex:line.raw_line_hex,delimiter_hex:line.delimiter_hex,
      lexical_path:line.lexical_path});
  }
  same(binding.body_requests.length,requests.length,'every shadow/alias/duplicate returned line retained');
  const allowedBodyPaths=new Set();
  for(let i=0;i<requests.length;i++) {
    const b=binding.body_requests[i];
    keys(b,['query_label','raw_line_index','raw_line_hex','delimiter_hex',
      'lexical_path','max_bytes'],'complete body authorization');
    const {max_bytes,...identity}=b; same(identity,requests[i],'body authority must match exact ordered raw line');
    need(Number.isSafeInteger(max_bytes)&&max_bytes>0,'separately bound finite body byte limit');
    const d=inputByPath.get(b.lexical_path);
    need(d&&d.role==='body'&&['file','symlink'].includes(d.kind),'approved finite body descriptor');
    const referent=inputByPath.get(d.resolved);
    need(referent&&referent.kind==='file'&&referent.role==='body',
      'body target must be a separately bound regular-file role before any open');
    need(BigInt(d.stat.size)<=BigInt(max_bytes),'whole body must fit finite declared limit');
    allowedBodyPaths.add(d.path); allowedBodyPaths.add(d.resolved);
  }
  for(const d of binding.inputs) if(d.role==='body')
    need(allowedBodyPaths.has(d.path),'body role cannot authorize an unreturned extra path');
  return requests;
}
async function captureBody(request,index) {
  const label='body_'+String(index).padStart(4,'0');
  mkdir(label);
  const d=inputByPath.get(request.lexical_path), resolution=resolveBound(d.path);
  same(resolution.resolved,d.resolved,'approved body resolution');
  record(label+'/ATTEMPT.json',{schema:'p212-body-copy-attempt-v1',request,
    exact_bound_descriptor:d,alias_chain:resolution.chain,
    source_read_operation:'open O_RDONLY|O_NOFOLLOW|O_NONBLOCK on fully bound regular referent; read in ordered chunks',
    destination_operation:'exclusive new body.raw; complete bytes or retained partial failure',
    authorization_receipt:binding.receipts.body_scope});
  const sourceFd=fs.openSync(d.resolved,
    fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);
  let destFd=null;
  try {
    const before=fs.fstatSync(sourceFd,{bigint:true});
    need(before.isFile(),'body referent must be regular file, never device/socket/directory');
    assertMetadata(stats(before),d.stat,'stable','body handle before');
    destFd=openOutput(label+'/body.raw');
    const hash=crypto.createHash('sha256'),buffer=Buffer.alloc(1024*1024);
    let total=0;
    while(true) {
      const n=fs.readSync(sourceFd,buffer,0,buffer.length,null); if(n===0) break;
      total+=n;
      // Retain the actually read chunk, then reject oversized output; never
      // relabel a truncated prefix as a whole body.
      let at=0; while(at<n) at+=fs.writeSync(destFd,buffer,at,n-at);
      hash.update(buffer.subarray(0,n));
      need(total<=request.max_bytes,'body exceeded bound; partial failure retained');
    }
    fs.fsyncSync(destFd);
    const after=fs.fstatSync(sourceFd,{bigint:true});
    assertMetadata(stats(after),stats(before),'stable','same body read handle after');
    same(BigInt(total),before.size,'complete same-handle body size');
    const bodyPin={bytes:total,sha256:hash.digest('hex')};
    if(d.content!==null) same(bodyPin,d.content,'prebound body bytes');
    if(bodyObservations.has(d.path))
      same(bodyPin,bodyObservations.get(d.path),'duplicate returned body unchanged');
    bodyObservations.set(d.path,bodyPin);
    record(label+'/READ_HANDLE.json',{lexical:d.path,resolved:d.resolved,
      before:stats(before),after:stats(after),body:bodyPin,
      operation:'actual ordered fs.readSync/fs.writeSync exclusive full copy',
      native_external_read_copy_envelope:'REQUIRED_SEPARATE_ROOT_CAPTURE',
      continuous_path_race_claim:false});
    fs.closeSync(destFd); destFd=null;
    const comparison=await nativeCapture(label+'_cmp',
      ['/usr/bin/cmp','--',d.path,out+'/'+label+'/body.raw'],[0]);
    need(comparison.result.allowed_native_exit&&comparison.result.native_exit.code===0,
      'actual byte comparison failed');
    need(comparison.stdout.length===0&&comparison.stderr.length===0,'cmp diagnostics require reception');
    const finalResolution=resolveBound(d.path);
    same(finalResolution.resolved,d.resolved,'body alias chain after');
    const finalStat=fs.statSync(d.path,{bigint:true});
    assertMetadata(stats(finalStat),stats(before),'stable','body path after actual cmp');
    same(pin(fs.readFileSync(out+'/'+label+'/body.raw')),bodyPin,'retained copy after native cmp');
    record(label+'/RESULT.json',{request,lexical:d.path,resolved:d.resolved,
      read_handle_before:stats(before),read_handle_after:stats(after),
      path_stat_after_cmp:stats(finalStat),alias_chain_before:resolution.chain,
      alias_chain_after:finalResolution.chain,body:bodyPin,
      raw_cmp_result:label+'_cmp/RESULT.json',
      source_semantics_received:false,source_edges:null,dependency_lock:null,
      root_original_reception:'PENDING'});
    return {request,body_file:label+'/body.raw',pin:bodyPin};
  } finally {
    fs.closeSync(sourceFd); if(destFd!==null) fs.closeSync(destFd);
  }
}
function sealLocal() {
  // This is an INNER payload seal, not a substitute for the actual product
  // request/yield/poll/final records or broader owned-session root reception.
  need(!ownedUnsettled,'never seal unsettled native streams');
  const actualFiles=[],actualDirs=[];
  function walk(directory,prefix) {
    for(const name of fs.readdirSync(directory).sort()) {
      const rel=prefix+name, full=out+'/'+rel,s=fs.lstatSync(full);
      need(!s.isSymbolicLink(),'no output symlink');
      if(s.isDirectory()){actualDirs.push(rel);walk(full,rel+'/');}
      else {need(s.isFile(),'ordinary output payload');actualFiles.push(rel);}
    }
  }
  walk(out,'');
  same(actualFiles.sort(),[...createdFiles].sort(),'complete generated file membership');
  same(actualDirs.sort(),[...createdDirs].sort(),'complete generated directory membership');
  const empty=actualDirs.filter(d=>!actualFiles.some(f=>f.startsWith(d+'/')));
  record('LOCAL_TREE.json',{files:actualFiles,directories:actualDirs,empty_directories:empty,
    scope:'PRE_SELF_INNER_PAYLOAD_CENSUS_ONLY_OUTER_NATIVE_RECEPTION_PENDING'});
  const rows=createdFiles.slice().sort().map(rel=>sha(fs.readFileSync(out+'/'+rel))+'  '+rel);
  write('SHA256SUMS',Buffer.from(rows.join('\n')+'\n'));
}
async function main() {
  need(process.argv.length===2||process.argv.length===3,'one binding argument only');
  const filename=process.argv[2]??path.dirname(SELF)+'/INTERFACE.disabled.json';
  absolute(filename);
  need(filename===path.dirname(SELF)+'/INTERFACE.disabled.json'||
    phases.some(p=>filename===BINDING_ROOT+'/'+p+'01/BINDING.json'),'finite binding path');
  // Only this selected workspace file is read before the disabled check.
  binding=canonical(fs.readFileSync(filename));
  validateBinding(binding,filename);
  same(process.execPath,binding.controller.executable_resolved,'observed Node executable');
  same(process.execArgv,binding.controller.exec_argv,'observed Node flags');
  same(process.argv,binding.controller.argv,'observed controller argv');
  same(process.cwd(),ROOT,'observed controller cwd');
  same({...process.env},ENV8,'no inherited environment additions');
  same(process.umask(),0o077,'umask already bound before startup');
  readPinned(SELF,binding.driver_pin);
  for(const ref of Object.values(binding.receipts)) if(ref!==null) receiveRef(ref);
  receiveRef(binding.controller.outer_entry_source); receiveRef(binding.controller.outer_request_record);
  const frontier=oldCompanions();
  // Keep the full fixed source graph. No manuscript execution/prose repair occurs.
  for(const [name,k] of Object.entries(frontier.profile.source_pins))
    readPinned(ROOT+'/'+frontier.profile.paper_root+'/'+name,k);
  // Validate the ENTIRE separately approved returned path set before snapshot()
  // can read any pre-pinned body bytes in this phase.
  if(binding.phase==='bodies') validateQueryInputs();
  const before=snapshot();
  // Exact absent destination check; no recursive creation or cleanup.
  resolveBound(QUERY_ROOT);
  try {fs.lstatSync(binding.phase_output);throw new Error('phase output already exists');}
  catch(e){need(e.code==='ENOENT','exclusive new output required');}
  fs.mkdirSync(binding.phase_output,{mode:0o700}); out=binding.phase_output;
  record('BINDING_RECEIVED.json',binding);
  record('INPUTS_BEFORE.json',before);
  record('ENTRY_LIMIT.json',{prestartup_receipt:binding.receipts.prestartup,
    internal_checks_occur_after_Node_startup:true,
    actual_product_request_yield_poll_final:'MUST_BE_CAPTURED_BY_SEPARATE_ENTRY',
    owned_scope:POLICY.owned_scope,
    broader_owned_session_census:'NOT_IMPLEMENTED_BY_THIS_NO_HOST_INVENTORY_DRIVER',
    outer_root_receipt_required:true,dependency_lock:null});
  const completed=[];
  if(binding.phase==='bodies') {
    for(let i=0;i<binding.body_requests.length;i++)
      completed.push(await captureBody(binding.body_requests[i],i));
    const bodyAfter=[];
    for(const [bodyPath,bodyPin] of bodyObservations)
      bodyAfter.push({path:bodyPath,first_complete_read:bodyPin,
        final_complete_read:pin(readPinned(bodyPath,bodyPin))});
    record('BODY_READS_AND_FINAL_KEYS.json',{
      scope:'FIRST_BODY_BYTES_WERE_UNKNOWN_AT_BINDING_NOT_PRESTARTUP_CONTENT_PINS',
      ordered_copies:completed,final_keys:bodyAfter,
      inference:'Each copy has same-handle before/after stats and a full hash; a later separate native path cmp and final complete source hash agree. cmp internal read handles are not observed.',
      continuous_race_claim:false});
  } else {
    const commands=expectedCommands();
    for(const command of (binding.phase==='contract'?commands.slice(0,2):commands.slice(2))) {
      const captured=await nativeCapture(command.label,command.argv,command.expected_exit_codes);
      need(captured.result.allowed_native_exit,'native exit outside proposed contract');
      need(captured.stderr.length===0,'raw diagnostic requires root disposition; no automatic continuation');
      let interpretation=null;
      if(binding.phase==='contract') need(captured.stdout.length>0,'installed contract output empty');
      else if(!command.label.startsWith('var_')&&command.label!=='expanded_TEXMF')
        interpretation=interpretName(command,captured);
      else interpretation={label:command.label,raw:pin(captured.stdout),
        kind:'VARIABLE_OR_LITERAL_EXPANSION_DATA_NOT_FILESYSTEM_ABSENCE',source_edges:null};
      completed.push({label:command.label,receipt:command.label+'/RESULT.json',interpretation});
    }
  }
  const after=snapshot(); record('INPUTS_AFTER.json',after);
  same(stableKey(after),stableKey(before),'entire phase declared comparable input projection');
  record('RESULT.json',{schema:'p212-finite-frontier-capture-v1',
    status:'FINITE_INNER_CAPTURE_COMPLETE_ROOT_ORIGINAL_RECEPTION_PENDING',
    phase:binding.phase,completed,actual_kpsewhich_commands:binding.phase==='bodies'?0:completed.length,
    actual_body_copies:binding.phase==='bodies'?completed.length:0,
    installed_option_semantics_accepted_by_this_driver:false,
    next_phase_automatically_authorized:false,future_closure:EMPTY_CLOSURE,
    broader_native_session_and_product_reception:'PENDING_ROOT',
    forbidden:FORBIDDEN});
  sealLocal();
}
main().catch(error=>{
  if(out) {
    try {record('FAILURE.json',{name:error.name,message:error.message,
      owned_unsettled:ownedUnsettled,final_success:false,automatic_retry:false,
      next_action:'PRESERVE_ALL_PARTIAL_OUTPUTS_AND_STOP_FOR_ROOT',
      native_product_originals:'EXTERNAL_CAPTURE_REQUIRED'});} catch(_) {}
  }
  process.stderr.write(String(error.stack??error)+'\n');
  // An unsettled detached process may still own raw output descriptors.
  // No success seal, hash or claim of no writer is produced in that case.
  if(ownedUnsettled) process.exit(76);
  process.exitCode=78;
});
