# R5-C2 — Exact universal spectrum of integral Hénon words

2026-09-09 UTC. This is the coordinator's explicitly authorized **new** question, not a replacement of the first-pass C2 boundedness question. Current status: **UNIFORM 16-EXCLUSION AUTHOR-PROVED, PENDING INDEPENDENT REVIEW; EXACT SPECTRUM NOT YET PROVED**. One authorized finite diagnostic is complete.

## 1. Exact single candidate

Let $\mathcal H$ consist of all maps

$$
W=H_{r-1}\circ\cdots\circ H_0,\qquad r\ge1,\qquad
H_i(x,y)=(y,f_i(y)-\varepsilon_i x),
$$

where every $\varepsilon_i\in\{1,-1\}$ and every $f_i\in\mathbb Z[t]$ has degree at least two. There is no bound on the finite word length, degrees or coefficient heights. Define

$$
\mathcal S=\{n\ge1:\exists W\in\mathcal H,\ P\in\mathbb Z^2,
\ \operatorname{per}_W(P)=n\}.
$$

One full $W$ is one native tick. The task is to determine **all of $\mathcal S$**, with exact attainment and uniform exclusion, as a single theorem. Determinant signs are not separate candidates or papers. No phase-augmentation clock is used.

Imported bounds, already owned by C428 and Pezda, give

$$
\{1,2,3,4,6,8\}\subseteq\mathcal S\subseteq
\mathcal P:=\{1,2,3,4,6,8,9,12,16,18,24\}.
$$

At the initial freeze the unclassified lengths were precisely $9,12,16,18,24$. The direct proof added in Section 8 now excludes 16 uniformly at author-proof level, independently of the diagnostic; independent review is pending. The lengths $9,12,18,24$ remain unclassified. Success still means proving membership or nonmembership for every original missing length, with no coefficient/word window promoted to a universal result. A failure to find witnesses is not an exclusion. If the source screen yields a theorem already identifying this exact class/spectrum, this candidate is rejected as source-owned. Partial classifications and unsupported interpolation extensions do not complete the original question or justify its admission.

## 2. Bounded source/collision screen

The first-pass C2 report and its accepted collision are read-only inputs. New targeted searches covered polynomial automorphisms over the integers, tame integral automorphisms, exact cycles, interpolation and Pezda's construction. Relevant local matches remained C428, the prior C2 rejection and the good-model lane's Pezda source notes. No previously admitted exact all-word spectrum theorem was identified among the inspected repository matches.

| Source and actual access | Owned result / scope limit |
| --- | --- |
| T. Pezda, *On cycles and orbits of polynomial mappings $\mathbb Z^2\mapsto\mathbb Z^2$*, 2002, [primary original article](https://dml.cz/bitstream/handle/10338.dmlcz/120574/ActaOstrav_10-2002-1_10.pdf). Previously verified definitions/Theorem 2.1; newly reread Proposition 3.7 and start/end of Section 4 through a read-only PDF-text stream. | The exact upper list $\mathcal P$ for general polynomial maps is fully source-owned. The displayed elementary local four- and six-cycles use invertible linear maps. The extra lengths are obtained by combining local cycle lengths with residue cycles and using a general local–global theorem. The 2002 text does **not** display integral Hénon words attaining $9,12,16,18,24$, nor assert that its gluing preserves polynomial invertibility. |
| T. Pezda, *Cycles of polynomial mappings in several variables over rings of integers in finite extensions of the rationals*, Acta Arith. 108(2) (2003), 127–146, [publisher PDF](https://www.impan.pl/shop/en/publication/transaction/download/product/83956). Actual definition, Theorem 3.2 and its Section 9 proof read via a read-only PDF-text stream. | Theorem 3.2 identifies possible cycle lengths for **polynomial maps** with the intersection of local possibilities when $N\ge2$. The interpolation/gluing proof does not give a tame-automorphism or constant-Jacobian conclusion. Applying it to $\mathcal H$ requires a new theorem, not a change of terminology. |
| C428, actual theorem and secant/interpolation/graph proof, read in the first-pass C2 investigation. | All-degree single-factor spectrum and its six-length union are imported; neither a new boundedness claim nor the old eight-cycle is an increment. |
| C.-M. Lam and J.-T. Yu, *Tame and wild coordinates of $\mathbb Z[x,y]$*, J. Algebra 279(2) (2004), 425–436; [publisher metadata/abstract](https://www.sciencedirect.com/science/article/pii/S0021869304000754). Search-visible publisher record accessed; direct browser reopening failed. | Coordinate/tame-coordinate recognition and construction over $\mathbb Z$ are a different problem. The title and abstract also warn against identifying all integral plane automorphisms with the integral tame subgroup merely from Jung's theorem over a field. No exact period-spectrum result was found in the accessed abstract. Full theorem text not claimed read. |
| M. El Kahoui, N. Essamaoui and M. Ouali, *Interpolation in the Automorphism Group of a Polynomial Ring*, Algebra Colloq. 27(3) (2020), 587–598, DOI 10.1142/S1005386720000486. Bibliographic locator found; primary DOI access attempted. | The discovery abstract concerns the reduction homomorphism $SA_n(R)\to SA_n(R/\mathfrak a)$, not exact interpolation of a cyclic permutation on an integral finite point configuration. No unverified stronger extension theorem is imported. |
| A. Borisov, O. Gabber and A. Vasiu, *Infinite transitivity of tame groups of automorphisms of affine spaces*, arXiv:2609.00391v1, [primary abstract/version record](https://arxiv.org/abs/2609.00391). Abstract accessed; HTML fetch refused for excessive content length. | This newly posted preprint concerns finite fields. Finite-field transitivity cannot by itself produce an exact periodic integer orbit of a lifted word. Full text not claimed read, and no integral interpolation consequence is inferred. |

This bounded screen did not locate an exact theorem settling $\mathcal S$. That is not a global novelty certificate. It does establish that Pezda's 2002 proof cannot simply be cited as having already exhibited the missing lengths inside the required class.

## 3. Proof routes retained and rejected

The complete success route is a uniform arithmetic exclusion for every unattainable length together with exact integral Hénon-word witnesses for every remaining length, combined with the imported universal upper theorem. The new 16-exclusion supplies one part of that obligation. A few examples or a partial exclusion without the full spectrum do not meet this contract.

The semigroup $\mathcal H$ is closed under composition. Consequently divisor closure of $\mathcal S$ follows by choosing an iterate as a new full native word. This is only a dependency reduction: attainable $24$ would supply $12$, and attainable $18$ would supply $9$. Conversely, excluding $12$ would exclude $24$, and excluding $9$ would exclude $18$. Positive attainment of $9$ and $12$ does not settle $18$ and $24$. This is not itself a new construction, does not turn a factor-step orbit into a native orbit, and is not claimed as an increment. After the author-level 16-exclusion, the maximal unresolved positive construction targets are $18,24$; the minimal exclusion targets are $9,12$.

The following shortcuts have not been justified:

- General polynomial interpolation preserves a cycle but need not produce a polynomial automorphism.
- Jung–van der Kulk factorization over $\mathbb Q$ does not guarantee integral coefficients in every Hénon factor.
- Polynomial automorphism or tame transitivity modulo every finite modulus does not give an exact integer-cycle lift.
- The first-pass phasewise secant lemma constrains a maximal-diameter phase but does not propagate one uniform alphabet through an arbitrary-length word.

One precise auxiliary reduction **is proved** in [PROOF_SUPPLEMENT.md](PROOF_SUPPLEMENT.md): $\mathcal S$ equals the integer native spectrum of the integral tame subgroup $\operatorname{TA}_2(\mathbb Z)$. Every tame word can be expressed with unrestricted Hénon factors; then every factor of degree below two can be padded by an integral polynomial vanishing on its own finite intermediate input support. The resulting nonlinear word acts identically on the selected entire native cycle. This preserves the native map permutation and least period, not only a factor-step return. It is an elementary auxiliary reduction, not the missing exact-spectrum theorem or a new admission.

## 4. Bounded discriminating diagnostic — single authorized run completed

Purpose: test whether compositions already produce a length outside the single-factor union in a small exact search, and preferably obtain explicit candidates for the missing maximal lengths. A successful witness is a proof lead; no-output has no exclusion meaning.

Frozen pre-run inputs, subsequently executed exactly: all monic quadratics $t^2+bt+c$ and monic cubics $t^3+bt^2+ct+d$ with lower coefficients in $\{-2,-1,0,1,2\}$, both Jacobian signs, and words of length exactly two. The search retains only cycles whose native and intermediate factor states all lie in $[-4,4]^2\cap\mathbb Z^2$. There are $2(25+125)=300$ factors, $90{,}000$ ordered factor pairs and $81$ states. It builds exact partial factor maps on this finite set, composes each ordered pair, and extracts its directed cycles without a period cutoff. This is at most $7.29$ million pair-state transitions plus graph traversal, with exact integer arithmetic. The pre-run estimate was below one minute on one CPU, with a hard runtime budget of two minutes. The search is a witness diagnostic, not an all-input certificate.

Outputs: only native periods outside $\{1,2,3,4,6,8\}$ with the exact factor polynomials, signs, all distinct native states and all intermediate states. Independently verify any reported witness by direct polynomial substitution. No old script or certificate is rerun. The coordinator approved preparation of precisely this diagnostic, actually read the complete code below, and then explicitly released its single execution. **That one execution is complete; no additional mathematical run is authorized.**

The factor order is degree $2$ then $3$, then lexicographic lower-coefficient tuples in ascending monomial order, then sign $-1$ before $+1$. States are lexicographic $(x,y)$. Each native cycle is oriented by $W$ and rotated so its lexicographically smallest state comes first; no reversal quotient is taken. Distinct cycles of each fixed word are traversed exactly once. The output counts word-cycle occurrences and distinct canonical coordinate cycles for missing lengths, retaining the first witness in deterministic factor order for each missing length. It does not print an uncontrolled list of all witnesses.

## 5. Complete executed diagnostic source

This is new code, retained in this report to respect the two-file ownership boundary. It uses one process, one CPU and a $120$-second real-time alarm. On timeout it prints a partial-status receipt and exits $124$; partial output is not completion. The code does not read or write project files, use a network, or run an old checker. Any emitted witness still requires the separately specified independent substitution check.

<!-- BEGIN R5_C2_DIAGNOSTIC_SOURCE -->
```python
import datetime
import itertools
import json
import signal
import sys
import time


class DiagnosticTimeout(Exception):
    pass


def timed_out(signum, frame):
    raise DiagnosticTimeout("120-second wall-clock budget reached")


def polynomial_value(coefficients, value):
    result = 0
    for coefficient in reversed(coefficients):
        result = result * value + coefficient
    return result


def run():
    started = time.perf_counter()
    started_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
    signal.signal(signal.SIGALRM, timed_out)
    signal.setitimer(signal.ITIMER_REAL, 120.0)
    radius = 4
    side = 2 * radius + 1
    states = [(x, y)
              for x in range(-radius, radius + 1)
              for y in range(-radius, radius + 1)]
    factors = []
    partial_maps = []
    completed_pairs = 0
    total_cycles = 0
    all_cycle_lengths = set()
    inherited_periods = {1, 2, 3, 4, 6, 8}
    missing_counts = {}
    missing_unique_cycles = {}
    first_witnesses = {}
    status = "COMPLETE"
    error = None
    try:
        for degree in (2, 3):
            for lower in itertools.product(range(-2, 3), repeat=degree):
                coefficients = lower + (1,)
                for epsilon in (-1, 1):
                    factor_id = len(factors)
                    factors.append({
                        "id": factor_id,
                        "degree": degree,
                        "coefficients_constant_first": list(coefficients),
                        "epsilon": epsilon,
                    })
                    images = []
                    for x, y in states:
                        z = polynomial_value(coefficients, y) - epsilon * x
                        if -radius <= z <= radius:
                            images.append((y + radius) * side + z + radius)
                        else:
                            images.append(-1)
                    partial_maps.append(images)

        assert len(states) == 81
        assert len(factors) == 300
        assert len(partial_maps) == 300

        for first_id, first_map in enumerate(partial_maps):
            for second_id, second_map in enumerate(partial_maps):
                native_map = [second_map[mid] if mid >= 0 else -1
                              for mid in first_map]
                done = [False] * len(states)
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
                        current = native_map[current]

                    if current >= 0 and current in position:
                        cycle = path[position[current]:]
                        pivot = cycle.index(min(cycle))
                        canonical = tuple(cycle[pivot:] + cycle[:pivot])
                        period = len(canonical)
                        total_cycles += 1
                        all_cycle_lengths.add(period)
                        if period not in inherited_periods:
                            missing_counts[period] = missing_counts.get(period, 0) + 1
                            missing_unique_cycles.setdefault(period, set()).add(canonical)
                            if period not in first_witnesses:
                                first_witnesses[period] = {
                                    "native_period": period,
                                    "word_order": "H_second composed with H_first",
                                    "first_factor": factors[first_id],
                                    "second_factor": factors[second_id],
                                    "native_states": [list(states[k]) for k in canonical],
                                    "intermediate_states": [
                                        list(states[first_map[k]]) for k in canonical
                                    ],
                                }
                    for vertex in path:
                        done[vertex] = True
                completed_pairs += 1
        assert completed_pairs == 90000
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
            "degrees": [2, 3],
            "monic": True,
            "lower_coefficient_range_inclusive": [-2, 2],
            "jacobian_signs": [-1, 1],
            "word_length": 2,
            "native_and_intermediate_box": [-4, 4],
            "state_count": len(states),
            "factor_count": len(factors),
            "planned_ordered_factor_pairs": 90000,
            "wall_clock_budget_seconds": 120,
        },
        "completed_ordered_factor_pairs": completed_pairs,
        "total_word_cycle_occurrences": total_cycles,
        "number_of_distinct_periods_seen": len(all_cycle_lengths),
        "new_period_word_cycle_counts": {
            str(k): missing_counts[k] for k in sorted(missing_counts)
        },
        "new_period_distinct_canonical_coordinate_cycles": {
            str(k): len(missing_unique_cycles[k])
            for k in sorted(missing_unique_cycles)
        },
        "first_new_period_witnesses": [
            first_witnesses[k] for k in sorted(first_witnesses)
        ],
        "scope_warning": (
            "A finite witness diagnostic only. No missing witness is a uniform "
            "exclusion; the exact all-word spectrum is not determined by this run."
        ),
    }
    print(json.dumps(receipt, indent=2, sort_keys=True), flush=True)
    return 0 if status == "COMPLETE" else (124 if status == "TIMEOUT_PARTIAL" else 1)


if __name__ == "__main__":
    sys.exit(run())
```
<!-- END R5_C2_DIAGNOSTIC_SOURCE -->

## 6. Execution and disposition

The coordinator actually read the complete source and explicitly released exactly one run before execution. The exact marked Python text was streamed without a source rewrite or an extra script file. Working directory: `/root/autodl-tmp/hilbert-polya-structure`. The two actual read-only extraction commands, first for binding and second for execution, were:

```bash
awk '/^<!-- BEGIN R5_C2_DIAGNOSTIC_SOURCE -->$/{inside=1;next} /^<!-- END R5_C2_DIAGNOSTIC_SOURCE -->$/{inside=0} inside && $0 != "```python" && $0 != "```" {print}' henon_dynamics/research_c429_c433/continuation_round5/c2_composition_exact_spectrum/REPORT.md | sha256sum
awk '/^<!-- BEGIN R5_C2_DIAGNOSTIC_SOURCE -->$/{inside=1;next} /^<!-- END R5_C2_DIAGNOSTIC_SOURCE -->$/{inside=0} inside && $0 != "```python" && $0 != "```" {print}' henon_dynamics/research_c429_c433/continuation_round5/c2_composition_exact_spectrum/REPORT.md | python3 -
```

Extracted source SHA-256: `a2b9349d48fcfc97ea57d4d396abd0e06598e68d79402eacc4f1a4a807a5dca4`. Both command exit codes were `0`. The execution receipt measured `3.008390285` seconds internally; the command tool separately reported `2.897282805` wall-time seconds. These are the two observed timing fields, not a recomputed benchmark. The exact full JSON output was:

```json
{
  "completed_ordered_factor_pairs": 90000,
  "elapsed_seconds": 3.008390285,
  "error": null,
  "first_new_period_witnesses": [],
  "input": {
    "degrees": [
      2,
      3
    ],
    "factor_count": 300,
    "jacobian_signs": [
      -1,
      1
    ],
    "lower_coefficient_range_inclusive": [
      -2,
      2
    ],
    "monic": true,
    "native_and_intermediate_box": [
      -4,
      4
    ],
    "planned_ordered_factor_pairs": 90000,
    "state_count": 81,
    "wall_clock_budget_seconds": 120,
    "word_length": 2
  },
  "new_period_distinct_canonical_coordinate_cycles": {},
  "new_period_word_cycle_counts": {},
  "number_of_distinct_periods_seen": 6,
  "python_version": "3.12.3 | packaged by Anaconda, Inc. | (main, Apr 19 2024, 16:50:38) [GCC 11.2.0]",
  "scope_warning": "A finite witness diagnostic only. No missing witness is a uniform exclusion; the exact all-word spectrum is not determined by this run.",
  "started_utc": "2026-09-09T16:04:29.631736+00:00",
  "status": "COMPLETE",
  "total_word_cycle_occurrences": 40098
}
```

All $90{,}000$ pairs were completed, with $40{,}098$ word-cycle occurrences and six distinct lengths. Since every observed length belonged to the six-element inherited set, the observed finite-window spectrum is exactly $\{1,2,3,4,6,8\}$. No new-length witness was emitted, so there is no candidate requiring a subsequent independent witness check. This finite-window result supplies **no exclusion** for $9,12,16,18,24$ in the unrestricted class and does not alter the unproved status of the main claim. No coefficient, degree, word-length or state-window expansion is performed or proposed as an automatic continuation.

The Hénon batch, research-lit and proof-writer skills are used for source subtraction, exact quantifiers and honest proof status. No external-model/API examples or old GPU-pilot defaults are executed. Mathematical runs: **one, exactly the released diagnostic**. Current exact-spectrum status: **NOT CURRENTLY JUSTIFIED**. No paper admission requested at this stage.

## 7. Direct residue-cycle control — no additional execution

Finite-residue attainment does not imply exact integral attainment, even for a single allowed factor. Consider

$$
H(x,y)=(y,x+y^3+y^2+y).
$$

Direct integer substitution gives the following table. The third column is the exact second coordinate before reduction, and the last column is the next native state modulo four.

| Input representative | $y$ | $x+y^3+y^2+y$ | $H(x,y)\bmod4$ |
| --- | --- | --- | --- |
| $(1,0)$ | $0$ | $1$ | $(0,1)$ |
| $(0,1)$ | $1$ | $3$ | $(1,3)$ |
| $(1,3)$ | $3$ | $40$ | $(3,0)$ |
| $(3,0)$ | $0$ | $3$ | $(0,3)$ |
| $(0,3)$ | $3$ | $39$ | $(3,3)$ |
| $(3,3)$ | $3$ | $42$ | $(3,2)$ |
| $(3,2)$ | $2$ | $17$ | $(2,1)$ |
| $(2,1)$ | $1$ | $5$ | $(1,1)$ |
| $(1,1)$ | $1$ | $4$ | $(1,0)$ |

The nine residue states are distinct, so this is a native nine-cycle over $\mathbb Z/4\mathbb Z$. It is not an integer nine-cycle: the integer outputs already leave the representative table. More decisively, the imported C428 single-factor theorem excludes every integer nine-cycle for this same $H$. This directly defeats any inference from a finite-residue nine-cycle to an exact integer nine-cycle. It does not settle whether a different longer word has an integer nine-cycle, and it makes no assertion about an actual $\mathbb Z_2$ nine-cycle. The table was checked by hand; no old checker or new program was run.

## 8. Uniform 16-exclusion — complete author proof, independent review pending

[PROOF_SUPPLEMENT.md](PROOF_SUPPLEMENT.md), Sections 5–8, now proves that **no allowed word has native least period 16 even on $\mathbb Z_2^2$**. It preserves all original word lengths, degrees, coefficient heights and sign patterns. The proof has two exact components:

1. The product of derivative-permutation signs over the four points of $\mathbb F_2^2$ is multiplicative under composition and equals $+1$ for every Hénon factor. Each value of the second coordinate occurs twice in the product.
2. A four-cycle contained in one residue class modulo two, for a polynomial map with constant unit Jacobian, must have odd derivative sign. The even-sign alternatives are exhausted: order three contradicts the first Taylor congruence; identity forces the mixed quadratic coefficients even, hence yields a strict valuation contradiction at the second-iterate displacement.

For a hypothetical native 16-cycle, $G=F^4$ has a local four-cycle. The original residue period is $1,2$ or $4$. In the first two cases the derivative-sign factors repeat an even number of times; in the last they multiply to the character above. Therefore $DG$ has even sign in every case, contradicting the local lemma. Its constant determinant is $(\pm1)^4=1$.

The normalization is fully justified over $\mathbb Z_2$: congruence preservation makes successive cycle differences have equal valuation, and translating and scaling by $2^{d-1}$ preserves integral coefficients, the constant Jacobian, derivative reduction and native least period. The proof treats a vanishing second-iterate displacement as an immediate least-period contradiction and a nonzero displacement by its exact minimum coordinate valuation. No numerical bounds or finite search are used. Pezda's local eight-cycle exclusion was reread during development but is not needed by the final proof.

Thus, pending independent acceptance of this proof,

$$
\{1,2,3,4,6,8\}\subseteq\mathcal S
\subseteq\{1,2,3,4,6,8,9,12,18,24\}.
$$

The four lengths $9,12,18,24$ remain unclassified. The exact universal-spectrum task remains **NOT CURRENTLY JUSTIFIED**. This uniform partial exclusion is not a standalone paper proposal; source priority and nonauthor review remain separate gates. Mathematical executions remain exactly **one**, the already released finite diagnostic.

## 9. Post-freeze focused source check for the 16-exclusion

The coordinator requested a focused check for prior dyadic polynomial-automorphism period restrictions, beyond Pezda's theorem for arbitrary maps. Bounded targeted searches covered integer and $2$-adic automorphism periods, period 16, finite-ring permutation parity and constant-Jacobian cycle restrictions. They did not locate a primary theorem stating the exact 16-exclusion. This negative search result is **not** a novelty certificate, and no exhaustive ownership claim follows.

- **Bell–Ghioca–Tucker, *Applications of p-adic analysis for bounding periods of subvarieties under etale maps*.** The primary [author PDF, Theorem 1.1 and Proposition 2.1](https://personal.math.ubc.ca/~dghioca/papers/burnside_revision.pdf) was actually read through browser text. The theorem bounds the preperiodic orbit length for an étale map of a smooth integral model by $p^{1+r}|\operatorname{GL}_g(k_v)|\#\mathcal X(k_v)$, with $r$ the smallest nonnegative integer strictly above $(\log e-\log(p-1))/\log2$. For $\mathbb Q_2$ and $\mathcal X=\mathbb A^2_{\mathbb Z_2}$, this displayed bound is $2^2\cdot6\cdot4=96$. This specialization, our arithmetic deduction, does not by itself exclude 16. The proof's general near-identity congruences do not state the two-dimensional constant-Jacobian mixed-coefficient obstruction used here. The [primary version record](https://arxiv.org/abs/1310.5775v2) was also checked. A subsequent shell PDF-text access attempt failed at TLS; no additional full-text read is claimed from that failed command.
- **Maubach–Willems, *Polynomial automorphisms over finite fields: Mimicking non-tame and tame maps by the Derksen group*.** The actual [primary preprint, Sections 1–2, including Theorem 2.1](https://arxiv.org/html/0912.3387v1), was read. The stated Jung–van der Kulk theorem applies to every field and identifies $\operatorname{TA}_2(k)$ with $\operatorname{GA}_2(k)$. Its finite-field parity discussion concerns permutations of field-valued points; $\mathbb F_4$ is not $\mathbb Z/4\mathbb Z$. The accessed statements neither assert a $\mathbb Z_2$ 16-exclusion nor identify the derivative character below as new. The 2011 publisher PDF was located, but direct reopening and shell streaming failed; the explicitly accessed full-text source is the versioned preprint, not an asserted full read of the published article.
- **Allen–DeMark–Petsche, *Non-Archimedean Hénon maps, attractors, and horseshoes*.** The [primary v3 abstract and version record](https://arxiv.org/abs/1610.04271v3) explicitly place the study in odd residue characteristic. It therefore does not supply the requested dyadic 16-exclusion. Only the abstract/version record is claimed read in this focused check.

There is a broader ambient-class consequence of the already checked character calculation and the classical field-factorization theorem. Let

$$
T\in\operatorname{Aut}_{\mathbb Z_2}(\mathbb A^2_{\mathbb Z_2}),
$$

meaning that both $T$ and its polynomial inverse have coefficients in $\mathbb Z_2$. Reduction gives a polynomial automorphism over $\mathbb F_2$, which is tame by the cited Jung–van der Kulk theorem. The same character $\chi$ is $+1$ on every affine generator, because one fixed matrix sign appears four times, and on every elementary shear, because each relevant coordinate value appears twice. Multiplicativity therefore gives $\chi(T)=1$ even when no tame factorization over $\mathbb Z_2$ has been given. Its Jacobian determinant is a constant unit $\delta$: the chain rule with the polynomial inverse makes it a unit of the polynomial ring over the domain $\mathbb Z_2$. Here $\det D(T^4)=\delta^4$ is a constant unit, not necessarily 1; the original local lemma covers exactly this hypothesis. That lemma and the unchanged $T^4$ residue-sign argument consequently exclude native period 16 for this ambient class as well.

This is a deduction from a classical factorization theorem plus the present local lemma, not a theorem quoted verbatim from Maubach–Willems. This ambient class contains the original integral nonlinear-word class; no strictness or integral tameness claim is needed. It does not identify every integral plane automorphism with the integral tame subgroup, does not claim a new independent contract, and does not settle source priority for the 16-exclusion. This post-freeze ambient-class corollary was not part of E4's original author-file binding; the original requested-class theorem remains exactly the unchanged independently reviewed proof.

## 10. Post-freeze independent-review status and continuation

E4's complete [179-line independent review](../reviews/e4_composition_period16/REVIEW.md) was actually read after it was frozen. Its verdict is **PASS / PROVABLE AS STATED, zero mathematical must-fixes** for both the finite-orbit class reduction and the universal native 16-exclusion, including the $\mathbb Z_2^2$ conclusion. Review SHA-256 is `0e866dbba4d2431fcb621c406195570aa4b8139d3614c91f44822b75d43e6572`.

The review binds the unchanged proof SHA-256 `16ed4ea2b81d7a6b6c029b2c6fcd463716a0af9bd925bfb54d4747ee1ea35edb` and the 341-line pre-append report SHA-256 `1e3d2e82de52341e686ebbf2bd48ee5c4b854c0b451dbbd7422495ee05308a0c`. Sections 1–8 above retain that pre-append report verbatim. Their statements that independent review is pending describe the author-freeze stage and are superseded by this post-freeze review record. No proof repair was requested or made. The new source subsection and broader-class deduction are explicitly outside the earlier report hash; source priority and final coordinator acceptance remain separate.

The complete spectrum remains unresolved. The coordinator has assigned the existing C1 thread a complementary exact native 12/24 tame-witness construction, with the finite-orbit padding lemma available as input. C2 continues the native-nine question through finite configurations and integral interpolation of tame involutions. Neither assignment authorizes an automatic program/window expansion. Any native witness must give an actual integer full-word orbit and all exact transitions; a finite-residue permutation is insufficient. Mathematical executions remain **one**.

## 11. Native-nine staircase interpolation diagnostic — single released run complete

The coordinator first authorized preparation, then actually read the complete mechanism and source, checked its extracted hash, and explicitly released **one execution** of precisely the following second diagnostic. That execution is complete. The already reviewed proof remains unchanged, and this new construction test is outside E4's earlier source/report binding. E4 has additionally reviewed the ambient-class corollary in Sections 9–10: its current 220-line review has SHA-256 `9003d5b80f6c40187ab9620e65f56d429675ab3ee5c2324151e8a44e8b3b5a59` and binds the pre-Section-11 report SHA-256 `0b61d292915d2ab54c6047fea37a4908df9ffbdf07598a8766d5c6c530764e36`. These are historical prefix bindings, not a claim that the new diagnostic has been independently rerun.

### 11.1 Exact construction mechanism and bounded question

For integer polynomials $p,q$, define the two tame involutions

$$
I(x,y)=(x,q(x)-y),\qquad J(x,y)=(p(y)-x,y),\qquad F=J\circ I.
$$

Choose permutations $(x_0,\ldots,x_4)$ and $(y_0,\ldots,y_4)$ of $\{0,1,2,3,4\}$. Form the nine distinct vertices

$$
v_{2i}=(x_i,y_i),\quad v_{2i+1}=(x_i,y_{i+1})\quad(0\le i<4),
\qquad v_8=(x_4,y_4).
$$

The required interpolation values are

$$
q(x_i)=y_i+y_{i+1}\ (i<4),\qquad q(x_4)=2y_4,
$$

$$
p(y_0)=2x_0,\qquad p(y_{i+1})=x_i+x_{i+1}\ (i<4).
$$

These equations make $I$ exchange $(v_0,v_1),(v_2,v_3),(v_4,v_5),(v_6,v_7)$ and fix $v_8$. They make $J$ fix $v_0$ and exchange $(v_1,v_2),(v_3,v_4),(v_5,v_6),(v_7,v_8)$. Therefore the full native map $F=J\circ I$ has cycle order

$$
v_0,v_2,v_4,v_6,v_8,v_7,v_5,v_3,v_1.
$$

All nine points are distinct because the $x_i$ are distinct and the two vertices in each paired column have distinct $y$ coordinates. Hence satisfaction of these exact integer equations supplies least period nine, not just a return time.

For $S(x,y)=(y,x)$, direct composition gives

$$
S\circ F\circ S
=H_{p,+1}\circ H_{q,+1},
\qquad H_{q,+1}(u,v)=(v,q(v)-u).
$$

Thus the actual Hénon-word native states are the coordinate-swapped $F$-cycle states. The intermediate state after the first factor at $S(x,y)$ is $(x,q(x)-y)=I(x,y)$, which belongs to the same nine-vertex configuration. If either interpolating polynomial has degree below two, add

$$
A(t)=\prod_{j=0}^4(t-j)
$$

to that polynomial. Both first-factor and second-factor input supports lie in $\{0,1,2,3,4\}$, so this produces an allowed degree-five factor without changing any displayed native or intermediate transition. The resulting two-factor word, with the exact padded coefficients displayed in any witness, is in the original class.

### 11.2 Necessary and sufficient integral interpolation test

For prescribed values $b_0,\ldots,b_4$ at $0,\ldots,4$, any integer polynomial realizing them can be divided by the monic polynomial $A(t)$ in $\mathbb Z[t]$. Its remainder has degree at most four, integral coefficients and the same five values. The unique rational interpolant is

$$
r(t)=\sum_{k=0}^4 \frac{\Delta^k b_0}{k!}
\prod_{j=0}^{k-1}(t-j).
$$

The five falling-factorial polynomials on the right are monic of successive degrees $0,\ldots,4$; their change-of-basis matrix from monomials is integral unitriangular. They therefore form a $\mathbb Z$-basis of the integer polynomials of degree at most four. Consequently integral polynomial interpolation is possible **if and only if**

$$
k!\mid\Delta^k b_0\qquad(0\le k\le4).
$$

The code tests exactly these integer divisibilities and reconstructs exact monomial coefficients. It does not accept an integer-valued rational polynomial as an element of $\mathbb Z[t]$.

Inputs are exactly the $120^2=14{,}400$ ordered pairs of permutations, in lexicographic order, with no symmetry pruning or coefficient/point-window expansion. Outputs are completion/timeout/error status, processed-pair counts, individual and simultaneous interpolation counts, distinct canonical native-nine coordinate-cycle counts and the first deterministic full witness if any. A witness includes $p,q$, their allowed padded versions, all nine native states for $F$ and the Hénon word, and all intermediate factor states. Internal substitution assertions are construction-consistency checks, not the separately required nonauthor witness verification.

The budget is one process, one CPU and a ten-second real-time alarm. On timeout the receipt is partial and the exit code is 124. No hit excludes **only this fixed nine-vertex staircase template with both coordinate alphabets $0,\ldots,4$**, not native period nine for general tame maps or Hénon words. The single released execution is recorded in Section 11.4.

### 11.3 Complete executed source — unchanged from the reviewed release

<!-- BEGIN R5_C2_NINE_STAIRCASE_SOURCE -->
```python
import datetime
import itertools
import json
import math
import signal
import sys
import time


class DiagnosticTimeout(Exception):
    pass


def timed_out(signum, frame):
    raise DiagnosticTimeout("10-second wall-clock budget reached")


def value(coefficients, argument):
    result = 0
    for coefficient in reversed(coefficients):
        result = result * argument + coefficient
    return result


def multiply_by_t_minus(coefficients, root):
    result = [0] * (len(coefficients) + 1)
    for degree, coefficient in enumerate(coefficients):
        result[degree] -= root * coefficient
        result[degree + 1] += coefficient
    return result


def integer_interpolant(values):
    differences = list(values)
    newton = []
    for degree in range(5):
        quotient, remainder = divmod(differences[0], math.factorial(degree))
        if remainder != 0:
            return None
        newton.append(quotient)
        differences = [differences[j + 1] - differences[j]
                       for j in range(len(differences) - 1)]
    coefficients = [0] * 5
    basis = [1]
    for degree, coefficient in enumerate(newton):
        for power, term in enumerate(basis):
            coefficients[power] += coefficient * term
        basis = multiply_by_t_minus(basis, degree)
    while len(coefficients) > 1 and coefficients[-1] == 0:
        coefficients.pop()
    assert [value(coefficients, t) for t in range(5)] == list(values)
    return coefficients


def allowed_padding(coefficients, annihilator):
    if len(coefficients) >= 3:
        return list(coefficients)
    padded = [0] * len(annihilator)
    for degree, coefficient in enumerate(coefficients):
        padded[degree] += coefficient
    for degree, coefficient in enumerate(annihilator):
        padded[degree] += coefficient
    return padded


def run():
    started = time.perf_counter()
    started_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
    signal.signal(signal.SIGALRM, timed_out)
    signal.setitimer(signal.ITIMER_REAL, 10.0)
    completed = 0
    p_integral = 0
    q_integral = 0
    both_integral = 0
    canonical_cycles = set()
    first_witness = None
    status = "COMPLETE"
    error = None
    try:
        permutations = list(itertools.permutations(range(5)))
        assert len(permutations) == 120
        annihilator = [1]
        for root in range(5):
            annihilator = multiply_by_t_minus(annihilator, root)
        native_vertex_order = [0, 2, 4, 6, 8, 7, 5, 3, 1]

        for xs in permutations:
            for ys in permutations:
                q_values = [None] * 5
                p_values = [None] * 5
                for j in range(4):
                    q_values[xs[j]] = ys[j] + ys[j + 1]
                q_values[xs[4]] = 2 * ys[4]
                p_values[ys[0]] = 2 * xs[0]
                for j in range(4):
                    p_values[ys[j + 1]] = xs[j] + xs[j + 1]
                q = integer_interpolant(q_values)
                p = integer_interpolant(p_values)
                q_integral += int(q is not None)
                p_integral += int(p is not None)
                if p is not None and q is not None:
                    both_integral += 1
                    vertices = []
                    for j in range(4):
                        vertices.extend([(xs[j], ys[j]), (xs[j], ys[j + 1])])
                    vertices.append((xs[4], ys[4]))
                    assert len(set(vertices)) == 9
                    f_cycle = [vertices[j] for j in native_vertex_order]
                    w_cycle = [(y, x) for x, y in f_cycle]
                    pivot = w_cycle.index(min(w_cycle))
                    f_cycle = f_cycle[pivot:] + f_cycle[:pivot]
                    w_cycle = w_cycle[pivot:] + w_cycle[:pivot]
                    canonical = tuple(w_cycle)
                    canonical_cycles.add(canonical)
                    q_allowed = allowed_padding(q, annihilator)
                    p_allowed = allowed_padding(p, annihilator)
                    intermediates = []
                    for j, (x, y) in enumerate(f_cycle):
                        i_image = (x, value(q, x) - y)
                        f_image = (value(p, i_image[1]) - i_image[0], i_image[1])
                        assert f_image == f_cycle[(j + 1) % 9]
                        u, v = w_cycle[j]
                        intermediate = (v, value(q_allowed, v) - u)
                        w_image = (intermediate[1],
                                   value(p_allowed, intermediate[1]) - intermediate[0])
                        assert intermediate == i_image
                        assert w_image == w_cycle[(j + 1) % 9]
                        intermediates.append(intermediate)
                    if first_witness is None:
                        first_witness = {
                            "x_permutation": list(xs),
                            "y_permutation": list(ys),
                            "p_coefficients_constant_first": p,
                            "q_coefficients_constant_first": q,
                            "p_required_values_at_0_through_4": p_values,
                            "q_required_values_at_0_through_4": q_values,
                            "F": "J composed with I",
                            "I": "(x, q(x)-y)",
                            "J": "(p(y)-x, y)",
                            "F_native_states": [list(point) for point in f_cycle],
                            "coordinate_conjugacy": "W = S F S; S(x,y)=(y,x)",
                            "W": "H_p_allowed,+1 composed with H_q_allowed,+1",
                            "first_H_coefficients_constant_first": q_allowed,
                            "second_H_coefficients_constant_first": p_allowed,
                            "both_H_jacobian_signs": [1, 1],
                            "W_native_states": [list(point) for point in w_cycle],
                            "W_intermediate_states": [list(point) for point in intermediates],
                            "native_least_period": 9,
                        }
                completed += 1
        assert completed == 14400
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
            "coordinate_alphabet": [0, 1, 2, 3, 4],
            "permutations_per_coordinate": 120,
            "planned_ordered_permutation_pairs": 14400,
            "template_vertex_count": 9,
            "candidate_native_period": 9,
            "unreduced_interpolant_max_degree": 4,
            "symmetry_pruning": False,
            "wall_clock_budget_seconds": 10,
        },
        "completed_ordered_permutation_pairs": completed,
        "p_integral_pair_count": p_integral,
        "q_integral_pair_count": q_integral,
        "both_integral_pair_count": both_integral,
        "distinct_canonical_W_coordinate_cycles": len(canonical_cycles),
        "first_witness": first_witness,
        "scope_warning": (
            "No hit excludes only this nine-vertex staircase with coordinate "
            "alphabets 0..4, not native period nine in the unrestricted class. "
            "Any witness still requires separate independent exact substitution."
        ),
    }
    print(json.dumps(receipt, indent=2, sort_keys=True), flush=True)
    return 0 if status == "COMPLETE" else (124 if status == "TIMEOUT_PARTIAL" else 1)


if __name__ == "__main__":
    sys.exit(run())
```
<!-- END R5_C2_NINE_STAIRCASE_SOURCE -->

### 11.4 Exact execution receipt and disposition

The coordinator actually read Sections 11.1–11.4 and the complete source, supplied its own extracted SHA-256, and released one execution without code changes or parameter expansion. The author first reproduced that exact SHA-256 and then streamed the marked source directly to Python. Both commands ran in `/root/autodl-tmp/hilbert-polya-structure`:

```bash
awk '/^<!-- BEGIN R5_C2_NINE_STAIRCASE_SOURCE -->$/{inside=1;next} /^<!-- END R5_C2_NINE_STAIRCASE_SOURCE -->$/{inside=0} inside && $0 != "```python" && $0 != "```" {print}' henon_dynamics/research_c429_c433/continuation_round5/c2_composition_exact_spectrum/REPORT.md | sha256sum
awk '/^<!-- BEGIN R5_C2_NINE_STAIRCASE_SOURCE -->$/{inside=1;next} /^<!-- END R5_C2_NINE_STAIRCASE_SOURCE -->$/{inside=0} inside && $0 != "```python" && $0 != "```" {print}' henon_dynamics/research_c429_c433/continuation_round5/c2_composition_exact_spectrum/REPORT.md | python3 -
```

The matching source hash is `ab61d5dbe05fdd9495fe711227671c6e429f7d7ba6c9c0a092bf765ddad0401d`. Both command exit codes were `0`. The program's internal elapsed field was `0.06650795` seconds; the execution tool separately returned a wall-time field of `0.00000553` seconds. These are the actual observed fields and are not presented as mutually calibrated benchmark measurements. Full exact JSON output:

```json
{
  "both_integral_pair_count": 0,
  "completed_ordered_permutation_pairs": 14400,
  "distinct_canonical_W_coordinate_cycles": 0,
  "elapsed_seconds": 0.06650795,
  "error": null,
  "first_witness": null,
  "input": {
    "candidate_native_period": 9,
    "coordinate_alphabet": [
      0,
      1,
      2,
      3,
      4
    ],
    "permutations_per_coordinate": 120,
    "planned_ordered_permutation_pairs": 14400,
    "symmetry_pruning": false,
    "template_vertex_count": 9,
    "unreduced_interpolant_max_degree": 4,
    "wall_clock_budget_seconds": 10
  },
  "p_integral_pair_count": 24,
  "python_version": "3.12.3 | packaged by Anaconda, Inc. | (main, Apr 19 2024, 16:50:38) [GCC 11.2.0]",
  "q_integral_pair_count": 24,
  "scope_warning": "No hit excludes only this nine-vertex staircase with coordinate alphabets 0..4, not native period nine in the unrestricted class. Any witness still requires separate independent exact substitution.",
  "started_utc": "2026-09-09T16:37:37.455713+00:00",
  "status": "COMPLETE"
}
```

The full $14{,}400$-pair diagnostic completed. There were 24 pairs satisfying the $p$ interpolation condition and 24 satisfying the $q$ condition, but no pair satisfying both. Hence it emits no integer native-nine witness and requires no subsequent witness verification. This is only a negative result for the specified staircase template. No larger coordinate alphabet, arbitrary spacings, different involution graph or extra word length was searched. No automatic expansion follows.

The exact universal spectrum remains unresolved at $9,12,18,24$. The uniform 16-exclusion and its reviewed proof are unchanged. Mathematical executions now total **two**, precisely the two individually released diagnostics. No extra source file, external-model API, previous checker, shared-file edit or manuscript build was used.

## 12. A hand-derived modulo-three constraint for invariant reversible nine-cycles

This section is a new, unreviewed auxiliary argument, outside E4's earlier report-prefix binding. It does not change the frozen period-16 proof, does not execute another diagnostic, and does not classify period nine for general words. Its purpose is to identify the exact surviving local branch of the two-involution construction. No independent-paper or new source-priority claim is made for the local lemma.

### 12.1 No local nine-cycle with constant Jacobian sign

**Lemma.** Let $T\in\mathbb Z_3[x,y]^2$ have constant Jacobian determinant in $\{1,-1\}$. There is no least-period-nine cycle for $T$ whose nine points are all congruent modulo three.

**Proof.** If necessary replace $T$ by $T^2$. Since $\gcd(2,9)=1$, the same nine points still form one least-period-nine cycle; its Jacobian determinant is now one. Write the cycle as $z_0,\ldots,z_8$. For a vector $z$, write $\nu(z)=\min(v_3(z_1),v_3(z_2))$, with $\nu(0)=+\infty$.

Polynomial congruence preservation shows that the valuations of successive differences $z_{i+1}-z_i$ cannot decrease around the cycle. Hence they all equal a finite $d\ge1$. All points $z_i-z_0$ are divisible by $3^d$. Put $a=3^{d-1}$ and

$$
g(X)=\frac{T(z_0+aX)-z_0}{a}.
$$

The constant coefficient is integral, and every coefficient of total degree $k\ge1$ has a factor $a^{k-1}$ after division. Thus $g\in\mathbb Z_3[x,y]^2$, with determinant one. Its nine-cycle begins at zero, all its points lie in $3\mathbb Z_3^2$, and $v=g(0)$ satisfies $\nu(v)=1$. Put $A=Dg(0)$ and $u=(v/3)\bmod3\ne0$.

At all cycle points, Taylor expansion gives $g(z)\equiv v+Az\pmod9$. Consequently $g^9(0)=0$ implies

$$
\left(\sum_{i=0}^{8}\overline A^i\right)u=0.
$$

In $\mathbb F_3[X]$ one has

$$
1+X+\cdots+X^8=(X-1)^8,
$$

since $X^9-1=(X-1)^9$. Therefore $(\overline A-I)^8u=0$. The nonzero vector $u$ shows that $\overline A-I$ is singular. Because $\det\overline A=1$, the other eigenvalue is also one; explicitly, $\det(\overline A-I)=\det\overline A-\operatorname{tr}\overline A+1=0$ gives $\operatorname{tr}\overline A=2$. Cayley–Hamilton yields

$$
(\overline A-I)^2=0,
\qquad \overline A^3=I,
\qquad I+\overline A+\overline A^2=0.
$$

Set $h=g^3$ and $w=h(0)$. The same Taylor congruence gives

$$
w\equiv(I+A+A^2)v\equiv0\pmod9.
$$

The least period is nine, so $w\ne0$. Write $e=\nu(w)\ge2$. All of $0,g(0),g^2(0)$ are divisible by three, so the chain rule gives

$$
B:=Dh(0)\equiv\overline A^3=I\pmod3.
$$

Write $B=I+3C$ with $C$ integral. Taylor expansion of $h$ on $3^e\mathbb Z_3^2$, applied successively starting at zero, gives

$$
h^3(0)=(I+B+B^2)w+R,
\qquad R\in3^{2e}\mathbb Z_3^2.
$$

Here the intermediate points remain divisible by $3^e$, since $h(0)=w$ and all coefficients of $h$ are integral. Direct multiplication shows

$$
I+B+B^2=3I+9C+9C^2.
$$

As $2e\ge e+2$, it follows that $h^3(0)\equiv3w\pmod{3^{e+2}}$. Some coordinate of $3w$ has valuation exactly $e+1$, so this is nonzero. This contradicts $h^3(0)=g^9(0)=0$ and proves the lemma. $\square$

### 12.2 Exact residue branch for the invariant two-involution template

Let

$$
I(x,y)=(x,q(x)-y),\qquad
J(x,y)=(p(y)-x,y),\qquad F=J\circ I,
$$

with $p,q\in\mathbb Z[t]$. Suppose that a native nine-cycle $C$ of $F$ satisfies the **additional hypothesis $I(C)=C$**. It then also satisfies $J(C)=C$. This is true for the staircase mechanism in Section 11, but is not a consequence of reversibility alone: for an arbitrary nine-cycle, $I$ can send it to a different nine-cycle.

Choose $P\in C$. Since $IFI=F^{-1}$ and $I$ preserves $C$, there is a $k\in\mathbb Z/9\mathbb Z$ such that

$$
I(F^jP)=F^{k-j}P.
$$

The equation $2j=k\pmod9$ has exactly one solution. Thus $I|_C$ has exactly one fixed point.

Let $m$ be the native least period of $P\bmod3$ for $\overline F$. Then $m\mid9$ and $m\le9$, so $m\in\{1,3,9\}$. If $m=9$, the reduction map identifies $C$ bijectively with all of $\mathbb F_3^2$. It intertwines the two involutions $I|_C$ and $\overline I$, so they must have the same number of fixed points. But for each of the three $x\in\mathbb F_3$, the equation $2y=\overline q(x)$ has exactly one solution. Hence $\overline I$ has three fixed points, a contradiction. If $m=1$, all nine original points are congruent modulo three, contradicting Section 12.1 because $\det DF=1$.

Therefore any such invariant reversible nine-cycle must satisfy

$$
\boxed{m=3.}
$$

This leaves three residue points, each containing three original points, with $F^3$ acting as a local three-cycle in each occupied residue class. Neither the fixed-point count nor the local-nine lemma excludes those local three-cycles. For general words without the invariant-involution hypothesis, residue period nine is also still possible. The complete integer spectrum remains unresolved.

### 12.3 All five-term arithmetic-progression staircase alphabets are excluded

**Corollary for the staircase only.** In the nine-vertex mechanism of Section 11.1, suppose the five distinct $x_i$ form an arbitrary ordering of one integer arithmetic progression of length five and nonzero step, and the five distinct $y_i$ form an arbitrary ordering of another such progression. The starting integers, both nonzero steps and both orderings are unrestricted. There are no integral polynomials $p,q$ realizing this staircase as the indicated invariant native nine-cycle.

**Proof.** Section 12.2 would force the cycle to reduce to a three-cycle modulo three. Each occupied residue point would then contain exactly three of the nine points. In particular, the number of original points in each residue class of either individual coordinate must be divisible by three.

In the staircase, each of $x_0,x_1,x_2,x_3$ occurs as the first coordinate of exactly two vertices, while $x_4$ occurs once. Suppose the step of the $x$ arithmetic progression is not divisible by three. Its five values then have residue multiplicities $2,2,1$, in some order. Of the two residue classes containing two $x$ values, at least one does not contain $x_4$. That class contains exactly four vertices of $C$, contradicting divisibility by three. Therefore the $x$ step is divisible by three, and all five $x$ values are congruent modulo three.

For the second coordinate, $y_0$ occurs once and each of $y_1,y_2,y_3,y_4$ occurs twice. The same argument, with $y_0$ as the exceptional endpoint, forces the $y$ step to be divisible by three. Hence all nine points are congruent modulo three, contradicting Section 12.1. $\square$

This hand proof in particular explains the no-hit result for the two alphabets $0,\ldots,4$ without relying on its computation, and covers arbitrary spacings of the special arithmetic-progression kind. It does **not** cover arbitrary five-element alphabets, repeated coordinate values, a different involution graph, non-invariant reversible cycles or longer general words. The historical diagnostic receipt and the count of two executions remain unchanged.
