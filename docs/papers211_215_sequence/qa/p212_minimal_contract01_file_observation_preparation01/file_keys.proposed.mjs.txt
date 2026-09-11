// PROSPECTIVE FILE-ONLY SOURCE. No CLI or automatic call; import/observation still require separate authority.
// This is a trusted root file-key utility, not an observed interpreter bootstrap.
import fs from 'node:fs';
import {createHash} from 'node:crypto';

export function collectP212S0Files(request) {
  const SOURCE_ENABLED = true;
  const need = (ok,label) => { if (!ok) throw new Error(label); };
  need(SOURCE_ENABLED,'HOLD_SOURCE_ONLY: no finite file observation');
  const canonical = v => JSON.stringify(v);
  const keys = (v,k,label) => {
    need(v !== null && typeof v === 'object' && !Array.isArray(v),label);
    need(canonical(Object.keys(v).sort()) === canonical([...k].sort()),label+' exact keys');
  };
  const FIELDS = ['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
  const fields = stat => Object.fromEntries(FIELDS.map(k=> {
    need(typeof stat[k] === 'bigint','actual integer metadata'); return [k,stat[k].toString()];
  }));
  const pin = raw => ({bytes:raw.length,sha256:createHash('sha256').update(raw).digest('hex')});
  const same = (a,b,label) => need(canonical(a) === canonical(b),label);
  keys(request,['schema','enabled','status','purpose','entries','total_byte_limit',
    'permission_receipt','settlement_receipt'],'literal finite request');
  need(request.schema === 'p212-s0-ten-field-file-request-v1' && request.enabled === true &&
    request.status === 'ROOT_BOUND_FINITE_FILES_ONLY','received finite file permission');
  need(['source_gate','pre_call','post_call','closed_raw'].includes(request.purpose),'finite purpose');
  need(Array.isArray(request.entries) && request.entries.length > 0 && request.entries.length <= 96,'finite entries');
  need(Number.isSafeInteger(request.total_byte_limit) && request.total_byte_limit >= 0 &&
    request.total_byte_limit <= 268435456,'finite total accepted bytes');
  const reference = (r,label) => {
    keys(r,['path','pin'],label); keys(r.pin,['bytes','sha256'],label+' pin');
    need(typeof r.path === 'string' && r.path.startsWith('/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/') &&
      Number.isSafeInteger(r.pin.bytes) && r.pin.bytes > 0 && /^[0-9a-f]{64}$/.test(r.pin.sha256),label);
  };
  reference(request.permission_receipt,'actual external permission receipt');
  if (request.purpose === 'closed_raw') reference(request.settlement_receipt,'prior actual settled-direct-call reception');
  else need(request.settlement_receipt === null,'no fictitious settlement role');
  const seen = new Set(), ids = new Set();
  // Validate the ENTIRE finite request before the first path observation.
  for (const entry of request.entries) {
    keys(entry,['id','path','role','optional','max_bytes','capture_hex','expected'],'file permission');
    need(typeof entry.id === 'string' && /^[A-Z][A-Z0-9_]{0,63}$/.test(entry.id) && !ids.has(entry.id),'unique entry id');ids.add(entry.id);
    need(typeof entry.path === 'string' && /^\/[!-~]+$/.test(entry.path) && !entry.path.includes('\\') &&
      !entry.path.split('/').slice(1).some(v=>v===''||v==='.'||v==='..'),'literal canonical file spelling');
    need(!seen.has(entry.path),'unique path'); seen.add(entry.path);
    need(['source','receipt','binding','executable','loader','configuration','stdin','raw'].includes(entry.role),'file role');
    need(typeof entry.optional === 'boolean' && entry.capture_hex === true,'literal policy, preserve every actually read byte');
    need(Number.isSafeInteger(entry.max_bytes) && entry.max_bytes >= 0 && entry.max_bytes <= 134217728,'file ceiling');
    need((request.purpose === 'closed_raw') === (entry.role === 'raw'),'raw reads require prior settlement only');
    need(entry.path.startsWith('/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p212_minimal_contract01_raw01/') ===
      (entry.role === 'raw'),'raw path cannot enter another purpose');
    need((entry.role === 'stdin') === (entry.path === '/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p212_keyed_stdin_input01/empty.stdin'),'selected stdin cannot be relabelled');
    if (entry.role === 'stdin') need(entry.path === '/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p212_keyed_stdin_input01/empty.stdin' &&
      !entry.optional && entry.max_bytes === 0 && entry.capture_hex,'exact selected empty-input role');
    if (entry.expected !== null) {
      keys(entry.expected,['state','metadata','content'],'expected prior key');
      need(entry.expected.state === 'present' || (entry.optional && entry.expected.state === 'absent'),'expected state');
      if (entry.expected.state === 'present') {
        keys(entry.expected.metadata,FIELDS,'ten-field expected metadata');
        for (const v of Object.values(entry.expected.metadata)) need(typeof v === 'string' && /^-?(0|[1-9][0-9]*)$/.test(v) && v !== '-0','exact decimal metadata');
        keys(entry.expected.content,['bytes','sha256'],'expected whole content');
        need(Number.isSafeInteger(entry.expected.content.bytes) && entry.expected.content.bytes >= 0 &&
          /^[0-9a-f]{64}$/.test(entry.expected.content.sha256),'expected full pin');
        need(entry.expected.content.bytes <= entry.max_bytes && BigInt(entry.expected.content.bytes) === BigInt(entry.expected.metadata.size) &&
          (BigInt(entry.expected.metadata.mode)&0o170000n) === 0o100000n,'complete consistent expected regular key before reads');
      } else need(entry.expected.metadata === null && entry.expected.content === null,'actual absence has no invented key');
    } else need(request.purpose === 'source_gate' || request.purpose === 'closed_raw','pre/post need independently received expected keys');
  }
  const rows = [];
  let acceptedBytes = 0, failure = null;
  for (const entry of request.entries) {
    const row = {id:entry.id,path:entry.path,role:entry.role,state:null,lstat_before:null,
      fd:null,fstat_before:null,fstat_after:null,lstat_after:null,bytes_read:0,eof:false,
      content:null,raw_hex:entry.capture_hex ? '' : null,close_succeeded:null,error:null,close_error:null};
    rows.push(row);
    let fd = null;
    const chunks = [];
    try {
      let lexical;
      try { lexical = fs.lstatSync(entry.path,{bigint:true}); }
      catch(error) {
        if (entry.optional && error?.code === 'ENOENT') {
          row.state = 'absent'; row.error = {operation:'lstat',code:'ENOENT'};
          if (entry.expected !== null) same(entry.expected.state,'absent','received optional absence stays absent');
          continue;
        }
        throw error;
      }
      row.state = 'present'; row.lstat_before = fields(lexical);
      need(lexical.isFile() && !lexical.isSymbolicLink(),'physical regular leaf only; no alias following');
      if (entry.expected !== null) {
        need(entry.expected.state === 'present','absent input appeared');
        same(row.lstat_before,entry.expected.metadata,'received expected key BEFORE open/read');
      }
      fd = fs.openSync(entry.path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);
      row.fd = fd; const before = fs.fstatSync(fd,{bigint:true}); row.fstat_before = fields(before);
      need(before.isFile(),'opened regular file'); same(row.fstat_before,row.lstat_before,'same-fd key BEFORE bytes');
      need(before.size <= BigInt(entry.max_bytes) && before.size <= BigInt(request.total_byte_limit-acceptedBytes),'known oversize stops before bytes');
      const hash = createHash('sha256'), buffer = Buffer.alloc(65536);
      while (true) {
        const remaining = Math.min(entry.max_bytes-row.bytes_read,request.total_byte_limit-acceptedBytes-row.bytes_read);
        need(remaining >= 0,'no negative byte budget');
        const count = fs.readSync(fd,buffer,0,Math.min(buffer.length,remaining+1),null);
        if (count === 0) { row.eof = true; break; }
        const chunk = Buffer.from(buffer.subarray(0,count));
        row.bytes_read += count; hash.update(chunk); if (entry.capture_hex) chunks.push(chunk);
        need(count <= remaining,'one overflow sentinel preserved; no whole-file success');
      }
      row.content = {bytes:row.bytes_read,sha256:hash.digest('hex')};
      need(BigInt(row.bytes_read) === before.size,'complete EOF byte count equals actual size');
      row.fstat_after = fields(fs.fstatSync(fd,{bigint:true}));
      same(row.fstat_after,row.fstat_before,'same opened file after complete EOF');
      row.lstat_after = fields(fs.lstatSync(entry.path,{bigint:true}));
      same(row.lstat_after,row.lstat_before,'endpoint after complete EOF');
      if (entry.expected !== null) same(row.content,entry.expected.content,'received complete content pin');
      if (entry.role === 'stdin') same(row.content,pin(Buffer.alloc(0)),'entire zero-byte stdin');
    } catch(error) {
      row.error = {operation:'finite_file_key',name:String(error?.name ?? 'Error'),code:typeof error?.code === 'string' ? error.code : null,
        message:String(error?.message ?? error)};
      failure = {id:entry.id,path:entry.path,error:row.error};
    } finally {
      if (fd !== null) {
        try { fs.closeSync(fd); row.close_succeeded = true; }
        catch(error) { row.close_succeeded = false; row.close_error = {name:String(error?.name ?? 'Error'),message:String(error?.message ?? error)};
          failure = {id:entry.id,path:entry.path,error:row.close_error}; }
      }
      if (entry.capture_hex) row.raw_hex = Buffer.concat(chunks).toString('hex');
    }
    if (failure !== null) break;
    acceptedBytes += row.bytes_read;
  }
  return {schema:'p212-s0-ten-field-files-v1',status:failure ? 'FAILED_PARTIAL_PRESERVED' : 'OBSERVED_ROOT_RECEPTION_PENDING',
    request,rows,accepted_bytes:acceptedBytes,failure,actual_ancestor_scan:false,native_statx_attestation:false,
    process_or_startup_observation:false,source_acceptance:false,operation_permission:false};
}

// The only directory observations are the query cwd and three new capture
// directories. Names are data, never followed or used to expand file entries.
export function collectP212S0Directories(request) {
  const SOURCE_ENABLED = false;
  if (!SOURCE_ENABLED) throw new Error('HOLD_SOURCE_ONLY: no directory observation');
  const QA = '/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa';
  const allowed = [QA+'/p212_build_dependency_query01/query_cwd',QA+'/p212_minimal_contract01_raw01',
    QA+'/p212_minimal_contract01_raw01/help01',QA+'/p212_minimal_contract01_raw01/version01'];
  const FIELDS = ['dev','ino','mode','nlink','uid','gid','rdev','size','mtimeNs','ctimeNs'];
  const identity = s => ['dev','ino','mode','uid','gid','rdev'].map(k=>s[k]);
  const need = (v,m) => { if (!v) throw new Error(m); };
  const fields = s => Object.fromEntries(FIELDS.map(k=>{need(typeof s[k]==='bigint','actual directory fields');return [k,s[k].toString()];}));
  need(request !== null && typeof request === 'object' && !Array.isArray(request) &&
    JSON.stringify(Object.keys(request).sort()) === JSON.stringify(['schema','enabled','status','paths','permission_receipt'].sort()),'exact directory request');
  need(request.schema === 'p212-s0-directory-request-v1' && request.enabled === true &&
    request.status === 'ROOT_BOUND_FOUR_DIRECTORY_POINTS_ONLY','received directory request');
  need(JSON.stringify(request.paths) === JSON.stringify(allowed),'exact four directory roles, no discovery');
  const r = request.permission_receipt;
  need(r && JSON.stringify(Object.keys(r).sort()) === '["path","pin"]' && typeof r.path === 'string' &&
    r.path.startsWith(QA+'/') && r.pin && JSON.stringify(Object.keys(r.pin).sort()) === '["bytes","sha256"]' &&
    Number.isSafeInteger(r.pin.bytes) && r.pin.bytes > 0 && /^[0-9a-f]{64}$/.test(r.pin.sha256),'external directory permission reference');
  const rows = [];
  let failure = null;
  for (const path of allowed) {
    const row = {path,before:null,after:null,names:[],eof:false,close_succeeded:null,error:null,close_error:null};
    rows.push(row); let directory = null;
    try {
      const before = fs.lstatSync(path,{bigint:true}); row.before = fields(before);
      need(before.isDirectory() && !before.isSymbolicLink(),'physical directory leaf');
      directory = fs.opendirSync(path);
      while (true) {
        const entry = directory.readSync();
        if (entry === null) { row.eof = true; break; }
        row.names.push(entry.name);
        need(row.names.length <= 2,'one extra name preserved; unexpected directory membership');
        need(/^[A-Za-z0-9_.-]+$/.test(entry.name),'unambiguous literal capture member');
      }
      row.names.sort(); row.after = fields(fs.lstatSync(path,{bigint:true}));
      need(JSON.stringify(identity(row.before)) === JSON.stringify(identity(row.after)),'directory identity after name EOF');
    } catch(error) {
      row.error = {name:String(error?.name ?? 'Error'),code:typeof error?.code === 'string' ? error.code : null,message:String(error?.message ?? error)};
      failure = {path,error:row.error};
    } finally {
      if (directory !== null) {
        try { directory.closeSync(); row.close_succeeded = true; }
        catch(error) { row.close_succeeded = false; row.close_error = {name:String(error?.name ?? 'Error'),message:String(error?.message ?? error)};
          failure = {path,error:row.close_error}; }
      }
    }
    if (failure !== null) break;
  }
  return {schema:'p212-s0-directory-points-v1',status:failure ? 'FAILED_PARTIAL_PRESERVED' : 'OBSERVED_ROOT_RECEPTION_PENDING',
    request,rows,failure,unscanned_ancestors_trusted:true,directory_handle_identity_attested:false,operation_permission:false};
}
