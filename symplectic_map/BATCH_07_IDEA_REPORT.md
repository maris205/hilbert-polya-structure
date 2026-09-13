# Batch 07 Idea Discovery Report

This report is append-only from its creation on 2026-08-30 UTC.  Later
addenda may consume, reject, correct, or supersede a candidate, but they may
not erase a search result, killed alternative, formula, counterexample,
collision, score, limitation, or authority boundary recorded below.

## Current decision and authority

- Current serial position: Paper 28, after Paper 27 reached an independently
  reviewed terminal non-release disposition.
- Historical action finding: the disclosed pre-discovery no-match future
  glob remains immutable history.  Its independent review permits bounded
  continuation only under an exact-path, no-glob firewall.
- Candidate identifier: primitive_selector_cycle_monodromy_v1.
- Candidate version: V1 author stop.
- Public-safe working title: **Primitive Newton-Selector Cycles in
  Permutation-Twisted Hamiltonian Shears: Normal-Fan Classification and Exact
  Monodromy**.
- Candidate decision: advance V1 to two fresh, mutually blind candidate
  reviews.
- Paper number consumed: no.
- Project directory authorized or created: no.
- Scientific computation, CAS, numerical experiment, dataset, or GPU use:
  none.
- External effect: none.

The proposed contribution is not merely the existence of a long tropical
state cycle.  For every rooted primitive cyclic word of selector pairs of
length at least three, it constructs one fixed autonomous polynomial
symplectomorphism whose strict Newton selectors follow exactly that word,
classifies strict words in the whole equitotal permutation-twisted class by a
rational polyhedral iff criterion, proves the actual polynomial-degree lift,
proves least selector and quotient periods, and computes a monodromy that
losslessly encodes the rooted word.

The quantifier is important: for every word w there exists one autonomous map
F_w.  There is no claim that one universal map realizes every word or every
length.

## Discovery lanes and killed alternatives

The search did not promote the first attractive construction.  Four
alternatives were killed before the retained theorem was frozen.

| Lane | Candidate | Exact disposition |
|---|---|---|
| Planar autonomous wall cycling | Extend Paper 24 from two chambers to an autonomous primitive cycle of length at least three using positive two-variable supports and a pure-power second shear | STOP.  The induced projective map is continuous and decreasing, so it has no orbit of least period greater than two. |
| Periodically forced shears | Prescribe a phase-dependent list of one-monomial shear maps and multiply their degree matrices | STOP AS TAUTOLOGICAL.  The switch word is an external schedule, not an endogenous Newton selector. |
| Symmetric permutation twist | Add a cyclic coordinate permutation to a fully equivariant spike family | STOP AS RELABELLING-LEVEL.  Selector labels rotate, but the scalar forcing is stationary and the support symmetry makes the mechanism too close to a coordinate gauge. |
| Zero-coordinate supports | Use missing variables to create asynchronous gradient rows and a finite selector automaton | RESERVED / FORBIDDEN HERE.  Derivative disappearance and leading cancellation are the separate Paper 31 axis. |
| Equitotal incidence supports plus a finite-order twist | Encode an arbitrary primitive pair word in positive support incidence sets; classify it by normal cones and recover it from exact monodromy digits | RETAINED AS V1. |

### Exact planar obstruction

For a positive two-variable support and a pure-power momentum shear, let

\[
 H(r)=\max_{(a,b)}(ar+b),\qquad r>0.
\]

On the chamber selected by \((a,b)\), the projective degree map has the form

\[
 g(r)=\kappa\frac{H(r)-r}{H(r)-1}
 =\kappa\frac{(a-1)r+b}{ar+b-1}.
\]

It is continuous across Newton walls, and on every open chamber

\[
 g'(r)=\kappa\frac{1-a-b}{(ar+b-1)^2}<0.
\]

A continuous decreasing interval map has no cycle of least period greater
than two, because its square is increasing and an increasing interval map has
no nontrivial periodic orbit.  Thus a literal planar period-three extension
of Paper 24 is structurally impossible in this positive synchronous class.
This obstruction is one reason the retained theorem uses a higher-dimensional
finite-order residual twist rather than disguising another planar example.

## Exact theorem package

### 1. General equitotal permutation-twisted class

Let K be a characteristic-zero field and let r be a positive integer.  For
finite collected supports

\[
 E_V,E_W\subset\mathbb Z_{\ge2}^{\,r},
\]

assume that every \(\alpha\in E_V\) has the same total A and every
\(\beta\in E_W\) has the same total B.  Let every displayed coefficient be
nonzero and put

\[
 V(q)=\sum_{\alpha\in E_V}a_\alpha q^\alpha,\qquad
 W(p)=\sum_{\beta\in E_W}b_\beta p^\beta.
\]

Define the two Hamiltonian shears

\[
 S_V(q,p)=(q,p+\nabla V(q)),\qquad
 T_W(q,p)=(q+\nabla W(p),p).
\]

For a permutation matrix P, let

\[
 \Pi_P(q,p)=(Pq,Pp),\qquad
 F=\Pi_P\circ T_W\circ S_V.
\]

Both gradient shears preserve the standard form
\(\omega=\sum_i dq_i\wedge dp_i\), because their off-diagonal Jacobian
blocks are symmetric Hessians.  The simultaneous permutation also preserves
\(\omega\).  Hence F is a polynomial symplectomorphism, with a polynomial
inverse obtained by reversing the permutation and subtracting the two
gradients in reverse order.

For a strict selected pair \((\alpha,\beta)\), define

\[
 A_\alpha=\mathbf1\alpha^{\mathsf T}-I,\qquad
 B_\beta=\mathbf1\beta^{\mathsf T}-I.
\]

Literal multiplication gives

\[
 B_\beta A_\alpha
 =I+\mathbf1c_{\alpha,\beta}^{\mathsf T},\qquad
 c_{\alpha,\beta}=(B-1)\alpha-\beta.
\]

The complete selected q-degree step after the permutation is therefore

\[
 C_{\alpha,\beta}
 =P+\mathbf1c_{\alpha,\beta}^{\mathsf T}.
\]

Put

\[
 \lambda=(A-1)(B-1).
\]

Then

\[
 c_{\alpha,\beta}^{\mathsf T}\mathbf1=\lambda-1.
\]

### 2. Normal-fan iff classification

For \(\alpha\in E_V\) and \(\beta\in E_W\), define the open rational normal
cones

\[
\mathcal N_V^+(\alpha)
=\{x>0:(\alpha-\gamma)\cdot x>0
\text{ for every }\gamma\ne\alpha\},
\]

\[
\mathcal N_W^-(\beta)
=\{x>0:(\eta-\beta)\cdot x>0
\text{ for every }\eta\ne\beta\}.
\]

The minus sign records that the W selector below is a minimizer on the
residual q-weight, not a maximizer.

For a rooted word

\[
 w=((\alpha_0,\beta_0),\ldots,(\alpha_{\ell-1},\beta_{\ell-1}))
\]

and a permutation P whose relevant quotient orbit has period \(\ell\), set

\[
 \mathcal C_w=
 \mathbb R_{>0}^{\,r}\cap
 \bigcap_{j=0}^{\ell-1}
 P^{-j}\bigl(
 \mathcal N_V^+(\alpha_j)\cap
 \mathcal N_W^-(\beta_j)
 \bigr).
\]

This is an open rational polyhedral cone.  Within the equitotal
positive-support class, a positive seed realizes w as a strict selector word
if and only if it lies in \(\mathcal C_w\), with the separate requirement
that the word has no smaller cyclic period for primitive minimality.
Nonemptiness is therefore an exact feasibility test, not a sufficient-only
certificate.  Every nonempty rational cone contains a positive integer seed
after scaling.

The reason the two normal fans suffice is exact.  If

\[
 u_n=x_n+t_n\mathbf1,\qquad x_n=P^nu_0,
\]

then equitotality makes the V score differences independent of \(t_n\).
Once \(\alpha_n\) is selected,

\[
 v_n=A_{\alpha_n}u_n
 =\bigl(\alpha_n\cdot x_n+(A-1)t_n\bigr)\mathbf1-x_n.
\]

For equal-total \(\beta,\eta\),

\[
 (\beta-\eta)\cdot v_n
 =-(\beta-\eta)\cdot x_n.
\]

Thus W selects exactly the unique minimizer of \(\beta\cdot x_n\).  This
proves both directions of the normal-fan criterion.

### 3. Uniform realization of every primitive pair word

Let

\[
 w=((a_0,b_0),\ldots,(a_{\ell-1},b_{\ell-1})),
 \qquad \ell\ge3,
\]

be any rooted primitive cyclic word over finite label alphabets.  Repeated
labels are allowed.  Let r=\(\ell+1\).  The ambient affine symplectic space
has dimension \(2r=2(\ell+1)\); r is the number of symplectic coordinate
pairs, not the ambient dimension.

Let \(e_0,\ldots,e_{\ell-1},e_\ast\) be the standard basis.  Let P cyclically
permute the first \(\ell\) coordinates and fix the star coordinate.  Choose
integers

\[
 H\ge2,\qquad b\ge2,\qquad K\ge1,
\]

and the positive q-weight seed

\[
 u_0=\mathbf1+(H-1)e_0.
\]

The momentum seed may be \(w_0=\mathbf1\).  Put

\[
 S_a=\{j:a_j=a\},\qquad T_b=\{j:b_j=b\}.
\]

For each used V label a and used W label b, define

\[
 \alpha_a
 =b\mathbf1+
 K\sum_{j\in S_a}e_j+
 K(\ell-|S_a|)e_\ast,
\]

\[
 \beta_b
 =b\mathbf1+
 K\sum_{j\notin T_b}e_j+
 K|T_b|e_\ast.
\]

All coordinates are at least two, and every exponent has the same total

\[
 D=br+K\ell.
\]

Thus the construction uses A=B=D and

\[
 \lambda=(D-1)^2.
\]

At phase j, \(x_j=P^ju_0\) has value H in exactly one moving coordinate and
value one elsewhere.  Write

\[
 C_0=b(H+\ell)+K\ell,\qquad
 g=K(H-1)>0.
\]

Then the scores are exactly

\[
 \alpha_a\cdot x_j=
 \begin{cases}
 C_0+g,&a=a_j,\\
 C_0,&a\ne a_j,
 \end{cases}
\]

\[
 \beta_b\cdot x_j=
 \begin{cases}
 C_0,&b=b_j,\\
 C_0+g,&b\ne b_j.
 \end{cases}
\]

Therefore \(\alpha_{a_j}\) is the unique V maximizer and
\(\beta_{b_j}\) is the unique W minimizer, both with the exact strict gap
\(K(H-1)\).  The fixed autonomous map \(F_w\), whose supports are assembled
once from the incidence sets of w, realizes the requested selector word
without an external switching schedule.

This is family-wise universality: each word produces one explicit autonomous
map.  It is not one universal map for all words.

### 4. Actual polynomial degree lift and carries

The max-plus matrices above are not accepted as formal surrogates.  The
actual weighted polynomial degrees obey them.

If \(\alpha_i\ge2\) and \(u>0\), then

\[
 (A_\alpha u)_i
 =\alpha\cdot u-u_i
 \ge2\sum_k u_k-u_i
 >u_i.
\]

The same inequality holds for \(B_\beta v>v\).  Starting from
\(0<w_0\le u_0\), induction gives

\[
 A_{\alpha_n}u_n>u_n\ge w_n,
\qquad
 B_{\beta_n}A_{\alpha_n}u_n
 >A_{\alpha_n}u_n>u_n.
\]

After applying P, the next q-degree vector remains strictly larger than the
next momentum-degree vector.  Hence every source and target carry is strict.

Every selected derivative row has a unique highest-weight monomial.  Its
derivative scalar is nonzero in characteristic zero, all support coordinates
are positive, products of nonzero leading forms remain nonzero in a
polynomial domain, and each carried term has strictly lower degree.  Thus no
leading cancellation, tie, or hidden coefficient certificate is used.  The
claim holds for every nonzero coefficient tuple with the displayed collected
supports.

The complete recurrence is consequently exact:

\[
 u_{n+1}
 =P u_n+
 \bigl(c_{a_n,b_n}^{\mathsf T}u_n\bigr)\mathbf1.
\]

Writing \(u_n=x_n+t_n\mathbf1\) gives

\[
 t_{n+1}=\lambda t_n+\mu,\qquad
 \mu=(D-1)(C_0+g)-C_0>0.
\]

The scalar forcing is deliberately constant in this realization.  The word
is encoded in the phase-resolved selector matrices and monodromy, not in a
different scalar growth curve for each word.

### 5. Exact ordered monodromy

Let

\[
 c_j=c_{a_j,b_j},\qquad
 C_j=P+\mathbf1c_j^{\mathsf T},
\]

and define the ordered prefix products

\[
 Q_s=C_{s-1}\cdots C_0.
\]

Then

\[
 Q_s=P^s+\mathbf1R_s^{\mathsf T},\qquad R_0=0,
\]

where literal multiplication gives

\[
 R_{s+1}^{\mathsf T}
 =c_s^{\mathsf T}P^s+\lambda R_s^{\mathsf T}.
\]

Hence

\[
 R_s^{\mathsf T}
 =\sum_{j=0}^{s-1}
 \lambda^{s-1-j}c_j^{\mathsf T}P^j.
\]

Because \(P^\ell=I\), the exact period monodromy is

\[
 M_w=Q_\ell
 =I+\mathbf1R_\ell^{\mathsf T},
\]

\[
 R_\ell^{\mathsf T}
 =\sum_{j=0}^{\ell-1}
 \lambda^{\ell-1-j}c_j^{\mathsf T}P^j.
\]

Furthermore,

\[
 R_\ell^{\mathsf T}\mathbf1=\lambda^\ell-1,
\]

\[
 \chi_{M_w}(z)
 =(z-1)^{r-1}(z-\lambda^\ell),
\]

\[
 M_w^k
 =I+
 \frac{\lambda^{k\ell}-1}{\lambda^\ell-1}
 \mathbf1R_\ell^{\mathsf T}.
\]

For \(0\le s<\ell\),

\[
 Q_sM_w^ku_0
 =P^su_0+
 \left[
 R_s^{\mathsf T}u_0+
 \lambda^s
 \frac{\lambda^{k\ell}-1}{\lambda^\ell-1}
 R_\ell^{\mathsf T}u_0
 \right]\mathbf1.
\]

These are exact phase-resolved weighted degree vectors, not asymptotic
spectral estimates.

### 6. Monodromy decodes the rooted word

The realization has the strict digit bounds

\[
 0<(c_{a,b})_i<\lambda
\]

for every coordinate and every used pair.  A lower bound is

\[
 (D-1)b-(b+K\ell)>0,
\]

while \(b+K\ell<D-1\) gives the upper bound.  The map

\[
 (a,b)\longmapsto c_{a,b}
\]

is injective.  Indeed, if

\[
 (D-1)(\alpha_a-\alpha_{a'})
 =\beta_b-\beta_{b'},
\]

then a moving coordinate in the symmetric difference of \(S_a,S_{a'}\)
would have left magnitude \(K(D-1)\), while the right magnitude is at most
K.  Thus \(a=a'\), and then \(b=b'\).

Each coordinate of \(R_\ell\) is therefore an ordinary base-\(\lambda\)
integer with the rotated vectors \(c_j^{\mathsf T}P^j\) as its digit vectors.
There is no carry.  Given P, \(\lambda\), and the marked phase zero, the
unique base-\(\lambda\) expansion recovers every c_j and then every ordered
pair \((a_j,b_j)\).  Thus the exact monodromy losslessly encodes the rooted
selector word.

Cyclic rotations are not falsely identified.  The seed marks phase zero.
Changing the root cyclically shifts the matrix word and gives the
corresponding cyclic period map; the unrooted necklace is a separate quotient
of the rooted statement.

### 7. Primitive period and exact recurrences

Modulo the diagonal line \(L=\mathbb R\mathbf1\),

\[
 [C_j u]=[Pu],\qquad [u_n]=[P^nu_0].
\]

If \(0<d<\ell\) and

\[
 P^du_0-u_0=c\mathbf1,
\]

then the fixed star coordinate forces \(c=0\), while the unique H-spike has
moved and prevents \(P^du_0=u_0\).  Hence the quotient orbit has least period
\(\ell\).  The realized selector-pair word is the prescribed primitive word,
so its least period is also \(\ell\).  For \(d<\ell\), the induced quotient
action \(P^d\) is not the identity, so no shorter prefix is a period
monodromy.

For any fixed phase and any linear degree observable, the exact subsequence
obeys

\[
 d_{n+2\ell}-(1+\lambda^\ell)d_{n+\ell}
 +\lambda^\ell d_n=0.
\]

The complete scalar degree sequence also satisfies

\[
 (E^\ell-1)(E-\lambda)d=0,
\]

that is,

\[
 d_{n+\ell+1}-\lambda d_{n+\ell}
 -d_{n+1}+\lambda d_n=0.
\]

These are annihilating recurrences only.  No claim is made that either is a
minimal scalar recurrence, or that the scalar trajectory distinguishes two
different words with the same \(\ell,D,H\).

## Equality walls, failure examples, and sharp boundaries

1. V walls are the exact hyperplanes
   \((\alpha-\gamma)\cdot P^ju_0=0\).  W walls are
   \((\beta-\eta)\cdot P^ju_0=0\).  On a wall the selector label is not
   unique, even if tied branches happen to produce the same scalar degree.
2. Setting \(H=1\) makes the seed diagonal.  Every realization score ties,
   the quotient period collapses to one, and there is no primitive selector
   word.
3. Replacing P by a permutation with a shorter quotient orbit makes the
   monodromy and selector period divide that shorter order.
4. Omitting the permutation leaves the residual direction fixed and returns
   to the untwisted finite-change/stationary boundary rather than a primitive
   cycle.
5. Allowing unequal support totals reintroduces \(t_n\) into score
   differences; eventual highest-total selection can destroy the requested
   word.  Equitotality is structural, not cosmetic.
6. Allowing a zero support coordinate can delete a gradient monomial and
   reopen cancellation questions.  That regime is excluded here and reserved
   for Paper 31.
7. In positive characteristic, an exponent scalar may vanish.  The theorem
   is characteristic zero.
8. A zero displayed coefficient changes the collected support and voids the
   score and noncancellation proof.
9. A nonprimitive prescribed pair word still has an \(\ell\)-step product,
   but its selector period is the proper divisor.  It is outside the
   primitive headline.
10. The polynomial state and its degree vector grow; the theorem concerns a
    periodic selector word and quotient residual, not a periodic polynomial
    state orbit.

## Primary-source search and collision boundary

### Search method and limitations

Two independent read-only scouts searched public primary sources and official
bibliographic records through 2026-08-29.  No unpublished local manuscript
was uploaded or transported.  The screen was bounded and may miss
unindexed, non-English, subscription-only, newly posted, or differently
worded work.  It supports only the statement that no exact conjunction was
found, never an absolute priority claim.

Representative exact query strings were:

1. max-plus periodic coefficients monodromy matrix discrete event system
2. tropical selector dynamics cycle max-plus
3. primitive period max-plus dynamical system
4. tropical recurrence periodic symbolic sequence cluster maps
5. path-ordered product tropical recurrence algebraic entropy
6. polynomial symplectic automorphism degree growth Hamiltonian shear permutation
7. symplectic map tropical recurrence degree growth
8. sign stability mutation loops entropy cluster stretch factor
9. periodically switched max-plus-linear systems
10. order preserving homogeneous map periodic points period bounds max-plus
11. Newton polytope iteration piecewise linear degree recurrence selector
12. non-autonomous degree growth birational mapping algebraic entropy
13. primitive selector cycle polynomial symplectic map
14. period monodromy tropical recurrence selector
15. 2025 2026 tropical algebraic entropy periodic degree growth symplectic cluster map

### Closest public primary sources

| Source | What it proves | Exact separation from V1 |
|---|---|---|
| Ohmori--Yamazaki, *A Generalization for Ultradiscrete Limit Cycles in a Certain Type of Max-Plus Dynamical Systems*, JMP 65 (2024), DOI 10.1063/5.0203186, arXiv:2402.06230 | Explicit max-plus state cycles for a restricted run/reset family, including all state periods at least four | Not arbitrary selector-pair words; no period-three theorem, normal-fan iff, polynomial symplectic lift, or word-decoding monodromy |
| Fordy--Hone, *Discrete Integrable Systems and Poisson Algebras from Cluster Maps*, CMP 325 (2014), DOI 10.1007/s00220-013-1867-y, arXiv:1207.6072 | Exact tropical recurrences, displayed periodic selector blocks, ordered branch products, conditional general spectral links | Particular blocks rather than universal word realization; general selector periodicity and parts of the spectral bridge are conjectural |
| Fordy--Hone, *Symplectic Maps from Cluster Algebras*, SIGMA 7 (2011), DOI 10.3842/SIGMA.2011.091, arXiv:1105.2985 | Symplectic reductions and particular periodic tropical degree orbits | No arbitrary strict word, least selector-period classification, or Hamiltonian polynomial-shear realization |
| W. Kim, *Integrable Deformations of Cluster Maps of Type D_2N*, MPAG 29 (2026), DOI 10.1007/s11040-026-09545-3, arXiv:2506.06182 | Exact structured 2N tropical periodicity feeding a degree-growth theorem in a cluster setting | Structured finite-type period, not every primitive word or a word-decoding monodromy |
| Ishibashi--Kano, *Algebraic Entropy of Sign-Stable Mutation Loops*, Geom. Dedicata 214 (2021), DOI 10.1007/s10711-021-00606-1, arXiv:1911.07587 | Sign itineraries, stable tropical presentation matrices, and entropy bounds/equalities under stated hypotheses | No arbitrary selector-word realization in polynomial Hamiltonian shears and no least-word iff |
| Gunawardena, *From Max-Plus Algebra to Nonexpansive Mappings*, TCS 293 (2003), DOI 10.1016/S0304-3975(02)00235-9 | Constructs broad finite state cycles in min-max/topical maps | State cycles, not endogenous Newton selector words or symplectic degree monodromy |
| Akian--Gaubert--Lemmens--Nussbaum, *Iteration of Order Preserving Subhomogeneous Maps on a Cone*, MPCPS 140 (2006), DOI 10.1017/S0305004105008832, arXiv:math/0410084 | Period bounds and realizations for state orbits of order-preserving subhomogeneous maps | Different period object; V1 lets mode dimension grow and proves selector-word rather than state period |
| Zorzenon--Komenda--Raisch, *Switched Max-Plus Linear-Dual Inequalities*, DEDS 34 (2024), DOI 10.1007/s10626-023-00389-5, arXiv:2305.02934 | Cycle-time analysis for fixed periodic switching schedules | Switch word is external; V1 encodes and selects it endogenously in one autonomous map |
| Friedland--Milnor, *Dynamical Properties of Plane Polynomial Automorphisms*, ETDS 9 (1989), DOI 10.1017/S014338570000482X | Reduced-word normal forms and exact degree products for plane polynomial automorphisms | Group-word minimality in dimension two, not Newton-selector period or the higher-dimensional normal-fan construction |
| Hasselblatt--Propp, *Degree-Growth of Monomial Maps*, ETDS 27 (2007), DOI 10.1017/S0143385707000168, arXiv:math/0604521 | Piecewise-linear degree chambers and spectral entropy for monomial maps | Stationary matrix powers; no prescribed primitive selector realization |
| Bedford--Kim, *Linear Recurrences in the Degree Sequences of Monomial Mappings*, ETDS 28 (2008), DOI 10.1017/S0143385708000242, arXiv:0710.1642 | Recurrence/nonrecurrence criteria for chamber-selected monomial degrees | No Hamiltonian shear word realization or selector minimality |
| Hone--Ragnisco--Zullo, *Algebraic Entropy for Algebraic Maps*, J. Phys. A 49 (2016), DOI 10.1088/1751-8113/49/2/02LT01, arXiv:1508.01440 | Exact tropical degree recurrences for polynomial and symplectic examples, including a period-nine tropical limit | Isolated examples, not arbitrary words or a normal-fan iff |
| Janeczko--Jelonek, *Polynomial Symplectomorphisms*, BLMS 40 (2008), DOI 10.1112/blms/bdm112 | Structural results on the polynomial symplectomorphism group | No iterate-degree selector theorem |
| Bellon--Viallet, *Algebraic Entropy*, CMP 204 (1999), DOI 10.1007/s002200050652, arXiv:chao-dyn/9805006 | Foundational degree-growth entropy | V1 makes no novelty or headline claim for entropy |

The two independent source screens found no primary theorem combining:

1. every arbitrary primitive selector-pair word, including length three;
2. endogenous realization by one autonomous polynomial symplectomorphism per
   word;
3. a rational-polyhedral iff for strict word feasibility;
4. actual-degree carry and noncancellation;
5. separate least selector and quotient periods; and
6. an exact monodromy that recovers the rooted word.

This is a bounded search gap, not a priority certificate.

## Local collision matrix

| Paper | Closest owned axis | V1 disposition |
|---:|---|---|
| 12 | Hénon period-three residue and trace separator | Period-three vocabulary only; no selector-degree collision. |
| 13 | Primitive Hénon cycle cover and orbit coordinates | Primitive periodic points, not primitive selector words. |
| 14 | Monomial Hénon finite-rank torus escape | No Newton-degree cocycle. |
| 15 | Quartic Hénon trace fibres | No Hamiltonian shear selectors. |
| 16 | Collected-support Hénon torus escape | Support language only; no degree monodromy. |
| 17 | Shift-like torus-coset dimension decay | No selector cycle. |
| 18 | Marked trace coordinates and Fitting ramification | No degree transport. |
| 19 | Maximal translates and support-one gcd obstruction | No polynomial symplectic selector word. |
| 20 | Stationary two-mode Hamiltonian degree matrix and quadratic Perron law | V1 excludes stationary two-mode spectra and begins at selector length three. |
| 21 | Stationary three-mode cubic recurrence and visibility | V1 makes no cubic/Perron or stationary-spectrum claim. |
| 22 | Arbitrary-mode endpoint spikes and cubic spectral collapse | V1 uses word-incidence equitotal supports; no endpoint family or cubic quotient claim. |
| 23 | Four-mode staggered quartic spectral escape | Different fixed stationary support mechanism. |
| 24 | Genuine ordinary-degree period-two wall exchange and two-step monodromy | Closest local predecessor. V1 treats arbitrary words of length at least three, a positive equitotal normal-fan classification, weighted seeds, and permutation-twisted exact coding; it makes no Paper-24 wall or ordinary-degree claim. |
| 25 | Support-rank characteristic factorization, unbounded Perron degree, and minimal scalar recurrence | V1 does not claim Perron algebraic degree, rank sharpness, or scalar minimality. |
| 26 | Planar collected-support envelope contraction and forward/inverse recurrences | V1 is higher-dimensional, equitotal, and selector-word focused; no planar contraction or inverse bridge. |
| 27 | Positive diagonal translation, finite global wall changes, and reflected phase reciprocity | The untwisted positive-support class remains finite-change. V1 adds a finite-order quotient twist, excludes reciprocity, and never rebrands Paper 27's theorem. |

The later reserved axes remain separate:

- Paper 29: toric cohomological degree spectra;
- Paper 30: signed block-symplectic transfer reciprocity; and
- Paper 31: zero-coordinate gradient cancellation.

V1 uses no compactification or higher cohomological degree, no reciprocal
transfer characteristic polynomial, and no zero support coordinate.

## Locked anti-claims

Paper 28 V1 does not claim:

1. one universal map for all words or all lengths;
2. fixed mode dimension while the word length tends to infinity;
3. ordinary total-degree selector cycles from the diagonal seed;
4. a periodic polynomial state orbit;
5. a first long cycle in max-plus, tropical, cluster, nonexpansive, or
   switched dynamics;
6. novelty of ordered matrix products, Floquet/period maps, monodromy, or
   algebraic entropy in isolation;
7. a dynamical-degree, entropy-equality, topological-entropy, or integrability
   theorem;
8. a minimal scalar recurrence or a new Perron algebraic-degree result;
9. arbitrary unequal-total Newton supports;
10. a tie-breaking theorem on equality walls;
11. positive-characteristic validity;
12. zero-coordinate supports or a cancellation classification;
13. inverse-degree reciprocity, cohomological spectra, or transfer
    characteristic reciprocity;
14. generic nonconjugacy of all maps in the family;
15. absolute literature priority; or
16. submission, upload, hosting, distribution, identity disclosure, or any
    external effect.

## Proof spine and adversarial obligations

1. Prove polynomial symplecticity and write the inverse in the exact phase
   order.
2. Derive \(A_\alpha\), \(B_\beta\), and
   \(B_\beta A_\alpha=I+\mathbf1c^{\mathsf T}\) from literal monomial
   gradients.
3. Prove the general normal-fan iff, including the W-minimizer sign.
4. Prove the incidence-support score table for arbitrary repeated-label
   words and exact gap \(K(H-1)\).
5. Carry both q and momentum degree states and prove strict source and target
   carries.
6. Prove unique leading-form survival over every nonzero coefficient tuple
   in characteristic zero.
7. Derive the prefix-product recursion and exact period monodromy without a
   black-box matrix package.
8. Establish digit bounds, pair-to-c injectivity, and base-\(\lambda\)
   recovery of the rooted word.
9. Separate rooted words, cyclic rotations, selector period, quotient period,
   scalar recurrence period, and state nonperiodicity.
10. Audit all equality walls and the diagonal-seed, shorter-permutation,
    unequal-total, zero-coordinate, coefficient-zero, and positive-
    characteristic failures.
11. Recheck the primary-source matrix at publication lock; make no priority
    inference from a search miss.
12. Keep every theorem-critical proof in the anonymous main body and remove
    all governance paths, hashes, event history, and discovery narrative.

## Article-mass test

The theorem supports a proof-first article without padding:

| Public component | Content pages |
|---|---:|
| Abstract | 0.5 |
| Introduction, exact contribution, and bounded positioning | 2.5 |
| Symplectic family and weighted-degree transport | 3.0 |
| Normal-fan iff classification | 4.0 |
| Arbitrary primitive-word realization | 4.0 |
| Strict carries and leading-form survival | 3.5 |
| Ordered cocycle, monodromy, and word decoding | 4.0 |
| Minimality, equality walls, and counterexamples | 3.5 |
| Collision boundary, limitations, and conclusion | 2.0 |
| **Total** | **27.0** |

References are excluded.  No proof appendix is needed.  The plan uses zero
figures, zero empirical plots, zero datasets, and at most three hand-typeset
mathematical tables.

## Provisional author scores and next gate

- Bounded-search novelty: 8.2 / 10.
- Standalone mathematical value after predecessor absorption: 8.2 / 10.
- Proof confidence after independent algebra attack: 9.3 / 10.
- Credible anonymous proof-first content: 27.0 pages.
- Scientific execution supporting headline: none.
- Current finding census at author stop: Blocker 0; Major 0; Minor 0;
  Ambiguity 0.

These are author-side provisional scores, not a candidate PASS.  Two fresh,
mutually independent reviewers must now work from this frozen report and the
declared predecessor/source boundary.  R1 must independently assess theorem
size, current literature, collision, proof plausibility, and article mass.
R2 must independently rederive the score table, carries, matrix products,
digit decoding, minimality, and counterexamples without reading R1's private
reasoning.  Either reviewer returns FAIL / WRITE NOTHING on any finding.  No
Paper 28 number, project, source-design file, build, release, or external
effect is authorized at this stop.

BATCH07_PAPER28_CANDIDATE_V1_AUTHOR_STOP

## Append-only V1 notation and quantifier correction

This correction changes no support, score, matrix, theorem, score, source,
or permission.  It removes two notation/quantifier ambiguities in the V1
author stop.

### Baseline exponent versus W-label

In the explicit realization section, the baseline exponent previously denoted
by b is canonically renamed \(b_0\ge2\).  Symbols \(b_j\), \(T_b\), and
\(\beta_b\) remain W-alphabet labels.  The controlling formulas are:

\[
 \alpha_a
 =b_0\mathbf1+
 K\sum_{j\in S_a}e_j+
 K(\ell-|S_a|)e_\ast,
\]

\[
 \beta_{\mathfrak b}
 =b_0\mathbf1+
 K\sum_{j\notin T_{\mathfrak b}}e_j+
 K|T_{\mathfrak b}|e_\ast,
\qquad
 T_{\mathfrak b}=\{j:b_j=\mathfrak b\}.
\]

Thus

\[
 D=b_0r+K\ell,\qquad
 C_0=b_0(H+\ell)+K\ell,\qquad
 \lambda=(D-1)^2.
\]

The digit estimates use

\[
 (D-1)b_0-(b_0+K\ell)>0,
\qquad
 b_0+K\ell<D-1.
\]

Every earlier occurrence of the baseline b in those four formula families
means \(b_0\); every subscripted or alphabetic b means a W label.

### Exact seed and iff quantifiers

Fix the permutation convention

\[
 Pe_j=e_{j+1\pmod\ell}\quad(0\le j<\ell),
\qquad Pe_\ast=e_\ast.
\]

Then \(x_j=P^ju_0\) has its unique H-coordinate at \(e_j\).
Weighted degree means the coordinatewise polynomial degree induced by
positive q-variable weights \(u_0\) and momentum-variable weights \(w_0\).

The controlling general iff is:

> For equitotal supports contained in
> \(\mathbb Z_{\ge2}^{\,r}\), a rooted length-\(\ell\) word w is the exact
> strict selector word of the permutation-twisted weighted-degree orbit if
> and only if \(u_0\in\mathcal C_w\), the permutation residual has the
> declared length-\(\ell\) return, and \(0<w_0\le u_0\).

The positive-support inequalities then make both carry conditions automatic
at every phase.  Primitive selector minimality additionally requires that w
have no proper cyclic period and that the selector pairs separate the
declared quotient orbit.  In the explicit incidence realization, the unique
H-coordinate, the fixed star coordinate, and the prescribed primitive word
prove those clauses exactly.

For the scalar recurrence, \(d_n\) denotes the maximum weighted coordinate
degree after the complete nth iterate.  The q degrees strictly dominate the
momentum degrees after the first complete step, so this scalar is the maximum
entry of \(u_n\); no unproved choice of a visible coordinate is used.

The historical author-stop line immediately above is retained as the
pre-correction marker.  The sole controlling V1 review target is the complete
report through the corrected marker below.

BATCH07_PAPER28_CANDIDATE_V1_AUTHOR_STOP_CORRECTED

## Append-only V2 correction packet after the dual V1 failure

Authorization: `B07-E0163-P28-CANDIDATE-V1-DUAL-FAIL-V2-AUTHORIZATION-HASH-CORRECTION`,
with controlling gate
`BATCH07_PAPER28_CANDIDATE_V1_DUAL_FAIL_V2_CORRECTION_AUTHORIZED_CORRECTED`.
The pre-correction artifact is the complete 32,149-byte V1 report with 852
line feeds and SHA-256
`89c1544ebf78c1e55348e4e5f685a78e5fef712324e0e42a7e7508336ec947c5`.
No V1 byte or historical marker is removed.  This packet supersedes only the
conflicting dimension, momentum-seed iff, decoder-side-information, and
closest-literature sentences identified below.  Every unaffected definition,
calculation, boundary, anti-claim, and scope restriction in V1 remains part of
the candidate.

### 1. Exact closure of the dimension finding

Every general strict-carry and coefficient-uniform actual-degree statement is
now restricted to
\[
                 r\geq 2.
\]
For \(u\in\mathbb R_{>0}^{r}\) and
\(\alpha\in\mathbb Z_{\geq2}^{r}\),
\[
 (A_\alpha u)_i-u_i
 =\alpha^{\mathsf T}u-2u_i
 =(\alpha_i-2)u_i+\sum_{k\ne i}\alpha_k u_k>0                 \tag{V2.1}
\]
when \(r\geq2\).  The same calculation gives
\((B_\beta v)_i-v_i>0\) for positive \(v\), coordinatewise
\(\beta\geq2\), and \(r\geq2\).  This is the exact missing hypothesis in
the two automatic-carry inequalities.

The headline construction has
\[
             \ell\geq3,\qquad r=\ell+1\geq4,
             \qquad \dim_{\mathrm{symp}}=2r=2(\ell+1),          \tag{V2.2}
\]
so it lies strictly inside the corrected range.  No theorem about a strict
actual-degree lift is asserted for \(r=1\).  The quadratic example
\(V(q)=q^2\), \(W(p)=-p^2/4\) over \(\mathbb Q\) is retained as a sharp
excluded boundary: the target coordinate can cancel to \(-p/2\), while the
formal matrices give \(A_2=B_2=[1]\).  Thus dimension one is not hidden in a
generic-coefficient exception; it is outside the theorem.

### 2. Exact momentum-seed gate and the corrected iff

Fix a positive position-weight seed \(u_0\) for which the phase-zero selected
V exponent is \(\alpha_{a_0}\), and put
\[
                         v_0=A_{\alpha_{a_0}}u_0.
\]
Within the positive-weight domain, the exact phase-zero **strict source-carry
gate** is
\[
                 0<w_0<v_0=A_{\alpha_{a_0}}u_0                 \tag{V2.3}
\]
coordinatewise.  This is the necessary-and-sufficient inequality for the
strict domination used by this actual-degree lift.  It replaces every V1
sentence that made \(0<w_0\leq u_0\) a necessary part of a global iff.

Once (V2.3) holds, the selected first full step satisfies
\[
 w_1=P v_0,
 \qquad
 u_1=P B_{\beta_{b_0}}v_0,
 \qquad
 u_1>w_1                                                   \tag{V2.4}
\]
by (V2.1).  Inductively, if \(u_n>w_n\), then
\[
 A_{\alpha_{a_n}}u_n>u_n>w_n,
 \qquad
 P B_{\beta_{b_n}}A_{\alpha_{a_n}}u_n
   >P A_{\alpha_{a_n}}u_n,                                \tag{V2.5}
\]
so no additional momentum inequality is required at later phases.

The convenient seed chamber
\[
                         0<w_0\leq u_0                        \tag{V2.6}
\]
remains a simple sufficient subcone because (V2.1) gives
\(A_{\alpha_{a_0}}u_0>u_0\), but (V2.6) is not necessary.  For example, in
the explicit \(\ell=3\), \(b_0=2\), \(K=1\), \(H=2\) construction with a
phase-zero singleton V occurrence,
\[
 u_0=(2,1,1,1),\quad \alpha_{a_0}=(3,2,2,4),\quad
 A_{\alpha_{a_0}}u_0=(12,13,13,13).
\]
The positive weight \(w_0=(3,1,1,1)\) violates (V2.6) but satisfies (V2.3),
and therefore produces the same strict selector/carry induction.

The corrected classification separates three logically distinct statements.

1. **Selector iff.**  In the equitotal positive-support class, the rooted
   strict selector-pair word is realized exactly iff
   \[
   u_0\in \mathcal C_{\mathsf w}
   =\mathbb R_{>0}^{r}\cap
     \bigcap_{j=0}^{\ell-1}P^{-j}
       \bigl(N_V^+(\alpha_{a_j})\cap N_W^-(\beta_{b_j})\bigr). \tag{V2.7}
   \]
   The V cone is a strict maximizer cone and the W cone is a strict minimizer
   cone.  Equal exponent totals make diagonal translations invisible to all
   these comparisons.

2. **Strict actual-degree lift iff.**  For a seed satisfying (V2.7), the
   strict-carry lift used in the theorem holds exactly when its positive
   momentum weight satisfies (V2.3).  The coefficient tuple is otherwise
   arbitrary in \((\Bbbk^*)^{|E_V|+|E_W|}\), over a characteristic-zero
   field/domain, because the unique selected monomials and both strict carries
   then exclude leading cancellation at every step.

3. **Least periods.**  A primitive prescribed pair word has least selector
   period \(\ell\).  The quotient position-weight orbit has least period
   \(\ell\) precisely under the additional phase-separation condition
   \[
        [P^d u_0]\ne[u_0]\quad
        \text{in }\mathbb R^r/\mathbb R\mathbf1
        \quad(1\leq d<\ell).                                \tag{V2.8}
   \]
   The explicit spike seed \(u_0=\mathbf1+(H-1)e_0\), \(H\geq2\), satisfies
   (V2.8): the fixed star coordinate forces a possible diagonal displacement
   to be zero, while the unique H-spike moves through the \(\ell\)-cycle.

Thus normal-fan membership, first-carry admissibility, word primitivity, and
quotient-phase separation are no longer compressed into one overbroad iff.
For the explicit realization used by the article, all four are literal and
nonempty; choosing (V2.6) is merely the canonical easy seed choice.

### 3. Decoder side information and exact recovery scope

Retain
\[
 R_\ell^{\mathsf T}
 =\sum_{j=0}^{\ell-1}\lambda^{\ell-1-j}c_j^{\mathsf T}P^j,
 \qquad 0<(c_j)_i<\lambda.                                  \tag{V2.9}
\]
The precise decoder statement is now the following.

* Given \(M_{\mathsf w}=I+\mathbf1R_\ell^{\mathsf T}\), \(P\), \(\lambda\),
  \(\ell\), and a marked phase zero, coordinatewise base-\(\lambda\)
  expansion recovers the ordered rotated digit vectors
  \(c_j^{\mathsf T}P^j\), hence the rooted ordered vector word
  \((c_0,\ldots,c_{\ell-1})\), exactly.
* Given in addition the labelled support dictionary of the constructed map
  \(F_{\mathsf w}\), equivalently the injective table
  \((a,b)\mapsto c_{a,b}=(D-1)\alpha_a-\beta_b\), the same data recover the
  rooted ordered label-pair word
  \(((a_0,b_0),\ldots,(a_{\ell-1},b_{\ell-1}))\) exactly.
* If the supports are supplied without literal alphabet names, recovery is of
  the rooted support-pair word, or equivalently of the label word only up to
  independent bijective renaming of the V and W alphabets.  Literal names
  cannot be inferred from algebraic data and are not claimed to be.
* If phase zero is not marked, only the cyclic rotation class is intrinsic;
  cyclically shifted products are treated separately.  No equality of all
  rotated monodromy matrices is asserted.

The digit theorem therefore encodes genuine phase-resolved support data, but
does not pretend that arbitrary human alphabet names are spectral invariants.
The scalar weighted-degree trajectory still does not distinguish words with
the same \((\ell,D,H)\); its role remains only the stated annihilating
recurrence, never a decoding theorem or a minimal-recurrence claim.

### 4. Added adjacent-literature boundary

The bounded search dossier now includes the following two primary sources.

* Jérémy Blanc and Immanuel van Santen, *Dynamical degrees of
  affine-triangular automorphisms of affine spaces*, **Ergodic Theory and
  Dynamical Systems** 42 (2022), DOI `10.1017/etds.2021.90`,
  arXiv:`1912.01324`.  They develop weighted degree functions/monomial
  valuations, leading parts, associated matrices, permutation-elementary and
  affine-triangular automorphisms, and dynamical-degree calculations.  Their
  result is a necessary comparison for the permutation-plus-weighted-degree
  mechanism here.  It does not realize every primitive endogenous
  selector-pair word, give the Hamiltonian-shear symplectic construction,
  classify strict word chambers by a normal-fan iff, or decode a rooted finite
  selector cocycle from an exact monodromy.
* Irène Meunier, *Minimality locus of weighted degrees for tame
  automorphisms*, author-hosted 21-page public primary draft available by the
  2026-08-29 cutoff.  It studies monomial valuations and minimality loci for
  tame automorphisms, including elementary/triangular maps composed with
  permutations in dimensions two and three; its fixed/minimal regions are
  described by weighted-degree inequalities and hyperplanes.  This is a close
  geometric boundary for the phrase “normal-fan classification.”  It neither
  supplies arbitrary primitive selector-word realization nor the present
  symplectic strict-carry, base-\(\lambda\) decoding, and two least-period
  theorem package.

These comparisons narrow the positioning: weighted-degree chambers,
permutations, and matrix growth are established ingredients.  The claimed
contribution is their exact conjunction with arbitrary primitive rooted
selector-pair realization inside one autonomous polynomial symplectomorphism
\(F_{\mathsf w}\) **per word**, coefficient-uniform strict actual-degree
lifting, rational-polyhedral selector iff, phase-resolved monodromy decoding,
and separate least selector/quotient periods.  The article will use the
priority-safe formulation “we are unaware of a prior theorem combining these
properties after the stated bounded search,” not a universal first/only
claim.

### 5. V2 frozen theorem scope and all-zero author preflight

The V2 headline is unchanged except for the literal repairs above:

> For every rooted primitive selector-pair word of length \(\ell\geq3\), the
> incidence construction produces one fixed autonomous polynomial
> symplectomorphism \(F_{\mathsf w}\) on \(2(\ell+1)\) variables.  Its explicit
> spike seed lies in a nonempty strict normal-fan chamber; every positive
> momentum seed satisfying (V2.3) gives the coefficient-uniform strict
> actual-degree lift.  The selector word and quotient phase both have least
> period \(\ell\), and the rooted ordered support-pair word is decoded exactly
> by the marked monodromy, with literal labels recovered when the labelled
> support dictionary of \(F_{\mathsf w}\) is supplied.

It remains one map per word, not one universal map and not one map for all
words of a fixed length.  Ambient dimension grows with \(\ell\).  No ordinary
total-degree, dynamical-degree, entropy, Perron-realization, cohomological,
reciprocity, zero-coordinate, scalar word-decoding, or minimal scalar
recurrence conclusion is present.  Characteristic zero, nonzero coefficients,
strict inequalities, positive weights, exponent coordinates at least two,
equal totals, the declared permutation, word primitivity, and marked versus
unmarked phase conventions remain explicit hypotheses.

V2 author preflight after these exact corrections:

| class | count |
|---|---:|
| Blocker | 0 |
| Major | 0 |
| Minor | 0 |
| Ambiguity | 0 |

Provisional author-only scores are novelty \(8.0/10\), standalone value
\(8.0/10\), proof confidence \(9.4/10\), and 24--28 anonymous content pages.
They confer no authority.  V2 requires two new, mutually blind formal reviews;
neither V1 reviewer may be reused.  No Paper28 number or project path is
consumed by this author stop.

BATCH07_PAPER28_CANDIDATE_V2_AUTHOR_STOP

## Append-only V3 scalar-index correction packet

Authorization: `B07-E0166-P28-CANDIDATE-V2-ASYMMETRIC-VERDICT-V3-CORRECTION-AUTHORIZATION`,
with terminal gate
`BATCH07_PAPER28_CANDIDATE_V2_ASYMMETRIC_VERDICT_V3_CORRECTION_AUTHORIZED`.
The complete V1 and V2 bytes and their markers remain immutable.  This packet
supersedes only the scalar-observable definitions and starting indices in V1
and V2.  Every other V2 correction, theorem hypothesis, formula, proof step,
literature boundary, failure example, and anti-claim remains controlling.

### Exact separation of position and complete-state scalar degrees

For the explicit spike realization, write the position- and momentum-weight
vectors after the complete \(n\)-th iterate as \(u_n\) and \(w_n\).  Retain
\[
 u_n=P^nu_0+t_n\mathbf1,
 \qquad t_0=0,
 \qquad t_{n+1}=\lambda t_n+\mu,                              \tag{V3.1}
\]
and define two different scalar sequences:
\[
 q_n:=\max_i (u_n)_i,
 \qquad
 d_n:=\max\!\left\{\max_i(u_n)_i,\max_i(w_n)_i\right\}.       \tag{V3.2}
\]
Thus \(q_n\) is the position-only maximum and \(d_n\) is the maximum weighted
coordinate degree of the complete state.  They are not identified at time
zero unless their initial maxima agree.

For the spike seed \(u_0=\mathbf1+(H-1)e_0\),
\[
                         q_n=H+t_n.                            \tag{V3.3}
\]
Consequently \(q_n\) satisfies, from \(n=0\),
\[
 q_{n+2}-(1+\lambda)q_{n+1}+\lambda q_n=0,                    \tag{V3.4}
\]
and hence also the deliberately nonminimal annihilator
\[
 q_{n+\ell+1}-\lambda q_{n+\ell}-q_{n+1}+\lambda q_n=0
 \qquad(n\geq0).                                              \tag{V3.5}
\]

More generally, for every fixed position coordinate \(i\),
\[
 (u_n)_i=1+(H-1)\mathbf1_{\{n\equiv i\pmod\ell\}}+t_n,       \tag{V3.6}
\]
so that fixed coordinate sequence satisfies (V3.5) for \(n\geq0\).
Restricting to one residue class modulo \(\ell\) gives the stated
\(\ell\)-step order-two annihilator
\[
 x_{n+2\ell}-(1+\lambda^\ell)x_{n+\ell}
   +\lambda^\ell x_n=0.                                      \tag{V3.7}
\]
The former phrase “any linear degree observable” is withdrawn; (V3.3),
(V3.6), and their displayed consequences are the exact scalar claims.

The V2 first-carry gate gives
\[
 0<w_0<A_{\alpha_{a_0}}u_0,
 \qquad u_1>w_1,
 \qquad u_n>w_n\quad(n\geq1).                                \tag{V3.8}
\]
Therefore
\[
                         d_n=q_n\quad(n\geq1),                \tag{V3.9}
\]
and the complete-state scalar satisfies
\[
 d_{n+\ell+1}-\lambda d_{n+\ell}-d_{n+1}+\lambda d_n=0
 \qquad(n\geq1).                                             \tag{V3.10}
\]
There is no unconditional \(n=0\) instance for \(d\).  Because every term
other than \(d_0\) in that instance already equals its \(q\)-counterpart,
\[
 d_{\ell+1}-\lambda d_\ell-d_1+\lambda d_0
   =\lambda(d_0-q_0).                                        \tag{V3.11}
\]
Hence the complete-state recurrence also holds at \(n=0\) **if and only if**
\[
                 d_0=q_0
 \quad\Longleftrightarrow\quad
                 \max_i(w_0)_i\leq\max_i(u_0)_i.             \tag{V3.12}
\]
The canonical subcone \(0<w_0\leq u_0\) implies (V3.12), but is neither
required for the strict actual-degree lift nor substituted back into its
exact gate.

The V2 counterexample now becomes a sharp boundary check rather than a false
theorem instance.  With
\[
 \ell=3,\ r=4,\ b_0=2,\ K=1,\ H=2,\quad
 u_0=(2,1,1,1),\quad w_0=(10,10,10,10),
\]
the strict first-carry inequality still holds because
\(A_{\alpha_{a_0}}u_0=(12,13,13,13)\).  Here
\(\lambda=100\), \(\mu=127\), \(q_0=2\), and \(d_0=10\).
Equation (V3.11) gives the observed defect
\[
 d_4-100d_3-d_1+100d_0=100(10-2)=800,
\]
while (V3.10) holds for every \(n\geq1\) and (V3.5) holds for \(q\) from
\(n=0\).  No initial datum is silently replaced.

### V3 scope and author preflight

The scalar statements remain annihilating recurrences only.  No minimality,
word decoding from a scalar sequence, ordinary total-degree theorem,
dynamical degree, entropy, or periodic polynomial-state claim is added.
The rooted support-pair word is still decoded only from the marked full
monodromy with the exact side information frozen in V2.

The literature and standalone delta are unchanged from V2; the V2 R1 PASS is
retained as historical evidence bound only to V2 and is not treated as a V3
review.  The corrected V3 author-only preflight is:

| class | count |
|---|---:|
| Blocker | 0 |
| Major | 0 |
| Minor | 0 |
| Ambiguity | 0 |

Provisional author scores remain novelty \(8.0/10\), standalone value
\(8.0/10\), proof confidence \(9.5/10\), and 24--28 anonymous content pages.
They confer no authority.  Two entirely new, mutually blind V3 formal
reviewers must assess the complete append-only candidate.  Paper28 remains
unconsumed and no project path is opened by this stop.

BATCH07_PAPER28_CANDIDATE_V3_AUTHOR_STOP

## Append-only V4 coordinate-domain and empty-competitor correction packet

Authorization: `B07-E0168-P28-CANDIDATE-V3-DUAL-FAIL-V4-CORRECTION-AUTHORIZATION`,
with gate
`BATCH07_PAPER28_CANDIDATE_V3_DUAL_FAIL_V4_CORRECTION_AUTHORIZED`.
All V1--V3 bytes and markers remain immutable.  This packet supersedes only
the coordinate quantifier and scalar name in (V3.6)--(V3.7), together with
every earlier unqualified statement that both selector sides always have a
finite gap exactly \(g\).  All other V3 statements remain controlling.

### 1. Named moving and star coordinate sequences

Let
\[
 I_{\mathrm{mov}}=\{0,1,\ldots,\ell-1\},
 \qquad I=I_{\mathrm{mov}}\sqcup\{\star\}.
\]
For each coordinate, introduce a fresh scalar name that is not the earlier
residual vector \(x_n=P^nu_0\):
\[
 y_n^{(i)}:=(u_n)_i\quad(i\in I_{\mathrm{mov}}),
 \qquad
 y_n^{(\star)}:=(u_n)_\star.                                 \tag{V4.1}
\]
The exact coordinate formulas are
\[
 y_n^{(i)}
 =1+(H-1)\mathbf1_{\{n\equiv i\pmod\ell\}}+t_n
 \quad(i\in I_{\mathrm{mov}}),                              \tag{V4.2}
\]
and, separately,
\[
                         y_n^{(\star)}=1+t_n.                 \tag{V4.3}
\]
There is no expression \(n\equiv\star\pmod\ell\).  Thus (V4.2) is stated
only on its literal moving-coordinate domain, and (V4.3) covers the fixed
coordinate.

For every named coordinate \(i\in I\), both (V4.2) and (V4.3) imply
\[
 y_{n+\ell+1}^{(i)}-\lambda y_{n+\ell}^{(i)}
 -y_{n+1}^{(i)}+\lambda y_n^{(i)}=0
 \qquad(n\geq0).                                             \tag{V4.4}
\]
For an entirely unambiguous phase-subsequence statement, fix
\(i\in I\) and \(s\in I_{\mathrm{mov}}\), and define
\[
                         z_m^{(i,s)}:=y_{s+m\ell}^{(i)}.
\]
Then
\[
 z_{m+2}^{(i,s)}-(1+\lambda^\ell)z_{m+1}^{(i,s)}
 +\lambda^\ell z_m^{(i,s)}=0
 \qquad(m\geq0).                                             \tag{V4.5}
\]
Equations (V4.1)--(V4.5) replace the undefined scalar \(x_n\) in V3.7 and
do not alter the position maximum \(q_n\), complete-state maximum \(d_n\),
or any starting index in (V3.3)--(V3.12).

### 2. Exact competitor-dependent selector margins

Let \(\mathcal A\) and \(\mathcal B\) be the distinct V and W labels that
actually occur in the prescribed word.  At phase \(j\), the incidence score
table is exactly
\[
 \alpha_{a_j}^{\mathsf T}x_j=C_0+g,
 \qquad
 \alpha_a^{\mathsf T}x_j=C_0
 \quad(a\in\mathcal A\setminus\{a_j\}),                      \tag{V4.6}
\]
and
\[
 \beta_{b_j}^{\mathsf T}x_j=C_0,
 \qquad
 \beta_b^{\mathsf T}x_j=C_0+g
 \quad(b\in\mathcal B\setminus\{b_j\}),                    \tag{V4.7}
\]
where \(g=K(H-1)>0\).

Consequently, **for every actually existing competitor**, the selected V
score exceeds that competitor by exactly \(g\), and every competing W score
exceeds the selected W score by exactly \(g\).  If
\(\mathcal A\setminus\{a_j\}=\varnothing\), the sole V exponent is the
unique maximizer vacuously and no finite competitor margin is assigned on
that side.  If
\(\mathcal B\setminus\{b_j\}=\varnothing\), the sole W exponent is the
unique minimizer vacuously and no finite competitor margin is assigned.
Equivalently, an extended-real “distance to the best competitor” may be set
to \(+\infty\) for an empty competitor set, but it is not called \(g\).

The strict normal cone for a singleton support is the full weight space,
because its defining intersection of inequalities against other support
points is empty.  This preserves both directions of the normal-fan selector
iff.  It also preserves arbitrary primitive pair words in which one component
alphabet is a singleton while the other component carries the primitive
period; no artificial two-label hypothesis is added.

The phrase “both selectors have exact gap \(g\)” is therefore valid only when
both phasewise competitor sets are nonempty.  The theorem uses uniqueness,
not a finite margin on a singleton side, so the carry, leading-survival,
monodromy, decoding, and least-period proofs are unchanged.

### 3. V4 frozen scope and preflight

V4 changes no map, support vector, exponent total, cone, matrix, recurrence,
coefficient domain, momentum gate, decoder input, period claim, literature
comparison, or anti-claim.  Its only effect is to make three previously local
phrases literal on all allowed words and all \(r=\ell+1\) coordinates.

The V4 author-only preflight is:

| class | count |
|---|---:|
| Blocker | 0 |
| Major | 0 |
| Minor | 0 |
| Ambiguity | 0 |

Provisional author scores remain novelty \(8.0/10\), standalone value
\(8.0/10\), proof confidence \(9.6/10\), and 24--28 anonymous content pages.
They confer no authority.  V4 requires two entirely new, mutually blind full
formal reviews.  Paper28 remains unconsumed and its project remains absent.

BATCH07_PAPER28_CANDIDATE_V4_AUTHOR_STOP

## Append-only Paper29 candidate V1 discovery and author-stop packet

Authorization: `B07-E0217-P29-CANDIDATE-DISCOVERY-AUTHORIZATION`, with
terminal gate `BATCH07_PAPER29_CANDIDATE_DISCOVERY_AUTHORIZED`.  This packet
is the sole authorized physical-EOF append.  It preserves every Paper27 and
Paper28 discovery byte and consumes neither the Paper29 number nor a project
path.  Public literature lookup was read-only.  No project, source, build,
compiler, PDF, release, submission, upload, message, or other external effect
is authorized or claimed.

### 1. Candidate identity and public-safe headline

Reserved candidate ID:

`toric_cohomological_degree_spectrum_v1`

Proposed anonymous title:

> **Paired-Totally-Nonnegative Symplectic Monomial Maps on a Fixed Product
> Compactification: Two-Sided Stability, Exact Compound Degrees, and
> Realizable Spectral Walls**

Public-safe headline:

> On the single smooth toric compactification
> \(X=(\mathbf P^1)^{2n}\), an explicit non-diagonal family of integral
> log-symplectic monomial birational maps and their inverses are separately
> stable in every codimension.  All finite-time mixed degrees are coefficients
> of one block product, the dynamical-degree spectrum recovers the ordered
> integer parameters, and every center-symmetric log-concavity equality-wall
> pattern is realized, including the unipotent central boundary.

The novelty claim is the conjunction after all cited components are removed.
It is **not** a priority claim for absolute-compound pullbacks, total
nonnegativity as a stability criterion, the usual monomial dynamical-degree
formula, reciprocal symplectic spectra, or finite-time symplectic degree
duality.

### 2. Bounded discovery protocol and its limitation

The bounded search ended on 2026-08-29 and used primary articles, publisher or
DOI records, arXiv records, and author pages.  Query families included:

1. `monomial map dynamical degrees toric cohomology`;
2. `pullback absolute minors (P1)^n monomial map`;
3. `algebraic stability monomial maps fan toric`;
4. `stabilization monomial maps higher codimension same sign minors`;
5. `linear recurrences degree sequences monomial mappings`;
6. `compound matrix monomial map pullback cohomology`;
7. `totally nonnegative monomial maps dynamical degree`;
8. `monomial map inverse k-stable toric`;
9. `symplectic monomial map toric dynamical degree`;
10. `time reversal palindromic degree monomial maps symplectic`;
11. `Dopico Johnson totally nonnegative symplectic standard J`;
12. `integral symplectic Perron-Frobenius reciprocal polynomial`;
13. `Salem numbers dynamical degrees symplectic automorphisms`;
14. `equidistribution without stability toric surface maps`;
15. `volume preserving birational maps logarithmic form`; and
16. recent 2024--2026 toric, monomial, symplectic-spectrum, and degree-series
    records.

The search found no primary source directly containing the complete package
of paired TN blocks, same-\(X\) forward and inverse all-codimension stability,
the full finite-time coefficient product, exact parameter recovery, all
center-symmetric equality-wall patterns, and a sharp mixed-sign boundary.
That is a bounded negative search result, not proof that no such source exists.
Scores below are therefore deliberately conservative.

### 3. Discovery lanes, finalists, and killed collisions

No lane retained more than two proof-credible finalists.

| lane | candidate | proof status | disposition |
|---|---|---:|---|
| fixed compactification | generic eigenvalue-gap fan stabilization | credible | KILL: Jonsson--Wulcan and Lin--Wulcan already own the stabilization problem |
| fixed compactification | forward paired-TN blocks on \((\mathbf P^1)^{2n}\) | exact | MERGE: forward same-sign stability alone collides with Lin--Wulcan Example 3.4 |
| fixed compactification | forward **and inverse** paired-TN blocks on the same \(X\) | exact | FINALIST and selected |
| exact degrees | absolute-compound formula for arbitrary monomial maps | known | KILL: Lin Theorem 4.1 |
| exact degrees | scalar minimal recurrence for degree growth | fragile | KILL: Bedford--Kim/Hasselblatt--Propp collision and unjustified minimality |
| exact degrees | block coefficient product for every codimension and signed time | exact | FINALIST and merged |
| generating series | rationality/holonomicity for arbitrary toric maps | broad | KILL: recent Nguyen work and known nonrecurrence boundaries |
| generating series | one-sided Cayley--Hamilton annihilators | exact | RETAIN only as a consequence, never as novelty |
| spectra | reciprocal/palindromic symplectic dynamical spectrum | standard | KILL as headline |
| spectra | arbitrary reciprocal-polynomial realization | plausible | KILL: Ackermann/Salem literature and reserved Paper30 scope |
| spectra | ordered canonical parameter recovery plus equality-wall design | exact | FINALIST and merged |
| sign geometry | TN is necessary and sufficient for fixed-\(X\) stability | false/overbroad | KILL: necessity is neither true nor proved |
| sign geometry | mixed-sign \(SL_2(\mathbf Z)\) cancellation example | exact | RETAIN only as sharpness evidence |
| sign geometry | classification of all sign-regular symplectic matrices | potentially strong | PAUSE: proof confidence below 5/10 and far outside this paper |
| Salem obstruction | one quartic Salem central wall with other codimensions eventually stable | exact from known theorems | RUNNER-UP, then KILL: novelty only 7.3--7.5 and not a fixed all-\(k\) model |
| Salem obstruction | arbitrary Salem/Pisot entropy realization | literature-heavy | KILL: Ackermann, Reschke, Dang--Herrig, and Sugimoto collisions |

The selected candidate is narrower than the paused classification and stronger
than the killed forward-only statement.  Its proof is hand-derived and needs
no experiment or computer algebra.

### 4. Primary-source collision table

| source | exact contribution that must be credited or avoided |
|---|---|
| C. Favre, *Les applications monomiales en deux dimensions*, Michigan Math. J. 51 (2003), 467--475, DOI `10.1307/mmj/1070919553` | toric surface stabilization and failure background |
| B. Hasselblatt and J. Propp, *Degree-growth of monomial maps*, ETDS 27 (2007), 1375--1397, DOI `10.1017/S0143385707000168`, with corrigendum DOI `10.1017/S0143385707000685` | monomial degree growth, entropy, and failure of constant-coefficient recurrence |
| E. Bedford and K. Kim, *Linear recurrences in the degree sequences of monomial mappings*, ETDS 28 (2008), 1369--1375, DOI `10.1017/S0143385708000242` | recurrence/eigenvalue boundary |
| F. M. Dopico and C. R. Johnson, *Parametrization of the Matrix Symplectic Group and Applications*, SIAM J. Matrix Anal. Appl. 31 (2009), 650--673, DOI `10.1137/060678221` | standard-grouped-\(J\) TN symplectic classification; coordinate-order hard collision |
| M. Jonsson and E. Wulcan, *Stabilization of monomial maps*, Michigan Math. J. 60 (2011), 629--660, DOI `10.1307/mmj/1320763052` | fan refinement and \(1\)-stability |
| R. Ackermann, *Achievable spectral radii of symplectic Perron--Frobenius matrices*, New York J. Math. 17 (2011), 683--697 | integral symplectic Perron spectral realizations |
| C. Favre and E. Wulcan, *Degree growth of monomial maps and McMullen's polytope algebra*, Indiana Univ. Math. J. 61 (2012), 493--524, DOI `10.1512/iumj.2012.61.4555` | all dynamical degrees via mixed volumes/universal toric cohomology |
| J.-L. Lin, *Pulling back cohomology classes and dynamical degrees of monomial maps*, Bull. Soc. Math. France 140 (2012), 533--549, DOI `10.24033/bsmf.2635` | Theorem 4.1 gives absolute-minor pullbacks on \((\mathbf P^1)^d\); also the eigenvalue-modulus formula for \(\delta_k\) |
| J.-L. Lin, *Algebraic stability and degree growth of monomial maps*, Math. Z. 271 (2012), 293--311, DOI `10.1007/s00209-011-0864-0` | algebraic-stability criteria and polynomial-map cases on product compactifications |
| P. Reschke, *Salem Numbers and Automorphisms of Complex Surfaces*, Math. Res. Lett. 19 (2012), 475--482, DOI `10.4310/MRL.2012.v19.n2.a18` | Salem entropy realization collision |
| J.-L. Lin and E. Wulcan, *Stabilization of monomial maps in higher codimension*, Ann. Inst. Fourier 64 (2014), 2127--2146, DOI `10.5802/aif.2906` | decisive collision: Lemma 3.2/Example 3.4 already turn same-sign minors into \(k\)-stability; equality/gap and nonrecurrence boundaries |
| J. Blanc, *Symplectic birational transformations of the plane*, Osaka J. Math. 50 (2013), 573--590, DOI `10.18910/25084` | broad symplectic-Cremona claims are not new |
| J. Diller and J.-L. Lin, *Rational surface maps with invariant meromorphic two-forms*, Math. Ann. 364 (2016), 313--352, DOI `10.1007/s00208-015-1211-2` | birational maps preserving logarithmic/meromorphic two-forms |
| J. Blanc and S. Cantat, *Dynamical degrees of birational transformations of projective surfaces*, JAMS 29 (2016), 415--471, DOI `10.1090/jams831` | surface dynamical-degree and Salem/Pisot spectrum background |
| N.-B. Dang and R. Ramadas, *Dynamical invariants of monomial correspondences*, ETDS 41 (2021), 2000--2015, DOI `10.1017/etds.2020.32` | dynamical degrees and strict log-concavity for monomial correspondences |
| N.-B. Dang and T. Herrig, *Dynamical degrees of automorphisms on abelian varieties*, Adv. Math. 395 (2022), 108082, DOI `10.1016/j.aim.2021.108082` | classification/realization collision for abelian-variety spectra |
| J. Diller and R. Roeder, *Equidistribution without stability for toric surface maps*, Comment. Math. Helv. 101 (2026), 115--192, DOI `10.4171/CMH/595` | current adjacent result: log-volume preservation does not imply a stable toric model |
| Q.-K. Nguyen, *On the generating series of the degree sequence*, Math. Ann. 396 (2026), DOI `10.1007/s00208-026-03517-2`, arXiv:`2510.06142v2` | current degree-series collision: natural boundaries and non-holonomicity |

Also checked as recent scope controls were Loginov--Zhang,
arXiv:`2410.05036`, Sugimoto, J. Algebra 682 (2025), 413--443, DOI
`10.1016/j.jalgebra.2025.06.009`, and Oh, arXiv:`2505.13288v3`.
None was used to claim an exact collision where only adjacency was established.

### 5. Exact ordered setup

Fix \(n\geq1\), \(d=2n\), the torus
\[
 T=(\mathbf C^*)^{2n},
\]
and the **interleaved paired order**
\[
 (x_1,y_1,x_2,y_2,\ldots,x_n,y_n).                         \tag{29.1}
\]
Every matrix minor, toric divisor basis, and symplectic form below uses this
same order.  For an integer matrix \(M=(m_{ij})\), freeze the row-exponent
convention
\[
 f_M(z)_i=\prod_{j=1}^{d}z_j^{m_{ij}},
 \qquad f_M\circ f_N=f_{MN}.                               \tag{29.2}
\]

Let
\[
 J_2=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
 \qquad J_{\rm pair}=\bigoplus_{i=1}^nJ_2,                 \tag{29.3}
\]
and choose integers
\[
 q_1\geq q_2\geq\cdots\geq q_n\geq1.                    \tag{29.4}
\]
Define
\[
 B(q)=\begin{pmatrix}q&1\\q-1&1\end{pmatrix},
 \qquad A_{\boldsymbol q}=\bigoplus_{i=1}^nB(q_i).        \tag{29.5}
\]
Thus, pair by pair,
\[
 f_{\boldsymbol q}(x_i,y_i)
   =(x_i^{q_i}y_i,\;x_i^{q_i-1}y_i).                       \tag{29.6}
\]
The determinant of every block is one and
\[
 A_{\boldsymbol q}^{\mathsf T}J_{\rm pair}
 A_{\boldsymbol q}=J_{\rm pair}.                          \tag{29.7}
\]
Consequently this is a birational torus automorphism preserving the
log-symplectic form
\[
 \omega=\sum_{i=1}^n d\log x_i\wedge d\log y_i.           \tag{29.8}
\]
No claim is made that its rational extension is a morphism, or that
\(X=(\mathbf P^1)^{2n}\) carries a global nondegenerate holomorphic
symplectic form preserved everywhere.

Let \(h_1,\ldots,h_d\) be the coordinate hyperplane classes of
\(X=(\mathbf P^1)^d\), let \(h_I=\prod_{i\in I}h_i\), and set
\[
 H=h_1+\cdots+h_d.                                         \tag{29.9}
\]
Lin's product-compactification formula says that, in the \(h_I\) basis, the
pullback for \(f_M\) on \(H^{k,k}(X)\) is the entrywise absolute \(k\)-th
compound
\[
 \mathcal P_k(M)=\bigl(|\det M_{I,J}|\bigr)_{|I|=|J|=k},   \tag{29.10}
\]
up to the one fixed transpose produced by choosing column rather than row
cohomology coordinates.  That transpose is retained consistently and changes
none of the power, entry-sum, or spectral statements below.

### 6. Total nonnegativity and the exact stability bridge

For \(q\geq1\), all entries of \(B(q)\) are nonnegative and its only
two-by-two minor is one; hence \(B(q)\) is totally nonnegative.  More is needed
than entrywise nonnegativity for the direct sum.  In the contiguous paired
order, a minor of \(A_{\boldsymbol q}\) is zero unless it selects the same
number of rows and columns from every block.  In the nonzero case, no block
permutation is required and the minor is the unsigned product of the selected
block minors.  Therefore \(A_{\boldsymbol q}\) is totally nonnegative.
Cauchy--Binet makes every \(A_{\boldsymbol q}^m\), \(m\geq0\), totally
nonnegative and gives
\[
 C_k(A_{\boldsymbol q}^m)=C_k(A_{\boldsymbol q})^m.         \tag{29.11}
\]
Taking absolute values does nothing, so (29.10)--(29.11) prove
\[
 (f_{\boldsymbol q}^m)^*=(f_{\boldsymbol q}^*)^m
 \quad\hbox{on }H^{k,k}(X),
 \quad m\geq0,\quad0\leq k\leq d.                        \tag{29.12}
\]
This forward implication is an application of Lin--Wulcan's same-sign-minor
criterion, not a new theorem by itself.

For the inverse, put
\[
 E=\operatorname{diag}(1,-1),\quad
 S=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
 \widetilde B(q)=\begin{pmatrix}1&1\\q-1&q\end{pmatrix}.
                                                                    \tag{29.13}
\]
Then
\[
 B(q)^{-1}=E\widetilde B(q)E,
 \qquad \widetilde B(q)=S B(q)^{\mathsf T}S.               \tag{29.14}
\]
The matrix \(\widetilde B(q)\) is also TN.  With
\(E_0=\bigoplus_iE\) and
\(\widetilde A=\bigoplus_i\widetilde B(q_i)\),
\[
 A_{\boldsymbol q}^{-m}=E_0\widetilde A^mE_0.              \tag{29.15}
\]
The two diagonal compound sign matrices in (29.15) disappear after
entrywise absolute value, while \(\widetilde A^m\) is TN.  Hence
\[
 (f_{\boldsymbol q}^{-m})^*=((f_{\boldsymbol q}^{-1})^*)^m
 \quad\hbox{on every }H^{k,k}(X),\quad m\geq0.             \tag{29.16}
\]
Equations (29.12) and (29.16) mean that \(f\) and \(f^{-1}\) are separately
stable in every codimension on the same fixed \(X\).  They do **not** assert a
cohomological \(\mathbf Z\)-representation across mixed signs;
\((f^{-1})^*\) need not equal \((f^*)^{-1}\).

### 7. Exact all-time compound-degree polynomial

For \(m\in\mathbf Z\), interpret \(f_{\boldsymbol q}^m\) as the rational
extension of the torus map with exponent matrix \(A_{\boldsymbol q}^m\), and
define
\[
 D_{k,m}:=
 \frac{((f_{\boldsymbol q}^m)^*H^k)\cdot H^{d-k}}
      {k!(d-k)!}.                                           \tag{29.17}
\]
This is the factorial-normalized mixed degree, not the normalization by
\(H^d=d!\).  Since
\[
 H^k=k!\sum_{|I|=k}h_I,                                    \tag{29.18}
\]
\(D_{k,m}\) is precisely the sum of all absolute \(k\)-minors of
\(A_{\boldsymbol q}^m\).

For \(r\geq0\), let \(s_i(r)\) be the sum of the four entries of
\(B(q_i)^r\).  Cayley--Hamilton gives
\[
 \begin{split}
 s_i(0)&=2,\\
 s_i(1)&=2q_i+1,\\
 s_i(r+2)&=(q_i+1)s_i(r+1)-s_i(r).
 \end{split}                                                \tag{29.19}
\]
Because \(\widetilde B(q_i)^r=S(B(q_i)^r)^{\mathsf T}S\), its entry sum is
the same \(s_i(r)\).  Within a block, selecting zero, one, or two rows and
columns contributes respectively \(1\), \(s_i(r)t\), or \(t^2\).  Independent
block selection therefore proves the exact identity
\[
 \boxed{\quad
   \sum_{k=0}^{2n}D_{k,m}t^k
     =\prod_{i=1}^n\bigl(1+s_i(|m|)t+t^2\bigr),
   \qquad m\in\mathbf Z.\quad}                              \tag{29.20}
\]

At time zero this gives
\[
 \sum_kD_{k,0}t^k=(1+t)^{2n},
 \qquad D_{k,0}=\binom{2n}{k},                              \tag{29.21}
\]
which is the required normalization check.  Every one-sided degree sequence
also has a Cayley--Hamilton annihilator through its stable compound matrix;
no minimal-recurrence claim is made.

The palindromic local factors and \(|m|\) in (29.20) give
\[
 D_{k,m}=D_{2n-k,m}=D_{k,-m}.                              \tag{29.22}
\]
These symmetries are not claimed as family-specific novelty.  More generally,
for a unimodular \(J_{\rm pair}\)-symplectic exponent matrix, the signed-
permutation identity \(M^{-1}=J_{\rm pair}^{-1}M^{\mathsf T}J_{\rm pair}\)
and Jacobi's complementary-minor identity yield the same absolute-minor
sum dualities.  The family-specific content is the full product (29.20)
combined with the two same-\(X\) stability statements.

### 8. Dynamical spectrum, exact recovery, and equality walls

Define
\[
 \rho_i:=\rho(q_i)
 =\frac{q_i+1+\sqrt{(q_i+1)^2-4}}2.                         \tag{29.23}
\]
Then
\[
 \rho_1\geq\cdots\geq\rho_n\geq1                         \tag{29.24}
\]
and the block eigenvalues are \(\rho_i,\rho_i^{-1}\).  Lin's monomial
dynamical-degree theorem gives
\[
 \boxed{\quad
 \delta_k(f_{\boldsymbol q})
   =\prod_{i=1}^{\min(k,,2n-k)}\rho_i,
 \qquad 0\leq k\leq2n.\quad}                              \tag{29.25}
\]
This product formula itself is cited prior art.  What it enables here is an
exact inverse theorem inside the frozen canonical family.  For
\(1\leq i\leq n\),
\[
 r_i:=\frac{\delta_i}{\delta_{i-1}}=\rho_i,
 \qquad
 \boxed{q_i=r_i+r_i^{-1}-1}.                               \tag{29.26}
\]
Thus the complete dynamical-degree spectrum recovers the ordered integer
parameter list, including multiplicities.  It does not classify arbitrary
symplectic exponent matrices or realize an arbitrary reciprocal sequence.

For \(1\leq k<n\),
\[
 \frac{\delta_k^2}{\delta_{k-1}\delta_{k+1}}
   =\frac{\rho_k}{\rho_{k+1}},                              \tag{29.27}
\]
so equality occurs exactly when \(q_k=q_{k+1}\).  At the center,
\[
 \frac{\delta_n^2}{\delta_{n-1}\delta_{n+1}}=\rho_n^2,    \tag{29.28}
\]
so the central wall occurs exactly when \(q_n=1\).  The remaining walls are
the reflections \(k\leftrightarrow2n-k\).

The \(q=1\) case is printed separately because it is unipotent, not a
semisimple multiplicity:
\[
 B(1)^r=\begin{pmatrix}1&r\\0&1\end{pmatrix},
 \qquad s(r)=r+2.                                           \tag{29.29}
\]
It satisfies (29.19)--(29.25) with \(\rho=1\), including polynomial growth.
No formula dividing by \(\rho-\rho^{-1}\) is used at this boundary.

Now let \(W\subseteq\{1,\ldots,2n-1\}\) be any center-symmetric set:
\[
 k\in W\quad\Longleftrightarrow\quad2n-k\in W.            \tag{29.30}
\]
Choose
\[
 q_n=\begin{cases}1,&n\in W,\\2,&n\notin W,\end{cases}    \tag{29.31}
\]
and, for \(i=n-1,n-2,\ldots,1\), set
\[
 q_i=\begin{cases}
 q_{i+1},&i\in W,\\
 q_{i+1}+1,&i\notin W.
 \end{cases}                                                \tag{29.32}
\]
Then the log-concavity equality positions are exactly \(W\).  This realizes
every allowed wall pattern and no non-center-symmetric pattern, which is
forbidden by (29.25).

### 9. Coordinate-order collision with standard symplectic TN theory

Total nonnegativity is not invariant under arbitrary coordinate permutation.
Dopico--Johnson use grouped coordinates and
\[
 J_{\rm std}=\begin{pmatrix}0&I_n\\-I_n&0\end{pmatrix}.
\]
Their Theorem 5.6 restricts TN symplectic matrices in that standard order to
positive diagonal form when \(n>1\).  There is no contradiction.  Perfectly
shuffle two paired blocks from
\((x_1,y_1,x_2,y_2)\) to \((x_1,x_2,y_1,y_2)\).  The exponent matrix becomes
\[
 \widehat A=
 \begin{pmatrix}
 q_1&0&1&0\\
 0&q_2&0&1\\
 q_1-1&0&1&0\\
 0&q_2-1&0&1
 \end{pmatrix}.                                             \tag{29.33}
\]
It is \(J_{\rm std}\)-symplectic and entrywise nonnegative, but the minor in
rows \(\{1,2\}\) and columns \(\{2,3\}\) equals \(-q_2\).  Hence it is not
TN in the grouped order.  The theorem is always stated using the interleaved
ordered exponent basis, divisor basis, and \(J_{\rm pair}\) together.

Coordinate permutation is nevertheless a toric automorphism of \(X\), so the
same-\(X\) stability conclusion transports by conjugacy.  What does not
transport is the literal label “TN in standard grouped order.”

### 10. Sharp mixed-sign failure and other sanity checks

Symplecticity alone does not remove absolute-compound cancellation.  Take
\[
 R=\begin{pmatrix}3&1\\-1&0\end{pmatrix}\in SL_2(\mathbf Z). \tag{29.34}
\]
Then
\[
 R^2=\begin{pmatrix}8&3\\-3&-1\end{pmatrix},
 \qquad
 |R^2|=\begin{pmatrix}8&3\\3&1\end{pmatrix},
 \qquad
 |R|^2=\begin{pmatrix}10&3\\3&1\end{pmatrix}.             \tag{29.35}
\]
Thus \((f_R^2)^*\ne(f_R^*)^2\) on \(H^{1,1}((\mathbf P^1)^2)\).  This proves
only that determinant one/log-symplecticity is insufficient; it does not say
every mixed-sign matrix is unstable or that TN is necessary.

Literal small checks, used only to catch indexing errors, are:

1. \(n=1,q=2\): \(B^2=\left(\begin{smallmatrix}5&3\\3&2\end{smallmatrix}\right)\),
   so \(s(2)=13\) and the degree polynomial is \(1+13t+t^2\).
2. \(n=2,(q_1,q_2)=(3,2),m=1\): the local sums are \(7,5\), so
   \((1+7t+t^2)(1+5t+t^2)=1+12t+37t^2+12t^3+t^4\).
3. \(m=0\): (29.21) recovers the identity-map intersection numbers.
4. \(q=1\): (29.29) verifies the repeated-root recurrence directly.
5. If \(\rho=2\), then \(\rho+\rho^{-1}-1=3/2\), so an arbitrary positive
   reciprocal/log-concave spectrum need not come from integer canonical
   parameters; (29.26) is an internal recovery theorem, not a universal
   realization theorem.

No finite check is evidence for the theorem; each displayed claim has the
symbolic proof spine above.

### 11. Direct Batch07 collision matrix

| prior or reserved paper | object already owned | noncollision rule for Paper29 |
|---|---|---|
| Papers12--13 | Hénon residue and primitive periodic-cycle covers | no periodic-orbit residue, cover, or multiplier statement |
| Papers14 and 16 | finite-rank torus escape/survival bounds | no rational-point or finite-rank multiplicative-group counting |
| Papers15 and 18 | Hénon trace fibers and marked scalar boundary | \(\delta\)-parameter recovery is cohomological and not a periodic trace morphism |
| Papers17 and 19 | shift-like torus-coset decay and translate gcd obstruction | no survivor variety, translate classification, or support gcd |
| Papers20--23 | affine Hamiltonian shear degree matrices and spectral collapse/escape | the maps here are torus monomial birational maps and the degrees are all cohomological compounds on a fixed compactification |
| Papers24--26 | Newton selector exchange, support-rank Perron degree, and bidirectional Newton envelopes | no Newton wall, support selector, tropical carry, or polynomial-shear ordinary degree theorem |
| Paper27 | positive Newton translation and finite-wall phase reciprocity | no translation phase, Newton support, or phase-reciprocity claim; (29.22) is general symplectic minor duality |
| Paper28 | primitive selector-cycle normal-fan monodromy | no prescribed selector word, normal-fan coding, monodromy decoder, or primitive cycle |
| Paper29 | fixed product toric cohomology and canonical paired-TN family | owns only the exact package frozen here |
| reserved Paper30 | signed block-symplectic transfer-product reciprocal characteristic-polynomial converse | Paper29 makes no arbitrary reciprocal-polynomial converse and no transfer-product classification |
| reserved Paper31 | zero-coordinate gradient cancellation | Paper29's one \(2\times2\) mixed-sign counterexample is only a stability boundary, not a cancellation theory |

Every Paper12--28 theorem remains absorbed as prior portfolio context.  No old
result is renamed as a new Paper29 theorem.

### 12. Frozen theorem inventory and proof dependencies

The manuscript may promote exactly the following new theorem package, subject
to formal review:

1. **Two-sided fixed-product stability theorem.**  For the canonical ordered
   paired-TN family, \(f\) and \(f^{-1}\) are each \(k\)-stable for all \(k\)
   on the same \(X=(\mathbf P^1)^{2n}\).
2. **Exact compound-degree enumerator.**  Formula (29.20) gives all normalized
   mixed degrees for all \(k\) and all integer times, including the unipotent
   boundary.
3. **Canonical spectral recovery theorem.**  Formula (29.26) recovers the
   ordered integer parameter tuple from the dynamical-degree spectrum.
4. **Complete equality-wall realization theorem.**  Equations
   (29.30)--(29.32) realize exactly every center-symmetric wall set.
5. **Sharpness proposition.**  Coordinate ordering resolves the
   Dopico--Johnson collision, while (29.34)--(29.35) shows why symplecticity
   without sign coherence is insufficient.

Dependencies that must be cited rather than reproved as original are Lin's
absolute-minor pullback and dynamical-degree theorems, Lin--Wulcan's
same-sign-minor stability criterion, Cauchy--Binet, Cayley--Hamilton, Jacobi
complementary minors, and elementary symplectic reciprocal pairing.

### 13. Explicit anti-claims

This candidate does **not** claim:

- that TN implies fixed-\(X\) stability for the first time;
- that absolute compounds or the monomial \(\delta_k\) formula are new;
- a non-diagonal TN symplectic matrix in the standard grouped-\(J\) order;
- that \(f\) is a morphism or a global holomorphic symplectic automorphism of
  \(X\);
- that stability means absence of indeterminacy;
- that TN is necessary for stability;
- any non-center-symmetric wall realization;
- any formula for an arbitrary ample class rather than the fixed symmetric
  \(H=\sum h_i\);
- a full cohomological \(\mathbf Z\)-action across mixed positive and negative
  times;
- minimal recurrences, scalar word decoding, entropy novelty, Salem/Pisot
  novelty, or arbitrary reciprocal-polynomial realization;
- classification of all symplectic, sign-regular, or torically stable
  matrices;
- any Paper27 Newton-phase, Paper28 selector-monodromy, Paper30 transfer
  converse, or Paper31 zero-gradient theorem; or
- any empirical, numerical, or computer-algebra proof.

### 14. Credible anonymous page-mass plan

References are excluded from the content count.

| section | target content pages |
|---|---:|
| problem, contribution ledger, and anti-claims | 2.5 |
| primary literature and coordinate-order collision | 3.0 |
| toric cohomology and absolute compounds | 3.0 |
| forward and inverse all-codimension stability | 4.5 |
| exact finite-time degree product and recurrences | 4.0 |
| dynamical spectrum and parameter recovery | 3.5 |
| equality-wall theorem including \(q=1\) boundary | 3.0 |
| counterexamples, sharpness, and limitations | 2.5 |
| conclusion | 0.8 |
| **total** | **26.8** |

The range is credibly 25--28 proof-content pages, inside the charter's
[22,30] gate.  Page mass comes from complete proofs, source attribution,
boundary cases, and counterexamples, never spacing, empty displays, oversized
tables, or references.

### 15. V1 author preflight and formal-review boundary

The packet was subjected to two independent read-only preflights: a primary-
literature collision sweep and a line-by-line algebra/cohomology audit.  The
printed corrections fix the mixed-degree normalization, exponent convention,
direct-sum TN bridge, inverse sign conjugacy, \(q\)-ordering, integer recovery
scope, central unipotent wall, coordinate shuffle, and log-symplectic wording.
The author-only census is:

| class | count |
|---|---:|
| Blocker | 0 |
| Major | 0 |
| Minor | 0 |
| Ambiguity | 0 |

Provisional conservative scores are novelty \(7.7/10\), standalone value
\(7.8/10\), proof confidence \(9.2/10\), and 25--28 anonymous proof-content
pages.  The novelty score applies only to the full conjunction, not to any
cited ingredient.  These author scores confer no PASS authority.

Two entirely fresh, mutually blind formal reviewers must independently read
the complete append-only candidate.  R1 must stress current primary sources,
the Lin--Wulcan and Dopico--Johnson collisions, portfolio separation, genuine
standalone value, anti-claims, and page mass.  R2 must rederive the exponent
and pullback conventions, TN direct-sum bridge, forward/inverse stability,
normalization, coefficient product, general symplectic duality boundary,
\(q=1\) Jordan case, spectrum recovery, wall construction, and mixed-sign
counterexample.  Each reviewer may create an artifact only for an unconditional
all-zero PASS.  Paper29 remains unconsumed and no project path is opened by
this author stop.

BATCH07_PAPER29_CANDIDATE_V1_AUTHOR_STOP

## Append-only Paper29 candidate V2 single-index correction packet

Authorization:
`B07-E0219-P29-CANDIDATE-V1-DUAL-FAIL-V2-CORRECTION-AUTHORIZATION`, with
terminal gate `BATCH07_PAPER29_CANDIDATE_V2_CORRECTION_AUTHORIZED`.  Every V1
byte and the V1 author-stop marker remain immutable.  This packet consumes the
sole candidate-revision budget and supersedes exactly one malformed display.

### Sole correction to formula (29.25)

The V1 display accidentally printed `min(k,,2n-k)`.  Its unique corrected
form is
\[
 \boxed{\quad
 \delta_k(f_{\boldsymbol q})
   =\prod_{i=1}^{\min\{k,2n-k\}}\rho_i,
 \qquad 0\leq k\leq2n.\quad}                              \tag{29.25-V2}
\]
Thus the index is the integer \(\min\{k,2n-k\}\), with exactly one separator
between its two arguments.  Formula (29.25-V2) replaces V1 formula (29.25)
wherever the latter is invoked by the parameter-recovery and equality-wall
statements.

No definition, hypothesis, proof step, source attribution, novelty boundary,
score, page plan, example, wall construction, anti-claim, or portfolio
separation changes.  In particular, the \(q=1\) unipotent case and the
restriction to the canonical ordered paired-TN family remain literal.

The corrected V2 author-only census is:

| class | count |
|---|---:|
| Blocker | 0 |
| Major | 0 |
| Minor | 0 |
| Ambiguity | 0 |

Provisional conservative scores remain novelty \(7.7/10\), standalone value
\(7.8/10\), proof confidence \(9.2/10\), and 25--28 anonymous proof-content
pages.  They confer no PASS authority.  Two entirely fresh, mutually blind V2
formal reviewers must assess the complete append-only candidate; neither V1
reviewer may be reused.  Paper29 remains unconsumed and its project remains
absent.

BATCH07_PAPER29_CANDIDATE_V2_AUTHOR_STOP

## Append-only Paper30 candidate V1: reciprocal spectra of signed symmetric transfer words

Authorization: `B07-E0222-P30-CANDIDATE-DISCOVERY-AUTHORIZATION`, with
terminal gate `BATCH07_PAPER30_CANDIDATE_DISCOVERY_AUTHORIZED`.  Every earlier
byte, including both Paper29 author-stop packets, remains immutable.  This is
the sole Paper30 discovery append authorized at this gate.

Candidate ID: `symplectic_transfer_reciprocity_v1`.

Provisional public title:

> **Reciprocal Spectra of Signed Symmetric Transfer Words: A Ring-Uniform
> Two-Factor Converse and Sharp Length Walls**

### 1. Author decision and exact novelty boundary

The candidate is a cautious **GO to two fresh formal reviews**, not a claim of
priority.  Its proposed contribution is only the following conjunction:

1. an exact characteristic-polynomial image theorem for the fixed signed
   two-transfer word \(-T(A)T(-B)\), with both blocks symmetric;
2. a division-free construction over every nonzero commutative coefficient
   ring, with one symmetric block always unimodular;
3. an exact positive signed-transfer length dichotomy \(1/2\) over
   \(\mathbb R\), including repeated-root equality walls;
4. sharp quadratic one-transfer arithmetic criteria over \(\mathbb Q\) and
   \(\mathbb Z\), with strict ring-separation examples; and
5. the ordinary-similarity bridge to a transfer self-adjoint for a unimodular
   metric, together with the precise congruence obstruction to making that
   transfer standard symmetric.

The reciprocal trace reduction, general symplectic realization of reciprocal
polynomials, factorization of matrices into two symmetric factors, companion
Hankel symmetrizers, transfer determinants, and general shear generation are
all treated as prior ingredients.  None is claimed new.  The bounded search
through 2026-08-29 found no primary source stating the five-part conjunction,
but absence from this search is not evidence of global priority.

The conservative author-only scores are:

| criterion | score or range |
|---|---:|
| novelty of the full conjunction only | 7.6 / 10 |
| standalone value after ingredient absorption | 7.8 / 10 |
| proof confidence | 9.5 / 10 |
| credible anonymous proof-content pages | 24--27 |

These scores confer no PASS authority.

### 2. Frozen alphabet, domains, and conventions

Let \(R\) be a nonzero commutative ring with identity and let \(n\geq1\).
All matrices in the ring-level theorem are over \(R\).  Put
\[
 J=\begin{pmatrix}0&-I_n\\ I_n&0\end{pmatrix},
 \qquad
 T(S)=\begin{pmatrix}S&-I_n\\ I_n&0\end{pmatrix}.
 \tag{30.1}
\]
The matrix \(T(S)=U(S)J\) is a standard block transfer and is symplectic when
\(S=S^{\mathsf T}\), where
\[
 U(A)=\begin{pmatrix}I_n&A\\0&I_n\end{pmatrix},
 \qquad
 L(B)=\begin{pmatrix}I_n&0\\B&I_n\end{pmatrix}.
 \tag{30.2}
\]
Both shears are symplectic exactly under the displayed symmetry hypotheses.

A monic polynomial \(p(t)\in R[t]\) of degree \(2n\) is *reciprocal* here
when
\[
 p(t)=t^{2n}p(t^{-1});
 \tag{30.3}
\]
equivalently, its coefficient list is palindromic and its constant term is
one.  Degree is literal, so the zero ring is excluded.  Characteristic
polynomials use \(\chi_M(t)=\det(tI-M)\).

A signed symmetric-transfer word of positive length \(m\) over a field is
\[
 \varepsilon T(S_1)\cdots T(S_m),
 \qquad \varepsilon\in\{I_{2n},-I_{2n}\},
 \qquad S_i=S_i^{\mathsf T}.
 \tag{30.4}
\]
Its length is the number \(m\) of \(T\)-factors; the central sign is not a
factor.  This convention is frozen so that “minimal length” cannot silently
switch between transfers, shears, and composite cells.  A separate statement
below uses the elementary-shear alphabet \(\{U(A),L(B)\}\) and labels it
explicitly.

### 3. Discovery lanes, candidates, and killed collisions

The search used five distinct lanes and retained only one finalist.

| lane | tested candidate | disposition and exact reason |
|---|---|---|
| reciprocal transform and symplectic companions | every reciprocal \(p\) is the characteristic polynomial of some integral symplectic companion | **killed as headline**: the trace reduction and integral symplectic realization are already explicit in prior work, most recently also in Rüd--Zhang, Lemma 6.11 |
| one standard symmetric transfer | every reciprocal \(p\) equals \(\chi_{T(S)}\) over its coefficient field | **false**: it would make the reduced polynomial the characteristic polynomial of a symmetric matrix; \(x^2+1\) fails already over \(\mathbb R\) |
| positive or totally nonnegative factors | every reciprocal \(p\) has the two-transfer realization with positive-definite symmetric blocks | **false**: a product of two positive-definite symmetric matrices has real positive spectrum, contradicting arbitrary reduced polynomials |
| general symmetric factorization over rings | every integral matrix is a product of two integral symmetric matrices | **false**: Taussky's integral factorization work gives genuine arithmetic/ideal-class obstructions |
| two factors both unimodular | the final construction can always make both symmetric blocks invertible | **false** in the constructed family unless \(p(1)\) is a unit; the second block is invertible exactly when the shifted companion is |
| fixed signed two-transfer word | ring-uniform converse plus real and arithmetic one-transfer walls | **retained finalist**, subject to two fresh formal reviews |

The field-only version was also considered and discarded as strictly weaker:
the quotient-algebra construction below is division-free and its Hankel form
has determinant \(\pm1\), so the natural statement is over a commutative
ring.  Conversely, the Witt and real-rooted minimality results are not
silently extended to arbitrary rings.

### 4. Primary-source collision matrix

The strongest verified ingredient collisions are disclosed rather than
hidden.

| source | verified overlap | what remains outside that source |
|---|---|---|
| Margalit--Spallone, *A homological recipe for pseudo-Anosovs*, MRL 14 (2007), DOI [10.4310/MRL.2007.v14.n5.a12](https://doi.org/10.4310/MRL.2007.v14.n5.a12) | the map \(q\mapsto t^{\deg q}q(t+t^{-1})\) onto monic palindromic polynomials | fixed symmetric transfer-word factors, ring-uniform factor construction, and length/arithmetic walls |
| Rüd--Zhang, *Jacquet--Rallis Transfer for Parahoric Functions over Ramified Quadratic Extensions*, Lemma 6.11, [author PDF](https://math.mit.edu/~rud/2025/papers/transfer.pdf) | palindromic trace reduction and an explicit symplectic companion, with an integral construction | realization specifically as \(-T(A)T(-B)\) with symmetric \(A,B\), and minimal signed-transfer length |
| Ackermann, *Achievable spectral radii of symplectic Perron--Frobenius matrices*, NYJM 17 (2011), [official article](https://nyjm.albany.edu/j/2011/17-29.html) | integral symplectic realizations used in spectral-radius constructions | the fixed transfer word and exact image/length theorem |
| Frobenius' theorem as presented by Bosch, *The Factorization of a Square Matrix into Two Symmetric Matrices*, Amer. Math. Monthly 93 (1986), DOI [10.1080/00029890.1986.11971855](https://doi.org/10.1080/00029890.1986.11971855), and Bosch, SIAM Review 29 (1987), DOI [10.1137/1029077](https://doi.org/10.1137/1029077) | every matrix over a field is a product of two symmetric matrices | arbitrary commutative rings are not covered; the special unimodular companion symmetrizer and transfer consequences are not the stated object |
| Dopico--Uhlig, *Computing Matrix Symmetrizers, Part 2*, LAA 504 (2016), DOI [10.1016/j.laa.2015.06.031](https://doi.org/10.1016/j.laa.2015.06.031) | Frobenius symmetrizers over fields and computational constructions | division-free ring theorem and reciprocal transfer length |
| Taussky, *The factorization of an integral matrix into a product of two integral symmetric matrices I*, Acta Arith. 24 (1973), DOI [10.4064/aa-24-2-151-156](https://doi.org/10.4064/aa-24-2-151-156), and Part II, DOI [10.1002/cpa.3160260526](https://doi.org/10.1002/cpa.3160260526) | integral factorization is not automatic and has arithmetic obstructions | the standard companion has a special anti-unitriangular Hankel symmetrizer, which bypasses the general obstruction |
| Bender, *Characteristic Polynomials of Symmetric Matrices*, Pacific J. Math. 25 (1968), [publisher PDF](https://msp.org/pjm/1968/25-3/pjm-v25-n3-p03-p.pdf) | arithmetic/congruence conditions for polynomials to be characteristic polynomials of symmetric matrices | composition with the two-transfer converse and the resulting word-length stratification |
| Luo--Hill, *Companion matrices and their relations to Toeplitz and Hankel matrices*, Special Matrices 3 (2015), DOI [10.1515/spma-2015-0021](https://doi.org/10.1515/spma-2015-0021) | companion--Hankel intertwiners and structured identities | the claimed novelty is not the intertwiner alone |
| Molinari, *Transfer matrices and tridiagonal-block Hamiltonians*, J. Phys. A 30 (1997), DOI [10.1088/0305-4470/30/3/021](https://doi.org/10.1088/0305-4470/30/3/021), and *Determinants of block tridiagonal matrices*, LAA 429 (2008), DOI [10.1016/j.laa.2008.06.015](https://doi.org/10.1016/j.laa.2008.06.015) | transfer/block-determinant spectral duality | prescribed reciprocal characteristic polynomials in the frozen signed length-two family and sharp minimal length |
| De Terán--Dopico--Mackey--Perović, *Quadratic realizability of palindromic matrix polynomials*, LAA 567 (2019), DOI [10.1016/j.laa.2019.01.003](https://doi.org/10.1016/j.laa.2019.01.003) | broad structured realizability of quadratic palindromic matrix polynomials | no direct statement located for the frozen \(-T(A)T(-B)\) word and its \(1/2\) scalar characteristic-polynomial length wall |
| Jin--Tang--Zhu, *Unit Triangular Factorization of the Matrix Symplectic Group*, SIMAX 41 (2020), DOI [10.1137/19M1308839](https://doi.org/10.1137/19M1308839), and Jin--Lin--Xiao, LAA 650 (2022), DOI [10.1016/j.laa.2022.06.009](https://doi.org/10.1016/j.laa.2022.06.009) | general symplectic unit-triangular generation and optimal factor counts | the present statement prescribes only a characteristic polynomial and achieves two factors in a much smaller inverse-image problem |

Exact and near-exact queries included variants of `-T(A)T(-B)`,
`T(A)T(-B)`, “product of two transfer matrices” with
reciprocal/palindromic and symmetric, “reciprocal characteristic polynomial”
with transfer realization, companion/Hankel symmetrizers, block-Jacobi inverse
spectra, symmetric characteristic-polynomial arithmetic, and quadratic
palindromic realizability.  Publisher, DOI, author, journal, and arXiv pages
were used where accessible.  The search was bounded rather than exhaustive:
unindexed books, non-digitized older literature, non-English terminology, and
paywalled full texts can still contain a collision.  The manuscript must say
“we are not aware of a direct treatment” rather than “first”.

### 5. Reciprocal trace reduction over a ring

Write
\[
 p(t)=t^{2n}+c_1t^{2n-1}+\cdots+c_{n-1}t^{n+1}
      +c_nt^n+c_{n-1}t^{n-1}+\cdots+c_1t+1.
 \tag{30.5}
\]
Define integral polynomials
\[
 P_0(z)=2,\qquad P_1(z)=z,\qquad
 P_k(z)=zP_{k-1}(z)-P_{k-2}(z).
 \tag{30.6}
\]
They satisfy \(P_k(t+t^{-1})=t^k+t^{-k}\).  Hence
\[
 r(z)=P_n(z)+c_1P_{n-1}(z)+\cdots+c_{n-1}P_1(z)+c_n
 \tag{30.7}
\]
is monic of degree \(n\), and, with
\[
 q(x)=r(x+2),
 \tag{30.8}
\]
one has
\[
 \boxed{p(t)=t^nq(t+t^{-1}-2).}
 \tag{30.9}
\]
The construction uses integer coefficients only.  Uniqueness follows because
a nonzero leading term \(a_dx^d\) maps to a Laurent polynomial whose
coefficient of \(t^d\) is \(a_d\); thus the substitution
\(R[x]\to R[t,t^{-1}]\), \(x\mapsto t+t^{-1}-2\), is injective even when
\(R\) has zero divisors.  This proves existence and uniqueness without
assuming that two is invertible and without excluding characteristic two.

The polynomial \(q\) in (30.9) is called the *shifted reduced polynomial*.
This frozen choice prevents a later unnoticed switch between
\(t+t^{-1}\) and \(t+t^{-1}-2\).

### 6. Exact two-shear and two-transfer determinant identity

For symmetric \(A,B\in M_n(R)\), put
\[
 M(A,B)=U(A)L(B)
 =\begin{pmatrix}I_n+AB&A\\B&I_n\end{pmatrix}.
 \tag{30.10}
\]
Direct multiplication also gives the signed-transfer identity
\[
 \boxed{M(A,B)=-T(A)T(-B).}
 \tag{30.11}
\]
Consequently \(M(A,B)\in\operatorname{Sp}_{2n}(R)\).

Set \(s=t-1\).  A Schur-complement calculation in the universal polynomial
domain, temporarily localizing at \(s\), gives
\[
\begin{aligned}
 \chi_{M(A,B)}(t)
 &=\det\begin{pmatrix}sI_n-AB&-A\\-B&sI_n\end{pmatrix}\\
 &=\det\bigl(s^2I_n-(s+1)AB\bigr).
\end{aligned}
 \tag{30.12}
\]
Both sides are polynomials over the universal integer coefficient ring, so
the identity descends by specialization to every commutative \(R\); no
inverse of \(t-1\) is assumed in the theorem.  Therefore
\[
 \boxed{
 \chi_{M(A,B)}(t)
  =\det\bigl((t-1)^2I_n-tAB\bigr)
  =t^n\det\bigl((t+t^{-1}-2)I_n-AB\bigr).
 }
 \tag{30.13}
\]

This already proves the necessity half for the frozen family: its
characteristic polynomial is a monic reciprocal polynomial of degree \(2n\),
and its unique shifted reduced polynomial is \(\chi_{AB}\).

### 7. Division-free companion factorization

Let
\[
 q(x)=x^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0
 \tag{30.14}
\]
and let \(C=C_q\) be the column Frobenius companion: it has ones on the
subdiagonal and last column
\((-a_0,-a_1,\ldots,-a_{n-1})^{\mathsf T}\).  Equivalently, \(C\) is
multiplication by \(x\) on
\[
 \mathcal A=R[x]/(q)
 \tag{30.15}
\]
in the ordered basis \(1,x,\ldots,x^{n-1}\).

Let \(\lambda:\mathcal A\to R\) extract the coefficient of \(x^{n-1}\) in
the unique standard remainder, and define
\[
 H_{ij}=\lambda(x^{i+j}),\qquad 0\leq i,j<n.
 \tag{30.16}
\]
Equivalently, with \(\eta_m=\lambda(x^m)\),
\[
 \eta_0=\cdots=\eta_{n-2}=0,qquad \eta_{n-1}=1,
 \tag{30.17}
\]
and for \(m\geq n\),
\[
 \eta_m=-a_{n-1}\eta_{m-1}-\cdots-a_0\eta_{m-n}.
 \tag{30.18}
\]
Thus \(H=(\eta_{i+j})\) is symmetric.  Commutativity in \(\mathcal A\)
shows
\[
 \lambda((xf)g)=\lambda(f(xg)),
 \qquad C^{\mathsf T}H=HC.
 \tag{30.19}
\]
The entries with \(i+j<n-1\) vanish and those with \(i+j=n-1\) equal one.
After reversing the columns of \(H\), the matrix is triangular with diagonal
all one.  Hence
\[
 \boxed{\det H=(-1)^{n(n-1)/2}.}
 \tag{30.20}
\]
In particular, \(H\) is unimodular over every \(R\), including rings with
zero divisors.

Define
\[
 \boxed{A=H^{-1},\qquad B=HC.}
 \tag{30.21}
\]
Then \(A=A^{\mathsf T}\), while (30.19) gives
\[
 B^{\mathsf T}=C^{\mathsf T}H=HC=B,
 \qquad AB=C.
 \tag{30.22}
\]
All entries are integral polynomial expressions in the coefficients of
\(q\); there is no field extension, division by a coefficient, localization,
root choice, or rational canonical-form choice.

The second factor is also unimodular exactly on the sharp unit wall
\[
 B\in\operatorname{GL}_n(R)
 \Longleftrightarrow C\in\operatorname{GL}_n(R)
 \Longleftrightarrow q(0)\in R^\times
 \Longleftrightarrow p(1)\in R^\times.
 \tag{30.23}
\]
Only \(A\) is asserted to be unconditionally unimodular.

### 8. Main ring-level converse

Combining (30.9), (30.13), and (30.21) yields the proposed headline theorem.

> **Theorem A (ring-uniform signed two-transfer converse).**
> Let \(R\) be a nonzero commutative ring with identity.  For every monic
> reciprocal \(p(t)\in R[t]\) of degree \(2n\), form its unique shifted
> reduced polynomial \(q\) by (30.9), its companion \(C_q\), and the
> unimodular symmetric Hankel matrix \(H_q\) in (30.16).  Then
> \[
>  A=H_q^{-1},\qquad B=H_qC_q
> \]
> are symmetric, \(A\) is unimodular, and
> \[
>  \boxed{
>  -T(A)T(-B)=U(A)L(B)\in\operatorname{Sp}_{2n}(R),
>  \qquad
>  \chi_{-T(A)T(-B)}(t)=p(t).
>  }
> \tag{30.24}
> \]
> Conversely, every matrix in this frozen signed two-transfer family has the
> reciprocal characteristic polynomial (30.13), whose shifted reduced
> polynomial is exactly \(\chi_{AB}\).

The theorem is a polynomial-image characterization, not a bijection of
matrix pairs: many different symmetric pairs \((A,B)\) can have the same
\(\chi_{AB}\).  For \(R=\mathbb Z\), the construction produces literal
integer symmetric blocks.  This special companion factorization does not
contradict Taussky's obstructions for arbitrary integral matrices.

### 9. One signed transfer and the exact real length wall

For any symmetric \(S\), another block determinant gives
\[
 \chi_{T(S)}(t)
 =\det(t^2I_n-tS+I_n)
 =t^n\det((t+t^{-1})I_n-S).
 \tag{30.25}
\]
Likewise,
\[
 \chi_{-T(S)}(t)=t^n\det((t+t^{-1})I_n+S).
 \tag{30.26}
\]
Comparing with (30.9) proves the exact one-step criterion:
\[
 \boxed{
 p\text{ has a one-factor signed symmetric-transfer realization over }R
 \Longleftrightarrow
 q\text{ is the characteristic polynomial of an }R\text{-symmetric matrix}.
 }
 \tag{30.27}
\]
Indeed, for the positive sign take \(S=D+2I_n\) when \(\chi_D=q\); for the
negative sign take \(S=-D-2I_n\).  The two signs therefore have the same
characteristic-polynomial image.

Over \(\mathbb R\), the spectral theorem makes (30.27) a closed and complete
criterion: a monic real polynomial is the characteristic polynomial of a
real symmetric matrix exactly when all its roots are real, with
multiplicity.  Theorem A supplies two factors in every other case.  Thus:

> **Theorem B (sharp positive signed-transfer length over \(\mathbb R\)).**
> For a monic real reciprocal \(p\) of degree \(2n\), let \(q\) be fixed by
> (30.9), and let \(\ell_{\mathbb R}(p)\) be the least positive length in the
> alphabet (30.4).  Then
> \[
>  \boxed{
>  \ell_{\mathbb R}(p)=
>  \begin{cases}
>   1,&q\text{ is real-rooted},\\
>   2,&q\text{ has a nonreal root}.
>  \end{cases}}
> \tag{30.28}
> \]

Repeated real roots lie on the length-one side; no diagonalizability or
simple-root hypothesis is inserted.  The wall is therefore exact, including
its equality strata.  Over an algebraically closed field every \(q\) splits
and a diagonal symmetric matrix gives length one, so (30.28) is expressly a
real theorem, not a field-independent claim.

If zero transfer factors are admitted, the central matrices \(\pm I_{2n}\)
realize only \((t-1)^{2n}\) and \((t+1)^{2n}\); this harmless convention
exception is why (30.28) freezes *positive* length.

### 10. Quadratic arithmetic wall over \(\mathbb Q\) and \(\mathbb Z\)

Let \(K\) be a field of characteristic different from two and
\[
 q(x)=x^2+ax+b,
 \qquad \Delta=a^2-4b.
 \tag{30.29}
\]
For a symmetric matrix
\(D=\begin{psmallmatrix}u&v\\v&w\end{psmallmatrix}\) with \(\chi_D=q\),
one has \(u+w=-a\) and
\[
 \Delta=(u-w)^2+4v^2.
 \tag{30.30}
\]
Conversely, if \(\Delta=x^2+y^2\) in \(K\), then
\[
 u={-a+x\over2},\qquad w={-a-x\over2},\qquad v={y\over2}
 \tag{30.31}
\]
constructs such a symmetric \(D\).  With (30.27), this gives:
\[
 \boxed{
 \ell_{\mathbb Q}(p)=1
 \Longleftrightarrow
 \Delta=x^2+y^2\text{ for some }x,y\in\mathbb Q;
 }
 \tag{30.32}
\]
otherwise Theorem A gives \(\ell_{\mathbb Q}(p)=2\).  Over \(\mathbb Z\),
the exact integral criterion is
\[
 \boxed{
 \ell_{\mathbb Z}(p)=1
 \Longleftrightarrow
 \Delta=d^2+4c^2
 \text{ for }c,d\in\mathbb Z,
 \quad d\equiv a\pmod2.
 }
 \tag{30.33}
\]
Here length means that the transfer blocks are symmetric over the indicated
coefficient ring.  Equations (30.32)--(30.33) are complete only for the
quadratic reduced case; no all-degree rational classification is claimed.

### 11. Strict examples and assumption failures

**Nonreal-root length wall.**  Take
\[
 q(x)=x^2+1,
 \qquad
 p(t)=t^2q(t+t^{-1}-2)
     =t^4-4t^3+7t^2-4t+1.
 \tag{30.34}
\]
No real symmetric matrix has characteristic polynomial \(x^2+1\), so no
one-factor real signed transfer realizes \(p\).  The ring construction is
already explicit:
\[
 C_q=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
 \quad
 H=A=\begin{pmatrix}0&1\\1&0\end{pmatrix},
 \quad
 B=HC_q=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
 \tag{30.35}
\]
Thus \(AB=C_q\), and \(-T(A)T(-B)\) realizes (30.34) with integer blocks.
This also disproves every positive-definite-factor version, because \(AB\)
has nonreal spectrum.

**Real one-step but no rational one-step.**  Take
\[
 q(x)=x^2-3,
 \qquad
 p(t)=t^2q(t+t^{-1}-2)
     =t^4-4t^3+3t^2-4t+1.
 \tag{30.36}
\]
The polynomial \(q\) is real-rooted, so
\(T(2I_2+\operatorname{diag}(\sqrt3,-\sqrt3))\) is a one-factor real
realization.  If a rational symmetric
\(D=\begin{psmallmatrix}u&v\\v&-u\end{psmallmatrix}\) had
\(\chi_D=q\), then \(u^2+v^2=3\).  Clearing a primitive common denominator
would give \(r^2+s^2=3d^2\); reduction modulo three forces
\(3\mid r,s,d\), a contradiction.  Hence the rational and integral lengths
are two.  An integer two-factor witness is
\[
 A=\begin{pmatrix}0&1\\1&0\end{pmatrix},
 \qquad
 B=\begin{pmatrix}1&0\\0&3\end{pmatrix},
 \qquad
 AB=\begin{pmatrix}0&3\\1&0\end{pmatrix}.
 \tag{30.37}
\]

**Unit failure.**  If \(p(1)\) is not a unit, the canonical \(B=HC_q\) is
not invertible although both shears and their product remain symplectic.
This separates “symmetric transfer block” from an unnecessary demand that
each coefficient block be a unit.

**Noncommutative failure.**  The determinant and universal-polynomial
argument used here require a commutative coefficient ring.  No determinant-
like extension to a noncommutative ring is asserted.

### 12. Weighted-transfer similarity and the congruence obstruction

The universal construction has \(A\) invertible.  With \(C=AB\),
\(H=A^{-1}\), and
\[
 K=\begin{pmatrix}I_n&0\\I_n&-A\end{pmatrix},
 \tag{30.38}
\]
direct multiplication gives the ordinary similarity
\[
 \boxed{
 K M(A,B)K^{-1}
 =T(2I_n+C)
 =\begin{pmatrix}2I_n+C&-I_n\\I_n&0\end{pmatrix}.
 }
 \tag{30.39}
\]
Since \(HC=C^{\mathsf T}H\), the coefficient \(2I_n+C\) is self-adjoint for
the unimodular symmetric metric \(H\), and the right side preserves the
weighted form
\[
 J_H=\begin{pmatrix}0&H\\-H&0\end{pmatrix}.
 \tag{30.40}
\]
It need not be a standard symmetric transfer: \(C\) need not be symmetric.
The matrix \(K\) is unimodular in the integral construction, but (30.39) is
not claimed to be a standard symplectic conjugacy.

Over a field of characteristic different from two, a fixed matrix \(D\) is
similar to a symmetric matrix exactly when there is a nonsingular symmetric
intertwiner \(G\) such that
\[
 D^{\mathsf T}G=GD,
 \qquad G=P^{\mathsf T}P
 \text{ for some }P\in\operatorname{GL}_n.
 \tag{30.41}
\]
The second condition says that the invariant form lies in the congruence
class of the identity; unimodularity alone does not imply it.  For a cyclic
companion, after fixing \(H\), all symmetric intertwiners have the form
\(Hg(C)\) with \(g(C)\) invertible.  Thus the one-standard-transfer question
is an invariant-form/congruence problem, while the two-transfer construction
works with the available \(H\) itself.  For square-free \(q\) the companion
criterion is complete because every matrix with characteristic polynomial
\(q\) is cyclic.  Repeated-factor cases can admit noncyclic decompositions,
so no stronger general-field classification is printed.

Characteristic two remains inside Theorem A but outside the quadratic-form
and Witt-language claims in Sections 10 and 12.

### 13. Elementary-shear length as a separate corollary

In the alphabet \(U(A),L(B)\), every single shear has characteristic
polynomial \((t-1)^{2n}\).  Theorem A uses two shears.  Therefore every
reciprocal \(p\neq(t-1)^{2n}\) has exact elementary-shear
characteristic-polynomial realization length two.  The exceptional
polynomial is already realized by the identity with length zero and by a
nonidentity single shear if a positive nontrivial realization is requested.

Conversely, a standard transfer satisfies
\[
 T(S)=U(S-I_n)L(I_n)U(-I_n).
 \tag{30.42}
\]
Its elementary-shear length is three unless \(S=I_n\), when
\(T(I_n)=L(I_n)U(-I_n)\) has length two.  The lower bound follows because a
two-shear alternating product has respectively its lower-right or upper-left
diagonal block equal to \(I_n\), while same-type adjacent shears merge.  This
corollary is explanatory and is not substituted for the signed-transfer
length theorem (30.28).

### 14. Portfolio separation and explicit anti-claims

The candidate is algebraic and finite-dimensional.  It neither uses nor
repackages:

- Paper27's positive-support Newton translation, phase recurrence, or local
  build evidence;
- Paper28's primitive selector cycles, normal-fan monodromy, or build-profile
  firewall;
- Paper29's paired-TN toric monomial direct products, cohomological degrees,
  or center-symmetric walls; or
- reserved Paper31's zero-coordinate gradient cancellation axis.

The proposed paper will not claim:

- that reciprocal trace reduction or the \(q\)-transform is new;
- that reciprocal polynomials were not previously realized by integral
  symplectic companions;
- that Frobenius symmetric factorization, Hankel symmetrizers, transfer
  determinant duality, or unit-triangular symplectic generation is new;
- a classification of all symplectic matrices, transfer products, or matrix
  pairs with a fixed characteristic polynomial;
- a matrix-level bijection between reciprocal polynomials and factor pairs;
- one standard symmetric transfer over every field or coefficient ring;
- positive-definite, totally nonnegative, or sign-regular factors in the
  universal construction;
- two unimodular coefficient blocks unless \(p(1)\) is a unit;
- that (30.39) is a standard symplectic conjugacy;
- an all-degree rational or integral classification of symmetric
  characteristic polynomials;
- Witt-form statements in characteristic two;
- a determinant theorem over noncommutative rings;
- an empirical, numerical, finite-search, or computer-algebra proof; or
- absolute priority, “first”, “unique construction”, or exhaustive
  literature coverage.

### 15. Proof-first page-mass plan

References are excluded from the content count.

| section | target content pages |
|---|---:|
| problem, frozen alphabets, contribution ledger, and anti-claims | 2.5 |
| primary literature and direct-collision matrix | 3.0 |
| reciprocal reduction and universal determinant identity | 3.0 |
| quotient Frobenius form and ring-level converse | 4.5 |
| signed-transfer image and real \(1/2\) length theorem | 3.5 |
| quadratic \(\mathbb Q/\mathbb Z\) arithmetic wall | 3.5 |
| weighted transfer, invariant forms, and congruence boundary | 3.0 |
| strict examples, unit/characteristic failures, and shear corollary | 2.5 |
| portfolio separation, limitations, and conclusion | 1.0 |
| **total** | **26.5** |

The page mass comes from complete ring-specialization proofs, exact arithmetic
necessity and sufficiency, congruence qualifications, counterexamples, and
source absorption.  It does not rely on governance text, oversized displays,
spacing, appendices of raw search output, or references.

### 16. Author preflight and formal-review boundary

Two independent read-only preflights were completed before this author stop.
The literature preflight searched the strongest ingredient and direct-
conjunction collisions and returned cautious GO with scores novelty \(7.6\),
standalone \(7.8\), proof confidence \(9.5\), and 24--27 pages.  The algebra
preflight rederived (30.9)--(30.42), including zero divisors, characteristic
two in Theorem A, companion orientation, every sign, the \(p(1)\) unit wall,
the real-rooted boundary, the quadratic arithmetic criteria, and the
ordinary-versus-symplectic similarity distinction.  Its fatal-finding census
was zero.

The author-only census is:

| class | count |
|---|---:|
| Blocker | 0 |
| Major | 0 |
| Minor | 0 |
| Ambiguity | 0 |

Two entirely fresh, mutually blind formal reviewers must independently read
the complete append-only candidate.  R1 must repeat the primary-source search
through 2026-08-29 and stress Margalit--Spallone, Rüd--Zhang,
Frobenius--Bosch, Taussky, Bender, Luo--Hill, Molinari, unit-triangular
factorizations, quadratic palindromic realizability, full-conjunction novelty,
standalone page mass, anti-claims, and portfolio separation.  R2 must
independently rederive the reciprocal transform, universal block determinant,
ring specialization, anti-triangular determinant, intertwiner orientation,
symmetric factors, signed-transfer signs, real length theorem, quadratic
arithmetic criteria, both examples, unit wall, weighted similarity,
congruence caveat, and elementary-shear corollary.  Neither provisional score
nor either preflight may substitute for those reviews.

Each formal reviewer may create its own review artifact only for an
unconditional all-zero PASS with novelty and standalone value at least 7.5,
proof confidence at least 9.0, and credible proof-first content in [22,30]
pages.  A finding returns `FAIL_WRITE_NOTHING`.  Paper30 remains unconsumed,
its project remains absent, and this author stop grants no source, build, PDF,
release, submission, or external-effect authority.

BATCH07_PAPER30_CANDIDATE_V1_AUTHOR_STOP

## Paper 31 append-only V1 candidate record and author stop

Authorization:
`B07-E0225-P31-CANDIDATE-DISCOVERY-AUTHORIZATION`, ending in
`BATCH07_PAPER31_CANDIDATE_DISCOVERY_AUTHORIZED`.  The immutable parent is
the complete 112,514-byte report with 2,612 line feeds and SHA-256
`d91c4e5f813f1da387c756f17d5fcb08816a0e9f6392db11d23fbdcc8b9f5f86`.
This is the sole authorized Paper31 discovery append.  It changes no earlier
candidate, consumes no paper number, creates no project, and authorizes no
source, review artifact, build, PDF, release, submission, or external effect.

### Current decision

- Reserved candidate identifier: `zero_coordinate_gradient_cancellation_v1`.
- Public-safe working title: **Zero-Coordinate Cancellation in Polynomial
  Hamiltonian Shears: First-Jet Incidence and the Active-Hessian Boundary**.
- Mathematical disposition: the theorem package below is correct at author
  preflight and is retained as a local proof note.
- Candidate-gate disposition: **STOP AT AUTHOR PREFLIGHT**.  The sharp kernel
  equivalence is a direct use of the classical Jacobian criterion, and the
  remaining incidence, integration, and monomial-transport consequences do
  not credibly clear the novelty, standalone-value, or 22-page lower bound.
- Paper number consumed: no.
- Project path authorized or created: no.
- Scientific computation, CAS, numerical experiment, dataset, or GPU use:
  none.
- External effect: none.

The stop is not a proof failure.  It is the required value judgment after
absorbing Paper27 and the closest public literature.  A longer account could
be produced by expanding standard background on coordinate ideals, jets,
toric maps, and vanishing Hessians, but that would not create new theorem
mass and is forbidden as page padding.

### Discovery lanes and killed alternatives

| Lane | Candidate mechanism | Exact disposition |
|---|---|---|
| Coordinate-stratum first jets | Reduce an outer potential modulo the square of the inactive-coordinate ideal; distinguish tangential survival, defect-one normal rescue, and order-at-least-two disappearance | RETAINED.  This is the clean geometric language for the exact incidence law. |
| Active gradient substitution | Identify hidden cancellation with the kernel of substitution by the active gradient and test faithfulness by the active Hessian | RETAINED MATHEMATICALLY; VALUE-LIMITING.  The iff is the Jacobian criterion in coordinate-ring form. |
| Monomial inner potential | Compute every surviving component, coefficient, exponent, Newton support, and weighted degree without genericity | RETAINED.  It gives the sharp defect trichotomy but is short linear algebra. |
| Sparse inner potential | Use a full-active Newton vertex to isolate a nonzero Hessian monomial for every nonzero coefficient tuple | RETAINED AS A SUFFICIENT CERTIFICATE.  It is not promoted to a classification. |
| Support-only robust-Hessian classification | Characterize every finite support for which every nonzero coefficient choice has nonzero Hessian | STOP / OPEN.  The coefficient-discriminant and mixed-Hessian cancellations were not classified; asserting an iff would be new unproved research. |
| Iterated selector dynamics on defect strata | Turn disappearance into a finite automaton or a new degree-growth recurrence | STOP AS SCOPE COLLISION.  It would re-enter Paper27/Paper28 selector and recurrence territory and the first iterate already leaves the zero section. |
| Positive characteristic lift | Replace the Hessian by a characteristic-free criterion while retaining literal support incidence | STOP.  Frobenius simultaneously breaks the Hessian criterion and ordinary differentiation support; the correct Witt-Jacobian theory is a different project. |

No proof-credible alternative survived with a stronger value profile.  In
particular, the unproved support-only classification was not smuggled into the
candidate to lift its score.

### 1. Hamiltonian zero-section and the coordinate first jet

Let (K) be a field of characteristic zero, let (r\ge2), and fix a
nonempty proper active set (A\subsetneq[r]), with defect set
(D=[r]\setminus A).  Write

\[
 K[q_A]=K[q_i:i\in A],\qquad
 L_A=\{p_i=0:i\in D\}\subset\mathbb A_p^r,
\]

and let

\[
 I_D=\langle p_i:i\in D\rangle\subset K[p_1,\ldots,p_r]
\]

be the ideal of the coordinate subspace (L_A).  Take

\[
 V\in K[q_A],\qquad W\in K[p_1,\ldots,p_r]
\]

and define the two polynomial Hamiltonian shears

\[
 S_V(q,p)=(q,p+\nabla V(q)),\qquad
 T_W(q,p)=(q+\nabla W(p),p).
\]

Their off-diagonal Jacobian blocks are symmetric Hessians, so both maps
preserve the standard symplectic form

\[
 \omega=\sum_{i=1}^r dq_i\wedge dp_i.
\]

The zero section is sent by (S_V) to the Lagrangian graph of (dV), which
lies in the momentum coordinate subspace (L_A).  The fresh position update
of (T_W\circ S_V) on that zero section is

\[
 C_{V,W}(q)=\nabla W(\nabla V(q)).                 \tag{31.1}
\]

Every outer polynomial has the unique first-normal-jet decomposition

\[
 W(p)\equiv W_0(p_A)+\sum_{k\in D}p_kW_k(p_A)
             \pmod {I_D^2}.                       \tag{31.2}
\]

Consequently, on (L_A),

\[
 (\partial_iW)|_{L_A}=\partial_iW_0\quad(i\in A),
 \qquad
 (\partial_kW)|_{L_A}=W_k\quad(k\in D).           \tag{31.3}
\]

Thus only the class of (W) modulo (I_D^2) can affect (31.1).  Terms of
defect order zero give tangential components, terms of defect order one can
give a normal component, and terms of defect order at least two disappear
from the entire restricted gradient.  This is an exact statement, not an
asymptotic Taylor heuristic.

### 2. Exact kernel--Hessian boundary

Define the substitution homomorphism

\[
 \psi_V:K[p_1,\ldots,p_r]\longrightarrow K[q_A],\qquad
 p_i\longmapsto
 \begin{cases}
  \partial_iV,&i\in A,\\
  0,&i\in D.
 \end{cases}                                      \tag{31.4}
\]

It factors through (K[p]/I_D\simeq K[p_A]).  The induced map

\[
 \theta_V:K[p_A]\longrightarrow K[q_A],\qquad
 p_i\longmapsto\partial_iV                         \tag{31.5}
\]

is injective exactly when the active gradient components are algebraically
independent.  In characteristic zero, their Jacobian is the active Hessian,
so the Jacobian criterion gives the sharp equivalence

\[
 \boxed{
 \ker\psi_V=I_D
 \quad\Longleftrightarrow\quad
 \det\operatorname{Hess}_A(V)\not\equiv0 .}       \tag{31.6}
\]

Here nonzero means nonzero as a polynomial; pointwise invertibility at every
point is neither assumed nor concluded.  No algebraic closure of (K) is
needed.

Equation (31.6) is the universal incidence-faithfulness boundary.  If its
right-hand side holds, then for every (W) and every component (j),

\[
 C_{V,W,j}=\psi_V(\partial_jW)\ne0
 \quad\Longleftrightarrow\quad
 \partial_jW\notin I_D.                            \tag{31.7}
\]

If (W=\sum_{\beta}d_\beta p^\beta) is collected, (31.7) is the literal
support-incidence test

\[
 \exists\,\beta\in\operatorname{supp}W:
 \quad \beta_j>0,
 \qquad (\beta-e_j)_i=0\quad(i\in D).              \tag{31.8}
\]

For (j\in A), this says that some differentiated monomial has no inactive
variable.  For (j\in D), it forces

\[
 \beta_j=1,\qquad
 \beta_i=0\quad(i\in D\setminus\{j\}),             \tag{31.9}
\]

which is the exact defect-one rescue.  Distinct collected monomials cannot
merge merely by differentiating in a fixed component.

The converse is constructive.  If the active Hessian determinant vanishes,
the Jacobian criterion supplies a nonzero relation

\[
 0\ne R(p_A)\in\ker\theta_V.
\]

For any inactive (k\in D), set

\[
 W=p_kR(p_A).                                      \tag{31.10}
\]

Its normal first-jet coefficient is the visibly nonzero polynomial (R),
so incidence predicts survival, but

\[
 C_{V,W,k}=R(\nabla_AV)=0.                         \tag{31.11}
\]

Hence a degenerate active Hessian always permits hidden cancellation that is
invisible to coordinate incidence.  If (D=\varnothing) is considered as a
non-headline boundary, the same conclusion follows by integrating (R)
termwise with respect to an active variable; characteristic zero is used to
divide by the new exponents.

### 3. Exact monomial transport and the defect trichotomy

Let the inner potential be the nonlinear monomial

\[
 V=cq^\alpha,\qquad c\in K^\times,\qquad
 \operatorname{supp}\alpha=A,\qquad |\alpha|\ge2. \tag{31.12}
\]

With (s=|A|) and (mathbf1_A) the active all-ones vector, direct
factorization gives

\[
 \det\operatorname{Hess}_A(cq^\alpha)
 =(-1)^{s+1}c^s(|\alpha|-1)
   \left(\prod_{i\in A}\alpha_i\right)
   q^{s\alpha-2\mathbf1_A}\ne0.                   \tag{31.13}
\]

For an outer monomial (d_\beta p^\beta), define its inactive defect order

\[
 \delta_A(\beta)=\sum_{i\in D}\beta_i.            \tag{31.14}
\]

Its complete restricted-gradient trichotomy is:

1. If (delta_A(\beta)=0), precisely the components
   (j\in\operatorname{supp}\beta\subseteq A) survive.
2. If (delta_A(\beta)=1), there is a unique inactive (k) with
   (eta_k=1), and precisely component (k) survives.
3. If (delta_A(\beta)\ge2), the entire gradient contribution vanishes.

For every surviving component, substitution gives the exact exponent

\[
 \boxed{
 \nu_{\alpha,j}(\beta)
   =( |\beta|-1)\alpha-\beta+e_j,}                 \tag{31.15}
\]

written in all (r) coordinates.  The coefficient is

\[
 d_\beta\beta_j c^{|\beta|-1}
 \prod_{i\in A}\alpha_i^{\,\beta_i-\mathbf1_{i=j}},\tag{31.16}
\]

where the indicator is zero when (j\notin A).  It is nonzero in
characteristic zero.

The active exponent substitution on a derivative monomial has column matrix

\[
 M_\alpha=\alpha\mathbf1_A^{\mathsf T}-I_s,
 \qquad
 \det M_\alpha=(-1)^{s+1}(|\alpha|-1)\ne0.         \tag{31.17}
\]

It is therefore injective on the active exponent lattice.  For fixed (j),
distinct admissible outer exponents remain distinct after (31.15), so
arbitrary nonzero coefficient signs cannot create a hidden collision.

More explicitly, put

\[
 B_{A,j}(W)=\{\beta\in\operatorname{supp}W:
                  \beta_j>0,\ (\beta-e_j)_D=0\}.
\]

Then there are only two branches:

\[
 B_{A,j}(W)=\varnothing\Longleftrightarrow C_{V,W,j}=0,
\]

while otherwise

\[
 \operatorname{supp}C_{V,W,j}
 =\{\nu_{\alpha,j}(\beta):\beta\in B_{A,j}(W)\}, \tag{31.18}
\]

with coefficients (31.16).  Consequently

\[
 \operatorname{Newt}(C_{V,W,j})
 =\operatorname{conv}\{\nu_{\alpha,j}(\beta):
                         \beta\in B_{A,j}(W)\},    \tag{31.19}
\]

and for every positive weight (u),

\[
 \deg_u C_{V,W,j}
 =\max_{\beta\in B_{A,j}(W)}
       \nu_{\alpha,j}(\beta)\cdot u.              \tag{31.20}
\]

The zero branch has no invented Newton polytope or degree.

### 4. A coefficient-robust sparse-inner certificate

The monomial hypothesis is not required for universal incidence
faithfulness.  Let

\[
 V=\sum_{\alpha\in E}c_\alpha q^\alpha,
 \qquad c_\alpha\in K^\times,
\]

and suppose the Newton polytope of (V) has a vertex
(alpha^\star) satisfying

\[
 \operatorname{supp}\alpha^\star=A,
 \qquad |\alpha^\star|\ge2.                       \tag{31.21}
\]

Choose a linear weight exposing (alpha^\star) uniquely.  In the grouped
determinant expansion, the unique extreme-weight row-labelled tuple is
((\alpha^\star,\ldots,\alpha^\star)).  It contributes

\[
 (-1)^{s+1}(c_{\alpha^\star})^s
 (|\alpha^\star|-1)
 \left(\prod_{i\in A}\alpha_i^\star\right)
 q^{s\alpha^\star-2\mathbf1_A},                   \tag{31.22}
\]

which no other tuple can cancel.  Therefore

\[
 \det\operatorname{Hess}_A(V)\not\equiv0          \tag{31.23}
\]

for every allowed nonzero coefficient tuple.  Equations (31.6)--(31.9) then
apply to every outer (W).

Condition (31.21) is sufficient, not necessary.  For example,
(V=q_1^2+q_2^2) has no full-active support exponent but has nonsingular
constant Hessian.  Conversely, total degree at least two without a
full-active certificate does not suffice:
(V=(q_1+q_2)^2) has singular Hessian.  No classification of all supports
with coefficient-uniform nonvanishing is claimed.

### 5. Sharp fixtures and failure boundaries

**Defect-one rescue.**  In three coordinate pairs, let

\[
 V=q_1^2q_2^2,\qquad W=p_1p_2p_3,
 \qquad A=\{1,2\}.
\]

Although (W(\nabla V)=0),

\[
 \nabla W(\nabla V)=(0,0,4q_1^3q_2^3).
\]

The normal (q_3)-update is rescued by the single (p_3) factor.

**Order-two disappearance.**  With the same active set,
(W=p_1p_3^2) has defect order two.  Every component of its gradient still
contains an inactive factor after at most one differentiation, so the fresh
update is zero.

**Two-coordinate defect.**  In four coordinate pairs, with
(A=\{1,2\}) and (W=p_1p_3p_4), every derivative retains (p_3) or
(p_4); the entire restricted gradient vanishes.

**Hidden cancellation at the Hessian boundary.**  Put

\[
 V=(q_1+q_2)^3,\qquad W=p_3(p_1-p_2),
 \qquad A=\{1,2\}.
\]

The active gradient components are equal and the active Hessian has rank one.
The defect-one incidence test sees the nonzero normal coefficient
(p_1-p_2), but

\[
 \partial_3W(\nabla V)=p_1-p_2\big|_{p=\nabla V}=0.
\]

This is the promised hidden algebraic cancellation.

**Positive-characteristic failures.**  Over characteristic (p>0),

\[
 V=\sum_{i\in A}q_i^{p+1}
\]

has active gradient ((q_i^p)_{i\in A}), whose components are algebraically
independent, while its active Hessian is zero.  Thus the Hessian equivalence
fails.  Separately, (W=p_j^p) has zero ordinary derivative despite its
literal exponent incidence.  These are two distinct Frobenius failures, not
one removable sign issue.

The linear boundary (|\alpha|=1), a nonminimal declared active set, a zero
coefficient, an uncollected support, and an outer monomial outside the
admissible set are likewise excluded rather than silently interpreted.

### 6. Bounded primary-source comparison through 2026-08-29

| Source | Established neighboring content | Collision finding |
|---|---|---|
| M. Beecken, J. Mittmann, N. Saxena, *Algebraic Independence and Blackbox Identity Testing*, Information and Computation 222 (2013), 2--19, DOI `10.1016/j.ic.2012.10.004`, arXiv:`1102.2789`; J. Mittmann, N. Saxena, P. Scheiblechner, arXiv:`1202.4301` | The ordinary Jacobian criterion in characteristic zero/large characteristic and its failure/replacement in small positive characteristic | DIRECT INGREDIENT.  Equation (31.6) is this criterion applied to a gradient tuple after quotienting by a coordinate ideal. |
| M. de Bondt and A. van den Essen, *Singular Hessians*, Journal of Algebra 282 (2004), 195--204, DOI `10.1016/j.jalgebra.2004.08.026`; M. de Bondt, *Polynomials with constant Hessian determinants in dimension three*, J. Pure Appl. Algebra 219 (2015), 3743--3754, arXiv:`1203.6605` | Singular gradient maps, Hessian structure, and weighted leading parts with nonzero Hessian | CLOSE HESSIAN CONTEXT.  No outer first-jet incidence theorem was located, but nonzero/vanishing Hessian is classical territory. |
| T. Fassarella, *Logarithmic Hesse's Problem*, arXiv:`1102.1659`; L. Fiorindo, *Polynomials with vanishing Hessian and Lefschetz properties*, arXiv:`2212.11801` | Algebraic dependence of partial derivatives, polar maps, and modern vanishing-Hessian geometry | DIRECT BOUNDARY CONTEXT.  The candidate's hidden-cancellation fixture is an elementary use of this dependence mechanism. |
| D. Eisenbud and B. Sturmfels, *Binomial Ideals*, Duke Math. J. 84 (1996), 1--45, DOI `10.1215/S0012-7094-96-08401-X`, arXiv:`alg-geom/9401001` | Kernels of monomial parametrizations and toric/binomial ideals | DIRECT MONOMIAL-MAP CONTEXT.  The zero-kernel conclusion from the invertible matrix (31.17) is a particularly elementary case. |
| J. Huh, *The maximum likelihood degree of a very affine variety*, Compositio Math. 149 (2013), 1245--1266, DOI `10.1112/S0010437X13007057`, arXiv:`1207.0553` | Gradient maps, Newton polytopes, and decomposition along coordinate planes for nondegenerate hypersurfaces | ADJACENT NEWTON/COORDINATE-STRATUM CONTEXT, not the exact shear-composition survival law. |
| H. Koch and H. E. Lomelí, *On Hamiltonian flows whose orbits are straight lines*, DCDS-A 34 (2014), 2091--2104, DOI `10.3934/dcds.2014.34.2091`, arXiv:`1304.3377` | Polynomial Hamiltonian shear maps, quasi-translations, singular Hessians, and symplectic factorization context | DIRECT OBJECT CONTEXT, but no coordinate-defect first-jet classification. |
| Closed Paper27 proof package, Sections 4--5 | Grouped positive-face Hessian nonvanishing, Jacobian independence, substitution survival, and a degenerate equal-gradient cancellation fixture | INTERNAL ABSORPTION.  Paper31 newly isolates the inactive-coordinate first jet and defect-one trichotomy; it cannot count the Hessian/Jacobian machinery again as new. |

The bounded exact-phrase and claim-level search located no primary source
stating the full conjunction of (31.2), (31.6), the universal componentwise
incidence law, its sharp normal-cancellation converse, and (31.15)--(31.20) in
Hamiltonian-shear language.  This is only a bounded no-collision finding, not
a priority claim.  More importantly, absence of an exact conjunction does
not make a direct assembly of classical ingredients sufficiently novel.

### 7. Anti-claims and exact scope

The candidate does **not** claim:

- a classification of polynomial shears, all sparse supports, all
  coefficient-robust Hessians, or all polynomial compositions;
- pointwise invertibility, étaleness, dominance over every characteristic,
  or a Jacobian-conjecture consequence;
- an iteration theorem, invariant defect stratum, dynamical degree,
  entropy, selector automaton, or recurrence;
- that the full-active Newton-vertex certificate is necessary;
- a Newton polytope for a zero component;
- that incidence decides cancellation when the active Hessian is singular;
- that a finite literal example proves the universal theorem; or
- a first/only claim beyond the bounded comparison above.

All displayed universal results are hand-derived polynomial identities over a
characteristic-zero field.  The examples test boundaries only.  No scientific
execution or CAS output is evidence for any claim.

### 8. Author proof audit, value audit, and terminal recommendation

The zero-write discovery adversary independently rederived the factorization
of (psi_V), the Jacobian/Hessian equivalence, both active and inactive
incidence clauses, the annihilating-relation converse, the monomial Hessian
sign and exponent, the matrix determinant, and the full-active-vertex
certificate.  It found no blocker, minor error, or residual ambiguity after
the boundary wording above.  It independently assessed the exact package as
a short note dominated by classical machinery.

Frozen author-preflight census:

| class | count |
|---|---:|
| Blocker | 0 |
| Major | 2 |
| Minor | 0 |
| Ambiguity | 0 |

The two major findings are:

1. **Novelty / standalone value below gate.**  The kernel--Hessian headline
   is the classical Jacobian criterion after a coordinate quotient.  The
   integration counterexample, first-jet incidence split, and invertible
   monomial exponent map are exact but elementary, while Paper27 already
   absorbs the grouped-Hessian and substitution-survival machinery.
2. **Credible page mass below gate.**  The proof-first contribution supports
   approximately 17--20 anonymous content pages.  Reaching 22 pages would
   require background expansion or an unproved general support
   classification, neither of which is admissible.

Frozen conservative author scores are:

- novelty: (7.0/10);
- standalone value: (7.2/10);
- proof confidence: (9.5/10);
- credible anonymous proof-first content: (17\text{--}20) pages.

The required gates are novelty at least 7.5, standalone value at least 7.5,
proof confidence at least 9.0, and 22--30 credible pages, conjunctively.  The
candidate therefore stops before formal candidate review.  A later ledger
event must close the reserved slot as
`TERMINAL_AUTHOR_PREFLIGHT_NOVELTY_STANDALONE_PAGE_MASS_FAILED`, with effect
`NO_PAPER_NUMBER_NO_PROJECT_NO_SOURCE_NO_RELEASE`.  No revision is warranted:
the failed quantities are the theorem's intrinsic increment and mass, not a
repairable typo or omitted hypothesis.

BATCH07_PAPER31_CANDIDATE_V1_AUTHOR_STOP
