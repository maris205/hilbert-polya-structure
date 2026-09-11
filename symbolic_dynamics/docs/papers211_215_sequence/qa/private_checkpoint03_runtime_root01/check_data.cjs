'use strict';
// Root's ordinary-trusted documentary receiver. No observer/executor imports.
// Only two exact existing private originals and directory metadata are read.
// Never emit configuration bodies, argument strings or ENV5 values.
const fs=require('node:fs'), crypto=require('node:crypto'), path=require('node:path');
const W='/root/autodl-tmp/symbolic_dynamics';
const Q='docs/papers211_215_sequence/qa/';
const A=Q+'private_checkpoint03_runtime_policy_audit01/';
const R=Q+'private_checkpoint03_runtime_root01/';
const D='/root/symbolic-dynamics-checkpoint03-runtime-tc9tt3hi';
let checks=0; const keys=new Map();
function need(x,label){checks++;if(!x)throw new Error('PUBLIC_CHECK_FAILED: '+label);}
function hash(b,alg='sha256'){return crypto.createHash(alg).update(b).digest('hex');}
function meta(s){return Object.fromEntries(['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'].map(k=>[k,String(s[k])]));}
function eq(a,b){return JSON.stringify(a)===JSON.stringify(b);}
function sorted(x){if(Array.isArray(x))return x.map(sorted);if(x&&typeof x==='object')return Object.fromEntries(Object.keys(x).sort().map(k=>[k,sorted(x[k])]));return x;}
function same(a,b){return eq(sorted(a),sorted(b));}
function readPublic(p){need(!path.isAbsolute(p)&&!p.split('/').includes('..'),'workspace scope');const f=path.join(W,p);const s=fs.lstatSync(f,{bigint:true});need(s.isFile(),'workspace regular file');const b=fs.readFileSync(f),e=fs.lstatSync(f,{bigint:true});need(same(meta(s),meta(e))&&BigInt(b.length)===s.size,'workspace endpoint stable');const k={path:p,bytes:b.length,sha256:hash(b),metadata:meta(s)};if(keys.has(p))need(same(keys.get(p),k),'workspace repeated whole key');else keys.set(p,k);return b;}
function obj(p){return JSON.parse(readPublic(p).toString('utf8'));}
function seal(dir,expected){const b=readPublic(dir+'SHA256SUMS');need(hash(b)===expected,'fixed seal hash');const lines=b.toString('utf8').trimEnd().split('\n'), names=[];for(const line of lines){const m=/^([0-9a-f]{64})  ([A-Za-z0-9_.-]+)$/.exec(line);need(!!m,'seal syntax');need(m[2]!=='SHA256SUMS'&&!names.includes(m[2]),'nonself unique seal');names.push(m[2]);need(hash(readPublic(dir+m[2]))===m[1],'payload hash');}need(same(fs.readdirSync(path.join(W,dir)).sort(),[...names,'SHA256SUMS'].sort()),'complete directory membership');return names;}
function pins(p){const lines=readPublic(p).toString('utf8').trimEnd().split('\n');for(const line of lines){const m=/^([0-9a-f]{64})  (.+)$/.exec(line);need(!!m,'input pin syntax');need(hash(readPublic(m[2]))===m[1],'input pin current');}return lines.length;}
const auditNames=seal(A,'d7f6576ce1fcc3ea7572cecdfe6ad46c00f7cad5849d771ab0371249e14020e4');
need(auditNames.length===11,'eleven audit payloads');
const pinCount=pins(A+'INPUT_PINS.sha256');need(pinCount===16,'sixteen documentary input pins');
const sourceNames=seal(Q+'private_checkpoint03_runtime_source_root01/','d4249c91405bc799773849728df74338a5ab4298a15c9f19ca8bf7304c8a91ae');
const prepNames=seal(Q+'private_checkpoint03_runtime_preparation01/','7353b8e3804c52d0c2618040ae2ac2f07dc5f0061a4cb95e378e4d21bf6e2165');
need(sourceNames.length===9&&prepNames.length===9,'source/preparation payload counts');
need(pins(Q+'private_checkpoint03_runtime_preparation01/INPUT_PINS.sha256')===9,'nine preparation pins');
const actual=obj(R+'ACTUAL_OBSERVER_NATIVE.json'),grant=obj(R+'ROOT_SINGLE_OBSERVER_GRANT.json');
need(same(grant,actual.grant)&&same(grant.exact_outer_request,actual.request),'exact grant binding');
need(actual.returns.length===1&&actual.returns[0].tool==='exec_command','sole command return');
const native=actual.returns[0].result;
need(native.exit_code===0&&!('session_id'in native)&&native.chunk_id==='48584f','single final zero return');
need(native.output.endsWith('\n'),'full native newline');
const nativeLines=native.output.trimEnd().split('\n').map(x=>JSON.parse(x));need(nativeLines.length===2,'two native lines');
need(nativeLines[0].private_evidence_directory===D&&nativeLines[0].status==='OBSERVATION_STARTED_NOT_ACCEPTED','start line');
const md0=fs.lstatSync(D,{bigint:true});need(md0.isDirectory()&&md0.mode===0o40700n&&md0.uid===0n&&md0.gid===0n,'private directory');
const privateKeys=[];
function readPrivate(name,expectedSize,expectedHash){need(['SUMMARY.json','PRIVATE_OBSERVATION.json'].includes(name),'exact private filename');const p=D+'/'+name,s=fs.lstatSync(p,{bigint:true});need(s.isFile()&&s.mode===0o100600n&&s.uid===0n&&s.gid===0n&&s.nlink===1n,'private file type owner mode');const b=fs.readFileSync(p),e=fs.lstatSync(p,{bigint:true});need(same(meta(s),meta(e)),'private file endpoints');need(b.length===expectedSize&&hash(b)===expectedHash,'private original whole bytes');privateKeys.push({name,bytes:b.length,sha256:hash(b),metadata:meta(s)});return b;}
const sb=readPrivate('SUMMARY.json',490,'8e95b1e14cef2094259f579f94a7318130aedf89ded757d9b4548c27ae7aa934');
const ob=readPrivate('PRIVATE_OBSERVATION.json',17546,'a220ee82528592f9538a50d1c1d0ec32f2899842387b33493d720db3ed8e6432');
const s=JSON.parse(sb),o=JSON.parse(ob);
need(same(s,nativeLines[1]),'summary equals actual native object');
need(s.private_observation_pin.bytes===ob.length&&s.private_observation_pin.sha256===hash(ob),'summary full original key');
need(o.schema===s.schema&&o.status===s.status&&o.status==='OBSERVED_ROOT_RECEIPT_AND_SSH_POLICY_PENDING','schema and original status');
need(o.config_evaluation_or_includes_followed===false&&o.git_ssh_network_or_agent_calls===0&&o.checkpoint_executor_invoked===false&&o.observer_executed===true&&o.continuous_launch_attestation===false,'declared observed scope');
need(s.ssh_policy_accepted===false&&s.four_operation_phases==='HOLD','summary not operation');
const rt=o.runtime;
need(same(rt.argv,[W+'/'+Q+'private_checkpoint03_runtime_preparation01/observe.py'])&&rt.cwd===W&&rt.executable==='/usr/bin/python3','downstream argv cwd spelling');
need(rt.isolated===1&&rt.no_site===1&&rt.dont_write_bytecode===true&&rt.optimize===0&&rt.uid===0&&rt.euid===0&&rt.pythonpath_absent===true,'downstream runtime fields');
const ev=o.inherited_environment_private,envNames=['HOME','USER','LOGNAME','SSH_AUTH_SOCK','SSH_AGENT_PID'];
need(Object.keys(ev).every(k=>envNames.includes(k)&&typeof ev[k]==='string'),'private five-role membership/types');
need(Object.keys(ev).length===1,'one present inherited role');
const old=obj(Q+'private_checkpoint03_scope_preparation01/READONLY_ROLE_RESULT.json');
const ctr=obj(Q+'private_checkpoint_preparation02/controls_preview34/SOURCE_ROLES.json');
const fresh=o.protected_roles;
need(Object.keys(fresh).length===15&&s.protected_role_count===15,'fifteen roles');
function oldkey(v){if(v.present===false)return {present:false};return Object.fromEntries(['bytes','sha256','mode','oid'].map(k=>[k,v[k]]));}
const common=Object.keys(fresh).filter(k=>k in old.protected_before).sort();need(common.length===13,'thirteen common roles');
const comparisons=common.map(k=>{need(same(oldkey(fresh[k]),old.protected_before[k])&&same(oldkey(fresh[k]),old.protected_after[k]),'common role both old endpoints');return {role:k,both_archived_byte_keys_equal:true};});
const bare='/root/symbolic-dynamics-private-sync-accepted-20260907.git/refs/heads/main';
need(!(bare in fresh)&&same(Object.keys(o.separate_bare_main),[bare]),'separate bare main membership');
need(same(oldkey(o.separate_bare_main[bare]),old.protected_before[bare])&&same(oldkey(o.separate_bare_main[bare]),old.protected_after[bare]),'bare main both old endpoints');
need(same(oldkey(fresh['/usr/bin/python3.10']),oldkey(ctr.interpreter)),'resolved interpreter historical key');
const alias=fresh['/usr/bin/python3'];
need(alias.symlink_target==='python3.10'&&alias.resolved==='/usr/bin/python3.10'&&(BigInt(alias.lexical_metadata.st_mode)&0o170000n)===0o120000n&&same(alias.resolved_key,oldkey(fresh['/usr/bin/python3.10'])),'lexical alias distinct regular file');
need(!('/usr/bin/node'in fresh),'old Node excluded from new observed scope');
const hosts=o.hostkey_file_keys_no_contents;
need(Object.keys(hosts).length===4&&Object.values(hosts).filter(x=>x.present).length===1&&s.hostkey_role_count===4,'four hostkey snapshots one present');
const frontier=o.dropin_name_frontier_private;
need(frontier.present===true&&Array.isArray(frontier.entries)&&frontier.entries.length===0&&frontier.member_contents_read===false,'empty received frontier');
const configs=o.base_configs_private;
need(same(Object.keys(configs).sort(),['/etc/ssh/ssh_config','/root/.ssh/config'])&&s.base_config_count===2,'two exact base role names');
const scans=[];let configBodies=[];
for(const [file,role] of [['/etc/ssh/ssh_config','system_base'],['/root/.ssh/config','user_base']]){
 const c=configs[file];need(c.key.present===true&&typeof c.whole_body_hex_private==='string'&&/^(?:[0-9a-f]{2})*$/.test(c.whole_body_hex_private),'complete even private hex');
 const b=Buffer.from(c.whole_body_hex_private,'hex');configBodies.push([b,c.whole_body_hex_private]);
 need(b.length===c.key.bytes&&hash(b)===c.key.sha256&&hash(Buffer.concat([Buffer.from('blob '+b.length+'\0'),b]),'sha1')===c.key.oid,'decoded complete config key');
 need([...b].every(x=>x<128),'whole config ASCII');
 const lines=b.toString('ascii').split('\n'),active=[];let comments=0;
 lines.forEach((line,i)=>{const t=line.trim();if(!t)return;if(t.startsWith('#')){comments++;return;}
  need(!/["'\\\0=#]/.test(t),'simple active text grammar');
  const tokens=t.split(/\s+/),directive=tokens.shift().toLowerCase();
  need(['include','host','sendenv','hashknownhosts','gssapiauthentication','stricthostkeychecking'].includes(directive),'known active directive');
  const row={line:i+1,directive,argument_count:tokens.length,parse_uncertainty:false};
  if(['hashknownhosts','gssapiauthentication','stricthostkeychecking'].includes(directive)){need(tokens.length===1&&['yes','no'].includes(tokens[0]),'safe enum grammar');row.safe_enum=tokens[0];}
  if(directive==='include')need(tokens.length===1&&tokens[0]==='/etc/ssh/ssh_config.d/*.conf','exact existing shallow Include selector');
  if(directive==='host')need(tokens.length===1&&tokens[0]==='*','all-target Host');
  active.push(row);
 });
 scans.push({role,whole_hex_bytes:b.length,declared_present:true,total_text_lines:lines.length,comment_lines:comments,active_line_count:active.length,active_directives:active});
}
const assessment=obj(A+'POLICY_ASSESSMENT.json');
need(same(scans,assessment.observed_base_scan),'complete redacted scan matches independent report');
need(scans[0].active_directives[0].directive==='include'&&scans[0].active_directives[1].directive==='host'&&scans[1].whole_hex_bytes===0,'empty user base and global Include before Host');
need(assessment.status==='ORIGINAL_DATA_CHECKED_EFFECTIVE_SSH_NO_WRITE_POLICY_HOLD'&&assessment.all_four_phases==='HOLD'&&assessment.installed_defaults_proved===false,'effective policy remains hold');
need(assessment.policy_rows.length===18,'all eighteen policy rows');
const roleReport=obj(A+'ROLE_COMPARISON.json');need(roleReport.common_protected_count===13&&roleReport.all_common_byte_keys_match===true&&roleReport.python_resolved_matches_controls34_interpreter===true,'independent bounded role census');
const safe=obj(A+'SAFE_NATIVE_CHECKS.json');
for(const group of ['initial','source_checks','closing'])for(const rec of safe[group])need(rec.result.exit_code===0&&typeof rec.result.output==='string'&&!('session_id'in rec.result),'archived safe native final records');
need(safe.initial[0].result.output===safe.closing[0].result.output&&safe.initial[1].result.output===safe.closing[1].result.output,'independent private metadata/hash endpoints');
for(const [b,h] of configBodies)if(b.length){for(const name of auditNames){const pub=readPublic(A+name);need(!pub.includes(b)&&!pub.includes(Buffer.from(h)),'audit excludes full private config/body hex');}}
for(const name of auditNames)need(!readPublic(A+name).toString('utf8').includes(JSON.stringify(ev)),'audit excludes exact raw ENV5 map serialization');
const md1=fs.lstatSync(D,{bigint:true});need(same(meta(md0),meta(md1)),'private directory stable endpoint');
for(const k of privateKeys){const p=D+'/'+k.name;need(same(meta(fs.lstatSync(p,{bigint:true})),k.metadata)&&hash(fs.readFileSync(p))===k.sha256,'private original final whole key');}
for(const k of [...keys.values()])readPublic(k.path);
process.stdout.write(JSON.stringify({status:'ROOT_ORIGINAL_DATA_ACCEPTED_EFFECTIVE_SSH_POLICY_HOLD',checks,
workspace_complete_key_count:keys.size,workspace_keys:[...keys.values()],private_directory_metadata:meta(md0),
private_original_keys:privateKeys,sole_native_chunk:native.chunk_id,common_comparisons:comparisons,separate_bare_main_equal:true,
resolved_interpreter_equal:true,lexical_alias_separate:true,redacted_base_scan:scans,selected_leaf_count:0,
environment_present_count:1,environment_absent_count:4,private_values_exported:false,hostkey_contents_exported:false,
scope:'Existing originals as data; no new host role/config/leaf/socket reads, no observer replay, executor, SSH, Git or network. Ordinary trusted tooling; endpoint observations only; historical equality is four fields or absence, not historical metadata; no installed defaults, authentication, remote state or continuous startup claim.',
four_operation_phases:'HOLD'},null,2)+'\n');

