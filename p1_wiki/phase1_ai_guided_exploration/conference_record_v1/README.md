# Conference-oriented Phase-I research record v1

This is a new, external-facing presentation of the Phase-I Hilbert--Pólya / arithmetic-dynamics research record.  It is deliberately separate from the source-bound internal working-paper package in [the parent directory](../README.md): that older package preserves the historical evidence-corpus snapshot, whereas this package recasts the same bounded record as a generic, conference-oriented methodology paper.

The paper is not a proof of the Riemann Hypothesis (RH), a completed Hilbert--Pólya realization, a prime-power trace formula, a completed-Ξ determinant identity, or a spectral identification of Riemann zeros.  It is a research-record and candidate-search methodology paper.

## Paper

> **AI-Guided Exploration of Arithmetic Dynamical Systems: Constraints, Failure Modes, and Search Strategies toward Hilbert--Pólya Structures**

**Author.** Liang Wang<br>
School of Artificial Intelligence and Automation, Huazhong University of Science and Technology, Wuhan 430070, P.R. China<br>
wangliang.f@gmail.com

- [Compiled PDF](latex/manuscript.pdf)
- [LaTeX front matter](latex/manuscript.tex), [body](latex/body.tex), and [bibliography](latex/references.bib)
- [Build script](latex/build.sh)
- [Citation and claim audit](citation-audit.md)
- [Paper-configuration record](paper-configuration.md)

The repository address used in the manuscript is <https://github.com/maris205/hilbert-polya-structure>.

## What changed from the internal research record

The argument and its nonclaims are retained, but the organization now follows a conventional short-paper arc:

1. External motivation from carefully bounded examples of AI-assisted mathematics.
2. The updated RH roadmap as an evidence-obligation architecture, not a progress chart.
3. A six-direction Phase-I evidence landscape, expressed graphically rather than as a claimed common score.
4. A lineage-constrained candidate-engineering protocol for the next round.
5. Detailed direction-by-direction material and provenance in appendices.

The paper makes the user-specified search constraint explicit: a main candidate cannot be a generic dynamical system with primes pasted onto it later.  It must record a traceable **prime-symbolic ancestor**, the non-autonomous deformation, conservative/dimensional lift, geometric realization, or other transformation being used, and the precise arithmetic mechanism that is preserved, changed, or shown to fail.  A system without this ledger is an **external control**, not a main candidate.

The paper's roadmap asset is a release-local copy at [assets/rh_roadmap.png](assets/rh_roadmap.png), SHA-256 `f5e70c5120474702e4f0715bce90c7a88fd5936164594e8b37a2ee0993549d1d`.  It is byte-identical to the Round-2 roadmap reference, while the older internal paper deliberately retains its historical roadmap asset.

## Research boundary and provenance

The detailed Phase-I narrative is bounded to the source-corpus snapshot
`419ee36c1e310469209f7b83c096ec8aea448386` (2026-09-13 UTC).  This package and its updated roadmap are later presentation artifacts; they do not revise historical source locks, route dispositions, or stopping conditions.

The prime-symbolic search genealogy is grounded in the internal [Prior Work Guide](../../../flow_systems/docs/prior_work/README.md), which records the progression from prime/composite observables and symbolic admissibility, through non-autonomous dynamics and Logistic limitations, toward conservative Hénon/symplectic geometry and prime-side operator-geometry benchmarks.  That guide supplies a search-space provenance constraint; it does not prove that any proposed descendant already realizes prime dynamics.

## Reproducible build

The PDF is a generic two-column A4 rendering, intentionally not a named conference's template.  From `latex/`, run:

```bash
./build.sh
```

The build requires LuaLaTeX, BibTeX, TeX Gyre Termes, TikZ, and `pdfinfo`.  It writes transient files to `latex/build/` and replaces the tracked `latex/manuscript.pdf` only after the compilation steps complete successfully.

Before an actual submission, the author should adapt the format to the chosen venue, make an anonymous version if the venue is double-blind, complete funding and competing-interest declarations, and create an immutable Git tag or release for the cited record.  This package is not submitted, peer reviewed, or assigned a publication venue.
