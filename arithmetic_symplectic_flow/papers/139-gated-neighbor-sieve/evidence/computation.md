# Exact temporal-prefix checks — ANG-20260914-GNS01

**Date:** 2026-09-14.  
**Status:** STOP / FORK — PRIME READOUT AND REVERSIBILITY PROVED; PERIOD 4 EXCLUDED; PERIOD 8 OPEN AT THE SEARCH CAP.

## Inputs and limits

The input is exactly the formula frozen in the [candidate card](../candidate-card.md).
Temporal periods are tested in order T=4, then T=8, without a rule change.
Coordinates are integer-labelled from 2. The spatial limit is 16, as frozen
in the card. Before execution the search additionally declares CAP=100000
stored prefixes; it stops on creating extension number 100001, before
continuing that stage. No probabilistic pruning or precision tolerance is
used. The cap is a resource stop, never an unsatisfiability certificate.

The t-th bit of each integer encodes the temporal value at t modulo T.
Every divisor in G is tested using exact integer division and integer square
root. At each completed step all possible next temporal words satisfying
that coordinate's equation are retained. The higher spatial boundary is
free: no value at a higher coordinate is inserted as a cutoff convention.
Had the search reached equation 16, it would test existential extension
without storing coordinate 17. Neither run reaches that spatial limit.

Both commands below were executed from
/root/autodl-tmp/hilbert-polya-structure/arithmetic_symplectic_flow.
Python standard-library integer arithmetic is the only computation; no
prime table, external solver, supplied prime mask or other file is input.

## Command 1 — forced/free-bit enumeration

```bash
python - <<'PY'
from math import isqrt
CAP=100000
for T in (4,8):
    mask=(1<<T)-1
    def temporal(w):
        return (((w<<1)&mask)|(w>>(T-1))) ^ ((w>>1)|((w&1)<<(T-1)))
    roots=[w for w in range(mask+1) if temporal(w)==mask]
    states=[(a,b) for a in roots for b in range(mask+1)]
    print('T',T,'CAP',CAP,'u2_words',roots,'initial_prefixes_2_to_3',len(states))
    for n in range(3,17):
        nxt=[]; admissible=0; extensions=0; maxfree=-1; capped=False
        for st in states:
            g=mask
            for d in range(2,isqrt(n)+1):
                if n%d==0: g &= mask ^ st[d-2]
            w=st[n-2]; A=st[n-3]^w; E=temporal(w)^g
            if E & (mask^A): continue
            admissible += 1
            free=mask^A; maxfree=max(maxfree,free.bit_count())
            if n==16: continue
            base=(w^E)&A
            subset=free
            while True:
                nxt.append(st+(base|subset,)); extensions+=1
                if len(nxt)>CAP:
                    capped=True; break
                if subset==0: break
                subset=(subset-1)&free
            if capped: break
        print('equation_n',n,'input_prefixes',len(states),'admissible',admissible,'extensions',extensions,'max_free_bits',maxfree,'capped',capped,'free_boundary_existential',n==16)
        if capped or not admissible or n==16: break
        states=nxt
PY
```

Full output, exit code 0:

```text
T 4 CAP 100000 u2_words [3, 6, 9, 12] initial_prefixes_2_to_3 64
equation_n 3 input_prefixes 64 admissible 32 extensions 132 max_free_bits 4 capped False free_boundary_existential False
equation_n 4 input_prefixes 132 admissible 24 extensions 52 max_free_bits 2 capped False free_boundary_existential False
equation_n 5 input_prefixes 52 admissible 16 extensions 36 max_free_bits 2 capped False free_boundary_existential False
equation_n 6 input_prefixes 36 admissible 4 extensions 4 max_free_bits 0 capped False free_boundary_existential False
equation_n 7 input_prefixes 4 admissible 4 extensions 16 max_free_bits 2 capped False free_boundary_existential False
equation_n 8 input_prefixes 16 admissible 0 extensions 0 max_free_bits -1 capped False free_boundary_existential False
T 8 CAP 100000 u2_words [51, 102, 153, 204] initial_prefixes_2_to_3 1024
equation_n 3 input_prefixes 1024 admissible 192 extensions 2052 max_free_bits 8 capped False free_boundary_existential False
equation_n 4 input_prefixes 2052 admissible 216 extensions 2340 max_free_bits 5 capped False free_boundary_existential False
equation_n 5 input_prefixes 2340 admissible 336 extensions 5356 max_free_bits 5 capped False free_boundary_existential False
equation_n 6 input_prefixes 5356 admissible 796 extensions 11892 max_free_bits 5 capped False free_boundary_existential False
equation_n 7 input_prefixes 11892 admissible 1996 extensions 28000 max_free_bits 5 capped False free_boundary_existential False
equation_n 8 input_prefixes 28000 admissible 4928 extensions 69664 max_free_bits 5 capped False free_boundary_existential False
equation_n 9 input_prefixes 69664 admissible 5250 extensions 100001 max_free_bits 8 capped True free_boundary_existential False
```

The final T=8 line is deliberately partial. Its admissible and extension
counts must not be read as complete counts for equation 9. Earlier uncapped
lines are exhaustive prefix counts, not counts of infinite periodic states
or primitive cyclic packets.

## Command 2 — direct period-four extension check and full certificate

This implementation computes cyclic shifts by explicit temporal bit lists
and scans every possible next word, rather than generating forced/free
submasks. Its direct equation check cross-validates the first method at T=4.

```bash
python - <<'PY'
from math import isqrt
T=4; mask=15
def temporal(w):
    bits=[(w>>t)&1 for t in range(T)]
    return sum((bits[(t+1)%T]^bits[(t-1)%T])<<t for t in range(T))
def residual(st,n):
    g=15
    for d in range(2,isqrt(n)+1):
        if n%d==0: g &= 15 ^ st[d-2]
    w=st[n-2]
    return st[n-3]^w,temporal(w)^g
states=[(a,b) for a in range(16) if temporal(a)==15 for b in range(16)]
for n in range(3,8):
    nxt=[]
    for st in states:
        A,E=residual(st,n)
        for v in range(16):
            if A&(v^st[n-2])==E: nxt.append(st+(v,))
    states=nxt
    print('direct_enumeration_equation',n,'prefix_count',len(states))
print('certificate_columns: u2 u3 u4 u5 u6 u7 u8 ; A8 E8 forbidden_mask')
for st in states:
    A,E=residual(st,8)
    print(*st,';',A,E,E&(15^A))
assert len(states)==16
assert all(residual(st,8)[1]&(15^residual(st,8)[0]) for st in states)
print('CERTIFIED: all 16 surviving prefixes fail equation 8, independently of u9')
PY
```

Full output, exit code 0:

```text
direct_enumeration_equation 3 prefix_count 132
direct_enumeration_equation 4 prefix_count 52
direct_enumeration_equation 5 prefix_count 36
direct_enumeration_equation 6 prefix_count 4
direct_enumeration_equation 7 prefix_count 16
certificate_columns: u2 u3 u4 u5 u6 u7 u8 ; A8 E8 forbidden_mask
3 3 15 0 15 3 0 ; 3 12 12
3 3 15 0 15 3 1 ; 2 6 4
3 3 15 0 15 3 2 ; 1 9 8
3 3 15 0 15 3 3 ; 0 3 3
6 6 15 0 15 6 0 ; 6 9 9
6 6 15 0 15 6 2 ; 4 12 8
6 6 15 0 15 6 4 ; 2 3 1
6 6 15 0 15 6 6 ; 0 6 6
9 9 15 0 15 9 0 ; 9 6 6
9 9 15 0 15 9 1 ; 8 12 4
9 9 15 0 15 9 8 ; 1 3 2
9 9 15 0 15 9 9 ; 0 9 9
12 12 15 0 15 12 0 ; 12 3 3
12 12 15 0 15 12 4 ; 8 9 1
12 12 15 0 15 12 8 ; 4 6 2
12 12 15 0 15 12 12 ; 0 12 12
CERTIFIED: all 16 surviving prefixes fail equation 8, independently of u9
```

Each nonzero forbidden mask identifies temporal bits on which the right-hand
gate is zero while the required residual is one. No choice of u9 repairs
that row. Since every possible prefix has been enumerated, the finite
subsystem excludes a full state fixed by R to the fourth power. This is a
finite contradiction proof, not extrapolation from finite periodic behavior.

## Reproduction boundary

The commands are complete as executed, and their outputs are preserved in
this file. This is a same-author second implementation check, not independent
peer review. No external source theorem or numerical solver certificate is
assumed. The period-eight calculation remains incomplete, irrespective of
the exactness of each completed finite operation.
