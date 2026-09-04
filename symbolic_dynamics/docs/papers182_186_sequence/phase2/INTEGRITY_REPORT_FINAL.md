# Terminal integrity report — P182–P186

**Source audit:** 2026-09-03 UTC.  **Terminal close:** 2026-09-04 UTC.
**Mode:** post-revision, exact-byte,
registered-population verification.  **Internal verdict:**
`PASS_INTERNAL / ZERO_OPEN_INTEGRITY_ISSUES / OWNER_AMBER / HOLD_EXTERNAL`.

This is the terminal integrity report for the exact manuscript bytes bound
below.  It does not claim submission readiness, publication readiness,
ownership clearance, priority, novelty, freedom to operate, or permission to
circulate.  External release remains prohibited while `HOLD_EXTERNAL` is
active.  Any change to a bound `main.tex` or `references.bib` invalidates the
corresponding rows and requires a fresh check.

The verified denominators are deliberately bounded.  Semantic extraction
completeness is `not_machine_detectable`; the truth of an unregistered claim
is outside the denominator.  The five finite programs and all reviewer-owned
programs are exact falsification and proof-regression controls.  They are not
experiments, are not proofs, and do not create statistically independent error
processes.  The all-parameter claims stand or fall with the written proofs.

## Exact objects

| paper | `main.tex` SHA-256 | live PDF SHA-256 | current receipt relation |
|---:|---|---|---|
| P182 | `9d496bf69fc3d7426c1f95bb7bacdaf0ea0cd6c7e3b36c5d3c55f64236f088c7` | `880abab7db480447c0874e5da6434f7a1d0a8dfbe2ec0b2a23974b573023aa07` | live = Round 2 = Round 1 |
| P183 | `9ee13796fc2a69fd9d064c55d0adf1e9fad26d3811e29f767e38d548908e6678` | `6834170a0ee554a9f4c75040aad762326e24fa5a532e7987c57025be02bd235b` | live = Round 2 = Round 1 |
| P184 | `6f11630dfbb68ff3ac30e652130497b3c473a45869c968fb0679136ba2b8b44a` | `991e9eae521268083d5eabb02d5ff536a40eefe000aa970ce23d6c97ea8888ab` | live = Round 2 = Round 1 |
| P185 | `e17e073a15d839a3178bc5ed922227bd24cea41d4c6ceff4e6066090651da6f6` | `fcd6257debd3a3e8744571a390296fe02566cc6655957011778400582bea03c3` | live = Round 2 = accepted Round 1 |
| P186 | `e7f407c5200e2e308885d61bd1328c8e3d20f57e50f219ab5ad104609cee0394` | `449ddc9983cec9618e8a7cead63730d3ed29e1dbb5f36a630948eac3618f2b48` | live = Round 2 = accepted Round 1 |

The source audit was also performed against the five current
`references.bib`, `CLAIMS_EVIDENCE.md`, and `SOURCE_VERIFICATION.md` files.
The incorporated initial report has SHA-256
`62b6eefdbf962a061052ee7cb013513d0085d885eeef9130582233a5b510a8eb`;
the incorporated final originality audit has SHA-256
`306edb8b26ae7a192dcb632378a61e6663039f6b9a91152751e75e7d0910b619`.

## Verification summary

| surface | exact denominator | result | open integrity issues |
|---|---:|---|---:|
| bibliography entries | 15 | 15 VERIFIED | 0 |
| unique bibliography/citation keys | 15 / 15 | exact set equality | 0 orphan; 0 dangling |
| citation commands / key occurrences | 14 / 16 | every occurrence inspected in context | 0 |
| formal theorem/control claim groups | 32 | 32 located in manuscript proofs and control ledgers | 0 |
| cited-source scope groups | 15 | 15 context-aligned | 0 |
| total registered claim groups | 47 | 47 checked | 0 |
| external statistical/data surfaces | 0 | none reported | 0 |
| exact-control surfaces | 5 | present; bounded controls only | 0 |
| final originality sample | 61 of 116 distinct prose blocks | 52.6%; 64 query executions; 0 qualifying close/verbatim matches | 0 detected in sample |
| self-plagiarism | — | `NOT_CHECKED`: anonymous authors and no publication lists | not a clean result; outside issue count |

The final internal gate requires zero open integrity issue in the registered
populations.  That requirement is met on the exact bytes above: Critical 0,
Serious 0, Medium 0, Minor 0.  The explicit limitations and lifecycle holds
below are not silently converted into clean findings.

## Phase A — fresh reference and key audit

Semantic Scholar DOI lookup returned HTTP 429 in the recorded verification.
This is preserved as `S2_API_UNAVAILABLE`, not misreported as a negative
existence result.  The fallback was item-by-item publisher/DOI WebSearch plus
a fresh Crossref field comparison for all **14 DOI-bearing entries**.  The
one non-DOI entry, `Birkhoff1967`, was checked against the official AMS
Colloquium Publications volume record at
`https://bookstore.ams.org/COLL/25`.  Author, title, venue/book, volume,
issue, pages/article number, and the applicable publication-year convention
matched after the already-recorded P185 issue-number correction.

Two year conventions are retained explicitly rather than normalized into
false discrepancies:

- `Fayers2023` was published online in 2022 and belongs to the 2023 journal
  issue, volume 27, pages 297--328; the bibliography's issue-year convention
  is 2023.
- `Stanley2012` uses the Cambridge University Press second-edition **print
  year 2012** convention; this is the intended cited-edition year.

| paper | recomputed `references.bib` key set | recomputed unique body-citation key set | result |
|---:|---|---|---|
| P182 | `{Birkhoff1967, GoldmanRota1970, ChajdaLanger2019, Hong2022, GasanovaNicklasson2024}` | `{Birkhoff1967, GoldmanRota1970, ChajdaLanger2019, Hong2022, GasanovaNicklasson2024}` | equal |
| P183 | `{Brown2000, YinZhu2016, CirkovicEtAl2023}` | `{Brown2000, YinZhu2016, CirkovicEtAl2023}` | equal |
| P184 | `{XuZou2009, AnashinKhrennikov2009, KonyaginEtAl2016}` | `{XuZou2009, AnashinKhrennikov2009, KonyaginEtAl2016}` | equal |
| P185 | `{MansourVajnovszki2013, Wachs1994}` | `{MansourVajnovszki2013, Wachs1994}` | equal |
| P186 | `{Stanley2012, Fayers2023}` | `{Stanley2012, Fayers2023}` | equal |

Across the batch, both unions have cardinality 15 and are identical.  There
are no duplicate keys across papers, orphan bibliography entries, dangling
citations, placeholder keys, or DOI misdirection observed in the registered
population.

### Reference-by-reference existence/metadata result

| key | primary verification surface | verdict |
|---|---|---|
| `Birkhoff1967` | official AMS book record, Colloquium Publications 25, third edition (1967) | VERIFIED |
| `GoldmanRota1970` | `https://doi.org/10.1002/sapm1970493239` + Crossref/publisher fields | VERIFIED |
| `ChajdaLanger2019` | `https://doi.org/10.1007/s00500-019-03866-y` + Crossref/publisher fields | VERIFIED |
| `Hong2022` | `https://doi.org/10.1016/j.aam.2022.102362` + Crossref/publisher fields | VERIFIED |
| `GasanovaNicklasson2024` | `https://doi.org/10.1007/s10801-023-01294-8` + Crossref/publisher fields | VERIFIED |
| `Brown2000` | `https://doi.org/10.1023/A:1007822931408` + Crossref/publisher fields; arXiv `math/0006145` | VERIFIED |
| `YinZhu2016` | `https://doi.org/10.1016/j.physa.2015.12.008` + Crossref/publisher fields; arXiv `1412.2187` | VERIFIED |
| `CirkovicEtAl2023` | `https://doi.org/10.1093/comnet/cnad031` + Crossref/publisher fields; arXiv `2201.03769` | VERIFIED |
| `XuZou2009` | `https://doi.org/10.1016/j.jalgebra.2008.09.029` + Crossref/publisher fields; arXiv `0810.3164` | VERIFIED |
| `AnashinKhrennikov2009` | `https://doi.org/10.1515/9783110203011` + Crossref/publisher fields | VERIFIED |
| `KonyaginEtAl2016` | `https://doi.org/10.1016/j.jctb.2015.07.003` + Crossref/publisher fields; arXiv `1307.2718` | VERIFIED |
| `MansourVajnovszki2013` | `https://doi.org/10.1016/j.ipl.2013.05.008` + Crossref/publisher fields; corrected issue 17 | VERIFIED |
| `Wachs1994` | `https://doi.org/10.1016/0097-3165(94)90117-1` + Crossref/publisher fields | VERIFIED |
| `Stanley2012` | `https://doi.org/10.1017/CBO9781139058520` + Cambridge second-edition record; print-2012 convention | VERIFIED |
| `Fayers2023` | `https://doi.org/10.1007/s00026-022-00577-4` + Springer/Crossref; online-2022/issue-2023 convention | VERIFIED |

## Phase B — every citation context

All 14 citation commands and all 16 citation-key occurrences were read in
their current sentence-level context.  The one repeated key is
`ChajdaLanger2019`, used once for finite-subspace enumeration and once for the
standard complement count.  No citation supplies evidence for the novelty or
ownership of a selected map.

| paper / source line | key | exact role assigned by the sentence | context verdict |
|---|---|---|---|
| P182:71 | `Birkhoff1967` | lattice polynomials and absorption | ALIGNED; classical background |
| P182:72 | `Hong2022` | meet-of-covers pop map on Tamari lattices as a different operator | ALIGNED; adjacent-work boundary |
| P182:74 | `GasanovaNicklasson2024` | meet--join sorting relations in Hibi-type algebras | ALIGNED; adjacent-work boundary |
| P182:80 | `GoldmanRota1970` | Gaussian coefficients and finite-subspace enumeration | ALIGNED; standard enumeration |
| P182:80 | `ChajdaLanger2019` | finite-subspace enumeration | ALIGNED; standard enumeration |
| P182:258 | `ChajdaLanger2019` | `q^{a(k-a)}` complements of a fixed subspace | ALIGNED; standard complement count |
| P183:73 | `YinZhu2016` | reciprocity equilibrium ensembles in directed networks | ALIGNED; background, not the literal chain |
| P183:75 | `CirkovicEtAl2023` | growing preferential-attachment model with reciprocal edges | ALIGNED; contrast class |
| P183:78 | `Brown2000` | Markov chains generated by finite semigroups | ALIGNED; general framework |
| P184:69 | `XuZou2009` | linear dynamics over finite rings | ALIGNED; broad background |
| P184:69 | `AnashinKhrennikov2009` | algebraic and p-adic finite-state dynamics | ALIGNED; broad background |
| P184:70 | `KonyaginEtAl2016` | functional graphs of polynomial maps over finite fields | ALIGNED; contrast class |
| P185:73 | `Wachs1994` | restricted-growth functions and set-partition encodings | ALIGNED; classical background |
| P185:75 | `MansourVajnovszki2013` | prefix-statistic restricted growth words and Gray-code generation | ALIGNED; adjacent interface |
| P186:71 | `Stanley2012` | strict/weak sequence shift and stars-and-bars identities | ALIGNED; classical background |
| P186:73 | `Fayers2023` | beta sets in core-partition theory | ALIGNED; example context |

Each manuscript immediately limits or subtracts the credited role.  None of
the contexts cherry-picks quantitative data, transfers a cited theorem to a
different hypothesis class, or attributes the paper's selected literal map,
functional graph, or fibre atlas to the source.

## Phases C and E — data, controls, and registered claims

There are no externally sourced datasets, empirical statistics, experiments,
human-subject records, or empirical figures.  Numerical examples and control
tables are exact evaluations of displayed formulas and finite state-space
enumerations.  Consequently the external statistical/data denominator is
zero; this does not turn the controls into experimental evidence.

The claim-ledger denominator was recomputed from the current five
`CLAIMS_EVIDENCE.md` files rather than copied from the initial report:

| paper | ledger rows | explicit exclusions | formal theorem/control denominator |
|---:|---:|---:|---:|
| P182 | 8 | 1: C8 says the owner-search non-hit is **not claimed** | 7 |
| P183 | 6 | 0 | 6 |
| P184 | 6 | 0 | 6 |
| P185 | 6 | 0 | 6 |
| P186 | 7 | 0 | 7 |
| **total** | **33** | **1** | **32** |

All 32 retained rows have an exact theorem/lemma/corollary/proposition or
declaration location and a finite-control location where applicable.  Adding
the 15 separately audited cited-source scope groups yields the registered
final denominator **47/47**.  This is a semantic grouping audit, not a
mechanical proof that all substantive statements were extracted.  Semantic
extraction completeness remains exactly `not_machine_detectable`.

The controls may catch finite counterexamples and transcription regressions;
they cannot certify the all-parameter proofs.  Likewise, process separation
between author and reviewer controls documents provenance separation, not an
independent-error guarantee.

## Phase D — final heuristic originality audit

The final audit checked **61 distinct manuscript-body prose blocks out of
116**, or **52.6%**, using **64 query executions**.  It included every block
modified by Review A.  Three repeat queries were deliberate: one additional
P183 history-count formulation and post-repair rechecks of the P185 and P186
abstracts.  The recorded result is 0 qualifying `CLOSE_MATCH` and 0
`VERBATIM` match among the inspected public-Web results.

This is a bounded heuristic screen, not Turnitin, iThenticate, or a
professional plagiarism certificate.  It cannot inspect the unsampled 55
blocks, closed corpora, translated reuse, or matches that public search did
not surface.  A non-hit is not proof of originality, authorship, novelty,
priority, ownership, or freedom to operate.  Author-specific self-plagiarism
remains `NOT_CHECKED` because the papers are anonymous and no author
publication list was supplied; it must not be relabelled as clean.

## Revision and Review-A closure

Review A was process-separated from each paper's author and read the frozen
Round-0 artifacts without editing the paper directories.  Its controls are
not described as independent replications.

| paper | initial C/M/m | requested change | exact closure |
|---:|---:|---|---|
| P182 | 0/0/0 | none | byte-identical Round-1 receipt; no open Review-A item |
| P183 | 0/0/0 | none | byte-identical Round-1 receipt; no open Review-A item |
| P184 | 0/0/0 | none | byte-identical Round-1 receipt; no open Review-A item |
| P185 | 0/0/1 | P185-A-MI-01: qualify the transient image/CDF range; state `t=0`, `t>=n-1`, and the `t=n-1` empty-product convention | accepted on Round-1 source/PDF hashes; reviewer replay 2,104,528 assertions; 0 new findings |
| P186 | 0/0/2 | P186-A-MI-01: a gap survives exactly when `g>t`; P186-A-MI-02: qualify the unique deepest state by `n>=2` | both accepted on Round-1 source/PDF hashes; reviewer replay 12,106,438 assertions; 0 new findings |

The P185 and P186 edits are claim-boundary repairs, not new theorem content.
The final originality sample re-opened both changed abstract blocks.  Review A
reports zero open Critical/Major/Minor findings after acceptance.

The pre-freeze integrity repair to `MansourVajnovszki2013` (issue 16 to issue
17) is also closed.  The pre-freeze P182 malformed exponent and P186 stray
summation comma were corrected and rebuilt before Round 0; neither remains an
open source-rendering issue.

## Final issue and boundary ledger

### Open integrity issues

| severity | count |
|---|---:|
| Critical | 0 |
| Serious | 0 |
| Medium | 0 |
| Minor | 0 |

The internal integrity decision is therefore `PASS_INTERNAL` for the exact
registered populations and bytes in this report.  Zero open integrity issues
is a required invariant: a later bibliographic mismatch, dangling/orphan key,
claim-context distortion, unresolved revision finding, or changed bound file
reopens the gate.

### Non-clean limitations and lifecycle controls

- Semantic claim-extraction completeness: `not_machine_detectable`.
- Self-plagiarism: `NOT_CHECKED`.
- Semantic Scholar path: `S2_API_UNAVAILABLE`; publisher/DOI WebSearch,
  14-DOI Crossref comparison, and the official AMS book record supplied the
  recorded fallback.
- Originality and owner searches: bounded non-hits only; they do **not**
  establish novelty, priority, ownership clearance, or freedom to operate.
- Exact programs: controls, not experiments and not proofs.
- Reviewer provenance: process-separated, not an independent-error claim.
- Ownership/release state: `OWNER_AMBER / HOLD_EXTERNAL`.

This terminal integrity report closes no owner gate and authorizes no external
action.  It remains an internal, hash-bound audit record only.
