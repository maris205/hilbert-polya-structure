# R7: exact-return vertical fibers and the missing existence bridge

2026-09-10 UTC. One bounded source/feasibility audit. Both R6 X2 reports
remain frozen. No MS6 admission or novelty claim is made.

## 1. Claim, assumptions, notation, and status

Fix $k=\overline{\mathbf F}_p$, $f=x^d+c$ with $d\ge2$, $c\in k$,
and $g\in K^\times$, where $K=k(x)$. Write

$$\sigma a=a\circ f,\qquad \delta a=\sigma a/a,\qquad
\mathcal C_f=K^\times/\delta K^\times,$$

and consider the rational skew map

$$T(x,y)=(f(x),g(x)y).$$

At a primitive base cycle $O$ avoiding the zeros and poles of $g$, let
$n=|O|$ and $P_O=\prod_{a\in O}g(a)$. For $a\in O$, the vertical
fiber $V_a=\{a\}\times\mathbf G_m$ returns by

$$T^n(a,y)=(a,P_Oy). \tag{1.1}$$

Thus $P_O=1$ is equivalent to the restriction of the **corresponding
base-return iterate $T^n$** being the identity on $V_a$.
All intermediate restrictions are defined because the entire cycle
avoids the support of $g$. Removing finitely many exceptional cycles
on either side preserves this equivalence.

The sole existence bridge under examination is whether this cofinite
exact-return identity implies $[g]\in\mathcal C_f$ is torsion, or
constructs a finite algebraic transfer with a compatible one-step lift.
The all-$p$, all-$d$, all-$c$ scope is unchanged; base inseparability
cannot be removed as an unstated assumption.

**Status: NOT CURRENTLY JUSTIFIED.** Two targeted search batches and
actual reading of the nearest primary theorem did not supply this
bridge. This bounded outcome is not a claim that no such theorem exists.

## 2. Strategy and dependency map

1. Separate exact base return from setwise periodicity and from identity
   under an unspecified later iterate; give a direct adverse control.
2. Prove precisely what a rational first integral would supply here.
3. Match the nearest source's hypotheses, including inverse images,
   fixed versus varying iterates, characteristic, and generic separability.
4. Stop at the assigned two-query-batch boundary; record the missing arrow.

Imported input, not a new R7 result: A2's
[R6 report, §3](../../continuation_round6/a2_multiplicative_saturation/REPORT.md)
proves that a nonzero algebraic transfer $H$ in a finite $\sigma$-stable
extension, with $\widetilde\sigma H=gH$, implies an integer-power rational
relation. Its exact statement, minimal-polynomial proof, and constant-phase
caveat were read. The present report does not recount that as new progress.

## 3. Direct control: even unspecified pointwise return is automatic

**Lemma 3.1 (proved).** Every good periodic base fiber is fixed pointwise
by some positive iterate of $T$, for every $g\in K^\times$.

**Proof.** Each $P_O\in k^\times$ lies in a finite field, so it has a
finite multiplicative order $r_O$. Equation (1.1) gives

$$T^{nr_O}|_{V_a}=\operatorname{id}_{V_a}.$$

This uses no condition that $P_O=1$. $\square$

Consequently the following two proposed replacements lose the essential
information: infinitely many setwise periodic vertical fibers; and
infinitely many vertical fibers fixed pointwise by individually chosen
iterates. Neither replacement retains the length $n$ in (1.1).

Here is a direct control inside the specified skew family. Take any odd
$p$, $f=x^2$, and $g=x-1$. There are infinitely many good primitive
base cycles: roots of unity of odd order prime to $p$ are periodic under
squaring, their union is infinite, and deleting the fixed point $1$
removes only one cycle. Lemma 3.1 applies to all of them.

But $[g]$ is not torsion. If $(x-1)^m=\delta h$ for any integer $m>0$,
valuation at the fixed point $1$ gives

$$m=\operatorname{ord}_1(h\circ f)-\operatorname{ord}_1(h)=0,$$

because $x^2-1=(x-1)(x+1)$ has order one at $1$ when $p$ is odd.
This is a contradiction. By §4, this $T$ has no nonconstant rational
first integral either. Removing the fiber $V_1$ from a working open set
does not remove the valuation obstruction to an identity in $K$.

No assertion is made here that this control satisfies cofinite
**exact-base-return** identity. It is not presented as an MS6
counterexample; it refutes the two weaker proposed bridge premises.

## 4. Exact output interface: first integral if and only if torsion

**Proposition 4.1 (proved here).** For the fixed family and parameter
range of §1, the following are equivalent:

1. There is $R\in k(x,y)\setminus k$ such that $R\circ T=R$.
2. There are an integer $m>0$ and $h\in K^\times$ such that
   $g^m=\delta h$.

This equivalence does not require the periodic hypothesis or separability.

**Proof, step 1: torsion gives an integral.** Given condition 2, set
$R=y^m/h$. Then

$$R\circ T=\frac{g^my^m}{h\circ f}=\frac{y^m}{h}=R.$$

Its positive degree in $y$ shows that it is nonconstant.

**Step 2: an integral must depend on $y$.** If $R\in K\setminus k$,
its degree as a rational map on $\mathbf P^1$ is positive, and
$R\circ f=R$ would imply $d\deg R=\deg R$. Since $d>1$, this is
impossible, including when $f$ is inseparable. Thus condition 1 implies
$R\notin K$.

**Step 3: extract a nonzero Laurent coefficient.** Use the injective
formal Laurent embedding $K(y)\hookrightarrow K((y))$ and write

$$R(x,y)=\sum_{j\ge j_0}a_j(x)y^j.$$

Because $R\notin K$, some $a_j\ne0$ has $j\ne0$. Substitution by $T$
acts on this series by $a_j\mapsto\sigma a_j$ and $y\mapsto gy$;
$g$ is a unit of the coefficient field $K$, so this operation preserves
the Laurent expansion and its coefficient identities. Invariance gives

$$(\sigma a_j)g^j=a_j.$$

If $j>0$, take $m=j$ and $h=a_j^{-1}$. If $j<0$, take $m=-j$ and
$h=a_j$. Both cases give $m>0$ and $g^m=\delta h$. $\square$

The expansion at $y=0$ is a function-field device. It does not require
that $y=0$ belong to the actual open set on which $T$ is being evaluated.

A compatible finite purely inseparable cover cannot bypass this output
interface: if its first integral is $I\notin k$, choose $e$ with
$J=I^{p^e}\in k(x,y)$. Then $J\circ T=J$, and $J\notin k$ because
$k$ is algebraically closed. Proposition 4.1 again yields torsion.

The direction from a finite stable algebraic transfer to torsion is A2's
imported lemma, not a new proof here. Without the periodic hypothesis,
torsion need not give such a transfer in one compatible finite field:
A2 §3 explicitly treats the constant root-of-unity obstruction.
No unconditional three-way equivalence is asserted.

## 5. Nearest primary theorem actually read

Jason Bell, Rahim Moosa, and Adam Topaz, *Invariant hypersurfaces*,
J. Inst. Math. Jussieu **21** (2022), 713–739;
[arXiv record and publication metadata](https://arxiv.org/abs/1812.08346),
[v2 primary text](https://arxiv.org/pdf/1812.08346v2).

Theorem 8.1 permits arbitrary characteristic. It assumes fixed dominant
maps $\phi_1,\phi_2:Z\dashrightarrow X$ with geometrically reduced
generic fibers. Infinitely many hypersurfaces, defined over the separable
closure of one finitely generated subfield, must have equal proper
pullbacks under these maps. It then gives nonconstant $R$ with
$R\phi_1=R\phi_2$.

Actual reading: §1 statements/definitions; all of §8, including the
displayed proof sketch and Frobenius warning; Proposition 6.5 with proof;
the complete reduced-ring portion of Theorem 3.1's proof used by §8.
The proof uses fixed pullback identities and a finite-rank unit argument,
not identities for a different iterate at each hypersurface.
The earlier characteristic-zero theorem is not silently extended.

Cantat's original PDF returned a 403; no independent reading of that
original is claimed. The accessible BMT primary theorem is the basis
of this audit, not search-engine descriptions of Cantat's theorem.

## 6. Concrete applicability check, not a generic dismissal

For $(\phi_1,\phi_2)=(T,\operatorname{id})$, the coefficient-field
condition causes no difficulty: all data descend to a finite subfield,
and its separable closure is $k=\overline{\mathbf F}_p$.
The theorem does not require birationality or degree one.

The function-field extension induced by $T$ has degree $d$. Indeed,
after writing the image fiber coordinate as $v=g(x)y$, the only
algebraic extension is $k(x,v)/k(f(x),v)$. It is separable exactly
when $p\nmid d$. Thus the geometric-reducedness hypothesis excludes
$p\mid d$; adding a purely inseparable cover is not an operation
authorized by that theorem to remove this restriction.

Even when $p\nmid d$, two different obstacles remain:

1. **Forward return is not full inverse invariance.** For a good cycle
   $O$, put $D_O=\bigcup_{a\in O}V_a$. One has $T(D_O)=D_O$, but
   $T^{-1}(D_O)$ can contain extra predecessor fibers. For the clean
   positive control $f=x^2$, $p$ odd, $g=1$, every cycle has exact-return
   identity. But each nonzero cycle $O$ has $2|O|$ distinct inverse-image
   points, only $|O|$ of them in $O$. Its $D_O$ therefore has extra
   predecessor fibers. For example, $T^{-1}(V_1)=V_1\cup V_{-1}$.
   Distinct cycles have disjoint predecessor sets, so deleting finitely
   many fibers on one open set does not repair infinitely many cycles.
   Producing another, horizontal family would itself
   require new work; the available fibration $x=\text{constant}$ is only
   preserved as a fibration, since $x\circ T=f(x)\ne x$.
2. **The iterate is not fixed.** For any fixed $N>0$, a vertical fiber
   returned by $T^N$ must lie above a root of $f^N(x)-x$. There are
   finitely many such roots. Neither the given hypothesis nor this
   construction supplies infinitely many vertical fibers for one fixed
   pair $(T^N,\operatorname{id})$. Nor are iterate degrees bounded:
   the first coordinate of $T^N$ has degree $d^N$.

These are hand-checked failures of this proposed application. They do
not prove that the exact-return existence bridge is false, nor exclude
a different theorem exploiting the exact lengths in (1.1).

## 7. Search ledger and final handoff

Exactly two batches, four formulations each, were used:

- Batch 1: pointwise periodic curves in positive characteristic;
  skew multiplicative periodicity and rational first integrals;
  periodic hypersurfaces/first integrals; finite-field skew coboundaries.
- Batch 2: Cantat invariant-hypersurface theorem; pointwise-periodic
  rational maps; positive-characteristic skew-linear periodic curves;
  arXiv periodic-hypersurface/first-integral literature with 2024–2026 terms.

No third batch was opened. Primary opens and within-document finds
followed. No relevant local primary paper was identified; unrelated
symbolic-stream PDFs were not read. Zotero/Obsidian and an installed
arXiv-fetch script were unavailable, so the authorized web fallback was
used. No snippet or failed fetch is counted as an accessed theorem.

**Handoff:** the exact-return reformulation survives unchanged;
unspecified pointwise return is decisively insufficient; and a rational
first integral would be exactly a finite-torsion output by §4. The
cofinite exact-return premise has still not been shown to produce it.
BMT Theorem 8.1 is a real nearby theorem with a precisely mismatched
input, not the missing bridge. No nonexistence or novelty verdict follows
from the bounded search.

Only this report was written. No new agent, mathematical program,
external model/API, old/shared-file edit, Git operation, manuscript,
or PDF write was performed. Research-lit/novelty-check primary-source
discipline and proof-writer's explicit status/quantifier checks shaped
the report; their expansive search/reviewer defaults were constrained
by the coordinator's two-batch and no-external-model authorization.
