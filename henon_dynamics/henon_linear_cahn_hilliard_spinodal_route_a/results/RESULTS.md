# C304 exact results

- Theorem domain: every finite \(d\ge1\), \(\kappa>0\),
  \(\alpha\in\mathbb R\).
- Evidence cases: 18; shell rows: 216; support probes: 6;
  \(\kappa=0\) rows: 3; boundary rows: 6.
- Audited evidence leaves: 1653.
- Independent checker: 1930 assertions.
- SymPy: 36 exact identities.
- Hostile mutations: 72/72 rejected.
- Byte replay: two isolated outputs equal the archive.

The evidence payload hash is stored inside
`c304_ch_evidence.json`; the physical file hash and final PDF/manifest hashes
are generated and checked by the release script and recorded in
`paper/COMPILE_REPORT.md`.

Headline conclusion: the whole linear periodic spinodal semigroup is
classified, including all represented fastest shells without using the
finite receipt cutoff as proof. Route A remains rejected.
