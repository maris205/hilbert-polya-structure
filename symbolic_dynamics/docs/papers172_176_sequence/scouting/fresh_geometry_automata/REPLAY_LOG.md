# Canonical replay log

**Runtime:** Python 3 standard library, `PYTHONDONTWRITEBYTECODE=1`  
**Replay date:** 2026-09-03 UTC  
**External status:** `HOLD_EXTERNAL`

## Command

```bash
PYTHONDONTWRITEBYTECODE=1 python3 \
  docs/papers172_176_sequence/scouting/fresh_geometry_automata/verify_breadth.py \
  > /tmp/fresh_geometry_automata.txt
```

## Fresh-process identity

The canonical-generation process and an independent second process produced
byte-identical transcripts:

```text
run A SHA-256: 390a644edc00d5dc00d79cce4471f363976f748a21c0d0f085654abca8e54809
run B SHA-256: 390a644edc00d5dc00d79cce4471f363976f748a21c0d0f085654abca8e54809
cmp exit:        0
canonical bytes: 17,438
canonical lines: 152
```

The transcript contains 147 parameter-box rows representing 18 literal maps
and ends with:

```text
SYSTEMS 18
ASSERTIONS 1066283
RESULT PASS
```

## Exact scope highlights

- every set partition through `n=9` for `D01` and `D18`;
- every `k`-subset in the stated boxes through `p=13` for `D02`, with
  pointwise depth, period, target fibre, and pivot-set checks;
- all endofunctions/words/parking preferences through `n=6`;
- all binary subspaces through ambient dimension six;
- all perfect matchings through six pairs and all permutations through
  `S_8` for two independent permutation maps;
- all accessible binary automata through four states, all `4x4` binary
  matrices for two different updates, all graphs through six vertices, all
  labelled posets through five vertices, and all rooted labelled trees
  through seven vertices.

Byte identity proves deterministic replay of the bounded program only.  It
does not prove the all-prime theorem, literature novelty, ownership, priority,
or permission to release.
