# HCS-C52 research question

Status: **locked B0--B2 question; theorem certified**

## Dominant question

For the explicit source fivefold

\[
 X:\quad
 \sum_{i=0}^{7}x_i^3=0,
 \qquad
 \sum_{i=0}^{6}x_ix_{i+1}+\rho x_7x_0=0
 \subset\mathbf P^7_{\mathbf Q(\rho)},
\]

what is the smallest middle-cohomology summand containing the extreme
Hodge lines that can be cut out by algebraic graph correspondences coming
from projective monomial source symmetries?

This deliberately narrows the C51 gate.  It asks first for the strongest
projector supplied by the natural graph algebra, not for an unrestricted
classification of all algebraic correspondences.

## Finer questions

1. Which projective monomial maps preserve both the Fermat cubic and the
   source-ordered quadric, including the \(\rho x_7x_0\) closing edge?
2. Do those maps form
   \(\operatorname{Dih}(C_{12})\) of order \(24\)?
3. How is the middle Chow--Künneth projector isolated from the ambient Tate
   cohomology?
4. What are the exact \(G_{\mathrm{mon}}\)-characters on
   \(H^{4,1}_{\mathrm{prim}}\) and
   \(H^{3,2}_{\mathrm{prim}}\)?
5. Is the extreme \(H^{4,1}\) line trivial under the source group, and how
   many trivial copies occur in \(H^{3,2}\)?
6. What ranks and Hodge ledgers do the Reynolds projector and its complement
   have after \(\pi_5\)?
7. Can any idempotent in \(\mathbf Q[G_{\mathrm{mon}}]\), central or not,
   separate the extreme pair from every trivial level-one copy?
8. Which conclusions hold in the Chow category, and which are only
   cohomological controls?

## Locked answer form

The paper is designed around one positive/negative pair.

### Positive component

Construct mutually orthogonal \(K\)-rational Chow projectors

\[
 \pi_{\mathrm{core}}=\pi_5e_G,
 \qquad
 \pi_{\mathrm{lev}}=\pi_5-\pi_5e_G,
\]

with middle ranks \(10\) and \(158\), respectively, and prove their Hodge
ledgers.

### Negative component

Prove that the rank-10 core is the minimal graph-algebra block containing
the extreme Hodge pair.  The desired rank-two projector is therefore not
available in \(\mathbf Q[G_{\mathrm{mon}}]\).

## Stop/go gates

- **B0 PASS:** the inherited field, equations, smoothness scope, Hodge
  normalization, and closing edge are byte- and formula-locked.
- **B1 PASS:** the monomial group and Chow projectors are reconstructed
  exactly, including multiplication, transpose, commutation, and
  orthogonal idempotence.
- **B2 PASS:** an exact characteristic-zero Cayley-ring calculation gives
  the declared character and rank ledgers, and the augmentation lemma is
  proved.
- **AMBER RELEASE:** B0--B2 pass; the project ends with the graph-algebra
  optimum theorem.
- **STOP:** failure of any B0--B2 gate.  No finite-prime pattern may repair
  a failed characteristic-zero theorem.
- **C53, not C52:** a full projected Frobenius polynomial, a local
  irreducibility obstruction, or an incidence correspondence outside the
  graph algebra.

## Explicit non-questions

C52 does not ask whether:

- every automorphism of \(X\) is monomial;
- the rank-10 Hodge structure is the cohomology of an actual
  Calabi--Yau threefold;
- the core is CM, modular, or automorphic;
- its \(L\)-function has continuation or a functional equation;
- a prime-by-prime numerical projector exists;
- the full normalized Hénon Euler germ satisfies RH.

## Evidence labels

- **Inherited theorem:** C50--C51 model, characteristic-zero smoothness,
  and Hodge dimensions of \(H^5(X)\).
- **Target theorem:** B1 Chow projector and B2 representation/optimality
  statements.
- **Pilot evidence:** temporary modular or reconnaissance calculations.
- **Future C53 evidence:** projected local Frobenius polynomials and
  correspondences outside \(\mathbf Q[G]\).
- **Source status:** primary locators and claim boundaries are recorded in
  SOURCE_AUDIT.md; no absolute external-priority claim is made.
