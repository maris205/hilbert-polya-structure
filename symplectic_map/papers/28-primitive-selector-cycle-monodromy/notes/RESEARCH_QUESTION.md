# Paper 28 research question and theorem contract

## Central question

Given an arbitrary rooted primitive word of paired Newton-selector labels,
can one build a single autonomous polynomial symplectomorphism whose actual
iterated weighted degrees select exactly that word, classify the admissible
strict seeds by an exact normal-fan condition, and recover the phase-resolved
support word from the exact period monodromy?

The desired answer is family-wise: one explicitly constructed map for each
word.  The project does not seek one universal map, one map per length, or a
fixed-dimensional family accommodating unbounded word length.

## Input data and conventions

The input is a rooted primitive cyclic pair word

\[
 \mathsf w=((a_0,b_0),\ldots,(a_{\ell-1},b_{\ell-1})),
 \qquad \ell\ge3,
\]

over the finite alphabets of labels that actually occur.  Repeated labels and
a singleton alphabet on either component are allowed.  “Primitive” means
that the pair word has no smaller cyclic period.  A marked phase zero turns
the cyclic word into a rooted word.

Set \(r=\ell+1\).  There are \(r\) symplectic coordinate pairs, hence
ambient affine dimension \(2r=2(\ell+1)\).  Moving coordinates are indexed by
\(I_{\mathrm{mov}}=\{0,\ldots,\ell-1\}\), and \(\star\) denotes a separate
fixed coordinate.  The permutation \(P\) cycles the moving coordinates and
fixes \(\star\).

All polynomial statements are over a characteristic-zero field.  Collected
support vectors have integer coordinates at least two, and every displayed
coefficient is nonzero.  Weighted-degree seeds are positive.

## Exact theorem target

For every input \(\mathsf w\), choose integers
\(H\ge2\), \(\rho\ge2\), and \(K\ge1\), and define

\[
 u_0=\mathbf1+(H-1)e_0,
\]

\[
 S_a=\{j:a_j=a\},\qquad T_b=\{j:b_j=b\},
\]

\[
 \alpha_a=\rho\mathbf1+K\sum_{j\in S_a}e_j
 +K(\ell-|S_a|)e_\star,
\]

\[
 \beta_b=\rho\mathbf1+K\sum_{j\notin T_b}e_j
 +K|T_b|e_\star.
\]

All exponent totals equal

\[
 D=\rho r+K\ell.
\]

For arbitrary nonzero coefficients on these collected supports, form

\[
 V(q)=\sum_a A_aq^{\alpha_a},\qquad
 W(p)=\sum_b B_bp^{\beta_b},
\]

\[
 S_V(q,p)=(q,p+\nabla V(q)),\quad
 T_W(q,p)=(q+\nabla W(p),p),
\]

and

\[
 F_{\mathsf w}=\Pi_P\circ T_W\circ S_V,
 \qquad \Pi_P(q,p)=(Pq,Pp).
\]

The article must prove all of the following conjunctively.

### T1. Autonomous polynomial symplectomorphism

\(F_{\mathsf w}\) is a polynomial symplectomorphism with an explicit
polynomial inverse.  Symplecticity follows from symmetric Hessian blocks and
the simultaneous coordinate permutation, not from a formal degree model.

### T2. Exact general selector iff

In the general positive equal-total support class with \(r\ge2\), a positive
position-weight seed realizes a prescribed strict selector word exactly when
it belongs to the corresponding intersection of pulled-back V-maximizer and
W-minimizer open normal cones.  Singleton support gives an empty family of
competitor inequalities and therefore the full positive weight space.

This selector iff concerns position weights.  It is logically separate from
the momentum condition needed for the strict actual-degree lift.

### T3. Every primitive pair word is realized

At phase \(j\), the spike vector \(P^ju_0\) makes \(\alpha_{a_j}\) the unique
V maximizer and \(\beta_{b_j}\) the unique W minimizer.  Against every
competitor that actually exists, the score difference is exactly

\[
 g=K(H-1)>0.
\]

No finite gap is assigned on a singleton side; uniqueness there is vacuous.
The supports are assembled once, so the selector word is endogenous to the
one autonomous map rather than imposed by an external switching schedule.

### T4. Exact strict actual-degree chamber

Let \(m_0\) be the initial momentum-weight vector and let the phase-zero V
selector be \(\alpha_{a_0}\).  The strict lift used in the theorem holds
exactly under the coordinatewise gate

\[
 0<m_0<A_{\alpha_{a_0}}u_0,
 \qquad A_\alpha=\mathbf1\alpha^{\mathsf T}-I.
\]

The subcone \(0<m_0\le u_0\) is convenient and sufficient, but it is not
necessary.  From the first full step onward the position degrees strictly
dominate the momentum degrees.  Unique selected monomials, nonzero derivative
scalars in characteristic zero, and strict carries then give the actual
polynomial weighted degrees for every nonzero coefficient tuple.

### T5. Exact ordered cocycle

For

\[
 c_{a,b}=(D-1)\alpha_a-\beta_b,qquad
 \lambda=(D-1)^2,
\]

the selected complete position matrix is

\[
 C_{a,b}=P+\mathbf1c_{a,b}^{\mathsf T}.
\]

If \(C_j=C_{a_j,b_j}\) and
\(Q_s=C_{s-1}\cdots C_0\), then

\[
 Q_s=P^s+\mathbf1R_s^{\mathsf T},
\]

\[
 R_s^{\mathsf T}=\sum_{j=0}^{s-1}
 \lambda^{s-1-j}c_j^{\mathsf T}P^j.
\]

Since \(P^\ell=I\), the period monodromy is
\(M_{\mathsf w}=I+\mathbf1R_\ell^{\mathsf T}\), with its characteristic
polynomial and powers derived explicitly.

### T6. Decoder with exact information boundary

Every coordinate of every \(c_{a,b}\) lies strictly between 0 and \(\lambda\),
and \((a,b)\mapsto c_{a,b}\) is injective at the support-vector level.  Given
\(M_{\mathsf w}\), \(P\), \(\lambda\), \(\ell\), and marked phase zero,
coordinatewise base-\(\lambda\) expansion recovers the rooted ordered
support-vector word.  Given also the labelled support dictionary, it recovers
the literal rooted label-pair word.

Without literal names, labels are determined only up to independent
renaming.  Without phase zero, only the cyclic rotation class is intrinsic.
The scalar degree trajectory is not a word decoder.

### T7. Two least periods

The primitive pair word has least selector period \(\ell\).  The position
weight modulo the diagonal line has least period \(\ell\) because the fixed
star coordinate forces any diagonal displacement to vanish while the unique
moving spike changes position.  These are not claims that the polynomial
state is periodic.

### T8. Precisely indexed scalar consequences

Writing

\[
 u_n=P^nu_0+t_n\mathbf1,\qquad
 t_{n+1}=\lambda t_n+\mu,
\]

the position maximum \(q_n=H+t_n\) obeys its order-two recurrence from
\(n=0\).  Moving coordinates

\[
 y_n^{(i)}=1+(H-1)\mathbf1_{\{n\equiv i\pmod\ell\}}+t_n
\]

and the star coordinate \(y_n^{(\star)}=1+t_n\) obey the stated
\((E^\ell-1)(E-\lambda)\) annihilator from \(n=0\).  The complete-state
maximum \(d_n\) equals \(q_n\) only from \(n\ge1\); its same recurrence begins
at \(n\ge1\) and holds at \(n=0\) iff \(d_0=q_0\).  No recurrence is claimed
minimal.

## Scientific contribution boundary

Weighted-degree chambers, monomial valuations, polynomial
symplectomorphisms, max-plus periodic orbits, switched schedules, cluster-map
tropical recurrences, monomial-map degree recurrences, ordered products, and
base expansions are established ingredients.  The claimed contribution is
the proved conjunction of arbitrary primitive rooted pair-word realization,
autonomous Hamiltonian-shear lifting, exact strict normal-fan feasibility,
coefficient-uniform actual-degree survival, two least periods, and a marked
support-word-decoding monodromy.

The literature statement is priority-safe: after a bounded primary-source
search through 2026-08-29, the authors are unaware of a prior theorem with
that entire conjunction.  This is not an absolute first/only claim.

## Excluded claims

The project makes no claim of a universal map, fixed dimension, ordinary
total-degree universality, periodic polynomial states, scalar word decoding,
minimal scalar recurrence, entropy equality, dynamical degree,
integrability, generic nonconjugacy, inverse reciprocity, cohomological
spectrum, positive-characteristic validity, zero-coordinate support
survival, or absolute priority.

## Completion test

The research question is answered only if every T1--T8 clause is proved in
the anonymous main body, every hypothesis has a sharp boundary or
counterexample, and a fresh source-design reviewer reports an all-zero
finding census.  The credible target is 22--30 anonymous content pages, with
zero theorem dependence on computation and no governance material in the
public manuscript.

BATCH07_PAPER28_RESEARCH_QUESTION_FROZEN
