#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C152."""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from math import gcd, isqrt
from pathlib import Path


def canon_hash(data):
    work = dict(data); work.pop("payload_sha256", None)
    return sha256(json.dumps(work, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def vector_hash(values):
    return sha256((",".join(map(str, values)) + "\n").encode()).hexdigest()


def sieve_mobius(limit):
    mu = [1] * (limit + 1)
    prime = [True] * (limit + 1)
    for p in range(2, limit + 1):
        if prime[p]:
            for multiple in range(p, limit + 1, p):
                prime[multiple] = False if multiple != p else prime[multiple]
                mu[multiple] *= -1
            square = p * p
            for multiple in range(square, limit + 1, square):
                mu[multiple] = 0
    return mu


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence", nargs="?", type=Path, default=Path(__file__).resolve().parents[1] / "results/c152_heat_evidence.json")
    args = parser.parse_args()
    data = json.loads(args.evidence.read_text())
    checks = 0

    def check(condition, message):
        nonlocal checks
        checks += 1
        if not condition: raise AssertionError(message)

    expected = {"schema","candidate_id","evaluation_date","scope_literal","source_commit","source_lock","heat_transform_theorem","counting_theorem","coefficient_certificate","coefficient_ledger","count_ledger","natural_quantization_boundary","route_a","claim_boundary","payload_sha256"}
    check(set(data) == expected, "top closure")
    check(data["schema"] == "hcs-c152-billiard-primitive-heat-evidence-v1", "schema")
    check(data["candidate_id"] == "HCS-C152", "candidate")
    check(data["evaluation_date"] == "2026-08-25", "date")
    check(data["source_commit"] == "2d4e6211a254ef49d87718569d23466f4c6dcf4c", "commit")
    check(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    check(data["payload_sha256"] == canon_hash(data), "hash")
    lock = data["source_lock"]
    check(lock["direction_convention"] == "m,n>=1 ordered; coordinate swap retained; axes excluded; equal lengths retain multiplicity", "convention")
    check(lock["length"] == "L_(m,n)=2*sqrt(m^2+n^2)", "length")
    check(lock["cutoff"] == {"coefficient_s_max": 20000, "count_radii": [10,20,40,80,120,160,200]}, "cutoff")
    check(lock["precision"] == "exact integer coefficients and counts; analytic asymptotic proved separately", "precision")
    smax = 20000
    limit = isqrt(smax)
    primitive = [0] * (smax + 1)
    unrestricted = [0] * (smax + 1)
    for m in range(1, limit + 1):
        maximum_n = isqrt(smax - m*m)
        for n in range(1, maximum_n + 1):
            square = m*m+n*n
            unrestricted[square] += 1
            if gcd(m,n)==1: primitive[square] += 1
    mu = sieve_mobius(max(limit, 200))
    factor = [0] * (smax + 1)
    for d in range(1,limit+1):
        for u in range(2,smax//(d*d)+1):
            factor[d*d*u] += mu[d]*unrestricted[u]
    for s in range(smax+1): check(factor[s] == primitive[s], f"coefficient identity {s}")
    ledger = [{"s=m2+n2":s,"ordered_positive_primitive_multiplicity":primitive[s]} for s in range(2,smax+1) if primitive[s]]
    check(data["coefficient_ledger"] == ledger, "coefficient ledger")
    cert = data["coefficient_certificate"]
    check(cert["s_max"] == smax, "smax")
    check(cert["dense_primitive_vector_sha256"] == vector_hash(primitive), "primitive vector hash")
    check(cert["dense_mobius_factorized_vector_sha256"] == vector_hash(factor), "factor vector hash")
    check(cert["coefficient_identity_all_s_through_cutoff"] is True, "identity flag")
    check(cert["nonzero_coefficient_count"] == len(ledger), "nonzero count")
    collisions = [row for row in ledger if row["ordered_positive_primitive_multiplicity"] >= 4]
    check(cert["collision_coefficient_count"] == len(collisions), "collision count")
    check(cert["first_multiplicity_four_square"] == 65, "first collision")
    frozen_counts = data["count_ledger"]
    for row in frozen_counts:
        radius=row["R"]
        direct=sum(1 for m in range(1,radius+1) for n in range(1,isqrt(radius*radius-m*m)+1) if gcd(m,n)==1)
        inversion=0
        for d in range(1,radius+1):
            inner=sum(1 for a in range(1,radius//d+1) for b in range(1,radius//d+1) if d*d*(a*a+b*b)<=radius*radius)
            inversion += mu[d]*inner
        check(row == {"R":radius,"N_primitive":direct,"mobius_inversion_value":inversion,"leading_ratio_N_over_R2":f"{direct}/{radius*radius}"}, f"count row {radius}")
        check(direct == inversion, f"Mobius count {radius}")
    heat=data["heat_transform_theorem"]
    check(heat["mobius_factorization"] == "H_prim(t)=sum_(d>=1) mu(d)*theta_+(4*t*d^2)^2", "factor theorem")
    check("sum d^(-2)" in heat["absolute_interchange_bound"], "absolute bound")
    check(heat["collision_convention"].startswith("each ordered positive"), "collision convention")
    check(heat["not_a_wave_trace"] is True and heat["not_a_dirichlet_spectral_trace"] is True and heat["not_an_isolated_orbit_determinant"] is True, "nonidentities")
    count=data["counting_theorem"]
    check(count["Q_definition"].endswith("axes excluded"), "quarter disk convention")
    check(count["quarter_disk_estimate"] == "Q(R)=pi*R^2/4+O(R+1)", "Q estimate")
    check(count["primitive_count_asymptotic"] == "N_prim(R)=3*R^2/(2*pi)+O(R*log R)", "N asymptotic")
    check(count["heat_asymptotic"] == "H_prim(t)=3/(8*pi*t)+O(t^(-1/2)*log(1/t)) as t decreases to zero", "heat asymptotic")
    check(count["proof_status"] == "PROVED_FROM_QUARTER_DISK_BOUND_MOBIUS_INVERSION_AND_STIELTJES_INTEGRATION", "proof status")
    quant=data["natural_quantization_boundary"]
    check(quant["self_adjoint"] is True and quant["same_unit_square_classical_geometry"] is True, "natural quantization")
    check(quant["heat_transform_equals_operator_trace"] is False and quant["clean_family_trace_bridge_constructed"] is False, "no trace identity")
    check(data["route_a"] == {"tuple":["A1_WEAK","A2_FAIL","A3_FAIL","A4_NATURAL_QUANTIZATION"],"overall":"ROUTE_A_EXPLORATORY","route_b_invocation_allowed":False}, "route")
    check(all(value is False for value in data["claim_boundary"].values()), "claim boundary")
    print(json.dumps({"status":"C152_CHECKER_PASS","assertions":checks},sort_keys=True))

if __name__ == "__main__": main()
