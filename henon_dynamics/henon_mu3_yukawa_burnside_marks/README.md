# HCS-C64: table-of-marks separation of the C63 relation

Status: **PREFREEZE_IMPLEMENTED / PAPER_COMPILED / NOT_RELEASED**.

C64 follows the exact C63 rank/nullity theorem.  It reconstructs the same 16
core-free subgroup types of (G=W(E_6)), computes their integral self-mark
matrix, and shows that the C63 exterior relation is invisible to permutation
characters but visible to Burnside marks.

The (16\times16) mark matrix has rank 16 and determinant
(226492416=2^{23}3^3).  For
[
R_4=S_2+S_3+S_5+S_6-S_{11}-S_{12}-S_{13}-S_{14},
]
the mark vector is
[
(0,4,2,0,0,-2,0,20,0,0,-2,-4,2,0,0,0)^T.
]
Thus the relation is nonzero in the 16-type Burnside submodule and has mark
content 2.

The scope remains `NO_BAD_EULER_OR_ROOT_NUMBER`.  This package makes no claim
about the full Burnside ring, arithmetic resolvents, local fields, Euler
factors, or root numbers.

Entry points:

- `code/c64_mark.py`: source-rebinding producer;
- `code/c64_mark_checker.py`: independent exact checker;
- `code/c64_mark_replay_checker.py`: clean-process replay;
- `code/c64_mutation_test.py`: hostile evidence mutations;
- `results/c64_mark_evidence.json`: canonical evidence;
- `paper/main.pdf`: compiled manuscript.
