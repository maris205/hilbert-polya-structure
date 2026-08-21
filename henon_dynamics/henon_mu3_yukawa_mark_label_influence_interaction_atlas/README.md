# HCS-C87 label influence and interaction atlas

C87 resolves the frozen full-core predicate at first and second discrete
order.  It enumerates all 65536 supports, all 16 single-label derivatives,
and all 120 unordered-pair Hessians.  Unlike C73's scalar first-order
baseline, C87 retains every coalition-size swing vector, both signs of every
pair Hessian, and the faithful label/pair orbit quotient.

Headline exact values:

- `S9`: 30400 swings, Banzhaf `475/512`, Shapley `271/360`.
- `S1,S16`: 2240, `35/512`, `61/1260`.
- `S7,S15`: 2112, `33/512`, `2/45`.
- `S3,S4,S8,S11,S12`: 320, `5/512`, `31/2520`.
- six dummy labels: zero.
- all 120 pairs: 27 faithful pair orbits and ten numerical classes.
- pair-orbit size spectrum: `{1:5,2:7,4:7,5:3,8:1,10:3,20:1}`.

The pair atlas distinguishes synergy (`Delta_ij=+1`) from antagonism
(`Delta_ij=-1`) and reports exact uniform Banzhaf and factorial-weighted
Shapley pair interactions.  First-order Shapley efficiency and all sixteen
pair endpoint identities are checked exactly.  The C82 boundary bridge is
`40704+445696=16*30400`.

The producer derives `F` from C73's 25 minimal edges; the independent checker
derives it from C78's pivot-plus-four-block criterion.  A SymPy multilinear
kernel independently reconstructs all 136 coalition-size derivative rows.
Replay is byte-identical and all 27 hostile mutations are rejected.

Canonical evidence SHA-256:
`bedeb7a3d912330e5eadc72629ee24d773648993f73f20f23eaf477028334d6e`.
The complete file binding is in
[C87_PREFREEZE_MANIFEST.json](C87_PREFREEZE_MANIFEST.json).

This package makes no arithmetic/local, Euler-factor, root-number, automorphy,
full Burnside/table-of-marks, or Hilbert--Polya claim.  Scope firewall:
`NO_BAD_EULER_OR_ROOT_NUMBER`.
