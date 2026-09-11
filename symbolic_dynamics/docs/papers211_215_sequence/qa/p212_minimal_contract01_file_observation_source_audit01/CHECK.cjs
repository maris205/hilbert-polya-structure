'use strict';
// Independently authored documentary verifier. No submitted source is loaded,
// parsed as JavaScript, compiled, tested or run; operational path strings are DATA.
const fs=require('node:fs'), crypto=require('node:crypto');
const W='/root/autodl-tmp/symbolic_dynamics';
const Q='docs/papers211_215_sequence/qa/';
const A=Q+'p212_minimal_contract01_file_observation_preparation01';
const O=Q+'p212_minimal_contract01_source_preparation01';
const R=Q+'p212_minimal_contract01_source_root01';
const D=Q+'p212_minimal_contract01_file_observation_source_audit01';
const AN=['CHECK_DOCUMENTS.cjs','CHECK_NATIVE.json','CLOSE.cjs','CLOSING_NATIVE.json','CONTRACT.md','CREATION_NATIVE.json','DOCUMENTARY_RESULT.json','DRAFT_ENTRY01.mjs.txt','ENTRY_REQUEST.proposed.json','FILE_REQUEST.proposed.json','HANDOFF.md','INPUTS.sha256','PINSET.json','READ_NATIVE.json','SOURCE_DELTA.json','SOURCE_ORIGIN.md','capture.proposed.sh.txt','collect_files.proposed.mjs.txt','file_keys.proposed.mjs.txt','SHA256SUMS'];
const ON=['ARCHIVAL_DISPOSITIONS.json','BINDING.disabled.json','CLOSING_KEYS.json','CLOSING_NATIVE.json','CONTRACT.md','DEPENDENCY_GATE.md','DIRECTORY_REQUEST.disabled.json','DOCUMENTARY_CHECK01.json','DOCUMENTARY_NATIVE.json','FILE_REQUEST.disabled.json','HANDOFF.md','INPUTS.sha256','OBLIGATION_DELTA.md','PRIMARY_SOURCE_EVIDENCE.json','REQUEST.disabled.json','SOURCE_ORIGIN.md','capture.js','file_keys.mjs','receive.mjs','SHA256SUMS'];
const EXTRA=['AGENTS.md','.agents/skills/symbolic-dynamics-research/SKILL.md','docs/research_state/WORKFLOW.md','docs/papers211_215_sequence/PROBLEM_ANCHOR.md',R+'/RECEPTION.md',R+'/SHA256SUMS'];
const BASE=[...AN.map(n=>A+'/'+n),...ON.map(n=>O+'/'+n),...EXTRA];
const FIELDS=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
const PHASE1=['file_keys.proposed.mjs.txt','collect_files.proposed.mjs.txt','capture.proposed.sh.txt','FILE_REQUEST.proposed.json','DRAFT_ENTRY01.mjs.txt','ENTRY_REQUEST.proposed.json','SOURCE_DELTA.json'];
const PHASE2=[...PHASE1,'PINSET.json','INPUTS.sha256','CONTRACT.md','SOURCE_ORIGIN.md','HANDOFF.md','CHECK_DOCUMENTS.cjs','CLOSE.cjs','READ_NATIVE.json','CREATION_NATIVE.json'];
const PHASE3=[...PHASE2,'CHECK_NATIVE.json','DOCUMENTARY_RESULT.json'];
const stable=v=>JSON.stringify(v);
function context(ownNames) {
  const allowed=new Set([...BASE,...ownNames.map(n=>D+'/'+n)]);
  const c={checks:0,readBytes:0,keys:[],pairs:[],jsonNumbers:0,jsonStructures:0,cache:new Map(),allowed};
  c.need=(v,m)=>{c.checks++;if(!v)throw Error(m);};
  c.hash=b=>crypto.createHash('sha256').update(b).digest('hex');
  c.stat=s=>Object.fromEntries(FIELDS.map(k=>{c.need(typeof s[k]==='bigint','actual_bigint:'+k);return[k,s[k].toString()];}));
  c.eq=(a,b,m)=>c.need(stable(a)===stable(b),m);
  c.raw=(a,b,m)=>{c.need(Buffer.isBuffer(a)&&Buffer.isBuffer(b)&&a.equals(b),m);c.pairs.push({label:m,bytes:a.length,sha256:c.hash(a)});};
  c.read=p=>{
    c.need(allowed.has(p),'fixed_document_permission:'+p);
    if(c.cache.has(p))return c.cache.get(p);
    const row={path:p,eof:false,eof_zero_return:null,byte_count:0,complete:false,closed:false};
    c.keys.push(row);let fd=null;
    try {
      const st=fs.lstatSync(p,{bigint:true});row.lstat_before=c.stat(st);
      c.need(st.isFile()&&!st.isSymbolicLink()&&st.size>=0n&&st.size<=8388608n,'fixed_regular_document');
      fd=fs.openSync(p,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);
      row.fd_before=c.stat(fs.fstatSync(fd,{bigint:true}));c.eq(row.lstat_before,row.fd_before,'same_fd_before');
      const chunks=[],block=Buffer.alloc(65536);
      for(;;) {
        const n=fs.readSync(fd,block,0,block.length,null);
        c.need(Number.isInteger(n)&&n>=0&&n<=block.length,'real_read_return');
        if(n===0){row.eof=true;row.eof_zero_return=0;break;}
        row.byte_count+=n;c.readBytes+=n;
        c.need(row.byte_count<=8388608&&c.readBytes<=67108864,'document_byte_bounds');
        chunks.push(Buffer.from(block.subarray(0,n)));
      }
      row.fd_after=c.stat(fs.fstatSync(fd,{bigint:true}));
      row.lstat_after=c.stat(fs.lstatSync(p,{bigint:true}));
      c.eq(row.fd_before,row.fd_after,'same_fd_after');c.eq(row.lstat_before,row.lstat_after,'same_endpoint_after');
      c.need(BigInt(row.byte_count)===st.size,'complete_actual_eof_size');
      const b=Buffer.concat(chunks);row.sha256=c.hash(b);
      fs.closeSync(fd);fd=null;row.closed=true;row.complete=true;
      const t=b.toString('utf8');c.need(Buffer.from(t,'utf8').equals(b),'whole_document_utf8_reversible');
      c.cache.set(p,b);return b;
    }catch(e){row.failure={name:e.name,code:e.code||null,message:e.message};throw e;}
    finally{if(fd!==null){try{fs.closeSync(fd);row.closed=true;}catch(e){row.close_failure={name:e.name,code:e.code||null,message:e.message};throw e;}}}
  };
  c.text=p=>c.read(p).toString('utf8');
  c.pin=p=>{const b=c.read(p);return{path:p,bytes:b.length,sha256:c.hash(b)};};
  // Lexical number scan before JSON.parse: skip whole quoted strings, preserve
  // the original buffers, refuse unsafe integral tokens; floats remain raw-pinned.
  c.parse=(raw,label,canonical=false)=>{
    c.need(Buffer.isBuffer(raw),'json_raw_buffer');
    const t=raw.toString('utf8');c.need(Buffer.from(t).equals(raw),'json_utf8_reversible');
    let i=0;
    while(i<t.length) {
      if(t[i]==='"'){i++;while(i<t.length){if(t[i]==='\\'){i+=2;continue;}if(t[i++]==='"')break;}continue;}
      if(t[i]==='-'||(t[i]>='0'&&t[i]<='9')) {
        const m=t.slice(i).match(/^-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?/);
        c.need(!!m,'json_number_lexeme');const token=m[0],value=Number(token);
        c.need(Number.isFinite(value),'json_finite_number');
        if(!/[.eE]/.test(token))c.need(Number.isSafeInteger(value)&&BigInt(token)===BigInt(value),'json_exact_integer_token');
        c.jsonNumbers++;i+=token.length;continue;
      }i++;
    }
    const v=JSON.parse(t);
    const walk=x=>{c.jsonStructures++;if(x&&typeof x==='object')for(const y of Object.values(x))walk(y);};
    walk(v);
    if(canonical)c.raw(Buffer.from(JSON.stringify(v,null,2)+'\n'),raw,'entire_json_canonical:'+label);
    return v;
  };
  c.data=(p,canonical=false)=>c.parse(c.read(p),p,canonical);
  c.oldKey=k=>{
    c.need(k&&allowed.has(k.path),'old_key_fixed_document_only');
    c.read(k.path);const current=c.keys.find(r=>r.path===k.path);
    for(const name of ['lstat_before','fd_before','fd_after','lstat_after']) {
      c.eq(Object.keys(k[name]).sort(),FIELDS.slice().sort(),'all_ten_old_fields');
      for(const field of FIELDS)c.need(typeof k[name][field]==='string'&&/^-?(0|[1-9][0-9]*)$/.test(k[name][field])&&k[name][field]!=='-0','exact_old_bigint_decimal');
    }
    for(const name of ['path','eof','eof_zero_return','byte_count','complete','closed','sha256','lstat_before','fd_before','fd_after','lstat_after'])
      c.eq(k[name],current[name],'old_whole_key:'+name);
  };
  c.inventory=(dir,names,sealHash,expectedPayloadBytes)=>{
    const seal=c.read(dir+'/SHA256SUMS');c.need(c.hash(seal)===sealHash,'whole_external_seal_pin');
    const lines=seal.toString('utf8').split('\n');c.need(lines.pop()==='','manifest_final_lf');
    const rows=lines.map(l=>{const m=l.match(/^([0-9a-f]{64})  ([A-Za-z0-9_.-]+)$/);c.need(!!m,'strict_manifest_row');return{sha256:m[1],name:m[2]};});
    c.eq(rows.map(r=>r.name),names.filter(n=>n!=='SHA256SUMS').slice().sort(),'complete_nonself_manifest_names');
    c.eq(fs.readdirSync(dir).sort(),names.slice().sort(),'complete_fixed_directory_inventory');
    let bytes=0;for(const row of rows){const p=c.pin(dir+'/'+row.name);c.need(p.sha256===row.sha256,'whole_payload_pin');row.bytes=p.bytes;bytes+=p.bytes;}
    c.need(bytes===expectedPayloadBytes,'exact_payload_bytes');
    return{directory:dir,payloads:rows.length,files:names.length,payload_bytes:bytes,physical_bytes:bytes+seal.length,seal:{bytes:seal.length,sha256:c.hash(seal)},rows};
  };
  return c;
}
function run() {
 const own=['CHECK.cjs','CLOSE.cjs','READ_NATIVE.json','WEB_NATIVE.json'];
 const c=context(own),report={schema:'p212-eight-file-independent-documentary-check-v1',status:'RUNNING',source_program_executed:false,host_or_future_path_observation:false,operation_authorized:false,science_or_build:false};
 try {
  for(const p of [...BASE,...own.map(n=>D+'/'+n)])c.read(p);
  report.author=c.inventory(A,AN,'8a296cda89323b49cef3a6797a3e8d75b47f0966ff9b440e2c57bc29f0415d0e',736027);
  report.original=c.inventory(O,ON,'523e5f3c361a41fd36f8e25f16f03a8cdfd6fdcb035df20dd2eabfb9bafdff40',1321223);
  c.need(c.hash(c.read(R+'/RECEPTION.md'))==='663fcfdaf3d0541acb3199f2bc31f0e55050f75b74480c025df97abbf78ac1f7','accepted_policy_premise');
  c.need(c.hash(c.read(R+'/SHA256SUMS'))==='e2a1d505ebcaf7685a0e1f89cfe5f971514adb588265aefe0dab4bf3610a1c12','accepted_policy_seal_premise');
  const lines=c.text(A+'/INPUTS.sha256').split('\n');c.need(lines.pop()==='','inputs_final_lf');
  const imported=lines.map(l=>{const m=l.match(/^([0-9a-f]{64})  (.+)$/);c.need(!!m&&BASE.includes(m[2]),'fixed_input_pin_scope');c.need(c.hash(c.read(m[2]))===m[1],'whole_author_input_pin');return m[2];});
  c.need(imported.length===25&&new Set(imported).size===25,'all_twenty_five_input_pins');
  const delta=c.data(A+'/SOURCE_DELTA.json',true),entry=c.data(A+'/ENTRY_REQUEST.proposed.json',true),pins=c.data(A+'/PINSET.json',true),template=c.data(A+'/FILE_REQUEST.proposed.json',true);
  const pinCheck=p=>{const real=c.pin(p.path);c.need(real.bytes===p.bytes&&real.sha256===p.sha256,'complete_source_pin');if('lines'in p)c.need(c.text(p.path).split('\n').length-1===p.lines,'whole_source_line_count');};
  for(const p of pins.documents)pinCheck(p);
  c.need(pins.documents.length===7,'seven_core_document_pins');
  for(const p of [delta.root_reception,delta.original_reader,delta.proposed_reader,delta.original_file_request,delta.proposed_file_request,delta.complete_new_entry_source,delta.complete_new_capture_source,delta.unexecuted_entry_draft.preserved_carrier,delta.unexecuted_entry_draft.current_carrier,delta.old_capture_source_unchanged,delta.old_receiver_source_unchanged])pinCheck(p);
  const old=c.read(O+'/file_keys.mjs'),now=c.read(A+'/file_keys.proposed.mjs.txt');
  let at=0;const pieces=[];
  c.need(delta.reader_edits.length===2,'exact_two_source_edits');
  for(const e of delta.reader_edits){const before=Buffer.from(e.old_text);c.need(Number.isSafeInteger(e.old_byte_offset)&&e.old_byte_offset>=at,'ordered_raw_edit');c.raw(old.subarray(e.old_byte_offset,e.old_byte_offset+before.length),before,'old_exact_edit_span');pieces.push(old.subarray(at,e.old_byte_offset),Buffer.from(e.new_text));at=e.old_byte_offset+before.length;}
  pieces.push(old.subarray(at));c.raw(Buffer.concat(pieces),now,'whole_two_edit_reader_derivation');
  const marker=Buffer.from(delta.unchanged_directory_suffix_starts),oi=old.indexOf(marker),ni=now.indexOf(marker);
  c.need(oi>0&&ni>0,'literal_directory_suffix_marker');c.raw(old.subarray(oi),now.subarray(ni),'entire_unchanged_disabled_directory_suffix');
  c.need(now.subarray(ni).includes(Buffer.from('const SOURCE_ENABLED = false;')),'directory_still_disabled');
  c.raw(c.read(A+'/FILE_REQUEST.proposed.json'),c.read(O+'/FILE_REQUEST.disabled.json'),'entire_eight_file_request_unchanged');
  c.eq(template.entries,entry.exact_eight_candidates,'complete_eight_ordered_entries');
  c.need(template.entries.length===8&&template.entries.reduce((s,e)=>s+e.max_bytes,0)===102760448,'eight_limits_sum');
  c.need(template.total_byte_limit===102760448&&template.entries.every(e=>e.expected===null&&e.capture_hex===true),'fixed_bound_and_no_fabricated_key');
  c.need(template.enabled===false&&template.permission_receipt===null&&template.settlement_receipt===null,'no_current_request_authority');
  const src=c.text(A+'/collect_files.proposed.mjs.txt'),draft=c.text(A+'/DRAFT_ENTRY01.mjs.txt'),ud=delta.unexecuted_entry_draft;
  c.need(draft.split(ud.changes.old_finally).length===2,'unique_draft_finally');
  let derived=draft.replace(ud.changes.old_finally,ud.changes.new_finally);
  for(const [a,b]of ud.exact_text_replacements){c.need(derived.includes(a),'draft_exact_replacement');derived=derived.split(a).join(b);}
  c.raw(Buffer.from(derived),c.read(A+'/collect_files.proposed.mjs.txt'),'whole_preserved_draft_derivation');
  c.need(src.includes('const TEMPLATE = '+JSON.stringify(template,null,2)+';'),'whole_inline_template_text');
  c.need(src.includes('const REQUEST_PATH = '+JSON.stringify(entry.proposed_bound_request.future_path)+';'),'fixed_request_path_DATA_correspondence');
  c.need(src.split('readerResult=collectP212S0Files(request);').length===2,'single_reader_call_site');
  c.raw(Buffer.from(entry.proposed_native_request.arguments.cmd),c.read(A+'/capture.proposed.sh.txt'),'entire_proposed_native_cmd_raw');
  c.eq({...entry.proposed_native_request.arguments,cmd:null},{cmd:null,workdir:W,shell:'/bin/bash',login:false,tty:false,yield_time_ms:1000,max_output_tokens:4000},'all_prospective_tool_arguments');
  c.eq(entry.proposed_continuation.arguments,{session_id:null,chars:'',yield_time_ms:10000,max_output_tokens:4000},'complete_disabled_same_session_poll');
  c.eq(entry.proposed_bound_request.allowed_later_delta,['enabled','status','permission_receipt'],'only_three_future_activation_fields');
  const nulls=['request_cmd','operation_request','root_grant','actual_native_request','actual_native_result','actual_session_id','actual_continuations','target_directory','target_directory_key','actual_destination_keys','actual_bound_request','actual_bound_request_key','actual_input_keys','independent_source_acceptance','root_source_acceptance','materialization_receipt','new_observation_grant','actual_stdout','actual_stderr','actual_output_canonical_pin'];
  const falses=['operation_authorized','new_observation_grant_consumed','observation_accepted','installed_closure_accepted','operation_permission','future_path_queried','future_path_materialized','directory_guard_enabled','help_version_capture_enabled','old_receiver_enabled','author_self_review'];
  for(const n of nulls)c.need(entry[n]===null,'future_role_null:'+n);
  for(const n of falses)c.need(entry[n]===false,'future_role_false:'+n);
  for(const p of entry.prospective_sources){pinCheck(p.documentary_carrier);c.need(p.actual_future_key===null,'future_source_key_null');}
  for(const n of ['actual_bytes','actual_pin','actual_nonself_before_key','actual_nonself_after_key'])c.need(entry.proposed_bound_request[n]===null,'future_bound_input_null');
  for(const n of ['actual_complete_native_originals','closed_stdout_key','closed_stderr_key','canonical_reencoding_raw_equal','actual_semantic_receipt'])c.need(entry.later_reception[n]===null,'future_reception_null');
  for(const n of ['complete_canonical_parse_and_raw_bytes_received','complete_reader_rows_received','existing_receive_mjs_enabled','old_closed_raw_file_request_compatible'])c.need(entry.later_reception[n]===false,'future_reception_false');
  c.need(entry.bounds.candidate_read_bytes_including_one_possible_overflow_sentinel===102760449&&entry.bounds.candidate_hex_characters_including_one_possible_overflow_sentinel===205520898,'sentinel_and_hex_arithmetic');
  c.need(16384*6===98304&&205520898<268435456,'string_chunk_and_candidate_hex_bounds');
  const clauses=['const REQUEST_BYTE_LIMIT = 65536;','const OUTPUT_BYTE_LIMIT = 268435456;','const DIAGNOSTIC_BYTE_LIMIT = 8388608;','const MAX_VALUE_NODES = 8192;','const MAX_VALUE_DEPTH = 32;','const IDENTITY = FIELDS.slice(0,7);',"need(typeof s[k] === 'bigint','ACTUAL_BIGINT_FILE_FIELD');","const withoutActivation={...request,enabled:false,status:TEMPLATE.status,permission_receipt:null};","need(same(withoutActivation,TEMPLATE),'EXACT_EIGHT_UNCHANGED_CANDIDATES_AND_LIMITS');",'fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK','if (count===0) { record.eof=true; break; }',"need(count<=remaining,'REQUEST_OVERFLOW_SENTINEL_PRESERVED');",'if (closeFailure!==null) throw closeFailure;',"const piece=value.slice(at,at+16384).replace(/[^\\x20-\\x21\\x23-\\x5b\\x5d-\\x7e]/g,","ch=>'\\\\u'+ch.charCodeAt(0).toString(16).padStart(4,'0'));",'Object.getOwnPropertyDescriptor(value,String(i))','Object.getOwnPropertyDescriptor(value,name)',"Object.prototype.hasOwnProperty.call(d,'value')","Number.isSafeInteger(value)&&!Object.is(value,-0)","writer.written+buffer.length<=writer.limit",'offset+=count; writer.written+=count;',"'ENCODER_DATA_ONLY_NO_CYCLE'","writer.document = value => { writer.value(value); writer.ascii('\\n'); };","BigInt(now.size)===BigInt(writer.written)","readerResult.status==='OBSERVED_ROOT_RECEPTION_PENDING'?0:78","diagnosticOnly('failure_envelope_incomplete',secondary,error);","fs.closeSync(1)","process.exitCode=exitCode;"];
  for(const x of clauses)c.need(src.includes(x),'reviewed_literal_clause:'+x);
  report.source_clauses=clauses.length;
  // Read helper constants as JSON DATA only, never eval the JavaScript source.
  const checker=c.text(A+'/CHECK_DOCUMENTS.cjs'),closer=c.text(A+'/CLOSE.cjs');
  const literal=(source,name)=>{const lead='const '+name+'=',lines=source.split('\n').filter(l=>l.startsWith(lead));c.need(lines.length===1&&lines[0].endsWith(';'),'one_literal_document_constant');return c.parse(Buffer.from(lines[0].slice(lead.length,-1)),name);};
  c.eq(literal(checker,'EXPECTED_ENTRY'),entry,'complete_checker_expected_entry_DATA');
  c.eq(literal(checker,'EXPECTED_DELTA'),delta,'complete_checker_expected_delta_DATA');
  c.eq(literal(checker,'OWN_NAMES'),PHASE2,'historical_sixteen_file_phase');
  c.eq(literal(closer,'OWN_NAMES'),PHASE3,'historical_eighteen_file_phase');
  const reads=c.data(A+'/READ_NATIVE.json',true),created=c.data(A+'/CREATION_NATIVE.json',true),native=c.data(A+'/CHECK_NATIVE.json',true),closing=c.data(A+'/CLOSING_NATIVE.json',true);
  const actual=(e,expectedCmd)=>{
    c.need(e.tool==='exec_command','actual_native_tool');
    c.eq(e.request,{cmd:expectedCmd,workdir:W,max_output_tokens:100000},'entire_original_native_request');
    c.eq(Object.keys(e.result).sort(),['chunk_id','wall_time_seconds','exit_code','original_token_count','output'].sort(),'entire_native_return_fields');
    c.need(e.result.exit_code===0&&typeof e.result.output==='string'&&!e.result.output.startsWith('Warning: truncated output'),'complete_actual_native_zero');
    return c.parse(Buffer.from(e.result.output),e.result.chunk_id,true);
  };
  const checked=actual(native,'node '+A+'/CHECK_DOCUMENTS.cjs');
  const closed=actual(closing,'node '+A+'/CLOSE.cjs');
  c.raw(Buffer.from(native.result.output),c.read(A+'/DOCUMENTARY_RESULT.json'),'whole_original_documentary_stdout');
  c.need(reads.events.length===20&&reads.cutoff_first_chunk_id==='e1b001'&&reads.cutoff_last_chunk_id==='7b6a29','all_twenty_original_read_events');
  for(const e of reads.events)c.need(e.tool==='exec_command'&&e.result.exit_code===0&&!('session_id'in e.result)&&typeof e.result.output==='string'&&!e.result.output.startsWith('Warning: truncated output'),'original_read_event_complete');
  const byId=id=>{const e=reads.events.filter(e=>e.result.chunk_id===id);c.need(e.length===1,'unique_actual_read_id');return e[0];};
  const intake=c.parse(Buffer.from(byId('7b6a29').result.output),'intake_original',true);
  c.need(intake.status==='PASS_DOCUMENTARY_INPUT_BYTES_ONLY'&&intake.checks===437&&intake.key_count===32&&intake.total_read_bytes===1404071,'actual_initial_documentary_result');
  c.need(checked.status==='PASS_DOCUMENTARY_SOURCE_CONSISTENCY_ONLY'&&checked.checks===3293&&checked.key_count===41&&checked.total_read_bytes===1835423,'actual_historical_checker_result');
  c.need(closed.status==='PASS_PRESEAL_DOCUMENTARY_CLOSURE_ONLY'&&closed.key_count===43,'actual_historical_preseal_result');
  report.old_key_occurrences=0;
  for(const [r,names]of [[intake,PHASE1],[checked,PHASE2],[closed,PHASE3]]) {
    c.eq(r.keys.map(k=>k.path),[...imported,...names.map(n=>A+'/'+n)],'complete_phase_key_sequence');
    c.need(r.keys.length===r.key_count&&r.keys.reduce((s,k)=>s+k.byte_count,0)===r.total_read_bytes,'complete_phase_counts');
    for(const k of r.keys){c.oldKey(k);report.old_key_occurrences++;}
  }
  const slices=[['e1b001',EXTRA[1],1,200],['5e3dcb',EXTRA[2],1,160],['3366c6',R+'/RECEPTION.md',1,260],['713550',R+'/SHA256SUMS',1,260],['5c8eac',O+'/file_keys.mjs',1,260],['178f5c',O+'/FILE_REQUEST.disabled.json',1,260],['9c404c',O+'/CONTRACT.md',1,320],['b46ea2',O+'/OBLIGATION_DELTA.md',1,320],['44b268',O+'/DEPENDENCY_GATE.md',1,320],['8f8986',O+'/SHA256SUMS',1,320],['21346f',A+'/collect_files.proposed.mjs.txt',1,165],['ce0fc7',A+'/collect_files.proposed.mjs.txt',166,330],['e688e5',A+'/capture.proposed.sh.txt',1,30],['9924d7','AGENTS.md',1,200]];
  const slice=(p,start,end)=>Buffer.from((c.text(p).match(/[^\n]*\n|[^\n]+$/g)||[]).slice(start-1,end).join(''));
  for(const[id,p,start,end]of slices)c.raw(Buffer.from(byId(id).result.output),slice(p,start,end),'entire_original_read_range:'+id);
  const transferred=c.parse(Buffer.from(byId('792911').result.output),'whole_transfer');
  c.need(transferred.length===2,'two_full_original_source_carriers');
  for(const p of transferred){c.raw(Buffer.from(p.text),c.read(p.path),'whole_transfer_raw:'+p.path);c.need(Buffer.byteLength(p.text)===p.bytes,'whole_transfer_byte_count');}
  const oldPinRows=c.parse(Buffer.from(byId('1efb2a').result.output),'source_pin_read',true);
  c.need(oldPinRows.length===5,'five_original_source_pins');for(const p of oldPinRows)pinCheck(p);
  const inline=byId('7b6a29').request.cmd;
  c.need(inline.startsWith("node -e '")&&inline.endsWith("\n'"),'complete_inline_documentary_helper_carrier');
  const inlineSource=inline.slice(9,-1).split("'\\''").join("'");
  const prefix=checker.slice(0,checker.indexOf('const INPUT_SPEC='));
  c.raw(Buffer.from(inlineSource.slice(0,inlineSource.indexOf('const INPUT_SPEC='))),Buffer.from(prefix),'entire_inline_documentary_reader_prefix');
  c.eq(literal(inlineSource,'INPUT_SPEC'),literal(checker,'INPUT_SPEC'),'whole_inline_fixed_inputs_DATA');
  c.eq(literal(inlineSource,'OWN_NAMES'),PHASE1,'whole_inline_seven_source_inputs');
  c.eq(literal(inlineSource,'PACK'),literal(checker,'PACK'),'whole_inline_old_inventory_DATA');
  c.need(created.events.length===4,'all_four_creation_events');
  const expectedUpdate=literal(checker,'EXPECTED_UPDATE'),adds=[],updates=[];
  for(const[index,e]of created.events.entries()) {
    c.need(e.tool==='apply_patch'&&typeof e.request==='string','actual_whole_patch_request');
    c.eq(e.result,{},'actual_empty_patch_return_not_content_proof');
    const lines=e.request.split('\n');c.need(lines.shift()==='*** Begin Patch','patch_begin');
    let i=0;
    while(i<lines.length&&lines[i]!=='*** End Patch') {
      if(lines[i].startsWith('*** Add File: ')){
        const path=lines[i++].slice(14),body=[];
        while(i<lines.length&&!lines[i].startsWith('*** ')){c.need(lines[i].startsWith('+'),'full_add_body_line');body.push(lines[i++].slice(1));}
        const target=index===0&&path===A+'/collect_files.proposed.mjs.txt'?A+'/DRAFT_ENTRY01.mjs.txt':path;
        c.need(PHASE2.map(n=>A+'/'+n).includes(target),'fixed_creation_body_target');
        const bytes=Buffer.from(body.join('\n')+'\n');c.raw(bytes,c.read(target),'entire_creation_body:'+index+':'+target);
        adds.push({event_index:index,created_path:path,received_against:target,bytes:bytes.length});
      }else if(lines[i].startsWith('*** Update File: ')){
        const start=i++;while(i<lines.length&&!lines[i].startsWith('*** '))i++;
        const block=Buffer.from(lines.slice(start,i).join('\n')+'\n');c.need(index===1,'only_declared_update_event');
        c.raw(block,Buffer.from(expectedUpdate),'entire_preserved_draft_patch');
        updates.push({event_index:index,path:A+'/collect_files.proposed.mjs.txt',complete_update_bytes:block.length});
      }else throw Error('unrecognized_patch_directive');
    }
    c.need(lines[i]==='*** End Patch'&&lines.slice(i+1).every(x=>x===''),'patch_complete_end');
  }
  c.need(adds.length===14&&updates.length===1,'complete_creation_census');
  c.eq(adds,checked.native_evidence.add_bodies,'all_author_add_receipt_fields');
  c.eq(updates,checked.native_evidence.updates,'all_author_update_receipt_fields');
  c.eq(closed.payloads.map(p=>p.name),PHASE3.slice().sort(),'all_historical_eighteen_payloads');
  for(const p of closed.payloads)pinCheck(p);
  c.eq(closed.native_checker,{chunk_id:native.result.chunk_id,exit_code:0,checks:checked.checks,status:checked.status,stdout_bytes:Buffer.byteLength(native.result.output),stdout_sha256:c.hash(Buffer.from(native.result.output))},'entire_closing_native_checker_record');
  // Full structured closures checked above; not historical scripts rerun.
  const ownReads=c.data(D+'/READ_NATIVE.json',true);
  const ownEvent=n=>{const es=ownReads.events.filter(e=>e.label===n);c.need(es.length===1,'own_native_read_unique');return es[0];};
  const cat=paths=>Buffer.concat(paths.map(p=>c.read(p)));
  const combinations=[
    ['read01',cat([A+'/SHA256SUMS',A+'/INPUTS.sha256',A+'/SOURCE_ORIGIN.md',A+'/collect_files.proposed.mjs.txt'])],
    ['read02',cat([A+'/file_keys.proposed.mjs.txt',A+'/capture.proposed.sh.txt',A+'/CHECK_DOCUMENTS.cjs'])],
    ['read03',cat([A+'/CHECK_DOCUMENTS.cjs',A+'/CLOSE.cjs'])],
    ['read04',slice(A+'/CHECK_DOCUMENTS.cjs',65,95)],
    ['read05',Buffer.concat([c.read(O+'/capture.js'),slice(O+'/receive.mjs',1,140)])],
    ['read06',Buffer.concat([slice(O+'/receive.mjs',141,300),cat([O+'/BINDING.disabled.json',O+'/DIRECTORY_REQUEST.disabled.json',O+'/REQUEST.disabled.json'])])],
    ['read07',cat([O+'/CONTRACT.md',O+'/OBLIGATION_DELTA.md',O+'/DEPENDENCY_GATE.md'])],
    ['read09',Buffer.from(byId('7b6a29').request.cmd+'\n')],
    ['read10',cat([A+'/HANDOFF.md',A+'/CONTRACT.md'])],
    ['read11',cat([A+'/ENTRY_REQUEST.proposed.json',A+'/SOURCE_DELTA.json',A+'/PINSET.json',A+'/FILE_REQUEST.proposed.json'])],
    ['read12',cat([A+'/DRAFT_ENTRY01.mjs.txt',O+'/file_keys.mjs'])],
    ['read13',cat([O+'/SOURCE_ORIGIN.md',O+'/HANDOFF.md',R+'/RECEPTION.md',R+'/SHA256SUMS'])]
  ];
  for(const[n,expected]of combinations){const e=ownEvent(n);c.need(e.result.exit_code===0,'actual_own_read_zero');c.raw(Buffer.from(e.result.output),expected,'whole_independent_native_source_read:'+n);}
  c.need(ownEvent('read08').result.output.startsWith('Warning: truncated output'),'preserved_actual_truncated_metadata_attempt');
  const primary=c.data(D+'/WEB_NATIVE.json',true);c.need(primary.events.length===5,'all_five_actual_primary_calls');
  report.native_originals={author_read_events:20,creation_events:4,creation_add_bodies:14,creation_update_bodies:1,author_intake:{chunk:'7b6a29',checks:intake.checks,keys:intake.key_count},author_check:{chunk:native.result.chunk_id,checks:checked.checks,keys:checked.key_count},author_preseal:{chunk:closing.result.chunk_id,checks:closed.checks,keys:closed.key_count},historical_scripts_reexecuted:false,author_final_seal_native_original_in_packet:false};
  report.root_policy_premise={reception:c.pin(R+'/RECEPTION.md'),seal:c.pin(R+'/SHA256SUMS'),other_root_payloads_reaudited:false,accepted_premise_not_new_self_review:true};
  report.scope={personally_noncontributing:true,inherited_root_familiarity:true,source_semantics_by_manual_review:true,documentary_checks_not_semantic_proof:true,installed_correspondence_verified:false,old_grants_reused:false,source_materialized:false};
  report.inputs=BASE.map(p=>c.pin(p));
  report.status='PASS_EXACT_DOCUMENTARY_SOURCE_RECEIPT_ONLY';
 }catch(e){report.status='FAIL_EXACT_DOCUMENTARY_SOURCE_RECEIPT_ONLY';report.failure={name:e.name,code:e.code||null,message:e.message};process.exitCode=1;}
 report.checks=c.checks;report.key_count=c.keys.length;report.total_read_bytes=c.readBytes;report.json_numeric_tokens=c.jsonNumbers;report.json_structure_values=c.jsonStructures;report.raw_pairs=c.pairs;report.keys=c.keys;
 process.stdout.write(JSON.stringify(report,null,2)+'\n');
}
module.exports={context,BASE,A,O,R,D,AN,ON,FIELDS,W};
if(require.main===module)run();
