#!/usr/bin/env python3
"""Exact spike for degree-parity cut switching on labelled simple graphs."""

from collections import Counter


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def edge_table(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def odd_mask(graph, n, edges):
    parity = 0
    for bit, (i, j) in enumerate(edges):
        if (graph >> bit) & 1:
            parity ^= 1 << i
            parity ^= 1 << j
    return parity


def cut_mask(vertices, n, edges):
    out = 0
    for bit, (i, j) in enumerate(edges):
        if ((vertices >> i) ^ (vertices >> j)) & 1:
            out |= 1 << bit
    return out


def update(graph, n, edges):
    odd = odd_mask(graph, n, edges)
    return graph ^ cut_mask(odd, n, edges)


def lane(n):
    edges = edge_table(n)
    edge_count = len(edges)
    phase = 1 << edge_count
    fixed = 0
    even_time_fixed = 0
    images = Counter()
    parity_fibres = Counter()

    for graph in range(phase):
        odd = odd_mask(graph, n, edges)
        check(odd.bit_count() % 2 == 0, "handshaking parity failed")
        parity_fibres[odd] += 1
        first = update(graph, n, edges)
        second = update(first, n, edges)
        fixed += first == graph
        even_time_fixed += second == graph

        if n % 2:
            check(second == first, "odd-order map is not idempotent")
            check(odd_mask(first, n, edges) == 0,
                  "odd-order image is not Eulerian")
            images[first] += 1
        else:
            check(second == graph, "even-order map is not an involution")
            check(odd_mask(first, n, edges) == odd,
                  "even-order parity fibre was not preserved")

    fibre_size = 1 << max(0, edge_count - n + 1)
    check(set(parity_fibres) == {
        mask for mask in range(1 << n) if mask.bit_count() % 2 == 0
    }, "not every even parity vector occurs")
    check(set(parity_fibres.values()) == {fibre_size},
          "degree-boundary fibres are not uniform")

    if n % 2:
        expected_fixed = fibre_size
        check(fixed == expected_fixed, "odd-order fixed count failed")
        check(even_time_fixed == expected_fixed,
              "odd-order positive iterate count failed")
        check(len(images) == expected_fixed, "odd-order image size failed")
        check(set(images.values()) == {1 << (n - 1)},
              "Eulerian representative fibres are not uniform")
        two_cycles = 0
        mode = "idempotent"
    else:
        expected_fixed = 2 * fibre_size
        check(fixed == expected_fixed, "even-order fixed count failed")
        check(even_time_fixed == phase, "even-order second iterate failed")
        two_cycles = (phase - fixed) // 2
        mode = "involution"

    return {
        "n": n,
        "phase": phase,
        "fixed": fixed,
        "two_cycles": two_cycles,
        "mode": mode,
        "degree_fibre": fibre_size,
    }


def main():
    rows = [lane(n) for n in range(1, 8)]
    print("degree-parity cut switching exact spike: PASS")
    print(f"assertions={ASSERTIONS}")
    for row in rows:
        print(
            "lane"
            f" n={row['n']} phase={row['phase']} mode={row['mode']}"
            f" fixed={row['fixed']} two_cycles={row['two_cycles']}"
            f" degree_fibre={row['degree_fibre']}"
        )


if __name__ == "__main__":
    main()
