# Exact bounded evidence

Executed 2026-09-05 in `/root/autodl-tmp/hilbert-polya-structure`:

```sh
python henon_dynamics/continuation_c399_c403_round2/nonaffine_charp/exact_probe.py
```

Python 3.12.3, python-flint 0.9.0. All arithmetic is exact. The producer
reconstructs every displacement polynomial from its square-free blocks and
checks that each block is square-free. This is a consistency check within
the producer, not process-separated review. It counts roots over the algebraic
closure by summing square-free degrees, without enumerating finite fields.
The final run exited zero; its complete stdout is `EXACT_STDOUT.json`.
The saved JSON uses the exact emitted text, with the usual final newline.

For the rational map, coprimality of the homogeneous-coordinate numerator and
denominator is checked at every iteration. The fixed divisor at infinity has
multiplicity $3^n+1-\deg(A_n-xB_n)$, and infinity contributes **one** geometric
point regardless of this multiplicity.

## Counts and multiplicity blocks

An entry $d\mathbin{@}m$ means a square-free polynomial of degree $d$ whose
roots have exact multiplicity $m$ in the displacement. It is not an
irreducible-factor degree claim.

### $f_1=x+x^6$ over $\mathbb F_3$, affine domain

| $n$ | Scheme length $6^n$ | Geometric $N_n$ | Multiplicity at zero | Square-free blocks |
|---|---:|---:|---:|---|
| 1 | 6 | 1 | 6 | $1@6$ |
| 2 | 36 | 11 | 6 | $10@3,1@6$ |
| 3 | 216 | 61 | 36 | $60@3,1@36$ |
| 4 | 1296 | 411 | 6 | $390@3,21@6$ |
| 5 | 7776 | 2571 | 6 | $2550@3,21@6$ |
| 6 | 46656 | 15491 | 36 | $15480@3,10@18,1@36$ |

For $n=4$ the multiplicity-six block is

$$x(x^{20}+x^{10}+2),$$

and its nonzero factor includes the square-free witness
$Q_4=x^4+x+2$. The exact checks are

$$Q_4^6\mid f_1^{\circ4}-x,\quad Q_4^7\nmid f_1^{\circ4}-x,
\qquad\gcd(Q_4,f_1-x)=\gcd(Q_4,f_1^{\circ2}-x)=1.$$

Thus its four distinct roots have exact period four, not a fixed-origin
ramification repeat. At period five the analogous witness is

$$Q_5=x^{20}+2x^{15}+x^{10}+x^5+2,$$

with exact multiplicity six and $\gcd(Q_5,f_1-x)=1$. Both witnesses are
square-free. The assertions concern all their geometric roots and do not
need an irreducibility assumption.

### $f_2=x+x^{-2}$ over $\mathbb F_2$, projective domain

| $n$ | Scheme length $3^n+1$ | Geometric $N_n$ | Infinity multiplicity | Finite blocks |
|---|---:|---:|---:|---|
| 1 | 4 | 1 | 4 | none |
| 2 | 10 | 1 | 10 | none |
| 3 | 28 | 7 | 4 | $6@4$ |
| 4 | 82 | 13 | 34 | $12@4$ |
| 5 | 244 | 61 | 4 | $60@4$ |
| 6 | 730 | 109 | 10 | $84@4,24@16$ |
| 7 | 2188 | 547 | 4 | $546@4$ |
| 8 | 6562 | 853 | 130 | $840@4,12@256$ |

The apparent odd-period formula is only an observed pattern in this census.
The proved elliptic-curve reduction in `PROOF_PACKAGE.md`, not this pattern,
is the decisive rejection reason.

### $f_3=x^3+x^2$ over $\mathbb F_2$, affine domain

| $n$ | Scheme length $3^n$ | Geometric $N_n$ | Square-free blocks |
|---|---:|---:|---|
| 1 | 3 | 3 | $3@1$ |
| 2 | 9 | 9 | $9@1$ |
| 3 | 27 | 21 | $19@1,2@4$ |
| 4 | 81 | 81 | $81@1$ |
| 5 | 243 | 233 | $228@1,5@3$ |
| 6 | 729 | 711 | $709@1,2@10$ |
| 7 | 2187 | 2180 | $2173@1,7@2$ |
| 8 | 6561 | 6561 | $6561@1$ |
| 9 | 19683 | 19650 | $19639@1,11@4$ |

Zero is a simple root of every displayed displacement. The period-three
multiple factor is $x^2+x+1$, consisting of nonzero fixed points whose
multipliers acquire resonance at the third iterate. This is **not** evidence
for a primitive three-cycle.

The genuinely new witnesses are

$$R_5=x^5+x^3+1,\qquad R_7=x^7+x^6+x^5+x^2+1.$$

$R_5$ has exact multiplicity three in $f_3^{\circ5}-x$; $R_7$ has exact
multiplicity two in $f_3^{\circ7}-x$. Each is square-free and coprime to
$f_3-x$, hence all its roots have exact period five or seven respectively.
These are unrelated to the fixed critical point and the nonzero fixed-point
multiplier-three tower.

## Scope of the conclusion

The exact new-period witnesses refute the particular one-exceptional-orbit
counting ansatz. They do not prove that infinitely many such exceptional
cycles exist, that no finite description is possible, or that either
non-affine zeta is rational, transcendental, or has a natural boundary.
