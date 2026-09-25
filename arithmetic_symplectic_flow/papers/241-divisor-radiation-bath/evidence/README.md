# Evidence — ANG-20260918-DRB01

**Paper:** `241-divisor-radiation-bath`  
**Object version:** candidate card version 1, frozen before proof on 2026-09-18.  
**Status:** `ADVANCE — PRIME-ONLY FULL-FIELD PACKETS; PHYSICAL LOGARITHMIC CLOCK; NATURALNESS OPEN`.  
**Gates:** `T0 ESTABLISHED; T1 ENGINEERING POSITIVE / NATURALNESS OPEN; T2 ESTABLISHED; T3 NOT SUPPLIED`.  
**Formal Route coordinates:** `UNASSIGNED`. **Route B:** `NOT INVOKED`.  
**Independent mathematical review:** Separate raw-card derivation and full
written readback completed; see the [actual review record](review.md).

## Exact inputs and method

The only mathematical inputs are the complete
[candidate card](../candidate-card.md): every integer \(n\ge2\), every
channel \(d=1,\ldots,n-1\), the displayed divisibility incidence,
\(c_n=1+n^{-2}\), \(W(q)=4q^2/(1+q^2)^2\), the full weighted
Hilbert field, \(f=e^{-\omega}\), \(g=\omega e^{-\omega}\), the
completed-square Hamiltonian, full energy one, and actual time.

The [paper](../paper.md) gives these exact proof stages:

1. Global Lipschitz mild evolution for each fixed full integer component.
2. Strong-domain energy cancellation, then dense initial frequency cutoffs
   and continuous-energy passage to every mild state.
3. Bounded frequency projections of an arbitrary periodic mild field,
   Bochner temporal harmonics, and the nonintegrable resonant pole.
4. Constant-oscillator, stationary and inactive-field cases, followed by
   every scalar energy-one branch.
5. Least-period/repetition proof and a direct evaluation of the
   rational-well time integral with uniform error bounds.

No simulation, numerical experiment, orbit table, prime table, spectral
approximation, fitted input or precision-dependent evidence was used.
Frequency cutoffs in the proofs do not truncate the candidate: initial
strong approximants evolve under the full equations, and the harmonic
identity is passed to the entire continuous frequency axis.

## Controls and scope limits

The paper accounts for prime label 2, prime-power label 4, mixed label 6,
all inactive channels and every stationary configuration. Separate
comparators remove all incidences, replace them by arbitrary Boolean
incidence, make the barrier constant, remove the barrier excess, or change
the fixed energy. They expose the engineering and PROVES_TOO_MUCH boundary.
They never change the main candidate's frozen definitions.

The exact same physical time is used for the full action, scalar integral,
least period and repetitions. No outgoing condition or quotient is used.
No radiation-decay, scattering, stability, analytic-product, trace or
quantum conclusion is part of the evidence.

## Work and review provenance

The authoring agent supplied the original proposal and wrote the full
proof package. A child agent separately derived the bounded periodic
classification from the frozen card as author-assisting mathematical work;
the root also checked the global-owner strategy from the raw card. These
are disclosed shared-task author checks, not peer review. The root owns
the separate independent-review assignment and its recorded evidence.

The bounded local collision scout searched package names, README files
and candidate cards for continuum-field and divisor-channel mechanisms.
Its nearest controls were 171, 182, 236, 237 and 239. This is not a
literature novelty claim; no external literature search was performed.

## Reproducibility and document checks

The mathematical results are reproduced by the proofs themselves, not by
a runnable numerical program. The package paths to check are
`paper.md`, `candidate-card.md`, `claim-ledger.md`, `README.md` and this
evidence record. Required document checks are relative Markdown link
resolution, common candidate identity, consistent gate/status boundaries,
and unchanged version-one definitions before the appended result.

Document checks executed on 2026-09-18 with an inline Perl reader using
`File::Basename`, `File::Spec` and `Digest::SHA`. Inputs were exactly the
five package files listed above. The check extracted relative Markdown
targets, verified target files and the used heading anchors, required the
same candidate ID, exact status and gate strings in every file, and hashed
the candidate-card prefix preceding its appended result. Actual output:

```text
Frozen prefix SHA-256: d6b6c5ac903afea7f316ea24c776ba94b521efe7012a3e3a887be858895009e3
Checked 5 files; 31 local links/anchors; 0 errors.
```

A scoped `rg -n` readback of `PENDING`, status, gates and `T1.*CLOSED`
confirmed the shared strings and that independent review remained PENDING;
no `T1.*CLOSED` match was present. `git status --short --
papers/241-divisor-radiation-bath` reported the new untracked package;
no commit or staging was performed by its authoring agent. This receipt
adds no link, anchor or status change to the checked material. Clean links
establish navigation, not mathematical correctness or a review outcome.

The SHA-256 of the entire frozen card before appending its audit outcome was
`d6b6c5ac903afea7f316ea24c776ba94b521efe7012a3e3a887be858895009e3`,
observed with `sha256sum papers/241-divisor-radiation-bath/candidate-card.md`.
That version-one content is preserved as the prefix of the card; the result
below it does not revise any frozen definition.

## Root final integration receipt — 2026-09-18

At 14:10 UTC, root completed a read-only Node stdin check from the ASFS
workspace using fs, path and crypto. Inputs were the five standard files
of both 240 and 241, this package's evidence/review.md, readme.md and
papers/README.md. Each package file was checked for its exact ID/status,
explicit UNASSIGNED and NOT INVOKED strings, final LF and absence of CR
or other control bytes; all DRB01 files were checked for the exact gate
string. Code blocks and inline code were excluded when extracting links.
Relative Markdown file targets were resolved against the containing file;
HTTP(S), mailto and data links were skipped and fragment anchors stripped.
The two indexes were checked for both IDs and package links. The frozen
card prefix and final manuscript were hashed with SHA-256.

The first integration pass found only two missing explicit Route-state
strings in this evidence header; root added them without changing any
claim or definition. The subsequent actual result was:

```text
packageFiles=11; packageLinks=78; indexFiles=2; indexLinks=463; errors=[]
frozenPrefixHash=d6b6c5ac903afea7f316ea24c776ba94b521efe7012a3e3a887be858895009e3
paperHash=1fb542d9416e0d3bc12c242edb9e65d0448f4fa4dc607c4b676f086c386ebada
```

This final file-path pass complements the author's earlier used-anchor
check; it does not independently validate remote URLs or Markdown anchor
semantics. The separate technical reviewer confirmed the final manuscript
hash and verified in memory that reversing the geometry-cell and review-
metadata edits restored its original reviewed bytes. The proof was not
rerun for unchanged inputs.

The scoped command git diff --check -- readme.md papers/README.md exited 0
without diagnostics. Both new untracked packages were checked by explicit
file reads rather than treated as covered by that Git check. Other work
was preserved; no staging, commit, numerical run, PDF or publication was
performed. This receipt adds no links, gate changes or mathematical input;
document consistency and model review are not proof certificates.
