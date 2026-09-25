# Source-changing collisions do not turn unimodular matrix clocks into prime times

**Paper ID:** `232-source-feedback-frontier`  
**Scope ID:** `ASFS-SCOUT-20260918-SFC01`  
**Audited short-screen candidate:** `ANG-20260918-CAC01`  
**Date / status:** `2026-09-18; EXACT CLOCK OBSTRUCTION — STOP / FORK`.  
**Formal Route coordinates:** `UNASSIGNED`. **Route B:** `NOT INVOKED`.

## Abstract

A reversible two-layer collision rule changes the letters of a finite-defect
arithmetic word. The letters are multiplicative atoms derived from the full
integer monoid. A matrix cocycle driven by that same evolving word determines
a direction-history extension and a complete scale-quotient flow. Thus the
source action and the clock have an explicit common owner. Nevertheless every
positive closed-flow return has an exponential multiplier that is an
eigenvalue of an integral unimodular matrix. It cannot be an integer greater
than one. Consequently no closed return, primitive or repeated, has time
r log p in the frozen normalization. Constant prime words do own circles of
time log((p+sqrt(p^2+4))/2), within p^(-2) of log p, but this quantitative
approximation is not the exact prime-power law. The candidate stops without
changing matrices, selecting constant words or importing a continued-fraction
operator. A separately frozen nonlinear mode-feedback candidate is owned by
233; none of its conclusions enters this proof.

## 1. Scope, lineage and nearest comparisons

The [scope and exact CAC01 subcard](candidate-card.md) were frozen before
this audit. The current search question is whether actual source-state
feedback improves on the static potential in 230 or the predicate-only
register fork in 231. The present source arrow is

```text
proper-factor exclusion / multiplicative indecomposability
  -> cover-derived atom alphabet and finite-wall words
  -> reversible additive collisions of adjacent atoms
  -> a matrix multiplier read from the same evolving source.
```

This is a precise replacement of prime-symbolic admissibility, not an
autonomous enumeration of the primes, a chronological-sieve conjugacy, or a
Logistic/Hénon geometric lift. The [prior-work guide](../../docs/prior_work/README.md)
provides this lineage frame, not a theorem for the new action.

Here source feedback means interactions among neighboring letters under F.
The matrix direction and scale are driven by that source but do not act back
on F; no bidirectional source--clock feedback is claimed. Reversible means
invertible evolution, not a proved time-reversal symmetry with an involution.

[220](../220-finite-defect-cover-flow/README.md) uses finite-defect words but
a shift/letter-scale action. [225](../225-euclid-edge-scattering/README.md)
has source-changing edges on a branch where its geometric drift excludes all
returns. The present collision action is a different full source map and
does not have that terminal/escape split. Its matrix clock is also distinct
from the directly assigned symbol roof or Gauss-system filtering examined
in [127](../127-prime-continued-fraction-digit-boundary/README.md).
None of these owners supplies its periodic or analytic results here.

## 2. Frozen definitions and same-object ledger

Let

\[
A=\{a\in\mathbb N:a\ge2,\ a\ne uv\text{ for all }u,v\ge2\},
\quad
W=\{w\in A^{\mathbb Z}:\#\{j:w_{j+1}\ne w_j\}<\infty\}.
\tag{1}
\]

The atoms A are precisely the ordinary primes, by the definition of
compositeness. No list of them is supplied. W has the product-subspace
topology with discrete coordinates, and includes every finite wall pattern.

For each S let D_S be the finite ordered list of pairs (a,b) in A squared
with a+b=S and a!=b, sorted by a. The map C fixes (a,a) and cycles D_S
by one position on every off-diagonal pair. Apply it simultaneously on even
starting pairs, then on odd starting pairs:

\[
F=C_{\rm odd}\circ C_{\rm even}.
\tag{2}
\]

For the full orbit of w put a_t=(F^t w)_0 and use the complete direction
extension

\[
\widehat W=\{(w,\xi):w\in W,\ \xi\in[0,1/2]^{\mathbb Z},\quad
\xi_{t+1}=1/(a_t+\xi_t)\},
\quad
\widehat F(w,\xi)=(Fw,(\xi_{t+1})_t).
\tag{3}
\]

Set

\[
M_a=\begin{pmatrix}a&1\\1&0\end{pmatrix},\quad
c(w,\xi)=a_0+\xi_0,\quad
G(z,r)=(\widehat Fz,r/c(z)),
\tag{4}
\]
\[
Q=(\widehat W\times\mathbb R_{>0})/\langle G\rangle,\qquad
\Phi^t[z,r]=[z,e^t r].
\tag{5}
\]

| Owner field | Exact scope |
| --- | --- |
| Carrier | Entire W, all compatible histories in (3), and full quotient (5) |
| Source action | The two collision layers (2), not a conserved integer scan |
| Multiplier | Same-source matrix identity in (4); no alternate letter roof |
| Physical clock | The actual radial action in (5), with normalization fixed |
| Packets | All primitive oriented point orbits of Phi, modulo actual time only |
| Repetitions | Traversals of the same orbit; no new label or word substituted |
| Classical geometry | NOT APPLICABLE; no positive-dimensional symplectic base supplied |
| Analytic/later owner | No transfer space, zeta, trace, determinant or quantum object |

## 3. Full reversible source and direction owner

### Proposition 1 — The collision map is a homeomorphism of W

Each collision layer and F preserve W and have continuous inverses there.
No assumption about representations of arbitrary even integers is required.

**Proof.** D_S is finite because 2<=a,b<=S-2. Whenever C queries D_S,
the input pair already belongs to it, so the list is nonempty; cyclic
successor and predecessor are mutually inverse. Diagonal pairs are a
disjoint fixed set. Thus C is a bijection of A squared.

A word in W is constant on each tail, possibly with different constants.
In either disjoint layer, only finitely many off-diagonal blocks occur;
all remaining blocks are fixed. The output still has constant tails. The
same reasoning applies to predecessor collisions. Each output coordinate
depends on finitely many input coordinates, so each layer and its inverse
are continuous in the product topology. The inverse of F reverses the
layer order and each collision. QED.

This is not an empty feedback claim. For example the atom pairs of sum 16
are (3,13), (5,11), (11,5), (13,3), and C sends the first to the second.
Starting with w_1=13 and all other entries 3, the full F yields entries 5
at -1 and 11 at 2, with all others 3. Thus the evolving letters themselves
change. This finite exact substitution is not a claim of a returning orbit.

### Proposition 2 — Every source word owns exactly one compatible history

Projection from the full space (3) to W is a homeomorphism, and
\(\widehat F\) is a homeomorphism. In particular (3) discards no source word.

**Proof.** For a>=2, f_a(x)=1/(a+x) maps I=[0,1/2] into I and is
Lipschitz with constant at most 1/4. For any two-sided driving word a_t,
the nested compact intervals

\[
f_{a_{-1}}\circ f_{a_{-2}}\circ\cdots\circ f_{a_{-N}}(I)
\tag{6}
\]

have diameters at most (1/2)4^(-N), hence have a unique common point
xi_0. The time-translated construction defines every xi_t and gives (3).
Conversely any compatible history belongs to every interval (6), proving
uniqueness. Every coordinate is positive because it is the image of a
previous coordinate under f_a.

Each finite composition is continuous as a function of w: every a_t is
the zeroth coordinate of a continuous finite iterate of F or its inverse.
The diameter bound is uniform in w, so xi_t is a uniform limit of those
continuous finite-past expressions. The graph map into the product history
space is continuous, with continuous projection as its inverse. Shifting
the unique history agrees with applying F. QED.

## 4. The quotient owns its actual clock

### Proposition 3 — Hausdorff complete flow and derived first return

The quotient Q is Hausdorff, Phi is a complete continuous flow, and r=1
is a global section with actual first-return roof

\[
\tau(z)=\log c(z)\ge\log2.
\tag{7}
\]

**Proof.** Put u=log r. Then G(z,u)=(\widehat Fz,u-tau(z)), with
continuous tau>=log2. The sum of m forward roof terms is at least m log2;
backward sums have the opposite sign and the same magnitude bound. Thus
no nonzero G iterate fixes a point. An open height interval of length less
than log2 has disjoint translates from itself under every nonzero iterate.

For any two bounded height neighborhoods, only finitely many translates
can intersect. If two points are not in the same orbit, the Hausdorff base
product separates them from each of these finitely many corresponding
translates; intersect the finitely many neighborhoods. Their saturated
neighborhoods are disjoint. This proves quotient separation without a
local-compactness assumption.

Translation of u commutes with G, so it defines (5) for every real t.
The forward and backward roof sums diverge, hence every orbit meets the
section and cannot have infinitely many crossings in a bounded time
interval. From (z,0), the first positive section time is tau(z), since
G(z,tau(z))=(\widehat Fz,0) and all later positive section times are
strictly larger forward sums. This derives (7) from (4)--(5); it does not
replace the multiplier by its letter. QED.

### Proposition 4 — Constant prime words have quadratic-unit periods

For each prime p, the constant word p has exactly one primitive flow circle,
and its least period is

\[
T_p=\log\lambda_p,\qquad
\lambda_p=\frac{p+\sqrt{p^2+4}}2.
\tag{8}
\]

Moreover

\[
0<T_p-\log p<\frac1{p^2}.
\tag{9}
\]

**Proof.** Both collision layers fix the constant word. Its unique compatible
history is constant and solves xi=1/(p+xi), giving
xi=(sqrt(p^2+4)-p)/2 and c=p+xi=lambda_p. Its full positive r-fibre
modulo multiplication by lambda_p is a single circle; every amplitude is
a time translate of every other amplitude. The least positive return is
log lambda_p, with repeats r log lambda_p.

Since sqrt(1+4/p^2) lies strictly between 1 and 1+2/p^2, we have
1<lambda_p/p<1+1/p^2. Applying 0<log(1+x)<x gives (9). QED.

This supplies a genuine approximate prime-scale control. It does not supply
exact log p. Nor can a single global time conversion make every (8) equal
log p: the ratio T_p/log p tends to 1 along the unbounded primes, forcing
the conversion to be 1, whereas (9) is strict for every prime.

## 5. Decisive obstruction for every possible closed return

### Theorem 5 — No positive closed time exponentiates to an integer

If a full Phi orbit returns after time T>0, then e^T is an eigenvalue of
an integral matrix of determinant +1 or -1. In particular

\[
e^T\notin\{2,3,4,\ldots\},\qquad
T\ne r\log p\quad(p\text{ prime},\ r\ge1\text{ integer}).
\tag{10}
\]

This includes all repeated returns, not merely constant words or primitives.

**Proof.** A flow return in the quotient means that for some integer m,
\(\widehat F^m z=z\) and T equals the signed m-step roof sum. Positivity
of the roof and T imply m>0. Write z_t=\widehat F^t z. The exact identity

\[
M_{a_t}\binom1{\xi_t}=c(z_t)\binom1{\xi_{t+1}}
\]

gives, after m steps,

\[
A_m\binom1{\xi_0}=e^T\binom1{\xi_0},\qquad
A_m=M_{a_{m-1}}\cdots M_{a_0}\in\operatorname{Mat}_2(\mathbb Z),
\quad \det A_m=(-1)^m.
\tag{11}
\]

If R=e^T were an integer greater than one, the characteristic equation
R^2-(tr A_m)R+det A_m=0 would make R divide det A_m=+1 or -1, an
impossibility. Since e^(r log p)=p^r is such an integer, (10) follows.
No enumeration of periodic source words is used. QED.

The matrix multiplier is therefore an algebraic unit, whereas the required
integer prime/power multiplier is not. This is a scoped obstruction to the
frozen integral-unimodular clock mechanism, not a no-go theorem for all
arithmetic flows or all matrix cocycles.

## 6. Controls and remaining gaps

| Control | Exact consequence | Boundary |
| --- | --- | --- |
| Delete all collisions, using F=id as a different owner | Constant-word circles and (8) remain; every word is now fixed, producing countably infinitely many circles at each fixed zeroth letter p | Theorem 5 still applies; deleting collisions adds multiplicity but does not repair the clock |
| Replace atom alphabet by all integers >=2 | The same owner proof works, and constant composite words also give circles | The general clock construction is not a prime selector |
| Globally rescale time | Constant-circle asymptotics force scale 1 if all target log p times are required | No fixed global conversion repairs (8) |
| Replace M_a by diag(a,a^(-1)) | The integer-unimodular hypothesis is lost, and the selected eigenvalue can be a | This is a different matrix/direction owner, not an allowed repair |
| Keep only constant source words | Removes genuine states of W | Forbidden sector selection; not the candidate's full ledger |

For the identity-collision control, W is countable: a word is specified by
finitely many wall positions and letters. There are infinitely many words
with w_0=p, and each owns its separate r-circle with multiplier lambda_p.
Thus that multiplicity is countably infinite, not a continuous family.

The complete nonconstant periodic-word classification is NOT SUPPLIED.
Whether a returning word uses nontrivial collisions remains OPEN here. These
questions are not needed for (10), so the rapid clock stop does not justify
a longer local search. The source alphabet, finite-wall rule, collision
ordering and scale law remain declared designs; naturalness is OPEN.

## 7. Bounded source retrieval and its disposition

The source-feedback search also re-encountered two already documented
external controls. Kopra's introduction defines direct primeness in terms
of product decomposition of subshifts; that terminology is not an ordinary
prime-number source. This is the existing
[112 collision](../112-direct-prime-subshift-terminology-boundary/README.md),
not a newly admitted candidate. See [Kopra, DOI 10.1017/etds.2022.33](https://doi.org/10.1017/etds.2022.33).

The Prime Clockwork abstract distinguishes an expanding clock installation
process from the grand cycles of finite installed seconds arrays. The
existing [118 owner boundary](../118-prime-clockwork-growth-cycle-owner-boundary/README.md)
therefore remains relevant; no finite-array cycle is transferred to the
growth action here. See [Emmerich, arXiv:2609.03896v1](https://arxiv.org/abs/2609.03896v1).
This was targeted retrieval, not a systematic review or a claim that all
relevant literature has been exhausted. CAC01's mathematical results above
are proved directly from its card and do not depend on either external work.

## 8. Portfolio decision and separate nonlinear lane

| Gate | CAC01 result | Boundary |
| --- | --- | --- |
| T0 | Full reversible source, unique full history extension, Hausdorff quotient and complete actual flow established | Broadened symbolic/groupoid owner only |
| T1 | Source-changing collisions are explicit; clock comes from the same driven multiplier | Naturalness OPEN; no endogenous prime enumeration |
| T2 | Constant-word primitive ledger exact; all closed return times satisfy (10) | Exact prime-power clock FAIL; complete mixed ledger NOT CLASSIFIED |
| T3 | No operator, trace, zeta or determinant developed | NOT ADVANCED after the decisive clock stop |
| Classical A0/A1/A2 | No finite-dimensional symplectic base | NOT APPLICABLE |
| Formal Route / B | No formal evaluation | UNASSIGNED / NOT INVOKED |

**CAC01 decision: STOP / FORK.** Preserve its source-feedback construction
and approximate constant-circle time as scoped controls. The decisive gate
reason is the arithmetic of its own integral matrix return multiplier.
The same-object ledger is intact; neither the matrices nor time were changed.

The other retained proposal is the separately frozen
[233 multiplication-resonant mode flow](../233-multiplicative-resonant-flow/candidate-card.md),
`ANG-20260918-MRF01`. It acts on all integer amplitudes through factor
fusion/fission in physical time and has its own full-carrier audit. It is
not a clock correction to CAC01, and none of its eventual results transfers
to this screen. Its detailed outcome belongs to its own paper and ledger.

The completed [233 proof](../233-multiplicative-resonant-flow/paper.md)
establishes that full global mild action and constructs an actual periodic
packet in its powers-of-6 sector. That lane therefore also stops, for a
different reason: the nonlinear source admits an intrinsic mixed-prime
return. Its remaining periodic set is unclassified. The portfolio closes
with two distinct scoped stops and two retained owner constructions, not a
combined candidate or accumulated Route credit.

## Evidence, limits and disclosure

The [card](candidate-card.md), [claim ledger](claim-ledger.md) and
[evidence index](evidence/README.md) preserve exact inputs and verification.
No numerical orbit search, random sample, GPU run, finite-cutoff extrapolation,
PDF or publication artifact is needed for the results above.

Data availability: all construction inputs and proofs are in this package.
Ethics: no human subjects or private data are involved. Author contributions:
AI-assisted candidate formalization, proof drafting and technical checking;
no human CRediT role is inferred. Funding and conflict declarations were not
supplied. This internal record and model checking are not external peer
review, publication readiness or a correctness certificate.
