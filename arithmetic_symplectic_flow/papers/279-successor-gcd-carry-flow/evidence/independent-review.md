# Independent internal review — successor–gcd–carry flow

**Candidate:** `ANG-20260920-SGC01`  
**Status reviewed:** `OWNED ARITHMETIC CARRY CLOCK; EXTRA PRIME-TWO PACKET — STOP / FORK`  
**Review verdict:** PASS for the accuracy of the scoped mathematical record; the candidate's prime-single-packet target FAILS.  
**Review type:** internal model review, not external peer review or formal verification.

## 1. Scope, inputs and actual review sequence

The inputs are the complete [frozen card](../candidate-card.md) and
[manuscript](../paper.md), with the full arithmetic state and all branches
retained. No clock or return theorem was inherited from 278 or another owner.

- Version-1 card SHA256:
  `440e90ebb6f3c4e3531b24d8a241df8184f6687f0db2d81ebf94b633affefcc7`.
- Compared 357-line manuscript SHA256:
  `0749940501fb24daadadab2ab01350f7ff591b796918d964a2821a98d002c816`.

Any later appended administrative outcome is outside the original frozen
input; the version-1 byte prefix remains the card binding.

The ARS three checkpoints were performed in this order:

1. Read only the raw card, verify its hash, derive the local arithmetic
   and full-state dynamics. The extra prime-two primitive was reported
   immediately when found, before manuscript reading. Complete only the
   other precommitted domain, all-state, control and closure checks.
2. After communicating those raw results, read the entire manuscript
   and compare its actual hash and claims with the independent derivation.
3. Recheck the strongest adverse possibilities, especially packet merging,
   restricted inverse domains, noninteger states and topology overclaims.

No numerical run, orbit census, new family, rule repair, source deletion,
coarse-quotient classification or T3 investigation was performed. The
companion architecture/scout records were not reviewed. The manuscript's
concrete groupoid proof was checked directly; its Sims terminology citation
is not presented here as a new bibliographic audit or an imported operator
theorem. Only this independent-review file is authored by the reviewer.

## 2. Checkpoint 1 — complete raw-card findings

### Exact domains, images and owned clock

Integer multiplication is injective on K: reducing `ax=0` modulo am
forces x=0 modulo m for every m. Its image is the kernel modulo a;
compatible divided residues construct the inverse on that kernel. Haar
scaling `h(b+aB)=h(B)/a` follows first on residue cylinders and then on
all Borel sets. These arguments do not require K to be an integral domain.

| Branch at n | Domain | Exact image | Restricted inverse | Forward IMAGE J |
| --- | --- | --- | --- | --- |
| CARRY | −1+nK | whole K at n | ny−1, y in K | n |
| SUCCESSOR, legal j | j+nK | j+1+nK at n | y−1 on that image | 1 |
| GCD, d=gcd(n,j)>1 | j+nK | j/d+(n/d)K at d | dy on that image | d |

The branches are exhaustive and disjoint with the frozen priority. Each
is a homeomorphism onto a clopen image. Carry supplies a preimage ny−1
for every seed at every root, so T is onto, unlike the preceding owner.
It is not injective: seeds 0 and n−1 both map to seed 1 at root n.
There is no GCD branch at n=2. The requested checks give −1→0→1,
T(2,1)=(2,1), and T(6,2)=(2,1); the last branch's image is only 1+3K.

Y is locally compact Hausdorff, second countable and noncompact. Its
rootwise measure is Radon, sigma-finite, full-support and non-atomic.
A finite inverse branch has affine formula `theta_alpha(y)=a_alpha y−b_alpha`,
but only on its actual terminal clopen domain U_alpha. Here a_alpha is
the product of carry and GCD divisors, and b_alpha is a nonnegative integer.
For Borel B in that domain, its image has measure h(B)/a_alpha.

Two branches can be paired only on clopen subsets of the intersection
of their terminal domains in the same root. The IMAGE orientation gives

    J=a_beta/a_alpha,       c=log a_alpha−log a_beta

for the arrow `theta_beta(y) → theta_alpha(y)`. This is not a forward
algorithm-time convention. A forward branch with expansion e has clock
−log e; its insertion arrow has +log e. Successor has clock zero.

Retained lag makes presentation independence explicit: two deletion-length
pairs for one arrow differ by a common amount. Extending along the common
terminal branch multiplies both factors equally. Aligned compositions
give the cocycle law. Arbitrary terminal residue cylinders give the full
arithmetic topology; the locally constant formula and full support fix
the continuous image-density version even at null points. The resulting
real extension has complete jointly continuous time translation on all
objects and arrows. No unrestricted affine or translation arrows occur.

Haar uniqueness is conditional on additive source homogeneity and the
separately fixed root masses. Translation by 1 is not a T symmetry:
at (2,0), TR_1 gives (2,1), while R_1T gives (2,2). In fact (2,1) and
(2,2) have no actual tail arrow between them, so even this translation
cannot be silently adjoined to the existing groupoid.

### The decisive failure and complete full-state ledger

The first discriminating failure is exact, with no census:

    (2,1) → (2,1),             (2,2) → (2,3) → (2,2).

Both primitive cycles contain one factor-2 carry. They have disjoint
forward tails, different least lags and the same least clock log 2.
The second is an additional primitive packet, not a repetition of the
first. Root confirmed the same independent result and retained the rules.

A periodic orbit cannot contain GCD descent, so its modulus is constant.
The inverse of a nonempty periodic word with r carries is `n^r x−b`,
with b a positive integer. For r=0 a fixed point is impossible. For r≥1,
the equation `(n^r−1)x=b` forces an ordinary integer seed: whenever
`ax=b` in K with integer a>0 and b, reduction mod a forces a|b and
injectivity forces x=b/a. This establishes the needed rational-intersection
fact without a false integral-domain assumption or added rational arrows.

Every nonpositive integer increases strictly until positive, and positive
seeds stay positive. Modulus descent occurs only finitely often. Once the
modulus stabilizes, a block through the next carry sends a positive integer
x to `floor(x/n)+1`. For n≥3 repeated carries reach the cycle 1,...,n−1.
A composite n would encounter a proper-divisor residue there, contradicting
stability. For n=2, integers ≤1 enter the fixed point 1, while integers ≥2
enter the cycle 2,3. This proves the complete periodic classification.

| Eventual full-state tail | Base isotropy lags | Isotropy clock | Least positive time |
| --- | --- | --- | --- |
| C_p at prime p≥3, seeds 1,...,p−1 | (p−1)Z | r(p−1) maps to r log p | log p |
| C_2^a, seed 1 | Z | r maps to r log 2 | log 2 |
| C_2^b, seeds 2,3 | 2Z | 2r maps to r log 2 | log 2 |
| No periodic tail | trivial | zero | none |

Every integer state enters one of these tails. Conversely, every inverse
branch takes integers to integers, so no noninteger seed can become
eventually periodic. The last row is exactly the noninteger-seed locus.
The clock is injective on every nontrivial base isotropy group; all
fixed-object extension isotropy groups are therefore trivial. There is
one actual arrow/time packet for each listed cycle, including BOTH at 2.
Transient phases cancel from the clock but do not identify distinct tails.
For example (6,2) enters C_2^a, while (6,4) enters C_2^b.

The complete returning locus is the integer-seed locus: countable, dense
and Haar-null, not the whole source. Nonintegers remain conull and retained.
At root 2, the all-carry word has fibre `1+D_2`, where `D_2=intersection_r 2^r K`.
This is an uncountable fibre. Only its seed 1 actually returns, because
`(2^r−1)(x−1)=0` forces x=1. Word periodicity is not state isotropy.

### Closure and precommitted controls

On a prime root, `B_d(y)=p y−d`, 1≤d≤p, is an actual inverse block
with d−1 successors and one carry. N such blocks applied to 1 yield
all integers in

    [(p−p^N)/(p−1), ((p−2)p^N+1)/(p−1)],

a consecutive interval of length p^N. Pairing their N-carry tails with
N turns of the seed-1 cycle gives zero-clock arrows. These intervals
exhaust Z for p>2 and Z_{≤1} for p=2; applied to seed 2 at root 2,
the corresponding intervals [2,2^N+1] exhaust Z_{≥2}. Each increasing
union is dense in K: long enough intervals meet every residue class.
Adding cycle isotropy
gives closure, within the corresponding prime-root component, equal to
`K × (u+log p Z)`. The reverse inclusion follows from the closed clock
lattice on every arrow between states at that prime root.

Thus periodic extension orbits are not closed and the full coarse
quotient is not T1. This does not itself exclude a Hausdorff circle as
a subspace. No full quotient classification or circle theorem is needed.

SOURCE-OFF has one least-log-n packet for each n≥3 and still TWO at 2.
The 4-packet is not a 2-packet repetition. PREDICATE has one packet for
each n in A with n≥3, and again the same two packets at 2. Excluded
integer trajectories reset to root 2; nonintegers cannot become integers
through that seed-preserving reset. Generic encodability thus persists,
but does not remove the multiplicity failure. UNIT-ROOF merely counts
algorithmic lag and supplies no invertible classical suspension of T.

## 3. Checkpoint 2 — manuscript comparison

Only after all raw findings above were communicated was the 357-line
manuscript read. Its actual SHA matched §1. The local branch table,
inverse-domain restrictions, IMAGE sign and cocycle agree with the raw
derivation. Lemmas 4–5 and Theorem 6 correctly distinguish periodic
states from eventual basins, ordinary integers from arbitrary seeds,
least lag from least clock, and primitive packets from repetitions.

The manuscript preserves the two prime-two packets in the main ledger
and in BOTH altered-rule controls. Its direct proof of non-T1 uses the
already established integer basin and cycle-clock cancellation; this is
shorter than the explicit inverse-block construction and is sufficient.
It makes no inference ruling out circle embeddings. The naturalness,
classical-owner and T3 limits remain explicit. No manuscript correction
was requested after this comparison.

## 4. Checkpoint 3 — final adverse review and disposition

The final checks tested possible escape routes from the negative result:

- **Merge equal clock lengths:** invalid. Seeds 1 and 2 at root 2 have
  disjoint full-state tails. The second traversal of the seed-1 packet
  has time 2 log 2, whereas the second primitive has least time log 2.
- **Ignore integer or null states:** invalid for the frozen full owner.
  The bad packet is intrinsic and cannot be deleted by an a.e. reduction.
- **Credit periodic words instead:** invalid. Noninteger all-carry seeds
  explicitly demonstrate why the full-state return equation is required.
- **Enlarge inverse domains or arrows:** invalid. GCD images and terminal
  intersections are restricted; affine formulas do not justify a larger
  action, different stabilizers or a merger of the two cycles.
- **Use onto as invertibility, or lag as physical time:** invalid. T has
  multiple preimages, and the two distinct least lags share one least clock.
- **Overstate topology or naturalness:** unsupported. Non-T1 does not prove
  absence of circle subspaces, and conditional Haar uniqueness does not
  select the entire source program or defeat its predicate comparator.

No blocking or nonblocking mathematical correction to this failure record
is requested. The decisive candidate obstruction is the extra prime-two
primitive, so **STOP / FORK** is warranted. The full source/index result
may be retained, but not promoted as a prime-single-packet construction.
No special rule at 2, retiming, seed deletion, T3 or Route-B rescue follows.

The reviewer, root and two bounded auxiliary checks used the same inherited
model and shared project context. Auxiliary work covered raw local branches
and prime-root closure, not a separate manuscript review. Raw derivation
preceded manuscript reading, but root communications and later comparison
were not blind. ARS provided staged review discipline, not independent-error
guarantees. This is internal corroboration, not external peer review or
formal proof verification.
