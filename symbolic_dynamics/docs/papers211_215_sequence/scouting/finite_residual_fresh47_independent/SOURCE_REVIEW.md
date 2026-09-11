# Independent bounded test: source review before execution

Reviewer/author: `current_round_independent_scout`, 2026-09-11.
Root explicitly authorized an independently written/reviewed small-word
counterexample search. The proof was read before this test was written;
this is not a blinded test or an independent theorem-development claim.

`pressure.py` is a new implementation, not an execution of the author's
embedded proposal. Its literal step uses maximal groups; its statistic
builds tree vertices and computes distances by longest common prefixes,
rather than reducing all suffixes. The source has been read in full before
execution. The loop bounds are fixed to (1,8), (2,8), (3,7), totaling 3800
input words. Every literal nonterminal step loses at least two letters;
failure exits with its actual witness. Checks cover all orbit transitions,
including terminal detection, both schedule inequalities, endpoint length,
normal form and exact clock. A zero conditional count is not counted as
evidence for the second inequality in that box. No inverse test is claimed.

The only imports are Python standard-library itertools and json. Execution
uses `python3 -I -S`, with ordinary trusted-runtime semantics, not a pinned
installed-dependency closure or a source-only interpreter certification.
The program accesses no files or network, accepts no parameters, and writes
only stdout. Shell redirection records full stdout/stderr in this owned
directory. Source and raw output are retained; no random or enlarged run
is authorized by this note. Finite agreement cannot prove the theorem.

Planned exact command (workspace root working directory):

```sh
python3 -I -S docs/papers211_215_sequence/scouting/finite_residual_fresh47_independent/pressure.py > docs/papers211_215_sequence/scouting/finite_residual_fresh47_independent/stdout.txt 2> docs/papers211_215_sequence/scouting/finite_residual_fresh47_independent/stderr.txt
```

No result is asserted in this pre-execution source review. Execution status
and interpretation will be recorded separately without altering this note.
