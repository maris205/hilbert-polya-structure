'use strict';
// Saved-DATA semantic checker SOURCE. Never loads/runs a scientific producer.
const fs = require('node:fs');
const crypto = require('node:crypto');
let assertions = 0;
const ledger = [];
function stable(x) {
  if (Array.isArray(x)) return '[' + x.map(stable).join(',') + ']';
  if (x && typeof x === 'object') return '{' + Object.keys(x).sort().map(k => JSON.stringify(k)+':'+stable(x[k])).join(',') + '}';
  if (typeof x === 'number' && !Number.isSafeInteger(x)) throw Error('noninteger data');
  return JSON.stringify(x);
}
function need(x, label) { assertions++; if (!x) throw Error(label); }
function eq(a, b, label) { need(stable(a) === stable(b), label); }
function shape(x, keys, label) { need(x && !Array.isArray(x) && typeof x === 'object',label); eq(Object.keys(x).sort(),keys.split(' ').sort(),label+' fields'); }
function tuple(x, size, label) { need(Array.isArray(x) && x.length === size,label+' arity'); }
function cmp(a,b) {
  if (Array.isArray(a) && Array.isArray(b)) {
    for(let i=0;i<Math.min(a.length,b.length);i++) { const c=cmp(a[i],b[i]); if(c) return c; }
    return a.length-b.length;
  }
  return a < b ? -1 : a > b ? 1 : 0;
}
const sorted = xs => [...xs].sort(cmp);
const unique = xs => sorted([...new Map(xs.map(x=>[stable(x),x])).values()]);
const range = n => Array.from({length:n},(_,i)=>i);
const sum = xs => xs.reduce((a,b)=>a+b,0);
const fact = n => n<2 ? 1 : n*fact(n-1);
const edge = (a,b) => a<b ? [a,b] : [b,a];
const edges = w => sorted([edge(w[0],w[1]),...w.slice(2).map((v,u)=>edge(u,v))]);
const degree = (es,x) => sum(es.map(([a,b])=>Number(a===x)+Number(b===x)));
function digits(n,len,k) { return range(len).map(()=>{const x=k%n;k=Math.floor(k/n);return x;}); }
function rank(n,w) { return sum(w.map((x,j)=>x*n**j)); }
function literal(w) { const f=w.slice(2),u=w[0],v=w[1],next=f[v];f[v]=u;return [v,next,...f]; }
function inverse(w) { const f=w.slice(2),v=w[0],u=f[v];f[v]=w[1];return [u,v,...f]; }
function add(map,k,v=1) { map.set(k,(map.get(k)||0)+v); }
function polynomial(map) { return [...map].filter(([,v])=>v).sort((a,b)=>a[0]-b[0]); }
function rotateMin(word) { return sorted(word.map((_,i)=>word.slice(i).concat(word.slice(0,i))))[0]; }
function primitive(word) {
  for(let d=1;d<=word.length;d++) if(word.length%d===0 && word.every((x,i)=>x===word[i%d])) return rotateMin(word.slice(0,d));
  throw Error('empty visit word');
}
function reconstruct(visit,t,n,frozen=[]) {
  const f=Array(n).fill(null);for(const [x,y] of frozen)f[x]=y;
  for(const x of new Set(visit)) for(let age=0;age<visit.length;age++) {
    const j=(t-age+visit.length)%visit.length;
    if(visit[j]===x){f[x]=visit[(j-1+visit.length)%visit.length];break;}
  }
  need(f.every(x=>x!==null),'last-arrival covers all labels');
  return [visit[t],visit[(t+1)%visit.length],...f];
}
function record(name,scope,observed,expected) {
  const passed=stable(observed)===stable(expected);
  ledger.push([name,scope,observed,expected,passed]);need(passed,'rebuilt predicate '+name);
}
function structure(w) {
  const n=w.length-2,es=edges(w),active=new Set([w[0]]);
  for(let changed=true;changed;){changed=false;for(const [a,b] of es)if(active.has(a)||active.has(b))for(const x of [a,b])if(!active.has(x)){active.add(x);changed=true;}}
  const core=new Set(active);
  for(let changed=true;changed;){changed=false;const ce=es.filter(([a,b])=>core.has(a)&&core.has(b));for(const x of [...core])if(degree(ce,x)<2){core.delete(x);changed=true;}}
  const labels=sorted([...core]),ce=es.filter(([a,b])=>core.has(a)&&core.has(b));
  const frozen=range(n).filter(x=>!core.has(x)).map(x=>[x,w[x+2]]);
  const activeMask=sum([...active].map(x=>2**x)),admissible=[];
  for(let mask=0;mask<2**n;mask++)if((mask&activeMask)===mask){const vs=range(n).filter(x=>mask&(1<<x)),sub=es.filter(([a,b])=>(mask&(1<<a))&&(mask&(1<<b)));if(vs.every(x=>degree(sub,x)>=2))admissible.push(mask);}
  eq(admissible.reduce((a,b)=>a|b,0),sum(labels.map(x=>2**x)),'pruning/max-induced core agreement');
  return {key:[labels,ce,frozen],activeMask,admissible,activeEdges:es.filter(([a,b])=>active.has(a)&&active.has(b))};
}
function allCoreGraphs(s) {
  const types=[];for(let a=0;a<s;a++)for(let b=a;b<s;b++)types.push([a,b]);
  const result=[];
  function pick(start,left,chosen) {
    if(!left){if(!range(s).every(x=>degree(chosen,x)>=2))return;
      const seen=new Set([0]);for(let change=true;change;){change=false;for(const [a,b]of chosen)if(seen.has(a)||seen.has(b))for(const x of[a,b])if(!seen.has(x)){seen.add(x);change=true;}}
      if(seen.size===s)result.push(chosen);return;
    }
    for(let k=start;k<types.length;k++)pick(k,left-1,[...chosen,types[k]]);
  }
  pick(0,s+1,[]);return sorted(result);
}
function table(family,l) {
  const [a,b,c]=l;
  if(family===0){if(a===1&&b===1)return[0,1,1];if(Math.max(a,b)<=2)return[1,a+b,1];return[2,2*(a+b),Math.min(a,b)>=3?2:1];}
  if(family===1)return[Math.max(a,b)<=2?3:4,(a+b+2*c)*(Math.max(a,b)<=2?1:2),Math.min(a,b)>=3?2:1];
  const d=l.filter(x=>x===1).length;return d===3?[5,2,1]:[6,2*sum(l),d>=2?1:2];
}
function pathAudit(s,e) {
  const branches=range(s).filter(x=>degree(e.edges,x)>2),all=[];
  need(e.family===0||e.family===1||e.family===2,'family domain');
  eq(e.paths.length,e.family===0?2:3,'path count');
  for(const p of e.paths){need(p.length>=2&&p.every(x=>Number.isInteger(x)&&x>=0&&x<s),'path labels');
    for(let i=1;i<p.length;i++)all.push(edge(p[i-1],p[i]));}
  eq(sorted(all),e.edges,'path edge cover');eq(e.lengths,e.paths.map(p=>p.length-1),'length fields');
  const internal=e.paths.flatMap(p=>p.slice(1,-1));
  eq(sorted(internal),range(s).filter(x=>!branches.includes(x)),'disjoint exhaustive internal labels');
  if(e.family===0){eq(branches.length,1,'figure-eight branch');for(const p of e.paths){eq([p[0],p.at(-1)],[branches[0],branches[0]],'cycle endpoints');eq(p,sorted([p,[...p].reverse()])[0],'cycle reversal representative');}eq(e.paths,sorted(e.paths),'cycle pair order');}
  else {eq(branches.length,2,'two branches');const[a,b]=branches;
    if(e.family===1){eq(e.paths.map(p=>[p[0],p.at(-1)]),[[a,a],[b,b],[a,b]],'barbell path roles');for(const p of e.paths.slice(0,2))eq(p,sorted([p,[...p].reverse()])[0],'barbell reversal representative');}
    else {for(const p of e.paths)eq([p[0],p.at(-1)],[a,b],'theta endpoints');eq(e.paths,sorted(e.paths),'theta path order');}
  }
  eq([e.row,e.period,e.decorations],table(e.family,e.lengths),'seven-row fields');
}
// Independent expansion of the displayed rational EGF, truncated only at t^4.
function coefficient24(s) {
  const pieces=[new Map(),new Map(),new Map()];
  const put=(f,p,v)=>add(pieces[f],p,v);
  if(s===1)put(0,1,24);if(s===2)put(0,3,24);if(s===3)put(0,4,12);
  const d=k=>k<2?0:k===2?2:k+1;
  if(s>=3)put(0,2*s+2,6*d(s-1));
  for(let j=0;j<=2;j++){const bridge=s-2-j;if(bridge>=0)put(1,4+j+2*bridge,12*[1,2,1][j]);}
  for(let k=2;k<=s-2;k++){const bridge=s-2-k;put(1,8+2*k+4*bridge,6*d(k));}
  if(s===2)put(2,2,12);
  const m=s-2;if(m>=1)put(2,2*s+2,12);
  if(m>=2)put(2,2*s+2,12*(m-1));
  if(m>=3)put(2,2*s+2,4*(m-1)*(m-2)/2);
  return pieces;
}

try {
  need(process.argv.length===2,'usage: node check.js (zero script arguments)');
  const path='/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p212_a_runs/initial02/stdout.raw';
  const expectedHash='24d6054e4a29411948becfa256d2182301b3f73d3ef78df1cad9088ed8b9922b';
  const expectedBytes=3004047;
  const meta=x=>['dev','ino','mode','size','mtimeNs','ctimeNs'].map(k=>String(x[k]));
  const pre=fs.statSync(path,{bigint:true});need(pre.isFile(),'raw not regular');
  const raw=fs.readFileSync(path);const rawHash=crypto.createHash('sha256').update(raw).digest('hex');
  eq(rawHash,expectedHash,'raw SHA256');eq(raw.length,Number(expectedBytes),'raw bytes');
  const d=JSON.parse(raw.toString('utf8'));
  eq(raw.toString('utf8'),stable(d)+'\n','complete canonical ASCII JSON encoding');
  shape(d,'schema role parameters method catalogues coefficients_scaled24 carriers checks check_census failure_ids finite_passed limits','top');
  const params={schema:'P212_A_PARAMETERS_V1',carrier_sizes:[1,2,3,4],label_base:0,state_order:'little_endian_base_n_u_v_f0_through_f_n_minus_1',core_sizes:[1,2,3,4],coefficient_scale:24,unexercised_first_sizes:[5,6,5],imports:[],data_inputs:[]};
  eq(d.parameters,params,'all fixed parameters');eq(d.schema,'P212_A_FULL_OUTPUT_V1','schema');
  eq(d.role,'independent_review_A_finite_checks_only','role');
  eq(d.method,'two_slot_swaps_vs_visit_word_last_arrival_and_incidence_quotient','method');
  eq(d.limits,['no_all_size_proof_from_finite_checks','no_first_size_5_6_5_execution','no_external_certification','no_final_manuscript_or_build_verdict'],'limits');
  eq(d.carriers.length,4,'carrier count');eq(d.catalogues.length,4,'catalogue size count');
  for(let n=1;n<=4;n++){
    const c=d.carriers[n-1];shape(c,'n states orbits groups row_counts period_counts extension_terms_scaled24 unexercised_group_ids','carrier');eq(c.n,n,'carrier n');eq(c.states.length,n**(n+2),'complete state count');
    c.states.forEach((r,i)=>{tuple(r,8,'state row');eq(r[0],i,'state id');eq(r[1],digits(n,n+2,i),'all state words/ranks');});
  }
  const catalogues={};
  for(let s=1;s<=4;s++){
    tuple(d.catalogues[s-1],2,'catalogue size row');const [savedSize,entries]=d.catalogues[s-1];eq(savedSize,s,'catalogue s');
    eq(entries.map(e=>e.edges),allCoreGraphs(s),'complete multigraph catalogue');catalogues[s]=entries;
    const c=d.carriers[s-1];
    entries.forEach((e,id)=>{
      shape(e,'id edges family paths lengths row period decorations visit_words incidence_states','catalogue entry');eq(e.id,id,'catalogue id');pathAudit(s,e);
      const incidence=c.states.map(r=>r[1]).filter(w=>stable(edges(w))===stable(e.edges));
      const multiplicities=new Map();for(const ed of e.edges)add(multiplicities,stable(ed));
      const multiplicity=[...multiplicities.values()].reduce((a,b)=>a*fact(b),1);
      eq(e.incidence_states,sorted(incidence).map(w=>[w,multiplicity]),'full incidence states and occurrence multiplicities');
      eq(e.visit_words,unique(e.visit_words),'visit-word ordering/deduplication');
      const wordStates=[];
      for(const visit of e.visit_words){need(Array.isArray(visit)&&visit.length>0,'visit array');eq(visit,primitive(visit),'primitive necklace');eq(unique(visit),range(s),'visit covers core');
        const orbit=visit.map((_,t)=>reconstruct(visit,t,s));
        record('word_primitive_state_period',[s,id],unique(orbit).length,visit.length);
        record('word_swap_successors',[s,id],orbit.map(literal),orbit.slice(1).concat([orbit[0]]));
        record('word_exact_edges',[s,id],unique(orbit.map(edges)),[e.edges]);wordStates.push(...orbit);
      }
      record('word_incidence_exhaustion',[s,id],sorted(wordStates),sorted(incidence));
      record('word_decoration_count',[s,id],e.visit_words.length,e.decorations);
      record('word_period_table',[s,id],e.visit_words.map(w=>w.length),Array(e.decorations).fill(e.period));
    });
  }
  const coefficients=[];
  for(let s=1;s<=4;s++){
    const obs=[new Map(),new Map(),new Map()];for(const e of catalogues[s])for(const visit of e.visit_words)add(obs[e.family],visit.length,24);
    const pieces=coefficient24(s);
    for(let f=0;f<3;f++)record('labelled_core_series_scaled24',[s,f],polynomial(obs[f]),polynomial(new Map([...pieces[f]].map(([p,v])=>[p,fact(s)*v]))));
    const total=sum(pieces.map(x=>sum([...x.values()]))),weighted=sum(pieces.map(x=>sum([...x].map(([p,v])=>p*v))));
    record('closed_core_coefficient_scaled24',s,total,s===1?24:s===2?48:5*s*s+s+24);
    record('weighted_core_coefficient_scaled24',s,weighted,12*s*s*(s+1));
    coefficients.push([s,pieces.map(polynomial),total,weighted]);
  }
  eq(d.coefficients_scaled24,coefficients,'all coefficient rows');
  for(let n=1;n<=4;n++){
    const c=d.carriers[n-1],states=c.states.map(r=>r[1]),arrows=states.map(w=>rank(n,literal(w))),back=states.map(w=>rank(n,inverse(w)));
    const structures=states.map(structure),keys=unique(structures.map(x=>x.key));
    const keyId=new Map(keys.map((k,i)=>[stable(k),i]));
    const expectedGroups=[];
    for(let mask=1;mask<2**n;mask++){
      const labels=range(n).filter(x=>mask&(1<<x)),outside=range(n).filter(x=>!(mask&(1<<x)));
      for(const e of catalogues[labels.length])for(let code=0;code<n**outside.length;code++){
        const targets=digits(n,outside.length,code),frozen=outside.map((x,i)=>[x,targets[i]]);
        expectedGroups.push({key:[labels,sorted(e.edges.map(([a,b])=>edge(labels[a],labels[b]))),frozen],entry:e});
      }
    }
    expectedGroups.sort((a,b)=>cmp(a.key,b.key));
    eq(unique(expectedGroups.map(x=>x.key)).length,expectedGroups.length,'expected group uniqueness');
    record('complete_core_complement_groups',n,keys,expectedGroups.map(x=>x.key));
    const orbitFor=Array(states.length).fill(-1);
    c.orbits.forEach((route,j)=>{need(Array.isArray(route)&&route.length>0,'orbit route');eq(unique(route).length,route.length,'no repeat before closing');
      eq(route[0],orbitFor.indexOf(-1),'smallest new seed order');
      for(let t=0;t<route.length;t++){const id=route[t];need(Number.isInteger(id)&&id>=0&&id<states.length,'orbit state range');eq(orbitFor[id],-1,'no overlapping orbits');eq(arrows[id],route[(t+1)%route.length],'each literal saved orbit arrow');orbitFor[id]=j;}
      record('first_repetition_is_seed',[n,j],arrows[route.at(-1)],route[0]);
    });
    record('orbit_partition',n,sorted(c.orbits.flat()),range(states.length));
    const incoming=states.map(()=>[]);arrows.forEach((to,i)=>incoming[to].push(i));
    const members=keys.map(()=>[]);
    states.forEach((w,i)=>{
      const st=structures[i],key=st.key,[labels,ce]=key,gid=keyId.get(stable(key));members[gid].push(i);
      eq(c.states[i],[i,w,arrows[i],back[i],gid,orbitFor[i],st.activeMask,st.admissible],'complete state record');
      record('unit_predecessor',[n,i],incoming[i],[back[i]]);
      record('inverse_both_directions',[n,i],[arrows[back[i]],back[arrows[i]]],[i,i]);
      record('full_augmented_edges',[n,i],edges(states[arrows[i]]),edges(w));
      record('frozen_core_key',[n,i],structures[arrows[i]].key,key);
      record('register_membership',[n,i],[labels.includes(w[0]),labels.includes(w[1])],[true,true]);
      record('active_excess',[n,i],st.activeEdges.length,range(n).filter(x=>st.activeMask&(1<<x)).length+1);
      record('core_excess_and_degrees',[n,i],[ce.length===labels.length+1,labels.every(x=>degree(ce,x)>=2)],[true,true]);
    });
    const rowCounts=range(7).map(()=>[0,0,0]),groups=[],limits=[[],[],[]];
    keys.forEach((key,gid)=>{
      const [labels,,frozen]=key,e=expectedGroups[gid].entry;
      const predicted=sorted(e.visit_words.map(v=>{const visit=v.map(x=>labels[x]);return rotateMin(visit.map((_,t)=>rank(n,reconstruct(visit,t,n,frozen))));}));
      const ids=unique(members[gid].map(i=>orbitFor[i]));
      const actual=sorted(ids.map(j=>rotateMin(c.orbits[j])));
      record('complete_decorated_orbit_partition',[n,gid],actual,predicted);
      record('exact_periods_for_group',[n,gid],ids.map(j=>c.orbits[j].length),Array(e.decorations).fill(e.period));
      rowCounts[e.row][0]++;rowCounts[e.row][1]+=ids.length;rowCounts[e.row][2]+=members[gid].length;
      groups.push([gid,key,labels.length,e.id,ids,predicted]);
      if(e.family===0&&Math.min(...e.lengths)>=3)limits[0].push(gid);
      if(e.family===1&&Math.min(...e.lengths.slice(0,2))>=3)limits[1].push(gid);
      if(e.family===2&&Math.min(...e.lengths)>=2)limits[2].push(gid);
      if(labels.length===n){const actualVisits=unique(ids.map(j=>primitive(c.orbits[j].map(i=>states[i][0]))));eq(actualVisits,e.visit_words,'catalogue visits from saved actual complete-core orbits');}
    });
    eq(c.groups,groups,'complete group records');eq(c.row_counts,rowCounts,'seven row census');eq(c.unexercised_group_ids,limits,'unexercised fields');
    const counts=new Map();for(const route of c.orbits)add(counts,route.length);eq(c.period_counts,polynomial(counts),'period count fields');
    const predicted24=new Map(),extensions=[];
    for(let s=1;s<=n;s++){const multiplier=fact(n)/fact(n-s)*n**(n-s),core=new Map();for(const piece of coefficient24(s))for(const[p,v]of piece){add(core,p,v);add(predicted24,p,multiplier*v);}extensions.push([s,multiplier,polynomial(core)]);}
    eq(c.extension_terms_scaled24,extensions,'all extension terms');
    record('full_period_census_scaled24',n,polynomial(new Map([...counts].map(([p,v])=>[p,24*v]))),polynomial(predicted24));
    const periods=n===1?[1]:range(2*n).map(x=>x+1).concat(range(Math.max(0,n-2)).map(x=>2*n+2+2*x));
    record('attained_period_set',n,sorted([...counts.keys()]),periods);
    record('sharp_maximum',n,Math.max(...counts.keys()),n===1?1:4*n-4);
    record('fixed_states',n,arrows.filter((x,i)=>x===i).length,n**n);
    record('weighted_full_mass',n,sum([...counts].map(([p,v])=>p*v)),n**(n+2));
    record('seven_row_presence',n,rowCounts.map(r=>r[0]>0),[1,2,3,2,4,2,3].map(first=>n>=first));
    record('unexercised_first_size_families',n,limits,[[],[],[]]);
  }
  record('complete_fixed_carrier_total','all',sum(d.carriers.map(c=>c.states.length)),4356);
  eq(d.checks,ledger,'every complete ledger row and exact order');
  const names=sorted([...new Set(ledger.map(r=>r[0]))]);
  eq(d.check_census,names.map(name=>[name,ledger.filter(r=>r[0]===name).length,ledger.filter(r=>r[0]===name&&!r[4]).length]),'complete check census');
  eq(d.failure_ids,ledger.flatMap((r,i)=>r[4]?[]:[i]),'failure ids');eq(d.finite_passed,d.failure_ids.length===0,'finite passed definition');eq(d.finite_passed,true,'all finite predicates true');
  const after=fs.readFileSync(path);eq(after.equals(raw),true,'whole raw bytes unchanged after DATA audit');eq(meta(fs.statSync(path,{bigint:true})),meta(pre),'raw input metadata unchanged');
  console.log(JSON.stringify({schema:'P212_A_SAVED_DATA_RECEPTION_V1',status:'COMPLETE_SAVED_DATA_SEMANTIC_PASS',input:{path,sha256:rawHash,bytes:raw.length},assertions,ledger_rows:ledger.length,check_classes:names.length,carriers:d.carriers.map(c=>({n:c.n,states:c.states.length,orbits:c.orbits.length,groups:c.groups.length})),source_producer_executed:false,canonical_adoption:false,all_parameter_proof_from_data:false}));
} catch(error) {console.log(JSON.stringify({schema:'P212_A_SAVED_DATA_RECEPTION_V1',status:'FAIL',assertions,error:error.message,source_producer_executed:false,canonical_adoption:false}));process.exitCode=1;}
