#!/usr/bin/env python3
"""Author exact OR theorem controls. Pure standard library; no scout imports."""
from collections import Counter, deque
from itertools import product
from math import gcd
import argparse


ASSERTIONS = 0


def eq(actual, expected, tag):
    global ASSERTIONS
    ASSERTIONS += 1
    if actual != expected:
        raise AssertionError((tag, actual, expected))


def step(x):
    return tuple((a+1) % 3 if a <= x[(i+1) % len(x)] else 0
                 for i,a in enumerate(x))


def table_step(x):
    table = ((1,1,1),(0,2,2),(0,0,0))
    return tuple(table[a][x[(i+1) % len(x)]] for i,a in enumerate(x))


def code(x):
    result = 0
    for a in x:
        result = 3*result+a
    return result


def supported(x):
    return all((a,x[(i+1) % len(x)]) != (2,1) for i,a in enumerate(x))


def e01(x):
    return sum((a,x[(i+1) % len(x)]) == (0,1) for i,a in enumerate(x))


def in_a(x):
    return all((x[(i+1)%len(x)]-a) % 3 in (0,1) for i,a in enumerate(x))


def in_b(x):
    edges = {(0,1),(1,0),(1,2),(2,0)}
    return all((a,x[(i+1)%len(x)]) in edges for i,a in enumerate(x))


def lucas(n):
    a,b = 2,1
    for _ in range(n):
        a,b = b,a+b
    return a


def a_count(n):
    return 2**n+(2,1,-1,-2,-1,1)[n%6]


def b_count(n):
    values = [3,0,2]
    for j in range(3,n+1):
        values.append(values[j-2]+values[j-3])
    return values[n]


def max_tail(n):
    return 0 if n == 1 else 2 if n == 2 else 3*(n//3)+1


def runs(x):
    """Cyclic zero/one/two runs; empty list means a constant word."""
    n = len(x)
    if len(set(x)) == 1:
        return []
    cut = next(i for i in range(n) if x[i] == 0 and x[i-1] != 0)
    y = x[cut:]+x[:cut]
    result = []
    j = 0
    while j < n:
        row = []
        for value in (0,1,2):
            count = 0
            while j < n and y[j] == value:
                j += 1
                count += 1
            row.append(count)
        if not row[0] or not row[1]+row[2]:
            raise AssertionError(("invalid run word",x,row,j))
        result.append(tuple(row))
    return tuple(result)


def rotate_normal(rows):
    return min(rows[i:]+rows[:i] for i in range(len(rows)))


def run_step(rows):
    return tuple((max(rows[i-1][2],1),c,a-int(b == 0))
                 for i,(c,a,b) in enumerate(rows))


def to_queue(rows):
    return tuple(v for c,a,b in rows for v in (c-1,a-1,b))


def queue_step(z):
    # Physical bin rule: retain a single parked particle in every third bin.
    cap = tuple(int(i%3 == 2) for i in range(len(z)))
    return tuple(min(z[i],cap[i])+max(z[i-1]-cap[i-1],0)
                 for i in range(len(z)))


def cleared(z):
    k = len(z)//3
    parked = sum(z[j]>0 for j in range(2,len(z),3))
    return parked == k or sum(z) == parked


def clear_time(z):
    t = 0
    bound = 3*min(len(z)//3,sum(z))-1 if sum(z) else 0
    while not cleared(z):
        z = queue_step(z)
        t += 1
        if t > bound:
            raise AssertionError(("queue bound",z,t,bound))
    return t


def weak_compositions(total, parts):
    if parts == 1:
        yield (total,)
    else:
        for first in range(total+1):
            for rest in weak_compositions(total-first,parts-1):
                yield (first,)+rest


def predicted_maximizers(n):
    if n == 1:
        return {(0,),(1,),(2,)}
    m = n//2
    if n%2 == 0:
        return {(0,1)*m,(1,0)*m}
    base = [(0,0,1)+(0,1)*(m-1), (0,1,1)+(0,1)*(m-1),
            (0,1,2)+(0,1)*(m-1)]
    return {x[i:]+x[:i] for x in base for i in range(n)}


def verify_box(n):
    states = list(product(range(3),repeat=n))
    size = len(states)
    nxt = []
    fibres = [0]*size
    for x in states:
        y = step(x)
        eq(y,table_step(x),"independent local table")
        j = code(y)
        nxt.append(j)
        fibres[j] += 1
    degree = fibres.copy()
    queue = deque(i for i,d in enumerate(degree) if d == 0)
    peeled = []
    while queue:
        i = queue.popleft()
        peeled.append(i)
        j = nxt[i]
        degree[j] -= 1
        if degree[j] == 0:
            queue.append(j)
    depth = [0]*size
    for i in reversed(peeled):
        depth[i] = depth[nxt[i]]+1
    seen = set()
    cycles = Counter()
    for i,d in enumerate(degree):
        if d and i not in seen:
            j = i
            length = 0
            while j not in seen:
                seen.add(j)
                length += 1
                j = nxt[j]
            cycles[length] += 1
    a_total = b_total = both = 0
    for i,x in enumerate(states):
        ok = supported(x)
        aa,bb = in_a(x),in_b(x)
        a_total += aa
        b_total += bb
        both += aa and bb
        eq(fibres[i],2**e01(x) if ok else 0,"every target fibre")
        eq(bool(degree[i]),aa or bb,"complete recurrent iff")
        eq(depth[i] <= max_tail(n),True,"all point tail bound")
        if aa:
            eq(states[nxt[i]],tuple((v+1)%3 for v in x),"A action")
        if bb:
            eq(states[nxt[i]],x[1:]+x[:1],"B action")
        if ok and len(set(x))>1:
            old = runs(x)
            new = runs(states[nxt[i]])
            eq(rotate_normal(new),rotate_normal(run_step(old)),"literal run recurrence")
        if n <= 7 and fibres[i]:
            # Exact full source-set construction, checked by direct updates.
            available = [j for j in range(n) if (x[j],x[(j+1)%n]) == (0,1)]
            constructed = set()
            for choices in product((0,1),repeat=len(available)):
                source = [(v-1)%3 for v in x]
                for j,bit in zip(available,choices):
                    if bit:
                        source[j] = 1
                source = tuple(source)
                eq(step(source),x,"inverse source reconstruction")
                constructed.add(source)
            eq(len(constructed),fibres[i],"exhaustive inverse cardinality")
    eq(a_total,a_count(n),"A census")
    eq(b_total,b_count(n),"B census")
    eq(both,3 if n%3 == 0 else 0,"core intersection")
    eq(sum(d>0 for d in fibres),lucas(2*n),"first image")
    eq(max(depth),max_tail(n),"sharp all-length tail")
    maximum = max(fibres)
    eq(maximum,2**(n//2),"fibre maximum")
    eq({states[i] for i,v in enumerate(fibres) if v == maximum},
       predicted_maximizers(n),"all maximal targets")
    for t in range(1,2*n+4):
        d = gcd(n,t)
        predicted = (a_count(n) if t%3 == 0 else 0)+b_count(d)-(3 if d%3 == 0 else 0)
        actual = sum(length*count for length,count in cycles.items() if t%length == 0)
        eq(actual,predicted,"every checked temporal fixed count")
    for i in set(nxt[j] for j in nxt):
        x = states[i]
        if len(set(x)) == 1:
            continue
        row = runs(x)
        eq(all(c>=1 and a>=1 and b>=0 for c,a,b in row),True,"twice-image domain")
        z = to_queue(row)
        eq(to_queue(run_step(row)),queue_step(z),"queue exact recurrence")
        eq(depth[i],clear_time(z),"exact first entry from twice-image")
    print(f"n={n} states={size} image={sum(v>0 for v in fibres)} recurrent={len(seen)} "
          f"tail={max(depth)} max_fibre={maximum} max_targets={len(predicted_maximizers(n))} "
          f"cycles={tuple(sorted(cycles.items()))}",flush=True)


def verify_transport():
    cases = 0
    for k in range(1,5):
        for mass in range(6):
            maximum = 0
            for z in weak_compositions(mass,3*k):
                t = clear_time(z)
                maximum = max(maximum,t)
                eq(sum(queue_step(z)),mass,"queue mass conservation")
                eq(all(not z[j] or queue_step(z)[j]>0 for j in range(2,3*k,3)),
                   True,"occupied slots remain occupied")
                cases += 1
            eq(maximum,3*min(k,mass)-1 if mass else 0,"sharp queue bound")
    print(f"TRANSPORT_COMPLETE k=1..4 mass=0..5 cases={cases}",flush=True)


def verify_witnesses():
    for n in list(range(3,151))+[300,301,302,1000]:
        k,r = divmod(n,3)
        x = (1,)*(k+r+1)+(2,)+(1,2)*(k-1)
        expected_second = (0,)*(k+r+1)+(1,)+(0,1)*(k-1)
        eq(step(step(x)),expected_second,"sharp initial prehistory")
        z = to_queue(runs(expected_second))
        eq(sum(z),k+r,"witness mass")
        eq(clear_time(z)+2,max_tail(n),"arbitrary-length sharp witness")
    print("WITNESSES n=3..150,300,301,302,1000",flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--maxn",type=int,default=12)
    args = parser.parse_args()
    print("OR_TERNARY_AUTHOR_THEOREM_CONTROL / NO_PAPER_NUMBER / HOLD_EXTERNAL")
    for n in range(1,args.maxn+1):
        verify_box(n)
    verify_transport()
    verify_witnesses()
    print(f"ASSERTIONS={ASSERTIONS}")
    print("PASS / AUTHOR_STAGE1_CONTROL_ONLY / OWNER_GATE_PENDING / HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
