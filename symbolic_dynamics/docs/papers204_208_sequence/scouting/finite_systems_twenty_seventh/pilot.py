"""GCF0 full original boxes only. Pure standard-library author scout."""
import math
import sys

checks=0

def check(condition, label):
    global checks
    checks+=1
    if not condition:
        raise AssertionError(label)

def compositions(n, mass):
    if n==1:
        yield (mass,)
    else:
        for first in range(mass+1):
            for rest in compositions(n-1,mass-first):
                yield (first,)+rest

def currents(x):
    n=len(x)
    return tuple(math.gcd(x[i],x[(i+1)%n]) if x[i] and x[(i+1)%n] else 0
                 for i in range(n))

def step(x):
    flow=currents(x)
    return tuple(a-flow[i]+flow[i-1] for i,a in enumerate(x))

def second_step(x):
    result=list(x)
    for i,a in enumerate(x):
        b=x[(i+1)%len(x)]
        amount=0
        if a>0 and b>0:
            amount=max(d for d in range(1,min(a,b)+1) if a%d==b%d==0)
        result[i]-=amount
        result[(i+1)%len(x)]+=amount
    return tuple(result)

def hist(values):
    result={}
    for value in values:
        result[value]=result.get(value,0)+1
    return tuple(sorted(result.items()))

print('SCHEMA GCF0-v1 MAP n N source successor tail period indegree')
print('BOXES',((3,12),(4,10),(5,8)))
box_count=0
state_count=0
all_periods=set()
all_height=0
for n,maximum in ((3,12),(4,10),(5,8)):
    for mass in range(maximum+1):
        states=tuple(compositions(n,mass))
        check(len(states)==math.comb(mass+n-1,n-1),'whole carrier size')
        check(len(set(states))==len(states),'carrier unique')
        forward={}
        incoming={x:[] for x in states}
        for x in states:
            y=step(x)
            check(y==second_step(x),'literal and divisor-enumeration updates')
            check(y in incoming and sum(y)==mass,'closure and conservation')
            check(all(x[i]!=0 or y[i]==0 for i in range(n)),'hereditary zeros')
            check(not all(x) or all(y),'invariant positive stratum')
            flow=currents(x)
            check((y==x)==(len(set(flow))==1),'constant-current fixed criterion')
            if 0 in x:
                zero=x.index(0)
                weight=lambda z:sum(k*z[(zero+k)%n] for k in range(1,n))
                increase=sum(flow[(zero+k)%n] for k in range(1,n-1))
                check(weight(y)-weight(x)==increase,'boundary flux potential')
                check((increase==0)==(y==x),'boundary strictness')
            forward[x]=y
            incoming[y].append(x)
        tails={}
        periods={}
        cycles=set()
        for x in states:
            positions={}
            orbit=[]
            current=x
            while current not in positions:
                positions[current]=len(orbit)
                orbit.append(current)
                current=forward[current]
            tail=positions[current]
            cycle=tuple(orbit[tail:])
            least=min(range(len(cycle)),key=lambda j:cycle[j])
            cycle=cycle[least:]+cycle[:least]
            cycles.add(cycle)
            tails[x]=tail
            periods[x]=len(cycle)
            check(tail+len(cycle)<=len(states),'finite graph decomposition')
            if 0 in x:
                check(len(cycle)==1,'proved zero-boundary convergence')
        check(sum(map(len,incoming.values()))==len(states),'indegree mass')
        for x in states:
            print('MAP',n,mass,x,forward[x],tails[x],periods[x],len(incoming[x]))
        for cycle in sorted(cycles):
            print('CYCLE',n,mass,cycle)
        height=max(tails.values())
        maximum_fibre=max(map(len,incoming.values()))
        max_targets=tuple(x for x in states if len(incoming[x])==maximum_fibre)
        deepest=tuple(x for x in states if tails[x]==height)
        print('SUMMARY',n,mass,'states',len(states),'image',sum(bool(v) for v in incoming.values()),
              'fixed',sum(forward[x]==x for x in states),'height',height,
              'periods',tuple(sorted(set(periods.values()))),'tail_hist',hist(tails.values()),
              'fibre_hist',hist(map(len,incoming.values())),'max_fibre',maximum_fibre,
              'max_targets',max_targets,'deepest',deepest)
        box_count+=1
        state_count+=len(states)
        all_periods.update(periods.values())
        all_height=max(all_height,height)
check(box_count==33 and state_count==2743,'declared exact box totals')
print('TOTAL',box_count,state_count,checks,tuple(sorted(all_periods)),all_height)
print('RUNTIME',sys.executable,sys.version,sys.flags,file=sys.stderr)
for name,module in sorted(sys.modules.items()):
    path=getattr(module,'__file__',None)
    if path:
        print('MODULE',name,path,file=sys.stderr)
