# Canonical result ledger used by the manuscript

Authority result root (read-only during writer stage):

`/root/autodl-tmp/hilbert-polya-structure/symbolic_dynamics/papers/45-isospectral-arithmetic-fiber-retractions/results`

## Artifact seals

| Artifact | SHA-256 |
|---|---|
| `SHA256SUMS.txt` | `2fae66ff866b63e7119fce7b86c928f589570572728cae942d758f4e599ad734` |
| `evaluator_a.json` | `ba3f374f1e65e3598c7d4e769144514e911f5be268ae36afc90000df5a5154da` |
| `evaluator_b.json` | `ac8226e8d9a726ebf78e753d66b19e200ba382a5ecdc926ff79a262c7c81a675` |
| `proof_auditor_p.json` | `1a62f35af5b7147599d23139231f17443c14970612ac115387a484b84b60ce4d` |
| `comparator_x.json` | `6a8404c802342e9ea37fc311ecb23492f2503fa7137258a46b416aafaaee12c5` |
| `evaluation_report.json` | `4c5efa633213cd6f056b550c562dbf9929b3a7145aae33149b482ecd3fec0b5b` |
| `mutation_outcomes.json` | `8042263d0ddd43b3b2c8c27737c10a053b422e1dfbf9667f292a4b5bba4f147b` |
| `integrity_audit.json` | `fef14966637e160367f545e7c6ee9f53399c6f3de3f6a01b74614ac3bff94c9b` |

Binding hashes:

- Experiment contract:
  `6ff3776a29b1211762b929782b556d0cae71a60ec97b102863059fc5bf302fbe`
- Infinite case set:
  `6401b141f7b46b0f7275ec124ec571542655b9874cfa9aa5c7123108577e8a84`
- Frozen preauthority input manifest:
  `4053f398c8318d09a821907ce421cb34a2adbe88efa2ac4dbfdc059e54d1e849`
- Integration contract:
  `32edd4caf36a388758a76af8e8b160543f7c5f08aabe72f2f2c9da601487957b`

## Exact envelopes

- Evaluator A: 21 finite records and zero infinite records.
- Evaluator B: 21 finite records and exactly 15 infinite certificates.
- Proof auditor P: exactly 15 per-case audits, no findings, overall PASS.
- Comparator X: seven finite case IDs, zero exact mismatches, zero interval
  mismatches, PASS.
- Evaluation report: C1 PASS, C2 PASS, B/P case-ID equality and owner-hash
  closure PASS.
- Mutation execution: 168 physical outcomes covering 75 registered
  mutations, zero survivors.
- Output transaction: exact eight-path namespace, manifest/path/containment
  checks PASS, forced-late identity verified, and second identical run made
  zero replacements.

## Finite cases

The seven comparator case IDs are:

1. `FIN-H2-M1-REAL`
2. `FIN-H2-M6-REAL`
3. `FIN-H2-M6-COMPLEX`
4. `FIN-H3-M12-REAL`
5. `FIN-H4-M8-COMPLEX`
6. `FIN-H6-M32-REAL`
7. `FIN-PRIMORIAL-H3-THREE-REGIMES`

The first six each have three precision/cutoff rows. Every finite block rank
is one, the two symbolic nonzero eigenvalues agree, every recorded power
residual is exactly zero, and all compared certified intervals overlap
within their registered widths.

The exact finite primorial rows are:

| `h` | `sigma` | cutoff `x` | maximizing label | primorial label | tie labels |
|---:|---:|---:|---:|---:|---|
| 3 | 2/3 | 100 | 36 | 36 | 36 |
| 3 | 1 | 1000 | 900 | 900 | 900 |
| 3 | 4/3 | 10000 | 900 | 900 | 6300, 900, 9900 |

The supercritical row has multiple ties in the finite objective; the
canonical `maximizer_label` and `primorial_label` are both exactly 900.

## Infinite certificates

The 15 B/P-closed cases cover:

- exact existence domains for both operators;
- the power-Schatten wall and modulo existence guard;
- legal trace and regularized determinant domains;
- both similarity iff statements;
- exact primorial optimizer and all three regimes;
- Tauberian strip, positive simple pole, residue, and asymptotic inversion;
- the two Weyl constants and mandatory `sigma=1` crossover;
- the commutator wall for `h>=3`, its separate `h=2` witness, and the
  exact `h=2` Hilbert--Schmidt Euler identity;
- the free-UFD clone as a negative control.

These artifacts are canonical evidence for implementation agreement and
proof closure. The manuscript's mathematical claims remain supported by the
proof, not by finite fitting or a numeric vote.

