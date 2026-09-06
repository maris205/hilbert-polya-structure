"""P208 Review A: triangular-face carrier; BFS flips; word decoder.

No author/gate code or external input is imported. Fixed complete boxes n3..10.
Literal kernel first drafted in kernel.py before manuscript/code inspection.
Flat parenthesis words are used only for testing the manuscript's equations.
"""
from itertools import combinations, product
from functools import lru_cache
from math import comb
import json

CHECKS = 0
def check(p, detail=None):
    global CHECKS
    CHECKS += 1
    if not p: raise AssertionError(detail)

def faces_at_fan(n, v=0):
    ring = [(v+i)%n for i in range(1,n)]
    return tuple(sorted(tuple(sorted((v,a,b))) for a,b in zip(ring,ring[1:])))

def adjacency(state):
    out = {}
    for face in state:
        for e in combinations(face,2): out.setdefault(e,[]).append(face)
    return out

def flip(state, edge):
    pair = adjacency(state)[edge]
    check(len(pair)==2, (state, edge))
    a,b = edge
    c,d = [next(x for x in face if x not in edge) for face in pair]
    faces = set(state)
    faces.difference_update(pair)
    faces.update((tuple(sorted((a,c,d))),tuple(sorted((b,c,d)))))
    return tuple(sorted(faces))

@lru_cache(None)
def sweep(state):
    original = sorted(e for e,f in adjacency(state).items() if len(f)==2)
    work = state
    protected = set()
    for edge in original:
        check(edge in adjacency(work), 'scheduled edge survives')
        old = set(adjacency(work))
        work = flip(work, edge)
        new = set(adjacency(work))
        check(protected <= new, 'inserted boundary survives')
        check(len(new-old)==1 and not (new-old)&set(original), 'new edge not original')
        protected |= new-old
    return work

@lru_cache(None)
def carrier(n):
    seed = faces_at_fan(n)
    seen,queue = {seed},[seed]
    for state in queue:
        for edge,faces in adjacency(state).items():
            if len(faces)==2:
                nxt=flip(state,edge)
                if nxt not in seen: seen.add(nxt); queue.append(nxt)
    return sorted(seen)

E='.'
def pair(a,b): return '('+a+b+')'
C=pair(E,E)
def left_comb(n):
    w=E
    for _ in range(n-1): w=pair(w,E)
    return w
def right_comb(n):
    w=E
    for _ in range(n-1): w=pair(E,w)
    return w
def size(w): return w.count(E)

@lru_cache(None)
def split(w):
    check(w[0]=='(' and w[-1]==')', w)
    i=1
    if w[i]==E: end=i+1
    else:
        depth=1; end=i+1
        while depth:
            depth += (w[end]=='(')-(w[end]==')'); end+=1
    return w[1:end],w[end:-1]

def word(state,a,b):
    if b==a+1: return E
    faces=[f for f in state if a in f and b in f and all(a<=v<=b for v in f)]
    check(len(faces)==1, ('root triangle',a,b,state))
    mid=next(v for v in faces[0] if v not in (a,b))
    return pair(word(state,a,mid),word(state,mid,b))

def triangulate(w,start=0):
    if w==E: return ()
    a,b=split(w); mid=start+size(a); end=start+size(w)
    return tuple(sorted(((start,mid,end),)+triangulate(a,start)+triangulate(b,mid)))

def spine(w):
    out=[]
    while w!=E:
        w,r=split(w);out.append(r)
    return tuple(reversed(out))
def fold(parts):
    w=E
    for b in parts: w=pair(w,b)
    return w
def insert(w,a): return w.replace(E,a,1)
def wrap(w,k):
    for _ in range(k): w=pair(E,w)
    return w

@lru_cache(None)
def rf(w):
    check(size(w)<=9,'original maximum N for F calls')
    if w in (E,C): return w
    a,b=split(w)
    if a==E: return rg(b)
    return pair(E,rp(spine(w)))
@lru_cache(None)
def rg(w):
    check(size(w)+1<=9,'original maximum N for G calls and outputs')
    if w==E: return C
    a,b=split(w)
    if a==E: return insert(rg(b),C)
    return pair(C,rp(spine(w)))
@lru_cache(None)
def rp(parts):
    if len(parts)==2: return rf(pair(*parts))
    return insert(rg(parts[-1]),rp(parts[:-1]))

# These constructors preserve multiplicity until an explicit uniqueness check.
@lru_cache(None)
def source(w,kind):
    if w==E: return (E,) if kind=='F' else ()
    a,r=split(w);l=size(a)
    if a!=left_comb(l): return ()
    if r==E: return (right_comb(size(w)-(kind=='G')),)
    if kind=='G' and l==1: return ()
    wrappers=l-1-(kind=='G')
    return tuple(wrap(fold(s),wrappers) for s in lists(r))

@lru_cache(None)
def lists(w):
    branches=spine(w);out=[]
    def extensions(pos):
        if pos==len(branches): return [()]
        answer=[]
        for end in range(pos+1,len(branches)+1):
            for b in source(fold(branches[pos:end]),'G'):
                for suffix in extensions(end): answer.append((b,)+suffix)
        return answer
    for end in range(1,len(branches)+1):
        for seed in source(fold(branches[:end]),'F'):
            a,b=split(seed)
            for suffix in extensions(end): out.append((a,b)+suffix)
    return tuple(out)

@lru_cache(None)
def h(w):
    if w==E: return 1
    gaps=[0];decor=[]
    for b in spine(w):
        if b==E:gaps[-1]+=1
        else:decor.append(b);gaps.append(0)
    if not decor:return 2**(gaps[0]-1)
    if 0 in gaps[1:-1]: return 0
    exponent=max(gaps[0]-1,0)+max(gaps[-1]-1,0)+sum(a-1 for a in gaps[1:-1])
    ans=2**exponent
    for d in decor:ans*=h(d)
    return ans

@lru_cache(None)
def kval(w):
    if w==E:return E
    left,right=split(w)
    if left!=E:
        # Section 6: K(T)=F^2(T)=G(P(LS(T))). All calls stay at this size.
        return rg(rp(spine(w)))
    # For T=(e,R), G(T)=iota(G(R),c), extending G(R)'s left comb.
    # Insert that incremented comb into the defining D_l(Q) formula.
    a,q=split(rg(right));l=size(a)
    check(a==left_comb(l), 'K leaf-phase definition domain')
    return insert(rg(q),left_comb(l))
def closed(w):
    if size(w)<=2:return w==left_comb(size(w))
    a,b=split(w)
    return size(a)>=2 and a==left_comb(size(a))
def z(n):return E if n==1 else C if n==2 else pair(C,z(n-2))
def witness(n):return pair(E,C) if n==3 else pair(witness(n-1),E)
def jpow(w,t):
    for _ in range(t):w=pair(C,w)
    return w
def orbit(s,transition):
    seen={}; path=[]
    while s not in seen:
        seen[s]=len(path);path.append(s);s=transition[s]
    return path,seen[s],path[seen[s]:]

def main():
    records=[]
    for n in range(3,11):
        states=carrier(n); count=comb(2*(n-2),n-2)//(n-1)
        check(len(states)==count, ('Catalan BFS completeness',n))
        words={s:word(s,0,n-1) for s in states}
        check(len(set(words.values()))==len(states),'labelled dictionary injective')
        image={words[s]:words[sweep(s)] for s in states}
        inverse={w:[] for w in words.values()}
        for s,t in image.items():inverse[t].append(s)
        kt={w:kval(w) for w in image}
        smaller=[E] if n==3 else [word(s,0,n-2) for s in carrier(n-1)]
        ginverse={w:[] for w in image}
        for v in smaller: ginverse[rg(v)].append(v)
        core=set();kcore=set();rows=[]; maxdepth=0
        for faces in states:
            w=words[faces];check(triangulate(w)==faces,'face/word roundtrip')
            check(rf(w)==image[w],'protected-cell dictionary')
            decoded=source(w,'F')
            check(len(decoded)==len(set(decoded)),'source parser disjoint')
            check(set(decoded)==set(inverse[w]),('complete labelled source equality',w))
            a,b=split(w); expected=h(b) if a==left_comb(size(a)) else 0
            check(len(decoded)==expected,'evaluated fibres')
            check(expected==0 or expected&(expected-1)==0,'positive binary power')
            check(h(w)<=2**(size(w)-2),'h bound')
            check((h(w)==2**(size(w)-2))==(w==left_comb(size(w))),'strict equality')
            ls=lists(w)
            check(len(ls)==len(set(ls)),'list parser disjoint')
            check(len(ls)==h(w),'gap formula')
            for seq in ls:check(rp(seq)==w,'every decoded cell list maps back')
            path,depth,cycle=orbit(w,image);maxdepth=max(maxdepth,depth);core.update(cycle)
            kp,kdepth,kcycle=orbit(w,kt);kcore.update(kcycle)
            check(size(kt[w])==size(w),'K size')
            check(kdepth<=size(w)//2,'K global clock')
            if size(w)>=3:
                check(closed(kt[w]),'K full image closure')
                if closed(w):
                    ka,kb=split(kt[w]);check(ka==C and closed(kb),'strong closure incl N3/4')
                    check(kdepth<=(size(w)-2)//2,'K class clock')
            if a!=E: check(image[image[w]]==kt[w],'unrestricted nonleaf square')
            else:check(image[image[w]]==pair(E,kval(b)),'leaf square')
            # Only tested auxiliary constructed words stay within the original N<=9 box.
            if size(w)+1<=9:
                g=rg(w);check(kval(g)==rg(kt[w]),'KG=GK')
                check(rf(pair(E,w))==g,'G literal via tested RF')
                check(source(g,'G') and w in source(g,'G'),'G source membership')
            if size(w)+2<=9:
                check(rg(rg(w))==pair(C,kt[w]),'G2 factorization')
                check(kval(pair(C,w))==pair(C,kt[w]),'KJ=JK')
            # Full G-source set equality for every target using size-minus-one carrier words.
            gb=ginverse[w]
            predicted_g=source(w,'G')
            check(len(predicted_g)==len(set(predicted_g)) and set(predicted_g)==set(gb),'complete G sources')
            rows.append(dict(faces=faces,word=w,output=image[w],sources=sorted(inverse[w]),
                entrance=depth,cycle=cycle,k_output=kt[w],k_entrance=kdepth))
        targetcore={C} if n==3 else {z(n-1),pair(E,z(n-2))}
        check(core==targetcore,'full recurrent core')
        check(kcore=={z(n-1)},'K unique recurrence')
        check(maxdepth==(0 if n<=4 else n-2),'sharp full clock')
        maxf=max(map(len,inverse.values()));maximizers=sorted(w for w,s in inverse.items() if len(s)==maxf)
        check(sum(map(len,inverse.values()))==count,'fibre mass')
        check(maxf==(1 if n<=4 else 2**(n-4)),'max fibre')
        if n>=5:
            check(maximizers==[word(faces_at_fan(n,1),0,n-1)],'unique labelled fan at1')
            N=n-1;s=witness(N);path,depth,_=orbit(s,image)
            check(depth==N-1,'witness sharpness')
            check(image[s]==pair(E,witness(N-1)),'witness first step')
            expected=jpow(left_comb(4),N//2-2) if N%2==0 else pair(E,jpow(left_comb(4),(N-1)//2-2))
            check(path[N-2]==expected,'both witness parity tails')
        records.append(dict(n=n,states=count,max_entrance=maxdepth,max_fibre=maxf,maximizers=maximizers,rows=rows))
    print(json.dumps(dict(status='PASS',assertions=CHECKS,representation='triangular faces / flip BFS / flat-word decoder',
        boxes=records),sort_keys=True,indent=2))

if __name__=='__main__':main()
