# Paper 47 exact integration report

**Candidate:** SD-C49  
**Evidence:** finite exact controls plus independently owned analytic certificates  
**Status:** PASS

## Independent support controls

| N | ordered edges | loops |
|---:|---:|---:|
| 16 | 16 | 8 |
| 32 | 40 | 16 |
| 64 | 96 | 32 |
| 128 | 228 | 64 |

D constructed support only by `(mn) % (m+n) == 0`. P constructed it only from coprime-scale triples and constructed complete rows separately from divisors of `m^2`. Exact row, matrix, quotient, loop, and based-walk projections agree.

## Exact traces at N=128

| s | Tr A_N | Tr A_N^2 |
|---:|---:|---:|
| 2 | 41409901935572392721815151397221689468404267553321859/101654908017905176701346636040340858705380733523968000 | 262961558380597053013440468024388279046378647597875763915765670634418385662079156063587740520340462244111049/3473278220054389510808841367424280307069018657614718322827263349301414109567121655843882011353572966400000000 |
| 4 | 192232094350895361567196017232646564052164493824161472995573615475942480163461782784523151239008597093761747/2841773089135409599752688391528956614874651628957496809585942740337520635100372263872267100198377881600000000 | 1283889780198035396929599000986211044572490125072626453615573695206488196972177735453961195175899622795295103607495838061110892916863429622882321213557275813002767475274507153249558015716077571119672241785363163517867/325718863035413081577675250375050272587086297503365524846434937240042069451329962987339366461309662006709565036912331079156668766790797739648027968878390103504328765653236462599579198102214990960179281920000000000000000 |

The finite second trace uses the termwise `(a,b)` cutoff `floor(N/((a+b)max(a,b)))`; no finite zeta factor was extracted. The rectangular primitive/full MT controls are a separate domain.

## Exact comparison checks

- `based_closed_walks`: PASS
- `coprime_coordinate_bijection`: PASS
- `endpoint_and_complex_phase_controls`: PASS
- `exact_trace_powers_1_through_5`: PASS
- `finite_evidence_class`: PASS
- `first_trace_even_harmonic`: PASS
- `full_divisor_rows`: PASS
- `literal_matrices`: PASS
- `negative_principal_minor`: PASS
- `ordered_support_quotients_loops`: PASS
- `rectangular_primitive_mt_gcd_extraction`: PASS
- `second_trace_termwise_finite_cutoff`: PASS

## Audits and adversarial controls

- theorem/governance mutations: 39 instances, 60 designated invocations, 0 survivors
- expanded nested-schema mutations: 35 instances, 48 designated invocations, 0 survivors
- frozen-auditor mutations: 15 instances, 0 survivors
- proof/source/type/independence/literature audits: PASS
- two full Route-v0.2 validators: byte-identical route SHA-256 and PASS

## Analytic and ownership boundary

The phase walls `0, 1/2, 1`, compactness, determinant domains, and infinite zeta/MT identities are proof-certificate claims, not numerical extrapolations. Classical Egyptian parameterization and Mordell--Tornheim theory receive zero novelty credit. `STOP_DUPLICATE` remains a live external publication disposition and is not a Route terminal.

Route A is rejected: graph cycles are not rational-prime primitives, no completed target divisor is supplied, and no fixed self-adjoint Hilbert--Polya lift is constructed.
