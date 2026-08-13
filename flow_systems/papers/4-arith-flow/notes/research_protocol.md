# Stage 4 Research Protocol — Frobenius Suspension as a Positive Control

Date frozen: 2026-08-13  
Session: Flow Systems, Stage 4  
Route focus: Route A / A0--A3  
Status: source-audit protocol; no Hilbert--Pólya claim

## 1. Research question

> For a fixed variety over a finite field, does the constant-roof suspension of
> Frobenius give an exact, locally compact continuous-time realization of the
> closed-point Euler product, and which precise obstruction prevents the same
> one-clock mechanism from generating the rational-prime divisor of
> \(\operatorname{Spec}\mathbb Z\) without encoding that divisor in the phase
> space?

This is a positive-control and boundary question.  It is not a proposal that a
finite-field Frobenius suspension is a Hilbert--Pólya system.

### Subquestions

1. **Orbit dictionary.**  With an explicit topology and clock, are primitive
   suspension orbits in bijection with closed points, with least period
   \(\deg(x)\log Q=\log N(x)\), and are all flow points periodic?
2. **Zeta identity.**  Does the unweighted primitive-orbit product equal both
   the Artin--Mazur fixed-point zeta and the Hasse--Weil zeta, with repetition
   coefficients and the absolute-convergence domain derived rather than
   stipulated?
3. **Characteristic-zero boundary.**  Can one fixed \(Q\)-clock support more
   than one rational-prime base, and does replacing it by a disjoint
   \(\log p\)-roof circle for every \(p\) constitute a generative arithmetic
   mechanism or merely compile the target Euler product into a flow?

All subquestions inherit the following scope: continuous-time flows, exact
symbolic arguments, no Riemann-zero data, no rational-prime table in the main
candidate, and evidence available through 2026-08-13.  There are no deviations.

## 2. FINER assessment

| Criterion | Score | Reason |
|---|---:|---|
| Feasible | 5/5 | The fixed control \(\mathbb P^1/\mathbb F_2\) has explicit point counts and a fully explicit mapping torus. |
| Interesting | 5/5 | It gives the cleanest known success case for “closed points become primitive flow orbits” while exposing the one-clock obstruction at characteristic zero. |
| Novel | 4/5 | The component identities are classical; the source-locked Route-A separation between native success, Riemann-target failure, and tautological compilation is the project-specific contribution. |
| Ethical | 5/5 | No human data, privacy risk, or dual-use concern. |
| Relevant | 5/5 | It tests whether the Stage-2 packet obstruction is accidental or reflects the absence of a global Frobenius clock over \(\operatorname{Spec}\mathbb Z\). |
| **Average** | **4.8/5** | Proceed as a theorem-and-obstruction paper if the source audit survives the controls below. |

## 3. Methodology blueprint

### Paradigm and method

- **Paradigm:** exact mathematical/constructive analysis.
- **Method:** source-verified definition audit followed by direct proofs and
  adversarial counter-constructions.
- **Data:** primary mathematical sources and symbolic identities only.
- **Preregistration analogue:** the candidate, topology, clock, zeta convention,
  target split, and failure conditions are frozen below before any manuscript
  conclusion is drafted.

### Frozen positive control

The concrete audit object is

\[
  \texttt{FF-FROB-SUSP-P1-F2}:
  \quad X=\mathbb P^1_{\mathbb F_2},\qquad
  S=X(\overline{\mathbb F}_2)_{\rm disc},\qquad
  F(a)=a^2,
\]

with constant roof \(\tau=\log 2\).  Its mapping torus is

\[
  M_F=(S\times\mathbb R)/\mathbb Z,
  \qquad n\cdot(a,u)=(F^n a,u-n\tau),
\]

and the flow is \(\phi^t[a,u]=[a,u+t]\).

The theorem-family extension to a fixed smooth projective geometrically
connected \(X/\mathbb F_Q\) is allowed only after every assertion has first been
checked for the concrete control.  The family extension is not a parameter
search.

### Frozen orbit-zeta convention

\[
  \zeta_{\rm orb}(s)
  :=\prod_{\gamma\in\mathcal P(M_F)}
       \left(1-e^{-s\ell(\gamma)}\right)^{-1}.
\]

Primitive orbit multiplicity is one.  There is no inserted potential, phase,
stability denominator, central-line shift, or fitted prefactor.  The equivalent
discrete variable is \(z=e^{-s\tau}=2^{-s}\).

### Allowed and forbidden information

**Allowed**

- the equation and scheme structure of \(\mathbb P^1_{\mathbb F_2}\);
- the arithmetic Frobenius action and finite-field extension tower;
- exact closed-point, fixed-point, mapping-torus, and Euler-product theorems;
- unique factorization for the clock-lattice obstruction;
- the already-frozen Route-A rules and Stage-1 constant-roof obstruction.

**Forbidden**

- any table of rational primes in the main candidate definition;
- any Riemann-zero table, zero fitting, or spectral-statistics comparison;
- assigning \(\log p\) roofs component by component and then presenting the
  result as arithmetic emergence;
- inserting von Mangoldt weights, \(p^{-r/2}\), signs, or phases by hand;
- using the Hasse--Weil cohomological determinant as though it had already been
  derived from a Poincare return derivative or a transfer operator of the
  one-dimensional circle flow.

## 4. Claim and evidence obligations

| ID | Obligation | Pass condition | Failure condition |
|---|---|---|---|
| O1 | Frobenius/closed-point dictionary | every closed point gives exactly one primitive cycle of size \(\deg x\), and every geometric point belongs to one such cycle | missing points, infinite cycles, or noncanonical labels |
| O2 | Topological legitimacy | the chosen quotient is Hausdorff, locally compact, second countable, and carries a continuous \(\mathbb R\)-action | topology is left implicit or natural topology is silently replaced |
| O3 | Primitive/repetition ledger | primitive and repeated flow orbits are separated exactly; local finiteness by length is proved | fixed points and primitive cycles are conflated |
| O4 | Zeta identity | Artin--Mazur, orbit Euler product, and Hasse--Weil product agree as formal series and on a stated common convergence domain | equality holds only after changing weights or clocks |
| O5 | Weight provenance | \(1/r\) in \(\log\zeta\) and \(\log N(x)\) in \(-\zeta'/\zeta\) follow by differentiation | arithmetic weights are inserted as a potential |
| O6 | Analytic boundary | absolute convergence and meromorphic continuation are distinguished | rational continuation is confused with Euler-product convergence |
| O7 | One-clock test | prove exactly which rational-prime bases can lie in \((\log Q)\mathbb N\) | rank matching or asymptotic density is substituted for equality |
| O8 | Non-tautology gate | a \(\operatorname{Spec}\mathbb Z\) construction must generate its primitive divisor from one coupled dynamics | the phase space is assembled from the target closed-point/norm list |
| O9 | Native/target split | every Route-A verdict states whether the target is \(Z(X,t)\) or Riemann \(\xi/\zeta\) | finite-field success is used to promote a Riemann candidate |
| O10 | No-zero integrity | no zero locations enter candidate, test, or conclusion | any parameter or normalization is chosen from zeros |

Evidence labels are restricted to the Route-A vocabulary:
`PROVED`, `CONDITIONAL_THEOREM`, `NUMERICALLY_CERTIFIED`,
`NUMERICAL_OBSERVATION`, `HEURISTIC`, `MODELING_CHOICE`,
`FITTED_PARAMETER`, `OPEN`, `REFUTED`, `NOT_TESTABLE`, and `STOP_SCOPED`.

## 5. Falsification controls

1. **Clock-lattice control.**  For a fixed prime power \(Q=\ell^f\), solve
   \(n\log Q=r\log p\) in positive integers.  Unique factorization must force
   \(p=\ell\); for primitive equality \(n\log Q=\log p\), it must further force
   \(f=n=1\).  Thus a single finite-field clock cannot cover all rational primes.
2. **Arbitrary-Euler-product compiler.**  For any prescribed locally finite
   length multiset \(\{L_j\}\), the disjoint union
   \(\coprod_j\mathbb R/L_j\mathbb Z\) has orbit product
   \(\prod_j(1-e^{-sL_j})^{-1}\).  If the same argument would certify this
   compiler, it proves too much.
3. **Tautological \(\operatorname{Spec}\mathbb Z\) control.**  The flow
   \(\coprod_{p}\mathbb R/(\log p)\mathbb Z\) reproduces \(\zeta(s)\), but its
   primitive objects and roofs are the target list.  It must fail A0 regardless
   of exact A1--A2 algebra.
4. **Same-cycle-type permutation.**  Replace Frobenius by a permutation of an
   equicardinal discrete set whose every point is periodic and whose finite
   cycle counts agree degree by degree.  The mapping-torus flow and orbit zeta
   remain isomorphic, while algebraic/cohomological provenance is gone.
   Additional infinite orbits are explicitly excluded because finite-cycle
   counts would not detect them.  Therefore the bare flow topology cannot
   carry all of the finite-field geometry.
5. **Frobenius/inverse-Frobenius control.**  \(F\) and \(F^{-1}\) have the same
   cycles and zeta.  Any claimed sign, orientation phase, or quantum phase not
   invariant under this replacement is not supplied by the frozen orbit product.
6. **Topology control.**  Discrete topology makes the quotient locally compact;
   the Zariski topology on positive-dimensional geometric points is not Hausdorff.
   Any use of local compactness must disclose the discrete-topology modeling
   choice.
7. **Base-field control.**  Replacing \(\mathbb F_Q\) by
   \(\mathbb F_{Q^m}\) changes the return map to \(F^m\), the roof to
   \(m\log Q\), and the primitive-cycle decomposition.  A Riemann claim may not
   hide this dependence.

In the Route-A control vocabulary, control 4 is a randomized-label/same-cycle
control, control 7 is a neighboring-parameter control, and controls 2--3 are
simpler-parent/proves-too-much controls.  Thus at least three independent A0/A1
control classes are present.  No shuffled-prime or composite numerical table is
required: the clock-lattice and arbitrary-compiler controls are exact and
stronger for this source audit.

## 6. Route-A preregistered interpretation

Two evaluation columns are mandatory.

| Layer | Native Hasse--Weil benchmark | Riemann rational-prime target |
|---|---|---|
| A0 | may reach `A0_ANALYTIC_ARITHMETIC_ORIGIN` because \(X\) and Frobenius are fixed before the orbit ledger | must fail if only one \(Q\)-clock is used; a disjoint \(\log p\) assembly also fails as direct target encoding |
| A1 | may reach `A1_PASS_ANALYTIC` if the exact cycle/orbit bijection and topology pass | analytic orbit structure may remain, but it carries the wrong primitive labels |
| A2 | may reach `A2_ANALYTIC_DETERMINANT` for the native Artin--Mazur/Hasse--Weil object | the one-clock candidate has the wrong Euler factors; the disjoint-prime compiler is exact but inadmissible at A0 |
| A3 | may reach a controlled native continuation/determinant statement, with the cohomological source named | no Riemann functional equation, archimedean factor, Weil compression, or nonperiodic divisor may be inferred from the circle flow |

No Route-B invocation is allowed.

## 7. Stop/go rule

Proceed to a paper only if O1--O7 are proved and O8--O10 remain enforced.  A
successful paper may conclude:

- **positive:** finite-field Frobenius suspension is an exact arithmetic-flow
  calibration with one primitive orbit per closed point and the correct native
  zeta;
- **negative:** the same construction cannot be transferred to rational primes
  by one global constant roof, while the disjoint-prime repair is a tautological
  Euler-product compiler.

Stop candidate promotion immediately if the finite-field native target and the
Riemann target are merged, or if the discrete topology/cohomological determinant
is presented as a natural fixed quantum operator.

## 8. Phase-1 devil's-advocate checkpoint

**Verdict: PASS for source investigation; REJECT any advance claim.**

No critical integrity issue is present.  Four major guardrails are binding:

1. the discrete topology is a `MODELING_CHOICE`, not an intrinsic theorem of the
   scheme;
2. exact native Hasse--Weil success is not evidence for rational-prime A0;
3. the mapping torus is topologically a disjoint union of neutral circles and
   therefore risks being only an orbit ledger in geometric dress;
4. the strongest counterexample is the tautological disjoint-prime flow, which
   exactly reproduces \(\zeta\) and thereby demonstrates why exact zeta matching
   without A0 is insufficient.

The strongest hostile-reviewer objection is: “The construction does not discover
closed orbits; it discretizes a set on which Frobenius cycles were already known
and then suspends those cycles.”  The project must accept this objection for the
bare topology while preserving the exact finite-field identity as a calibration
result.
