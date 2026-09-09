"""Exact exploratory search after R6-IH freeze; no floating point.

For each coordinate alphabet E with min(E)=0, max(E)<=--diameter,
enumerate all restrictions of Z[t] to E whose values are in E+a*E.
Newton interpolation coefficients are integral iff the restriction is
realized by an integral-coefficient polynomial (division by monic factors).
Only cycles using exactly E are reported. This is NOT an all-diameter proof.
"""
import argparse
import itertools
import json
import time


def add_root(poly, root):
    ans = [0] * (len(poly) + 1)
    for j, c in enumerate(poly):
        ans[j] -= root * c
        ans[j + 1] += c
    return ans


def evaluate(poly, x):
    ans = 0
    for c in reversed(poly):
        ans = ans * x + c
    return ans


def restrictions(alphabet, sign):
    outputs = sorted({x + sign * y for x in alphabet for y in alphabet})
    def visit(k, poly, basis, values):
        if k == len(alphabet):
            yield values, poly, basis
            return
        x = alphabet[k]
        old, step = evaluate(poly, x), evaluate(basis, x)
        for out in outputs:
            if (out - old) % step:
                continue
            coeff = (out - old) // step
            new = poly + [0] * (len(basis) - len(poly))
            new = [u + coeff * v for u, v in zip(new, basis)]
            yield from visit(k + 1, new, add_root(basis, x), values + [out])
    yield from visit(0, [], [1], [])


def exact_cycles(alphabet, values, sign):
    aset = set(alphabet)
    val = dict(zip(alphabet, values))
    done = set()
    for initial in itertools.product(alphabet, repeat=2):
        if initial in done:
            continue
        path, index = [], {}
        state = initial
        while state not in done and state not in index:
            index[state] = len(path)
            path.append(state)
            nxt = val[state[1]] - sign * state[0]
            if nxt not in aset:
                break
            state = state[1], nxt
        else:
            if state in index:
                cycle = path[index[state]:]
                if {x for pair in cycle for x in pair} == aset:
                    yield cycle
        done.update(path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--diameter', type=int, default=10)
    args = parser.parse_args()
    start = time.monotonic()
    answers = {1: {}, -1: {}}
    tested = 0
    for diameter in range(args.diameter + 1):
        if diameter == 0:
            alphabets = [(0,)]
        else:
            alphabets = ((0,) + tuple(i for i in range(1, diameter)
                           if mask & (1 << (i - 1))) + (diameter,)
                         for mask in range(1 << (diameter - 1)))
        for alphabet in alphabets:
            for sign in (1, -1):
                for values, poly, basis in restrictions(alphabet, sign):
                    tested += 1
                    for cycle in exact_cycles(alphabet, values, sign):
                        period = len(cycle)
                        if period in answers[sign]:
                            continue
                        while len(poly) > 1 and poly[-1] == 0:
                            poly.pop()
                        # Adding a monic polynomial vanishing on E preserves
                        # the cycle and ensures degree >=2 in affine cases.
                        witness = list(poly)
                        if len(witness) < 3:
                            bump = basis if len(basis) >= 3 else add_root(basis, 0)
                            witness += [0] * (len(bump) - len(witness))
                            witness = [u + v for u, v in zip(witness, bump)]
                        for x, y in cycle:
                            assert (y, evaluate(witness, y) - sign * x) in cycle
                        assert len(set(cycle)) == period
                        answers[sign][period] = {
                            'diameter': diameter, 'alphabet': alphabet,
                            'polynomial_ascending': witness, 'cycle': cycle}
        print(json.dumps({'diameter_finished': diameter,
                          'restrictions_tested': tested,
                          'periods': {str(s): sorted(v) for s, v in answers.items()},
                          'elapsed_seconds': round(time.monotonic() - start, 3)}),
              flush=True)
    print(json.dumps({'scope': vars(args), 'witnesses': answers}, indent=2))


if __name__ == '__main__':
    main()
