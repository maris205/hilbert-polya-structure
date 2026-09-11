'use strict';
// Root documentary receiver. Never imports/evaluates submitted Python or reads host/private roles.
const fs = require('fs'), path = require('path'), crypto = require('crypto');
const ROOT = '/root/autodl-tmp/symbolic_dynamics';
const QA = 'docs/papers211_215_sequence/qa/';
const A = QA + 'private_checkpoint_executor_ssh_delta04/';
const B = QA + 'private_checkpoint_executor_ssh_audit04/';
const R = QA + 'private_checkpoint_executor_ssh_root04/';
const OLD = QA + 'private_checkpoint_executor_preparation03/';
const fields = ['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const keys = new Map(); let checks = 0, matchedReadBytes = 0, matchedReads = 0;
function need(ok, msg) { checks++; if (!ok) throw Error(msg); }
function eq(a,b,msg) { need(JSON.stringify(a) === JSON.stringify(b), msg); }
function sha(b) { return crypto.createHash('sha256').update(b).digest('hex'); }
function stamp(s) { return Object.fromEntries(fields.map(k => [k, String(s[k])])); }
function read(rel) {
  need(rel.startsWith('docs/') && path.posix.normalize(rel) === rel && !rel.includes('..'), 'workspace relative only '+rel);
  const abs = ROOT + '/' + rel, s = fs.lstatSync(abs,{bigint:true});
  need(s.isFile() && !s.isSymbolicLink() && s.size <= 16000000n, 'bounded workspace regular '+rel);
  const fd = fs.openSync(abs,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);
  let bytes; try {
    const f = fs.fstatSync(fd,{bigint:true}); eq(stamp(s),stamp(f),'same-fd before '+rel);
    bytes = fs.readFileSync(fd); eq(stamp(f),stamp(fs.fstatSync(fd,{bigint:true})),'same-fd after '+rel);
  } finally { fs.closeSync(fd); }
  eq(stamp(s),stamp(fs.lstatSync(abs,{bigint:true})),'path closing '+rel);
  need(bytes.length === Number(s.size),'whole bytes '+rel);
  const key = {path:rel,bytes:bytes.length,sha256:sha(bytes),metadata:stamp(s)};
  if (keys.has(rel)) eq(key,keys.get(rel),'unchanged repeated key '+rel); else keys.set(rel,key);
  return bytes;
}
function text(rel) { return read(rel).toString('utf8'); }
function json(rel) { return JSON.parse(text(rel)); }
function pinLines(rel, prefix, expected) {
  const body = text(rel); need(body.endsWith('\n'),'pin final LF');
  const rows=body.trimEnd().split('\n'); need(rows.length === expected,'pin count '+rel);
  const names=new Set();
  for (const row of rows) {
    const m=/^([0-9a-f]{64})  ([^\r\n]+)$/.exec(row); need(!!m,'pin syntax');
    need(!names.has(m[2]),'unique pin'); names.add(m[2]);
    need(sha(read(prefix+m[2]))===m[1],'pin bytes '+m[2]);
  }
  return names;
}
function seal(dir, count, digest) {
  need(sha(read(dir+'SHA256SUMS'))===digest,'fixed package seal '+dir);
  const names=pinLines(dir+'SHA256SUMS',dir,count);
  eq(fs.readdirSync(ROOT+'/'+dir).sort(),[...names,'SHA256SUMS'].sort(),'complete package membership '+dir);
}
function slice(rel,first,last) {
  const lines=text(rel).match(/[^\n]*\n|[^\n]+$/g)||[];
  return Buffer.from(lines.slice(first-1,last).join(''),'utf8');
}
function actual(rec, expected, label) {
  need(rec.result && rec.result.exit_code===0 && typeof rec.result.chunk_id==='string','successful native '+label);
  const b=Buffer.from(rec.result.output,'utf8'); need(b.equals(expected),'raw full native '+label);
  matchedReads++; matchedReadBytes+=b.length;
}
seal(A,15,'101a5445cf0aaa3429a7a7a3e3f6a390b159598359e32c3594af88dcd559b818');
seal(B,13,'d7d442bde9c8c259cc83113cad15614d88b87fc1c482c4fc53ddf9a8cd6ea9a4');
pinLines(A+'INPUT_PINS.sha256','',7); pinLines(B+'INPUT_PINS.sha256','',22);
const old=text(OLD+'checkpoint.py'), next=text(A+'checkpoint.py');
need(old.split('\n').length-1===774 && next.split('\n').length-1===804,'source lines');
need(Buffer.byteLength(old)===45584 && Buffer.byteLength(next)===47072,'source bytes');
const oldCommand="        GIT_SSH_COMMAND='/usr/bin/ssh -o BatchMode=yes -o StrictHostKeyChecking=yes '\n                        '-o ConnectTimeout=20 -o ConnectionAttempts=1')";
const start=next.indexOf('        GIT_SSH_COMMAND='), end=next.indexOf('\n    if index is not None:',start);
need(start>=0 && end>start,'literal block extent'); const block=next.slice(start,end);
let expected=old;
for(const [a,b]of [["PREP = QA / 'private_checkpoint_executor_preparation03'","PREP = QA / 'private_checkpoint_executor_ssh_delta04'"],[oldCommand,block]]) {
  need(expected.split(a).length===2,'one exact replacement'); expected=expected.replace(a,b);
}
need(expected===next,'entire exact two-replacement source');
const pieces=[...block.matchAll(/'([^'\n]*)'/g)].map(m=>m[1]); need(pieces.length===32,'literal pieces');
const command=pieces.join(''), tokens=command.split(' '), policy=json(A+'OPTION_POLICY.json');
need(command===policy.git_ssh_command,'literal policy'); eq(tokens,policy.command_prefix_tokens,'token policy');
const entries=[]; for(let i=0;i<tokens.length;i++) if(tokens[i]==='-o') entries.push(tokens[++i].split('='));
need(entries.length===31 && new Set(entries.map(e=>e[0])).size===31,'31 unique options');
eq(Object.fromEntries(entries),policy.explicit_o_fields,'all field values');
for(const s of policy.original_options_preserved) need(command.includes('-o '+s),'retained old option');
const diag=json(A+'DIAGNOSTIC_PROPOSALS.disabled.json');
need(diag.enabled===false && diag.current_operational_authority===false && diag.old_no_G_gate_relaxed===false,'diagnostics disabled');
eq(diag.proposals[0].argv,['/usr/bin/ssh','-V'],'D01 exact argv');
eq(diag.proposals[1].argv,tokens.concat(['-G','-o','CanonicalizePermittedCNAMEs=none','-l','git','-p','22','127.0.0.1']),'D02 exact argv');
eq(diag.proposals[1].semantic_fields_to_receive,policy.explicit_o_fields,'D02 fields');
need(diag.proposals.every(p=>p.enabled===false),'every diagnostic disabled');
const option=json(B+'OPTION_REVIEW.json'); need(option.rows.length===31,'review option rows');
eq(option.rows.map(r=>[r.name,r.value]),entries,'review31values');
need(option.rows.every(r=>r.installed_support==='UNKNOWN' && r.no_runtime_grant===true),'no installed grant');
const assessment=json(B+'ASSESSMENT.json');
need(assessment.blocking_source_findings.length===0 && assessment.authority_granted===false,'bounded verdict');
need(assessment.authorship_disclosure.reviewer_authored_old_checkpoint03===true && assessment.authorship_disclosure.reviewer_authored_delta04===false,'disclosed baseline authorship');
eq(assessment.source.changed_new_lines,[[24,24],[273,304]],'review scope');
const diff=json(R+'ACTUAL_DIFF_NATIVE.json'); need(diff.result.exit_code===1,'actual ordinary diff difference');
const diffBytes=Buffer.from(diff.result.output,'utf8'); need(diffBytes.equals(read(A+'EXACT_DELTA.patch')),'actual raw author patch');
need(diffBytes.equals(read(B+'ACTUAL_DELTA.patch')),'actual raw review patch');
need((diff.result.output.match(/^@@ /gm)||[]).length===2,'two diff hunks');
const ar=json(A+'NATIVE_READS_AND_CHECKS.json'); need(ar.records.length===12,'author native count');
for(const rec of ar.records) {
  const m=/^sed -n '(\d+),(\d+)p' (docs\/\S+)$/.exec(rec.request.cmd);
  if(m) actual(rec,slice(m[3],+m[1],+m[2]),'author '+rec.result.chunk_id);
}
need(ar.records.some(r=>r.result.chunk_id==='4bb7dd' && r.result.exit_code===1),'author failure retained');
const ac=json(A+'AUTHOR_CLOSING_CHECKS.json'), af=json(A+'FINAL_DOCUMENT_RECEIPT.json');
for(const [list,count] of [[ac.complete_document_key_set,13],[af.pre_receipt_payloads,14]]) {
  need(list.length===count,'author final key count'); for(const k of list){const b=read(k.path);need(b.length===k.bytes && sha(b)===k.sha256,'whole author final key '+k.path);}
}
const sr=json(B+'SOURCE_READS_NATIVE.json'); need(sr.reads.length===6,'six source slices');
for(const rec of sr.reads) actual(rec,slice(rec.path,rec.range[0],rec.range[1]),'review source '+rec.result.chunk_id);
for(const tag of ['old','new']) {
  const rows=sr.reads.filter(r=>r.tag===tag); need(rows.length===3,'three slices '+tag);
  const joined=Buffer.concat(rows.map(r=>Buffer.from(r.result.output,'utf8')));
  need(joined.equals(Buffer.from(tag==='old'?old:next)),'complete source coverage '+tag);
}
const dr=json(B+'DOCUMENT_READS_NATIVE.json'); need(dr.reads.length===11,'eleven whole documents');
for(const rec of dr.reads) {
  let p=rec.path;
  if(p===undefined) {
    need(rec.request.cmd==="sed -n '1,260p' "+OLD+'SOURCE_CONTRACT.md','exact exceptional old-contract read');
    p=OLD+'SOURCE_CONTRACT.md';
  }
  actual(rec,read(p),'whole review document '+rec.result.chunk_id);
}
const cs=json(B+'CHECKS_NATIVE.json'), close=json(B+'CLOSING_NATIVE.json');
need(cs.checks.length===8 && close.first_closing_attempts.length===5 && close.actual_json_read_parse_records.length===7,'native archive dimensions');
need(cs.checks.some(r=>r.result.chunk_id==='b54ef2'&&r.result.exit_code===2),'review failed path retained');
need(cs.checks.some(r=>r.result.chunk_id==='31c433'&&r.result.exit_code===0&&r.result.output===''),'actual raw cmp retained');
need(close.first_closing_attempts.some(r=>r.result.chunk_id==='69b6cb'&&r.result.exit_code===127),'jq failure retained');
const before=cs.checks.find(r=>r.result.chunk_id==='e49c66'), after=close.first_closing_attempts.find(r=>r.result.chunk_id==='ec6806');
actual(before,read(B+'INPUT_PINS.sha256'),'initial22keyoutput'); actual(after,read(B+'INPUT_PINS.sha256'),'closing22keyoutput');
for(const rec of close.actual_json_read_parse_records) {
  actual(rec,read(B+rec.name),'JSON original '+rec.name); need(rec.parse_result.valid_json===true,'reported data parse'); JSON.parse(rec.result.output);
}
actual(close.final_scope_and_local_link_check,read(B+'READ_SCOPE.md'),'final scope read');
const prose=['REPORT.md','PRIMARY_ARGUMENT.md','READ_SCOPE.md'];
const proseNative=close.first_closing_attempts.find(r=>r.result.chunk_id==='24f605');
const lateDisclosure="The proposed jq-only JSON check returned exit 127 because jq was unavailable.\nNo installation or source interpreter was substituted. The actual workspace\nJSON files were then read completely as text and parsed as data in the\norchestration context; all seven parsed successfully. The failed attempt\nand the successful read/parse records remain separately preserved.\n";
const currentScope=text(B+'READ_SCOPE.md'); need(currentScope.split(lateDisclosure).length===2,'one exact later jq disclosure');
actual(proseNative,Buffer.concat([read(B+'REPORT.md'),read(B+'PRIMARY_ARGUMENT.md'),Buffer.from(currentScope.replace(lateDisclosure,''),'utf8')]),'two final reports and exact pre-jq historical scope');
// No commands stored in an evidence object are executed by this receiver.
for(const base of [A,B]) for(const name of fs.readdirSync(ROOT+'/'+base)) if(name.endsWith('.json')) JSON.parse(text(base+name));
read(R+'receive.cjs'); read(R+'receive02.cjs'); read(R+'FIRST_FAILED_NATIVE.json'); read(R+'receive03.cjs'); read(R+'SECOND_FAILED_NATIVE.json'); read(R+'HISTORICAL_SCOPE_DIAGNOSTIC_NATIVE.json');
const frozen=[...keys.values()]; for(const k of frozen) read(k.path);
process.stdout.write(JSON.stringify({status:'PASS_DOCUMENTARY_SOURCE_RECEPTION',checks,whole_workspace_keys:keys.size,author_payloads:15,independent_payloads:13,author_input_pins:7,independent_input_pins:22,matched_native_complete_reads:matchedReads,matched_native_read_bytes:matchedReadBytes,source_sha256:sha(Buffer.from(next)),raw_diff_bytes:diffBytes.length,source_hunks:2,options:31,source_execution:false,host_or_private_reads:false,operational_authority:false,keys:[...keys.values()]},null,2)+'\n');
