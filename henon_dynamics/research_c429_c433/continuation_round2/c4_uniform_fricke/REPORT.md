# R2 C4: uniform nodal inertia in the Fricke periodic tower

2026-09-09. New round; accepted first-pass FG2 and all first-pass proof/review
bytes are read-only inputs. No mathematical program or old proof rerun.

## 1. Exact frozen claim and conventions

Keep the original FGT family and native clock:
$$
k=\mathbb Q(A,B,C,D),\quad
S:\ x^2+y^2+z^2-xyz-Ax-By-Cz=D,\qquad T=s_zs_ys_x,
$$
where $A,B,C,D$ are algebraically independent and the rightmost
involution acts first. Let $P_n$ be the ordinary geometric affine points
of exact least native period $n$. Let $L_n/k$ be their splitting field.
The original full question asks for the compatible image on every
$\coprod_{n\le N}P_n$, including constants and layer intersections;
it is unchanged and not presumed closed in this round.

Let $\Delta$ be the reduced irreducible discriminant divisor of singular
affine Fricke fibres in the base $B=\mathbb A^4_{A,B,C,D}$. The proposed
single uniform mechanism is:

**NI (nodal-inertia claim).** For every $n\ge3$, the normalization of
$B_{\overline{\mathbb Q}}$ in the geometric splitting field of $P_n$ is
étale over the Cayley parameter $b_C=(0,0,0,4)$. Consequently it is
unramified at the generic point of $\Delta$. For every finite joint
level $N\ge2$, the inertia at $\Delta$ in the full periodic compositum acts
only on $P_2$, where its nontrivial element is the single phase flip
supplied by accepted FG2. The corresponding neighbourhood may depend
on $n$ or $N$; no common neighbourhood for the infinite tower is claimed.
The omitted boundary $N=1$ has empty generic point set and trivial field.

The statement concerns generic characteristic-zero period fields. Its
local proof may use the singular Cayley fibre as a degeneration, but
does not identify singular fixed points with ordinary generic periodic
points. Classical fixed-intersection degrees must first be combined
with reduced local branches; formal Möbius degrees alone do not establish
ordinary exact-period counts. No claim is made for arbitrary rational
specializations or positive-characteristic reductions.

**Success criterion:** prove all exact-period sheets, including possible
remote sheets, extend without ramification near $b_C$ for every $n\ge3$,
then justify the generic-divisor conclusion. Proving only that no higher
period branch approaches one node is insufficient. **Failure criterion:**
an unaccounted sheet, resonance, or inability to pass from local sections
to the whole normalization leaves NI unproved. No isolated $n=3,4$
computation will replace this uniform question.

**Status at freeze:** NOT CURRENTLY JUSTIFIED. The planned hand argument
uses the classical Cayley torus quotient, an iterate-germ identity,
source-subtracted all-period intersection degrees and degree exhaustion.
FG2 is an accepted input, not a theorem to be reconstructed here.

## 2. Round result and proof-status separation

**Current author status: PROVABLE AS STATED. Independent whole-proof
review pending.** The frozen NI claim is unchanged; the full proof is
in [PROOF_SUPPLEMENT.md](PROOF_SUPPLEMENT.md). Original FGT remains
unclosed, and no independent paper admission is requested from NI alone.

For $u_n=(2+\sqrt5)^n+(2-\sqrt5)^n$, the proof establishes:

1. The singular-fibre discriminant is geometrically irreducible. Its
   four local Cayley branches are the accepted FG2 phase branches.
2. Every smooth Cayley fixed point of every $T^n$ has return derivative
   with no eigenvalue one, and supplies a distinct étale parameter
   branch. There are exactly $u_n-4$ such ordinary points.
3. At each node the full parameter-family fixed ideal of $T^n$ equals
   that of $T$ when $n$ is odd, or of $T^2$ when $n$ is even. The node
   contributes respectively zero or two generic point sheets, the
   latter all of native period two by FG2.
4. Thus the exhibited generic point count is
   $u_n-4+8\mathbf 1_{2\mid n}=u_n+4(-1)^n$. It equals the classical
   generic fixed-intersection length for every $n$, proving reducedness
   and excluding all remote or escaping generic sheets.
5. Exact native periods persist on the smooth branches. For $n\ge3$
   every generic exact-period sheet is therefore étale at Cayley.
   The full Galois splitting field then splits over the strict
   henselization; finite normalization and descent prove étaleness of
   the entire splitting cover, not just a selected point field.
6. A finite cover's branch image is closed. Irreducibility of $\Delta$
   propagates this étaleness to generic-$\Delta$ unramifiedness. In
   every finite joint tower the only $\Delta$ inertia is the accepted
   single period-two phase flip.

The count is ordinary only after item 4. Möbius inversion then gives
$$
|P_1|=0,\quad |P_2|=22,\quad
|P_n|=\sum_{d\mid n}\mu(n/d)u_d\quad(n\ge3).
$$
This is a consistency/interface formula, not a replacement finite
census or a new claim of source ownership for the counting sequence.

## 3. Export to the layer-intersection question

For every finite $N\ge3$, put $H_N=L_3\cdots L_N$ and
$J_N=L_2\cap H_N$. The conjugates of NI's inertia generator span the
whole FG2 phase subgroup $V_2=C_2^{11}$ and act trivially on $H_N$.
Consequently
$$
J_N\subseteq L_2^{V_2}.
$$
This is the exact uniform interface sent to
[D2's round-two layer-intersection lane](../d2_fricke_layer_intersection/REPORT.md).
Its remaining cycle-sign quadratic test is not resolved by NI.
Higher-layer irreducibility/transitivity, higher rotation generators,
maximal higher groups and the full compatible FGT image also remain
unproved. No common infinite-tower étale neighborhood is asserted.

## 4. Primary-source subtraction and audit scope

- [Cantat–Loray, §2.1](https://arxiv.org/pdf/0711.1579), pp. 12–13:
  the Cayley quotient and monomial action are classical background.
  The exact native matrix is also already fixed in accepted D2.
- [Iwasaki–Uehara, §8](https://arxiv.org/pdf/math/0512583v3), pp. 21–23:
  the no-curve, graph-intersection and boundary calculation owns the
  all-exponent length input. Smooth-fibre reducedness is not imported.
- [Stacks 0CBF](https://stacks.math.columbia.edu/tag/0CBF) and
  [06DI](https://stacks.math.columbia.edu/tag/06DI) supply the general
  normalization/base-change facts used in the full splitting-cover
  passage. Their displayed lemmas were read in full by the author.

The new proof increment is the uniform parameter-family iterate
identity combined with complete degree exhaustion and exact-period
persistence to isolate nodal inertia from every higher native layer.
Targeted Fricke/Markoff periodic-monodromy and discriminant searches
did not locate this exact statement in the inspected primary passages;
this is a bounded source check, not a global novelty certificate.

A single bounded read-only child audited only the abstract étale
splitting-normalization step. It passed the stated step and identified
why a non-Galois single-root shortcut would be invalid; the proof uses
full splitting and Galoisness explicitly. This is author-side support,
not independent acceptance of NI or of the source applicability.

The proof-writer checklist determined the explicit status gate, the
all-sheet obligation and the separation of imported lengths from
ordinary counts. No mathematical programs, old reruns, PDF/manuscript
builds, external-model uploads, Git or shared-file writes were run.
Only this assigned new continuation directory was written.
