# Independent bounded review: geometry symbolic certificate

2026-09-07. Reviewer: the positive-characteristic scout, not the author of
the nonlinear-geometry package. This is current-team internal review, not
human peer review, a worldwide novelty audit, or authority to admit a paper.

## Claim, status and exact review scope

**PASS within the bounded executable-certificate scope; no remaining
blocking defect found in the final four scripts.** The producer repaired
the concrete evidence-scope issues identified during this review. This
finding does not turn the certificate into an automatic proof of the
entire rational-periodic classification.

The reviewed claim is that the scripts establish exact affine identities,
integer-progression counts, endpoint complements and selected signed-cycle
identities for every allowed radius, rather than merely agreeing with a
finite list of numerical-radius functional graphs. All four scripts were
read completely. The geometry proof was read as context, especially its
Steps 2–8 and Appendix A; the coordinator separately owns the full
mathematical/source/substance adjudication.

The family uses $d\ge3$ odd, $R=(d+1)/2\ge2$, $R=3q+s$, and
$s\in\{0,1,2\}$. Here $q\ge1$ for $s=0,1$, and $q\ge0$ for $s=2$.
For $r=R\bmod6$, the least radii are respectively $6,7,2,3,4,5$.
The local recurrence is $(x,y)\mapsto(y,-x+s_d(y))$, with the polynomial
and integer core/boundary values fixed in the proof. The certificate's
use of these values is checked for internal consistency; this review does
not independently certify external source ownership or replace the proof's
rational-integrality and escape arguments.

## Frozen inputs

All paths in this table are relative to
`henon_dynamics/research_c414_c418/nonlinear_geometry/`.

| Input | SHA256 |
|---|---|
| `symbolic_bulk.py` | `7a99667d25790a65cdbce9b429577350c65e7038c5aac00e663a5e7ab3789691` |
| `symbolic_boundary.py` | `af7491291cb6292c044bad6ddceaa7f76ba0146110ceca6fd473347308350fea` |
| `symbolic_corners.py` | `8d878ed3f4b639b63f5d674ca11b85818bce5ef9b9317626f23f9fbde6f6010d` |
| `verify_symbolic_certificate.py` | `0377f99976173cf0e4d177e0793de49ce8bbecf0565cb4fa47b49aef697b98fb` |
| `PROOF_PACKAGE.md`, context and proof-side dependencies | `a1a0c8fbd2ff8b1fbd3bc73606c8dd435c727fe914cbf907d9e55d7f8c9891e0` |

The four script digests were read before and after the final certificate
run, and again after the distinct reviewer check. All four were unchanged.
The producer's final two proof clarifications concern explicit source
ownership and the negative-phase parametrization pointer; their final
paragraphs and the resulting proof digest were actually inspected. No code
input changed with those prose clarifications.

## Dependency map and concrete findings

### 1. Bulk assertions genuinely quantify free lattice variables and radius

`symbolic_bulk.py` represents a coordinate by an exact integer triple
$(a,b,c)$ for $ax+by+c$, retaining $x,y$ as free integers in their fixed
residue classes. All 36 residue pairs are processed. Equality of coefficient
triples at the return time proves an identity on the whole cell. The
60-step bound is a failure guard, not a cutoff on $R$ or on the lattice
points: failure to close would raise an assertion.

Every intermediate coordinate is asserted to be $\pm x+c$ or $\pm y+c$.
The intersections of its exact $[-R,R]$ constraints give the rectangle
offsets. Proper-divisor return tests solve two linear equations over exact
rationals. Inconsistent singular systems are excluded explicitly; a
consistent rank-one family would fail the checker rather than be omitted.
An earlier least period must divide the already established cell period,
so testing its proper divisors is sufficient.

For $R=6m+r$, each one-coordinate progression count is exactly $2m+c_r$.
The checker compares polynomial coefficients after multiplying these
counts, subtracting central exceptions and dividing by the actual generic
period. It checks nonnegativity at the least admissible $m$; thereafter
the slope is positive. There is no fitted polynomial or omitted
positive-part correction.

The final verifier explicitly checks the entire orbit radius of each of
the 17 central exceptional points, not merely their starting coordinates.
Their radius is at most two, justifying their subtraction for every
$R\ge2$. The separate reviewer command below also checks the negative
phase on the correctly transformed set, not on reused positive-phase
point labels.

### 2. Strip inequalities prove entire radius progressions

`symbolic_boundary.py` uses $(a,b,c)$ for $aR+bx+c$. Both $R$ and $x$
remain indeterminates; residue evaluations only select the appropriate
integer value of the six-periodic sequence. Every intermediate bulk use
records an exact interval condition on $x$, or an inequality on $R$.

For a coordinate $\pm R+c$ on the bulk side, the nontrivial condition is
a monotone lower bound on $R$. Constants are checked against the least
radius. The final first-return assertion checks every intermediate
second coordinate is in the core before its first boundary return.
The 36 computed rules are compared with the compressed proof table,
including time, translated coordinate, output level and sign.

Testing a linear inequality at its least permitted radius is sufficient
here because its favorable slope is explicitly known; it is not evidence
from one numerical orbit. No unsupported substitution of a small $R$ for
the free variable is used in the recurrence identities.

### 3. Corner coverage was a real review finding and is now checked exactly

Initially, the verifier checked selected corner cycles but did not call an
exhaustive-complement check. The original endpoint generator also used a
broad bounded offset loop without expressing its completeness argument.
The producer replaced this with the exact complements of every strip.

For each residue, the full inner section interval is $[-R-2,R+2]$ and
the generic interval is $[-R+L,R+U]$. Its two complements have precisely
the offsets

$$[-2,L-1]\text{ at }-R,\qquad [U+1,2]\text{ at }+R,$$

filtered by the coordinate residue. The implementation checks
$2R_{\min}+U-L\ge0$, so their separation holds throughout the increasing
radius progression. The outer layer is reduced by the exact next-coordinate
condition $2R+s-x\le R+2$, namely $x\ge R+s-2$. Thus its only
non-immediately-escaping starts are $(R+c,R+2)$ with $s-2\le c\le2$.

The final `verify_corner_coverage` checks equality of this derived set with
all endpoint-table keys, every endpoint return row, the subsequent escape
of the recorded inadmissible outer targets, and the coefficient-level
identity between full-section count, strip count and complement size.
The complement sizes are $11,10,9$, repeated across the paired classes
$r$ and $r+3$: 30 symbolic endpoint rows, each valid on two progressions.

Pairwise same-level endpoint differences are affine in $R$. The producer
checks a strict sign condition at the least $R$ whose slope preserves that
sign thereafter. Independently, the reviewer solved their possible equality
equations exactly over $\mathbb Q$ and excluded every root lying in an
admissible progression. All 128 same-level pair comparisons passed. This
addresses small-radius label aliases instead of assuming distinct formal
labels always represent distinct lattice points.

### 4. Cardinalities are derived, with the proof-side graph obligations retained

The initial total-count check summed two hand-entered component tables.
The final version instead starts from the actual bulk coefficient output,
the checked signed constant-corner cycles and the exact strip progression
counts. The resulting total is compared coefficient by coefficient with
the claimed polynomial after $q=2m+\lfloor r/3\rfloor$.

The expected counts were also derived independently during this review:

- When $s=0$, the stationary section coordinates are the $2q+1$ multiples
  of three in $[-R,R]$. Their negative time-two returns contribute
  $4(2q+1)$ points. The constant endpoint cycles contribute $4+2\cdot14$.
  The boundary total is therefore $8q+36$.
- When $s=1$, the stationary progression from $-R+8$ through $R-6$ in
  steps of six has $q-1$ points, including the empty case $q=1$. The
  constant cycles contribute $2\cdot6+2\cdot16$. The interleaved growing
  strings have $q+1$ and $q$ nodes, giving normalized time
  $1+2(q+1)+6q=8q+3$ and negative sign. Their lift contributes $16q+6$
  points. Together this is $52q+14$.
- When $s=2$, the paired progression from $-R+5$ through $R-5$ in steps
  of six has $q$ points, including the empty case $q=0$. Its two lifts
  contribute $16q$ points. The constant cycles add $2\cdot4+6$, giving
  $16q+14$.

Weighting the bulk multiplicities by their periods independently gives
$36q^2-28q$, $36q^2-4q$ and $36q^2+36q$. Adding the appropriate
boundary expression and the 17 central points gives exactly

$$36q^2-20q+53,\quad36q^2+48q+31,\quad36q^2+52q+31.$$

The code confirms the node counts and time/sign arithmetic. It does **not**
by itself prove that the selected normalized cycles and the growing string
exhaust every other strip trajectory. The exact translations, escape
routing, uniqueness and closure of the growing chain are proof-side
arguments in Steps 5–7. I checked those stated progressions against the
certificate for this review; the coordinator's full-proof adjudication is
separate. A selected-cycle check must not be relabeled as an automatic
exhaustive graph proof.

### 5. Small radii and coincident cycle lengths

The least-radius inequalities above include every progression's first
member. The $q-1$ and $q$ families vanish at their correct first values,
not at an ad hoc asymptotic cutoff. Uniform-formula substitutions at
$R=2,3,4$ give $31,69,115$ points. These arithmetic substitutions do not
enumerate the corresponding functional graphs.

The growing period is $16q+6\ge22$. All other periods are at most 20
except 36, and $16q+6=36$ would require nonintegral $q=15/8$. Thus the
growing cycle has no accidental period coincidence at a permitted radius.
The repeated periods four or six in the additive tables come from
core-avoiding-section and boundary-meeting cycles, which are disjoint
classes in the proof. They must be added rather than deduplicated.

## Actual commands and results

All commands in this section ran from
`/root/autodl-tmp/hilbert-polya-structure/henon_dynamics/research_c414_c418/nonlinear_geometry`.
Python was 3.12.3 with optimization flag zero. The scripts use exact
standard-library arithmetic. No package install, external model API,
GPU job, old-batch rerun, or numerical-radius graph census was performed.

The input-integrity command, actually run before and after the check, was

```bash
sha256sum symbolic_bulk.py symbolic_boundary.py symbolic_corners.py verify_symbolic_certificate.py
```

It exited zero both times and printed the four digests above. The final
context digest was obtained with the same command plus `PROOF_PACKAGE.md`.

The final producer certificate was executed **once**, with an explicit
non-assert guard against Python assertion suppression:

```bash
python -B -c 'import sys, runpy; print("Python", sys.version.split()[0], "optimize", sys.flags.optimize); sys.flags.optimize == 0 or sys.exit("Assertions are disabled"); runpy.run_path("verify_symbolic_certificate.py", run_name="__main__")'
```

Actual stdout, exit status zero:

```text
Python 3.12.3 optimize 0
PASS: 36 affine bulk cells, all 36 affine boundary strips,
      exact endpoint complements, disjointness at every admissible R,
      all endpoint return rows and all constant endpoint cycles,
      central cycles, progression-derived boundary cardinalities,
      and exact total cardinality polynomials.
No numerical degree graph was enumerated by this certificate.
```

The distinct reviewer-only check below reconstructs the central sets from
the displayed cycles, evaluates both phase recurrences directly, solves
endpoint alias equations by exact fractions rather than the producer's
monotone-sign test, and independently weights the cycle-table polynomials.
It imports only the endpoint set constructor from the producer; it does
not rerun the full producer certificate or use its claimed totals as the
calculation of those totals.

The first attempt at this one-off reviewer command had a missing closing
parenthesis in a conditional `boundary` expression. Python rejected the
command at parse time with exit one and
`SyntaxError: '(' was never closed` at line 52; no mathematical check in
that attempt ran. The expression was replaced by the explicit dictionary
below. This correction affected only the reviewer command, not any input
file, and did not cause another producer-certificate run.

```bash
python -B -c '
import sys
from collections import Counter
from fractions import Fraction
from itertools import combinations
from symbolic_corners import corner_starts
if sys.flags.optimize:
    raise RuntimeError("Assertions are disabled")
sigma = (0, 1, 1, 0, -1, -1)
five = {(0, 2), (2, 1), (1, -1), (-1, -2), (-2, 0)}
six = {(0, 1), (1, 1), (1, 0), (0, -1), (-1, -1), (-1, 0)}
central = {(0, 0)} | five | {(-x, -y) for x, y in five} | six
assert len(central) == 17
for phase, expected in ((1, {1: 1, 5: 10, 6: 6}), (-1, {1: 1, 3: 6, 10: 10})):
    points = central if phase == 1 else {(-x, y) for x, y in central}
    periods = Counter()
    for start in points:
        point = start
        for elapsed in range(1, 11):
            assert max(map(abs, point)) <= 2
            x, y = point
            point = (y, -x + phase * sigma[y % 6])
            if point == start:
                periods[elapsed] += 1
                break
        else:
            raise AssertionError((phase, start, "no return"))
    assert dict(periods) == expected
    print("central phase", phase, "point counts by least period", dict(sorted(periods.items())))
counts = []
comparisons = 0
for r in range(6):
    minimum = r if r >= 2 else r + 6
    starts = corner_starts(r)
    counts.append(len(starts))
    for (a, c, level), (b, e, other_level) in combinations(starts, 2):
        if level != other_level:
            continue
        comparisons += 1
        if a == b:
            assert c != e
        else:
            possible = Fraction(e - c, a - b)
            admissible = possible.denominator == 1 and possible >= minimum and possible % 6 == r
            assert not admissible, (r, possible, (a, c, level), (b, e, other_level))
assert counts == [11, 10, 9, 11, 10, 9]
print("endpoint complement sizes", counts, "exact affine alias equations excluded", comparisons)
plus, minus = (1, 1, 0), (1, -1, 0)
expected = ((36, -20, 53), (36, 48, 31), (36, 52, 31))
boundaries = {
    0: [(4, (0, 2, 2)), (14, (0, 0, 2))],
    1: [(6, (0, 0, 2)), (16, (0, 0, 2)), (36, (0, 1, -1))],
    2: [(4, (0, 0, 2)), (6, (0, 0, 1)), (8, (0, 2, 0))],
}
for s in range(3):
    cycles = [(4, plus), (12, minus if s == 0 else plus), (20, plus if s == 2 else minus)]
    totals = tuple(sum(period * coefficients[j] for period, coefficients in cycles + boundaries[s])
                   + (17 if j == 2 else 0) + ((0, 16, 6)[j] if s == 1 else 0)
                   for j in range(3))
    assert totals == expected[s]
    print("independent weighted-cycle coefficients s =", s, totals)
for radius, q, s, expected_count in ((2, 0, 2, 31), (3, 1, 0, 69), (4, 1, 1, 115)):
    a, b, c = expected[s]
    assert a * q * q + b * q + c == expected_count
print("smallest-radius formula substitutions R = 2, 3, 4 give 31, 69, 115; no radius graph enumeration")
'
```

Actual stdout of the corrected reviewer command, exit status zero:

```text
central phase 1 point counts by least period {1: 1, 5: 10, 6: 6}
central phase -1 point counts by least period {1: 1, 3: 6, 10: 10}
endpoint complement sizes [11, 10, 9, 11, 10, 9] exact affine alias equations excluded 128
independent weighted-cycle coefficients s = 0 (36, -20, 53)
independent weighted-cycle coefficients s = 1 (36, 48, 31)
independent weighted-cycle coefficients s = 2 (36, 52, 31)
smallest-radius formula substitutions R = 2, 3, 4 give 31, 69, 115; no radius graph enumeration
```

## Handoff and open scope

The final certificate is evidence for the explicitly reviewed symbolic
claims on every admissible progression. No remaining certificate repair
is requested. Repeating this successful run on unchanged code is not
needed. A change to the recurrence, strip constraints, endpoint table,
counting logic or claimed scope would invalidate the affected finding.

Full escape-routing/growing-chain exhaustion, external ownership, theorem
substance, Route A evaluation and admission remain the coordinator's
separate gates. The final proof now explicitly credits the published
positive-phase bulk classification and its 17 exceptions; this review
checked the clarification's presence, not the external primary text.
No source result is promoted to target Euler factors, root numbers,
automorphy, a target divisor correspondence or a Hilbert–Pólya operator.

The repository workflow and proof-writer skill guided quantifier, boundary
and dependency checks. Their influence was substantive: the review caused
the producer to replace an assumed endpoint cutoff and hand-entered totals
with exact complements and derived counts. The reviewer changed no producer
code, manuscript, registry, state file, frozen tree or Git object; this
independent review record is the only file written for this task.
