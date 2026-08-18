# Paper Plan — Paper 48

**Working title:** *Carry-Free Radix Operators: Exact Schatten Surfaces,
Binary Endpoint Pinching, and Weighted Cycle Traces*

**One-sentence contribution:** For every integer radix \(b\ge2\) and every
finite Schatten index \(q\ge1\), we classify the positive-integer carry-free
Dirichlet-weighted adjacency operator by the exact strict surface
\(\Re s>\max\{1,\log_b\|C_b\|_{S_q}\}\), including the binary endpoint repair
and the legal trace, determinant, and least-period ledgers.

**Format:** Anonymous mathematical article, 11pt A4; self-contained theorem
proofs in the main text, technical replays and validation details in appendices.

**Target length:** 16–20 main-text pages, including the abstract and all
planned floats, plus references and appendices.  Each section allocation
below is an occupancy budget that already includes its associated figure or
table and transition prose; the proof-bearing §§5–6 are not to be shortened
to absorb float drift.

**Date:** 2026-08-18

**Two independent gates:** `PLAN_READY` refers only to the manuscript
outline, claim/evidence map, and proof structure reviewed at this phase.  It
does not certify a protected authority tree and did not authorize writer
closure.  The later publication/closure gate was initially
`WAIT_PROTECTED_AUTHORITY`; it has since passed by exact live-manifest
injection and independent replay.  The resulting overlay remains separately
`HOLD_FOR_INDEPENDENT_WRITER_AUDIT`.

**Status:** `PLAN_READY` for manuscript planning and proof structure, as
recorded in `reviews/PLAN_RECHECK_FINAL.md`; writer closure status is
`HOLD_FOR_INDEPENDENT_WRITER_AUDIT`.

## Story and scope

The paper tells one story.  A one-digit compatibility matrix controls exact
unweighted radix-shell norms.  Dirichlet weights turn those norms into two
geometric ratios: a universal column wall at \(\sigma=1\) and a digit-norm
wall at \(\sigma=\log_b\kappa_{b,q}\).  Equality requires two different
pinching arguments because the binary same-shell block is exactly zero.  The
same ideal classification then fixes the legal trace and determinant domains,
while the positive-vertex convention fixes the trace and least-period ledger.

The manuscript does **not** claim novelty for carry criteria, Kummer or Lucas
congruences, finite Pascal/Boolean/disjointness matrices, digit Kronecker
products, or the explicit finite singular values.  It makes no priority claim,
no composite-radix Kummer claim, no unweighted Artin–Mazur-zeta claim, no
complex zero-free trace claim, and no Hilbert–Pólya or target-divisor claim.

## Claims–evidence matrix

The controlling detailed matrix is `CLAIMS_EVIDENCE.md`.  The main text uses
the following compressed map.

| Claim | Evidence in the manuscript | Independent/finite check | Location |
|---|---|---|---|
| Exact digit spectrum | covariance inverse and sine recurrence | overlapping A/B intervals | §3, App. A |
| Exact shell norms | digit permutation and tensor factorization | 420 shell envelopes | §4, App. B |
| Sharp \(S_q\) surface | block summation, column wall, pinching | four P certificates | §5, App. C |
| Binary bad-range repair | paired adjacent-shell compressions | 180 adjacent rows; zero same-shell rows | §5.4 |
| Trace/determinant domains | trace ideals and absolute walk sums | determinant-domain audit | §6.1–6.3 |
| Trace and least periods | zero deletion, loop digits, power witnesses | finite trace/witness agreement | §6.4–6.5 |
| Reproducible validation | frozen census and independent replay | 1,965 rows/lane; 39+76 hostile cases | §7, App. D |

## Section plan

### Abstract (180–230 words)

- Open with the exact operator and theorem, not field-level background.
- State the two-wall mechanism and the binary exception.
- Give the finite digit singular-value formula.
- State bounded/compact/\(S_2\), trace-class, and determinant domains.
- End with the trace/least-period distinction and one concise validation
  sentence explicitly labeled as finite consistency evidence.
- Avoid citations and undefined abbreviations.

### 1. Introduction (1.5–2 pages)

- Motivate the question: how a local radix compatibility rule and a global
  Dirichlet decay interact in an infinite operator ideal.
- Define \(B_{b,s}\), \(C_b\), \(\kappa_{b,q}\), and preview the sharp surface.
- Explain why a naive finite-tensor argument is insufficient: positive
  vertices, infinitely many magnitude shells, two independent divergence
  mechanisms, and equality.
- Present three falsifiable contribution bullets:
  1. exact all-radix finite-\(q\) Schatten classification;
  2. separate binary endpoint mechanism and ideal corollaries;
  3. legal trace/determinant and positive-vertex period ledger.
- Preview the strongest numerical illustration only as a consequence of the
  exact formula: \(\alpha_2=\log_2\sqrt5\), while the \(q=2\) wall is \(1\).
- Place Figure 1 after the contributions so a skim reader sees digit rule →
  shell factorization → two walls → operator/dynamical consequences.
- End with a paragraph stating the source/novelty firewall and paper map.

### 2. Related work and ownership boundary (1.5–2 pages)

Organize by question rather than by paper.

1. **Carries and binomial congruences.** Credit Kummer’s prime-radix carry
   valuation theorem and Lucas’s digitwise congruence.  State that the paper
   defines carry-free addition directly for every radix and uses Kummer only
   as a prime-radix comparator.
2. **Finite Pascal, binomial, Boolean, and disjointness matrices.** Synthesize
   Christopher–Kennedy, Bacher–Chapman, LaGrange, Chistikov et al.,
   Linial–Shraibman, and Alman–Guan–Padaki.  Assign zero novelty credit to
   finite spectra, tensor structure, coverings, and algorithms.
3. **Trace ideals and regularized determinants.** Cite Simon for standard
   definitions and general trace-ideal/determinant machinery; reproduce every
   specialized estimate used here.
4. **Positioning sentence.** The bounded directed search did not find the
   exact infinite positive-vertex, Dirichlet-weighted, all-radix theorem.  This
   is not a priority claim.

### 3. Carry-free source and the digit operator (2 pages)

- Freeze the vertex set \(\mathbb N=\{1,2,\ldots\}\), direct no-carry
  predicate, complex-power convention, one-edge clock, and marker \(z\).
- Explain why zero-completed digit words are finite controls only.
- Remove the imaginary phase by left/right diagonal unitaries.
- State and prove the digit-spectrum proposition:
  \(s_j(C_b)=[2\sin((2j-1)\pi/(4b+2))]^{-1}\).
- Derive \(\kappa_{b,2}^2=b(b+1)/2<b^2\), \(|\det C_b|=1\),
  \(\tau_b>b\), and \(\alpha_b>1\).
- Insert the generated digit/threshold table.  Label its decimals as display
  values of exact formulas, not experimental estimates.

### 4. Exact radix-shell calculus (2.5–3 pages)

- Define \(I_k=[b^k,b^{k+1})\cap\mathbb N\), unweighted blocks
  \(A_{k\ell}\), and weighted blocks \(B_{k\ell}\).
- Prove for \(k>\ell\):
  \[
  A_{k\ell}\simeq
  \mathbf 1_{(b-1)b^{k-\ell-1}}\otimes C_{b-1}\otimes C_b^{\otimes\ell}.
  \]
- Prove for \(k=\ell\):
  \(A_{kk}\simeq C_{b-2}\otimes C_b^{\otimes k}\), with \(C_0=0\).
- Translate both identities into exact \(S_q\)-norm formulas.
- Prove the two-sided uniform weighted comparison, including the lower
  factor \(b^{-\sigma}\), using inverse diagonal factors.
- Include Figure 2 (the exact critical curves for \(b=2,3,4,5\)) after the
  comparison, so the two geometric ratios have already been introduced.

### 5. Sharp ideal thresholds (3–3.5 pages)

#### 5.1 Sufficiency

- Sum cross-shell norms with \(k=\ell+h\).
- Make the two ratios explicit:
  \(b^{(1-\sigma)/2}\) in \(h\) and
  \(\kappa_{b,q}b^{-\sigma}\) in \(\ell\).
- Use the Banach-ideal triangle inequality only for \(q\ge1\).

#### 5.2 Universal wall and operator classes

- Use the \(n=1\) column and a positive-density units-digit class to reject
  boundedness at and below \(\sigma=1\).
- Combine with \(q=2\) sufficiency to obtain bounded = compact = \(S_2\)
  exactly on \(\sigma>1\).

#### 5.3 Digit wall for \(b\ge3\)

- Pinch to mutually orthogonal same-shell blocks and show nonsummability at
  and below the digit wall.

#### 5.4 Binary endpoint repair

- State first that §5.3 is illegal at \(b=2\) because \(A_{kk}=0\).
- Pinch instead to \(I_{2j}\oplus I_{2j+1}\); explain the duplicated singular
  values of the off-diagonal block.
- Use the exact adjacent-shell formula to reject the full binary
  nonmembership range
  \(\kappa_{2,q}2^{-\sigma}\ge1\): the same paired-shell lower bound does not
  decay in the equality case and grows in the strict-below case.
- Identify equality as the repaired endpoint, rather than as the only case
  covered by paired shells, because the \(b\ge3\) same-shell compression is
  unavailable there.
- Insert Figure 3, a source-level comparison of the two pinching mechanisms.

#### 5.5 Main theorem and trace-class corollary

- State the full iff theorem with all quantifiers and strict inequalities.
- Give trace class iff \(\sigma>\alpha_b\), and record
  \(\alpha_2=\log_2\sqrt5\).

### 6. Traces, determinants, and temporal support (2.5–3 pages)

#### 6.1 Diagonal trace

- Characterize loops by digits \(2d<b\).
- Delete the all-zero word before passing from a finite digit control to the
  positive graph.
- State the trace Dirichlet series in \(\sigma>\alpha_b\).
- Separate structural vanishing at \(b=2\), real positivity at \(b>2\), and
  the absence of any complex zero-free claim.

#### 6.2 Trace powers

- For \(r\ge2\) and \(\sigma>1\), derive the absolutely convergent based
  closed-walk sum by finite-shell compression and positive majorization.

#### 6.3 Regularized and ordinary determinants

- State that \(\det_2(I-zB_{b,s})\) is entire in \(z\) for \(\sigma>1\).
- Derive its logarithm near \(z=0\).
- Restrict ordinary trace and Fredholm determinant to
  \(\sigma>\alpha_b\).

#### 6.4 Least periods

- Use distinct powers \(b^j\) only as digit-position support witnesses.
- Prove the binary period set \(\{r\ge2\}\) and higher-radix period set
  \(\{r\ge1\}\), including least-period rather than merely period checks.

#### 6.5 No unweighted Artin–Mazur zeta

- Explain that allowed lengths have infinitely many fixed points, so the
  unweighted fixed-point ledger is not a finite Artin–Mazur coefficient.

### 7. Independent finite controls and proof audit (1.5–2 pages)

- Begin with the evidence firewall: this section validates implementation
  and exact finite identities; it does not prove §5–§6.
- Describe lane A (direct positive prefixes and quotient/remainder carry
  checks) and lane B (independent digit automata and shell tensors).
- Report exactly: 1,965 rows per lane, 8,010 overlapping digit intervals,
  420 shell envelopes, zero exact-field mismatches, and zero missing/extra/
  duplicate rows.
- Describe auditor P’s exclusive ownership of four infinite certificates,
  while keeping the self-contained proof in the manuscript primary.
- Report 39 atomic mutations (68 designated rejections and 322
  non-designated acceptances), 76 physical/adversarial instances, and zero
  survivors.
- Mention normal and hostile independent replays of State A and State B.
- Include the generated validation census table.
- State limitations: bounded source search, finitely many validation cases,
  no \(q<1\), no authority/publication inference, and no Route-B eligibility.

### 8. Discussion and conclusion (0.75–1 page)

- Rephrase the mechanism: local digit singular values and global shell decay
  generate two independent walls; binary zero blocks alter the proof but not
  the final formula.
- Identify the genuinely reusable lesson: an endpoint theorem for an
  infinite digit operator must separate shell summability, column
  boundedness, and zero-block geometry.
- List limitations without inflating them into future claims:
  \(q<1\) is outside the Banach-ideal proof; priority is not established;
  no completed \(s\)-plane object or rational-prime primitive ledger exists.
- Give two concrete future questions: quasi-Schatten thresholds for
  \(0<q<1\), and more general digit automata whose shell factors are not pure
  tensor powers.

## Appendix plan

### Appendix A. Digit covariance and singular values

- Write the row-reversal identity and inverse tridiagonal matrix explicitly.
- Solve the interior recurrence and terminal boundary condition.
- Check determinant/product and strict AM–GM.

### Appendix B. Shell-factor bookkeeping

- Give coordinate maps for cross-shell and same-shell blocks.
- Account for top-digit choices, repetition multiplicity, zero rows, and
  transposition.
- State the binary adjacent-shell specialization.

### Appendix C. Endpoint pinching and determinant convergence

- Give the direct-sum Schatten calculation for both pinching constructions.
- Supply the finite-shell-to-trace-power limiting argument.
- Record the local logarithm domain without overclaiming global series
  convergence in \(z\).

### Appendix D. Reproducibility and evidence ledger

- Bind the integration seal, State-A/State-B tree digests, contract digest,
  and canonical summary digest.
- Reproduce the finite-control and hostile-control census.
- Explain the independent replay protocol and finite/infinite evidence types.
- Keep the protected-authority replay row in the publication/closure gate,
  not the manuscript-plan gate.  That row was later injected and replayed
  independently without changing the historical meaning of `PLAN_READY`.

## Figure and table plan

| ID | Type | Purpose | Data/source | Generation |
|---|---|---|---|---|
| Figure 1 | Hero TikZ diagram | Show digit compatibility → exact shell tensor → two critical walls → trace/determinant/period consequences. | Frozen definitions and theorem | Manual vector TikZ, source retained |
| Figure 2 | Line plot | Plot \(\sigma_c(q)=\max\{1,\log_b\kappa_{b,q}\}\) for \(b=2,3,4,5\), emphasizing the universal plateau and trace-class points. | Exact singular-value formula serialized in `canonical_summary.json` | Python → vector PDF |
| Figure 3 | TikZ comparison | Contrast same-shell pinching for \(b\ge3\) with paired adjacent-shell pinching for \(b=2\). | Exact shell identities | Manual vector TikZ, source retained |
| Table 1 | LaTeX table | Display \(\tau_b\), \(\alpha_b\), \(\kappa_{b,2}\), and the exact \(q=2\) wall for \(b=2,3,4,5\). | `canonical_summary.json` | Python → LaTeX |
| Table 2 | LaTeX table | Report the finite and hostile validation census with explicit evidence type. | `canonical_summary.json` | Python → LaTeX |

Figure captions must state what is compared and what the reader should infer.
No figure may call a finite PASS a proof.  Use line styles and markers in
addition to color; no titles inside figures.

## Citation plan

- §1: Kummer and Lucas only for historical carry/binomial context; Simon for
  standard trace-ideal terminology.
- §2: `kummer1852ergaenzung`, `lucas1878congruences`,
  `christopher1997binomial`, `bacher2004pascal`,
  `lagrange2013eigenvalues`, `chistikov2017fractional`,
  `linial2007factorization`, and `alman2023kronecker`.
- §3–§6: proofs are self-contained; cite `simon2005trace` only for standard
  trace-ideal and regularized determinant background.
- No citation is generated from memory.  Every entry must be bound in
  `evidence/SOURCE_VERIFICATION.md`; unresolved metadata blocks finalization.

## Reverse-outline target

The topic sentences should read as this chain:

1. A local carry-free digit rule defines an infinite weighted operator.
2. Prior work owns the carry arithmetic and every finite tensor control.
3. The digit matrix supplies exact singular-value growth.
4. Radix shells convert digit growth into two geometric ratios.
5. Those ratios, together with distinct endpoint pinchings, give the exact
   strict Schatten surface.
6. The ideal surface fixes legal trace and determinant domains, while zero
   deletion fixes temporal support.
7. Independent finite lanes and hostile tests validate the implementation
   without replacing the proof.
8. The mechanism is exact but deliberately narrower than a completed
   arithmetic spectral theory.

## Plan-review questions

An independent formal reviewer must answer all of the following before the
status can become `PLAN_READY`:

1. Does every theorem claim have a proof location independent of finite PASS
   records?
2. Is equality treated separately at \(\sigma=1\), the digit wall for
   \(b\ge3\), and the digit wall for \(b=2\)?
3. Are zero deletion, complex phases, trace powers, and determinant domains
   stated with correct quantifiers?
4. Does the related-work plan assign zero credit to every finite carry,
   Pascal, Boolean, and disjointness owner?
5. Can a skim reader recover the operator, main theorem, binary exception,
   and contribution boundary from the title, abstract plan, introduction,
   and Figure 1?
6. Is the 16–20 page occupancy budget, including the abstract and all planned
   floats, feasible without moving essential proof intuition out of the main
   text?
