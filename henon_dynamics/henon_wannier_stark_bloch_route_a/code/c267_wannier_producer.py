#!/usr/bin/env python3
"""Deterministic evidence producer for HCS-C267."""
from __future__ import annotations
import hashlib, json
from fractions import Fraction
from pathlib import Path
import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results/c267_wannier_evidence.json"
SOURCE = "a24c701881d22a4e49eaa2a44b94395c3c540b3d"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH = 1788048000
mp.mp.dps = 90

def ds(x):
    if abs(x) < mp.mpf("1e-84"): x = mp.mpf("0")
    return mp.nstr(x, 76, strip_zeros=False)

def cs(z): return {"re": ds(mp.re(z)), "im": ds(mp.im(z))}

def kernel(F, J, r, n, m):
    theta = mp.sign(F) * 2 * mp.pi * mp.mpf(r.numerator) / r.denominator
    z = mp.mpf(0) if r in (Fraction(0), Fraction(1)) else 4 * mp.mpf(J) / F * mp.sin(theta / 2)
    return (1j ** (n-m)) * mp.exp(-1j * theta * (n+m)/2) * mp.besselj(n-m, z), z

def payload_hash(d):
    q = dict(d); q.pop("payload_sha256", None)
    raw = json.dumps(q, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()

def main():
    Fvals=(-5,-2,-1,1,3,7); Jvals=(-4,-1,0,2,5)
    rvals=tuple(Fraction(*x) for x in ((0,1),(1,10),(1,4),(1,3),(1,2),(3,4),(1,1)))
    pairs=((0,0),(1,0),(-1,0),(3,-2),(-4,2))
    propagation=[]
    for F in Fvals:
      for J in Jvals:
       for r in rvals:
        entries=[]
        for n,m in pairs:
            v,z=kernel(F,J,r,n,m); entries.append({"n":n,"m":m,"value":cs(v)})
        _,z=kernel(F,J,r,0,0)
        shell=[{"n":n,"probability":ds(mp.besselj(n,z)**2)} for n in range(-12,13)]
        propagation.append({"F":F,"J":J,"period_fraction":f"{r.numerator}/{r.denominator}",
            "theta_over_pi":f"{2*mp.sign(F)*r.numerator}/{r.denominator}","z":ds(z),
            "kernel_entries":entries,"delta_shell":shell,"second_moment":ds(z*z/2)})
    eigen=[]
    for F in Fvals:
      for J in Jvals:
       for m in (-2,0,3):
        a=mp.mpf(2)*J/F
        eigen.append({"F":F,"J":J,"m":m,"energy":F*m,"a":ds(a),
          "components":[{"n":n,"value":ds(mp.besselj(n-m,a))} for n in range(-10,11)]})
    data={
      "schema":"hcs-c267-wannier-stark-v1","candidate_id":"HCS-C267","evaluation_date":"2026-08-31",
      "source_commit":SOURCE,"fixed_epoch":EPOCH,"scope_literal":"NO_BAD_EULER_OR_ROOT_NUMBER",
      "evaluator":{"version":"0.2.0","sha256":EVAL},
      "operator":"(H psi)_n = F*n*psi_n - J*(psi_{n+1}+psi_{n-1}) on ell^2(Z), F != 0",
      "fourier_contract":{"transform":"sum_n psi_n exp(i n k)","operator":"-i F d/dk - 2 J cos(k)",
        "gauge":"G=exp(-i(2J/F)sin(k)); Hhat=G^{-1}(-iF d/dk)G",
        "eigenvector":"phi_m(n)=J_{n-m}(2J/F)","eigenvalue":"F*m"},
      "propagator_contract":{"kernel":"i^(n-m) exp(-i F t(n+m)/2) J_{n-m}((4J/F)sin(Ft/2))",
        "least_identity_return":"2*pi/abs(F)","delta_probability":"J_n(z(t))^2",
        "delta_second_moment":"z(t)^2/2 = 8J^2/F^2 sin^2(Ft/2)"},
      "spectral_contract":{"spectrum":"simple pure point F*Z","U_compact":False,
        "U_Sp_for_finite_p":False,"resolvent_Sp":"iff p>1 for z outside F*Z","resolvent_trace_class":False},
      "boundary_contract":{"J=0":"diagonal ladder; same least return; frozen delta shell",
        "F->0":"changed owner: free lattice, ac band [-2|J|,2|J|], no full return for J!=0"},
      "regression":{"propagation_rows":propagation,"eigen_rows":eigen,
        "counts":{"parameter_time_rows":len(propagation),"kernel_cells":len(propagation)*len(pairs),
          "shell_cells":len(propagation)*25,"eigen_rows":len(eigen),"eigen_cells":len(eigen)*21}},
      "analytic_proof_obligations":["unitary Fourier-gauge conjugacy","Bessel recurrence eigen-equation and gauge completeness",
        "characteristic/spectral propagator identity","spectral minimal-return argument","Bessel shell generating identity",
        "unitary image of an orthonormal sequence is not precompact","resolvent singular-value p-series criterion"],
      "route_a":{"tuple":["A0_FAIL","A1_WEAK","A2_FAIL","A3_FAIL","A4_NATURAL_QUANTIZATION"],
        "overall":"ROUTE_A_REJECTED","route_b_invocation_allowed":False},
      "scope_flags":{"arithmetic_local_data":False,"euler_factors":False,"root_numbers":False,
        "automorphy":False,"target_divisor":False,"functional_equation":False,"hilbert_polya_operator":False},
      "nonclaims":["No novelty priority is claimed.","Finite regressions do not prove infinite-dimensional statements.",
        "The lattice Hamiltonian is not identified with a target Hilbert--Polya operator."],
      "sources":[{"author":"G. H. Wannier","doi":"10.1103/PhysRev.117.432","role":"model lineage"},
        {"author":"J. Yellin","doi":"10.1103/PhysRevE.52.2208","role":"exact uniform-field lattice propagator lineage"}],
    }
    data["payload_sha256"]=payload_hash(data)
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(data,sort_keys=True,indent=2,ensure_ascii=False)+"\n")
    print(f"C267_PRODUCER_PASS rows={len(propagation)} kernel={len(propagation)*5} shell={len(propagation)*25} eigen={len(eigen)*21} payload={data['payload_sha256']}")
if __name__ == "__main__": main()
