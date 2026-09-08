# FC7 eighth-pass source audit

2026-09-08 UTC. This is targeted verification of the seventh pass's
source gap, not a global novelty survey. The original full question is
preserved in [the frozen attempt](FROZEN_ATTEMPT.md).

## Actual access and mathematical use

| Source | Access actually obtained | Role and limit |
| --- | --- | --- |
| Ostafe–Pelican–Shparlinski, *On pseudorandom numbers from multivariate polynomial systems*, FFA 16(5), 2010, 320–328, DOI 10.1016/j.ffa.2010.05.002 | Publisher indexed abstract/metadata, author publication lists and institutional record. Direct publisher article, volume and PDF requests failed. | Metadata is verified; the original theorem body and complete hypotheses remain unverified. |
| Roy–Steiner, *An Algebraic System for Constructing Cryptographic Permutations over Finite Fields*, arXiv:2204.01802v1, 4 April 2022 | Version-specific HTML and PDF returned. Read HTML sections 5.1–5.2 and 5.5, the explicit Assumption 5.2, and the relevant references. | Their section 5.5 reports the generic 2010 estimate. This is a later primary research paper containing a secondary citation, not original-2010-body access. Their stronger conditional theorem is not imported. |
| Ostafe–Shparlinski, *On the degree growth in some polynomial dynamical systems and nonlinear pseudorandom number generators*, arXiv:0902.3884v3 | PDF body accessed; introduction, triangular construction, Lemma 3 and Theorem 4 with the surrounding moment argument were read. | Classical Weil/moment ownership. The special triangular theorem is not applied to the Hénon map. The local proof explicitly enforces a univariate degree below the characteristic. |

Primary links actually used:

- [Publisher article](https://www.sciencedirect.com/science/article/pii/S1071579710000511)
  and [Macquarie institutional record](https://researchers.mq.edu.au/en/publications/on-pseudorandom-numbers-from-multivariate-polynomial-systems/).
- [Pelican's publication list](https://sites.google.com/site/elapelican/home/publication-list)
  and [Ostafe's university page](https://web.maths.unsw.edu.au/~alinaostafe/);
  the target entry did not provide an accessible manuscript link.
- [Roy–Steiner v1 HTML](https://arxiv.org/html/2204.01802v1),
  [version-specific PDF](https://arxiv.org/pdf/2204.01802v1), and
  [Ostafe–Shparlinski PDF](https://arxiv.org/pdf/0902.3884).

The reported generic bound is
$O(N^{1/2}p^{n/2}/\sqrt{\log p})$. Its dimension-two scale does not
deliver the desired short-cycle power saving. The
[proof package](PROOF_PACKAGE.md) independently derives that scale
for this fixed map, so its helper theorem does not depend on
unseen 2010 details. Neither fact establishes exhaustive novelty.

## Discovery-only leads and failed access

Ostafe's 2010 Zurich thesis *Polynomial Dynamics and Pseudorandomness*
was identified by title and catalogue metadata, including the
[Swiss National Library bulletin](https://ead.nb.admin.ch/web/sb-pdf/2011/sb201122.pdf)
and the indexed [supervisor student record](https://www.math.uzh.ch/student?key1=604&type=2).
The thesis body was not found/read, and the direct student-page request
failed. ResearchGate, MaRDI, J-GLOBAL and bibliography hits were discovery
locators only; they do not supply proof evidence.

Later Roy–Steiner revision locators included
[IACR 2024/1316](https://eprint.iacr.org/2024/1316.pdf) and
[SAC24 preproceedings](https://sacworkshop.org/SAC24/preproceedings/RoySteiner.pdf).
The IACR direct request failed and the SAC PDF body was not read.
Only the explicitly accessed arXiv v1 body is used for the comparison;
no claim is made that the displayed v1 statements persist unchanged
in the later revision.

The Ibeas–Winterhof UDT5(2010) paper and the
Ostafe–Shparlinski–Winterhof joint-linear-complexity paper appeared in
indexed primary-source discovery. They were not read in body and no
theorem from them is used. There was no author contact or manuscript
upload to any service.

## Exact search-query ledger

Seventeen query strings were submitted, once each, in five
search-bearing calls of sizes 3, 4, 4, 3 and 3. Direct URL opens,
in-page finds and subsequent version-specific reads are not counted
as search queries. No recency filter was applied: this is retrieval
of a specific foundational source.

1. "On pseudorandom numbers from multivariate polynomial systems" pdf
2. "Ostafe" "Pelican" "2010" polynomial systems theorem
3. "10.1016/j.ffa.2010.05.002"
4. "Ostafe" "thesis" "polynomial" "2010"
5. "On pseudorandom numbers" "systems" "Theorem 1"
6. "On pseudorandom numbers from multivariate" filetype:pdf -site:ftp.math.utah.edu -site:imar.ro -site:old.uefiscdi.ro
7. "multivariate polynomial systems" "Pelican" "log"
8. "Polynomial Dynamics and Pseudorandomness" Ostafe pdf
9. "Ostafe" "Pelican" exponential sums bounds orbits polynomial
10. site:math.uzh.ch "Ostafe" "pdf"
11. "On pseudorandom numbers from multivariate polynomial systems" arxiv
12. "Ostafe" "Polynomial Dynamics" dissertation pdf
13. "S1071579710000511" pdf
14. "Ostafe" "Pelican" "pseudorandom" "bound"
15. "An Algebraic System for Constructing Cryptographic Permutations over Finite Fields"
16. "Ostafe" "Pelican" "Theorem" polynomial discrepancy
17. "multivariate polynomial systems" "degree growth" "2010" "bound"

## Skills, local-first fallback and execution boundary

Research-lit was used for local-first retrieval. No Zotero or Obsidian
tools were available; relevant filename-filtered local discovery found
no matching PDF. The named literature/tools/legacy-fetch fallbacks were
absent. Primary web access was therefore used. No source PDF was saved,
and no API bibliography resolver or human-read attestation was created.

ARS was limited to bounded source verification, not a full research
pipeline. Proof-writer required separate status for the original claim
and the helper, so the classical-scale bound does not replace FC7.
The batch skill prevents this short specialization from filling a
paper slot. Current-team instructions govern delegation/model choices;
no legacy external-model example was executed.

Mathematical programs: **0**. Old mathematics/build reruns: **0**.
No GPU, paid model API, Git mutation or formal Route-A evaluation.
Source comparison remains bounded by actual access, not by the number
of search queries. NO_BAD_EULER_OR_ROOT_NUMBER.
