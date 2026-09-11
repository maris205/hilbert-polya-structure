# Self-displacement difference: frozen theorem contract

## Gate status

`PROMOTE_PROOF_SPIKE / OWNER_AMBER / HOLD_EXTERNAL`.

This document freezes only the statements proved below.  It does not assign
novelty, priority, or freedom to operate.  In particular, the complete
functional graph of the full carrier is **not** claimed.

## Literal finite system

Let (p) be an odd prime and

\[
  \mathcal X_p=\{f:\mathbb F_p\longrightarrow\mathbb F_p\}.
\]

Define the self-displacement difference

\[
  (D_pf)(x)=f\bigl(x+f(x)\bigr)-f(x),\qquad x\in\mathbb F_p.
\]

All (p) output values are computed synchronously from the old function.
There is no selector, tie-break, exceptional branch, or imposed hold rule;
a state holds exactly when the displayed formula returns the same function.

## The affine invariant stratum

Write (f_{a,b}(x)=ax+b) and

\[
  \mathcal A_p=\{f_{a,b}:a,b\in\mathbb F_p\}\subset\mathcal X_p.
\]

### Theorem A: complete affine temporal atlas

The stratum \(\mathcal A_p\) is invariant, and in its coefficient
coordinates

\[
 D_p(a,b)=(a^2,ab),\qquad
 D_p^t(a,b)=\left(a^{2^t},,b a^{2^t-1}\right)\quad(t\geq 0),
\]

with the second formula interpreted directly at (t=0).

If (a\ne0), write

\[
  \operatorname{ord}(a)=2^s r,\qquad r\text{ odd}.
\]

Then ((a,b)) has exact tail (s) and eventual period

\[
  \operatorname{ord}_{r}(2),
\]

where the period is (1) when (r=1).  The state ((0,0)) is fixed, and
each ((0,b)) with (b\ne0) has tail (1) to it.

For every (t\ge1),

\[
 \left|\operatorname{Fix}\left(D_p^t\mid\mathcal A_p\right)\right|
   =1+p\gcd\left(p-1,2^t-1\right).
\]

Consequently the least-period census on the affine stratum follows by
Möbius inversion.

#### Proof

Direct substitution gives

\[
\begin{aligned}
 D_pf_{a,b}(x)
 &=a\bigl(x+(ax+b)\bigr)+b-(ax+b)\\
 &=a^2x+ab.
\end{aligned}
\]

Induction yields the iterate formula.  Squaring removes exactly one factor
of (2) from the order of (a) at each step until its order is odd.  On
the odd-order subgroup, squaring is a permutation; return occurs precisely
when (2^t\equiv1\pmod r).  Once the first coordinate returns, the second
coordinate multiplier is (a^{2^t-1}=1), so (b) imposes no additional
period condition.  Finally, an iterate-fixed nonzero (a) is exactly a
solution of (a^{2^t-1}=1) in the cyclic group
(\mathbb F_p^\times), and every one of the (p) values of (b) then
works.  The single remaining iterate-fixed point is ((0,0)).

### Theorem B: all-time affine fibres

Fix (t\ge1) and a target ((A,B)\in\mathbb F_p^2).  Then

\[
 \left|(D_p^t\mid\mathcal A_p)^{-1}(A,B)\right|=
 \begin{cases}
 p,&(A,B)=(0,0),\\
 0,&A=0,\ B\ne0,\\
 2^{\min(t,\nu_2(p-1))},
   &A\ne0\text{ and }A\in(\mathbb F_p^\times)^{2^t},\\
 0,&A\ne0\text{ and }A\notin(\mathbb F_p^\times)^{2^t}.
 \end{cases}
\]

For every nonzero root (a^{2^t}=A), the corresponding source has the
unique second coordinate

\[
                    b=B a^{1-2^t}.
\]

#### Proof

This is immediate from the iterate formula.  The kernel of the
(2^t)-power homomorphism of the cyclic group
(\mathbb F_p^\times) has size
(\gcd(p-1,2^t)=2^{\min(t,\nu_2(p-1))}).  When (a=0), every (b)
maps to ((0,0)) after one or more steps.

## Full-carrier fixed points

Define the bijection

\[
 L:\mathbb F_p^2\longrightarrow\mathbb F_p^2,
 \qquad L(x,c)=(x+c,2c).
\]

Let (C=\langle2\rangle\le\mathbb F_p^\times).  Form a labelled
hypergraph (\mathcal H_p) with vertex set (\mathbb F_p).  For every
nonzero (L)-orbit include one labelled edge equal to its projection on
the first coordinate.  Concretely, the orbit through ((b+a,a)) is

\[
 \mathcal O_{b,aC}=\{(b+c,c):c\in aC\},
\]

and its projected edge is (b+aC).  Edges remain labelled by their
phase-space orbits even if two projected subsets happen to coincide.

### Theorem C: fixed graphs are orbit packings

There is a bijection

\[
 \operatorname{Fix}(D_p)\longleftrightarrow
 \{\text{matchings of the labelled hypergraph }\mathcal H_p\}.
\]

For a matching, put (f(b+c)=c) on each chosen edge (b+aC), and put
(f(x)=0) on every uncovered vertex.

#### Proof

The fixed equation is

\[
              f(x+f(x))=2f(x).
\]

It says exactly that the graph
(\Gamma_f=\{(x,f(x)):x\in\mathbb F_p\}) is forward invariant under
(L).  Since (L) is a bijection and the graph is finite, forward
invariance is invariance.  The (c=0) orbits are the singletons
((x,0)).  Every nonzero orbit has the displayed form, and its first
coordinates are distinct because multiplication by (2) runs through a
multiplicative coset.  A union of nonzero orbits is part of a function graph
exactly when their projected edges are pairwise disjoint.  The uncovered
first coordinates must then be filled by their zero singleton orbits.

### Corollary: primitive-root specialization

If (2) is primitive modulo (p), then

\[
                        |\operatorname{Fix}(D_p)|=p+1.
\]

Indeed every nonzero orbit projects to
(\mathbb F_p\setminus\{b\}).  Two such edges intersect, so a matching is
either empty or consists of one of the (p) nonzero orbits.

The primitive-root hypothesis is necessary.  For (p=7),
(C=\{1,2,4\}); the hypergraph has fourteen labelled three-edges and
seven disjoint pairs.  Hence it has

\[
                            1+14+7=22
\]

matchings and (D_7) has (22) fixed functions, not (p+1=8).

## Exact pilot boundary

The dependency-free verifier exhausts the full functional graph for
(p=2,3,5), uses a memory-bounded integer encoding to exhaust the full
functional graph for (p=7), checks the affine atlas for several odd primes
through (19), and checks the orbit-matching formula through (19).  At
(p=7) it obtains:

- (823543) states and (186740) image states;
- (22) fixed and (2416) recurrent states;
- maximum tail (12);
- cycle counts
  (1:22,2:588,3:126,4:42,6:98,12:7);
- maximum one-step fibre (298).

These (p=7) whole-graph numbers are pilot evidence, not an extrapolated
theorem.  In particular, neither a full-carrier clock formula nor a
full-carrier every-target fibre formula is part of this contract.

## Permitted and forbidden claims

Permitted:

- the literal definition of (D_p);
- Theorems A--C and the primitive-root corollary;
- exact finite pilot data explicitly reproduced by the verifier;
- the statement that the full map is dynamically different from its
  affine invariant stratum.

Forbidden without a new proof:

- (|\operatorname{Fix}(D_p)|=p+1) for arbitrary primes;
- a uniform bound or formula for the full-carrier tail or period;
- a classification of all recurrent full-carrier states;
- an all-target full-carrier inverse formula;
- treating the ordinary squaring coordinate on the affine stratum as a
  contribution claim;
- any novelty, priority, or external-owner claim.
