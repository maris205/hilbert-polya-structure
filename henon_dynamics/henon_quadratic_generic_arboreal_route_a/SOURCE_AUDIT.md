# C393 source and provenance audit

Frozen baseline `0c877206d202f732e21ea0b194f9c7fdf30467ee`;
evaluator v0.2.0 SHA256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.
Date 2026-09-05. Scope `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Primary owners and theorem inputs

- R. W. K. Odoni, *The Galois Theory of Iterates and Composites of
  Polynomials*, Proceedings LMS s3-51(3), 385–414 (1985).
  [Publisher DOI](https://doi.org/10.1112/plms/s3-51.3.385) and
  programmatically fetched CrossRef BibTeX confirmed metadata.
  This credits the classical iteration/Galois framework; the new-branch
  proof for the frozen polynomial is provided in full, not attributed to
  an unread specific numbered Odoni theorem.
- Richard Pink, *Profinite iterated monodromy groups arising from quadratic
  morphisms with infinite postcritical orbits*, preprint (2013),
  [arXiv:1309.5804](https://arxiv.org/abs/1309.5804).
  Actual arXiv abstract and the author's ETH publication listing checked.
  This is credited for the broader quadratic-monodromy framework; its
  abstract explicitly does not say every non-PCF quadratic rational map
  has full tree group. No unverified blanket theorem is imported.
- Jamie Juul, Pär Kurlberg, Kalyani Madhu and Tom J. Tucker,
  *Wreath Products and Proportions of Periodic Points*,
  IMRN 2016(13), 3944–3969 (2016; online 2015),
  [DOI 10.1093/imrn/rnv273](https://doi.org/10.1093/imrn/rnv273).
  [Publisher record](https://academic.oup.com/imrn/article/2016/13/3944/2451547),
  author institution record and CrossRef BibTeX checked. CrossRef's
  online year 2015 is distinguished from issue year 2016.
  The actual [arXiv full text](https://arxiv.org/pdf/1410.3378) was read at
  Theorem 3.1, Lemma 5.2, Proposition 5.3 and Section 5's function-field
  Chebotarev estimate (printed pages 12–14 in that accessed preprint).
  The author's published-PDF link returned 502; no claim that this separate
  PDF was read is made.

The fixed-level finite-field Chebotarev/Weil theorem is an explicitly imported
classical input, not proved by residue polynomial samples. The full-group
proof, branch-genus calculation, cycle recursion and ordered limit deduction
are supplied directly. The classical periodic-density mechanism belongs to
Juul–Kurlberg–Madhu–Tucker; the paper claims a project source completion,
not a new general density theorem or a literature-priority certificate.

## Collision screen

C374 is a numerical-basepoint power-map radical/cyclotomic tower with affine
index-two image; C34 is finite wreath data; C369 is a fixed S4 atlas.
None owns this generic all-height nonabelian group and complete new-branch
genus/cycle/finite-field closure. Searches covered Odoni, quadratic critical
orbits, Pink's infinite postcritical monodromy, arboreal surveys and the
wreath-product periodic-density literature. They do not prove absence of
all prior special-case statements.

## Exact claim boundary

Generic t is not every numerical specialization. Good primes depend on
height through B_n, including c_0=0. Each finite field forces a later
critical collision. Chebotarev is fixed-height; the proof takes the prime
limsup first, then the height limit. No rate in p or uniform-all-height
statement is inferred. Frobenius cycles are not original-map primitive
trajectories with manually assigned log-prime periods.

Current-team C382 agent actually read the full proof and independently
checked inertia, the full kernel, genus and limit ordering; no blocking
issue was found. Root separately reviewed the source ownership and code.
The actual symbolic backend failure and repair are retained in the seven-mode
audit, not reframed as a novel insight. No external/human review occurred.
