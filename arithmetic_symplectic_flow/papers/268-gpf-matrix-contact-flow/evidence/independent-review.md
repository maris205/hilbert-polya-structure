# Independent review — full GPF matrix/contact owner

**Candidate:** `ANG-20260919-GMC01`  
**Reviewer task:** `/root/nonconfining_transport_scout`  
**Date:** 2026-09-19  
**Current status:** `CHECKPOINTS 1–3 COMPLETE; NO BLOCKING MATHEMATICAL FINDING`.

This review began from the [frozen candidate card](../candidate-card.md),
before the reviewer read an author manuscript or received author proof
answers. The card SHA-256 at that checkpoint was

```text
17d94ef5bb3121ed83668e913e0c95fdb35340081df4e95525f0315d2b1c3971
```

The reviewer independently returned the mathematical findings below to root
before an author draft was read. This is a separate model-agent review with
shared conversation context and the inherited session configuration. It is
not blind review, external peer review, or an independent-error certificate.
No external novelty claim is made. Root owns integration and all other paths.

## Checkpoint 1 — frozen scope and independent derivation

**Disposition: COMPLETE.** Retain the entire `X_G x PSL(2,R)` carrier,
the exact positive matrix cocycle, both signs of the deck exponent, and
the full right-diagonal physical flow. No eigenline, source component,
transverse history, orientation, or group direction is removed.

The only source-classification input is the corrected periodic ledger in
[266](../../266-prime-source-return-rescreen/paper.md): one fixed source
path for each prime and one nonconstant source four-cycle. Its geometric,
clock, and analytic conclusions are not transferred. No assertion that
every two-sided history is periodic is used.

### Independent owner and quotient check

Write `nu([g])=||g||_op` for the operator norm of an SL(2,R) representative.
It is independent of the representative's sign. Every forward matrix
`M_a` has positive entries, and

    a / sqrt(a-1) >= 2,  for a >= 2.

On applying a length-k positive cocycle product to e1, the coordinates
remain nonnegative and the first coordinate increases by a factor at least
2 at every step. Thus

    nu(M^(k)(z)) >= 2^k,  k > 0.

For a determinant-one real 2-by-2 matrix P, its two singular values are
reciprocal; hence `||P^(-1)||_op=||P||_op`. Expressing a negative cocycle
as the inverse of the corresponding forward product gives

    nu(M^(k)(z)) >= 2^|k|,  k != 0.

Consequences checked independently:

- The proposed formula for T inverse is the actual inverse on the full
  carrier. The source observable is locally constant, so T and its inverse
  are continuous.
- No nonzero deck exponent fixes a point: that would make its cocycle the
  identity class, contradicting the norm bound.
- If the group coordinates of two neighborhoods have compact closure, a
  deck translate can meet both only when `2^|k|` is bounded by the operator
  norm of a member of their compact quotient-product set. Only finitely
  many k can occur. This argument needs no local compactness of X_G.
- Choose a sufficiently small group neighborhood U such that
  `nu(h g^(-1))<2` for all g,h in U. Every V x U is disjoint from all of
  its nontrivial deck translates. Its image is an open quotient chart.
- The preceding local finite-intersection property separates two distinct
  quotient points: first bound the possible k using group neighborhoods,
  then shrink neighborhoods to separate the finitely many remaining
  translates. Thus Q is Hausdorff and has the stated three-dimensional
  smooth plaques, with its full arithmetic transversal retained.

The resulting charts are leafwise product charts. They do not establish
that Q is a finite-dimensional manifold.

### Independent contact, Reeb, and volume check

Use the Lie-algebra basis

    H = diag(1/2,-1/2),
    E = [[0,1],[0,0]], F = [[0,0],[1,0]].

For `alpha_e(X)=2 tr(HX)`,

    alpha(H)=1, alpha(E)=alpha(F)=0,
    [E,F]=2H, [H,E]=E, [H,F]=-F,
    d alpha(E,F)=-2,
    d alpha(H,E)=d alpha(H,F)=0.

Therefore `(alpha wedge d alpha)(H,E,F)=-2`, so the proposed leafwise
form is contact. The Maurer-Cartan expression is unchanged under replacing
g and its tangent representative by their negatives. Left multiplication
preserves alpha, which establishes compatibility with the deck maps on
every plaque.

The actual right-diagonal flow has vector field `R_g=gH`. Consequently
`alpha(R)=1` and `i_R d alpha=0`. It is the Reeb flow of this form, is
complete for all real t, and commutes with T. Cartan's identity gives
preservation of alpha and `alpha wedge d alpha`. This is a leafwise
volume assertion, not a global finite invariant probability measure.
The nonzero Reeb vector in the quotient charts also excludes stationary
points.

### Independent full return and multiplicity check

For a nonperiodic source history, `sigma^k z=z` forces k=0. The remaining
equation `g A_t=g` forces t=0. Such histories have no positive-time return.

For a primitive source period m, put `P=M^(m)(z)`. Every admissible return
exponent is `k=mr`, and its full equation is

    g A_t g^(-1) = P^r.

P is positive hyperbolic with determinant one and eigenvalues
`lambda,lambda^(-1)`, where lambda>1. Set `ell=2 log lambda`. Positive r
requires `t=r ell` and the expanding/contracting order of its eigenlines;
negative r requires `t=|r| ell` and the reverse order.

The centralizer of the diagonal group in PSL(2,R) is exactly A_R. Its
normalizer has two components,

    A_R and w A_R,  w=[[0,1],[-1,0]].

For one diagonalizing matrix g+, the complete returning locus in that
group fibre consists of the two cosets `g+ A_R` and `g+ w A_R`. Each coset
is one right-flow orbit, not a continuous family of distinct packets.
Deck multiplication translates its time parameter by integral multiples
of ell, giving one circle per coset. The two cosets are not identified
by deck multiplication or actual time translation. Deck transport between
different phases of a source cycle conjugates its holonomy and preserves
the expanding/contracting distinction.

Thus the complete primitive ledger is:

- two orientation circles for each constant prime source;
- two orientation circles for the mixed source four-cycle, not eight;
- no other positive-time returns and no stationary points.

Each circle has least positive time ell, and its r-fold traversal has
time r ell. In particular the mixed circle's length is not divided by its
four source phases. The remaining points of a periodic-source group fibre
are retained and are not periodic.

### Independently derived least times

For each prime p,

    lambda_p = (p+1+sqrt((p-1)^2+4)) / (2 sqrt(p-1)),
    ell_p = 2 arcosh((p+1)/(2 sqrt(p-1))).

Since `(p+1)/sqrt(p-1) > sqrt(p)+1/sqrt(p)` and `u+1/u` increases for
u>1, `lambda_p>sqrt(p)`, so `ell_p>log p` for every prime p. Direct
Taylor expansion of the displayed exact expression gives

    ell_p = log p + 1/p + O(p^(-2)).

This is derived physical time of the frozen matrix/right-flow owner,
not exact log p and not a separately inserted roof. At p=2,

    ell_2 = 2 log((3+sqrt(5))/2).

At the mixed source phase `(7,3)`, the source outputs are 5,2,7,3. The
left-cocycle order is therefore

    B_3 B_7 B_2 B_5 = [[266,74],[100,28]],
    det = 48, trace = 294,
    tr(M_3 M_7 M_2 M_5) = 49 sqrt(3)/2,
    ell_C = 2 arcosh(49 sqrt(3)/4)
          = 2 log((49 sqrt(3)+sqrt(7187))/4).

Each of its two orientation circles has this same least time. These
mixed packets remain in the full owner.

### Actual exact-algebra check and its limit

After the independent derivation, the reviewer ran exactly this command
from the project directory; it writes no files:

```bash
python -c 'import sympy as s; B=lambda a:s.Matrix([[a,1],[1,1]]); C=B(3)*B(7)*B(2)*B(5); print("mixed numerator =", C); print("det =", C.det(), "trace =", s.trace(C)); print("normalization squared =", (3-1)*(7-1)*(2-1)*(5-1)); p=s.symbols("p", positive=True); lam=(p+1+s.sqrt((p-1)**2+4))/(2*s.sqrt(p-1)); u=s.symbols("u", positive=True); print("large-p clock difference =", s.series((2*s.log(lam)-s.log(p)).subs(p,1/u),u,0,3))'
```

Output, exit code 0:

```text
mixed numerator = Matrix([[266, 74], [100, 28]])
det = 48 trace = 294
normalization squared = 48
large-p clock difference = u + 5*u**2/2 + O(u**3)
```

This checks exact finite matrix arithmetic and the local algebraic series
against the proof formulas. It is not a numerical orbit census, a proof
of source completeness, an infinite-data experiment, or a separate
theorem justification. The complete source classification remains the
scoped 266 input, and the return classification is the full equation
argument above.

### Raw-card disposition and retained limits

No blocking defect was found in the proposed owner/contact construction.
There are three independently visible target limits: two orientations per
prime, retained mixed packets, and strict exact-clock mismatch. These
support a scoped geometric/clock engineering record and a target stop,
not natural arithmetic selection. Source and clock naturalness stay OPEN;
there is no feedback from the group fibre to the arithmetic source. No
trace, transfer space, zeta, determinant, or other T3 object is supplied.
No formal coordinates or external novelty claims are evaluated. Paused
241/242 are not used or changed.

## Checkpoint 2 — comparison with author manuscript

**Disposition: COMPLETE.** The independent results above were committed
before the reviewer read the [author manuscript](../paper.md). The first
full manuscript read had SHA-256

```text
81b8ff8b458156cfb0407cf7d1c02ae868428e6fa1ad530bcb643aac70f45bc3
```

The paper's action, quotient, contact, return, multiplicity, and least-time
proofs agree with the independent derivation. In particular its positive
cone in Lemma 1 is a proof witness for operator-norm escape; it is not
substituted for the physical group carrier. Proposition 2 explicitly
proves quotient separation without assuming a locally compact arithmetic
transversal. Proposition 3 retains negative deck powers and derives both
orientation circles from the full equation. Sections 5.1–5.3 derive the
least times, account for all source phases, and keep the mixed circles.

Root identified final editorial repairs while this comparison was in
progress. The reviewed first draft already contained the leafwise status
wording, the identity-control freeness/properness limitation, and the
explicit full-integer comparison alphabet. Its remaining equation (10)
spacing error and combined classical/formal status row were then corrected
by the author. The reviewer read back those final equation, control, and
gate sections; no additional mathematical repair was required.

The author stopped with this final paper SHA-256, which binds checkpoints
2 and 3:

```text
0c186e27af45fe9e5b3ead45bf951057c05f4ddfe704313b27e677eac990721c
```

Root subsequently appended a result section to the candidate card. Its
version-1 definition prefix was independently checked to retain the
initial SHA-256. The check removed only the appended section and its
single separator blank line:

```bash
sed '/^## Appended audit outcome/,$d' papers/268-gpf-matrix-contact-flow/candidate-card.md | sed '${/^$/d;}' | sha256sum
```

Its output was the initial card digest
`17d94ef5bb3121ed83668e913e0c95fdb35340081df4e95525f0315d2b1c3971`.
The appended result was read and agrees with the reviewed paper. This
receipt binds the paper and frozen mathematical inputs; it is not a
review of all root-owned navigation or administrative files.

## Checkpoint 3 — final counterargument and disposition check

**Disposition: COMPLETE.** The following adverse readings were checked
against the final mathematical proof and its explicit boundaries.

| Counterargument or hidden failure mode | Checked disposition |
| --- | --- |
| Positive matrices secretly restrict the physical fibre to a cone or chosen eigenline | No. Positivity supplies a norm estimate; every group element remains and the periodic locus is obtained only after solving the full equation. |
| A non-locally-compact transverse space invalidates quotient separation | The proof uses uniform group-coordinate escape and finitely many possible local deck intersections, then proves separation directly. No transverse local compactness is assumed. |
| Centralizer freedom creates continuously many primitive packets | The centralizer is the same one-parameter right flow, so it is exactly time phase within each orientation. |
| Opposite eigenline orderings can be identified in PSL or by a deck shift | PSL removes the central sign only. The normalizer's second coset is not diagonal; deck powers preserve each coset separately. Two circles are retained. |
| Four mixed source phases give extra packets or shorten the mixed time by four | Phase changes are deck identifications. At a chosen source phase a returning deck exponent must be a multiple of four, giving two circles of the full holonomy length. |
| The source theorem classifies every backward history | The proof invokes only its complete periodic ledger. Nonperiodic histories are excluded from returns by the source equation itself, without deleting those histories. |
| A returned eigenvalue is merely named a physical time | The full equation forces t to be an integer multiple of twice the logarithm of the expanding eigenvalue; converse solutions and least positive time are proved. |
| Logarithmic asymptotics repair the exact target clock | They do not. The strict inequality ell_p>log p, boundary p=2, and unchanged normalization remain explicit. |
| The identity-matrix or arbitrary-symbol controls inherit this owner's geometry automatically | The final paper says the identity replacement loses free/proper action over a constant source; the full-shift comparator states its changed alphabet and claims only the needed constant-word returns. |
| An owned contact clock establishes arithmetic naturalness or a later analytic result | The matrix assignment and time action remain declared designs, with no group-to-source feedback. Naturalness is OPEN and T3 is NOT SUPPLIED. |

No blocking mathematical finding or outstanding reviewer-requested proof
revision remains for the hash-bound manuscript. The supported disposition
is the paper's scoped leafwise geometric/clock construction together with
its target STOP / FORK: doubled prime multiplicity, retained mixed circles,
and exact-clock mismatch remain decisive. This review does not convert
that construction into a classical ASFS result, a naturalness theorem,
an analytic owner, or external validation. The full state space, physical
time, same-object boundary, and 241/242 pause remain intact.
