#!/usr/bin/env python3
"""Exact replay for normalizer dynamics on all subgroups of D_{2n}.

The literal carrier is the complete subgroup set of

    D_{2n}=<r,s | r^n=s^2=1, srs=r^{-1}>,  n >= 3,

and the update is H -> N_{D_{2n}}(H).  Every audited normalizer is first
computed from element-set conjugation.  The script then independently checks
the divisor-coordinate theorem, all-time images and target fibres, the depth
polynomial, and explicit graph conjugacies for arithmetically different n.
It uses integers only and no external package.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from hashlib import sha256


BOXES = (
    3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 18, 20, 21,
    22, 24, 25, 27, 28, 30, 32, 33, 35, 36, 40, 42, 44, 45,
    48, 50, 52, 54, 56, 60, 63, 64, 66, 70, 72, 75, 80, 84,
)

ISO_PAIRS = ((33, 35), (66, 70), (132, 140), (264, 280))


@dataclass
class Checks:
    assertions: int = 0

    def equal(self, got, expected, label: str) -> None:
        self.assertions += 1
        if got != expected:
            raise AssertionError(f"{label}: got {got!r}, expected {expected!r}")

    def true(self, condition: bool, label: str) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(label)


def divisors(n: int) -> tuple[int, ...]:
    return tuple(d for d in range(1, n + 1) if n % d == 0)


def tau(n: int) -> int:
    return len(divisors(n))


def sigma(n: int) -> int:
    return sum(divisors(n))


def v2(n: int) -> int:
    out = 0
    while n % 2 == 0:
        n //= 2
        out += 1
    return out


def odd_part(n: int) -> int:
    return n >> v2(n)


def mul(left: tuple[int, int], right: tuple[int, int], n: int) -> tuple[int, int]:
    a, b = left
    c, d = right
    return ((a + (c if b == 0 else -c)) % n, (b + d) % 2)


def inv(element: tuple[int, int], n: int) -> tuple[int, int]:
    a, b = element
    return ((-a) % n, 0) if b == 0 else (a, 1)


def conjugate(g: tuple[int, int], h: tuple[int, int], n: int) -> tuple[int, int]:
    return mul(mul(g, h, n), inv(g, n), n)


Key = tuple[str, int, int]


def subgroup_entries(n: int) -> tuple[tuple[Key, frozenset[tuple[int, int]]], ...]:
    entries: list[tuple[Key, frozenset[tuple[int, int]]]] = []
    for d in divisors(n):
        rotations = frozenset((x, 0) for x in range(0, n, d))
        entries.append((("R", d, 0), rotations))
    for d in divisors(n):
        rotations = {(x, 0) for x in range(0, n, d)}
        for j in range(d):
            reflections = {((j + x) % n, 1) for x in range(0, n, d)}
            entries.append((("H", d, j), frozenset(rotations | reflections)))
    return tuple(entries)


def predicted_next(key: Key) -> Key:
    kind, d, j = key
    if kind == "R":
        return ("H", 1, 0)
    if d % 2:
        return key
    return ("H", d // 2, j % (d // 2))


def literal_graph(n: int, checks: Checks) -> tuple[dict[Key, frozenset], dict[Key, Key]]:
    entries = subgroup_entries(n)
    key_to_set = dict(entries)
    set_to_key = {value: key for key, value in entries}
    checks.equal(len(key_to_set), tau(n) + sigma(n), f"classification count n={n}")
    checks.equal(len(set_to_key), len(key_to_set), f"classification uniqueness n={n}")

    group = tuple((a, b) for b in (0, 1) for a in range(n))
    next_map: dict[Key, Key] = {}
    for key, subgroup in entries:
        normalizer = frozenset(
            g for g in group
            if all(conjugate(g, h, n) in subgroup for h in subgroup)
        )
        checks.true(normalizer in set_to_key, f"normalizer is a subgroup n={n}, key={key}")
        next_map[key] = set_to_key[normalizer]
        checks.equal(next_map[key], predicted_next(key), f"normalizer formula n={n}, key={key}")
        checks.true(subgroup <= normalizer, f"inflationary n={n}, key={key}")
    return key_to_set, next_map


def iterate(next_map: dict[Key, Key], key: Key, t: int) -> Key:
    for _ in range(t):
        key = next_map[key]
    return key


def tail(next_map: dict[Key, Key], key: Key) -> int:
    out = 0
    while next_map[key] != key:
        key = next_map[key]
        out += 1
    return out


def expected_depths(n: int) -> Counter[int]:
    a = v2(n)
    s = sigma(odd_part(n))
    out = Counter({0: s, 1: tau(n)})
    for k in range(1, a + 1):
        out[k] += (1 << k) * s
    return out


def expected_fibre(n: int, target: Key, t: int) -> int:
    kind, d, _ = target
    if kind == "R":
        return 0
    a = v2(n)
    k = v2(d)
    if k == 0:
        tree_mass = (1 << (min(t, a) + 1)) - 1
        return tree_mass + (tau(n) if target == ("H", 1, 0) else 0)
    return (1 << t) if k + t <= a else 0


def expected_image_size(n: int, t: int) -> int:
    a = v2(n)
    s = sigma(odd_part(n))
    top = max(a - t, 0)
    return s * ((1 << (top + 1)) - 1)


def graph_signature(n: int) -> tuple[int, int, int]:
    return (v2(n), sigma(odd_part(n)), tau(n))


def root_list(n: int) -> list[tuple[int, int]]:
    roots = [(e, j) for e in divisors(odd_part(n)) for j in range(e)]
    return [(1, 0)] + sorted(root for root in roots if root != (1, 0))


def explicit_conjugacy(n: int, q: int) -> dict[Key, Key]:
    """Canonical graph conjugacy when the arithmetic signatures agree."""
    if graph_signature(n) != graph_signature(q):
        raise ValueError("signatures differ")
    roots_n = root_list(n)
    roots_q = root_list(q)
    root_match = dict(zip(roots_n, roots_q, strict=True))
    out: dict[Key, Key] = {}

    rotations_n = [("R", d, 0) for d in divisors(n)]
    rotations_q = [("R", d, 0) for d in divisors(q)]
    out.update(zip(rotations_n, rotations_q, strict=True))

    for key, _ in subgroup_entries(n):
        kind, d, j = key
        if kind == "R":
            continue
        k = v2(d)
        e = d >> k
        root = (e, j % e)
        offset = (j - (j % e)) // e
        e2, j2 = root_match[root]
        out[key] = ("H", (1 << k) * e2, j2 + offset * e2)
    return out


def audit_box(n: int, checks: Checks) -> str:
    key_to_set, next_map = literal_graph(n, checks)
    keys = tuple(key_to_set)
    a = v2(n)
    m = odd_part(n)
    s = sigma(m)

    actual_depths = Counter(tail(next_map, key) for key in keys)
    checks.equal(actual_depths, expected_depths(n), f"depth polynomial n={n}")
    checks.equal(max(actual_depths), max(1, a), f"sharp clock n={n}")
    fixed = {key for key in keys if next_map[key] == key}
    expected_fixed = {
        ("H", e, j) for e in divisors(m) for j in range(e)
    }
    checks.equal(fixed, expected_fixed, f"fixed-root atlas n={n}")
    checks.equal(len(fixed), s, f"fixed count n={n}")

    for t in range(1, a + 4):
        fibres: dict[Key, list[Key]] = defaultdict(list)
        for source in keys:
            fibres[iterate(next_map, source, t)].append(source)
        checks.equal(len(fibres), expected_image_size(n, t), f"image n={n}, t={t}")
        checks.equal(sum(map(len, fibres.values())), len(keys), f"mass n={n}, t={t}")
        for target in keys:
            checks.equal(
                len(fibres[target]), expected_fibre(n, target, t),
                f"target fibre n={n}, t={t}, target={target}",
            )
        fixed_t = {key for key in keys if iterate(next_map, key, t) == key}
        checks.equal(fixed_t, fixed, f"fixed iterate n={n}, t={t}")

    one_image = expected_image_size(n, 1)
    depth_text = "/".join(f"{k}:{actual_depths[k]}" for k in sorted(actual_depths))
    return (
        f"BOX n={n:3d} a={a} odd={m:3d} states={len(keys):4d} "
        f"fixed={s:3d} image1={one_image:3d} max_tail={max(actual_depths)} "
        f"signature={graph_signature(n)} depths={depth_text}"
    )


def audit_isomorphic_pair(n: int, q: int, checks: Checks) -> str:
    checks.equal(graph_signature(n), graph_signature(q), f"pair signature {n},{q}")
    keys_n = dict(subgroup_entries(n))
    keys_q = dict(subgroup_entries(q))
    next_n = {key: predicted_next(key) for key in keys_n}
    next_q = {key: predicted_next(key) for key in keys_q}
    phi = explicit_conjugacy(n, q)
    checks.equal(set(phi), set(keys_n), f"conjugacy domain {n},{q}")
    checks.equal(set(phi.values()), set(keys_q), f"conjugacy codomain {n},{q}")
    checks.equal(len(set(phi.values())), len(phi), f"conjugacy bijective {n},{q}")
    for key in keys_n:
        checks.equal(phi[next_n[key]], next_q[phi[key]], f"conjugacy square {n},{q},{key}")
    return f"ISO n={n} q={q} signature={graph_signature(n)} states={len(keys_n)} PASS"


def main() -> None:
    checks = Checks()
    profile: list[str] = []
    print("GDN_GENERAL_DIHEDRAL_NORMALIZER_REPLAY_V1")
    print("DOMAIN n>=3; complete subgroup carrier of D_(2n); update H->N_D(H)")
    print("SYMBOLIC H_(d,j)->H_(d/gcd(d,2),j mod d/gcd(d,2)); rotations->G")
    print("SYMBOLIC depth(R_d)=1; depth(H_(d,j))=v2(d); fixed roots=SIGMA(oddpart(n))")
    print("SYMBOLIC signature=(v2(n),SIGMA(oddpart(n)),TAU(n)); signature classifies graph")
    for n in BOXES:
        line = audit_box(n, checks)
        profile.append(line)
        print(line)
    for n, q in ISO_PAIRS:
        line = audit_isomorphic_pair(n, q, checks)
        profile.append(line)
        print(line)
    digest = sha256("\n".join(profile).encode()).hexdigest()
    print(f"PROFILE_SHA256 {digest}")
    print(f"TOTAL boxes={len(BOXES)} iso_pairs={len(ISO_PAIRS)} assertions={checks.assertions}")
    print("VERDICT PASS_EXACT_REPLAY")


if __name__ == "__main__":
    main()
