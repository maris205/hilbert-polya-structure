'use strict';
// Independent captured-record checker. No generated carrier, new trajectory,
// source import/evaluation, external target lookup, or scientific execution.
module.exports = function checkScience(raw) {
 let checks=0, asserted=0; const ok=(b,s)=>{checks++;if(!b)throw Error('SCIENCE_DATA: '+s);};
 const eq=(a,b,s)=>ok(JSON.stringify(a)===JSON.stringify(b),s);
 const A=(b,s)=>{asserted++;ok(b,s);};
 const statuses=['ACCEPTED','PARITY','NEGATIVE_DESCENT','NONSTRICT_DESCENT','SHORT_PEAK','ASCENT_EQUALITY','ASCENT_ORDER','EMPTY_INTERVAL'];
 const shapes=['R1','R2','RGE3','WRAP'];
 const zeros=a=>Object.fromEntries(a.map(k=>[k,0]));
 const sum=a=>a.reduce((x,y)=>x+y,0), key=a=>a.join(','), lex=(a,b)=>{for(let i=0;i<a.length;i++){if(a[i]!==b[i])return a[i]-b[i];}return 0;};
 const integer=s=>{ok(/^(0|[1-9][0-9]*)$/.test(s),'canonical nonnegative integer');const n=Number(s);ok(Number.isSafeInteger(n),'bounded exact integer');return n;};
 const signed=s=>{ok(/^(0|-?[1-9][0-9]*)$/.test(s),'canonical signed integer');const n=Number(s);ok(Number.isSafeInteger(n),'bounded signed integer');return n;};
 const state=(s,n,N)=>{const a=s.split(',').map(integer);ok(a.length===n&&sum(a)===N,'captured state carrier membership');return a;};
 const list=(s,n,N)=>{if(s==='-')return [];const a=s.split(';').map(x=>state(x,n,N));for(let i=1;i<a.length;i++)ok(lex(a[i-1],a[i])<0,'strictly ordered distinct sources');return a;};
 const tuples=s=>s==='-'?[]:s.split(';').map(t=>{const a=t.split(',').map(signed);ok(a.length===5,'five interval entries');return a;});
 const census=(s,order)=>{const a=s.split(',');ok(a.length===order.length,'complete census');return Object.fromEntries(a.map((t,i)=>{const z=t.split(':');ok(z.length===2&&z[0]===order[i],'ordered census keys');return [z[0],integer(z[1])];}));};
 const fields=(line,tag,names)=>{const t=line.split(' ');ok(t.length===names.length+1&&t[0]===tag,'ordered '+tag+' grammar');const d={};names.forEach((name,i)=>{const z=t[i+1].split('=');ok(z.length===2&&z[0]===name&&z[1].length>0,'exact field '+tag+'.'+name);d[name]=z[1];});return d;};
 ok(Buffer.isBuffer(raw)&&raw.length===1623893,'exact raw byte length');ok(raw.every(x=>x===10||x>=32&&x<127),'complete printable ASCII/LF');
 const text=raw.toString('ascii');ok(text.endsWith('\n')&&!text.endsWith('\n\n'),'single final LF');const lines=text.slice(0,-1).split('\n');ok(Buffer.from(lines.join('\n')+'\n','ascii').equals(raw),'entire science raw reconstruction');
 eq(lines.slice(0,2),['P213_VERIFY_V1','PARAM n_min=1 n_max=6 mass_min=0 mass_max=4 carriers=30 states=461'],'exact header and unchanged bounded contract');
 let cursor=2, carriers=0,statesTotal=0,wordsTotal=0,twoTotal=0,degreeTwoTotal=0, pathPoints=0,sourceEntries=0,acceptedIntervalCells=0;
 const totalStatus=zeros(statuses),totalShape=zeros(shapes),totalAcceptedShape=zeros(shapes),carrierReports=[];
 function choose(n,k){let v=1;for(let j=1;j<=k;j++)v=v*(n-k+j)/j;ok(Number.isInteger(v),'exact small binomial');return v;}
 const maskOf=a=>a.reduce((m,v,i)=>m+(v<=a[(i+1)%a.length]?2**i:0),0);
 const isolated=a=>{const z=Math.min(...a);return a.every((v,i)=>(v-z)*(a[(i+1)%a.length]-z)===0);};
 for(let n=1;n<=6;n++)for(let N=0;N<=4;N++){
  carriers++; const targets=[],words=[];
  while(cursor<lines.length&&!lines[cursor].startsWith('CARRIER ')){
   const localWords=[];
   if(n>=3)for(let m=1;m<2**n-1;m++){
    const w=fields(lines[cursor++],'WORD',['n','N','y','s','status','weight','intervals','sources']);
    ok(integer(w.n)===n&&integer(w.N)===N,'word carrier order');w.y=state(w.y,n,N);
    eq(w.s,Array.from({length:n},(_,i)=>String(m>>i&1)).join(''),'all masks once in exact numeric order');w.mask=m;
    ok(statuses.includes(w.status),'finite status vocabulary');w.weight=integer(w.weight);w.intervals=tuples(w.intervals);w.sources=list(w.sources,n,N);localWords.push(w);
   }
   const t=fields(lines[cursor++],'TARGET',['n','N','y','next','tau','terminal','indegree','fixed_product','sources']);
   ok(integer(t.n)===n&&integer(t.N)===N,'target carrier order');for(const k of ['y','next','terminal'])t[k]=state(t[k],n,N);
   t.tau=integer(t.tau);t.indegree=integer(t.indegree);t.fixed_product=t.fixed_product==='-'?null:integer(t.fixed_product);t.sources=list(t.sources,n,N);
   for(const w of localWords)eq(w.y,t.y,'word group exact target');targets.push(t);words.push(localWords);
  }
  const cr=fields(lines[cursor++],'CARRIER',['n','N','states','height','max_indegree','maximizers','status','shapes','accepted_shapes','degree_two']);
  ok(integer(cr.n)===n&&integer(cr.N)===N,'carrier lexicographic order');for(const k of ['states','height','max_indegree','degree_two'])cr[k]=integer(cr[k]);cr.maximizers=list(cr.maximizers,n,N);cr.status=census(cr.status,statuses);cr.shapes=census(cr.shapes,shapes);cr.accepted_shapes=census(cr.accepted_shapes,shapes);
  A(targets.length===choose(N+n-1,n-1),'full captured composition cardinality');A(targets.every((t,i)=>i===0||lex(targets[i-1].y,t.y)<0),'strict captured lexicographic carrier');A(targets.every(t=>t.y.length===n&&sum(t.y)===N&&Math.min(...t.y)>=0),'all carrier members');
  // Membership + distinctness + stars-and-bars cardinality proves completeness;
  // no unrecorded composition is constructed.
  statesTotal+=targets.length;eq(cr.states,targets.length,'carrier states count');const byState=new Map(targets.map(t=>[key(t.y),t]));const incoming=new Map(targets.map(t=>[key(t.y),[]]));
  for(const t of targets){
   const a=t.y,b=t.next,z=Math.min(...a),flux=a.map((v,i)=>Math.min(v,a[(i+1)%n]));
   eq(b,a.map((v,i)=>v-flux[i]+flux[(i+n-1)%n]),'literal local min-flux identity at captured edge');
   A(byState.has(key(b)),'captured forward closure');A(z===Math.min(...b),'minimum preservation');A(a.every((v,i)=>v!==z||b[i]===z),'permanent residual zeros');A((key(a)===key(b))===isolated(a),'exact fixed classification');if(n<=2)A(key(a)===key(b),'short-cycle identity');incoming.get(key(b)).push(a);
  }
  let two=0,height=0;const paths=new Map();
  for(const t of targets){
   const visited=new Set(),path=[];let q=t;
   while(true){A(!visited.has(key(q.y)),'no nonfixed captured cycle');visited.add(key(q.y));path.push(q.y);if(key(q.next)===key(q.y))break;q=byState.get(key(q.next));}
   pathPoints+=path.length;paths.set(key(t.y),path);eq(t.tau,path.length-1,'reported first fixed time');eq(t.terminal,path[path.length-1],'reported captured terminal');height=Math.max(height,t.tau);
   const z=Math.min(...t.y),r=t.y.map(v=>v-z),endpoint=Array(n).fill(z);
   for(let i=0;i<n;i++)if(r[i]>0&&r[(i+1)%n]===0){let j=i,mass=0,steps=0;while(r[j]>0){mass+=r[j];j=(j+n-1)%n;ok(++steps<n,'finite zero-separated original run');}endpoint[i]+=mass;}
   A(key(endpoint)===key(path[path.length-1]),'original endpoint mass formula');A(t.tau<=Math.max(0,N-1),'global temporal bound');
   if(n===3&&r.filter(v=>v>0).length===2){two++;const h=r.findIndex((v,i)=>v>0&&r[(i+2)%3]===0),e=(h+1)%3,L=r[h]+r[e];for(let time=0;time<path.length+1;time++){const q=path[Math.min(time,path.length-1)];A(q[h]-z===Math.max(L-2**time*r[e],0),'two-site head clock');A(q[e]-z===Math.min(2**time*r[e],L),'two-site receiver clock');}}
  }
  const sharp=n<=2||N===0?0:n===3?Math.ceil(Math.log2(N)):N-1;
  A(height===sharp,'sharp height formula');const witness=Array(n).fill(0);if(n<=2||N<=1)witness[0]=N;else if(n===3){witness[0]=N-1;witness[1]=1;}else if(N===2){witness[0]=1;witness[1]=1;}else{witness[0]=N-2;witness[1]=1;witness[2]=1;}
  A(byState.get(key(witness))?.tau===height,'captured height witness');eq(cr.height,height,'reported height');
  const status=zeros(statuses),shape=zeros(shapes),acceptedShape=zeros(shapes);let degreeTwo=0;
  for(let tIndex=0;tIndex<targets.length;tIndex++){
   const t=targets[tIndex],y=t.y,pred=incoming.get(key(y));eq(t.sources,pred,'whole inverse set from captured edges');eq(t.indegree,pred.length,'reported indegree');sourceEntries+=pred.length;
   const atlas=n<=2?[y]:Math.min(...y)===Math.max(...y)?[y]:[];
   for(const w of words[tIndex]){
    wordsTotal++;const bits=Array.from({length:n},(_,i)=>w.mask>>i&1),blocks=[];
    for(let v=0;v<n;v++)if(bits[(v+n-1)%n]===0&&bits[v]===1){let p=v;while(bits[p%n])p++;let f=p;while(!bits[f%n])f++;blocks.push([v,p,f]);}
    ok(blocks.length>0,'nonconstant cyclic word blocks');const values=Array(n).fill(null),intervals=[];for(const [v]of blocks)values[v]=y[v];let reason=null;
    descent:for(const [v,p,f]of blocks)for(let j=f-1;j>p;j--){const i=j%n,following=(j+1)%n,num=y[i]+values[following];if(num%2){reason='PARITY';break descent;}const forced=num/2;if(forced<0){reason='NEGATIVE_DESCENT';break descent;}if(forced<=values[following]){reason='NONSTRICT_DESCENT';break descent;}values[i]=forced;}
    if(reason===null)for(const [v,p,f]of blocks){const rise=p-v,pi=p%n,next=(p+1)%n;if(rise===1){const f=y[pi]-values[v]+values[next];if(!(values[v]<=f&&f>values[next])){reason='SHORT_PEAK';break;}values[pi]=f;continue;}
     if(y[(v+1)%n]!==y[v]){reason='ASCENT_EQUALITY';break;}let bad=false;for(let j=v+1;j<p-1;j++)if(y[j%n]>y[(j+1)%n])bad=true;if(bad){reason='ASCENT_ORDER';break;}
     for(let j=v;j<p-1;j++)values[j%n]=y[(j+1)%n];const pp=(p-1)%n,total=y[pi]+values[next],lo=y[pp],hi=Math.min(Math.floor(total/2),y[pi]-1);intervals.push([pp,pi,lo,hi,total]);if(lo>hi){reason='EMPTY_INTERVAL';break;}
    }
    const want=reason||'ACCEPTED';eq(w.status,want,'independent first-failure status');eq(w.intervals,intervals,'complete first-failure interval prefix');status[want]++;
    for(const [v,p,f]of blocks){const k=p-v===1?'R1':p-v===2?'R2':'RGE3';shape[k]++;if(want==='ACCEPTED')acceptedShape[k]++;if(f>=n){shape.WRAP++;if(want==='ACCEPTED')acceptedShape.WRAP++;}}
    const expected=pred.filter(a=>maskOf(a)===w.mask);A(JSON.stringify(w.sources)===JSON.stringify(expected),'comparison-word sources from captured edges');
    if(want!=='ACCEPTED'){eq(w.weight,0,'rejected zero weight');eq(w.sources,[],'rejected empty fibre');}
    else{
     let product=1;const free=new Set();for(const [a,b,lo,hi,total]of intervals){product*=hi-lo+1;ok(a!==b&&!free.has(a)&&!free.has(b),'disjoint free coordinate pairs');free.add(a);free.add(b);}if(intervals.length>=2)degreeTwo++;
     for(const source of w.sources){A(source.every(v=>v!==null&&v>=0),'accepted coordinates');A(sum(source)===sum(y),'accepted automatic mass');A(maskOf(source)===w.mask,'accepted exact tie word');for(let i=0;i<n;i++)if(!free.has(i))eq(source[i],values[i],'all forced coordinates');for(const [a,b,lo,hi,total]of intervals)ok(source[a]>=lo&&source[a]<=hi&&source[a]+source[b]===total,'captured point in interval cell');}
     // Distinct captured sources, all inside the disjoint-coordinate Cartesian
     // cell, with product cardinality: full cell coverage without generating it.
     A(product===w.sources.length,'independent interval product cardinality');A(new Set(w.sources.map(key)).size===w.sources.length,'distinct within word');eq(w.weight,product,'reported interval weight');acceptedIntervalCells+=product;
    }
    atlas.push(...w.sources);
   }
   A(new Set(atlas.map(key)).size===atlas.length,'disjoint atlas union');A(JSON.stringify(atlas.slice().sort(lex))===JSON.stringify(pred),'all-target exact atlas source set');
   if(isolated(y)){const z=Math.min(...y),r=y.map(v=>v-z);let product=1;if(Math.max(...r)>0)for(let i=0;i<n;i++)if(r[i]>0){let gap=0,j=(i+n-1)%n;while(r[j]===0){gap++;j=(j+n-1)%n;ok(gap<n,'bounded fixed support gap');}if(gap>=2)product*=Math.floor(r[i]/2)+1;}
    A(product===pred.length,'fixed target product');eq(t.fixed_product,product,'reported fixed product');
   }else eq(t.fixed_product,null,'no nonfixed product claim');
  }
  const maximum=Math.max(...targets.map(t=>t.indegree)),maximizers=targets.filter(t=>t.indegree===maximum).map(t=>t.y);eq(cr.max_indegree,maximum,'maximum indegree');eq(cr.maximizers,maximizers,'entire maximum witness set');
  if(n>=3){const d=Math.floor(n/3);A(maximum<=(2**n-1)*(N+1)**d,'bounded polynomial upper instance');if(N>=2*d){const q=Math.floor(N/(2*d)),spaced=Array(n).fill(0);for(let i=0;i<d;i++)spaced[3*i+2]=2*q;spaced[2]+=N-2*d*q;A(isolated(spaced),'spaced fixed witness');A(byState.get(key(spaced))?.indegree>=(q+1)**d,'spaced fibre lower witness');A(maximum*(2*d)**d>=N**d,'rational lower instance');}}else A(maximum===1,'identity fibre');
  eq(cr.status,status,'complete carrier status census');eq(cr.shapes,shape,'complete carrier shapes');eq(cr.accepted_shapes,acceptedShape,'complete accepted shapes');eq(cr.degree_two,degreeTwo,'degree-two carrier count');
  for(const k of statuses)totalStatus[k]+=status[k];for(const k of shapes){totalShape[k]+=shape[k];totalAcceptedShape[k]+=acceptedShape[k];}twoTotal+=two;degreeTwoTotal+=degreeTwo;
  carrierReports.push({n,N,states:targets.length,height,maximum,two_site:two,degree_two:degreeTwo});
 }
 const total=fields(lines[cursor++],'TOTAL',['carriers','states','words','two_site','degree_two','status','shapes','accepted_shapes']);for(const [k,v]of Object.entries({carriers,states:statesTotal,words:wordsTotal,two_site:twoTotal,degree_two:degreeTwoTotal}))eq(integer(total[k]),v,'exact TOTAL '+k);eq(census(total.status,statuses),totalStatus,'global statuses');eq(census(total.shapes,shapes),totalShape,'global shapes');eq(census(total.accepted_shapes,shapes),totalAcceptedShape,'global accepted shapes');
 A(carriers===30,'declared carriers');A(statesTotal===461,'declared states');for(const k of statuses)if(k!=='NEGATIVE_DESCENT')A(totalStatus[k]>0,'retained branch '+k);A(totalStatus.NEGATIVE_DESCENT===0,'nonnegative recursion');for(const k of shapes)A(totalAcceptedShape[k]>0,'accepted shape '+k);A(degreeTwoTotal>0,'degree-two coverage');A(twoTotal>0,'two-site coverage');
 const pass=fields(lines[cursor++],'PASS',['checks']);eq(integer(pass.checks),asserted,'source assertion multiplicity independently derived from captured records');ok(cursor===lines.length,'no extra/missing science lines');
 return {status:'PASS_CAPTURED_INITIAL_SCIENCE_DATA_ONLY',checks,source_assertions_reconstructed:asserted,raw_bytes:raw.length,lines:lines.length,carriers,states:statesTotal,words:wordsTotal,two_site:twoTotal,degree_two:degreeTwoTotal,captured_orbit_points:pathPoints,captured_inverse_source_entries:sourceEntries,accepted_interval_cell_points:acceptedIntervalCells,status_census:totalStatus,shape_census:totalShape,accepted_shape_census:totalAcceptedShape,carrier_reports:carrierReports,new_science_execution:false,all_parameter_proof:false,canonical_adoption:false,strict_pair:false};
};
