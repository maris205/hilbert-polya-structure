# SD-C23 experiment artifact schema

All tabular artifacts are UTF-8 CSV with a header, LF line endings, deterministic row order, and no runtime metadata. JSON artifacts are UTF-8, sorted by key, indented by two spaces, and newline terminated.

| Artifact | Rows | Exactness role |
|---|---:|---|
| unweighted_trace_primitive.csv | 32 | integer rooted traces, Möbius primitive counts, necklace reconstruction |
| trace_cutoff_flags.csv | 128 | exact comparison of four finite cutoffs with $2r-1$ |
| confinement_certificates.csv | 32 | exact stabilization and extremal-cycle certificates |
| primitive_orbit_inventory.csv | 667 | explicit primitive directed rotation classes through length 16 |
| weighted_trace_ledger.csv | 48 | rational traces for $s=1,2,3$ and $r\le16$ |
| determinant_coefficients.csv | 51 | Newton and primitive-product coefficients through degree 16 |
| quotient_cycle_families.csv | 225 | explicit $q$-family cycles for $2\le d,q\le16$ |
| graph_controls.csv | 20 | full, spine, successor, and quotient-blacklist controls |
| weight_inventory_controls.csv | 64 | positive-weight persistence controls |
| trace_class_diagnostics.csv | 56 | finite row-nuclear prefixes at eight exponents and seven cutoffs |
| route_gate_summary.csv | 5 | one strict verdict row per Route-A layer |

summary.json records frozen counts and theorem labels. source_oracle_certificate.json records source-edge identities and the target-data firewall. analysis_summary.json records scientific gates and the Route tuple. test_summary.json records the declared and passed test counts. integrity_audit.json records schema, provenance, source-policy, scope, cache, and artifact gates. SHA256SUMS.txt hashes all authority code and result artifacts except itself.

Exact integers and rational numbers are serialized as decimal integers or numerator/denominator strings. Floating values are confined to trace-class prefix diagnostics and are not used to infer the sharp half-plane.
