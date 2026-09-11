'use strict';
// SOURCE ONLY. Execute only after root receives this source and grants DATA.
const fs=require('node:fs'), crypto=require('node:crypto');
const W='/root/autodl-tmp/symbolic_dynamics';
const F='papers/212-closed-pointer-orbits/frozen_round1/';
const M='docs/papers211_215_sequence/qa/p212_round1_preparation01/FILES.tsv';
const C='docs/papers211_215_sequence/reviews/p212_b/build01/source_only/';
const fields=['dev','ino','mode','size','mtimeNs','ctimeNs'];
const inputs=new Map();let checks=0;
function need(x,s){checks++;if(!x)throw Error(s);}
function sha(b){return crypto.createHash('sha256').update(b).digest('hex');}
function metadata(s){return Object.fromEntries(fields.map(k=>[k,String(s[k])]));}
function same(a,b,s){need(JSON.stringify(a)===JSON.stringify(b),s);}
function safe(p){need(typeof p==='string'&&/^[A-Za-z0-9_./-]+$/.test(p)&&!p.startsWith('/')&&!p.split('/').some(x=>x===''||x==='.'||x==='..'),'workspace relative path');}
function read(p){
 safe(p);const full=W+'/'+p;
 const parts=p.split('/');
 for(let i=1;i<parts.length;i++)need(fs.lstatSync(W+'/'+parts.slice(0,i).join('/')).isDirectory(),'ordinary directory '+p);
 const named=fs.lstatSync(full,{bigint:true});need(named.isFile(),'regular nonlink '+p);
 const fd=fs.openSync(full,'r');let b,k;
 try{const before=fs.fstatSync(fd,{bigint:true});need(before.isFile(),'regular descriptor '+p);
  same(metadata(named),metadata(before),'opened same input '+p);b=fs.readFileSync(fd);
  const after=fs.fstatSync(fd,{bigint:true});same(metadata(before),metadata(after),'stable descriptor '+p);
  same(metadata(after),metadata(fs.lstatSync(full,{bigint:true})),'stable named input '+p);
  need(String(b.length)===String(after.size),'complete size '+p);
  k={path:p,bytes:b.length,sha256:sha(b),metadata:metadata(after)};
 }finally{fs.closeSync(fd);}
 if(inputs.has(p))same(inputs.get(p),k,'repeated key '+p);else inputs.set(p,k);
 return b;
}
function lines(b){const t=b.toString('utf8');need(Buffer.from(t).equals(b),'UTF8 table');need(t.endsWith('\n'),'final table LF');return t.slice(0,-1).split('\n');}
function main(){
 need(process.cwd()===W&&process.argv.length===2,'fixed cwd/no args');
 const mapRaw=read(M);need(sha(mapRaw)==='bda339fb7873faf5da8045df37a7f7cbe86885ce75df5211c0e9f360b43b73d1','fixed25 mapping');
 const pinRaw=read(F+'SHA256SUMS');need(sha(pinRaw)==='1c6993c46eb9e7db32c098e6db60411b60292685f25a6987193c213d91af7cf7','fixedRound1 seal');
 const mappings=lines(mapRaw).map(line=>{const p=line.split('\t');need(p.length===2,'mapping pair');p.forEach(safe);return p;});
 const pinRows=lines(pinRaw).map(line=>{need(/^[0-9a-f]{64}  [A-Za-z0-9_./-]+$/.test(line),'pin syntax');safe(line.slice(66));return[line.slice(66),line.slice(0,64)];});
 need(mappings.length===25&&pinRows.length===25,'exact25 rows');
 need(new Set(mappings.map(x=>x[0])).size===25&&new Set(mappings.map(x=>x[1])).size===25,'unique mappings');
 need(new Set(pinRows.map(x=>x[0])).size===25,'unique pins');
 same(mappings.map(x=>x[1]).sort(),pinRows.map(x=>x[0]).sort(),'mapping covers all frozen pins');
 const pins=new Map(pinRows),rows=[];
 for(const[source,destination]of mappings){const frozen=read(F+destination),current=read(source);
  need(sha(frozen)===pins.get(destination),'frozen content pin '+destination);
  need(current.equals(frozen),'whole mapped no-change '+destination);
  rows.push({source,frozen:F+destination,bytes:frozen.length,sha256:sha(frozen),raw_equal:true});
 }
 const eight=['main.tex','math_commands.tex','references.bib','sections/01_setup.tex','sections/02_returns.tex','sections/03_period_set.tex','sections/04_census.tex','sections/05_scope.tex'];
 const cold=[];
 for(const name of [...eight,'main.pdf']){const fresh=read(C+name),frozen=read(F+name);
  need(fresh.equals(frozen),'whole cold-source/new-PDF equality '+name);
  cold.push({path:C+name,bytes:fresh.length,sha256:sha(fresh),raw_equal_frozen:true});
 }
 const paths=[...inputs.keys()];for(const p of paths)read(p);
 process.stdout.write(JSON.stringify({schema:'P212_B_NO_CHANGE_DATA_V1',status:'PASS_EXACT_25_MAPPING_AND_8_SOURCE_PLUS_NEW_PDF',
  checks,mapped_payloads:rows,cold_sources_and_new_pdf:cold,inputs:[...inputs.values()].sort((a,b)=>a.path<b.path?-1:a.path>b.path?1:0),
  scope:{host_paths_followed:false,producer_executed:false,build_executed:false,artifact_gate_replaced:false,final_review_issued:false}},null,2)+'\n');
}
try{main();}catch(e){process.stderr.write(String(e.stack||e)+'\n');process.exitCode=1;}
