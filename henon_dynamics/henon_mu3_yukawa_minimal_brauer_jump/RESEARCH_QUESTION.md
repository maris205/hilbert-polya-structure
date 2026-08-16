# HCS-C57 research question

Status: **RELEASE_FROZEN; DOCS_FINAL_NO_MORE_EDITS; PAPER_COMPILED;
PAPER_HOSTILE_PASS; THEOREM_TARGET_LOCKED; machine
PREFREEZE_CODE_RESULTS_PASS.**

## 1. Problem

Let \(Y/\mathbf Q\) be the frozen HCS-C55 Yukawa cubic surface, and let
\(K/\mathbf Q\) be the HCS-C56 common normal field of its 27 lines. HCS-C56
proves

\[
\operatorname{Gal}(K/\mathbf Q)\cong W(E_6).
\]

For which finite extensions \(L/\mathbf Q\) does the 2-primary part of

\[
\operatorname{coker}\!\left[
\operatorname{Br}(L)\longrightarrow\operatorname{Br}(Y_L)
\right]
\]

first become nonzero? Can one exhibit an attaining field and a canonical
quaternion algebra representing the new class?

## 2. Locked question

Fix an unordered double-six \(D=\{\mathcal E,\mathcal G\}\), where
\(\mathcal E\) and \(\mathcal G\) denote the effective sums of its two
sixers, and write

\[
U=U_1=\operatorname{Stab}_{W(E_6)}(D)\cong S_6\times C_2,
\qquad F_D=K^U.
\]

Let

\[
U_1^+=\operatorname{Stab}(\mathcal E)\cap
\operatorname{Stab}(\mathcal G)\cong S_6
\]

be the index-two subgroup preserving the two sixers separately. Let \(H_Y\)
denote the hyperplane class and put
\(\mathcal L_0=\operatorname{div}_Y(u_0)\).

The locked question is:

> Prove that nonzero 2-primary algebraic Brauer quotient forces
> \(36\mid[K\cap L:\mathbf Q]\mid[L:\mathbf Q]\), and hence that degree
> \(36\) is the exact minimum among finite \(L/\mathbf Q\) for which \(Y_L\) has
> nonzero 2-primary part; prove that \(F_D\) attains the minimum with quotient
> \(\mathbf Z/2\); bind \(F_D\) to exact degree-36 double-six and orientation
> resolvers; and construct the generator
> \((\delta_D,Q_D/u_0^4)\), where \(Q_D\) is defined canonically by an exact
> determinant rather than by an unreviewable expanded table.

## 3. Adaptive relation to C55 and C56

C57 is not a fifth rendering of the C55 cubic calculation.

- C55 provides the cubic surface as a geometric invariant of the
  four-dimensional equivariant deformation germ.
- C56 proves the complete arithmetic of its line scheme:
  a connected degree-27 field \(E\), its full \(W(E_6)\) normal closure \(K\),
  Picard ranks \(7/1\), and no Q-line.
- C57 asks when the Picard Galois module creates a new 2-primary Brauer class
  after base change, proves the sharp degree threshold, and produces the
  class.

The actual obstruction inherited from C56 is that the full \(W(E_6)\) action
has trivial base-field Brauer quotient. The adaptive response is to descend
to the smallest subgroup allowed by the complete 2-primary classification,
not to choose an arbitrary subfield of \(K\).

## 4. FINER assessment

Scores use 1 (weak) through 5 (strong).

| criterion | score | reason |
|---|---:|---|
| Feasible | 5 | The exact producer and independent checker pass G0--G7 for incidence, field, cohomology, orientation, G6 quartic/rank, and G7 divisor/quaternion/class inputs; the separate scope firewall, official paper gates, final root audit, and release packaging also pass. |
| Interesting | 5 | The result gives a sharp arithmetic minimum and an explicit nonzero Brauer class on a distinguished cubic surface. |
| Novel, bounded | 4 | General double-six resolvers and order-two classes are classical; the bounded search did not locate this fixed surface's complete field-and-quaternion package. |
| Ethical/reproducible | 5 | The proof separates general theorems, exact finite algebra, and negative claims; no private data or numerical fitting is involved. |
| Relevant | 5 | The question uses the full C56 line Galois group and advances from configuration arithmetic to a new cohomological invariant. |

Decision: **LOCK / GO**, conditional only on packaging the already accepted
G0--G7 theorem evidence together with the separate fail-closed
negative-scope contract.

## 5. Exact in-scope claims

1. The sharp implication

   \[
   \left(
   \operatorname{Br}(Y_L)/\operatorname{im}\operatorname{Br}(L)
   \right)[2]\ne0
   \Longrightarrow
   36\mid[K\cap L:\mathbf Q]\mid[L:\mathbf Q].
   \]

2. Equality classification by the 36 conjugate fixed fields
   \(K^{gUg^{-1}}\).
3. Exact field identities
   \(\mathbf Q(\theta_D)=F_D=\mathbf Q(\delta_D)\), proved by stabilizers.
4. The oriented quadratic extension
   \(F_D'=K^{U_1^+}=F_D(\sqrt{\delta_D})\).
5. The exact cohomology
   \(H^1(U,\operatorname{Pic}\overline Y)=\mathbf Z/2\).
6. The number-field Hochschild--Serre bridge to the algebraic Brauer
   quotient.
7. A determinant-defined normalized quartic \(Q_D\) satisfying

   \[
   \operatorname{div}_{Y_{F_D}}(Q_D)=\mathcal E+\mathcal G\sim4H_Y,
   \]

   and

   \[
   \operatorname{div}_{Y_{F_D}}(Q_D/u_0^4)
   =\mathcal E+\mathcal G-4\mathcal L_0
   =\operatorname{Norm}_{F_D'/F_D}
   (\mathcal E-2\mathcal L_0),
   \]

   together with the unramified quaternion
   \((\delta_D,Q_D/u_0^4)\).
8. A bounded, dated instance-novelty statement.

## 6. Exact out-of-scope claims

The following are not part of the research question:

- general novelty of degree-36 double-six resolvents;
- the equation \(\delta=P(\theta)\);
- local evaluation of the quaternion;
- rational points, their absence, Hasse failure, weak approximation, or a
  Brauer--Manin obstruction;
- full local inertia, Artin conductors, bad Euler factors, or root numbers;
- stable-rationality novelty;
- any later-batch theorem target;
- a theorem about all Yukawa or all Hénon cubic surfaces;
- motives, VHS realizations, automorphy, or dynamics.

## 7. Why the degree argument is complete

Let \(H_L\) be the image of \(G_L\) in \(W(E_6)\). The universal quantifier
over finite \(L/\mathbf Q\) is discharged by the complete
Swinnerton-Dyer/Elsenhans--Jahnel 2-primary classification:

\[
\begin{array}{rcl}
\mathbf Z/2\text{ branch}
&\Longrightarrow&H_L\subseteq gU_1g^{-1},
\quad [W(E_6):U_1]=36,\\
(\mathbf Z/2)^2\text{ branch}
&\Longrightarrow&H_L\subseteq gU_3g^{-1},
\quad [W(E_6):U_3]=720.
\end{array}
\]

It follows in both branches that

\[
36\mid[W(E_6):H_L]
=[K\cap L:\mathbf Q]\mid[L:\mathbf Q].
\]

If \([L:\mathbf Q]=36\), then the \(U_3\) branch is impossible and equality
forces \(H_L\) to be a conjugate of \(U_1=U\).

The exact machine enumeration of natural stabilizers is useful for checking
\(U\), its order, its orbits, and its cohomology. It is **not** the proof
that every possible \(H_L\) with nonzero 2-primary cohomology lies in a
double-six stabilizer.

## 8. Success and kill criteria

The exact machine tuple and independent replay pass all of the following
machine-verifiable gates; their labeled written bridges remain separate:

- exact incidence and all-and-only double-six enumeration;
- exact degree-36 resolver identities and irreducibility;
- core-free and self-normalizing fixed-field binding;
- exact orientation square and stabilizer \(S_6\);
- exact \(H^1=\mathbf Z/2\) plus the written arithmetic bridge;
- G6: canonical determinant-defined quartic, rank sandwich, and all 60
  restrictions for every conjugate;
- G7: divisor exhaustion, norm-divisor identity, quaternion, and
  nonzero-class identification;
- the separate unnumbered scope contract, whose fail-closed fields reject
  every forbidden overclaim.

Failure of any numbered gate or of the separate firewall blocks theorem
release. It does not license a smaller “resolver only” paper.

## 9. Current state

The theorem question and proof architecture are locked. The project-local
certificate, strict schema, independent check, scoped manifest, 33/33 tests,
and 535/535 rebound cases pass at `PREFREEZE_CODE_RESULTS_PASS`. The official
18-file paper source, 24-page PDF, compilation report, hostile paper audit,
final root audit, external formal binding, implementation identity,
self-excluding 64-entry manifest, and byte-identical archived Route also pass.
P57 records `RELEASE_FROZEN` and `DOCS_FINAL_NO_MORE_EDITS` while preserving
the protected machine layer.
