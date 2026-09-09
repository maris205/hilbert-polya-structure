# B1 — congruence separation for two-sided integral polynomial orbits

Date: 2026-09-09 UTC. Lane owner: B1. Status:
`FULL_QUESTION_UNCLOSED; AUXILIARY_PROVED_BY_AUTHOR; NOT_ADMITTED`.
No mathematical program was executed.

## Frozen original question and approach

For every $F\in\operatorname{Aut}_{\mathbb Z}(\mathbb A^2)$ (both $F$ and
$F^{-1}$ have integral polynomial coordinates) and every $P,Q\in\mathbb Z^2$,
does
$$
Q\in\{F^n(P):n\in\mathbb Z\}
\quad\Longleftrightarrow\quad
\forall m\ge2\;\exists n_m\in\mathbb Z:
F^{n_m}(P)\equiv Q\pmod m
$$
hold? The clock is one application of $F$; all integer times, all prime powers,
and all mixed moduli remain part of the question.

Success is a complete all-quantifier proof, or one explicit triple with a proof
of every modulus hit and every integer-time non-hit. A finite census, periodic
target theorem, or existence of a noninteger-looking local time is not success.

The B1 strategy is independent of B2's analytic/height route:

1. Test constructive collisions induced by polynomial centralizers or reversing
   symmetries; determine exactly which such constructions are ruled out.
2. Check primary-source global algebraic/group-action orbit-separation results
   for a theorem that genuinely extends past bounded-degree linearization.
3. Isolate intrinsic congruence invariants that a hypothetical collision must
   share, without mistaking necessary invariants for a separation theorem.

Decisive failure checks: a centralizer construction must survive torsion-free
profinite time; a reversing-symmetry construction must actually prove that the
reflected point lies on the same cycle for every mixed modulus. A global
separation theorem must cover wandering singleton targets and the exponential
degree-growth branch. Failure of one of these methods does not refute LG4.

## Source subtraction and inherited interface

Read in full the four frozen R4 arithmetic records:
[contract](../../../research_c424_c428/continuation_round4/arithmetic/FROZEN_CONTRACTS.md),
[proof](../../../research_c424_c428/continuation_round4/arithmetic/PROOF_PACKAGE.md),
[source audit](../../../research_c424_c428/continuation_round4/arithmetic/SOURCE_AUDIT.md),
and [disposition](../../../research_c424_c428/continuation_round4/arithmetic/DISPOSITION.md).
Their linear, triangular, bounded-degree and periodic-target cases, and their
full profinite-translation theorem, are imported and not claimed as new.

In particular, for nonperiodic $P$, the map
$$
\theta_P:\widehat{\mathbb Z}\longrightarrow
X_P=\overline{\{F^nP:n\in\mathbb Z\}}
$$
is a homeomorphism, with $F\theta_P(t)=\theta_P(t+1)$. It uses the actual
finite-orbit periods at every modulus and retains mixed-modulus compatibility.
The missing original claim remains
$$
\theta_P^{-1}(\mathbb Z^2)=\mathbb Z.
$$
Existence and uniqueness in $\widehat{\mathbb Z}$ do not establish membership
in its nonclosed diagonal copy of $\mathbb Z$.

## Working record

Initial local-first search found no relevant PDF by filename in the project
`papers/` or `literature/` directories; the frozen arithmetic source/proof
records supplied the relevant local library. No old program was run. All new
mathematical arguments below will be proof-only unless a separately prewritten,
bounded diagnostic receives coordinator allocation.

## Auxiliary theorem: the virtual-centralizer route cannot give a collision

**Claim (VC).** Under the full original assumptions, suppose additionally that
there is $G\in\operatorname{Aut}_{\mathbb Z}(\mathbb A^2)$ and an integer $k\ge1$
such that
$$
Q=G(P),\qquad GF^k=F^kG.
$$
Then the original all-modulus condition implies $Q\in\mathcal O_F(P)$.
This is a target-location hypothesis, not a solution for arbitrary $Q$.

**Status:** `PROVABLE AFTER EXTRA ASSUMPTION` relative to LG4;
the displayed auxiliary claim is proved below. It is a corollary of imported
profinite time and classical centralizer structure, not a new paper contract.

**Dependencies.** The proof uses R4 auxiliary theorem A, its bounded-degree
theorem B, and Lamy's centralizer theorem. The precise external input is:
for a complex plane polynomial automorphism of dynamical degree greater than
one, its polynomial centralizer is finite-by-infinite-cyclic. Lamy also records
the elementary/Hénon dichotomy, so a plane automorphism outside the uniformly
bounded-degree branch has dynamical degree greater than one. Here “degree” in
his Proposition 4.8 means dynamical degree, as defined on p. 414; it does not
mean merely ordinary polynomial degree greater than one.
[Lamy, original article, pp. 414–415 and Lemma 4.7/Proposition 4.8, pp. 429–430](https://www.math.univ-toulouse.fr/~slamy/stock/lamy_algebra.pdf).

### Step 1: a commuting map acts as a translation

Assume $P$ is nonperiodic, $GF=FG$, and $G(P)=\theta_P(t)$ for
$t\in\widehat{\mathbb Z}$. Polynomial maps with integral coefficients extend
continuously to $\widehat{\mathbb Z}^{\,2}$. For every ordinary integer $n$,
$$
G\theta_P(n)=GF^nP=F^nG(P)=\theta_P(n+t).
$$
The two sides are continuous as functions of the profinite variable $n$.
Density of $\mathbb Z$ therefore proves
$$
G\theta_P(s)=\theta_P(s+t)\quad
\text{for every }s\in\widehat{\mathbb Z}.                    \tag{1}
$$
In particular $G$ preserves $X_P$, and $G^a(P)=\theta_P(at)$ for every
positive integer $a$.

If $G^a=F^b$ for some integers $a\ge1$ and $b$, injectivity of $\theta_P$
gives $at=b$. Reduction modulo $a$ gives $a\mid b$ in $\mathbb Z$.
Writing $b=ac$, multiplication by $a$ is injective on every $\mathbb Z_p$,
hence on $\widehat{\mathbb Z}$; thus $t=c\in\mathbb Z$. This establishes
the conclusion whenever this power relation holds. In particular, a
finite-order commuting symmetry cannot move $P$ to a distinct point of $X_P$.

### Step 2: why the power relation holds in the Hénon branch

Let $C$ be the complex polynomial centralizer of $F$ and suppose its dynamical
degree is greater than one. The cited theorem gives a homomorphism
$\ell:C\to\mathbb Z$ with finite kernel and infinite cyclic image. Its
construction is the signed translation along the common tree axis. The
element $F$ has nonzero image: otherwise it would belong to the finite kernel
and have finite order. Also $F$ is central in $C$, so $\langle F\rangle$ is
normal. The kernel of
$$
C/\langle F\rangle\longrightarrow
\ell(C)/\langle\ell(F)\rangle
$$
is a quotient of the finite kernel of $\ell$, and the target is finite.
Therefore $C/\langle F\rangle$ is finite. The coset of any $G\in C$ has
finite order, giving $G^a=F^b$ as required in Step 1.

This argument only uses the finite-by-cyclic statement. It does not replace
the semidirect product in the primary source by a direct product; the latter
need not be the uniform statement. Nor is an arithmetic model for the
complex centralizer's generators required: $F$ and the given $G$ already
have integral models, and their power identity holds as a polynomial identity.

### Step 3: retain the complete native clock when only an iterate commutes

Now assume only $GF^k=F^kG$. The original all-modulus condition gives the
unique full native time $t\in\widehat{\mathbb Z}$ with $Q=\theta_P(t)$.
Choose the ordinary integer $j\in\{0,\ldots,k-1\}$ representing $t$ modulo
$k$, and write $t=j+ku$ for the unique $u\in\widehat{\mathbb Z}$.
Set
$$
A=F^k,\qquad H=F^{-j}G.
$$
Then $HA=AH$, and continuity from ordinary integer times gives
$$
H(P)=F^{-j}Q=\theta_P(ku)=\theta_{A,P}(u).       \tag{2}
$$
The point $P$ is nonperiodic for $A$. If $F$ has dynamical degree greater
than one, then so does $A$. Steps 1–2 applied to $(A,H,P)$ force $u=c$ for
an ordinary integer $c$. Equation (2) yields
$Q=F^{j+kc}(P)$ in the original clock.

For periodic $P$, and for uniformly bounded positive and negative iterate
degrees, the inherited R4 results already prove the conclusion for every
$Q$, without the hypothesis involving $G$. The elementary/Hénon dichotomy
therefore accounts for every $F$ in (VC). The reverse implication in (VC) is
the direct reduction of the actual integer-time identity. This finishes the
auxiliary proof.

**Exact remaining compatibility condition.** An arbitrary integral point
$Q\in X_P$ is not known to be $G(P)$ for a polynomial automorphism commuting
with an iterate. A translation sending $P$ to $Q$ is integral, but does not
usually commute with any $F^k$. Nothing above constructs the required $G$.

## Return ideals: a necessary invariant, with a complete failure example

For integer points $A,B\in\mathbb Z^d$, define the ideal
$$
I(A,B)=(A_1-B_1,\ldots,A_d-B_d)\subseteq\mathbb Z,
\qquad D_n(P)=I(F^nP,P),\quad n\in\mathbb Z.
$$
Every integral polynomial coordinate satisfies
$f(A)-f(B)\in I(A,B)$, by expanding monomial differences. Consequently
$I(FA,FB)\subseteq I(A,B)$; application of $F^{-1}$ proves equality.
Applying this identity to $F^j$ shows
$$
D_n(F^jP)=D_n(P)\qquad (j,n\in\mathbb Z).       \tag{3}
$$
If $P,Q$ lie on the same orbit modulo every modulus, then
$$
D_n(P)=D_n(Q)\qquad\text{for every }n\in\mathbb Z.           \tag{4}
$$
Indeed, at any modulus $m$, lying in the same finite cycle implies that
$F^nP=P$ modulo $m$ if and only if $F^nQ=Q$ modulo $m$. Thus each prime-power
divisibility condition on the two ideals is the same. Their nonnegative
generators are equal, including the zero ideal case. A mismatch in (4) is
therefore a valid finite congruence separator.

**The complete invariant (4) does not separate the remaining nonlinear
branch.** Take
$$
F(x,y)=(y,y^3-x),\quad F^{-1}(x,y)=(x^3-y,x),\quad
P=(1,2),\quad Q=(-1,-2).
$$
Both $F$ and $F^{-1}$ are odd, so $F^nQ=-F^nP$ for all integer $n$.
The vectors defining $D_n(Q)$ and $D_n(P)$ are negatives, proving (4) for
every integer $n$, not just finitely many tested times.

Nevertheless, direct substitution modulo $7$ gives the closed cycle
$$
(1,2)\mapsto(2,0)\mapsto(0,5)\mapsto(5,6)
\mapsto(6,1)\mapsto(1,2).
$$
The reduction $Q=(6,5)$ is absent. Thus $Q$ is not in the integral orbit and
is already separated modulo $7$. This is not an LG4 counterexample: it
refutes only the proposed sufficiency of all return ideals/period lengths.

The starting point is genuinely nonperiodic. If
$a_0=1,a_1=2,a_{r+2}=a_{r+1}^3-a_r$, then
$a_{r+1}>a_r\ge1$ inductively implies
$a_{r+2}>a_{r+1}^3-a_{r+1}>a_{r+1}$. Hence the positive orbit is unbounded.
This example is in the degree-growth Hénon branch, not a periodic or affine
degeneracy. The displayed finite cycle was derived by hand; no program or
unbounded enumeration was used.

## Reversing symmetries: why the constructive route is not closed

Suppose $R\in\operatorname{Aut}_{\mathbb Z}(\mathbb A^2)$ satisfies
$RF=F^{-1}R$, and suppose, as an additional condition still needing proof,
that $R(P)=\theta_P(t)$. The same continuity argument as in Step 1 gives
$$
R\theta_P(s)=\theta_P(t-s).                    \tag{5}
$$
Unlike (1), equation (5) is a reflection. Squaring it is the identity for
every profinite $t$, so an involution relation does not force $t$ to be an
ordinary integer. This prevents transferring the finite-order commuting
argument to a reversing symmetry.

Reversibility itself does not supply the assumed all-modulus hit. An exact
nonlinear falsifier is
$$
F(x,y)=(y,y^5-y-x),\qquad R(x,y)=(y,x),\qquad P=(1,2).
$$
Here $R^2=\mathrm{id}$ and $RFR=F^{-1}$ by substitution. Modulo $5$,
Fermat's identity reduces $F$ to $(y,-x)$. The full cycle of $P$ is
$$
(1,2)\mapsto(2,4)\mapsto(4,3)\mapsto(3,1)\mapsto(1,2),
$$
whereas $R(P)=(2,1)$ is absent. Consequently the claim that polynomial
reversibility forces reflected points into the same modular cycle is false.
This is again a method falsifier, not a negative answer to LG4.

## Source audit and subtraction

The new externally used algebraic input is the primary article by Stéphane
Lamy, *L'alternative de Tits pour Aut[$\mathbb C^2$]*, Journal of Algebra
239 (2001), 413–437, DOI `10.1006/jabr.2000.8701`. Actual reading covered its
introductory dichotomy/dynamical-degree definition and the full statements
and proofs of Lemma 4.7 and Proposition 4.8 with adjoining Corollary 4.6 and
Remark 4.9. The PDF's parsed semidirect-product symbol is degraded; its
introductory text explicitly says semidirect product and the displayed
generators/relations prove the finite-by-cyclic property used here. One
requested web screenshot failed; it is not counted as visual verification.
The Déserti survey was a locator only, not the theorem authority.

The author-hosted 19-page version of
[Amerik–Kurlberg–Nguyen–Towsley–Viray–Voloch, *Evidence for the dynamical Brauer–Manin criterion*](https://kurlberg.github.io/eprints/dbm.pdf)
was also inspected at §4.6, Proposition 4.9 and its proof, with the relevant
invariant-target theorem passage. Its numbering differs from R4's fixed
arXiv-v2 numbering. Its predecessor-point obstruction concerns forward
time; it cannot refute the two-sided question. The singleton positive
criterion based on nonperiodic reductions does not address our integral
automorphisms, for which every reduction is a finite permutation. No theorem
for general wandering singleton targets was obtained from this source.

The bounded new search used eighteen literal queries, in five groups:

1. `"Hénon" "Hasse principle"`; `"polynomial automorphism" "orbit" "local-global"`;
   `"étale" "wandering" "dynamical Hasse"`; `"orbit" "profinite" "Xie"`.
2. `"Hénon" "centralizer" polynomial automorphisms virtually cyclic`;
   `"polynomial automorphisms" "orbit separability"`;
   `"dynamical Brauer" "two-sided"`; `"Hénon" "orbit" "congruences"`.
3. `Lamy alternative Tits groupe automorphismes polynomiaux C2 Proposition 4.8 centralisateur pdf`;
   `"polynomial automorphism" "strong approximation" orbit`;
   `"Henon" "dynamical" "local-global principle"`.
4. `"dynamical Hasse principle" "points" automorphisms`;
   `"polynomial" "orbit" "closed" "profinite topology"`;
   `"orbit separability" "polynomial" automorphism`.
5. `"dynamical support problem" polynomial automorphism`;
   `"dynamical" "support problem" "orbits"`;
   `"Hénon" "orbit intersection" arithmetic`;
   `"polynomial automorphism" "congruence subgroup"`.

No recency or domain filters were used. Search snippets, unrelated results,
and inaccessible page portions were not promoted to theorem evidence.
No general applicable LG4 theorem or explicit counterexample was found in
this bounded search; that statement is not a claim of worldwide openness
or novelty. No Zotero/Obsidian tool was available. No external LLM upload,
paid API, mathematical execution, GPU work, TeX/PDF build, formal evaluation,
shared-index edit, or Git mutation occurred.

## Final full-question status and reusable interface

**Original LG4:** `NOT CURRENTLY JUSTIFIED / FULL_QUESTION_UNCLOSED`.
The original statement and its domain remain unchanged. No explicit triple
with all-modulus hits and no integer-time hit has been constructed.

The current new boundary is (VC): no hypothetical false positive is obtained
from an integral polynomial automorphism that commutes with a positive
iterate. This includes finite-order commuting symmetries and roots/iterates,
but not general reversing symmetries or arbitrary integral target points.
It is a classical-structure corollary and is not requested for paper admission.

The return-ideal lemma is a reusable necessary congruence test; its exact
degree-three falsifier prevents treating the entire sequence as sufficient.
The degree-five example prevents treating reversibility as a proof of
all-modulus incidence. These are proved route boundaries, not full LG4 no-go
theorems.

To finish LG4 positively by this approach one would need an additional
global algebraic rigidity statement connecting every integral point of
$X_P$ to the virtual centralizer orbit, or a different argument that forces
$\theta_P^{-1}(Q)\in\mathbb Z$. Neither is supplied. To finish negatively
through a reverser one must first prove (not sample) every prime-power and
mixed-modulus cycle incidence, and separately exclude every integer time.

`NO_BAD_EULER_OR_ROOT_NUMBER`: none of these source-arithmetic statements
constructs target Euler factors, root numbers, automorphy, a zero/divisor
correspondence, or a Hilbert–Pólya realization.
