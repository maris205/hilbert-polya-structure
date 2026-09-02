#!/usr/bin/env python3
"""Symbolic cross-check for HCS-C287."""
from __future__ import annotations
import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"results/c287_wave_evidence.json"


def main():
    d=json.loads(DATA.read_text())
    L,c,n=s.symbols("L c n",positive=True)
    T=2*L/c
    omega=s.pi*n*c/L
    energy_a=c**2*s.pi**2*n**2/(4*L)
    energy_b=L/4
    obs_a=(n*s.pi/L)**2*T/2
    obs_b=(1/c)**2*T/2
    checks=[s.simplify(obs_a-4*energy_a/c**3)==0,s.simplify(obs_b-4*energy_b/c**3)==0,s.simplify(omega*T-2*s.pi*n)==0,s.simplify(omega*(L/c)-s.pi*n)==0]
    x,t=s.symbols("x t",real=True)
    F=s.Function("F")
    u=F(x+c*t)-F(-x+c*t)
    checks += [s.simplify(s.diff(u,t,2)-c**2*s.diff(u,x,2))==0,s.simplify(u.subs(x,0))==0]
    for row in d["parameter_rows"]:
        LL=s.Rational(row["L"]); cc=s.Rational(row["c"])
        checks.append(s.Rational(row["critical_time"])==2*LL/cc)
        checks.append(s.Rational(row["observation_energy_ratio"])==4/cc**3)
    for row in d["revival_cells"]:
        nn=row["n"]
        checks.append(s.cos(2*s.pi*nn)==1)
        checks.append(s.sin(2*s.pi*nn)==0)
        checks.append(s.cos(s.pi*nn)==(-1)**nn)
    assert all(checks)
    print(f"C287_SYMPY_PASS ({len(checks)} symbolic checks)")


if __name__=="__main__": main()
