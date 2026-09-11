# P212-A-M1 exact live citation repair

Root read the proposed CITATION_DELTA.patch and initial A source findings
completely at c3de6f. Root independently opened the primary
[Holroyd et al. preprint, v4](https://arxiv.org/html/0801.3306): Theorem3.8
is the recurrent-unicycle characterization, whereas Lemma4.9 is the
Eulerian full-edge tour. The latter's proof and Corollary4.10 were also
read. This confirms the locator repair, not a new mathematical contribution.

Actual a5994e compared both live originals to immutable Round0, preserved
them physically under before_citation/, then compared each complete saved
copy. Root applied exactly the proposed two lines with apply_patch: body
locator Theorem3.8 becomes Lemma4.9; bibliography note adds Lemma4.9 while
retaining Theorem3.8/Corollary4.10. No frozen or historical receipt changed.
CITATION_DELTA_NATIVE.json retains the subsequent full25-mapping check:
exactly these two replacements,23 other raw pairs unchanged, including
proof, verifier, parameters, canonical and the initial PDF. Same reviewer
must accept this applied delta before P212-A-M1 closes.

The live main.pdf remains the historical initial PDF, not a PDF rebuilt
for these new citation bytes. A later approved source-only build must use
the repaired bibliography/body. Do not rerun the old initial artifact DATA
checker against changed live source or claim its complete live-input key
still holds. Its original evidence remains valid for its accepted initial
source snapshot. No science, new PDF build, reviewer PASS or Round1 here.
