# HCS-C55 methodology blueprint

Status: **DOCS_FINAL_NO_MORE_EDITS; exact evidence, independent hostile paper
audit, and official compilation closed**.

## 1. Problem anchor

HCS-C53 constructs the rational equation model and the descended rank-\(10\)
middle core. HCS-C54 determines the full projective-monomial source group and
its nonconstant rational form. HCS-C55 asks the next geometric question:

> Does this central core extend over its full four-dimensional invariant
> deformation germ, and what exact local period tensor does that variation
> carry?

The answer is organized around one theorem-sized object: the rational
projective Yukawa cubic of the four-dimensional equivariant core.

## 2. Dominant contribution

The dominant contribution is the combined construction

\[
(B_{\rm core},\mathcal X,e_{\rm rel},\mathbb V_{\rm core},[Y_H]),
\]

where:

- \(B_{\rm core}\) is an algebraic rational four-germ cut transversely from
  the smooth fixed Hilbert locus;
- \(e_{\rm rel}\) is the norm graph of the nonconstant rank-\(24\) group
  scheme;
- \(\mathbb V_{\rm core}=e_{\rm rel}R^5f_*\mathbf Q(1)\) is a locally
  maximal rank-\(10\) CY3-type VHS;
- \([Y_H]\) is the exact rational projective Yukawa cubic;
- \(V(Y_H)\subset\mathbf P^3\) is a smooth geometrically irreducible cubic
  surface over \(\mathbf Q\). This field-of-definition statement does not
  assert that the surface is a rational variety over \(\mathbf Q\).

The algebraic family and relative correspondence are part of the theorem.
An honest Calabi--Yau threefold is not.

## 3. Supporting contribution

The cubic supplies a necessary local-VHS gate:

\[
Y_{\rm candidate}(v)=\lambda Y_H(Av)
\]

must hold under any pointed polarized-VHS identification. This gate is useful
because it is exact and basis-covariant, but it is intentionally one-sided.
A match advances a comparator to higher differential and monodromy tests; it
does not construct a correspondence or a motive.

## 4. Evidence hierarchy

| Level | Evidence | Mathematical role |
|---|---|---|
| E1 | vanishing, normal/Euler sequences, Hilbert theory | algebraizes all invariant abstract directions |
| E2 | ambient descent and Romagny fixed-point smoothness | handles the nonconstant rational group form |
| E3 | norm graph and central Hodge ledger | constructs the relative rank-\(10\) sub-VHS |
| E4 | Cayley residue multiplication and perfect top pairing | derives the Yukawa tensor |
| E5 | exact producer and structurally independent checker | certifies ranks, descent, coefficients, and smoothness |
| E6 | hostile schema and adversarial mutations | rejects convention collapse and shared-bug promotion |

E5 and E6 certify finite exact algebra. They do not replace the geometric
proofs in E1--E4.

## 5. Scope partitions

### 5.1 Source-theoretic partition

- adjunction and Akizuki--Nakano unobstructedness;
- Hilbert smoothness from \(H^1(N)=0\);
- embedded Kodaira--Spencer surjectivity from
  \(H^1(T_{\mathbf P^7}|X)=0\);
- fixed-locus smoothness for the finite linearly reductive group scheme;
- existence of a rational transverse slice.

### 5.2 Exact central-fiber partition

- the ambient \(\mathscr G\to\operatorname{PGL}_8\) cocycle;
- the four invariant rational tangent directions;
- the rank-\(10\) central Reynolds core;
- Cayley dimensions, top standard monomial, and tensor reductions;
- primitive cubic coefficients and gradient algebra.

### 5.3 Relative Hodge partition

- the universal action graph;
- horizontal algebraic action on \(R^5f_*\mathbf Q\);
- one Tate twist;
- local constancy and period-map immersion.

### 5.4 Comparator partition

- BCD \(\operatorname{Dic}_3\) and \(\mathbf Z_{12}\) families are
  admissible only as honest \((1,4)\) comparators;
- their full four-variable tensor is not supplied by the mirror-side
  one-parameter special geometry;
- no comparison label is promoted before the exact incidence problem is
  solved.

## 6. Proof/computation interface

The proof owns the meanings of every exact field:

- the fixed Hilbert tangent is \(H^0(N)^{\mathscr G}\);
- the abstract core tangent is \(H^1(T_X)^{\mathscr G}\);
- the four-slice is a complement to the kernel of Kodaira--Spencer;
- a tangent operator is \([yp]\in R_{1,0}\);
- its first action on \([y]\) is \([y^2p]\in R_{2,-3}\);
- the third variation is \([y^4p_ip_jp_k]\);
- the paired top trace is \([y^5p_ip_jp_k]\in R_{5,-6}\).

The code must certify these objects separately. It may not silently rename
one as another.

## 7. Exact-computation policy

- Arithmetic is exact over \(\mathbf Q(\rho)\) or \(\mathbf Q\).
- The chosen embedding, conjugation, determinant twist, tangent basis, term
  order, and top monomial are serialized.
- The Cayley descent convention is serialized as
  \(D(y)=y,D(z)=\rho z\); the checker rejects \(D(z)=\rho^2z\).
- The producer records all \(20\) unordered tensor entries.
- A direct generic-cubic reduction and a \(1/3/6\) reconstruction must agree.
- The checker reconstructs, rather than trusts, coefficient normalization.
- Smoothness is proved by an exact gradient quotient and an independently
  implemented projective saturation or equivalent no-nonzero-gradient test.
- Producer and checker must not share a cached Groebner basis.
- Repeated runs must be byte-identical apart from explicitly excluded
  environment/timing metadata.

## 8. Mandatory firewalls

Every theorem, result, paper section, and evaluation must reject:

- fixed Hilbert germ \(=\) four-dimensional core;
- tangent representation \(=\) literal linear family;
- \(h^1(T_X)=146-63\) without a proof that \(H^0(T_X)=0\);
- a constant rational group of order \(24\);
- an average over only the two rational group elements;
- an unconstructed relative Chow--Künneth projector;
- \(\mathbf Q(2)\) in place of \(\mathbf Q(1)\);
- \(D(z)=\rho^2z\) in place of the required \(D(z)=\rho z\);
- tangent operator \([y^2p]\);
- top trace at \(y^4\);
- omitted mixed-term multinomial factors;
- geometric irreducibility from rational factorization alone;
- a claim that the \(\mathbf Q\)-defined cubic surface is
  \(\mathbf Q\)-rational;
- a positive BCD comparison from Hodge numbers or a one-variable tensor;
- a motive from a Hodge or Yukawa match.

## 9. Basis and normalization policy

The displayed cubic uses

\[
q_0=e_0,\quad q_1=e_1+e_3,\quad
q_2=(1+2\rho)(e_1-e_3),\quad q_3=-\rho e_2.
\]

The exploratory convention \(q_0=2e_0\) is a different coordinate system.
The release must choose one basis once and propagate it to the tangent
certificate, all \(20\) reductions, the polynomial, its derivatives, and
every hash.

Only the projective tensor is intrinsic. A common nonzero trace or residue
normalization is harmless; direction-dependent rescaling is not.

## 10. Promotion rule

Promotion is split into three noncircular stages.

1. Code/results release-candidate status requires deterministic producer
   output, independent checker output, complete scalar-leaf classification,
   the exhaustive semantic-leaf rebound sweep, every negative mutation, and
   the persistent scoped manifest. This stage has passed.
2. Paper-source freeze requires the source audit with exact locators and the
   independent proof/paper consistency sweep. This stage has passed.
3. Final documentation and inventory freeze requires the single clean
   official LaTeX build, the PDF/source/report/Route hash backfill, and the
   verified 47-entry full-project manifest under an external-only hash policy.
   This stage has passed.

The implementation commit remains null as an explicitly later provenance
stage and is not a theorem dependency. The full-project manifest inventory is
current; its SHA-256 is deliberately reported only outside manifest-covered
artifacts to avoid a self-hash cycle, and it is not used as paper evidence.
