# P175 — Diagonal-Feedback Commutators and Support-Colouring Fibres

Anonymous AMS short note, final Round 2 with both hostile reviews closed.

## Status

- Scientific gate: `GREEN_OWNER_THIN`.
- External state: `HOLD_EXTERNAL`.
- Hostile reviews: Review A `0/0/0`; Review B `0 Critical / 1 Major / 0
  Minor`, with the owner reframe implemented and delta-accepted.
- Release, priority, novelty, and submission claims: not authorized.
- Figure: N/A; the complete height-two branching formula replaces a
  decorative diagram.

## Literal system

For (K=\mathbb F_q), the carrier is (M_n(K)) in its fixed standard basis
and

\[
\Phi(A)=[\operatorname{Diag}(a_{11},\ldots,a_{nn}),A].
\]

The output entry is
((a_{ii}-a_{jj})a_{ij}), so (\Phi^2=0).  A target is reachable exactly
when its diagonal vanishes and its undirected off-diagonal support graph is
(q)-colourable.  Every one-step fibre is the corresponding
occupation-weighted proper-colouring sum.  The paper derives the exact image,
zero fibre, depth layers, branch counts, all-time fibres, and zeta function.

## Artifact package

- `main.tex` — anonymous LaTeX source.
- `references.bib` — eight verified and cited owner references.
- `main.pdf` — settled canonical Round-2 PDF.
- `main_round0_original.pdf` — byte-identical frozen Round-0 copy.
- `main_round1.pdf`, `main_round2.pdf` — preserved review rounds.
- `NARRATIVE_REPORT.md` — claim story and owner subtraction.
- `PAPER_PLAN.md` — section, evidence, citation, and figure plan.
- `CLAIMS_EVIDENCE.md` — proof/computation ledger by claim.
- `SOURCE_VERIFICATION.md` — primary-source verification and ownership
  boundaries.
- `verify_p175.py` — independent exact verifier using only the Python
  standard library.
- `verification_output.txt` — canonical deterministic transcript.
- `BUILD.md` — reproducible build and settled checksums.
- `SELF_QA.md` — source, proof, computation, anonymity, and visual QA.
- `HOSTILE_REVIEW_A.md`, `HOSTILE_REVIEW_B.md` — independent review ledgers.

## Reproduce the exact controls

From this directory:

```sh
python3 verify_p175.py
```

The settled run covers eleven ((n,q)) boxes, including the nonprime field
(\mathbb F_4), and records 2,111,465 assertions.  Computation is explicitly
falsification evidence rather than proof.

## Reproduce the paper

Run the four commands recorded in `BUILD.md`.  The settled `main.pdf` and
`main_round2.pdf` must compare byte for byte.  The source suppresses
volatile PDF metadata so a clean build with the recorded toolchain is
deterministic.

## Ownership boundary

P175 gives zero contribution credit to classical matrix/group commutator
theory, P119's Bier-owned fixed-regular triangular Engel mechanism, the
exact complete-graph Potts specialization, Stanley's chromatic-symmetric
occupation enumerator and its deterministic weight transform, and
Artin–Mazur zeta bookkeeping.  The narrow residual is the literal
matrix-to-support reduction for every target and the consequent rooted tree.
A bounded literature search does not prove novelty; external circulation
stays on hold.
