# Factor-word return transport has two distinct log-two packets

Candidate ID: ANG-20260925-FWR01.
Outcome: OWNED FACTOR-WORD CLOCK; DUPLICATE LOG2 PACKETS — STOP / FORK
Paper471; version1; 2026-09-25; batch SYMBOLIC-RETURN-20260925-Y.
Exact analytic result for the frozen measured-history owner, not a Route result.

## Abstract

The full space consists of every finite ordered word of integers at least two,
with an interval attached to each word. Proper-divisor splitting and adjacent
multiplication determine the actual interval branches. All four frozen owners
have the prescribed inverse IMAGE law for the original counting-times-length
measure, including every cut and endpoint. In the entire product-six component,
MAIN has exactly two least-two cycles, with different full incoming basins and
the same entire isotropy-clock group \(\log 2\,\mathbb Z\).
Thus its primitive ledger duplicates the ordinary prime two.
Order-forgetting retains two such packets; the split-OFF and merge-OFF owners
terminate globally. The proof retains all terminal objects, incoming histories,
zero clocks and real phases. It makes no higher-period or other-product census.

## 1. Frozen owner and question

Write \(A=\{2,3,\ldots\}\), \(W=A^{<\infty}\), and
\(X=W\times[0,1]\), with discrete/product Borel structure and
\(\mu=\operatorname{counting}_W\otimes dx\).
The empty word is included and has product one. Each word component has mass
one; \(\mu\) is sigma-finite, not an asserted invariant probability.
The [card](candidate-card.md) fixes the operations, their order, and the measure.
No arithmetic label, geometric section, interval endpoint or null cycle is removed.

| Owner | Ordered operation list | Actual output word |
| --- | --- | --- |
| M: MAIN | All proper-divisor splits, then all adjacent merges | Literal result |
| S: split-OFF | Adjacent merges only | Literal result |
| K: merge-OFF | Proper-divisor splits only | Literal result |
| O: order-forget | MAIN's list | Nondecreasing sort of the result |

A split at position \(i\), with \(2\le d<a_i\) and \(d\mid a_i\), replaces
\(a_i\) by \((d,a_i/d)\); splits are lexicographically ordered by \((i,d)\).
A merge at \(i\) replaces \((a_i,a_{i+1})\) by \(a_i a_{i+1}\);
merges are ordered by \(i\). For each owner separately denote its list size by
\(h(w)\) and its actual output words by \(R_j(w)\), \(0\le j<h(w)\).
If \(h(w)=0\), the whole component is terminal. Otherwise
\[
 j=\min\{h(w)-1,\lfloor h(w)x\rfloor\},\qquad
 T(w,x)=(R_j(w),h(w)x-j).                                      \tag{1}
\]
In O, \(R_j\) already includes sorting; its unsorted source words remain objects.
The one-object chain is the divisor operation, (1), its original-measure
inverse density, and its full actual history groupoid. No classical symplectic
form, positive suspension roof, operator or determinant is supplied.

The target requires a nonempty positive ledger, every primitive equal to the
logarithm of an ordinary integer prime, and at most one full packet per prime.
All-prime coverage is additional. The frozen discriminating window is all
fixed and two-step periodic points with word product six, for each owner.

## 2. All inverses and every-Borel IMAGE

Let \(P(w)=\prod_i a_i\), with \(P(\varnothing)=1\).
Every operation, including sorting, preserves \(P\).
For fixed \(N\), the set \(W_N=\{w:P(w)=N\}\) is finite:
for nonempty \(w\), \(2^{|w|}\le N\), and every letter is at most \(N\).
This is a bound on state words, not a finite approximation to their intervals.

For \(h=h(w)>0\), the actual source intervals are
\[
 I_{w,j}=[j/h,(j+1)/h)\quad(j<h-1),\qquad
 I_{w,h-1}=[(h-1)/h,1].
\]
Each branch is an injective affine map onto the component \(R_j(w)\)
with interval image \(Y_j=[0,1)\) for \(j<h-1\), and \(Y_{h-1}=[0,1]\).
Its complete inverse and frozen density are
\[
 \theta_{w,j}(R_j(w),y)=\left(w,\frac{j+y}{h(w)}\right),\quad
 y\in Y_j,\qquad J_{w,j}=\frac1{h(w)}.                         \tag{2}
\]
The last-branch convention is essential: \(y=1\) has no inverse in a
nonlast branch. Interior cuts belong to the branch on their right.

For M, S and K, all inverse words are obtained as follows, retaining only
the owner's available operation. To reverse a split, merge each adjacent
pair of target letters and use its first letter as the split divisor.
To reverse a merge, expand each target letter \(c\) into every ordered pair
\((a,b)\) with \(a,b\ge2\) and \(ab=c\).
Rebuild the source list and rank, apply (2), and check the actual forward map.
For O, an unsorted target has no predecessor. For a sorted target, enumerate
every distinct permutation \(v\) of its letters, reverse the literal operations
into \(v\), and check O's actual sorted output and interval domain.
This is exhaustive because any forward step has exactly one of these operations
and one actual interval branch. Each target has finitely many predecessors;
different descriptions of one actual predecessor are deduplicated.

All domains are Borel, and (2) is the restriction of an affine germ.
For every Borel \(E\subset\{R_j(w)\}\times Y_j\), ordinary affine
change of variables gives
\[
 \mu(\theta_{w,j}E)=\frac1{h(w)}\mu(E)
                  =\int_E J_{w,j}\,d\mu.                     \tag{3}
\]
Counting gives both components mass one. This proves (3) for arbitrary
Borel sets, not merely cylinders or interval lengths. The germ in (2) fixes
the same positive finite value at all endpoints, whose null mass alone
would not fix an RN version. The actual branch partition is disjoint.
Consequently each owner owns
\[
 \kappa(w,x)=-\log J_{w,j}(T(w,x))=\log h(w)\ge0.               \tag{4}
\]
A legal step has zero clock exactly when \(h(w)=1\).
A terminal has no outgoing step or outgoing clock; its unit arrow still has zero.

## 3. Complete histories, kernels and phases

The following construction applies separately to all four owners.
Let \(D_r\) be the domain of \(r\) legal steps, \(D_0=X\), and put
\[
 Q_r(z)=\prod_{i=0}^{r-1}h(\operatorname{word}(T^i z)),\quad
 Q_0=1,\qquad S_r=\log Q_r.
\]
Retain every triple
\[
 G=\{(z,r-s,w):z\in D_r,\ w\in D_s,\ T^rz=T^sw\},\qquad
 c(z,r-s,w)=S_r(z)-S_s(w).                                    \tag{5}
\]
Its source is \(w\), range \(z\); equal triples are identified, not distinct lags.
Two witnesses for the same triple differ by adding the same integer to
both meeting depths. Using the larger witness extends a common legal tail;
its clock cancels. Thus (5) is well-defined. For composition, extend the two
middle histories to the larger of their depths. They are legal to that depth,
their clocks cancel, and lags and clocks add. Inverses negate both.
Countably many Borel witness relations make \(G,c\) Borel; a first-witness
enumeration gives a Borel expression without selecting source orbits.
In particular \((Tz,-1,z)\) has clock \(-\kappa(z)\).

A fixed legal inverse word of length \(r\) is affine on its actual Borel
domain, with IMAGE density \(J_r=Q_r^{-1}\), by repeated (3).
For two such inverse words \(\theta_\alpha,\theta_\beta\) with a common
tail domain, the history-pair map from \(w=\theta_\beta u\) to
\(z=\theta_\alpha u\) has, for every Borel subset of its domain,
\[
 J_{\alpha\beta}(w)=\frac{J_\alpha(u)}{J_\beta(u)}
                  =\frac{Q_s(w)}{Q_r(z)}=e^{-c(z,r-s,w)}.      \tag{6}
\]
Affine change of variables proves the identity also on cut-restricted domains;
the frozen germs and (5) ensure agreement at every common point.
The full kernels, with no omitted merging arrows, are exactly
\[
 \ker c=\{Q_r(z)=Q_s(w)\},\qquad
 \ker\ell=\{r=s\},\qquad \ker c\cap\ker\ell
       =\{r=s,\ Q_r(z)=Q_r(w)\},                               \tag{7}
\]
where each set consists only of actual triples from (5).

Write \(\mathcal I(y)\) for the entire inverse set in Section 2.
Then \(\mathcal I^0(y)=\{y\}\) and
\(\mathcal I^{r+1}(y)=\bigcup_{u\in\mathcal I^r(y)}\mathcal I(u)\)
give all predecessors at every depth, by induction in both directions.
Compatible infinite incoming histories are exactly sequences
\(z_0=y,\ z_{-i-1}\in\mathcal I(z_{-i})\) for every \(i\).
This is an exact compatibility condition, not a claim of infinite existence
from finitely many tests. The whole source orbit of \(y\) is
\[
 [y]_G=\bigcup_{\substack{s\ge0\\y\in D_s}}\ \bigcup_{r\ge0}
                   \mathcal I^r(T^sy).                        \tag{8}
\]
Thus terminals, infinite nonperiodic histories and all incoming trees remain.
Product preservation excludes incoming from every other \(W_N\), in all owners.

An isotropy triple is a coincidence of two iterates of the same point.
If its lag is nonzero, the intervening forward segment is a cycle.
Hence a non-eventually-periodic source, including every terminal-ending source,
has trivial isotropy and \(H=\{0\}\).
For a source eventually reaching a least-\(p\) cycle
\(f_0,\ldots,f_{p-1}\), let \(C_i=\sum_{j<i}\kappa(f_j)\) and \(C=C_p\).
Coincidences on that cycle have exactly lags \(p\mathbb Z\);
their clocks are exactly \(C\mathbb Z\). Initial tails cancel, so
\[
 \operatorname{Iso}_G(z)=p\mathbb Z,\qquad
 H_z=c(\operatorname{Iso}_G(z))=C\mathbb Z.                    \tag{9}
\]
This is the entire image, not a subgroup obtained from a chosen repetition.
Here \(C\ge0\), with \(C=0\) precisely when every core step has \(h=1\).

More explicitly, let \(\tau_z\) be first arrival at this core and
\(\epsilon_z\in\{0,\ldots,p-1\}\) its arrival index. Set
\(d_z=\tau_z-\epsilon_z\) and \(B_z=S_{\tau_z}(z)-C_{\epsilon_z}\).
All arrows between two points in its full basin are exactly
\[
 \ell=d_z-d_w+jp,\qquad c=B_z-B_w+jC,\qquad j\in\mathbb Z.      \tag{10}
\]
Extending to sufficiently late core meetings proves existence for every \(j\);
subtracting such a meeting proves the converse.

On all \(X\times\mathbb R\), an arrow sends \((w,t)\) to \((z,t+c)\).
Translation of \(t\) acts on its orbit set. Over a source class with reference
point \(a\), choose any arrow \(a\to z\) and call its clock \(B_z\).
Its extension classes are precisely the phases \(t-B_z\pmod{H_a}\);
changing the connector changes \(B_z\) by an element of the entire \(H_a\).
This asserts no measurable global selector or regular quotient.
Extension isotropy is source isotropy intersected with \(\ker c\).
For (9) it is trivial when \(C>0\), and \(p\mathbb Z\) when \(C=0\).
Each base class with \(C>0\) supplies one translation packet, primitive \(C\),
with all integer repetitions and all phases \(\mathbb R/C\mathbb Z\).
When \(H=0\), phases are real and there is no positive translation period.

## 4. Full-source control dynamics and terminal protection

For S, a step reduces word length by one and \(h(w)=|w|-1\).
A nonempty length-\(L\) word reaches a singleton in exactly \(L-1\) steps.
The empty component is already terminal. Thus every S source terminates.
Its remaining clock is
\(\Psi_S(w,x)=\log((L-1)!)\) for \(L\ge1\), and zero for the empty word.
For K, each legal split increases length by one while preserving product.
The bound \(2^L\le P(w)\) proves termination for every source; its terminal
word has no letter with a proper divisor. This conclusion requires no
periodic census and no unique-factorization theorem.
For either terminating owner let \(\tau(z)\) be its actual termination depth
and \(e(z)=T^{\tau(z)}z\); set \(\Psi_K(z)=S_{\tau(z)}(z)\) for K.

For either S or K, two sources belong to the same class exactly when
their actual terminal points \(e(z),e(w)\), including interval coordinates,
coincide. Every arrow in that class is exactly
\[
 (z,\tau(z)-\tau(w),w),\qquad c=\Psi(z)-\Psi(w).                \tag{11}
\]
Indeed a meeting implies the same terminal; extending it to that terminal
proves (11), and absence of cycles makes its lag unique.
Thus \(\ker c\) means equal \(\Psi\), \(\ker\ell\) equal \(\tau\),
and the joint kernel both, always within a common terminal fibre.
All source and extension isotropy are trivial, \(H=0\) globally,
and the phase is \(t-\Psi(z)\in\mathbb R\).
The inverse recursion in Section 3 is complete. No infinite incoming history
exists: backward S length increases but is product-bounded; backward K
length decreases. Terminal objects can nevertheless have incoming arrows.

For M and O, the only terminal words are empty words and irreducible
singletons. Product preservation shows that each such terminal point has no
incoming and is an isolated source class. Every word of composite product
has an outgoing operation, so its forward history is infinite.
Its entire incoming and phase ledger is (2), (5)–(10), including both
eventual cycles and non-eventual histories. No classification of their
unexamined periodic cores is inferred from the product-six calculation.

## 5. Entire product-six fixed and two-step window

Let \(A_6=(6)\), \(B_6=(2,3)\), \(C_6=(3,2)\), abbreviated below to \(A,B,C\).
These are all of \(W_6\): three letters would have product at least eight;
the only ordered two-factor decompositions of six are \((2,3),(3,2)\).
Write \(A_x=(A,x)\), and similarly for \(B_x,C_x\).
Every operation changes length by one, so there is no fixed point in this
component for any owner. The complete legal one-step tables are

| Owner | \(A_x,\ 0\le x<1/2\) | \(A_x,\ 1/2\le x\le1\) | \(B_x\) | \(C_x\) |
| --- | --- | --- | --- | --- |
| M | \(B_{2x}\) | \(C_{2x-1}\) | \(A_x\) | \(A_x\) |
| S | terminal | terminal | \(A_x\) | \(A_x\) |
| K | \(B_{2x}\) | \(C_{2x-1}\) | terminal | terminal |
| O | \(B_{2x}\) | \(B_{2x-1}\) | \(A_x\) | \(A_x\) |

In M and O the return on the A component is
\(D(x)=2x\) for \(x<1/2\), and \(D(x)=2x-1\) for \(x\ge1/2\).
Solving each branch equation \(D(x)=x\) gives exactly \(x=0,1\),
with both actually included. Checking the B and C rows yields
\[
 \begin{array}{c|c|c}
 \text{owner}&\operatorname{Fix}(T^2)\cap(W_6\times[0,1])
             &\text{least-two cores}\\ \hline
 M&\{A_0,B_0,A_1,C_1\}&(A_0,B_0),\ (A_1,C_1)\\
 O&\{A_0,B_0,A_1,B_1\}&(A_0,B_0),\ (A_1,B_1)\\
 S,K&\varnothing&\text{none}
 \end{array}                                                   \tag{12}
\]
For S and K a second step already fails everywhere in this component.
No half-open circle identification is made: zero and one are different objects.

The complete inverses on this entire component, with omitted sets empty, are
\[
 \begin{array}{c|c|c|c}
 &\mathcal I(A_y)&\mathcal I(B_y)&\mathcal I(C_y)\\ \hline
 M&\{B_y,C_y\}&\{A_{y/2}\}\ (y<1)&\{A_{(1+y)/2}\}\\
 S&\{B_y,C_y\}&\varnothing&\varnothing\\
 K&\varnothing&\{A_{y/2}\}\ (y<1)&\{A_{(1+y)/2}\}\\
 O&\{B_y,C_y\}&
 \{A_{(1+y)/2}\}\cup\{A_{y/2}:y<1\}&\varnothing
 \end{array} .                                                 \tag{13}
\]
In particular M's \(B_1\) has no predecessor but is not deleted, and
every O point \(C_y\) has no predecessor but has its stated outgoing step.

## 6. Entire incoming packets, kernels and adverse multiplicity

Put \(\mathcal D=\{k/2^r:r\in\mathbb N_0,\ k\in\mathbb Z,\ 0\le k<2^r\}\).
For both M and O, the full basins of their zero- and one-endpoint cores are
\[
 \mathcal B_0=\{A,B,C\}\times\mathcal D,\qquad
 \mathcal B_1=\{A_1,B_1,C_1\}.                                 \tag{14}
\]
To prove coverage, every B or C point reaches A in one step, and consecutive
A returns apply \(D\). Its complete inverse satisfies
\(D^{-1}\{1\}=\{1\}\) and
\(D^{-r}\{0\}=\{k/2^r:k\in\mathbb Z,\ 0\le k<2^r\}\), by induction from its two actual
branches. These are precisely the eventual zero or one returns.
Product preservation rules out incoming from anywhere else in \(X\).
Equation (13) iterated at every depth gives all compatible infinite backward
histories within these basins, including every endpoint restriction.

In each core, only its A step has \(h=2\); the other step has \(h=1\).
Thus its least source period is two and (9) gives, exactly,
\[
 \operatorname{Iso}_G=2\mathbb Z,\quad H=\log2\,\mathbb Z,\quad
 L=\log2,\quad \operatorname{Iso}_{G\ltimes\mathbb R}=\{0\}.      \tag{15}
\]
All positive repetitions are \(n\log2\), not \((\log2)/2\).
For an explicit full-basin kernel test, use the reference \(f_0=A_0\) or
\(A_1\), let \(r_z\) count A-starting steps before first core arrival,
and put \(a_z=r_z-\epsilon_z\), \(d_z=\tau_z-\epsilon_z\).
For every pair \(z,w\) in the same basin, all arrows and clocks are
\[
 \ell=d_z-d_w+2j,\qquad
 c=(a_z-a_w+j)\log2,\qquad j\in\mathbb Z.                       \tag{16}
\]
The clock kernel sets \(a_z-a_w+j=0\); the lag kernel sets
\(d_z-d_w+2j=0\); the joint kernel imposes both. This includes all
zero-clock merging arrows, not just units. All real phases are
\(t-a_z\log2\pmod{\log2\mathbb Z}\), equivalently \(t\pmod{\log2\mathbb Z}\).
The two basins in (14) cannot merge: a common future of their cores would
identify two different cycles of a deterministic map. They therefore
give two distinct full packets of the same primitive, separately for M and O.

For completeness, S's product-six classes are exactly
\(\{A_y,B_y,C_y\}\), \(0\le y\le1\).
Their clocks are zero, \(\tau(A_y)=0\), \(\tau(B_y)=\tau(C_y)=1\);
\(\ker c=G\), while the lag and joint kernels include the distinct
equal-depth arrows \(B_y\leftrightarrow C_y\). Their phases are real.
K's classes are exactly
\(\{B_y,A_{y/2}\}\) for \(y<1\), the singleton \(\{B_1\}\), and
\(\{C_y,A_{(1+y)/2}\}\) for all \(y\in[0,1]\).
Here A has \(\tau=1,\Psi=\log2\), and B,C have \(\tau=0,\Psi=0\).
All three K kernels on this component consist only of units; phases are
\(t-\Psi\). Both controls have \(H=0\), as also proved globally in Section 4.

## 7. Decision, limitations and reproducibility

MAIN owns its all-point clock and its complete tested packet ledger.
Its two distinct primitive-\(\log2\) packets violate uniqueness per prime,
so the candidate stops. Neither an endpoint deletion nor sorting the source
is an allowed repair; the separately owned O control also duplicates this clock.
S and K establish that the two directions of rewriting are needed for returns
here, not that their combination supplies a prime-unique mechanism.
Equal-width port counts are explicit design input: generic branching can
produce this clock, so stronger arithmetic naturalness remains OPEN.
No longer cycle or other product was enumerated.

T0 and measured clock ownership are established; arithmetic T1 is NOT PASSED.
The bounded T2 uniqueness test fails. T3 is NOT AUDITED; classical fields
are NOT APPLICABLE, formal Route coordinates UNASSIGNED, Route B NOT INVOKED.
No analytic operator, invariant flow measure, RH statement or novelty certificate
is claimed. This is a STOP / FORK record, not cumulative credit from controls.

Exact inputs are the full 101-line frozen card and the repository template.
Card SHA256: 5f7989f2062a2fbb66a251b20d8646e010b3d94e4788e00a72be5dc1a3218820.
All science above uses symbolic definitions and exact algebra, without numerical
code. Mechanical checks cover links, consistency, line counts and SHA256 only.
See [claim ledger](claim-ledger.md), [README](README.md), the
[batch exposure record](../470-gcd-memory-register/batch-log.md), and
[evidence directory](evidence/) for separately staged review material.
No scope, raw, peer answer or reviewer body was read by this author.

AI assistance: the AI author supplied derivation, drafting and internal checks.
Same-author helper direct_controls read only the frozen 101-line card for
bounded S/K derivation; its earlier scout role inspected filenames only.
The author independently checked the control arguments. It was not an
independent reviewer. Shared prior authorship and outcome-unsealed design
reasoning are disclosed in the card/batch record; same-model review is
NOT_CALIBRATED. No human or external verification is certified.
ARS writing guidance was used for claim bounds and disclosure, not review credit.
Data availability: definitions and proofs are in this package; no external
dataset or scientific computation was used. No human subjects are involved.
Human authorship, funding and conflicts were not supplied and are not invented.
