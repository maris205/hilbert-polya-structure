'use strict';
// SOURCE ONLY. Explicit runtime-only external authority; never loads the
// driver/preload and never calls child_process.spawn or any native tool.
// Ordinary trusted-product bootstrap is assumed, not independently attested;
// separate source, finite bootstrap-key and trust-boundary receipts are required.
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const cp=require('node:child_process'),assert=require('node:assert/strict'),Module=require('node:module');
const ROOT='/root/autodl-tmp/symbolic_dynamics',QA=ROOT+'/docs/papers211_215_sequence/qa';
const SELF=QA+'/p212_keyed_stdin_source_delta01/node_runtime_probe.js';
const ENV8={PATH:'/usr/bin:/bin',LANG:'C.UTF-8',LC_ALL:'C.UTF-8',TZ:'UTC',
 SOURCE_DATE_EPOCH:'1788825600',FORCE_SOURCE_DATE:'1',openin_any:'p',openout_any:'p'};
const PROVENANCE={schema:'p212-trusted-product-boundary-v1',
 assumption:'ordinary_product_observer_bash_env_bootstrap',product_startup_attested:false,
 claim:'finite_received_keys_and_discrete_downstream_observations'};
const need=(v,m)=>assert.ok(v,m);
const pin=raw=>({bytes:raw.length,sha256:crypto.createHash('sha256').update(raw).digest('hex')});
try {
 need(process.argv.length===3,'HOLD_RUNTIME_PROBE: external runtime-only authorization required');
 const raw=Buffer.from(process.argv[2]),a=JSON.parse(raw);
 need(Buffer.from(JSON.stringify(a,null,2)+'\n').equals(raw),'complete canonical authorization');
 assert.deepEqual(Object.keys(a).sort(),['enabled','provenance','receipts','schema','status'],'exact trusted-product runtime-only keys');
 need(a.schema==='p212-trusted-product-runtime-probe-authorization-v1','distinct probe schema');
 need(a.enabled===true&&a.status==='ROOT_BOUND_TRUSTED_PRODUCT_RUNTIME_DISCOVERY_ONLY','separate runtime-only flag');
 assert.deepEqual(a.provenance,PROVENANCE,'fixed conditional model; no product-startup attestation');
 const roles=['source','bootstrap_key','trusted_product_boundary'];
 need(a.receipts&&typeof a.receipts==='object'&&!Array.isArray(a.receipts),'named receipt map');
 assert.deepEqual(Object.keys(a.receipts).sort(),[...roles].sort(),'three distinct receipt roles');
 const originals=[];
 for(const role of roles) {
  const ref=a.receipts[role];
  assert.deepEqual(Object.keys(ref).sort(),['path','pin'],'whole receipt reference');
  need(ref.path.startsWith(QA+'/')&&fs.realpathSync(ref.path)===ref.path,'physical workspace receipt');
  need(Number.isSafeInteger(ref.pin.bytes)&&ref.pin.bytes>=0&&/^[0-9a-f]{64}$/.test(ref.pin.sha256),'whole finite pin');
  const fd=fs.openSync(ref.path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);
  try {
   const before=fs.fstatSync(fd,{bigint:true});
   need(before.isFile()&&before.size===BigInt(ref.pin.bytes),'whole regular receipt handle');
   const bytes=fs.readFileSync(fd),after=fs.fstatSync(fd,{bigint:true});
   for(const k of ['dev','ino','mode','nlink','uid','gid','rdev','size','blksize','blocks','mtimeNs','ctimeNs','birthtimeNs'])
    need(before[k]===after[k],'same receipt handle stable '+k);
   assert.deepEqual(pin(bytes),ref.pin,'whole source/bootstrap receipt');
   originals.push({role,reference:ref,raw_hex:bytes.toString('hex')});
  } finally { fs.closeSync(fd); }
 }
 need(new Set(originals.map(r=>r.reference.path)).size===roles.length,'source, independent bootstrap key and trust decision use separate receipts');
 assert.deepEqual({...process.env},ENV8,'exact ENV8');
 assert.deepEqual(process.execArgv,[],'no unreceived startup loader/options');
 need(__filename===SELF&&process.cwd()===ROOT,'one source and cwd');
 assert.deepEqual(Object.keys(require.cache),[SELF],'no extra CommonJS file');
 const natives=process.binding('natives'),fingerprints={};
 for(const k of Object.keys(natives).sort()) {
  need(typeof natives[k]==='string'||(k==='configs'&&natives[k]===undefined),'typed whole builtin registry');
  fingerprints[k]=typeof natives[k]==='string'?{type:'string',...pin(Buffer.from(natives[k]))}:{type:'undefined'};
 }
 const maps=fs.readFileSync('/proc/self/maps');
 process.stdout.write(JSON.stringify({status:'RUNTIME_ENUMERATION_ONLY_ROOT_FULL_KEY_PENDING',
  source:SELF,provenance:PROVENANCE,receipts:originals,executable:process.execPath,versions:process.versions,
  architecture:process.arch,platform:process.platform,argv:process.argv,exec_argv:process.execArgv,
  environment:{...process.env},cwd:process.cwd(),umask:process.umask(),
  require_cache:Object.keys(require.cache).sort(),module_load_list:process.moduleLoadList,
  builtin_source_fingerprints:fingerprints,proc_maps_hex:maps.toString('hex'),
  driver_imported:false,child_spawned:false,source_or_runtime_acceptance:false,
  limit:'Mapped path strings and builtin fingerprints are enumeration only. Root must receive whole native files/config/bootstrap and an explicit finite lazy-binding policy.'},null,2)+'\n');
} catch(error) {
 process.stderr.write('HOLD_RUNTIME_PROBE: '+String(error)+'\n');process.exitCode=78;
}
