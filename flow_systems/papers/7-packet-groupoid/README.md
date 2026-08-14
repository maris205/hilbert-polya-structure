# 7-packet-groupoid

Paper 7 asks whether Deninger's prime-period packets admit a canonical
measured/operator enrichment that owns a return trace and dynamical
determinant.  The answer for the frozen sources is sharply split: a useful
decomposable proxy can be constructed and audited, but it is not transported
from the arithmetic flow.

## Result

The source object intrinsically owns prime packets, repetitions `p^Z`, least
periods `log(p)`, and compact transverse packet structure.  A repaired
finite-kernel restriction of Morishita's map gives a continuous,
flow-anti-equivariant same-source topological map into the Connes--Consani
adelic space.  Every source circle over `p` maps onto the same adelic circle
`C_p`; transverse labels collapse, and a two-zero-coordinate certificate
proves that the map is not globally onto.  No audited source theorem
transports a transverse measure, von Neumann algebra, normal trace, trace
ideal, zero mode, or determinant.

On the explicitly selected proxy, Paper 7 proves:

- every positive finite central mass sequence defines a faithful normal
  semifinite trace, so packetwise Haar probability does not select relative
  masses across primes;
- for a nonzero positive-time test function, the global bounded smear is in
  the bounded `L1(tau_m)` ideal exactly when `sum_p m_p log(p)` converges;
  unit masses fail this gate;
- the separately defined positive-time return ledger is an exact locally
  finite Radon measure with primitive/repetition support `r log(p)`, but it is
  not a global normal trace value outside that ideal;
- the zero-mode family `K_s=direct_sum_p p^(-s)P_(0,p)` is bounded
  `L1(tau)` exactly on its proved domain and, for unit masses on `Re(s)>1`,
  gives the branch-fixed principal trace-log identity
  `D_tau^pr(s)=product_p(1-p^(-s))`;
- that exact scalar is base-blind and compiles arbitrary locally finite clock
  lists, so it is not a primitive-orbit Ruelle determinant, a source-owned
  arithmetic normalization, or Hilbert--Pólya evidence.

The four typed Route-A records are therefore all
`ROUTE_A_EXPLORATORY`:

| Record | Exact tuple |
|---|---|
| `DEN-WITT-Z-FIN` | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` |
| `DEN-WITT-PACKET-DECOMP-MASS-FAM` | `(A0_WEAK_ARITHMETIC_RELATION, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` |
| `DEN-WITT-PACKET-DECOMP-RETURN-DIST-M` | `(A0_WEAK_ARITHMETIC_RELATION, A1_PASS_ANALYTIC, A2_FAIL, A3_FAIL, A4_FAIL)` |
| `DEN-WITT-PACKET-DECOMP-K0-M1` | `(A0_WEAK_ARITHMETIC_RELATION, A1_FAIL, A2_ANALYTIC_DETERMINANT, A3_FAIL, A4_FAIL)` |

The records cannot exchange coordinates.  Route B is not invoked and no
Route-B YAML exists.

Independent release gates are closed: citation/source integrity `ACCEPT`,
peer review `FINAL ACCEPT` with Critical/Major/Minor `0/0/0`, and release/
visual audit `PASS`.  The final PDF is 22 pages; its SHA-256 is
`4f0f9fbebf705e6b73c34fb66b01d4dda9d6ac37b7409f587bbefd8fecdcbd8d`.

## Main artifacts

- `paper/paper.pdf`: 22-page review-ready release.
- `paper/manuscript.tex` and `paper/references.bib`: bilingual manuscript and
  source/manifestation-locked bibliography.
- `notes/research_protocol.md`, `notes/candidate_lock.md`, and
  `notes/phase3_protocol_amendment.md`: registered question, typed objects,
  domains, and amendment.
- `notes/source_audit.md` and `notes/operator_source_audit.md`: source
  ownership and determinant-terminology audits.
- `notes/proof_audit.md`: proofs P7-1 through P7-8 and scoped P7-9 ownership
  certificate.
- `notes/route_audit.md`: independent four-record Route-A evaluation.
- `notes/sources/paper7_source_manifest.md`: canonical union of 15 primary
  PDFs and their read-integrity sidecars.
- `notes/citation_audit.md`, `notes/peer_review_round1.md`, and
  `notes/release_audit.md`: independent citation, mathematical, and release
  gates.
- `code/`, `experiments/`, and `results/`: target-free deterministic controls,
  nine CSV artifacts, and schema-v2 hash manifest.

## Reproduce

From the workspace root:

```bash
bash papers/7-packet-groupoid/experiments/reproduce.sh
```

The frozen package runs 21 tests, regenerates nine CSV artifacts (407 rows,
669 primes through 5000), verifies implementation and artifact hashes, and
performs two independent byte-for-byte regenerations.  It uses no Riemann
zeros, fitted weights, fitted clocks, random numbers, network data, or
external Python packages.

Build the release from `paper/` using the XeLaTeX/BibTeX sequence documented
in `paper/README.md`.  Exact release hashes and the disclosed 35 nonfatal
underfull-box diagnostics are recorded there.

The canonical source manifest records lawful reading endpoints and exact
hashes; it does not assert public redistribution rights for the retained
PDFs.  Check each publisher/author license before publishing those PDF bytes.
