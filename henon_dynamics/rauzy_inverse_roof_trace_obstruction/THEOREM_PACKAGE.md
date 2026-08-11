# HCS-C30 theorem package: inverse dynamics, roof, and trace obstruction

## 1. Decision and scope

HCS-C29 remains a correct finite symmetric-graph and finite-Weil determinant
calculation.  HCS-C30 closes its proposed promotion to the original
Rauzy--Veech/AGY dynamics.  The decisive identity-holonomy words have no
positive length-cone or transfer-branch orbit in **any cyclic phase**; a
genuine inverse arrow cannot carry a second positive value of an additive
time cocycle; and faithful forward/inverse composition operators cannot form
an ordinary nuclear Hashimoto operator on one infinite-dimensional space.

The Route-A decision for that promotion is

```text
(A1_FAIL, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)
overall: ROUTE_A_REJECTED_FOR_DYNAMICAL_PROMOTION
```

This does not retract the C29 matrix relations or its finite group-trace
determinant germ.  It proves that the latter belongs to a newly declared
symmetric graph suspension, not to the AGY natural extension.

## 2. Source lock, chronology, and three matrix actions

The release certificate locks the C25, C26, and C29 certificates and theorem
packages by SHA-256.  No prime table, Riemann-zero data, fitted weight, or
averaged transition matrix is used.

For a token word

\[
w=e_1\cdots e_n,
\qquad
B_w=B(e_n)\cdots B(e_1),
\]

later events multiply on the left.  A positive token has its source matrix
\(B(e)\), while a formal inverse token has the exact integer inverse
\(B(e)^{-1}\).

### Proposition 2.1 -- raw identity is source-level, not a finite-fibre artifact

For a C25 arrow from state \(s(e)\) to state \(t(e)\), the frozen frames obey

\[
g_e=S_{t(e)}^{-1}B(e)S_{s(e)}.
\]

The same equality holds for formal inverses.  Along a closed mixed path based
at \(v\), the frames telescope:

\[
g_w=S_v^{-1}B_wS_v.
\]

The source-locked C29 certificate records the fixed-frame identities, while
the C30 producer independently replays the raw products and verifies

\[
B_{C_1}=B_{C_2}=B_{W_{24}}=I_4.
\]

For \(W_{24}\), this is also checked directly in the source C26 \(A,B,C\)
alphabet.  The implication is used only for closed paths.

### Three actions that must not be conflated

1. **Genuine forward Rauzy length action.**  AGY's length convention is

   \[
   \lambda_k=B(e_k)^{-\mathsf T}\lambda_{k-1}.
   \]

   Thus a positive token \(a\) uses \(B(a)^{-\mathsf T}\), while a formal
   inverse token \(a^{-1}\) uses \(B(a)^{\mathsf T}\).  For each cyclic
   rotation of a raw path word, the exact prefixes are

   \[
   P_0=I,
   \qquad
   P_k=B(e_k)^{-\mathsf T}P_{k-1}.
   \]

2. **Transfer/projective inverse-branch action.**  Contravariance reverses a
   raw path rotation.  For \(u_1\cdots u_n=e_n\cdots e_1\),

   \[
   Q_0=I,
   \qquad
   Q_k=B(u_k)^{\mathsf T}Q_{k-1}.
   \]

   The C26 `holonomy_order_word` is the corresponding transfer application
   order; `later_on_left_path_order_word` is its raw path order.

3. **Raw covariant homology control.**  The auxiliary recurrence

   \[
   H_0=I,
   \qquad
   H_k=B(e_k)H_{k-1}
   \]

   acts on homology/cocycle coordinates, not on Rauzy lengths.  It is retained
   as a convention sentinel, never as an AGY orbit test.

A positive-domain orbit for the first or second action requires one vector
\(x\in\mathbb R_{>0}^{4}\) for which every coordinate of every corresponding
prefix is strictly positive.  C30 checks every cyclic phase independently.

## 3. Exact all-phase cone obstruction

The certificate uses two kinds of exact Farkas descriptors.  A `NEG_ROW` is a
required coordinate row whose entries are all nonpositive and not all zero.
A `POSITIVE_DEPENDENCE` records positive integer coefficients with

\[
\sum_j c_j r_j=0.
\]

Either descriptor contradicts strict positivity without floating point or a
linear-programming tolerance.

### Theorem 3.1 -- C25 word \(C_1\) fails in all cyclic phases

Let

\[
C_1=(0t,1b,0t^{-1},0b,3t,0b^{-1}).
\]

In forward-length phase zero, the step-one fourth-coordinate row and the
step-four second-coordinate row are

\[
(0,-1,0,1),
\qquad
(0,1,0,-1).
\]

Both would have to be positive, but they sum to zero.  Canonical exact
descriptors prove that all six forward-length phases are infeasible.  A
separate contravariant replay proves that all six transfer phases are also
infeasible.  Hence \(C_1\) is not a positive Rauzy/AGY periodic orbit.

### Theorem 3.2 -- C25 word \(C_2\) fails in all cyclic phases

Let

\[
C_2=(4t,6b^{-1},6t,5b,6t^{-1},6b).
\]

Forward-length phase zero contains the required row

\[
(-1,0,0,0)
\]

at step three, so it is already negative on every \(x>0\).  Canonical exact
descriptors give six failures out of six forward-length phases and six out of
six transfer phases.  Thus \(C_2\) is not a positive Rauzy/AGY periodic orbit.

### Theorem 3.3 -- C26 word \(W_{24}\) fails in all cyclic phases

For the genuine forward-length action, phase zero has at step eight the
required coordinate row

\[
(-11430,-460520,-3353,-456200),
\]

which is strictly negative on every \(x>0\).  The complete phase census gives

\[
24/24\quad\text{forward-length phases infeasible}.
\]

Fifteen canonical descriptors are selected by the `NEG_ROW` rule; the other
nine are positive dependences, each an opposite pair \(r,-r\).  The distinct
support-size census is fourteen five-term certificates and ten two-term
certificates; it must not be confused with the type census.

The independent transfer replay also gives \(24/24\) failures.  Its phase-zero
application begins with \(A^{-1},C,B^{-1}\), and the second-coordinate row of
the third prefix is

\[
(-984333,-498163,-999116,-479060).
\]

Therefore no cyclic basepoint turns \(W_{24}\) into an AGY positive-domain
orbit.

### Proposition 3.4 -- the covariant homology control separates conventions

Under the raw covariant recurrence \(H_k=B(e_k)H_{k-1}\), the words \(C_1\)
and \(C_2\) admit the positive integer witnesses

\[
(1,2,1,1),
\qquad
(1,1,3,1),
\]

respectively.  Every raw-covariant prefix of the indicated witness remains
positive.  These are homology-zigzag controls, not length or transfer orbits.
Their existence confirms that the two dynamical gates were not computed with
the wrong covariant action.  The raw C26 control is itself infeasible.

### Corollary 3.5 -- formal-cycle boundary

The three decisive C29 words are formal symmetric-path
**identity-holonomy** cycles, not geometric AGY periodic orbits.  Their C29
finite trace-log contribution remains algebraically defined, but it has no
positive Rauzy-length interpretation.  A kernel word of the matrix holonomy
need not be the unit arrow of the free path groupoid.

## 4. Roof-cocycle obstruction and identity trichotomy

### Theorem 4.1 -- an inverse arrow has opposite groupoid time

Let \(\tau\) be a real additive one-cocycle on a groupoid.  Then

\[
\tau(1_x)=0,
\qquad
\tau(g^{-1})=-\tau(g).
\]

Consequently no symmetric generating set can satisfy both cocycle
compatibility and \(\tau(e),\tau(e^{-1})>0\).

For the normalized projective action on the simplex, put

\[
\ell(x)=\sum_{j=1}^{4}x_j,
\qquad
h_M(x)=\frac{Mx}{\ell(Mx)},
\qquad
r_M(x)=\log\ell(Mx).
\]

Where defined,

\[
r_{MN}(x)=r_N(x)+r_M(h_Nx),
\qquad
r_{M^{-1}}(h_Mx)=-r_M(x).
\]

These identities follow directly from projective normalization.

### Proposition 4.2 -- identity arrow, identity holonomy, and zero period differ

Three statements must be kept separate.

1. If a path is the unit arrow of the groupoid, every additive cocycle
   vanishes on it.
2. If only its matrix holonomy is \(I\), an arbitrary edge-constant
   antisymmetric cocycle need not vanish.  The signed abelianizations of
   \(C_1\) and \(C_2\) are respectively \(1b+3t\) and \(4t+5b\).
3. If a cocycle factors through the projective matrix action and all prefixes
   are defined, a holonomy identity telescopes:

   \[
   \sum_{k=1}^{n}r_{B(e_k)}(x_{k-1})
   =\log\frac{\ell(B_wx)}{\ell(x)}=0.
   \]

The C26 word also has zero signed count in each of \(A,B,C\), so every
edge-constant antisymmetric cocycle vanishes on that particular word.

### Corollary 4.3 -- a positive symmetric length changes the system

An assignment

\[
L(e)=L(e^{-1})>0
\]

defines a valid positive roof over the finite non-backtracking symbol shift.
There \(e^{-1}\) is another alphabet symbol; one cannot simultaneously impose
the path-groupoid cancellation \(ee^{-1}=1\), because the proposed length of
that word is \(2L(e)\), not zero.  The result is a new graph-geodesic
suspension, not the AGY natural extension or its return-time roof.

### Corollary 4.4 -- zero-time repetitions are singular in a flow Euler factor

On any enlarged domain where an identity-holonomy word supports the
projective normalizer, its period and every repeated period are zero.  A
flow-style primitive factor would contain

\[
(1-e^{-s\cdot0})^{-1},
\]

while its logarithmic repetitions give \(\sum_{m\ge1}1/m\).  Replacing the
period by unit graph length yields the valid C29 Hashimoto \(u\)-germ, but only
after making the dynamical change in Corollary 4.3.

## 5. Same-space nuclearity obstruction

### Theorem 5.1 -- faithful bounded inverses cannot form a compact Hashimoto operator

Let \(X\) be an infinite-dimensional Banach space.  Suppose every oriented
edge is represented by a bounded operator \(U_e\in\mathcal B(X)\) with

\[
U_{e^{-1}}U_e=I_X.
\]

Let \(\mathbb B\) be the finite non-backtracking block operator on
\(X^{E^\pm}\), with a nonzero scalar multiple of \(U_f\) in the block for
each legal transition \(e\to f\).  Assume every \(f\) has a legal predecessor,
as it does in the C25 and C26 symmetric graphs.  Then \(\mathbb B\) is neither
compact nor nuclear/trace class.

#### Proof

Choose a legal predecessor \(e\) of \(f\).  Coordinate injection and
projection give

\[
P_f\mathbb B J_e=c_{f,e}U_f,
\qquad c_{f,e}\ne0.
\]

If \(\mathbb B\) belonged to either operator ideal, every \(U_f\) would
belong to the same ideal.  The ideal property would then put

\[
I_X=U_{f^{-1}}U_f
\]

in that ideal, impossible on infinite-dimensional \(X\).  \(\square\)

The same argument applies to \(H_+\to H_-\to H_+\) if both arrows are compact
and their product is the identity.  Opposite anisotropies escape only when the
two arrows are not asserted to be compact bounded inverses on one common
realization.

### Corollary 5.2 -- marked coefficient isolation closes cancellation

Suppose an edge- or occurrence-resolved family \(\mathbb B(\mathbf z)\) were
holomorphic in nuclear norm.  Its Cauchy coefficients would be nuclear.  A
cyclic layer lift isolates a relation-word coefficient.  For the reciprocal
projective weight this coefficient is the identity; after imposing a bounded
positive roof it is a boundedly invertible multiplication operator.  Neither
is compact.  Thus cancellation in an unmarked operator sum cannot create a
coefficientwise nuclear word theorem.

## 6. Positive-domain/flat-trace dichotomy

### Theorem 6.1 -- empty domain or a degenerate fixed family

For each certified C29 identity-holonomy word \(W\), the standard geometric
promotion meets the following dichotomy.

1. On the source positive Rauzy domain, the complete word has no orbit by
   Section 3.
2. If the projective domain is enlarged so that all prefixes are defined,
   \(B_W=I\) gives

   \[
   h_W=\operatorname{id},
   \qquad
   Dh_W=I.
   \]

   Its fixed set is the full domain and

   \[
   \det(I-Dh_W)=0.
   \]

Hence the standard isolated-hyperbolic fixed-point atom

\[
\frac{w_W(x_W)}{\det(I-Dh_W(x_W))}
\]

does not exist for the words producing the C29 signal.  Their powers retain
derivative \(I\), so no uniform contraction or hyperbolic periodic-data bound
can hold for every admissible word on such an enlarged domain.

This theorem does not rule out every clean-fixed-manifold or distributional
regularization.  Such a construction would be a new zeta prescription and
would need a separate theorem; it could not silently retain the C29 discrete
isolated-orbit interpretation.

## 7. What survives

The finite C29 operator is a matrix over a group von Neumann algebra.  Its
small-\(u\) trace-log

\[
D_\infty(u)
=\exp\!\left[-\sum_{n\ge1}\frac{N_nu^n}{n}\right]
\]

is valid and nonconstant.  Its trace is the finite edge-matrix trace tensored
with the group trace, not the ordinary Hilbert-space trace on \(\ell^2(G)\),
and the regular operator need not be compact.  Rephrasing this object does not
create an ordinary Fredholm or positive Fuglede--Kadison determinant theorem.

Thus the exact decisions are

```text
ORIGINAL_AGY_NATURAL_EXTENSION_IDENTIFICATION = FAIL
INTRINSIC_STRICTLY_POSITIVE_TWO_WAY_GROUPOID_ROOF = IMPOSSIBLE
NEW_SYMMETRIC_HASHIMOTO_SUSPENSION = VALID_BUT_DIFFERENT_SYSTEM
STANDARD_ISOLATED_ORBIT_FLAT_TRACE_FOR_C29_WORDS = FAIL
GENERAL_CLEAN_FIXED_SET_REGULARIZATION = OPEN
```

## 8. Route-A evaluation

- **A1_FAIL.**  The C29 identity-holonomy words are not positive-domain
  periodic orbits of the proposed AGY promotion.  The graph suspension has a
  declared unit clock, not a recovered AGY clock or arithmetic primitive law.
- **A2_FAIL.**  No ordinary nuclear determinant or standard isolated-orbit
  flat trace realizes those words.  The finite C29 group-trace germ survives
  as a different object.
- **A3_FAIL.**  The promotion fails before analytic continuation, functional
  equation, or a counting law becomes meaningful.
- **A4_FORMAL_HINT.**  Exact matrix-kernel relations and finite Weil traces may
  still suggest a different system in which the base orbit is hyperbolic and
  only the fibre holonomy is the identity.

Route B is not authorized.

## 9. Literature boundary and nonduplicative pivot

AGY supplies the positive forward induced map, its length action, and its
return-time roof; it does not supply positive time for formal inverse tokens:

- Avila, Gouëzel, and Yoccoz,
  [*Exponential mixing for the Teichmüller flow*](https://arxiv.org/abs/math/0511614),
  especially Sections 3.1.3, 3.2, 3.3.1, and 4.1.

Classical symbolic suspension theory begins with a genuine positive roof over
an actual shift:

- Parry and Pollicott,
  [*Zeta functions and the periodic orbit structure of hyperbolic dynamics*](https://smf.emath.fr/system/files/filepdf/AST_1990__187-188__1_0.pdf),
  Chapter 6.

Anisotropic and microlocal flat-trace theories are genuine escape mechanisms
for hyperbolic maps and flows, but they do not turn an identity map with a
full fixed domain into an isolated hyperbolic orbit:

- Gouëzel and Liverani,
  [*Banach spaces adapted to Anosov systems*](https://arxiv.org/abs/math/0405278);
- Giulietti, Liverani, and Pollicott,
  [*Anosov flows and dynamical zeta functions*](https://doi.org/10.4007/annals.2013.178.2.6),
  with their [erratum](https://arxiv.org/abs/2203.04917);
- Dyatlov and Zworski,
  [*Dynamical zeta functions for Anosov flows via microlocal analysis*](https://arxiv.org/abs/1306.4203).

Analytic stable--unstable pinning constructions avoid Theorem 5.1 because
they use contracting cross maps and partial adjoints rather than realizing a
map and its inverse as compact operators on the same space:

- Fried,
  [*Meromorphic zeta functions for analytic flows*](https://doi.org/10.1007/BF02099469);
- Baladi, Pujals, and Sambarino,
  [*Dynamical zeta functions for analytic surface diffeomorphisms with dominated splitting*](https://arxiv.org/abs/math/0307045).

The corresponding Hénon \(H_6\) mixed-domain and one-step pinning
infrastructure already exists in `henon_pinning_trace_obstruction`; rebuilding
generic Fried/Rugh machinery would duplicate prior local work.  The next
nonduplicative large gate is a quantitative common-space composition and
determinant-tail theorem, or a genuinely new twist/graded all-word theorem,
for that certified hyperbolic system.

The external novelty claim is deliberately search-bounded.  The new local
result is the source-locked all-phase cone/Farkas obstruction and its precise
interaction with roof, repetition, and trace semantics.
