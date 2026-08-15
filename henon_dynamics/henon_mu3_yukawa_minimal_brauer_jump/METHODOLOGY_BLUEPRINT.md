# HCS-C57 methodology blueprint

Status: **RELEASE_FROZEN; DOCS_FINAL_NO_MORE_EDITS; PAPER_COMPILED;
PAPER_HOSTILE_PASS; theorem and verification methodology locked; machine
PREFREEZE_CODE_RESULTS_PASS.**

## 1. Methodological principle

C57 is a proof-guided exact-computation project. Every released conclusion
must decompose into:

1. a frozen upstream premise;
2. a primary-source theorem with an exact locator;
3. a finite exact instance calculation;
4. a written algebraic or arithmetic bridge;
5. an independent replay and a fail-closed negative test.

No layer may silently stand in for another.

## 2. Evidence layers

### Layer A: frozen upstream mathematics

HCS-C55 fixes the smooth Q-defined cubic surface. HCS-C56 fixes its
degree-27 line field \(E\), common normal line field \(K\), and

\[
\operatorname{Gal}(K/\mathbf Q)=W(E_6).
\]

C57 imports those bytes and their layered status. It does not paste a
coefficient display and trust it.

### Layer B: universal source theorems

The complete 2-primary classification has two branches:

\[
\mathbf Z/2\Rightarrow H\subseteq gU_1g^{-1},
\qquad
(\mathbf Z/2)^2\Rightarrow H\subseteq gU_3g^{-1}.
\]

The indices are 36 and 720. This source theorem controls arbitrary finite
extensions. The exact machine enumeration only checks the selected
\(U_1\)-model and must not be described as a classification of all subgroups.
Its use over a number field is field-independent: the containment and
restriction results concern the finite Galois image inside \(W(E_6)\) and
the integral Picard lattice, while Swinnerton-Dyer supplies the
number-field Picard/Brauer bridge.

### Layer C: exact instance algebra

The machine lane must certify:

- incidence gcd and quotient over the degree-27 line algebra;
- all 72 sixers and 36 double-sixes;
- exact degree-36 resolvers and stabilizers;
- integral Picard cohomology;
- exact degree-12 line carrier;
- canonical quartic restriction matrix and determinant;
- divisor and norm identities.

### Layer D: written bridges

The formal package supplies:

- the fixed-field identity \(K^{H_L}=K\cap L\);
- index divisibility and equality classification;
- inflation--restriction and Hochschild--Serre;
- the explicit number-field bridge separating the EJ group-lattice theorem
  from the cyclic construction repeated over \(F_D\);
- the rank upper bound from Hilbert--90 descent of the rational divisor
  equivalence and then ambient restriction;
- divisor exhaustion from degree;
- cyclic-algebra unramifiedness and nonzero cocycle matching.

### Layer E: hostile verification

The checker must recompute, not trust, every positive semantic field.
Mutation tests must flip every theorem-critical scalar and every negative
scope flag, rebind allowed hashes, and still force rejection.
This negative-scope contract is an unnumbered release firewall, not G7.

## 3. Exact workflow

### M0: source and object lock

1. Import the frozen C56 Route and certificate contract.
2. Replay the C56 default checker.
3. Reconstruct the cubic, line eliminant, and back-substitution data.
4. Reject any mismatch in order, normalization, field role, or status.

### M1: incidence

1. Derive the divided differences symbolically.
2. Compute \(J(x,y)\) over \(\mathbf Q[x]/(g)\).
3. Certify the exact degree-10 gcd, degree-17 quotient, multiplication, and
   absence of the diagonal.
4. Independently enumerate finite-field incidence at more than one good
   prime and bind it to the characteristic-zero line labels.

### M2: configurations and groups

1. Enumerate sixers as six-line independent sets.
2. Pair opposite sixers to obtain double-sixes.
3. Reconstruct \(W(E_6)\) on both line classes and the Picard lattice.
4. Verify \(U_1,U_1^+\), core, self-normalizer, and orbit structures.
5. Compute \(H^1(U_1,\Lambda)\) from integral cochains and Smith normal form.

The complete \(U_1/U_3\) containment remains a source theorem.

### M3: resolvers and field binding

1. Build the \(\theta_D\) and \(\delta_D\) orbit products exactly.
2. Use CRT bounds that prove uniqueness of every lifted coefficient.
3. Store complete modular factors and multiply-back witnesses.
4. Prove irreducibility by incompatible proper subset-sum degrees.
5. Verify stabilizers of \(\theta_D,\delta_D,\beta_D\).
6. Derive field equality through Galois correspondence.

No numerical root matching and no expanded \(\delta=P(\theta)\) calculation
is admitted as a theorem step.

### M4: carrier factor

1. Represent the degree-12 factor \(A_{12}\) over
   \(\mathbf Q(\theta_D)\).
2. Verify \(g=A_{12}B_{15}\) by exact division.
3. Independently multiply forward.
4. Verify that the subtop coefficient recovers the chosen \(\theta_D\).
5. Bind the 12 roots to the selected double-six.

### M5: canonical quartic (G6)

Let

\[
c=[u_0^3]F=75081586157.
\]

The \(4\times4\) gauge block from
\((Fu_0,Fu_1,Fu_2,Fu_3)\) to the coefficients of
\((u_0^4,u_0^3u_1,u_0^3u_2,u_0^3u_3)\) is triangular with

\[
\det=c^4
=31778526453059635681033276764499400992765201\ne0.
\]

This proves that the 31-monomial gauge is a unique quotient representative.
Then:

1. construct the \(60\times31\) restriction matrix in the locked order;
2. delete the normalization column;
3. use the locked 30 rows for the pivot determinant;
4. verify the determinant is nonzero at every conjugate;
5. solve by Cramer's rule and replay all 60 equations;
6. verify that \(\mathcal E+\mathcal G\) and \(4H_0\) are
   \(F_D\)-rational, descend a principal equivalence by the scalar cocycle
   \(\sigma(r)/r\) and Hilbert theorem 90, and lift the resulting
   \(F_D\)-section through
   \(H^0(\mathbf P^3,\mathcal O(4))\twoheadrightarrow
   H^0(Y,\mathcal O_Y(4))\), proving rank at most 30;
7. prove rank at least 30 by the good-specialization pivot certificate.

The determinant definition is the canonical exact output. An expanded table
is neither required nor currently promoted.

### M6: divisor and Brauer class (G7)

1. Verify 12 distinct carrier lines and all quartic restrictions.
2. Use \((4H_Y)\cdot H_Y=12\) to rule out residual and multiplicity.
3. Verify that \(u_0=0\) contains no carrier line.
4. Build the oriented divisor
   \(\mathcal D=\mathcal E-2\operatorname{div}(u_0)\).
5. Verify the norm-divisor identity.
6. in the marked Picard basis compute
   \(e_\Sigma=\sum e_i\), \(H_Y=3h-e_\Sigma\),
   \(d_0=e_\Sigma-2h\), and
   \([\mathcal D]=3d_0\);
7. verify for the central involution that
   \(\iota(d_0)=-d_0\) and
   \((\iota-1)\Lambda^{S_6}=2\mathbf Z d_0\), and match the quaternion
   cocycle value \(3d_0\) to the nonzero class in
   \(H^1(U_1,\Lambda)\).

No local evaluation is performed.

## 4. Independence requirements

| claim | producer | independent checker |
|---|---|---|
| incidence | characteristic-zero quotient/gcd | reconstruct divided differences, gcd, quotient, and modular graph |
| resolver | orbit-product CRT | parse coefficients, redo factor witnesses, stabilizers, and field implications |
| cohomology | exact cochain/SNF | rebuild group, relation lattice, principal lattice, and Smith factors |
| carrier | exact field factor table | independent division and forward multiplication |
| quartic | locked pivot construction | rebuild all entries, determinant, all conjugates, and rank gates |
| divisor | restriction output | recompute line distinctness, degree, and norm identity |
| scope | producer metadata | exhaustive semantic-leaf classification and rebound |

One program invoking the same helper twice is not independence.

## 5. Kill gates

C57 cannot be released if any of the following occurs:

1. the frozen C56 object cannot be replayed exactly;
2. incidence is numerical or incomplete;
3. a resolver lacks exact coefficient bounds or irreducibility;
4. fixed-field equality is inferred without stabilizers;
5. \(H^1\) is reported without an integral relation/principal-lattice replay;
6. the gauge block or pivot determinant is missing;
7. quartic rank uses only the finite-field lower bound;
8. divisor equality is asserted without degree exhaustion;
9. unramifiedness and nontriviality are conflated;
10. any forbidden rational-point, Brauer--Manin, local-Artin, stable-rationality,
    or \(\delta=P(\theta)\) flag can be turned on without checker failure.

## 6. Current milestone

The theorem design, source contract, and methodology are locked. The exact
project-local code/results tuple, independent checker, 33/33 tests, and
535/535 rebound cases pass at `PREFREEZE_CODE_RESULTS_PASS`. The formal source
gate, 18-file paper source, independent hostile paper audit, official 24-page
build, final hostile root audit, external 13-root binding, implementation
identity, self-excluding 64-entry release manifest, and byte-identical archived
Route pass. Their acyclic external hash policies close P57 while preserving the
`PREFREEZE_CODE_RESULTS_PASS` machine layer.

Later batch items remain contingent and unselected; this methodology assigns
them no topic.
