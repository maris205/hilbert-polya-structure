<!-- PSR01 CORRECTION NOTICE START -->
> **2026-09-19 superseding correction — ANG-20260914-GPF01.**
> Current status: **CORRECTED FULL LEDGER — INFINITE UNIT PRIMITIVES; ORDINARY ZETA WITHDRAWN**.
> The unchanged full path suspension has one time-1 primitive per prime and one time-4 primitive. Every shift iterate has infinitely many fixed paths. The old finite Fix count and claimed full ordinary zeta below are WITHDRAWN; its repetition series has no absolute-convergence half-plane. The path owner and unit roof are unchanged.
> See the [complete correction and proof](../266-prime-source-return-rescreen/paper.md).
> Full carrier, action, roof and same-object identity are preserved;
> formal coordinates UNASSIGNED, Route B NOT INVOKED.
>
> **Historical text retained below; superseded claims must not be used.**
<!-- PSR01 CORRECTION NOTICE END -->

# The GPF-Fibonacci natural extension gives one exact arithmetic path packet and its same-object suspension zeta

**Paper ID:** 079-gpf-path-groupoid-flow  
**Record ID:** ANG-20260914-GPF01  
**Date / status:** 2026-09-14; BROADENED T0–T3 ESTABLISHED  
**Classical Route state:** NOT APPLICABLE; Route B NOT INVOKED.

## Frozen broadened object

Let S=N_{>0}^2 and let G:S->S be the exact GPF-Fibonacci map from 078,

\[
G(x,y)=(y,\operatorname{gpf}(x+y)).
\]

Define its two-sided natural-extension path space

\[
X_G=\{z=(z_j)_{j\in\mathbb Z}\in S^{\mathbb Z}:z_{j+1}=G(z_j)
\text{ for all }j\in\mathbb Z\}.
\]

The left shift sigma(z)_j=z_{j+1} is an invertible action on X_G. The broadened
carrier may equivalently be recorded as the transformation groupoid
X_G semidirect Z. Its arithmetic mechanism is not a label added to the shift:
every adjacent pair in every path obeys the same gpf update G.

Use the constant roof tau=1 and form the suspension

\[
Y_G=(X_G\times[0,1]) / ((z,1)\sim(\sigma z,0)).
\]

This is a path/groupoid suspension, not a claim that Y_G is symplectic,
Hamiltonian, smooth finite-dimensional, or a classical ASFS mapping torus.

## T0–T2: carrier, endogenous arithmetic, and complete packet ledger

The arithmetic source is inherited without change from G: the greatest prime
factor of x+y is evaluated at every edge. The relation to the project lineage is

prime-factor observable -> autonomous second-order arithmetic recurrence ->
two-sided symbolic path deformation.

This is a direct replacement of the first three lineage arrows, not a claim of
the Logistic-to-Hénon or conservative lift arrows.

If sigma^n z=z, then z_0 is G-periodic with G^n z_0=z_0. By the Back--Caragiu
theorem used in 078, all G trajectories ultimately enter the unique 4-cycle.
Thus every G-periodic state lies on that cycle. Conversely its four phase paths
are sigma-periodic. Hence

\[
\#\operatorname{Fix}(\sigma^n)=
\begin{cases}
4,&4\mid n,\\
0,&4\nmid n.
\end{cases}
\]

The four points are phases of **one** oriented primitive shift orbit, not four
primitive packets. Under the unit suspension it becomes one primitive closed
orbit of time 4; its r-th repetition has time 4r.

## T3: same-object zeta

The Artin--Mazur formal zeta of the exact shift is

\[
Z_\sigma(z)=
\exp\!\left(\sum_{n\ge1}
\frac{\#\operatorname{Fix}(\sigma^n)}{n}z^n\right)
=\exp\!\left(\sum_{r\ge1}\frac{z^{4r}}{r}\right)
=\frac1{1-z^4}.
\]

With the same unit roof, the oriented primitive-orbit product is

\[
\zeta_G(s)=\prod_{\gamma\;\mathrm{primitive}}
(1-e^{-sT_\gamma})^{-1}
=\frac1{1-e^{-4s}},\qquad \operatorname{Re}s>0.
\]

The displayed product is deliberately modest: it has one packet and a unit
clock. It neither contains log p, prime-power data, an explicit-formula divisor,
nor any Riemann-zero claim.

| Broadened audit | Result |
| --- | --- |
| T0 carrier/type and same-object ownership | established |
| T1 endogenous arithmetic and clock | gpf mechanism established; unit clock only |
| T2 closed packet and repetitions | established: one primitive packet, 4r repetitions |
| T3 same-object zeta | established for Re(s)>0 |
| classical P0/A0--A2 | NOT APPLICABLE / not transferred |
| Route B | NOT INVOKED |

## Controls and boundary

- The complete periodic packet uses all periodic phases of the same path action;
  no representative state is selected and no orbit is discarded.
- The shift's inverse exists because paths are bi-infinite. This does not make
  the original noninjective G map a diffeomorphism, nor does it create a
  finite-dimensional phase space.
- The roof one is an action clock. It is not an inserted prime logarithm, but it
  also provides no prime-log arithmetic timing.

## Decision

**Portfolio position: advance as a broadened exact control; fork for classical
geometry.** 079 is the first current object with one internal arithmetic rule,
complete prime-only periodic packet, exact repetitions, and a same-object zeta.
It does not satisfy the classical symplectic/Hénon requirement. Any future
classical lift must retain this complete packet ledger and unit-clock limitation
under a separately frozen owner relation.

## Evidence index

- [078 GPF-Fibonacci A0/A1 control](../078-gpf-fibonacci-a0-a1-control/paper.md)
- Back and Caragiu, [*The Greatest Prime Factor and Recurrent Sequences*](https://fq.math.ca/Papers1/48-4/Back_Caragiu.pdf)
- [032 primorial-gap suspension control](../032-primorial-gap-suspension-flow/paper.md) — broadened packet/zeta comparison only; no object is transferred.
- [035 gap-packet cotangent owner](../035-gap-packet-cotangent-owner/paper.md) — contact-owner comparison only; no owner is imported.
