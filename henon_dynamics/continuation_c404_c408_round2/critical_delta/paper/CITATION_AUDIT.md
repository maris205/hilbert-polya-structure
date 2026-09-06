# C406 manuscript bibliography and citation audit

Date: 2026-09-06. Exactly four primary works are cited. No citation
or numerical quota was imposed, and no additional survey was requested.

The complete author SOURCE_AUDIT.md and the independent source-ownership
addendum were read before drafting. The reviewed proof and audit files
remain unchanged. The present document concerns the actual manuscript's
bibliography and attribution, not another proof-review verdict.

## Metadata acquisition

DOI content negotiation was performed successfully for all four entries:

    curl -L --fail --max-time 35 --silent --show-error \
      -H 'Accept: application/x-bibtex' https://doi.org/DOI

The returned records were used as the metadata base, not invented from
memory. TeX escaping, stable keys, and title capitalization were normalized.
The programmatic returns for S3 and S4 omit the article identifier; these
were completed from the already verified primary/institutional metadata
below. No unresolved placeholder is inserted in the bibliography.

### S1: egger2011trace

- DOI: `10.1088/1751-8113/44/18/185202`.
- DOI return confirms title, two authors, J. Phys. A: Mathematical and
  Theoretical 44(18), 185202, and 2011.
- [Primary author text](https://arxiv.org/pdf/1104.1364) confirms the
  displayed name Sebastian Egger né Endres and Frank Steiner.
- The DOI machine record parses the first name as `Endres, Sebastian
  Egger né`. The BibTeX field is normalized to
  `{Egger n{\'e} Endres}, Sebastian`, following the author's displayed name;
  no additional person or author was introduced.
- Actual manuscript attribution: the harmonic-chain model, its classical
  constant-coupling discreteness result, and the fully Dirichlet divisor
  benchmark. Relevant source parts inspected: introduction and §§2–4,
  especially equation (4), Theorem 2.2, and equations (35)–(39).
- No finite-constant-coupling high-energy theorem is attributed to S1.

### S2: kostenko2010point

- DOI: `10.1016/j.jde.2010.02.011`.
- DOI return confirms Aleksey S. Kostenko and Mark M. Malamud,
  Journal of Differential Equations 249(2), 253–304 (2010).
- [Primary author text](https://arxiv.org/pdf/0908.3542) and
  [TU Dublin institutional record](https://researchprofiles.tudublin.ie/en/publications/1-d-schr%C3%B6dinger-operators-with-local-point-interactions-on-a-disc-3/)
  were independently checked.
- Actual manuscript attribution: general realization and discreteness
  machinery for point interactions with shrinking gaps. Example 5.12
  and §5.4 were inspected; no second counting coefficient is borrowed.

### S3: drabkin2012transport

- DOI: `10.1063/1.4769219`.
- DOI return confirms Maxim Drabkin, Werner Kirsch, Hermann
  Schulz-Baldes, the title, J. Math. Phys. 53(12), and 2012.
- Article identifier `122109` is from the verified
  [FAU institutional record](https://cris.fau.de/publications/112746744/).
- [Primary author text](https://arxiv.org/html/1207.0295v1), §§2.1–2.3,
  was read at the delta jump, free propagation, one-step transfer matrix,
  and positive periodic specialization.
- Actual manuscript attribution: those classical periodic formulas only.
  The manuscript derives its own length-pi normalization and uniform
  finite-chain estimate. No random-transport theorem is imported.

### S4: bifulco2024comparison

- DOI: `10.1063/5.0178226`.
- DOI return confirms P. Bifulco and J. Kerner, the title,
  J. Math. Phys. 65(7), and 2024.
- Full author names are verified in the
  [primary arXiv record](https://arxiv.org/abs/2308.16869), which also
  links the journal DOI. Article identifier `073502` is recorded in
  the author's verified source audit and the author's 2025 dissertation
  bibliography; the journal is the published reference used here.
- The body locator in the manuscript is explicitly **arXiv v1,
  Section 5, Theorem 11**, following the
  [actual inspected text](https://arxiv.org/html/2308.16869v1).
  That theorem assumes fully Dirichlet coupling and is a local Weyl law.
- The journal text is reorganized. The manuscript does not claim that
  Theorem 11 is the journal theorem number. The automated HTML date
  is not used as the bibliographic year.
- The later dissertation passages were an ownership check, not an
  additional theorem input, and are not padded into the bibliography.

## Claim-to-citation boundary

The four references identify prior model and comparison machinery.
The proposed critical law, coefficient range, local-periodic reduction,
and the asymptotic-coupling theorem are proved within the manuscript.
No novelty claim is inferred from absent search results. The fixed
constant-coupling sequence is distinguished by its zero limiting ratio;
the companion C400 law is not used as an uncited theorem input.

Only the four keys listed above occur in references.bib. The manuscript
contains no uncited bibliography padding, no fabricated arXiv or DOI
identifier, and no preprint-only locator silently assigned to a journal
version. The initial compile receipt records the actual BibTeX and
LaTeX diagnostics after compilation.
