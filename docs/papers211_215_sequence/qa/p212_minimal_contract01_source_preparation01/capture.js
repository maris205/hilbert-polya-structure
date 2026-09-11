// SOURCE PROPOSAL ONLY. Reading this function calls no tool.
// A separately reviewed enabled-source delta is required: JSON cannot open it.
async function captureP212S0Call(tools, selection) {
  'use strict';
  const SOURCE_ENABLED = false;
  const need = (ok, message) => { if (!ok) throw new Error(message); };
  need(SOURCE_ENABLED, 'HOLD_SOURCE_ONLY: no product invocation');
  const ROOT = '/root/autodl-tmp/symbolic_dynamics';
  const QA = ROOT + '/docs/papers211_215_sequence/qa';
  const CWD = QA + '/p212_build_dependency_query01/query_cwd';
  const INPUT = QA + '/p212_keyed_stdin_input01/empty.stdin';
  const RAW = QA + '/p212_minimal_contract01_raw01';
  const BINDING = QA + '/p212_minimal_contract01_binding01/BINDING.json';
  const ENV8 = {PATH:'/usr/bin:/bin',LANG:'C.UTF-8',LC_ALL:'C.UTF-8',TZ:'UTC',
    SOURCE_DATE_EPOCH:'1788825600',FORCE_SOURCE_DATE:'1',openin_any:'p',openout_any:'p'};
  const PROVENANCE = {schema:'p212-s0-product-direct-provenance-v1',
    ordinary_product_and_root_key_tools_trusted:true,unscanned_ancestors_trusted:true,
    inherited_bash_env_startup_attested:false,product_startup_attested:false,
    claim:'finite_received_ten_field_file_keys_and_completed_direct_product_calls',
    native_pid_observation:false,descendant_census:false,escaped_writer_exclusion:false};
  const keys = (x, k, label) => {
    need(x !== null && typeof x === 'object' && !Array.isArray(x), label);
    need(JSON.stringify(Object.keys(x).sort()) === JSON.stringify([...k].sort()), label + ' exact keys');
  };
  const equal = (a,b,label) => need(JSON.stringify(a) === JSON.stringify(b), label);
  const ref = (x,label) => {
    keys(x,['path','pin'],label); keys(x.pin,['bytes','sha256'],label + ' pin');
    need(typeof x.path === 'string' && x.path.startsWith(QA + '/') &&
      !/[\x00-\x20\x7f]/.test(x.path) && !x.path.split('/').slice(1).some(v=>v===''||v==='.'||v==='..'),label + ' path');
    need(Number.isSafeInteger(x.pin.bytes) && x.pin.bytes > 0 &&
      /^[0-9a-f]{64}$/.test(x.pin.sha256),label + ' whole pin');
  };
  keys(selection,['schema','enabled','status','call','prepared_request','external_binding',
    'preflight_receipt','one_call_authority','previous_help_receipt','provenance'],'selection');
  need(selection.schema === 'p212-s0-direct-call-selection-v1' && selection.enabled === true &&
    selection.status === 'ROOT_BOUND_ONE_DIRECT_S0_CALL','fresh received one-call selection');
  need(selection.call === 'help' || selection.call === 'version','only two S0 roles');
  equal(selection.provenance,PROVENANCE,'exact narrower provenance');
  ref(selection.external_binding,'external nonself selected-binding key');
  need(selection.external_binding.path === BINDING,'distinct fixed binding role');
  ref(selection.preflight_receipt,'actual immediate preflight reception');
  ref(selection.one_call_authority,'separately recorded one-call authority');
  const receiptPaths = [BINDING,selection.preflight_receipt.path,selection.one_call_authority.path];
  if (selection.call === 'help') need(selection.previous_help_receipt === null,'help has no future receipt');
  else { ref(selection.previous_help_receipt,'independent prior complete help reception');
    receiptPaths.push(selection.previous_help_receipt.path); }
  need(new Set(receiptPaths).size === receiptPaths.length,'distinct nonrecursive roles');
  const callDir = RAW + '/' + selection.call + '01';
  const quote = s => "'" + s.replaceAll("'", "'\\''") + "'";
  const argv = ['/usr/bin/env','-i',...Object.entries(ENV8).map(([k,v])=>k+'='+v),
    '/usr/bin/kpsewhich','--'+selection.call];
  // Only shell builtins precede two successive exec replacements. No pipe,
  // background task, Node/Python child, shell expansion of argument data or
  // fd attestation is claimed. Root preowns this fresh 0700 call directory.
  const request = {
    cmd:'umask 077 || exit 78\nset -o noclobber || exit 78\nexec < '+quote(INPUT)+
      ' > '+quote(callDir+'/stdout.raw')+' 2> '+quote(callDir+'/stderr.raw')+
      ' || exit 78\nexec '+argv.map(quote).join(' '),
    workdir:CWD,shell:'/bin/bash',login:false,tty:false,yield_time_ms:1000,max_output_tokens:4000
  };
  equal(selection.prepared_request,request,'entire prepared request, not a subset');
  const frames = [], started = Date.now();
  let currentSession = null, productCompleted = false, failure = null, actualExit = null;
  const record = (kind,value) => frames.push({sequence:frames.length,kind,unix_ms:Date.now(),value});
  // Store the actual returned objects without a lossy JSON round-trip.
  // The product outer transport originals still require separate root attachment.
  record('EXEC_COMMAND_REQUEST',request);
  try {
    let result = await tools.exec_command(request);
    let returns = 0;
    while (true) {
      record(returns === 0 ? 'EXEC_COMMAND_RETURN' : 'WRITE_STDIN_RETURN',result);
      returns++;
      need(result !== null && typeof result === 'object' && !Array.isArray(result),'actual product object');
      const permitted = ['chunk_id','exit_code','original_token_count','output','session_id','wall_time_seconds'];
      need(Object.keys(result).every(k=>permitted.includes(k)),'unrecognized product field: preserve and HOLD');
      const sessionPresent = Object.hasOwn(result,'session_id');
      const exitPresent = Object.hasOwn(result,'exit_code');
      if (sessionPresent && Number.isSafeInteger(result.session_id) && result.session_id > 0) {
        if (currentSession !== null) need(currentSession === result.session_id,'same actually returned session');
        currentSession = result.session_id;
      }
      need(sessionPresent !== exitPresent,'exactly one ongoing session or final exit');
      need(typeof result.output === 'string','complete product control output');
      need(result.output === '','all nonempty, omitted or unknown product control output requires disposition');
      need(typeof result.wall_time_seconds === 'number' && Number.isFinite(result.wall_time_seconds) &&
        result.wall_time_seconds >= 0,'actual elapsed-time field');
      if (Object.hasOwn(result,'chunk_id')) need(typeof result.chunk_id === 'string' && result.chunk_id.length > 0,'actual chunk identifier');
      if (Object.hasOwn(result,'original_token_count')) need(Number.isSafeInteger(result.original_token_count) &&
        result.original_token_count >= 0,'actual output-count field');
      if (exitPresent) {
        need(Number.isInteger(result.exit_code),'actual final exit');
        actualExit = result.exit_code; productCompleted = true; currentSession = null;
        need(actualExit === 0,'nonzero direct product exit; no tool success inferred');
        break;
      }
      need(Number.isSafeInteger(result.session_id) && result.session_id > 0,'valid actual continuation handle');
      need(returns <= 120 && Date.now()-started < 120000,'bounded collection expired; retain handle, no signal/retry');
      const poll = {session_id:currentSession,chars:'',yield_time_ms:1000,max_output_tokens:4000};
      record('WRITE_STDIN_REQUEST',poll);
      result = await tools.write_stdin(poll);
    }
  } catch (error) {
    failure = {name:String(error?.name ?? 'Error'),message:String(error?.message ?? error)};
    record('NORMALIZED_JS_CATCH_NOT_ORIGINAL_EXCEPTION',failure);
  }
  return {schema:'p212-s0-direct-product-record-v1',call:selection.call,
    status:failure ? 'UNKNOWN_OR_FAILED_PRESERVED' : 'PRODUCT_COMPLETED_RAW_RECEPTION_PENDING',
    selection,request,argv,environment:ENV8,frames,product_completed:productCompleted,
    actual_product_exit:actualExit,unsettled_session_id:currentSession,failure,
    stdout_path:callDir+'/stdout.raw',stderr_path:callDir+'/stderr.raw',
    stdout_final_pin:null,stderr_final_pin:null,native_pid:null,native_pid_basis:'NOT_EXPOSED_BY_PRODUCT',
    provenance:PROVENANCE,collection_budget_ms:120000,budget_is_hard_interrupt:false,
    automatic_retry:false,automatic_signal:false,automatic_cleanup:false,next_call_permission:false,
    option_acceptance:false,lookup_body_build_science_permission:false,manifest:null,
    enclosing_functions_originals:'ROOT_MUST_ATTACH_ACTUAL_REQUEST_YIELD_WAIT_FINAL_VALUES'};
}
