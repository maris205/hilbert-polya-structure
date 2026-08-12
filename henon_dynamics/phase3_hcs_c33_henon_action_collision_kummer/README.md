# HCS-C33 Phase 3: a Hénon action node with a Hill--Kummer class

## Outcome

For the area-preserving Hénon family

\[
H_A(q,p)=(1-Aq^2-p,q),
\]

this project proves an exact characteristic-zero theorem on the period-five
action map.  The degree-nine factor

\[
\begin{aligned}
P_9(A)={}&110592A^9-294912A^8+159744A^7+225792A^6\\
&-162816A^5-51520A^4+50672A^3+736A^2-6032A+1037
\end{aligned}
\]

cuts out a generic equal-action collision of two distinct exact-period-five
points.  Their images in the \((A,c)\)-plane form an ordinary transverse
node, both points are Morse, neither return map has multiplier \(+1\) or
\(-1\), and their intrinsic Hill values descend through branch exchange as

\[
[N_H]=[h_1h_2]\in K_9^\times/K_9^{\times2},
\qquad K_9=\mathbb Q[A]/(P_9).
\]

The class is nontrivial.  Its rational field norm is

\[
N_{K_9/\mathbb Q}(N_H)
=\frac{1929715196403899883576140608}{243}
=\frac{2^6\,13\,19^5\,41\,59^5\,5653^2}{3^5},
\]

which is not a square in \(\mathbb Q\).  Consequently
\(u^2=N_H\) defines a nontrivial quadratic Kummer extension of the generic
collision field.

This is a substantial arithmetic invariant of a genuine Hénon periodic-orbit
family.  It is not yet a dynamical zeta function or a Hilbert--Pólya
operator.

## What is new and what is not

The period-five normalization, discrete Hénon actions, equal-critical-value
strata, Hill's formula, and Kummer covers all have prior art.  The candidate
increment is the coupled exact specialization

\[
\boxed{
\text{Hénon equal-action node}
+\text{ two intrinsic Hill branches}
+\text{ a nontrivial descended square class}.}
\]

The action curve is birational to the known six-sheet period-five marker
cover, so no new normalization or ordinary \(S_6\) cover is claimed.  The
new datum lies in the singular action embedding and its stability
decoration.

## Exact theorem gates

The released producer derives every promoted polynomial from the
chronological recurrence.  The independent checker then reconstructs:

1. the exact conventions, exact-period-five marker, and cyclic action
   reduction;
2. the action image \(W_5(A,c)=0\) and
   \(\operatorname{Disc}_cW_5=2^{12}3^{30}A^{60}P_2^5P_5^3P_9^2\);
3. generic irreducibility and the birational inverse to the known marker
   normalization;
4. the quadratic normalization fiber over \(K_9\);
5. the plane-curve node and the two distinct normalization slopes;
6. the Hill/action-Hessian identity and both multiplier gates;
7. the symmetric Hill norm, its field norm, and its nonsquare class;
8. the exact \(S_9\) proof for \(P_9\) using the frozen cycle types
   \((9)\), \((5,2,1,1)\), and \((8,1)\);
9. all four primes dividing \(P_9(6)=61\cdot157\cdot3203\cdot21943\),
   with \(61\) explicitly retained only as a post-hoc C32 regression.

No floating-point arithmetic enters the promoted theorem.

## Route-A decision

The formal evaluation is

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)
overall: ROUTE_A_REJECTED
```

The two branches are genuine chronological periodic points, but one fixed
period provides no all-length clock, Euler product, Fredholm determinant,
functional equation, or self-adjoint realization.  Route B is not
authorized.

## Reproduction

After the release manifest has been generated, run from the repository root:

```bash
henon_dynamics/phase3_hcs_c33_henon_action_collision_kummer/code/run_c33.sh
```

The default runner is read-only.  It verifies the manifest, reproduces the
certificate and independent report into a temporary directory, compares
them byte for byte, runs the mutation suite, and verifies the manifest
again.  Only the explicit `--refresh-manifest` mode refreshes released
artifacts.

## Project map

- `RESEARCH_QUESTION.md` fixes the theorem and falsification rule.
- `METHODOLOGY_BLUEPRINT.md` records the exact experimental design.
- `THEOREM_PACKAGE.md` states the proved results and scope.
- `DERIVATION_PACKAGE.md` gives the derivation chain.
- `SOURCE_AUDIT.md` records the prior-work boundary.
- `EXACT_GATE_PROTOCOL.md` defines the machine certificate.
- `route_a_evaluation.yaml` records the formal Route-A decision.
- `code/` contains producer, independent checker, mutations, runner, and
  manifest verifier.
- `results/` contains the frozen certificate and human-readable summary.
- `paper/` contains the manuscript and compiled PDF.

## Next large door

The next legitimate question is not another isolated period-five scan.  A
reopening must determine whether the conjugates of \([N_H]\) generate a
larger, provably independent Kummer module under parameter monodromy, or
whether analogous classes can be assembled across periods into one
trace-compatible object.  Either route requires an all-conjugate or
all-period theorem before any zeta claim.
