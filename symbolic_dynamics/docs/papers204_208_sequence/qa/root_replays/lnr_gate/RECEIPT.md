# Root LNR candidate-gate inspection and fresh replay pair

2026-09-06 UTC. Disposition: **MATH_VALID / HOLD_SOURCE / NO_ADMISSION**.
Root read the complete original candidate gate and source audit, the author
inverse proof and source/execution record, and the independent execution
receipt. Root also read the pinned Tropp primary text at Example 6.18 and
Theorem 6.32 with its hypotheses and proof sketch. The matrix-norm
substitution applies to the stated real square matrices.

The source finding `LNR-S1` remains open. Root's earlier direct publisher
preview and author-site checks did not supply Mukherjee 2011's actual
convergence theorem. The unseen body licenses neither full overlap nor a
new sharp refinement. No numbered paper or reserve is created.

From `/root/autodl-tmp/symbolic_dynamics`, root actually ran the following
producer for each `j=1,2`, with stdout/stderr redirected to this directory:

```sh
PYTHONHASHSEED=0 python3 docs/papers204_208_sequence/scouting/word_local/LNR_GATE/verify_gate.py
```

Each fresh producer was followed through `&&` by raw `cmp` against
`scouting/word_local/LNR_GATE/CANONICAL.json`; a final raw `cmp` compared
the two outputs. The combined process session 51944 completed with exit
zero: both producers and all three byte comparators therefore exited zero.
Both complete outputs contain 3,157,633 successful assertions and are
12,257 bytes, SHA-256
`ebff1e816b557e3a1f960a0d7f12e66aae8706f2667b0d2ff07d38ca1d3fd1f6`.
Both stderr files are empty. These are new root executions, separate from
the preserved assessor pair; finite checks corroborate, not prove, the
all-parameter deductions.

Root's actual hash checks passed all six gate input pins, both inverse
context pins, all 26 gate nonself manifest entries and all 20 inverse
nonself entries. Gate manifest SHA-256:
`f277a07888096babee8e9f1c36ff1ce6a2302f295837927451ee73c15041bd4e`.
The original failed self-including manifest remains preserved and is not
called a passing manifest. No original proof, report, canonical or gate
finding was edited by this inspection. `HOLD_EXTERNAL` remains.
