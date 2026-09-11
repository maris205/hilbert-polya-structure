'use strict';
const fs=require('node:fs'),crypto=require('node:crypto');
const W='/root/autodl-tmp/symbolic_dynamics', R='docs/papers211_215_sequence/qa/p214_b_runs/initial01';
const fields=['dev','ino','mode','size','mtimeNs','ctimeNs']; let checks=0;
function need(x,s){checks++;if(!x)throw Error(s)}
function read(p){return fs.readFileSync(W+'/'+p)}
function sha(b){return crypto.createHash('sha256').update(b).digest('hex')}
function meta(s){return Object.fromEntries(fields.map(k=>[k,String(s[k])]))}
function add(q,a,b){return q===4?a^b:(a+b)%q}
function mul(q,a,b){if(q!==4)return a*b%q;let z=0;for(let x=a,y=b;y;y>>=1,x<<=1){if(y&1)z^=x;if(x&4)x^=7}return z&3}
function digits(code,q,n){const a=[];for(let i=0;i<n;i++){a.push(code%q);code=Math.floor(code/q)}return [0,...a]}
function index(a,q){let z=0,p=1;for(let i=1;i<a.length;i++){z+=a[i]*p;p*=q}return z}
function ringAdd(q,a,b){return a.map((x,i)=>add(q,x,b[i]))}
function ringMul(q,m,a,b){const z=Array(m).fill(0);for(let i=0;i<m;i++)for(let j=0;i+j<m;j++)z[i+j]=add(q,z[i+j],mul(q,a[i],b[j]));return z}
function valuation(a,m){for(let i=0;i<m;i++)if(a[i])return i;return m}
function list(s){return s==='-'?[]:s.split(',').map(Number)}
function main(){
 const preBytes=read(R+'/PRE.json'),postBytes=read(R+'/POST.json');need(preBytes.equals(postBytes),'PRE/POST');const pre=JSON.parse(preBytes);need(pre.length===44,'keys');
 for(const row of pre){const b=read(row.path),s=fs.statSync(W+'/'+row.path,{bigint:true});need(s.isFile(),'regular');need(b.length===row.bytes,'size');need(sha(b)===row.sha256,'hash');need(JSON.stringify(meta(s))===JSON.stringify(row.metadata),'metadata')}
 const exit=JSON.parse(read(R+'/EXIT.json')),receipt=JSON.parse(read(R+'/RECEIPT.json'));need(exit.status===0&&exit.signal===null&&exit.error===null,'exit');need(receipt.run_id==='initial01'&&receipt.input_keys===44&&receipt.pre_post_equal===true,'receipt');
 const out=read(R+'/stdout.raw'),err=read(R+'/stderr.raw');need(err.length===0&&sha(err)===receipt.stderr.sha256,'stderr');need(out.length===receipt.stdout.bytes&&sha(out)===receipt.stdout.sha256,'stdout envelope');need(out.length===641682&&sha(out)==='7834b38f93b9dfe5e5a57f230ef8d8bac3082a7f7870e9cb384c0dfb9b9ec8f9','stdout identity');need(out[out.length-1]===10,'LF');
 const lines=out.toString('ascii').trimEnd().split('\n');need(lines.length===10553,'lines');let at=0;need(lines[at++]==='P214_B_FORWARD_TRIANGULAR_V1','header');let totalStates=0,expectedAudit=0;
 for(const q of [2,3,4]){
  expectedAudit+=q*3+(q-1)+q*q*(2+3*q);
  for(const m of [2,3,4]){
   const size=q**(m-1),states=size*size,t=[0,1,...Array(m-2).fill(0)],elements=Array.from({length:size},(_,i)=>digits(i,q,m)),trans=[],pred=Array.from({length:states},()=>[]);
   for(let id=0;id<states;id++){const x=elements[Math.floor(id/size)],y=elements[id%size],z=ringMul(q,m,x,ringAdd(q,t,y)),next=(id%size)*size+index(z,q);trans.push(next);pred[next].push(id)}
   for(let id=0;id<states;id++){
    const match=/^STATE\|q=(\d+)\|m=(\d+)\|id=(\d+)\|x=(\d+)\|y=(\d+)\|next=(\d+)\|depth=(\d+)\|formula=(\d+)$/.exec(lines[at++]);need(match,'state syntax');const g=match.slice(1).map(Number),x=Math.floor(id/size),y=id%size;let cur=id,depth=0;while(cur!==0&&depth<=2*m){cur=trans[cur];depth++}need(cur===0,'reaches zero');const formula=Math.max(2*(m-valuation(elements[y],m)),2*(m-valuation(elements[x],m))-1);need(JSON.stringify(g)===JSON.stringify([q,m,id,x,y,trans[id],depth,formula]),'state data')
   }
   expectedAudit+=states*(4+(m===2?1:0))+2*(2*m-1);
   for(let id=0;id<states;id++){
    const match=/^TARGET\|q=(\d+)\|m=(\d+)\|id=(\d+)\|u=(\d+)\|w=(\d+)\|d=(\d+)\|pre=([^|]+)\|triangular=([^|]+)$/.exec(lines[at++]);need(match,'target syntax');const nums=match.slice(1,7).map(Number),u=Math.floor(id/size),w=id%size,d=Math.min(valuation(ringAdd(q,t,elements[u]),m),m-1),p=list(match[7]),tri=list(match[8]);need(JSON.stringify(nums)===JSON.stringify([q,m,id,u,w,d]),'target data');need(JSON.stringify(p)===JSON.stringify(pred[id]),'literal predecessors');need(JSON.stringify(tri)===JSON.stringify(pred[id]),'triangular predecessors');expectedAudit+=2+pred[id].length
   }
   expectedAudit+=3+Math.max(0,m-2)+(m>=3?2:0);
   const image=pred.filter(x=>x.length).length,max=Math.max(...pred.map(x=>x.length)),targets=pred.map((x,i)=>[x,i]).filter(([x])=>x.length===max).map(([,i])=>i).join(',');
   const cm=/^CARRIER\|q=(\d+)\|m=(\d+)\|states=(\d+)\|maxdepth=(\d+)\|image=(\d+)\|maxfibre=(\d+)\|max_targets=(.+)$/.exec(lines[at++]);need(cm,'carrier syntax');need(JSON.stringify(cm.slice(1,7).map(Number))===JSON.stringify([q,m,states,2*m-2,image,max]),'carrier data');need(cm[7]===targets,'max targets');totalStates+=states
  }
 }
 expectedAudit+=2;const last=new RegExp('^PASS\\|carriers=9\\|states=5271\\|state_records=5271\\|target_records=5271\\|checks=(\\d+)$').exec(lines[at++]);need(last&&at===lines.length,'PASS');need(totalStates===5271&&Number(last[1])===expectedAudit,'totals');
 const report={schema:'P214_B_INITIAL_RECEIVER_V1',checks,input_keys:44,carriers:9,states:5271,records:10542,audit_checks:expectedAudit,stdout_bytes:out.length,stdout_sha256:sha(out),result:'PASS'};fs.writeFileSync(W+'/docs/papers211_215_sequence/qa/p214_b_source_root01/INITIAL_NATIVE.json',JSON.stringify(report,null,2)+'\n',{flag:'wx',mode:0o600});process.stdout.write(JSON.stringify(report)+'\n')
}
try{main()}catch(e){process.stderr.write(String(e.stack||e)+'\n');process.exitCode=1}
