# P211 B deductive reconstruction and independent review devices

2026-09-08 UTC. This is a source-only mathematical review document, not
a producer result, infrastructure certificate or manuscript acceptance.
The proof-writer discipline is used to separate claims, assumptions,
dependencies, proof steps and boundaries. The claims below are assessed
**PROVABLE AS STATED** within their explicit hypotheses by the deductions
given here. That mathematical status does not assert that the still-unrun
B implementation works or that the whole review has passed.

## 1. Claim, notation, assumptions and strategy

Fix any integer n >= 1. The carrier O_n is all nondecreasing functions
`f:[n] -> [n]`. It is not restricted initially to extensive, top-fixing
or idempotent functions. Write X for the increasing list/set of right
kernel-block endpoints of f and Y for its increasing image. Then
`n in X`, `|X|=|Y|>=1`. Conversely any such pair determines one whole
function, denoted here `f_(X,Y)`, by pairing the increasing lists.
For any support C containing n, `e_C(i)=min{c in C:c>=i}`.
Set `A=Y union {n}` and use the literal update

`T(f)=e_X composed with e_A`, with e_A acting first.

This is recomputed at each feedback step, not a fixed product of the
original two projections and not the composition-power sequence of f.
Endpoint coordinates, ceiling idempotents, completed support A, and
the admissible rank difference `|A|-|X| in {0,1}` are established source
background, not P211 residual novelty. The direct proofs below suffice
mathematically without importing a theorem from a finite computation.

The four manuscript-level claims under review are: exact one-step image
and common anchors; exact all-time image dynamics; full recurrent core,
terminal map and sharp height; and a complete one-step predecessor atlas
over every labelled target. No global fibre maximization, basin formula,
all-time inverse, priority, or universal no-factor/no-lift claim is added.

B's strategy is to turn the interlaced image into a boundary word, derive
the death time of every individual labelled boundary, and derive the
inverse by first choosing kernel extras. These are independent review
coordinates and counting devices for the same claims, not additional
manuscript contributions. The graph-composition method of section 8 is
a finite validation design, not a substitute for sections 2--7.

## 2. Exact image and anchor identity

**Claim.** A target g with kernel endpoints `W={w_1<...<w_k}` and image
`Z={z_1<...<z_k}` belongs to T(O_n) exactly when

`w_i <= z_i < w_(i+1)` for i<k, and `w_k=z_k=n`.

For every source, if these are the supports of Tf, then
`W intersection Z = X intersection A`.

**Proof.**

1. List A increasingly. On the inner ceiling block ending at a in A,
   the product has value `ceil_X(a)`. As a increases these values are
   nondecreasing. The A sites with a given output z form a consecutive
   nonempty group. Its last site w is the right kernel endpoint of the
   resulting whole function. Thus each resulting pair satisfies `w<=z`.
2. If the next group has last site w', its first site a' has
   `ceil_X(a')>z`, so a'>z and hence w'>z. This proves the strict cross
   inequality. The final inner site is n and its output is n, giving
   `w_k=z_k=n`. In particular W is contained in A and Z in X.
3. If c belongs to both X and A, the A site c maps to c; the next A site,
   if present, lies above c and cannot map to c. Hence c is the last
   member of its output group and lies in W intersection Z. Conversely
   W subset A and Z subset X give the reverse inclusion. This proves
   the exact anchor identity, not merely a count inequality.
4. Conversely assume the displayed target inequalities. Construct the
   valid source with kernel Z and image W; both have the same positive
   rank and contain n. On each inner W block ending w_i,
   `ceil_Z(w_i)=z_i`, because `z_(i-1)<w_i<=z_i`, with previous bound 0
   for i=1. Therefore `e_Z e_W=g`. This gives a labelled predecessor
   without enumerating possible sources and proves sufficiency. QED.

Extensivity and top fixing follow from the image inequalities but do not
replace them. For example, the target values `(2,3,4,4)` are extensive
and top fixing but have `(W,Z)=({1,2,4},{2,3,4})`, violating
`z_1<w_2`; it has no predecessor.

## 3. Boundary language and all labelled death times

**Equivalent coordinates.** At each site write K if it lies only in W,
V if it lies only in Z, B if it lies in both, and ignore sites in neither.
The image criterion is exactly a concatenation of words `(K V)* B`,
ending at the B site n. Common anchors partition the line into independent
strict intervals. In one such interval before anchor c the coordinates are

`w_1<z_1<...<w_r<z_r<c`.

Indices in this paragraph are local to that anchor interval. There may
be no strict pair (r=0). This equivalence follows by reading each target
pair in its increasing order: equality gives B, strict inequality gives
K followed by V, and the cross inequality separates successive pairs.

**Claim.** After one T step that strict interval becomes

`(z_1,w_2),...,(z_(r-1),w_r)`, followed by `(c,c)`.

The two outer strict sites disappear and every remaining strict site
exchanges K/V roles. If the original 2r strict sites are q_1,...,q_(2r),
then at epoch t site q_j survives exactly when
`t<min(j,2r+1-j)`. It has its original role at even t and the opposite
role at odd t. Anchors persist at every t.

**Proof.**

1. For a target-image state the literal next product is `e_W e_Z`.
   The inner block ending at z_i maps to w_(i+1) for i<r. The inner
   blocks ending at z_r and c both map to c, so they merge and their
   right endpoint is c. No later block can map below c, and every
   earlier interval terminates at its own common anchor; intervals
   do not interact. If r=0, the anchor block maps to itself; if r=1,
   both strict sites disappear immediately. This proves the one-step
   list, including both boundary cases.
2. At t=0 all strict sites are present. The one-step list removes q_1
   and q_(2r), retaining q_2,...,q_(2r-1) in their original increasing
   order and swapping their roles. Applying the same calculation to
   the retained alternating word removes its two outer sites. By
   induction at t<=r the survivors are exactly
   `q_(t+1),...,q_(2r-t)` with t role swaps. This is equivalent to the
   asserted strict inequality involving the minimum of the distances
   to the two ends. At t>=r no strict site remains, and anchors stay.
3. The full pair of supports at every time is therefore recovered from
   this per-label rule. It reconstructs the entire nondecreasing map,
   not just its rank, run length, terminal class or abstract orbit. QED.

The source function `boundary_language` implements this exact language;
`surviving_masks` uses the closed individual death epochs and parity,
not recursive simulation of the literal product.

## 4. Exact times, core, terminal map and height

**Claim.** Let R(g) be the largest strict-pair count before an anchor in
an image state g, taking R=0 when no strict pair occurs. Then its first
fixed epoch is R(g). The fixed and recurrent points of the full carrier
are exactly all e_C with n in C. For arbitrary f, the terminal projection
has support `X intersection A`; its full time is 0 when f=e_C and
otherwise `1+R(Tf)`. The maximum full time is H_1=0 and
`H_n=ceil(n/2)` for n>=2.

**Proof.**

1. In an image state, some strict site survives until the epoch just
   before the largest r is exhausted, so the map is not fixed before
   R. At R all strict sites vanish, and only equal support pairs at
   common anchors remain; this is their ceiling projection. That map
   is fixed. Thus the first fixed epoch is exactly R, not merely at
   most R. Every image orbit stabilizes, hence so does every full
   orbit after its first literal step. No nonfixed cycle can recur.
2. If X=Y then n is in Y and `T(f)=e_X e_X=e_X=f`. Conversely a fixed
   f must lie in the proved image; section 3 excludes a strict pair
   in a fixed image state, so its kernel and image coincide. Thus
   the fixed set is exactly the stated projections and has size
   `2^(n-1)`.
3. For arbitrary f the first step has anchor set `X intersection A`
   by section 2, and those anchors survive forever by section 3.
   Its terminal is exactly e_(X intersection A). For a nonfixed f,
   equality has not occurred at epoch 0, so the first fixed epoch
   is one plus the first fixed epoch of Tf. Fixed sources require
   their separate zero-time branch; applying `1+R` to them is wrong.
4. A strict interval with r pairs uses 2r distinct labels below its
   next anchor, so `r<=floor((n-1)/2)`. Every nonfixed full source
   consequently has time at most `1+floor((n-1)/2)=ceil(n/2)`.
5. For n=2m+1>=3 choose the histogram with count 2 at each odd label
   below n and count 1 at n. Its kernel is
   `{2,4,...,2m,2m+1}`, image `{1,3,...,2m-1,2m+1}`. Its first
   image has strict pairs `(1,2),(3,4),...,(2m-1,2m)` before n,
   so R=m. Its first map value changes from 1 to 2, proving that
   the initial step is nontrivial, and its full time is m+1.
6. For n=2m choose the histogram with count 2 at every odd label and
   0 at every even label, including n. The kernel is `{2,4,...,2m}`,
   image `{1,3,...,2m-1}`, completed by n. Its first image has
   strict pairs `(1,2),...,(2m-3,2m-2)` before the final anchor n;
   the last two inner blocks ending 2m-1 and 2m merge. Thus R=m-1
   and its genuine first value change 1 to 2 gives full time m.
   At m=1 the strict list is empty and the source still takes one
   step, so this argument includes n=2. At n=1 the sole map is the
   identity and its time is 0. These witnesses prove sharpness. QED.

## 5. Every-target inverse: forced and free sites

Fix a labelled target g. If it fails the exact image condition, section 2
proves its fibre empty. Otherwise retain its pairs `(w_i,z_i)` and put
z_0=0. Define disjoint free gaps

`D_i={z_(i-1)+1,...,w_i-1}`.

**Claim.** All predecessors, and only predecessors, arise from supports
X,A satisfying the following local constraints and one global rank branch:

- Z is forced into X and W is forced into A.
- No X site lies in `[w_i,z_i)` and no A site in `(w_i,z_i]`.
- Inside each D_i choose disjoint extra X and A sites, with every extra
  X site strictly before every extra A site. Unused sites are permitted.
- With a total of a extra X sites and b extra A sites, require b-a to
  be 0 or 1. Set Y=A in the first case and `Y=A minus {n}` in the second.

**Proof of necessity.**

1. Any predecessor product has output support Z contained in X and
   kernel endpoints W contained in A, by the grouping proof in
   section 2. Since the A site w_i maps to z_i, there is no X site
   in `[w_i,z_i)`. If an A site occurred in `(w_i,z_i]`, its outer
   ceiling would also be z_i; that would extend the right endpoint
   beyond w_i, a contradiction. This proves the two prohibitions.
2. The forced and forbidden target spans, along with D_i, cover
   all sites from 1 to n. Within D_i, an A site a must map to z_i:
   it exceeds z_(i-1), so cannot map to an earlier output, and it
   is below the forced w_i, so cannot skip the next output. Any X
   site at or above a but still in D_i would instead be an output
   strictly between z_(i-1) and z_i. Hence every extra X site must
   be strictly less than every extra A site in that gap; coincidence
   is also excluded. This covers arbitrary empty/nonempty choices.
3. The actual full source has equal kernel/image ranks, and A is
   obtained by adjoining n to its image. Consequently `|A|-|X|`
   is 0 or 1. Since W and Z each have size k, the same difference
   is b-a. The two cases determine respectively whether Y=A or
   Y=A without n. No further missing-label branch is available.

**Proof of sufficiency and uniqueness.**

4. Conversely choose the stated local data and branch. X contains
   Z and in particular n, and A contains W and n. In branch 0,
   X,Y have rank k+a=k+b. In branch 1, their ranks are
   k+a=k+b-1. This is positive because k>=1. Thus the pair X,Y
   reconstructs a unique whole nondecreasing source.
5. Every selected A site in D_i follows all extra X sites there,
   and the next X site at or above it is the forced z_i. The
   forced A site w_i also has next X site z_i. No A site appears
   between w_i and z_i. Therefore exactly the A group ending w_i
   maps to z_i. Running through all target ranks proves that the
   resulting product is the specified whole target g.
6. From any resulting source, X and Y are recovered uniquely as
   its kernel and image, A as `Y union {n}`, the branch by whether
   n lies in Y, and each extra set by removing forced supports.
   Thus the construction is injective as well as exhaustive. QED.

This proof is separate from the temporal deletion proof: neither its
necessity nor sufficiency uses any time bound, recurrent classification
or orbit computation.

## 6. B's kernel-first decoder and binomial identity

Choose first an arbitrary subset L of the union of D_i as the extra
kernel sites. Put `q_i=max(L intersection D_i)` when nonempty, and
q_i=z_(i-1) otherwise. Exactly the following sites are eligible extra
image sites:

`E_i={q_i+1,...,w_i-1}`; set E to their disjoint union.

Let a=|L| and e=|E|. The exact separate branch counts are

`N_delta = sum_(L subset union D_i) binom(e(L), |L|+delta)`, delta=0,1,

with binomial equal to 0 outside its usual range. All limits depend only
on the labelled target. For each term choose that many sites of E, put
`X=Z union L`, `A=W union selected`, and use the branch rule for Y.

**Proof.** Once L is fixed, the ordering requirement in section 5 is
exactly that each image extra lie strictly after q_i in its gap. There
are no further local restrictions among these selected image sites.
The global rank condition requires precisely a+delta selections from
the disjoint union E. Thus the displayed binomial counts each possible
image subset once. Section 5 proves the corresponding sources are
exactly all predecessors, with no duplication across kernel choices or
branches. This also proves correctness when some or all gap lengths
are zero, and when an entire kernel choice admits neither branch. QED.

The proposed function `kernel_first_atlas(target)` uses only this target
data. It never queries the actual graph, actual predecessors, a source
enumeration, or the literal update. An outer validation stage may then
attach independently enumerated histogram IDs and compare entire fibres.

## 7. Laurent formula by a different coefficient calculation

For a gap of length d, a legal colouring with a kernel extras and b image
extras chooses a+b sites and splits their increasing order into the first
a kernel sites and final b image sites. Therefore its weighted polynomial is

`P_d(u)=sum_(a,b>=0; a+b<=d) binom(d,a+b) u^(b-a)`.

Multiplying these independent local polynomials and extracting the two
global rank differences 0 and 1 gives the exact every-target count.
This is the manuscript coefficient identity, with its known rank-branch
background credited separately, not a global fibre extremum.

B computes each coefficient by parity instead: for signed exponent e,

`[u^e]P_d = sum_(s=|e|, |e|+2,...,d) binom(d,s)`.

Indeed putting s=a+b and e=b-a gives the unique nonnegative integers
`a=(s-e)/2`, `b=(s+e)/2` exactly for the indicated parity and range.
Convolving these coefficient lists and comparing exponents 0 and 1
separately with section 6's N_0,N_1 is therefore a genuinely different
counting implementation. It is not an enumeration of selected unions
and splits, nor a product of ternary gap words. The all-target sum is
|O_n| because the proven inverse atlas partitions all sources by their
unique literal target, including empty fibres.

## 8. Independent finite graph certificate design

A histogram `(h_1,...,h_n)` records the number of inputs mapped to each
label. Nonnegative entries summing to n are in bijection with all O_n;
stars and bars gives `binom(2n-1,n-1)` states. Positive cumulative sums
recover the kernel support, and occupied bins recover the image.

The literal product is evaluated by pushing each inner A-block width to
its first outer X cut, retaining all block endpoints, widths, suffix
masks and assigned output labels. This is a whole-function evaluation of
`e_X e_A`, independently of the image-language/clock/inverse formulas.

Given the literal arrow array F on all M states, define full arrays
`G_0=identity`, `G_(t+1)[s]=F[G_t[s]]`. The first t with consecutive
entries equal in a source column is its first fixed epoch. The full
carrier guard M is a purely finite-graph bound: a path on M vertices
that has no fixed entrance by then has repeated a vertex on a nonfixed
cycle. Successful stabilization of every column rules out all such
cycles. This design retains every table through its duplicated final
stable array and does not import the closed clock as a stopping bound.

Separately compare every image state's all-label survival masks at epochs
0 through R+1 with those full arrays, every source's predicted terminal
and full time, every target's target-only decoded complete ID fibre,
both inverse rank branches, and the parity witness. Original n=1,...,7
and 2353 states are the complete approved finite scope, not proof of n
beyond 7. At this preparation gate the program has not been imported,
compiled or executed; no numerical checks or passing stdout are claimed.

## 9. Hand attacks, dependency and risk ledger

The n=3 source histogram `(2,0,1)` has values `(1,1,3)`, kernel `{2,3}`,
image `{1,3}`. Right-factor-first gives histogram `(0,1,2)` and one
further step gives `(0,0,3)`, while reversing the original factors
already gives `(0,0,3)`. This attacks both composition orientation and
the full/image clock distinction. The extensive nonimage in section 2
attacks substitution of a weaker image predicate.

For the n=3 constant-three target, D_1={1,2}. With L empty the 0 branch
gives one source and the 1 branch gives two. With L={1}, only the
0 branch has one source; L={2} and L={1,2} give zero. Thus both branch
counts are 2, with histograms `(0,0,3),(0,1,2),(0,3,0),(3,0,0)` in
lexicographic order. This attacks loss of either rank branch and kernel
choices that have no legal completions.

Dependency order is: support grouping -> exact image/anchors -> labelled
deletion -> core/time/sharp witnesses; support grouping -> forced/free
inverse constraints -> kernel-first bijection -> binomial/Laurent count.
The two substantive axes meet only at the elementary support interface.
The finite design evaluates the literal map separately and then attacks
both axes, rather than using one claimed formula as evidence for another.

Remaining risks are implementation mistakes before actual runtime
reception; familiar-source/nonblind review; the thinness of elementary
deletion and ordered colour counting; and bounded external ownership
coverage. A precise old whole-map adapter or direct owner could still
remove residual value. Neither this proof nor a later finite success
would establish priority, universal nonfactorization, infrastructure
acceptance or permission to release externally. OWNER_AMBER and
HOLD_EXTERNAL remain in force.
