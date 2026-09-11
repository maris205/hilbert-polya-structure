"""Standalone OFS candidate pressure: polygon edges and reverse snapshots.

No project imports or data input. All actual polygon calls stay n=3..10.
The independent carrier is a flip-graph BFS from a fan, not tree generation.
Bracket grammar is a secondary specification of the submitted claims.
"""
from collections import Counter, defaultdict, deque
from functools import cache
from itertools import combinations, product
from math import comb
import hashlib
import json
import sys

CHECKS = Counter()

def check(condition, label):
    CHECKS[label] += 1
    assert condition, label

def edge(a,b):
    return (min(a,b),max(a,b))

def cross(e,f):
    a,b=e; c,d=f
    return a<c<b<d or c<a<d<b

@cache
def boundary(n):
    return frozenset(edge(i,(i+1)%n) for i in range(n))

@cache
def replacement(n,diags,e):
    full=set(diags)|boundary(n)
    a,b=e
    opposite=[v for v in range(n) if v!=a and v!=b
              and edge(a,v) in full and edge(b,v) in full]
    check(len(opposite)==2,'quadrilateral unique')
    f=edge(*opposite)
    check(cross(e,f),'quadrilateral crossing')
    return f

def flip(n,diags,e):
    check(e in diags,'flipped edge present')
    return tuple(sorted((set(diags)-{e})|{replacement(n,diags,e)}))

def carrier(n):
    fan=tuple((0,i) for i in range(2,n-1))
    seen={fan}; q=deque([fan])
    while q:
        t=q.popleft()
        for e in t:
            u=flip(n,t,e)
            if u not in seen:
                seen.add(u); q.append(u)
    check(len(seen)==comb(2*(n-2),n-2)//(n-1),'Catalan BFS completeness')
    return tuple(sorted(seen))

@cache
def sweep(n,diags):
    check(3<=n<=10,'original polygon scope')
    state=diags; inserted=set()
    for e in diags:
        check(e in state,'unvisited original survives')
        f=replacement(n,state,e)
        check(f not in diags,'inserted not original')
        check(inserted<=set(state),'all inserted protected')
        state=flip(n,state,e); inserted.add(f)
    check(inserted==set(state),'complete old-edge removal')
    return state

def reverse_sources(n,target):
    """Recover UNKNOWN original edges in decreasing lexicographic order.

    Already recovered edges are protected. The next restored edge must be
    smaller than all of them and noncrossing with each. At depth n-3 the
    restored set equals the source, proving exact forward schedule reversal.
    No forward graph lookup, author parser or source enumeration is used.
    """
    answer=set()
    def visit(state,restored,ceiling):
        check(len(restored)<=n-3,'reverse search depth')
        if len(restored)==n-3:
            check(set(state)==set(restored),'reverse finished original set')
            answer.add(state)
            return
        for d in state:
            if d in restored:
                continue
            old=replacement(n,state,d)
            if old>=ceiling or any(cross(old,e) for e in restored):
                continue
            visit(flip(n,state,d),restored+(old,),old)
    visit(target,(),(n,n))
    return frozenset(answer)

LEAF='.'
CHERRY='[..]'

def pair(a,b):
    return '['+a+b+']'

@cache
def split(s):
    assert s[0]=='[' and s[-1]==']'
    if s[1]=='.':
        k=2
    else:
        depth=0
        for k in range(1,len(s)):
            depth += (s[k]=='[')-(s[k]==']')
            if depth==0:
                k+=1; break
    return s[1:k],s[k:-1]

def leaves(s):
    return s.count('.')

def lc(n):
    a=LEAF
    for _ in range(n-1): a=pair(a,LEAF)
    return a

def comb_size(s):
    n=1
    while s!=LEAF:
        a,b=split(s)
        if b!=LEAF: return 0
        s=a; n+=1
    return n

def leftlist(s):
    answer=[]
    while s!=LEAF:
        s,r=split(s); answer.append(r)
    return tuple(reversed(answer))

def fromleft(items):
    s=LEAF
    for a in items: s=pair(s,a)
    return s

def graft(s,a):
    k=s.index('.')
    return s[:k]+a+s[k+1:]

@cache
def brackets(n,diags):
    full=set(diags)|boundary(n)
    def rec(a,b):
        if b-a==1: return LEAF
        ks=[k for k in range(a+1,b) if (a,k) in full and (k,b) in full]
        check(len(ks)==1,'root triangle dictionary')
        k=ks[0]
        return pair(rec(a,k),rec(k,b))
    return rec(0,n-1)

@cache
def polygon(s):
    n=leaves(s)+1
    ds=set()
    def visit(t,a,b,root=False):
        if t==LEAF: return
        if not root: ds.add((a,b))
        l,r=split(t); k=a+leaves(l)
        visit(l,a,k); visit(r,k,b)
    visit(s,0,n-1,True)
    return n,tuple(sorted(ds))

@cache
def actual_f(s):
    if s==LEAF: return s
    n,ds=polygon(s)
    return brackets(n,sweep(n,ds))

def actual_g(s):
    return actual_f(pair(LEAF,s))

def cell_product(items):
    p=actual_f(pair(items[0],items[1]))
    for item in items[2:]: p=graft(actual_g(item),p)
    return p

def protected_equation(s):
    if s in (LEAF,CHERRY): return s
    l,r=split(s)
    if l!=LEAF: return pair(LEAF,cell_product(leftlist(s)))
    a,b=split(r)
    if a==LEAF: return graft(actual_g(b),CHERRY)
    return pair(CHERRY,cell_product(leftlist(r)))

@cache
def hf(s):
    if s==LEAF: return 1
    items=leftlist(s)
    pos=[i for i,x in enumerate(items) if x!=LEAF]
    if not pos: return 1<<(len(items)-1)
    if any(b-a==1 for a,b in zip(pos,pos[1:])): return 0
    gaps=[pos[0]]+[b-a-1 for a,b in zip(pos,pos[1:])]+[len(items)-1-pos[-1]]
    exponent=max(gaps[0]-1,0)+max(gaps[-1]-1,0)+sum(g-1 for g in gaps[1:-1])
    result=1<<exponent
    for i in pos: result*=hf(items[i])
    return result

def fibre_claim(s):
    if s==LEAF: return 1
    l,r=split(s)
    return hf(r) if comb_size(l) else 0

@cache
def source_parser(s,kind='F'):
    """Recursive BLOCK-CUT source set, distinct from polygon reverse search."""
    if s==LEAF:
        return frozenset([LEAF]) if kind=='F' else frozenset()
    l,r=split(s); a=comb_size(l)
    if not a: return frozenset()
    if r==LEAF:
        right=LEAF
        for _ in range(leaves(s)-1-(kind=='G')): right=pair(LEAF,right)
        return frozenset([right])
    if kind=='G' and a==1: return frozenset()
    if a==1:
        return frozenset(fromleft(t) for t in parse_product(r))
    if a==2:
        base=frozenset(fromleft(t) for t in parse_product(r))
        return base if kind=='G' else frozenset(pair(LEAF,t) for t in base)
    smaller=pair(lc(a-1),r)
    base=source_parser(smaller,'G')
    return frozenset(pair(LEAF,t) for t in base) if kind=='G' else frozenset(pair(LEAF,pair(LEAF,t)) for t in base)

@cache
def parse_product(s):
    items=leftlist(s); answer=set()
    def rec(start,prefix):
        if start==len(items):
            answer.add(prefix); return
        for end in range(start+1,len(items)+1):
            block=fromleft(items[start:end])
            if start==0:
                for source in source_parser(block,'F'):
                    if source!=LEAF:
                        rec(end,split(source))
            else:
                for source in source_parser(block,'G'):
                    rec(end,prefix+(source,))
    rec(0,())
    return frozenset(answer)

def inclass(s):
    if leaves(s)<=2: return True
    return comb_size(split(s)[0])>=2

def ztree(n):
    if n<=2: return lc(n)
    return pair(CHERRY,ztree(n-2))

@cache
def kmap(s):
    """Equation (5), using the submitted F equation only for its enlarged G.

    No enlarged polygon is run: protected_equation evaluates strictly smaller
    cells using original-size actual polygon sweeps.
    """
    if s==LEAF: return s
    gs=protected_equation(pair(LEAF,s))
    l,r=split(gs)
    return graft(actual_g(r),lc(comb_size(l)-1))

def gspec(s):
    return protected_equation(pair(LEAF,s))

def orbit(start,table):
    seen={}; trail=[]; state=start
    while state not in seen:
        seen[state]=len(trail); trail.append(state); state=table[state]
    return seen[state],tuple(trail[seen[state]:]),tuple(trail)

def dyck(s):
    if s==LEAF: return ''
    l,r=split(s)
    return 'U'+dyck(l)+'D'+dyck(r)

def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def main():
    check(sys.flags.optimize==0 and __debug__,'assertions enabled')
    rows=[]; full=[]; false_uudu=None; false_naive=None
    for n in range(3,11):
        states=carrier(n); table={t:sweep(n,t) for t in states}
        by_target=defaultdict(set)
        for t,u in table.items(): by_target[u].add(t)
        image_count=len(by_target)
        br={t:brackets(n,t) for t in states}
        recurrent=set(); depths=Counter(); periods=Counter(); fs=Counter(); records=[]
        for t in states:
            s=br[t]
            check(polygon(s)==(n,t),'roundtrip dictionary')
            check(actual_f(s)==protected_equation(s),'protected-cell full equation')
            h,cyc,path=orbit(t,table)
            recurrent.update(cyc); depths[h]+=1; periods[len(cyc)]+=1
            check((h==0)==(t in cyc),'entrance convention')
            expected=frozenset(by_target[t]); rev=reverse_sources(n,t)
            check(rev==expected,'full reverse-snapshot source set')
            decoded=source_parser(s)
            check(decoded==frozenset(br[x] for x in expected),'full block-parser source set')
            check(fibre_claim(s)==len(expected),'all-target evaluated fibre')
            fs[len(expected)]+=1
            check(len(expected)==0 or len(expected)&(len(expected)-1)==0,'positive fibre power two')
            if n>=4:
                check((split(s)[0]==LEAF)!=(split(br[table[t]])[0]==LEAF),'ear0 toggling')
                check(split(br[table[t]])[0]==LEAF or inclass(br[table[t]]),'first-image phase class')
            k=kmap(s)
            check(leaves(k)==leaves(s),'K size preservation')
            check(inclass(k),'K all-tree closure')
            check(kmap(gspec(s))==gspec(k),'KG commutation specification')
            if inclass(s) and leaves(s)>=3:
                kl,kr=split(k)
                check(kl==CHERRY and inclass(kr),'K closed class stronger')
            if s!=LEAF and split(s)[0]==CHERRY:
                check(k==pair(CHERRY,kmap(split(s)[1])),'K frozen prefix intertwiner')
            if split(s)[0]==LEAF:
                check(br[table[table[t]]]==pair(LEAF,kmap(split(s)[1])),'F square leaf phase')
            else:
                check(br[table[table[t]]]==k,'F square nonleaf phase all')
            kt=s; kd=0
            while kt!=ztree(n-1):
                kt=kmap(kt); kd+=1
                check(kd<=n,'K converges without lookup')
            check(kd<=(n-1)//2,'K all-tree clock')
            if inclass(s): check(kd<=max(0,(n-3)//2),'K C clock')
            if n>=5 and table[t] in by_target:
                hi=orbit(table[t],table)[0]
                check(hi<=n-3,'first-image sharp phase bound')
            records.append({'source':t,'target':table[t],'depth':h,'cycle':sorted(cyc),
                            'reverse_sources':sorted(rev),'parser_sources':sorted(polygon(x)[1] for x in decoded),
                            'bracket':s,'K':k,'K_depth':kd})
            if n==6 and expected and 'UUDU' in dyck(s) and false_uudu is None:
                false_uudu={'target':t,'word':dyck(s),'source':min(expected)}
        core={br[t] for t in recurrent}
        expected_core={CHERRY} if n==3 else {ztree(n-1),pair(LEAF,ztree(n-2))}
        check(core==expected_core,'complete unique recurrent core')
        check(set(periods)==({1} if n==3 else {2}),'complete all-source periods')
        check(max(depths)==(0 if n<=4 else n-2),'sharp global entrance')
        maximum=max(fs); max_targets=[t for t in states if len(by_target[t])==maximum]
        fan1=tuple(edge(1,j) for j in range(n) if j not in (0,1,2))
        check(maximum==(1 if n<=4 else 1<<(n-4)),'sharp maximum fibre')
        if n>=5: check(max_targets==[tuple(sorted(fan1))],'all maximum fibre targets unique fan1')
        witness=pair(LEAF,CHERRY)
        for _ in range(n-5): witness=pair(witness,LEAF)
        if n>=5:
            witness=pair(witness,LEAF)
            wt=polygon(witness)[1]; wh,_,wp=orbit(wt,table)
            check(wh==n-2,'sharp witness entrance both parities')
            N=n-1; k=N//2
            tail=lc(4)
            for _ in range(k-2): tail=pair(CHERRY,tail)
            if N%2: tail=pair(LEAF,tail)
            check(br[wp[N-2]]==tail,'sharp witness exact penultimate tail')
        image_formula=sum(comb(2*k,k)//(k+1)*comb(n-2+k,3*k+1) for k in range((n-3)//2+1))
        check(image_count==image_formula,'deducted image Catalan composition')
        check(sum(v*c for v,c in fs.items())==len(states),'fibre mass')
        rows.append({'n':n,'states':len(states),'image':image_count,'core':sorted(core),
                     'depth_histogram':sorted(depths.items()),'fibre_histogram':sorted(fs.items()),
                     'max_fibre_targets':max_targets,'source_sets_and_graph_sha256':digest(records)})
        full.append({'n':n,'states':records})
    check(false_uudu is not None,'preserved literal UUDU counterexample')
    payload={'scope':'ALL labelled polygon triangulations n=3..10 only; auxiliary bracket identities are specifications, not enlarged polygon tests',
             'representation':'polygon edge BFS; independent reversed unknown snapshot; separately coded bracket source grammar',
             'rows':rows,'refuted_literal_uudu':false_uudu,'full_graph_and_source_sets':full,
             'check_counts':dict(sorted(CHECKS.items())),'total_assertions':sum(CHECKS.values())}
    print(json.dumps(payload,sort_keys=True,indent=2))

if __name__=='__main__': main()
