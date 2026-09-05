#!/usr/bin/env python3
"""A new small literal order/stack-statistic intake, not a continuation of GM."""
from itertools import product
import json
from pilot import profile


def nearest(w, sign):
    ans = []
    for i, value in enumerate(w):
        positions = [j for j in range(i) if sign*(w[j]-value) > 0]
        ans.append(i-max(positions) if positions else 0)
    return tuple(ans)


def visible_depth(w):
    stack, ans = [], []
    for value in w:
        while stack and stack[-1] <= value:
            stack.pop()
        ans.append(len(stack))
        stack.append(value)
    return tuple(ans)


def alternating_ending(w):
    up, down, ans = [], [], []
    for i, value in enumerate(w):
        up.append(1+max([down[j] for j in range(i) if w[j]<value], default=0))
        down.append(1+max([up[j] for j in range(i) if w[j]>value], default=0))
        ans.append(max(up[-1], down[-1])-1)
    return tuple(ans)


def main():
    for name, step in [('NS', lambda w: nearest(w, -1)),
                       ('NG', lambda w: nearest(w, 1)),
                       ('VD', visible_depth), ('AE', alternating_ending)]:
        for n in range(1, 9):
            states = product(*(range(i+1) for i in range(n)))
            print(json.dumps(dict(candidate=name, n=n, **profile(states, step)),
                             sort_keys=True))


if __name__ == '__main__':
    main()
