# P143 exact control transcript

Command:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p143.py
```

Frozen stdout:

```text
P143 EXACT CONTROL
columns=n,states,preorders,fixed_equivalences,strict_2cycle_states,min_fibre,max_fibre
1,2,1,1,0,2,2
2,16,4,2,2,2,5
3,512,29,5,24,8,24
4,65536,355,15,340,16,600
assertions=265050
P143_THEOREM_INTERFACES_PASS
```

The run is exhaustive over all (2^{n^2}) Boolean matrices for (1\le n\le4).  It checks theorem interfaces and the fibre formula independently of the manuscript proofs.  It is counterexample pressure, not proof or novelty evidence.

## Independent labelled-embedding lane

The separate program “verify_p143_embeddings.py” imports no code from the
main verifier and never calls the inclusion--exclusion evaluator.  It
enumerates labelled maps into the Boolean lattice, tests preservation and
reflection directly, expands every map class by class to a source matrix, and
compares the resulting source set with the direct fibre for every preorder
target through size four.  It then tests every one of the 219 labelled
four-element posets in a five-coordinate Boolean host.

Frozen fingerprints:

- 14,835,086 direct embedding candidates;
- all 66,066 source matrices through size four matched bijectively;
- 10,450,918 isotone maps and 863,040 induced maps in the B5 lane;
- 13,238,845 exact assertions;
- canonical stdout in “embedding_verification_output.txt”.

Both transcript files have byte-comparison replay commands in README.md.
Neither lane is proof or ownership evidence.
