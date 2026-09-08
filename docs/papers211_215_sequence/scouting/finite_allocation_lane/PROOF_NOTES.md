# MCA deductive notes and unclosed axis

Author `/root/round211_nonlinear_scout`; root independently supplied the
same forced-source inverse decoder and the m>N distinct-size bound, and
supplied the m=2 desk specialization. Both are proof contributors. None of
these statements is an independent review. Assume exactly `INTAKE.md`.

## 1. Recurrence, periods and a nonsharp clock

The partition of token labels into occupied piles can only coarsen: every
label in one old pile receives the same new position, and a merged pile
never splits. Until the next merger, a pile with old position i and mass u
is at `i+t*u (mod m)`. Two distinct piles `(i,u),(j,v)` meet if and only if

    t*(u-v) = j-i (mod m)

has a positive integer solution. By the elementary linear-congruence
criterion this occurs exactly when `gcd(m,u-v)` divides `j-i`; the gcd
uses an integer representative and is unchanged by the choice. Because
the current slots are distinct, zero is not a solution, and the earliest
solution lies between 1 and m-1. If any pair is soluble, the minimum such
time over all pairs is a genuine first merger: no pile has changed before
that epoch. If no pair is soluble, the partition never changes.

Consequently a state is recurrent exactly when

    gcd(m,c_i-c_j) does NOT divide j-i

for every distinct pair of occupied slots. Indeed, a later merger makes
return to the original label partition impossible. Conversely, without
any merger all pile positions are periodic translations, so the full
labelled allocation returns. There is no division by geometric symmetry:
every nonempty pile has actual labels. The exact period on this recurrent
set is

    lcm_(occupied i) (m/gcd(m,c_i))
      = m/gcd(m,c_i : i occupied).

The empty state has period 1. For N>0 and initially q occupied slots there
are at most q-1 merger epochs, each no later than m-1 steps after the last.
Thus the time to recurrence satisfies

    h(f) <= (q-1)*(m-1)
         <= (min(N,m)-1)*(m-1).

For m=1 it is zero, and for N=0 it is zero by separate convention. This
bound is not claimed sharp. For prime m=p the recurrent criterion becomes
especially simple: all positive pile masses must have the same residue
modulo p. A nonzero mass difference has gcd 1 and forces a future merger;
a zero difference modulo p cannot close a nonzero slot separation.

**Value deduction:** coarsening plus constant-velocity trajectories and an
elementary cyclic congruence supply all of this argument. No novel sticky
particle theorem is claimed. Old BA/TCF and the primary momentum-conserving
systems are not exact literal adapters, but the broad coalescence mechanism
must still be deducted rather than marketed as an untouched time axis.

## 2. A complete, but generic, inverse decoder

Fix a labelled target g and let `G_j={a:g(a)=j}`, of size s_j. For every j,
partition G_j into nonempty blocks B. A block of size k, if it was an old
pile, has the **forced source slot** `i=j-k (mod m)`. Keep the collection of
partitions exactly when all these forced source slots, across all j, are
distinct. Assign every label in B to its forced slot i. This produces one
source f and no additional choice is possible.

Proof of bijection: a true source's occupied fibres are nonempty disjoint
blocks with distinct source slots, and its update sends a block of size k
at i to j=i+k. Hence it gives a permitted partition collection. Conversely
distinctness makes each chosen block the complete old pile at its assigned
slot, of the stipulated mass k; its update therefore sends exactly its
labels to j. These constructions are mutually inverse.

For a compact count put

    E_r(z) = sum_(1<=k<=N, k=r mod m) z^k/k!.

Then

    |F^{-1}(g)| = (product_j s_j!)
      [product_j z_j^(s_j)]
      product_(i=0)^(m-1) (1 + sum_(j=0)^(m-1) E_(j-i)(z_j)).

Each factor chooses an empty source slot or its one target-coloured block;
the factorial denominators and the s_j! labels give the displayed count.
This is the standard labelled block-assignment expansion, not a separate
extremal mechanism. For the constant target the expression reduces to

    N! [z^N] product_(r=0)^(m-1) (1+E_r(z)).

Equivalently it counts labelled set partitions whose nonempty block sizes
have pairwise distinct residues modulo m.

## 3. Honest extremum boundary

It is **not proved** that constant targets maximize fibres for general m,N.
Translating each source slot by minus its destination is not an injection:
blocks of equal size residue from different target classes would be sent
to the same slot. No merge-repair encoding with a unique inverse has been
proved. The pilot can only test the conjecture within its frozen box.

If m>N, blocks within an individual target class must have distinct integer
sizes. Let D(s) count partitions of s labelled elements into distinct block
sizes, with D(0)=1. Discarding the cross-target source conflicts yields

    |F^{-1}(g)| <= product_j D(s_j),

and the constant target has fibre D(N). The EGF
`sum D(s)z^s/s! = product_(k>=1)(1+z^k/k!)` is the established distinct-size
partition enumerator, not a new formula. We have not proved the additional
supermultiplicativity bound needed to turn the displayed product into D(N),
nor a full-residue replacement. Restricting to m>N would also leave general
modulus behavior outside the attempted all-parameter contract.

For m=2 the extremum is elementary and does not rescue the candidate. If N
is positive and odd, any two occupied piles have opposite load parities,
so both land in one slot. For the constant target at 0, the old load k at
slot 0 must be even; choosing its labels gives
`sum_(even k) binom(N,k)=2^(N-1)` sources. Translation gives the same number
at target 1; all nonconstant fibres are empty. If N is even, the two loads
have the same parity, so the allocation either stays or swaps its two
slots. The parity is unchanged after swapping, hence F² is the identity
on the whole carrier and every fibre is 1. The N=0 singleton carrier is
handled separately.

The missing sharp extremum and the generic temporal subtraction preclude
admission on the present deductions. No asymptotic source theorem, finite
experiment or m=2 special case closes that logical gap.
