# P122 hostile review B — round-one re-entry

**Reviewer role:** second independent nonauthor re-entry reviewer  
**Artifact reviewed:** current round-one source, support, code, references, main.pdf, and main_round1.pdf  
**Decision:** **GO_INTERNAL**  
**Severity:** no CRITICAL findings; no MAJOR findings; one nonblocking MINOR wording note  
**External status:** **HOLD**

I read HOSTILE_REVIEW_A only to identify its M1--M4 repair obligations. I
reconstructed the operator, inverse theorem, Boolean state, owner boundary,
and controls independently rather than importing A's verdict. I did not
modify any manuscript, bibliography, support, code, or PDF file.

## 1. Reconstructed claim ceiling

The map cuts a permutation before each left-to-right maximum and reverses
exactly its even record blocks. The defensible residual package is:

1. the sharp clock for this literal synchronous operator;
2. the admissible target-cut bijection and target-local fibre DP; and
3. the all-size weighted record-word automaton for image and Garden counts.

Foata's record/cycle correspondence, the all-odd-cycle fixed enumeration,
relative-rank record weights, generic lexicographic descent, and generic
finite-state or segmentation methodology earn zero credit. P105 already owns
the broad same-carrier silhouette of a permutation map with depth \(n-1\),
fibres, and Garden states. Under this ceiling, the target-cut theorem and its
separate all-size aggregation are sufficient for a concise internal note.

I found no claim of maximum indegree, all depth layers, iterated fibres,
five-state minimality, asymptotics, novelty, priority, or first occurrence.

## 2. Independent mathematical reconstruction

### 2.1 Descent and sharp clock

The first changed record block starts at its strict maximum. Reversal puts
its smaller final entry at the first changed location, proving strict
lexicographic descent. For \(\pi=\alpha n\beta\), an even value of
\(|\beta|\) makes \(n\beta\) an inert odd block, so only \(\alpha\) evolves.
An odd value of \(|\beta|\) gives
\[
                  \Phi(\pi)=\Phi(\alpha)\operatorname{rev}(\beta)n,
\]
after which \(n\) is an inert singleton and the remaining standardized prefix
has order \(n-1\). This proves the \(n-1\) upper bound. The family
\(\omega_n=(2,3,\ldots,n,1)\) satisfies
\(\Phi(\omega_n)=\omega_{n-1}n\), so the bound is sharp. No small-order or
parity exception is missing.

### 2.2 Fibre inverse

For a target segment ending at \(i_r\), an odd source block is unchanged and
therefore has its maximum at the segment's first target endpoint; an even
source block is reversed and has its maximum at the last endpoint. Because
source block maxima increase, this endpoint is the complete target-prefix
maximum \(M_{i_r}\), proving necessity of the admissibility test.

Conversely, retaining odd admissible segments and reversing even ones puts
\(M_{i_r}\) first in every reconstructed source segment. Its occurrence is
inside that segment, whereas the preceding prefix maximum lies strictly
earlier; distinctness therefore makes successive block maxima increase
strictly. All other segment entries are smaller than the new first entry, so
no interior record cut appears. The selected cuts are exactly the source
record cuts, and applying \(\Phi\) restores the target. Unique record
factorization gives injectivity. Last-cut decomposition then gives the stated
DP and fibre size.

### 2.3 Five-coordinate state

Let \(d_j\) denote reachability of a cut at \(j\), with \(d_0=1\). After
position \(j\), the manuscript now explicitly defines
\[
E_j=\bigvee_{\substack{0\le i\le j\\i\ {\rm even}}}d_i,\qquad
O_j=\bigvee_{\substack{0\le i\le j\\i\ {\rm odd}}}d_i,
\]
the most recent record \(\ell_j\),
\(Q_j=d_{\ell_j-1}\), \(L_j=\ell_j\bmod2\), and \(D_j=d_j\).
These are the five invariants actually needed.

At a record \(j\), an odd last segment may be the singleton and contributes
\(D_{j-1}\). An even last segment exists precisely when a reachable preceding
cut has the parity of \(j\), contributing \(E_{j-1}\) for even \(j\) and
\(O_{j-1}\) for odd \(j\). The new record gives
\(Q_j=D_{j-1}\) and \(L_j=j\bmod2\). At a nonrecord, the even case is
impossible; the only possible odd segment starts at \(\ell_j\), requiring
\(Q_{j-1}=1\) and \(j\equiv L_{j-1}\pmod2\). OR-ing the resulting \(D_j\)
into the parity-\(j\) accumulator preserves \(E_j,O_j\). Finally,
\(d_0=d_1=1\) yields \(s_1=(1,1,1,1,1)\). Thus the initialization,
coordinate domains, and inductive preservation are complete.

The relative-rank code is explicitly identified as a bijection
\(\mathfrak S_n\to[1]\times\cdots\times[n]\). At position \(j\), exactly one
rank is a record and \(j-1\) ranks are nonrecords. Hence the record/nonrecord
transition weights \(1\) and \(j-1\) count each target exactly once, and the
terminal condition \(D=1\) is exactly nonempty fibre membership.

## 3. Closure of A's M1--M4

### M1 — bibliographic identity and owner subtraction: CLOSED

- The live arXiv record 2607.22767, checked on 2026-08-30, lists **Pyuyi
  Chufeng Huang**, the title used in the bibliography, submission on
  2026-07-24, and current v2 dated 2026-07-31. The manuscript correctly
  describes it as a record-set/order-polynomial neighbor rather than a
  permutation self-map.
- Bouvel--Cioni--Ferrari now uses the published Electronic Journal of
  Combinatorics record, volume 29(4), P4.32 (2022), DOI
  10.37236/11390. Its left-to-right-maximum description of bubblesort
  preimages and functional trees is explicitly deducted.
- Cioni--Ferrari now uses the published Discrete Mathematics record,
  344(11), 112561 (2021), DOI 10.1016/j.disc.2021.112561. Its recursive
  queuesort preimages and special left-to-right-maximum target class are
  explicitly deducted.
- Remmel--Wachs is pinned to page 40. That page states the exact convention:
  list cycles by increasing largest element, write each largest element
  first, then erase parentheses, producing left-to-right maxima. Foata--Han
  is retained only as broader transformation background.
- The manuscript calls the literature result a bounded non-hit and makes no
  novelty or priority inference from it.

The direct owner risk remains nonzero because the search is bounded and
Huang is a live 2026 neighbor. This is a reason for external HOLD, not an
internal mathematical stop.

### M2 — five-bit invariant and proof: CLOSED

The source now contains \(d_0=1\), exact finite ranges for \(E_j,O_j\), all
five coordinate meanings, the forced start state, and a coordinate-by-
coordinate induction for record and nonrecord transitions. My independent
derivation above agrees with equations (4.2)--(4.4).

As an additional hostile check independent of the shipped aggregate totals,
I enumerated every record/nonrecord word through length 16 and compared the
transition state after every prefix with a direct admissible-cut computation.
All **983,045** state assertions passed. This is corroboration, not the
all-size proof.

### M3 — internal collision firewall: CLOSED

The manuscript explicitly names P105 as the closest same-carrier collision:
P105 already owns the broad package “permutations, depth \(n-1\), fibres, and
Garden states” through cycle-minimum pruning and an iterate normal form.
P122 consequently restricts its residue to adaptive record cuts, the
endpoint-parity target-cut bijection, and the weighted record-word automaton.

P117 and P120 are also subtracted as parity-triggered reversal/mirroring
neighbors on different carriers and with different temporal mechanisms.
The text gives no value credit for shared carrier, depth scale, or reversal
vocabulary. This is the firewall A required.

### M4 — auditable example: CLOSED

For target \(12435\), the source lists prefix maxima \(1,2,4,4,5\), all four
admissible endpoint sequences, and all four reconstructed preimages:
\[
\begin{array}{c@{\leftrightarrow}c}
(1,2,3,5)&12453\\
(1,3,5)&14253\\
(1,5)&15342\\
(2,3,5)&21453.
\end{array}
\]
Direct reconstruction confirms that all four sources map to \(12435\), and
the displayed DP vector \((1,1,2,3,0,4)\) is correct. The same target has
record word \(R,R,R,N,R\), and the five-row bit trace agrees coordinatewise
with the invariant. The example therefore audits both residual mechanisms,
not merely their final counts.

The associated round-zero minor repairs are also closed: “reconstructed
source segment” is used, items (ii) and (iii) are named unambiguously, and
relative ranks are stated as a bijection rather than informal independence.

## 4. Fresh mechanical controls

From the paper directory I reran:

    PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py

The fresh transcript is byte-identical to code/verification_output.txt:

    record-block reversal fibre verifier: PASS
    assertions=1636476
    record-block image automaton: PASS
    assertions=551
    combined_assertions=1637027

The canonical and fresh transcript SHA-256 is
f696fb468ff4de65f82d755079634da55271853310ca442736d51f43e085f5dc.
The three verifier hashes agree with the round-zero audit:

- verify.py:
  75f04bc6e5ebe6d0c807d131af3873bd7df98fb582628d69b8e2a8f351aa07b4
- fibre_verify.py:
  ffbedd6caeea5b09e4ac905c06651348ec87463ee127d73807ad8c93b1dd6e46
- image_automaton.py:
  e9fb3c83d23bfdcb5e92232d0226453fd7bf68dff041412afb18f20f7b158f11

The literal lane exhausts sources and targets through \(n=9\); the separate
record-word lane checks literal image counts through \(n=9\), factorial
record-set mass, and the transfer through \(n=30\). No floating-point,
random, network, or symbolic-simplifier dependency is present.

## 5. Isolated build and visual audit

I copied only main.tex and references.bib into a fresh temporary directory and
ran

    pdflatex -> bibtex -> pdflatex -> pdflatex.

All stages exited zero. The final log has zero LaTeX/package/pdfTeX warning
hits, zero undefined citations or references, and zero overfull/underfull box
reports. The isolated PDF SHA-256 is
5d629906f7841e707ae4f75e41a7f4377c55b9bb6fa523ecf0b022dcc565625e,
byte-identical to both main.pdf and main_round1.pdf.

The current artifact is 4 A4 pages and 293,924 bytes. I rendered and inspected
all four pages. There is no clipping, overlap, malformed formula, missing
glyph, broken reference, unresolved citation marker, or unreadable table.
All fonts are embedded/subsetted and Unicode-mapped. Author metadata is
empty; the PDF has no forms, JavaScript, or encryption.

## 6. Findings by severity

### CRITICAL

None.

### MAJOR

None. A's M1--M4 are all closed, and I found no false theorem, failed inverse,
invalid Boolean transition, owner-credit leak, internal collision leak, or
reproducibility failure.

### MINOR

**mB1 — status wording only.** The abstract says that novelty, priority, and
external release “remain open,” whereas Section 5 and every support document
say external circulation remains “on hold.” The latter is the operative
status and is unambiguous. Harmonizing the abstract to “remain on hold” at
the next authorized editorial touch would remove the slight mismatch. This
does not block internal freeze and does not authorize a source edit in this
review.

## 7. Verdict

**GO_INTERNAL.** The round-one repair closes every required re-entry item.
The fibre bijection and weighted five-bit image census are correct,
self-contained, mechanically stress-tested, and sufficiently distinct after
the P105/P117/P120 deductions to support an internal short-paper freeze.

**External HOLD remains mandatory.** The owner search is bounded, the Huang
neighbor is current, and neither the verifier nor this review establishes
novelty or priority. No public posting, submission, priority statement, or
external-release action is authorized.
