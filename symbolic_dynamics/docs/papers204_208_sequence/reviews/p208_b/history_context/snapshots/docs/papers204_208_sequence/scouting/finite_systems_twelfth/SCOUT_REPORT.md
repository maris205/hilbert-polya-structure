# Twelfth bounded scout — closed with no promotion

Date: 2026-09-06 UTC. Owner/author: `batch197_fifth_scout`.
Final disposition: **six desk literals, three executed rules, zero
promotions/reserves/IDs**. No further slate is started by this handoff.

The immutable [intake](INTAKE.md) predates code and fixes all 16 complete
boxes. [Proofs and dispositions](PROOF_AND_DISPOSITION.md) separate complete
generic adapters from unresolved all-parameter claims. The [source record](SOURCE_AND_COLLISION.md)
contains historical exact-rule exclusions, actual query forms, primary
read scopes, two access failures and the unavailable external-tool boundary.
No OFS/triangulation/flip proof content or P207 B input was changed or used.

## Results on the original full boxes

H is maximum entrance time to the recurrent core. Periods list lengths
present, not cycle counts. All exact cycle counts and full witness orbits
are in the complete canonical stdout linked below.

| Rule / parameters | States | First image | Core | H | Periods | Maximum fibre |
|---|---:|---:|---:|---:|---|---:|
| STC n=1 | 1 | 1 | 1 | 0 | 1 | 1 |
| STC n=2 | 2 | 2 | 2 | 0 | 2 | 1 |
| STC n=3 | 8 | 4 | 1 | 2 | 1 | 5 |
| STC n=4 | 64 | 26 | 13 | 3 | 1,2 | 27 |
| STC n=5 | 1,024 | 196 | 1 | 4 | 1 | 364 |
| STC n=6 | 32,768 | 2,762 | 1 | 4 | 1 | 8,260 |
| PCG r=2,p=3, deducted control | 81 | 81 | 81 | 0 | 1,2 | 1 |
| PCG r=2,p=5, deducted control | 625 | 625 | 625 | 0 | 1,2 | 1 |
| PCG r=2,p=7, deducted control | 2,401 | 2,401 | 2,401 | 0 | 1,2 | 1 |
| PCG r=3,p=3 | 19,683 | 5,379 | 2,993 | 6 | 1,2,4,6 | 211 |
| UMP p=3,d=0 | 2 | 1 | 1 | 1 | 1 | 2 |
| UMP p=3,d=1 | 8 | 5 | 2 | 2 | 1 | 4 |
| UMP p=3,d=2 | 512 | 241 | 151 | 2 | 1,2,3 | 56 |
| UMP p=5,d=1 | 32 | 21 | 16 | 2 | 1,2 | 7 |
| UMP p=7,d=1 | 128 | 71 | 57 | 2 | 1,2,3 | 16 |
| UMP p=11,d=1 | 2,048 | 1,035 | 276 | 4 | 1,5,10 | 244 |

Total: **59,387 states in 16 boxes** per run. PCG's r=2 rows are explicitly
old linear controls; they are not three extra novel systems. The three
unexecuted desks are not silently included in any state/assertion count.

## Final dispositions

| Literal | Proven deduction / obstruction | Missing retained conjunction | Disposition |
|---|---|---|---|
| STC | First-step co-bipartite cut adapter; K_n fixed for n>=3; explicit P4/complement two-cycle. | No all-n core/clock or evaluated all-n inverse extremum. | `KILL_INCOMPLETE_GLOBAL_CONJUNCTION` |
| PCG | Complete r=2 involution and characteristic-two adjugation deductions; actual odd-field period-six witness. | No general r,p temporal classification or independent all-target/extremal inverse formula. | `KILL_INCOMPLETE_GLOBAL_CONJUNCTION` |
| UMP | Three-point dynamics completely reduces to an affine scalar/translation action; actual four-point F11 ten-cycle. | No global all-subset core/clock or evaluated inverse/extremal theorem. | `KILL_INCOMPLETE_GLOBAL_CONJUNCTION` |
| SRS | All q odd, second iterate is constant M_2. | Time axis is generic span-erasure; not retained. | `DESK_KILL_GENERIC_ERASURE` |
| NCS | Complete one-step core and all fibres from elementary centralizers. | Entire temporal axis transfers; true inverse does not repair value. | `DESK_KILL_GENERIC_CENTRALIZER` |
| QSZ | All p odd, degree-two root/moment collapse gives entrance <=3 and periods <=2. | Generic time axis and unevaluated static moment inverse. | `DESK_KILL_GENERIC_MOMENT_COLLAPSE` |

All are `NO_PROMOTION`. There is no pending candidate gate to confuse with
an accepted review, and there is no claim that negative finite evidence
proves impossibility of every future theorem about these maps.

## Actual execution evidence

The self-contained [producer](pilot.py) imports only Python standard-library
modules. It exhausts every state in the fixed carriers. STC's spanning-tree
subset-zeta parity is cross-checked against reduced-Laplacian determinants
and the diagonal-cofactor cut at every graph/edge. PCG's permanent-minor
coordinates are cross-checked by independent entry increments. UMP's pair
enumeration is cross-checked by point-reflection counts at every point.
The functional graph is peeled by indegree, and its depth/core is separately
checked against the descending image sets.

The [actual recorder](record_pair.py) was run as
`python -I -B docs/papers204_208_sequence/scouting/finite_systems_twelfth/record_pair.py`.
It created its new output directory exclusively, then ran two fresh child
processes with `-I -B` in separate empty run directories. Runtime probes
record isolated=1, bytecode disabled and optimization zero. Each child's
complete stdout/stderr, command, cwd, exit status and input hashes remain:

* [Run 1 raw canonical](execution_pair_v1/run1/producer.stdout),
  [receipt](execution_pair_v1/run1/receipt.json): 789,402 assertions,
  child exit 0, approximately 3.03 seconds.
* [Run 2 raw canonical](execution_pair_v1/run2/producer.stdout),
  [receipt](execution_pair_v1/run2/receipt.json): 789,402 assertions,
  child exit 0, approximately 3.00 seconds.
* [Actual pair receipt](execution_pair_v1/PAIR_RECEIPT.json): both runtime
  probes and producers exited zero; a distinct actual `cmp -- run1 run2`
  process exited zero; Python byte equality also passed; all three input
  files' before/after hashes agree. Both stderr files are empty.

The complete raw stdout SHA-256 is
`de2e2141ca7f0d01889e4cd5dadda0557e5dd514bf258bfeb16c629f7900bfb7`.
This is raw byte equality, not parsed/normalized JSON equality. There were
no failed scientific executions or source revisions in this pair. The
input-pinning covers intake, producer and recorder; no repository helper
or old verifier was imported. No new PDF, build or visual audit is claimed.

`CONTEXT_INPUTS.sha256` uses **workspace-root-relative** historical paths.
`SHA256SUMS` uses **this-directory-relative** package paths and covers every
nonself file. They have different bases and must be checked accordingly.
The final seal is an integrity check of this author evidence, not a new
mathematical replay, root acceptance or independent review.

## Handoff boundary

Research-lit/idea-creator caused source and generic-owner deductions before
pilot, and proof-writer kept elementary derivations separate from bounded
observations. Their optional external review step was unavailable and was
not fabricated. The report itself is the author closure requested for this
bounded lane; root owns any central index integration. All historical
packages, sealed B materials and central indices remain untouched.
External status remains `HOLD_EXTERNAL`.
