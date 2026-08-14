# HCS-C55 source-control and bounded-novelty audit

Status: **DOCS_FINAL_NO_MORE_EDITS; primary theorem locators, exact
release-candidate tuple, bounded novelty screen, independent hostile paper
audit, and official compilation verified**.

Audit date: 2026-08-15 UTC.

## 1. Formal evidence boundary

The C55 theorem uses external sources for general deformation, fixed-point,
Hodge-residue, and comparator facts. The source-specific group action,
four-dimensional invariant basis, top reductions, cubic coefficients, and
gradient algebra must be proved or exactly certified inside HCS-C52--C55.

Temporary architecture calculations are reconnaissance, not release
evidence. At promotion, the formal chain will consist only of:

- released HCS-C52--C54 artifacts;
- the C55 proof and derivation packages;
- the primary sources and locators below;
- promoted C55 producer/checker artifacts and the independent read-only
  hostile audit record. No unpackaged temporary hash is release authority.

## 2. Deformation and algebraization sources

### 2.1 Akizuki--Kodaira--Nakano vanishing

**Jean-Pierre Demailly**, “\(L^2\) Vanishing Theorems for Positive Line
Bundles and Adjunction Theory,” CIME lectures, 1994; published in
*Transcendental Methods in Algebraic Geometry*, Lecture Notes in Mathematics
1646, Springer, 1996, pp. 1--97; arXiv:alg-geom/9410022.

Verified locator:

- Theorem 4.11 states that for a positive line bundle \(F\) on a compact
  complex \(n\)-fold,
  \(H^q(X,\Omega_X^p\otimes F)=0\) when \(p+q\ge n+1\).

Use in C55:

\[
H^2(X,\Omega_X^4(3))=H^2(X,T_X)=0
\]

for \(n=5,p=4,q=2\). This source proves the vanishing theorem, not the
source-specific identification of the invariant tangent basis.

Verified author-site PDF SHA-256:

\[
7dfeb8895ff6dde0b05ff449eabc1909d64caccf852d79d5e76630057e62d3db.
\]

### 2.2 Hilbert tangent and obstruction theory

**Robin Hartshorne**, *Deformation Theory*, Graduate Texts in Mathematics
257, Springer, 2010, DOI 10.1007/978-1-4419-1596-2.

Verified locators:

- Theorem 1.1(b),(c): the Hilbert tangent is \(H^0(N)\), and for a local
  complete intersection \(H^1(N)=0\) implies nonsingularity of the Hilbert
  scheme at the point;
- Theorem 2.4 and Corollary 2.5 give the first-order tangent description;
- Corollary 6.3 and Remark 6.3.1 give the no-local-obstruction/lci route.

Use in C55: smoothness of \(\operatorname{Hilb}(\mathbf P^7)\) at
\([X_0]\) after the internal cohomology calculation \(H^1(N)=0\).

The official Springer metadata was verified. No local book PDF is included
in the C55 source pack, so no PDF hash is asserted.

### 2.3 Smoothness for a nonconstant group scheme

**Matthieu Romagny**, “Algebraicity and smoothness of fixed point stacks,”
arXiv:2205.11114, v3 dated 2022-09-16.

Verified author-PDF locators:

- the manuscript itself is dated 2022-05-23;
- the paragraph before Theorem 1.2.1 includes finite locally free group
  schemes of invertible order among linearly reductive group schemes;
- Theorem 1.2.1(2) states that a smooth \(X/S\) has smooth fixed-point stack
  under a linearly reductive \(G/S\);
- Definition 4.3.5, item (2), again records the finite locally free
  invertible-order case;
- Theorem 4.3.6 proves the smoothness assertion.

Use in C55: smoothness of the \(\mathscr G\)-fixed Hilbert germ over
\(\mathbf Q\). This is the direct group-scheme source and does not require
pretending that \(\mathscr G\) is constant.

Author-site PDF SHA-256:

\[
dc2a73f456a3cd69ca28a4c54585c4e6744359e939d7864c661c7d05f9aaa475.
\]

As of this audit, only arXiv/preprint metadata is asserted; no journal
publication is claimed.

### 2.4 Equivariant versality as background

**D. S. Rim**, “Equivariant \(G\)-structure on versal deformations,”
*Transactions of the American Mathematical Society* 257 (1980), 217--226,
DOI 10.1090/S0002-9947-1980-0549162-8.

The corollary on p. 225 provides equivariant structure on a versal
deformation for a linearly reductive group. C55 uses it only as an abstract
comparison for the completed fixed Kuranishi germ. The algebraic family is
constructed from the fixed Hilbert locus, not inferred from Rim alone.

## 3. Cayley ring, infinitesimal variation, and pairing

### 3.1 Complete-intersection residue identification

**Jan Nagel**, “The Abel--Jacobi Map for Complete Intersections,”
*Indagationes Mathematicae* 8 (1997), no. 1, 95--113,
DOI 10.1016/S0019-3577(97)83353-8.

Verified locators:

- Definition 2.15 defines the Cayley Jacobian ideal and bigraded ring;
- Proposition 2.16 gives
  \(H_{\rm var}^{n-p,p}(X)\simeq R_{p,d(X)}\), where
  \(d(X)=\sum d_i-n-r-2\);
- Lemma 3.1 gives the commutative diagram identifying the infinitesimal
  variation with the correctly graded multiplication maps.

For a \((2,3)\) complete intersection of dimension five, \(d(X)=-3\), so
the relevant pieces are \(R_{p,-3}\).

Local PDF SHA-256:

\[
a9812b6bbcec658d0d8ab5eec2249f1e63e9b0da1922043f2f27500c7cd85a4f.
\]

### 3.2 Multiplication and perfect pairing

**Kazuhiro Konno**, “On the variational Torelli problem for complete
intersections,” *Compositio Mathematica* 78 (1991), no. 3, 271--296.

Verified locators:

- Theorem 6.1(2) identifies \(R_{1,0}\) with the Kodaira--Spencer image
  and, outside the stated K3 exception, with \(H^1(T_X)\);
- Theorem 6.1(3) identifies cup product with Jacobian multiplication;
- Theorem 6.1(4) identifies the cup-product pairing with the ring pairing,
  outside the stated odd-dimensional \((2,2)\) exception;
- Lemma 6.2 proves the required duality/perfect-pairing statement.

The C55 \((2,3)\) fivefold is not an excluded \((2,2)\) complete
intersection. These locators justify the operator and pairing mechanisms up
to uniform normalization; they do not supply the \(20\) source-specific
coefficients.

Official Numdam/local PDF SHA-256:

\[
ff4912811c92a9647b25d9f98b1dce9990bccacb967f9e31d2d7660f62980436.
\]

### 3.3 The precise \((2,3)\) fivefold instance and a warning

**David Favero, Atanas Iliev, and Ludmil Katzarkov**, “On the Griffiths
Groups of Fano Manifolds of Calabi--Yau Hodge Type,”
*Pure and Applied Mathematics Quarterly* 10 (2014), no. 1, 1--55,
DOI 10.4310/PAMQ.2014.v10.n1.a1; arXiv:1212.2608.

Verified locators:

- Section 5.1 records
  \(h^{4,1}=1\) and \(h^{3,2}=83\);
- Section 5.4 defines the precise bigrading
  \(\deg y=(1,-3),\deg z=(1,-2),\deg x_i=(0,1)\) and states
  \(H_{\rm var}^{5-p,p}=R_{p,-3}\);
- Section 5.6 explicitly warns that the induced map on already contracted
  \(R_{2,-3}\) classes is not ordinary multiplication in that bigrading.

Use in C55: instance-specific Hodge/Cayley context and the firewall requiring
operator multiplication from \(R_{1,0}\), followed by the top pairing.

Local PDF SHA-256:

\[
02fd23c00c0130c1a4d75451da6a26df516f24d1b2bc89c5cc8477f544388271.
\]

### 3.4 Calabi--Yau-type definition and generalized Yukawa

**Atanas Iliev and Laurent Manivel**, “Fano manifolds of Calabi--Yau Hodge
type,” *Journal of Pure and Applied Algebra* **219**(6) (2015), 2225--2244,
doi:10.1016/j.jpaa.2014.07.033; arXiv:1102.3623.

The arXiv/author-manuscript title omits the word “Hodge”; the published
metadata above is preferred for the bibliography.

Verified locators:

- Definition 2.1 includes the contraction isomorphism in the definition of a
  manifold of Calabi--Yau type;
- Theorem 2.2 and Proposition 2.3 describe the integrable-system and local
  period-map behavior;
- the discussion preceding Proposition 2.3 defines the generalized Yukawa
  cubic;
- Section 3.1 lists the \((2,3)\) fivefold with \(83\) moduli.

Use in C55: conceptual terminology only. The exact rational sub-VHS and cubic
are internal to C55.

Local PDF SHA-256:

\[
f4b9b70ef06230e0a69c84399f1f0bd5e050992f50db9018c1cab110b8a18d33.
\]

## 4. Honest \((1,4)\) comparator sources

### 4.1 Four-modulus quotient families

**Volker Braun, Philip Candelas, and Rhys Davies**, “A Three-Generation
Calabi--Yau Manifold with Small Hodge Numbers,” *Fortschritte der Physik*
**58** (2010), nos. 4--5, 467--502,
doi:10.1002/prop.200900106; arXiv:0910.5464.

Verified source facts:

- the covering CY3 admits free actions by
  \(\mathbf Z_{12}\) and \(\operatorname{Dic}_3\);
- both smooth quotients have
  \((h^{1,1},h^{2,1})=(1,4)\);
- the invariant defining equations have four projective parameters;
- the paper explicitly says its Yukawa couplings are not discussed;
- the enhanced \(\operatorname{Dih}_6\) locus is singular, with generic
  member having three nodes.

Verified locators:

- the Introduction states the four-dimensional complex-structure count and
  explicitly says that Yukawa couplings are not discussed;
- Section 2.1 reduces the invariant equation to four projective parameters;
- Section 4.2 identifies the \(c_0=c_1=0\) enhanced-dihedral locus and says
  its generic member has three nodes;
- Section 7 constructs the \(\mathbf Z_{12}\) quotient and again obtains
  \((h^{1,1},h^{2,1})=(1,4)\).

Use in C55: admission of the two generic quotient families as potential
honest comparators, rejection of the nodal enhanced-symmetry locus as a
smooth substitute, and confirmation that the source paper does not provide
the required four-variable tensor.

Local PDF SHA-256:

\[
cb999f7a4b6dbd955c4263ea4d67303c091a4e9b34d4077e84503cb4ba4dd82a.
\]

### 4.2 One-parameter special geometry

**Volker Braun, Philip Candelas, and Xenia de la Ossa**, “Two One-Parameter
Special Geometries,” arXiv:1512.08367.

Verified source facts:

- Sections 2.3--2.4 study a one-parameter complex-structure variation of
  the mirror of the \((1,4)\) quotient, equivalently the
  one-K\"ahler-parameter special geometry on the original side;
- it derives a fourth-order Picard--Fuchs equation and a scalar
  one-variable Yukawa coupling.

Use in C55: a negative scope boundary. This mirror-side scalar coupling is
not the full four-variable B-model tensor of the original quotient required
by the realization gate. C55 does not assert that it is a restriction of
that four-variable tensor.

Local PDF SHA-256:

\[
40f5d170981d446f47ba08e7742a509975c62cae47e25bcbf07a5693f09cb364.
\]

### 4.3 Small-Hodge catalogue

**Philip Candelas, Andrei Constantin, and Challenger Mishra**,
“Calabi--Yau Threefolds With Small Hodge Numbers,” *Fortschritte der
Physik* **66** (2018), no. 6, article 1800029,
doi:10.1002/prop.201800029; arXiv:1602.06303.

The catalogue records the \((1,4)\) entry through the order-\(12\) quotient
constructions. Use in C55: candidate inventory only. A catalogue entry is not
a uniqueness theorem and does not supply a Yukawa tensor.

Local PDF SHA-256:

\[
bc748edb1d1577440ae9684485559655da0a1c2aa1cb733d97c46833eb86be3b.
\]

## 5. Claim-to-source boundary

| C55 claim | External source role | C55 internal closure |
|---|---|---|
| \(H^2(T_X)=0\) | Demailly 4.11 | adjunction specialization |
| smooth Hilbert point | Hartshorne 1.1(b),(c) | \(N=\mathcal O(2)\oplus\mathcal O(3)\), vanishing |
| smooth fixed germ | Romagny 1.2.1(2), 4.3.6 | ambient nonconstant action and rational slice |
| abstract equivariant comparison | Rim p. 225 | not used for algebraization |
| Hodge pieces | Nagel 2.16; FIK 5.4 | exact quotient ranks and invariant sectors |
| period derivative | Nagel 3.1; Konno 6.1(2),(3) | all-\(24\) invariant basis and multiplication-by-\(y\) rank |
| top pairing | Konno 6.1(4), 6.2 | exact \(R_{5,-6}\) line and its rational descent |
| projective cubic | generalized-Yukawa background | all \(20\) reductions and common normalization |
| smooth cubic surface | no external classification needed | exact finite gradient quotient and geometric argument |
| BCD comparator admission | BCD original paper/catalogue | admission closed; optional full tensor/incidence remains unavailable in the bounded-search data |

## 6. Search-bounded novelty audit

This is a targeted audit, not a systematic-review or uniqueness certificate.

Search date: 2026-08-15 UTC.

The architecture search and a fresh official-arXiv-focused query used
conjunctions of:

- Braun/Candelas/Davies, \(\operatorname{Dic}_3\), \(\mathbf Z_{12}\);
- four-parameter or four-variable Yukawa;
- three-generation Calabi--Yau and \(h^{2,1}=4\).

The search recovered the original quotient paper and the later
one-parameter special-geometry paper. It did not locate a paper giving the
full four-variable B-model Yukawa tensor for either quotient. This negative
search result justifies only the label
NOT-COMPARABLE-WITH-CURRENT-DATA. It is not evidence that such a tensor does
not exist unpublished or under different terminology.

No novelty claim is made for:

- Hilbert-scheme algebraization;
- Reynolds projectors;
- the general Cayley residue formalism;
- the general projective-cubic necessary condition.

The source-specific novelty target is the exact rational four-direction
tensor and its application to this descended HCS core, subject to ordinary
referee review.

## 7. Source-audit verdict

**PASS: SOURCE LOCATORS AND BOUNDED NOVELTY FIREWALLS SUPPORT THE
RELEASE-CANDIDATE THEOREM.**

No current source supports the forbidden promotions “literal invariant
linear family,” “relative Chow--Künneth projector,” “\(\mathbf Q(2)\),”
“honest CY3,” or “motive from Yukawa.” The exact code gates previously
identified by the hostile audit pass in the release-candidate tuple; their
finite conclusions remain distinct from the source-theoretic implications.
