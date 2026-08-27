#!/usr/bin/env python3
"""Independent symbolic positive-weight checks for C203."""
import argparse,json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[1]; DEFAULT=ROOT/"results/c203_signed_laplacian_evidence.json"
def main():
    p=argparse.ArgumentParser(); p.add_argument("--evidence",type=Path,default=DEFAULT); d=json.loads(p.parse_args().evidence.read_text()); checks=0
    def check(x,msg):
        nonlocal checks; checks+=1
        value=s.simplify(x)
        failed=(not value.is_zero_matrix) if isinstance(value,s.MatrixBase) else (value!=0)
        if failed: raise AssertionError(msg+": "+str(value))
    x,y,z,lam=s.symbols("x y z lambda",positive=True)
    # Positive path: balanced rank two, weighted tree characteristic formula.
    B=s.Matrix([[1,0],[-1,1],[0,-1]]); W=s.diag(x,y); L=B*W*B.T
    check(L*s.ones(3,1),"path kernel"); check(L.det(),"path determinant")
    check((lam*s.eye(3)+L).det()-(lam**3+2*(x+y)*lam**2+3*x*y*lam),"path charpoly")
    check(L.extract([1,2],[1,2]).det()-x*y,"path rooted minor")
    # One-negative triangle: determinant 4xyz and full weighted expansion.
    Bn=s.Matrix([[1,0,1],[-1,1,0],[0,-1,1]]); Ln=Bn*s.diag(x,y,z)*Bn.T
    check(Ln.det()-4*x*y*z,"negative triangle determinant")
    expected=lam**3+2*(x+y+z)*lam**2+3*(x*y+x*z+y*z)*lam+4*x*y*z
    check((lam*s.eye(3)+Ln).det()-expected,"negative triangle charpoly")
    check(Ln.extract([1,2],[1,2]).det()-(x*y+x*z+y*z),"negative triangle cofactor")
    # Positive triangle is balanced: determinant zero and tree coefficient only.
    Bp=s.Matrix([[1,0,1],[-1,1,0],[0,-1,-1]]); Lp=Bp*s.diag(x,y,z)*Bp.T
    check(Lp.det(),"positive triangle determinant"); check(Lp*s.ones(3,1),"positive triangle kernel")
    check((lam*s.eye(3)+Lp).det()-(lam**3+2*(x+y+z)*lam**2+3*(x*y+x*z+y*z)*lam),"positive triangle charpoly")
    # Exhaustive ledger coefficient equality is separately reconstructed with exact integers.
    for row in d["exhaustive_regression"]["graphs"]:
        check(s.Integer(row["determinant"])-s.Integer(row["characteristic_coefficients_matrix"][0]),"constant coefficient")
        check(sum(row["components"][k]["balanced"] for k in range(len(row["components"])))-row["nullity"],"nullity ledger")
    print(json.dumps({"status":"C203_SYMPY_PASS","checks":checks,"symbolic_weighted_identities":10,"ledger_identities":2*len(d["exhaustive_regression"]["graphs"])},sort_keys=True))
if __name__=="__main__": main()
