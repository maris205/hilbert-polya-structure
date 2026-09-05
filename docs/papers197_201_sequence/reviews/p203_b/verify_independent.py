#!/usr/bin/env python3
"""P203 manuscript Review B: row strings, SCCs, reverse BFS, target clauses.

Adapted by its original writer from the pinned MCT Stage1 control, not from
an author or Review-A program. Reuse is explicit; this is a new Round1 review
execution with additional paper-specific recurrent/trace/identity checks.
No author or A code read, imported or copied. Finite PASS is not a proof.
"""
from collections import Counter, deque
from itertools import combinations
import json

CHECKS = 0


def ck(test, note=""):
    global CHECKS
    CHECKS += 1
    if not test:
        raise AssertionError((CHECKS, note))


def row_word(index, n):
    colors = iter(format(index, "0%db" % (n*(n-1)//2)))
    rows = [["."]*n for _ in range(n)]
    for a,b in combinations(range(n), 2):
        rows[a][b] = rows[b][a] = next(colors)
    return tuple("".join(r) for r in rows)


def number(rows):
    s = "".join(rows[a][b] for a,b in combinations(range(len(rows)), 2))
    return int(s or "0", 2)


def mono(rows, t):
    a,b,c = t
    return rows[a][b] == rows[a][c] == rows[b][c]


def flip(rows, t):
    rr = [list(s) for s in rows]
    for a,b in combinations(t, 2):
        rr[a][b] = rr[b][a] = "1" if rows[a][b] == "0" else "0"
    return tuple("".join(s) for s in rr)


def selector(rows, triples, tournament=False):
    for t in triples:
        a,b,c = t
        on = rows[a][b] == rows[b][c] != rows[a][c] if tournament else mono(rows,t)
        if on:
            return t
    return None


def graph_scc(f):
    """Generic Kosaraju, then incoming BFS; no presumed period or clock."""
    size = len(f)
    incoming = [[] for _ in f]
    for x,y in enumerate(f):
        incoming[y].append(x)
    visited, finish = set(), []
    for root in range(size):
        if root in visited:
            continue
        todo = [(root,False)]
        while todo:
            x,exit_stage = todo.pop()
            if exit_stage:
                finish.append(x)
            elif x not in visited:
                visited.add(x)
                todo.append((x,True))
                todo.append((f[x],False))
    assigned = set()
    recurrent = set()
    cycles = Counter()
    periods = [0]*size
    for root in reversed(finish):
        if root in assigned:
            continue
        component, todo = [], [root]
        assigned.add(root)
        while todo:
            x = todo.pop()
            component.append(x)
            for y in incoming[x]:
                if y not in assigned:
                    assigned.add(y)
                    todo.append(y)
        if len(component)>1 or f[root] == root:
            cycles[len(component)] += 1
            recurrent.update(component)
            for x in component:
                periods[x] = len(component)
    distance = [-1]*size
    todo = deque(recurrent)
    for x in recurrent:
        distance[x] = 0
    while todo:
        x = todo.popleft()
        for y in incoming[x]:
            if distance[y] < 0:
                distance[y] = distance[x]+1
                periods[y] = periods[x]
                todo.append(y)
    ck(all(d>=0 for d in distance))
    return incoming,distance,periods,cycles


def target_clause_sources(rows, triples):
    """Local forbidden-equality clauses; never run source selector/F."""
    if not any(mono(rows,t) for t in triples):
        return {number(rows)}, []
    accepted = []
    for t in triples:
        if not mono(rows,t):
            continue
        tedges = set(combinations(t,2))
        valid = True
        for earlier in triples:
            if earlier == t:
                break
            common = tedges.intersection(combinations(earlier,2))
            if not common:
                if mono(rows,earlier):
                    valid = False; break
            else:
                # Distinct triples share exactly one edge or none.
                e, = common
                other = [rows[a][b] for a,b in combinations(earlier,2) if (a,b)!=e]
                if other[0] == other[1] != rows[e[0]][e[1]]:
                    valid = False; break
        if valid:
            accepted.append(t)
    return {number(flip(rows,t)) for t in accepted},accepted


def star_certificate(rows, a, b):
    n = len(rows)
    outside = [z for z in range(n) if z not in (a,b)]
    c = rows[a][b]
    if any(rows[a][z]!=c or rows[b][z]!=c for z in outside):
        return False
    faces = {z:tuple(sorted((a,b,z))) for z in outside}
    for x,y in combinations(outside,2):
        if rows[x][y] == c:
            boundary = tuple(sorted((a,x,y)))
            if any(faces[z]>=boundary for z in outside if z not in (x,y)):
                return False
    last = max(faces.values())
    return all(not mono(rows,p) or p>last for p in combinations(outside,3))


def top_certificate(rows, four, triples):
    c = rows[four[0]][four[1]]
    if any(rows[a][b]!=c for a,b in combinations(four,2)):
        return False
    faces = list(combinations(four,3))
    for p in triples:
        inside = tuple(v for v in p if v in four)
        if len(inside)<=1:
            if mono(rows,p) and p<=faces[-1]:
                return False
        elif len(inside)==2:
            u, = (v for v in p if v not in four)
            x,y = inside
            if rows[u][x] == rows[u][y]:
                # All unflipped faces block when spokes have internal colour;
                # all flipped faces block when spokes have opposite colour.
                need_contains = rows[u][x] != c
                for face in faces:
                    if (x in face and y in face)==need_contains and p<=face:
                        return False
    return True


def prescribed_rows(n, colour):
    rr = [["."]*n for _ in range(n)]
    for a,b in combinations(range(n),2):
        rr[a][b] = rr[b][a] = str(colour(a,b))
    return tuple("".join(r) for r in rr)


def sharp_rows(n):
    def edge(a,b):
        def spoke(i):
            return 0 if i<=1 else (i-1)%2
        if a==0:
            return spoke(n-1-b)
        i,j = sorted((n-1-a,n-1-b))
        if j==i+1:
            return i%2
        return 1-spoke(i) if spoke(i)==spoke(j) else spoke(i)
    return prescribed_rows(n,edge)


def parameter_witnesses():
    for n in range(3,81):
        triples = list(combinations(range(n),3))
        rows = sharp_rows(n)
        for t in range(n-2):
            chosen = selector(rows,triples)
            ck(chosen == (0,n-2-t,n-1-t), (n,t,"sharp"))
            ck(rows[chosen[0]][chosen[1]] == str(t%2))
            after = flip(rows,chosen)
            if t==n-3:
                ck(selector(after,triples)==chosen)
                ck(flip(after,chosen)==rows)
            rows = after
    print("sharp_witness_n=3..80")
    for n in range(4,25):
        triples = list(combinations(range(n),3))
        for colour in (0,1):
            star = prescribed_rows(n,lambda a,b: colour if a<=1 else 1-colour)
            preds, family = target_clause_sources(star,triples)
            ck(len(preds)==n-2)
            ck(star_certificate(star,0,1))
            top = prescribed_rows(n,lambda a,b: 1-colour if a==0 and b>=4 else colour)
            preds, family = target_clause_sources(top,triples)
            ck(len(preds)==4)
            ck(top_certificate(top,(0,1,2,3),triples))
    print("star_and_top_witness_n=4..24_both_colours")


def complete_boxes():
    total = 0
    fixed_counts = (1,1,2,6,18,12,0)
    for n in range(7):
        triples = list(combinations(range(n),3))
        rows = [row_word(g,n) for g in range(2**(n*(n-1)//2))]
        total += len(rows)
        selected = [selector(r,triples) for r in rows]
        f = [number(flip(r,t)) if t else g for g,(r,t) in enumerate(zip(rows,selected))]
        incoming,depth,period,cycles = graph_scc(f)
        best = 1 if n<=3 else max(4,n-2)
        cert_counts = Counter()
        for g,(r,t) in enumerate(zip(rows,selected)):
            ck(period[g] in (1,2))
            ck((t is None) == (f[g]==g))
            ck(depth[g]==0 if t is None else (depth[g]==0)==(selected[f[g]]==t))
            preds, candidates = target_clause_sources(r,triples)
            ck(preds == set(incoming[g]), (n,g,"sources"))
            ck(len(preds) <= best)
            ck(bool(incoming[g]) == (t is None or bool(candidates)), (n,g,"paper_image_iff"))
            if t is not None:
                ck((depth[g]==0) == (t in candidates), (n,g,"paper_C_recurrent_iff"))
            if n>=4:
                accepted = set(candidates)
                stars = []
                tops = []
                for a,b in combinations(range(n),2):
                    full_star = {tuple(sorted((a,b,z))) for z in range(n) if z not in (a,b)}
                    certified = star_certificate(r,a,b)
                    ck(certified == full_star.issubset(accepted), (n,g,a,b,"star_iff"))
                    if certified:
                        stars.append((a,b))
                for four in combinations(range(n),4):
                    certified = top_certificate(r,four,triples)
                    ck(certified == set(combinations(four,3)).issubset(accepted), (n,g,four,"top_iff"))
                    if certified:
                        tops.append(four)
                maximum_certificate = bool(tops) if n<=5 else bool(stars or tops)
                ck((len(preds)==best)==maximum_certificate)
                cert_counts["star_targets"] += bool(stars)
                cert_counts["top_targets"] += bool(tops)
                cert_counts["both_targets"] += bool(stars and tops)
            for p,q in combinations(candidates,2):
                ck(len(set(p)&set(q))==2)
            if len(candidates)>=3:
                intersection = set.intersection(*(set(t) for t in candidates))
                union = set.union(*(set(t) for t in candidates))
                ck(len(intersection)==2 or len(union)==4)
            if t is not None:
                ck(0 in selected[f[g]], (n,g,"root0_after_one"))
                ck(sum(r[a].count("1")%2 != rows[f[g]][a].count("1")%2 for a in range(n))==0)
                seen_vertices = set(t)
                x = g
                anchor = None
                prior_shared = None
                retired = set(t)-set(selected[f[g]]) if depth[g]>0 and min(selected[f[g]])<min(t) else set()
                for tick in range(depth[g]):
                    y = f[x]
                    old,new = selected[x],selected[y]
                    ck(new < old)
                    common = set(old)&set(new)
                    ck(len(common)==2)
                    ck(prior_shared is None or common!=prior_shared, (n,g,tick,"repeated_shared_edge"))
                    ck(not (retired&set(new)), (n,g,tick,"initial_retired_return"))
                    prior_shared = common
                    ck(len(set(new)-seen_vertices)==1, (n,g,tick,"return",old,new))
                    seen_vertices.update(new)
                    if tick==0:
                        anchor = min(new)
                    ck(min(new)==anchor)
                    x = y
                ck(len(seen_vertices)==3+depth[g])
        ck(max(depth)==max(n-3,0))
        ck(max(map(len,incoming))==best)
        ck(sum(t is None for t in selected)==fixed_counts[n])
        ck(sum(map(len,incoming))==len(rows))
        print("MCT",json.dumps({"n":n,"states":len(rows),"image":sum(bool(p) for p in incoming),
              "depth":sorted(Counter(depth).items()),"cycles":sorted(cycles.items()),
              "max_fibre":best,"max_targets":sum(len(p)==best for p in incoming),
              "certificates":dict(cert_counts)},sort_keys=True,separators=(",",":")))
        if 3<=n<=6:
            qt=[selector(r,triples,True) for r in rows]
            qf=[number(flip(r,t)) if t else g for g,(r,t) in enumerate(zip(rows,qt))]
            _,qd,_,qc=graph_scc(qf)
            ck(max(qd)==(0 if n==3 else n-2))
            ck(sum(q is None for q in qt)!=(fixed_counts[n]) if n>=4 else True)
            print("Q01_control",json.dumps({"n":n,"height":max(qd),"cycles":sorted(qc.items())},sort_keys=True,separators=(",",":")))
    print("total_states",total)


if __name__=="__main__":
    print("review=P203_B_frozen_repaired_Round1")
    print("representation=row_strings_Kosaraju_reverse_BFS_target_clauses")
    print("reuse=reviewer_own_MCT_Stage1_engine_disclosed_not_author_or_A_code")
    complete_boxes()
    parameter_witnesses()
    print("assertions="+str(CHECKS))
    print("status=PASS")
    print("scope=finite_crosscheck_not_all_parameter_proof_or_priority_certificate")
