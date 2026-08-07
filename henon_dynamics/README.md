# Hilbert–Pólya dynamical structure exploration

This directory is the continuously updated Hénon-dynamics research track of
the Hilbert–Pólya Structure Exploration project.  It starts from the original
area-preserving Hénon manuscript, but treats every proposed bridge to
arithmetic or spectral structure as a hypothesis to be tested rather than an
assumption.

The working style is breadth-first:

```text
candidate dynamics
    -> exact periodic/symbolic structure
    -> weighted dynamical zeta
    -> transfer/operator test
    -> Route-A or Route-B decision
```

Positive constructions, obstructions, and well-scoped failures are all kept.
Chronological products are preserved in non-autonomous systems; they are not
replaced by averaged transition matrices.

## Entry points

- [`propose.md`](propose.md) — research framework and workflow.
- [`docs/prior_work/README.md`](docs/prior_work/README.md) — earlier papers and
  experiments.
- [`docs/related_programs/README.md`](docs/related_programs/README.md) — related
  dynamical-zeta and transfer-operator programs.
- [`docs/candidate_registry.md`](docs/candidate_registry.md) — candidate and
  closure registry.
- [`docs/obstruction_registry.md`](docs/obstruction_registry.md) — reusable
  no-go mechanisms.
- [`next_paper_henon_candidate_search/`](next_paper_henon_candidate_search/) —
  breadth-first candidate generation and paper planning.
- [`skills/`](skills/) — Route-A and Route-B evaluation rules used by this
  research track.

The foundational local source is
[`5-An Area-Preserving Henon-Map Model.pdf`](docs/prior_work/papers/5-An%20Area-Preserving%20Henon-Map%20Model.pdf).

## Current theorem packages

| Project | Main result | Hilbert–Pólya status |
|---|---|---|
| [`henon_instability_roof_zeta/`](henon_instability_roof_zeta/) | Certified Hénon survivor and instability-roof clock | Current HP gate negative |
| [`henon_pinning_trace_obstruction/`](henon_pinning_trace_obstruction/) | Exact pinning-kernel and sign obstructions | Route-A rejected |
| [`henon_frobenius_scheme_obstruction/`](henon_frobenius_scheme_obstruction/) | Fixed-period Frobenius/local-zeta collapse | Scoped obstruction |
| [`henon_dihedral_chronology_obstruction/`](henon_dihedral_chronology_obstruction/) | Loss of chronology under coarse dihedral quotienting | Scoped obstruction |
| [`fibonacci_trace_map_clock_obstruction/`](fibonacci_trace_map_clock_obstruction/) | Trace-map clock and analytic-germ obstructions | Route-A rejected |
| [`s_integer_solenoid_chronology_zeta/`](s_integer_solenoid_chronology_zeta/) | Same-Parikh returns with rational versus natural-boundary zeta; full-zeta continuation | Structural theorem; Route-A rejected |
| [`nonabelian_voltage_zeta_obstruction/`](nonabelian_voltage_zeta_obstruction/) | Order collapse, finite-roof zero density, and exact-conductor branch return | Scoped obstruction; Route-A rejected |
| [`s_arithmetic_height_clock_obstruction/`](s_arithmetic_height_clock_obstruction/) | Explicit real/tree clock, near-wall divergence, canonical Weil height, and bounded-Hecke Weyl obstruction | Worked arithmetic example; Route-A rejected |
| [`modular_scattering_clock_obstruction/`](modular_scattering_clock_obstruction/) | Modular open-channel zeta arithmetic, denominator-only repetition no-go, and stable Selberg closure | Scoped obstruction; Route-A rejected |
| [`modular_open_trace_obstruction/`](modular_open_trace_obstruction/) | Algebraic endpoint coboundary, full-boundary Selberg periods, commuting squarefree scattering channels, and projector scope boundary | Scoped obstruction; Route-A rejected |

## Latest result: HCS-C18

The latest paper tests the two standard escapes left open by HCS-C17:
retaining rational endpoints and retaining all squarefree congruence cusp
channels. Unoriented open scattering geodesics retain the exact positive
control

\[
Z_{\rm sc}(s;T_0)=\frac{T_0^{-2s}}2\left[
\frac{\zeta(2s-1)}{\zeta(2s)}
+\frac{\zeta(2s)L(2s,\chi_{-4})}{\zeta(4s)}\right],
\]

but the section-induced endpoint clock is an algebraic/set-theoretic
coboundary on \(\mathbb P^1(\mathbb Q)\). On the full real boundary, its
nonzero loop periods are exactly the signed hyperbolic translation lengths;
this classifies period support and does not by itself construct a determinant.

Independently, the standard squarefree \(\Gamma_0(N)\) scattering family has
a fixed Walsh basis in the frozen Huxley--Hejhal width normalization. Bare
products at distinct spectral parameters are therefore permutation-invariant.
This is a conditional matrix-product diagnostic, not an identification of the
spectral parameter with time. Rank-one cusp projectors leave the commutative
algebra and give certified parameter-to-edge assignment and path sensitivity;
no primitive path law or Fredholm determinant is inferred.

- [Project overview](modular_open_trace_obstruction/README.md)
- [Compiled paper](modular_open_trace_obstruction/paper/main.pdf)
- [Derivation package](modular_open_trace_obstruction/DERIVATION_PACKAGE.md)
- [Certificate producer](modular_open_trace_obstruction/code/open_trace.py)
- [Independent checker](modular_open_trace_obstruction/code/independent_check.py)
- [Route-A record](modular_open_trace_obstruction/evaluations/route_a/hcs_c18/evaluation.yaml)

Reproduce its frozen artifacts with:

```bash
cd modular_open_trace_obstruction
python code/open_trace.py --output results
python code/independent_check.py --results results \
  --output results/independent_check.json
python -m unittest discover -s code -p 'test_*.py' -v
```

## Mirrored-data boundary

The related `henon_weighted_zeta` source, scripts, final paper, and compact
R058/R059 certificates are mirrored here.  Its large historical R052--R061
matrix/NPZ sweeps are deliberately not mirrored; the complete historical test
suite expects those local data assets and is therefore not a code-only CI
target.  The data-independent source tests can be run with:

```bash
cd docs/related_programs/henon_weighted_zeta
python -m pytest -q \
  tests/test_controls.py tests/test_geometry.py tests/test_homotopy.py \
  tests/test_interval_cover.py tests/test_operator.py tests/test_orbits.py \
  tests/test_precision.py tests/test_subdivided_cover.py tests/test_zeta.py
```

At the current snapshot this subset passes 45/45 tests.  Artifact-dependent
claims should instead be checked against the compact certificates and hashes
retained by their consuming theorem packages.

## Update discipline

When a research round reaches a meaningful stage:

1. add or update its project-level `README.md`;
2. keep exact code, compact result certificates, and independent checks;
3. append rather than overwrite formal Route-A evaluation records;
4. update the candidate, obstruction, and related-program registries;
5. state explicitly what is proved, what failed, and what remains open.

Regenerable caches, nested Git metadata, TeX auxiliary files, and bulky raw
array dumps are intentionally excluded from synchronization.  Papers,
source, compact certificates, and audit records remain versioned.

Last synchronized research snapshot: **2026-08-07**.
