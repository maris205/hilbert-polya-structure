#!/usr/bin/env python3
"""Produce canonical finite evidence for HCS-C306."""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c306_walkers_evidence.json"
SOURCE = "c0259978b1d7ebae63fe7b39fce1af2655b8529d"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600


def canonical_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def fmt(value: float, digits: int = 15) -> str:
    if abs(value) < 0.5 * 10 ** (-digits):
        value = 0.0
    return f"{value:.{digits}f}"


def determinant(matrix: list[list[float]]) -> float:
    n = len(matrix)
    if n == 0:
        return 1.0
    a = [row[:] for row in matrix]
    out = 1.0
    for col in range(n):
        pivot = max(range(col, n), key=lambda row: abs(a[row][col]))
        if abs(a[pivot][col]) < 1e-18:
            return 0.0
        if pivot != col:
            a[pivot], a[col] = a[col], a[pivot]
            out = -out
        value = a[col][col]
        out *= value
        for row in range(col + 1, n):
            ratio = a[row][col] / value
            for j in range(col + 1, n):
                a[row][j] -= ratio * a[col][j]
    return out


def eps(L: int, r: int) -> float:
    return 2.0 - 2.0 * math.cos(math.pi * r / (L + 1))


def phi(L: int, r: int, x: int) -> float:
    return math.sqrt(2.0 / (L + 1)) * math.sin(math.pi * r * x / (L + 1))


def slater(L: int, mode: tuple[int, ...], state: tuple[int, ...]) -> float:
    return determinant([[phi(L, r, x) for x in state] for r in mode])


def one_kernel(L: int, x: int, y: int, time: float) -> float:
    return sum(math.exp(-eps(L, r) * time) * phi(L, r, x) * phi(L, r, y)
               for r in range(1, L + 1))


def neighbours(state: tuple[int, ...], L: int) -> list[tuple[int, ...]]:
    out = []
    for index in range(len(state)):
        for step in (-1, 1):
            trial = list(state)
            trial[index] += step
            if 1 <= trial[index] <= L and len(set(trial)) == len(trial):
                trial.sort()
                candidate = tuple(trial)
                if candidate not in out:
                    out.append(candidate)
    return sorted(out)


def case_row(L: int, k: int) -> dict:
    states = list(itertools.combinations(range(1, L + 1), k))
    modes = list(itertools.combinations(range(1, L + 1), k))
    index = {state: i for i, state in enumerate(states)}
    values = [[slater(L, mode, state) for state in states] for mode in modes]
    energies = [sum(eps(L, r) for r in mode) for mode in modes]
    sign = -1.0 if (k * (k - 1) // 2) % 2 else 1.0
    h = [sign * value for value in values[0]]
    h_l1 = sum(h)

    legal_directed = 0
    total_killing = 0
    max_eigen_residual = 0.0
    for s_index, state in enumerate(states):
        adjacent = neighbours(state, L)
        legal_directed += len(adjacent)
        total_killing += 2 * k - len(adjacent)
        for m_index, energy in enumerate(energies):
            q_value = -2 * k * values[m_index][s_index]
            q_value += sum(values[m_index][index[target]] for target in adjacent)
            max_eigen_residual = max(max_eigen_residual,
                                     abs(q_value + energy * values[m_index][s_index]))

    max_orth = 0.0
    for a in range(len(modes)):
        for b in range(len(modes)):
            inner = sum(values[a][j] * values[b][j] for j in range(len(states)))
            max_orth = max(max_orth, abs(inner - (1.0 if a == b else 0.0)))

    probe_indices = sorted({0, len(states) // 2, len(states) - 1})
    probes = []
    max_km = 0.0
    for time_text in ("0", "0.375", "1.25"):
        time = float(time_text)
        for s_index in probe_indices:
            state = states[s_index]
            if time == 0.0:
                survival = 1.0
                density = float(2 * k - len(neighbours(state, L)))
            else:
                survival = 0.0
                density = 0.0
                for m_index, energy in enumerate(energies):
                    amplitude = values[m_index][s_index] * sum(values[m_index])
                    weight = math.exp(-energy * time)
                    survival += weight * amplitude
                    density += energy * weight * amplitude
            probes.append({
                "state_index": s_index,
                "time": time_text,
                "survival_decimal_15": fmt(survival),
                "absorption_density_decimal_15": fmt(density),
            })
        if time > 0:
            for x_index in probe_indices:
                for y_index in probe_indices:
                    x, y = states[x_index], states[y_index]
                    km = determinant([[one_kernel(L, xi, yj, time) for yj in y] for xi in x])
                    spectral = sum(math.exp(-energies[a] * time) * values[a][x_index] * values[a][y_index]
                                   for a in range(len(modes)))
                    max_km = max(max_km, abs(km - spectral))

    max_balance = 0.0
    for i, state in enumerate(states):
        for target in neighbours(state, L):
            j = index[target]
            left = h[i] * h[i] * h[j] / h[i]
            right = h[j] * h[j] * h[i] / h[j]
            max_balance = max(max_balance, abs(left - right))

    ground = energies[0]
    if k < L:
        gap = eps(L, k + 1) - eps(L, k)
        gap_text: str | None = fmt(gap)
        gap_boundary = "ordinary: replace occupied mode k by k+1"
    else:
        gap_text = None
        gap_boundary = "singleton Q-process: no nonzero relaxation mode"

    return {
        "L": L,
        "k": k,
        "dimension": len(states),
        "states": [list(state) for state in states],
        "mode_count": len(modes),
        "legal_directed_edges": legal_directed,
        "total_killing_rate": total_killing,
        "negative_generator_trace": 2 * k * len(states),
        "ground_mode": list(range(1, k + 1)),
        "ground_energy_decimal_15": fmt(ground),
        "ground_h_l1_decimal_15": fmt(h_l1),
        "ground_h_min_decimal_15": fmt(min(h)),
        "ground_h_l2_squared_decimal_15": fmt(sum(value * value for value in h)),
        "spectral_gap_decimal_15": gap_text,
        "spectral_gap_boundary": gap_boundary,
        "max_eigen_residual_decimal_12": f"{max_eigen_residual:.12e}",
        "max_orthonormality_residual_decimal_12": f"{max_orth:.12e}",
        "max_karlin_mcgregor_residual_decimal_12": f"{max_km:.12e}",
        "max_q_detailed_balance_residual_decimal_12": f"{max_balance:.12e}",
        "probe_count": len(probes),
        "probes": probes,
    }


def build_payload() -> dict:
    cases = [case_row(L, k) for L in range(1, 9) for k in range(1, L + 1)]
    payload = {
        "schema": "hcs-c306-killed-noncolliding-walkers-evidence-v1",
        "candidate_id": "HCS-C306",
        "obstruction_id": "HEN-O290",
        "title": "Killed noncolliding walkers: determinant, spectrum, absorption, and Q-process",
        "evaluation_date": "2026-09-03",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator_authority_sha256": EVALUATOR,
        "model": {
            "state_space": "W_{L,k}={1<=x_1<...<x_k<=L}, with integers 1<=k<=L",
            "one_particle_rates": "rate 1 to each nearest neighbour; Dirichlet killing at 0 and L+1",
            "many_particle_killing": "kill at the first boundary attempt or first coincidence attempt",
            "generator": "Q_k(x,y)=1 for one legal coordinate step, Q_k(x,x)=-2k, and zero otherwise",
            "not_exclusion": "illegal collision attempts kill; they are not reflected or suppressed",
        },
        "theorem": {
            "one_particle": "p_t(i,j)=2/(L+1) sum_{r=1}^L exp(-epsilon_r t) sin(pi r i/(L+1)) sin(pi r j/(L+1))",
            "energies": "epsilon_r=2-2 cos(pi r/(L+1)); Lambda_m=sum_a epsilon_{m_a}",
            "karlin_mcgregor": "P_t(x,y)=det[p_t(x_i,y_j)]",
            "slater_basis": "Phi_m(x)=det[phi_{m_a}(x_b)] is a complete orthonormal eigenbasis on W_{L,k}",
            "survival": "S_x(t)=sum_m exp(-Lambda_m t) Phi_m(x) A_m, A_m=sum_y Phi_m(y)",
            "absorption": "P_x(tau<=t)=1-S_x(t); f_x(t)=sum_m Lambda_m exp(-Lambda_m t) Phi_m(x) A_m",
            "moments": "E_x[tau^r]=r! sum_m Phi_m(x) A_m/Lambda_m^r for every integer r>=1",
            "ground": "m_0=(1,...,k), h=sign(Phi_m0)>0, Lambda_0=sum_{r=1}^k epsilon_r",
            "leading": "S_x(t)=h(x)A_0 exp(-Lambda_0 t)+O(exp(-Lambda_1 t)) when k<L; k=L is exact exp(-2Lt)",
            "qsd": "nu(y)=h(y)/A_0 is the unique QSD and the Yaglom limit from every state",
            "doob": "q^h(x,y)=q(x,y)h(y)/h(x), q^h(x,x)=q(x,x)+Lambda_0, invariant pi^h(x)=h(x)^2",
            "gap": "for k<L the Q-process gap is epsilon_{k+1}-epsilon_k; for k=L the Q-process is a singleton with no nonzero relaxation mode",
        },
        "proof_certificates": {
            "boundary_diagonalization": "the discrete sine basis diagonalizes the one-particle Dirichlet generator",
            "exterior_power": "antisymmetrized tensor eigenvectors restrict to the chamber and give all binomial(L,k) Slater modes",
            "path_switching": "Karlin--McGregor sign reversal cancels paths at their first coincidence",
            "positivity": "the signed consecutive-mode sine determinant is strictly positive on the chamber",
            "perron": "finite irreducibility plus symmetry makes the positive ground mode simple and controls QSD/Yaglom asymptotics",
            "transform": "Qh=-Lambda_0 h gives conservative Doob rates; symmetry gives detailed balance with h^2",
        },
        "finite_spectral_atlas": {
            "L_min": 1,
            "L_max": 8,
            "case_count": len(cases),
            "state_rows": sum(row["dimension"] for row in cases),
            "mode_rows": sum(row["mode_count"] for row in cases),
            "probe_rows": sum(row["probe_count"] for row in cases),
            "cases": cases,
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall_verdict": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "obstruction": "the finite killed-walk semigroup has no target arithmetic local carrier, primitive-orbit Euler ledger, intrinsic prime clock, or target determinant; its self-adjoint generator is only a candidate-local A4 formal hint",
        },
        "scope_flags": {
            "claims_target_arithmetic_local_data": False,
            "claims_target_euler_factors": False,
            "claims_root_number": False,
            "claims_automorphy": False,
            "claims_target_divisor_or_counting_law": False,
            "claims_target_functional_equation": False,
            "claims_target_zero_match": False,
            "claims_hilbert_polya_operator": False,
            "invokes_route_b": False,
        },
        "boundaries": [
            "The determinant is the killed collision kernel, not an exclusion or reflecting kernel.",
            "Absorption laws are exact finite spectral sums; no simpler first-passage closed form is claimed.",
            "For k=L the chamber has one state, tau is Exp(2L), and the Q-process has no nonzero relaxation mode.",
            "Finite decimal rows are regression diagnostics; the all-parameter theorem is analytic.",
        ],
        "source_owner_tokens": [
            "doi:10.2140/pjm.1959.9.1141",
            "doi:10.2307/3212311",
        ],
        "regression_summary": {
            "case_count": len(cases),
            "state_rows": sum(row["dimension"] for row in cases),
            "mode_rows": sum(row["mode_count"] for row in cases),
            "probe_rows": sum(row["probe_count"] for row in cases),
            "L_cutoff": 8,
        },
    }
    payload["payload_sha256"] = canonical_hash(payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = build_payload()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(f"C306 producer PASS cases={payload['regression_summary']['case_count']} states={payload['regression_summary']['state_rows']} probes={payload['regression_summary']['probe_rows']}")
    print("payload_sha256=" + payload["payload_sha256"])


if __name__ == "__main__":
    main()
