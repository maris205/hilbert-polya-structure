# Binary prefix compression has an active-divisor nonprime return

Paper: 474-divisor-prefix-compression. Candidate: **ANG-20260925-DPC01**.
Date: 2026-09-25. Batch: SYMBOLIC-RETURN-20260925-Y, round 5/5.
Outcome: **OWNED BINARY PREFIX IMAGE; ACTIVE-DIVISOR LOG16 RETURN — STOP / FORK**.
Status: exact mathematical negative result for the frozen necessary target.
Classical A0–A2: NOT APPLICABLE; formal Route coordinates: UNASSIGNED;
Route B: NOT INVOKED; arithmetic T1: NOT PASSED; T3: NOT AUDITED.

## Abstract

The frozen object rewrites two unary-coded run lengths in the full binary
sequence space, using proper divisibility to choose quotient or sum writeback.
Its clock is the negative logarithm of the inverse-image scaling of the original fair
Bernoulli measure, not an independently supplied roof. All inverse branches,
terminal sequences, histories and null-point clock values are retained.
Across nine complete cylinders with arbitrary tails, MAIN has exactly one
fixed sequence. Proper-divisor feedback is active there, and its entire
physical stabilizer is `(log 16) Z`. Thus its primitive is not log an ordinary
prime. Two arithmetic OFF controls have no fixed sequences in the window;
the delimiter-retaining control instead has an entire zero-clock fixed
cylinder. The owner is well defined, but its necessary prime-purity target
fails. No higher-period search or operator construction is undertaken.

## 1. Frozen identity, question and lineage

The scientific input is the [98-line frozen card](candidate-card.md),
SHA256 `595b1751966b2edd700669757ec791437664f80636752dbe08ca1b26f6977e87`.
Its object, original measure and all four rewrite rules remain unchanged.

| Field | This object's owner |
| --- | --- |
| Carrier | Full binary Cantor Borel space with original fair-bit measure |
| Evolution | The partial prefix maps M, A, Q, L below; no terminal loops |
| Arithmetic | Proper-divisor test on the next two actual run lengths |
| Clock | Every-point inverse-prefix IMAGE derivative, then its history cocycle |
| Physical realization | Height translation on the full measured-history orbit set |
| Period convention | Least positive generator of the entire height stabilizer |
| Classical symplectic map, positive roof, mapping torus | NOT APPLICABLE |
| Operator, determinant, trace, quantum owner | NOT SUPPLIED / NOT AUDITED |

The lineage arrow is actual run lengths → proper-divisor symbol →
quotient/sum writeback and delimiter consumption → the next actual pair.
The tested integer is neither a fixed external parameter nor a prime label.
This is a broadened symbolic deformation, not a positive-dimensional
conservative realization or a proof of strong arithmetic naturalness.

The precommitted gate is the complete fixed set in the union W of nine
cylinders whose first two labels lie in `{2,3,4}`. Positive primitive times
must be logs of ordinary primes, with at most one full packet per prime;
nonempty positive data and eventual all-prime coverage are additional demands.
One owned nonprime primitive suffices to stop MAIN. This paper does not
classify other cylinders' fixed sets or any nonfixed periodic cores.

## 2. Four maps on the full binary source

Let `X={0,1}^{N0}`, `mu=(1/2,1/2)^{N0}`, and `c(n)=1^(n-1)0` for `n>=1`.
For a finite word w, `[w]` is its whole cylinder; concatenation is literal.
The legal one-step domain is
`D_1 = disjoint union_(d,n>=1) [c(d)c(n)]`, the sequences with at least two zeros.
Its complement consists of `1^infinity` and all `c(k)1^infinity`, `k>=1`.
These sequences are terminal objects, not absorbing fixed points.
Every source has a unique decomposition `x=c(d)c(n)xi` in its legal domain.

Write `D(d,n)` for `1<d<n` and `d|n`, and put
`g(d,n)=n/d` on D and `g(d,n)=d+n` otherwise. With `U=c(d)c(n)`, define:

| Owner | Replacement V in `T(U xi)=V xi` | Own local clock `kappa/log 2` |
| --- | --- | --- |
| M MAIN | `c(g(d,n))` | `d+n-n/d` on D, otherwise `0` |
| A divisor-bit-OFF | `c(d+n)` | `0` |
| Q quotient-write-OFF | `c(n)` on D, otherwise `c(d+n)` | `d` on D, otherwise `0` |
| L delimiter-loss-OFF | `c(g(d,n))c(n)` | `d-g(d,n)` |

The clocks in the last column are derived below, not assumed as roofs.
All four maps are Borel and defined on exactly D_1. Each branch is a
homeomorphism of its full source cylinder onto `[V]`, but globally targets
can have several predecessors. Every step decodes its current prefix anew.
No choice of tail, inverse representative, density, prime table or target
acceptor is part of the definition. Signed and zero clock values are kept.

## 3. Complete inverse atlas and every-Borel IMAGE

For every owner and every positive pair `(d,n)`, define
`I_dn(V xi)=U xi` on the WHOLE cylinder `[V]`, with that owner's V.
The inverse identities hold on `[U]` and `[V]` by literal deletion and
insertion of finite words. Each I_dn is a Borel homeomorphism onto `[U]`.
If `Tz=y`, the first two zeros of z recover its unique `(d,n)`, hence
`z=I_dn(y)` on one of these domains. Conversely every listed inverse is
an actual predecessor. Thus the countable atlas is complete, including
all overlaps, all run lengths and targets with no outgoing permission.
An identical actual predecessor is not counted twice merely through notation.

For every finite word w and Borel `E subset X`, prefix insertion P_w satisfies
`mu(P_w E)=2^(-|w|)mu(E)`.
Proof: both sides, as functions of E, are finite Borel measures; they agree
on finite cylinders by the defining product probabilities, and therefore
on their generated Borel sigma-algebra by the pi-lambda uniqueness argument.
For Borel `E subset [V]`, write `E=P_V B`; P_V is a homeomorphism, so B is Borel.
Consequently

`mu(I_dn E)=2^(-|U|)mu(B)=2^(|V|-|U|)mu(E)=integral_E J_dn dmu`,

where `J_dn=2^(|V|-|U|)` at EVERY point of `[V]`.
This proves the asserted IMAGE identity for every Borel set, not merely
for cylinders. The assigned value at a null sequence is part of the frozen
prefix version: it is not uniquely forced by an almost-everywhere derivative.
Indeed every singleton is null, since its length-N cylinder has mass `2^-N`.
Null terminal and returning sequences are nonetheless retained as objects.

At the actual source branch, `kappa=-log J_dn=(|U|-|V|)log 2`, giving the
four formulas in Section 2. The original probability measure never changes.
In particular A has identically zero clock; L has negative additive-branch
clock and is not a positive-roof suspension.

Finite compositions have countable prefix charts as well. To check this,
intersect an output cylinder with the next required input cylinder.
Two finite-word cylinders are disjoint or one contains the other; pulling
back the nonempty intersection through a prefix substitution gives another
full cylinder with a prefix substitution. Induction proves the claim for
every finite itinerary, with no bound on code lengths.
The inverse derivative on such a chart is the product of its prescribed
one-step derivatives, at every point including null sequences.

## 4. Actual histories, kernels, isotropy and phases

The following construction applies separately to EACH owner with its own T
and clock. Let D_r be the legal r-step domain, `D_0=X`, and
`S_r(x)=sum_(j<r) kappa(T^j x)`, with `S_0=0`.
Use actual triples

`G={(x,r-s,y): x in D_r, y in D_s, T^r x=T^s y}`, with source y and range x.

Units have lag zero; multiplication adds lags; inversion exchanges endpoints
and reverses lag. Equal actual triples are identified, but different lags
are not. Finite prefix charts above give a countable Borel arrow atlas.
No history labels are extra arrows, and no terminal forward step is inserted.

Define `c(x,r-s,y)=S_r(x)-S_s(y)`.
If two witnesses give the same lag, their `(r,s)` differ by the same integer.
Order them so the difference t is nonnegative. The second witness ensures
that the common endpoint admits t further steps. Both sums gain the same
`S_t` there, proving descent. To compose two arrows, extend the shorter of
their two middle endpoint histories to the longer legal middle history.
Their middle sums then cancel, proving additivity. In particular
`c(Tx,-1,x)=-kappa(x)` and `c(g^-1)=-c(g)`.

For an actual history-pair chart `a=(T^r|U)^(-1) o (T^s|V)` from y to x,
the every-point inverse-prefix rule and Section 3 give

`mu(aE)=integral_E exp(S_s(y)-S_r(a y)) dmu(y)=integral_E exp(-c(a y,r-s,y)) dmu(y)`.

This holds for every Borel subset E of the chart domain, by the finite-prefix
composition argument. Refinements and alternate witnesses preserve c as
just proved. Thus the full history clock is owned by the original IMAGE,
not inferred from an orbit label or a separately chosen measure.

The complete three kernels are, without suppressing any branch or endpoint,

`K_lag={(x,0,y): there exists r, T^r x=T^r y legally}`;
`K_clock={(x,r-s,y): T^r x=T^s y legally, S_r(x)=S_s(y)}`;
`K_joint=K_lag intersect K_clock`.

These conditions use the owner's own sums. In particular `K_clock=G` for A.
For L, define `b(x)=k log 2` when x has first block c(k), and `b(1^infinity)=0`.
Since `kappa_L=b-b o T_L`, telescoping gives `c_L(x,k,y)=b(x)-b(y)` on
ALL actual arrows. Hence its clock kernel consists exactly of equal-b
endpoints, and its joint kernel additionally requires zero lag.
This is an endpoint potential for this control, not a reweighting of mu.

The lifted arrows on the FULL `X times R` are `(y,h)->(x,h+c(x,k,y))`.
Physical height translation acts on their orbit SET; no separation,
manifold, section or Hausdorff quotient is assumed. The precise tests are:
base objects x,y share an orbit iff some legal iterates meet; two lifted
points share an orbit iff for some actual `(x,k,y)`, `h_x-h_y=c(x,k,y)`.
These are existence tests over the whole countable atlas, not selected paths.

Source isotropy is completely described as follows. A nonzero lag isotropy
arrow implies `T^(s+p)x=T^s x` for some p>0, so x eventually reaches an
actual cycle. Conversely any such cycle supplies isotropy. If its least
discrete period is p, the isotropy lags are EXACTLY `p Z`: every eventual
return has lag divisible by p, and any multiple is realized sufficiently
far along the cycle. If x is not eventually periodic, its isotropy is zero.
For an eventual p-cycle put `C=sum_(j=0)^(p-1) kappa(T^j z)` at a cycle point z.
Additivity and cancellation of the common initial tail give `c(x,mp,x)=mC`.
Thus the ENTIRE physical stabilizer is `H_x=C Z`, not a subgroup selected
from one return; for non-eventually-periodic x it is `{0}`.
Extension isotropy is `{mp:mC=0}` over an eventual cycle and is zero otherwise.
Zero-clock source isotropy survives in the extension even though H is zero.

To justify the physical assertion, `[x,h+t]=[x,h]` holds precisely when
some isotropy arrow at x has c=t. Therefore H is exactly the image just
computed. Each base orbit contributes one height-translation orbit `R/H`:
choose an anchor a, transport a height to a with any actual arrow, and
reduce modulo H_a. Alternative choices differ by isotropy and give the
same coset. This also proves all compatible phase identifications.
If C is nonzero, the primitive positive time is `|C|`; positive repeats
are `m|C|`, m>=1, with opposite traversal signs retained in the arrows.
If C=0 or there is no eventual cycle, there is no positive primitive.
Distinct base orbit classes are distinct packets even when their times agree.

## 5. All incoming, including terminals and infinite prehistories

For every y in the FULL X and each owner define the explicit set

`Pre(y)={c(d)c(n)xi : d,n>=1 and y=V_dn xi}`.

This uses that owner's full V_dn, with no outgoing condition on y.
Let `Pre^0(C)=C`, `Pre^(j+1)(C)=union_(y in Pre^j(C)) Pre(y)`.
The inverse identities prove by induction that `Pre^j(C)` is EXACTLY the
set whose legal j-th iterate lies in C. The complete incoming basin is
`B(C)=union_(j>=0) Pre^j(C)`. This is an all-depth equality, not a truncated
search. Compatible infinite incoming histories are precisely sequences
`(x_0,x_-1,x_-2,...)` with `x_0 in C` and `x_(-j-1) in Pre(x_-j)` for every j.
Induction gives every legal finite prefix, and conversely every actual
infinite predecessor chain satisfies this rule. Such chains are retained;
they are not adjoined as extra states or multiple copies of an actual arrow.

The zero-free terminal `1^infinity` has no predecessors for any owner.
For a one-zero terminal `c(k)1^infinity`, M/A/Q use the formula above with
their one-block output label equal to k and tail `1^infinity`; all such
predecessors are kept. L has no predecessors of any terminal, since each
of its outputs contains two zeros. Finite histories stop on arrival at a
terminal rather than continuing on an artificial loop.
For a basin of a terminal t, each x has a unique arrival depth ell(x): two
different depths would require a positive legal iterate of t. Any arrow
within that basin has lag `ell(x)-ell(y)` and clock
`S_{ell(x)}(x)-S_{ell(y)}(y)`. Source and extension isotropy, and H, are zero.
Its exact phase at t is `h-S_{ell(x)}(x)` in R, without modular reduction.

## 6. Exhaustive fixed classification on nine complete cylinders

Let `W=union_(d,n in {2,3,4}) [c(d)c(n)]`.
The following proof quantifies over EVERY binary tail xi, including tails
with finitely many zeros and the all-ones tail; there is no tail enumeration.

For M, A and Q write the single output label as f(d,n).
Equality `c(d)c(n)xi=c(f(d,n))xi` forces `f(d,n)=d` by the position of the
first zero. Removing that identical prefix then forces `xi=c(n)xi`.
For any nonempty finite word w the equation `xi=w xi` has the unique
solution `w^infinity`: iteration forces each finite prefix of that infinite
word, which uniquely determines the sequence. The converse is immediate.

For M the additive case would give `d+n=d`, impossible. On D it requires
`n/d=d`, or `n=d^2`. In the nine allowed pairs this holds only for `(2,4)`.
It meets the proper-divisor guard. Thus

`Fix(M) intersect W = {P}`, where `P=c(2)c(4)^infinity`.

For A, `d+n=d` is always impossible. For Q, the additive case is impossible
and the divisor case would require `n=d`, contrary to `d<n`. Therefore
`Fix(A) intersect W = Fix(Q) intersect W = empty`.

For L equality reads `c(d)c(n)xi=c(g(d,n))c(n)xi`.
It is equivalent just to `g(d,n)=d`; the remaining tail is then unchanged.
The same integer equations give `(d,n)=(2,4)` and no other allowed pair.
Consequently `Fix(L) intersect W=[c(2)c(4)]`, the ENTIRE cylinder.
Different tails give distinct actual fixed points, not duplicate labels.

## 7. Complete packets of every admitted fixed core

### 7.1 MAIN: the active-divisor packet

At P the actual input labels are `(2,4)`, D is true, and the quotient is 2.
Lengths are `|U|=6`, `|V|=2`, so `J=2^-4` and
`K=kappa(P)=4 log 2=log 16` under the original fair measure.
This is an arithmetic-active return. A instead writes c(6), and Q writes
c(4); neither returns P. The different outcomes are changes in actual maps,
not merely a relabelled clock on the same selected point.

Its full incoming basin is `B_P=union_(j>=0) Pre_M^j({P})` with the exact
unrestricted recursion of Section 5. To make its nontrivial breadth explicit,

`Pre_M(P)={c(1)c(1)c(4)^infinity} union {c(d)c(2d)c(4)^infinity:d>=2}`.

Indeed an additive output label 2 forces `(1,1)`, and a proper-divisor
output 2 forces `n=2d,d>=2`; these exhaust every positive input pair.
The d=2 predecessor is P itself. Further levels use ALL positive pairs,
not just W. The recursion, its all-depth proof, and the compatibility test
give every finite and infinite incoming history without adding a cutoff.

Every point in B_P reaches P, and any point sharing P's base orbit reaches
P as well, since every legal iterate of P equals P. Hence B_P is the entire
base orbit class, not merely a section of it. For x in B_P choose any
arrival depth ell and define `E(x)=S_ell(x)-ell K`. Later arrivals only add
the corresponding multiple of K, so E is well defined and E(P)=0.
The complete restricted groupoid and clock are

`G|B_P = B_P times Z times B_P`,
`c(x,k,y)=E(x)-E(y)+kK`.

To realize any integer k, choose sufficiently large r,s with `r-s=k` beyond
both arrival depths. Conversely every arrow in this class has precisely
that formula by the arrival identity for the sums. Its full lag kernel
is k=0; clock kernel is `E(x)-E(y)+kK=0`; joint kernel is k=0 and E(x)=E(y).
At EVERY incoming x, source isotropy is Z, its clock image is EXACTLY
`K Z`, and extension isotropy is zero. Incoming arrows cannot reduce K:
their endpoint contributions cancel in any isotropy loop.
The exact phase is `h-E(x) mod K`, equivalently `h-S_ell(x) mod K`.
All real phases are retained, forming one circle packet, not one packet
per phase or per predecessor. Its primitive is log16, repeats are
`m log16`, and lag-negative traversals have the opposite signed clock.
Since 16 is composite, `log16` is not log an ordinary prime; in particular
this primitive cannot be replaced by log2 merely because `16=2^4`.

### 7.2 L: every tail, all isotropy, no positive time

Write `z_xi=c(2)c(4)xi` for an arbitrary tail. At every such point the
L branch has `|U|=|V|`, so its clock is zero. Its COMPLETE predecessor
set is `{z_xi}`: an L predecessor must retain second label 4 and the exact
tail xi, and solve `g(d,4)=2`. The additive equation has no positive d;
the proper-divisor case has exactly d=2. Iterating proves its entire
incoming basin is the singleton, and its only infinite predecessor chain
is constant. No two different z_xi share a future.
For each such core the full source isotropy is Z, its clock is identically
zero, H is `{0}`, and extension isotropy is still Z at EVERY real height.
The lag and joint kernels contain only lag zero; the clock kernel contains
all isotropy. Its physical orbit is a line, not a positive closed packet.
The full cylinder's uncountably many distinct cores and every real phase
are retained. A and Q have no window cores, so have no associated incoming
fixed packets to omit; their full-state histories remain those of Sections 4–5.

## 8. Controls, decisive gate and claim limits

| Owner | Complete fixed set in W | Fixed-core physical ledger |
| --- | --- | --- |
| M | Exactly P | One full packet, H=(log16)Z, primitive log16 |
| A | Empty | No fixed-core packet in W; its clock is globally zero |
| Q | Empty | No fixed-core packet in W; own D-branch clock is d log2 |
| L | Entire [c(2)c(4)] | Every core retained, zero clock, no positive packet |

These are three genuinely distinct OFF rewrites on the same full carrier,
not three invented accepting subsets. Their IMAGE and histories were derived
from their own V words. L exhibits the ownership danger of hiding a whole
fixed cylinder behind a chosen representative; none is removed here.
A's zero clock and L's endpoint-potential clock imply H=0 globally for
those controls without a cycle census. No corresponding simplification is
borrowed for M or Q. OFF separation at P supports activity of the actual
divisor operation; it does not establish prime naturalness or exclude a
PROVES_TOO_MUCH mechanism beyond this bounded gate.

T0: full owner, branch atlas, IMAGE, histories and quotient-set action are
established. T1: an endogenous IMAGE clock and explicit symbolic arithmetic
feedback are established, but prime-side adequacy and strong naturalness
are NOT PASSED. T2: this fixed packet and its entire repetition law are
owned; the necessary MAIN universal prime-purity condition is REFUTED.
Coverage of other primes and the global periodic ledger are not computed;
their lack of classification does not reopen the already refuted purity.
T3 is NOT AUDITED. Classical A0–A2 are NOT APPLICABLE, formal coordinates
UNASSIGNED, and B NOT INVOKED.

Decision: STOP / FORK this frozen candidate, with no roof, measure, code or
tail selection repair. The decisive gate is the owned active-divisor
primitive log16. No new candidate is created or authorized here; no475.

## 9. Evidence, access and research-integrity record

The [claim ledger](claim-ledger.md) and [package overview](README.md) name
this same candidate and outcome. Proofs here use only the frozen definitions
and first-principles word and measure arguments. There are no numerical
experiments, scientific code, external sources, uploads, PDFs or Git actions.
No current independent raw derivation, peer report or author-helper output
was read. Root reported a separate scope PASS before distinct author release;
that report was not read by this author. At author freeze, independent final
review was pending root's later unlock; subsequent review is recorded separately
in `evidence/review.md`, without a verdict being presumed by this manuscript.

Author input receipt: card 1–98 FULL EOF, SHA256 as in Section 1; template
1–107 FULL EOF. For local formatting, papers/README.md 1–240 of 2587 was
read and exposed old batch summaries, then headings only and the required
format section 2545–2587 through EOF; the whole registry was NOT read.
That 1–240 prefix SHA256 is
`29c62fd64bc767b3e5ea810203010bd4396986d60b18e0346feea653cd716cac`.
This summary exposure was reported to root; no old proof was opened.

As design scout, this author read old definition prefixes 377/1–52 of108,
326/1–55 of210, 364/1–43 of123, and 368/1–46 of80, not their EOF or outcome
sections; exact prefix receipts are preserved in the card. Root's additional
325/1–70 comparison is root-attributed provenance, not a personal source read.
Family connections are acknowledged; no novelty or nonconjugacy theorem is
claimed. The scout also read root readme.md 1–80 of2812, exposing old summary
outcomes (prefix SHA256
`c77bc7c15c39f17347b6ec0bbaf339e769977be04ee6a72bcc0973150c6892f8`).
Informal fixed/length design calculations informed W before freezing;
this is not outcome-blind preregistration.

ARS instructions used: personally read router 488 lines, deep workflow602,
runtime113, DA192, logical-fallacies192 and anti-leakage83 in the retained
current research context; local AGENTS221 and plan411 were read fully.
For this author task, academic-paper workflow544, draft-writer660,
writing-quality160, title-rhetoric114 and academic-style188 were read fully;
a truncated workflow middle chunk was re-read before use. The writer guidance
informed explicit limits, proof/evidence separation and disclosure. This is
a root-scoped three-Markdown-artifact task, not a claimed full submission
pipeline; no venue-specific criteria binding or publication readiness exists.

AI disclosure: this design and manuscript were produced by an AI agent with
same-model shared research history, internally NOT_CALIBRATED. No blind,
human, external, cross-model or calibrated peer review is claimed. Root owns
card/integration and a different agent owns independent review. No empirical
dataset, human subjects, funder, human authorship or conflict-of-interest
declaration has been supplied; none is fabricated. The mathematical source
and every permitted artifact are local and the final scientific disposition
is a negative gate result, not evidence for an RH or Hilbert–Pólya claim.

EOF — ANG-20260925-DPC01 author manuscript.
