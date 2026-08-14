# HCS-C56 research question

Status: **ANSWERED; DOCS_FINAL_NO_MORE_EDITS AND PROJECT RELEASE_CANDIDATE.**

## Primary question

For the exact smooth cubic surface

$$
Y=V(Y_H)\subset\mathbf P^3_{\mathbf Q}
\tag{RQ.1}
$$

released by HCS-C55, what is the arithmetic structure of its complete scheme
of 27 lines?

The question is instance-specific.  It does not ask for the generic Galois
group of cubic surfaces, the monodromy of a family, or another interpretation
of the HCS-C55 variation of Hodge structure.

## Exact subquestions

1. Is the Fano scheme \(F_1(Y)\) connected and finite étale of degree 27?
2. Can it be presented as
   \[
   F_1(Y)\cong\operatorname{Spec}(E),
   \qquad E=\mathbf Q[d]/(g),
   \qquad [E:\mathbf Q]=27,
   \]
   with a directly verified chart reconstruction?
3. Is the splitting field \(K\) of \(g\) the common field of definition of
   all lines, and is
   \[
   \operatorname{Gal}(K/\mathbf Q)\cong W(E_6)?
   \]
4. Does the resulting Galois action force
   \[
   \rho(Y_{\overline{\mathbf Q}})=7,\qquad
   \rho(Y/\mathbf Q)=1?
   \]
5. What does connectedness say about rational lines and degrees of fields
   defining a line?

## Hypothesis

The target hypothesis is:

> The 27-line scheme is one degree-27 field point, and its normal closure has
> the largest incidence-compatible Galois group \(W(E_6)\).

This hypothesis is falsifiable at several independent gates:

- \(Y\) could fail the imported smoothness/source identity;
- the main chart could fail to contain a rank-27 closed subscheme;
- \(g\) could factor over \(\mathbf Q\);
- the separating coordinate could fail;
- the Galois group could be the index-two subgroup \(U\) or another proper
  transitive subgroup;
- the Picard fixed space could have rank greater than one.

## Why this is a separate C56

HCS-C55 ends with a smooth \(\mathbf Q\)-defined cubic surface arising from a
Yukawa tensor.  HCS-C56 introduces:

- the incidence scheme \(F_1(Y)\subset\operatorname{Gr}(2,4)\);
- a degree-27 number field;
- exact modular factorization and a Frobenius class;
- the \(W(E_6)\) action on the 27-line/Schläfli configuration;
- a rank computation in the cubic-surface Picard lattice.

C55 can be correct while every maximality claim in C56 is false.  The new
work is therefore not C55 divided into smaller sections.

## In scope

- exact source import of the frozen C55 primitive cubic;
- scheme-theoretic construction of all lines;
- exact Gröbner/eliminant/back-substitution identities;
- modular irreducibility and Frobenius witnesses;
- exact \(W(E_6)\) and Picard-lattice computation;
- connectedness, field degrees, Picard ranks, and rational-line consequences;
- projective invariance under \(\operatorname{GL}_4(\mathbf Q)\) and common
  rational scaling.

## Out of scope

- rational points on \(Y\), rationality or stable rationality of \(Y\);
- Hasse-principle or Brauer–Manin assertions;
- zeta functions, \(L\)-functions, automorphy, or local point counts;
- motive or polarized-VHS realization;
- a Calabi–Yau threefold;
- a theorem for all Yukawa or Hénon cubic surfaces;
- a generic/family monodromy theorem;
- an exhaustive novelty claim.

## Success criterion

The mathematical question is answered affirmatively when:

1. the direct chart morphism and degree-27 scheme equality are independently
   checked;
2. irreducibility is proved by complete modular data, not a CAS verdict;
3. the \(U\) alternative in Elsenhans–Jahnel Lemma 8 is excluded by Coxeter
   parity, not ordinary \(S_{27}\) sign;
4. the Picard rank is reconstructed independently;
5. every scalar certificate leaf is semantically checked under rebound
   mutation.

Items 1--5 pass at exact prefreeze.  Frozen release additionally requires
the paper compilation and final provenance audits; those workflow gates do
not turn the already certified mathematical premises into assumptions.

## Current answer

**Yes, at the exact prefreeze level.**  The producer and independent checker
certify C56-EXACT-0 through C56-EXACT-4.  The line scheme is one degree-27
finite étale field point, its normal closure has group \(W(E_6)\), and the
fixed-space rank in the geometric Picard lattice is one.  The written Hochschild--Serre
torsion/rank bridge then gives arithmetic Picard rank one.

The code/results state remains the exact `PREFREEZE_CODE_RESULTS_PASS` byte
state with 10/10 semantic gates, 2684/2684 rebound mutations, and 15/15 tests.
The official 19-page paper build and its source/PDF/log/text/report hashes
pass.  The final read-only audit also passes, and the self-excluding formal
root-package aggregate is bound in the Route record.  The project is therefore
a no-commit `RELEASE_CANDIDATE`; implementation/provenance commits remain
intentionally unset.  A separate 46-entry self-excluding full-project
successor is verified externally and is not a theorem premise.
