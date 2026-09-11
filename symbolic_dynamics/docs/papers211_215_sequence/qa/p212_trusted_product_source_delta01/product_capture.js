// SOURCE ONLY. No tool is called by loading/reading this file.
// Future root may paste the exact received function into functions.exec and
// call it ONCE with a newly received literal descriptor. It never seals files.
// Ordinary product/observer/Bash/env bootstrap is an explicit assumption,
// not independently attested startup. The finite downstream key stays separate.
async function captureContract(tools, authorization) {
  'use strict';
  const ROOT='/root/autodl-tmp/symbolic_dynamics';
  const QA=ROOT+'/docs/papers211_215_sequence/qa';
  const SOURCE=QA+'/p212_trusted_product_source_delta01/outer_contract.py';
  const BINDING=QA+'/p212_build_dependency_outer_binding01/contract01/BINDING.json';
  const CACHE=QA+'/p212_build_dependency_outer_binding01/contract01/never_created_cache';
  const environment={PATH:'/usr/bin:/bin',LANG:'C.UTF-8',LC_ALL:'C.UTF-8',TZ:'UTC',
    SOURCE_DATE_EPOCH:'1788825600',FORCE_SOURCE_DATE:'1',openin_any:'p',openout_any:'p'};
  const PROVENANCE={schema:'p212-trusted-product-boundary-v1',
   assumption:'ordinary_product_observer_bash_env_bootstrap',product_startup_attested:false,
   claim:'finite_received_keys_and_discrete_downstream_observations'};
  const need=(ok,label)=>{if(!ok)throw new Error(label);};
  const canonical=x=>JSON.stringify(x,null,2)+'\n';
  const same=(a,b)=>canonical(a)===canonical(b);
  const freezeValue=x=>JSON.parse(JSON.stringify(x));
  need(same(Object.keys(authorization).sort(),
    ['enabled','external_binding_descriptor','provenance','schema','status']),'exact one-use root authorization keys');
  need(authorization.schema==='p212-trusted-product-contract-capture-authorization-v1',
    'distinct trusted-product collector interface');
  need(authorization.enabled===true&&authorization.status==='ROOT_BOUND_TRUSTED_PRODUCT_CONTRACT_ONLY',
    'HOLD: actual source-delta/trust/runtime/binding receptions must precede this call');
  need(same(authorization.provenance,PROVENANCE),'fixed conditional model; no startup attestation');
  const d=authorization.external_binding_descriptor;
  need(d&&d.path===BINDING&&d.role==='configuration'&&d.kind==='file'&&d.resolved===BINDING
    &&d.comparison==='stable'&&d.symlink_target===null&&d.members===null,'physical external nonself binding');
  need(d.content&&Number.isSafeInteger(d.content.bytes)&&d.content.bytes>0
    &&/^[0-9a-f]{64}$/.test(d.content.sha256),'no placeholder binding pin');
  const descriptorRaw=canonical(d);
  const argv=['/usr/bin/env','-i',...Object.entries(environment).map(([k,v])=>k+'='+v),
    '/usr/bin/python3.10','-I','-S','-B','-X','pycache_prefix='+CACHE,SOURCE,BINDING,descriptorRaw];
  const quote=s=>"'"+s.replaceAll("'","'\\''")+"'";
  const request={cmd:'exec '+argv.map(quote).join(' '),workdir:ROOT,shell:'/bin/bash',
    login:false,tty:false,yield_time_ms:1000,max_output_tokens:4000};
  const frames=[],started=Date.now();
  let activeSession=null,closed=false,failure=null;
  const record=(kind,value)=>frames.push({sequence:frames.length,kind,unix_ms:Date.now(),
    value:freezeValue(value)});
  record('EXACT_EXEC_COMMAND_REQUEST',request);
  try {
    let result=await tools.exec_command(request);
    record('ACTUAL_EXEC_COMMAND_RETURN',result);
    while(true) {
      need(result&&typeof result==='object'&&!Array.isArray(result),'actual tool object required');
      const hasSession=Number.isSafeInteger(result.session_id)&&result.session_id>0;
      const hasExit=Number.isInteger(result.exit_code);
      if(hasSession) {
        if(activeSession!==null)need(result.session_id===activeSession,'same actual owned native session');
        activeSession=result.session_id;
      } else if(hasExit) {
        closed=true;activeSession=null;
      }
      need(typeof result.output==='string','actual complete tool output string required');
      need(!/^Warning: truncated output/m.test(result.output)
        &&!/^.*\[?\.\.\. \d+ tokens truncated \.\.\.\]?/m.test(result.output),
        'product reported an omitted output: preserve and HOLD');
      need(hasSession!==hasExit,'exactly one ongoing session or final actual exit');
      if(hasExit) {
        need(result.exit_code===0,'nonzero actual product exit requires separate disposition');
        break;
      }
      need(Date.now()-started<660000,'collection deadline: retain live handle; no termination/retry');
      const poll={session_id:activeSession,chars:'',yield_time_ms:1000,max_output_tokens:4000};
      record('EXACT_WRITE_STDIN_REQUEST',poll);
      result=await tools.write_stdin(poll);
      record('ACTUAL_WRITE_STDIN_RETURN',result);
    }
  } catch(error) {
    failure={name:String(error?.name??'Error'),message:String(error?.message??error)};
    record('ACTUAL_JS_CATCH',failure);
  }
  // These are actual tools.exec_command/write_stdin values, not a claim to
  // know the enclosing functions.exec / functions.wait transport envelopes.
  // Root must separately retain those request/yield/cell/poll/final originals.
  return {status:failure?'UNKNOWN_OR_FAILED_PRODUCT_CAPTURE':'NATIVE_PRODUCT_CLOSED_ROOT_RECEPTION_PENDING',
    provenance:PROVENANCE,frames,actual_native_session_closed:closed,unsettled_native_session_id:activeSession,
    failure,external_binding_descriptor:d,prepared_argv:argv,automatic_retry:false,
    automatic_intervention:false,outer_manifest:null,lookup_or_body_permission:false,
    enclosing_functions_envelopes:'ROOT_MUST_ATTACH_ACTUAL_ORIGINAL_VALUES',
    attachment:'Root may attach these exact returned values with apply_patch after exclusive destination check; no execution replay.'};
}
