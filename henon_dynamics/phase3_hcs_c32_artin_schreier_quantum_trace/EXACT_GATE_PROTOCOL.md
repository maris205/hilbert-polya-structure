# HCS-C32 Phase-3 exact gate protocol

Date frozen: 2026-08-12 UTC

Candidate: `HCS-C32-MORSE-LOCAL-HILL-GATE`

Evidence status: the prime-period witness described below was found during an
exploratory pilot before this file was written.  It is therefore a discovery
witness, not a preregistered prediction.  All release claims must survive a
fresh deterministic producer, an independently written checker, and mutation
tests after this freeze.

## 1. Exact question

For a prime \(p>3\), let \(z\) be an isolated nondegenerate critical point of

\[
\Phi_n(x_0,\ldots,x_{n-1})
=\sum_{i\bmod n}
\left(x_ix_{i+1}-x_i+2x_i^3\right)
\]

over a finite extension of \(\mathbb F_p\).  Does its local
Artin--Schreier/Fourier--Deligne vanishing-cycle factor distinguish the full
Hill value

\[
h(z)=\det(I-DH_6^n(z))
\]

from another critical point with the same critical value and the same Hessian
square class?

The cyclic Hill convention is frozen as

\[
\det D^2\Phi_n(z)=(-1)^{n+1}h(z).
\]

## 2. Chronology and multiplicity conventions

The recurrence is

\[
x_{i+1}=1-6x_i^2-x_{i-1}.
\]

Starting from \((x_0,x_{-1})\), the derivative factors are multiplied in
application order,

\[
DH_6^n=A(x_{n-1})\cdots A(x_0),
\qquad
A(x)=
\begin{pmatrix}
-12x&-1\\
1&0
\end{pmatrix}.
\]

The Hessian is reconstructed from the action terms, rather than from a generic
cyclic-tridiagonal shortcut.  Each term \(x_ix_{i+1}\) contributes one mixed
derivative in both symmetric positions.  This automatically preserves the
double edge at \(n=2\) and the diagonal contribution at \(n=1\).

An orbit is primitive of clock length \(n\) only when the state
\((x_i,x_{i-1})\) has least positive return time \(n\).  Rotations are marked
states in the raw census and are separately quotientable into cyclic classes.

## 3. Local-data equivalence relation

For \(z\in\operatorname{Crit}(\Phi_n)(\mathbb F_p)\), record

\[
\mathcal I(z)=
\left(
n,
\Phi_n(z),
\chi_p(\det D^2\Phi_n(z))
\right),
\]

where \(\chi_p\) is the quadratic character and the determinant is required to
be nonzero.

The computational witness is decisive only if two distinct primitive cyclic
orbits have equal \(\mathcal I\), unequal Hessian/Hill determinants in
\(\mathbb F_p\), and an exact congruence witness

\[
C^{\mathsf T}D^2\Phi_n(z_1)C=D^2\Phi_n(z_2),
\qquad C\in\operatorname{GL}_n(\mathbb F_p).
\]

The congruence witness proves equality of the quadratic germs without relying
only on a Legendre-symbol implementation.

## 4. PASS and STOP rules

### PASS

The gate passes only if a source-certified theorem or exact counterexample
shows that the local vanishing-cycle Frobenius representation distinguishes
two points satisfying the local-data equivalence relation above.  Merely
recovering the critical value, dimension, Hessian square class, quadratic
Gauss sum, or Weil index does not pass.

### STOP

The gate stops if both conditions hold:

1. the good-prime Morse-local representation is determined by the critical
   value, dimension, additive character, and Hessian square class; and
2. an exact Hénon witness has the same such data but a different Hill value.

This is a scoped STOP for the **Morse-local Hill-information gate**.  It is not
a no-go theorem for the full global exponential-sum cohomology, the entire
critical-value configuration, degenerate critical points, bad primes, or a
one-parameter discriminant family.

## 5. Registered deterministic scan

The release producer must replay all primitive \(\mathbb F_p\)-rational
periodic states for

\[
p\in\{5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61\},
\qquad 1\le n\le5.
\]

It must report every group containing unequal nonzero determinants at fixed
\((p,n,\Phi_n,\chi_p(\det D^2\Phi_n))\).  The first witness under lexicographic
\((n,p)\) ordering is expected to occur at \((n,p)=(5,61)\), but this
expectation is post-pilot and is not counted as independent evidence.

For the selected pair the producer must derive, not merely hardcode:

- the two primitive cyclic classes and all rotations;
- critical-equation residuals;
- common action value;
- Hessian matrices and determinants;
- chronological monodromy matrices and Hill determinants;
- quadratic characters and an explicit square ratio;
- a deterministic congruence matrix between Hessians;
- the formal-local conclusion only under the source-certified Morse lemma.

## 6. Independent-checker contract

The checker must independently reconstruct all dynamics, action, Hessian, and
monodromy data from the orbit words.  It must verify the congruence matrix
directly, recompute the scan census, use strict JSON types, reject unknown
schema keys, and distinguish semantic failure from checker error.

Mutation tests must at least cover:

1. chronology reversal;
2. an altered orbit coordinate;
3. the \(n=2\) mixed-derivative multiplicity;
4. a changed action value;
5. a changed Hessian or Hill determinant;
6. a square/nonsquare flip;
7. a singular congruence matrix;
8. a false primitive-period claim;
9. promotion from scoped Morse-local STOP to a global cohomology no-go;
10. suppression of the post-pilot disclosure.

## 7. Source and artifact locks

| Upstream artifact | SHA-256 |
|---|---|
| Phase-1 RQ brief | `28ccf8b0cf7dc59584630e98a88d67cd630ec46caac08a69f2a10bee4a6a9a4e` |
| Phase-1 methodology | `a6be8f6d2e4ad8063ee743966390553d8e7370c15dc77a7895fb840fd5c91b8d` |
| Phase-1 DA checkpoint | `8d60ca898d1e2fb52b95216f5e65b72d99a871804e368d43936f961aa238d974` |
| Phase-2 search strategy | `4b156ca8b17e4fc5122d95e9d62bb300140ac8b7f2b25131b7551a58a8a162cf` |
| Phase-2 bibliography | `75b975013aea8835df561f6eb8cbea557486018379e002a80b2a26923c167ee4` |
| Phase-2 verified report | `4cc9bc74a22166f7aeb716ca91ef5bf35caf31d4c293fe87d67489a91688c1ec` |
| C12A derivation | `f524678196be667f0861c8cf64cb2f847824e3604bc356d6e59ca3188bdc6dfb` |
| C12A certificate | `851ca31f62fb508ad806c26084eab9fe092d5ee037bf99f0cb811cbccf7f8eb8` |

Primary-source theorem locators and their exact scope belong in the final
Phase-3 synthesis; their presence is a release gate, not an assumption of this
protocol.

