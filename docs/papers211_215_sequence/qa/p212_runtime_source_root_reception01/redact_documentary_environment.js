'use strict';
// One-time security repair of root-owned, newly generated documentary JSON.
// Exact originals survive in a mode-0700 LOCAL_ONLY directory, never Git inputs.
// This is a bulk mechanical redaction, not revision of submitted/scientific evidence.
const fs=require('fs'),path=require('path'),crypto=require('crypto');
const ROOT='/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa';
const PRIVATE='/root/p211-p212-docenv-private.qSe4kr';
const targets=[];
for(let i=0;i<5;i++)for(const suffix of ['ATTEMPT','NATIVE'])targets.push(['p212_runtime_source_root_reception01',`COMMAND_${String(i).padStart(2,'0')}_${suffix}.json`]);
targets.push(['p212_runtime_source_root_reception01','PREPARATION_RESULT.json']);
for(let i=0;i<2;i++)for(const suffix of ['ATTEMPT','NATIVE'])targets.push(['orientation_root_reception01',`COMMAND_${i}_${suffix}.json`]);
targets.push(['orientation_root_reception01','RESULT.json']);
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const modes=fs.statSync(PRIVATE);if((modes.mode&0o777)!==0o700)throw Error('private mode');
if(fs.readdirSync(PRIVATE).length!==0)throw Error('private target must start empty');
const mapping=[];
function scrub(value){
  if(!value||typeof value!=='object')return 0;
  let count=0;
  for(const k of Object.keys(value)){
    if(k==='environment'){
      const old=value[k];
      value[k]={recording:'SECURITY_REDACTED_AMBIENT_DOCUMENTARY_ENVIRONMENT_NOT_A_RUNTIME_REUSE_KEY',
        key_names:Object.keys(old).sort(),
        safe_locale_path_fields:Object.fromEntries(['PATH','LANG','LC_ALL','LC_CTYPE','TZ'].filter(n=>n in old).map(n=>[n,old[n]])),
        exact_original:'Restricted LOCAL_ONLY original; see SECURITY_REDACTION_RECEIPT.json. No credential value is retained in this workspace JSON.'};
      count++;
    }else count+=scrub(value[k]);
  }
  return count;
}
// Copy and byte-verify every target first. Do not partially redact before preservation.
for(const[dir,name]of targets){const source=path.join(ROOT,dir,name),target=path.join(PRIVATE,dir+'__'+name),raw=fs.readFileSync(source);
  fs.copyFileSync(source,target,fs.constants.COPYFILE_EXCL);fs.chmodSync(target,0o600);
  if(!fs.readFileSync(target).equals(raw))throw Error('private raw copy');
  mapping.push({workspace:source,restricted_original:target,original_bytes:raw.length,original_sha256:sha(raw)});
}
for(const m of mapping){const raw=fs.readFileSync(m.workspace);if(sha(raw)!==m.original_sha256)throw Error('changed input');
  const j=JSON.parse(raw),count=scrub(j);if(count<1)throw Error('expected environment object');
  const replacement=Buffer.from(JSON.stringify(j,null,2)+'\n');
  fs.writeFileSync(m.workspace,replacement);m.redacted_environment_objects=count;m.redacted_bytes=replacement.length;m.redacted_sha256=sha(replacement);
  if(!fs.readFileSync(m.workspace).equals(replacement))throw Error('replacement raw check');
}
const receipt={status:'SECURITY_REDACTED_WITH_EXACT_RESTRICTED_ORIGINALS',scope:'Exactly 16 root-owned documentary JSON artifacts; no submitted source, science, failed source, raw command stream, preparation seal or old artifact changed.',
  git_scope:'Restricted originals are LOCAL_ONLY, outside workspace, excluded from any Git or external transfer.',
  semantic_scope:'All non-environment values preserved exactly; previous native stdout result digest identifies the restricted original, not redacted workspace JSON. Raw native stdout/stderr files unchanged.',
  mapping};
fs.writeFileSync(path.join(ROOT,'p212_runtime_source_root_reception01','SECURITY_REDACTION_RECEIPT.json'),JSON.stringify(receipt,null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify({status:receipt.status,files:mapping.length,environment_objects:mapping.reduce((n,m)=>n+m.redacted_environment_objects,0),no_credential_value_emitted:true}));
