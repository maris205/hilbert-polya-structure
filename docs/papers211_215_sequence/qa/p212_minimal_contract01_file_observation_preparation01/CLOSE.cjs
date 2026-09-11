const fs = require("node:fs");
const crypto = require("node:crypto");
const FIELD_NAMES = ["dev","ino","mode","nlink","uid","gid","rdev","size","mtimeNs","ctimeNs"];
let checks = 0, totalRead = 0;
const keys = [], buffers = new Map();
function need(test, label) { checks++; if (!test) throw new Error(label); }
function hash(buffer) { return crypto.createHash("sha256").update(buffer).digest("hex"); }
function fullStat(s) { return Object.fromEntries(FIELD_NAMES.map(k => [k, s[k].toString()])); }
function equal(a,b) { return JSON.stringify(a) === JSON.stringify(b); }
function fullRead(path) {
  need(ALLOWED.has(path), "OUTSIDE_FIXED_DOCUMENTARY_INPUT_SET");
  if (buffers.has(path)) return buffers.get(path);
  const record = {path, eof:false, byte_count:0, complete:false, closed:false};
  keys.push(record);
  let fd = null;
  try {
    const first = fs.lstatSync(path,{bigint:true});
    record.lstat_before = fullStat(first);
    need((first.mode & 0o170000n) === 0o100000n, "NONREGULAR_DOCUMENT");
    need(first.size >= 0n && first.size <= 16777216n, "DOCUMENT_SIZE_BOUND");
    fd = fs.openSync(path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);
    record.fd_before = fullStat(fs.fstatSync(fd,{bigint:true}));
    need(equal(record.lstat_before,record.fd_before), "DOCUMENT_ENDPOINT_FD_BEFORE");
    const chunks = [], block = Buffer.alloc(65536);
    for (;;) {
      const count = fs.readSync(fd,block,0,block.length,null);
      need(Number.isInteger(count) && count >= 0 && count <= block.length, "READ_COUNT");
      if (count === 0) { record.eof = true; record.eof_zero_return = 0; break; }
      record.byte_count += count; totalRead += count;
      chunks.push(Buffer.from(block.subarray(0,count)));
      need(record.byte_count <= 16777216 && totalRead <= 67108864, "DOCUMENT_READ_BOUND");
    }
    record.fd_after = fullStat(fs.fstatSync(fd,{bigint:true}));
    record.lstat_after = fullStat(fs.lstatSync(path,{bigint:true}));
    need(equal(record.fd_before,record.fd_after), "DOCUMENT_SAME_FD_AFTER");
    need(equal(record.lstat_before,record.lstat_after), "DOCUMENT_ENDPOINT_AFTER");
    need(BigInt(record.byte_count) === first.size, "DOCUMENT_COMPLETE_SIZE");
    const buffer = Buffer.concat(chunks);
    need(buffer.length === record.byte_count, "DOCUMENT_CAPTURE_COUNT");
    record.sha256 = hash(buffer);
    fs.closeSync(fd); fd = null; record.closed = true;
    record.complete = true;
    buffers.set(path,buffer);
    return buffer;
  } catch (error) {
    record.failure = {name:error.name,code:error.code || null,message:error.message};
    throw error;
  } finally {
    if (fd !== null) {
      try { fs.closeSync(fd); record.closed = true; }
      catch (error) { record.close_failure = {name:error.name,code:error.code || null,message:error.message}; throw error; }
    }
  }
}
function pin(path) {
  const b = fullRead(path);
  return {path,bytes:b.length,sha256:hash(b)};
}

const INPUT_SPEC=[{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/SHA256SUMS","sha256":"523e5f3c361a41fd36f8e25f16f03a8cdfd6fdcb035df20dd2eabfb9bafdff40"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/ARCHIVAL_DISPOSITIONS.json","sha256":"886c14e841f3c2a7127699637e5d2a7f211d0fd103c1b09641006dfc7dea5f6e"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/BINDING.disabled.json","sha256":"1ee579b56e551dbadcf019a217ab1a194161019723fd4172be26db3b00a3dbd6"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/CLOSING_KEYS.json","sha256":"ec12e41a690ee44b4a5a1dcae3d3a59ba630e3dc2b09d2fb04cace2f93c71a95"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/CLOSING_NATIVE.json","sha256":"2a28cb9ce721c2ce496d06dc0f4e2f0b6181e0c1becbf0be04e985c45fa96853"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/CONTRACT.md","sha256":"79393d2248d06859da5e972af8604cf3f356e996e12c4eefa49720da021eb193"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/DEPENDENCY_GATE.md","sha256":"83c8083824976a78d87b6c4387fbf781af2779db39934babbbf8a94e3559c910"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/DIRECTORY_REQUEST.disabled.json","sha256":"b27e00424c7f670347776e704be4e0e4d83df3b83c0a59ff79b2f1dc2ca68c73"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/DOCUMENTARY_CHECK01.json","sha256":"1bca0e8ff95b69acdf2f90ab7c558cac7c946f7ac368e18914c25ba846b772e3"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/DOCUMENTARY_NATIVE.json","sha256":"a6291de898e88cd843569d8569ba8d9be8b12a9075d2c5a968cf84699ad1c0aa"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/FILE_REQUEST.disabled.json","sha256":"c81d8d5e3fd5e4305c0871365832dca0256256ffd63a899686c236b0fb3df790"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/HANDOFF.md","sha256":"5646008e7943787cec097104c038959aae291292d6b5c656b53ec04854dd27bc"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/INPUTS.sha256","sha256":"8b272d0277e21d4be04f25fed9fb7635470f822c4b3e9ce96c2c79c64036d4f3"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/OBLIGATION_DELTA.md","sha256":"7ccc470b31a5903af44f6364484b1303284ab438d78c057e7e47176b2350e733"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/PRIMARY_SOURCE_EVIDENCE.json","sha256":"d8b6d4b371683d0429c8dd69b3403287f20b083a5105ac9635a75295b923cd32"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/REQUEST.disabled.json","sha256":"bdd262ecf3029d86c7e811d98f7a5d0bd1bbed9fcd73978e48a47f22b1d539d4"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/SOURCE_ORIGIN.md","sha256":"58ab8a9c8fe3dec8e16c35c3c97d430972549e5db70c61dcfd8d237686a236aa"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/capture.js","sha256":"c0369d9c6d0b623f59620884ef7b6252c9d99c98ff38a73168d0eba9733b8063"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/file_keys.mjs","sha256":"448b7a0c17ddc708fd14a9adb15beef5b5eb8b5081fd7480045b00c80973b896"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/receive.mjs","sha256":"adc0570ff23bece682812c77e69a2e8e7e9e1bcc64cba87c970e97f390202421"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_root01/RECEPTION.md","sha256":"663fcfdaf3d0541acb3199f2bc31f0e55050f75b74480c025df97abbf78ac1f7"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_root01/SHA256SUMS","sha256":"e2a1d505ebcaf7685a0e1f89cfe5f971514adb588265aefe0dab4bf3610a1c12"},{"path":"AGENTS.md","sha256":null},{"path":".agents/skills/symbolic-dynamics-research/SKILL.md","sha256":null},{"path":"docs/research_state/WORKFLOW.md","sha256":null}];
const OUTDIR="docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_preparation01";
const OWN_NAMES=["file_keys.proposed.mjs.txt","collect_files.proposed.mjs.txt","capture.proposed.sh.txt","FILE_REQUEST.proposed.json","DRAFT_ENTRY01.mjs.txt","ENTRY_REQUEST.proposed.json","SOURCE_DELTA.json","PINSET.json","INPUTS.sha256","CONTRACT.md","SOURCE_ORIGIN.md","HANDOFF.md","CHECK_DOCUMENTS.cjs","CLOSE.cjs","READ_NATIVE.json","CREATION_NATIVE.json","CHECK_NATIVE.json","DOCUMENTARY_RESULT.json"];
const EXPECTED_REQUEST={"cmd":"node docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_preparation01/CHECK_DOCUMENTS.cjs","workdir":"/root/autodl-tmp/symbolic_dynamics","max_output_tokens":100000};
const ALLOWED=new Set([...INPUT_SPEC.map(x=>x.path),...OWN_NAMES.map(n=>OUTDIR+'/'+n)]);

const report={schema:"p212-eight-file-documentary-preseal-closure-v1",status:"RUNNING",
 operation_authorized:false,independent_review:null,observed_eight_file_result:null};
try {
 for(const p of INPUT_SPEC) {
  const actual=pin(p.path);
  if(p.sha256!==null) need(actual.sha256===p.sha256,"SELECTED_FROZEN_INPUT_PIN");
 }
 for(const name of OWN_NAMES) fullRead(OUTDIR+"/"+name);
 need(equal(fs.readdirSync(OUTDIR).sort(),OWN_NAMES.slice().sort()),"EXACT_EIGHTEEN_PRESEAL_PAYLOADS");
 const native=JSON.parse(fullRead(OUTDIR+"/CHECK_NATIVE.json").toString("utf8"));
 need(native.tool==="exec_command"&&equal(native.request,EXPECTED_REQUEST),"ACTUAL_WHOLE_CHECKER_REQUEST");
 need(native.result.exit_code===0&&!native.result.session_id&&typeof native.result.chunk_id==="string","ACTUAL_CHECKER_FINAL_ZERO");
 need(Buffer.from(native.result.output).equals(fullRead(OUTDIR+"/DOCUMENTARY_RESULT.json")),"ACTUAL_COMPLETE_STDOUT_DOCUMENTARY_RESULT_RAW_EQUAL");
 const checked=JSON.parse(native.result.output);
 need(checked.status==="PASS_DOCUMENTARY_SOURCE_CONSISTENCY_ONLY"&&checked.key_count===41,"ACTUAL_PASS_DOCUMENTARY_ONLY");
 need(checked.operation_authorized===false&&checked.independent_review===null&&checked.source_import_parse_ast_syntax_or_execution===false,"NO_SOURCE_EXECUTION_ACCEPTANCE_OR_AUTHORITY");
 for(const old of checked.keys) {
  const now=keys.find(k=>k.path===old.path);
  need(!!now,"PRIOR_KEY_PRESENT");
  for(const field of ["eof","eof_zero_return","byte_count","complete","closed","sha256",
   "lstat_before","fd_before","fd_after","lstat_after"])
   need(equal(old[field],now[field]),"PRIOR_FULL_KEY_UNCHANGED:"+field);
 }
 report.prior_key_count=checked.keys.length;
 report.native_checker={chunk_id:native.result.chunk_id,exit_code:native.result.exit_code,
   checks:checked.checks,status:checked.status,stdout_bytes:Buffer.byteLength(native.result.output),
   stdout_sha256:hash(Buffer.from(native.result.output))};
 report.payloads=OWN_NAMES.slice().sort().map(name=>({name,...pin(OUTDIR+"/"+name)}));
 report.status="PASS_PRESEAL_DOCUMENTARY_CLOSURE_ONLY";
} catch(error) {
 report.status="FAIL_PRESEAL_DOCUMENTARY_CLOSURE_ONLY";
 report.failure={name:error.name,code:error.code||null,message:error.message};process.exitCode=1;
}
report.checks=checks;report.key_count=keys.length;report.total_read_bytes=totalRead;report.keys=keys;
process.stdout.write(JSON.stringify(report,null,2)+"\n");
