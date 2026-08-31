# Exact control results

## Canonical command

```sh
cd /root/autodl-tmp/symbolic_dynamics/papers/130-crossing-component-fibre-geometry
python3 code/verify.py | cmp - code/verification_output.txt
```

Result: **PASS**, byte-identical canonical stdout.

The command was rerun from the stable round-two snapshot with
`PYTHONDONTWRITEBYTECODE=1`; fresh stdout again matched the canonical file
byte for byte.  The verifier and canonical transcript were not edited.

## Exhaustive scope

- all rooted chord matchings for `0<=n<=7`;
- 146,600 states, including the empty state;
- 626 noncrossing targets;
- 146,600 independently reconstructed sources;
- **735,609 assertions**.

Per-size state counts are
`1,1,3,15,105,945,10395,135135`; target counts are
`1,1,2,5,14,42,132,429`.  Connected counts are
`c_1..c_7=1,1,4,27,248,2830,38232`, and transformed factors are
`a_0..a_7=1,1,2,8,52,464,5184,68928`.

## Independent checks made

1. Generate matchings without importing scouting code.
2. Construct crossing graphs and component supports from the literal
   alternation rule.
3. Check that component supports form a noncrossing partition.
4. Apply consecutive pairing and check noncrossing image plus idempotence.
5. Extract sibling groups from every source and check same-parent and local
   noncrossing conditions.
6. Generate noncrossing set partitions independently from restricted-growth
   strings and check Catalan totals.
7. Compute the formal transform coefficients and check `A=1+C(uA)` through
   degree seven.
8. For every target, construct all local sibling partitions and every
   connected decoration, then compare the reconstructed source set exactly
   with the exhaustive fibre; injectivity and surjectivity are separate
   assertions.
9. Check pointwise products, mass, Garden counts, strict
   supermultiplicativity, rainbow fibre one and unique consecutive maximizer.

## Interpretation

The verifier deliberately checks the inverse in both directions, not merely
the known aggregate counts.  It remains finite falsification evidence.  The
all-size proof is Theorem 2.1 in `main.tex`.

## Frozen control and round-two hashes

- `code/verify.py`:
  `abd519009e877fa1fa98ece4e6cc290a5fb55bda47f07d4e79b9ccad43568a3d`
- `code/verification_output.txt`:
  `89b6142c21feac945f9d0dd362b5edf78aed78530596330be0c237e9088d60b4`
- fresh stdout:
  `89b6142c21feac945f9d0dd362b5edf78aed78530596330be0c237e9088d60b4`
- round-one `main.tex` (historical):
  `199e28d4f91d945234e57c375e04fc5679f414c56613122223721069c08defb6`
- round-one `main_round1.pdf` (historical):
  `6580b2822113677f5256d0dffcd95b8048e2c0fe6442d434e9fd4b28a1b9a0cb`
- round-two `main.tex`:
  `70f020aa1b89353b94f76b781bee19e6c6fbc2d56824431d95090e3e4fcb033a`
- round-two `main.pdf` = `main_round2.pdf`:
  `c5a4fd3976a733c62a7f8f4e90b773cc6300970b9a25ac95b33f68a491f9c3fa`

Review B's two repairs alter only exposition and firewall precision.  The
assertion total, verifier bytes and canonical transcript bytes remain fixed.
