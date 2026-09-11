# Drazin feedback: one source-known negative entrance

Author/proof contributor: `/root/round211_fresh14`, 2026-09-10 UTC.
This is an author-side subtraction certificate, not independent review.

## Claim, assumptions and notation

Fix a prime power $q$ and $n\geq1$. The finite carrier is
$X=\operatorname{End}_{\mathbb F_q}(V)$ for $V=\mathbb F_q^n$.
The literal autonomous update is $T(A)=A^D$, the Drazin inverse recomputed
from the current matrix. No transpose, ordering, regularization, selected
singular branch or extra state is added. This is the sole explicitly
formulated entrance in fresh14; the operation is classical, not newly invented.

The Drazin inverse is the unique $B$ satisfying, for some integer $h\geq0$,
$$
A^{h+1}B=A^h,\qquad BAB=B,\qquad AB=BA.
$$
Uniqueness is the standard algebraic result whose full proof was read in
[Cockett--Pacaud Lemay--Srinivasan, Proposition 2.3](https://arxiv.org/html/2402.18226v2).
Below, $\operatorname{Nil}(W)$ denotes nilpotent endomorphisms of $W$.
Transient depth is the least nonnegative time at which an orbit is periodic.

For all such $q,n$:

1. $T^3=T$. The recurrent set and first image are exactly
   $\mathcal R=\{B:\ker B=\ker B^2\}$. Fixed points satisfy $B^3=B$;
   the other recurrent states have exact period two.
2. For the canonical Fitting decomposition $A=C\oplus N$, the depth is
   zero exactly when $N=0$, otherwise one. The largest depth is zero at
   $n=1$ and one at every $n\geq2$.
3. A target outside $\mathcal R$ has no preimage. For $B\in\mathcal R$,
   let $U=\operatorname{im}B$, $W=\ker B$, $k=\dim W$, and
   $D=B|_U$. Then the entire fibre is
   $$
   T^{-1}(B)=\{D^{-1}\oplus N:N\in\operatorname{Nil}(W)\},
   \qquad |T^{-1}(B)|=q^{k(k-1)}.
   $$
4. For $n\geq2$, zero is the unique maximum-fibre target, with
   $q^{n(n-1)}$ sources. At $n=1$, every target has one source.

## Status

**PROVABLE AS STATED**, using the explicitly cited classical nilpotent
count. **NO_PROMOTION**: the temporal conclusion is an instance of the
already-written section/label wrapper; the evaluated inverse is the
classical nilpotent enumeration on one forced subspace.

## Strategy and dependency map

Rank stabilization gives a unique invertible/nilpotent split. It gives
the update and recurrence without an experiment. The produced matrix
fixes both summands, so inverse recovery leaves only an arbitrary nilpotent
on its kernel. The nilpotent count is an imported theorem, not an original
enumerative proof or an empirical formula.

## Proof

**Step 1 — Fitting decomposition over the stated field.**
The descending image chain of $A$ stabilizes by time $n$. Once two
successive image dimensions agree, equality of the images and applying
$A$ give stabilization at every later time. Rank-nullity gives the same
stabilization for the ascending kernels. Put
$U_A=\operatorname{im}A^n$ and $W_A=\ker A^n$.
If $x=A^ny\in U_A\cap W_A$, then $A^{2n}y=0$, so kernel stabilization
implies $A^ny=0$ and $x=0$. Rank-nullity now gives $V=U_A\oplus W_A$.
Both summands are invariant. The restriction $C=A|_{U_A}$ is surjective,
hence invertible; $N=A|_{W_A}$ is nilpotent.

This split is unique among invariant invertible/nilpotent splits: on any
invertible summand all powers have full image and trivial kernel; on an
at-most-$n$-dimensional nilpotent summand the $n$th power is zero.
Thus its summands must be $U_A,W_A$.

**Step 2 — The update and complete recurrence.**
On this decomposition define $B=C^{-1}\oplus0$. Direct block multiplication
verifies all three Drazin equations with $h=n$, so uniqueness gives
$T(A)=B$. The next two iterates are
$$
T^2(A)=C\oplus0,\qquad T^3(A)=C^{-1}\oplus0=T(A).
$$
Consequently every image is periodic with period dividing two. Conversely,
a periodic state lies in the image of $T$. A matrix has zero nilpotent
block exactly when $\ker B=\ker B^2$: on a nonzero nilpotent block the
first kernel inclusion must be strict, since equality would stabilize
the entire kernel chain at its first term and force the block to be zero.
This proves the image/recurrent description and the asserted depths.
On $\mathcal R$, equality with its inverse is $C^2=I$, equivalently
$B^3=B$. No other periods occur. Nonzero nilpotent matrices do not exist
in dimension one; in each dimension at least two, a single size-two
nilpotent Jordan block plus zeros has depth one. All characteristics,
including two, are covered; involutions need not be diagonalizable.

**Step 3 — The complete inverse, with no free complementary-space factor.**
Suppose $T(A)=B$. Step 2 identifies $\operatorname{im}B=U_A$ and
$\ker B=W_A$, so $B$ determines the actual subspaces of the original
labelled vector space, not merely their dimensions. Its invertible
restriction determines $A|_{U_A}=D^{-1}$. The only remaining block is
any nilpotent $N$ on $W_A$. There is no off-diagonal freedom, since the
Fitting summands are $A$-invariant. Conversely each such block matrix
has Drazin inverse $B$. This proves the displayed fibre bijection.

For a $k$-dimensional vector space over $\mathbb F_q$, the classical
Fine--Herstein/Hall count is $|\operatorname{Nil}(W)|=q^{k(k-1)}$.
An original proof was actually read as
[Leinster, Theorem 5](https://arxiv.org/html/1912.12562v2), which constructs
$\operatorname{Nil}(W)\times W\cong\operatorname{End}(W)$.
The $k=0$ case has one zero-dimensional endomorphism and gives the same
formula. This proves the count without claiming a new proof of that theorem.

**Step 4 — Extremum and edge cases.**
The exponent $k(k-1)$ is zero at $k=0,1$ and strictly increasing for
$k\geq1$. For $n\geq2$, its unique largest possible $k$ is $n$;
the only target with $\ker B=V$ is zero. All dimension-one targets have
$k=0$ or one, so all fibres have size one. This proves the final claim. ∎

## Exact subtraction, not a keyword exclusion

The already-written local
[section-wrapper proof, Step 1.1](../finite_algebraic_normal_form_fresh_desk/PROOF_PACKAGE.md)
states that $T=sg\pi$, with $\pi s=\mathrm{id}$, satisfies
$T^t=sg^t\pi$ and has fibres obtained directly from $\pi$.
Here let the label set consist of triples $(U,W,C)$ with
$V=U\oplus W$ and $C\in\operatorname{GL}(U)$; let $\pi$ forget the
nilpotent block of the canonical Fitting decomposition; let $s$ insert
zero on $W$; and set $g(U,W,C)=(U,W,C^{-1})$.
These are defined for every state and $\pi s=\mathrm{id}$, $g^2=\mathrm{id}$.
Thus the entire temporal result is this exact old proof adapter.
Step 3 evaluates its remaining projection fibre by a source-owned static
count. No residual coupled clock or independent inverse mechanism remains.

This is not a literal identification with the old companion map or with
P103 double adjugation. For example, a nonzero singular projection in
dimension at least three is fixed by $T$, while P103 sends it to zero.
The P103 original's Jacobi/determinant normal form, not its title, supports
that distinction. Gram-related search returns were navigation only;
no unread Gram theorem is used to rule out this entrance.

## Corrections and open risks

No assertion of global novelty, global exhaustion, or a completed paper
follows. No finite pilot or independent candidate gate was performed.
The later Drazin paper's inverse-of-inverse subsection was visible only
as a heading; targeted body requests failed. The temporal proof above
does not pretend that subsection was read. The original 1958 theorem
pages were not successfully received from the publisher; the actually
read Leinster theorem/proof is the primary proof used for the count.
