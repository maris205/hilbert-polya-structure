// SOURCE PROPOSAL ONLY. Data consumer: no filesystem, process or tool access.
// No CLI, automatic call, import of producer source or option-semantics verdict.
import {createHash} from 'node:crypto';

export function receiveP212S0Call(packetBytes) {
  const SOURCE_ENABLED = false;
  const need = (v,m) => { if (!v) throw new Error(m); };
  need(SOURCE_ENABLED,'HOLD_SOURCE_ONLY: no submitted consumer execution');
  const QA = '/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa';
  const BINDING = QA+'/p212_minimal_contract01_binding01/BINDING.json';
  const RAW = QA+'/p212_minimal_contract01_raw01';
  const CWD = QA+'/p212_build_dependency_query01/query_cwd';
  const INPUT = QA+'/p212_keyed_stdin_input01/empty.stdin';
  const FIELDS = ['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
  const ENV8 = {PATH:'/usr/bin:/bin',LANG:'C.UTF-8',LC_ALL:'C.UTF-8',TZ:'UTC',
    SOURCE_DATE_EPOCH:'1788825600',FORCE_SOURCE_DATE:'1',openin_any:'p',openout_any:'p'};
  const PROVENANCE = {schema:'p212-s0-product-direct-provenance-v1',
    ordinary_product_and_root_key_tools_trusted:true,unscanned_ancestors_trusted:true,
    inherited_bash_env_startup_attested:false,product_startup_attested:false,
    claim:'finite_received_ten_field_file_keys_and_completed_direct_product_calls',
    native_pid_observation:false,descendant_census:false,escaped_writer_exclusion:false};
  const same = (a,b,m) => need(JSON.stringify(a) === JSON.stringify(b),m);
  const keys = (v,k,m) => {
    need(v !== null && typeof v === 'object' && !Array.isArray(v),m);
    same(Object.keys(v).sort(),[...k].sort(),m+' exact keys');
  };
  const pin = raw => ({bytes:raw.length,sha256:createHash('sha256').update(raw).digest('hex')});
  const hex = (s,m) => { need(typeof s === 'string' && /^(?:[0-9a-f]{2})*$/.test(s),m);return Buffer.from(s,'hex'); };
  const json = (raw,m) => {
    need(Buffer.isBuffer(raw),m+' raw bytes');
    const text = raw.toString('utf8'), value = JSON.parse(text);
    need(Buffer.from(text,'utf8').equals(raw) && Buffer.from(JSON.stringify(value,null,2)+'\n').equals(raw),
      m+' entire canonical UTF-8 JSON; duplicate/alternative hidden members refused');
    return value;
  };
  const ref = (r,m) => {
    keys(r,['path','pin'],m);keys(r.pin,['bytes','sha256'],m+' pin');
    need(typeof r.path === 'string' && r.path.startsWith(QA+'/') && /^\/[!-~]+$/.test(r.path) &&
      !r.path.split('/').slice(1).some(v=>v===''||v==='.'||v==='..'),m+' literal path');
    need(Number.isSafeInteger(r.pin.bytes) && r.pin.bytes > 0 && /^[0-9a-f]{64}$/.test(r.pin.sha256),m+' complete pin');
  };
  const metadata = (s,m) => {
    keys(s,FIELDS,m);
    for (const [k,v] of Object.entries(s)) need(typeof v === 'string' && /^-?(0|[1-9][0-9]*)$/.test(v) &&
      v !== '-0' && (['mtimeNs','ctimeNs'].includes(k) || BigInt(v) >= 0n),m+' exact integer');
  };
  const ROW_KEYS = ['id','path','role','state','lstat_before','fd','fstat_before','fstat_after',
    'lstat_after','bytes_read','eof','content','raw_hex','close_succeeded','error','close_error'];
  const fileRow = (row,m,allowAbsent=false) => {
    keys(row,ROW_KEYS,m);
    if (row.state === 'absent') {
      need(allowAbsent,m+' optional absence only');same(row.error,{operation:'lstat',code:'ENOENT'},m+' actual ENOENT role');
      for (const key of ['lstat_before','fd','fstat_before','fstat_after','lstat_after','content','close_succeeded','close_error'])
        need(row[key] === null,m+' no fabricated absent metadata');
      need(row.bytes_read === 0 && row.eof === false && row.raw_hex === '',m+' no absent read');
      return null;
    }
    need(row.state === 'present' && row.error === null && row.close_error === null,m+' complete successful file');
    for (const name of ['lstat_before','fstat_before','fstat_after','lstat_after']) {
      metadata(row[name],m+' '+name);same(row[name],row.lstat_before,m+' ten fields agree');
    }
    need((BigInt(row.lstat_before.mode)&0o170000n) === 0o100000n,m+' regular nonalias leaf');
    need(Number.isSafeInteger(row.fd) && row.fd >= 0 && row.eof === true && row.close_succeeded === true,m+' actual same-fd EOF/close record');
    const bytes = hex(row.raw_hex,m+' complete actual bytes');
    need(Number.isSafeInteger(row.bytes_read) && row.bytes_read === bytes.length && BigInt(bytes.length) === BigInt(row.lstat_before.size),m+' full EOF size');
    same(row.content,pin(bytes),m+' every byte pin');return bytes;
  };
  const packet = json(packetBytes,'packet');
  keys(packet,['schema','call','selection_hex','binding_hex','binding_before','binding_after',
    'inputs_before_hex','inputs_after_hex','directories_before_hex','directories_after_hex','product_hex',
    'raw_keys_hex','binding_receipts','selection_receipts','direct_settlement_receipt','actual_functions_envelopes'],'packet');
  need(packet.schema === 'p212-s0-call-reception-input-v1' && ['help','version'].includes(packet.call),'one exact S0 call');
  const call = packet.call, selectionRaw = hex(packet.selection_hex,'selection bytes');
  const selection = json(selectionRaw,'selection'), bindingRaw = hex(packet.binding_hex,'binding bytes');
  const binding = json(bindingRaw,'binding'), productRaw = hex(packet.product_hex,'product bytes');
  const product = json(productRaw,'product');
  keys(selection,['schema','enabled','status','call','prepared_request','external_binding',
    'preflight_receipt','one_call_authority','previous_help_receipt','provenance'],'selection');
  need(selection.schema === 'p212-s0-direct-call-selection-v1' && selection.enabled === true &&
    selection.status === 'ROOT_BOUND_ONE_DIRECT_S0_CALL' && selection.call === call,'received exact selection');
  same(selection.provenance,PROVENANCE,'selected narrower provenance');
  ref(selection.external_binding,'nonself binding reference');
  same(selection.external_binding,{path:BINDING,pin:pin(bindingRaw)},'whole external selected-binding pin');
  for (const [name,row] of [['before',packet.binding_before],['after',packet.binding_after]]) {
    need(row.path === BINDING && row.role === 'binding','selected binding '+name+' independent file role');
    need(fileRow(row,'binding '+name).equals(bindingRaw),'selected binding '+name+' complete raw bytes');
  }
  same(packet.binding_before.lstat_before,packet.binding_after.lstat_before,'DQD-O1 new ten-field before/after identity');
  keys(binding,['schema','enabled','status','scope','provenance','sources','receipts','environment','tool_argv','cwd',
    'stdin','input_permissions','directory_identity','owned_uid','raw_root','prepared_requests','option_acceptance','later_authority'],'binding');
  need(binding.schema === 'p212-s0-direct-binding-v1' && binding.enabled === true &&
    binding.status === 'ROOT_BOUND_S0_DIRECT_TWO_CALLS_SEPARATELY_GATED' && binding.scope === 'S0_CONTRACT01_ONLY','distinct binding; reject old schemas');
  same(binding.provenance,PROVENANCE,'binding provenance');same(binding.environment,ENV8,'entire ENV8');
  same(binding.tool_argv,[['/usr/bin/kpsewhich','--help'],['/usr/bin/kpsewhich','--version']],'only tool vectors');
  need(binding.cwd === CWD && binding.raw_root === RAW && binding.option_acceptance === null,'fixed cwd/raw and no own options receipt');
  same(binding.later_authority,{lookup:false,bodies:false,build:false,science:false,review:false,external:'HOLD_EXTERNAL'},'all successors remain closed');
  same(binding.stdin,{path:INPUT,content:pin(Buffer.alloc(0)),policy:'TRUSTED_FRESH_SHELL_OPEN_OF_INDEPENDENTLY_KEYED_EMPTY_REGULAR_LEAF',
    fd0_same_handle_attested:false,ancestor_chain_attested:false,initial_offset_basis:'SOURCE_DERIVED_FRESH_OPEN'},'explicit changed EOF policy');
  keys(binding.sources,['capture','file_keys','receiver'],'all new exact source roles');
  keys(binding.receipts,['source','policy','tool_closure'],'separate actual root semantic decisions');
  for (const [role,r] of Object.entries({...binding.sources,...binding.receipts})) ref(r,role+' reference');
  const receiveReferences = (rows,expected,m) => {
    need(Array.isArray(rows),m+' rows');same(rows.map(r=>r.role),Object.keys(expected),m+' exact ordered roles');
    const paths = [];
    for (const row of rows) { keys(row,['role','reference','raw_hex'],m+' row');ref(row.reference,m+' reference');
      same(row.reference,expected[row.role],m+' bound reference');same(pin(hex(row.raw_hex,m+' whole receipt')),row.reference.pin,m+' whole receipt bytes');paths.push(row.reference.path); }
    need(new Set(paths).size === paths.length,m+' distinct receipts');
  };
  receiveReferences(packet.binding_receipts,binding.receipts,'binding decisions');
  const selectionRefs = {preflight:selection.preflight_receipt,authority:selection.one_call_authority};
  if (call === 'help') need(selection.previous_help_receipt === null,'no future help receipt');
  else selectionRefs.previous_help = selection.previous_help_receipt;
  receiveReferences(packet.selection_receipts,selectionRefs,'one-call decisions');
  const selectedPaths=[BINDING,...Object.values(selectionRefs).map(r=>r.path)];
  need(new Set(selectedPaths).size===selectedPaths.length,'binding/preflight/grant/help roles remain distinct');
  const sourceDecisionPaths=[...Object.values(binding.sources),...Object.values(binding.receipts)].map(r=>r.path);
  need(new Set(sourceDecisionPaths).size===sourceDecisionPaths.length&&!sourceDecisionPaths.includes(BINDING),'distinct source/decision roles, no binding self reference');
  need(Array.isArray(binding.input_permissions) && binding.input_permissions.length > 0 && binding.input_permissions.length <= 96,'finite received input set');
  const inputs = new Map(), inputIds = new Set();
  for (const entry of binding.input_permissions) {
    keys(entry,['id','path','role','optional','max_bytes','capture_hex','expected'],'exact file permission');
    need(typeof entry.id === 'string' && /^[A-Z][A-Z0-9_]{0,63}$/.test(entry.id) && typeof entry.path === 'string' &&
      /^\/[!-~]+$/.test(entry.path) && !entry.path.includes('\\') && !entry.path.split('/').slice(1).some(v=>v===''||v==='.'||v==='..'),'finite exact file spelling');
    need(!inputs.has(entry.path) && !inputIds.has(entry.id) && entry.path !== BINDING && !entry.path.startsWith(RAW+'/') &&
      typeof entry.optional === 'boolean' && entry.capture_hex === true,'no duplicate/self/raw body hiding');inputIds.add(entry.id);
    need(['source','receipt','executable','loader','configuration','stdin'].includes(entry.role),'S0 input roles only');
    need(Number.isSafeInteger(entry.max_bytes) && entry.max_bytes >= 0 && entry.max_bytes <= 134217728,'finite whole-file bound');
    keys(entry.expected,['state','metadata','content'],'independently received expected key');
    if (entry.expected.state === 'present') { metadata(entry.expected.metadata,'expected metadata');keys(entry.expected.content,['bytes','sha256'],'expected whole pin');
      need(Number.isSafeInteger(entry.expected.content.bytes) && entry.expected.content.bytes >= 0 &&
        entry.expected.content.bytes <= entry.max_bytes && /^[0-9a-f]{64}$/.test(entry.expected.content.sha256) &&
        BigInt(entry.expected.content.bytes) === BigInt(entry.expected.metadata.size) &&
        (BigInt(entry.expected.metadata.mode)&0o170000n) === 0o100000n,'expected consistent regular whole content'); }
    else need(entry.optional && entry.expected.state === 'absent' && entry.expected.metadata === null && entry.expected.content === null,'explicit optional absence');
    inputs.set(entry.path,entry);
  }
  for (const path of ['/bin/bash','/usr/bin/env','/usr/bin/kpsewhich',INPUT])
    need(inputs.has(path) && inputs.get(path).expected.state === 'present' && !inputs.get(path).optional,'mandatory direct input '+path);
  for (const path of ['/bin/bash','/usr/bin/env','/usr/bin/kpsewhich']) need(inputs.get(path).role==='executable','exact executable purpose');
  need(inputs.get(INPUT).role === 'stdin' && inputs.get(INPUT).max_bytes === 0,'strict selected stdin permission');
  same(inputs.get(INPUT).expected.content,pin(Buffer.alloc(0)),'actual prebound zero-byte policy');
  for (const r of [...Object.values(binding.sources),...Object.values(binding.receipts)])
    need(inputs.has(r.path) && inputs.get(r.path).expected.state === 'present' &&
      JSON.stringify(inputs.get(r.path).expected.content) === JSON.stringify(r.pin),'every source/receipt whole key is a received input');
  for (const r of Object.values(binding.sources)) need(inputs.get(r.path).role==='source','complete source purpose');
  for (const r of Object.values(binding.receipts)) need(inputs.get(r.path).role==='receipt','complete receipt purpose');
  const receiveInputRecord = (rawHex,purpose) => {
    const record = json(hex(rawHex,purpose+' key bytes'),purpose+' key');
    keys(record,['schema','status','request','rows','accepted_bytes','failure','actual_ancestor_scan','native_statx_attestation',
      'process_or_startup_observation','source_acceptance','operation_permission'],purpose+' record');
    need(record.schema === 'p212-s0-ten-field-files-v1' && record.status === 'OBSERVED_ROOT_RECEPTION_PENDING' && record.failure === null,'complete input record');
    keys(record.request,['schema','enabled','status','purpose','entries','total_byte_limit','permission_receipt','settlement_receipt'],'input request');
    need(record.request.schema === 'p212-s0-ten-field-file-request-v1' && record.request.enabled === true &&
      record.request.status === 'ROOT_BOUND_FINITE_FILES_ONLY' && record.request.purpose === purpose &&
      record.request.settlement_receipt === null,'input key request exact phase');
    ref(record.request.permission_receipt,'key permission receipt');
    same(record.request.entries,binding.input_permissions,'entire received input permissions');
    need(Array.isArray(record.rows) && record.rows.length === inputs.size,'complete input rows');
    let total = 0;
    record.rows.forEach((row,i)=> {
      const e = binding.input_permissions[i];need(row.id === e.id && row.path === e.path && row.role === e.role,'exact ordered input row');
      const bytes = fileRow(row,'input '+e.id,e.optional);same(row.state,e.expected.state,'expected state');
      if (bytes !== null) { same(row.lstat_before,e.expected.metadata,'entire expected ten fields');same(row.content,e.expected.content,'expected full bytes');total+=bytes.length; }
    });
    need(record.accepted_bytes === total && Number.isSafeInteger(record.request.total_byte_limit) &&
      total <= record.request.total_byte_limit && record.request.total_byte_limit <= 268435456,'complete accepted byte budget');
    for (const k of ['actual_ancestor_scan','native_statx_attestation','process_or_startup_observation','source_acceptance','operation_permission'])
      need(record[k] === false,'no stronger key claim');
    return record;
  };
  const before = receiveInputRecord(packet.inputs_before_hex,'pre_call');
  const after = receiveInputRecord(packet.inputs_after_hex,'post_call');
  same(before.rows.map(r=>[r.path,r.state,r.lstat_before,r.content]),after.rows.map(r=>[r.path,r.state,r.lstat_before,r.content]),'unchanged relevant input key around THIS call');
  const paths = [CWD,RAW,RAW+'/help01',RAW+'/version01'];
  need(typeof binding.owned_uid === 'string' && /^(0|[1-9][0-9]*)$/.test(binding.owned_uid),'actual selected owner uid');
  need(Array.isArray(binding.directory_identity) && binding.directory_identity.length === 4,'four preowned directory identities');
  const identity = s => ['dev','ino','mode','uid','gid','rdev'].map(k=>s[k]);
  const directoryRecord = (rawHex,phase) => {
    const r = json(hex(rawHex,'directory bytes'),'directory');
    keys(r,['schema','status','request','rows','failure','unscanned_ancestors_trusted','directory_handle_identity_attested','operation_permission'],'directory record');
    need(r.schema === 'p212-s0-directory-points-v1' && r.status === 'OBSERVED_ROOT_RECEPTION_PENDING' && r.failure === null &&
      r.unscanned_ancestors_trusted === true && r.directory_handle_identity_attested === false && r.operation_permission === false,'narrow complete directory record');
    keys(r.request,['schema','enabled','status','paths','permission_receipt'],'directory request');
    need(r.request.schema === 'p212-s0-directory-request-v1' && r.request.enabled === true &&
      r.request.status === 'ROOT_BOUND_FOUR_DIRECTORY_POINTS_ONLY','directory permission');ref(r.request.permission_receipt,'directory permission reference');
    same(r.request.paths,paths,'only four exact directories');need(Array.isArray(r.rows) && r.rows.length === 4,'all four directory rows');
    r.rows.forEach((row,i)=> {
      keys(row,['path','before','after','names','eof','close_succeeded','error','close_error'],'directory row');
      need(row.path === paths[i] && row.eof === true && row.close_succeeded === true && row.error === null && row.close_error === null,'actual complete owned directory row');
      metadata(row.before,'directory before');metadata(row.after,'directory after');same(identity(row.before),identity(row.after),'same point directory identity');
      const d = binding.directory_identity[i];keys(d,['path','metadata'],'bound directory identity');metadata(d.metadata,'bound directory');
      need(d.path === row.path && row.before.uid === binding.owned_uid && (BigInt(row.before.mode)&0o177777n) === 0o40700n,'actual root-owned 0700 directory');
      same(identity(row.before),identity(d.metadata),'received directory identity');
      const filledHelp = call === 'version' || phase === 'after', filledVersion = call === 'version' && phase === 'after';
      const names = i === 0 ? [] : i === 1 ? ['help01','version01'] :
        (i === 2 ? filledHelp : filledVersion) ? ['stderr.raw','stdout.raw'] : [];
      same(row.names,names,'exact planned directory delta only');
    });return r;
  };
  directoryRecord(packet.directories_before_hex,'before');directoryRecord(packet.directories_after_hex,'after');
  const quote = s => "'" + s.replaceAll("'","'\\''") + "'";
  const expectedRequests = ['help','version'].map(c=> {
    const argv = ['/usr/bin/env','-i',...Object.entries(ENV8).map(([k,v])=>k+'='+v),'/usr/bin/kpsewhich','--'+c];
    return {cmd:'umask 077 || exit 78\nset -o noclobber || exit 78\nexec < '+quote(INPUT)+' > '+quote(RAW+'/'+c+'01/stdout.raw')+
      ' 2> '+quote(RAW+'/'+c+'01/stderr.raw')+' || exit 78\nexec '+argv.map(quote).join(' '),workdir:CWD,shell:'/bin/bash',login:false,tty:false,yield_time_ms:1000,max_output_tokens:4000};
  });
  same(binding.prepared_requests,expectedRequests,'both whole fixed requests');const expectedRequest = expectedRequests[call === 'help' ? 0 : 1];
  same(selection.prepared_request,expectedRequest,'selected whole request');
  keys(product,['schema','call','status','selection','request','argv','environment','frames','product_completed','actual_product_exit',
    'unsettled_session_id','failure','stdout_path','stderr_path','stdout_final_pin','stderr_final_pin','native_pid','native_pid_basis',
    'provenance','collection_budget_ms','budget_is_hard_interrupt','automatic_retry','automatic_signal','automatic_cleanup',
    'next_call_permission','option_acceptance','lookup_body_build_science_permission','manifest','enclosing_functions_originals'],'entire product record');
  need(product.schema === 'p212-s0-direct-product-record-v1' && product.call === call && product.status === 'PRODUCT_COMPLETED_RAW_RECEPTION_PENDING' &&
    product.product_completed === true && product.actual_product_exit === 0 && product.unsettled_session_id === null && product.failure === null,'actual successful product completion record');
  same(product.selection,selection,'complete actual selection');same(product.request,expectedRequest,'entire actual request');same(product.environment,ENV8,'declared child ENV8');
  same(product.argv,['/usr/bin/env','-i',...Object.entries(ENV8).map(([k,v])=>k+'='+v),'/usr/bin/kpsewhich','--'+call],'literal actual command vector');
  same(product.provenance,PROVENANCE,'no stronger product provenance');
  need(product.stdout_path === RAW+'/'+call+'01/stdout.raw' && product.stderr_path === RAW+'/'+call+'01/stderr.raw' && product.native_pid_basis === 'NOT_EXPOSED_BY_PRODUCT' &&
    product.collection_budget_ms === 120000 && product.enclosing_functions_originals === 'ROOT_MUST_ATTACH_ACTUAL_REQUEST_YIELD_WAIT_FINAL_VALUES','raw roles and capture limits');
  for (const k of ['stdout_final_pin','stderr_final_pin','native_pid','manifest']) need(product[k] === null,'producer does not invent a seal/PID');
  for (const k of ['budget_is_hard_interrupt','automatic_retry','automatic_signal','automatic_cleanup','next_call_permission','option_acceptance','lookup_body_build_science_permission'])
    need(product[k] === false,'all ungranted duties remain false');
  need(Array.isArray(product.frames) && product.frames.length >= 2 && product.frames.length <= 242 && product.frames.length%2 === 0,'bounded complete request/return pairs');
  let session = null, finalSeen = false, priorTime = -1;
  for (let i=0;i<product.frames.length;i+=2) {
    const q=product.frames[i],r=product.frames[i+1];
    for (const [frame,index] of [[q,i],[r,i+1]]) {keys(frame,['sequence','kind','unix_ms','value'],'actual frame');
      need(frame.sequence === index && Number.isSafeInteger(frame.unix_ms) && frame.unix_ms >= priorTime,'ordered actual frame/time');priorTime=frame.unix_ms;}
    need(q.kind === (i===0?'EXEC_COMMAND_REQUEST':'WRITE_STDIN_REQUEST') && r.kind === (i===0?'EXEC_COMMAND_RETURN':'WRITE_STDIN_RETURN'),'actual frame kinds');
    same(q.value,i===0?expectedRequest:{session_id:session,chars:'',yield_time_ms:1000,max_output_tokens:4000},'exact actual tool request');
    const v=r.value;need(v && typeof v==='object' && !Array.isArray(v),'actual result object');
    need(Object.keys(v).every(k=>['chunk_id','exit_code','original_token_count','output','session_id','wall_time_seconds'].includes(k)),'unknown product field remains HOLD');
    need(v.output === '' && typeof v.wall_time_seconds === 'number' && Number.isFinite(v.wall_time_seconds) && v.wall_time_seconds >= 0,'complete empty product control stream');
    if (Object.hasOwn(v,'chunk_id')) need(typeof v.chunk_id==='string' && v.chunk_id.length>0,'real chunk field');
    if (Object.hasOwn(v,'original_token_count')) need(Number.isSafeInteger(v.original_token_count) && v.original_token_count>=0,'actual count');
    const hasSession=Object.hasOwn(v,'session_id'),hasExit=Object.hasOwn(v,'exit_code');need(hasSession!==hasExit,'one actual session or final exit');
    if (hasSession) {need(Number.isSafeInteger(v.session_id)&&v.session_id>0&&(session===null||session===v.session_id),'same actual continuation');session=v.session_id;}
    else {need(v.exit_code===0&&i+2===product.frames.length,'final actual zero exit only at end');session=null;finalSeen=true;}
  }
  need(finalSeen && session === null,'no inferred unresolved lifetime');
  keys(packet.direct_settlement_receipt,['reference','raw_hex'],'direct settlement receipt');ref(packet.direct_settlement_receipt.reference,'direct settlement reference');
  same(pin(hex(packet.direct_settlement_receipt.raw_hex,'whole prior settlement receipt')),packet.direct_settlement_receipt.reference.pin,'received actual prior settlement bytes');
  const raw = json(hex(packet.raw_keys_hex,'raw-key bytes'),'raw-key record');
  keys(raw,['schema','status','request','rows','accepted_bytes','failure','actual_ancestor_scan','native_statx_attestation','process_or_startup_observation','source_acceptance','operation_permission'],'raw-key record');
  need(raw.schema==='p212-s0-ten-field-files-v1'&&raw.status==='OBSERVED_ROOT_RECEPTION_PENDING'&&raw.failure===null,'complete raw file key');
  keys(raw.request,['schema','enabled','status','purpose','entries','total_byte_limit','permission_receipt','settlement_receipt'],'raw request');
  need(raw.request.schema==='p212-s0-ten-field-file-request-v1'&&raw.request.enabled===true&&raw.request.status==='ROOT_BOUND_FINITE_FILES_ONLY'&&raw.request.purpose==='closed_raw','raw only after direct settlement');
  ref(raw.request.permission_receipt,'raw permission');same(raw.request.settlement_receipt,packet.direct_settlement_receipt.reference,'settlement before raw keying');
  need(Array.isArray(raw.rows)&&raw.rows.length===2&&Array.isArray(raw.request.entries)&&raw.request.entries.length===2,'both separate whole raw streams');
  const streams = raw.rows.map((row,i)=> {
    const name=i===0?'stdout':'stderr',entry=raw.request.entries[i];
    same(entry,{id:name.toUpperCase(),path:RAW+'/'+call+'01/'+name+'.raw',role:'raw',optional:false,max_bytes:16777216,capture_hex:true,expected:null},'exact raw permission');
    need(row.id===entry.id&&row.path===entry.path&&row.role==='raw','separate raw row role');
    const bytes=fileRow(row,name+' complete raw');need(bytes.length<=16777216,'per-stream bound');return bytes;
  });
  need(streams[0].length>0&&streams[1].length===0,'nonempty raw help/version and truly empty separate stderr');
  need(raw.accepted_bytes===streams[0].length&&raw.request.total_byte_limit===33554432,'exact raw total budget');
  for (const k of ['actual_ancestor_scan','native_statx_attestation','process_or_startup_observation','source_acceptance','operation_permission']) need(raw[k]===false,'no stronger raw-key claim');
  need(Array.isArray(packet.actual_functions_envelopes)&&packet.actual_functions_envelopes.length>0,'original enclosing transport attachments required');
  for (const row of packet.actual_functions_envelopes) {keys(row,['kind','request_hex','return_hex'],'original enclosing envelope');
    need(['functions.exec','functions.wait'].includes(row.kind),'actual enclosing envelope role');
    // functions.exec has a FREEFORM JavaScript request, not necessarily JSON.
    // Preserve exact original representations; root must authenticate and
    // check completeness/binding against originals, not a made-up wrapper.
    need(hex(row.request_hex,'whole enclosing request').length>0&&hex(row.return_hex,'whole enclosing return').length>0,'nonempty whole original envelope representations');}
  return {schema:'p212-s0-call-data-check-v1',status:'DATA_CONSISTENT_ROOT_ORIGINAL_AND_SEMANTIC_RECEPTION_PENDING',call,
    packet_pin:pin(packetBytes),selection_pin:pin(selectionRaw),binding_pin:pin(bindingRaw),product_record_pin:pin(productRaw),
    stdout:pin(streams[0]),stderr:pin(streams[1]),input_count:inputs.size,provenance:PROVENANCE,
    native_original_authenticity_automatically_proved:false,receipt_semantics_automatically_accepted:false,
    installed_options_accepted:false,next_call_permission:false,lookup_body_build_science_permission:false,manifest:null};
}
