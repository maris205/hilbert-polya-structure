# Coordinator check: two resonant counterexamples

Date: 2026-09-06. Scope: two finite algebraic cases in the arithmetic scout,
not an all-period theorem and not an external or human review.

The coordinator did not import `bounded_probe.py` or its JSON. Each iterate
was written directly from the displayed map. Both independent calls used
SymPy's **F5B** Gröbner implementation, with reversed variable priority
`(y,x)` and grevlex order. The scout uses SymPy's default Buchberger method
and priority `(x,y)`. This is an independent construction/algorithm check
inside the same computer algebra system, not a different CAS or a formal
proof-assistant certificate.

| Map and equation | Leading monomials | Quotient dimension | Actual call |
|---|---|---:|---|
| `H=(y,y^3+y^2-x)` in characteristic 3, `H^3=(x^27,y^27)` | `x^27, y^14` | 378 | exit 0, 0.406 s |
| `H=(y,y^4+y^3-x)` in characteristic 2, `H^2=(x^16,y^16)` | `x^16, y^11` | 176 | exit 0, 0.423 s |

The environment reported Python 3.12.3 and SymPy 1.14.0. Each basis was
zero-dimensional. The original map has Jacobian determinant 1, whereas
the Frobenius derivative vanishes. Thus its fixed-equation Jacobian is
invertible, justifying the scout's identification of affine length with
geometric point count. The resulting counts differ from the respective
constant-density guesses 486 and 192. This refutes those guesses only.

## Exact executed commands

Working directory: `/root/autodl-tmp/hilbert-polya-structure`.

```sh
python -c 'import sympy as s; x,y=s.symbols("x y"); p=3; q=3; m=2; n=3; a=y**q+y**m-x; b=a**q+a**m-y; c=b**q+b**m-a; eq=[s.Poly(b-x**(q**n),y,x,modulus=p).as_expr(),s.Poly(c-y**(q**n),y,x,modulus=p).as_expr()]; G=s.groebner(eq,y,x,modulus=p,order="grevlex",method="f5b"); lm=[g.LM(order=G.order).exponents for g in G.polys]; by=min(i for i,j in lm if j==0); bx=min(j for i,j in lm if i==0); dim=sum(not any(i>=a and j>=b for a,b in lm) for i in range(by) for j in range(bx)); print({"method":"f5b","variables":"y,x","leading":lm,"length":dim,"zero_dimensional":G.is_zero_dimensional}); assert dim==378'

python -c 'import platform; import sympy as s; x,y=s.symbols("x y"); a=y**4+y**3-x; eq=[s.Poly(a-x**16,y,x,modulus=2).as_expr(),s.Poly(a**4+a**3-y-y**16,y,x,modulus=2).as_expr()]; G=s.groebner(eq,y,x,modulus=2,order="grevlex",method="f5b"); lm=[g.LM(order=G.order).exponents for g in G.polys]; by=min(i for i,j in lm if j==0); bx=min(j for i,j in lm if i==0); dim=sum(not any(i>=a and j>=b for a,b in lm) for i in range(by) for j in range(bx)); print({"python":platform.python_version(),"sympy":s.__version__,"method":"f5b","variables":"y,x","leading":lm,"length":dim,"zero_dimensional":G.is_zero_dimensional}); assert dim==176'
```

## Bounded adjudication

The [arithmetic scout](henon_arithmetic/SCOUT_REPORT.md) correctly separates
three outcomes: existing finite Galois/Artin ownership, an explicit additive
group reduction, and a nonadditive resonant problem whose all-period
intersection analysis remains missing. The displayed additive reduction
`S=H^-1 Phi_q` and its zero derivative are consistent with the stated
fixed-point equation. No result here proves that the nonadditive family
cannot yield a stronger theorem. No new paper number or Route-A grade follows
from this check.

## Additional source-formula sanity check

After the [nonaffine cross-audit](henon_arithmetic/CROSS_AUDIT_NONAFFINE.md)
flagged an odd-cycle sign issue, the coordinator separately read the accessed
[preprint's Definition 3.1, Lemma 4.11 and Theorems 4.12/6.9](https://arxiv.org/html/2509.15214v1)
and executed the following elementary check (exit 0; approximately 0.326 s):

```sh
python -c 'import sympy as s; u=s.symbols("u"); P=s.Matrix([[0,0,1],[1,0,0],[0,1,0]]); print(s.factor((s.eye(3)+u*P).det())); assert s.expand((s.eye(3)+u*P).det()-(1+u**3))==0'
```

The result is `1+u^3`, not `1-u^3`. This confirms the narrow algebraic caveat;
it does not independently certify the paper's entire argument or determine
which arithmetic isogeny specializations are affected. The original scout's
blanket source-formula coverage was qualified accordingly. The definitions
and framework remain prior work, and this sign correction is not assigned
a new paper contract. No external author notification or source edit was made.
