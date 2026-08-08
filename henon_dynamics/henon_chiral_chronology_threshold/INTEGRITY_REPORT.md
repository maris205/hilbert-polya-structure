# HCS-C21 research-integrity report

## Source integrity

The exact producer refuses to run if any of these inputs changes:

| Dependency | Frozen SHA-256 |
|---|---|
| Local Paper-5 PDF | `23dad812162728316f633081e1a1995d4c00614a70d0f5877d425c68d0c726b9` |
| HCS-C12C certificate | `964b8c98abc850493529b8e939a9c8ff96c832300ad2b1629b1cff807f0e8020` |
| HCS-C20 certificate | `7ee43e3253aff15ec00d78b9633c3d3362e71cd5a880cd3e928e7f322abb2681` |

The decisive external period-six formulas were checked directly in
Endler--Gallas, *Physics Letters A* 356 (2006), equations (11)--(15).  They
are attributed as prior work.

## Computational integrity

- All mathematical calculations use exact symbolic arithmetic.
- The checker imports neither the producer nor predecessor implementations.
- The independent report is deterministic across repeated runs.
- The current certificate SHA-256 is
  `5386c95cbc65e6a4323cfcf230de6b41f353be909d197818f9c4fbf0a75a96fc`.
- The checker reports PASS with 133 named checks.
- The fourteen-test suite includes ten deliberate certificate mutations, all
  of which fail closed.
- The stored hash ledger verifies every code and JSON artifact.

## Data integrity

No Riemann-zero table, prime table, target spectrum, fitted scale, learned
parameter, floating-point threshold, or training/test split enters the
result.  The only finite combinatorial range is the explicit source-scoped
comparison through period seven.

## Clock integrity

The project separates:

- primitive Hénon period \(n\);
- chronological phase \(s\);
- Frobenius degree \(r_F\);
- source radical \(\eta\), with \(\eta^2=A-3\).

Chronological maps are composed in order.  No averaged transition matrix is
used.

## Claim integrity

The package does not claim:

- novelty for the published period-six marker or coordinate carrier;
- a full period-six or saturated period-seven classification;
- a primitive cross-period Hecke correspondence;
- a dynamical or Fredholm determinant;
- a global Euler product or functional equation;
- a Riemann-zero divisor;
- a Hilbert--Pólya operator.

The targeted novelty search cannot establish priority and is explicitly
reported as non-exhaustive.

## PDF-integrity limitation

The local Paper-5 bytes are frozen, but an optional PDF read-integrity
preflight was unavailable.  No page-specific claim in the C21 synthesis
depends on an unverified local page number.

## Manuscript integrity

The released HCS-C21 manuscript was rebuilt after all source revisions.

- PDF SHA-256:
  `984ad0bc7cd0fe8840ce6a6f442dd377f930127e28836137ca814a2dd30847e1`;
- pages: 17;
- undefined citations/references: none;
- missing characters: none;
- overfull boxes: none;
- fonts: all embedded;
- source freshness: no tracked TeX or BibTeX input is newer than the PDF.

Eighteen cosmetic bibliography underfull notices arise from long frozen
repository URLs.  They were visually inspected and do not remove content.
The full build ledger is in `COMPILE_REPORT.md`.
