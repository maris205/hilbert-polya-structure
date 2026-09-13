# Paper 28 strict canonical source lock

## Lock status and public-safe identity

Candidate: `primitive_selector_cycle_monodromy_v1`, controlling version V4  
Public-safe working title: *Primitive Newton-Selector Cycles in
Permutation-Twisted Hamiltonian Shears: Normal-Fan Classification and Exact
Monodromy*  
Scientific execution supporting the theorem: zero  
External effect authorized by this lock: none

This file is the strict canonical compression of the independently passed
source design.  Later planning and writing may reorganize exposition but may
not strengthen a quantifier, omit a hypothesis, merge distinct period or
decoder levels, change a recurrence start index, or enlarge the novelty
claim.  All theorem-critical proofs belong in the anonymous main body.

## Headline quantifier and input word

The public theorem is family-wise.  Let

\[
 \mathsf w=((a_0,b_0),\ldots,(a_{\ell-1},b_{\ell-1})),
 \qquad \ell\ge3,
\]

be a rooted primitive word over the V and W labels that actually occur.
Repeated labels are allowed.  Either component alphabet may be a singleton;
the pair word itself must still be primitive.  A marked phase zero roots the
word.  For every such word the construction gives one fixed autonomous
polynomial symplectomorphism \(F_{\mathsf w}\).  It does not give one map for
all words, one map per length, or a fixed-dimensional realization for
unbounded length.

Set \(r=\ell+1\).  There are \(r\) symplectic coordinate pairs and hence
ambient affine dimension \(2r=2(\ell+1)\).  The moving index set is

\[
 I_{\mathrm{mov}}=\{0,\ldots,\ell-1\},
\]

and \(\star\) is a separate fixed coordinate.  The permutation P cycles the
moving coordinates,

\[
 Pe_j=e_{j+1\pmod\ell},\qquad Pe_\star=e_\star,
\]

so \(P^\ell=I\) and \(P\mathbf1=\mathbf1\).

## Field, parameters, supports, and coefficients

All polynomial claims are over a field \(\Bbbk\) of characteristic zero.
Choose integers

\[
 H\ge2,\qquad \rho\ge2,\qquad K\ge1,
\]

and the positive spike seed

\[
 u_0=\mathbf1+(H-1)e_0.
\]

For each used label define the nonempty occurrence sets

\[
 S_a=\{j:a_j=a\},\qquad T_b=\{j:b_j=b\}.
\]

The collected exponent vectors are

\[
 \alpha_a=\rho\mathbf1+K\sum_{j\in S_a}e_j
 +K(\ell-|S_a|)e_\star,
\]

\[
 \beta_b=\rho\mathbf1+K\sum_{j\notin T_b}e_j
 +K|T_b|e_\star.
\]

Every exponent coordinate is at least two and every exponent has the common
total

\[
 D=\rho r+K\ell.
\]

For arbitrary displayed coefficients
\(\xi_a,\zeta_b\in\Bbbk^*\), set

\[
 V_{\mathsf w}(q)=\sum_a\xi_aq^{\alpha_a},\qquad
 W_{\mathsf w}(p)=\sum_b\zeta_bp^{\beta_b}.
\]

The support is the collected support shown above.  A zero coefficient changes
that support and lies outside the theorem.  All initial weighted-degree
seeds are positive; ordinary total degree is not substituted for the stated
weighted degree.

## Frozen map order and symplectic branch

Define the two gradient shears and the simultaneous permutation by

\[
 S_V(q,p)=(q,p+\nabla V(q)),\qquad
 T_W(q,p)=(q+\nabla W(p),p),
\]

\[
 \Pi_P(q,p)=(Pq,Pp).
\]

The composition order is literally

\[
 F_{\mathsf w}=\Pi_P\circ T_{W_{\mathsf w}}
 \circ S_{V_{\mathsf w}}.
\]

Symmetric Hessian blocks make both shears symplectic, and the same
permutation on q and p preserves the standard symplectic form.  The map is a
polynomial automorphism.  If
\(\bar q=P^{-1}Q\) and \(\bar p=P^{-1}\mathsf P\), its inverse is

\[
 F_{\mathsf w}^{-1}(Q,\mathsf P)=
 \left(
 \bar q-\nabla W_{\mathsf w}(\bar p),
 \bar p-\nabla V_{\mathsf w}
       (\bar q-\nabla W_{\mathsf w}(\bar p))
 \right).
\]

No later source may reverse the shear order, permute only one half of the
symplectic coordinates, or treat formal degree matrices as the proof of
symplecticity.

## General selector normal-fan iff

For the general positive equal-total support class with \(r\ge2\), define

\[
 \mathcal N_V^+(\alpha)=
 \{x>0:(\alpha-\gamma)^{\mathsf T}x>0
          \text{ for every competing }\gamma\},
\]

\[
 \mathcal N_W^-(\beta)=
 \{x>0:(\eta-\beta)^{\mathsf T}x>0
          \text{ for every competing }\eta\}.
\]

For a declared rooted length-\(\ell\) residual return, the prescribed strict
support word is selected exactly when the positive position seed belongs to

\[
 \mathcal C_{\mathsf w}=
 \mathbb R_{>0}^{r}\cap
 \bigcap_{j=0}^{\ell-1}P^{-j}
 \bigl(\mathcal N_V^+(\alpha_j)
       \cap\mathcal N_W^-(\beta_j)\bigr).
\]

This is a rational homogeneous open polyhedral cone.  V uses strict
maximizers.  After the selected V shear, equal totals reverse the residual W
comparison, so W uses strict minimizers.  The iff classifies selectors from
position weights only; it is not an iff for the actual polynomial-degree
lift.  A singleton support has an empty competitor family, its cone is the
full positive weight space, and its uniqueness is vacuous.

## Incidence realization of every primitive word

At phase j the residual spike is \(x_j=P^ju_0\).  With

\[
 C_0=\rho(H+\ell)+K\ell,
 \qquad g=K(H-1)>0,
\]

the exact score table is

\[
 \alpha_a^{\mathsf T}x_j
 =C_0+g\mathbf1_{\{j\in S_a\}},
\]

\[
 \beta_b^{\mathsf T}x_j
 =C_0+g\mathbf1_{\{j\notin T_b\}}.
\]

Thus \(\alpha_{a_j}\) is the unique V maximizer and \(\beta_{b_j}\)
is the unique W minimizer.  The difference from every competitor that
actually exists is exactly g: selected minus competitor on the V side and
competitor minus selected on the W side.  No finite gap is assigned when a
side is a singleton.  The supports are assembled once from occurrence sets,
so the infinite selector itinerary is endogenous to the one autonomous map,
not supplied by an external switching schedule.

## Exact carry chamber and actual weighted-degree transport

For an exponent vector write

\[
 A_\alpha=\mathbf1\alpha^{\mathsf T}-I,
 \qquad B_\beta=\mathbf1\beta^{\mathsf T}-I.
\]

Let \(m_0\) be the initial positive momentum-weight vector.  The exact
phase-zero source-carry gate is the coordinatewise chamber

\[
 0<m_0<A_{\alpha_{a_0}}u_0.
\]

The smaller subcone \(0<m_0\le u_0\) is convenient and sufficient but is
not necessary.  For \(r\ge2\), positive u, and
\(\alpha\in\mathbb Z_{\ge2}^{r}\),

\[
 (A_\alpha u)_i-u_i
 =(\alpha_i-2)u_i+\sum_{k\ne i}\alpha_ku_k>0,
\]

and the analogous inequality holds for B.  The gate gives
\(u_1>m_1\), and thereafter strict source and target carries propagate by
induction.  With selected phase pair \((\alpha_n,\beta_n)\),

\[
 m_{n+1}=PA_{\alpha_n}u_n,
\]

\[
 u_{n+1}=PB_{\beta_n}A_{\alpha_n}u_n.
\]

Unique support selectors, exponent coordinates at least two, nonzero
derivative scalars in characteristic zero, nonzero products in the
polynomial domain, and strict carries make these the actual polynomial
weighted-degree vectors for every nonzero coefficient tuple.  No genericity,
sign choice, computation, or hidden noncancellation certificate is used.

This exact identification of the stated weighted-degree transport must not be
promoted into a free-standing exact ordinary-degree theorem, an exact
algebraic/dynamical-degree claim, or an exact-degree invariant outside this
chamber.

## Ordered cocycle and monodromy

For an allowed pair put

\[
 c_{a,b}=(D-1)\alpha_a-\beta_b,
 \qquad \lambda=(D-1)^2,
\]

\[
 C_{a,b}=PB_{\beta_b}A_{\alpha_a}
 =P+\mathbf1c_{a,b}^{\mathsf T}.
\]

For \(c_j=c_{a_j,b_j}\), \(C_j=C_{a_j,b_j}\), and

\[
 Q_s=C_{s-1}\cdots C_0,
\]

the order of multiplication is fixed and

\[
 Q_s=P^s+\mathbf1R_s^{\mathsf T},
\]

\[
 R_s^{\mathsf T}=
 \sum_{j=0}^{s-1}\lambda^{s-1-j}c_j^{\mathsf T}P^j,
 \qquad R_s^{\mathsf T}\mathbf1=\lambda^s-1.
\]

Since \(P^\ell=I\), the period monodromy is

\[
 M_{\mathsf w}=Q_\ell=I+\mathbf1R_\ell^{\mathsf T}.
\]

Its characteristic polynomial and nonnegative powers are

\[
 \chi_{M_{\mathsf w}}(z)
 =(z-1)^{r-1}(z-\lambda^\ell),
\]

\[
 M_{\mathsf w}^k=I+
 \frac{\lambda^{k\ell}-1}{\lambda^\ell-1}
 \mathbf1R_\ell^{\mathsf T}\qquad(k\ge0).
\]

These are exact ordered formulas; no asymptotic spectral, entropy,
integrability, or reciprocity conclusion is attached to them.

## Decoder ladder and information boundary

Every coordinate of every map-specific digit satisfies

\[
 0<(c_{a,b})_i<\lambda,
\]

and the support-vector map \((a,b)\mapsto c_{a,b}\) is injective.  Therefore
coordinatewise base-\(\lambda\) expansion of
\(R_\ell^{\mathsf T}\) is carry-free and recovers the ordered rotated
digits \(c_j^{\mathsf T}P^j\); known P undoes their rotations.

The three decoder levels are immutable:

1. \(M_{\mathsf w},P,\lambda,\ell\), and marked phase zero recover the
   rooted ordered digit-vector word \((c_0,\ldots,c_{\ell-1})\).
2. Adding the unlabelled support dictionary of the map recovers the ordered
   exponent-support pairs.
3. Adding the labelled support dictionary recovers the literal rooted
   label-pair word.

Without literal names, labels are determined only up to independent
renaming of the V and W alphabets.  Without marked phase zero, only the cyclic
rotation class is intrinsic.  Monodromy alone does not manufacture a
dictionary, and the scalar degree trajectory is not a word decoder.

## Scalar forcing, periods, and recurrence domains

For the incidence construction,

\[
 \mu=(D-1)(C_0+g)-C_0>0,
\]

and

\[
 u_n=P^nu_0+t_n\mathbf1,
 \qquad t_0=0,
 \qquad t_{n+1}=\lambda t_n+\mu.
\]

The selector word has least period \(\ell\) because the input pair word is
primitive.  The position-weight orbit modulo
\(\mathbb R\mathbf1\) also has least period \(\ell\): the fixed star
coordinate forces any diagonal displacement to vanish, while the unique
moving H-spike rules out \(P^du_0=u_0\) for \(0<d<\ell\).  These are two
distinct least-period claims and neither asserts a periodic polynomial state.

Define the position maximum

\[
 q_n=\max_i(u_n)_i=H+t_n.
\]

Its order-two recurrence and its length-\(\ell\) annihilator both begin at
\(n=0\):

\[
 q_{n+2}-(1+\lambda)q_{n+1}+\lambda q_n=0,
 \qquad n\ge0,
\]

\[
 q_{n+\ell+1}-\lambda q_{n+\ell}-q_{n+1}+\lambda q_n=0,
 \qquad n\ge0.
\]

For a moving coordinate \(i\in I_{\mathrm{mov}}\),

\[
 y_n^{(i)}=1+(H-1)\mathbf1_{\{n\equiv i\pmod\ell\}}+t_n,
\]

whereas the fixed coordinate is stated separately as

\[
 y_n^{(\star)}=1+t_n.
\]

For every \(i\in I_{\mathrm{mov}}\sqcup\{\star\}\),

\[
 y_{n+\ell+1}^{(i)}-\lambda y_{n+\ell}^{(i)}
 -y_{n+1}^{(i)}+\lambda y_n^{(i)}=0,
 \qquad n\ge0.
\]

For \(s\in I_{\mathrm{mov}}\),
\(i\in I_{\mathrm{mov}}\sqcup\{\star\}\), and
\(z_m^{(i,s)}=y_{s+m\ell}^{(i)}\),

\[
 z_{m+2}^{(i,s)}-(1+\lambda^\ell)z_{m+1}^{(i,s)}
 +\lambda^\ell z_m^{(i,s)}=0,
 \qquad m\ge0.
\]

For the complete-state maximum

\[
 d_n=\max\{\max_i(u_n)_i,\max_i(m_n)_i\},
\]

strict carry gives \(d_n=q_n\) only for \(n\ge1\).  Consequently

\[
 d_{n+\ell+1}-\lambda d_{n+\ell}-d_{n+1}+\lambda d_n=0
 \qquad(n\ge1).
\]

The residual of the forbidden unconditional \(n=0\) instance is exactly

\[
 \lambda(d_0-q_0).
\]

It vanishes iff \(d_0=q_0\), equivalently
\(\max_i(m_0)_i\le\max_i(u_0)_i\).  Every displayed scalar relation is an
annihilator only; no minimal recurrence or scalar identification of the word
is claimed.

## Hypothesis and failure-boundary register

The following boundaries must remain visible beside the claims they limit:

- In dimension one, coefficient-uniform strict lifting can fail by
  cancellation; \(V(q)=q^2\) and \(W(p)=-p^2/4\) are the retained exact
  counterexample.  The general lift therefore requires \(r\ge2\), while the
  headline has \(r=\ell+1\ge4\).
- Equality on a V or W normal-fan wall creates a tie.  No tie-breaking result
  is part of the theorem.
- The exact first gate is strict and coordinatewise.  A positive momentum
  seed outside it is not covered by the actual-degree lift.
- \(H=1\) removes the spike gap and collapses the quotient geometry.  A
  permutation with a shorter quotient orbit can shorten the phase period.
- A nonprimitive word has a smaller selector period even though an
  \(\ell\)-step product can still be written.
- Unequal support totals restore diagonal drift to selector comparisons and
  invalidate the frozen fan reduction.
- A zero exponent coordinate can delete a gradient monomial; positive
  characteristic can annihilate a derivative scalar; a zero displayed
  coefficient changes the collected support.
- A singleton side has vacuous uniqueness and no finite competitor gap; it
  is not excluded.
- Removing the marked root or the appropriate dictionary weakens decoder
  output exactly as specified above.
- An admissible \(m_0\) can have \(d_0>q_0\); the registered
  \((\ell,r,\rho,K,H)=(3,4,2,1,2)\) fixture gives the removed initial
  recurrence residual 800.

The retained planar decreasing-projective-map obstruction is explanatory
only: it motivates the higher-dimensional finite-order residual twist and is
not itself a priority or classification theorem.

## Proof ownership and canonical traceability

The mathematical proof is internal.  The canonical claim-to-proof ownership
is:

| Public claims | Controlling proof block |
|---|---|
| symplectic map and inverse | P1 |
| selected gradient and rank-one matrices | P2 |
| exact carry chamber | P3--P4 |
| coefficient-uniform leading-form survival | P5 |
| selector normal-fan iff | P6 |
| arbitrary primitive-word incidence realization and singleton convention | P7 |
| constant scalar forcing | P8 |
| ordered prefixes and monodromy | P9 |
| digit bounds and pair injectivity | P10 |
| decoder ladder | P11 |
| two least periods | P12 |
| recurrence formulas and start indices | P13 |

P1 is an independent map-level branch.  The weighted-degree branch begins at
P2, splits into P3--P5 carry/survival and P6--P7 selector/incidence branches,
then rejoins in the explicit actual-degree realization before P8--P13.  No
logical arrow originates in a finite fixture, computation, or literature
search miss.

## Citation ownership and novelty wording

External sources own only established background and adjacent classes:
polynomial symplectomorphisms and automorphism words; weighted degrees,
leading parts, monomial valuations, and chamber geometry; monomial-map degree
recurrences; max-plus state cycles and externally switched schedules;
structured cluster/sign itineraries and ordered tropical matrices; and
degree-growth or entropy context.  None is cited as proving this paper's
Hamiltonian-shear construction, two-fan iff, arbitrary endogenous pair-word
realization, strict coefficient-uniform lift, two least-period theorem, or
marked decoder.  Those obligations remain internally proved by P1--P13.

Bibliographic status must remain exact.  Versions of record anchor published
claims; primary preprints are labelled as preprints; the Meunier item is an
author-hosted preliminary manuscript with no invented venue, DOI, year, or
peer-review status; a precise use of Hasselblatt--Propp includes its
corrigendum; conjectural statements in the cluster literature are not
presented as theorems; and article numbers are not converted into fabricated
page ranges.

The only approved priority substance is that, after a bounded search of
public primary literature and official bibliographic records through
29 August 2026, the authors are unaware of a prior theorem containing the
full six-part conjunction: every rooted primitive pair word, one autonomous
map per word, an exact rational-polyhedral strict-selector criterion,
coefficient-uniform actual weighted-degree survival, separate least selector
and quotient periods, and marked support-word recovery with declared side
information.  This is a bounded-search statement, not proof of absence.  The
search and every mutable DOI/status must be refreshed at publication lock.

## Anonymous-publication and zero-execution firewall

The eventual anonymous article contains the mathematics, bounded literature
positioning, hand-derived examples and counterexamples, and scientific
limitations.  It contains no batch identifier, filesystem path, hash,
lifecycle event, reviewer identity or role, governance chronology, internal
score, author identity disclosure, or release history.

No script, notebook, CAS, solver, CPU/GPU scientific job, random test,
parameter sweep, dataset, generated figure, sampled-outcome table, or machine
certificate supports the theorem.  Registered numeric fixtures are manual
sanity checks, falsifiers, or boundary illustrations only.  They do not prove
a universal statement.  This lock authorizes no upload, submission, release,
external message, or other external effect.

## Exact anonymous content-page allocation

The sole controlling allocation is:

| Anonymous section | Pages |
|---|---:|
| Abstract | 0.5 |
| Introduction and bounded positioning | 2.5 |
| Symplectic family and exact weighted-degree transport | 3.0 |
| Normal-fan iff | 4.0 |
| Incidence realization of primitive words | 4.0 |
| Strict carries and leading forms | 3.5 |
| Ordered monodromy and decoding | 4.0 |
| Least periods, scalar boundaries, and counterexamples | 3.5 |
| Limitations and conclusion | 1.5 |
| **Total anonymous content** | **26.5** |

The six mathematical-core entries total exactly

\[
 3.0+4.0+4.0+3.5+4.0+3.5=22.0
\]

pages, and the three peripheral entries total exactly

\[
 0.5+2.5+1.5=4.5
\]

pages, so the controlling mass is \(22.0+4.5=26.5\).  References are
excluded.  The proof package's 21.5-page table is a distinct approximate
proof-placement subtotal with different grouping conventions; it is not an
addend to 4.5 or to either controlling subtotal.  The candidate reviewers'
25.5- and 26.0-page estimates remain historical estimates only.

## Locked exclusions

The article makes no claim of:

- one universal map, one map per length, or fixed dimension for arbitrary
  length;
- ordinary-total-degree realization or a free-standing exact-degree,
  algebraic-degree, or dynamical-degree theorem beyond the stated actual
  weighted-degree transport;
- scalar word decoding, scalar-trajectory separation of words, or minimal
  scalar recurrence;
- literal-label recovery without the labelled support dictionary, or rooted
  recovery without a marked phase;
- periodic polynomial state;
- entropy equality, algebraic or topological entropy, integrability, generic
  nonconjugacy, inverse reciprocity, or cohomological spectrum;
- positive-characteristic validity, zero-coordinate support survival, or a
  cancellation classification outside the stated hypotheses; or
- absolute priority, a first/only/unprecedented result, or completeness of
  the bounded literature search.

These exclusions and every preceding hypothesis are part of the source lock,
not optional exposition.

BATCH07_PAPER28_SOURCE_LOCK_FROZEN
