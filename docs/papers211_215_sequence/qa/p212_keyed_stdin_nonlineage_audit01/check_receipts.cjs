'use strict';
// Auditor-owned JSON/string-only reception; no reviewed program or checker is loaded.
const fs=require('fs'),crypto=require('crypto'),assert=require('assert/strict');
const own='docs/papers211_215_sequence/qa/p212_keyed_stdin_nonlineage_audit01/',base='docs/papers211_215_sequence/qa/';
let checks=0;
const eq=(a,b,m)=>{checks++;assert.deepEqual(a,b,m);};
const ok=(a,m)=>{checks++;assert(a,m);};
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const pins=JSON.parse(fs.readFileSync(own+'INPUTS_BEFORE.json')).inputs;
const allowed=new Map(pins.map(x=>[x.path,x]));
function bytes(p){ok(allowed.has(p)||p.startsWith(own),'explicit documentary path '+p);ok(!p.includes('empty.stdin'),'no proposed input');const b=fs.readFileSync(p);if(allowed.has(p)){eq(b.length,allowed.get(p).bytes,p+' length');eq(sha(b),allowed.get(p).sha256,p+' digest');}return b;}
const native=JSON.parse(bytes(own+'NATIVE01.json'));
const compareRows=[];
for(const call of native.calls){
 const command=call.request&&call.request.cmd;
 if(!command||call.return.exit_code!==0)continue;
 const parts=command.split('\n'),out=[];
 let eligible=true;
 for(const part of parts){
  let m=/^nl -ba ([^ |]+)(?: \| sed -n '(\d+),(\d+)p')?$/.exec(part);
  if(m){
   if(!allowed.has(m[1])){eligible=false;break;}
   const b=bytes(m[1]);ok(b[b.length-1]===10,'LF final');const lines=b.toString('utf8').slice(0,-1).split('\n');
   const first=m[2]?Number(m[2]):1,last=m[3]?Number(m[3]):lines.length;
   out.push(Buffer.from(lines.map((s,i)=>String(i+1).padStart(6,' ')+'\t'+s+'\n').slice(first-1,last).join('')));
   continue;
  }
  m=/^sed -n '(\d+),(\d+)p' ([^ ]+)$/.exec(part);
  if(m&&allowed.has(m[3])){
   const b=bytes(m[3]);ok(!b.length||b[b.length-1]===10,'LF final');const lines=b.toString('utf8').match(/[^\n]*\n/g)||[];
   out.push(Buffer.from(lines.slice(Number(m[1])-1,Number(m[2])).join('')));continue;
  }
  eligible=false;break;
 }
 if(!eligible)continue;
 const expected=Buffer.concat(out),actual=Buffer.from(call.return.output,'utf8');
 eq(actual,expected,'actual archived tool output bytes versus exact rendered source '+call.return.chunk_id);
 compareRows.push({chunk_id:call.return.chunk_id,bytes:actual.length,sha256:sha(actual),commands:parts});
}
ok(compareRows.length>=25,'bounded original display comparisons');
const er=base+'p212_keyed_stdin_linecount_erratum01/';
const bad=bytes(er+'check.cjs'),good=bytes(er+'check_delta01.cjs');
const replacement=bad.toString().replace("  \\\\.\\\\/([^\\\\n]+)$","  ([^\\\\n]+)$");
const sBad=bad.toString(),sGood=good.toString();
const a=sBad.split('\n'),b=sGood.split('\n');eq(a.length,b.length,'same checker length');
const changes=a.flatMap((x,i)=>x===b[i]?[]:[i+1]);eq(changes,[35,36],'only scoped manifest layout and label adapter');
for(const line of changes)ok(a[line-1]!==b[line-1],'actual differing line');
const wc=JSON.parse(bytes(er+'WC_NATIVE.json')),failure=JSON.parse(bytes(er+'CHECK_NATIVE.json'));
const pass=JSON.parse(bytes(er+'CHECK_DELTA_NATIVE.json'));
eq(wc.return.exit_code,0);eq(wc.return.chunk_id,'abb65c');
eq(failure.return.exit_code,1);eq(failure.return.chunk_id,'28125e');ok(failure.return.output.includes('exact ./-relative source manifest'));
eq(pass.return.exit_code,0);const p=JSON.parse(pass.return.output);
eq(p.checks,2613);eq(p.totals,{oldLines:2519,added:204,deleted:44,lines:2679,bytes:148546});
eq(p.old_package_payloads,55);eq(p.old_package_files,56);
for(const key of p.whole_read_keys){const content=bytes(key.path);eq(content.length,key.bytes,key.path);eq(sha(content),key.sha256,key.path);}
const names=['observe.py','driver.js','outer_contract.py','python_runtime_probe.py','node_runtime_probe.js','node_preload.js','product_capture.js'];
const numbers=[[436,22106],[1048,55092],[747,41004],[146,8600],[66,5001],[147,10913],[89,5830]];
const wcExpected=names.map((n,i)=>String(numbers[i][0]).padStart(6,' ')+String(numbers[i][1]).padStart(7,' ')+' '+base+'p212_keyed_stdin_source_delta01/'+n+'\n').join('')+'  2679 148546 total\n';
eq(Buffer.from(wc.return.output),Buffer.from(wcExpected),'actual complete wc output bytes');
const delta=bytes(own+'DELTA_RESULT.json');
const actualDelta=native.calls.find(c=>c.return&&c.return.chunk_id==='3fd564');
ok(actualDelta,'own complete diff native return');eq(delta,Buffer.from(actualDelta.return.output),'attached delta whole raw UTF8 stdout');
const initial=native.calls.find(c=>c.return&&c.return.chunk_id==='35c9c4');ok(initial,'input pin native');
eq(bytes(own+'INPUTS_BEFORE.json'),Buffer.from(initial.return.output),'attached before pin whole output');
process.stdout.write(JSON.stringify({kind:'SOURCE_OUTPUT_AND_EXACT_ERRATUM_RECEPTION_ONLY',checks,rendered_source_output_comparisons:compareRows.length,rendered_source_output_bytes:compareRows.reduce((s,r)=>s+r.bytes,0),rendered_source_output_rows:compareRows,root_erratum_native:{failed_chunk:failure.return.chunk_id,passed_chunk:pass.return.chunk_id,checks:p.checks,whole_keys:p.whole_read_keys.length,totals:p.totals},no_reviewed_execution:true},null,2)+'\n');

