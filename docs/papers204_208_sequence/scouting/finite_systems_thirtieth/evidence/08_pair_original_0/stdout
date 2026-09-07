# Algebraic Phase 2b breadth scout

Status: **EXTERNAL HOLD**. This is a scouting and falsification record, not a
novelty or priority claim. No paper number is assigned.

## Scope and firewall

This lane asks for literal nonlinear finite algebraic self-maps after the
ordered-DAG, Boolean-zeta, Young-up-down, and shifted-Cartier leads failed their
owner gates. I screened the titles, README files, and collision/owner material
through P116. In particular, the following mechanisms receive no new credit
here:

- power maps and scalar-polynomial wrappers;
- closure, annihilator, valuation, and ideal-power engines, including the P107
  annihilator-power system;
- image/adjugate/Jordan mechanisms, including P103 and P109;
- Cartier and generic finite-linear or semilinear dynamics;
- sumset squaring and the P97 support engine;
- generic class-two word-area dynamics already represented by P111; and
- a group-algebra norm followed by scalar squaring, as in P102.

The twelve entries below are exactly the twelve systems opened in this breadth
lane. “Kill” means that the early signal is already explained by a forbidden
wrapper or a direct owner. “Conditional promote” means only that a theorem
contract survived this bounded screen.

## Exactly twelve literal systems

| ID | Literal phase space and self-map | Early exact signal | Gate |
|---|---|---|---|
| B2B-01 | For $R=\mathbb F_q\oplus V$ with $V^2=0$, on $\operatorname{Id}(R)^2$, $F(I,J)=(IJ,(I:J))$ | Complete graph, basin, layer, zeta, and indegree formulas from one Gaussian noncontainment statistic | **CONDITIONAL PROMOTE** |
| B2B-02 | On $V^2$, $V=\mathbb F_2^d$, $Q(x,y)=(y,x+\ell(y)y)$ for $0\ne\ell\in V^*$ | Only periods $1,2,3,6$ with closed counts | **KILL: explicit linear conjugate** |
| B2B-03 | On subsets $S\subseteq\mathbb Z/m\mathbb Z$, send $S$ to the odd-multiplicity support of $\Lambda^2(\bigoplus_{a\in S}\chi_a)$ | Translation-doubling cocycle and an exact three-support reflection law; full graphs also have periods $18,30$ | **RESERVE, high owner risk** |
| B2B-04 | On $U_n(\mathbb F_q)$, for the fixed regular shift $J$, $E(X)=[X,J]$ | Every lower-central layer maps onto the next with a uniform fibre; one exact stratified rooted component | **CONDITIONAL PROMOTE** |
| B2B-05 | On $G^2$ for a class-two group, $T(x,y)=(x[x,y],y[x,y])$ | The commutator is invariant and $T^t(x,y)=(x c^t,y c^t)$ | **KILL: central translation** |
| B2B-06 | On pairs of involutions, $S(a,b)=(aba,bab)$ | For $r=ab$, the update is $r\mapsto r^3$ | **KILL: power wrapper** |
| B2B-07 | On a symplectic space, $C(x,y)=(y,-x+\omega(x,y)y)$ | $\omega(x,y)$ is invariant and each level is a fixed companion matrix | **KILL: fibrewise linear** |
| B2B-08 | On $M_d(\mathbb F_q)$, $K(A)=AA^{\mathsf T}-A^{\mathsf T}A$ | $K(A)$ is symmetric, hence $K^2=0$ | **KILL: theorem-thin** |
| B2B-09 | On block matrices with a fixed invertible leading block, apply the principal pivot transform | The transform is an involution | **KILL: direct owner** |
| B2B-10 | On $G^2$, $H(x,y)=(y,y^{-1}xy)$ | $xy$ is invariant; this is a Hurwitz move | **KILL: direct owner** |
| B2B-11 | On subgroup pairs in a class-two group, $D(H,K)=([H,K],C_K(H))$ | The first coordinate becomes central and the orbit is fixed after at most two further updates | **KILL: closure/height wrapper** |
| B2B-12 | For an involutory automorphism $\theta$ of $G$, $L_\theta(x)=x\theta(x)^{-1}$ | The first image is anti-fixed and subsequent motion there is squaring | **KILL: Lang then power** |

## B2B-01: square-zero product--residual ideals

**System.** Let $V$ have dimension $d$ over $\mathbb F_q$ and let
$R=\mathbb F_q\oplus V$ with
$(a,u)(b,v)=(ab,av+bu)$. The phase space is the ordered pairs of ideals of
$R$, and
\[
        F(I,J)=(IJ,(I:J)),\qquad
        (I:J)=\{r\in R:rJ\subseteq I\}.
\]
Besides $R$, every ideal is a subspace $U\leq V$. Put
\[
 L_e=\sum_{i=0}^{e}{e\brack i}_q,\qquad L=L_d,
 \qquad
 A=\sum_{r=1}^{d}{d\brack r}_q\bigl(L-L_{d-r}\bigr).
\]
Here $A$ counts ordered subspaces $(U,W)$ with $W\ne0$ and
$W\nsubseteq U$; the displayed form indexes $U$ by codimension.

**Exact anomaly and strengthened contract.** The recurrent set consists of
the fixed points $(R,R)$ and $(0,V)$ and the two-cycle
$(0,0)\leftrightarrow(0,R)$. Thus
\[
 \zeta_F(z)=(1-z)^{-2}(1-z^2)^{-1}.
\]
The basin of $(0,V)$ has size $A$, split as depth zero $1$ and depth one
$A-1$. The two-cycle basin has size
$(L+1)^2-1-A$, split by depths zero through three as
\[
        2,\quad L^2-A,\quad L-1,\quad L-1.
\]
The basin of $(R,R)$ is the singleton itself. Globally the depth census is
$4,L^2-1,L-1,L-1$ at depths $0,1,2,3$.

The complete positive indegree list is
\[
\begin{aligned}
 \deg^-(0,V)&=A,&
 \deg^-(0,R)&=L^2-A+1,\\
 \deg^-(0,0)&=1,&
 \deg^-(R,R)&=1,\\
 \deg^-(U,R)&=1,&
 \deg^-(U,U)&=1
\end{aligned}
\]
for every **nonzero** proper ideal $U\leq V$ in the last line; every other
state has indegree zero. The exclusion of $U=0$ is essential because both
states in that nominal last-line pattern are already exceptional.

**Proof route A: multiplication table and case tree.** For proper ideals
$U,W\leq V$, $UW=0$. Moreover $(U:0)=R$, while for $W\ne0$,
$(U:W)=R$ if $W\leq U$ and $(U:W)=V$ otherwise. Together with
$F(R,J)=(J,R)$ and $F(U,R)=(U,U)$, this gives every arrow in at most four
cases. Reading the resulting case tree proves the recurrent cores, all
layers, and the indegree list.

**Proof route B: rank stratification and Gaussian incidence.** Stratify the
subspace lattice by codimension $r$. A fixed codimension-$r$ subspace
contains $L_{d-r}$ subspaces, so summing its noncontained targets gives
$A$. Partition all $(L+1)^2$ states by containment, zero/right-unit
exceptions, and then pull the partition through successive fibres. This
derives the basin and depth formulas without enumerating the arrow cases
state by state.

**Owner subtraction.** Ideal multiplication and quotient as the monoidal
product and residual of the ideal lattice are background and receive zero
credit. The closest located primary neighbor is Flaut--Piciu,
[Commutative Rings Behind Divisible Residuated Lattices
(2024)](https://doi.org/10.3390/math12233867), also
[available on arXiv](https://arxiv.org/abs/2411.03860). It develops precisely
that residuated ideal-lattice structure and finite examples, but the bounded
search found no iteration of the ordered map above. Square-zero/trivial
extension ideal classification is also background. The residual is only the
conjunction of the exact two-basin split, four layers, complete indegrees,
and Gaussian statistic.

**Hostile decision.** The new basin and indegree split materially clears the
earlier “one short depth census” objection: this is now a complete
parameterized functional graph rather than one total. It remains mechanical
once the square-zero multiplication table is written down. Promote only if a
primary-source audit confirms that this exact ordered iteration is not
already present and a paper can explain why the Gaussian incidence statistic
is structurally useful beyond this one ring.

**Decisive kill condition.** Kill on any direct owner of
$(I,J)\mapsto(IJ,(I:J))$ on ideal quantales/residuated lattices, or if the
final theorem package cannot extend beyond restating the four-case table.

## B2B-02: functional-controlled quadratic Fibonacci

**System.** For a nonzero functional $\ell:V\to\mathbb F_2$,
\[
        Q(x,y)=(y,x+\ell(y)y),\qquad (x,y)\in V^2.
\]
Writing $h=2^{d-1}$, the exact point counts are
\[
 P_1=h,\quad P_2=h(h-1),\quad P_3=3h,\quad P_6=3h(h-1),
\]
and no other period occurs.

**Two proof routes that were tested.** First, split
$V=\ker\ell\oplus\langle e\rangle$ and follow the four scalar states
$(\ell(x),\ell(y))$; direct multiplication gives $Q^6=1$ and the census.
Second, use a fibre gauge over those four scalar states. The gauge matrices
are respectively the identity,
$\left(\begin{smallmatrix}1&0\\1&1\end{smallmatrix}\right)$,
$\left(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right)$, and the identity.
They conjugate $Q$ to the direct product of coordinate swap on
$(\ker\ell)^2$ and $(a,b)\mapsto(b,a+b)$ on $\mathbb F_2^2$.

**Owner and internal subtraction.** A current broad neighbor for genuinely
quadratic permutations is Chen,
[A general approach to permutation polynomials from quadratic forms
(2025)](https://arxiv.org/abs/2506.24012), but an owner decision is moot:
the displayed conjugacy makes this a generic finite-linear system in
disguise.

**False conjecture and kill.** The literal update is nonadditive for
$d\ge2$, but “nonadditive implies genuinely nonlinear dynamics” is false.
The explicit conjugacy is the decisive kill.

## B2B-03: parity support of exterior squares

**System.** Let $\chi_a$ be the characters of a cyclic group indexed by
$a\in\mathbb Z/m\mathbb Z$. For $S\subseteq\mathbb Z/m\mathbb Z$, define
\[
 {\cal E}(S)=
 \left\{g:\#\{\{a,b\}\subset S:a\ne b,\ a+b=g\}\equiv1\pmod2\right\}.
\]
This is the odd-multiplicity support of
$\Lambda^2(\bigoplus_{a\in S}\chi_a)$ and is a literal self-map of the
Boolean phase space.

**Exact anomaly.** For translation by $c$,
\[
        {\cal E}(S+c)={\cal E}(S)+2c.
\]
If $|S|=3$ and $\sigma=\sum_{a\in S}a$, then
\[
        {\cal E}(S)=\sigma-S,\qquad
        {\cal E}^2(S)=S+\sigma.
\]
When $3$ is invertible modulo $m$, centering at the centroid separates this
into center doubling and shape reversal. Yet the full graphs already contain
period $18$ for $m=9$ and period $30$ for $m=11$, so the three-support
formula does not control the global dynamics.

**Proof route A: character pairs.** Expand the exterior square as the sum
over unordered pairs of distinct characters, reduce multiplicities modulo
two, and pair the three edges of a triple with the reflected vertices.

**Proof route B: group algebra over $\mathbb F_2$.** Encode $S$ by
$f_S(X)$ in $\mathbb F_2[X]/(X^m-1)$. Separate the diagonal from the
quadratic convolution before passing to parity; translation becomes
multiplication by $X^c$ and the output acquires $X^{2c}$. This route is
algebraic rather than a pair-by-pair Ferrers-style enumeration.

**Owner subtraction.** Lambda-ring and representation-ring identities are
background. The closest direct thematic primary neighbor is Connes,
[Iteration of the exterior power on representation rings
(2019)](https://doi.org/10.1016/j.geomphys.2019.02.013), which explicitly
iterates an exterior-power-derived operation on representation rings. Its
operator is different from odd-multiplicity support, but the title-level and
mechanism-level proximity creates substantial owner risk. No exact owner of
the parity-support self-map was located in the bounded search.

**False conjecture and gate.** “All cycles come from translation doubling”
is false, as the periods $18$ and $30$ show. Reserve only. Promote would
require a global theorem explaining the rich periods and a stronger
subtraction against exterior-power iteration. Kill if the only provable
result remains the size-three stratum.

## B2B-04: fixed regular-unipotent Engel iteration

**System.** Let $U_n(\mathbb F_q)$ be upper unitriangular, let
$J=I+N$ with ones on the first superdiagonal, and set
\[
        E(X)=[X,J]=X^{-1}J^{-1}XJ.
\]
Write $\gamma_k$ for matrices whose first $k-1$ superdiagonals vanish.

**Exact anomaly and proposed contract.** For $1\le k<n$,
\[
 E:\gamma_k\twoheadrightarrow\gamma_{k+1},
 \qquad |E^{-1}(Y)\cap\gamma_k|=q^{\,n-k}.
\]
Consequently the restriction to $\gamma_k$ is one rooted functional
component of height $n-k$, with depth-zero layer $1$ and, for
$1\le t\le n-k$,
\[
 L_{k,t}=
 \left(q^{\,n-k-t+1}-1\right)
 q^{\sum_{j=k}^{k+t-2}(n-j)}.
\]
In particular the full $U_n$ system has height $n-1$.

**Proof route A: superdiagonal recursion.** Write $X=I+(x_{ij})$, expand the
commutator against the fixed shift, and order equations by superdiagonal.
The first new superdiagonal is a discrete difference with one free boundary
coordinate. Inductively solve the higher equations after the lower ones are
fixed. This proves both surjectivity and the $q^{n-k}$ free-coordinate
count.

**Proof route B: centralizer cosets plus filtration induction.** Fibres of
the fixed-$J$ commutator equation, when nonempty, are cosets controlled by
the regular-unipotent centralizer. Compute its intersection with
$\gamma_k$, then prove image equality rather than mere inclusion by
induction on the central series. The layer formula follows independently by
subtracting successive cumulative fibres.

**Owner subtraction and strongest objection.** Fixed-second-variable Engel
chains and the centralizer-coset principle receive zero credit. A primary
computational neighbor explicitly using fixed-$y$ Engel chains is
[A Computational Approach to Verbal Width for Engel Words in Alternating
Groups (2019)](https://www.mdpi.com/2073-8994/11/7/877). A current primary
neighbor defining and studying the same repeated-commutator object through
Engel sinks is Khukhro--Shumyatsky,
[On finite groups containing an element whose Engel sink is small
(2026)](https://arxiv.org/abs/2605.08607). The bounded searches found no
exact fixed-regular-unipotent functional graph.

The strongest hostile objection is that, after the one image-surjectivity
lemma and the classical regular-centralizer count, every fibre and every
layer is a mechanical quotient/product. Lower-central structure and regular
centralizers therefore carry zero credit; the residual must be the complete
two-parameter stratified tree, not the ingredients.

**Decisive kill condition.** Kill if a source states the exact map on
$U_n(\mathbb F_q)$ with the same surjectivity/fibre theorem, or if
surjectivity reduces verbatim to a standard named lemma with no independent
structural corollary. Subject to that gate, this is the strongest lead.

## The eight fast kills

### B2B-05: class-two commutator co-translation

For a finite group of nilpotency class at most two, set $c=[x,y]$ and
$T(x,y)=(xc,yc)$. Centrality gives $[xc,yc]=c$ and hence
$T^t(x,y)=(xc^t,yc^t)$. Route A is direct commutator calculus; route B
passes to the central extension $G/Z(G)$ and reads each fibre as a central
translation. The anomaly is the exact period $\operatorname{ord}(c)$ and
the fixed set is the commuting-pair locus. This is killed both by its
central-translation normal form and by proximity to P111. Any claim beyond
the distribution of commutator orders would need a separate group-family
theorem, not dynamics.

### B2B-06: mutual involution sandwich

On pairs $a^2=b^2=1$, put $S(a,b)=(aba,bab)$. With $r=ab$, one computes
$r\mapsto r^3$ and
\[
 S^t(a,r)=
 \left(a r^{-(3^t-1)/2},r^{3^t}\right).
\]
Route A uses the presentation of the dihedral subgroup generated by two
involutions; route B uses the semidirect coordinates
$\langle r\rangle\rtimes\langle a\rangle$. The exact anomaly is real, but
all temporal structure is exponentiation by three. The decisive kill is the
forbidden power-map wrapper.

### B2B-07: alternating-form trace companion

For a symplectic vector space, set
$C(x,y)=(y,-x+\omega(x,y)y)$. The scalar
$c=\omega(x,y)$ is invariant. Route A computes the invariant and iterates
the two-vector recurrence; route B identifies each $c$-level with the
companion action
$\left(\begin{smallmatrix}0&-1\\1&c\end{smallmatrix}\right)$ on every
generated plane. Thus the apparent nonlinear coupling is only a disjoint
union of classical linear systems indexed by $c$. Kill at once under the
generic-linear firewall.

### B2B-08: transpose-commutator collapse

On $M_d(\mathbb F_q)$ let
$K(A)=AA^{\mathsf T}-A^{\mathsf T}A$. The image is symmetric in every
characteristic, and $K(B)=0$ for symmetric $B$, so $K^2=0$. Route A is the
transpose identity; route B decomposes the matrix algebra into the fixed
locus of transpose and observes that the image lands there. The early
anomaly is a uniform depth bound two. Kill: there is no nontrivial temporal
stratification, and the mechanism is too close to one-line matrix-image
collapses already firewalled by P103/P109.

### B2B-09: principal pivot transform

For
$M=\left(\begin{smallmatrix}P&Q\\R&S\end{smallmatrix}\right)$ with $P$
invertible, use
\[
 \operatorname{ppt}(M)=
 \begin{pmatrix}
 P^{-1}&-P^{-1}Q\\
 RP^{-1}&S-RP^{-1}Q
 \end{pmatrix}.
\]
The anomaly is involutivity. Route A multiplies the four block identities;
route B characterizes the transform by exchanging selected input/output
coordinates. This is directly owned background; see Tsatsomeros,
[Principal pivot transforms: properties and applications
(1998)](https://arxiv.org/abs/math/9807132). Kill without a spike.

### B2B-10: Hurwitz self-map

On $G^2$, put $H(x,y)=(y,y^{-1}xy)$. The product $xy$ is invariant.
Route A is direct word calculus; route B recognizes the braid-group
generator acting on factorizations. This is the classical Hurwitz action,
not a new system. A representative primary source using the standard
Hurwitz action is
[Dual Euclidean Artin groups and failure of the lattice
property](https://doi.org/10.1016/j.jalgebra.2015.04.021).
Direct ownership is the decisive kill.

### B2B-11: commutator--centralizer subgroup update

For subgroup pairs in a class-two finite group, set
$D(H,K)=([H,K],C_K(H))$. The first output is central; one more update has
trivial first coordinate, after which the state is fixed. Route A uses
three subgroup commutator/centralizer cases; route B passes to the
alternating commutator pairing on $G/Z(G)$ and reads the centralizer as an
orthogonal complement. The depth-at-most-two signal is only closure plus
height, so this is killed under the closure firewall.

### B2B-12: involutory Lang difference

For a finite group with $\theta^2=1$, let
$L_\theta(x)=x\theta(x)^{-1}$. If $y=L_\theta(x)$, then
$\theta(y)=y^{-1}$, and therefore $L_\theta(y)=y^2$. Route A proves this by
word manipulation; route B factors through the anti-fixed locus of the
involutory action. The first step is a Lang-type difference and every later
step is a square map. Thus its exact anomaly is precisely a forbidden
power-map wrapper, which is the decisive kill.

## Deterministic theorem pilots and falsification log

Only the three pre-gate leaders received new scripts in this lane.

| Script | Bounded coverage | Exact assertions | Result |
|---|---|---:|---|
| [alg_phase2b_squarezero_residual.py](../proof_spikes/alg_phase2b_squarezero_residual.py) | $(q,d)=(2,1\ldots4),(3,1\ldots3),(5,1\ldots2)$; literal ring products, colons, every state, basin, depth, and indegree | 35,772 | All strengthened formulas pass |
| [alg_phase2b_quadratic_fibonacci.py](../proof_spikes/alg_phase2b_quadratic_fibonacci.py) | Every state for $1\le d\le10$, inverse, sixth iterate, period census, and explicit conjugacy | 6,990,559 | Exact conjugacy found; candidate killed |
| [alg_phase2b_exterior_parity.py](../proof_spikes/alg_phase2b_exterior_parity.py) | Full graphs $1\le m\le12$, all translations through $m=9$, and supports of size at most three through $m=15$ | 30,516 | Local formulas pass; global periods refute simple model |

The three new scripts make **7,056,847** exact assertions. Their canonical
outputs were each rerun and byte-compared. The root-owned read-only
[alg_regular_engel.py](../proof_spikes/alg_regular_engel.py) adds 103,599
passing assertions for $q=2,3,5$ in its stated bounded ranges; including
that independent lane gives 7,160,446 assertions of bounded evidence. It
was not edited here.

False or overbroad conjectures caught:

1. B2B-02 is literally nonlinear but not dynamically new: the verified
   fibre gauge conjugates it to a linear direct product.
2. B2B-03 is not globally a centroid-doubling system: periods $18$ and $30$
   occur outside the size-three explanation.
3. In B2B-01 the tempting rule
   $\deg^-(U,R)=\deg^-(U,U)=1$ for every proper $U$ is false at $U=0$.
   The complete table above correctly restricts it to nonzero proper $U$.

These computations are bounded falsification evidence, not proofs or owner
evidence.

## Bounded current owner-search record

Searches were deliberately stopped once the promote/kill decision was
stable. Representative formulations included:

- B2B-01: “ideal quotient dynamics IJ I:J ideals,” “product residuation
  iteration ideals commutative ring,” “residuated lattice dynamical system
  multiplication residual,” and a 2025--2026 date-bounded variant.
- B2B-02: “quadratic permutation F2 vector space linear functional,”
  “piecewise-linear Fibonacci finite vector space,” and a 2025--2026
  quadratic-permutation query.
- B2B-03: “exterior square cyclic group representation ring parity
  multiplicities,” “lambda operation representation ring modulo two,” and
  “exterior power support dynamics cyclic group,” including 2025--2026.
- B2B-04: “Engel map unitriangular group fixed element functional graph,”
  “iterated commutator x to [x,g] regular unipotent,” and “fixed regular
  Jordan unipotent Engel fibres,” including 2025--2026 Engel-sink work.

“Engel graph” often denotes a different undirected graph and was not treated
as an exact hit. Absence above means only bounded no-hit. The exact closest
owners and residual subtraction are recorded in the individual entries; no
search absence is promoted into novelty language.

## Ranked gate

| Rank | ID | Score / 10 | Decision | Residual after owner subtraction |
|---:|---|---:|---|---|
| 1 | B2B-04 | 7.0 | **CONDITIONAL PROMOTE** | Fixed-regular-unipotent surjectivity plus the full $(q,n,k,t)$ stratified component; regular centralizers and Engel chains are zero credit |
| 2 | B2B-01 | 6.8 | **CONDITIONAL PROMOTE** | Exact Gaussian two-basin split, four depth layers, complete indegrees, and zeta for one ordered product--residual map |
| 3 | B2B-03 | 5.2 | **RESERVE, high risk** | Odd-support exterior-square dynamics beyond the exact size-three stratum; direct thematic owner remains close |
| 4 | B2B-08 | 2.8 | KILL | Only $K^2=0$ |
| 5 | B2B-11 | 2.5 | KILL | Only a closure/height collapse |
| 6 | B2B-05 | 2.3 | KILL | Central translation indexed by a commutator |
| 7 | B2B-12 | 2.1 | KILL | Lang first step followed by squaring |
| 8 | B2B-06 | 2.0 | KILL | Cubing in dihedral coordinates |
| 9 | B2B-07 | 1.9 | KILL | Linear companion maps on invariant fibres |
| 10 | B2B-02 | 1.5 | KILL | Explicitly conjugate to a generic linear direct product |
| 11 | B2B-09 | 1.0 | KILL | Classical principal pivot involution |
| 12 | B2B-10 | 1.0 | KILL | Classical Hurwitz action |

Final gate: promote at most the two conditional leaders, reserve B2B-03 only
as a search-dependent fallback, and close the remaining nine. External
release, novelty, and priority claims remain **HOLD**.
