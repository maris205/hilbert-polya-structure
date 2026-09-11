'use strict';
// Authored documentary JSON/string checker only. No reviewed code is imported/evaluated/parsed.
const fs=require('fs'),crypto=require('crypto'),assert=require('assert/strict'),path=require('path');
const own='docs/papers211_215_sequence/qa/p212_keyed_stdin_observation_preparation01/',root='/root/autodl-tmp/symbolic_dynamics',qa=root+'/docs/papers211_215_sequence/qa';
const names=['AUTHORIZATION.disabled.json','ARGV.disabled.json','REQUEST.disabled.json','BINDING.disabled.json','INPUTS_BEFORE.json','SOURCE_READS_NATIVE.json','PROPOSAL.md','HANDOFF.md','check.cjs'];
let checks=0;const eq=(a,b,m)=>{checks++;assert.deepEqual(a,b,m);};const ok=(a,m)=>{checks++;assert(a,m);};
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const canonical=v=>JSON.stringify(v,null,2).replace(/[\u007f-\uffff]/g,c=>'\\u'+c.charCodeAt(0).toString(16).padStart(4,'0'))+'\n';
function ownRead(n){ok(names.includes(n),'exact owned documentary name');const s=fs.lstatSync(own+n);ok(s.isFile()&&!s.isSymbolicLink(),'physical own file');return fs.readFileSync(own+n);}
const initial=JSON.parse(ownRead('INPUTS_BEFORE.json'));eq(initial.keys.length,13);
const allowed=new Map(initial.keys.map(k=>[k.path,k]));eq(allowed.size,13);
function read(p){ok(allowed.has(p),'explicit source/document allowlist');ok(!p.includes('empty.stdin'),'never inspect proposed input');const s=fs.lstatSync(p);ok(s.isFile()&&!s.isSymbolicLink(),'physical selected document');const b=fs.readFileSync(p);const k={path:p,bytes:b.length,lf_lines:b.reduce((n,c)=>n+(c===10),0),sha256:sha(b)};eq(k,allowed.get(p),'unchanged whole documentary pin '+p);return b;}
const inputKeys=initial.keys.map(k=>{read(k.path);return k;});
const fileKeys=names.map(n=>{const b=ownRead(n);return{name:n,bytes:b.length,sha256:sha(b)};});
const json=n=>{const b=ownRead(n),v=JSON.parse(b);eq(b,Buffer.from(canonical(v)),'exact canonical ASCII JSON '+n);return v;};
const a=json('AUTHORIZATION.disabled.json'),argv=json('ARGV.disabled.json'),r=json('REQUEST.disabled.json'),b=json('BINDING.disabled.json');
const src=qa+'/p212_keyed_stdin_source_delta01/observe.py',input=qa+'/p212_keyed_stdin_input01/empty.stdin';
const capture='/root/symbolic-dynamics-p212-keyed-stdin-observation-20260910-01';
const fixed={source_receipt:qa+'/p212_keyed_stdin_source_root01/RECEPTION.md',trust_receipt:qa+'/p212_trusted_product_boundary_root01/RECEPTION.md',frontier:qa+'/p212_keyed_stdin_source_delta01/FRONTIER.json'};
eq(Object.keys(a),['schema','enabled','status','provenance','source_receipt','trust_receipt','frontier']);
eq(a.schema,'p212-independent-preprobe-observer-authorization-v1');eq(a.enabled,false);eq(a.status,'HOLD_SOURCE_ONLY_NO_OBSERVER_OR_AUTHOR_PROBE');
const oldTemplate=JSON.parse(read('docs/papers211_215_sequence/qa/p212_keyed_stdin_source_delta01/AUTHORIZATION.disabled.json'));
const withoutPins=JSON.parse(JSON.stringify(a));for(const k of Object.keys(fixed))withoutPins[k].pin=null;
eq(withoutPins,oldTemplate,'only exact documentary control pins filled');
for(const [k,p]of Object.entries(fixed)){
 eq(a[k].path,p);const raw=read(p.slice(root.length+1));eq(a[k].pin,{bytes:raw.length,sha256:sha(raw)});eq(b.controls[k],a[k]);ok(raw.length<=1048576,'source control max');
}
const trust=JSON.parse(read('docs/papers211_215_sequence/qa/p212_trusted_product_boundary_root01/DECISION.json'));
eq(a.provenance,trust.provenance);eq(b.provenance,trust.provenance);eq(b.enabled,false);eq(r.enabled,false);
eq(b.ordinary_trust_binding.historical_prefix_relocation_automatic,false);eq(b.ordinary_trust_binding.selection,'PROPOSED_ONLY_REQUIRES_ROOT_EXACT_RELOCATED_PREFIX_ACCEPTANCE');
const env=trust.environment_after_env;
eq(Object.keys(env),['PATH','LANG','LC_ALL','TZ','SOURCE_DATE_EPOCH','FORCE_SOURCE_DATE','openin_any','openout_any']);
eq(b.ordinary_trust_binding.environment_after_env,env);
const prefix=['/usr/bin/env','-i',...Object.entries(env).map(([k,v])=>k+'='+v),'/usr/bin/python3.10','-I','-S','-B',src];
eq(argv,[...prefix,canonical(a)],'one complete canonical authorization argument');eq(b.ordinary_trust_binding.exact_native_prefix,prefix);
const arg=Buffer.from(argv.at(-1));eq(arg,ownRead('AUTHORIZATION.disabled.json'),'argument equals whole file bytes including final LF');ok(arg.length<=32768);ok(arg.every(c=>c<128));
const quote=s=>"'"+s.replace(/'/g,"'\"'\"'")+"'";
const command='umask 077\nset -C\nexec '+argv.map(quote).join(' ')+' < '+quote(input)+' > '+quote(capture+'/stdout.raw')+' 2> '+quote(capture+'/stderr.raw')+'\n';
eq(r.candidate_request,{cmd:command,workdir:root,shell:'/bin/bash',login:false,tty:false,yield_time_ms:1000,max_output_tokens:2000});
ok(!command.includes('/dev/null'),'no null device fallback');ok(!command.includes('mkdir'),'no capture preparation execution');ok(!command.includes('timeout'),'no new deadline/kill wrapper');
eq(b.stdin.path,input);eq(b.stdin.actual_current_key,null);eq(b.stdin.prepared_by_this_packet,false);eq(b.stdin.inherited_fd0_identity_attested,false);
eq(b.capture.directory,capture);eq(b.capture.current_existence_or_absence_observed,false);eq(b.capture.capacity_observed,false);eq(b.capture.prepared,false);
eq(b.scope.maximum_observer_invocations,1);eq(b.scope.internal_target_passes,2);eq(b.scope.automatic_retries,0);eq(b.scope.observer_spawned_children,0);eq(b.scope.author_probes,0);
const source=read(src.slice(root.length+1));eq(b.observer_source.pin,{bytes:source.length,sha256:sha(source)});eq(b.observer_source.lf_lines,436);
const text=source.toString('utf8');
for(const [name,n]of Object.entries({MAX_TARGETS:384,MAX_COMPONENTS:768,MAX_NATIVE_CALLS:60000,MAX_ALL_READ_BYTES:536870912,MAX_CAPTURE_BYTES:8388608,MAX_OUTPUT_BYTES:134217728,CHUNK:65536}))
 ok(text.includes(name+' = '+n+'\n'),'whole source finite constant '+name);
ok(text.includes("authorization['enabled'] is True")&&text.includes("'ROOT_BOUND_FINITE_OBSERVATION_ONLY'"),'disabled authorization not accepted');
ok(text.indexOf("authorization['enabled'] is True")<text.indexOf('        initialize_native()'),'grant check before native init');
ok(text.includes('for pass_number in (1, 2):'),'one invocation internal two passes');
ok(text.includes("need(data.mask & 0xFFF == 0xFFF"),'native mask preserved');
const frontier=JSON.parse(read(fixed.frontier.slice(root.length+1)));
eq(frontier.author_probe_execution_allowed,false);eq(frontier.targets.length,164);eq(frontier.allowed_components.length,204);
eq(frontier.targets.map(t=>t.path),[...new Set(frontier.targets.map(t=>t.path))].sort());
eq(frontier.allowed_components,[...new Set(frontier.allowed_components)].sort());
const inputRows=frontier.targets.filter(t=>t.path===input);eq(inputRows.length,1);eq(inputRows[0].mode,'file');eq(inputRows[0].max_bytes,0);eq(inputRows[0].capture_hex,true);
eq(frontier.targets.some(t=>t.path==='/dev/null'),false);eq(frontier.allowed_components.includes('/dev'),false);
const members=frontier.targets.filter(t=>t.mode==='membership');eq(members.length,5);eq(members.reduce((s,t)=>s+t.expected_names.length,0),292);eq(frontier.closure_gaps,initial.frontier.closure_gaps);
eq(b.scope.frontier,{path:fixed.frontier,pin:a.frontier.pin,target_count:164,component_count:204,membership_sets:5,membership_names:292,closure_gaps:8,expanded:false});
for(const t of frontier.targets)ok(frontier.allowed_components.includes(t.path),'target component is explicit');
const seals=[
 ['p212_keyed_stdin_source_delta01','f076522fc7e120c46be0c57b60168784c38c32339e07f65b74e0012694ca1ee8',55,['observe.py','FRONTIER.json','AUTHORIZATION.disabled.json']],
 ['p212_keyed_stdin_source_root01','0f65f815ca28d4153bc968b0d8dd041f3571287ebe639c942abce6064bb32380',16,['RECEPTION.md']]
];
for(const [dir,digest,count,selected]of seals){
 const base='docs/papers211_215_sequence/qa/'+dir+'/',raw=read(base+'SHA256SUMS'),s=raw.toString();
 eq(sha(raw),digest,'fixed frozen manifest');ok(s.endsWith('\n')&&!s.endsWith('\n\n'));
 const rows=s.slice(0,-1).split('\n').map(line=>{const m=/^([0-9a-f]{64})  ([^\r\n]+)$/.exec(line);ok(m,'bare-relative manifest');ok(m[2]!=='SHA256SUMS'&&!m[2].split('/').includes('..'),'nonself confined');return{sha256:m[1],name:m[2]};});
 eq(rows.length,count);eq(new Set(rows.map(x=>x.name)).size,count);
 for(const n of selected){const row=rows.find(x=>x.name===n);ok(row,'selected manifest entry');eq(sha(read(base+n)),row.sha256);}
}
const native=JSON.parse(ownRead('SOURCE_READS_NATIVE.json'));const pinCall=native.calls.find(c=>c.return.chunk_id==='5c5ed9');ok(pinCall,'actual initial key return');eq(Buffer.from(pinCall.return.output),ownRead('INPUTS_BEFORE.json'),'exact before raw output attachment');
for(const k of initial.keys)read(k.path);
process.stdout.write(canonical({kind:'DISABLED_FINITE_OBSERVER_PROPOSAL_DOCUMENTARY_CHECK_ONLY',checks,status:'PASS_SOURCE_DATA_ONLY_NO_OPERATION',input_keys:inputKeys,proposal_keys:fileKeys,authorization_argument_bytes:arg.length,argv_count:argv.length,source_sha256:sha(source),control_pins:Object.fromEntries(Object.entries(fixed).map(([k])=>[k,a[k]])),actual_input_or_capture_observed:false,reviewed_code_executed:false}));
