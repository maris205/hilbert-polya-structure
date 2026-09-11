# CS independent candidate gate

Date: 2026-09-05 UTC. Gate agent: `/root/batch197_fosp_gate`.

**Verdict: MATH_VALID / KILL_GENERIC_LINEARIZATION_SCALAR_ACTION.**
Do not admit CS or assign it a paper number. This is a candidate gate,
not manuscript Review A/B and not an external expert review. All author
proofs and failed-candidate evidence remain intact; HOLD_EXTERNAL remains.

The mathematical claims CS.1–CS.5 survive this check. The adverse decision
is about the residual contribution after exact mechanism subtraction.
In particular, the alleged separate all-time scalar rank-jump axis is
precisely the elementary map `(r,w) -> rw`, `w in F_q^2`, with three
forgotten free coordinates. This is an exact derivation, not a similarity
of language and not a claimed conjugacy of the original map with P175.

## 1. Inputs, separation, and contribution ownership

The three candidate inputs were read completely: `../PROOF_NOTES.md`,
`../pilot.py`, and `../SOURCE_AND_COLLISION_NOTES.md`. No author canonical
output or author helper was imported or used as the independent oracle.
The gate also inspected the internal owner surfaces listed in section 5.
Exact input hashes are in `INPUTS.sha256`, relative to the workspace root.

The CS proof author is `/root/batch197_lzk_gate`. This gate agent was not
an author of the incoming CS notes. The triangular coordinate reduction
in section 4 is a **new mathematical contribution by this gate agent**.
Consequently this agent must not later act as an independent manuscript
reviewer of a CS paper incorporating that argument. A bounded read-only
request asked the original author to challenge the new algebra; the author
confirmed the formulas and all boundary cases. That response is preserved
in `AUTHOR_RESPONSE.md` and is explicitly author feedback, not an
independent review or the basis of the gate's proof.

The project research and research-review skills structured the claim
audit and evidence handoff. The requested review MCP tools were unavailable;
no external review invocation, model switch, specialist contact or upload
is claimed. This is the parent-authorized process-separated candidate gate
under the current inherited model. Gate outputs are confined to this folder.

## 2. Literal map and independent mathematical audit

Let `q=2^e`, `e>=1`, `M=Mat_2(F_q)`, and

    F(A,B)=([A,B],A+B),    C=[A,B],    S=A+B,    s=tr(S).

The full carrier has `q^8` states. Characteristic two, matrix size two,
and the full carrier are essential hypotheses of this contract.

For any two 2-by-2 matrices the polarized Cayley–Hamilton identity is

    [X,Y]=tr(X)Y+tr(Y)X+(tr(XY)+tr(X)tr(Y))I.

This follows by expanding the characteristic identity of `X+Y` and
subtracting those of `X` and `Y`; it can also be checked entrywise.
Cyclicity of trace gives `tr(C)=tr(CS)=0`: expand `CS=[A,B](A+B)` and
pair the cyclically equal terms. If `tr(X)=tr(XY)=0`, therefore,

    F(X,Y)=(sX,Y+X),    s=tr(Y).

Both zero constraints are preserved: `tr(X^2)=tr(X)^2=0` in
characteristic two. Hence after the first step, on the fixed-s stratum,
the map is the restriction of the ambient linear map

    K_s(X,Y)=(sX,Y+X).

For `s!=0,1`, changing to `D=Y+X/(1+s)` gives exactly
`(X,D)->(sX,D)`. For `s=1`, `K_s^2` is the identity. For `s=0`,
`K_s(X,Y)=(0,Y+X)` is already fixed. This proves CS.1 and the period
claims without a finite cutoff. It does **not** claim that F itself is
globally linear or that its first image is an unconstrained vector space.

For completeness the image is established by the inverse equation.
Holding the target sum S fixed replaces `(A,B)` by `(A,S-A)`, and the
equation becomes `ad_S(A)=C`. If S is scalar, all `q^4` choices of A
give C=0. If S is nonscalar, choose v such that `v,Sv` is a basis.
Such v exists: otherwise every line would be invariant, and applying S
to two independent vectors and their sum forces S scalar. A commuting
operator is determined by its value on v, so its centralizer is the
two-dimensional space `<I,S>`. The trace pairing is nondegenerate, and
`ad_S(M)` annihilates both I and S. Rank-nullity now proves

    ad_S(M)={C:tr(C)=tr(CS)=0}.

Every nonempty fibre is an affine coset of `<I,S>` and has `q^2` members.
This supplies the scalar exception and CS.4, including its decoder.
On `s!=0`, S cannot be scalar, so the constrained image is preserved
bijectively by `K_s`. Thus all its states are recurrent. On `s=0`,
only `(0,S)` is recurrent. The source `(E12,E21)` has first image
`(I,E12+E21)`, so its tail is exactly two. All assertions about the
recurrent set and maximum tail follow.

The stated counts are also valid. There are `q^3-q` nonscalar traceless
nonzero choices of C; for each, `tr(S)=s` and `tr(CS)=0` are independent
linear equations and have `q^2` solutions. For fixed nonzero s this gives
`D=q^5-q^3` nonfixed recurrent states. The resulting cycle counts are
`D/2` for period two and `phi(d)D/d` for each `d>1` dividing `q-1`.
The fixed count is `q^4`. Summing gives recurrent count `q^6-q^5+q^3`.
Depth two is exactly `s=0,C!=0`; nonscalar traceless sums, nonzero
admissible commutators and centralizer fibres give
`(q^3-q)(q^2-1)q^2=q^7-2q^5+q^3` sources. No census discrepancy was found.

## 3. What is already removed before the proposed extra axis

The following are assigned zero independent contribution credit:

- The polarized 2-by-2 characteristic identity and trace cyclicity.
- Constant-trace strata followed by scalar multiplication or a size-two
  unipotent shear, including multiplicative orders and period-two parity.
- The rank and kernel of an inner derivation, the two-dimensional
  nonscalar centralizer, and affine-coset source multiplicities.
- Counting solutions of one or two independent linear equations and
  dividing periodic-point counts by their exact periods.

The full-carrier map is a literal coupling of those mechanisms, not
literally P175 or P125. Literal difference alone does not supply the two
materially separate residual theorem axes required for admission.

## 4. Decisive all-q reduction of CS.5

This derivation operates on the **entire** input layer `tr(A+B)=0`.
Write its seven independent coordinates as

    A = [[d,b],[c,d+tau]],    S=A+B=[[z,x],[y,z]].

Direct matrix multiplication gives

    [A,S]=[[by+cx,tau*x],[tau*y,by+cx]].

In particular `[ [A,S], S ]=0`. Therefore

    F^2(A,B)=(0,Z),
    Z=(z+by+cx)I+(1+tau)(xE12+yE21).

Put `r=1+tau`, `alpha=z+by+cx`, and `w=(x,y)`. The coordinate map

    (tau,x,y,z,d,b,c) -> (r,x,y,alpha,d,b,c)

is a polynomial bijection of `F_q^7`. Its inverse is
`tau=r+1`, `z=alpha+by+cx`, with the other coordinates unchanged.
Also `(A,B)<->(A,S)` is a bijection. There are no nonscalar, nonzero,
invertibility, or generic-position restrictions in this change of
coordinates. It includes `r=0`, `w=0`, and scalar S.

For a fixed target `Z=alpha I+uE12+vE21`, its inverse problem is now
exactly

    r*w=(u,v),    (d,b,c) arbitrary in F_q^3.

If `(u,v)=0`, there are `q^2` choices with `r=0` and `q-1` choices
with `r!=0,w=0`. If `(u,v)!=0`, r is any of the `q-1` nonzero
scalars and w is uniquely `r^{-1}(u,v)`. Thus the full endpoint fibres
are

    q^3(q^2+q-1)=q^5+q^4-q^3,    for scalar Z;
    q^3(q-1)=q^4-q^3,           for nonscalar traceless Z.

Every `(0,Z)` is fixed. Moreover the trace of the second coordinate
after step one is the original `tr(A+B)` and never changes, so no
nonzero-trace input contributes to these zero-trace targets. This proves
the entire zero-trace part of CS.5 for every `t>=2`, not just a subset.
The remaining nonzero-trace part is the bijective `K_s` core with its
constant original multiplicity `q^2`, already removed in section 3.

The exceptional fibre maximum is simply the zero fibre of scalar-vector
multiplication; comparing the two displayed numbers gives the q scalar
maximizing targets. Its exact extremum is not a separate mechanism.

**Boundary:** this is an exact input/output normal form for the endpoint
map `F^2` on one invariant-trace input layer. It is not a dynamical
conjugacy of the original one-step map F with scalar multiplication.
That stronger statement is neither needed nor asserted.

## 5. Internal subtraction and bounded primary-source check

| Read internal surface | Exact distinction and subtraction |
|---|---|
| `papers/175-diagonal-feedback-commutator/main.tex`, map and complete-fibre/clock sections | P175 is the single-matrix map `A->[Diag(A),A]`; all its orbits reach its unique zero fixed point. CS has a matrix-pair carrier, many fixed states and nontrivial periodic strata, so no conjugacy is asserted. Generic matrix commutators and short annihilation earn no new credit. P175's arbitrary support-colouring atlas does not occur in CS; CS.5 instead collapses to the scalar product in section 4. |
| `papers/125-quadratic-state-shear/main.tex`, abstract and map/scope | P125 is `(x,y)->(y,x+Q(x)y)` on quadratic vector-space pairs over F2. It is not CS. It consumes the state-dependent shear vocabulary, but the exact generic-linear reduction here is established independently in section 2. |
| `docs/papers162_166_sequence/scouting/replacement_nonlinear_algebra/SCOUT.md`, NL01–NL06, NL13, NL17–NL18 and firewall | Earlier killed registers already centralize into bilinear fibres or finite-linear quotient dynamics. NL13 is the direct scalar skew product `(a,b)->(a,ab)`; NL17 is Peirce multiplication plus elementary hyperbola count. These are mechanism precedents, not false equality of carriers or formulas. |
| `docs/papers197_201_sequence/scouting/algebra_lane/COLLISION_MEMO.md`, hard-kill map | The killed anticommutator register `(A,B)->(B,AB+BA)` is not CS, but prevents treating a swapped bilinear register as independently valuable merely because its formula is different. |

The following primary pages were independently opened on 2026-09-05:

- Wei, Xu and Zou, [Dynamics of Linear Systems over Finite Commutative
  Rings](https://arxiv.org/abs/1709.08579), author abstract: finite-field
  linear dynamics is described using elementary divisors. This is a
  generic background owner only, not a source asserting the CS map.
- Brešar, Gardella and Thiel, [Products of commutators in matrix
  rings](https://www.cambridge.org/core/journals/canadian-mathematical-bulletin/article/products-of-commutators-in-matrix-rings/10FD7B61EB100163AA3815437915BA66),
  publisher full text, abstract/introduction: concerns additive
  commutators, their products and fixed-element questions. This places
  the matrix-ring primitives in their owner region, not CS dynamics.
- Kadyrsizova and Yerlanov, [Algebraic sets defined by the commutator
  matrix](https://arxiv.org/abs/2006.13514), author abstract: studies
  specified zero-diagonal/antidiagonal commutator varieties. It is a
  nearby static constraint owner, not an exact CS.5 citation.

The executed queries were `"commutator" "A+B" "dynamics" matrices
finite field`, `"commutator-sum" matrices`, and the exact title of the
Wei–Xu–Zou work. No opened source stated the literal CS conjunction.
This bounded non-hit supplies **no novelty, priority, recent-coverage or
external-acceptance certificate**. The kill follows from the self-contained
exact reductions above, not from an invented direct external collision.

## 6. Independent finite evidence and disposition

`verify_gate.py` uses packed **column-major** matrix integers, explicit
F2/F4 multiplication tables, and literal matrix products. It imports no
candidate implementation. For q=2 and q=4 it traverses all functional
graphs, checks every first target fibre, every target fibre at times 2–8,
eight literal iterates per source, the recurrent criterion, and the
triangular bijection and endpoint formula on all zero-trace input states.

The actual `CANONICAL.json` has **1,250,591 successful assertions** over
256 and 65,536 full input states. The q=4 first image has 4,036 states;
the recurrent count is 3,136 and the depth-two count is 14,400. Its
later nonempty fibre spectrum is `16:3072, 192:60, 1216:4`, where each
pair means `fibre size:number of targets`. These are finite checks of
the displayed proofs, never a substitute for their all-q arguments.
Execution and exact raw-byte replay details are in `EXECUTION.md`.

There is no open mathematical finding in CS.1–CS.5 identified by this
gate. There is one decisive value finding: **after generic trace-layer
linearization and elementary centralizer fibres are deducted, CS.5 is
not a materially separate residual axis**. The input/output reduction
removes it completely. Preserve CS as a mathematically valid rejected
scout, keep the correct formulas, and replace this candidate with a
different mechanism family. A larger field box or repackaging the same
rank jump does not answer this finding. No paper number is assigned.
