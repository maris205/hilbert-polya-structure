# Actual replay record

Date: 2026-09-05 UTC. Workspace root:
`/root/autodl-tmp/symbolic_dynamics`.

Command, independently executed in two fresh interpreters:

```sh
python -B docs/papers204_208_sequence/scouting/algebra_third/pilot.py
```

Both executions exited zero. Their complete captured stdout was identical:
34 LF-terminated JSON lines, 15,182 bytes, no timestamps. The actual first
stdout was saved without normalization as `PILOT_CANONICAL.jsonl` using
`apply_patch`. The second stdout was compared before saving. These are
author reruns, not an independent review. Development execution also
exited zero; it is not counted as the required fresh pair.

A further actual shell-level byte comparison was executed:

```sh
cmp docs/papers204_208_sequence/scouting/algebra_third/PILOT_CANONICAL.jsonl <(python -B docs/papers204_208_sequence/scouting/algebra_third/pilot.py)
```

It exited zero with empty stdout. The script has no input files, random
seed, third-party dependency, current-date dependence or imported project
code. It fixes every parameter in `main()`. Python `-B` avoids creation of
bytecode files; only the script and interpreter/standard library determine
the result. Group elements use lexicographic permutation indexing, with
identity index zero, and composition acts rightmost first.

Built-in controls compare all-target HN inverse counts, all-target EG
centralizer/conjugacy counts, all-target ND ordered-product counts, and
LV's output-sum constraint. A `structural_control: PASS` field refers only
to those stated controls. ST and RC fields explicitly say `not_claimed`.
Generic cycle/depth accounting assertions run for every map and box.
The broader narrow deductions in the proof notes are deductive work, not
falsely described as additional script assertions.

The directory-relative nonself manifest is checked after all packet files
are written. It does not include itself and makes no claim about central
batch state or unrelated historical manuscripts.
