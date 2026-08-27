# Batch review: HCS-C189--HCS-C193

Date: 2026-08-27

Source commit: `4d7b214759f7ff982c0b19e662918acd307e0f58`.

Evaluator authority: `flow_systems/skills/route-a-evaluator.md` version 0.2.0,
SHA-256 `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.

Common scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

Recommendation: **retain all five independent all-parameter dynamical
theorems and their exact boundaries; keep C189--C193 rejected by Route A,
because C193's genuine Diophantine A0 signal still does not identify rational
primes as primitive carriers and the other four fail A0; leave Route B
unauthorized.**

## Completed paper outputs

### C189 -- Watanabe--Strogatz common-forcing Möbius dynamics

For every `N>=3` and arbitrary continuous common first-harmonic forcing,
C189 lifts the shared phase Riccati equation to

\[
 A(t)=\frac12\begin{pmatrix}if(t)&H(t)\\
 \overline{H(t)}&-if(t)\end{pmatrix}\in\mathfrak{su}(1,1)
\]

and proves that every labelled oscillator is moved by the same projected
`PSU(1,1)` map.  On each distinct-point circular-order component, `N-3` real
cross ratios are independent and separate generic orbits.  Injectivity keeps
every collision partition invariant; strata with one, two, or at least three
distinct clusters have group-orbit dimensions one, two, and three.

For constant forcing, the discriminant
`Delta=omega^2-|H|^2` gives the complete identity/elliptic/parabolic/hyperbolic
classification.  The elliptic projected period is

\[
 T_{\rm ell}=\frac{2\pi}{\sqrt{\Delta}},
\]

with the central `-I` already trivial in `PSU(1,1)`.  Rational strobes fix
whole configuration strata, while the other nonidentity types have no
nonfixed periodic boundary orbit.  Thus the exact reduction yields no finite
isolated arithmetic primitive-orbit owner.

### C190 -- Bulgarian solitaire recurrent necklaces

For every deck size, write uniquely
`N=binom(k,2)+r`, `0<=r<k`.  Brandt's recurrent-coordinate theorem identifies
the recurrent partitions with length-`k`, weight-`r` binary words and one
Bulgarian move with right rotation.  Hence, for `t>=1` and `g=gcd(k,t)`,

\[
 F_t=\#\operatorname{Fix}(T_N^t)=
 \begin{cases}
 \binom{g}{rg/k},&(k/g)\mid r,\\
 0,&\text{otherwise}.
 \end{cases}
\]

Divisor Möbius inversion gives every least-period population and cycle count,
and therefore the complete finite zeta.  C190 additionally closes the full
noninvertible Koopman algebraic spectrum:

\[
 \det(\xi I-U_N)=
 \xi^{p(N)-\binom{k}{r}}
 \prod_{d\mid k}(\xi^d-1)^{C_d}.
\]

The zero algebraic multiplicity counts every transient vertex, while the
nonzero roots of unity come from recurrent cycles.  Reflection reverses the
recurrent rotation, with phase-labelled formulas kept distinct from a false
global reversor.  Complete transient trees, hitting distributions and
nilpotent Jordan sizes remain outside the theorem.

### C191 -- Sinkhorn--Knopp projective scaling

For every square nonnegative matrix without a zero row or column, C191 keeps
three classical boundaries separate: support is equivalent to convergence to
a doubly stochastic limit; total support is equivalent to a representation by
finite positive diagonal factors; and full indecomposability is the exact
one-gauge uniqueness boundary for those factors.  The doubly stochastic
representative itself remains unique on the total-support class.

For `A>0`, the full column-scaling ray map obeys the data-dependent Hilbert
bound

\[
 d_H(T_Ax,T_Ay)\le \kappa(A)^2d_H(x,y),
\]

and no dimension-only contraction factor is inferred.  At the positive doubly
stochastic limit `S`, direct log-coordinate differentiation gives

\[
 DF(0)=S^TS,
 \qquad \rho_{\mathbf1^\perp}=\sigma_2(S)^2<1.
\]

An asymmetric doubly stochastic sentinel proves that replacing `S^T S` by
`S^2` is not an invisible convention error.  The rate is local and
asymptotic.  Since every supported orbit converges, any exactly periodic
scaling orbit is constant and supplies no primitive arithmetic clock.

### C192 -- Brown--Diaconis hyperplane chamber walks

For every finite real hyperplane arrangement and face probability measure,
C192 retains the Brown--Diaconis flat-indexed factorization

\[
 \lambda_W=\sum_{F\subseteq W}w(F),\qquad
 m_W=|\mu(W,V)|,
\]

and consequently the characteristic polynomial, `det(I-zK)`, and every power
trace, including coincident numeric eigenvalues with their flat
multiplicities intact.  Separating measures have a unique stationary law,
the weighted without-replacement product samples it exactly, and the
with-replacement chamber-hitting construction supplies the stated coupling
bounds.

The sharp nonseparating result is not merely “nonunique”: hyperplanes
containing every positive-weight face define closed components, and all
stationary laws form the simplex on their component laws.  Geometric
codimension for braid flats is reconstructed from the intersection-poset
rank, not the number of vanishing hyperplanes.  Stationary stopped output is
not upgraded to a strict strong stationary time without independence from the
stopping time.

### C193 -- positive Markoff--Vieta descent tree

For the complete set of normalized positive integer solutions of

\[
 x^2+y^2+z^2=3xyz,\qquad x\le y\le z,
\]

C193 proves that every nonroot triple has `y<z` and that the other
largest-coordinate root `z'=3xy-z` satisfies `0<z'<=y<z`.  Integer height
therefore decreases under the autonomous parent map and terminates at
`(1,1,1)`.  The two other coordinate mutations satisfy

\[
 3yz-x>z,\qquad 3xz-y>z,
\]

so every Vieta edge in the permutation quotient is either the unique parent
or a strict child.  Reverse edges generate every positive solution and the
full quotient graph is a rooted tree, not merely a finite census prefix.

The tree does not prove that a largest Markoff number determines the other
coordinates; the Frobenius uniqueness conjecture and modular Markoff graphs
remain outside scope.  The integer cubic is an intrinsic Diophantine owner,
but strict descent has no nonroot periodic orbit, rational-prime carrier,
prime-power repetition or `log p` clock.

## Strict Route-A record

| paper | A0 | A1 | A2 | A3 | A4 | overall |
|---|---|---|---|---|---|---|
| C189 | `A0_FAIL` | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C190 | `A0_FAIL` | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C191 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FAIL` | `ROUTE_A_REJECTED` |
| C192 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C193 | `A0_WEAK_ARITHMETIC_RELATION` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |

Every `route_b_invocation_allowed` value is false.  C193's positive A0 signal
is local to its integer surface and is not transferred to any other paper;
no paper borrows another candidate's orbit, spectrum or operator coordinate.

## Uniform release audit

| paper | checker assertions | SymPy checks | hostile rejections | evidence bytes | payload closure | PDF pages |
|---|---:|---:|---:|---:|---:|---:|
| C189 | 2,646 | 18 | 25/25 | 185,717 | 27/27 | 2 |
| C190 | 658,664 | 2,210 | 119/119 | 772,424 | 27/27 | 2 |
| C191 | 2,411 | 951 | 243/243 | 154,517 | 27/27 | 2 |
| C192 | 20,609 | 3,398 | 75/75 | 116,204 | 27/27 | 2 |
| C193 | 8,417 | 8,418 | 157/157 | 402,099 | 27/27 | 2 |
| **total** | **692,747** | **14,995** | **619/619** | **1,630,961** | **135/135** | **10** |

The hostile total consists of 614 repaired-hash semantic attacks and five
stale-hash attacks.  Every checker is producer-independent, and every SymPy
path reconstructs headline identities separately.  Finite coverage is
substantial but remains regression: C189 stores 96 Riccati rows and 128
cross-ratio cells; C190 directly enumerates 215,307 partitions through
`N=40`; C191 exhausts 272 declared order-two/three support patterns; C192
stores 1,604 transition cells across eight arrangements; and C193 retains a
513-row depth-ten tree prefix, its 512 depth-eleven frontier children, all 15
solutions below height 2,000, and 19 complete descent traces.

Every package contains exactly 27 payload files and one self-excluded
manifest, hence exactly 28 physical release files.  All three revision PDFs
are pairwise content-distinct, `main.pdf` is byte-identical to round two, and
two fresh fixed-epoch builds from `main.tex` alone reproduce the final PDF.
All listed fonts are embedded and subsetted; build logs contain no warning,
bad box, undefined reference or missing glyph; extracted text contains the
declared scope and theorem sentinels; all ten rendered pages were inspected.

## Content-addressed release ledger

| paper | evidence SHA-256 | PDF SHA-256 | manifest SHA-256 |
|---|---|---|---|
| C189 | `a1e064bcb10ddbda1b4cfa06eba88ea2b66aea45a2c69d15136ce56c205d1a31` | `e84da7cdccc10df2f468035199612043c72e4e65715b0d4a6830b2234211e68a` | `bf70286c23df1d6b3b04830440ae233bfb267018ad98b8542e0f463158ea8faa` |
| C190 | `78d1ab6aa74d47adb23c8bbcfe1f5ba04125a4aaa152e3d834be4c7f6dde03a4` | `aca83c129125d10ed7a797c51494630c14953f7b63beeea14f8821dc09db2c1d` | `f8bb81f81c102cceb0edd079b12022d2a82d91625ce1595dc832ead800018786` |
| C191 | `6950c217543c2e9c023db08ac406b3f8f116a393294d43ce9ec4da96cfef6f9e` | `b578720d2c9ba9e0be06cf659cf3e15521bfdd9267082333fd3c0144223d8129` | `29bd92e011e3a50420481739a9ca6581b2b857717f764849ba5115ea9f272646` |
| C192 | `7a6e111aeb06f2d47ec9f0830958edca762f1f7d73ef3f6e6c1b26f3e4539b8b` | `32d7b5d7230986cb8f8d00e2cdcffcbe3e083b99be180320132bcf195333ef45` | `f324d76d32fccaf73df718937624ea040c14120550105212257b40863c1886d5` |
| C193 | `39a46bbfd4375c7e01571f18551f69b256f8d09c9b2fc522ba1c4ebd58f53e25` | `7dd5274a024a51df47bbcb67e57e8efbae0b672ee76c3a1ddf73ce96e1f42b06` | `cee4c442b47c7823cf3fec529fdd7cf07b8492c147acbe41b4e1f6d07583c8b4` |

## Internal cross-review and repair ledger

These are artifact-bound theorem, scope and release audits.  They are not
external peer review, independent error processes or novelty certifications.

- **C189:** independent Riccati reconstruction froze the conjugation signs,
  cross-ratio argument order, three-landmark recovery, singular collision
  strata, the identity/parabolic distinction and the `SU(1,1)` versus
  `PSU(1,1)` period factor.  The arbitrary-forcing proof remains analytic and
  the finite exact cells remain sentinels.
- **C190:** direct full-partition enumeration and a separate symbolic path
  confirmed the rotation convention, residue-zero fixed count, transient zero
  eigenvalue and recurrent reflection.  Visual inspection caught and repaired
  a missing backslash before a spacing command before the final PDF was
  frozen.
- **C191:** hostile review added a genuinely asymmetric doubly stochastic
  target, checker transpose sentinels and direct symbolic differentiation so
  the erroneous Jacobian `S^2` cannot pass.  It also separated total support,
  block gauges and the generic local asymptotic rate.  The final Chinese
  abstract was rebuilt after Latin-font fallback warnings were removed.
- **C192:** cross-review rejected vanishing-hyperplane count as geometric
  codimension, replacing it with intersection-poset chain rank.  It also
  separated stationary stopped output from strict SST independence and
  upgraded the nonseparating boundary to the exact component simplex.  Three
  excluded LuaLaTeX sidecars were removed so the physical 28-file contract is
  literal.
- **C193:** review supplied the two strict nonparent-ascent inequalities,
  closing the proof that the full quotient Vieta graph, rather than only the
  chosen descent edges, is a tree.  It renamed the stored word as a local child
  rank, retained the open depth-eleven frontier, and kept Frobenius uniqueness
  outside scope.  Two no-information symbolic assertions were replaced by
  real decomposition certificates; visual audit then caught and repaired a
  literal `qquad` in the first PDF page.

## ARS Stage 2.5 failure-mode audit

1. **Implementation bug passing self-review: CLEAR.**  Five independent
   checkers, five separate symbolic reconstructions, byte replay, semantic
   mutations, boundary sentinels and cross-package reruns agree.
2. **Hallucinated citation: CLEAR.**  Watanabe--Strogatz, Brandt,
   Sinkhorn--Knopp/Brualdi--Parter--Schneider, Brown--Diaconis and the Markoff
   sources retain exact ownership and convention maps.
3. **Hallucinated result: CLEAR AT PROOF LAYER.**  Each arbitrary-family
   headline has a written proof or a precisely delimited source theorem plus
   proved consequences.  No cutoff is promoted to an infinite theorem.
4. **Shortcut reliance: CLEAR.**  Rational rows, `N<=40`, small support
   patterns, eight arrangements and a finite Markoff prefix are regression
   evidence only.
5. **Bug reframed as insight: CLEAR.**  The transpose blind spot, braid-flat
   rank error, incomplete Vieta-edge proof, empty symbolic checks, missing
   glyphs and literal spacing command were repaired and all dependent hashes
   were regenerated.
6. **Methodology fabrication: CLEAR.**  Producer, checker, symbolic, replay,
   mutation, build, font, text, visual and manifest procedures are executable
   and content-addressed.
7. **Frame lock: CLEAR.**  The five phase spaces and clocks remain distinct;
   no exact coordinate from one candidate is used to repair another's failed
   gate.

## ARS Stage 4.5 post-manuscript audit

The seven modes were repeated against the final PDFs, evaluator YAMLs,
evidence bytes, release ledgers and rendered pages.  The clocks remain one
common-forcing flow, one solitaire move, one row--column cycle, one sampled
face product, and one state-dependent Vieta descent.  All final manuscripts
retain source ownership, limitations, declarations, common scope and the
strict Route-A stop.

No target zero or prime census, target divisor, target functional equation or
counting law, arithmetic local datum, Euler factor, root number, automorphy
object, Hilbert--Pólya operator or Route-B input appears as an affirmative
claim.

## Batch conclusion

The round takes five separate large steps: an arbitrary-forcing Lie-projective
reduction with singular strata, an all-deck noninvertible functional-graph
spectrum, an all-support-stratum scaling theorem with exact local dynamics, an
all-arrangement Markov-semigroup theorem, and the complete positive integer
Vieta tree.  It does not split one result into five papers.

The strongest honest roadmap conclusion is still a stop.  C193 advances A0
from absent to a weak intrinsic Diophantine relation, but none of the five
systems produces the required rational-prime primitive carrier, prime-power
repetition and logarithmic arithmetic clock.  All five therefore remain
`ROUTE_A_REJECTED`, with their exact mathematics retained and Route B false.
