# P207 manuscript B — independent deduction and source subtraction

2026-09-06 UTC. Reviewer `/root/batch197_fifth_scout`, not a mathematical
contributor to P207. The reviewed object is the physical seven-page
`papers/207-upper-neighbor-rank-dynamics/frozen_round1/`, not the current
lifecycle index. All 106 physical inputs, including the 105-entry freeze
manifest itself, were pinned before mathematical work. The previous task
of this process was a utility-only receipt/code audit; that familiarity is
disclosed, not counted as a mathematical review. Root and
`batch197_fosp_gate` are authors; `batch197_lzk_gate` is A.

## 1. Literal map, quantifiers and complement

Throughout, n >= 3, the carrier is the complete labelled box {0,1,2}^n,
indices are modulo n, both distinct neighbors use the old state, and
ties contribute zero. At coordinate i,

`U(x)_i = [x_(i-1)>x_i] + [x_(i+1)>x_i]`.

The entrance is the least t >= 0 with U^(t+2)x = U^t x, not the first
repeat of either coordinate separately. Define F using strict lower
comparisons and Jx = 2-x. Comparing each old pair gives U=FJ and hence
`U^(-1)(b) = J(F^(-1)(b))`, with every source coordinate recovered by J.
No division by rotations or complementing the target is involved.
U=FJ is not JFJ. For example F(0202)=0202 but U(0202)=2020 and
U(2020)=0202. Input complement therefore supplies all one-step inverse
sets but no iteration conjugacy. Both the primitive and this transport
receive zero independent contribution credit.

## 2. Permanent extrema and the independent finite certificate

At a strict minimum, U produces 2. Either neighbor can count only its
other neighbor as greater, so its output is at most 1. The center is
now a strict maximum. At a strict maximum, U produces 0 and both
neighbors count the old center, so their outputs are at least 1. The
center is now a strict minimum. Thus E(x) is a monotone set under U,
and each of its sites alternates 0 and 2 after its first update. This
is an exact local argument and does not require a cyclic atlas.

The finite lemma has initial coordinates -6,...,6, rows v^t on
|j| <= 6-t, and four updates. Its premise is v^4_0 != v^2_0. Its
conclusion is a time 1 <= s <= 4 and |j| <= 5-s where j is a strict
extremum of v^s and was not one in v^0. The latter narrower interval
keeps both neighbors of the witness inside its computed row.

B enumerates edge-sign words e of length 12, not height words of
length 11 or 13. Put e_i=sign(w_(i+1)-w_i). For each e define the
suffix height-lift counts

`c_12(a)=1; c_j(a)=sum_(b: sign(b-a)=e_j) c_(j+1)(b)`.

The weight sum_a c_0(a) counts all height lifts uniquely. A lexicographic
lift is recovered using positive suffix counts. Every initial strict
extremum depends only on the adjacent signs. Moreover the first update
at an interior site is `[e_left=-1]+[e_right=+1]`; consequently all
subsequent truncated rows are identical for all lifts of a given sign
word. Testing one lift, and directly checking its height inequalities,
therefore verifies the implication for its entire class. This is a
proved quotient of precisely the original finite window box, not a
sample and not an enlarged cyclic box.

The actual standalone B output records:

| Quantity | Count |
|---|---:|
| All length-12 sign words | 531,441 |
| Unrealizable sign words | 381,392 |
| Realizable sign words | 150,049 |
| Total height-lift weight | 1,594,323 = 3^13 |
| Equal-center classes / height lifts | 129,934 / 1,427,787 |
| Changed-center classes / height lifts | 20,115 / 166,536 |

All 20,115 changed classes are printed in the complete canonical, each
with its exact lift weight, witness time and witness position. All
realizable classes also enter an ordered SHA-256 stream. The height-lift
recurrence and exhaustive outer loop prove coverage; a digest alone
would not. Each computed row is additionally compared with a direct
height-comparison update on its representative.

The separate artifact auditor rederived the author's actual partition
on all 177,147 inner height words: 158,643 equal, 18,300 with an inner
witness, and 204 requiring exterior letters. It validated all nine
distinct extensions of each exceptional word and all 1,836 stored
witnesses directly. That inspection intentionally reads author data;
it is not the independent B producer or an additional B replay. The
weighted B census also matches A's direct 13-height census exactly.
The older failed shorter-cone statements remain historical failures,
not premises of this lemma.

## 3. From the finite lemma to every cycle length

Read thirteen consecutive cyclic coordinates about any site, including
repeated coordinates for 3 <= n < 13. This is one of the height words
covered above. Locality proves inductively that every computed cone
entry agrees with the corresponding actual cyclic iterate. Repetition
does not require distinct initial coordinates and does not change any
strict comparison in the unrolled cone.

If E(U^4 a)=E(a), monotonicity rules out every new extremum at all
intermediate times. Apply the finite lemma at each center to obtain
U^4 a=U^2 a. The n+1 inclusions among E(U^(4q)x), q=0,...,n+1,
cannot all be strict in an n-element set. Some q <= n has equal
four-step endpoints, so U^(4q+2)x is U^2-fixed. This set is forward
invariant because U commutes with U^2. Hence

`U^(4n+4)=U^(4n+2)` and `H(n)<=4n+2`.

This is a deductive all-length consequence of a declared
computer-assisted finite lemma. It is not extrapolated from n <= 10
and is not a sharp clock. Any recurrent point outside Fix(U^2) would
eventually enter it and then return outside, contradicting invariance.
Thus the recurrent set is precisely Fix(U^2).

## 4. Recurrent language and a third core representation

For y=Ux and x=Uy, a height 2 at either time forces height 0 at the
other. The only two-time columns are 00, 02, 20, 01, 10, 11. A 00
column forces both adjacent columns to be 00, by applying both
zero-output equations at its zero heights. Connectedness leaves only
the all-zero word in that case.

For a nonzero word write S0=02, S1=20, W0=01, W1=10, N=11.
An N column needs one height-two neighbor at each time; those neighbors
are distinct and must be S0,S1 in either order. In particular N cannot
neighbor W0 or W1. That exclusion uses N's own equation; merely testing
the weak center would be insufficient, as the preserved author failure
correctly explains. At W0, exactly one x-neighbor is positive and no
y-neighbor is 2. Its zero x-neighbor must be W0, and its other neighbor
must be S1 or W1. Exchange times for W1. Thus each weak site belongs
to a unique same-phase dimer, with opposite-phase strong/weak exterior
neighbors. S0 has S1,W1,N neighbors, and S1 has the time-reversed rule.
Substitution into both equations proves sufficiency as well.

In x, zeros therefore form singleton S0 sites or W0 dimers. Positive
runs are a singleton S1 with optional neutral at either end, or a W1
dimer. This gives exactly positive words 2,11,12,21,121 and zero
lengths 1,2. A neutral next to a zero needs a strong singleton zero:
the left zero boundary of 12/121 and right zero boundary of 21/121
must each be singleton. Conversely these run conditions uniquely
recover all columns and enforce both updates. No positive-only word
is an exception: every U-image contains a zero at a source maximum.
A fixed point cannot contain 2, and without 2 every 1 outputs 0;
therefore only 0^n is fixed and every other core point has exact period 2.

B forms a graph R on the 36 ordered pairs of the six columns. There
is an edge (L,C)->(C,R) exactly when the two literal rank equations
hold at C. Its 45 edges are generated from those equations, without
the author's eight-role transitions or A's four-height overlap graph.
A labelled closed walk gives columns (x_i,y_i) enforcing y=Ux,x=Uy.
Conversely x determines y and the entire walk. This is a bijection,
including short periodic words; trace counts labelled states, not
rotation classes.

To verify the full determinant independently, B computes det(I-zR)
at all integer z=0,...,36 by fraction-free Bareiss elimination with
exact divisibility checks and row-pivot signs. A 36-by-36 determinant
has degree at most 36, so these 37 samples determine every coefficient.
Newton forward differences in the binomial polynomial basis reconstruct
it exactly using rational arithmetic; all coefficients are integral.
The result is

`det(I-zR)=(1-z)(1-z^2-4z^3-2z^4+z^8)`,

with every coefficient of degrees 10 through 36 zero. B counts the
closed walks separately through exponent 60. They agree with the
author's 1+tr(Q^n) and A's overlap graph. This is not a characteristic
polynomial inferred from only a few traces.

The author Q is also valid: each emitted word recovers unique weak
dimer ends and the oriented neutral role, so it introduces no
orientation multiplier. Compressing its deterministic intermediate
roles gives the stated two-phase block transfer B(z); direct 2-by-2
algebra gives `(1+z^4)^2-(z+2z^2)^2`. With D(z) the displayed degree-8
polynomial, the formal identity -z D'(z)/D(z) yields the stated eight
initial traces and recurrence for n >= 9. Formal exponents 1,2 do not
extend the original dynamical carrier below n=3. All finite graph
and trace manipulations are deducted standard tools.

## 5. Exact seed and the length-three boundary

Let m=floor(n/2), n>=4, and start from 20^(n-1). Before the fronts
meet, at time s<m the center is 2 when s is even, an interior site
at distance 0<d<s is 2 when s-d is even, a frontier site d=s>0 is
1, and all sites farther away are zero. At s=0 this is the seed.
The interior alternates because adjacent phases are opposite; a
frontier 1 has two zero neighbors and outputs 0; the next zero
sees one positive neighbor and outputs 1; the zero immediately inside
the front sees two positive neighbors and outputs 2. The center is
permanent, and distant zeros stay zero. These cases prove the induction.

At time m, for n=2m the remaining zero sees both frontier ones and
becomes 2; the state is alternating 02. For n=2m+1 two adjacent
zeros each see one frontier and become a weak 11 dimer. Both states
satisfy the core language. At each earlier positive time a frontier
has height 1 and is a strict maximum, so after two more updates its
height is 2; it cannot already be in Fix(U^2). At time zero the
zero run has length n-1>=3, also excluding the core. Thus the seed's
entrance is exactly m. Since 01^(n-1) maps to the seed, and the seed
is not initially recurrent, its entrance is exactly m+1.

For n=3, the carrier's cycle is the complete three-vertex graph.
Equal source heights give 000; two equal lower heights give a rotation
of 110; two equal higher heights give a rotation of 200; three
distinct heights give a permutation of 210. These are all in the
proved core. The noncore source 001 proves H(3)=1. B checks all
27 states here and only the already-stated seed family for n=4,...,64.
It does not promote those seed checks to full boxes or a sharp H(n).

## 6. Complete static inverse and independent source-pair decoder

For F, every image has a zero at a source minimum. For an all-zero
target the two zero-output inequalities across every edge force equal
source heights, giving exactly three sources. A positive-only target
has none. In a mixed target, adjacent zero positions force equal
source heights, so each zero run has one source height a. At its
boundaries a is at most the adjacent positive source values, including
a singleton zero run. Positive source values cannot be 0. At an
interior position of a positive target run, source height 1 would see
only source heights 1,2 and output 0. Interior source heights are
therefore 2. Five positive positions would force a middle 222 and
output 0, so only run lengths 1,...,4 occur.

Enumerating the two endpoint heights then gives the complete table in
the manuscript: w=2 has sources 1 or 2 with the stated lower exterior
bounds; w=1 has exactly one exterior equality and the other exterior
strictly lower; w=11 has 11,22 or the two boundary-height-two mixed
strings; w=12/21 has its corresponding mixed string; w=111 has
122 or 221; w=121 has 121; w=1111 has 1221. All eight displayed
kernels follow. B independently regenerates the kernel counts for all
positive source strings at lengths 1,...,6, including the zero kernels.

Choosing the zero-run heights and one permitted positive string between
each pair reconstructs every source at its original coordinates.
Conversely a source recovers every choice, proving injectivity. This
gives the trace of the ordered kernel product, including r=1 where
the two exterior heights coincide. Rechoosing a starting zero run
only cyclically permutes the product; zero-run lengths affect placed
coordinates, not the kernel count. These static facts are deducted.

B's independent whole-target inverse producer does not use that
decoder or TCSD's sign-fibre union. Its nine states are source pairs
(a,b). Appending c gives (b,c) with target label `[a>b]+[c>b]`.
For a labelled target b_0...b_(n-1), the trace of its nine-by-nine
label-matrix product counts exactly the closed source paths. Starting
at (x_(n-1),x_0), read the centers x_0,...,x_(n-1); closure enforces
the cyclic source boundaries and gives one path per labelled source.
The DFS decoder recovers every source code and compares the entire
sorted source list with direct literal source enumeration, not just
its cardinality. The prefix-matrix trace is independently compared
with both. These comparisons cover every source and target for
n=3,...,10, including empty fibres and all maximizers.

For time data B simultaneously advances the full vector of initial
states, assigning a height at the first time its current state is
U^2-fixed. This is neither author Kahn peeling nor A's per-orbit walk.
All 88,560 states in those eight boxes are assigned within the stated
bound. All language, fixed/core, height, source-set, trace-count and
equality comparisons pass. Finite boxes corroborate the deductions;
they do not prove their all-length quantifiers.

## 7. Whole-target maximum: every noncommuting product case

Write A=K2, J0=K1, B0=K11. All kernels are entrywise nonnegative and
K12,K21,K111,K121,K1111 are entrywise <= A. Expanding a cyclic trace
as a sum of entry products proves monotonicity under these replacements;
no positive-semidefinite order or commutation is asserted. Let r>=2
be the product length, k its B0 count, and j its J0 count afterward.

The leading A block has determinant 1 and trace 3. Its positive
eigenvalues are lambda=(3+sqrt(5))/2 and lambda^(-1); the third is 0.
Let a_r=(lambda^r+lambda^(-r))^(1/r). The singular values of J0 are
2,1,1 and the Frobenius norm of B0 is 3. Norm monotonicity gives
`||J0||_r <= sqrt(6) < lambda < a_r`, `||B0||_r <= 3`.
For r>=3, `||J0||_r <= cubert(10)` and `3*cubert(10)<lambda^2`.
The rational lower bound lambda>13/5 and 169^3>270*25^3 establish
the latter strictness exactly, without floating-point estimates.

The precise prior norm theorem is Tropp, printed pp.49–53, Definition
6.15, Example 6.18 and Theorem 6.32 with its proof sketch. Apply that
two-factor UI-norm inequality in Schatten norm t>=1 to get
`||UV||_t <= ||U||_(pt) ||V||_(qt)` for conjugate p,q>1.
For the first s factors take t=r/s, p=s/(s-1), q=s, 2<=s<=r.
Both exponents on the factors are the needed previous r/(s-1) and r;
all t>=1. Finally an SVD gives |tr P|<=||P||_1. This proves
`|tr(M1...Mr)| <= product ||Mi||_r` with no commutation,
invertibility, symmetry or PSD assumption on the matrices. The theorem
and the exponent reduction are prior support, not a new axis.

The proof then treats every possible number of costly kernels:

- k=0: the bound is a_r^r=L_(2r), strictly smaller if any J0 occurs.
- k=1,j=0: cyclicity gives tr(B0 A^(r-1))=tr(A^r). The positive
  exponent kills third-coordinate contributions and the leading blocks
  agree. This exact identity is needed; the coarse norm bound alone
  would not establish the required comparison.
- k=1,j>0: for r=2, tr(B0 J0)=4<7. For r>=3 combine the scalar
  norm bounds 3*cubert(10)<a_r^2 for one B0 and one J0; all additional
  J0 factors are strictly smaller than a_r. No factor commutation or
  bound on a combined matrix B0 J0 is being assumed.
- k>=2: Hölder gives at most a_r^(r-k)3^k. Since
  (a_r/lambda)^r=1+lambda^(-2r)<10/9, this is strictly below
  (10/9)lambda^(r-k)3^k, including r=k. The remaining inequality
  `(10/9)3^k < lambda^(k+floor(k/2))` starts with
  10<lambda^3 and 30<lambda^4 for k=2,3. Increasing k by two
  multiplies the left by 9 and the right by lambda^3>9.

Every positive run and following nonempty zero run cost at least two
target sites, and every B0 costs one additional site: n>=2r+k.
The even Lucas subsequence is lambda^s+lambda^(-s), strictly increasing
for s>=1. Thus k<=1 gives at most L_(2r)<=L_(2 floor(n/2));
k>=2 is strictly below it. The no-positive-run fibre is 3. For r=1
the nonzero kernel traces are 0,3,3,1,1,2,1 in the stated order;
for n>=4 these are below L4=7. At n=3 they give precisely 000
and rotations of 002,011 as the seven size-three maximizers.

For equality at n>=4, r>=2, k<=1 and q=n-2r must be 0 or 1.
If q>=2, strict growth of the even Lucas sequence already forbids
equality. At q=0 every run is singleton; any J0 is strict, so exactly
alternating 02 targets remain. At q=1 exactly one run is doubled:

- A doubled zero gives rotations of 00(20)^(r-1)2, provided all
  positive singleton runs are 2; any 1 produces strict J0.
- A doubled positive run has kernel B0,K12 or K21. B0 with all
  remaining factors A attains by the exact identity. Any J0 is
  strict. These targets are rotations of 011(02)^(r-1).
- For K12/K21 without J0, A^(r-1) has a strictly positive leading
  2-by-2 block, and A-K12/A-K21 is nonzero and nonnegative there.
  The trace expansion is therefore strictly smaller. With J0,
  strictness already follows after entrywise replacement. Longer
  positive runs cannot fit the single spare position.

This exhausts necessity and sufficiency. Even alternation has exactly
two labelled rotations. Each odd family has one unique doubled run,
so its rotational stabilizer is trivial; presence of symbol 1
separates the two families. There are therefore exactly 2n odd
maximizing targets. B checks all A/J0/B0 words for lengths 2,...,10
and the displayed fixed identities through exponent 100, but the
uniform argument above, not those pressure tests, proves the maximum.

## 8. Fully deducted adapters and residual value

The original TCSD contract and exact gap proof were read in full.
Translate its height alphabet by +1 and write D(x)_i=sign(x_(i+1)-x_i).
Then U=G D, where `G(s)_i=[s_(i-1)=-1]+[s_i=+1]`.
For every rank target b its entire inverse is the disjoint union of
D^(-1)(s) over G(s)=b. Each source stays at its original labels,
and its recovered signs determine its unique stratum. TCSD evaluates
each stratum: equality edges are deleted; invalid long/monotone strict
runs give zero; an alternating skeleton gives a Lucas count; doubled
runs split it into the proved Fibonacci gap product. Thus the whole
static inverse already has a complete evaluated prior adapter, not
merely a sequence coincidence. It receives zero fresh credit here.

TCSD's maximum controls one sign-target fibre, not a union over G.
For b=0101 the two feasible strata (-,0,0,+) and (0,+,-,0) each
contain three sources, giving six in total. They are, respectively,
1000,2000,2111 and 0010,0020,1121. The original TCSD gap-merging
proof does not itself compare those aggregated unions for all b;
nor does its sign equality classification classify rank targets.
This is a precise boundary of the inspected adapter, not a proof
that no stronger summation adapter can exist. The whole-target
mixed-kernel comparison and exhaustive equality analysis remain the
once-counted rank-family inverse residual under the inspected evidence.

The attainer source sets are also entirely deducted. On alternating
lower-rank targets, mark exactly the source sites of height 1. Valleys
have heights 0/1 and peaks 1/2; adjacency of two marks is precisely
the forbidden equality 1=1. This is a bijection with independent
sets of the labelled cycle. Reconstruct heights 1 on marks, 0 on
unmarked valleys and 2 on unmarked peaks. Equivalently shift the
valley height by one to obtain weak maps of a crown to a two-chain.
Doubling a valley source position gives the odd 00 family; doubling
a peak gives the odd 11 family, whose only options here are 11/22
because its zero boundaries are <=1. Deleting the repeated source
position reverses each map. These full source-set adapters and Lucas
counts prove attainment, not optimality among all other rank targets.

B also inspected P112's literal tournament edge update and P186's
literal support map in their original TeX. P112 reorients tournament
edges using old outdegrees and retains equal-score edges; P186 takes
the support of a_j-j from an ordered subset. Neither literal is this
fixed-labelled ternary-cycle rank update. This is a bounded literal
comparison, not a claim to exclude every encoding or factor. A narrow
textual search of prior TeX/proof filenames produced no additional
direct literal hit; that nonhit has no priority value. TCSD's explicit
full adapter takes precedence over any keyword nonhit.

After those deductions, the retained conjunction remains the specific
permanent-extremum/local-growth temporal theorem, exact core and seed,
together with the shared whole-target extremal comparison once.
Generic finite graph counting, finite-set termination, static source
decoders, Lucas counts, norm inequalities and complement transport
are not extra axes or extra papers. No inspected complete adapter
eliminates this whole residual; this supports only the narrow internal
value judgment, not global originality or an external novelty claim.

## 9. Primary sources actually read and inaccessible bodies

All access statements below concern this B task on 2026-09-06. Search
results with unrelated uses of rank were discarded as theorem evidence.

| Source | Actual B access and use | Limit |
|---|---|---|
| Zabih–Woodfill 1994, ECCV pp.151–158, DOI 10.1007/BFb0028345 | Full eight-page saved author PDF read as layout text; author PDF newly opened online; Springer metadata checked. Section 3 defines the strict-lower primitive. | Image-correspondence applications do not supply the reviewed iterative theorem. The publisher's 2005 online date does not change the 1994 conference citation. |
| Mukherjee 2011, PRL 32(7), pp.1001–1008, DOI 10.1016/j.patrec.2011.02.005 | Publisher preview retrieved through indexed search: abstract, introduction, visible strict-lower Definition 2.1, section excerpts and conclusion. Direct opening returned 403. | The convergence theorem and proof remain unread. No claim about its complete hypotheses, dual-rule extensions or nonapplicability to all encodings is made. LNR-S1 remains open. |
| Currie–Visentin 1991, Order 8, pp.133–142, DOI 10.1007/BF00383399 | Actual publisher metadata and abstract read; historical fence/crown enumeration identified. | Subscription body unread. No theorem number or exact global rank maximum is attributed to it. The elementary attainer bijection is verified directly. |
| Tropp 2022, Caltech CMS Lecture Notes 2022-01, DOI 10.7907/nwsv-df59 | Saved primary PDF/layout text: title/citation pages and printed pp.49–53, complete applicable norm definitions/theorem/proof sketch. | Web PDF opener failed; the already-saved primary file was successfully read. No second download or full-book read is claimed. |
| Goles–Olivos 1980, Discrete Math. 30(2), pp.187–189 | Actual publisher abstract retrieved through indexed search; binary symmetric threshold period-at-most-two statement inspected. | Direct body opener failed; no full-body or UGR embedding claim. |
| Goles–Martínez 1981, Information and Control 51(2), pp.95–97 | Actual publisher abstract states a symmetric multithreshold-to-binary embedding; metadata read. | Direct opener failed despite its indexed open-archive label. Its body and exact embedding hypotheses remain unread. |
| Goles et al., arXiv:2309.01854v1 | Primary version-pinned HTML Sections 1–2 and opening Section 3.1 read, including binary-spin weighted-neighbor-sum rule and tie conventions. | No complete UGR-to-threshold encoding was established. Equal center and equal neighbor sum for triples 012 and 111 produce distinct U outputs 1 and 0, excluding only the obvious equal-neighbor-weight scalar representation, not all threshold lifts. |

Primary links: [Zabih–Woodfill author PDF](https://www.cs.cornell.edu/~rdz/Papers/ZW-ECCV94.pdf),
[Springer conference record](https://link.springer.com/chapter/10.1007/BFb0028345),
[Mukherjee publisher preview](https://www.sciencedirect.com/science/article/abs/pii/S0167865511000420),
[Currie–Visentin publisher record](https://link.springer.com/article/10.1007/BF00383399),
[Tropp primary notes](https://www.tropp.caltech.edu/notes/Tro22-Matrix-Analysis-LN.pdf),
[Goles–Olivos publisher abstract](https://www.sciencedirect.com/science/article/pii/0012365X80901211),
[Goles–Martínez publisher abstract](https://www.sciencedirect.com/science/article/pii/S0019995881901996),
[version-pinned threshold-network paper](https://arxiv.org/html/2309.01854v1).

Fresh bounded queries included exact-title owner searches, upper/greater
rank iteration synonyms, cycle/largest-preimage rank queries, symmetric
multithreshold keywords and 2024–2026/730-day-filtered searches. Their
precise scope and failures are in `SOURCE_ACCESS_LOG.md`. Nonhits are
not a novelty proof. No source was purchased, uploaded to, contacted,
or accessed by bypassing a restriction. No specialist or external
reviewer was fabricated.

## 10. Initial B conclusion and unchanged limitations

No Critical, Major or Minor mathematical, artifact, build or claimed-scope
finding remains in the reviewed narrow P207 contract. Recommend exact
no-change continuation, pending an actual root response and B delta
acceptance. This is not a completed B delta, Round2, terminal paper
gate or five-paper completion.

The Mukherjee body access limit remains unresolved and must not be
renamed source clearance. Its visible definition is strict lower rank;
the unread body is not positive evidence of a general upper-rank theorem.
The nonconjugacy example prevents only the naive iterative transport.
Any later applicable primary theorem or full internal adapter reopens
the affected scope. No sharp global H(n) for n>=4, larger alphabet,
all-time inverse, basin census or global priority claim is admitted.
The status remains `OWNER_AMBER / HOLD_EXTERNAL`.
