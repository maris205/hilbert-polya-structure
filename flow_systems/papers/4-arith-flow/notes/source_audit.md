# Source Audit — Finite-Field Frobenius Suspension

Audit date: 2026-08-13  
Candidate: `FF-FROB-SUSP-P1-F2`  
Scope: closed-point dictionary, suspension topology, orbit zeta, weights,
convergence, and the characteristic-zero transfer boundary

## 1. Executive result

The source-locked audit gives one exact positive control and two exact negative
boundaries.

1. **Exact native positive control (`PROVED`).**  Put the discrete topology on
   \(S=\mathbb P^1(\overline{\mathbb F}_2)\), suspend the square Frobenius with
   roof \(\log 2\), and translate vertically.  Frobenius cycles, closed points of
   \(\mathbb P^1_{\mathbb F_2}\), and primitive flow orbits are in bijection.
   The least period attached to \(x\) is \(\deg(x)\log 2=\log N(x)\), and

   \[
     \zeta_{\rm orb}(s)
       =Z(\mathbb P^1_{\mathbb F_2},2^{-s})
       =\frac{1}{(1-2^{-s})(1-2^{1-s})}
   \]

   first as an absolutely convergent Euler product for \(\Re s>1\), then by
   rational continuation.
2. **One-clock obstruction (`PROVED`).**  A period lattice
   \((\log Q)\mathbb N\), with \(Q=\ell^f\), can meet rational-prime-power
   lattices only for the characteristic prime \(\ell\).  It cannot generate the
   periods \(\log p\) for all rational primes.
3. **Disjoint-repair circularity (`PROVED` relative to the Route-A source
   lock).**  The union of one circle of circumference \(\log p\) for every
   rational prime has orbit zeta \(\zeta(s)\), but it reads the complete target
   primitive divisor and roof lengths into the phase space.  It is an exact
   proves-too-much control, not a candidate that passes A0.

No Riemann-zero location, prime table, fitted parameter, or spectral statistic
was used.

## 2. Search and verification record

### Search frame

- **Last searched:** 2026-08-13.
- **Source families:** original papers, official journal archives, an official
  research monograph archive, the Stacks Project, and author-maintained lecture
  notes.
- **Queries:** combinations of “Frobenius closed points orbits finite field,”
  “Artin--Mazur periodic points finite-field zeta,” “suspension flow closed orbit
  roof sum,” and “Hasse--Weil closed-point Euler product.”
- **Inclusion:** a source had to define or prove one of the exact interfaces in
  the audit.  Primary sources were preferred; authoritative expositions were
  admitted only to make a primary theorem or convention unambiguous.
- **Exclusion:** encyclopedia pages, tertiary summaries, sources available only
  through unattributed snippets, and any source whose claimed theorem could not
  be checked in its original/authoritative text.

### Verified source corpus

| Key | Source and verified locator | Role | Quality |
|---|---|---|---|
| `AM65` | M. Artin and B. Mazur, [“On Periodic Points,” *Annals of Mathematics* 81 (1965), 82--99](https://doi.org/10.2307/1970384), especially journal p. 84 | defines the fixed-point zeta and states that the \(q\)-power map on a finite-field variety has the classical zeta | primary, peer-reviewed, Grade A for the claim |
| `DEL74` | P. Deligne, [“La conjecture de Weil I,” *Publ. Math. IHES* 43 (1974), 273--307](https://numdam.org/articles/10.1007/BF02684373/), §§1.1--1.6 and 2.6; DOI `10.1007/BF02684373` | closed-point product, Frobenius orbit dictionary, fixed-point counts, cohomological determinant, rationality, weights, and proper-smooth functional equation | primary, peer-reviewed, Grade A |
| `DEL-EN` | Deligne, [authoritative English translation hosted by J. S. Milne](https://www.jmilne.org/math/Documents/DeligneWeilI.pdf), §§1.1--1.6, 2.6 | checked English wording and section locators against `DEL74` | authoritative translation of a primary source; supporting Grade A |
| `PP90` | W. Parry and M. Pollicott, [*Zeta Functions and the Periodic Orbit Structure of Hyperbolic Dynamics*](https://numdam.org/item/AST_1990__187-188__1_0/), Astérisque 187--188 (1990), Chapter 6, printed pp. 89 and 99--100 | standard suspension quotient, vertical flow, base-cycle/flow-orbit correspondence, roof-sum period, and orbit Euler product | authoritative research monograph, Grade A for conventions |
| `STACKS-01TF` | [Stacks Project, Tag 01TF](https://stacks.math.columbia.edu/tag/01TF) | a point closed in a finite-type fibre has finite residue extension | authoritative living reference, Grade A for the lemma |
| `STACKS-03SL` | [Stacks Project, Tag 03SL](https://stacks.math.columbia.edu/tag/03SL), Definition 64.3.8 | arithmetic Frobenius is \(a\mapsto a^q\); clarifies arithmetic/geometric Frobenius convention | authoritative living reference, Grade A for definitions |
| `MILNE13` | J. S. Milne, [*Lectures on Etale Cohomology*, v2.21](https://www.jmilne.org/math/CourseNotes/LEC.pdf) (2013), §§26--29, especially pp. 150--151 and 165 | independent authoritative check of point-count, closed-point product, convergence statement, and compact-support determinant | author-maintained advanced notes, Grade B/A-supporting |

No bibliographic existence issue was found.  The exact DOI metadata for `AM65`
and `DEL74`, and the official Numdam metadata for `PP90`, agree with the source
documents.  There is no relevant funding or commercial conflict.  The old dates
are not a currency weakness: these are foundational theorem claims, not a
state-of-the-field survey.

### Source limitations

`PP90` treats suspensions over compact symbolic systems with regular positive
roofs.  The frozen Frobenius base \(S\) is instead a countable discrete space.
This audit therefore uses `PP90` only for the standard definition and roof-sum
identity; local compactness, component structure, and convergence for the frozen
object are proved directly below.  Conversely, the cohomological determinant in
`DEL74` is a determinant of Frobenius on etale cohomology, not a theorem that the
one-dimensional suspension flow has a trace-class transfer operator.

## 3. Source-derived arithmetic dictionary

Let \(X_0/\mathbb F_Q\) be a variety and let
\(S=X_0(\overline{\mathbb F}_Q)\).  Fix arithmetic Frobenius

\[
  F:S\longrightarrow S,\qquad a\longmapsto a^Q.
\]

`STACKS-03SL` fixes this arithmetic-Frobenius convention.  Replacing \(F\) by
geometric Frobenius \(F^{-1}\) reverses each finite cycle but changes neither
cycle length nor the zeta identities below.

Deligne §1.4 gives the complete dictionary:

| Statement | Status | Source |
|---|---|---|
| \(\operatorname{Fix}(F^n)=X_0(\mathbb F_{Q^n})\) | `PROVED` | `DEL74`, §1.4(b) |
| closed points \(|X_0|\) are Frobenius orbits on \(S\) | `PROVED` | `DEL74`, §1.4(c) |
| the orbit attached to \(x\) has cardinality \(\deg(x)=[\kappa(x):\mathbb F_Q]\) | `PROVED` | `DEL74`, §1.4(c) |
| \(\#X_0(\mathbb F_{Q^n})=\sum_{\deg(x)\mid n}\deg(x)\) | `PROVED` | `DEL74`, equation (1.4.1) |
| Frobenius fixed points enter with multiplicity one | `PROVED` | `DEL74`, discussion after (1.5), using \(dF=0\) |

Every element of \(S\) is defined over some finite extension of \(\mathbb F_Q\):
for a finite-type affine chart its finitely many coordinates are algebraic over a
finite field, hence lie in one \(\mathbb F_{Q^n}\).  Thus every point of \(S\)
is periodic.  The set is countable because

\[
  S=\bigcup_{n\geq1} X_0(\mathbb F_{Q^n})
\]

and every set in this union is finite.  These statements are also consistent
with `STACKS-01TF`, which makes the finite residue-field extension at a closed
point explicit.

## 4. Frozen topology and suspension theorem

### 4.1 Why the topology must be stated

The phase-space topology is not supplied by the closed-point dictionary.  This
audit freezes **the discrete topology** on \(S\).  That choice is
`MODELING_CHOICE`, even though the set and its Frobenius action are arithmetic.
The usual Zariski topology on the geometric points of a positive-dimensional
variety is not Hausdorff, so it cannot be silently substituted while retaining
the local-compact-Hausdorff claims below.

Let \(\tau=\log Q\), give \(S\times\mathbb R\) the product topology, and let
\(\mathbb Z\) act by

\[
  n\cdot(a,u)=(F^n a,u-n\tau).
\]

The quotient

\[
  M_{X,Q}:=(S\times\mathbb R)/\mathbb Z
\]

has the vertical flow \(\phi^t[a,u]=[a,u+t]\).  This is the standard suspension
definition in `PP90`, Chapter 6, with a constant roof.

### 4.2 Direct topology proof

**Proposition 4.1 (`PROVED`).**  The \(\mathbb Z\)-action is free and properly
discontinuous.  The quotient is Hausdorff, locally compact, and second
countable.  For the frozen \(X_0=\mathbb P^1_{\mathbb F_2}\), the quotient is
noncompact.

**Proof.**  Freeness follows from the real coordinate: if
\((F^n a,u-n\tau)=(a,u)\), then \(n\tau=0\), so \(n=0\).  If \(K\) is a compact
subset of \(S\times\mathbb R\), its real projection is bounded.  Only finitely
many translates by \(n\tau\) can intersect that bounded interval, which proves
proper discontinuity.  A free properly discontinuous action on the locally
compact Hausdorff space \(S\times\mathbb R\) has a locally compact Hausdorff
quotient.  Since \(S\) is countable discrete, a countable union of bases for
copies of \(\mathbb R\) gives second countability.  In the frozen case,
\(\mathbb P^1(\overline{\mathbb F}_2)\) is infinite while each Frobenius cycle
is finite, so there are infinitely many open-and-closed circle components;
their component cover has no finite subcover.  Hence the quotient is not
compact. \(\square\)

### 4.3 Component and primitive-period theorem

**Proposition 4.2 (`PROVED`).**  There is a flow-preserving homeomorphism

\[
  M_{X,Q}\cong
  \coprod_{x\in|X_0|}
  \mathbb R/(\deg(x)\log Q)\mathbb Z.
\]

Consequently:

- each closed point \(x\) gives exactly one primitive flow orbit;
- its least period is
  \(\ell_x=\deg(x)\log Q=\log\#\kappa(x)=\log N(x)\);
- every point of the flow lies on a periodic orbit;
- the family of primitive orbits is locally finite by length;
- orientation is the positive vertical direction and primitive multiplicity is
  one.

**Proof.**  Let \(a,F a,\ldots,F^{d-1}a\) be a Frobenius cycle of least length
\(d\).  Its invariant suspension is

\[
  (\{a,Fa,\ldots,F^{d-1}a\}\times\mathbb R)/\mathbb Z.
\]

Sending \([F^j a,u]\) to \(u+j\tau\pmod{d\tau}\) identifies it with a circle
of circumference \(d\tau\) and intertwines vertical translation.  Distinct
Frobenius cycles are disjoint open-and-closed subsets because \(S\) is discrete.
The dictionary in §3 labels them by closed points and gives \(d=\deg(x)\).
For a length cutoff \(T\), only degrees
\(d\leq T/\log Q\) occur; points of each such exact degree form a subset of the
finite set \(X_0(\mathbb F_{Q^d})\), so only finitely many primitive orbits lie
below the cutoff. \(\square\)

This is the constant-roof specialization of the base-cycle/closed-flow-orbit
correspondence and roof-sum formula in `PP90`, Chapter 6, pp. 99--100.

### 4.4 Dynamical degeneracy

The quotient is a one-dimensional smooth manifold with countably many circle
components, but it has no nontrivial transverse direction.  Its Poincare return
map on a zero-dimensional transverse section has an empty derivative (empty
determinant one); there is no hyperbolic stable/unstable multiplier, mixing, or
orbit interaction.  These are direct properties of the component description,
not defects in the closed-point bijection.

In particular, the cohomological Frobenius action of `DEL74` is extra algebraic
structure inherited from \(X_0\).  It is not the monodromy derivative of this
circle flow.  Treating the two as already identified would be `NOT_TESTABLE`.

## 5. Exact Artin--Mazur, orbit, and Hasse--Weil identities

Let

\[
  N_n:=\#\operatorname{Fix}(F^n)
      =\#X_0(\mathbb F_{Q^n}).
\]

Artin and Mazur define the fixed-point zeta (their p. 84) by

\[
  \zeta_{AM}(z)=
  \exp\!\left(\sum_{n\geq1}\frac{N_n}{n}z^n\right),
\]

and explicitly state that for the \(Q\)-power map on the algebraic-closure
points of a variety over \(\mathbb F_Q\), this is the classical zeta of the
variety (`AM65`).

Let \(a_d\) be the number of Frobenius cycles of exact length \(d\), equivalently
the number of closed points of degree \(d\).  The exact ledger is

\[
  N_n=\sum_{d\mid n} d\,a_d.
\]

Therefore, as formal power series,

\[
\begin{aligned}
  \log\zeta_{AM}(z)
    &=\sum_{n\geq1}\frac{z^n}{n}
      \sum_{d\mid n}d\,a_d \\
    &=\sum_{d\geq1}a_d\sum_{r\geq1}\frac{z^{rd}}{r}
      =-\sum_{d\geq1}a_d\log(1-z^d),
\end{aligned}
\]

so

\[
  \zeta_{AM}(z)
   =\prod_{d\geq1}(1-z^d)^{-a_d}
   =\prod_{x\in|X_0|}(1-z^{\deg x})^{-1}.
\]

The last expression is exactly Deligne's closed-point definition in §1.1.
Putting \(z=Q^{-s}=e^{-s\log Q}\) and using Proposition 4.2 gives

\[
  \boxed{
  \zeta_{\rm orb}(s)
    =\prod_{\gamma\in\mathcal P(M_{X,Q})}
       (1-e^{-s\ell_\gamma})^{-1}
    =Z(X_0,Q^{-s}).}
\]

This is an equality of the unweighted orbit Euler product with the native
Hasse--Weil zeta.  No stability denominator or packet measure is needed because
there is exactly one circle orbit for each Frobenius cycle.

### Repetition and logarithmic-derivative weights

The primitive factor has the exact expansion

\[
  \log\zeta_{\rm orb}(s)
    =\sum_{x\in|X_0|}\sum_{r\geq1}
       \frac{e^{-sr\ell_x}}{r}.
\]

Thus the \(1/r\) repetition coefficient is combinatorial, not fitted.  On its
absolute-convergence half-plane,

\[
  -\frac{d}{ds}\log\zeta_{\rm orb}(s)
    =\sum_{x\in|X_0|}\sum_{r\geq1}
       \ell_x e^{-sr\ell_x}
    =\sum_{x,r}\log N(x)\,N(x)^{-rs}.
\]

The finite-field analogue of the logarithmic prime weight therefore comes from
the period derivative.  This does **not** supply the signed/oscillatory
\(N(x)^{-r/2}\) explicit-formula amplitude required by the Riemann project; a
shift by \(1/2\) would be a separate normalization that is absent from the
frozen flow.

## 6. Concrete calculation and convergence domain

For the frozen \(X_0=\mathbb P^1_{\mathbb F_2}\),

\[
  N_n=\#\mathbb P^1(\mathbb F_{2^n})=2^n+1.
\]

Hence

\[
\begin{aligned}
  Z(\mathbb P^1,z)
   &=\exp\left(\sum_{n\geq1}\frac{(2^n+1)z^n}{n}\right)\\
   &=\frac{1}{(1-2z)(1-z)},
\end{aligned}
\]

and

\[
  \zeta_{\rm orb}(s)
    =\frac{1}{(1-2^{1-s})(1-2^{-s})}.
\]

For \(\sigma=\Re s\), absolute convergence of the logarithm is equivalent to

\[
  \sum_{n\geq1}\frac{(2^n+1)2^{-\sigma n}}{n}<\infty,
\]

which holds exactly when \(\sigma>1\).  At \(\sigma=1\), the first term contains
the harmonic series; for \(\sigma<1\), its summands do not even decay
exponentially.  Therefore:

- **Euler product / defining series:** absolutely convergent exactly for
  \(\Re s>1\);
- **continued function:** meromorphic on all \(s\in\mathbb C\) through the
  displayed rational expression in \(2^{-s}\).

The two domains must not be conflated.  More generally, Deligne's
cohomological formula

\[
  Z(X_0,z)=\prod_i
   \det(1-zF^*\mid H_c^i(X_{\overline{\mathbb F}_Q},\mathbb Q_\ell))^{(-1)^{i+1}}
\]

gives rational continuation; for proper smooth \(X_0\), Poincare duality gives
the native functional equation (`DEL74`, §§1.5 and 2.6).  It remains a
cohomological determinant, not a transfer-operator theorem for the circle
suspension.

### Imaginary periodicity

Because every finite-field zeta in the \(s\)-variable is a rational function of
\(Q^{-s}\),

\[
  \zeta_{X_0}(s+2\pi i/\log Q)=\zeta_{X_0}(s).
\]

For \(\mathbb P^1_{\mathbb F_2}\), the continued poles repeat on the vertical
lattices

\[
  s=1+\frac{2\pi i k}{\log2},\qquad
  s=\frac{2\pi i k}{\log2},\qquad k\in\mathbb Z.
\]

This is the analytic fingerprint of the single logarithmic clock.  It is
incompatible with using this determinant as the Riemann zeta/xi determinant;
the conclusion uses only the explicit formula above, not any Riemann-zero data.

## 7. Why one finite-field clock cannot cover \(\operatorname{Spec}\mathbb Z\)

Let the base-field cardinality be \(Q=\ell^f\), where \(\ell\) is a rational
prime and \(f\geq1\).  Every suspension period lies in
\((\log Q)\mathbb N\).

**Theorem 7.1 (one-clock obstruction, `PROVED`).**  If positive integers
\(n,r\) and a rational prime \(p\) satisfy

\[
  n\log Q=r\log p,
\]

then \(p=\ell\).  If the target is the primitive equality
\(n\log Q=\log p\), then necessarily \(f=n=1\) and \(Q=p=\ell\).

**Proof.**  Exponentiation gives
\(\ell^{fn}=p^r\).  Unique factorization forces \(p=\ell\), after which
\(fn=r\).  For \(r=1\), positive integrality forces \(f=n=1\). \(\square\)

Thus a single global \(Q\)-clock can at most see prime powers of the
characteristic prime.  It cannot geometrically realize the rational-prime
period set \(\{\log p:p\text{ prime}\}\).  This strengthens the Stage-1
constant-roof obstruction in the precise finite-field setting.

The same fact appears analytically: all finite-field orbit lengths are lattice
lengths and the continued zeta is imaginary-periodic.  Passing from one finite
field to all rational primes requires more than a larger finite-field variety;
it requires a non-lattice global clock or an object coupling different residue
characteristics.

## 8. The disjoint-prime suspension is an exact but tautological control

Consider the formal locally compact flow

\[
  M_{\mathbb Z}^{\rm taut}
    :=\coprod_{p\ {\rm prime}}\mathbb R/(\log p)\mathbb Z,
  \qquad \phi^t[u]=[u+t].
\]

It is a countable disjoint union of circles, so the same direct topology proof
applies.  Its primitive-orbit product is, for \(\Re s>1\),

\[
  \zeta_{M_{\mathbb Z}^{\rm taut}}(s)
     =\prod_p(1-e^{-s\log p})^{-1}
     =\prod_p(1-p^{-s})^{-1}
     =\zeta(s).
\]

Writing the construction invariantly as

\[
  \coprod_{x\in|\operatorname{Spec}\mathbb Z|}
  \mathbb R/(\log N(x))\mathbb Z
\]

does not change its information flow: every target primitive closed point and
its target norm is queried before the corresponding flow component exists.
There is no single return map whose periodic points generate the divisor.  The
construction therefore violates both explicit A0 failure clauses in
`skills/route-a-evaluator.md`: the target prime set is used directly and the
roof \(\log p\) is assigned componentwise.

This is not merely an aesthetic objection.  Given any countable locally finite
length multiset \(\{L_j\}\),

\[
  \coprod_j\mathbb R/L_j\mathbb Z
\]

has orbit zeta \(\prod_j(1-e^{-sL_j})^{-1}\).  The construction is a universal
Euler-product compiler.  Exact matching therefore certifies no arithmetic
origin unless the lengths arise from a separately frozen coupled dynamics.

The `SPECZ-TAUT-NORM-CIRCLES` control may legitimately receive an exact
primitive-orbit ledger and exact orbit product.  It must nevertheless receive
`A0_FAIL`, overall `ROUTE_A_REJECTED`, and `PROVES_TOO_MUCH`; its exact later
layers cannot repair the failed entry gate.

## 9. What survives and what does not

### Source-certified positive structure

| Item | Result | Evidence |
|---|---|---|
| arithmetic source | fixed \(\mathbb P^1/\mathbb F_2\) and Frobenius, no target table | `PROVED` |
| primitive objects | one Frobenius cycle / closed point / flow circle | `PROVED` |
| primitive period | \(\deg(x)\log2=\log N(x)\) | `PROVED` |
| repetitions | \(r\)-fold traversal, coefficient \(1/r\) in \(\log\zeta\) | `PROVED` |
| multiplicity | one per closed point; fixed geometric points counted with multiplicity one | `PROVED` |
| topology | LCH, Hausdorff, second countable, noncompact | `PROVED` after discrete-topology `MODELING_CHOICE` |
| orbit zeta | exactly Hasse--Weil / Artin--Mazur | `PROVED` |
| convergence | exactly \(\Re s>1\) for the frozen Euler product | `PROVED` |
| continuation | rational in \(2^{-s}\), hence meromorphic | `PROVED` |

### Missing or target-incompatible structure

| Item | Boundary | Evidence |
|---|---|---|
| all rational-prime periods | impossible for one \(Q\)-clock | `REFUTED` by Theorem 7.1 |
| intrinsic LCH topology | discreteness is imposed and erases algebraic adjacency | `MODELING_CHOICE` |
| nontrivial stability/monodromy | no transverse direction; all components are neutral circles | `PROVED` absent |
| signed/complex phase | Frobenius and inverse Frobenius give the same orbit product | `NOT_TESTABLE` from this zeta |
| flow transfer-operator determinant | no operator/trace class is defined for the frozen LCH flow | `NOT_TESTABLE` |
| identification with etale determinant | both produce the native zeta, but no dynamical trace bridge equating their operators is supplied | `OPEN` / `NOT_TESTABLE` |
| Riemann gamma factor and pole removal | absent | `A3_FAIL` for the Riemann target |
| Riemann Weil compression | no natural Hermitian compression arises from the circle flow | `NOT_TESTABLE`; artificial insertion forbidden |
| fixed quantum lift | no symplectic/contact/scattering structure or candidate operator | outside A0--A3; Route B forbidden |

## 10. Provisional Route-A verdicts

The same construction has different answers for different targets.  Reporting
only one tuple would be misleading.

### 10.1 Native finite-field calibration

Candidate: `FF-FROB-SUSP-P1-F2`  
Target: \(Z(\mathbb P^1_{\mathbb F_2},2^{-s})\)

| Layer | Provisional verdict | Reason |
|---|---|---|
| A0 | `A0_ANALYTIC_ARITHMETIC_ORIGIN` | \(X\), \(F\), and \(\log\#\mathbb F_2\) are intrinsic and frozen independently of a zeta divisor. |
| A1 | `A1_PASS_ANALYTIC` | primitive cycles, periods, repetitions, orientation, multiplicity, completeness, and local finiteness are exact; transverse monodromy is trivially zero-dimensional. |
| A2 | `A2_ANALYTIC_DETERMINANT` | the orbit/Artin--Mazur product equals the native Hasse--Weil zeta exactly, and a separate cohomological determinant is exact. |
| A3 | `A3_CONTROLLED_CONTINUATION` | rational continuation and the proper-smooth native functional equation are cohomologically controlled; no Riemann Weil-compression claim is made. |
| Overall | calibration only | exact positive structural prior, not a Riemann candidate |

The A2 label does **not** assert a trace-class transfer operator for the circle
flow.  It refers to the exact analytic dynamical-zeta object permitted by the
Route-A convention, with the cohomological determinant separately named.

### 10.2 Riemann rational-prime target

Candidate: the same `FF-FROB-SUSP-P1-F2`  
Target: Riemann \(\zeta/\xi\)

| Layer | Provisional verdict | Reason |
|---|---|---|
| A0 | `A0_FAIL` | primitive labels are closed points over one finite field; the one-clock theorem excludes all rational-prime bases except 2. |
| A1 | `A1_PASS_ANALYTIC` as a flow, but wrong arithmetic support | exact orbit structure cannot bypass A0. |
| A2 | `A2_FAIL` for the Riemann target | the exact determinant is the wrong Euler product and has a \(2\pi i/\log2\)-periodic divisor. |
| A3 | `A3_FAIL` | incompatible global analytic structure; no archimedean factor or natural Weil compression from the flow. |
| Overall | `ROUTE_A_REJECTED` | native finite-field success retained as a positive control |

### 10.3 Tautological characteristic-zero compiler

Candidate: `SPECZ-TAUT-NORM-CIRCLES`

| Layer | Provisional verdict | Reason |
|---|---|---|
| A0 | `A0_FAIL` | prime components and \(\log p\) roofs are the target data. |
| A1 | `A1_PASS_ANALYTIC` | one primitive circle per encoded prime, exact repetitions. |
| A2 | `A2_ANALYTIC_DETERMINANT` only as a tautological orbit product | exact \(\zeta(s)\) equality demonstrates the proves-too-much problem. |
| A3 | `A3_FAIL` for dynamical provenance | continuation and functional equation are inherited from external number theory, not derived from the circle flow. |
| Overall | `ROUTE_A_REJECTED / PROVES_TOO_MUCH` | negative control only |

Route B is not authorized for any object in this audit.

## 11. Falsification-control outcomes

| Control | Outcome | Consequence |
|---|---|---|
| one-clock lattice | rational-prime bases other than the characteristic prime are impossible | exact Riemann A0 failure |
| arbitrary length compiler | any Euler product can be realized by disjoint circles | exact zeta equality alone proves too much |
| disjoint \(\operatorname{Spec}\mathbb Z\) circles | gives \(\zeta(s)\) exactly while directly encoding primes | validates the A0 gate |
| same-cycle-type permutation | bare mapping-torus flow retains zeta but loses algebraic provenance | cohomology is not recoverable from flow topology alone |
| \(F\) versus \(F^{-1}\) | same lengths and zeta | no phase/orientation sign is identified |
| topology replacement | discrete topology passes LCH; Zariski topology does not provide the same Hausdorff flow | topology choice must stay explicit |
| base-field extension | return map, roof, cycles, and imaginary period change | no field-independent global clock emerges |

## 12. Audit conclusion and next smallest theorem

The candidate is worth a paper **as a positive-control/boundary theorem**, not as
a Hilbert--Pólya proposal.  Its strongest positive result is unusually clean:
finite-field closed points are exactly primitive orbits of a continuous flow and
their native Hasse--Weil zeta is exactly its unweighted orbit zeta.  Its strongest
obstruction is equally clean: one global finite-field clock is a lattice clock
and cannot couple distinct residue characteristics, while the obvious disjoint
repair is a universal target compiler.

The next smallest constructive question is therefore not another constant-roof
suspension.  It is:

> Can a single, non-disjoint arithmetic phase space carry a natural return
> dynamics whose primitive cycles generate closed points across different
> residue characteristics, with the norm clock obtained from that dynamics
> rather than read from the closed-point list?

Until such a mechanism is frozen, the finite-field model remains a certified
positive structural prior and the disjoint \(\operatorname{Spec}\mathbb Z\)
model remains a proved obstruction/control.
