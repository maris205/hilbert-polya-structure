#!/usr/bin/env python3
"""Producer-independent exhaustive checker for HCS-C175."""
from __future__ import annotations

from hashlib import sha256
from itertools import product
import json
from math import comb, gcd
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c175_rule184_evidence.json"
checks = 0


def require(condition: bool, message: str) -> None:
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)


def traffic_move(word: tuple[int, ...]) -> tuple[int, ...]:
    """Independent implementation: enumerate moving particles, then apply moves."""
    n = len(word)
    moving = [i for i in range(n) if word[i] == 1 and word[(i + 1) % n] == 0]
    out = list(word)
    for i in moving:
        out[i] = 0
        out[(i + 1) % n] = 1
    return tuple(out)


def predicted_core(word: tuple[int, ...]) -> bool:
    n = len(word)
    k = sum(word)
    minority = 1 if 2 * k <= n else 0
    return all(not (word[i] == minority == word[(i + 1) % n]) for i in range(n))


def orbit_data(word: tuple[int, ...]) -> tuple[bool, int | None, int]:
    seen = {word: 0}
    out = word
    entry = 0 if predicted_core(word) else -1
    for t in range(1, len(word) * len(word) + len(word) + 2):
        out = traffic_move(out)
        if entry < 0 and predicted_core(out):
            entry = t
        if out in seen:
            first = seen[out]
            return first == 0, t - first if first == 0 else None, entry
        seen[out] = t
    raise AssertionError("orbit did not close inside theorem bound")


def independent_count(n: int, r: int) -> int:
    if r == 0:
        return 1
    if not 1 <= r <= n // 2:
        return 0
    return n * comb(n - r, r) // (n - r)


def fixed_closed(n_sites: int, particles: int, n: int) -> int:
    m = min(particles, n_sites - particles)
    g = gcd(n_sites, n)
    repeats = n_sites // g
    return independent_count(g, m // repeats) if m % repeats == 0 else 0


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mu(n: int) -> int:
    factors = 0
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            if n % p == 0:
                return 0
            factors += 1
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        factors += 1
    return -1 if factors % 2 else 1


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    data = json.loads(path.read_text())
    body = dict(data)
    claimed_hash = body.pop("payload_sha256")
    encoded = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    require(sha256(encoded).hexdigest() == claimed_hash, "payload hash")
    require(set(data) == {
        "schema", "candidate_id", "date_utc", "source_commit", "scope_literal",
        "source_lock", "classification_theorem", "finite_attraction_theorem",
        "fixed_and_primitive_theorem", "koopman_boundary", "finite_replay",
        "progress_and_boundary", "route_a", "scope_flags", "nonclaims",
        "payload_sha256",
    }, "top-level closure")
    require(data["schema"] == "HCS-C175-v1", "schema")
    require(data["candidate_id"] == "HCS-C175", "candidate")
    require(data["date_utc"] == "2026-08-26", "date")
    require(data["source_commit"] == "100e5f601a0196710d53784bdeef40d2bff89fa8", "source commit")
    require(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")

    lock = data["source_lock"]
    require(set(lock) == {
        "object", "family", "arithmetic_origin", "clock", "normalization",
        "determinant_convention", "cutoff", "precision", "allowed_data", "forbidden_data",
    }, "source lock closure")
    require("Rule 184" in lock["object"] and "every N>=1" in lock["family"], "object and family")
    require(lock["clock"] == "one simultaneous Rule-184 update", "clock")
    require("labelled cyclic sites" in lock["normalization"], "normalization")
    require("Artin--Mazur" in lock["determinant_convention"] and "periodic-core" in lock["determinant_convention"], "determinant convention")
    require("1<=N<=12" in lock["cutoff"] and "1<=n<=2N+2" in lock["cutoff"], "cutoff")
    require("no intrinsic prime" in lock["arithmetic_origin"], "arithmetic origin")
    require("target zero or prime tables" in lock["forbidden_data"] and "Route-B" in lock["forbidden_data"], "forbidden data")

    classification = data["classification_theorem"]
    require(set(classification) == {"local_rule", "low_density", "high_density", "balanced", "uniform", "period_divisibility"}, "classification closure")
    require("10->01" in classification["local_rule"], "local rule")
    require("no cyclic 11" in classification["low_density"] and "right rotation" in classification["low_density"], "low theorem")
    require("no cyclic 00" in classification["high_density"] and "left rotation" in classification["high_density"], "high theorem")
    require("two alternating" in classification["balanced"] and "period two" in classification["balanced"], "balanced theorem")
    require("least period divides N" in classification["period_divisibility"], "period theorem")

    attraction = data["finite_attraction_theorem"]
    require(set(attraction) == {"gap_update", "zero_marker_rule", "lyapunov", "bound", "duality"}, "attraction closure")
    require("g_i'=g_i" in attraction["gap_update"], "gap update")
    require("never increases" in attraction["lyapunov"] and "within at most m" in attraction["lyapunov"], "Lyapunov")
    require("m^2" in attraction["bound"] and "holes" in attraction["duality"], "bound and duality")

    fixed_theorem = data["fixed_and_primitive_theorem"]
    require(set(fixed_theorem) == {"independent_cycle_count", "fixed_count", "exact_points", "primitive_cycles", "zeta", "core_determinant"}, "fixed theorem closure")
    require("gcd(N,n)" in fixed_theorem["fixed_count"] and "q divides m" in fixed_theorem["fixed_count"], "fixed formula text")
    require("mu(d/e)" in fixed_theorem["exact_points"] and "E_(N,k)(d)" in fixed_theorem["exact_points"], "exact formula text")
    require("product_(d|N)" in fixed_theorem["zeta"], "zeta text")
    require("det(I-z*U_core)" in fixed_theorem["core_determinant"] and "1/zeta" in fixed_theorem["core_determinant"], "core determinant text")

    replay = data["finite_replay"]
    require(set(replay) == {
        "N_max", "iterate_n_rule", "sector_rows", "fixed_rows", "primitive_rows",
        "sector_row_count", "fixed_row_count", "primitive_row_count",
        "classified_word_count", "fixed_word_iterate_checks",
        "maximum_observed_core_entry_time",
    }, "replay closure")
    require(replay["N_max"] == 12 and replay["iterate_n_rule"] == "1<=n<=2N+2", "replay bounds")
    require(replay["sector_row_count"] == len(replay["sector_rows"]) == 90, "sector row count")
    require(replay["fixed_row_count"] == len(replay["fixed_rows"]) == 1636, "fixed row count")
    require(replay["primitive_row_count"] == len(replay["primitive_rows"]) == 299, "primitive row count")
    require(replay["classified_word_count"] == 8190, "classified words")
    require(replay["fixed_word_iterate_checks"] == 196608, "fixed checks")
    require(replay["maximum_observed_core_entry_time"] == 5, "maximum entry time")

    sectors = {(row["N"], row["k"]): row for row in replay["sector_rows"]}
    fixed_rows = {(row["N"], row["k"], row["n"]): row for row in replay["fixed_rows"]}
    primitive_rows = {(row["N"], row["k"], row["period_d"]): row for row in replay["primitive_rows"]}
    require(len(sectors) == 90 and len(fixed_rows) == 1636 and len(primitive_rows) == 299, "unique row keys")

    classified_total = 0
    fixed_check_total = 0
    maximum_entry = 0
    for n_sites in range(1, 13):
        by_k = {k: [] for k in range(n_sites + 1)}
        for word in product((0, 1), repeat=n_sites):
            by_k[sum(word)].append(word)
        for particles, words in by_k.items():
            classified_total += len(words)
            minority = min(particles, n_sites - particles)
            dynamic_periodic: list[tuple[int, ...]] = []
            period_counts = {d: 0 for d in divisors(n_sites)}
            entries = []
            images = set()
            for word in words:
                nxt = traffic_move(word)
                require(sum(nxt) == particles, f"particle conservation N={n_sites} word={word}")
                images.add(nxt)
                periodic, period, entry = orbit_data(word)
                require(entry >= 0 and entry <= minority * minority, f"entry bound N={n_sites} word={word}")
                entries.append(entry)
                maximum_entry = max(maximum_entry, entry)
                require(periodic == predicted_core(word), f"periodic classification N={n_sites} word={word}")
                if periodic:
                    require(period is not None and n_sites % period == 0, f"period divides N={n_sites} word={word}")
                    dynamic_periodic.append(word)
                    period_counts[period] += 1

            row = sectors[(n_sites, particles)]
            require(set(row) == {
                "N", "k", "minority_m", "branch", "sector_state_count",
                "periodic_core_count", "periodic_core_formula", "transient_state_count",
                "max_core_entry_time", "proved_entry_bound_m_squared", "full_sector_bijective",
            }, f"sector closure N={n_sites} k={particles}")
            require(row["minority_m"] == minority, f"minority N={n_sites} k={particles}")
            require(row["sector_state_count"] == len(words) == comb(n_sites, particles), f"sector size N={n_sites} k={particles}")
            require(row["periodic_core_count"] == len(dynamic_periodic), f"core count N={n_sites} k={particles}")
            require(row["periodic_core_formula"] == independent_count(n_sites, minority), f"core formula N={n_sites} k={particles}")
            require(row["transient_state_count"] == len(words) - len(dynamic_periodic), f"transients N={n_sites} k={particles}")
            require(row["max_core_entry_time"] == max(entries), f"entry max N={n_sites} k={particles}")
            require(row["proved_entry_bound_m_squared"] == minority * minority, f"entry bound text N={n_sites} k={particles}")
            require(row["full_sector_bijective"] == (len(images) == len(words)) == (minority <= 1), f"bijection boundary N={n_sites} k={particles}")

            current = {word: word for word in words}
            fixed_counts: dict[int, int] = {}
            for n in range(1, 2 * n_sites + 3):
                current = {word: traffic_move(image) for word, image in current.items()}
                observed = sum(image == word for word, image in current.items())
                fixed_check_total += len(words)
                formula = fixed_closed(n_sites, particles, n)
                fixed_counts[n] = formula
                item = fixed_rows[(n_sites, particles, n)]
                require(set(item) == {"N", "k", "n", "gcd_N_n", "repetition_q", "fixed_count_formula", "fixed_count_enumerated"}, f"fixed closure N={n_sites} k={particles} n={n}")
                require(item["gcd_N_n"] == gcd(n_sites, n), f"gcd N={n_sites} k={particles} n={n}")
                require(item["repetition_q"] == n_sites // gcd(n_sites, n), f"q N={n_sites} k={particles} n={n}")
                require(item["fixed_count_formula"] == item["fixed_count_enumerated"] == formula == observed, f"fixed count N={n_sites} k={particles} n={n}")

            for d in divisors(n_sites):
                exact = sum(mu(d // e) * fixed_counts[e] for e in divisors(d))
                item = primitive_rows[(n_sites, particles, d)]
                require(set(item) == {"N", "k", "period_d", "exact_periodic_points", "primitive_cycles", "enumerated_exact_periodic_points"}, f"primitive closure N={n_sites} k={particles} d={d}")
                require(item["exact_periodic_points"] == item["enumerated_exact_periodic_points"] == exact == period_counts[d], f"exact points N={n_sites} k={particles} d={d}")
                require(item["primitive_cycles"] == exact // d and exact % d == 0, f"primitive cycles N={n_sites} k={particles} d={d}")

    require(classified_total == replay["classified_word_count"], "classified total")
    require(fixed_check_total == replay["fixed_word_iterate_checks"], "fixed total")
    require(maximum_entry == replay["maximum_observed_core_entry_time"], "entry total")

    koopman = data["koopman_boundary"]
    require(set(koopman) == {"whole_sector", "transient_boundary", "periodic_core", "reversal"}, "Koopman closure")
    require("exactly when m<=1" in koopman["whole_sector"], "whole-sector boundary")
    require("m>=2" in koopman["transient_boundary"] and "not unitary" in koopman["transient_boundary"], "transient operator boundary")
    require("canonical periodic core" in koopman["periodic_core"] and "unitary" in koopman["periodic_core"], "core unitary")
    require("discards full-system transients" in koopman["reversal"], "reversal boundary")

    route = data["route_a"]
    require(set(route) == {"tuple", "overall", "A0_qualification", "A1_qualification", "A2_qualification", "A3_qualification", "A4_qualification", "route_b_invocation_allowed"}, "route closure")
    require(route["tuple"] == ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "route tuple")
    require(route["overall"] == "ROUTE_A_REJECTED", "overall")
    require(route["A1_qualification"] == "COMPLETE_INTRINSIC_PRIMITIVE_CYCLES_WITHOUT_ARITHMETIC_INFORMATION", "A1 qualification")
    require("PERIODIC_CORE" in route["A4_qualification"] and "TRANSIENTS" in route["A4_qualification"], "A4 qualification")
    require(route["route_b_invocation_allowed"] is False, "Route B")
    require(not any(data["scope_flags"].values()), "scope flags")
    require(len(data["nonclaims"]) == 5, "nonclaims")
    nonclaims = " ".join(data["nonclaims"])
    require("novelty" in nonclaims and "root numbers" in nonclaims and "external peer review" in nonclaims, "nonclaim boundary")
    print(json.dumps({"status": "C175_INDEPENDENT_CHECK_PASS", "assertions": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
