# HCS-C29 methodology blueprint

## Research paradigm

**Selected:** theorem-driven exact computational mathematics.

The primary question is an invariant algebraic/analytic statement, not an
empirical association.  Exact proofs determine the claim; enumeration is a
certificate and mutation-test layer rather than the logical basis.

## Method

**Type:** mixed theoretical and exact computational verification.

**Specific method:** source-locked groupoid construction, free-word
reduction, exact integral matrix products, fixed-length finite-Weil character
limits and independent trace-moment replay.

The method answers the question directly: a single primitive reduced kernel
word proves nonconstancy, while the natural-extension control prevents a
semantic false positive.

## Data strategy

Only frozen repository artifacts are used.

| Input | SHA-256 | Role |
|---|---|---|
| `agy_metaplectic_transfer_obstruction/results/c25_certificate.json` | `a35cee22714abbb9dc9aadcc165720d1ff77aff3b7f29071f53a1b451760bd12` | seven-state graph, edge matrices, frames and decoder |
| `agy_metaplectic_transfer_obstruction/THEOREM_PACKAGE.md` | `e1835d63bef914b355ceb4f64acc9043d11a842e9f4e59c7573c63ff66d03702` | fixed-start injectivity and positive-monoid freeness |
| `agy_holomorphic_slice_obstruction/results/c26_certificate.json` | `1c0289b9b47e65e0603ea001be7cce263aea13d58c66e4609eac88edf8f7ce4a` | frozen C26 branches and bridge matrices |
| `agy_holomorphic_slice_obstruction/THEOREM_PACKAGE.md` | `4e882cbc332711b4cd2f98e9530f89268c8fcf1712eb150aacfee968dcf50495` | scalar trace-class operator and chronology |
| `agy_prime_direct_sum_determinant/results/c28_certificate.json` | `98b9ed10433f5cc7eb56aa04f397caa1ebfbc03acc904552618bd06f30370a1e` | normalized finite-Weil character limit |
| `agy_prime_direct_sum_determinant/THEOREM_PACKAGE.md` | `3de68629b3c59c958683d79d96fc90fde901efd878896d192595370d02df8a4c` | exact scope and determinant normalization |

There is no Riemann-zero table, prime fitting or floating-point discovery
input.

## Analytical framework

1. **Semantic control.** Construct the regular group-von-Neumann twist of the
   positive C26 operator and prove that the natural extension retains the
   same positive periodic products.
2. **Object change.** Form the symmetric double of either the C25 edge graph
   or the selected C26 return rose.  Attach `g_e^-1` to a formal reverse arrow
   and forbid immediate reversal.
3. **Exact kernel witnesses.** Prove the two length-six C25 edge relations and
   the length-24 C26 branch relation by exact integer matrix multiplication
   and free/cyclic reduction.
4. **Trace theorem.** Define the finite-Weil non-backtracking operator and
   expand each normalized trace moment without reordering chronology.
5. **Limit theorem.** Use the C28 pointwise character limit, finite path count
   at each moment and a prime-independent operator-norm bound to obtain local
   uniform convergence of `exp[p^-2 Log_0 det(I-uB_p)]`.
6. **Certification.** An exact producer freezes the witnesses and a bounded
   identity-holonomy census.  An independent checker reimplements matrix
   arithmetic and rejects rehashed semantic mutations.

## Controls and falsifiers

| Gate | Expected result | Falsifier |
|---|---|---|
| Positive periodic-product control | all nonempty regular-group traces vanish, and natural extension preserves the defining positive words | any legal positive AGY word has identity matrix |
| Backtracking-allowed symmetric graph | artificial length-two identities appear | absence indicates inverse convention bug |
| Non-backtracking symmetric graph | explicit primitive identity cycles survive | any adjacent/cyclic inverse pair or nonidentity product |
| Gauge change | closed identity status is invariant | a vertex-frame change alters the witness verdict |
| C26 branch relation | free-reduced `A,B,C` word has product identity | cancellation, wrong chronology or matrix mismatch |
| Repetition | use `Theta_p(g_C^r)` exactly | substitution by `Theta_p(g_C)^r` |
| Normalized determinant | common `Log_0` disc and nonconstant limit | prime-dependent branch/disc or coefficient cancellation |

Chronological averaging, total transition matrices and fitted edge weights are
forbidden.

## Validity criteria

| Criterion | Strategy |
|---|---|
| Construct validity | Separate the genuine natural extension from the new symmetric groupoid in every artifact. |
| Internal validity | Exact integer products, state continuity, cyclic non-backtracking and primitive-word checks. |
| Gauge validity | Recompute after deterministic integral vertex-frame changes; closed holonomy may conjugate but identity cannot change. |
| Reproducibility | Source hashes, deterministic JSON, independent implementation and a read-only release manifest. |
| Claim validity | The theorem is a determinant-germ statement only; roof, nuclear inverse dynamics and Hilbert--Pólya claims remain open. |

## Limitations by design

- Formal reverse arrows are not forward AGY branches.
- Unit edge length is a combinatorial graph clock, not the Teichmüller/AGY
  return time.
- The C26 holomorphic contraction proof is one-sided.
- General twisted Ihara and group-trace determinant theory is prior art; the
  project-specific exact relation and source firewall are the intended delta.
- A nonconstant germ need not have discrete, arithmetic or Riemann-like zeros.

## Ethical considerations

No human subjects, personal data or dual-use operational content are involved.
All computations and AI-assisted drafting will be disclosed in the final
research package.

## Reporting standard and preregistration

- Reporting standard: proof/certificate claims--evidence matrix; no clinical
  reporting guideline applies.
- Preregistration: yes, in-repository freeze of source hashes, conventions,
  gates, mutations and stopping rules before Phase-2 code.
- IRB: not applicable.

## Phase-2 stop rule

Do not extend the word or prime cutoff once the exact nonconstant germ is
certified.  The only authorized subsequent large gate is an intrinsic roof
plus a two-sided trace theorem.  Failure there triggers a system-level pivot
to a genuine local-field oscillator/theta architecture.
