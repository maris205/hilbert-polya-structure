# Closed prime circles inside a non-Hausdorff full quotient

Date: 2026-09-20. Audit `ASFS-AUDIT-20260920-HQT01`.
Unchanged candidate `ANG-20260919-HWS01`.
Status: `CLOSED EMBEDDED PRIME CIRCLES; FULL QUOTIENT NON-HAUSDORFF — SCOPED ADVANCE / STOP`.
Paper ID: `285-haar-seeded-packet-topology`. Result type: exact local
theorems and an adverse global-separation result, not a numerical study.

## Abstract

The full arithmetic-seed witness flow of paper 278 has one abstract
cyclic-time packet per prime. This follow-up proves that each packet is
a closed embedded circle in the full coarse real-extension quotient,
with its usual circle topology and least period log p. The ambient
quotient is nevertheless non-Hausdorff. An explicit pair of equivalent
escaping sequences converges to two inequivalent nonreturning states.
Both conclusions use the unchanged full source, arrows, topology and
Haar image clock. No returning stratum is substituted for the owner.
This strengthens the owner-level T2 result, but does not close arithmetic
naturalness, supply T3, or justify a classical or formal Route promotion.

## 1. Contract, dependencies and unchanged object

The [frozen card](candidate-card.md) is the controlling audit contract.
Its version-1 SHA-256, before any theorem assertion in this package, is
`41ae89afb4f65e3f27151d388ee5b148a491023eb5f5b897fe54b6e134991041`.
The [278 card](../278-haar-seeded-witness-flow/candidate-card.md) and
[278 paper](../278-haar-seeded-witness-flow/paper.md) remain authoritative
and unchanged; their exact hashes are bound in the audit card and
[evidence record](evidence/README.md).

Write K for the full profinite integers and Y for the disjoint union of
ALL root copies of K: hubs H_n (n>=2), scans S_(n,d) (2<=d<n), and escape
roots E_k (k>=0). T consumes a residue j at H_n and replaces the seed x
by (x-j)/n. The zero port starts the divisor scan (or returns to H_2);
a nonzero port with gcd(n,j)>1 descends to that gcd hub; a coprime port
escapes. Scans preserve the seed, move to the first encountered proper
divisor hub, or return to H_n if no remaining divisor is encountered.
Escape roots advance E_k to E_(k+1). See the card for all endpoint rules.

The full retained-lag groupoid is

    G = {(z,m-k,w): T^m z = T^k w},

with its full finite inverse-branch-pair topology. Its established
continuous clock on an alpha/beta branch pair is

    c(g) = log D_alpha - log D_beta,

where D is the product of actually consumed hub moduli. On M=Y x R,
G_c identifies (w,u) with (z,u+c(g)). Let pi:M->Q=M/G_c be the FULL
quotient map, using the quotient topology. Real translation survives as
an action on Q; it is not included in the equivalence relation defining Q.

The prior-work arrow is the 278 deformation of prime-symbolic witness
admissibility into full arithmetic-residue dynamics. We do not replace
this lineage with generic geometry. Choice of scan architecture and
arithmetic naturalness remain OPEN. Classical symplectic/map/roof fields
are NOT APPLICABLE; this is the separately labelled groupoid track.

We use the following established 278 facts, not fresh assumptions:

- Multiplication by every nonzero integer is injective on K. K itself
  is not an integral domain; this narrower injectivity is sufficient.
- The only primitive periodic source cycles are zero-seed prime cycles
  C_p. Their hub point is z_p=(H_p,0), and their length is ell_p=p-1.
- B_p, the set of all source states eventually reaching C_p, is one full
  G orbit. Distinct primes have disjoint such orbits. Its clock isotropy
  image is (log p)Z, with the least positive value log p; other source
  states have clock isotropy image {0}.
- D_p=intersection_(r>=0) p^r K contains nonzero seeds with p-primary
  component zero. They follow the prime zero-port root word forever,
  but only seed zero has an actual return.

## 2. Returning basins are finite in each root

For a hub n and prime p define

    C_n^p = {x in K : (H_n,x) belongs to B_p}.

**Lemma 1 (rootwise finiteness).** For every root R and prime p, the set
of seeds {x:(R,x) in B_p} is finite and consists of nonnegative integers
embedded in K. At hubs it is empty for p>n.

*Proof.* If n is prime, a nonzero residue at H_n escapes. The zero-port
word returns to H_n with the seed divided by n. If some finite number
of these words reaches seed zero, injectivity of integer multiplication
forces the initial seed to have been zero. A nonzero seed which follows
the word forever does not reach C_n, as distinguished in 278. Therefore

    C_n^p = {0} if n=p, and is empty otherwise, for prime n.

This includes n=2: its zero port is a one-step cycle, with no scan roots.
For composite n let q(n) be its least proper divisor. The actual zero
port followed by the scan reaches H_q(n). Each nonzero nonescaping port
j reaches H_d, d=gcd(n,j), with 2<=d<n. Consequently the EXACT recursion is

    C_n^p = n C_q(n)^p
            union over 1<=j<n, d=gcd(n,j)>=2 of (j+n C_d^p).

Both inclusions follow from the actual forward branch and its unique
inverse x=j+n y. All hub indices on the right are smaller than n.
Induction proves finiteness, nonnegative-integral seeds, and emptiness
when p>n. No untested residue or noninteger seed is discarded.

At a scan root S_(n,d), let a be the first divisor of n encountered in
{d,...,n-1}, or a=n if there is no such divisor. The deterministic scan
reaches H_a with the seed unchanged. Its returning seed set is exactly
C_a^p. This includes late or disconnected scan roots, even those which
could never be entered from the beginning of a hub's scan. At every
E_k it is empty. These are all source roots. QED.

**Corollary 2.** Each B_p is closed in Y, discrete in its subspace
topology, and G-saturated.

*Proof.* In each clopen root copy of the Hausdorff space K, the set is
finite and hence closed. A subset of a topological disjoint union is
closed exactly when its intersections with all components are closed.
Each point can be separated from the finitely many other points in its
own root, proving discreteness. Saturation follows either from the
established one-orbit result or directly from eventual arrival in C_p
being preserved by a common forward tail. QED.

Rootwise finiteness is not global finiteness: all finite preimages and
all scan phases are still counted in B_p. This result is proved for
every root and every prime, not inferred from a cutoff computation.

## 3. Comparison with the full quotient topology

Set A_p=B_p x R and P_p={pi(z_p,t):t in R}. The all-preimage convention
and actual arrows imply A_p=pi^(-1)(P_p): any point of B_p has an arrow
from z_p, and varying the starting real coordinate supplies all R at
that point. Conversely an arrow to z_p places its source in B_p.

**Lemma 3 (full quotient comparison).** P_p is closed in Q and the
restriction pi_p:A_p->P_p is a quotient map when P_p has the SUBSPACE
topology inherited from the full Q.

*Proof.* A_p is closed in M by Corollary 2 and is saturated. Since
pi^(-1)(P_p)=A_p is closed, the definition of quotient topology makes
P_p closed in Q. For any C subset of P_p, if pi_p^(-1)(C) is closed in
A_p, it is closed in M because A_p is closed. Saturation gives
pi^(-1)(C)=pi_p^(-1)(C), so C is closed in Q, hence in P_p. The reverse
implication is continuity of pi_p. This closed-set characterization
proves the quotient-map assertion. No Hausdorffness of Q is assumed.
QED.

This comparison is essential. Merely recognizing a circle in a reduced
subgroupoid quotient would not identify its topology inside the full Q.
We use a subset for proof, not as a new owner or a deletion of its complement.

## 4. Exact embedded-circle theorem

For each z in B_p, choose its first hitting time m_z of the hub point
z_p. All phases eventually hit that point. Let D_z be the product of
hub moduli consumed in this finite prefix, with D_(z_p)=1. The actual
arrow a_z=(z,m_z,z_p) from z_p to z has clock log D_z. This follows
from the inverse-prefix convention of the unchanged clock.

**Theorem 4.** For every prime p, the canonical map

    kappa_p: R/(log p)Z -> Q, [t] -> pi(z_p,t)

is a topological embedding with closed image P_p. The real-translation
action on that image is the usual circle translation. Its least positive
period is log p, and all positive repetitions are r log p, r>=1.

*Proof.* On A_p define the phase map

    Theta_p(z,u) = [u-log D_z] in R/(log p)Z.

It is continuous: B_p has the discrete subspace topology, so no
cross-root or cross-seed continuity of a chosen hitting time is needed.
For any arrow g:w->z within B_p, the composition a_z^(-1) g a_w is
isotropy at z_p. Thus, for some integer k,

    c(g) = log D_z - log D_w + k log p.

It follows that Theta_p is invariant under every G_c arrow on A_p.
Conversely, equality of two phases gives exactly such an integer k;
compose a_w^(-1), an actual k-fold isotropy arrow at z_p, and a_z.
This is an actual G_c arrow between the two extension points, with
the required real-coordinate difference. Therefore its fibres are
precisely the full extension orbits within A_p.

Lemma 3 gives a continuous induced map F_p:P_p->R/(log p)Z. The map
t->pi(z_p,t) is continuous and has period log p by the full isotropy
ledger; it factors continuously through the ordinary circle quotient
to give kappa_p with image P_p. At z_p, D_z=1, so F_p kappa_p is the
identity. The fibre characterization gives kappa_p F_p the identity
on P_p. Thus kappa_p is a homeomorphism onto that actual subspace,
which is closed by Lemma 3. Adding time t adds [t] to Theta_p, proving
the action statement. The full isotropy image, not the length of a
root word alone, proves the least period and all repetitions. QED.

This is one circle per full packet, not one chosen source trajectory
per primitive. The entire B_p x R is accounted for. In particular no
extra multiplicity is obtained by selecting its different scan phases.

## 5. The full quotient is nevertheless non-Hausdorff

**Theorem 5 (fixed separation control).** The unchanged full Q is not
Hausdorff. The obstruction can be witnessed by two nonreturning limit
states in the zero-port fibre at H_3.

*Proof.* Put r_k=k! and define source states

    x_k=(H_3,3^r_k),    y_k=(H_3,2*3^r_k).

After r_k complete zero-port cycles, each of length two, their hub
seeds are respectively 1 and 2. Each then takes its coprime port to
(E_0,0). Both prefixes have length 2r_k+1 and the same consumed
product 3^(r_k+1). Hence (x_k,0,y_k) is an actual retained-lag groupoid
arrow with clock zero. In the full extension quotient,

    pi(x_k,0) = pi(y_k,0) for every k.

The seeds 3^(k!) converge in K to an element e with 3-primary component
zero and all other primary components one. Here is a finite-modulus
proof, with no numerical limit inference. For every m=3^a b with
gcd(3,b)=1, the residues of 3^(k!) are eventually zero modulo 3^a.
In the finite unit group modulo b, the element 3 has finite order d:
two powers coincide and cancellation gives a positive power equal to
one. For k large enough d divides k!, so the same residues are
eventually one modulo b. The Chinese remainder identifications give
compatible residues at every m and hence exactly the stated limit e.

Thus x_k->x=(H_3,e) and y_k->y=(H_3,2e). The element e is nonzero
(it is one modulo 2) and lies in every 3^r K. So both limit seeds
follow the zero-port H_3/S_(3,2) cycle forever, and neither is zero.

There is NO common forward tail for x and y. To meet, their iterates
must have the same root, hence the same parity of iteration. On hub
visits the seeds are e/3^i and 2e/3^j; on scan visits the same formulas
hold with both division counts increased by one. Equality would imply

    (3^j - 2*3^i)e = 0

for nonnegative integers i,j. The integer coefficient is never zero.
Injectivity of multiplication by nonzero integers on K would force
e=0, a contradiction. Thus there is no G arrow between x and y, and
in particular pi(x,0) and pi(y,0) are distinct in Q.

By continuity of pi, the single sequence pi(x_k,0)=pi(y_k,0) converges
to both these distinct points. A sequence in a Hausdorff space cannot
have two distinct limits: disjoint limit neighborhoods would both have
to contain its entire tail. Therefore Q is not Hausdorff. QED.

This does not contradict Theorem 4. The two limiting states are outside
every B_p; in particular they are not extra prime circles. Escaping
sequence terms are also retained. The failure depends on the full
owner, which cannot be repaired in this audit by deleting either set.
We do not claim that Q is non-T1, or classify all orbit closures.

## 6. Controls, limits and portfolio decision

| Obligation/control | Result and boundary |
|---|---|
| p=2 endpoint and all-prime induction | Included exactly; no finite prime cutoff |
| Composite hubs and late scan roots | Exact basin recursion; none silently omitted |
| Full quotient versus returning reduction | Lemma 3 proves the actual subspace comparison |
| Primitive and repetition law | Unchanged full isotropy; one circle, least log p, repeats r log p |
| Nonzero periodic-word seeds | Retained; root-word periodicity is not an actual return |
| Escaping separation sequence | Actual equal-clock arrows; inequivalent exact limits |
| Naturalness / PROVES_TOO_MUCH risk | OPEN; a topological result does not select the scan architecture |
| Generic Hausdorff-flow or geometric promotion | STOP: the full coarse quotient fails Hausdorff separation |

Portfolio: **scoped advance / stop**. The advance is an exact topological
strengthening of the same candidate's owner-level T2 packets. The stop
is any promotion of its full coarse quotient as a Hausdorff classical
ambient flow. It is not a stop of the open research programme and not
a claim that the original étale groupoid itself is non-Hausdorff.

T0 and the scoped arithmetic/clock T1 facts remain those of 278; naturalness
remains OPEN. T2 now includes closed embedded prime circles. No T3
operator, trace, determinant, domain or normalization has been supplied
or pursued. Classical A0/A1/A2 are NOT APPLICABLE; formal Route coordinates
UNASSIGNED, Route B NOT INVOKED. The same-object ledger stayed intact.

The [parallel scout record](evidence/scout-record.md) preserves one
definition-level nonadmission; it adds no theorem credit here. The
[internal adverse review](evidence/independent-review.md) is not external
peer review, formal verification, or an independent-error guarantee.

The next authorized decision is to retain these exact positive and
negative facts while continuing source-architecture breadth. Any new
owner that removes states or changes clocks must receive a fresh card;
any analytic owner would need its own explicit contract and may not
assume a Hausdorff coarse space. Neither is implemented in this audit.
Packages 241/242 remain paused. The programme goal remains active.

## Reproducibility and disclosure

The [card](candidate-card.md), [claim ledger](claim-ledger.md),
[evidence index](evidence/README.md), and [review](evidence/independent-review.md)
bind definitions, proof scope and document versions. Methods are the
all-root induction, a closed-saturated quotient argument, exact clock
composition, and convergence at every finite modulus. There are no
scientific numerical inputs, cutoff, precision choices, generated prime
tables, zero data or fitted parameters. Document hashes and Markdown
checks are administrative verification, not mathematical experiments.

AI-assisted authorship and internal review used the ARS bounded freeze
and adverse-check workflow. No external peer review or novelty claim
is implied, and no publication, PDF or other external artifact was made.
