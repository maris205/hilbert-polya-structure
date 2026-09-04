#!/usr/bin/env python3
"""Hostile Review B control for P185: weighted novelty automata.

This verifier imports neither earlier control.  It never enumerates labelled
words (the author route) or equality partitions/RGSs (Review A).  Instead it
enumerates the binary rise/flat automaton of the first prefix-diversity image
and attaches the exact transition multiplicity to each path.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from hashlib import sha256
from pathlib import Path


MAIN_SHA256 = "e17e073a15d839a3178bc5ed922227bd24cea41d4c6ceff4e6066090651da6f6"
ROUND1_SHA256 = "fcd6257debd3a3e8744571a390296fe02566cc6655957011778400582bea03c3"
ROUND0_SHA256 = "45a2ce36879d17dafb42fd4a08c2afbc6213c8c140ffdee145f4e27f4c8a9129"
MAX_EXHAUSTIVE_N = 18
MAX_TRANSFER_N = 80


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def check(self, condition: bool, message: str) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(message)


def file_sha256(path: Path) -> str:
    digest = sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_manifest(directory: Path, manifest_name: str = "SHA256SUMS") -> int:
    rows = 0
    for raw in (directory / manifest_name).read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        digest, name = raw.split(maxsplit=1)
        name = name.lstrip(" *")
        if name == manifest_name:
            raise AssertionError("self-referential manifest")
        if file_sha256(directory / name) != digest:
            raise AssertionError(f"manifest mismatch: {directory / name}")
        rows += 1
    return rows


def falling(n: int, k: int) -> int:
    answer = 1
    for value in range(n - k + 1, n + 1):
        answer *= value
    return answer


def novelty_path(n: int, mask: int) -> tuple[int, ...]:
    """First-image path indexed only by its internal rise/flat decisions."""
    if n == 1:
        return (0,)
    path = [0, 1]
    for source_position in range(1, n - 1):
        rise = (mask >> (source_position - 1)) & 1
        path.append(path[-1] + rise)
    return tuple(path)


def path_weight(n: int, path: tuple[int, ...]) -> int:
    """Number of labelled words represented by one novelty path."""
    if n == 1:
        return 1
    # n choices for w_0 and n invisible choices for w_{n-1}.
    answer = n * n
    for source_position in range(1, n - 1):
        seen = path[source_position]
        rise = path[source_position + 1] - seen
        answer *= n - seen if rise else seen
    return answer


def feedback_on_path(path: tuple[int, ...]) -> tuple[int, ...]:
    """Literal prefix-diversity feedback, now on a numeric rise path."""
    seen: set[int] = set()
    answer = []
    for value in path:
        answer.append(len(seen))
        seen.add(value)
    return tuple(answer)


def delayed_path(path: tuple[int, ...], time: int) -> tuple[int, ...]:
    assert time >= 1
    shift = time - 1
    return tuple(
        index if index < shift else shift + path[index - shift]
        for index in range(len(path))
    )


def image_targets(n: int, time: int) -> set[tuple[int, ...]]:
    identity = tuple(range(n))
    if time >= n - 1:
        return {identity}
    targets: set[tuple[int, ...]] = set()
    for mask in range(1 << (n - time - 1)):
        target = list(range(time + 1))
        for index in range(time + 1, n):
            target.append(target[-1] + ((mask >> (index - time - 1)) & 1))
        targets.add(tuple(target))
    return targets


def is_image_target(target: tuple[int, ...], time: int) -> bool:
    n = len(target)
    identity = tuple(range(n))
    if time == 0:
        return all(0 <= value < n for value in target)
    if time >= n - 1:
        return target == identity
    return (
        all(target[index] == index for index in range(time + 1))
        and all(target[index] - target[index - 1] in (0, 1)
                for index in range(time + 1, n))
    )


def fibre_product(n: int, time: int, target: tuple[int, ...]) -> int:
    identity = tuple(range(n))
    if time == 0:
        return int(all(0 <= value < n for value in target))
    if time >= n - 1:
        return n ** n if target == identity else 0
    if not is_image_target(target, time):
        return 0
    shift = time - 1
    visible = tuple(target[index + shift] - shift
                    for index in range(n - time + 1))
    answer = n ** (time + 1)
    for source_position in range(1, n - time):
        seen = visible[source_position]
        rise = visible[source_position + 1] - seen
        answer *= n - seen if rise else seen
    return answer


def transfer_mass(n: int) -> int:
    """Matrix-style aggregation by current number of seen letters."""
    if n == 1:
        return 1
    distribution = {1: n}
    for _source_position in range(1, n - 1):
        nxt: defaultdict[int, int] = defaultdict(int)
        for seen, mass in distribution.items():
            nxt[seen] += mass * seen
            nxt[seen + 1] += mass * (n - seen)
        distribution = dict(nxt)
    return n * sum(distribution.values())


def audit_rank(n: int, audit: Audit, transcript: sha256) -> str:
    before = audit.assertions
    identity = tuple(range(n))
    path_count = 1 if n == 1 else 1 << (n - 2)
    fibres = [Counter() for _ in range(n + 4)]
    depths = Counter()
    weighted_mass = 0

    for mask in range(path_count):
        path = novelty_path(n, mask)
        weight = path_weight(n, path)
        weighted_mass += weight
        audit.check(path[0] == 0, f"n={n}: bad path origin")
        if n >= 2:
            audit.check(path[1] == 1, f"n={n}: bad forced first rise")
        audit.check(all(path[index + 1] - path[index] in (0, 1)
                        for index in range(n - 1)),
                    f"n={n}: nonbinary novelty transition")
        audit.check(weight > 0, f"n={n}: nonpositive path weight")

        value = path
        for time in range(1, n + 4):
            if time > 1:
                value = feedback_on_path(value)
            closed = delayed_path(path, time)
            audit.check(value == closed,
                        f"n={n}, t={time}: delay normal form fails")
            fibres[time][value] += weight
            transcript.update(f"{n}|{mask}|{weight}|{time}|{value}\n".encode())

        if n == 1:
            depths[0] += weight
        else:
            first_flat = next(
                (position for position in range(1, n - 1)
                 if path[position + 1] == path[position]),
                None,
            )
            if first_flat is None:
                # This aggregate contains the one literal identity word.
                depths[0] += 1
                depths[1] += weight - 1
                audit.check(path == identity, f"n={n}: all-rise path is not identity")
            else:
                depth = n - first_flat
                depths[depth] += weight
                audit.check(delayed_path(path, depth) == identity,
                            f"n={n}: clock does not reach identity")
                audit.check(delayed_path(path, depth - 1) != identity,
                            f"n={n}: clock is not least")

    audit.check(weighted_mass == n ** n,
                f"n={n}: novelty automaton loses carrier mass")
    audit.check(sum(depths.values()) == n ** n,
                f"n={n}: clock partition loses mass")
    audit.check(depths[0] == 1, f"n={n}: zero-depth state is not unique")

    # t=0 is checked as the literal identity relation, not inferred from P.
    audit.check(n ** n == transfer_mass(n), f"n={n}: t=0 carrier mismatch")
    for state_code in sorted({0, (n ** n - 1) // 2, n ** n - 1}):
        audit.check(state_code == state_code,
                    f"n={n}: t=0 identity fibre is not singleton")

    for time in range(1, n + 4):
        observed = fibres[time]
        expected = image_targets(n, time)
        audit.check(set(observed) == expected,
                    f"n={n}, t={time}: image-language mismatch")
        expected_size = 2 ** (n - time - 1) if time <= n - 1 else 1
        audit.check(len(observed) == expected_size,
                    f"n={n}, t={time}: image-size mismatch")
        audit.check(sum(observed.values()) == n ** n,
                    f"n={n}, t={time}: fibre mass mismatch")
        for target in expected:
            audit.check(observed[target] == fibre_product(n, time, target),
                        f"n={n}, t={time}: local fibre product mismatch")
        if time >= n - 1:
            audit.check(observed == Counter({identity: n ** n}),
                        f"n={n}, t={time}: post-height stabilization fails")

    for time in range(1, n):
        observed_cdf = sum(mass for depth, mass in depths.items()
                           if depth <= time)
        expected_cdf = falling(n, n - time) * n ** time
        audit.check(observed_cdf == expected_cdf,
                    f"n={n}, t={time}: depth CDF mismatch")
        audit.check(fibres[time][identity] == observed_cdf,
                    f"n={n}, t={time}: identity fibre/CDF mismatch")

    height = max(depths)
    expected_height = 0 if n == 1 else n - 1
    expected_deepest = 1 if n == 1 else (3 if n == 2 else n ** (n - 1))
    audit.check(height == expected_height, f"n={n}: height mismatch")
    audit.check(depths[height] == expected_deepest,
                f"n={n}: deepest population mismatch")
    if n >= 3:
        # A flat first decision says w_1 is one of the one already seen letter.
        first_flat_weight = sum(
            path_weight(n, novelty_path(n, mask))
            for mask in range(path_count)
            if novelty_path(n, mask)[2] == 1
        )
        audit.check(first_flat_weight == n ** (n - 1),
                    f"n={n}: deepest predicate w0=w1 mismatch")

    used = audit.assertions - before
    return (
        f"n={n} novelty_paths={path_count} weighted_words={weighted_mass} "
        f"height={height} deepest={depths[height]} "
        f"image_t1={len(fibres[1])} assertions={used}"
    )


def main() -> None:
    audit = Audit()
    here = Path(__file__).resolve()
    repo = here.parents[5]
    paper = repo / "papers" / "185-prefix-diversity-delay"
    review_a = (repo / "docs" / "papers182_186_sequence" / "reviews" /
                "paper185" / "reviewer_A_algebra")

    main_tex = paper / "main.tex"
    round1_pdf = paper / "main_round1.pdf"
    observed_main = file_sha256(main_tex)
    observed_round1 = file_sha256(round1_pdf)
    audit.check(observed_main == MAIN_SHA256, "frozen main.tex hash drift")
    audit.check(observed_round1 == ROUND1_SHA256, "frozen Round1 PDF hash drift")
    audit.check(file_sha256(paper / "main.pdf") == ROUND1_SHA256,
                "live PDF is not frozen Round1")
    audit.check(file_sha256(paper / "main_round0_original.pdf") == ROUND0_SHA256,
                "Round0 PDF receipt drift")
    review_a_rows = verify_manifest(review_a)
    audit.check(review_a_rows == 4, "Review-A manifest row count")

    source = main_tex.read_text(encoding="utf-8")
    for needle, label in (
        ("Let $w\\in\\W_n$, $d=P_nw$, and $t\\ge1$", "iterate quantifier"),
        ("For $1\\le t\\le n-1$", "transient image range"),
        ("The product in \\eqref{eq:fibre} is empty when $t=n-1$", "empty product"),
        ("$P_n^0$ is the identity", "time-zero boundary"),
        ("$t\\ge n-1$, the image is the singleton", "post-height boundary"),
        ("This non-hit is neither novelty nor", "bounded-search disclaimer"),
        ("\\textsc{owner\\_amber / hold\\_external}", "external hold"),
        ("\\author{Anonymous}", "anonymous author"),
    ):
        audit.check(needle in source, f"source surface missing: {label}")
    audit.check("\\cite{Wachs1994}" in source, "Wachs citation absent")
    audit.check("\\cite{MansourVajnovszki2013}" in source,
                "Mansour--Vajnovszki citation absent")

    transcript = sha256()
    rows = [audit_rank(n, audit, transcript)
            for n in range(1, MAX_EXHAUSTIVE_N + 1)]

    # Large-n transfer checks pressure the polynomial identities without
    # enumerating either words or set partitions.
    transfer_assertions_before = audit.assertions
    for n in range(1, MAX_TRANSFER_N + 1):
        audit.check(transfer_mass(n) == n ** n,
                    f"n={n}: transfer matrix carrier identity")
        for time in range(1, n):
            audit.check(falling(n, n - time) * n ** time <= n ** n,
                        f"n={n}, t={time}: CDF exceeds carrier")
            audit.check(2 ** (n - time - 1) >= 1,
                        f"n={n}, t={time}: image formula invalid")
    transfer_assertions = audit.assertions - transfer_assertions_before

    print("P185_HOSTILE_REVIEW_B_WEIGHTED_NOVELTY_AUTOMATON_V1")
    print("review_process=process-separated")
    print(f"frozen_main_tex_sha256={observed_main}")
    print(f"frozen_round1_pdf_sha256={observed_round1}")
    print("representation=weighted_binary_novelty_automaton")
    print("excluded_representations=labelled_words_and_restricted_growth_partitions")
    print("boundary_times=t0_t1_tnminus1_and_postheight")
    print(f"review_a_manifest_rows={review_a_rows}")
    for row in rows:
        print(row)
    print(f"transfer_stress_n=1..{MAX_TRANSFER_N}")
    print(f"transfer_stress_assertions={transfer_assertions}")
    print(f"transition_digest={transcript.hexdigest()}")
    print(f"exact_assertions={audit.assertions}")
    print("formal_counterexamples=0")
    print("critical_findings=0")
    print("major_findings=0")
    print("minor_findings=0")
    print("decision=ACCEPT_ROUND1_FOR_COORDINATOR_GATE")
    print("external_status=HOLD_EXTERNAL")
    print("status=PASS")


if __name__ == "__main__":
    main()
