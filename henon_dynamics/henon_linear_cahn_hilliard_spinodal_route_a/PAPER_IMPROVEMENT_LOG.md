# Two-round paper improvement log

## Round 0: core manuscript

The first manuscript stated the arbitrary-dimensional Fourier semigroup,
shell spectrum, stability trichotomy, and compact proof. Its limitation was
that it did not yet expose every boundary and could leave the role of finite
shell enumeration ambiguous.

## Review 1 and implementation

The first hostile review required a theorem-sized advance rather than more
examples. Round 1 added:

- the exact Lyapunov/energy dissipation identity;
- complete Morse index and kernel formulas with lattice multiplicities;
- a global fastest-shell proof by completion of the square and an explicit
  \(\alpha/\kappa\) exhaustion bound;
- tie-preserving spectral projections and actual-support asymptotics;
- the recurrence-to-stationarity proof and the full \(\kappa=0\) trichotomy.

This explicitly prevents the receipt cutoff from masquerading as proof.

## Review 2 and implementation

The second red-team pass attacked evidence semantics and claim boundaries.
Round 2 added:

- exact counts and independent checker/SymPy/replay/mutation lanes;
- a repaired-hash mutation locking `analytic_exhaustion_cutoff` and the
  theorem's `fastest_exhaustion` statement;
- strict JSON/YAML parser and type/key/list defenses;
- collision analysis, Route-A tuple, scope firewall, reproducibility, and
  AI-use disclosure;
- deterministic multi-round PDF and font/text audits.

The final manuscript makes no nonlinear coarsening or novelty claim and
retains self-adjointness only as `A4_FORMAL_HINT`.

## Post-round cross-audit repair

An independent cross-package audit found two documentation defects after
Round 2. The singular \(\kappa=0\) face now states its natural generator
domain explicitly: \(H^2(\mathbb T^d)\cap L^2_0\) when \(\alpha\ne0\), and
all of \(L^2_0\) for the zero generator when \(\alpha=0\). The build
description now correctly counts three round variants, each compiled in two
fresh directories, with `main.pdf` a byte-identical alias of Round 2. These
are scope and reproducibility repairs, not a new manuscript round or a new
mathematical claim; the affected PDFs and the release closure were rebuilt.
