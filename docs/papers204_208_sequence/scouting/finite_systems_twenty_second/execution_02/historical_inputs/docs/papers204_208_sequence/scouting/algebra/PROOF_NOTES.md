# Algebra lane: two deductive candidate contracts

Proof author: `/root/batch197_lzk_gate`, 2026-09-05. These are scouting
proofs, not accepted manuscripts, independent reviews, or novelty claims.
The author-side exhaustive checks are in `pilot.py`; they are falsifiers
and are not used in any all-parameter argument below.

## OF: orthogonal Fibonacci update on the full subspace-pair carrier

Disposition update: **NO_PROMOTION recommended**. The following theorems
are mathematically retained, but the general polarity-memory deduction
below removes the temporal mechanism from the residual contribution.

Let E be a nondegenerate alternating space of dimension 2m over F_q, with
q any prime power and m >= 0. Let L(E) denote **all** linear subspaces,
including degenerate ones. On L(E)^2 set

    F(U,V) = (V,(U+V)^perp).

This is not an ortholattice assumption: a symplectic subspace can meet its
perpendicular nontrivially. Write rad A = A intersect A^perp.

### OF-T: exact recurrent set, uniform identity, and sharp height

The recurrent set is exactly

    R = {(A,B): A perpendicular B and rad A = rad B}.

On the full carrier F^6 = F^3. Thus every eventual period is 1 or 3 and
every tail has length at most 3. If m >= 1, the maximum tail is exactly 3.
Fixed states are (L,L), where L=L^perp is Lagrangian.

Proof. After one update the pair is orthogonal. Start now with A perp B
and put C=(A+B)^perp, R_A=rad A and R_B=rad B. De Morgan duality and the
modular subspace identity give

    F(A,B)   = (B,C),
    F^2(A,B) = (C,A+R_B),
    F^3(A,B) = (A+R_B,B+R_A).                         (OF.1)

For example, (B+C)^perp = B^perp intersect (A+B) = A+R_B because
A is contained in B^perp. The third step follows by the same calculation.
Orthogonality A perp B also implies

    rad C = rad(A+B) = R_A+R_B = rad(A+R_B).         (OF.2)

To check the middle equality, if a+b in A+B annihilates A+B, its pairing
with A shows a in R_A, and its pairing with B shows b in R_B. For the last
equality, R_B annihilates A+R_B; any a+r annihilating A must have a in R_A.
Hence F^2 of an orthogonal pair has orthogonal coordinates with equal
radicals. Formula (OF.1) is the identity on such a pair, proving F^6=F^3
on the original full carrier. Every periodic state is already an image
and hence orthogonal. Its period divides 3, so (OF.1) implies R_B <= A
and R_A <= B. Orthogonality then forces R_A=R_B. This proves the stated
recurrent set in both directions.

For sharpness take a hyperbolic plane H=<e,f> with <e,f>=1 and its
orthogonal complement K, and start from (<e>,<f>). Its first three states
are (<f>,K), (K,<f>), (<f>,<f>). The second has coordinate radicals 0
and <f>, so is not recurrent; the third has equal radicals and is
recurrent. This works also when K=0. Finally F(U,V)=(U,V) says U=V=U^perp.
For m=0 there is one state and the sharp height is 0, not 3. QED.

### OF-I: every inverse fibre and its unique maximum

For a target (X,Y) put S=Y^perp. It has predecessors if and only if X<=S.
In that case let a=dim X and b=dim S-a. Then

    |F^{-1}(X,Y)| = N_q(a,b)
                    = sum_{k=0}^a [a choose k]_q q^{(a-k)b}.    (OF.3)

Moreover the largest fibre equals the total number G_{2m}(q) of subspaces
of E, and its unique maximizing target is (E,0).

Proof. A predecessor is (U,X) with U+X=S. Choose K_0=U intersect X of
dimension k, in [a choose k]_q ways. In S/K_0 the subspace U/K_0 is a
complement of X/K_0. Fix a complement W to X in S; all such U/K_0 are
graphs of linear maps W -> X/K_0, giving q^{(a-k)b} choices. This also
decodes every source without overlap. The fibre is a subset of L(S).
If S is proper in E, |L(S)|<|L(E)|. If S=E but X is proper, the zero
subspace is missing from the fibre, so again it is smaller. At X=S=E,
all subspaces are predecessors. This covers m=0 as well. QED.

### OF-C: closed recurrent and cycle census

Define

    s_a(q) = |Sp_{2a}(q)| = q^{a^2} product_{i=1}^a(q^{2i}-1),
    I_{m,r}(q) = [m choose r]_q product_{i=0}^{r-1}(q^{m-i}+1).

The recurrent count is

    R_m(q) = sum_{r=0}^m I_{m,r}(q)
             sum_{a+b+c=m-r} s_{m-r}(q)/(s_a(q)s_b(q)s_c(q)).   (OF.4)

The fixed count is L_m(q)=product_{i=1}^m(q^i+1), and the number of strict
3-cycles is (R_m(q)-L_m(q))/3.

Proof. A recurrent pair has a unique common totally isotropic radical R
of dimension r. The quotient R^perp/R is symplectic of dimension 2(m-r).
The images A/R, B/R are orthogonal nondegenerate subspaces; their
orthogonal complement supplies a third nondegenerate summand. Conversely
each ordered orthogonal decomposition of this quotient lifts uniquely to
a recurrent pair. For half-dimensions a,b,c the symplectic group is
transitive on decompositions, with stabilizer Sp_{2a} x Sp_{2b} x Sp_{2c}:
choose symplectic bases in the three summands to prove both assertions.
This gives the inner sum. An ordered independent isotropic r-tuple can
be selected in product_{j=0}^{r-1}(q^{2m-j}-q^j) ways. Divide by the
number product_{j=0}^{r-1}(q^r-q^j) of ordered bases of a fixed r-space
and simplify to I_{m,r}. Taking r=m gives L_m. Formula OF-T then gives
the strict cycle count. QED.

### OF-K: generic polarity-memory transfer (deductive kill)

Let P be any self-adjoint antitone Galois polarity on a join-semilattice:
write x perpendicular y when x<=P(y), equivalently y<=P(x). Define
a_{i+2}=P(a_i join a_{i+1}), with arbitrary a_0,a_1. Every consecutive
triple (a_i,a_{i+1},a_{i+2}) for i>=1 is pairwise perpendicular. Therefore

    a_i <= a_{i+3} for every i>=1.                   (OF.K1)

For i>=0, apply antitonicity to the instances i+1 and i+2 of (OF.K1):

    a_{i+6}=P(a_{i+4} join a_{i+5})
             <=P(a_{i+1} join a_{i+2})=a_{i+3}.

The opposite inequality is (OF.K1) at i+3. Hence a_{i+6}=a_{i+3} for
every i>=0, proving F^6=F^3 for the two-register map on this much larger
class. No vector-space modularity, alternating form, or finite field is
used. In the power-set case P is the common-neighbor map of any symmetric
relation, with loops allowed. The independent literal negative-control
search tried all such relations through four points and all 266,376
pair-states; its failure to find a counterexample was retained and then
explained by this deduction. That computation is not the proof.

Ownership subtraction now includes the entire generic polarity-memory
clock, as well as De Morgan duality, modularity, complement graphs,
Gaussian coefficients, symplectic group orders and isotropic-subspace
counts. The remaining radical description is a geometric classification
of the generic recurrent saturation, and OF-I is ordinary complement
counting. Relative to the existing P106 polarity and P182 Gaussian
subspace-lattice surface, this does not justify a different-mechanism
seat. Retain the exact deductions and recommend NO_PROMOTION; do not
claim a false literal identity with either historical manuscript.

## CS: commutator-sum feedback on all pairs of 2-by-2 matrices

Let q=2^e, e>=1, and M=Mat_2(F_q). On M^2 define

    F(A,B) = ([A,B], A+B),  [A,B]=AB-BA.

The entire q^8-state carrier is used, not a preselected commuting or
trace-constrained subset. Let C=[A,B], S=A+B, and s=tr S.

### CS-T: exact iterates, core, periods, and depth census

For k>=0 put beta_k(s)=sum_{j=0}^{k-1}s^j, with beta_0=0. Then

    F^{k+1}(A,B) = (s^k C, S+beta_k(s)C).             (CS.1)

The recurrent set is the union of all (0,B), and all (C,S) with

    C != 0, tr C=tr(CS)=0, tr S != 0.                (CS.2)

All (0,B) are fixed. A nonfixed recurrent point has period 2 if s=1,
and multiplicative order ord(s) if s!=0,1. The maximum tail is 2.

Proof. Cyclicity gives tr C=tr(CS)=0. The polarized two-by-two
Cayley-Hamilton identity in characteristic two is

    [X,Y] = tr(X)Y + tr(Y)X
             + (tr(XY)+tr(X)tr(Y)) I.

For tr X=tr(XY)=0 this becomes [X,Y]=tr(Y)X. The constraints are
preserved by (X,Y)->(sX,X+Y), since tr X=0 and
tr(X^2)=(tr X)^2=0. The second-coordinate trace is therefore invariant,
and induction proves (CS.1). If s=0, the state after two steps is
(0,S+C). If s!=0, the restriction to the image is invertible: scaling
the first coordinate is invertible and the second is recovered by a
shear. For C!=0 the first-coordinate return condition is s^k=1; when
s!=1 this also gives beta_k(s)=0. If s=1, the second coordinate returns
exactly when k is even. This proves the claims, using CS-I below for the
image description. The pair A=E_12, B=E_21 has C=I and s=0, so it reaches
the fixed set at step 2 and not at step 1. QED.

There are q^4 fixed states and, putting D=q^5-q^3, exactly

    c_2 = D/2;
    c_d = phi(d)D/d for every d>1 dividing q-1;
    no other nontrivial periods.                    (CS.3)

The recurrent count is q^6-q^5+q^3. The exact depth-2 count is
q^7-2q^5+q^3; the depth-1 count is q^8 minus these two counts.

Proof of counts. A nonzero scalar C cannot satisfy tr(CS)=0 when s!=0.
There are q^3-q nonscalar trace-zero C. For each such C, the functionals
tr S and tr(CS) are linearly independent, hence exactly q^2 choices of S
for every prescribed s!=0. This proves the recurrent and cycle counts.
Depth 2 occurs exactly when the input sum S has zero trace and its
commutator C is nonzero. There are q^3-q nonscalar trace-zero sums S;
CS-I gives q^2-1 nonzero allowed C, each with q^2 original pairs.
Their product is the displayed depth-2 count. QED.

### CS-I: exact image, every one-step fibre, every later fibre

For a target (C,S), the one-step count is

    q^4, if S is scalar and C=0;
    q^2, if S is nonscalar and tr C=tr(CS)=0;
    0,   otherwise.                                (CS.4)

Thus |im F|=q^6-q^3+q. The maximum fibre q^4 is attained precisely at
the q targets (0,lambda I).

Proof. Write B=S-A. Solving the target equation is solving ad_S(A)=C.
For scalar S it is zero. For nonscalar S the centralizer is <I,S>, of
dimension 2. Indeed a nonscalar two-by-two matrix has a cyclic vector v;
an operator commuting with S is determined by its value on v and must
be a linear polynomial in S. The trace pairing on M is nondegenerate.
The image of ad_S annihilates I and S; since it has dimension 2, it is
exactly {C:tr C=tr(CS)=0}. Each nonempty inverse is an affine coset of
<I,S>. The q^4 choices of S include q scalar ones, proving the census.
This gives an explicit source decoder (A_0+uI+vS,S-A_0-uI-vS). QED.

For every t>=2 the complete target count is

    q^2,                for recurrent (C,S) with tr S!=0;
    q^5+q^4-q^3,        for (0,Z) with Z scalar;
    q^4-q^3,            for (0,Z) with tr Z=0 and Z nonscalar;
    0,                   otherwise.                 (CS.5)

In particular its maximum is q^5+q^4-q^3, attained precisely at the same
q scalar fixed targets.

Proof. On nonzero-trace image strata the dynamics is bijective, and each
image state has q^2 original predecessors by (CS.4); hence the later
counts remain q^2. On the zero-trace stratum the fixed endpoint is
Z=S+[A,S]. For every nonscalar trace-zero S, the equation
[A,S]=Z+S is solvable exactly when tr(ZS)=0, with q^2 choices of A.
If Z is scalar, all q^3-q nonscalar trace-zero S qualify; additionally
S=Z contributes q^4 sources. This gives q^5+q^4-q^3. If Z is nonscalar
and trace zero, the restriction of tr(ZS) to the three-dimensional
trace-zero space is nonzero, with a two-dimensional kernel containing
all q scalars. Exactly q^2-q nonscalar S qualify, yielding q^4-q^3.
All these zero-trace targets are fixed, so the counts do not change
after step 2. No other targets can occur by CS-T. QED.

Ownership subtraction: the Cayley-Hamilton identity, scalar order and
Jordan/shear dynamics after fixing s, centralizer kernels, trace-pairing
orthogonality and affine-fibre counting are owned elementary mechanisms.
The possible residual is their literal feedback coupling, the trace-zero
collapse versus nonzero-trace periodic core, and the rank-jump count in
(CS.5). A separate gate must decide whether this is too thin a transfer.
Neither P119's fixed group commutator nor P175's diagonal feedback is
the same literal map, but that fact alone does not establish a new
mechanism.
