#!/usr/bin/env python3
"""Two further bounded literal probes; same-lane graph census helper imported."""
from pilot_initial import analyze
import json


def autocorrelation_zero(n, mask):
    differences = 0
    for a in range(n):
        if (mask >> a) & 1:
            for b in range(n):
                if (mask >> b) & 1:
                    differences |= 1 << ((a-b)%n)
    return ((1 << n)-1) ^ differences


def missing_language_tools(n):
    edges = 1 << n
    vertices = 1 << (n-1)
    short_mask = vertices-1
    endpoints = []
    reverse = []
    for word in range(edges):
        endpoints.append((1 << (word >> 1)) | (1 << (word & short_mask)))
        rev = 0
        for i in range(n):
            rev |= ((word >> i) & 1) << (n-1-i)
        reverse.append(rev)
    closure = []
    for support in range(1 << vertices):
        closure.append(sum(1 << word for word, ep in enumerate(endpoints)
            if (ep & support) == ep))
    def update(language):
        support = 0
        for word, ep in enumerate(endpoints):
            if (language >> word) & 1:
                support |= ep
        absent = closure[support] & ~language
        return sum(1 << reverse[word] for word in range(edges)
            if (absent >> word) & 1)
    return update


if __name__ == "__main__":
    for n in range(1,13):
        row = analyze(list(range(1 << n)), lambda mask:autocorrelation_zero(n,mask))
        print(json.dumps({"candidate":"AZ","n":n,**row},sort_keys=True,separators=(",",":")),flush=True)
    for n in range(1,5):
        row = analyze(list(range(1 << (1 << n))), missing_language_tools(n))
        print(json.dumps({"candidate":"MA","n":n,**row},sort_keys=True,separators=(",",":")),flush=True)
