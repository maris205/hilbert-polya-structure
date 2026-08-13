# Narrative Report

## Working title

**Tensor-Atom Exterior Transfer for Full Shifts: Möbius Supertrace and a
Critical-Strip Obstruction**

## One-sentence contribution

Tensor-factorization topology gives the Paper-04 full-shift Euler object a
canonical Möbius grading and exact determinant orientation in
\(\Re s>1\), while every source-locked symbolic duality fails to produce the
completed Riemann divisor; even the first adversarial critical-strip
regularization is zero-free and deletes the prime and prime-square traces.

## Why this stage matters

Paper 04 reached A0--A2 on one countable symbolic suspension:

\[
\det(I-L_s)=\zeta(s)^{-1},
\qquad
Z(s)=\zeta(s),
\qquad \Re s>1.
\]

That result left two plausible escape routes. A grading might reverse the
Fredholm orientation, and a stable/unstable or group-completion duality might
generate \(s\leftrightarrow1-s\). Paper 05 tests both routes using only the
same full-shift tensor source.

The outcome is asymmetric. The grading idea works exactly: factorization
homology makes tensor atoms odd, gives the Möbius ledger, and fixes a
Berezinian realization of \(\zeta(s)\). The completion idea does not work:
the honest Koszul resolution cancels to the vacuum, symbolic reversal sends
\(s\) to itself, and tensor inversion sends \(s\) to \(-s\). No construction
selects the missing half-density center \(1/2\).

## Claims and evidence

| Claim | Evidence | Status |
|---|---|---|
| Tensor-factorization topology canonically recovers \(\mu(n)\) | Crosscut theorem for the open divisor interval; 511/511 exact chain complexes through \(N=512\) | PROVED |
| Tensor atoms have intrinsic odd degree after choosing the exterior/Koszul functor | Prime interval is the empty reduced complex in degree \(-1\); random parity controls fail the chain gate | PROVED within frozen functor |
| Exterior transfer fixes determinant orientation | \(\operatorname{Str}\Gamma_-(L_s)=1/\zeta(s)\), \(\operatorname{Ber}_{V_{\bar1}}(I-L_s)=\zeta(s)\) in \(\Re s>1\); 512/512 coefficients exact | PROVED |
| The honest equivariant Koszul resolution does not carry the Euler product | Bosonic and exterior factors cancel, \(\operatorname{Str}T_s=1\), \(\operatorname{sdet}(I-zT_s)=1-z\) | PROVED |
| Natural symbolic dualities do not yield the Riemann involution | reversal gives \(s\mapsto s\); group inversion gives \(s\mapsto-s\) and is parity-even | PROVED |
| Critical-strip regularization does not rescue the divisor | first common order is \(\det_3\) on \(1/3<\Re s<2/3\); it is zero-free and removes \(r=1,2\) traces | PROVED, adversarial obstruction |
| Paper05 advances A3 | No Gamma factor, source-derived half-density, functional equation, continuation, or zero divisor | FAIL |

## Strongest positive theorem

For the order complex \(\Delta_n\) of the open tensor-divisor interval,

\[
\widetilde H_j(\Delta_n;\mathbb Z)\cong
\begin{cases}
\mathbb Z,& n\text{ squarefree},\ j=\omega(n)-2,\\
0,& n\text{ not squarefree}.
\end{cases}
\]

Therefore \(\widetilde\chi(\Delta_n)=\mu(n)\). On the atom space \(V\),

\[
\operatorname{Str}_{\Lambda^\bullet V}\Gamma_-(L_s)
=\frac1{\zeta(s)},
\qquad
\operatorname{Ber}_{V_{\bar1}}(I-L_s)
=\zeta(s),
\qquad \Re s>1.
\]

This is the exact A2 gain.

## Strongest obstruction theorem

The analytic membership criterion is

\[
L_s\in\mathcal S_q\iff q\Re s>1,
\qquad
L_{1-s}\in\mathcal S_q\iff q(1-\Re s)>1.
\]

The first integer order with a common strip is \(q=3\). If one grants the
otherwise non-intrinsic \(1/2\)-centering and defines

\[
D_3(s)=\det\nolimits_3(I-L_s)\det\nolimits_3(I-L_{1-s}),
\]

then \(D_3(s)=D_3(1-s)\) on
\(1/3<\Re s<2/3\), but \(D_3\) is zero-free there and

\[
\log D_3(s)
=-\sum_{r\ge3}\frac1r\sum_p
\left(p^{-rs}+p^{-r(1-s)}\right).
\]

The regularization achieves the visible symmetry only by removing the
prime and prime-square terms.

## Exact experiment

The CPU-only experiment constructs every augmented order complex through
\(N=512\) and verifies:

- 511/511 integer boundary identities \(\partial^2=0\);
- 511/511 Euler coefficients equal \(\mu(n)\);
- 511/511 homology supertraces equal \(\mu(n)\);
- 511/511 squarefree-sphere or nonsquarefree-acyclic Betti patterns;
- 512/512 exterior and Berezinian coefficient prefixes;
- 16/16 orientation gauges preserve all invariants.

The largest fiber is \(n=480\), with 976 simplices. The full audit contains
15,629 simplices including augmented empty simplices.

Controls separate the mechanism from arbitrary signs. Global parity reversal
matches only \(199/512\) coefficients. Random atom characters achieve mean
squarefree sign accuracy \(0.492512\). Liouville parity leaves 198 false
nonsquarefree terms. Shifted and additive monoids lose the entropy ledger,
and free positive mixing fails all 28 semiprime tests.

Finite dual ratios satisfy their algebraic identities to floating precision,
but their maximum adjacent-cutoff phase drift is \(3.10576\) radians. The
finite symmetry therefore receives no continuation credit.

## Literature position

Exterior powers and alternating determinants already occur in symbolic
dynamics, especially in Béal's exterior-power automata for sofic zeta
functions. Signed Putnam homology and Lefschetz zeta formulas are also
established. The contribution here is not the first graded symbolic zeta.
It is the source-locked combination of:

1. tensor atoms of the full-shift monoid;
2. factorization-poset homology indexed by those atoms;
3. the exact distinction between exterior transfer and honest Koszul
   cancellation;
4. a Route-A test of the missing \(s\leftrightarrow1-s\) structure.

## Stage outcome

~~~text
GO_A2_GRADED_ORIENTATION
STOP_A3_COMPLETION
SD-C07 retained
NO SD-C08
ROUTE B LOCKED
~~~

## Bold next hypothesis

The missing \(1/2\)-center should not be inserted as a scalar. If it exists
inside Symbolic Dynamics, it should arise as a canonical half-density
character of a normalized symbolic Jacobian or a stable/unstable transfer
pair. The next stage should construct that character from a source-locked
symbolic system, or prove that every finite-state/local-potential realization
collapses to the same cancellation found here.
