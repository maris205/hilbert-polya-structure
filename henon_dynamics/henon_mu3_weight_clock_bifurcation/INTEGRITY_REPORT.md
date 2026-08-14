# HCS-C51 integrity report

Status: **document/PDF and release-candidate machine audits passed; final manifest/commit freeze pending**

## Mathematical red team

- The radial decomposition was independently attacked and corrected to use
  four strata.  A direction with
  \(\mathcal C_n\ne0,\mathcal Q_{n,\rho}=0\) has no nonzero root.
- The clock index is uniformly \(j\ge1\); the leading term is \(j=1\).
- The total-rank formula is conditional on smoothness and is applied to the
  Hénon source only at \(n=2,3,4\).
- The \(n=3\) Fermat refinement is twenty primitive Tate lines plus a
  rank-two non-Tate Jacobi packet, with one additional trivial line in
  \(E_3\).
- The compatible-system no-go is restricted to a semisimple direct
  source-native \(K\)-packet retaining the \(E_n/O_n\) weight decomposition
  and unchanged split-prime trace.
- Restriction of scalars removes the bare \(n=4\) parity obstruction and is
  not claimed to be excluded.
- The \(n=3,4\) odd functional equations remain conjectural.

## Source audit

Primary locators were checked for Deligne purity, SGA 2 weak Lefschetz,
Griffiths' residue/Jacobian-ring method, Hirzebruch--Riemann--Roch, Fermat
Jacobi sums, elliptic modularity, automorphic functional equations, and
regularized determinant background.  SOURCE_AUDIT.md records the precise
claim carried by each source and the associated overclaim firewall.

## Machine scope

The release-candidate code lane reports:

- 15/15 independent semantic gates passing;
- 43/43 isolated mutation tests passing;
- canonical \(j\ge1\) indexing;
- exact rational and type checks;
- conditional-family and direct-\(K\) scope gates;
- certificate SHA-256
  `daffc0070d06258d3a4c8f5613c9d54a816eb2203be41aa045dbbe05c0e3d593`;
- certificate payload digest
  `2fdfc4fb2559d4cc9b253d978b8074bf57c49888ce2ff4d29545b127e9af95c1`;
- independent-check SHA-256
  `7675d1bfc0ce4451a2c077c707242630d5784a746ff3f90971996cb049bbcfed`.

The frozen artifact status is `RELEASE_CANDIDATE`.  The producer and checker
replay finite symbolic identities and schema semantics.  They do not
independently reprove Deligne purity, weak Lefschetz, modularity,
Hirzebruch--Riemann--Roch, or the full prose proof.

## Document audit

- Root mathematical Markdown was regenerated with literal TeX backslashes;
  literal carriage-return corruption is forbidden.
- Inline mathematical expressions use explicit Markdown TeX delimiters.
- Claims distinguish proved, inherited, conditional, expected, and open.
- The projector gate requires algebraicity over \(K\) and
  \(\ell\)-compatible realizations.
- Root/archive Route-A YAML files are byte-identical and schema-parseable.

## Paper/PDF audit

The preliminary manuscript freeze passed.  `paper/COMPILATION_REPORT.md`
records:

- clean rebuild exit status zero;
- 15 pages, SHA-256
  `7957f38aa779a3c2708e1a5bccf0b83d6759d6889412b5175069e5afa13ff89b`,
  and 384062 bytes;
- zero undefined citations/references and zero box warnings;
- embedded fonts and successful text extraction;
- visual inspection of the title/abstract, C52/Route-A, and bibliography
  pages.

## Release blockers

1. Refresh the full-project manifest and run the default runner.
2. Backfill the implementation commit and refreeze provenance.

No claim of release readiness is made before these steps pass.
