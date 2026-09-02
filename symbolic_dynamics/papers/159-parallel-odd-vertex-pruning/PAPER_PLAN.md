# P159 paper plan — parallel odd-vertex pruning

**Status:** `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`  
**Frozen inputs:** `docs/papers157_161_sequence/phase1/ovp/THEOREM_CONTRACT.md`
and `PRE_PAPER_HOSTILE_GATE.md`.  The pre-paper gate is not a formal manuscript
Review A or Review B.

## One-sentence object

For the map that simultaneously deletes every current odd-degree vertex from
a labelled graph, derive the target-uniform strict inverse space and use its
correctly oriented rank-transfer powers to enumerate every temporal fibre,
image layer, and absorption-depth layer.

## Residual theorem package

1. Establish finite stabilization and the sharp `floor(n/2)` path clock as
   context, not as a contribution axis.
2. Derive the strict fibre
   `binom(n-s,d) 2^[s(d-1)+binom(d-1,2)]` for positive even rank loss `d` by
   a connected binary incidence system and prove target independence.
3. Orient the matrix with target rank as row and source rank as column; prove
   `B_n^t` for non-even targets and `I+B_n+...+B_n^t` for even targets.
4. Derive the exact time-`t` image criterion, image count, fixed count, depth
   CDF, and exact shells.
5. Expose all degenerate boundaries in theorem statements and proof text.

The paper leads with items 2–4.  Handshaking, incidence rank, cycle-space
counts, the even fixed locus, parallel-peeling vocabulary, generic matrix
powers, and the clock receive zero contribution credit.

## Section architecture

- **Abstract:** literal map, strict transfer, all-time distinction between
  non-even and even targets, image/CDF consequences, clock, and exact audit.
- **Section 1:** carrier, update, notation, source subtraction, and one
  boundary-complete theorem.
- **Section 2:** short forward proof and path witness, including `n=0,1`.
- **Section 3:** parity-extension variables, consistency, connected incidence
  rank, nullity, target independence, `d=0`, and `s=0,d=2`.
- **Section 4:** row-target/column-source multiplication, literal inverse
  chains, geometric waiting sum, image criterion, phase/fixed/image/CDF
  formulas, and nilpotence.
- **Section 5:** exact-arithmetic lanes, internal collision firewall, scope,
  limitations, declarations, and external hold.

## Proof dependency

```text
literal simultaneous update
    -> handshaking + strict rank loss -> fixed locus / sharp path clock
    -> fix target S and deleted set D
       -> connected variable-edge graph Q_{S,D}
       -> GF(2) incidence consistency and rank
       -> target-uniform strict transfer B_n
          -> unique strict inverse chains -> B_n^t
          -> early arrival only at even targets -> geometric sum
          -> positive even rank increments -> image criterion
          -> fixed-target summation -> CDF and exact shells
```

## Mandatory visible boundaries

- `d=0` is outside strict `B_n`; one same-rank preimage iff the target is
  even.
- For fixed `D` at `s=0,d=2`, the unique source is `K_2`; ambient aggregation
  is `binom(n,2)`.
- Matrix orientation is `row=target`, `column=source`, with all three `n=4`
  sentinels printed.
- `t=0` is the identity image and identity fibre, separate from the `t>=1`
  image condition.
- `n=0,1` are explicit fixed carriers with clock zero.
- “Even graph” never silently means connected; “Eulerian” is restricted to
  the cited optimization literature.

## Citation plan

- Sequential parity games: Nowakowski–Ottaway and Krüger.
- Eulerian/parity editing: Cygan et al. and Dabrowski et al.
- Generic parallel peeling: Jiang–Mitzenmacher–Thaler.
- Standard graph facts: Diestel.

Every bibliography entry has a direct owner/subtraction role.  No absence
claim is supported by a citation.

## Evidence plan

- `main.tex` carries the all-parameter proof.
- `PROOF_PACKAGE.md` expands the proof dependencies and boundary cases.
- `verify_p159.py` independently constructs tuple-based graph states and
  separately audits GF(2) systems.
- `verification_output.txt` is the unchanged frozen deterministic transcript.
- `SOURCE_VERIFICATION.md` records primary/authoritative metadata and the
  bounded non-hit without converting it into priority.

No decorative figure is required; formal Review A returned zero findings.
