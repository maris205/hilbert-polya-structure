# P146 exact control transcript

Command:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p146.py
```

Frozen stdout:

```text
P146 EXACT CONTROL
columns=n,histories,triangulations,min_H,max_H,path_dual_equalities
3,1,1,1,1,1
4,4,2,2,2,2
5,20,5,4,4,5
6,120,14,8,12,12
7,840,42,16,28,28
8,6720,132,32,112,64
9,60480,429,64,316,144
assertions=9562
P146_THEOREM_INTERFACES_PASS
```

The run enumerates all 68,185 complete deletion histories for
\(3\le n\le9\), reconstructs all 625 terminal triangulations and their
final-face refinements, asserts weak-dual connectivity, checks every
root-resolved hook count, independently evaluates the unrooted leaf-deletion
recurrence, and brute-forces rooted child-before-parent orders through
six-vertex dual trees.  It is exact falsification pressure, not a proof or
novelty certificate.  The canonical transcript is
“verification_output.txt”.
