# Narrative report — parallel odd-vertex pruning

## One-sentence result

Simultaneously deleting all odd-degree vertices from an arbitrary labelled
graph produces a finite absorbing dynamics whose sharp clock is
`floor(n/2)` and whose complete all-time inverse geometry is governed by one
explicit nilpotent rank-transfer matrix.

## Problem and surprise

Odd-degree vertex deletion is usually encountered as a sequential game or as
an optimization constraint.  The deterministic parallel map looks like a
generic pruning rule, but its backward dynamics is unexpectedly rigid.  If a
target graph has `s` vertices and a predecessor loses `d` vertices, all free
edges lie in the connected graph formed by edges meeting the deleted set.
The requirements “old vertices even, deleted vertices odd” are therefore one
binary incidence system.  Its rank is fixed, and its consistency depends only
on `d` being even—not on a single target edge.

This target-independence is the organizing fact.  It creates an explicit
strict inverse transfer `B_n(s,m)`.  Since every strict predecessor is itself
non-even, transfer powers count literal orbit segments without correction.
The temporal theorem, image tower, and every-target fibres then become
different readings of the same rigorously justified matrix.

## Claim hierarchy

1. The centerpiece is the strict predecessor count and its target
   independence.
2. The all-time fibre theorem is the main dynamical consequence and cannot be
   replaced by a generic matrix-power remark.
3. The exact image criterion and temporal CDF are concrete corollaries.
4. The sharp path clock is visually simple but is supporting evidence, not
   the sole contribution.

## Scope boundary

Handshaking, incidence rank, cycle-space enumeration, sequential parity
games, Eulerian-deletion optimization, generic pruning, and zeta conversion
are established inputs.  The note makes no priority assertion.  Its narrow
residual is the complete simultaneous-map atlas, particularly the uniform
strict inverse and its exact powers.

## Evidence state

The symbolic proof is closed in `PROOF_PACKAGE.md`.  Exhaustive literal
construction through ambient order six checks 1,350,807 assertions, including
every target and every relevant time.  Two cold processes reproduce the
canonical transcript byte for byte with SHA-256
`690b03f65380c5f662e68ae94bdc2f2276307d50a102d3274367a6f9b902ab95`.

## Remaining pre-paper risks

- A hostile reviewer must search alternate names for parallel odd/odd
  deletion and parity peeling.
- The word “Eulerian” must not silently impose connectivity; use “even graph”
  in theorem statements.
- The `d=0` self-predecessor must remain separate from the strict transfer.
- Matrix orientation and source-rank refinement must be checked after TeX
  compression.
