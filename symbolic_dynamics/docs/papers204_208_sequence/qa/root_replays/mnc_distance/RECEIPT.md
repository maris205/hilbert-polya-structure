# Root distance-decoder author replay

2026-09-06 UTC. Author corroboration, not independent review or admission.
From `/root/autodl-tmp/symbolic_dynamics`, the self-contained producer
`scouting/word_local/verify_mnc_distance.py` was actually executed once
to save `MNC_DISTANCE_CANONICAL.json`, then twice afresh to this
directory's `run1.stdout` and `run2.stdout`, with stderr saved separately.
Each producer was connected by `&&` to a raw `cmp` against the saved
canonical; a final raw `cmp` compared the two fresh outputs. Combined
process session 72781 completed with exit zero. All three producers
and all three byte comparisons therefore exited zero. Both saved
stderr files are empty.

The producer is Python 3 standard-library only and reads/imports no
scientific files. SHA-256:
`0ca5ccdcdba86db2f71473309e395eeb8431e19db878cdefe3fe51d4e9024ec8`.
The canonical and both fresh raw outputs have SHA-256
`5068bbd4966afae69cf073aeb10bedff7423843fe876d5ebc9a17bebcf5847fd`.
Each reports 118,044 assertions over the original full $n=3,\ldots,9$
boxes: literal distance/minimum factor, every distance-word full inverse
set, each evaluated weight, and every target's summed count. No old
checker, author canonical or expected table is imported. The output
digest for a target vector is not substituted for actual comparisons.

The all-$n$ warrant is the deductive `MNC_DISTANCE_DECODER.md`, pinned
at this milestone to
`c42e699f5c01fee70e5272bf1600003f9cb190325c45ab64a9b478325c7815d4`.
The static walk decoder is zero-credit background. The MNC temporal
and global-extremal author package, and an independent source/value
gate, are separate obligations. Root supplied this lemma and therefore
cannot independently review an eventual MNC manuscript.
