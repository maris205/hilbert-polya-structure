"""Independent literal kernel, drafted before reading author code/proof.

State is a sorted tuple of triangular faces, not a binary tree or diagonal set.
The complete carrier is discovered by BFS in the undirected flip graph.
"""
from itertools import combinations

def faces_at_fan(n, v=0):
    ring = [(v+i)%n for i in range(1,n)]
    return tuple(sorted(tuple(sorted((v,a,b))) for a,b in zip(ring,ring[1:])))

def adjacency(state):
    out = {}
    for face in state:
        for e in combinations(face,2):
            out.setdefault(e,[]).append(face)
    return out

def flip(state, edge):
    pair = adjacency(state)[edge]
    assert len(pair) == 2
    a,b = edge
    c,d = [next(x for x in face if x not in edge) for face in pair]
    faces = set(state)
    faces.difference_update(pair)
    faces.update((tuple(sorted((a,c,d))),tuple(sorted((b,c,d)))))
    return tuple(sorted(faces))

def sweep(state):
    original = sorted(e for e, f in adjacency(state).items() if len(f)==2)
    work = state
    for edge in original:
        work = flip(work, edge)
    return work

def carrier(n):
    seed = faces_at_fan(n)
    seen = {seed}
    queue = [seed]
    for state in queue:
        for edge, faces in adjacency(state).items():
            if len(faces) == 2:
                nxt = flip(state,edge)
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append(nxt)
    return sorted(seen)
