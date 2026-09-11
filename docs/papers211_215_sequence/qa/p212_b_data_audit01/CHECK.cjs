'use strict';
// SOURCE ONLY: root must receive this complete file and separately grant DATA.
// Reads saved workspace evidence; never imports/calls the producer or guard.
const fs = require('node:fs');
const crypto = require('node:crypto');
const W = '/root/autodl-tmp/symbolic_dynamics';
const D = 'docs/papers211_215_sequence/qa/p212_b_data_audit01';
const R = 'docs/papers211_215_sequence/qa/p212_b_source_root01';
const P = 'docs/papers211_215_sequence/qa/p212_b_execution_preparation01';
const B = 'docs/papers211_215_sequence/reviews/p212_b';
const RUN = 'docs/papers211_215_sequence/qa/p212_b_runs/initial01';
const FAMILIES = ['figure_eight','barbell','theta'];
const ROWS = ['figure_eight_double_loop','figure_eight_short_nontrivial',
 'figure_eight_long','barbell_short','barbell_long','theta_triple_direct','theta_other'];
const FIRST = [1,2,3,2,4,2,3];
let assertions = 0;
const consumed = new Map();
function need(ok, message) { assertions++; if (!ok) throw Error(message); }
function sha(b) { return crypto.createHash('sha256').update(b).digest('hex'); }
function cmp(a,b) {
 if (Array.isArray(a) && Array.isArray(b)) {
  for (let i=0;i<Math.min(a.length,b.length);i++) { const c=cmp(a[i],b[i]); if(c) return c; }
  return Math.sign(a.length-b.length);
 }
 return a===b ? 0 : a<b ? -1 : 1;
}
function wire(x) {
 if (typeof x==='boolean') return x?'true':'false';
 if (typeof x==='number') { need(Number.isSafeInteger(x)&&!Object.is(x,-0),'unsafe JSON integer'); return String(x); }
 if (typeof x==='string') {
  need([...x].every(c=>c.charCodeAt(0)<=127),'non-ASCII scientific string');
  return JSON.stringify(x).replace(/\x7f/g,'\\u007f');
 }
 if (Array.isArray(x)) return '['+x.map(wire).join(',')+']';
 need(x!==null && typeof x==='object' && Object.getPrototypeOf(x)===Object.prototype,'unsupported JSON type');
 return '{'+Object.keys(x).sort().map(k=>wire(k)+':'+wire(x[k])).join(',')+'}';
}
function plain(x) { return JSON.stringify(x); }
function uniqueJson(text){
 // Strict ordinary JSON grammar plus duplicate-key and finite-number rejection.
 let i=0;const ws=()=>{while(i<text.length&&/[ \t\r\n]/.test(text[i]))i++;};
 function string(){const start=i;need(text[i++]==='"','JSON string start');
  while(i<text.length){const ch=text[i++];if(ch==='"')return JSON.parse(text.slice(start,i));
   need(ch.charCodeAt(0)>=32,'JSON raw control character');
   if(ch==='\\'){need(i<text.length,'JSON escape end');const e=text[i++];
    if(e==='u'){need(/^[0-9a-fA-F]{4}$/.test(text.slice(i,i+4)),'JSON Unicode escape');i+=4;}
    else need('"\\/bfnrt'.includes(e),'JSON escape spelling');
   }
  }throw Error('unterminated JSON string');
 }
 function value(){ws();const ch=text[i];
  if(ch==='"')return string();
  if(ch==='{'){i++;ws();const result={},seen=new Set();if(text[i]==='}'){i++;return result;}
   while(true){ws();const key=string();need(!seen.has(key),'duplicate JSON object key');seen.add(key);ws();need(text[i++]===':','JSON colon');
    const v=value();Object.defineProperty(result,key,{value:v,enumerable:true,writable:true,configurable:true});ws();const end=text[i++];
    if(end==='}')return result;need(end===',','JSON object separator');}
  }
  if(ch==='['){i++;ws();const result=[];if(text[i]===']'){i++;return result;}
   while(true){result.push(value());ws();const end=text[i++];if(end===']')return result;need(end===',','JSON array separator');}
  }
  for(const [token,v]of [['true',true],['false',false],['null',null]])if(text.startsWith(token,i)){i+=token.length;return v;}
  const match=/^-?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?/.exec(text.slice(i));need(match!==null,'JSON value token');
  i+=match[0].length;const n=Number(match[0]);need(Number.isFinite(n)&&(!Number.isInteger(n)||Number.isSafeInteger(n)),'finite safe JSON number');return n;
 }
 const result=value();ws();need(i===text.length,'JSON complete consumption');return result;
}
function equal(a,b,label) {
 need(typeof a===typeof b,label+': type');
 if (a===null || b===null) { need(a===b,label+': null'); return; }
 if (Array.isArray(a)||Array.isArray(b)) {
  need(Array.isArray(a)&&Array.isArray(b),label+': array'); need(a.length===b.length,label+': length');
  for(let i=0;i<a.length;i++) equal(a[i],b[i],label+'/'+i);
 } else if(typeof a==='object') {
  const ak=Object.keys(a).sort(),bk=Object.keys(b).sort();
  need(plain(ak)===plain(bk),label+': keys'); for(const k of ak)equal(a[k],b[k],label+'/'+k);
 } else need(a===b,label+': value');
}
function product(n,k) {
 if(!k)return [[]]; const out=[];
 for(let a=0;a<n;a++)for(const tail of product(n,k-1))out.push([a,...tail]);
 return out;
}
function choose(values,k,start=0) {
 if(!k)return [[]]; const out=[];
 for(let i=start;i<=values.length-k;i++)for(const tail of choose(values,k-1,i+1))out.push([values[i],...tail]);
 return out;
}
function range(n) { return Array.from({length:n},(_,i)=>i); }
function fac(n) { let a=1;for(let i=2;i<=n;i++)a*=i;return a; }
function code(state,n) { return state.reduce((s,v,i)=>s+v*n**i,0); }
function stateAt(i,n) { const a=[];for(let j=0;j<n+2;j++){a.push(i%n);i=Math.floor(i/n);}return a; }
function pair(a,b) { return a<b?[a,b]:[b,a]; }
function edgeList(st) { return [pair(st[0],st[1]),...st.slice(2).map((b,a)=>pair(a,b))].sort(cmp); }
function degrees(vs,es) {
 const ds=new Map(vs.map(v=>[v,0]));for(const [a,b]of es){ds.set(a,ds.get(a)+1);ds.set(b,ds.get(b)+1);}return ds;
}
function connected(vs,es,start) {
 const seen=new Set([start]), todo=[start];
 while(todo.length){const v=todo.pop();for(const [a,b]of es){
  const w=a===v?b:b===v?a:null;if(w!==null&&!seen.has(w)){seen.add(w);todo.push(w);}
 }} return [...seen].sort(cmp);
}
function invariant(st) {
 const es=edgeList(st),active=connected(range(st.length-2),es,st[0]);
 let core=active.slice();const layers=[];
 while(true){const retained=es.filter(([a,b])=>core.includes(a)&&core.includes(b));
  const d=degrees(core,retained),remove=core.filter(v=>d.get(v)<2);
  if(!remove.length){const complement=st.slice(2).map((b,a)=>[a,b]).filter(([a])=>!core.includes(a));
   return {key:[core,retained,complement],value:{edges:es,active,pruning_layers:layers,core,core_edges:retained,complement}};
  }layers.push(remove);core=core.filter(v=>!remove.includes(v));
 }
}
function describe(vs,es) {
 // Reception route: traverse maximal chains using temporary incidence indices,
 // rather than executing B's degree-two contraction implementation.
 const d=degrees(vs,es),branches=vs.filter(v=>d.get(v)>2).sort(cmp),used=new Set(),paths=[];
 for(const b of branches)for(let eid=0;eid<es.length;eid++) {
  if(used.has(eid)||!es[eid].includes(b))continue;
  let current=b,id=eid;const path=[b];
  while(true){need(!used.has(id),'chain reused incidence');used.add(id);
   const [a,z]=es[id],next=a===current?z:a;path.push(next);
   if(branches.includes(next))break;
   const options=es.map((e,i)=>e.includes(next)&&!used.has(i)?i:-1).filter(i=>i>=0);
   need(options.length===1,'chain continuation');current=next;id=options[0];
  }
  const reverse=path.slice().reverse();paths.push(cmp(path,reverse)<=0?path:reverse);
 }
 need(used.size===es.length,'all core incidences decomposed');
 let family,row,period,classes,ordered;
 if(branches.length===1){family='figure_eight';ordered=paths.sort(cmp);const [a,b]=ordered.map(p=>p.length-1);
  row=a===1&&b===1?ROWS[0]:Math.max(a,b)<=2?ROWS[1]:ROWS[2];
  period=row===ROWS[0]?1:(a+b)*(Math.max(a,b)>=3?2:1);classes=Math.min(a,b)>=3?2:1;
 }else if(branches.length===2&&paths.some(p=>p[0]===p.at(-1))){family='barbell';
  ordered=[...paths.filter(p=>p[0]===p.at(-1)).sort(cmp),...paths.filter(p=>p[0]!==p.at(-1)).sort(cmp)];
  const [a,b,c]=ordered.map(p=>p.length-1);row=Math.max(a,b)<=2?ROWS[3]:ROWS[4];
  period=(a+b+2*c)*(Math.max(a,b)>=3?2:1);classes=Math.min(a,b)>=3?2:1;
 }else{need(branches.length===2,'branch signature');family='theta';ordered=paths.sort(cmp);
  const ls=ordered.map(p=>p.length-1);row=ls.every(x=>x===1)?ROWS[5]:ROWS[6];
  period=row===ROWS[5]?2:2*ls.reduce((a,b)=>a+b,0);classes=ls.filter(x=>x===1).length>=2?1:2;
 }
 return {family,row,branches,paths:ordered,lengths:ordered.map(p=>p.length-1),period,classes};
}
function catalogue(s) {
 // Independent completeness: all edge multisets of size s+1, not Prüfer words.
 const vs=range(s),pairs=[];for(const a of vs)for(let b=a;b<s;b++)pairs.push([a,b]);
 const out=[];
 function visit(start,left,es){if(!left){const d=degrees(vs,es);
  if(vs.every(v=>d.get(v)>=2)&&connected(vs,es,0).length===s)out.push(es.map(e=>e.slice()));return;
 }for(let i=start;i<pairs.length;i++)visit(i,left-1,[...es,pairs[i]]);}
 visit(0,s+1,[]);return out.sort(cmp);
}
function anchor(st,d) {
 const [u,v,...f]=st;if(u!==d.branches[0])return null;const ps=d.paths;
 if(d.family==='theta'){
  const remain=ps.map(p=>p.slice(1,-1)),raw=[];
  for(const target of [v,f[u]]){
   const eligible=remain.filter(t=>(t.length?t[0]:d.branches[1])===target).sort(cmp);
   if(!eligible.length)return null;const token=eligible[0];raw.push(token);
   remain.splice(remain.findIndex(t=>cmp(t,token)===0),1);
  }need(remain.length===1,'theta remaining token');raw.push(remain[0]);
  const rotations=range(3).map(i=>[...raw.slice(i),...raw.slice(0,i)]).sort(cmp);return [raw,rotations[0]];
 }
 let targets;
 if(d.family==='figure_eight'){if(v!==ps[0][1]&&v!==ps[0].at(-2))return null;targets=[v,f[u]];}
 else{if(v!==ps[2][1])return null;targets=d.branches.map(b=>f[b]);}
 const bits=[];for(let i=0;i<2;i++){const p=ps[i],t=targets[i];if(t!==p[1]&&t!==p.at(-2))return null;
  bits.push(p.length<=3||t===p[1]?0:1);}
 const reverse=bits.map((b,i)=>ps[i].length>3?1-b:0);return [bits,cmp(bits,reverse)<=0?bits:reverse];
}
function staticAnchors(s,cats) {
 const map=new Map(cats.map(es=>[plain(es),{d:describe(range(s),es),a:[]}]));
 for(const st of product(s,s+2)){const entry=map.get(plain(edgeList(st)));if(!entry)continue;
  const value=anchor(st,entry.d);if(value!==null)entry.a.push([st,value]);}
 return new Map([...map].map(([k,v])=>[k,v.a]));
}
function scientificPieces() {
 // Reception route: direct theorem-weight sums, not B's denominator recurrence.
 const pieces=new Map(FAMILIES.map(f=>[f,new Map()]));
 const add=(f,s,p,c)=>{const m=pieces.get(f),key=plain([s,p]);m.set(key,(m.get(key)||0)+c);};
 for(let a=1;a<=4;a++)for(let b=1;b<=4;b++){
  const s=a+b-1;if(s>4)continue;
  const short=Math.max(a,b)<=2;
  add('figure_eight',s,a===1&&b===1?1:(a+b)*(short?1:2),a===1&&b===1?24:short?12:6);
 }
 for(let a=1;a<=4;a++)for(let b=1;b<=4;b++)for(let c=1;c<=4;c++){
  const s=a+b+c-1;if(s>4)continue;const short=Math.max(a,b)<=2;
  add('barbell',s,(a+b+2*c)*(short?1:2),short?12:6);
 }
 add('theta',2,2,12);
 for(let k=1;k<=3;k++)for(const offsets of product(2,k)){
  const total=offsets.reduce((a,b)=>a+b+1,0),s=2+total;if(s>4)continue;
  add('theta',s,6+2*total,12*(k===1?1:2)/fac(k));
 }
 return pieces;
}
function poly(m){return [...m].filter(([,v])=>v!==0).sort((a,b)=>a[0]-b[0]);}
function entries(piece){return [...piece].map(([k,v])=>[...JSON.parse(k),v]).sort(cmp);}
function reconstructScience(){
 const checks=[];
 function P(name,scope,observed,expected){checks.push({id:checks.length,name,scope,observed,expected,passed:wire(observed)===wire(expected)});}
 const cats=new Map(range(4).map(i=>[i+1,catalogue(i+1)]));
 const anchors=new Map([...cats].map(([s,c])=>[s,staticAnchors(s,c)])),pieces=scientificPieces(),carriers=[];
 for(let n=1;n<=4;n++){
  const N=n**(n+2),states=range(N).map(i=>stateAt(i,n)),forward=[],inv=Array(N).fill(-1);
  // Literal simultaneous forward update, then inversion of the complete table.
  for(let i=0;i<N;i++){const [u,v,...f]=states[i],next=f.slice(),old=f[v];next[v]=u;
   const j=code([v,old,...next],n);need(inv[j]===-1,'literal map injective');forward.push(j);inv[j]=i;}
  const slot=Array(N).fill(-1);
  for(let i=0;i<N;i++){P('inverse_range',`${n}/${i}`,inv[i]>=0&&inv[i]<N,true);P('unit_preimage',`${n}/${i}`,slot[inv[i]],-1);slot[inv[i]]=i;}
  const roots=Array(N).fill(-1),components=new Map();
  for(let i=0;i<N;i++)if(roots[i]<0){const members=[],seen=new Set();let j=i;
   while(!seen.has(j)){seen.add(j);members.push(j);j=forward[j];}
   need(j===i,'literal cycle no transient');const root=Math.min(...members);members.sort((a,b)=>a-b);
   components.set(root,members);for(const q of members)roots[q]=root;
  }
  const groups=new Map(),records=[],invariants=states.map(invariant);
  for(let i=0;i<N;i++){const st=states[i],{key,value}=invariants[i],k=plain(key);
   if(!groups.has(k))groups.set(k,{key,members:[]});groups.get(k).members.push(i);
   const [u,v,...f]=st,g=f.slice();g[v]=u;
   P('literal_forward',`${n}/${i}`,states[forward[i]],[v,f[v],...g]);
   P('backward_invariant',`${n}/${i}`,invariants[inv[i]].key,key);
   P('full_edges_invariant',`${n}/${i}`,invariants[inv[i]].value.edges,value.edges);
   P('registers_core',`${n}/${i}`,[key[0].includes(u),key[0].includes(v)],[true,true]);
   P('core_internal',`${n}/${i}`,key[0].every(a=>key[0].includes(f[a])),true);
   P('active_excess',`${n}/${i}`,value.edges.filter(([a,b])=>value.active.includes(a)&&value.active.includes(b)).length,value.active.length+1);
   records.push({id:i,state:st,inverse:inv[i],forward:forward[i],orbit:roots[i],invariant:value});
  }
  const orbits=[];
  for(const [oid,members]of [...components].sort((a,b)=>a[0]-b[0])){const order=[];let j=oid;
   while(!order.includes(j)){order.push(j);j=inv[j];}
   P('dsu_cycle',`${n}/${oid}`,[j,order.slice().sort((a,b)=>a-b)],[oid,members]);orbits.push({id:oid,inverse_time:order,period:order.length});
  }
  const expected=new Map();
  for(let s=1;s<=n;s++)for(const vertices of choose(range(n),s)){
   const outside=range(n).filter(v=>!vertices.includes(v));
   for(const es of cats.get(s)){const lifted=es.map(([a,b])=>pair(vertices[a],vertices[b])).sort(cmp),d=describe(vertices,lifted);
    for(const dest of product(n,n-s)){const complement=outside.map((v,i)=>[v,dest[i]]),key=[vertices,lifted,complement];
     expected.set(plain(key),{key,s,local:es,d});}
   }
  }
  P('complete_groups',String(n),[...groups.values()].map(x=>x.key).sort(cmp),[...expected.values()].map(x=>x.key).sort(cmp));
  const groupRecords=[],observedPoly=new Map(),pure=new Map(FAMILIES.map(f=>[f,new Map()])),rowCounts=Object.fromEntries(ROWS.map(r=>[r,[0,0,0]]));
  for(const entry of [...expected.values()].sort((a,b)=>cmp(a.key,b.key))){const gid=groupRecords.length,{key,s,local,d}=entry,[vertices,,complement]=key;
   const members=groups.get(plain(key))?.members||[],oids=[...new Set(members.map(i=>roots[i]))].sort((a,b)=>a-b),periods=oids.map(i=>components.get(i).length);
   P('period_table',`${n}/g${gid}`,periods,Array(d.classes).fill(d.period));
   const actual=[],classes=new Map();
   for(const i of members){const value=anchor(states[i],d);if(value===null)continue;const [raw,cls]=value;actual.push([i,raw,cls]);
    const ck=plain(cls);if(!classes.has(ck))classes.set(ck,{cls,ids:new Set()});classes.get(ck).ids.add(roots[i]);}
   const wanted=[];
   for(const [st]of anchors.get(s).get(plain(local))){const [u,v,...f]=st,full=Array(n).fill(0);
    for(const [a,b]of complement)full[a]=b;for(let a=0;a<s;a++)full[vertices[a]]=vertices[f[a]];
    const fullState=[vertices[u],vertices[v],...full],value=anchor(fullState,d);need(value!==null,'lifted anchor');wanted.push([code(fullState,n),...value]);}
   actual.sort(cmp);wanted.sort(cmp);
   P('complete_anchor_states',`${n}/g${gid}`,actual,wanted);
   const classRows=[...classes.values()].sort((a,b)=>cmp(a.cls,b.cls)).map(x=>[x.cls,[...x.ids].sort((a,b)=>a-b)]);
   P('decoration_bijection',`${n}/g${gid}`,classRows.map(x=>x[1]).sort(cmp),oids.map(i=>[i]));
   P('decoration_cardinality',`${n}/g${gid}`,classes.size,d.classes);
   for(const oid of oids){const p=components.get(oid).length;observedPoly.set(p,(observedPoly.get(p)||0)+1);
    if(s===n){const m=pure.get(d.family);m.set(p,(m.get(p)||0)+1);}}
   rowCounts[d.row][0]++;rowCounts[d.row][1]+=oids.length;rowCounts[d.row][2]+=members.length;
   groupRecords.push({id:gid,key,description:d,states:members,orbits:oids,actual_anchors:actual,expected_anchors:wanted,class_to_orbits:classRows});
  }
  const contributions=[],expectedPoly=new Map();
  for(let s=1;s<=n;s++){const multiplier=fac(n)/fac(n-s)*n**(n-s),terms=new Map();
   for(const family of FAMILIES)for(const [size,p,c]of entries(pieces.get(family)))if(size===s){terms.set(p,(terms.get(p)||0)+c*multiplier);expectedPoly.set(p,(expectedPoly.get(p)||0)+c*multiplier);}
   contributions.push({s,multiplier,terms24:poly(terms)});
  }
  P('full_census',String(n),poly(new Map([...observedPoly].map(([p,c])=>[p,24*c]))),poly(expectedPoly));
  for(const family of FAMILIES){const expectedFamily=new Map(entries(pieces.get(family)).filter(([s])=>s===n).map(([,p,c])=>[p,c*fac(n)]));
   P('pure_family_series',`${n}/${family}`,poly(new Map([...pure.get(family)].map(([p,c])=>[p,24*c]))),poly(expectedFamily));}
  let periodSet=[1];if(n>1){periodSet=range(2*n).map(i=>i+1);for(let p=2*n+2;p<=4*n-4;p+=2)periodSet.push(p);}
  P('attained_period_set',String(n),[...observedPoly.keys()].sort((a,b)=>a-b),periodSet);
  P('maximum',String(n),Math.max(...observedPoly.keys()),n===1?1:4*n-4);
  P('fixed_states',String(n),observedPoly.get(1)||0,n**n);
  P('state_mass',String(n),[...observedPoly].reduce((s,[p,c])=>s+p*c,0),N);
  const fixed=[];let iterates=range(N);
  for(let k=1;k<=(n===1?1:4*n-4);k++){iterates=iterates.map(i=>inv[i]);const ids=range(N).filter(i=>iterates[i]===i);
   const predicted24=[...expectedPoly].filter(([p])=>k%p===0).reduce((s,[p,c])=>s+p*c,0);P('fixed_iterate',`${n}/${k}`,24*ids.length,predicted24);fixed.push({k,ids,predicted24});}
  ROWS.forEach((row,i)=>P('row_presence',`${n}/${row}`,rowCounts[row][0]>0,n>=FIRST[i]));
  carriers.push({n,states:records,orbits,groups:groupRecords,row_counts:rowCounts,period_polynomial:poly(observedPoly),extension_contributions:contributions,fixed_iterates:fixed});
 }
 const coreSeries=[];
 function binom2(x){return x<2?0:x*(x-1)/2;}
 for(let s=1;s<=4;s++){const terms=new Map();for(const f of FAMILIES)for(const [size,p,c]of entries(pieces.get(f)))if(size===s)terms.set(p,(terms.get(p)||0)+c);
  const closed24=s===1?24:s===2?48:5*s*s+s+24,total=[...terms.values()].reduce((a,b)=>a+b,0);
  const rational24=24*binom2(s+1)-24*binom2(s)+(s>=4?12*binom2(s-2):0)-(s>=5?2*binom2(s-3):0);
  P('univariate_rational_identity',String(s),total,rational24);P('closed_core_coefficient',String(s),total,closed24);
  P('weighted_core_coefficient',String(s),[...terms].reduce((a,[p,c])=>a+p*c,0),12*s*s*(s+1));coreSeries.push({s,terms24:poly(terms),closed24});
 }
 const limits=[];
 for(const [family,first_size]of [['figure_eight_both_long',5],['barbell_both_long',6],['theta_all_nondirect',5]]){const witnesses=[];
  for(const c of carriers)for(const g of c.groups){const d=g.description,ls=d.lengths;
   if((family==='figure_eight_both_long'&&d.family==='figure_eight'&&Math.min(...ls)>=3)||
    (family==='barbell_both_long'&&d.family==='barbell'&&Math.min(...ls.slice(0,2))>=3)||
    (family==='theta_all_nondirect'&&d.family==='theta'&&Math.min(...ls)>=2))witnesses.push([c.n,g.id]);}
  P('finite_coverage_boundary',family,witnesses,[]);limits.push({family,first_size,witnesses,status:'deductive_only'});
 }
 P('total_states','all',carriers.reduce((s,c)=>s+c.states.length,0),4356);
 const failure_ids=checks.filter(c=>!c.passed).map(c=>c.id),names=[...new Set(checks.map(c=>c.name))].sort();
 return {schema:'p212-review-b-v1',role:'nonauthor_process_separated_B',
  method:'inverse_digits_DSU_Pruefer_cotree_contraction_static_anchors_denominator_recurrence',labels:'zero_based_little_endian',carrier_sizes:[1,2,3,4],
  catalogues:[...cats].map(([s,es])=>({s,entries:es.map(e=>({edges:e,description:describe(range(s),e),static_anchors:anchors.get(s).get(plain(e))}))})),
  carriers,series_pieces:FAMILIES.map(f=>({family:f,terms24:entries(pieces.get(f))})),core_series:coreSeries,coverage_limits:limits,predicates:checks,
  predicate_census:names.map(name=>({name,checks:checks.filter(c=>c.name===name).length,failures:checks.filter(c=>c.name===name&&!c.passed).length})),
  summary:{states:4356,orbits:carriers.map(c=>c.orbits.length),predicates:checks.length,failure_ids,passed:!failure_ids.length},
  exclusions:['finite evidence is not an all-n proof','first-size 5/6/5 families are unexecuted','no external review or global novelty certificate','no build or lifecycle completion']};
}

const META=['dev','ino','mode','size','mtimeNs','ctimeNs'];
const STATIC=[
 [P+'/guard.js','d4bb88f451d2c5c5d11ca3b0bb7b033fe81592e71652de97c4609603289a77da'],
 [P+'/PREPARATION_INPUTS.sha256','d48b94d8d5f4be5afc225b4c4d6aa792a70ea06d5e1da0475bb08329bad933af'],
 [P+'/SOURCE_INPUTS.sha256','5cc34231172483209506a5602145973a08f7d335fc4c5346d5b73e4da31e07bf'],
 [P+'/BASELINE_INPUTS.sha256','66840c7d156f419afe45a69bd562bfe7cc19b56f379835a990eeefecc32f683b'],
 [P+'/SHA256SUMS','ea37f3031748b92d5bcfa7e55a2ccd4a8ba04e6c159c74107c27d8aaae85f899'],
 [R+'/SOURCE_RECEPTION.md','255d0d9235303455c204062c35ca183d683997dd0fdd1b72bd3525452883e9ac'],
 [R+'/ADOPTED_SOURCE_INPUTS.sha256','9087ab5414709fd5ad822737faf3320a81355c30cb7f2ab2ca65ed8c84f2b3cd'],
 [B+'/verify.py','3129ed2e32862addc39f90ceb00a9a3862ba0b11a3037da1549ff8d358f2395d'],
 ['docs/papers211_215_sequence/qa/p212_a_source_root01/RUNTIME_INPUTS.json','fd64f171325548a01dc076ceda92685aad6577485334e7622d7a84ee4bc9e22b']
];
function metadata(st){return Object.fromEntries(META.map(k=>[k,String(st[k])]));}
function relative(path){
 const r=path.startsWith(W+'/')?path.slice(W.length+1):path;
 need(!r.startsWith('/')&&/^[A-Za-z0-9_./-]+$/.test(r)&&!r.split('/').some(x=>x==='..'||x==='.'||x===''),'workspace path only');return r;
}
function read(path){
 const r=relative(path),full=W+'/'+r,fd=fs.openSync(full,'r');let bytes,key;
 try{const before=fs.fstatSync(fd,{bigint:true});need(before.isFile(),'regular workspace input '+r);
  bytes=fs.readFileSync(fd);const after=fs.fstatSync(fd,{bigint:true});
  equal(metadata(before),metadata(after),'stable read '+r);equal(metadata(after),metadata(fs.statSync(full,{bigint:true})),'stable path '+r);
  need(BigInt(bytes.length)===after.size,'complete read '+r);
  key={path:r,kind:'regular-file',bytes:bytes.length,sha256:sha(bytes),metadata:metadata(after)};
 }finally{fs.closeSync(fd);}
 if(consumed.has(r))equal(consumed.get(r),key,'repeated current key '+r);else consumed.set(r,key);
 return {bytes,key};
}
function json(path){const result=read(path);return {value:uniqueJson(result.bytes.toString('utf8')),...result};}
function objectKeys(x,keys,label){need(x!==null&&typeof x==='object'&&!Array.isArray(x),label+' object');equal(Object.keys(x).sort(),keys.slice().sort(),label+' exact fields');}
function regularKey(row,label){
 objectKeys(row,['path','kind','bytes','sha256','metadata'],label);
 need(typeof row.path==='string'&&row.kind==='regular-file',label+' path/kind');
 need(Number.isSafeInteger(row.bytes)&&row.bytes>=0,label+' byte count');need(typeof row.sha256==='string'&&/^[0-9a-f]{64}$/.test(row.sha256),label+' hash');
 objectKeys(row.metadata,META,label+' metadata');for(const k of META)need(typeof row.metadata[k]==='string'&&/^\d+$/.test(row.metadata[k]),label+' metadata '+k);
 need(row.metadata.size===String(row.bytes),label+' metadata byte size');
}
function savedKey(row,label){
 if(row.kind==='required-absence'){objectKeys(row,['path','kind','errno'],label);need(typeof row.path==='string'&&row.errno==='ENOENT',label+' absence');}
 else regularKey(row,label);
}
function checkCurrent(row,label){regularKey(row,label);const {key}=read(row.path);equal({...key,path:row.path},row,label+' complete current workspace key');}
function pinRows(path,count,base=''){
 const {bytes}=read(path),txt=bytes.toString('utf8');need(txt.endsWith('\n'),'manifest LF '+path);
 const lines=txt.slice(0,-1).split('\n');need(lines.length===count,'manifest count '+path);
 const rows=lines.map(line=>{need(/^[0-9a-f]{64}  [A-Za-z0-9_./-]+$/.test(line),'manifest syntax '+path);return [relative(base+line.slice(66)),line.slice(0,64)];});
 need(new Set(rows.map(r=>r[0])).size===rows.length,'manifest unique '+path);return rows;
}
function hashRows(rows){for(const [path,hash]of rows)need(read(path).key.sha256===hash,'pinned bytes '+path);}
function nativeResult(x,label){
 need(x!==null&&typeof x==='object'&&!Array.isArray(x),label+' result object');
 const allowed=['chunk_id','exit_code','original_token_count','output','session_id','wall_time_seconds'];
 need(Object.keys(x).every(k=>allowed.includes(k)),label+' result fields');
 need(typeof x.output==='string'&&typeof x.wall_time_seconds==='number'&&Number.isFinite(x.wall_time_seconds)&&x.wall_time_seconds>=0,label+' complete output/time');
 need(typeof x.chunk_id==='string'&&/^[0-9a-f]+$/.test(x.chunk_id),label+' actual chunk');
 if('original_token_count'in x)need(Number.isSafeInteger(x.original_token_count)&&x.original_token_count>=0,label+' token count');
 if('session_id'in x)need(Number.isSafeInteger(x.session_id)&&x.session_id>0,label+' session id');
 if('exit_code'in x)need(Number.isSafeInteger(x.exit_code),label+' exit code');
}
function receiveNative(summary){
 const first=json(R+'/INITIAL_NATIVE.json').value;
 objectKeys(first,['arguments','result'],'initial native wrapper');
 const args=first.arguments;
 need(args!==null&&typeof args==='object'&&!Array.isArray(args),'exec arguments');
 need(Object.keys(args).every(k=>['cmd','workdir','max_output_tokens','yield_time_ms','login','shell','tty'].includes(k)),'exec argument set');
 need(args.cmd==='node '+P+'/guard.js initial01','exact root guard command');
 need(args.workdir===W,'exact root guard cwd');
 if('tty'in args)need(args.tty===false,'no PTY capture');
 if('shell'in args)need(args.shell==='/bin/bash'||args.shell==='bash','declared bash shell');
 if('login'in args)need(typeof args.login==='boolean','login type');
 for(const k of ['yield_time_ms','max_output_tokens'])if(k in args)need(Number.isSafeInteger(args[k])&&args[k]>0,'exec bound '+k);
 nativeResult(first.result,'initial native');let text=first.result.output,terminal=first.result,continuation=null;
 const continuationPath=W+'/'+R+'/INITIAL_CONTINUATION_NATIVE.json';
 if('session_id'in first.result){
  need(!('exit_code'in first.result),'yielded first native has no exit');
  continuation=json(R+'/INITIAL_CONTINUATION_NATIVE.json').value;
  objectKeys(continuation,['arguments','result'],'continuation wrapper');
  const a=continuation.arguments;need(a!==null&&typeof a==='object'&&!Array.isArray(a),'write_stdin arguments');
  need(Object.keys(a).every(k=>['session_id','chars','yield_time_ms','max_output_tokens'].includes(k)),'continuation argument fields');
  need(a.session_id===first.result.session_id,'same actual continued session');
  if('chars'in a)need(a.chars==='','no continuation input');
  for(const k of ['yield_time_ms','max_output_tokens'])if(k in a)need(Number.isSafeInteger(a[k])&&a[k]>0,'continuation '+k);
  nativeResult(continuation.result,'continuation native');need(!('session_id'in continuation.result),'only settled one-continuation interface');
  terminal=continuation.result;text+=terminal.output;
 }else need(!fs.existsSync(continuationPath),'no fabricated unused continuation');
 need(terminal.exit_code===0,'outer guard native success');
 need(text===JSON.stringify(summary)+'\n','complete native guard stdout binding');
 return {initial:first,continuation,joined_output:text};
}
function receiveCapture(){
 need(process.cwd()===W,'DATA cwd');need(process.argv.length===2,'DATA has no application args');
 hashRows(STATIC);
 // The receiver and explanatory package are root-reviewed separately. This
 // nonself source seal is read as data; no script in it is imported or run.
 hashRows(pinRows(D+'/SHA256SUMS',4,D+'/'));
 hashRows(pinRows(D+'/INPUT_PINS.sha256',18));
 const listing=fs.readdirSync(W+'/'+RUN).sort();
 equal(listing,['EXIT.json','POST.json','PRE.json','RECEIPT.json','REQUEST.json','stderr.raw','stdout.raw'].sort(),'exact first-run inventory');
 const req=json(RUN+'/REQUEST.json').value,preRaw=read(RUN+'/PRE.json').bytes,postRaw=read(RUN+'/POST.json').bytes;
 objectKeys(req,['grant_path','grant_key','grant','command','run_id','run_directory','guard_key','preparation_manifest_key'],'request');
 need(req.grant_path===R+'/GRANT.initial01.json'&&req.run_id==='initial01'&&req.run_directory===W+'/'+RUN,'request run identity');
 checkCurrent(req.grant_key,'request grant key');need(req.grant_key.path===req.grant_path,'grant path binding');
 checkCurrent(req.guard_key,'guard key');need(req.guard_key.path===P+'/guard.js'&&req.guard_key.sha256===STATIC[0][1],'guard binding');
 checkCurrent(req.preparation_manifest_key,'preparation key');need(req.preparation_manifest_key.path===P+'/PREPARATION_INPUTS.sha256'&&req.preparation_manifest_key.sha256===STATIC[1][1],'preparation binding');
 const grant=json(req.grant_path).value;
 equal(req.grant,grant,'whole actual grant');
 const grantFields=['schema','authority','action','run_id','run_directory','guard_sha256','preparation_manifest_sha256','source_manifest_sha256','source_reception_sha256','adopted_source_manifest_sha256','runtime_manifest_sha256','runtime_policy_sha256','guard_source_reception_sha256','command'];
 objectKeys(grant,grantFields,'grant');
 equal([grant.schema,grant.authority,grant.action,grant.run_id,grant.run_directory],['P212_B_ONE_RUN_GRANT_V1','root','execute_once','initial01',W+'/'+RUN],'grant authority/action');
 const command={executable:'/usr/bin/python3.10',args:['-I','-S','-B',W+'/'+B+'/verify.py'],cwd:W,env:{LANG:'C',LC_ALL:'C'},stdin:'/dev/null',timeout_ms:600000};
 equal(req.command,command,'request scientific command');equal(grant.command,command,'grant scientific command');
 need(JSON.stringify(req.command)===JSON.stringify(command)&&JSON.stringify(grant.command)===JSON.stringify(command),'command exact key/env order');
 equal([grant.guard_sha256,grant.preparation_manifest_sha256,grant.source_manifest_sha256,grant.source_reception_sha256,grant.adopted_source_manifest_sha256],
       [STATIC[0][1],STATIC[1][1],STATIC[2][1],STATIC[5][1],STATIC[6][1]],'fixed grant source pins');
 const expected=new Map();
 function add(path,hash){need(/^[0-9a-f]{64}$/.test(hash),'declared hash');need(!expected.has(path)||expected.get(path)===hash,'compatible duplicate pin');expected.set(path,hash);}
 const rootBindings=[[R+'/RUNTIME_INPUTS.json',grant.runtime_manifest_sha256],[R+'/ORDINARY_RUNTIME_POLICY.md',grant.runtime_policy_sha256],
  [R+'/GUARD_SOURCE_RECEPTION.md',grant.guard_source_reception_sha256],[R+'/SOURCE_RECEPTION.md',grant.source_reception_sha256],[R+'/ADOPTED_SOURCE_INPUTS.sha256',grant.adopted_source_manifest_sha256]];
 const staticFixed=[STATIC[2],STATIC[3],STATIC[8]];
 for(const row of [...rootBindings,...staticFixed])add(...row);
 add(P+'/PREPARATION_INPUTS.sha256',req.preparation_manifest_key.sha256);add(req.grant_path,req.grant_key.sha256);
 hashRows([...expected]);
 for(const [path,count]of [[P+'/SOURCE_INPUTS.sha256',3],[R+'/ADOPTED_SOURCE_INPUTS.sha256',12],[B+'/INPUT_PINS.sha256',32],[P+'/BASELINE_INPUTS.sha256',10],[P+'/PREPARATION_INPUTS.sha256',7]]){
  need(expected.has(path),'manifest already pinned '+path);need(read(path).key.sha256===expected.get(path),'manifest before expansion '+path);
  for(const row of pinRows(path,count))add(...row);
 }
 hashRows(pinRows(P+'/SHA256SUMS',8,P+'/'));
 const runtime=json(R+'/RUNTIME_INPUTS.json').value,baseline=json(STATIC[8][0]).value;
 objectKeys(runtime,['status','ordinary_trust_only','origin','roles','historical_metadata_changes'],'current root runtime declaration');
 equal([runtime.status,runtime.ordinary_trust_only,runtime.origin],['CURRENT_SELECTED_RUNTIME_PREFLIGHT_PASS',true,STATIC[8][0]],'current runtime scope/origin');
 objectKeys(baseline,['status','ordinary_trust_only','origin','roles'],'archived runtime declaration');
 equal([baseline.status,baseline.ordinary_trust_only,baseline.origin],['CURRENT_SELECTED_RUNTIME_PREFLIGHT_PASS',true,'docs/papers211_215_sequence/qa/p213_a_execution_preparation01/DEPENDENCIES.proposed.json'],'archived runtime scope/origin');
 need(Array.isArray(runtime.roles)&&runtime.roles.length===19,'nineteen selected runtime roles');
 need(Array.isArray(baseline.roles)&&baseline.roles.length===19,'nineteen archived candidate roles');
 need(new Set(runtime.roles.map(r=>r.path)).size===19,'unique runtime roles');
 need(runtime.roles.filter(r=>r.kind==='regular-file').length===18,'eighteen runtime regular files');
 function content(row){savedKey(row,'runtime role');return row.kind==='required-absence'?{path:row.path,kind:row.kind,errno:row.errno}:{path:row.path,kind:row.kind,bytes:row.bytes,sha256:row.sha256};}
 equal(runtime.roles.map(content),baseline.roles.map(content),'whole ordered runtime content candidate');
 const bindingDrift=[];
 for(let i=0;i<19;i++)if(runtime.roles[i].metadata&&JSON.stringify(runtime.roles[i].metadata)!==JSON.stringify(baseline.roles[i].metadata))
  bindingDrift.push({path:runtime.roles[i].path,historical:baseline.roles[i].metadata,current:runtime.roles[i].metadata});
 equal(runtime.historical_metadata_changes,bindingDrift,'root full historical runtime metadata drift');
 need(runtime.roles.some(r=>r.path==='/usr/lib/python310.zip'&&r.kind==='required-absence'&&r.errno==='ENOENT'),'specified zip absence role');
 need(preRaw.equals(postRaw),'whole PRE/POST raw bytes equal');
 const pre=uniqueJson(preRaw.toString('utf8')),post=uniqueJson(postRaw.toString('utf8'));
 need(preRaw.toString('utf8')===JSON.stringify(pre,null,2)+'\n','PRE full capture encoding');
 for(const name of ['REQUEST.json','EXIT.json','RECEIPT.json']){const r=json(RUN+'/'+name);need(r.bytes.toString('utf8')===JSON.stringify(r.value,null,2)+'\n','capture JSON encoding '+name);}
 for(const [label,obj]of [['PRE',pre],['POST',post]]){objectKeys(obj,['schema','keys','errors','runtime_baseline_metadata_changes'],label);
  need(obj.schema==='P212_B_KEYS_V1','snapshot schema');equal(obj.errors,[],label+' no errors');need(Array.isArray(obj.keys),'snapshot keys array');
 }
 equal(pre,post,'complete PRE/POST values');
 const contentInputs=[...expected].sort((a,b)=>a[0].localeCompare(b[0],'en'));
 need(pre.keys.length===contentInputs.length+19,'complete selected input census');
 for(let i=0;i<contentInputs.length;i++){
  const [path,hash]=contentInputs[i],row=pre.keys[i];regularKey(row,'workspace sample '+i);
  need(row.path===path&&row.sha256===hash,'ordered content pin '+i);checkCurrent(row,'complete workspace sample '+i);
 }
 const drift=[];
 for(let i=0;i<19;i++){const historical=runtime.roles[i],row=pre.keys[contentInputs.length+i];savedKey(row,'saved runtime sample '+i);
  equal(content(row),content(historical),'saved runtime content '+i);
  if(historical.metadata&&JSON.stringify(row.metadata)!==JSON.stringify(historical.metadata))drift.push({path:row.path,historical:historical.metadata,current:row.metadata});
 }
 equal(pre.runtime_baseline_metadata_changes,drift,'complete historical metadata drift disclosure');
 const exit=json(RUN+'/EXIT.json').value;
 objectKeys(exit,['status','signal','error','pid','science_submitted'],'child exit');
 equal([exit.status,exit.signal,exit.error,exit.science_submitted],[0,null,null,true],'child clean zero submission');need(Number.isSafeInteger(exit.pid)&&exit.pid>0,'actual child pid');
 const receipt=json(RUN+'/RECEIPT.json').value;
 objectKeys(receipt,['schema','run_id','ordinary_runtime_only','pre_post_equal','exit','stdout','stderr','execution_completed_zero','semantic_reception','canonical_adoption'],'capture receipt');
 equal([receipt.schema,receipt.run_id,receipt.ordinary_runtime_only,receipt.pre_post_equal,receipt.execution_completed_zero,receipt.semantic_reception,receipt.canonical_adoption],
  ['P212_B_CAPTURE_V1','initial01',true,true,true,'NOT_PERFORMED','NOT_AUTHORIZED'],'capture scope/status');equal(receipt.exit,exit,'whole exit in receipt');
 checkCurrent(receipt.stdout,'stdout key');checkCurrent(receipt.stderr,'stderr key');
 need(receipt.stdout.path===W+'/'+RUN+'/stdout.raw'&&receipt.stderr.path===W+'/'+RUN+'/stderr.raw','raw stream locations');
 const raw=read(RUN+'/stdout.raw').bytes,err=read(RUN+'/stderr.raw').bytes;
 need(err.length===0,'empty scientific stderr');need(raw.length>1,'nonempty scientific stdout');
 const native=receiveNative({status:'CAPTURED_ZERO_EXIT_NOT_SEMANTIC_PASS',run_directory:W+'/'+RUN,stdout_sha256:sha(raw),stdout_bytes:raw.length});
 return {raw,pre,receipt,native,expected_workspace_inputs:contentInputs.length,runtime_roles:19};
}
function main(){
 const capture=receiveCapture(),raw=capture.raw;
 need([...raw].every(b=>b<128),'raw scientific ASCII');need(raw.at(-1)===10,'scientific final LF');
 const body=raw.subarray(0,-1).toString('ascii'),data=uniqueJson(body);
 need(wire(data)===body,'canonical full wire including duplicate/type/whitespace rejection');
 const expected=reconstructScience();equal(data,expected,'entire reconstructed scientific output');
 need(Buffer.from(wire(expected)+'\n','ascii').equals(raw),'entire reconstructed raw scientific stream');
 need(data.summary.passed===true&&data.summary.failure_ids.length===0,'all scientific predicates passed');
 need(data.predicate_census.length===27,'all twenty-seven predicate names');
 // Re-read only consumed workspace files. Runtime host roles are never followed.
 const paths=[...consumed.keys()];for(const path of paths)read(path);
 const report={schema:'P212_B_INITIAL_DATA_RECEPTION_V1',status:'PASS_COMPLETE_SAVED_DATA',run_directory:RUN,
  stdout:{bytes:raw.length,sha256:sha(raw)},stderr_bytes:0,scientific_summary:data.summary,predicate_census:data.predicate_census,
  field_census:{top_level:Object.keys(data).sort(),carriers:data.carriers.map(c=>({n:c.n,states:c.states.length,orbits:c.orbits.length,groups:c.groups.length,
    actual_anchors:c.groups.reduce((s,g)=>s+g.actual_anchors.length,0),expected_anchors:c.groups.reduce((s,g)=>s+g.expected_anchors.length,0),fixed_iterates:c.fixed_iterates.length})),
    catalogues:data.catalogues.map(c=>({s:c.s,cores:c.entries.length,static_anchors:c.entries.reduce((s,e)=>s+e.static_anchors.length,0)})),
    core_series:data.core_series,coverage_limits:data.coverage_limits},
  capture_scope:{ordinary_runtime_only:true,workspace_prepost_keys:capture.expected_workspace_inputs,runtime_roles:capture.runtime_roles,
    whole_prepost_raw_equal:true,full_native_sequence_received:true,current_workspace_inputs:consumed.size,host_paths_reopened:false},
  assertions,inputs:[...consumed.values()].sort((a,b)=>cmp(a.path,b.path)),
  exclusions:['DATA reconstruction is not another producer or manuscript reviewer','no new host/runtime discovery',
   'first-size 5/6/5 remains deductive-only','canonical adoption and strict pair remain separately authorized','no build/page/final-review completion']};
 process.stdout.write(JSON.stringify(report,null,2)+'\n');
}
try{main();}catch(error){process.stderr.write('P212 B DATA rejection: '+String(error.stack||error)+'\n');process.exitCode=1;}
