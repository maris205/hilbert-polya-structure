# C190 exact-validation plan

## Claim matrix

| Claim | All-parameter justification | Executable regression | Failure trigger |
|---|---|---|---|
| recurrent words and rotation | Brandt attribution plus explicit convention translation | independent words versus direct full partitions | any recurrent-set or `T phi=phi rho` mismatch |
| every positive fixed iterate | index-cycle counting | all residues for every `N<=40`, directly on all partitions | any gcd/binomial or full-map mismatch |
| least periods and primitive cycles | divisor Möbius inversion | direct functional-graph cycles | negative, nonintegral, or missing population |
| full finite zeta | finite cycle decomposition | exact factor ledger and trace identities | exponent/sign/reciprocity mismatch |
| full Koopman algebraic spectrum | functional-graph block triangularization | zero multiplicity, root multiplicities, N=8 matrix | wrong degree, root total, determinant, or trace |
| recurrent reflection | index identity `Q rho Q=rho^-1` | all 757 words and every phase-labelled formula | failure of involution or conjugacy |
| triangular boundary | weight-zero specialization | every triangular `N<=40` | more than one recurrent state or nontrivial cycle |
| Route-A stop | source/scope audit | exact-map checker and semantic mutations | arithmetic, target, global-reversor, or Route-B flag changes |

## Regression domain

- Systems: every `1<=N<=40`.
- Full integer partitions constructed directly: 215,307.
- Recurrent word/partition pairs: 757.
- Direct cycles: 114.
- Positive-iterate residue rows: 248.
- Least-period divisor rows: 117.
- Root-of-unity spectral rows: 248.

The finite domain is a deterministic regression design, not a sample-based
proof of the all-`N` theorem.  Aggregate transient counts are used only to
verify the Koopman zero multiplicity.  Complete transient trees and hitting
times are deliberately not emitted.

## Independent paths

1. The producer uses combination-generated weight words and formula ledgers.
2. The checker does not import the producer.  It generates words by a Boolean
   Cartesian product, generates integer partitions by descending recursion,
   and constructs the actual full functional graph.
3. The SymPy path independently reconstructs partition numbers, binomials,
   Möbius inversion, determinant degrees, trace identities, Burnside counts,
   and an explicit N=8 operator/reversor matrix.
4. Replay requires exact byte equality.
5. Repaired-hash attacks cover all semantic layers; a stale-hash mutation
   tests the canonical payload digest.

## Release gates

- all exact programs pass;
- the baseline plus two substantively improved PDFs are pairwise distinct,
  and round 2 equals the final PDF;
- two fresh fixed-epoch builds are byte identical to the release PDF;
- fonts are embedded; final/fresh logs and rendered pages are clean;
- the self-excluded manifest contains 27 payload files, giving a 28-file
  package after the manifest is included.
