// Independent fixed-workspace source/DATA validation. Never imports proposed code.
const fs=require('node:fs'),crypto=require('node:crypto'),assert=require('node:assert/strict');
const Q='docs/papers211_215_sequence/qa/',P=Q+'p212_kpathsea_elf_data_preparation01/';
const F='dev ino mode nlink uid gid rdev size mtimeNs ctimeNs'.split(' ');
let checks=0;const records=[],raw=new Map();
const ok=(x,s)=>{checks++;assert(x,s)},eq=(a,b)=>{checks++;assert.deepEqual(a,b)},pin=b=>({bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')});
const stat=s=>Object.fromEntries(F.map(k=>[k,String(s[k])]));
function read(path){
 if(raw.has(path))return raw.get(path);
 const before=fs.lstatSync(path,{bigint:true});ok(before.isFile(),'regular workspace file');
 const fd=fs.openSync(path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);let b,fdBefore,fdAfter;
 try{fdBefore=stat(fs.fstatSync(fd,{bigint:true}));eq(fdBefore,stat(before));b=fs.readFileSync(fd);fdAfter=stat(fs.fstatSync(fd,{bigint:true}));eq(fdAfter,fdBefore);}finally{fs.closeSync(fd)}
 const after=stat(fs.lstatSync(path,{bigint:true}));eq(after,fdBefore);eq(BigInt(b.length),before.size);
 records.push({path,begin:stat(before),fd_before:fdBefore,fd_after:fdAfter,end:after,content:pin(b)});raw.set(path,b);return b;
}
const request=JSON.parse(read(P+'REQUEST.proposed.json'));
eq(pin(raw.get(P+'REQUEST.proposed.json')).sha256,'12cf66ae6c2b0147ac0472cc5374ab8879ff972de48829fd049f626c960287d5');
const seal=read(P+'SHA256SUMS').toString('utf8').trimEnd().split('\n');eq(seal.length,5);
for(const line of seal){const m=/^([a-f0-9]{64})  ([A-Za-z0-9_.]+)$/.exec(line);ok(m,'strict basename');eq(pin(read(P+m[2])).sha256,m[1]);}
eq(fs.readdirSync(P).sort(),['HANDOFF.md','REQUEST.proposed.json','RUN.proposed.mjs.txt','SHA256SUMS','decoder_append.proposed.mjs.txt','load_kpathsea.proposed.mjs.txt'].sort());
eq(request.source_inputs.length,4);eq(request.fixed_data_inputs.length,5);
for(const x of [...request.source_inputs,...request.fixed_data_inputs]){ok(x.path.startsWith(Q)&&!x.path.includes('..'),'fixed workspace only');eq(pin(read(x.path)),{bytes:x.bytes,sha256:x.sha256});}
const [adapter,base,append,entry]=request.source_inputs.map(x=>raw.get(x.path).toString('utf8'));
eq(pin(Buffer.concat([raw.get(request.source_inputs[1].path),raw.get(request.source_inputs[2].path)])),{bytes:19846,sha256:'048e6e8457aa9e9de9e2619f68438be2fa12b3942e3796cd0750b79cc69ee406'});
eq(request.composition.bytes,19846);eq(request.composition.sha256,'048e6e8457aa9e9de9e2619f68438be2fa12b3942e3796cd0750b79cc69ee406');
eq(pin(raw.get(request.source_inputs[1].path)).sha256,'24122a0fa7da0e38390bbdb8ba240279c166f1b3116a3c87f9a136c9791b1068');
for(const x of request.fixed_data_inputs){ok(adapter.includes(x.sha256),'adapter exact external DATA pin');ok(adapter.includes(String(x.bytes)),'adapter size');}
for(const x of request.source_inputs.slice(0,3)){ok(entry.includes(x.sha256),'entry source pin');ok(entry.includes(String(x.bytes)),'entry source size');}
eq((append.match(/elf\(v,out,state\)/g)||[]).length,1);ok(!/\b(?:cache|decodeCapturedBodies)\s*\(/.test(append),'no old decode call');
ok(!/\bimport\b|\b(?:fs|process)\s*\./.test(append),'pure append');ok(append.includes('initCount:18'),'cumulative init');ok(append.includes('named.size<96'),'name ceiling');ok(append.includes('state.initCount<64'),'init ceiling');ok(append.includes('images.size<=32'),'image ceiling');ok(append.includes('result.prior_holds_retained=prior.holds'),'old holds retained');
const replay=JSON.parse(raw.get(request.fixed_data_inputs[1].path));eq(replay.chunk_id,'2c1bc2');eq(replay.exit_code,0);ok(!Object.hasOwn(replay,'session_id'),'no running replay');
const accepted=JSON.parse(replay.output),captureRaw=raw.get(request.fixed_data_inputs[2].path),capture=JSON.parse(captureRaw);
eq(accepted.status,'ACCEPT_THREE_REGULAR_CANDIDATE_BODY_DATA_ONLY');eq(accepted.findings.open,0);eq(accepted.failure,null);eq(accepted.stdout,pin(captureRaw));eq(Buffer.from(JSON.stringify(capture)+'\n'),captureRaw);
const current=records.find(x=>x.path===request.fixed_data_inputs[2].path),old=accepted.current_documents.filter(x=>x.path.endsWith('/'+current.path));eq(old.length,1);for(const k of ['begin','fd_before','fd_after','end'])eq(old[0][k],current.begin);
eq(capture.reader_result.rows.length,3);const row=capture.reader_result.rows[2],observed=accepted.observations[2],r=row.regular;
eq(row.id,'KPATHSEA_LEAF');eq(row.path,request.body_selection.lexical_origin_data_only);eq(row.role,'needed_regular_candidate');eq(row.complete,true);eq(row.error,null);eq(row.link,null);eq(r.eof,true);eq(r.close_succeeded,true);eq(r.close_error,null);eq(r.bytes_read,97064);ok(/^(?:[0-9a-f]{2})*$/.test(r.raw_hex),'hex');eq(r.raw_hex.length,194128);
eq(pin(Buffer.from(r.raw_hex,'hex')),{bytes:97064,sha256:'8077fa6889e0a1bedd742adb649182f4167b5a79c57630c1f5dc5a89e8301fe6'});eq(observed.body,r.content);eq(observed.reads,r.reads);for(const [k,v]of [['lstat_before',row.lstat_before],['fstat_before',r.fstat_before],['fstat_after',r.fstat_after],['lstat_after',row.lstat_after]])eq(v,observed[k]);
const native=JSON.parse(raw.get(request.fixed_data_inputs[4].path));eq(native.result.chunk_id,'11ea24');eq(native.result.exit_code,0);ok(!Object.hasOwn(native.result,'session_id'),'old decode complete');
const priorRaw=Buffer.from(native.result.output),prior=JSON.parse(priorRaw).result;eq(pin(priorRaw),{bytes:150872,sha256:'0906b783c684c8c101ebca7c614789625b02e601892eaa9db602b5f89c51bc15'});eq(prior.images.length,6);eq(prior.named_states.length,15);eq(prior.init_fini_entries,18);eq(prior.holds.length,32);eq(prior.cache.complete_same_name_scan,true);ok(prior.images.every(x=>x.structurally_decoded),'prior accepted table');
const oldImages=new Set(prior.images.map(x=>x.body_pin.sha256+':'+x.body_pin.bytes));for(const row of capture.reader_result.rows.slice(0,2))ok(oldImages.has(row.regular.content.sha256+':'+row.regular.content.bytes),'other accepted terminal body already counted');
ok(prior.named_states.some(x=>x.literal==='/usr/lib/x86_64-linux-gnu/libtinfo.so.6.3'),'existing tinfo name');
eq(request.bounds,{combined_known_image_nodes:32,combined_known_named_states:96,combined_init_fini_entries:64,new_decoded_bodies:1,new_cache_decodes:0,new_host_paths_opened:0});eq(request.execution_authorized,false);eq(request.installed_closure,false);eq(request.operation_permission,false);eq(request.external_status,'HOLD_EXTERNAL');
for(const [k,v]of Object.entries(request))if(k.startsWith('actual_'))eq(v,null);
for(const x of records){eq(stat(fs.lstatSync(x.path,{bigint:true})),x.begin);eq(pin(fs.readFileSync(x.path)),x.content);}
process.stdout.write(JSON.stringify({status:'ACCEPT_SOURCE_ONLY_FIXED_INPUT_VALIDATION',checks,keys:records,proposed_modules_executed:false,new_elf_or_cache_decoding:false,host_paths_opened:false,operation_permission:false,installed_closure:false,external_status:'HOLD_EXTERNAL'})+'\n');
