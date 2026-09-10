# C101 source audit

C101 reads only the frozen C88 subgroup first-passage atlas, its manifest, the
C90 joint first-passage receipt, and its manifest.  The producer checks all
four authority SHA-256 digests and canonical JSON bytes before computation.
The independent checker reconstructs the closure-chain dynamic program and
all 1,140 PMFs without importing producer output.  No external literature,
finite-field data, arithmetic local data, or fitted parameters enter the
package.
