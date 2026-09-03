# P168 improvement and closeout log

## Hostile Review A

Review A returned `ACCEPT_INTERNAL / PROVABLE AS STATED` with
`0 Critical / 0 Major / 0 Minor`.  Its independent coordinate-model and BFS
control made 82,955 assertions.  No theorem, proof, source, bibliography,
verifier, PDF, ownership boundary, or lifecycle repair was requested.

## Hostile Review B

Nonauthor Review B again returned `ACCEPT_INTERNAL / PROVABLE AS STATED`
with `0 Critical / 0 Major / 0 Minor`.  In addition to two exact author
replays, it retained two independently implemented controls:

- a primitive-companion/projective-point engine with 1,493,371 assertions;
- a coordinate-incidence join/kernel engine with 73,983 assertions.

Both replayed byte-identically.  Review B also reproduced the PDF in two
fresh source-only directories and passed all five-page visual, bounding-box,
font, metadata, anonymity, and lifecycle checks.

Because neither review found a defect, the closeout creates byte-identical
`main_round1.pdf` and `main_round2.pdf` provenance copies of the immutable
Round-0 artifact.  No manuscript source, theorem formula, author executable,
or canonical PDF changes.  The final checksum manifest is regenerated only
after those copies and both reports are present.  External status remains
`GREEN_OWNER_THIN / HOLD_EXTERNAL`.
