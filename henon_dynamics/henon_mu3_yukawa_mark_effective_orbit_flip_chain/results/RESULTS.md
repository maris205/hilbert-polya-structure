# C86 results

Canonical evidence SHA-256:
`7b3e2179590c3dc8662a59f1d79ffbb12f2a4a787438a6902d6c28b2842e70b8`.

The faithful order-1920 label action partitions all `65536` support masks
into `3024` orbits.  One-label toggling gives an exact strong quotient with
row sum `16`, `30240` nonzero directed arcs, and `15120` unoriented orbit
pairs.  The neighboring-orbit-count spectrum is

```text
7:128, 8:384, 9:480, 10:800, 11:864, 12:336, 13:32.
```

Positive quotient entries have multiplicity spectrum

```text
1:19296, 2:7344, 3:1008, 4:1584, 5:1008.
```

Orbit-size weighted detailed balance holds on every arc.  Aggregating actual
cube edges by repair distance gives the symmetric flow matrix

```text
445696  40704      0      0
 40704 469376  13184      0
     0  13184  24064    640
     0      0    640    384
```

The repair-zero diagonal entry `445696` exactly recovers C82's ordered
distance-one full-core autocorrelation.  The complete invariant spectrum is
`16-2k` with multiplicities

```text
1,7,27,73,151,252,352,424,450,424,352,252,151,73,27,7,1.
```

Its dimension is `3024`, first spectral moment is `0`, and second spectral
moment is `77760`.
