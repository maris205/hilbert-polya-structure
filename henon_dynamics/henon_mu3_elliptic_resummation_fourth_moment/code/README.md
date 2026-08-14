# HCS-C50 exact code

`c50_producer.py` recomputes the exact group identities, standard-representation
idempotents, 21 base-field curve/factor controls, four extension-field Newton
controls, characteristic-zero Singular basis, selected literal eight-step
chronology controls, all eleven fourth-moment ledger identities, Chern/Betti
numbers, and the twelve p=181 bad-reduction points.

`c50_checker.py` is independent of the producer.  It uses its own point-count,
matrix, Chern-series, source-ordered chronology, reverse bad-point enumeration,
and Singular wrapper.  A frozen full-payload digest and recursive exact-key
schema make every unconsumed leaf and exact JSON type fail closed.

Run the frozen verification with `code/run_c50.sh`.  The only result-refresh
mode is `code/run_c50.sh --refresh-results --refresh-manifest`; production,
independent checking, and all mutations finish before either frozen result is
replaced.  `--refresh-manifest` alone refreshes the full-project manifest after
an authorized documentation-only change; the inventory includes root research
documents, Route-A root/archive files, paper sources/PDF/compilation report,
code, and results while excluding volatile LaTeX build files.
