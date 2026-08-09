# R401-VAL-L3 phase-anchor and branch-tube protocol — draft

Protocol identifier: `R401-VAL-L3-S0-DRAFT`  
Date: 2026-08-09 (UTC)  
Authority: **DRAFT / NON_LICENSING**  
Parent result: A4.15 / `PASS_LOCAL_COMPLEMENT_ALL_SLABS`

## 1. Purpose and authority boundary

This draft specifies a representative implementation smoke for the A4.16
phase bridge.  It has two independent subclaims:

- **A4.16a, phase anchor:** every periodic candidate with
  \(T\in[0.64,0.69]\), \(K_\epsilon=1\), and
  \(\sup_{0\le t\le T}r_-(\Phi_\epsilon^t z)<0.06\) has fast winding one and
  exactly one positive \(P_+=0\) crossing in the accepted local root box;
- **A4.16b, branch membership:** the already accepted A4.12 fast branch stays
  in \(r_-<0.04\) over its complete period.

Together with A4.15, these statements imply uniqueness modulo time
translation within the full-period local-tube candidate class.  They do not
show that every global candidate stays in the tube.

The older frozen theorem-domain protocol requested a time-parameterized
phase-cover tree.  This draft prospectively replaces that local gate by a
state-space angular-winding tree plus a separate continuous branch-tube
cover.  No run under this draft can amend a frozen protocol or license a
theorem.  A later production protocol requires an explicit independent
review and machine-readable freeze.

## 2. Frozen-for-smoke model

The runner and checker independently reconstruct the exact algebraic model
from

\[
 a=51/50,\qquad c=2(\sqrt{1+a}-1),
\]

the algebraic orthogonal normal basis, and outward values of
\(\omega_\pm=2\pi\sqrt{\lambda_\pm}\).  They use

\[
 K_\epsilon=\frac{P_-^2+P_+^2}{2}
 +2\pi^2R\operatorname{exprel}(\pi\epsilon^2R)
\]

with \(R=|W_\epsilon(OQ)|^2\).  Decimal approximations to the normal basis
are display values only.

Dyadic geometry is serialized by exact integer numerator/denominator pairs.
Scientific Arb enclosures are serialized as outward decimal ball strings,
reparsed as Arb balls, and required to contain the independent checker’s
recomputation. CAPD transcript endpoints are parsed as exact decimal
rationals before the slow radius is recomputed. JSON duplicate keys,
nonfinite numbers, Boolean/integer aliases, missing fields, extra authority
fields, symlinks, or overwritten proof objects are fatal.

## 3. Representative matrix

The smoke matrix is the exact Cartesian product

\[
 \{\texttt{S000},\texttt{S025},\texttt{S050}\}
 \times\{128,256\}\ \text{MPFR bits}.
\]

The slab endpoints and protected root boxes are read from the accepted L1
plan and rebound by SHA-256.  The representative run may select budgets for a
future all-slab freeze, but it may not promote the other 48 slabs.

## 4. Static outer-domain certificate

For every matrix cell, a no-gap proof object must establish:

1. the outward algebraic enclosure directly proves
   \(0.06/\omega_-<0.015\);
2. \(r_-\le0.06\Rightarrow |Q_-|<0.015, |P_-|\le0.06\);
3. \(K=1\Rightarrow |P_+|<1.415\);
4. with \(W=Aq-a\epsilon q_1^2e_1\), \(W_2=q_1\), and the exact singular
   values of \(A\),

   \[
   |Q_+|\le
   \frac{1/(\sqrt2\pi)+a\epsilon/(2\pi^2)}{\sqrt{\lambda_+}}
   <0.18.
   \]

The fourth implication is evaluated directly with outward algebraic
intervals and rebound by the checker.  A sampled norm estimate or a rounded
stored singular vector is inadmissible.

## 5. Fast-angle state-space tree

The compact root domain is

\[
 E_j\times[-0.015,0.015]\times[-0.18,0.18]
 \times[-0.06,0.06]\times[-1.415,1.415]
\]

in coordinates \((\epsilon,Q_-,Q_+,P_-,P_+)\).  Define

\[
 D_+=\omega_+^2Q_+^2+P_+^2,
 \quad
 N_+=P_+^2+Q_+K_{Q_+},
 \quad
 \nu_+=\omega_+N_+/D_+.
\]

The slab interval (E_j) is carried unchanged through the tree. Only the
four state coordinates ((Q_-,Q_+,P_-,P_+)) are split. Each leaf has exactly
one of the following classifications:

- `ENERGY_EXCLUDED`: the interval enclosure of \(K\) omits 1;
- `TUBE_EXCLUDED`: the lower endpoint of \(r_-^2\) is strictly above
  \(0.06^2\);
- `ANGLE_CERTIFIED`: the leaf intersects neither excluded set and proves
  \(D_+>0\), \(N_+>0\), and \(\nu_+<18\);
- `UNRESOLVED`: non-passing and fatal.

Every internal node is split at an exact dyadic midpoint of the widest
normalized state coordinate, with fixed tie order
\((Q_-,Q_+,P_-,P_+)\). Parent boxes must equal the union of their two
children exactly. No stored `angle_passed` Boolean substitutes for the
interval endpoints. Every proof tree stores total, internal, terminal,
unresolved, and per-class counts plus a canonical content hash. Each `ANGLE`
tree additionally stores the decisive global extrema for \(D_+\), \(N_+\),
\(\omega_+N_+\), and \(\dot\vartheta_+\).

The checker separately proves

\[
 18(0.69)<4\pi
\]

using an outward lower bound for \(\pi\), and replays the winding-number
lemma from the archived inequalities.

## 6. Positive-section landing tree

On

\[
 E_j\times[-0.015,0.015]\times[0,0.18]
 \times[-0.06,0.06],
\]

with \(P_+=0\), the section tree must exclude all constrained shell points
outside \(0.12<Q_+<0.17\).  Its leaves are:

- `ENERGY_EXCLUDED`;
- `TUBE_EXCLUDED`;
- `LANDING_CLOSED_WINDOW`, proving the retained closed section window lies
  in the target landing band;
- `UNRESOLVED`, which is fatal.

Equivalent no-gap implementations may cover the two forbidden shells
\([0,0.12]\) and \([0.17,0.18]\) by energy exclusion and separately certify
the central section band.  Boundary points must be excluded strictly or
split; they may not disappear between half-open conventions.

## 7. Continuous branch-tube certificate

For each selected slab, the runner reads the accepted primary L1 root box
\((Q_-,Q_+,P_-,T)\) and embeds it at \(P_+=0\).  It treats \(\epsilon\) and
\(T\) as constant interval state variables and integrates on normalized time
\(s\in[0,1]\):

\[
 \frac{dZ}{ds}=T X_{K_\epsilon}(Z).
\]

The evaluator must use the pinned CAPD multiprecision Lohner implementation
and `SolutionCurve`, not a floating trajectory.  A frozen dyadic cover of
\([0,1]\), initially 64 phase cells, is evaluated as closed intervals.  On
every cell it must prove

\[
 (\omega_-Q_-)^2+P_-^2<0.04^2.
\]

If a cell is too wide, only prospective dyadic refinement is allowed.  A
run that reaches its phase-depth or wall budget is `UNRESOLVED`; it is not a
negative theorem.  The proof object stores every phase cell, outward state
enclosure, slow-radius upper endpoint, CAPD build identity, evaluator source
hash, binary hash, and raw stdout/stderr hash.

Only the 51 accepted primary L1 boxes are needed in a later all-slab branch
cover; guarded bridge boxes identify branch continuity but do not define new
branch points.

## 8. Producer/checker authority split

The static producer/checker pair may emit only
`PASS_STATIC_COMPONENT_SMOKE`, with `component_scope=STATIC_ONLY` and
`composite_s0_passed=false`. The branch producer/checker pair may emit only
`PASS_NON_LICENSING_BRANCH_TUBE_SMOKE`. Neither component may assign a
composite or theorem status. Each independent checker must not import its
producer module and must independently:

- reconstruct the six-pair matrix and exact L1 input hashes;
- reparse strict JSON and every outward endpoint;
- reconstruct all dyadic root covers and parent--child unions;
- recompute the Hamiltonian, slow radius, \(D_+\), \(N_+\), angular-rate,
  landing, and outer-shell inequalities;
- verify all CAPD branch phase cells and the strict \(0.04^2\) margin;
- verify exact source/binary/transcript hashes and cross-precision domain
  agreement;
- fail on any unresolved, missing, extra, conflicting, or noncanonical
  object.

Only a separate composite packager/checker that binds both independently
accepted components over the identical six-cell matrix may emit
`PASS_IMPLEMENTATION_SMOKE`, with `component_scope=COMPOSITE_S0`,
`composite_s0_passed=true`, and `final_status=null`. It means all six
representative composite records passed. It is not an all-slab A4.16
theorem.

## 9. Smoke budgets and kill conditions

The implemented representative smoke uses:

- static tree maximum depth: 24;
- 250,000 evaluated nodes per static tree;
- branch phase cover: 64 closed dyadic cells;
- Taylor order 24 and tolerance \(10^{-30}\);
- 600-second timeout per six-state CAPD evaluator process.

A future all-slab scheduler must separately freeze worker count, optional
phase refinement depth, crash/resume behavior, a 48 GiB memory high-water
pause, and a 150 GiB free-disk pause. Those operational gates are not claimed
as implemented by the representative component runners.

These values are implementation limits, not mathematical thresholds.  Any
budget hit makes the cell inconclusive.  Before a formal 102-record run,
observed smoke costs may be used once to set larger prospective budgets, then
the protocol and code hashes must be frozen.

Immediate kill conditions are:

- an outer-domain implication cannot be certified;
- any surviving angle leaf permits \(D_+\le0\), \(N_+\le0\), or
  \(\nu_+\ge18\);
- any section candidate can lie outside \((0.12,0.17)\) or loses transverse
  orientation;
- the known branch cannot be enclosed in \(r_-<0.04\);
- 128/256 domains disagree, a proof tree has a gap, or the checker cannot
  reproduce an inequality;
- an implementation requires weakening a gate after reading a held-out
  all-slab outcome.

## 10. Proof-object layout

The implemented smoke archives are

```text
results/r401_val_l3_phase_tube_smoke/
├── summary.json
├── manifest.json
├── proof_{128,256}_{S000,S025,S050}.json
└── independent_checker.json

results/r401_val_l3_branch_tube_smoke/
├── summary.json
├── manifest.json
├── R401_VAL_L3_BRANCH_TUBE_SMOKE_REPORT.md
├── capd_r401_phase_branch_tube_mp
├── compile_stdout.txt
├── compile_stderr.txt
├── raw/{128,256}/{S000,S025,S050}.{txt,stderr.txt}
└── independent_checker.json

results/r401_val_l3_s0_composite/
├── summary.json
├── manifest.json
├── R401_VAL_L3_S0_COMPOSITE_REPORT.md
└── independent_checker.json
```

The final schema may be tightened before smoke execution.  Once the first
authoritative smoke byte is produced, schema or threshold changes require a
new attempt directory; in-place repair is forbidden.

## 11. Non-promotion boundary

Even a six-pair smoke pass does not establish A4.16 on the other 48 slabs.
Even a future all-slab A4.16 pass remains conditional on complete tube
residence for arbitrary candidates.  This protocol does not license the
global shell cover, event-projected determinant, Taylor residual,
\(\delta_{\rm tr}\), \(P_0\), a trace formula, prime data, zeta zeros, a
Hilbert--Polya operator, RH, or an implication toward RH.
