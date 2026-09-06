"""Bounded exact counterexample search, not all-period evidence.

Test f=x+x^(p+1) on small finite fields, using the derived first-return
coefficient S=sum a_j/(1+a_j). Do not expand f^n globally.
Outputs to stdout only; old probe/evidence files are neither read nor run.
"""
import json
from flint import fq_default_ctx


def scan(p, degree):
    ctx = fq_default_ctx(p, degree, "a")
    one = ctx(1)
    size = p**degree
    elements = []
    for code in range(size):
        digits = []
        for _ in range(degree):
            digits.append(code % p)
            code //= p
        elements.append(ctx(digits))
    lookup = {str(x): i for i, x in enumerate(elements)}
    successor = [lookup[str(x + x**(p+1))] for x in elements]
    seen = set()
    cycles = []
    hits = []
    for start in range(size):
        if start in seen:
            continue
        path = []
        where = {}
        current = start
        while current not in seen and current not in where:
            where[current] = len(path)
            path.append(current)
            current = successor[current]
        if current in where:
            cycle = path[where[current]:]
            if cycle != [0]:
                orbit = [elements[i] for i in cycle]
                assert len(set(cycle)) == len(cycle)
                assert all(x != 0 and x != -one for x in orbit)
                total = sum((x/(one+x) for x in orbit), ctx(0))
                cycles.append({"period": len(cycle), "sum": str(total)})
                if total == 0:
                    hits.append({"period": len(cycle), "orbit": [str(x) for x in orbit], "codes": cycle})
        seen.update(path)
    return {"p": p, "degree": degree, "modulus": str(ctx.modulus()), "field_size": size,
            "cycles": cycles, "hits": hits}


if __name__ == "__main__":
    for p, degree in [(3,m) for m in range(2,9)] + [(5,m) for m in range(2,6)] + [(7,m) for m in range(2,5)]:
        result = scan(p, degree)
        print(json.dumps(result, ensure_ascii=False), flush=True)
        if result["hits"]:
            break
