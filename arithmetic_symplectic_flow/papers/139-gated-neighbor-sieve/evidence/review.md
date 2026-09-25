# Independent bounded review — ANG-20260914-GNS01

**Date:** 2026-09-14.  
**Candidate status reviewed:** STOP / FORK — PRIME READOUT AND REVERSIBILITY PROVED; PERIOD 4 EXCLUDED; PERIOD 8 OPEN AT THE SEARCH CAP.  
**Review result:** PASS WITH THE STATED SCOPE; no blocking error found.

The reviewer did not author this candidate package. This is an independent
model error check, not peer review. The review reads the unchanged
[candidate card](../candidate-card.md), [paper](../paper.md),
[claim ledger](../claim-ledger.md) and [exact computation record](computation.md).
It neither changes the candidate nor promotes its Route status.

## Mathematical checks

1. The displayed inverse is correct by binary cancellation. Coordinatewise
   finite dependence establishes continuity in both directions on the full
   product space.
2. The nonlinear neighbor term vanishes at either uniform word. The
   two-step prime-indicator output therefore follows by the stated
   trial-divisor proof, without supplied prime data.
3. The reflected boundary gives u2(t+2)=u2(t)+1. Thus its least period is
   exactly four, and every full period must be a multiple of four.
4. The temporal constraint in the paper is the frozen R equation rearranged,
   not an equation for a different finite-box map.
5. Independent direct enumeration below confirms the full period-four
   contradiction at equation eight with the higher neighbor free.

## Independent implementation and exact output

The reviewer ran the following command from the arithmetic_symplectic_flow
workspace. This JavaScript implementation represents temporal words by arrays
of four scalar bits and tests the original equation separately at every time.
It does not use the author's forced/free-bit extension algorithm or its
A/E residual test. All 16 possible upper-neighbor words are checked for
every retained prefix, including at coordinate eight. Thus u9 is not
silently set to zero or given a reflecting boundary.

```bash
node - <<'JS'
const T=4;
const words=Array.from({length:16},(_,code)=>Array.from({length:T},(_,t)=>Math.floor(code/2**t)%2));
const code=w=>w.reduce((s,b,t)=>s+b*2**t,0);
const boundary=words.filter(a=>a.every((_,t)=>(a[(t+1)%4]+a[(t+3)%4])%2===1));
let prefixes=boundary.flatMap(a=>words.map(b=>[a,b]));
console.log('boundary '+boundary.map(code).join(','));console.log('initial '+prefixes.length);
for(let n=3;n<=8;n++){
 const before=prefixes;
 const next=[];
 for(const pref of before){
  const un=pref[n-2],left=pref[n-3];
  for(const right of words){
   const valid=un.every((_,t)=>{
    let sieve=1;
    for(let d=2;d*d<=n;d++)if(n%d===0)sieve*=1-pref[d-2][t];
    const lhs=(un[(t+1)%4]+un[(t+3)%4]+sieve)%2;
    const rhs=((left[t]+un[t])%2)*((right[t]+un[t])%2);
    return lhs===rhs;
   });
   if(valid)next.push([...pref,right]);
  }
 }
 console.log('equation '+n+' completed_prefixes '+next.length);
 if(n===8){
  console.log('all_input_prefixes_at_8');
  for(const pref of before)console.log(pref.map(code).join(','));
 }
 prefixes=next;
}
if(prefixes.length!==0)process.exit(1);
JS
```

Actual output; process exit code 0:

```text
boundary 3,6,9,12
initial 64
equation 3 completed_prefixes 132
equation 4 completed_prefixes 52
equation 5 completed_prefixes 36
equation 6 completed_prefixes 4
equation 7 completed_prefixes 16
equation 8 completed_prefixes 0
all_input_prefixes_at_8
3,3,15,0,15,3,0
3,3,15,0,15,3,1
3,3,15,0,15,3,2
3,3,15,0,15,3,3
6,6,15,0,15,6,0
6,6,15,0,15,6,2
6,6,15,0,15,6,4
6,6,15,0,15,6,6
9,9,15,0,15,9,0
9,9,15,0,15,9,1
9,9,15,0,15,9,8
9,9,15,0,15,9,9
12,12,15,0,15,12,0
12,12,15,0,15,12,4
12,12,15,0,15,12,8
12,12,15,0,15,12,12
```

The counts and all surviving coordinate-2-through-8 prefixes agree with
the author's record. Every hypothetical full point fixed by R to the fourth
power restricts to one of these prefixes and supplies one of the tested u9
words. None satisfies equation eight. Therefore the finite inconsistency
is a rigorous full-space exclusion, not a numerical extrapolation from a
finite carrier.

## Period-eight and claim-boundary audit

The reviewer did not rerun period eight, extend its cap, search higher periods
or inspect a modified Boolean rule. The recorded code stops immediately
when the 100001st next prefix exceeds CAP=100000. Its last-stage admissible
count is consequently partial, as the paper explicitly states. The recorded
resource limit's advance declaration is documented by the author; this review
does not independently certify execution chronology.

Finite compatible prefixes do not establish a complete infinite periodic
point; a storage-cap stop does not establish inconsistency. The paper and
ledger correctly retain period-eight existence, all higher periods and the
zero-seed return problem as OPEN. The evidence neither supplies nor imports
a primitive packet, ordinary zeta, transfer operator or trace formula.

**Decision confirmed:** a scoped research stop/fork after the authorized
bounded checks, not global nonperiodicity. Same-object ownership is preserved;
T0 is established, arithmetic readout is positive but T1/T2 remain partial,
T3 remains open, and Route B remains NOT INVOKED.
