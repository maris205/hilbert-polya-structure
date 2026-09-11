'use strict';
// Documentary integrity only. Never imports, parses as code, or runs observe.py.
const fs=require('fs'),path=require('path'),crypto=require('crypto');
const root='/root/autodl-tmp/symbolic_dynamics';
const prep='docs/papers211_215_sequence/qa/private_checkpoint03_runtime_preparation01';
const accepted='docs/papers211_215_sequence/qa/private_checkpoint_executor_source_root03';
const hashes=new Map();let checks=0;
function need(v,m){checks++;if(!v)throw Error(m);}
function sha(b){return crypto.createHash('sha256').update(b).digest('hex');}
function key(rel){need(!path.isAbsolute(rel)&&!rel.split('/').includes('..'),'relative workspace path');const p=path.join(root,rel);const a=fs.lstatSync(p,{bigint:true});need(a.isFile()&&!a.isSymbolicLink(),'regular documentary input '+rel);const b=fs.readFileSync(p);const z=fs.lstatSync(p,{bigint:true});const fields=['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];const meta=x=>Object.fromEntries(fields.map(k=>[k,String(x[k])]));need(JSON.stringify(meta(a))===JSON.stringify(meta(z)),'stable document '+rel);const k={path:rel,bytes:b.length,sha256:sha(b),metadata:meta(a)};need(BigInt(b.length)===a.size,'whole length');if(hashes.has(rel))need(JSON.stringify(hashes.get(rel))===JSON.stringify(k),'unchanged repeat '+rel);else hashes.set(rel,k);return b;}
function manifest(dir,expected){const lines=key(dir+'/SHA256SUMS').toString().trimEnd().split('\n');need(lines.length===expected,'manifest count '+dir);const names=[];for(const line of lines){const m=/^([0-9a-f]{64})  (.+)$/.exec(line);need(!!m,'manifest grammar');need(!names.includes(m[2])&&m[2]!=='SHA256SUMS','unique nonself');names.push(m[2]);need(sha(key(dir+'/'+m[2]))===m[1],'manifest body '+m[2]);}const found=fs.readdirSync(path.join(root,dir));need(JSON.stringify(found.sort())===JSON.stringify([...names,'SHA256SUMS'].sort()),'complete directory '+dir);return names;}
manifest(prep,9);manifest(accepted,13);
const pins=key(prep+'/INPUT_PINS.sha256').toString().trimEnd().split('\n');need(pins.length===9,'nine input pins');
for(const line of pins){const m=/^([0-9a-f]{64})  (.+)$/.exec(line);need(!!m&&sha(key(m[2]))===m[1],'documentary pin');}
const proposed=JSON.parse(key(prep+'/PROSPECTIVE_REQUEST.json'));
need(proposed.enabled===false&&proposed.already_executed===false,'disabled author request');
need(proposed.source_sha256==='6e9acbfa3461b67f337d3eb013506b5840e7e11fc54670a50e992a39de6fe036','root independently selected source');
const source=key(prep+'/observe.py');need(source.length===9960&&sha(source)===proposed.source_sha256,'final complete source');
need(proposed.prospective_exec_command.cmd==='/usr/bin/python3 -I -S -B '+root+'/'+prep+'/observe.py','literal argv');
need(proposed.prospective_exec_command.workdir===root&&proposed.prospective_exec_command.login===false&&proposed.prospective_exec_command.shell==='/bin/bash','outer scope');
const records=JSON.parse(key(prep+'/ACTUAL_READS.json')).records;let sedMatches=0;const native=[];
for(const r of records){native.push({record_index:r.record_index,chunk_id:r.result.chunk_id,exit_code:r.result.exit_code,output_bytes:Buffer.byteLength(r.result.output),output_sha256:sha(Buffer.from(r.result.output)),scope:r.record_index===19?'PRE_REFINEMENT_NOT_FINAL':'ARCHIVED_DOCUMENTARY_READ'});const m=/^sed -n '([^']+)' (\S+)$/.exec(r.args.cmd);if(!m||r.record_index===19)continue;const selectors=m[1].split(';').map(x=>{const a=/^(\d+),(\d+)p$/.exec(x);need(!!a,'finite sed grammar');return[+a[1],+a[2]];});const body=key(m[2]).toString();const lines=body.match(/[^\n]*\n|[^\n]+$/g)||[];let out='';lines.forEach((line,i)=>selectors.forEach(([a,b])=>{if(i+1>=a&&i+1<=b)out+=line;}));need(r.result.exit_code===0&&out===r.result.output,'complete native slice '+r.record_index);sedMatches++;}
const own=path.relative(root,__filename);key(own);const inputs=[...hashes.keys()];for(const p of inputs)key(p);
process.stdout.write(JSON.stringify({schema:'checkpoint03-runtime-source-documentary-reception-v1',status:'DOCUMENT_KEYS_AND_SELECTED_NATIVE_SLICES_PASS_NOT_RUNTIME',checks,whole_documentary_keys:hashes.size,preparation_payloads:9,accepted_executor_receipt_payloads:13,input_pins:9,author_native_records:records.length,complete_native_sed_matches:sedMatches,author_pre_refinement_record:19,observer_invocations:0,git_ssh_or_host_role_invocations:0,native,keys:[...hashes.values()]},null,2)+'\n');

