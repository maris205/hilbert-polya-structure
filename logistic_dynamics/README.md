# Logistic-origin HP-Dynamics

This directory is the unified shareable archive for the HP-Dynamics research
programme that began with Logistic-map and non-autonomous Logistic
constructions.  The search later broadened to symbolic suspensions, renewal
systems, magnetic quantum graphs, and a target-free Hénon/FIO branch.  Those
breadth pivots are retained here because they answer the same Route-A question
and inherit the same source-lock and determinant-ledger rules.

The full laboratory repository remains
[`maris205/riemann_dyna`](https://github.com/maris205/riemann_dyna).  This
stream is its curated, source-locked publication mirror: stable checkpoints
are copied byte-for-byte, organized one stage per project directory, and bound
to the main-repository commit by hashes.

## Start here

- [`STAGE_INDEX.md`](STAGE_INDEX.md): complete generated inventory of all
  synchronized stages.
- [`sync_manifest.yaml`](sync_manifest.yaml): authoritative source paths,
  project mapping, status, paper boundary, and source commit.
- [`SYNC_POLICY.md`](SYNC_POLICY.md): what is mirrored, what remains external,
  and how future checkpoints are promoted.
- [`tools/sync_from_riemann_dyna.py`](tools/sync_from_riemann_dyna.py):
  deterministic synchronizer and drift checker.

The current freeze contains 31 project records:

| Class | Count | Treatment |
|---|---:|---|
| Published paper stages | 7 | Existing manuscript and compiled-paper directories are preserved |
| Planned result/obstruction papers | 19 | Each has a narrative report and claim-bounded paper plan |
| Results integrated into LOG-0001 | 2 | Retained as independent prerequisites without duplicate papers |
| Archive/control/diagnostic stages | 3 | No paper is opened and no theorem promotion is implied |

## Research progression

```text
legacy Logistic zero-matching numerics
        ↓
data-leakage and stability audit
        ↓
exact-U_c physical return structure and ACIP weights
        ↓
intrinsic polar roof and complex inverse branches
        ↓
LOG-0001 nuclear Fredholm determinant and growth theorems
        ↓
breadth pivots: symbolic / renewal / quantum graph / Hénon-FIO
        ↓
reusable obstructions and next structurally distinct candidate
```

The early notebooks are kept as historical evidence, not as current Route-A
candidates.  Numerical zero matching, USTC/GUE comparisons, fitted smoothing,
and post-hoc unfolding do not enter any promoted candidate definition.

## Unified project layout

New synchronized stages use this layout:

```text
projects/<stage_slug>/
├── README.md
├── source_lock.yaml
├── route_a_evaluation.yaml       # omitted only for pre-evaluation archives
├── SOURCE_PROVENANCE.yaml
├── NARRATIVE_REPORT.md           # result/obstruction stages only
├── PAPER_PLAN.md                 # paper-eligible stages only
├── configs/                      # repository-compatible copied paths
├── evaluations/
├── experiments/
├── tests/
├── artifacts/
├── formal/
├── results/
│   └── SOURCE_HASHES.sha256
└── obstructions/
```

Older published projects also contain `src/`, compatibility copies, and
`paper/`.  They are preserved rather than destructively normalized.  Their
new `SOURCE_PROVENANCE.yaml` record states which copied files are canonical.

## Synchronization

From the root of this repository, with `riemann_dyna` checked out as a sibling
directory:

```bash
python3 logistic_dynamics/tools/sync_from_riemann_dyna.py --check
```

To synchronize after intentionally updating `sync_manifest.yaml` to a new
main-repository commit:

```bash
python3 logistic_dynamics/tools/sync_from_riemann_dyna.py
python3 logistic_dynamics/tools/sync_from_riemann_dyna.py --check
```

The tool never deletes files and never rewrites hand-maintained manuscripts.
It fails if the source Git commit differs from the manifest or if any copied
file drifts from its recorded source.

## Promotion and paper policy

A stage receives a paper plan only when it contains at least one of:

- a genuine theorem edge;
- a certified reproducible result;
- a formal candidate with a stable source lock;
- a strict reusable obstruction;
- a meaningful negative result that changes the search frontier.

Audit-only, superseded, control, and external-dependency stages remain visible
but do not receive synthetic manuscripts.  One stage directory corresponds to
one paper-sized mathematical claim boundary; later corrections create a new
version or explicitly supersede the earlier stage.

## Global claim boundary

No stage in this stream currently proves a completed-xi determinant identity,
constructs a self-adjoint Hilbert–Pólya operator, proves the Riemann
Hypothesis, or authorizes Route B.  A correct zero-count order, a natural
unitary lift, finite numerical zero matching, or GUE statistics is not a
substitute for the exact prime-power trace and completed-xi divisor gates.

Canonical SSH remotes:

```text
source research: git@github.com:maris205/riemann_dyna.git
shareable mirror: git@github.com:maris205/hilbert-polya-structure.git
```
