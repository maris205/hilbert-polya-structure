# An expanding boundary jet blocks a rich Banach return representation

**Paper ID:** 199-boundary-jet-return-obstruction  
**Candidate ID:** AQC-20260916-BJO01  
**Research date:** 2026-09-16  
**Status:** STOP — NO BOUNDED RETURN ON A BANACH SPACE WITH FULL CONTINUOUS BOUNDARY JETS; NATURALNESS OPEN.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

## Abstract

The complete finite-support arithmetic cone flow of 193 and its actual
return are unchanged. We test a Banach space of continuous observables
on its whole section with continuous right boundary derivatives of all
orders and surjective finite jet maps. For any fixed complex s with
Re(s)>1, its actual weighted forward return cannot be both invariant
and bounded on such a space. The retained 2/3 edge has an expanding
return at the q_3 endpoint. Its finite dual-jet actions force
eigenvalues 3^(-s)(3/2)^j of arbitrarily large modulus, contradicting
boundedness. These are dual-jet eigenvalues, not physical states or
extra periodic orbits. The argument does not exclude all fixed Hilbert
representations, finite differentiability or nonsmooth spaces. The
previous power-observable spaces fail the new jet hypotheses, so their
positive determinant theorem is not contradicted. This realization
contract stops before compactness, traces or determinants.

## 1. Frozen object, source and exact question

The [card](candidate-card.md) was frozen before this proof. It is an
analytic realization audit, not a claim that a new Banach space already
exists. The old geometric dependency is the fully read
[193 construction](../193-indecomposable-radial-quotient/paper.md).
Its source is the real monoid algebra of all positive integers,
e_m e_n=e_(mn), with nonunit ideal I and Q=I/I^2. Products of two
nonunits span exactly the composite coordinates; thus the atoms A
of Q are the derived prime classes. No prime table is the input.

Retain the entire positive nonzero finite-support cone P, its topology
from all coefficient norms with weights a^k, D(q_a)=a q_a, the
Hausdorff quotient X=P/<D> and the complete flow phi_t[v]=[exp(t)v].
The actual global section and return proved for this same X are

\[
 S=\{u=\sum_a u_aq_a:u_a\ge0,\ \text{finite support},\ \sum_a u_a=1\},
 \quad c(u)=\sum_a u_a/a,\quad
 F(u)_a=\frac{u_a}{a c(u)},\quad \tau(u)=-\log c(u).
 \tag{1}
\]

The roof is positive and at least log 2. All mixed states and boundary
vertices are retained. The full old flow has one log-prime circle per
atom and all repetitions; no periodic ledger is replaced in this audit.

| Field | Same-object definition | Boundary |
| --- | --- | --- |
| Source lineage | Integer factor admissibility -> indecomposables -> positive carrier -> actual return -> observable regularity audit | A stated replacement of prime-symbolic observables, not a Logistic/Henon conjugacy |
| Complete geometric owner | Original P, topology, X and radial flow of 193 | No completion, changed topology or selected edge carrier |
| Actual return | Equation (1), original nonconstant roof | Not reverse time, an inverse-branch sum or an independent diagonal model |
| Realization obligation | Full-S complex Banach observables with the jet conditions below | Existence and bounded return are questions, not assumptions proved by a name |
| Parameter | One fixed s with Re(s)>1, including s=2 | No parameter fitting or uniform-in-s estimate needed |
| Later analytic/physical owner | No determinant, Hilbert generator, Hamiltonian or quantum object supplied | A failed representation does not invalidate the old flow |

The [lineage guide](../../docs/prior_work/README.md) motivates keeping
the symbolic arithmetic observable tied to its actual operator action.
Its external-paper descriptions are not proof premises here. No
literature novelty, target-zero identity or formal Route pass is claimed.

## 2. Exact Banach and jet hypotheses

Let B be any complex Banach space consisting injectively of continuous
functions on the entire S. On the actual states
u(t)=t q_2+(1-t)q_3, 0<=t<=1, write g_f(t)=f(u(t)). Require:

1. Every g_f is smooth from the right near zero, with derivatives
   of every order continuous up to zero.
2. Each delta_j(f)=g_f^(j)(0), j>=0, is a continuous linear
   functional on B.
3. Every J_m f=(delta_0(f),...,delta_m(f)) maps B onto C^(m+1).

The third condition means every finite list of boundary derivatives
can be independently realized. It is implied, for example, by
containing every coordinate polynomial P(u_2), if the first two
conditions also hold. There is no common bound on the norms of the
delta_j, no claim of surjectivity onto an infinite sequence space,
and no requirement that B embed continuously into C_b(S).

For a fixed s in the frozen half-plane, test the actual formula

\[
 (\mathcal L_s f)(u)=c(u)^s f(Fu),
 \qquad c(u)^s=\exp(s\log c(u)).
 \tag{2}
\]

The question is whether (2) preserves B and is bounded there. Merely
writing (2) does not prove invariance, continuity in the B norm,
compactness or trace class. A fixed physical space for a family of s
would first have to pass this single-parameter test.

## 3. The actual edge action and its finite dual jets

Substitution into (1), on every retained edge state, gives

\[
 c(u(t))=\frac{t+2}{6},\quad
 F(u(t))=u(h(t)),\quad h(t)=\frac{3t}{t+2}.
 \tag{3}
\]

Thus h(0)=0 and h'(0)=3/2. With w_s(t)=((t+2)/6)^s, the
restriction of (2) is exactly w_s(t)g_f(h(t)), and w_s(0)=3^(-s)
is nonzero. The real-positive branch makes w_s smooth near zero.
Only a right neighborhood is used; no fictitious negative states
are inserted into S. The edge is a set of test states, not the
replacement phase space.

Assume for contradiction that (2) preserves B boundedly, and let
L_s' be its bounded action on continuous complex-linear functionals:
L_s' ell=ell composed with L_s. Repeated differentiation gives

\[
 L_s'\delta_j
   =\lambda_j\delta_j+\sum_{i<j}A_{ji}\delta_i,
 \qquad \lambda_j=3^{-s}(3/2)^j.
 \tag{4}
\]

For clarity, the leading coefficient needs no unproved differential
operator theorem. Write the right Taylor polynomial of g_f through
order j. In w_s(t)g_f(h(t)), the term involving g_f^(j)(0)
has leading coefficient w_s(0)h'(0)^j/j!; multiplication by j!
gives (4). All other order-j terms involve derivatives of g_f of
order less than j. The smooth one-sided Taylor remainder justifies
the same coefficient calculation for every f in B.

Surjectivity of J_m implies that delta_0,...,delta_m are linearly
independent: a vanishing linear combination can be evaluated on
each prescribed unit jet. Their span V_m in B' is therefore an
(m+1)-dimensional invariant space for L_s'. Its triangular matrix
has diagonal lambda_0,...,lambda_m. In particular lambda_m is an
eigenvalue with a nonzero continuous eigenfunctional ell_m in V_m.
One can obtain it directly as delta_m plus lower derivatives by
successively cancelling lower terms in (4); the denominators
lambda_m-lambda_i are nonzero for i<m.

## 4. The bounded-realization obstruction

**Theorem.** For every fixed s with Re(s)>1, no B satisfying the
three jet conditions can make its actual forward rule (2) both
invariant and bounded. This rules out the frozen jet-rich Banach
realization already at boundedness, before any compactness or
ordinary nuclear/trace-class determinant claim.

**Proof.** Each nonzero eigenfunctional supplied above satisfies

\[
 |\lambda_m|\,\|\ell_m\|
   =\|L_s'\ell_m\|
   \le\|\mathcal L_s\|\,\|\ell_m\|.
\]

Cancel its positive finite norm. For every m>=0 this gives

\[
 \|\mathcal L_s\|\ge 3^{-\operatorname{Re}s}(3/2)^m.
 \tag{5}
\]

The right-hand side tends to infinity, contradicting boundedness.
No bound on the separate derivative functionals was assumed; their
possibly large norms cancel. No numerical cutoff substitutes for the
all-m argument. QED.

The theorem is a nonexistence result for the combined obligations,
not a construction of an unbounded operator on an unspecified domain.
A particular proposed B may already fail invariance. Nor does it
identify ell_m with a physical eigenfunction, an additional closed
orbit or a Riemann-zero state. They belong to finite subspaces of the
continuous dual used to disprove boundedness. No conclusion that
I-L_s is or is not a Fredholm operator is asserted.

## 5. Controls and precise escape boundaries

### Finite jets are not all jets

For only orders through m, the argument yields a finite lower bound,
not a contradiction. A direct local control illustrates the distinction.
On the two-atom edge alone, choose an integer s=d>=2 and polynomials
of degree at most d. For P(t)=sum_(j=0)^d b_j t^j, the edge rule is

\[
 w_d(t)P(h(t))
  =6^{-d}\sum_{j=0}^d b_j 3^j t^j(t+2)^{d-j}.
 \tag{6}
\]

It stays in that finite-dimensional polynomial space and is bounded
for every norm there. Its jets through d are all realizable, but not
arbitrary higher jets. This is an EXTERNAL LOCAL CONTROL, not a new
full-S candidate or permission to delete the other states.

### The 197 positive representation does not satisfy these hypotheses

By its explicit definition, every 197 observable restricts to

\[
 g_f(t)=b_2 t^s+b_3(1-t)^s.
 \tag{7}
\]

Already at first order, Re(s)>1 gives delta_0(f)=b_3 and
delta_1(f)=-s b_3. Thus J_1 has its image in the proper line
{(z,-s z):z in C}, so it is not onto for any s in the half-plane.
This direct first-order control was also identified in the separate
card-stage derivation before final manuscript review.

If s is not an integer, t^s is not smooth to every order at zero:
choose an integer order greater than Re(s); its derivative has a
nonzero coefficient and unbounded modulus t^(Re(s)-j). This
includes nonreal s whose real part is integral. If s=d>=2 is an
integer, all edge functions in (7) lie in a space of dimension at
most two, so finite jet maps with target dimension at least three
cannot be onto. Thus the theorem leaves
[197's proved determinant](../197-section-power-transfer/paper.md)
intact. Separating states is weaker than realizing arbitrary local
variations of an observable.

### Bounded continuous functions do not have continuous derivative access

On all C_b(S) the actual rule is bounded with exact norm 2^(-Re(s)):
c<=1/2 gives the upper bound, and f=1 at q_2 attains it. Even
on its smooth edge observables, delta_1 is not sup-norm continuous.
The globally defined functions f_N(u)=sin(Nu_2)/N have norm at most
1/N, but delta_1(f_N)=1. There is no conflict with either this
boundedness or the separately proved noncompactness in
[198](../198-cone-extension-frontier/paper.md).

### Contracting analytic germs provide a positive local control

Let f(z)=sum_(j>=0)b_j z^j on the open unit disk with b in ell^2,
using its coefficient Hilbert norm. Cauchy--Schwarz proves convergence
at every interior point; its derivative functionals are j! b_j and
all finite jets are onto. For 0<rho<1, the rule f(z)->w_0 f(rho z)
is bounded with norm equal to the modulus of w_0, since its coefficient
multiplier is w_0 rho^j. This EXTERNAL ANALYTIC CONTROL changes the
map and is not a solution for (3). It shows that the obstruction is
expansion with a nonzero weight, not smoothness or Hilbert spaces alone.

The proof would work for any smooth expanding fixed-point germ with
nonzero weight, giving diagonal values w(0)h'(0)^j. This is a
PROVES_TOO_MUCH control: the obstruction is not specifically prime
arithmetic. Finite regularity, missing boundary jet continuity, restricted
jet ranges, other Banach topologies, distributions or a different
operator orientation are not excluded by this theorem. They would
need separately frozen tests, not a same-card repair.

## 6. Gate decision and reproducibility

| Obligation | Exact result | Limit |
| --- | --- | --- |
| T0 geometric source and return | The full 193 owner and (1) remain unchanged | No new symplectic or fixed-Hilbert flow is constructed |
| T1 arithmetic/clock | Same integer source and actual roof retained | Source-clock naturalness stays OPEN |
| T2 primitive ledger | Original complete ledger remains a read-only dependency | No new packet or orbit claim from dual jets |
| T3 proposed jet-rich representation | Bounded invariance is impossible under all three hypotheses | Scoped STOP before compactness, traces or determinants |
| Classical A0--A2 | No classical symplectic carrier in this analytic audit | NOT APPLICABLE; no natural-A0 or formal A2 passage |
| Formal Route coordinates / Route B | No evaluator or readiness contract invoked | UNASSIGNED / NOT INVOKED |

Decision: STOP this exact jet-rich realization. Retain the positive
193/197 results and fork only with explicit changed analytic hypotheses.
This is not a universal no-go for fixed physical Hilbert spaces and
does not settle whether a useful nonsmooth full-state representation
exists. Naturalness remains OPEN.

The [card](candidate-card.md), [ledger](claim-ledger.md) and
[evidence index](evidence/README.md) specify inputs and actual review.
Methods are exact substitution into the frozen return, one-sided Taylor
coefficients, finite-dimensional triangular algebra and the dual norm
inequality. There is no numerical experiment, arithmetic dataset,
finite precision, cutoff-based inference or external theorem import.
The only geometric dependency is the explicitly read old owner;
the local obstruction is proved here rather than cited from a general
weighted-composition theorem. No novelty claim is made.

ARS contributes bounded claim/evidence/reasoning and adverse controls.
The actual separate model review shares the selected model and context;
it is nonblind, not human peer review or independent-error evidence.
No full publication pipeline, external model/API upload or PDF is used.
