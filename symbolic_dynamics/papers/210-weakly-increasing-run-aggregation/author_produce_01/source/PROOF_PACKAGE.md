# P210 proof package

## Claim

For every integer $N\ge1$, let $\mathcal C_N$ be all ordered positive compositions of $N$. The map $F$ synchronously sums each maximal weakly increasing run of **old** parts. Its fixed points are the strict descents, and its sharp maximum stabilization time is
$$H(N)=\max\{h\ge0:1+h(h+1)/2\le N\}.$$
The complete one-step image is characterized by the attained-minimum suffix scan below and is explicitly weight-preserving bijective to the nonempty compositions into positive triangular parts. Every-target endpoint-partition fibre bookkeeping is valid support with zero separate novelty credit.

## Status

PROVABLE AS STATED. These are the already admitted deductions, rewritten self-contained, not new claims or a new independent review. Root and /root/twenty_seventh_finite_scout are original proof contributors. /root/p210_author is manuscript/verifier author. All remain ineligible to independently review P210.

## Assumptions

1. $N$ is a positive integer; every part is a positive integer.
2. Parts are ordered. Each update selects all old strict-descent boundaries at once and sums the intervening runs. Newly formed sums are not reconsidered within the same update.
3. Round $t\ge1$ maps time $t-1$ to time $t$. Stabilization time counts nonfixed updates before first fixation.
4. A block is born at round $t$ only when it is the union of at least two old blocks in that round; unchanged blocks retain identity.

## Notation

$|A|$ is the mass of an interval block $A$. $T_k=k(k+1)/2$, $M_t=1+T_t$, and $\mathcal I_N=F(\mathcal C_N)$. A refinement of $s$ is a positive weakly increasing sequence of total $s$. For target suffix $(s_i,\ldots,s_m)$, feasibility means consecutive refinements have strict descents at their boundaries. The threshold $r_i$ is the minimum first part among all feasible suffix refinements, or undefined when none exist. There is no claim that the set of possible first parts is an interval.

## Proof strategy and dependency map

1. Positivity and strict length descent give termination and fixed points (generic support).
2. Persistent surviving boundary + rightmost/leftmost parents + induction + integrality give old left mass at least $t$ and preceding-round right birth.
3. Two disjoint first parents + step 2 + induction give new mass at least $M_t$.
4. A last nonfixed round + step 3 give the upper clock; descending-prefix orbit induction with arbitrary surplus gives equality.
5. Cumulative target cuts give unique refinement segmentation (generic support).
6. An attained suffix minimum + positivity exhaust exactly three cases and characterize the image.
7. Unique reset-cycle parsing + reserve-the-final-triangular-part inverse give a mass-preserving bijection. Known triangular enumeration is its consequence, not a new independent axis.
8. Endpoint-restricted partition multiplicities + step 5 give every-target fibre formula (support only).

No external mathematical theorem is needed for the deductions. Primary sources are used to subtract ownership of ordinary constructions and known counts, not to conceal missing steps.

## Proof

### Step 1. Coarsening and fixed points

Represent the parts as consecutive intervals partitioning $N$ labelled unit cells. An update deletes cuts but never inserts them, and sums of positive parts remain positive with unchanged total. A state is fixed exactly when every adjacent comparison is a strict descent. Otherwise some run has at least two parts, so length strictly decreases. The finite orbit therefore reaches a fixed point and has no longer cycle.

### Step 2. Deleted cuts force left mass

Claim: if a cut disappears in round $t\ge1$, its old left mass is at least $t$; for $t\ge2$ its old right block was born in round $t-1$.

At $t=1$, positivity gives the mass inequality. For $t\ge2$, write $A,B$ for the adjacent time-$(t-1)$ blocks at the disappearing cut, so $|A|\le|B|$. At time $t-2$, let $a$ be the rightmost parent of $A$ and $c$ the leftmost parent of $B$. Their common cut survived round $t-1$, hence $|a|>|c|$. If $B$ was unchanged in round $t-1$, it equals $c$ and $|A|\ge|a|>|c|=|B|$, impossible. Thus $B$ was born in that round. Its first internal cut was deleted then and has left block $c$. By induction $|c|\ge t-1$, so integrality gives $|A|\ge|a|\ge|c|+1\ge t$.

The conclusion concerns the specific right block; it does not suppose that all parents of a new block are new.

### Step 3. New blocks force triangular mass

For $t=1$, a new block contains at least two positive old blocks, so has mass at least $2=M_1$. For $t\ge2$, take its first two old parents $A_1,A_2$. Their cut disappears in round $t$. Step 2 gives $|A_1|\ge t$ and says $A_2$ was born in round $t-1$. Induction gives $|A_2|\ge M_{t-1}$. Since the two parents are disjoint, the new mass is at least $t+M_{t-1}=M_t$. Any other parents add positive mass.

### Step 4. Sharp all-size clock and every surplus

If a state has stabilization time $t\ge1$, round $t$ creates a block. By step 3, $N\ge M_t$, proving the upper bound $t\le H(N)$. If $N=1$, the sole state $(1)$ is fixed.

For every $h\ge1$ and $r\ge0$, start from $a=(h,h-1,\ldots,1,1+r)$. At time $j$, $1\le j\le h$, the state is
$$F^j(a)=(h,h-1,\ldots,j+1,\ r+1+T_j),$$
with empty prefix for $j=h$. Initially only $(1,1+r)$ merges. Given the formula with $j<h$, the suffix mass is at least $j+1$ and every earlier OLD prefix pair remains a strict descent. Only the last prefix part joins the suffix in that update, proving the next formula. Thus exactly $h$ nonfixed updates occur, for every surplus, ending in one part. For fixed $N\ge2$, choose $h=H(N)$ and $r=N-M_h$ to attain the upper bound.

### Step 5. Unique refinement segmentation

Suppose $F(a)=s=(s_1,\ldots,s_m)$. Every output cut is an original cut at cumulative target mass, so the segmentation of $a$ into segments of totals $s_i$ is unique. These are the maximal weakly increasing runs; each is a weakly increasing refinement and successive segment endpoints descend strictly. Conversely, concatenate any such refinements with strict boundary descents. Those segments are exactly the maximal runs, hence the image is $s$. This proves necessity, sufficiency and no overcounting.

### Step 6. Attained-minimum suffix threshold

For the last part $s_m$, the all-one refinement attains minimum $r_m=1$. Assume the right suffix is feasible with attained minimum $r$. To attach a new refinement, its last part $b$ must exceed some attainable first part $c\ge r$. Thus $b\ge r+1$ is necessary. Conversely, every refinement with ending part at least $r+1$ can attach to a suffix attaining $r$.

If $s_i\le r$, no such ending part exists. If $s_i=r+1$, that ending part consumes the entire mass, forcing singleton $(s_i)$ and new minimum $s_i$. If $s_i\ge r+2$, the refinement $(1,s_i-1)$ is weakly increasing and ends at least $r+1$, so minimum $1$ is attained. These cases are exhaustive. Failure cannot be rescued by a larger suffix first part. Induction and step 5 prove the complete image iff test in $O(m)$ integer comparisons. This is not a bit-complexity bound independent of integer size.

The targets $(2,3,2)$ and $(2,2,3)$ have identical total and multiset; the first passes with preimage $(2,1,2,1,1)$ while the second fails. The temporal total-mass bound does not supply the position-sensitive image result.

### Step 7. Explicit triangular coding, including the last-one boundary

Read an image target right to left. Write $b\ge1$ for the rightmost part, which sets threshold $1$. A part one above the threshold increments it; a larger part resets it to $1$. The remaining read-list uniquely consists of complete cycles
$$2,3,\ldots,k,\ k+2+u\qquad(k\ge1,\ u\ge0)$$
followed by a terminal string $2,3,\ldots,k$, $k\ge1$. A string is empty for $k=1$.

Encode $b$ as $b-1$ initial ones. In scan order, encode each complete cycle as $T_{k+1}$ followed by $u$ ones. Encode the terminal string as the final part $T_k$. The output is nonempty. A complete cycle has weight $(T_k-1)+(k+2+u)=T_{k+1}+u$, and the rightmost part plus terminal string has weight $b+T_k-1=(b-1)+T_k$, so total weight is preserved.

Conversely, reserve the final part $T_k$ of a nonempty triangular composition. Parse the rest uniquely as initial ones followed by triangular parts at least $3$, each with its maximal following string of ones. If there are $b-1$ initial ones, begin the target read-list with $b$. For every subsequent part $T_{j+1}$ with $u$ following ones, append $2,3,\ldots,j,j+2+u$. Finally append $2,3,\ldots,k$ and reverse the list. Every step is a legal increment/reset, so step 6 puts the target in the image. Its unique scan recovers the parsed blocks, and reserving the last triangular part recovers the terminal string even for $T_1=1$. The constructions are mutually inverse.

The known count therefore has formal series $\Theta/(1-\Theta)$ with $\Theta=\sum_{k\ge1}z^{T_k}$. Indeed, lists of length $q\ge1$ have series $\Theta^q$; positivity makes every coefficient finite and $\Theta(0)=0$. Removing the first part yields $i_N=\sum_{T_k\le N}i_{N-T_k}$ with auxiliary $i_0=1$. The empty auxiliary object is not a new $N=0$ carrier. These counting methods and their reset language are already owned.

### Step 8. Supporting fibre formula

Let $P_s(a,b)$ count weakly increasing refinements of total $s$ with endpoints $a,b$, and set it to zero outside $1\le a\le b\le s$. If $a=b$, it equals $1$ exactly when $a\mid s$. If $a<b$, reserving one $a$ and one $b$ and choosing arbitrary additional multiplicities gives
$$P_s(a,b)=[z^s]\,z^{a+b}\prod_{j=a}^b(1-z^j)^{-1}.$$
The order is uniquely sorted. Step 5 now gives
$$|F^{-1}(s)|=\sum_{1\le a_i\le b_i\le s_i}\prod_iP_{s_i}(a_i,b_i)\prod_{i<m}\mathbf1_{b_i>a_{i+1}}.$$
For evaluation define $v_m(a)=\sum_bP_{s_m}(a,b)$ and
$$v_i(a)=\sum_bP_{s_i}(a,b)\sum_{c<b}v_{i+1}(c),\qquad |F^{-1}(s)|=\sum_av_1(a).$$
The inner sum attaches every feasible right suffix with smaller first endpoint. Singletons and empty fibres require no exceptional rule. This is ordinary transfer bookkeeping, not a third advance.

## Corrections or missing assumptions

None required for the exact admitted contract. The all-surplus witness is stated for all $h\ge1,r\ge0$, not merely at maximal $h$ for a chosen total. The paper does not silently strengthen fixed-point classification to unique global endpoint or claim all deepest states have the witness form.

## Open risks and exclusions

No mathematical gap is knowingly left in the above deductions; independent manuscript review is still pending. The occupied carrier/ancestry/partition/run-network/triangular-count/reset ingredients are deducted in SOURCE_AUDIT.md. Global ownership remains uncertain. No maximal-fibre theorem, pointwise closed clock, higher-iterate inverse, full deepest-state classification or asymptotic theorem is admitted. The finite verifier cannot replace these proofs. OWNER_AMBER / HOLD_EXTERNAL remain.
