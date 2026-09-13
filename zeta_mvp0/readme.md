# Integrated RH corpus from `prime_dynamics_theory`

This file describes the source-preserving, archival Riemann-hypothesis
(`RH-*`) corpus integrated into `zeta_mvp0` from
[`maris205/prime_dynamics_theory`](https://github.com/maris205/prime_dynamics_theory).
The corpus lives in `papers/`; it is not a `zeta_mvp0/paper_*` package and
does not change the existing Paper 01/02 programme line.

## Scope

The import is pinned to source commit
`02d51d372e9c95ffc2ed36727829363a32cec030` and contains:

- all 403 source directories matching `papers/RH-*`;
- the standalone `papers/RH-ROADMAP-after-RH50.md`;
- the complete source `RH_HANDOFF.md`;
- the Hilbert--Pólya section (lines 1--9) of the source-root `README.md`; and
- the RH-specific source workflow excerpt (lines 55--174) from its `AGENTS.md`,
  preserved as archival data rather than as active target instructions.

The 403 paper directories cover the contiguous `RH-1` through `RH-398`
series plus `RH-MVP1`, `RH-MVP2`, and Volumes 2--4.  Their internal paths,
including source, tests, numerical inputs, PDFs, results, and source-tracked
build records, are retained beneath `papers/`.

## How to read the corpus

Start with
[source provenance](rh_import_metadata/PRIME_DYNAMICS_RH_SOURCE_PROVENANCE.md),
then consult the [source RH handoff](PRIME_DYNAMICS_RH_HANDOFF.md) for the
source programme's own current-state record.  The
[reproduction guide](rh_import_metadata/PRIME_DYNAMICS_RH_REPRODUCE.md) gives
an exact, read-only comparison procedure against the pinned source commit.

The canonical `zeta_mvp0` programme overview and current claim status remain
in the uppercase [README.md](README.md).  This lowercase `readme.md` is only
the navigation entry for the integrated RH corpus.

The import is separate from the existing
[`zeta_mvp1`](../zeta_mvp1/readme.md) overview.  That overview was not
overwritten and is not represented as a byte-identical source document here.

## Status boundary

This is a controlled *reference import*, not an independent review or a new
`zeta_mvp0` research paper.  It does not change the Q, W, \(S_{\rm op}\),
\(P^*_{\rm loc}\), \(P_0\), Z, or RH entries in the programme dashboard or
global claim ledger.  See the
[claim boundary](rh_import_metadata/PRIME_DYNAMICS_RH_CLAIM_BOUNDARY.md).

## Filename compatibility

This directory intentionally contains both the established uppercase
`README.md` and this user-requested lowercase `readme.md`.  They are distinct
files on the current case-sensitive filesystem.  A default case-insensitive
macOS or Windows checkout cannot represent both names; use a case-sensitive
worktree when this exact layout is required.
