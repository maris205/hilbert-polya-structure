# P153 — Factorial-collapse finite-plane dynamics

**Status: ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL.**

This directory contains an anonymous amsart short paper on the map
T(x,y)=(x+1,xy) on F_p^2 for odd primes p.

The construction is explicitly credited as a coordinate-swapped specialization
of the triangular polynomial family of Ostafe and Shparlinski. The retained
paper package is the complete nonpermutation functional graph together with
an all-time, every-target inverse-fibre atlas.

## Main outcome

- one p-cycle on the zero axis;
- p-1 disjoint arms of p transient vertices, all entering (1,0);
- temporal polynomial p+(p-1)(z+...+z^p);
- exact target fibres of sizes 1, p, or 0 at every time;
- image profile p(p-min(t,p))+min(t,p);
- pointwise inverse-identifiability criterion;
- fixed-iterate counts and zeta 1/(1-z^p).

## Reproduce

Run python3 verify.py and compare stdout with CANONICAL.txt.
Build the PDF with the four commands in BUILD.md.

`main_round0_original.pdf` preserves the author freeze.
`main_round1.pdf` preserves the Review-A repair freeze: five pages, 394,720
bytes, SHA-256
`81e56c67a1029add2bc93aaf67add40cbc68016a82e8eb2a1b7025cad2d3bb7a`.
The accepted current `main.pdf` and `main_round2.pdf` are byte-identical:
five A4 pages, 392,821 bytes, SHA-256
`ef8c82be2935ed23c406a7c688138400d9c76924d11f9d5c089893e8747049a5`.

Review A returned 0 Critical / 0 Major / 2 Minor and Review B returned
0 Critical / 0 Major / 2 Minor.  The Round-1 declaration/statement repairs
and the Round-2 proof-notation/font-warning repairs close every item;
surviving severity is 0 / 0 / 0.  Internal acceptance does not alter the
external state: `HOLD_EXTERNAL`.
