# C76 experiment plan

## Source binding

Read the C75 evidence and C75 prefreeze manifest byte-for-byte before doing
any enumeration.  The producer and checker bind these authorities to

```text
C75 evidence: 8beee17a227153e066907549df70c14a087b7de4141c3092d7cebd4a91541d98
C75 manifest: 7ede3e35c3101d17c683d2da440037d5bd4e002266530b52b3d1cb36ed4c8fcb
```

The C75 ambient generator `r=(2,0,0,2)` is retained as a diagnostic fact: it
has order six in the lifted ambient representation and belongs to the kernel
of the action on the sixteen labels.  It is not used to define C76 support
orbits.

## Exact enumeration

1. Recover the sixteen named coordinates and the complete twenty-subgroup
   closure table from the C75 evidence.
2. Reconstruct the five effective label permutations `z5,z2,a,c,u` and close
   them under composition.  Require group order 1920 and the recorded element
   order distribution.
3. Encode every label support as a 16-bit mask and compute `Phi(A)` by the
   exact subgroup-extension table.  Enumerate all 65536 masks.
4. Partition the masks into effective-group orbits and record representatives,
   orbit sizes, support cardinalities, and closure subgroup indices.
5. Test closure-minimality by every single-label deletion.  Repeat with the
   target fixed to the full 54-point core.

## Independent checks

The independent checker reimplements the finite-group operations and verifies
canonical JSON, authority hashes, all 20 subgroup closures, all 65536 support
assignments, the 3024-orbit partition, both minimality counts, and the exact
spectra.  A GAP cross-check verifies the 1920-element label group and reports
`C2 x S5 x D8`.  A clean replay starts a new interpreter;
the hostile audit mutates semantic fields and requires rejection.

## Claims firewall

This is an exact finite support-orbit atlas for a named presentation.  It does
not assert a full table of marks, a Burnside-ring identity, an arithmetic or
local interpretation, an Euler factor, a root number, automorphy, or a
Hilbert--Polya operator.
