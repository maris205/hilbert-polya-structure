#!/usr/bin/env python3
"""Prefreeze C62 exact lambda-square finite-group producer."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[3]
C61 = ROOT / "henon_dynamics/henon_mu3_yukawa_tensor_fourier_descent"
INPUT = C61 / "results/c61_group_evidence.json"
OUTPUT = Path(__file__).resolve().parents[1] / "results/c62_lambda_evidence.json"

Perm = tuple[int, ...]


def compose(left: Perm, right: Perm) -> Perm:
    return tuple(left[right[i]] for i in range(len(left)))


def inverse(p: Perm) -> Perm:
    q = [0] * len(p)
    for i, j in enumerate(p):
        q[j] = i
    return tuple(q)


def from_one(rows: Iterable[Iterable[int]]) -> tuple[Perm, ...]:
    return tuple(tuple(x - 1 for x in row) for row in rows)


def closure(generators: Iterable[Perm]) -> frozenset[Perm]:
    gens = tuple(generators)
    identity = tuple(range(len(gens[0])))
    out = {identity}
    stack = [identity]
    while stack:
        x = stack.pop()
        for g in gens:
            y = compose(g, x)
            if y not in out:
                out.add(y)
                stack.append(y)
    return frozenset(out)


def canonical_json(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(value: object) -> str:
    return hashlib.sha256(canonical_json(value)).hexdigest()


def right_cosets(group: frozenset[Perm], subgroup: frozenset[Perm]) -> tuple[tuple[Perm, ...], dict[Perm, int]]:
    unseen = set(group)
    reps: list[Perm] = []
    lookup: dict[Perm, int] = {}
    while unseen:
        rep = min(unseen)
        idx = len(reps)
        coset = {compose(rep, h) for h in subgroup}
        if not coset <= unseen:
            raise RuntimeError("right coset overlap")
        reps.append(rep)
        for x in coset:
            lookup[x] = idx
        unseen.difference_update(coset)
    return tuple(reps), lookup


class Cosets:
    def __init__(self, group: frozenset[Perm], subgroup: frozenset[Perm]) -> None:
        self.reps, self.lookup = right_cosets(group, subgroup)
        self.degree = len(self.reps)

    def image(self, g: Perm, i: int) -> int:
        return self.lookup[compose(g, self.reps[i])]


def small_generators(group: frozenset[Perm]) -> tuple[Perm, ...]:
    identity = tuple(range(len(next(iter(group)))))
    chosen: list[Perm] = []
    current = frozenset({identity})
    for g in sorted(group):
        if g in current:
            continue
        chosen.append(g)
        current = closure(chosen)
        if current == group:
            return tuple(chosen)
    raise RuntimeError("failed to find subgroup generators")


def group_digest(group: frozenset[Perm]) -> str:
    return digest([[x + 1 for x in p] for p in sorted(group)])


def conjugator(ambient: frozenset[Perm], source: frozenset[Perm], target: frozenset[Perm]) -> bool:
    gens = small_generators(source)
    for g in ambient:
        if all(compose(compose(g, h), inverse(g)) in target for h in gens):
            return True
    return False


def orbit_atlas(action: Cosets, ambient_gens: tuple[Perm, ...], ambient: frozenset[Perm], *, symmetric: bool) -> list[dict[str, object]]:
    n = action.degree
    unseen = {(i, j) for i in range(n) for j in range(i, n if symmetric else n) if symmetric or i < j}
    gens = ambient_gens + tuple(inverse(g) for g in ambient_gens)
    rows: list[dict[str, object]] = []
    while unseen:
        seed = min(unseen)
        seen = {seed}
        stack = [seed]
        while stack:
            a, b = stack.pop()
            for g in gens:
                x, y = action.image(g, a), action.image(g, b)
                z = (x, y) if x <= y else (y, x)
                if z not in seen:
                    seen.add(z)
                    stack.append(z)
        unseen.difference_update(seen)
        stabilizer = frozenset(
            g for g in ambient
            if tuple(sorted((action.image(g, seed[0]), action.image(g, seed[1])))) == seed
        )
        rows.append({
            "orbit_size": len(seen),
            "seed": list(seed),
            "stabilizer_order": len(stabilizer),
            "stabilizer_sha256": group_digest(stabilizer),
            "orbit_sha256": digest(sorted([list(x) for x in seen])),
            "stabilizer": stabilizer,
        })
    rows.sort(key=lambda row: (int(row["orbit_size"]), row["seed"]))
    return rows


def public_rows(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    return [{k: v for k, v in row.items() if k != "stabilizer"} for row in rows]


def fixed_points(action: Cosets, g: Perm) -> int:
    return sum(action.image(g, i) == i for i in range(action.degree))


def main() -> int:
    data = json.loads(INPUT.read_text())
    ambient_data = data["python_projection"]["ambient"]
    wgens = from_one(ambient_data["W_generators_one_based"])
    hp = closure(from_one(ambient_data["Hplus_generators_one_based"]))
    hm = closure(from_one(ambient_data["Hminus_generators_one_based"]))
    ambient = closure(wgens)
    plus, minus = Cosets(ambient, hp), Cosets(ambient, hm)
    if plus.degree != 320 or minus.degree != 320 or len(ambient) != 51840:
        raise RuntimeError("C61 action dimensions do not rebind")

    ext_plus = orbit_atlas(plus, wgens, ambient, symmetric=False)
    ext_minus = orbit_atlas(minus, wgens, ambient, symmetric=False)
    sym_plus = orbit_atlas(plus, wgens, ambient, symmetric=True)
    sym_minus = orbit_atlas(minus, wgens, ambient, symmetric=True)

    ext_char_equal = True
    sym_char_equal = True
    for g in ambient:
        g2 = compose(g, g)
        xp, xm = fixed_points(plus, g), fixed_points(minus, g)
        yp, ym = fixed_points(plus, g2), fixed_points(minus, g2)
        ext_char_equal &= (xp * xp - yp) == (xm * xm - ym)
        sym_char_equal &= (xp * xp + yp) == (xm * xm + ym)
    if not ext_char_equal or not sym_char_equal:
        raise RuntimeError("lambda character equality failed")

    ext_matches = []
    for p, m in zip(ext_plus, ext_minus):
        p_stab, m_stab = p["stabilizer"], m["stabilizer"]
        ext_matches.append({
            "orbit_size": p["orbit_size"],
            "plus_stabilizer_sha256": p["stabilizer_sha256"],
            "minus_stabilizer_sha256": m["stabilizer_sha256"],
            "conjugate": conjugator(ambient, m_stab, p_stab),
        })

    result = {
        "schema_id": "hcs-c62-lambda-prefreeze-v1",
        "status": "PREFREEZE_CODE_RESULTS_PASS",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "authority": {
            "c61_group_evidence_sha256": hashlib.sha256(INPUT.read_bytes()).hexdigest(),
            "ambient_order": len(ambient),
            "hplus_order": len(hp),
            "hminus_order": len(hm),
            "coset_degree": plus.degree,
        },
        "character_identities": {
            "exterior_square_equal": ext_char_equal,
            "symmetric_square_equal": sym_char_equal,
            "formula": "fixed_2_subsets=(fixed(g)^2-fixed(g^2))/2; fixed_multisets=(fixed(g)^2+fixed(g^2))/2",
        },
        "sizes": {"exterior_square": 320 * 319 // 2, "symmetric_square": 320 * 321 // 2},
        "exterior_square": {
            "plus": public_rows(ext_plus),
            "minus": public_rows(ext_minus),
            "stabilizer_matches": ext_matches,
        },
        "symmetric_square": {"plus": public_rows(sym_plus), "minus": public_rows(sym_minus)},
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(canonical_json(result))
    print(json.dumps({
        "output": str(OUTPUT),
        "status": result["status"],
        "ext_orbits": len(ext_plus),
        "sym_orbits": len(sym_plus),
        "ext_nonconjugate_matches": sum(not x["conjugate"] for x in ext_matches),
        "character_identities": result["character_identities"],
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())

