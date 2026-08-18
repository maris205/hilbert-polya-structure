# Paper 44 pre-output isolated integration candidate

This is a portable, result-empty implementation candidate for `SD-C46`, the
q-adic finite-size boundary law for primitive multiplicative shifts of finite
type.  Its only research input is the immutable 17-entry package under
`preauthority/`, bound by manifest SHA-256
`1952daeee561e4b0e1d11795a9638803a288a1eecddab0702ebcfec95816a7fd`.

The package implements two physically distinct evaluators.  Evaluator A
enumerates labelings on literal source-graph components.  Evaluator B uses
independently expanded fixtures, graph-period primitivity, exact word-count
powers, the closed chain histogram, a positive Binet interval series, and
cyclotomic quotient arithmetic.  Neither imports local helpers or reads the
other's fixtures, intermediates, expected tables, or outputs.  The comparator
uses recursive exact type/value equality before canonical-byte comparison;
Boolean/integer/float coercions are never accepted.  It also reconstructs
every finite value, case ID, gamma grid coordinate, adaptive truncation,
canonical rational, analytic tail, and outward interval endpoint.

Finite exact checks and certified interval diagnostics are explicitly not
proof of uniform convergence, the complete accumulation image, all-level
strong separation, or the natural boundary.  Those fields are owned only by
the independent proof-certificate auditor.  Source, type, evaluator
independence, primary Route, independent Route, and frozen whole-tree audits
are separate physical consumers.  The exact Ban--Hu--Lai author-manuscript
correction boundary is preserved in the immutable source files, including
the version-of-record caveat and zero-credit ownership subtraction.

The exact mutation registry has 19 frozen families and 20 concrete instances
(reducible and period-two controls are separate).  Every and only each
instance's designated consumers must return exit `2`, a canonical typed
`REJECT` envelope, and its frozen nonzero code.  Missing, extra, zero-return,
wrong-code, noncanonical, or exception outcomes count as survivors.  Eight
additional disposable mutations test the frozen external auditor itself,
including mode, empty-directory, FIFO, and symlink changes.  A larger release
suite physically exercises typed science records, interval metadata and false
enclosures, registry/check-map structure, mixed or unsafe Route objects,
coordinated re-ledger/re-report attempts, and final-tree kind/mode changes.
The adaptive atanh remainder, Perron-tail bound, internal and serialized
outward-rounding directions, guard-bit counts, Binet truncation, and geometric
tail are frozen literally in `contracts/INTERVAL_CERTIFICATION_CONTRACT.json`;
tail/sign/disjointness/static-byte negative controls are named there.

All runtime artifacts occupy an exact recursive `outputs/` namespace binding
path, kind, mode, and every regular-file hash.  State A uses
preauthority commit sentinels and forbids `PAPER_MANIFEST.sha256`.  State B
requires three equal nonzero lowercase 40-hex commit fields and a physical
whole-tree manifest that excludes itself and the static seal.  The integrity
protocol has only `PRE_CERT` and `FINAL`; FINAL directly reconstructs its
stored certificate byte for byte.  Mixed states reject.  `STOP_DUPLICATE` remains a
conditional external literature disposition, not a Route terminal.

The parent stages two complete byte-identical builds under hostile unrelated
working directories, verifies a legal paired State A/B build and invalid
mixed states, then performs one atomic directory rename.  `--force-late-failure`
stops after validation and before any target write; an exact second run makes
zero physical target writes.  An existing unequal output tree is never
overwritten.

The canonical candidate must not be run in place during preparation and must
contain no `outputs/`, `__pycache__/`, or `.pyc`.  Full smoke is performed only
in a fresh disposable clone.  Once sealed, the ordinary State-A command in a
disposable copy is:

```text
python -I -B code/integration/run_integration.py --state A
```

This directory authorizes no authority write, Git action, root-README edit,
mirror update, registry entry, paper publication, novelty claim, or priority
claim.
