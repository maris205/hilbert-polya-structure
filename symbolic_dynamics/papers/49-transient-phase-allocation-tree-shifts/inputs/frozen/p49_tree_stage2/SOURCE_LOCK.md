# Source and immutable-input lock

## Immutable Stage-1 input

The controlling manifest is
`/tmp/p49_53_phase1/SHA256SUMS.txt` with SHA-256

```text
7fd51d53d077e3d7e0af905eda6bf2d15ee9aa64d6459bf3dcfa1dc282d97ec8
```

Running `sha256sum -c SHA256SUMS.txt` inside `/tmp/p49_53_phase1` returned
`OK` for all 13 entries before Stage-2 work began.  No Stage-1 byte was
modified.  The manifest content is frozen here for audit:

| Immutable path relative to `/tmp/p49_53_phase1` | SHA-256 |
|---|---|
| `BASELINE_AND_SOURCE_BOUNDARY.md` | `47d65772916b1627fe70a60c1c34e3a30eafc0e9fa245f613565215618e7a5c5` |
| `CANDIDATE_UNIVERSE.md` | `acc7c68556bb59be72f0653ce5296ee59d0e1885af222722da86fbbf7f7b2fc2` |
| `CHECKPOINT1_RESPONSE.md` | `e4f726e564de1e522787e9ff213483da7ed00db51a9bae72dd7f0d9a2d267567` |
| `CLAIM_COLLISION_MATRIX.md` | `ab66fc0dfffc4ee4707bcc898d8580726eb665b1df5043773330c1c9fdc833ea` |
| `DEVILS_ADVOCATE_CHECKPOINT_1.md` | `91349680e54f4a9a35d4a0ac3d4cf3dd4752368f21b6d592dc96815bf1bf7106` |
| `DEVILS_ADVOCATE_FINAL_RECHECK.md` | `cd1d36ab2bf55a10fedce2fbb15812ec59ed4d2688dd978da2cb87873f8fa5ed` |
| `FULL_STAGE1_CHECKPOINT.md` | `3b7216ca00d636555fdd6844a1fa4be09b249fb20754552b18ffd895d00cd351` |
| `INDEPENDENT_ARBITRATION.md` | `6516094df5f3049f123027cf3a20efda50c49f9b285cf37c3b6376f23cf820bc` |
| `METHODOLOGY_BLUEPRINT.md` | `295e0644cb72da28f242faf5682f0c28abd1506971b1c61622bca30b75eadb2c` |
| `REPLACEMENT_SEARCH.md` | `ad29aa71b0e3e08a1cf6dad0d890b3a1a57b33984748510d1e907f47862c8c7f` |
| `RESEARCH_QUESTION_BRIEF.md` | `45abd919d013f5931ec29c171a72d5657d1aad470c2a060c44c3a9974baf4155` |
| `SOURCE_VERIFICATION.md` | `cde47eeb346340ee8cb310ed70ac0fea89e692c4be78aa9913424d4cbe938fd5` |
| `SPECIALIZED_FINAL_AUDITS.md` | `396d0d40b0508e5d55d71a84b0d658264f3af4a0bcc3f6d0f02de9d2370650ea` |

The Stage-2 theorem contract is a normalization and proof bridge, not an
amendment to those files.

## Primary-source metadata and owner subtraction

### Hausdorff metric and irreducible owner

Jung-Chao Ban, Guan-Yu Lai, and Yu-Liang Wu, “Hausdorff dimensions of
irreducible Markov hom tree-shifts,” *Journal of the London Mathematical
Society* 111 (2025), Issue 6, e70198; first published 5 June 2025.

- Publisher full text: https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/jlms.70198
- DOI: https://doi.org/10.1112/jlms.70198
- Versioned arXiv record: https://arxiv.org/abs/2401.05320v2
- arXiv v2 date: 4 June 2025.

Owner subtraction: this source owns the rooted-tree metric, irreducible
dimension theory via a nonlinear Perron--Frobenius variational formula, and a
general spectral-radius upper-bound discussion.  It explicitly leaves the
Hausdorff dimension for general, not necessarily irreducible, Markov hom
tree-shifts as a question.  The present package takes no novelty credit for
developing irreducible dimension theory.  Its complete cyclic-block formula
is a self-contained supporting lemma.  The residual object is the exact
transient phase-composition optimizer, its saturation arithmetic, and the
finite-depth approach to saturation.

### Reducible topological-entropy owners

Jung-Chao Ban, Chih-Hung Chang, Wen-Guei Hu, and Yu-Liang Wu, “On structure
of topological entropy for tree-shift of finite type,” *Journal of
Differential Equations* 292 (2021), 325--353.

- DOI: https://doi.org/10.1016/j.jde.2021.05.016
- arXiv: https://arxiv.org/abs/2105.05406

The same authors, “Topological entropy for shifts of finite type over Z and
trees,” *Theoretical Computer Science* 930 (2022), 24--32.

- DOI: https://doi.org/10.1016/j.tcs.2022.07.007
- arXiv: https://arxiv.org/abs/2006.13415

Owner subtraction: these papers own reducible topological-entropy structure,
including the fact that reducible topological entropy can exceed the values
of individual irreducible components.  Therefore the conceptual phrase
“max-component failure” receives no novelty credit here.  The residual claim
is specifically Hausdorff dimension in the BLW tree metric, with an exact
finite phase-allocation formula and matched lower and upper proofs.

## BLW version-risk firewall

The firewall is version-specific and narrow.  It does not assert that every
current publisher rendering contains the same prose.

An independent retrieval of
`https://export.arxiv.org/e-print/2401.05320v2` produced:

```text
arXiv v2 source tar SHA-256:
28e2e8f5b228b4347c96c74c1ca04e68d1c9cfa069d5e4d25f6665b6d679d213

main.tex SHA-256:
176b8d4f427f38dd4b0d1c41c0f1e2270bcc249ef3681494299d1a5f6658da43
```

In those exact `main.tex` bytes, line 182 gives a primitive specialization
to `dim_H=log rho`, while line 188 gives irreducible equality with
`log rho` exactly under uniform row sums.  Since primitive irreducible
zero-one matrices with unequal row sums exist, those two source-text clauses
create a literal tension in arXiv v2.  The Wiley HTML currently exposes the
variational statement and the uniform-row-sum corollary but does not visibly
show the arXiv line-182 specialization in the theorem excerpt.  This package
does not infer the editorial history or label the publisher article
erroneous.

Local verification aids present before Stage 2 were also hashed:

```text
/tmp/2401.05320.pdf
ef59afe6861a8e342ce8660a9ff02a623b72b436387d0460c73a31c72c0f1055

/tmp/2401.05320.txt
b17287fd03171b05eac2af5fb260fbf570e4d7083e5d293b01cffc43bdfb5a60
```

They identify themselves as arXiv v2 and contain the same two clauses.  They
are not copied into this package.

Firewall rule: no proof in `PROOF_PACKAGE.md` invokes the BLW primitive
specialization, the equality characterization, or the general spectral
upper bound.  The metric and object vocabulary are imported; all dimension
equalities in the theorem contract are derived directly from exact cylinder
counts and a compatible uniform conditional measure.

## Search and priority boundary

The primary-source search is bounded and claim-shaped.  It supports owner
subtraction and the statement that no exact transient phase-allocation
formula was located during Stage 1.  It does not support “first,” “priority,”
or exhaustive-novelty language.  This Stage-2 package is not a manuscript or
publication candidate.
