# P214 primary-source bibliography and attribution limits

Prepared 2026-09-11 UTC by
`/root/p212_minimal_s0_independent_source_audit/p214_primary_bibliography`.
Status: `TWO_PRIMARY_CITATIONS_VERIFIED / SOURCE_PREPARATION_ONLY`.
This is a bounded bibliography check, not a manuscript review, a candidate
gate, a novelty clearance, or verification of P214's mathematical proof.

The controlling scope was read directly from the
[admitted theorem contract](../../../docs/papers211_215_sequence/qa/fresh55_root_reception01/THEOREM_CONTRACT.md),
[Fresh55 desk](../../../docs/papers211_215_sequence/scouting/finite_residual_fresh55/DESK.md)
and [collision note](../../../docs/papers211_215_sequence/scouting/finite_residual_fresh55/COLLISION_NOTE.md).
The research-lit skill guided primary-source retrieval and separation of
publication metadata from the claims actually read. The repository research
skill limited this work to the admitted source-preparation obligation.

## Verified publication records

| Final key | Primary-verified bibliographic fields | Retrieved citation data |
|---|---|---|
| `Bors2017` | Alexander Bors, *On the dynamics of endomorphisms of finite groups*, Applicable Algebra in Engineering, Communication and Computing **28**(3), 205–214 (2017), DOI `10.1007/s00200-016-0304-9` | [Publisher BibTeX export](https://citation-needed.springer.com/v2/references/10.1007/s00200-016-0304-9?format=bibtex&flavour=citation), independently checked against the publisher page and citation meta tags; [actual lookup responses](BORS_LOOKUP_RESPONSES.json). |
| `ElAbdalaouiEtAl2016` | El Houcein El Abdalaoui, Sylvain Bonnot, Ali Messaoudi and Olivier Sester, *On the Fibonacci complex dynamical systems*, Discrete and Continuous Dynamical Systems **36**(5), 2449–2471 (2016), DOI `10.3934/dcds.2016.36.2449` | Actual DOI content negotiation with `Accept: application/x-bibtex`, checked against the publisher page and printed PDF banner/byline; [actual lookup responses and passage-read record](FIBONACCI_LOOKUP_RESPONSES.json). |

The entries in [references.bib](../references.bib) derive from these actual
responses, not from remembered or synthetic bibliographic templates.

Publication-date distinctions and all editorial transformations:

- Bors: publisher issue date June 2017; first online publication 17 September
  2016. The DOI/Crossref BibTeX response uses `Bors_2016` and year 2016,
  whereas the publisher's own BibTeX uses `Bors2017` and year 2017. The latter
  is retained for the journal citation. Both successful responses are saved.
- El Abdalaoui et al.: journal issue May 2016; publisher reports online
  publication October 2015; arXiv:1304.4864 is the 17 April 2013 preprint.
  The formal journal citation is used, not the preprint year.
- The DOI export parses the first author as `Abdalaoui, El Houcein El`.
  The editable entry uses `El Abdalaoui, El Houcein`; this follows the full
  publisher byline and the printed p. 2450 running head `E. H. EL ABDALAOUI`.
  This disclosed surname normalization does not change the displayed person.
- Formatting only: custom second key, braces protecting `Fibonacci`, ASCII
  BibTeX page-range dashes, HTTPS DOI URLs, reordered fields, and omission of
  abstract/ISSN/publisher/date fields not needed by this short bibliography.
  No author, title, venue, volume, issue, page, DOI or issue year is invented.

## Claim-bearing primary passages actually read

### Bors: finite-group endomorphisms, not a theorem about F

Read the [publisher's full text](https://link.springer.com/article/10.1007/s00200-016-0304-9),
Sections 1–2, especially the finite-dynamical-group restriction preceding
Theorem 1, Theorem 1(1)–(4), Definition 1 and Theorem 2 with its proof.
Theorem 1 gives nilpotent/periodic structure for a finite-group endomorphism;
Theorem 2 imposes rigid procreation on its reversed state graph. The source
does not assert these conclusions for arbitrary nonlinear finite maps.

Recommended manuscript prose:

> For finite-group endomorphisms, Bors describes the decomposition into
> nilpotent and periodic parts and proves rigidity of the reversed state
> graph [Bors2017, Theorems 1–2].

The P214 unequal-positive-fibre obstruction is elementary and should be
proved in the manuscript: a homomorphism's nonempty fibres are kernel
cosets. Do not describe this source as proving the clock, the inverse
formula, or nonconjugacy of the particular nonlinear map F.

### El Abdalaoui et al.: the old complex polynomial template

Read the [publisher page](https://www.aimsciences.org/article/doi/10.3934/dcds.2016.36.2449)
and [published PDF](https://www.aimsciences.org/data/article/export-pdf?id=2ce0402e-91a2-48b1-8ea3-762f77d957e4),
printed pp. 2449–2450. Section 1, second paragraph on p. 2449 explicitly
defines the complex map `H_c(x,y)=(xy+c,x)`. Definition 1.1, equation (1),
on p. 2450 separately gives the multiplicative-Fibonacci scalar recurrence.
The PDF was streamed through a two-page text extraction; no fulltext file
was retained. This is an actual selected-passage read, not a full-paper audit.

Recommended manuscript prose:

> El Abdalaoui et al. study the complex multiplicative-Fibonacci maps
> H_c(x,y)=(xy+c,x) [ElAbdalaouiEtAl2016, p. 2449]. At c=0, swapping
> coordinates yields M(a,b)=(b,ab). Our comparison uses this polynomial
> template, not a transfer of complex dynamical results to the finite ring.

The coordinate calculation is a local observation: for S(a,b)=(b,a),
`S H_0 S = M`. The separate P214 identity `F=QMP` and the distinction
between two-sided equivalence and dynamical conjugacy are P214's explicit
algebraic calculations, not claims attributed to the cited source. No
finite-ring extinction theorem or finite-ring fibre census was established
by the inspected complex-dynamics passages.

## Bounded selection and operational limits

Two references suffice for the intended distinct roles. The optional
Wei–Xu–Zou source was checked via its
[publisher record](https://link.springer.com/article/10.1007/s00200-016-0290-y)
and [arXiv full-text introduction and Lemma 2.1](https://arxiv.org/html/1709.08579v1).
It concerns module endomorphisms and cycle algorithms over finite
commutative rings; that does not add a necessary claim to this short
manuscript's broader finite-group comparison. It is therefore deliberately
omitted, not presented as a third verified BibTeX entry or as a theorem
supporting F. Its publication year is 2016 despite the 2017 arXiv upload.

The read-only child `fibonacci_primary_check` independently retrieved the
second source's metadata and first two published pages before the present
source author repeated those primary checks. This is source assistance,
not a manuscript-review panel. The child's web PDF open failed with a tool
safety error and an institutional-copy request timed out; direct publisher
HTTP streaming succeeded. Here an initial guessed Fresh55 contract path
failed and was resolved to the linked root-admission contract. Local
`literature/`, `tools/` and the new paper directory initially did not exist;
those failed discovery paths are not source coverage. No matching configured
Zotero/Obsidian tool or local arXiv fetch script was found; direct arXiv
pages and publisher sources were used. Large recovery-state displays were
truncated, so no complete historical-index read is claimed.
The local-link existence check passed. `jq` was unavailable (exit 127);
the two saved JSON records were then read and parsed successfully with
the orchestration environment's `JSON.parse`, without importing or executing
scientific code. The bibliography was checked as source text only; no
BibTeX or TeX build is claimed.

Only this paper's new `sources/` records and `references.bib` are owned by
this subtask. No manuscript, scientific verifier/import/run, canonical,
build/compile, central index, P212 mathematics, Git state, external upload,
or specialist contact was changed. The temporal proof remains self-contained.
