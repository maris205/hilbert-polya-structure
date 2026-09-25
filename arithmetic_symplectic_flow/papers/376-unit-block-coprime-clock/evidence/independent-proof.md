# Independent raw-card proof — hard coprime blocks and visible units

Candidate `ANG-20260922-UBC01`; 2026-09-22; round 2/5.
Author `/root/algebraic_henon_author`; internal AI, `NOT_CALIBRATED`.
Sole scientific input: [card](../candidate-card.md), complete lines 1–88 through EOF,
SHA-256 `090c1aab8a27e7d1efd9e5be157f4c69c77ae02408a4a0bc2b036180675c1a85`,
checked at CP1 and fully reread after root's explicit mathematical release.
No author paper, peer, other new science, web or numerical experiment was read.
Previously fully read ARS instructions reused. Shared history and the disclosed
pre-freeze definition change preclude a blindness or priority claim.

## 1. Entire source, inverses and block probabilities

An illegal pair within an unmarked segment has a finite witness. Hence MAIN X
is closed in B^N_0 and is standard Borel. Shift preserves X. E_a={y:ay in X}
is closed, and I_a:E_a->[a] intersect X is a Borel homeomorphism onto its image,
inverse to the restricted shift. Every source has exactly its actual first-letter
chart; all E_a, including their infinite-tail restrictions, are retained.
No openness of E_a or etale conclusion is assumed.

Telescoping gives sum_(a>=2)rho(a)=1. Thus 0<Z_n<=1: positivity follows by
choosing finitely many pairwise-coprime integers, for example recursively taking
2 and then one plus the product of previous choices. Their rho-product is positive.
Consequently sum_(|w|=n)p(w)=2^(-n-1), sum_w p(w)=1 and

    M=sum_(n>=0)(n+1)2^(-n-1)=2.                         (1)

Every legal p(w)>0 and p(w)<=1/2. OFF independently has Z_n=1 and the same
length law and M=2. SINGLE has its stated p(empty)=1/2, p(a)=rho(a)/2,
so its own normalization is one, M=3/2 and again p(w)<=1/2.
Sections 2–4 prove the measure/IMAGE assertions for EACH own regenerative law; SWITCH keeps MAIN's measure.

## 2. Stationarization, suffix law, support and atoms

Let nu be the OWN boundary law of 1W_0 1W_1 ... with independent p-blocks.
The frozen origin construction gives probability p(w)/M to each pair (w,j),
0<=j<=|w|, with independent surrounding blocks. Visible blocks 1w have positive
length, so their two-sided concatenation exists; every output coordinate is
measurable by examining finitely many finite blocks. This defines the stated mu.

To verify stationarity, test a nonnegative Borel function of the right tail.
Shifting an origin offset j<|w| gives the next offset in that same block.
The final offset shifts to a fresh boundary law nu; summing its contribution
over w gives nu/M. This is exactly the total original offset-zero contribution,
since the origin block at offset zero has distribution p. Other offsets match; mu(T^-1 E)=mu(E) for every Borel E.

Define F(v)=sum_(u:uv in W)p(uv) for every legal segment v. This sums distinct
complete block words ending in v, so p(v)<=F(v)<=1 and F(empty)=1.
Tonelli counts |w|+1 suffixes per word, giving sum_v F(v)=M; splitting the prefix as empty or u=t a gives

    F(v)=p(v)+sum_(a>=2:av in W) F(av).                  (2)

If C is ANY Borel subset of the boundary cylinder [1], then

    mu(v C)=F(v) nu(C)/M,       nu(1v C)=p(v)nu(C).      (3)

For nonempty v, the first identity sums origin words u v at offset |u|+1;
their next block boundary has independent law nu. For empty v it is the
offset-zero law. The second identity specifies the first boundary block. Both include null Borel C, not just cylinders.

Every sample has infinitely many future units. Thus the marker-free set N
and the entire eventually-marker-free set union_(k>=0)T^-k N have mu-mass zero.
They are not removed from the source. Every legal finite cylinder has positive
mass: close its unfinished segment by a unit, choose the finitely many resulting
legal blocks (and its initial suffix offset), and use their positive probabilities.
This also handles finite prefixes of marker-free histories, proving full support.
Boundary sequences have unique block parsing; fixing their first k blocks has
probability <=2^-k. Hence nu has no atoms. Equation (3), the countable suffix
partition and the null set N then show mu has no atoms at ANY source point.

## 3. The frozen all-point branch law and every-Borel IMAGE

On the first-unit stratum v[1], (2) proves normalization of the prescribed
q_1=p(v)/F(v) and q_a=F(av)/F(v) for legal av. Every legal value is positive;
illegal branches have value zero. The strata are Borel and the formulas constant
there, so these versions are Borel. For any C subset [1], (3) gives

    mu(1v C)=p(v)nu(C)/M,
    mu(av C)=F(av)nu(C)/M                              when av is legal.

Relative to mu(v C), these are precisely the frozen IMAGE factors. No null
measure is divided out: (3) proves the identities directly even when nu(C)=0.

On MAIN's marker-free N put R(y)=sum_(a>=2:y in E_a)rho(a). This is Borel,
0<=R<=1. The specified completion is exactly

    q_1(y)=1/(1+R(y)),   q_a(y)=rho(a)1_(E_a)(y)/(1+R(y)).          (4)

It is normalized, finite, and positive on every actual legal branch; the
denominator never vanishes. For E subset E_a intersect N, both E and I_a E
are null: a nonunit keeps the image marker-free, while prefix 1 makes it
eventually marker-free. Hence the every-Borel IMAGE identity holds there too.
Decomposing an arbitrary E subset E_a into its countably many first-unit strata
and its marker-free part proves, with the frozen values at EVERY point,

    mu(I_a E)=integral_E q_a dmu.                                  (5)

OFF has all nonunit prefixes legal on N, so R=1 in its own prescription.
SINGLE has no N: its first two unmarked letters would already be illegal. SWITCH is verified in section 8.
None of this claims continuity or a uniquely measure-induced value on N.

## 4. All finite histories, actual groupoid and full kernels

For a finite visible word u define D_u={xi:u xi in X}; keep this exact Borel
domain, including infinite-tail constraints, and D_empty=X. On D_u put

    Q_u(xi)=product_(j<|u|) q_(u_j)(u_(j+1)...u_(|u|-1) xi),
    Q_empty=1.                                                     (6)

Every factor evaluates an actual legal branch, so Q_u is Borel, positive and
finite. Iterating (5) and its nonnegative-function version proves every-Borel
IMAGE Q_u. On the common tail domain D_u intersect D_v, replacement vxi->uxi
has IMAGE Q_u/Q_v on every Borel subset. Division is only by a positive function.
These proofs apply separately to each control's own q and domains.

All actual triples are covered by these countably many prefix charts. Common
extensions of witnesses multiply both history densities by the same tail product;
therefore c=A_m(z)-A_n(y)=log(Q_v/Q_u) is independent of witnesses. Aligning
the intermediate shifts proves addition under composition and inverse sign.
This is the countable Borel actual-lag groupoid, not a free history. Each own version's FULL kernels are exactly:

    ker c = union_(u,v) { (u xi,|u|-|v|,v xi): xi in D_u intersect D_v,
                                              Q_u(xi)=Q_v(xi) };
    ker lag = the same union restricted to |u|=|v|, with no Q equality;
    their intersection requires BOTH conditions.                   (7)

Equations (2),(4),(6) and the own control formulas below supply explicit all-point
membership, with no finite-tail cutoff. These are entire kernels, not just
isotropy kernels. Zero clock is not silently identified with zero lag.

## 5. Entire isotropy, incoming histories and block/visible primitivity

For any of these sources, isotropy is zero unless the visible sequence is
eventually periodic; then its least eventual visible period d generates exactly
dZ. This follows directly from equality of unequal shifts and the subgroup law.
In MAIN and SWITCH a marker-free periodic tail is impossible: a repeated nonunit
letter would violate coprimality with itself in the same unfinished segment.
Thus their marker-free and eventually-marker-free histories have trivial isotropy.
SINGLE has no such histories at all. OFF's additional marker-free cycles are
explicitly retained below.

Every periodic MAIN/SWITCH/SINGLE core therefore contains a visible unit and
parses uniquely, cyclically, into blocks 1v with v in its OWN W. For such a block,
ending before the next unit, the finite-marker factors telescope as

    [p(v)/F(v)] [F(v)/F(v_tail)] ... [F(last)/F(empty)] = p(v).     (8)

For v empty this is p(empty). Consequently a cyclic block word (v_1,...,v_r)
has traversal time L=-log product_i p(v_i), which is >=r log2>0.
A proper visible power must take unit positions to unit positions; starting
at a unit, its shorter period therefore repeats complete blocks. Conversely
a repeated block word repeats the visible word. This proves equivalence of
block-necklace and visible-necklace primitivity, not merely an assumed coding.
Rotations starting inside a block belong to the same actual visible source orbit.
Different block necklaces, even with equal weight products, remain distinct packets.

If a source eventually reaches a primitive core of visible length d and time L,
c on its ENTIRE isotropy k d is k L: the finite prehistory cancels. Thus H=LZ;
otherwise H={0}. Extension fixed-object isotropy is trivial everywhere, since
all periodic L are positive; OFF has the same conclusion by section 7.
All incoming arrows to z are obtained from m,n>=0 and legal v of length n by
y=v T^m z in X, with g=(z,m-n,y). At height s their source height is s-c(g).
This includes every legal depth, all boundary tails and all actual loop labels.

Over one source orbit fix f and an actual arrow g:f->z. The physical phase is
h-c(g) modulo H_f; different choices change it by exactly H_f. Periodic source
orbits therefore give the entire phase set R/LZ, aperiodic ones a full real line.
These are orbit SETS only. One primitive necklace gives one packet; its k-fold
repetition has time kL, not a new packet. No incoming prefix or height is deleted.

## 6. MAIN's complete packet formula and precommitted tests

The preceding classification gives ALL MAIN packets, parametrized by primitive
cyclic words in W. Marker-free and eventually-marker-free orbits give only lines.
For n_i=|v_i| the exact primitive time is

    L=sum_i[(n_i+1)log2 + log Z_(n_i) - sum_(a in v_i)log rho(a)]. (9)

Multiplicity is by block necklace, not by numerical L. In particular Z_0=Z_1=1,
p(empty)=1/2, p((2))=1/8 and p((3))=1/24. The precommitted visible cores
1,12,1213 correspond to primitive block necklaces (empty),((2)),((2),(3)).
Their full positive primitive times are respectively log2, log8 and log192;
their source isotropy is respectively Z,2Z,4Z and H is that time times Z.
The differing singleton blocks make the last necklace primitive. Repetitions, incoming and phases follow section 5.

## 7. ARITHMETIC-OFF and SINGLE-LETTER-BLOCK: own complete ledgers

OFF's own p(w)=2^(-|w|-1)product rho(w_i) and M=2 enter the independent
stationarization proof above. Summing over all prefixes gives
F(v)=2^(-|v|)product rho(v_i). Thus q_1=1/2, q_a=rho(a)/2 on EVERY tail,
including N. All prefix domains are X. Equations (5)–(7) are its own IMAGE
and full kernels: Q_u=product b_(u_j). Its cylinder probabilities are these
products, so its own law is the full product b^N_0. All primitive necklaces
over B are packets, including the marker-free ones, of time sum_j log d_(u_j),
where d_1=2 and d_a=2a(a-1). Source isotropy, H, extension isotropy and phases
follow section 5 with these times. All incoming words are allowed. In particular
1,12,1213 again give log2,log8,log192, while the marker-free constant 2 gives
primitive log4. No marker-free OFF packet is discarded or transferred to MAIN.

SINGLE's OWN W,p and M=3/2 give F(empty)=1, F(a)=rho(a)/2. Its domains are
E_1=X and E_a=[1] for a>=2; its all-point law is
q_1(y)=1/2 if y_0=1, q_1(y)=1 if y_0>=2, and
q_a(y)=rho(a)/2 on [1], zero otherwise. This independently supplies every-Borel
IMAGE through (3)–(5), and its Q-products in (6) give full kernels via (7).
There is no possible marker-free or eventually-marker-free source to append.
ALL primitive necklaces in {empty} union A are its packets, with time sum -log p;
visible rotations, all legal incoming, H and phases follow the proven parsing.
Extension isotropy is trivial although individual branch clocks can be zero.
The three specified cores have primitive times log2,log4,log48 respectively,
with full H equal to those times times Z. Source periods remain 1,2,4.

## 8. BOUNDARY-SWITCH and an explicit noncanonical boundary

SWITCH keeps MAIN's X,mu,F and finite-marker law, but on N its OWN completion is
q_1^B=2/(2+R), q_a^B=rho(a)1_(E_a)/(2+R). It is Borel and normalized,
positive on every legal branch. The null-set and null-prefix-image proof in
section 3 gives every-Borel IMAGE for this separate version. Its whole cocycle
and entire kernels use these q^B in (6)–(7), also for prefixes entering N.
It has exactly MAIN's source isotropy, positive packet times and H-groups:
every periodic tail has infinitely many units, where the two versions agree.
Its marker-free and eventually-marker-free source orbits remain physical lines.

Let f_n=2^(2^n)+1. The identity product_(j<n) f_j=f_n-2 follows by repeated
difference of squares. If m<n, a common divisor of f_m,f_n divides 2; all
f_j are odd, so they are pairwise coprime. Thus y=(f_0,f_1,...) and every
shifted tail belong to N, and 2 is a legal predecessor. No primality is assumed.
For these tails R>=rho(2)=1/2. The actual arrow y->1y has MAIN clock
log(1+R), but SWITCH clock log(1+R/2), strictly different. Both y and 1y
are retained null sources. This proves version dependence of the full clock,
not failure of the every-Borel identity or a change of the periodic ledger.
Neither version is upgraded to a canonical or globally continuous completion.

## 9. Scoped gate and closure

All source, probability, IMAGE, full-history and control obligations above close
without deleting null states. MAIN's (12)^infinity has ENTIRE H=(log8)Z,
so log8 is primitive, not a hidden log2 repetition. It violates the frozen
prime-time target: STOP promotion. OFF and SWITCH share that adverse packet;
SINGLE has primitive log4. No retuning, selection or version repair. Strong naturalness OPEN; T3 NOT AUDITED; classical gates
NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED. No universal carrier no-go.
