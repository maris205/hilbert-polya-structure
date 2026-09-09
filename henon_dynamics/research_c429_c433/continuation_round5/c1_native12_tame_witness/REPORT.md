# R5-C1 — native 12/24 witness in the integral tame group

2026-09-10 UTC. Complementary author task for the single R5-C2 exact-spectrum question; not an independent paper candidate.

## Frozen target and first mechanism

Construct an explicitly specified $T\in\operatorname{TA}_2(\mathbb Z)$ and twelve pairwise distinct integer points $P_0,\ldots,P_{11}$ with $T(P_i)=P_{i+1\bmod12}$. An exact 24-cycle is also sufficient to obtain a 12-cycle for $T^2$, whose full word then becomes the specified native map. One tick is always one entire selected word. No modular cycle, unproved interpolation, or clock relabeling is accepted as an integer witness.

The first mechanism is a finite configuration acted on by two explicit integral triangular/affine involutions. Their alternating matchings must compose to a 12-cycle; polynomial values effecting the matchings must be genuinely interpolable over $\mathbb Z$, not only over $\mathbb Q$. The general rational interpolation shortcut is not assumed. Failure of this mechanism would not exclude 12 in the full tame group.

The complete class-reduction proof in `../c2_composition_exact_spectrum/PROOF_SUPPLEMENT.md`, §§1–4, has been read. Its finite-orbit degree padding may be imported after a genuine tame witness is constructed; it preserves the native permutation point for point. Its new 16-exclusion and the old 90,000-pair bounded diagnostic are not rerun. C2 owns the complementary 9 direction; this task only targets 12/24.

Current status: **NOT CURRENTLY JUSTIFIED for the full native-12/24 construction.** The three hand-proved mechanism boundaries below and one complete finite-family diagnostic are finished. Exactly one mathematical program execution was individually released by the coordinator after actual full-code reading; it found no target cycle. No general exclusion or paper admission follows.

## Proved mechanism boundaries

[PROOF_PACKAGE.md](PROOF_PACKAGE.md) contains complete hand proofs, not search conclusions:

1. If one triangular involution center is integral affine on the selected orbit inputs, the two-involution product transports injectively into a single integral Hénon map at integer points. C428 excludes native $12/24$ there. For $p(t)=kt+c$, $k\ne0$, the explicit change is $L(x,y)=(ky-x+c,x)$, giving scalar polynomial $kq(t)-2t+2c$; $k=0$ directly forces period at most two.
2. An alternating staircase with both coordinate-level lists nonconstant arithmetic progressions is impossible: the interpolation conditions imply both $a\mid2c$ and $6c^3\mid a$ for nonzero spacings $a,c$.
3. The twelve-vertex staircase with $x$ levels any permutation of $0,\ldots,5$ and $y$ levels any permutation of $0,\ldots,6$ is impossible. Bounds on finite differences force the seven-value interpolant to be at most quadratic; all four genuine quadratic candidates contradict the endpoint/total-sum identities; the affine remainder falls under the first lemma.

These are exact exclusions of stated mechanisms. They do not exclude arbitrary coordinate levels, repeated-height matchings, more factors, or native $12/24$ in the full tame group. C2's independently authorized nine-point permutation diagnostic is not repeated here.

## Single dual-quadratic diagnostic — COMPLETE, NO TARGET WITNESS

### Discriminating question and frozen inputs

For the complete finite parameter family

$$0\le A,B\le100,\qquad p_A(t)=t^2-A,\qquad q_B(t)=t^2-B,$$

does

$$T_{A,B}=J_{p_A}\circ I_{q_B},\qquad T_{A,B}(x,y)=\bigl((x^2-B-y)^2-A-x,\ x^2-B-y\bigr)$$

have an integer orbit of native least period $12$ or $24$? All $10,201$ ordered pairs, including the $101$ diagonal pairs $A=B$, are retained. This is one targeted witness diagnostic. A negative answer is only an exclusion for this explicit finite coefficient family, not for unrestricted tame words or all quadratic constants.

The original $90,000$-pair program is not rerun. This family explores larger negative constants, and the state box here is proved to contain every integer periodic orbit of each selected map, not simply imposed as a search window.

### Complete native and intermediate height bound

On a periodic native orbit, write $T_{A,B}(x_i,y_i)=(x_{i+1},y_{i+1})$. Then

$$x_i^2-B=y_i+y_{i+1},\qquad y_{i+1}^2-A=x_i+x_{i+1}.\tag{7}$$

The intermediate image under $I_{q_B}$ is exactly $(x_i,y_{i+1})$. Thus every intermediate coordinate is already a coordinate in the native cyclic collection. Let $M$ be the maximum real absolute value of any native coordinate; it is also the maximum over native and intermediate coordinates.

If the maximum is attained by some $x_i$, the first equation in (7) gives $M^2\le B+2M$. If it is attained by a $y_j$, the second equation with index $j-1$ gives $M^2\le A+2M$. Therefore

$$M^2\le2M+\max(A,B)\le2M+100,$$

so $M\le1+\sqrt{101}<12$. In particular all native and intermediate points lie in $[-12,12]^2\cap\mathbb Z^2$. This conservative box has $625$ states. Cycles are exactly the directed cycles of the partial map retaining an edge only when its native image is in the box. The graph decomposition has no guessed period cutoff.

### Exact Hénon word and conjugacy direction

Put $S(x,y)=(y,x)$ and $H_f(x,y)=(y,f(y)-x)$. Direct substitution gives

$$W_{A,B}=H_{p_A}\circ H_{q_B}=S\circ T_{A,B}\circ S.$$

Thus the integer swap $S$ sends a native $T$ cycle to a native $W$ cycle with the same least period. In the displayed word, the rightmost factor $H_{q_B}$ is applied first, then $H_{p_A}$; both are already nonlinear integral Hénon factors with determinant $+1$. On the swapped input $(y_i,x_i)$, the first Hénon intermediate state is $(x_i,y_{i+1})$, exactly the triangular intermediate state from (7). The diagnostic prints the complete native and intermediate state lists for the first witness of each target period, if any, together with complete cycle counts for the entire finite family. It does not print an uncontrolled list of all duplicate witnesses.

### Cost and release boundary

One CPU, one process, at most $625\cdot10,201=6,375,625$ pair-state map constructions plus finite graph traversal, all exact integers. Pre-run estimate: under $15$ seconds; hard wall-clock cap: $30$ seconds. The code reads and writes no project files and makes no network call. A timeout reports only fully completed parameter pairs, not a completed family. There is no automatic coefficient expansion, repeat run, or independent-check claim. Preparation and execution were separately approved by the coordinator, with execution released only after actual full reading of this report and the complete source. The original preparation-date label is 2026-09-10; the executable environment's unchanged timestamp is reported verbatim below.

### Complete prepared code

<!-- BEGIN R5_C1_DUAL_QUADRATIC_SOURCE -->
```python
import datetime
import json
import signal
import sys
import time


class DiagnosticTimeout(Exception):
    pass


def timeout_handler(signum, frame):
    raise DiagnosticTimeout("30-second wall-clock budget reached")


def witness_record(A, B, canonical, states):
    native = [states[index] for index in canonical]
    intermediate = [(x, x * x - B - y) for x, y in native]
    swapped = [(y, x) for x, y in native]
    period = len(native)
    assert len(set(native)) == period
    for index, (x, y) in enumerate(native):
        middle = intermediate[index]
        expected = native[(index + 1) % period]
        assert middle == (x, expected[1])
        assert (middle[1] * middle[1] - A - x, middle[1]) == expected
        assert (swapped[index][1], swapped[index][1] ** 2 - B - swapped[index][0]) == middle
        assert (middle[1], middle[1] ** 2 - A - middle[0]) == swapped[(index + 1) % period]
    return {
        "A": A,
        "B": B,
        "native_period": period,
        "native_map": "T = J_p composed with I_q",
        "T_native_states": [list(point) for point in native],
        "I_q_intermediate_states": [list(point) for point in intermediate],
        "conjugacy": "W = S composed with T composed with S, S(x,y)=(y,x)",
        "W_order": "H_q first, H_p second; each H_f(x,y)=(y,f(y)-x)",
        "first_H_q_coefficients_ascending": [-B, 0, 1],
        "second_H_p_coefficients_ascending": [-A, 0, 1],
        "W_native_states": [list(point) for point in swapped],
        "first_H_q_intermediate_states": [list(point) for point in intermediate],
        "verification": "All native edges, first-factor edges, closing edge and distinct states checked exactly in this run; not an independent implementation.",
    }


def run():
    radius = 12
    side = 2 * radius + 1
    states = [(x, y) for x in range(-radius, radius + 1)
              for y in range(-radius, radius + 1)]
    planned_pairs = 101 * 101
    completed_pairs = 0
    diagonal_pairs = 0
    pairs_with_cycles = 0
    total_cycle_occurrences = 0
    cycle_counts = {}
    diagonal_counts = {}
    target_counts = {12: 0, 24: 0}
    first_witnesses = {}
    status = "COMPLETE"
    error = None
    started_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
    started = time.perf_counter()
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.setitimer(signal.ITIMER_REAL, 30.0)
    try:
        assert len(states) == 625
        for A in range(101):
            for B in range(101):
                images = []
                for x, y in states:
                    next_y = x * x - B - y
                    if -radius <= next_y <= radius:
                        next_x = next_y * next_y - A - x
                        if -radius <= next_x <= radius:
                            images.append((next_x + radius) * side + next_y + radius)
                        else:
                            images.append(-1)
                    else:
                        images.append(-1)

                done = [False] * len(states)
                pair_counts = {}
                pair_targets = {}
                for start in range(len(states)):
                    if done[start]:
                        continue
                    path = []
                    position = {}
                    current = start
                    while (current >= 0 and not done[current]
                           and current not in position):
                        position[current] = len(path)
                        path.append(current)
                        current = images[current]
                    if current >= 0 and current in position:
                        cycle = path[position[current]:]
                        period = len(cycle)
                        pair_counts[period] = pair_counts.get(period, 0) + 1
                        if period in target_counts and period not in first_witnesses and period not in pair_targets:
                            pivot = cycle.index(min(cycle))
                            canonical = tuple(cycle[pivot:] + cycle[:pivot])
                            pair_targets[period] = witness_record(A, B, canonical, states)
                    for vertex in path:
                        done[vertex] = True

                assert all(done)
                # Commit only a fully traversed parameter pair. Timeout counts
                # therefore describe completed pairs, never a partial last pair.
                # Defer the alarm only for this short counter commit, so an
                # interrupted receipt cannot mix committed counts with an
                # uncommitted completed-pair counter.
                old_mask = signal.pthread_sigmask(signal.SIG_BLOCK, {signal.SIGALRM})
                try:
                    for period, count in pair_counts.items():
                        cycle_counts[period] = cycle_counts.get(period, 0) + count
                        if period in target_counts:
                            target_counts[period] += count
                        if A == B:
                            diagonal_counts[period] = diagonal_counts.get(period, 0) + count
                    first_witnesses.update(pair_targets)
                    total_cycle_occurrences += sum(pair_counts.values())
                    pairs_with_cycles += int(bool(pair_counts))
                    diagonal_pairs += int(A == B)
                    completed_pairs += 1
                finally:
                    signal.pthread_sigmask(signal.SIG_SETMASK, old_mask)

        assert completed_pairs == planned_pairs
        assert diagonal_pairs == 101
        assert total_cycle_occurrences == sum(cycle_counts.values())
    except DiagnosticTimeout as exc:
        status = "TIMEOUT_PARTIAL"
        error = str(exc)
    except Exception as exc:
        status = "ERROR_PARTIAL"
        error = repr(exc)
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0.0)

    receipt = {
        "status": status,
        "error": error,
        "started_utc": started_utc,
        "elapsed_seconds": round(time.perf_counter() - started, 9),
        "python_version": sys.version,
        "input": {
            "A_inclusive": [0, 100],
            "B_inclusive": [0, 100],
            "p": "t^2-A",
            "q": "t^2-B",
            "native_map": "T=J_p composed with I_q",
            "target_periods": [12, 24],
            "ordered_pairs_including_diagonal": planned_pairs,
            "native_and_intermediate_box": [-radius, radius],
            "state_count": len(states),
            "planned_pair_state_constructions": planned_pairs * len(states),
            "wall_clock_budget_seconds": 30,
        },
        "completed_ordered_pairs": completed_pairs,
        "completed_diagonal_control_pairs": diagonal_pairs,
        "completed_pairs_with_cycles": pairs_with_cycles,
        "total_cycle_occurrences": total_cycle_occurrences,
        "cycle_occurrences_by_native_period": {
            str(period): cycle_counts[period] for period in sorted(cycle_counts)
        },
        "diagonal_control_cycle_occurrences_by_native_period": {
            str(period): diagonal_counts[period] for period in sorted(diagonal_counts)
        },
        "diagonal_periods_subset_of_1_2_3": set(diagonal_counts).issubset({1, 2, 3}),
        "target_cycle_occurrences": {
            str(period): target_counts[period] for period in sorted(target_counts)
        },
        "first_target_witnesses": [
            first_witnesses[period] for period in sorted(first_witnesses)
        ],
        "scope": (
            "On COMPLETE, the proved height bound makes this all integer cycles "
            "for exactly the stated 10,201 parameter maps. A missing target "
            "does not exclude it for other constants, other centers or tame words. "
            "On a partial status, counters refer only to completed parameter pairs."
        ),
    }
    print(json.dumps(receipt, indent=2, sort_keys=True), flush=True)
    return 0 if status == "COMPLETE" else (124 if status == "TIMEOUT_PARTIAL" else 1)


if __name__ == "__main__":
    sys.exit(run())
```
<!-- END R5_C1_DUAL_QUADRATIC_SOURCE -->

### Single-run provenance and exact receipt

The coordinator bound the permitted extracted source to SHA-256

```text
acaa8a811a329dec8206f33a0e920bf4b644871b01cd3a782f29d63130a38608
```

The following read-only extraction/hash check returned that exact digest, with exit code `0`, immediately before the run. Working directory for both commands: `/root/autodl-tmp/hilbert-polya-structure`.

```bash
awk '/^<!-- BEGIN R5_C1_DUAL_QUADRATIC_SOURCE -->$/{capture=1;next} /^<!-- END R5_C1_DUAL_QUADRATIC_SOURCE -->$/{capture=0} capture && !/^```/{print}' henon_dynamics/research_c429_c433/continuation_round5/c1_native12_tame_witness/REPORT.md | sha256sum
```

Actual execution command, run exactly once:

```bash
set -o pipefail
awk '/^<!-- BEGIN R5_C1_DUAL_QUADRATIC_SOURCE -->$/{capture=1;next} /^<!-- END R5_C1_DUAL_QUADRATIC_SOURCE -->$/{capture=0} capture && !/^```/{print}' henon_dynamics/research_c429_c433/continuation_round5/c1_native12_tame_witness/REPORT.md | python
```

The execution tool returned `exit_code: 0` and `wall_time_seconds: 3.576800944`; its enclosing orchestration displayed `Wall time 3.9 seconds`. The program's separate `elapsed_seconds` and UTC timestamp are preserved without normalization in the full standard-output JSON below. These are different reported timing fields, not claimed to be identical measurements.

```json
{
  "completed_diagonal_control_pairs": 101,
  "completed_ordered_pairs": 10201,
  "completed_pairs_with_cycles": 689,
  "cycle_occurrences_by_native_period": {
    "1": 286,
    "2": 546,
    "3": 37
  },
  "diagonal_control_cycle_occurrences_by_native_period": {
    "1": 38,
    "2": 20,
    "3": 19
  },
  "diagonal_periods_subset_of_1_2_3": true,
  "elapsed_seconds": 3.69179403,
  "error": null,
  "first_target_witnesses": [],
  "input": {
    "A_inclusive": [
      0,
      100
    ],
    "B_inclusive": [
      0,
      100
    ],
    "native_and_intermediate_box": [
      -12,
      12
    ],
    "native_map": "T=J_p composed with I_q",
    "ordered_pairs_including_diagonal": 10201,
    "p": "t^2-A",
    "planned_pair_state_constructions": 6375625,
    "q": "t^2-B",
    "state_count": 625,
    "target_periods": [
      12,
      24
    ],
    "wall_clock_budget_seconds": 30
  },
  "python_version": "3.12.3 | packaged by Anaconda, Inc. | (main, Apr 19 2024, 16:50:38) [GCC 11.2.0]",
  "scope": "On COMPLETE, the proved height bound makes this all integer cycles for exactly the stated 10,201 parameter maps. A missing target does not exclude it for other constants, other centers or tame words. On a partial status, counters refer only to completed parameter pairs.",
  "started_utc": "2026-09-09T16:52:06.257436+00:00",
  "status": "COMPLETE",
  "target_cycle_occurrences": {
    "12": 0,
    "24": 0
  },
  "total_cycle_occurrences": 869
}
```

Thus all $10,201$ parameter pairs were completed, with $689$ pairs having an integer cycle and $869$ total cycle occurrences, counted once per cycle per parameter pair. Their native periods are only $1,2,3$, with counts $286,546,37$. The $101$ diagonal controls contribute counts $38,20,19$ respectively and satisfy the expected period subset. There is no native-$12$ or native-$24$ witness in this full finite parameter family. Completeness uses the proved height bound, not an assumed search radius; the computational result is not an independent implementation or hand classification. No further run, parameter expansion, older diagnostic rerun, or general-spectrum claim was made. The unrestricted tame-group $12/24$ problem remains open here.

## E1 correction response for the original C1 scout

I mistakenly treated an old E1 correction message as current authority and briefly changed one sentence in the frozen `../../lanes/c1_integer_valued_cubic/PROOF_PACKAGE.md`, Step 2. The coordinator restored the frozen HEAD bytes and reported a successful exact diff check for that file. The suggested clarification is retained only here for future quotation: the resulting maximum $E_p(P)$ is nonnegative, although individual entries in its defining maximum can be negative. No mathematical formula changed. The complete original C1-UB3 question remains open. No additional review or old-file modification is undertaken.
