# Paper 8 Phase-2 trace/harmonic source manifest

Frozen: 2026-08-14 (Asia/Shanghai)  
Scope: invariant-measure traces on continuous crossed products, Plancherel
weights and dual-Haar normalization, lower-semicontinuous trace induction,
normality, and Fourier/Poisson normalization.  The `grp-*` groupoid and
imprimitivity corpus is owned by the separate
`phase2_groupoid_source_audit.md`.

Only load-bearing full texts were retained.  Every local PDF has a same-stem
sidecar generated with ARS `pdf_read_preflight/1.0.0` under `pypdf 6.15.0`.
All six sidecars return `PASS`: declared, recursively enumerated, and reader
page counts agree and all warning arrays are empty.  Hashes are SHA-256 over
the exact local bytes.

| ID | Exact local full text | Authoritative retrieval endpoint | Pages | PDF SHA-256 | Sidecar SHA-256 | Retention role |
|---|---|---|---:|---|---|---|
| `TR-BR18` | `trace-bourne-rennie-2018-crossed-product.pdf` | <https://www.rennieillawarramath.com/website-pdfs/JournalArticles/2018BRCtsPublished.pdf> | 62 | `57e7ba6c1908a20956f783efbd8288be6d75e10d42d1d1b026f7f46bbef4f5f5` | `9979dbe95e08dc7a89f896e9480cc5f88a3b1f4bec65f8a9fd707831a81cea6c` | invariant-measure trace on a continuous `R^d` crossed product and its von Neumann extension |
| `TR-CZ83` | `trace-combes-zettl-1983-morita-traces.pdf` | <https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0265/LOG_0013.pdf> | 17 | `3e7ba9278b12848df4af02fe00ffef8f26114c44ec9ab7c4d995db29614e0a39` | `04db54cf9b02e5a05a01a8e98e99ea286c63217c13d545337f061361ac57067a` | l.s.c./normal trace induction under C*/W* Morita equivalence |
| `TR-ERS11` | `trace-elliott-robert-santiago-2011-lsc-traces.pdf` | <https://arxiv.org/pdf/0805.3122> | 33 | `5d2bebc7199c8243b4532db96bf1677e5ee54f968d8d16be671b58c4fa93d4da` | `40672ba53d30a0a75ba99cb895b518ca1f39cdf56894eac68fd71e20c69ad13c` | definition, regularization, and functorial pullback of l.s.c. traces |
| `TR-REN21` | `trace-renault-2021-dual-haar.pdf` | <https://comptes-rendus.academie-sciences.fr/mathematique/item/10.5802/crmath.183.pdf> | 6 | `d703672f7d3f70256a3f83ae5ba6c3cdd7ab87a65249fb51d7b544cc3095387f` | `9869ecee2908cc31de52112d1bfbe91ff5a55299f7f9594597ccc80ce4a8bc4e` | Plancherel weight and the Fourier-isometric normalization of dual Haar |
| `OP-JON09` | `op-jones-2009-von-neumann-notes.pdf` | <https://math.berkeley.edu/~vfr/VonNeumann2009.pdf> | 127 | `69b0850316db1efe424433f432e5f817adabaabff80c7a9029a4607a2b431936` | `c191b481f07158622f06e4ea84b86642d49696d7d8937f06a48181b2d76ed633` | `vN(Z)=L-infinity(T)`, Haar trace, and normality criterion |
| `HA-LAU17` | `harm-laugesen-2009-harmonic-analysis.pdf` | <https://arxiv.org/pdf/0903.3845v2> | 176 | `b1ef00490b91e492cd9906849256a172a0ea261f7d19fa6b6265ef425d78d51c` | `0eda6daa2fc6464eb03b99d5413a0005bcfbe7fafea19d3fb310a982e3689a8a` | locked Fourier convention, rapid decay, and Poisson summation |

The independent checksum list is `trace_source_checksums.sha256` in this
directory.  It covers the six PDFs and six preflight sidecars and intentionally
does not self-hash this manifest.

## Exact bibliographic and locator index

### `TR-BR18`

Chris Bourne and Adam Rennie, “Chern Numbers, Localisation and the Bulk-edge
Correspondence for Continuous Models of Topological Phases,” *Mathematical
Physics, Analysis and Geometry* **21** (2018), article 16, 62 pp.,
doi:10.1007/s11040-018-9274-4.

- Proposition 3.2, physical pp. 8--9: a faithful semifinite norm-l.s.c.
  invariant tracial weight on the coefficient algebra induces the standard
  trace on compact module endomorphisms and an extension on the generated von
  Neumann algebra.
- Lemma 7.4, physical p. 36: for compact `Omega`, an invariant full-support
  probability `P` gives
  `T(f)=integral_Omega f(0;omega)dP(omega)` on the continuous crossed product;
  `T` is faithful, semifinite, norm-l.s.c., contains the stated dense algebra
  in its domain, and extends to the displayed von Neumann closure.
- Definition A.2, physical p. 53: the paper's ambient semifinite spectral
  triple uses a faithful normal semifinite trace on its von Neumann algebra.

This is a direct continuous-crossed-product source, not a theorem identifying
Paper 8's locked regular representation or its isotropy-character
decomposition.  Full support is used for faithfulness; invariance and
unimodularity are the traciality gates.

### `TR-CZ83`

Francois Combes and Heinrich H. Zettl, “Order Structures, Traces and Weights
on Morita Equivalent C*-Algebras,” *Mathematische Annalen* **265** (1983),
67--81, doi:10.1007/BF01456936.

- Proposition 2.2, physical pp. 7--8 (printed pp. 72--73): strong Morita
  equivalence gives reciprocal induction of norm-l.s.c. traces and preserves
  faithfulness, dense definition, and semifiniteness.
- Proposition 3.1, physical pp. 11--12 (printed pp. 76--77): the W*-Morita
  analogue induces normal traces and preserves faithfulness and
  semifiniteness.

The theorem gives an induced trace, not an algebra isomorphism, a canonical
trivialization, a full/reduced factorization, or a trace-preserving
identification of two preselected completions.

### `TR-ERS11`

George A. Elliott, Leonel Robert, and Luis Santiago, “The Cone of Lower
Semicontinuous Traces on a C*-Algebra,” *American Journal of Mathematics*
**133**(4) (2011), 969--1005, doi:10.1353/AJM.2011.0027; retained arXiv
manifestation `0805.3122v2`.

- Section 3.1 and Lemma 3.1, physical p. 4: definition of an extended-positive
  C*-trace and its l.s.c. regularization.
- Section 3.3 and Theorem 3.11, physical p. 12: if `phi:A->B` is a
  *-homomorphism, composition defines the contravariant pullback
  `T(phi):T(B)->T(A)` of l.s.c. traces.

Pullback preserves lower semicontinuity and the trace identity.  The theorem
does not make the pullback densely finite or faithful; those are separate
image/kernel/domain questions.

### `TR-REN21`

Jean Renault, “Continuity of the Dual Haar Measure,” *Comptes Rendus
Mathematique* **359**(4) (2021), 415--419,
doi:10.5802/crmath.183, CC BY 4.0.

- Introduction, physical p. 3 (printed p. 416): a Haar measure on an abelian
  group determines the unique dual Haar measure for which Fourier transform is
  an `L2` isometry.
- Section 2, physical pp. 3--4 (printed pp. 416--417): the canonical
  left-Hilbert-algebra weight is faithful, semifinite, and sigma-weakly l.s.c.;
  for a group it is the Plancherel weight and satisfies the displayed
  convolution/identity-coefficient formula.
- Proposition 3 and Definition 4, physical p. 4 (printed p. 417): l.s.c.
  Plancherel weights for a continuous group bundle.
- Corollary 5, physical p. 5 (printed p. 418): for an abelian group bundle, the
  Fourier-isometric dual Haar measures form a continuous Haar system.

For `H=L Z` with counting Haar, specializing the Fourier-isometry convention
selects `dtheta/(2pi)` on `hat H`.  The numerical specialization is a short
calculation; the source supplies the uniqueness and normalization principle.

### `OP-JON09`

Vaughan F. R. Jones, *Von Neumann Algebras*, UC Berkeley course notes,
1 October 2009.

- Physical p. 15: Fourier transform identifies `vN(Z)` with
  `L-infinity(T,Haar)`.
- Physical p. 16: the canonical group trace is the identity Fourier
  coefficient and becomes `(1/(2pi)) integral_0^(2pi) f(theta)dtheta`.
- Definition 7.1.2, physical p. 43, and Theorem 7.1.3, physical p. 44: a state
  on a von Neumann algebra is normal iff it is ultraweakly continuous
  (equivalently completely additive).
- Definition 8.1.2 and Theorem 8.1.3, physical p. 50: ordinary trace class and
  its ideal structure.

These are authoritative lecture notes, not the primary historical source.
They do not state Paper 8's point-evaluation no-extension lemma; they supply
the exact normality criterion and the `vN(Z)` model used in that new lemma.

### `HA-LAU17`

Richard S. Laugesen, *Harmonic Analysis Lecture Notes*,
arXiv:0903.3845v2 (2017 manifestation of the 2009 notes).

- Definition 14.1, physical p. 79: `fhat(xi)=integral f(x)e^{-i xi x}dx`.
- Theorems 14.10--14.11, physical pp. 84--85: differentiation/decay; repeated
  application gives rapid decay for `C_c^infinity` functions.
- Theorem 23.5, physical p. 137: the Poisson summation formula with this exact
  Fourier convention.

The source formula uses its own `2pi Z` lattice.  Paper 8's arbitrary-`L`,
modulated/Floquet formula and the character sign must be derived from the
locked representation; they are not quoted verbatim from this source.

## Cross-audit source used but not duplicated

Dana P. Williams, *Crossed Products of C*-Algebras*, author draft v3.1,
equation (4.63) and Theorem 4.30, printed p. 138, supplies the quotient integral
formula and the one-orbit `C*(H) tensor K` isomorphism.  Its retained
`grp-williams-crossed-products-draft3.1.pdf` bytes, preflight, and limitations
belong to `phase2_groupoid_source_audit.md`.  It is not duplicated in this
manifest.  Specializing (4.63) to Lebesgue Haar on `R`, counting Haar on
`L Z`, and the quotient `R/(L Z)` yields the locked length-Haar Weil template;
the specialization and all sign checks remain Paper 8 proof obligations.

## Screened but not retained

| Source | Screening result |
|---|---|
| Peter Hahn, “The Regular Representations of Measure Groupoids,” *Trans. AMS* 242 (1978), 35--72, doi:10.1090/S0002-9947-1978-0496797-8 | Highly relevant to the general measured-groupoid von Neumann construction, but the official AMS PDF returned HTTP 403.  Unauthorized mirrors were rejected; metadata alone receives no theorem credit. |
| Patricia Boivin, “L^p Spaces of the von Neumann Algebra of a Measured Groupoid,” *C. R. Math.* 346 (2008), 969--974, doi:10.1016/j.crma.2008.07.020 | Correct measured-groupoid context but focused on noncommutative `L^p`/Hausdorff--Young theory, not the locked invariant-measure trace normalization. |
| Alain Connes, “A Survey of Foliations and Operator Algebras” (1982) | Contextual transverse-measure-to-trace statements, but no sharper support for the locked continuous crossed-product/Floquet claims than `TR-BR18` and the groupoid audit. |
| Jean Renault, “Invariant Measures and Traces on Groupoid C*-Algebras” (2026 preprint with coauthor) | Etale-groupoid hypotheses do not match the continuous `R`-action groupoid; excluded to prevent theorem-type drift. |

## Reuse boundary

The links and exact hashes make this reading corpus reproducible.  Retention
does not itself establish a right to redistribute every publisher or
author-hosted PDF.  Before a public repository release, verify the licence of
each artifact; if necessary publish this manifest, checksums, and retrieval
links without the PDF bytes.
