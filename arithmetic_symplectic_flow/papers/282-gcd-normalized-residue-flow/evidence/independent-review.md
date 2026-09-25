# Independent internal review — gcd-normalized residue flow

**Candidate:** `ANG-20260920-GNR01`  
**Status reviewed:** `OWNED GCD-RESIDUE CLOCK; ONLY ONE LOG-TWO PACKET — STOP / FORK`  
**Verdict:** PASS for the exact full-owner mathematical record; ordinary-prime-family coverage FAILS.  
**Review type:** internal model review, not external peer review or formal verification.

## 1. Inputs, scope and actual review order

- Original [version-1 card](../candidate-card.md) SHA256:
  `bc7e24440bbadd31bcdbd2b37c2fe3b8f9709555a5ce30da859b79e47c18de2b`.
- Compared full [328-line manuscript](../paper.md) SHA256:
  `a640a3aee9a3fb9003b42f5b4aa3d5c6c53388692109521714fc902e54a3aa93`.

The raw card was read and hashed before manuscript reading. An appended
administrative outcome, if later added, is not part of that original input.
The owner is the entire frozen Y, current-gcd/residue update, rootwise Haar
measure, retained-lag groupoid and image-clock extension. Neither old seed
nor graph results are mathematical inputs to this review.

The ARS checkpoints were completed in the following order:

1. Derive the raw local owner, full-seed equation and invariant sectors.
   Report the decisive single-packet/missing-prime result immediately;
   finish only the other precommitted inverse, control and isotropy checks.
2. After all raw results were sent, read the complete manuscript and check
   its actual hash and proofs against those results.
3. Adversarially check full-state ownership, eventual tails, repetitions,
   comparator separation and possible asymptotic/topological overclaims.

No numerical census, parameter change, source expansion, new general
asymptotic theorem, coarse-topology audit or T3 work was undertaken. Older
comparison packages and the separate scouting record were not re-audited.
Only this independent-review file is authored by the reviewer.

## 2. Checkpoint 1 — independent raw-card results

### Exact local owner and clock

Multiplication by a positive integer d on K is injective: reduction of
`dx=0` modulo dm forces x=0 modulo every m. Compatible residue division
identifies its image with the mod-d kernel. The Haar identity
`h(j+dB)=h(B)/d` follows on cylinders and then on all Borel sets. This
does not require K to be an integral domain.

For fixed root (a,b), d=gcd(a,b) and 0≤j<d, the branch maps

    {(a,b)} × (j+dK)  →  {(b,(a+b)/d+j)} × K,

homeomorphically, with inverse seed j+dy. Its forward IMAGE Jacobian
is d. To describe ALL inverses of a target root (r,s), choose

    d|r,  q=r/d,  0≤j<d,
    t=s−j−q≥1,  gcd(t,q)=1.

The source root is (dt,r) and its inverse seed is j+dy, defined for
every terminal y in K. These conditions exactly enforce positivity,
the source gcd and the target equation. They introduce no seed restriction.

Every output has s≥2; conversely source (r(s−1),r), digit 0, covers
all seeds at any (r,s) with s≥2. The exact missing image is therefore
all roots (r,1)×K, which remain in Y. The coproduct is locally compact
Hausdorff and second countable; its measure is non-atomic, full-support,
Radon and sigma-finite, with infinite mass. T is locally homeomorphic,
not onto.

A finite inverse branch has seed formula `theta_alpha(y)=b_alpha+D_alpha y`,
with D_alpha the product of the actual successive gcds and
`0≤b_alpha≤D_alpha−1`. Its domain is the entire terminal root K and
its image is the appropriate initial residue cylinder. Borel scaling
is h(B)/D_alpha. Thus, for a branch-pair arrow beta→alpha,

    J=D_beta/D_alpha,       c=log D_alpha−log D_beta.

Common-tail extensions multiply both D values equally; aligning the
middle iterates proves additivity under composition. Arbitrary terminal
clopen residue subsets, not only itinerary cylinders, supply the full
groupoid topology. Actual-tail refinements and endpoint/lag separation
give the locally compact Hausdorff étale owner. The locally constant
density is the unique continuous version by full support, including
null seeds. Forward execution has −log d; insertion has +log d; d=1
has zero clock. The real extension carries complete two-sided continuous
time translation, not a positive roof or algorithmic runtime.

### Full periodic equation and elementary sectors

Once d=1, the future roots are coprime Fibonacci pairs with increasing
sum, so no periodic orbit can enter that sector. For a putative full
period, its inverse seed equation is

    x=b+D x,   D≥2,   0≤b≤D−1.

Reducing `(D−1)x=−b` modulo D−1 forces b to be 0 or D−1. Integer
multiplication is injective, so x is respectively 0 or −1. The D=2
case is included by the two-element bound. These are derived consequences,
not restrictions or chosen representatives in the source.

On seed zero the root recurrence is `(a,b)→(b,(a+b)/d)`. In a period
all d≥2. The new entry cannot exceed max(a,b), and equality at that
maximum is possible only at (2,2). A cyclic maximum argument leaves
only the fixed root (2,2). Equivalently, summing the cyclic recurrence
forces all d=2, after which periodic averaging forces both entries to 2.

On seed minus one the new entry is `(a+b)/d+d−1`. A diagonal (n,n)
goes to the coprime pair (n,n+1), so cannot occur in a period. For an
unequal pair with smaller/larger entries du<dv,

    u+v+d−1 ≤ 2v+d−2 ≤ dv.

Thus the sliding maximum cannot increase. On a hypothetical cycle it
is constant, M. From a pair (M,b<M), the output must be M; symmetry
then makes the next pair (b,M) output M again, producing the forbidden
diagonal. There is no periodic state in the entire minus-one sector.

Consequently the ONLY periodic full state is z_star=(2,2,0). It was
reported as the decisive missing-prime result before manuscript reading.
The failure is not inferred from a finite list of diagonal examples.

### Eventual tails, all-state isotropy and packets

The inverse conditions at target (2,2) leave only source (2,2), d=2,
j=0, with inverse seed 2y. Hence z_star has only itself as immediate
preimage and, by induction, no other finite preimage. This additional
argument is essential: periodic classification alone would not exclude
other eventually periodic states.

At z_star, source isotropy has lags Z and clock `k→k log 2`; its time
stabilizer is `(log 2)Z`. Every other full state has trivial source
isotropy and time stabilizer. The fixed-object extension isotropy is
trivial everywhere, since the only nontrivial source isotropy has an
injective clock. Exactly one abstract packet survives, with least time
log 2 and repetitions r log 2. All odd-prime packets are absent.

The returning locus is a single Haar-null point in the unchanged source.
For example nonzero seeds in `intersection_r 2^r K` can retain the root
(2,2) indefinitely while their seeds keep dividing by 2. They are not
additional returns. Neither a root word nor a null-state deletion can
replace the full-state equation. No circle-embedding claim is made.

### Precommitted controls

For every diagonal n>2, a formal same-root branch needs j=n−2, but its
fixed-seed equation `(n−1)x=−(n−2)` is impossible modulo n−1. On seed
minus one each diagonal immediately becomes coprime. At (2,2), seed 0
is fixed while seed 1 goes to (2,3,0), whose future is coprime Fibonacci.

GCD-OFF gives `(b,a+b,x)`: strictly increasing root sum, no periodic or
eventually periodic states, branch derivative 1 and zero clock.

FEEDBACK-OFF has the zero-sector root recurrence independently of its
seed. Its only root cycle is (2,2), where the seed map is the binary
residue shift. Exactly seeds 0 and −1 are periodic, each fixed, each
with a separately derived least-log-2 packet. Their tails never meet.
The root (2,2) has no other root preimage; its nonnegative integer seeds
enter 0 and its negative integers enter −1. Nonintegers cannot enter an
integer tail because every inverse branch preserves integer seeds.
In particular seed 1 now leads to 0 instead of exiting to (2,3).
Restoring feedback removes the minus-one primitive and changes these
prefix dynamics; it does not produce the missing odd-prime family.

## 3. Checkpoint 2 — complete manuscript comparison

After communicating every raw checkpoint finding above, the entire
328-line manuscript was read. Its actual SHA matched §1. No mathematical
correction was needed.

The exact image, finite inverse formulas and Borel clock are correctly
owned. Proposition 6's cyclic sum/difference proof for seed zero is
complete. Its minus-one equality case produces {M−2,M} and then a
diagonal, agreeing with the independent maximum argument. Theorem 7
correctly supplements periodic classification with the unique-preimage
proof before asserting trivial isotropy at all other states.

The main packet and the two comparator packets are not mixed. The
FEEDBACK-OFF pair of fixed tails is not called two phases of one packet.
The manuscript does not assert general convergence, eventual coprimality
or growth for every nonperiodic orbit. Coarse topology and circle embedding
are explicitly unclaimed. Naturalness of the chosen completion, recurrence
and time remains open despite the exact arithmetic mechanism.

## 4. Checkpoint 3 — final adverse review

The strongest potential failure routes were checked:

- **A noninteger periodic seed:** excluded by the full affine congruence
  and integer-multiplication injectivity, not by a false domain assumption.
- **A missed root cycle:** both derived seed sectors were treated globally;
  the proof does not rely on sampled roots or numerical enumeration.
- **A hidden eventually periodic state:** excluded by the unique immediate
  preimage, not by silently identifying periodic and eventually periodic.
- **A formal diagonal/root return:** the actual seed equation remains
  mandatory and rejects the n>2 diagonal word.
- **Repair by the comparator:** the two feedback-off packets belong to
  that separate owner; neither adds primes to the frozen main object.
- **Overclaim from a cyclic clock:** no ambient Hausdorffness, embedded
  circle, general asymptotic theorem or natural-A0 result follows here.

No blocking or nonblocking correction to the mathematical failure record
is requested. Its appropriate disposition is **STOP prime-family promotion
/ FORK**, while retaining the exact source and one correctly timed packet.
No retuning, seed deletion, new operator, T3 or formal Route-B rescue is
authorized or credited by this review.

The reviewer and root share the inherited model and project context.
Two same-model auxiliary raw-card checks covered the inverse/clock algebra
and the minus-one/feedback-off sectors. They did not read the manuscript.
The raw checkpoint preceded manuscript reading; subsequent communication
and comparison were not blind. ARS supplies staged scrutiny, not independent
error guarantees. This is internal corroboration, not external peer review
or formal verification.
