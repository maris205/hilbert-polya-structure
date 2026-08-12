# HCS-C32 Phase-2 search strategy

Date: 2026-08-11 UTC
Stage: Phase 2, investigation only
Candidate: `HCS-C32_ARTIN_SCHREIER_QUANTUM_TRACE`

## 1. Review question

For the area-preserving Hénon map

\[
H_6(q,p)=(1-6q^2-p,q)
\]

and its type-I generating function

\[
S_6(q,Q)=qQ-q+2q^3,
\]

does the finite-field Fourier--cubic-chirp operator and its Artin--Schreier
kernel yield a genuinely Hénon-specific arithmetic trace structure, rather
than a repackaging of generic exponential-sum cohomology, kernel calculus, or
Hill's formula?

The novelty threshold was deliberately set above the following baseline:

1. a unitary Fourier transform multiplied by a cubic phase;
2. Deligne concentration, rank \(2^n\), and purity for a smooth leading cubic;
3. chronological kernel composition by tensor product and \(Rf_!\);
4. the generic discrete Hill determinant identity.

A Phase-3 experiment may be recommended at the Phase-2 checkpoint only if a
nonformal bridge remains open between critical values or vanishing cycles and
the actual Hénon periodic multiplier \(\det(I-DH_6^n)\).  Recommendation does
not constitute authorization to start that experiment.

## 2. Stage firewall

This directory contains only a search protocol, source corpus, annotated
bibliography, and claim-verification report. It contains no experiment code,
computed results, manuscript, Route-B invocation, or Hilbert--Pólya claim.

## 3. Sources and search services

The search used:

- OpenAlex and Crossref for reproducible theorem-source discovery and DOI
  verification;
- arXiv for author versions and exact-title searches;
- Numdam/Centre Mersenne, journal sites, author-hosted PDFs, and DOI landing
  pages for primary full text;
- the local `henon_dynamics` corpus for nonduplication and source-locked prior
  results;
- a ranked web-search interface for cross-domain collision searches.

Only primary mathematical or physics sources support technical claims.
Secondary indexes and snippets were used only to discover or disambiguate a
primary source.

Foundational sources had no date cutoff. The direct-collision search covered
material visible through 2026-08-11.

## 4. Inclusion and exclusion criteria

### Include

A work was included when it directly addressed at least one of:

- quantization of the Hénon map;
- Hénon dynamics over finite or non-Archimedean fields;
- the precise Artin--Schreier trace over field extensions;
- Deligne's smooth-leading-polynomial theorem;
- Fourier--Deligne sign, shift, convolution, or duality conventions;
- cohomological or categorical trace terminology;
- critical-locus/Milnor-number descriptions of exponential-sum cohomology;
- the discrete Hill action-Hessian/monodromy identity.

### Exclude

A work was excluded from technical support when it concerned only:

- Hénon--Heiles flows rather than the Hénon map;
- image encryption or finite-precision chaos without arithmetic dynamics;
- generic Artin--Schreier curves with no discrete-action or Hénon link;
- continuous semiclassical tunnelling without a finite-field sheaf bridge;
- generic finite-field phase space or Weil quantization restricted to linear
  symplectic transformations;
- a result already subsumed by a more direct primary source.

## 5. Exact query ledger

The theorem lane used the following OpenAlex queries. The totals are the
indexed totals returned on 2026-08-11; only the stated top records were
screened.

| ID | Query | Indexed | Screened |
|---|---|---:|---:|
| T1 | `Deligne La conjecture de Weil I Theorem 8.4 Lemma 8.5 exponential sums` | 125 | 10 |
| T2 | `smooth leading homogeneous form Artin Schreier cohomology rank d minus 1 power n` | 15 | 10 |
| T3 | `Fourier Deligne transformation Artin Schreier sheaf trace function` | 108 | 10 |
| T4 | `l-adic sheaf convolution trace functions Frobenius` | 503 | 10 |
| T5 | `Artin Schreier sheaf dual additive character inverse Poincare duality` | 8 | 8 |
| T6 | `SGA 4 1/2 applications trace formula trigonometric sums Deligne` | 24 | 10 |

Six additional exact-title/author Crossref queries were used for Deligne
1974, Deligne 1977, Katz--Laumon 1985 and its 1989 erratum, Laumon 1987, and
the categorical-trace boundary source.

The novelty lane used the following exact strings. Ranked-search hit totals
are unstable, so the flow below counts candidate works, not displayed hits.

### Hénon quantization and finite fields

1. `"Hénon map" quantization finite field`
2. `"quantum Hénon map" cubic phase`
3. `"Hénon map" "Artin-Schreier"`
4. `"polynomial automorphism" finite field quantum map Fourier`
5. `nonlinear quantum map finite field cubic`
6. `finite-field Hénon quantum`
7. `"A quantized Hénon map" finite-dimensional trace formula`
8. `Fornæss Weickert Fourier cubic`
9. `Hénon quantum propagator generating function periodic orbits`
10. `nonlinear symplectic map finite Hilbert cubic phase`
11. `exact quantization Hénon torus`
12. `finite quantum mechanics nonlinear canonical transformations`
13. `finite field cubic phase Fourier quantum`
14. `"Hénon" "finite field" quantization unitary`
15. `"Hénon" "Artin-Schreier sheaf"`
16. `"cubic chirp" Fourier "finite field" unitary operator`
17. `"nonlinear symplectic map" "finite field" quantization`

### Critical loci, stationary phase, and trace formalism

18. `"discrete Lagrangian" "Artin-Schreier" sheaf`
19. `"action functional" exponential sum finite field symplectic map`
20. `"periodic orbit" exponential sums finite fields Hessian monodromy`
21. `"Hessian" "Artin-Schreier sheaf" critical points`
22. `discrete Lagrangian Hill formula periodic orbit Hessian monodromy`
23. `generating function symplectic map action Hessian det(I-monodromy)`
24. `Artin-Schreier vanishing cycles stationary phase Hessian`
25. `polynomial exponential cohomology isolated critical points Milnor`
26. `Laumon Fourier transform critical values vanishing cycles`
27. `kernel convolution diagonal trace Lefschetz Verdier`
28. `fixed sheaf kernel convolution trace`
29. `Fourier-Deligne trace function cubic`

### Arithmetic Hénon controls

30. `Hénon finite field zeta periodic points`
31. `Hénon good reduction canonical height`
32. `Hénon open problems arithmetic finite field`
33. `Roberts Vivaldi finite fields Hénon`
34. `Gurevich Hadani quantization finite fields nonlinear`
35. `A Thom-Sebastiani theorem characteristic p stationary phase`
36. `Around Thom-Sebastiani finite field vanishing cycles`

## 6. PRISMA-style flow

The theorem-source lane is exactly reproducible:

- 76 records identified: 58 OpenAlex records and 18 Crossref records;
- 68 unique records after deduplication;
- 62 excluded at title/metadata screening;
- 6 primary full texts assessed and included.

After merging the theorem, novelty, and bridge lanes, the auditable named-work
corpus contains exactly 24 unique entries.  All 24 received full-text or
official-metadata assessment: 20 were retained as core, boundary, bridge, or
contextual sources, and 4 were retained in the ledger as assessed exclusions.
The six primary theorem works are already among these 24 entries and are not
added a second time.

The following six recurring title/abstract-stage exclusion families were
logged separately.  They are search-screening categories, not stable named
works, and therefore are not included in the 24-work corpus counts:

| Ledger item | Exclusion reason |
|---|---|
| Hénon--Heiles Hamiltonian papers | continuous Hamiltonian flow, not the Hénon map |
| Hénon image-encryption schemes using finite fields | engineering key generation, no arithmetic dynamics or sheaf trace |
| Brownian-perturbed/digital Hénon S-box schemes | finite-precision cryptography, no exact polynomial automorphism |
| “quantum” image-compression papers using hyper-chaotic Hénon maps | quantum-information terminology without map quantization |
| generalized Hénon homoclinic-bifurcation papers | real bifurcation theory, no finite-field trace object |
| generic point-count bounds for Artin--Schreier curves | no discrete action, Hénon critical scheme, or kernel powers |

## 7. Search limitations

- Failure to find a direct collision is not proof of novelty. The ruling is
  `NOT_FOUND_WITHIN_SEARCH_BOUNDS`, never `NO_PRIOR_WORK_EXISTS`.
- Older French sources are poorly recalled by broad citation-index queries;
  exact-title searches were essential.
- No search result located a source that already combines the Hénon discrete
  action, an Artin--Schreier kernel, extension-degree Frobenius spectra, and a
  Hill-controlled vanishing-cycle factorization.
- Conversely, every individual baseline ingredient was located in prior art.

## 8. Local nonduplication lock

The following repository files were read and hash-locked during the audit:

| Local source | SHA-256 | Relevance |
|---|---|---|
| `next_paper_henon_foundations/README.md` | `c79816759a0fcb63a459bf89d1127345162eb06de26e42a3071059e1a5b3cc17` | generating function and prior real quantization |
| `next_paper_henon_candidate_search/REPOSITORY_UPDATE.md` | `231ee0e2470e16c74e07ac67080c188e5d840dbd3826b0c2e058a24375847a0b` | C05 phase-gauge no-go |
| `henon_pinning_trace_obstruction/SOURCE_AUDIT.md` | `900a658625a36079e2b24c66fa142fbc8c216a9b7c9a243e15c0e694bac9abc0` | Hill formula already identified as generic prior art |
| `henon_frobenius_scheme_obstruction/DERIVATION_PACKAGE.md` | `f524678196be667f0861c8cf64cb2f847824e3604bc356d6e59ca3188bdc6dfb` | finite-flat rank and Hénon Hill specialization |
| `henon_frobenius_scheme_obstruction/results/c12a_certificate.json` | `851ca31f62fb508ad806c26084eab9fe092d5ee037bf99f0cb811cbccf7f8eb8` | exact C12A arithmetic certificate |

The audit therefore forbids claims of first Hénon quantization, first action
twist, first \(2^n\) periodic scheme, or first action-Hessian/monodromy
identity.
