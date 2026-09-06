"""Bounded local probe for g(u)=u+a*u^p+u^(2p); stdout only.

This is a new first-gate check, not an all-parameter proof or a periodic-point
census.  It uses exact arithmetic in F_p[u]/(u^precision), retaining the first
terms of g^(p^e)-u for the explicitly listed small cases.  A missing term at the
precision limit is reported as a lower bound, never as equality or identity.
"""

import json

from flint import nmod_mpoly_ctx, nmod_poly


def frobenius(poly, p, precision):
    coefficients = [0] * min(precision, p * max(0, poly.degree()) + 1)
    for i, coefficient in enumerate(poly):
        if i * p >= precision:
            break
        coefficients[i * p] = int(coefficient)
    return nmod_poly(coefficients, p)


def probe(p, a, highest_e, precision):
    u = nmod_poly([0, 1], p)
    current = u
    wanted = {p**e: e for e in range(highest_e + 1)}
    rows = []
    for n in range(1, p**highest_e + 1):
        fpower = frobenius(current, p, precision)
        current = (current + a * fpower + fpower * fpower).truncate(precision)
        if n in wanted:
            delta = current - u
            terms = [(i, int(c)) for i, c in enumerate(delta) if int(c)]
            rows.append(
                {
                    "p": p,
                    "a": a,
                    "iterate": n,
                    "precision": precision,
                    "first_order": terms[0][0] if terms else None,
                    "first_terms": terms[:8],
                    "missing_means_order_at_least": precision if not terms else None,
                }
            )
    return rows


def generic_first_probe(p, precision):
    context = nmod_mpoly_ctx.get(("u", "a"), p)
    u, a = context.gens()
    current = u
    for _ in range(p):
        fpower = context.from_dict(
            {
                (i * p, j * p): int(coefficient)
                for (i, j), coefficient in current.to_dict().items()
                if i * p < precision
            }
        )
        current = current + a * fpower + fpower * fpower
        terms = {
            monomial: int(coefficient)
            for monomial, coefficient in current.to_dict().items()
            if monomial[0] < precision
        }
        if len(terms) > 100000:
            return {"p": p, "precision": precision, "status": "STOP_TERM_CAP"}
        current = context.from_dict(terms)
    terms = (current - u).to_dict()
    exponents = sorted({int(monomial[0]) for monomial in terms})
    first = []
    for order in exponents[:5]:
        coefficient = nmod_poly(
            [int(terms.get((order, j), 0)) for j in range(max(k[1] for k in terms if k[0] == order) + 1)],
            p,
        )
        first.append({"u_order": order, "coefficient_in_a": str(coefficient).replace("x", "a")})
    return {
        "p": p,
        "parameter": "a_indeterminate",
        "iterate": p,
        "precision": precision,
        "first_order": exponents[0] if exponents else None,
        "first_terms": first,
        "missing_means_order_at_least": precision if not terms else None,
    }


if __name__ == "__main__":
    cases = [(3, 1, 3, 8000), (3, 2, 2, 2000), (5, 1, 2, 8000), (7, 1, 1, 3000)]
    rows = []
    for case in cases:
        rows.extend(probe(*case))
    generic_rows = [generic_first_probe(p, precision) for p, precision in [(3, 512), (5, 1024), (7, 2048)]]
    print(json.dumps({"scope": "explicit local finite-characteristic jets only", "rows": rows, "generic_first_rows": generic_rows}, indent=2))
