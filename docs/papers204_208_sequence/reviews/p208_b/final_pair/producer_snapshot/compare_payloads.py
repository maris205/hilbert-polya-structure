"""Compare every scientific field with independent B output; no science imports."""
import hashlib
import json
from pathlib import Path
from collections import Counter
from itertools import combinations
import sys

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
BASE=ROOT/'docs/papers204_208_sequence/reviews/p208_b'
FILES={'B':BASE/'CANONICAL.json',
       'author':ROOT/'papers/208-original-snapshot-triangulation-sweeps/frozen_round1/CANONICAL.json',
       'A':ROOT/'docs/papers204_208_sequence/reviews/p208_a/CANONICAL.json'}
CHECKS=0
def check(x,label):
    global CHECKS
    CHECKS+=1
    if not x:raise AssertionError(label)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def edges_key(value):return tuple(sorted(tuple(e) for e in value))
def tuple_edges(tree):
    intervals=[]
    def visit(t,lo):
        if not t:return lo+1
        middle=visit(t[0],lo);hi=visit(t[1],middle);intervals.append((lo,hi));return hi
    N=visit(tree,0)
    return N,tuple(sorted(e for e in intervals if e!=(0,N)))
def word_edges(word):
    pos=0;intervals=[]
    def visit(lo):
        nonlocal pos
        if word[pos]=='.':pos+=1;return lo+1
        check(word[pos]=='(','word syntax open');pos+=1
        middle=visit(lo);hi=visit(middle)
        check(word[pos]==')','word syntax close');pos+=1
        intervals.append((lo,hi));return hi
    N=visit(0);check(pos==len(word),'word fully consumed')
    return N,tuple(sorted(e for e in intervals if e!=(0,N)))
def triangles(n,edges):
    graph=set(edges)|{(i,i+1) for i in range(n-1)}|{(0,n-1)}
    return tuple(t for t in combinations(range(n),3) if all(e in graph for e in combinations(t,2)))
def main():
    before={k:{'path':str(p),'sha256':sha(p)} for k,p in FILES.items()}
    data={k:json.loads(p.read_text()) for k,p in FILES.items()}
    reports=[]
    check(data['B']['total_states']==data['author']['total_states']==2055,'total carrier')
    check(data['author']['total_decoded_predecessors']==2055,'complete fibre mass')
    check(len(data['B']['polygons'])==len(data['author']['rows'])==len(data['A']['boxes'])==8,'all boxes')
    for box,author,A in zip(data['B']['polygons'],data['author']['rows'],data['A']['boxes']):
        n=box['n'];check(n==author['n']==A['n'],'box identity')
        chords=[tuple(e) for e in box['chords']]
        def from_mask(s):return tuple(chords[j] for j in range(len(chords)) if s&(1<<j))
        byedges={edges_key(r['edges']):r for r in box['rows']}
        check(len(byedges)==len(box['rows'])==author['states']==A['states'],'carrier size')
        check(set(byedges)=={edges_key(r['diagonals']) for r in author['complete_graph_and_sources']},'author full carrier')
        check(set(byedges)=={word_edges(r['word'])[1] for r in A['rows']},'A full carrier')
        literal=[]
        for r in author['complete_graph_and_sources']:
            e=edges_key(r['diagonals']);b=byedges[e]
            check(tuple_edges(r['tree'])==(n-1,e),'author tree full labelled dictionary')
            check(edges_key(r['next_diagonals'])==from_mask(b['next']),'author transition')
            check(r['height']==b['depth'],'author entrance')
            check(r['fibre']==len(b['predecessors']),'author fibre')
            check(sorted(edges_key(s) for s in r['source_diagonals'])==sorted(from_mask(s) for s in b['predecessors']),'author complete labelled sources')
            check(edges_key(r['K_next_diagonals'])==from_mask(b['K_next']),'author K transition')
            check(r['K_height']==b['K_depth'],'author K entrance')
            literal.append((e,from_mask(b['next']),b['depth'],len(b['predecessors'])))
            check(set(r)=={'tree','diagonals','next_diagonals','height','fibre','source_diagonals','K_next_diagonals','K_height'},'all author per-state fields handled')
        check(hashlib.sha256(json.dumps(literal,separators=(',',':')).encode()).hexdigest()==author['literal_transition_depth_fibre_sha256'],'author exact literal-table digest independently reconstructed')
        for r in A['rows']:
            N,e=word_edges(r['word']);b=byedges[e];check(N==n-1,'A word size')
            check(tuple(tuple(t) for t in r['faces'])==triangles(n,e),'A all triangle faces')
            check(word_edges(r['output'])==(n-1,from_mask(b['next'])),'A transition')
            check(sorted(word_edges(s)[1] for s in r['sources'])==sorted(from_mask(s) for s in b['predecessors']),'A complete labelled sources')
            check(r['entrance']==b['depth'],'A entrance')
            check({word_edges(s)[1] for s in r['cycle']}=={from_mask(s) for s in b['cycle']},'A complete cycle')
            check(word_edges(r['k_output'])==(n-1,from_mask(b['K_next'])),'A K transition')
            check(r['k_entrance']==b['K_depth'],'A K entrance')
            check(set(r)=={'faces','word','output','sources','entrance','cycle','k_output','k_entrance'},'all A per-state fields handled')
        maximum=max(len(b['predecessors']) for b in box['rows'])
        maximizers=sorted(e for e,b in byedges.items() if len(b['predecessors'])==maximum)
        core={from_mask(s) for c in box['cycles'] for s in c}
        check(core=={edges_key(s) for s in author['core_diagonals']},'author entire core')
        check(maximum==author['maximum_fibre']==A['max_fibre'],'all maxima values')
        check(maximizers==sorted(edges_key(s) for s in author['all_maximum_targets'])==sorted(word_edges(s)[1] for s in A['maximizers']),'all maximizer sets')
        check(max(b['depth'] for b in box['rows'])==author['maximum_height']==A['max_entrance'],'global F depths')
        check(max(b['K_depth'] for b in box['rows'])==author['K_maximum_height'],'global K depth')
        check(sum(bool(b['predecessors']) for b in box['rows'])==author['image'],'complete image size')
        check(sorted(Counter(len(b['predecessors']) for b in box['rows']).items())==[tuple(x) for x in author['fibre_histogram']],'all fibre histogram bins')
        check(sorted(Counter(b['depth'] for b in box['rows']).items())==[tuple(x) for x in author['height_histogram']],'all height histogram bins')
        if n>=5:
            check(edges_key(author['sharp_witness_diagonals'])==from_mask(box['witness']),'witness identity')
            check([edges_key(s) for s in author['sharp_witness_full_orbit']]==[from_mask(s) for s in box['witness_full_orbit_to_core']],'every witness orbit state')
        else:
            check(author['sharp_witness_diagonals'] is author['sharp_witness_full_orbit'] is None,'small-size absent witness')
        check(set(author)=={'n','states','image','core_diagonals','maximum_height','maximum_fibre','all_maximum_targets','fibre_histogram','height_histogram','K_maximum_height','sharp_witness_diagonals','literal_transition_depth_fibre_sha256','sharp_witness_full_orbit','complete_graph_and_sources'},'all author box fields handled')
        check(set(A)=={'n','states','max_entrance','max_fibre','maximizers','rows'},'all A box fields handled')
        reports.append({'n':n,'states':len(byedges),'all_author_and_A_scientific_fields_equal':True})
    after={k:{'path':str(p),'sha256':sha(p)} for k,p in FILES.items()}
    check(before==after,'complete consumed JSON pins unchanged')
    print(json.dumps({'status':'PASS','checks':CHECKS,'boxes':reports,'before':before,'after':after,
      'excluded_nonscientific_top_fields':'role/status/representation/box-label text and implementation-specific assertion counts; no scientific per-state or aggregate author/A field excluded.'},sort_keys=True,indent=2))
if __name__=='__main__':main()
