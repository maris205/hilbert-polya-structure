# A1 Round 2: exact trace/coboundary interface; finiteness still open

2026-09-09 UTC. Author continuation, not an admitted paper or completed
PC424-L proof. The exact frozen question and full proofs are in
[PROOF_PACKAGE.md](PROOF_PACKAGE.md). First-pass accepted results remain
read-only inputs. The proof-writer discipline was used to freeze the
unchanged quantifiers and to distinguish proved interfaces from the
unproved finiteness bridge.

## Result and boundary

For every odd $p$, $k=\overline{\mathbb F}_p$, $c\in k$, and
$f=x^2+c$, the original question is still whether zero sums of $h\in k[x]$
over every ordinary primitive cycle force $h=Q\circ f-Q$.
Periods divisible by $p$ remain included, and each orbit point is counted
once. The targeted bridge was a scalar linear relation among the full
polynomial Frobenius powers $h,h^p,h^{p^2},\ldots$ modulo polynomial
coboundaries. **That bridge and PC424-L remain unproved.**

This round supplies an algebraic interface that preserves both sides
exactly. Put $R=k[x]$, $\sigma Q=Q\circ f$,
$D=\varinjlim(R,\sigma)$, and let $\alpha$ be the automorphism
induced by $\sigma$. Then use the finitely presented skew Laurent algebra
$A_f=D[T,T^{-1};\alpha]$.

| Exact output | Proof location | Reuse |
| --- | --- | --- |
| All finite-dimensional simple modules are ordinary primitive cycles with a nonzero scalar return twist. | Proposition 2.1 | No extra hidden simple representations and no omitted critical/wild-period cycles. |
| Trace on $h$ is precisely its ordinary cycle sum; arbitrary finite-dimensional modules impose no additional trace conditions. | Corollary 2.2 | The original kernel is the polynomial sector of the finite-representation trace radical. |
| $HH_0(A_f)_0\cong R/(\sigma-1)R$. | Proposition 3.1, (7) | The quotient is exactly the desired polynomial-coboundary space. Direct-limit descent is elementary; R6 is unnecessary here. |
| $HH_0(A_f)_n\cong(R/(f^{|n|}-x))/(\sigma-1)(R/(f^{|n|}-x))$ for $n\ne0$. | Proposition 3.1, (8) | The other grades retain full nonreduced periodic-scheme coinvariants, connecting to the coordinator's nilradical route. |
| A trace-zero class is Frobenius-nilpotent in each finite-dimensional quotient, with quotient-dependent exponent. | Section 4 | Pinpoints the local-to-global uniformity gap; does not supply it. |

The eigenspace argument in Proposition 2.1 is valid on critical cycles:
$XT^{-1}=T^{-1}f(X)$ makes the sum of ordinary eigenspaces
$T^{-1}$-stable; invertibility and finite dimension make it stable under
$T$ too, so simplicity makes $X$ semisimple. No derivative condition or
division by cycle length occurs.

## Source subtraction and failed general shortcut

The homology formalism is classical, not a proposed independent novelty
claim. The package gives elementary proofs of this exact specialization.
The accepted first-pass free Frobenius-module result, finite coefficient
descent and algebraic-transfer implications were not re-proved.

The primary-source audit checks the actual hypotheses of Etingof's
character theorem and Klep–Špenko's tracial Nullstellensatz. Neither gives
trace separation for this infinite-dimensional characteristic-$p$ quotient
algebra. The first needs a finite-dimensional semisimple algebra for the
spanning conclusion; the second concerns characteristic-zero free-algebra
trace equations on unconstrained matrix tuples.

An explicit Leavitt $L_2$ control rules out a blanket theorem for all
finitely presented algebras: it has no nonzero finite-dimensional unital
modules, but the classes $[u_1^{p^i}]$ are nonzero and lie in distinct
Hochschild grades, using Ara–Cortiñas Theorem 4.4. This refutes that general
shortcut, **not** the proposed result for $A_f$ or PC424-L.

## Handoff

The concrete remaining target is a theorem special to $A_f$ that promotes
the finite-quotient local Frobenius-nilpotence to one finite relation in
$HH_0(A_f)_0$. It must preserve the ordinary reduced orbit tests, specify
the missing uniform bound or separation mechanism, and exclude the
Leavitt control by an actual hypothesis. The nonzero-grade formula may
allow the periodic-nilradical lane to identify that missing mechanism.

All substantive interfaces were sent to the coordinator as obtained.
An independent checker was requested from the coordinator, but no
nonauthor acceptance is claimed here. There were no mathematical runs,
old reruns, manuscript/PDF changes, evaluations, shared-index edits or
Git actions. Only this round's assigned directory was written.
