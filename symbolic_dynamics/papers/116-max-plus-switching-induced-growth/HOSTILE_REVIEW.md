# Hostile-review resolution ledger

Status: **AUTHOR REPAIR COMPLETE / FRESH VERIFICATION PASS / EXTERNAL HOLD**.

This file records the disposition of the independent findings in
`HOSTILE_REVIEW_A.md` and `HOSTILE_REVIEW_B.md`. It is an author-side
resolution ledger, not a third review, final QA, novelty clearance, priority
decision, or release approval.

## Critical findings

| Finding | Disposition | Repair anchor |
|---|---|---|
| The manuscript falsely inferred “no reset word / no regeneration” from the rank of the generators. | **Accepted and repaired.** The false firewall was deleted. Proposition 2.2 proves that no length-one/two word resets and that exactly `ABA`, `ABB`, `BAA`, `BAB` reset at minimal length three. It lists their literal matrices and forced gaps `-3,0,0,3`. The P89 comparison now acknowledges shared reset/coupling structure and distinguishes only carrier, observable, and proof package. | `sections/2_generators.tex`; `sections/6_scope_controls.tex`; verifier lane `reset_words` |
| Page 5 printed the literal token `qquad` in the Perron-derivative display. | **Accepted and repaired.** The source uses `\qquad`. The fresh build gate includes PDF-text and visual inspection of the derivative display, because the old error was warning-silent. | `sections/4_limit_laws.tex`; settled build record below |

## Major mathematics and exposition findings

| Finding | Disposition | Repair anchor |
|---|---|---|
| “Exact word interval” lacked a construction of intermediate heights. | **Accepted and repaired.** Proposition 5.2 now states exact support `{n-2k: 0<=k<=floor(n/2)}` and constructs height `n-2k` with `(AA)^k` followed by an alternating suffix. | `sections/5_pressure.tex`, equation `exact-height-support`; verifier lane `word_support` |
| The full Gärtner--Ellis conclusion did not spell out its hypotheses. | **Accepted and repaired.** The proof now records existence, finiteness and differentiability on all of `R`, lower semicontinuity, empty effective-domain boundary (hence vacuous steepness), compact support/exponential tightness, and goodness of the Legendre transform. | `sections/5_pressure.tex` |
| The two routes were called independent end to end. | **Accepted and repaired.** They are now called complementary: the literal route supplies the finite reward kernel consumed by the spectral route. Only the Poisson and Perron variance calculations are described as independent after the kernel is fixed. | Introduction; Section 4; Section 6; support documents |
| The stationary-law title could be confused with the five-state literal-gap law, and “six possible values” could mean six distinct numbers. | **Accepted and repaired.** The title specifies the lumped projective chain and the table is described as six state--letter values. | `sections/4_limit_laws.tex` |
| Reachability of all five literal gaps should be exhibited. | **Accepted and repaired.** The proof names the empty word, `A`, `B`, `AB`, and `BA` as witnesses for `0,-2,2,3,-3`. | `sections/3_finite_law.tex` |
| Endpoint fluctuation and martingale-CLT invocation should be explicit. | **Accepted and repaired.** The endpoint normalization is written explicitly, and Hall--Heyde Theorem 3.2 is cited for the martingale CLT. | `sections/2_generators.tex`; `sections/4_limit_laws.tex`; `references.bib` |

## Owner and scope findings

| Finding | Disposition | Repair anchor |
|---|---|---|
| The finite projective-chain, coupling/memory-loss, random Lyapunov, switching, and Markov-jump engines were under-subtracted. | **Accepted and repaired.** The manuscript now explicitly assigns zero credit to general engines and cites Gaubert (1995), Mairesse (1997), Baccelli--Hong (2000), Blondel--Gaubert--Tsitsiklis (2000), Merlet's projective-semigroup work (2010), Goverde--Heidergott--Merlet (2011), van den Boom--De Schutter (2012), and Kordonis--Maragos--Papavassilopoulos (2018), alongside the pre-existing background owners. | Introduction; Section 6; `references.bib`; support owner ledgers |
| Pair-specific searching did not exhaust tropical equivalence classes. | **Accepted and made explicit.** No exhaustion is claimed under row/column scalings, permutations, transpose, or additive normalization; search absence is not treated as novelty evidence. | `sections/6_scope_controls.tex`; `CLAIMS_EVIDENCE.md`; `README.md` |
| Residual contribution prose remained too broad. | **Accepted and narrowed.** The residual is limited to this displayed pair's five literal gaps, reward table, rational drift/variance, cubic transfer/pressure relation, exact word extremes/support, and temperature constants. All general methods and terminology receive zero credit. | Introduction; Section 6; support documents |

## Verifier regression gate

The revised standard-library verifier adds exact assertions that:

- no word of length one or two has tropical rank one;
- exactly `ABA`, `ABB`, `BAA`, and `BAB` have rank one at length three;
- the four chronological products equal the four matrices in Proposition 2.2;
- both column differences give the stated reset gap, and literal actions give
  that constant gap on exact finite-input sentinels;
- exhaustive word histograms have exactly the parity-compatible support;
- each support height has an explicit `(AA)^k` plus alternating-suffix
  witness, and every interior biased law has the same full support.

The canonical assertion count and byte comparison are recorded in
`code/verify.out`, `CONTROL_RESULTS.md`, and `BUILD.md` after the fresh run.

## Release disposition

All mathematically valid repairs requested by the two hostile reviews have
been incorporated. This resolution does not convert a bounded owner search
into a novelty result and does not authorize circulation. Public posting,
submission, specialist contact, novelty, and priority remain **HOLD**.
