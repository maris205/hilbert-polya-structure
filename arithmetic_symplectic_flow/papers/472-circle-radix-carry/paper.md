# Circle radix, content carry, and a composite primitive return

Candidate ID: ANG-20260925-CRC01.
Paper: 472-circle-radix-carry; batch SYMBOLIC-RETURN-20260925-Y, round 3/5.
Date label: 2026-09-25. Type: ANG partial measured-history groupoid.
Outcome: OWNED CIRCLE-CARRY IMAGE; COMPOSITE TWO-STEP RETURN — STOP / FORK

## Abstract

The current height supplies an integer radix, the circle supplies its digit,
and divisor permission controls an actual two-coordinate carry map.
We prove the complete inverse atlas and every-Borel IMAGE identities for
MAIN and three separately owned controls, including the prescribed null cuts.
Both frozen tests are completely classified. The prescribed two-cell word
has exactly one MAIN cycle, whose entire incoming packet has period group
\((\log6)\mathbb Z\), not a smaller group obtained by dividing its source period.
This composite primitive refutes MAIN's universal prime-only requirement.
All controls, zero-clock fixed continua, incoming depths and real phases remain.
No higher-period census, conservative lift, operator or formal Route is claimed.

## 1. Frozen owner and arithmetic interface

The [original card](candidate-card.md), lines 1–102, governs this proof.
Set \(X=\mathbb T\times[1,\infty)\), with product topology and Borel structure,
\(\mathbb T=\mathbb R/\mathbb Z\), and
\(\mu=\operatorname{Haar}_{\mathbb T}\otimes dy\).
Using the unique representative \(\bar x\in[0,1)\), read
\[
n=\lfloor y\rfloor,\quad j=\lfloor n\bar x\rfloor,\quad
d=\gcd(n,j),\quad \gcd(n,0)=n.
\]
Thus \(n\ge1,\ 0\le j<n\). Put \(P(n,j)\iff j=0\) or \(j\ge1,\ j\mid n\).
Each row is its own partial map, including its own geometric guard.

| Owner | Permission | Actual action |
| --- | --- | --- |
| M, MAIN | \(P\) | \(([n\bar x-j],(y+j)/d)\) |
| G, permission-OFF | all digits | same formula as M |
| C, content-OFF | \(P\) | \(([n\bar x-j],y+j)\) |
| R, radix-OFF | \(P\) | \((x,(y+j)/d)\) |

Since \(1\le d\le n\) and \(y\ge n\), both \((y+j)/d\ge n/d\ge1\) and
\(y+j\ge1\). The full affine determinants in §2 are nonzero.
Thus output/regularity guards remove no further sources: G is total and the
other domains are exactly their \(P\)-cells. Illegal points remain objects
with identities and all incoming histories, not absorbing self-loops.
The actual cells are
\[
E_{n,j}=I_{n,j}\times[n,n+1),\qquad
I_{n,j}=\{[x]:j/n\le\bar x<(j+1)/n\}. \tag{1}
\]
Floors assign upper height/right digit cells. The seam is one circle point.
Every cut, \(y=1\), \(j=0\) and \(n=1\) is retained; its actual affine
extension germ fixes the pointwise version. Global continuity or a global
étale/local-homeomorphism assertion at all cuts is not required or claimed.

For integers \(N\ge2,\ 1<a<N\), the seed \(([a/N],N)\) reads \((n,j)=(N,a)\).
Its MAIN permission is exactly \(a\mid N\). When permitted, actual height
and digit transport determine the next readouts. The lineage is therefore
proper-divisor symbolic admission -> geometric radix/content/carry feedback,
not a passive independently retained integer root. Formula and measure are
declared designs. Natural prime returns and a Logistic/Hénon/conservative lift
do not follow merely from this exact interface.

## 2. Complete inverse atlas and full-point IMAGE

For target \(w=(\xi,\eta)\), put \(\bar\xi\in[0,1)\). Enumerate every \(n\ge1\)
and \(0\le j<n\), with \(d=\gcd(n,j)\), and define
\[
V_{n,j}=[(n+j)/d,(n+1+j)/d),\qquad Z_{n,j}=[n+j,n+j+1).
\]

| Owner | Actual inverse \(\theta_{n,j}(\xi,\eta)\) | Exact target domain |
| --- | --- | --- |
| M/G | \(([(\bar\xi+j)/n],d\eta-j)\) | \(\mathbb T\times V_{n,j}\), own permission |
| C | \(([(\bar\xi+j)/n],\eta-j)\) | \(\mathbb T\times Z_{n,j}\), \(P\) |
| R | \((\xi,d\eta-j)\) | \(I_{n,j}\times V_{n,j}\), \(P\) |

These domains already lie in \(X\). Their height inequalities are precisely
\(n\le y<n+1\). In M/G/C, \(n\bar x=\bar\xi+j\) recovers source digit \(j\);
in R the condition is \(I_{n,j}\). Substitution proves both inverse identities.
Conversely every actual source has one floor pair \((n,j)\); solving its
affine equations gives this row, proving exhaustiveness. Two labels cannot
give the same predecessor because its floors recover the labels.
All different actual predecessors are retained. No target-outgoing test or
index bound is imposed. Domains/images are Borel and global fibres countable.
In particular the full image of each owner is exactly the union of its
displayed inverse domains, with its own permission, not an assumed surjective image.

The prescribed full-two-dimensional germs, densities and clocks are

| Owner | \(DU\) on \(E_{n,j}\) | Inverse IMAGE \(J_\theta\) | \(\kappa_U=-\log J\) |
| --- | --- | --- | --- |
| M/G | \(\operatorname{diag}(n,1/d)\) | \(d/n\) | \(\log(n/d)\) |
| C | \(\operatorname{diag}(n,1)\) | \(1/n\) | \(\log n\) |
| R | \(\operatorname{diag}(1,1/d)\) | \(d\) | \(-\log d\) |

The canonical circle coordinate identifies Haar with Lebesgue on \([0,1)\).
Each displayed inverse is an affine injection into its actual source cell;
affine change of variables therefore proves, for EVERY Borel subset \(B\)
of its exact inverse domain,
\[
\mu(\theta B)=\int_B J_\theta\,d\mu. \tag{2}
\]
This is not restricted to cylinders or almost-everywhere test points.
Seam/height/digit edges and their affine images are null, so (2) includes
sets containing them; the frozen germ assigns the same positive finite
constants at those points. No atoms or removals are used. The null values
are an explicit geometric prescription, not forced by measure alone.
All four IMAGE owners are established with their original \(\mu\).

## 3. Whole histories, cocycle, kernels and isotropy

For each owner independently, let \(D_r\) be its \(r\)-legal-step domain,
\(D_0=X\), and \(S_r(z)=\sum_{i=0}^{r-1}\kappa_U(U^iz)\), \(S_0=0\).
Keep the actual Borel retained-lag groupoid
\[
\mathcal G_U=\{(z,r-s,w):z\in D_r,\ w\in D_s,\ U^rz=U^sw,\ r,s\ge0\}. \tag{3}
\]
Source is \(w\), range \(z\); inverse reverses endpoints and lag, multiplication
adds lags. Two common-future equalities compose by advancing the intermediate
point to the later of its two indicated times. Its legal later iterate
supplies the extra legal steps, even for partial maps.
This is a countable union of Borel equalizer sets in \(X\times\mathbb Z\times X\).
Only equal triples are identified: free branch words add no arrows.

Set
\[
c(z,r-s,w)=S_r(z)-S_s(w). \tag{4}
\]
Two presentations of a fixed triple have both indices shifted by the same
integer. Advance the smaller presentation; the added sums after the common
future cancel. This proves pointwise presentation independence on all cuts.
The same advancement proves additivity.
Restrict the two legs to actual finite cell itineraries, intersect their
Borel images, and compose inverse-first-leg with forward-second-leg.
The empty itinerary is the identity on all \(X\), including terminal objects.
These countably many branch pairs cover every arrow, and iterating (2) gives
their every-Borel IMAGE density
\[
J_{w\mapsto z}=\exp(S_s(w)-S_r(z))=\exp(-c(z,r-s,w)). \tag{5}
\]
Thus the history clock is owned by actual transport, not a detached word sum.

All kernels, including nonunit arrows, are exactly
\[
K_{\rm lag}=\{g=(z,k,w)\in\mathcal G_U:k=0\},\quad
K_c=\{g:c(g)=0\},\quad K_{\rm joint}=K_{\rm lag}\cap K_c. \tag{6}
\]
Different histories can meet, so these are not silently replaced by units.
Retain every \((z,h)\in X\times\mathbb R\), with
\((w,h)\mapsto(z,h+c(g))\). Forward \((Uz,-1,z)\) has clock \(-\kappa_U(z)\).
Real translation \(h\mapsto h+t\) acts on the orbit SET; no smooth/Hausdorff
quotient or classical positive-roof suspension is asserted.

The entire isotropy ledger is available without enumerating all cycles.
A nonzero self-lag is an equality of distinct forward iterates, so it exists
exactly when the source is eventually periodic. If the eventual cycle has
least source period \(\ell\) and signed clock sum \(C_\gamma\), equality of
cycle positions and arbitrary legal advancement show
\[
\operatorname{Iso}_{\mathcal G_U}(z)=\ell\mathbb Z,\qquad
c(\ell k)=kC_\gamma,\qquad H_z=C_\gamma\mathbb Z. \tag{7}
\]
Transient sums cancel. For non-eventually-periodic points, source isotropy
and \(H_z\) are trivial. Extension isotropy is \(\ell\mathbb Z\) if
\(C_\gamma=0\), and trivial otherwise. Terminal objects cannot be eventually
periodic, but all actual incoming arrows remain.
Only \(C_\gamma\ne0\) gives positive translation periods: the primitive is
\(|C_\gamma|\), with its positive integer repetitions. Source step count
does not divide this generator. Zero-clock isotropy is retained, not erased.

## 4. Unrestricted incoming and complete phase tests

Define \(\operatorname{Pre}_U(A)\) by applying EVERY §2 inverse to every target
in \(A\) where its own domain conditions hold, and iterate from
\(\operatorname{Pre}^0_U(A)=A\) with no index/depth cutoff.
Induction using the complete one-step inverses proves that this gives exactly
all finite incoming histories, including terminal targets and all null cuts.
Infinite backward histories are exactly sequences \((z_0,z_{-1},\ldots)\)
where every successive pair passes these actual inverse tests. This is also
an exact countable-label description with every finite-prefix condition.
It preserves all compatible infinite paths, without asserting that every
finite history admits an infinite continuation.

For a discovered cycle and a specified point \(b\) on it, set
\[
B_U(b)=\bigcup_{a\ge0}\operatorname{Pre}^a_U(\{b\}). \tag{8}
\]
This is its ENTIRE source orbit: an arrow to \(b\) implies eventual arrival
at a cycle point, which advances to \(b\); conversely arrival supplies an arrow.
Other points of the same cycle lie in (8), not in new packets.
Let \(a(z)\) be the least arrival time at this particular \(b\), and put
\(A(z)=S_{a(z)}(z)\). For cycle data \(\ell,C_\gamma\), all arrows within this
whole incoming basin are exactly
\[
k\equiv a(z)-a(w)\pmod\ell,\qquad
c(z,k,w)=A(z)-A(w)+\frac{k-a(z)+a(w)}{\ell}C_\gamma. \tag{9}
\]
Necessity follows by advancing both legs beyond their arrivals; equal cycle
positions force the congruence, and complete cycle sums give the formula.
For sufficiency choose large nonnegative legs of the indicated lag ending
at \(b\). This proves every allowed lag is actual.
Thus (8)–(9) give exact all-depth orbit and kernel tests: in (6), require
respectively \(k=0\), the right side of (9) zero, or both.
No zero-clock off-diagonal histories or fractional extra self-lags are omitted.

Every real phase is retained and its complete invariant is
\[
h-A(z)\pmod{C_\gamma\mathbb Z}. \tag{10}
\]
The actual arrow \(z\to b\) subtracts \(A(z)\). Another arrival differs by
a loop, hence by precisely \(H_b\); conversely (9) proves that equality
in (10) gives an extension arrow. When \(C_\gamma=0\), the phase is a real
number and the full zero-clock source isotropy persists.
Generally, in any source orbit choose a base \(b\) and an actual arrow
\(g_z:z\to b\); the invariant is \(h+c(g_z)\bmod H_b\).
Changing \(g_z\) adds a loop. This does not assert a measurable global
choice of bases or delete acyclic/terminal orbits.

## 5. ALL fixed states in the frozen window

Put \(W=\mathbb T\times[1,5)\), \(F_0=\mathbb T\times[1,2)\).
For M/G/R, fixed height requires \((d-1)y=j\).
If \(d\ge2\), its left side is at least \(y\ge n>j\), impossible.
If \(d=1\), then \(j=0\), so \(d=\gcd(n,0)=n\) forces \(n=1\).
Conversely every point of \(F_0\) has \(n=1,j=0,d=1\) and is fixed.
For C, fixed height forces \(j=0\), where \(0\le n\bar x<1\).
Angular equality is the ordinary equality \(n\bar x=\bar x\).
For \(n=1\) every angle works; for \(n=2,3,4\) only \(\bar x=0\) works.

| Owner | ALL fixed states in \(W\) | Core clock; ENTIRE \(H\) |
| --- | --- | --- |
| M/G/R | \(F_0\) | \(0;\ \{0\}\), each core |
| C | \(F_0\) | \(0;\ \{0\}\), each core |
| C | \(\{[0]\}\times[n,n+1),\ n=2,3,4\) | \(\log n;\ (\log n)\mathbb Z\), each core |

Heights 2, 3, 4 belong to the displayed upper cells; height 5 is outside W.
Each core has source period one and the full incoming set (8), with (9) at
\(\ell=1\) and all phases (10). Zero-clock cores have source/extension
isotropy \(\mathbb Z\) but no positive translation period.
C's additional cores have extension isotropy zero, primitive \(\log n\),
and all repetitions, including composite primitive \(\log4\).
Distinct fixed cores cannot be related by (3), since their forward iterates
remain their distinct cores. Thus every stated continuum means distinct
full source packets; equal times do not authorize collapsing them.

## 6. ALL solutions of the prescribed two-cell word

Anchor at \((n,j)=(3,1)\), followed by \((4,2)\).
Both permissions hold for every owner; the two content values are \(1,2\).
For M/G the successive representative formulas are
\((3x-1,y+1)\) and \((4(3x-1)-2,(y+3)/2)\).
Two-step equality therefore forces \(11x=6,\ y=3\).
The resulting pair
\[
b_0=([6/11],3),\qquad b_1=([7/11],4) \tag{11}
\]
passes both exact height/digit cells, including their lower height edges.
The equations exhaust every coordinate solution of this word.
Distinct heights prove least source period two. The own clocks are
\(\kappa(b_0)=\log3,\ \kappa(b_1)=\log2\), so
\[
C_\gamma=\log6,\qquad H=(\log6)\mathbb Z. \tag{12}
\]
By (7)–(9), this is ENTIRE on the full M basin and, separately, the full G
basin, with all indices and incoming depths from §2. It is not half this group.
Source isotropy is \(2\mathbb Z\), extension isotropy zero, and the positive
primitive is \(\log6\). Rotation of (11) does not double the packet.
With base \(b_0\), core phases are \(h\) and \(h-\log2\) modulo \(\log6\);
every other incoming phase is exactly (10).

For C the height changes by \(+1,+2\), giving \(y+3\), so this word has NO
two-step return. Its empty word ledger is not a zero period or a MAIN rescue.
For R the angle remains constant. Both digit conditions require
\[
x\in[1/3,2/3)\cap[1/2,3/4)=[1/2,2/3).
\]
The height equations still force \(y=3\); thus ALL its word solutions are
\[
([x],3)\longleftrightarrow([x],4),\qquad 1/2\le x<2/3. \tag{13}
\]
These endpoint choices follow the actual right-digit rule.
Each has least source period two, signed cycle sum \(-\log2\), ENTIRE
\(H=(\log2)\mathbb Z\), primitive \(\log2\), and extension isotropy zero.
Each retains its unrestricted basin (8) and every phase (10).
Based at height 3, the height-4 phase is \(h+\log2\), equal to \(h\) modulo
the group; this does not create an additional source self-lag.
R preserves the actual angle everywhere, so different angles in (13) cannot
be related by any actual arrow. This is a continuum of prime-2 packets,
not one packet selected from that continuum.

## 7. Control interpretation, scope and decision

The same-object ledger remained intact separately for all four owners.
The MAIN primitive \(\log6\), with 6 composite, REFUTES universal prime-only
purity. This is not merely an OPEN question after an adverse witness.
G retains this same core/time, so divisor permission is not needed for this
actual return. C removes this word's height-return mechanism but has its
own positive fixed continua/composite time. R retains the height cycle but
leaves an angular continuum of equal-time packets. None rescues MAIN.

| Obligation | Exact scope |
| --- | --- |
| T0: full Borel carrier/inverse/IMAGE/history owner | Established, §§1–4 |
| Proper-divisor lineage interface | Established; stronger naturalness OPEN |
| T1 arithmetic prime-return target | NOT PASSED |
| T2 packet/repetition accounting | Structural full-history ledger and both frozen tests established |
| Universal MAIN prime-only purity | REFUTED by (11)–(12) |
| Other cycles, global census, uniqueness/all-prime coverage | OPEN / not audited beyond the frozen tests |
| T3 / operator / trace | NOT AUDITED |
| Classical symplectic/contact/Hamiltonian fields | NOT APPLICABLE |
| Formal Route / Route B | UNASSIGNED / NOT INVOKED |

These are exact analytic windows, not numerical truncations promoted to a
global census. The null-cut version belongs to the frozen affine prescription,
not a measure-only uniqueness theorem. No selected centre or revised roof
removes the adverse packet. STOP / FORK now, without further cells or tuning.

## 8. Inputs, exposure and AI assistance

Author fully read original card lines 1–102 through its stated EOF, SHA-256
b7b36a6ad4028bc6fb5c50224dca33198400b99775438bd768fbc25194eafade,
and the stream paper template. Exact substitution, affine measure transport
and deterministic-history proofs are the entire scientific method.
No scientific program, orbit approximation, external dataset or literature
theorem is an input. Root separately froze/released the work after CP1;
the author read no CP1/raw/final-review or current peer manuscript.
The scout/root pre-freeze carry/fixed/two-step design arithmetic remains
disclosed: word selection was not blind or outcome-sealed.

Definition comparison: author read 313 card 1–102, non-EOF, prefix SHA
3347c5cc854cf71bc0df9ee7d168dcaa25149a5a34923c26770b94f00557338e.
Same-author helper read 308 card 1–91, non-EOF, prefix SHA
8719a6d8392336abd1e079839e92ab94bedbe21eb118d7b7694df8c8e27d7e7e.
Only appended-outcome headings were exposed by author's discovery, not bodies.
The helper saw an embedded unit-boundary action assertion in 308's original
definition; no old proof/result/clock transferred. Their discrete-root
radix sources are comparisons, not owners of this continuous-height action.

Same-author helper /root/arithmetic_feedback_scout/dss_g_fixed_author read
only CRC01 original lines 1–102 for the released fixed-window/guard subproof,
independently measured the same hash, and supplied that scoped derivation.
It did not inspect the two-step word, incoming trees, reviewers or other
science, and wrote no files. This was author assistance, not another reviewer.
All included derivations were integrated and checked by the author.
AI agents supplied mathematical derivation, drafting and internal checking;
no human or external verification is certified. Shared-history same-model
work is NOT_CALIBRATED, not blind discovery or a global novelty/nonconjugacy claim.
Root's separate integration/review is not a mathematical input to this proof.

Navigation: [claim ledger](claim-ledger.md), [package README](README.md),
[frozen card](candidate-card.md), [final review](evidence/review.md).
The review is a separate workflow artifact, not an author input.
