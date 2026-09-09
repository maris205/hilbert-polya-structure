# AS424-I: exact-support torsion memory

2026-09-08. Auxiliary analytic package, not an admitted paper. The statement
below is offered for nonauthor proof review. The final source comparison
downgrades the package from paper retention: its operators are classical
geometric U correspondences, and no substantial residual has been established.
No mathematical program, manuscript, or formal Route-A evaluation ran.

## 1. Complete object and statement

Let p be any prime, M>=3 an integer, and L a finite nonempty set of distinct
primes, with p not in L and gcd(M,p product(L))=1. Work over algebraic
closure F_p. Let V be the finite set of isomorphism classes (E,eta), where
E is supersingular and eta:(Z/MZ)^2 -> E[M] is an ordered basis.
Choose one representative of each class.

For l in L an edge from (E,eta) to (E',eta') is a separable degree-l
isogeny phi satisfying phi eta=eta'. Edges are counted individually.
Equivalently they are quotient maps for order-l subgroups followed by the
unique marked isomorphism to the selected target representative. Each
vertex has l+1 outgoing l-edges. Full-level marked automorphisms are trivial:
if u fixes E[M], then ker(u-1) contains M^2 points; a nonidentity elliptic
automorphism satisfies deg(u-1)<=4, contradicting M>=3. The latter bound
also follows from the degree quadratic form and deg u=1.

This is the classical marked isogeny graph construction [S3]; finiteness
of supersingular classes and prime-to-p elliptic torsion are classical
inputs, not new claims. The construction is valid also in characteristics
2 and 3 because the chosen M-torsion is etale and the marked automorphism
argument is characteristic-independent.

For a based closed edge word w=(phi_1,...,phi_n), let
alpha_w=phi_n ... phi_1 in End(E), S(w) its set of colors, and
x(w)=product_{j=1}^n x_{deg(phi_j)}. Call w stable-cyclic if
ker(alpha_w^k) is a cyclic geometric group for every k>=1. Degree is prime
to p throughout, so these are reduced geometric kernels, not scheme lengths.
Define

    C_n(x) = sum_{stable-cyclic based closed words |w|=n} x(w),
    Z(x) = exp(sum_{n>=1} C_n(x)/n).

The clock n is the actual number of isogenies. The specialization x_l=l^(-s)
uses the intrinsically additive log degree; it is not an adjustable roof.

**Candidate theorem.** The matrices in Section 3 satisfy

    C_n(x) = sum_{empty != S subset L} sum_{R subset S}
               (-1)^(|S|-|R|) Tr(B_{S,R}(x)^n),                 (1)

    Z(x) = product_{empty != S subset L} product_{R subset S}
               det(I-B_{S,R}(x))^((-1)^(|S|-|R|+1)).            (2)

Moreover Z is exactly the Euler product over primitive stable-cyclic
closed edge words modulo cyclic rotation, not reversal:

    Z(x) = product_[c] (1-x(c))^(-1).                          (3)

These identities hold as formal power series at x=0; (2) makes Z a rational
function with integer polynomial numerator and denominator and value 1
at zero. No connectedness, primitivity, spectral gap, or automorphic lift
of the matrices is assumed.

## 2. The elementary torsion criterion

For a prime l different from p, V_l=E[l] is two-dimensional over F_l.
For a separable isogeny alpha of L-smooth degree, its kernel is cyclic iff
alpha|E[l] is nonzero for every l dividing its degree. Indeed, a noncyclic
l-primary subgroup of elliptic torsion contains all of E[l], whereas a
cyclic one does not. For an active l the determinant of alpha_l is zero,
so nonzero means rank one.

If A is a two-dimensional rank-one matrix with determinant zero, then
Cayley-Hamilton gives A^2=(tr A)A. Consequently the following are equivalent:

1. A^k is nonzero for every k>=1;
2. A is nonzero and tr A is nonzero;
3. there is a line d with A(d)=d and A does not kill d.

In the third case d=im A is unique. If A is nonzero but tr A=0,
its kernel is cyclic for one pass but A^2=0. Thus for closed w,

    w stable-cyclic iff tr(alpha_w|E[l]) != 0 for every l in S(w). (4)

Write t=Trd(alpha_w) and N=deg(alpha_w). The integral reduced characteristic
polynomial is X^2-tX+N; its reduction is the characteristic polynomial on
E[l]. Thus (4) has the intrinsic integer form

    w stable-cyclic iff gcd(Trd(alpha_w),deg(alpha_w))=1.          (5)

This includes the rank-one requirement: at an active l the determinant
vanishes, and nonzero trace rules out the zero matrix.

Zero trace includes the zero matrix. This criterion is only at active
primes. Inactive torsion actions are invertible and need not have one fixed
projective line.

Rotating w preserves (4). Choose bases on the torsion spaces along the
word; the trace of a cyclic product of square matrices is unchanged even
when some factors are singular. Integrally, if the first edge is phi and
the remaining composite is psi, rotation changes psi phi to phi psi.
These are conjugate by the quasi-isogeny phi, whose inverse is
dual(phi)/deg(phi); reduced trace and degree are unchanged. This is an
isomorphism between the two rational endomorphism algebras, not a claim
that phi is invertible on its own l-torsion. Stable-cyclicity is preserved under every
word repetition and under taking a closed word root. For a root v, each
active-prime matrix A is singular; if A^k has nonzero trace, then A is
rank one with nonzero trace by the same formula. These observations justify
the primitive/repetition decomposition used in (3).

## 3. Source-defined finite memory

For each nonempty S subset L let Q_S consist of states

    (E,eta,(d_l)_{l in S}),   d_l in P(E[l]).

It has |V| product_{l in S}(l+1) elements. A degree-l edge phi can act on
Q_S only when l is in S and d_l != ker phi. Set

    d'_l = phi(E[l]),
    d'_q = phi(d_q),       q in S, q != l.

The l-map has rank one, and every allowed line has image phi(E[l]); for
q!=l it is invertible. Both rules are intrinsic to the edge. For R subset S,
define B_{S,R}(x) on the entire finite space C^(Q_S), with (target,source)
entry equal to the sum of x_l over allowed edges of colors l in R inducing
that transition. Parallel edges retain multiplicities. B_{S,empty}=0.

For a fixed base word, a memory sequence is allowed exactly when no
intermediate linear map kills the remembered line. A line survives all
steps iff the full composite does not kill it: zero at any intermediate
stage remains zero. Thus a closed memory over w corresponds to a projective
line fixed nontrivially by each alpha_w|E[l], l in S.

If S=S(w), Section 2 proves that the number of closed memory lifts is
exactly one for a stable-cyclic word and zero otherwise. If S strictly
contains S(w), the lift count is instead multiplied by the number of fixed
lines of the invertible inactive holonomies. Such factors can be 0,1,2,
or l+1. They cannot be silently set to one.

## 4. Proof of the trace and determinant identities

For fixed S, expansion of Tr(B_{S,R}^n) counts closed lifted histories whose
base support T is contained in R. A fixed history occurs in the alternating
sum over R subset S with coefficient

    sum_{T subset R subset S} (-1)^(|S|-|R|)
       = 1 if T=S, and 0 otherwise.

The alternating sum therefore removes every inactive-memory contribution
before S is summed. For T=S the preceding unique-lift criterion gives (1).
This is a finite exact inclusion-exclusion, not a truncation or a limiting
cancellation. The standard formal identity

    -log det(I-B)=sum_{n>=1} Tr(B^n)/n

is applicable because every matrix entry has positive total variable degree.
Apply it to (1) to get (2), with precisely the displayed signs.

Every nonempty closed edge word is a repetition of a unique primitive
cyclic word. Section 2 shows the selected class is root- and repeat-closed
and rotation-invariant. A primitive word of length d contributes d based
words at length kd; its weight is x(c)^k. Division by kd gives x(c)^k/k.
Summing k proves (3). All coefficients of each fixed total degree are
finite. Alternatively, absolute convergence follows in a sufficiently
small polydisc from the finite outgoing degree bound
sum_{l in L}(l+1)|x_l|<1. This also validates the local analytic identity.

## 5. Full-level and representative boundaries

A closed word is genuinely closed in the marked graph: alpha_w eta=eta,
so alpha_w acts identically on E[M]. The weaker congruence
deg(alpha_w)=1 mod M is only necessary (by Weil pairing), not substituted
for actual level closure. Since M is coprime to active torsion primes,
level closure does not change the criterion (4); the graph itself enforces
it before the torsion test is applied.

The dual of a degree-l edge generally ends at (E,l eta), not (E,eta).
There is no assumed edge-reversal involution. None of the construction,
trace expansion, or proof uses one. This addresses precisely a difficulty
treated by the abstract-isogeny-graph source [S2], but does not claim to
reprove or replace that source's single-color Ihara formula.

Changing vertex representatives by marked isomorphisms conjugates every
edge and transports every torsion line. The resulting finite matrices are
permutation-conjugate. A closed composite changes by conjugation by the
starting marked isomorphism, preserving kernels, powers, and traces.
There is no free choice of a closing automorphism after w is fixed.

The gcd in (5) is therefore independent both of representative isomorphisms
and of the cyclic starting vertex. It is not invariant under freely
postcomposing the composite with an arbitrary extra automorphism, an operation
which changes the marked word and is not authorized in this graph.

## 6. Two exact arithmetic controls (hand arguments; no program)

Take p=7, E:y^2=x^3-x, M=3, and L={2,5}. This curve has eight F_7-points,
hence trace zero and is supersingular. Over algebraic closure it has an
automorphism i with i^2=[-1]. Its dual is -i; consequently a+bi has degree
a^2+b^2 and trace 2a. Fix any full 3-torsion basis.

**One pass is not enough.** Let alpha=1+3i. It has degree 10 and fixes
E[3]. Its squarefree kernel is cyclic, and any factorization into a 2-edge
and a 5-edge gives a closed marked word. But

    alpha^2=-8+6i=[2](-4+3i),

so its second power kills E[2]. Thus the closed word is not stable-cyclic.
It has different adjacent colors, so a same-color immediate-dual check
would miss the problem.

**Unused colors really overcount.** Let beta=4+3i. It has degree 25,
trace 8, and fixes E[3]. On E[5] it is rank one with nonzero trace, hence
its two 5-edge factorization is stable-cyclic. Its square is a length-four
all-5 closed word. On E[2], beta acts as i, so beta^2 acts as the identity
and fixes all three projective lines. A trace carrying memories for {2,5}
therefore assigns this word three lifts instead of one. In (1) its S={2,5}
contribution cancels between R={2,5} and R={5}; S={5} counts it once.

The elementary point-count check used above is: the affine numbers over
x=0,1,...,6 are 1,1,0,0,2,2,1; add the point at infinity. This small exact
control is not a theorem by finite sampling. The general proof is Sections
2–5.

## 7. Exact collision with geometric U operators

The state Q_S is precisely a full M-level supersingular object carrying a
Gamma_0(l) line for every l in S. For a degree-l quotient phi with
ker(phi) different from d_l, its transported line phi(d_l) equals
phi(E[l]), because a rank-one map sends every surviving line onto its image.
Consequently the color-l transition is the unnormalized geometric U_l
correspondence on this level. This is not a new operator family. Hida's
author-hosted published offprint [S9], Section 1.5, formula (1.3), explicitly
defines U by quotienting by subgroups disjoint from the marked cyclic
subgroup and transporting that subgroup. His modular-form normalization
and differential factors are not inserted into our counting matrix.

Here is a direct proof that different colors commute; it does not import
an automorphic identification. Let l!=q belong to S and start at a state
Q. An allowed l-then-q path is uniquely specified by an order-l subgroup
K_l!=d_l and an order-q subgroup K_q!=d_q of the starting E. Indeed, the
first quotient induces an isomorphism on E[q], so the second kernel is
the image of a unique K_q. Its disjointness from the transported d_q is
equivalent to K_q!=d_q. Reverse the order of the quotients by K_q and K_l.
Both paths quotient E by K_l+K_q. Their full M-level bases and every
remembered line are the images under the same composite quotient. The
unique marked isomorphism to the chosen final representative identifies
their final states. Reversing this construction is an inverse bijection
of paths, including parallel-edge multiplicities. Therefore

    U_{l,S} U_{q,S}=U_{q,S} U_{l,S},
    B_{S,R}=sum_{l in R} x_l U_{l,S}.

For e_l>=1 on S and n=sum e_l, the coefficient with exact support S in
(1) consequently reduces to

    [product x_l^e_l] C_n
      = n!/(product e_l!) Tr(product_{l in S} U_{l,S}^{e_l}).     (6)

Thus chronological order supplies the ordinary multinomial factor after
the classical coprime-isogeny diamond is applied. Formula (1) remains a
correct way to combine the different support-level spaces, but this
bookkeeping is not evidence of a substantial spectral advance.

There is a second reduction. A nonempty stable word has N>1 and cannot
be a scalar endomorphism [a], since deg([a])=a^2 and trace([a])=2a have
nontrivial gcd when |a|>1. It generates an imaginary quadratic order
Z[alpha] with discriminant D=t^2-4N. For every active l, (5) gives l not
dividing D. The polynomial X^2-tX+N has the two distinct roots 0,t modulo
l, also for l=2. Hence l is split and conductor-free in Z[alpha] and in
its containing optimal quadratic order. In particular the stable selector
excludes the conductor-dividing ascending/descending difficulty in [S1].
The one-prime rim/optimal-embedding cycle theory is already owned by [S8].
Neither the gcd criterion nor restriction to these regular split elements
is offered as a paper-level result.

The comparison with Deitmar--Kang--McCallum [S10], Sections 3.1--3.3,
reveals existing commuting Bass translation and finite-quotient zeta
machinery. It is a structural predecessor, not an asserted exact theorem
subsumption: their Section 3 assumes a simplicial/irreducible building,
whereas products of several trees are reducible, and their multi-index
trace series has different weights from the chronological series (6).
No product-of-trees arithmetic uniformization was proved or needed here.

## 8. Ownership, residual claim, and remaining gate

[S1] Arpin et al., arXiv:2502.00638, owns mixed-prime isogeny diamonds,
canonical decomposition and Brandt principal-cycle counting. [S2] Lau et al.,
arXiv:2509.15214, owns abstract-isogeny-graph Ihara corrections, including
dual/level transport issues. [S3] Codogni–Lido, arXiv:2308.13913, owns the
marked graph framework and its established spectral theory. Ordinary
finite determinant/primitive trace manipulations are also deducted.

The remaining explicit formula is the all-support, chronological, repeat-stable
cyclic-kernel selector and its exact inactive-holonomy cancellation. It is
not a new isogeny graph, a count of canonical endomorphism classes, or a
claim to solve the all-exponent ideal-class enumeration asked in [S1].
The memory is the geometric U correspondence at Borel/Iwahori level,
as shown in Section 7. No positive paper-level increment survives that
deduction in the present package. No proof here establishes that the exact
combination has appeared elsewhere; different counting weights alone do
not establish its significance or worldwide novelty.

For fixed finite L, (2) specializes to a ratio of finite exponential
polynomials. Local HEN-O29 already blocks promotion of such a fixed finite
clock alphabet to a target Riemann–von Mangoldt divisor. No infinite-L
limit, target Euler factor, trace weight log p at a unique arithmetic
primitive, root number, automorphy, target-zero identity, or Hilbert–Pólya
realization is obtained. Reversal is not quotiented. No formal route grade.

**Final handoff disposition: AUXILIARY PROOF ONLY; NOT PAPER-RETAINED.**
The frozen mathematical question has the candidate complete argument above.
Source-owned correspondences plus elementary linear algebra, support
inclusion-exclusion, and finite trace identities do not meet the requested
substantial-paper gate on the evidence obtained. No manuscript admission,
worldwide novelty claim, or target-success claim follows.
