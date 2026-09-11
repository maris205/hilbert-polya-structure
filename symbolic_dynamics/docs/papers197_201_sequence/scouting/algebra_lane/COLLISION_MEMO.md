# Algebra/order/logic lane: internal collision memo

## Status language

This is a bounded internal collision audit through P196.  `NO_LITERAL_HIT`
below means only that the searched workspace did not contain the same
formula.  It is not a novelty conclusion, an owner search, or freedom to
operate.  The whole lane remains `HOLD_EXTERNAL`.

## Promoted proof spike: self-displacement difference

The nearest internal system is P178, state-selected finite differences.
The two maps must not be conflated.

| Feature | P178 | Self-displacement difference |
|---|---|---|
| carrier | all (f:\mathbb F_p\to\mathbb F_p) | the same |
| selected displacement | one global anchor (f(0)) | a separate local value (f(x)) at every site |
| literal update | (f(x+f(0))-f(x)) | (f(x+f(x))-f(x)) |
| proof engine | fixed-direction difference flag, augmentation-ideal nilpotence, anchored backward lifting, Jordan blocks | affine cocycle plus invariant graph of (L(x,a)=(x+a,2a)), projected-orbit hypergraph matchings |
| recurrent behavior | zero is the sole recurrent state; (T^p=0) | nonzero cycles already occur at (p=3); at (p=7) there are 2416 recurrent states |
| inverse mechanism | one affine lift for every nonzero direction word | power-map roots only on the affine stratum; no claimed full inverse atlas |

The carrier and the word “difference” are a real adjacency, so the gate is
`OWNER_AMBER`, not green.  Nevertheless P178's nilpotent flag proof does not
transfer after replacing its single anchor by (p) simultaneous local
directions.

The affine restriction
((a,b)\mapsto(a^2,ab)) contains ordinary finite-field powering.  All facts
coming solely from the first coordinate (a\mapsto a^2), including its
2-primary tail, receive zero contribution credit.  The residual conjunction
is the literal full-function rule, the second-coordinate cocycle, and the
global fixed-graph/orbit-packing theorem.

Other nearby firewalls are:

- P115 Cartier decimation and P157 Newton--Hensel iteration: different
  carriers and formulas, but they consume generic Frobenius/power and
  valuation arguments;
- P168 inverse-span and P178's linear difference flag: they forbid selling a
  hidden linearization as the main mechanism;
- the permanent P97--P196 ban on ordinary group/ring power maps and their
  cosmetic thickenings.

Workspace search found no literal occurrence of
(f(x+f(x))-f(x)).  Record this only as `NO_LITERAL_INTERNAL_HIT`.

## Reserve: Zadeh cyclic implication

The literal rule

\[
 T(x)_i=\max\{M-x_i,\min(x_i,x_{i+1})\}
\]

was not found in P1--P196.  Its closest selected paper is P196, whose rule is
cyclic Gödel implication on the same finite-chain word carrier.  P196 has a
one-step constrained image followed by rotation; the Zadeh rule instead has
a sharp length-(m) magnitude erosion and an independent-set sign core.
Thus there is no literal conjugacy or factor identified here.  However, the
same carrier, the same “cyclic implication” framing, the final rotation, and
the same generic local transfer-trace inverse engine make this a high-risk
near neighbor.  Its disposition is `RESERVE_NEAR_P196`, not promotion.

The generic transfer matrix and Möbius cycle inversion receive zero credit
because P187, P190, and P196 already occupy those proof surfaces.

## Hard-kill map

| Candidate | Collision or transfer | Disposition |
|---|---|---|
| Conjugation-rack CA (x_i\mapsto x_{i+1}^{-1}x_ix_{i+1}) | fixed states are cyclic commuting tuples; class-two groups reduce to central commutator increments.  P119, P135, P175 and the NL01--NL06 commutator registers consume the proof | `KILL_GROUP_WORD_TRANSFER` |
| Least-nonsquare Vieta scheduler | the scheduler does not remove the literal Markoff/Vieta involutions or their invariant cubic; AH07/AH08/MRK controls already mark this action owner-dense | `KILL_DIRECT_MARKOFF_VIETA_OWNER` |
| Constant-feedback translation of monic quadratics | after (a=2s, c=b-s^2), it is (c\mapsto c, s\mapsto s^2+s+c), a disjoint union of ordinary quadratic functional graphs | `KILL_UNIVARIATE_QUADRATIC_REDUCTION` |
| Star-Heyting cyclic implication | on this algebra (T^2=\rho T); this is exactly the one-step-core/rotation architecture isolated and zero-credited in P196, with additional P110 lattice pressure | `KILL_P196_ARCHITECTURE` |
| Fodor cyclic implication | exact pilots have depth two, but the system still makes a short compression to a rotation core on the same carrier as P196 | `KILL_NEAR_P196` |
| Gaines--Rescher cyclic implication | the first image is ({0,M}^m), and the induced rule is literally P196 at (q=2) | `KILL_FACTOR_P196_Q2` |
| Kleene--Dienes cyclic implication | the identity (T^2=\rho T) gives the same one-step-core/shift skeleton as P196 | `KILL_EXACT_ONE_STEP_ROTATION` |
| Matrix anticommutator register ((A,B)\mapsto(B,AB+BA)) | a bilinear shift register; P7, P111, P119, P175 and NL01--NL06 consume anticommutator/commutator register mechanisms | `KILL_BILINEAR_SHIFT_REGISTER` |
| Boolean elementary-symmetric coefficient map | atomwise it retains only the input weight and sends it to a Pascal row; this is a Vieta/symmetric normal-form compression | `KILL_VIETA_NORMAL_FORM_COMPRESSION` |
| Binary-projective Steiner cyclic product | its length-three slice is the literal map in retired P160; changing the cyclic length does not clear that owner | `KILL_LITERAL_RETIRED_P160` |
| Heyting meet--residuum pair | (T^2(A,B)=(A\cap B,\top)), a canonical lattice split/closure with P110/P182 transfer | `KILL_CANONICAL_LATTICE_SPLIT` |

## Gate conclusion

- Self-displacement difference: one tightly bounded proof spike may advance,
  with ordinary powering subtracted and `OWNER_AMBER / HOLD_EXTERNAL` shown
  prominently.
- Zadeh cyclic implication: retain only as a reserve unless a later sequence
  gate accepts the immediate P196 adjacency.
- Every other system in the breadth ledger is killed internally.
- No statement in this memo is an external novelty claim.
