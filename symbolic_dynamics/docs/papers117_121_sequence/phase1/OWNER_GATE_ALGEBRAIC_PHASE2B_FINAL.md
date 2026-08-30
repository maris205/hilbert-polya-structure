# Final algebraic Phase-2b owner gate

> **POST-GATE OWNER CORRECTION.** This screening document missed Bier
> (Linear Algebra Appl. 438 (2013), 2320--2330), whose Lemma 1 and proof of
> Theorem 1 use the same fixed regular $J$ and own the restricted and
> iterated image equalities.  The P119 score below is historical.  The
> manuscript now counts only the finite-field fibre/coset multiplicities,
> layers, typed predecessor census, and narrow $U_4$ guard as residual;
> external status remains HOLD.

**Audit date:** 2026-08-30  
**Role:** independent hard gate; no paper directory opened  
**External status:** **HOLD**  
**Novelty/priority status:** no claim; every search absence below is only a
bounded no-hit

## Final decisions

| candidate | score | final gate | exact reason |
|---|---:|---|---|
| fixed regular-unipotent Engel map on $U_n(\mathbb F_q)$ | **6.4/10** | **PROMOTE_TO_PAPER** | after subtracting Engel sinks, Lang-map fibres, regular-unipotent centralizers, and lower-central descent, a complete four-parameter exact functional tree remains; the core one-step theorem has two genuinely independent proofs |
| square-zero product--residual map on ideal pairs | **4.1/10** | **KILL** | the full graph is correct, but it is a mechanical readout of one four-case ideal table; the Gaussian route only counts cases from the first proof and is not an independent proof of the dynamics; the phase/proof grammar also presses directly against P107 and P109 |

These are terminal Phase-2b decisions, not conditional recommendations.

## Audit protocol

I normalized each theorem from its literal definition, proved or corrected every
claim without treating the scouting report as evidence, attacked the most natural
generalization, reran the canonical verifier twice, and searched for the same
object, same update, same proof engine, and same temporal package. Searches used
primary papers, official publisher records, and arXiv records; generic web pages
were used only to discover primary records and are not owner evidence.

The novelty-check workflow asks for an independent reviewer-model call. No such
reviewer tool was available in this session, and all live collaboration slots were
occupied. I therefore do not represent this as cross-model confirmation. The
verdict is deliberately conservative and external release remains on hold.

## I. Fixed regular-unipotent Engel dynamics

### I.1 Normalized theorem

Let $n\ge2$, let $q$ be a prime power, let $U_n(q)$ be the group of upper
unitriangular $n$ by $n$ matrices, and let
\[
 N=\sum_{i=1}^{n-1}E_{i,i+1},\qquad J=I+N.
\]
With commutator convention $[X,J]=X^{-1}J^{-1}XJ$, define
\[
 E(X)=[X,J].
\]
For $1\le k\le n$, let $\gamma_k$ consist of matrices whose first
$k-1$ superdiagonals vanish. Thus $\gamma_1=U_n(q)$ and
$\gamma_n=\{I\}$.

The following theorem is **PROVABLE AS STATED**.

1. For every $1\le k<n$,
   \[
      E(\gamma_k)=\gamma_{k+1}.
   \]
2. Every $Y\in\gamma_{k+1}$ has exactly $q^{n-k}$ predecessors in
   $\gamma_k$; a target outside $\gamma_{k+1}$ has none.
3. For $0\le t\le n-k$, every target in $\gamma_{k+t}$ has
   \[
      q^{S_{k,t}},\qquad
      S_{k,t}=\sum_{j=k}^{k+t-1}(n-j),
   \]
   predecessors under $E^t$ in $\gamma_k$.
4. The number of elements of exact entry depth $t$ in $\gamma_k$ is
   \[
   L_{k,0}=1,\qquad
   L_{k,t}=
   \left(q^{n-k-t+1}-1\right)
   q^{\sum_{j=k}^{k+t-2}(n-j)}
   \quad(1\le t\le n-k).
   \]
5. The whole functional graph has one recurrent point, $I$, maximum
   depth $n-1$, deepest layer
   \[
       (q-1)q^{\binom n2-1},
   \]
   and Artin--Mazur zeta function $(1-z)^{-1}$.

The empty sum in items 3 and 4 is zero. For $n=2$, the formula gives one root
and $q-1$ depth-one states, so the boundary case is included.

### I.2 Reconstruction: Route A, Lang fibres and a regular centralizer

Put $\phi(X)=J^{-1}XJ$. Then $E(X)=X^{-1}\phi(X)$ is a Lang-type
twisted coboundary. Since
$[\gamma_k,\gamma_1]\subseteq\gamma_{k+1}$,
\[
 E(\gamma_k)\subseteq\gamma_{k+1}.
\]

For $X_1,X_2\in\gamma_k$, equality
$X_1^{-1}\phi(X_1)=X_2^{-1}\phi(X_2)$ holds if and only if
$X_2X_1^{-1}$ is fixed by $\phi$. Hence every nonempty fibre is one
left coset of $C_{\gamma_k}(J)$.

The centralizer of the regular nilpotent matrix $N$ in the full matrix
algebra is $\mathbb F_q[N]$. Intersecting its unipotent units with
$\gamma_k$ gives
\[
 C_{\gamma_k}(J)
 =\left\{
 I+a_kN^k+\cdots+a_{n-1}N^{n-1}:a_i\in\mathbb F_q
 \right\},
\]
of order $q^{n-k}$. Also
\[
 |\gamma_k|
 =q^{\sum_{r=k}^{n-1}(n-r)}.
\]
Therefore
\[
 |E(\gamma_k)|
 =\frac{|\gamma_k|}{q^{n-k}}
 =q^{\sum_{r=k+1}^{n-1}(n-r)}
 =|\gamma_{k+1}|.
\]
The earlier inclusion is equality, and the same coset argument gives the
uniform fibre size.

Composing the successive uniform surjections gives item 3. Taking the
difference between the $t$-step and $(t-1)$-step fibres of $I$ gives item
4. Since every update raises the filtration index, all states reach $I$ in
at most $n-1$ steps; the remaining conclusions follow.

### I.3 Reconstruction: Route B, triangular coordinate solving

This route does not use the centralizer theorem, orbit--stabilizer, or a
cardinality comparison. Fix $Y=I+B\in\gamma_{k+1}$ and write
$X=I+A\in\gamma_k$. The equation $E(X)=Y$ is equivalent to
\[
       XJ=JXY.
\]
After expansion and cancellation,
\[
 AN-NA=B+NB+AB+NAB. \tag{1}
\]

Order the entries by superdiagonal. On superdiagonal $r+1$, the left side
of (1) is the difference map
\[
 (a_1,\ldots,a_{n-r})
 \longmapsto
 (a_1-a_2,\ldots,a_{n-r-1}-a_{n-r}).
\]
It is onto and has a one-dimensional constant kernel. The terms on the
right other than the current superdiagonal of $B$ involve only source
superdiagonals already chosen: $B$ starts at level $k+1$, while every
product with $A$ or $N$ raises the level. Thus the equations can be solved
successively from source diagonal $k$ through source diagonal $n-1$.
Each of the $n-k$ stages contributes one free field coordinate. Hence every
$Y$ has exactly $q^{n-k}$ solutions.

The two routes are materially different at the nontrivial step:

- Route A is a group-action proof using a generic Lang-fibre lemma and the
  regular centralizer.
- Route B is an explicit triangular solution of a nonlinear matrix equation
  using discrete differences.

They share only the elementary filtration and the subsequent multiplication
of proved fibre sizes. This is sufficient two-route independence for a short
paper; it is not two independent proofs of every bookkeeping corollary.

### I.4 Strongest counterexample direction

Regularity cannot be weakened to an arbitrary noncentral unipotent element.
In $U_4(q)$ take
\[
       J'=I+E_{12}+E_{34},
\]
which misses only the middle simple-root entry. If
$A=\sum_{i<j}a_{ij}E_{ij}$, then $A$ commutes with
$E_{12}+E_{34}$ precisely when
\[
       a_{23}=0,\qquad a_{24}=a_{13}.
\]
Thus $C_{U_4(q)}(J')$ has order $q^4$, not $q^3$. The corresponding
Lang map has image size $q^{6-4}=q^2$, whereas
$|\gamma_2|=q^3$. Hence both surjectivity onto $\gamma_2$ and the claimed
$q^{n-1}$ fibre size fail. This is a near-regular counterexample, not the
vacuous choice $J=I$.

The claim ceiling must therefore keep the fixed regular shift and may not say
“unipotent $J$” or “Engel maps on unitriangular groups” in general.

### I.5 Direct-owner audit and subtraction

The following are direct ingredient owners and receive zero credit.

1. The map $x\mapsto x^{-1}\phi(x)$ is the classical Lang map/twisted
   coboundary, and its fibres as fixed-point cosets are standard. The
   foundational primary records are Lang,
   [Algebraic Groups over Finite Fields
   (1956)](https://doi.org/10.2307/2372673), and Steinberg,
   [Endomorphisms of Linear Algebraic Groups
   (1968)](https://doi.org/10.1090/memo/0080). Their global surjectivity
   hypotheses do not apply to this inner automorphism on the present finite
   filtration, so they do **not** own
   $E(\gamma_k)=\gamma_{k+1}$; they do own the terminology and fibre-coset
   mechanism.
2. Fixed-second-variable iterates
   $x\mapsto[x,g]\mapsto[[x,g],g]\mapsto\cdots$ are exactly the classical
   left Engel sequence. Acciarri--Shumyatsky,
   [On groups in which Engel sinks are cyclic
   (2019)](https://arxiv.org/abs/1905.07494), defines this same sequence and
   studies its eventual sink. Thus “all orbits eventually reach $I$ in a
   nilpotent group” earns zero credit.
3. The current scope is confirmed by Khukhro--Shumyatsky,
   [On finite groups containing an element whose Engel sink is small
   (2026)](https://arxiv.org/abs/2605.08607), which explicitly treats inner
   automorphisms and left Engel sinks. It does not give the regular
   unitriangular layer census.
4. The lower-central series of $U_n(q)$ and the centralizer of a regular
   unipotent/Jordan block are classical. Steinberg's monograph is sufficient
   owner evidence; neither fact may be advertised as new.

Representative direct-hit searches included:

- “Engel map unitriangular regular unipotent fixed element,”
  “iterated commutator $x\mapsto[x,g]$ regular unipotent,” and
  “2025 2026 fixed-element Engel map unitriangular”;
- “$x^{-1}g^{-1}xg$ unitriangular functional graph,”
  “commutator map regular unipotent centralizer fibres,” and
  “$[U_n(q),J]$ regular unipotent image”; and
- “Lang map $x^{-1}\phi(x)$ fixed-point fibres,” “regular unipotent
  conjugacy class in a maximal unipotent subgroup,” and
  “2025 2026 regular-unipotent centralizer unitriangular.”

The closest exact formulation is the conjunction of Lang fibres, regular
centralizers, and Engel sinks. No primary source was located that states the
restricted surjections for every $k$, their iterated fibre products, and the
exact $(q,n,k,t)$ functional tree. This is a bounded no-hit, not a novelty
certificate.

### I.6 P001--P116 firewall and claim ceiling

- **P111:** both use upper-unitriangular language, but P111 is a positive
  random product in the integer Heisenberg group and studies word area,
  limit laws, norm exponents, and pressure. The present phase is the full
  finite group $U_n(q)$ and the deterministic update is one fixed-element
  commutator. No update or observable is shared.
- **P109:** this is the closest proof-shape collision. P109 applies a
  regular nilpotent linear map to the full subspace lattice and uses
  Grassmannian fibres and Gaussian intersection counts. The present map is
  nonlinear on group elements; its fibres are centralizer cosets and its
  type is lower-central level. The generic slogans “nilpotent descent,”
  “unique absorber,” and “uniform fibres” receive zero credit. The residual
  is only the exact regular-Lang multitype tree.
- **P103/P115:** there is no adjugate action and no coefficient
  decimation/semilinearity. Mentioning $N$ as a regular shift does not turn
  the update into a matrix power, image, Jordan, or Cartier system.
- **P97/P102/P107:** there is no support squaring, norm map, ideal
  annihilator, or CRT exponent dynamics.

The paper may claim only:

1. the literal fixed-$J$ self-map on $U_n(q)$;
2. the restricted image and fibre theorem for $\gamma_k$;
3. all iterated fibres, depths, deepest layer, indegree-by-filtration, and
   zeta derived from that theorem;
4. the two proofs above; and
5. the explicit failure for a nearly regular $J'$.

It may not claim a new Lang map, a new Engel concept, a new regular
centralizer theorem, general Engel dynamics, general unipotent $J$, or
novelty/priority.

### I.7 Why the residual is still paper-scale

After owner subtraction the result is elementary, but it is not a one-line
height observation. It gives one closed functional component at every
$(q,n)$, all filtration-restricted predecessor counts, every $t$-step fibre,
every transient layer, sharp depth, deepest-shell size, and the exact
regularity failure. The theorem is uniform in four indices $(q,n,k,t)$ and
the nonlinear update has both a conceptual group-action proof and a
coordinate proof. That is enough for a compact short note if the abstract
and introduction lead with the exact temporal census rather than with
Engel, Lang, or centralizer ingredients.

**Final verdict: PROMOTE_TO_PAPER, score 6.4/10, external HOLD.**

## II. Square-zero product--residual ideal dynamics

### II.1 Corrected normalized theorem

The nontrivial theorem requires $d\ge1$. Let $V$ be a $d$-dimensional
vector space over $\mathbb F_q$, let
\[
 R=\mathbb F_q\oplus V,\qquad
 (a,u)(b,v)=(ab,av+bu),
\]
and let
\[
 F(I,J)=(IJ,(I:J))
\]
on ordered pairs of ideals. Put
\[
 L_e=\sum_{i=0}^{e}{e\brack i}_q,\qquad L=L_d,
\]
and
\[
 A=\sum_{r=1}^{d}{d\brack r}_q(L-L_{d-r}).
\]

Every ideal is either $R$ or a subspace $U\le V$. The complete case table is
\[
\begin{array}{c|c}
\text{input}&F(\text{input})\\ \hline
(R,J)&(J,R)\\
(U,R)&(U,U)\\
(U,0)&(0,R)\\
(U,W),\ W\ne0,\ W\le U&(0,R)\\
(U,W),\ W\nleq U&(0,V).
\end{array}
\]
Here $U,W$ denote proper ideals contained in $V$.

It follows that $(R,R)$ and $(0,V)$ are fixed, while
$(0,0)\leftrightarrow(0,R)$ is the unique two-cycle. The exact global depth
counts are
\[
        4,\quad L^2-1,\quad L-1,\quad L-1
\]
at depths $0,1,2,3$, and
\[
        \zeta_F(z)=(1-z)^{-2}(1-z^2)^{-1}.
\]

The basin of $(0,V)$ has size $A$, split as $1,A-1$ at depths zero and
one. The two-cycle basin has size $(L+1)^2-1-A$, split as
\[
       2,\quad L^2-A,\quad L-1,\quad L-1.
\]
The basin of $(R,R)$ is a singleton.

The complete nonzero indegrees are
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
for every **nonzero** proper ideal $U$ in the last line. All other
indegrees vanish.

### II.2 Reconstruction and proof-route test

If an ideal contains an element $(a,u)$ with $a\ne0$, it contains a unit and
is $R$. Otherwise it is $0\oplus U$ for a unique subspace $U\le V$; every
such subspace is an ideal because $V^2=0$. This proves the ideal
classification and gives $L+1$ ideals.

For proper $U,W$, their product is zero. If $W\ne0$, an element $(a,v)$
lies in $(U:W)$ precisely when $aW\le U$. Radical elements always qualify;
a nonzero scalar qualifies precisely when $W\le U$. Hence the colon is
$R$ when $W\le U$ and $V$ otherwise. The cases with a zero or unit ideal
give the remaining rows of the table. Following the five rows proves the
cores, paths, and indegrees.

The statistic $A$ counts ordered pairs $(U,W)$ with $W\ne0$ and
$W\nleq U$: a codimension-$r$ subspace contains $L_{d-r}$ subspaces.
Gaussian summation therefore proves the basin cardinalities.

These are **not two materially independent proofs of the dynamics**.
The Gaussian route independently proves the incidence count $A$, but it
cannot identify a single arrow, recurrent core, depth, or indegree until the
same multiplication/colon table from the first route has already been used.
It is complementary enumeration, not an independent dynamical proof. This
fails the Phase-2b two-route demand.

### II.3 Strongest counterexample direction and omitted boundary

Square-zero is essential. For
$R_3=\mathbb F_q[\varepsilon]/(\varepsilon^3)$, write
$I_a=(\varepsilon^a)$ for $0\le a\le3$, with $I_0=R_3$ and $I_3=0$.
The same update becomes
\[
 (a,b)\longmapsto
 \bigl(\min(a+b,3),\max(a-b,0)\bigr).
\]
Besides the fixed state $(0,0)$ in exponent notation, it has the two cycles
\[
 (3,0)\leftrightarrow(3,3),\qquad
 (3,1)\leftrightarrow(3,2),
\]
and maximum preperiod five. An explicit length-five entry path is
\[
 (0,1)\to(1,0)\to(1,1)\to(2,0)\to(2,2)
 \to(3,0)\leftrightarrow(3,3).
\]
Thus even the next principal local algebra destroys the advertised fixed
radical, core count, and depth-three bound.

There is also a genuine boundary correction: when $d=0$, $V=0$, so
$(0,V)=(0,0)$ collides with the distinguished two-cycle and $A=0$. The
basin formula would contain $A-1=-1$. Any surviving statement must assume
$d\ge1$ explicitly.

### II.4 Direct-owner audit and subtraction

The following ingredients are directly owned.

1. $R=\mathbb F_q\oplus V$ is Nagata idealization/trivial extension.
   Anderson--Winders,
   [Idealization of a Module
   (2009)](https://doi.org/10.1216/JCA-2009-1-1-3), gives the same
   multiplication and explains submodules as square-zero ideals.
2. Ideal multiplication and colon are precisely multiplication and
   residuation on the ideal lattice. This starts with Ward--Dilworth,
   [The Lattice Theory of Ova
   (1939)](https://doi.org/10.2307/1968944), and is explicit in the current
   primary neighbor Flaut--Piciu,
   [Commutative Rings Behind Divisible Residuated Lattices
   (2024)](https://doi.org/10.3390/math12233867), also
   [on arXiv](https://arxiv.org/abs/2411.03860).
3. Flaut--Piciu explicitly defines the ideal product, quotient, and
   annihilator and computationally constructs small finite residuated
   lattices. Searches within its full text found no iteration, dynamics,
   square-zero specialization, or trivial extension; it therefore owns the
   algebra, not the exact functional graph.
4. Gaussian subspace counts are classical and receive zero credit.

Representative searches included:

- “$(I:J)$ $IJ$ iteration ideals,” “ideal quotient ideal product pair
  dynamics,” and “2025 2026 ideal multiplication functional graph”;
- “product--residuation iteration residuated lattice,”
  “$(x\cdot y,x\to y)$ dynamical system,” and “quantale multiplication
  residual dynamics”; and
- “square-zero local algebra ideal lattice subspaces,” “trivial extension
  colon ideal finite field,” and “2025 2026 idealization residuated lattice.”

No direct source for this exact ordered self-map was located. The absence
does not rescue the candidate: after the directly owned operations and
idealization are subtracted, the residual is only the five-row case-table
readout.

### II.5 P001--P116 firewall and fatal collision

- **P107 is the fatal internal pressure.** Both phases are finite ideal
  lattices; both use an ideal residual/annihilator operation; both conclude
  with exact basins, depths, periods, and zeta by reading a finite ideal
  operation table. The literal updates differ
  ($I\mapsto\operatorname{Ann}(I)^r$ versus
  $(I,J)\mapsto(IJ,(I:J))$), so this is not exact duplication, but the
  carrier and proof grammar are too close for another paper whose residual
  is mechanically thinner than P107's CRT/resonance package.
- **P109 supplies the second pressure.** The only parameter-dependent
  enumeration here is Gaussian subspace incidence. P109 already uses the
  full finite subspace lattice, Gaussian counts, exact absorption layers,
  local indegrees, and parameter recovery. Pairing that lattice with $R$
  does not create a new proof engine.
- **P103/P115/P111 are distinct** at the literal update level, but their
  separation cannot cure the P107/P109 collision.

The maximum honest claim ceiling, if retained as an internal lemma, is:
for $d\ge1$, the displayed five-row transition table and its exact
functional graph. It may not claim general square-zero extensions over
arbitrary base rings, radical-cube-zero rings, an independent second proof,
or a new theory of residuated-lattice dynamics.

Even as a compact note, the residual is not paper-scale under this
repository's firewall: one structural lemma, one Gaussian incidence sum, and
bookkeeping consequences do not survive subtraction strongly enough.

**Final verdict: KILL, score 4.1/10, external HOLD.**

## III. Fresh canonical verification

Both repository scripts were run twice from a clean process in this audit,
and their stdout streams were byte-compared.

| script | fresh result | assertions | stdout bytes | SHA-256 of each of two runs |
|---|---|---:|---:|---|
| [alg_regular_engel.py](../proof_spikes/alg_regular_engel.py) | PASS | 103,599 | 177 | adcd4bbb477a2683ab5503b67a41c9488b37982f9f3868b4beda5012334522f9 |
| [alg_phase2b_squarezero_residual.py](../proof_spikes/alg_phase2b_squarezero_residual.py) | PASS | 35,772 | 3,066 | 0497e6a9cd6ca47e60d080d45c26f120b97543dae575d3e01a660584c9dc5bf1 |

The Engel verifier exhausts its documented prime-field ranges
$q=2,n\le6$, $q=3,n\le4$, and $q=5,n\le4$, including every restricted
filtration image, fibre, depth histogram, and centralizer size. The
square-zero verifier exhausts every ideal pair for its documented nine
$(q,d)$ values and checks literal products, colons, cores, basin layers,
Gaussian $A$, and the complete indegree table.

The computations do not prove the all-prime-power theorems and do not
constitute owner evidence. They are deterministic falsification controls.

## Freeze instruction

Freeze only the fixed regular-unipotent Engel system for possible paper
assignment, under the claim ceiling in Section I.6. Permanently close the
square-zero product--residual system in the kill ledger. No external posting,
submission, specialist contact, novelty statement, priority statement, or
paper-number assignment is authorized by this gate.
