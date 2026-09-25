<!-- PSR01 CORRECTION NOTICE START -->
> **2026-09-19 bounded dependency correction.** The noninjectivity and continuous-discrete-factor obstructions below remain valid. References to 078/079 do NOT inherit their withdrawn unique-packet or finite-zeta claims. 079 remains a valid full path owner with a corrected, infinite periodic ledger.
> See the [PSR01 source correction](../266-prime-source-return-rescreen/paper.md).
> This notice changes no frozen candidate definition or Route status.
>
> **Historical text retained below; the specified comparison is superseded.**
<!-- PSR01 CORRECTION NOTICE END -->

# The noninjective GPF map cannot be lifted by a state-componentwise symplectic diffeomorphism

**Paper ID:** 080-gpf-symplectic-fibre-lift-obstruction  
**Record ID:** ASFS-SCOUT-20260914-54  
**Date / status:** 2026-09-14; PRE-P0 STOP  
**Route state:** No ASFS Route-A coordinate; Route B NOT INVOKED.

## Exact lift class

Let S=N_{>0}^2 and let

\[
G(x,y)=(y,\operatorname{gpf}(x+y)).
\]

The most direct way to try to preserve its arithmetic state is to choose a
positive-dimensional symplectic manifold for every state a in S, form a
disjoint union

\[
M=\bigsqcup_{a\in S}M_a,
\]

and require a symplectic diffeomorphism F:M->M to satisfy

\[
F(M_a)=M_{G(a)}
\quad\text{for every }a\in S.
\]

This would make the GPF recurrence a genuine component-level factor and keep its
complete state/packet ledger attached to the proposed geometry.

## Obstruction

**Proposition.** No F in the stated lift class exists.

**Proof.** A homeomorphism, hence a symplectic diffeomorphism, maps connected
components bijectively onto connected components. It therefore induces a
bijection on the labels a. The required induced label map is G. But

\[
G(1,1)=(1,\operatorname{gpf}(2))=(1,2)
=G(3,1)=(1,\operatorname{gpf}(4))=(1,2),
\]

so G is not injective and cannot be the component permutation induced by F. ∎

The common repair of placing all states in a connected smooth M also fails as a
direct factor construction: a continuous map from connected M to the discrete
space S has connected, hence singleton, image. It cannot be a nonconstant
surjective arithmetic-state observation.

## Scope and ownership

This proposition does not show that no symplectic system can contain some
encoding of G. It shows that the natural state-fibre lift, which would preserve
the exact transition and all state labels without an external selector, is
impossible. A connected embedding would need a discontinuous or otherwise
new observation mechanism, and a reversible completion would enlarge the state
with inverse-branch data. Either is a new object; it cannot inherit 078's A0/A1
or 079's T0–T3 results automatically.

| Gate | Result |
| --- | --- |
| 078 arithmetic source | retained as a separate control |
| direct componentwise symplectic P0 lift | scoped FAIL |
| connected continuous discrete factor | scoped FAIL |
| other geometry | OPEN, requires a fresh candidate card |
| Route B | NOT INVOKED |

## Decision

**Portfolio position: stop/fork for direct classical lifts.** Do not thicken the
integer states into independently permuted symplectic disks, tori, or fibres:
the noninjective arithmetic transition forbids it before orbit or roof work.
079 remains the valid type-labelled path/groupoid realization. A later classical
proposal must explicitly replace the factor relation and account for the new
state data.

## Evidence index

- [078 GPF-Fibonacci A0/A1 control](../078-gpf-fibonacci-a0-a1-control/paper.md)
- [079 GPF path-groupoid suspension](../079-gpf-path-groupoid-flow/paper.md)
- [033 wheel-packet symplectic-thickening screen](../033-wheel-packet-symplectic-thickening-screen/paper.md) — related ledger-ownership control only.
- [052 hyperbolic wheel-packet lift](../052-hyperbolic-wheel-packet-lift/paper.md) — distinct componentwise construction; no result transferred.
