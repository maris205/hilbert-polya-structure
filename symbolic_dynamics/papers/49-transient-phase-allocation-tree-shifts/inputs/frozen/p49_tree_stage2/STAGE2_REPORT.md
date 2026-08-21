# Stage-2 proof/implementation bridge report

## Outcome

```text
INTERNAL_PROOF_PACKAGE_COMPLETE
DETERMINISTIC_VALIDATION_PASS
NO_NONTRANSIENT_EXTENSION_CLAIMED
HOLD_FOR_INDEPENDENT_STAGE2_AUDIT
```

The frozen complete cyclic-block and transient-feeder theorem spine has a
self-contained proof.  Internal computation found no counterexample in the
declared finite domains.  This is not a manuscript, source-priority finding,
or release authorization.

## Theorem disposition

| Claim | Status | Principal proof anchor |
|---|---|---|
| Equiprobable cylinder liminf formula | `PROVABLE AS STATED` | Lemma 1 in `PROOF_PACKAGE.md` |
| `dim_H T_C=min_j H_j(c)` | `PROVABLE AS STATED` | Lemmas 2--3 |
| Exact finite one-level composition maximum | `PROVABLE AS STATED` | Lemma 4 and Theorem 5 |
| Constant circular-convolution saturation iff | `PROVABLE AS STATED` | Lemma 6 and Theorem 7 |
| `p|d` universal sufficiency | `PROVABLE AS STATED` | Theorem 8 |
| `p|d` necessity | `PROVABLE AFTER WEAKENING / EXTRA ASSUMPTION` | Theorem 8, full nonzero Fourier support required |
| `p=2` even/odd closed forms | `PROVABLE AS STATED` | Theorem 9 |
| Exact `d^L` optimizer and convergence | `PROVABLE AS STATED` for the canonical unrestricted feeder | Theorem 10 |
| General non-transient strengthening | `NOT CURRENTLY JUSTIFIED` | Explicitly excluded |

At every finite `L`, saturation is governed by constant circular
convolution.  `p|d^L` is only a universal sufficient condition; its
necessity still requires the declared Fourier-support hypothesis.

## Deterministic validation result

Two consecutive successful reruns produced identical evidence hashes.
Each run completed

```text
73,517 exact assertions
```

with these principal counts:

| Control family | Count |
|---|---:|
| General `(d,p,a)` parameter cases | 360 |
| One-level weak-composition cases | 6,219 |
| `H(b)` versus direct convolution identities | 6,219 |
| Constant-convolution saturation equivalences | 6,219 |
| Exact component-prefix cross-implementation equalities | 13,302 |
| Exact feeder-prefix cross-implementation equalities | 12,438 |
| Residue-subsequence contraction comparisons | 4,734 |
| Actual recursive component integer counts | 816 |
| Actual recursive feeder integer counts | 1,086 |
| `p=2` closed-form cases | 175 |
| Exact `L`-level composition cases | 10,212 |
| Exact `L`-level denominator prefix checks | 10,212 |
| `L`-level optimizer problems | 36 |
| Balanced convergence families | 15 |
| Required mutation controls | 6 |

The largest recorded coefficient-vector residue error fell from `2/93` at
cycle index two to `2/24573` at cycle index six.  This convergence diagnostic
is not substituted for the proof.

## Canonical evidence hashes

| Evidence file | SHA-256 |
|---|---|
| `evidence/formula_enumeration.json` | `65d4d156e1ebbfe17aebdde7fc8e8970a10e49a56135a67a04d08240b8467fff` |
| `evidence/prefix_cylinder.json` | `e9f7ea0266cf4080caf77a3ae63a82ad45dbf99f4a53d01a96768e9ada753d07` |
| `evidence/level_l.json` | `cf8ae3ee10fd798d937bed725b6a55ad0635e5dcdfdb29fb0c1070f2290a63f9` |
| `evidence/mutation_controls.json` | `eb4a831b6b8b1197776a4bbe6a1aca8439bb34bce0fcba1a8dbbce9ff8f127f6` |
| `evidence/run_summary.json` | `cf92a6878b38bf3ef7baa4ba1e28b98ee88caf35912920cea249e5580102765e` |

The two independent engines have hashes recorded inside
`evidence/run_summary.json`, and its abstract-syntax check records
`no_cross_import=true`.  Candidate dimension forms are ordered by clearing
rational denominators and comparing exact integers; decimal values are
diagnostic only.

## Decisive negative controls

1. `p=4,d=2,a=(2,3,2,3),m=(1,1,0,0)` gives four identical shifted products
   `6` and four identical feeder residues `(log 2+log 3)/2`.  It refutes an
   unconditional “saturation iff `p|d`” statement.
2. Removing a single phase-block edge rejects the complete-block count.
3. Adding a return edge rejects the finite transient decomposition.
4. Removing a feeder target rejects the unrestricted composition set.
5. `d=1`, a zero phase size, and an incorrect composition total are rejected.
6. The four-state matrix in C7 has core dimension `log(2)/3` and full
   dimension `log(2)/2`, refuting an arbitrary Hausdorff max-SCC formula.

## Source-lock correction and firewall

The Stage-1 manifest SHA-256 is
`7fd51d53d077e3d7e0af905eda6bf2d15ee9aa64d6459bf3dcfa1dc282d97ec8`;
all 13 entries verified.  The arXiv v2 source tar and `main.tex` hashes were
independently reproduced and are recorded in `SOURCE_LOCK.md`.

The BLW risk is stated narrowly as a versioned arXiv-v2 text tension.  This
package does not claim that every current Wiley rendering contains both
sentences, does not infer an editorial correction, and imports neither
equality clause.  Exact level counts supply both sides of every dimension
formula proved here.

## Package hygiene and manifest policy

The package contains Markdown contracts/reports, Python validators, and
canonical JSON only.  It contains no symbolic link, bytecode cache, LaTeX
source, figure, installation artifact, release seal, repository operation,
or publication-candidate directory.

`SHA256SUMS.txt` lists every regular package file except itself.  Its own
SHA-256 is emitted by `verify_manifest.py`, avoiding a self-referential
entry.  Any file-set, hash, path-normalization, cache, symbolic-link, or
nonregular-entry mismatch is fatal.

## Honest stopping condition

No required internal task remains.  An independent auditor must now verify
the proof and reproduce the package before any scope decision.  The present
status is

```text
HOLD_FOR_INDEPENDENT_STAGE2_AUDIT
```
