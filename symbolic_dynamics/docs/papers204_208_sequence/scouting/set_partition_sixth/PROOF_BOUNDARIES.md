# Sixth-lane proof package and admission boundaries

2026-09-06 UTC. Author: `batch197_fifth_scout`. This is a negative scout
package, not an independent review or a manuscript. All seven executed
literals remain `NO_PROMOTION`; UZ is an exact old negative control.

## Claim, status and dependencies

| Literal / proposed claim | Proof status | Dependency and resulting boundary |
|---|---|---|
| UPC: complete update reduction, $F^4=F^2$, exact recurrent strata and all inverse fibres | PROVABLE AS STATED | Transitive closure, Hasse paths, upper-closure generators; full deduction below, zero new axes |
| TDP: eventual fixed points for every finite nonempty ambient point set | PROVABLE AS STATED | Convexity of depth regions and nested finite-set erosion; not a sharp grid clock |
| MHT: eventual periods at most two; exact maximum fibre | PROVABLE AS STATED | Symmetric incidence, minimum-rank descent, and the unsatisfiable empty-edge boundary; zero new axes |
| SHD: all-parameter clock/core and a separate full inverse theorem | NOT CURRENTLY JUSTIFIED | Static shattering duality does not supply these results |
| UD: all-parameter clock/core and a separate full inverse theorem | NOT CURRENTLY JUSTIFIED | Inverse is exactly old UZ after output complementation; irregular finite periods are not a temporal proof |
| AKC: all-partition attraction to the noncrossing core, sharp clock and full inverse | NOT CURRENTLY JUSTIFIED | Noncrossing Kreweras results cannot be extended through cycle-support canonicalization without a proof |

The dependency order for the UPC proof is closure invariance, interval
classification, the complement-of-upper-closure formula, then time/core and
inverse consequences. Its inverse argument is separate from its time
calculation, but both are entirely accounted for by this adapter.

## 1. UPC: all-state adapter

### Assumptions and notation

Fix $n\geq0$. A state $A$ is any directed graph on $[n]$ whose edges
respect the fixed natural order. Let $F(A)$ contain precisely the ordered
pairs with exactly one positive-length directed path in $A$.
Let $P=\operatorname{TC}(A)$ be the strict reachability poset and $C$ its
cover relation. For $i<_Pj$, write
$[i,j]_P=\{i,j\}\cup\{k:i<_Pk<_Pj\}$.

Partition $P\setminus C$ as $Q\sqcup B$, where $Q$ consists of those
pairs whose intervals are chains and $B$ contains the other pairs.
Order $Q$ by interval inclusion: $(k,l)\leq(i,j)$ when $k,l\in[i,j]_P$.
This is an ordinary finite poset. Write $\uparrow S$ for the upward
closure of $S\subseteq Q$, $M=\min Q$, and $M_q=M\cap\downarrow q$.
Every $M_q$ is nonempty; all expressions also apply when $Q$ is empty.

### Step 1: closure and the permanent skeleton

Every cover pair in $P$ must be an edge in $A$, since otherwise a path
would have an intermediate vertex. A cover has exactly one path in $A$,
namely that edge. Every output pair is already reachable. Thus

$$C\subseteq F(A)\subseteq P,\qquad \operatorname{TC}(F(A))=P.$$

Consequently each $P$ is a permanent stratum, and all states of that
stratum are precisely the relations between $C$ and $P$.

### Step 2: which shortcuts survive

If $(i,j)\in B$, the finite interval has at least two maximal chains.
Indeed each element of a finite interval lies on a maximal chain, so a
unique maximal chain would contain the entire interval and make it a
chain. Distinct maximal chains give distinct cover paths, all present in
$A$. No member of $B$ can therefore occur in $F(A)$.

For $q=(i,j)\in Q$, the cover path through its chain interval is always
present. A second path exists exactly when $A$ contains a noncover
shortcut with both endpoints in that interval. Such a shortcut belongs
to $Q$, not $B$, since its own interval is a subchain. One shortcut
already gives a second path by replacing the corresponding stretch of
the cover path; every non-cover path must use such a shortcut.

Putting $S=A\cap Q$ gives the full literal identity

$$F(A)=C\cup N(S),\qquad N(S)=Q\setminus\uparrow S. \tag{1}$$

The coordinates $A\cap B$ are free input bits erased by one update.
Equation (1) is not only a factor on recurrent states: it describes
every source in every reachability stratum.

### Step 3: time and recurrent states

For any $S\subseteq Q$ and $q\in Q$,

$$
q\in N^2(S)
\iff (\forall y\leq q)(\exists s\in S)\ s\leq y
\iff M_q\subseteq S.
\tag{2}
$$

The forward implication follows by choosing each minimal $y\leq q$;
the reverse implication follows because every $y\leq q$ lies above a
minimal member of $Q$. Define

$$K(T)=\{q\in Q:M_q\subseteq T\},\qquad T\subseteq M.$$

The minimal-coordinate restriction of $K(T)$ is exactly $T$, so these
sets are distinct. Equation (2) says $N^2(S)=K(S\cap M)$.
Furthermore $N(K(T))=K(M\setminus T)$: a generator from $K(T)$ lies
below $q$ exactly when some minimal member of $M_q$ belongs to $T$.
It follows that

$$F^4=F^2.$$

In the $P$ stratum the recurrent states are exactly $C\cup K(T)$ for
$T\subseteq M$, in number $2^{|M|}$. If $M$ is empty there is one
fixed state $C$; otherwise all these recurrent states form two-cycles.
There are no further recurrent states, because (2) is a retraction onto
this explicitly described invariant set.

The universal height is at most two and is sharp for every $n\geq4$.
On four vertices, take the chain covers $12,23,34$ and the shortcut
$14$. The orbit is

$$
\{12,23,34,14\}
\longmapsto\{12,23,34,13,24\}
\longmapsto C\longleftrightarrow P.
$$

The first two states are distinct from the eventual two-cycle. Adding
isolated vertices proves sharpness for larger $n$. For $n\leq3$ there
are no branching intervals and every chain shortcut is a minimal member
of $Q$; all states are already recurrent. Empty and singleton vertex
carriers each have their single empty-relation fixed point.

### Step 4: all inverse fibres

For an arbitrary target relation $Y$, compute $P=\operatorname{TC}(Y)$
and its $C,Q,B$ as above. Necessarily $C\subseteq Y$. Put
$T=Y\cap Q$. The fibre is empty unless

$$Y\cap B=\varnothing\quad\hbox{and}\quad T\text{ is a downset of }Q.$$

When these conditions hold, let $D=Q\setminus T$, an upper ideal.
Equation (1) requires $\uparrow S=D$. In a finite poset this is
equivalent to

$$\min D\subseteq S\subseteq D.$$

For necessity, no generator can lie outside $D$, and every minimal
member of $D$ must generate itself. For sufficiency, every member of
$D$ lies above a minimal member of $D$, and upward closure cannot leave
the upper ideal. Hence the full fibre, with no quotient or missing
states, is

$$
F^{-1}(Y)=\{C\cup S\cup R:\min D\subseteq S\subseteq D,\ R\subseteq B\},
$$

and its cardinality is

$$|F^{-1}(Y)|=2^{|B|+|D|-|\min D|}. \tag{3}$$

All decoded sources have closure $P$ because they contain $C$ and lie
inside $P$. Thus no hidden cross-stratum source can occur. Empty $D$,
empty $Q$, and empty $P$ are included in (3).

### Credit and verification boundary

This proves a complete negative adapter, not a new research contract.
The map is a reachability-stratified complement-of-upper-closure rule;
its inverse is exactly the generator interval of an upper ideal with
independent erased bits. Both prospective axes receive zero credit.
The paper-specific maximum across all $P$ is not asserted here.
`proof_checks.py` uses uncapped integer path counts and a separately
constructed poset representation, imports no pilot code, and checks
every source, every target, every decoded inverse and the recurrent
census in the original $n=0,\ldots,6$ boxes. This is author checking,
not process-separated review.

## 2. TDP: proven erosion, no sharp grid theorem

Fix a nonempty finite ambient set $X\subset\mathbb R^2$. For $S\subseteq X$,
let $d_S(q)$ be the minimum of $|S\cap H|$ over all closed halfplanes
$H$ containing $q$. Let $F(S)$ be all $q\in X$ attaining the maximum.
For $S=\varnothing$, the stated rule gives $F(S)=X$.

For every integer $k$, the region $R_k=\{q:d_S(q)\geq k\}$ is convex:
it is the intersection of the complements of all closed halfplanes
containing fewer than $k$ points of $S$. Each complement is an open
halfplane and is convex. This argument uses convexity only, not a
claim that arbitrary intersections of open sets are open.
For nonempty $S$, any occupied point has depth at least one, while a
point outside $\operatorname{conv}S$ has depth zero by strict separation.
Therefore

$$\varnothing\ne F(S)\subseteq X\cap\operatorname{conv}S.$$

At the attained integer maximum $k$, $F(S)=X\cap R_k$. Convexity gives
$X\cap\operatorname{conv}F(S)=F(S)$. Thus after the first update,

$$\varnothing\ne S_{t+1}\subseteq S_t\quad(t\geq1).$$

Every strict update removes a point, giving eventual fixed points and
the generic bound of $|X|$ on the tail. This is the entire proved time
line. The height two seen in all ten rectangular boxes is not proved
for all rectangular grids. No all-grid inverse decoder or independent
extremal theorem has been obtained. Convex depth-region erosion is
explicitly deducted; TDP cannot fill a seat.

The integer pilot is not a floating-angle sample. For a query $q$,
directions where another ambient point lies on the boundary form
antipodal integer rays. The code takes one integer normal in every
open chamber between consecutive rays. The sign pattern is constant
in that chamber. A boundary direction includes its collinear points
and cannot lower the minimum below both adjacent perturbations.
The antipodal two-ray case is covered by a counterclockwise quarter
turn, and the one-point ambient set by an explicit normal. Hence all
possible minimum-depth values are represented exactly.

## 3. MHT: rank descent and the empty-edge extremum

Let $F(H)$ be all hitting sets of $H$ having the smallest cardinality,
with the conventions in `INTAKE.md`. The empty family and the family
$\{\varnothing\}$ form a two-cycle. Every other family containing the
empty edge reaches that cycle in one step. A nonempty family without
an empty edge has a nonempty family of nonempty minimum hitting sets,
so this nondegenerate region is forward invariant.

Write $H_t=F^t(H_0)$. For $t\geq1$ in that region every member of $H_t$
has one common size $r_t\in\{1,\ldots,n\}$. Since intersection is
symmetric, every member of $H_t$ hits every member of $H_{t+1}$.
Consequently $r_{t+2}\leq r_t$. Both parity subsequences of ranks
eventually stabilize. After stabilization, the members of $H_t$ have
the optimum size for hitting $H_{t+1}$, giving $H_t\subseteq H_{t+2}$.
Both parity subsequences of finite families then stabilize under
inclusion, so the eventual period is at most two. This is a generic
minimum-rank symmetric-incidence argument, not a sharp clock theorem.

The zero output has exactly $2^{2^n-1}$ sources: all families containing
the empty edge. Every other source lies in the other half of the full
carrier. For $n\geq1$ that other half has at least two distinct outputs:
the empty source outputs $\{\varnothing\}$, while the source consisting
only of $[n]$ outputs all singletons. Hence every nonzero target has
strictly smaller fibre, and zero is the unique maximum. At $n=0$ both
targets have fibre one. This extremum is only the unsatisfiable
boundary, not an independent inverse mechanism. Full nonzero-target
fibres and a sharp all-size time law are not supplied.

## 4. Exact open boundaries for the other literals

SHD uses two classical downset statistics, shattered and strongly
shattered coordinate sets. Their difference need not itself be a
downset. Strong/shattered duality, translation invariance and the
Sandwich theorem do not by themselves characterize all recurrent
families or invert this difference. The finite maximum height four
and periods at most two for $n\leq4$ remain bounded observations only.

UZ is exactly RX09/UCH in the old replacement ledger. UD is
$C\circ\mathrm{UZ}$, where $C$ complements each output subset in
$[n]$. Thus $\mathrm{UD}^{-1}(T)=\mathrm{UZ}^{-1}(C(T))$ and its entire
inverse problem has already been inherited. Postcomposition is not
conjugacy: UD already has a three-cycle at $n=1$, unlike UZ. No
all-parameter UD temporal classification is claimed; height thirteen
and periods through eight at $n=4$ do not close that gap.

AKC restricts to the classical Kreweras action on noncrossing
partitions. At $n=6$ its first image has 136 members, exceeding the
132 noncrossing partitions, so even one-step projection to that
stratum is false. The whole-partition recurrent census agrees with
the noncrossing census through $n=8$, but attraction for every $n$
and a sharp clock have not been proved. An inverse restatement as
cycle factorizations is not an enumerative decoder. No all-size
claim is inferred from genus intuition or the measured heights.

## Corrections, limitations and open risks

The late UZ collision is preserved in the intake and baseline output.
The extra MHT literal changes no original cutoff and is explicitly
a rank-filtered blocker control, not another certified independent
family. No candidate is admitted, placed in reserve, numbered or
externally released. The open questions above are reasons for
rejection at this gate, not promises that a larger pilot will resolve them.
