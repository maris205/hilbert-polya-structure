# Root correction: SMV's static axis is the old QEF axis

2026-09-07 UTC. Root-authored mathematical comparison, not an independent
manuscript review or admission. Both original scouting packages remain sealed
and unchanged. This supplements, rather than rewrites, lane37's source desk.

## Claim

Let $K$ be a finite field. On the same carrier $K^3$, write

$$T(x,y,z)=(x+yz,y+xz,z+xy),\qquad
F(x,y,z)=(yz-x,zx-y,xy-z),\qquad J(x,y,z)=(-x,-y,-z).$$

Then $F=T\circ J$, and for every target $u\in K^3$,

$$F^{-1}(u)=J\bigl(T^{-1}(u)\bigr).$$

Thus every one-step fibre size, the image, the maximum fibre size and the
set of maximizing targets coincide. Lane37's SMV static decoder and sharp
five-fibre bound are transferred from the earlier QEF mechanism by this
explicit input relabelling. No orbit, iterate, recurrent-set, period or
entry-time transfer follows from this identity.

## Status

PROVABLE AS STATED. Additional internal static collision, reinforcing
`NO_PROMOTION`; the missing full-carrier temporal theorem remains missing.
The distinction between a one-step input relabelling and conjugacy is essential.

## Assumptions and notation

The old literal is the QEF row of the
[original ninth-lane intake](../../scouting/finite_algebra_ninth/INTAKE.md).
Its full relevant static argument is Section6 of
[the preserved original proof](../../scouting/finite_algebra_ninth/PROOF_AND_ADAPTER_NOTES.md).
The new literal is SMV in the
[sealed lane37 intake](../../scouting/finite_systems_thirty_seventh/INTAKE.md),
with its static claim in
[the sealed author proof](../../scouting/finite_systems_thirty_seventh/PROOF_PACKAGE.md).
All coordinates in each map update simultaneously from the old state.
$G^{-1}(u)$ denotes a set of predecessors, not an inverse function.

The source-labelled QEF all-parameter claim was for odd prime fields.
Its extension to odd finite fields below is an explicit root observation
about the written field-algebra proof, not a retroactive change to that claim.

## Proof strategy and dependency map

1. Direct substitution establishes the exact map identity.
2. The involution $J$ gives a bijection of every target's predecessor sets.
3. Substitute the negated third variable into the actual old elimination
   polynomial; inspect the exceptional branches and the field hypotheses.
4. Separate this static transfer from dynamical conjugacy by fixed-point counts.

## Proof

### Step 1. Exact identity and fibre bijection

For every $(x,y,z)\in K^3$,

$$T(J(x,y,z))=(-x+(-y)(-z),-y+(-x)(-z),-z+(-x)(-y))
=(yz-x,zx-y,xy-z)=F(x,y,z).$$

Also $J^2$ is the identity. Therefore $F(v)=u$ if and only if
$T(Jv)=u$. The map $v\mapsto Jv$ is a bijection from $F^{-1}(u)$ to
$T^{-1}(u)$ and is its own inverse. Cardinality equality follows for each
target separately. A fibre is nonempty, maximal, or of any specified size
for one map if and only if the same holds for the other at that same target.

### Step 2. The displayed quintic and exceptional branches transfer

For target $u=(a,b,c)$ the old QEF proof uses

$$P_T(w)=(c-w)(1-w^2)^2-(a-wb)(b-wa).$$

The new SMV proof uses

$$P_F(z)=(z+c)(z^2-1)^2-(bz+a)(az+b).$$

Substitution gives $P_T(-z)=P_F(z)$ exactly. The old third source
coordinate $w$ equals $-z$ under $J$. The exceptional value $w=r$,
$r\in\{1,-1\}$, becomes $z=-r$; old consistency $b=ra$ becomes
new consistency $b=-az$. Negating the two remaining source coordinates
likewise transports the old exceptional quadratic solutions. Hence the
entire regular/exceptional decoder, not only its upper bound, is the same
one-step inverse mechanism under the explicit bijection.

For any odd finite field, the old proof uses only invertibility of
$1-w^2$ off $w=\pm1$, a nonzero degree-five leading coefficient,
distinctness of $1$ and $-1$, double-root divisibility at a consistent
exceptional branch, and the at-most-two-root bound for a quadratic.
All of these hold over every field of odd characteristic. The four nonzero
zero-target QEF predecessors have coordinates in $\{1,-1\}$ and product
$-1$, in addition to the zero triple. Thus its bound and witness extend
by the identical argument to every odd finite field. Their negations give
SMV's four sign predecessors with product $1$, plus zero. The maximum is
therefore five for both maps throughout the odd finite-field scope.

Using $\deg\gcd(P_F,(Z^q-Z)/(Z^2-1))$ to express the nonexceptional
field-root count is another notation for the root-count term, not a new
inverse mechanism. The polynomial $Z^q-Z$ has every field element as a
simple root; its derivative is $-1$, and removing the two simple factors
removes exactly the exceptional elements.

### Step 3. This does not transfer dynamics

In odd cardinality $q$, a fixed point of $T$ satisfies $yz=xz=xy=0$,
so it has at most one nonzero coordinate. There are $1+3(q-1)=3q-2$
such states. A fixed point of $F$ satisfies $yz=2x$, $zx=2y$, $xy=2z$.
If one coordinate is zero, the other two are zero. Otherwise division gives
$x^2=y^2=z^2=4$ and $xyz=8$, yielding exactly four nonzero sign choices.
Thus $F$ has exactly five fixed points. Since $q\ge3$, the two fixed-point
counts differ. In particular the two full finite dynamical systems are not
bijectively conjugate: a conjugacy would induce a bijection of their fixed sets.

This confirms why the valid static identity must not be replaced by an
iterate, period or clock transfer. In characteristic two, $J$ is the identity
and the two literals coincide, but the odd-field five-bound argument does
not apply; lane37 already excludes that boundary. This completes the stated
comparison without adding a pilot or changing any original theorem. ∎

## Correction and open risks

Lane37 correctly left its temporal/source questions open and did not claim
global novelty. Its selected-original desk nevertheless omitted this direct
earlier static adapter. The new comparison removes the impression that its
sharp static axis is a fresh residual within this repository. The original
three-candidate definitions, sole pilot, author deductions and genuine failed
documentary audit are preserved; their historical statements are not edited.

This root deduction is mathematical authorship and is not an independent
candidate or manuscript review. No outside novelty clearance, new execution,
paper number, or repaired temporal theorem is asserted. `HOLD_EXTERNAL`.
