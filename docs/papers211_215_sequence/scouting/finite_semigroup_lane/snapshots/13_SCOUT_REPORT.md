# Second algebra scout: six maps, one value-gate package

2026-09-05. Author: `/root/batch197_lzk_gate`.
Only this lane was written; no formal IDs, central edits, Git or external
actions. The previous algebra package's seven manifest checks were OK
before intake and that package was left unchanged.

Outcome: SI has complete deductive mathematics but its temporal engine
transfers from P167; VALUE_GATE_PENDING, not an admitted seat. The five
other maps are NO_PROMOTION recommendations. All six were piloted before
deep proof work, in 23 boxes. Both scripts have two fresh byte-identical
replays and actual canonical stdout.

| Map | Literal full carrier/update | Exact bounded signal | Disposition |
|---|---|---|---|
| SI | All f:[n]->[n]; S(f)(v)=unique preimage if present, else v for empty/multiple fibres | n=1..5. At n=5:3125 states, image560, core120, depths120/585/1520/660/240, unique max fibre456. Every-target counts and complete predecessor decoder PASS. | Proof complete; P167 split-branch adapter is explicitly subtracted. No new temporal mechanism certified. |
| HC | All f:[n]->[n]; H(f)(v)=|f^{-1}(v)| mod n | n=2..5; H=2,3,3,4. | No uniform temporal contract. Inverse is ordinary multinomial occupancy (constant inputs all give zero), hence no distinct inverse mechanism. Inventory literature is neighboring, not claimed exact owner. |
| TP | Full transformation semigroup T_n^2; (f,g)->(fg,gf), fg=f composed with g | n=2,3,4; at n=4,65536 states, core409, H5, periods1,2,4. | Evaluated Thue–Morse substitution is owned vocabulary; no all-n orbit or inverse theorem established. Do not treat low-n period powers as a proof. |
| SP | F_p^2; (x,y)->(x+y,xy) | p=2,3,5,7,11,13; last H18, core17. | Every fibre is the ordered root pairs of T²-sT+t, so the inverse axis is classical Viète/discriminant algebra. No uniform temporal theorem; reject. |
| TD | F_p[x]/(x^p); f->f f' modulo x^p | p=2,3,5; last3125 states, H7, periods1,2,3,8,20. | Derivative is well-defined because (x^p)'=0. No all-prime temporal/inverse contract; small-prime collapse is not extrapolated. |
| OT | Ordered triples in (F_p²)^3; replace each vertex by its perpendicular foot on the opposite line, retaining the departing vertex when the side norm is zero | p=3:729 states,image=core297,H1. p=5:15625 states,image=core8425,H1,600 strict8-cycles. | Regular orthic shape dynamics has an established pedal/angle-doubling neighborhood. No all-p theorem handling this zero-norm completion was proved; do not claim full power conjugacy or fill a seat with totalization effects. |

OT's exact formula in `pilot.py` uses d=c-b, norm=d_x²+d_y² and
foot(a;b,c)=b+((a-b) dot d)/norm*d when norm!=0. The declared completion
also handles repeated endpoints and isotropic nonzero directions. It is
not a map on subspaces and does not use a Galois/polarity closure.

## SI mathematics and decisive subtraction

Complete proofs: `SI_PROOF_AND_ADAPTER.md`.
The full height is n-1; first-image height max(n-2,0); the recurrent
set is S_n with inversion dynamics. For n>=3 there are 2n! deepest states.
Every first image is cycles plus loop-rooted paths. SI always splits off
the current root and reverses the rest of each path.

For any target with distinct nonfixed coordinate values, let k be its
number of fixed vertices and p its number of nontrivial path components.
Its fibre is

    N(k,p)=sum_{s=0}^{k-p} binom(k-p,s)
             sum_b {k-s brace b}_{>=2} (k-s)_b.

This counts forced unique occurrences followed by free assignments to
fixed labels, with singleton fibres allowed only at their own label.
Targets with repeated nonfixed values have zero fibre; among remaining
targets only (k,p)=(1,1) is unsupported. Identity uniquely maximizes,
with fibres 1,3,10,65,456 for n=1..5. An independent algebraic expression
within the **author-side** pilot uses rook inclusion-exclusion; the
second checker instead uses no-singleton partitions and compares all
decoded predecessor sets, not only counts.

P167 owns the same first-image component lemma and already contains the
split-root/reverse-rest branch; SI merely makes that branch unconditional.
The temporal proof therefore transfers. Conversely, SI is not a literal
P167 iterate: g=(2,0,2) is P167-periodic, whereas SI erodes it to identity.
SI's n=3 identity fibre10 also exceeds P167's Bell ceiling5, blocking
transfer of its kernel-partition injection. These differences establish
an exact adapter and its limits, **not** automatic two-axis value.

Recommendation: let an independent gate decide whether any materially
new temporal residual remains after this adapter. If none, NO_PROMOTION;
do not enlarge n to compensate. This author supplies no acceptance review.

## Artifacts and handoff

`pilot.py`, `PILOT_CANONICAL.jsonl` (23 rows),
`verify_si_structure.py`, `SI_STRUCTURE_CANONICAL.jsonl` (6 rows),
`SI_PROOF_AND_ADAPTER.md`, `SOURCE_AND_COLLISION_NOTES.md`, this report,
and `SHA256SUMS`. No numbered manuscript or frozen-paper package exists.
HOLD_EXTERNAL remains.

Final author-side verification, 2026-09-05 UTC, working directory this
package: `cmp PILOT_CANONICAL.jsonl <(python pilot.py)` and
`cmp SI_STRUCTURE_CANONICAL.jsonl <(python verify_si_structure.py)` both
returned exit 0 with empty comparison stdout. These are fresh raw-byte
replays against the two complete canonical files (23 and 6 rows), not
normalized text comparisons. The preceding first-lane manifest was
rechecked: all seven entries OK, and it was left unchanged. The current
manifest records all seven nonmanifest files in this package. This is
author-side artifact verification, not an independent candidate review.
