# Evidence — ASFS-20260915-PTI01

**Status:** STOP — EXACT FULL FLAT-TRACE SEQUENCES HAVE NO HILBERT TRACE-CLASS POWER REALIZATION.

## Inputs and chronology

On 2026-09-15 the author read the applicable AGENTS.md and plan, current
README, the complete 153 package and review, the 156 scope card and
summary, the local paper standard and prior-work lineage guide.
The [candidate card](../candidate-card.md) was frozen with an OPEN
existential question before asymptotic or spectral result writing.
The exact source, full map, roof, sequence, weights and all-powers
quantifier were not changed after the freeze.

## Proof chain and reproduction

The [paper](../paper.md) contains the complete candidate-specific proof:

1. Recheck the full prime/composite return equations and natural weights.
2. Use c_1=2 and exact dyadic endpoint counts for all k>=2.
3. Apply PNT and bound the complete proper-divisor remainder by
   m 2^floor(m/2).
4. Derive the full-sequence limits, not subsequence or limsup estimates.
5. Apply Lidskii to trace-class powers and isolate their finite
   peripheral phases by Cesàro averages.
6. Compare the forced integer multiplicity with 1<1/log 2<2.
7. Derive the ordinary determinant-germ consequence and exhibit the
   finite-cutoff trace-class control.

There is no prime-table input, numerical orbit cutoff, precision
parameter, training/validation fit or computational theorem claim.
The small-m rational identities are direct substitutions. The
infinite statements depend on mathematical proofs and cited standard
theorems, not a numerical census.

## Bounded external-source verification

The sources contribute theorem inputs, not this candidate's arithmetic
mechanism or owner status:

- [Valerio De Angelis, The Classical Proof of the Prime Number Theorem](https://vdeangel.xula.edu/Notes/PNT.html):
  directly browsed the opening “Statement of the Prime Number Theorem,”
  which defines pi(x) using p<=x and states pi(x)~x/log x.
- [Xianzhe Dai, Lectures on Dirac Operators and Index Theory](https://web.math.ucsb.edu/~dai/book.pdf):
  directly browsed Section 3.1, printed pp. 36–37 (PDF indices 35–36),
  including the two-sided trace-class ideal property and Theorem 3.1.2
  (Lidskii). Only these locators are cited, not an assertion that the
  entire book was read.
- [Aleksey Kostenko, Trace Ideals with Applications](https://users.fmf.uni-lj.si/kostenko/teach/IdealsNotes.pdf):
  the separate source checker and author verified Theorem 2.3.1
  (p. 12), the algebraic-multiplicity convention and inequality
  (3.4.14) (pp. 36–37), and Theorem 3.4.7 (p. 41). This covers the
  nonnormal compact spectrum, eigenvalue absolute summability and
  ordinary determinant product. The notes assume a separable Hilbert
  space; the paper gives its own reducing-subspace argument for the
  broader Hilbert statement.

The direct browser open of Kostenko timed out for the author. The
specified source was then read without saving a file, using:

~~~bash
curl -L --fail --max-time 30 https://users.fmf.uni-lj.si/kostenko/teach/IdealsNotes.pdf | pdftotext -layout - - | rg -n -A 25 -B 10 'Theorem 2.3.1|Theorem 3.4.7|3.4.14|algebraic multiplicities|separable Hilbert'
~~~

The command exited 0 and displayed the stated theorems, p=1 summability
inequality and separable-space assumption. These printed-page locators
come from that source text, not a claimed local-PDF preflight. The
source checker separately read the p. 36 algebraic-counting convention.

No source-specific kernel theorem is transferred to the noncompact map.
No unpublished manuscript was sent to an external model, and no local
PDF or publication artifact was created. There is no literature-wide
priority or novelty claim.

## Review and verification state

The research controller assigns a separate mathematical reviewer;
that review is distinct from authorship and from the bounded
source-checking subagent. Model review is not human peer review or
formal verification. The source checker independently checked
trace-class spectral assumptions; the author retains proof ownership.

Local Markdown links and ID/status consistency are checked after the
five core files are complete. Exact check outputs are appended below.

### Author check receipt — 2026-09-15

A read-only Node check covered the exact five core paths:
README.md, paper.md, candidate-card.md, claim-ledger.md and
evidence/README.md. It resolved each non-HTTP/non-mail/non-fragment
Markdown link from its containing directory with fs.existsSync;
checked the complete candidate ID and final status in every core file;
and checked trailing whitespace (allowing Markdown two-space line
breaks) and blank interruptions inside tables.

Output: files=5, local_links=21, id_status_checks=5, failures=[].
The separate command below exited 0 with no output:

~~~bash
git diff --check -- papers/157-power-trace-integrality-audit
~~~

The direct filesystem check is the substantive link/metadata check:
Git's diff check alone does not cover newly untracked file contents.
This receipt does not certify a mathematical theorem. A review file
added later has its own review provenance and is outside this
five-core-file count.

ARS claim/evidence/counterargument discipline was used within this
bounded note. No full publication runtime, hooks, external API or
additional research package was invoked.

See [claims](../claim-ledger.md) and [summary](../README.md).
