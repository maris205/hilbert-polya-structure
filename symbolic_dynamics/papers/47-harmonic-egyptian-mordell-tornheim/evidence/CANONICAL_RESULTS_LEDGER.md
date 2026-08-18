# P47 canonical State-A writer ledger

Status: `PASS / FINITE IMPLEMENTATION EVIDENCE ONLY`.

- protected 91-node manifest SHA-256: `30a79c4be4bc9b9333cb2a9f809d2039430cebc86686a054765734a782eea473`;
- writer canonical summary SHA-256: `45185ea8750dec4557b055f0381137076df5d1615c51c482fa96e623f8ed1d7f`;
- State-A output tree SHA-256: `328527680d533e34ce3aabc17f2cf5688759b0674b7fc8740d0c2df332b64c42`;
- State-A result-ledger SHA-256: `dba161719ef85dee433a13aa14505ab6b0f5ff0fef8c627ea39ddb4bf81bfe47`;
- direct evaluator SHA-256: `43cb20df0d6b62d5e5bde0f083597e5599a56e5ddc85c7705b5c5f429a0442f1`;
- parameter evaluator SHA-256: `653646ba9fb3f5299dae2b4709ec9b2f11b7304a427ad8b8ea5e493be73db86a`;
- exact comparison SHA-256: `e36e0a5c37029277fe16bc389c0582196be96cd846a3a4a018b83d5454d88aa0`.

## Complete support cutoffs

| N | Ordered edges | Loops |
|---:|---:|---:|
| 16 | 16 | 8 |
| 32 | 40 | 16 |
| 64 | 96 | 32 |
| 128 | 228 | 64 |

## Exact comparison key set

- `based_closed_walks`: `PASS`
- `coprime_coordinate_bijection`: `PASS`
- `endpoint_and_complex_phase_controls`: `PASS`
- `exact_trace_powers_1_through_5`: `PASS`
- `finite_evidence_class`: `PASS`
- `first_trace_even_harmonic`: `PASS`
- `full_divisor_rows`: `PASS`
- `literal_matrices`: `PASS`
- `negative_principal_minor`: `PASS`
- `ordered_support_quotients_loops`: `PASS`
- `rectangular_primitive_mt_gcd_extraction`: `PASS`
- `second_trace_termwise_finite_cutoff`: `PASS`

## N=128 exact rational trace controls

### s=2

- `Tr A_N`: `41409901935572392721815151397221689468404267553321859/101654908017905176701346636040340858705380733523968000`
- `Tr A_N^2`: `262961558380597053013440468024388279046378647597875763915765670634418385662079156063587740520340462244111049/3473278220054389510808841367424280307069018657614718322827263349301414109567121655843882011353572966400000000`

### s=4

- `Tr A_N`: `192232094350895361567196017232646564052164493824161472995573615475942480163461782784523151239008597093761747/2841773089135409599752688391528956614874651628957496809585942740337520635100372263872267100198377881600000000`
- `Tr A_N^2`: `1283889780198035396929599000986211044572490125072626453615573695206488196972177735453961195175899622795295103607495838061110892916863429622882321213557275813002767475274507153249558015716077571119672241785363163517867/325718863035413081577675250375050272587086297503365524846434937240042069451329962987339366461309662006709565036912331079156668766790797739648027968878390103504328765653236462599579198102214990960179281920000000000000000`

## Adversarial and provenance controls

- theorem/governance: 39 instances, 60 consumer invocations;
- expanded nested: 35 instances, 48 consumer invocations;
- frozen external-auditor: 15 instances;
- survivors across these suites: 0;
- Route: `ROUTE_A_REJECTED`, Route B invocation allowed = `false`.

## Interpretation boundary

These records establish finite exact agreement and artifact integrity.  They do not establish the infinite operator theorem, external novelty, or a spectral target.
