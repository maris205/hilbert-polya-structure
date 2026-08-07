# Nonabelian voltage zeta obstruction

**Candidate:** HCS-C15  
**Research status:** proved scoped obstruction package  
**Hilbert--Pólya status:** Route-A rejected

## Outcome

This round tested the proposed escape from finite Hénon symbolic models to
nonabelian voltage covers and Artin--Ihara factors. The escape fails in three
different ways, depending on how much representation data is retained.

1. **Canonical aggregation loses conjugacy data.** If a primitive base orbit
   has holonomy \(g\in G\), order \(o\), and weight \(x\), then the regular
   cover with the trivial Artin factor removed contributes

   \[
   (1-x)(1-x^o)^{-|G|/o}.
   \]

   This local factor sees \(\operatorname{ord}(g)\), not the conjugacy class
   of \(g\). This is a direct consequence of standard graph-covering theory,
   not a new Artin--Ihara factorization theorem.

2. **Every fixed finite-memory repair has too few zeros.** For a fixed
   finite-state system, constant finite-dimensional twist, and finitely many
   positive locally constant roof values,

   \[
   D(s)=\det\!\left(I-\sum_{j=1}^r e^{-s\tau_j}B_j\right)
   \]

   is a nonzero exponential polynomial of finite type. Jensen's formula
   gives \(N_D(T)=O(T)\) in a fixed vertical strip. The Riemann--von Mangoldt
   law is \(\Theta(T\log T)\), so no fixed determinant in this class has the
   divisor of \(\xi\), even when the finite roofs are incommensurable.

3. **The natural Heisenberg tower returns to the branching poles.** In
   \(H(\mathbb Z/3^m\mathbb Z)\), an exact-conductor one-dimensional character
   has adjacency eigenvalue

   \[
   2+2\cos(2\pi/3^m)\longrightarrow4.
   \]

   More strongly, the primitive \(3^m\)-dimensional Schrödinger block
   \(U+U^*+V+V^*\) also has top eigenvalue tending to \(4\). Thus deleting
   every abelian sector still does not prevent nontrivial Bass poles from
   returning toward \(u=1/3\) and \(u=1\). The tower is eventually
   non-Ramanujan in an exact-conductor nonabelian sector.

The result is negative for Hilbert--Pólya, but it gives a concrete design
rule: a surviving graph construction must use a canonically selected infinite
representation object, escape finite exponential type, and avoid amenable
near-trivial sectors. Merely deleting the trivial representation is not
enough.

## Chronology witness

Let \(H_7=H(\mathbb F_7)\) with multiplication

\[
(a,b,c)(a',b',c')=(a+a',b+b',c+c'+ab').
\]

The cyclically reduced primitive words

~~~text
P = XXXyxxyxYY
Q = XXXyxyxxYY
~~~

have the same one-letter counts and the same complete cyclic directed-bigram
ledger. They are neither cyclic nor time-reversal copies, but chronological
multiplication gives

\[
g_P=(0,0,3),\qquad g_Q=(0,0,2).
\]

These are distinct central conjugacy classes, neither equal nor inverse, and
both have order seven. The canonical aggregate merges their local factors; a
Schrödinger central-character sector distinguishes them. The computation
never replaces the ordered dynamics by an averaged transition matrix.

## Exact certificates

The D4 control computes a full \(32\times32\) regular-cover determinant and
checks the Artin product over four one-dimensional representations and one
two-dimensional representation. For the two-dimensional block with edge
variables \(x,y\), the exact determinant is

\[
(y-1)(y+1)
(3x^2y-x^2-y-1)
(3x^2y+x^2-y+1),
\]

where juxtaposition denotes multiplication. At unit roof it has degree eight,
so its
vertical zero repetition is exactly linear. An independent program enumerates
all 343 elements of \(H_7\), decomposes both right-regular permutations into
49 seven-cycles, and directly checks the new character on
\(H(\mathbb Z/9\mathbb Z)\).

## Reproduction

From this directory:

~~~bash
python -m pip install -r requirements.txt
python code/voltage_zeta.py --output results
python code/independent_check.py --output results/independent_check.json
cd code && python -m unittest -v test_voltage_zeta.py
~~~

The release environment is Python 3.12.3 with SymPy 1.14.0, and the expected
result is nine passing tests.

The producer uses exact symbolic arithmetic for every determinant and group
identity. Floating-point values occur only in illustrative density and tower
tables; the stated asymptotic results are proved independently.

## Directory guide

- **paper/**: manuscript source and compiled PDF;
- **code/**: exact producer, independent checker, and regression tests;
- **results/**: machine-readable certificates and density illustration;
- **evaluations/route_a/**: formal Route-A ruling;
- **DERIVATION_PACKAGE.md**: theorem statements and proofs;
- **SOURCE_AUDIT.md**: primary-source and novelty audit;
- **EXPERIMENT_PLAN.md**: frozen object, controls, and falsifiers;
- **PAPER_PLAN.md**: claims--evidence map;
- **IDEA_REPORT.md**: breadth-first selection and next pivot.

## Claim boundary

This project does **not** claim a new general Artin--Ihara decomposition, a
new theory of zeros of exponential sums, or a Hilbert--Pólya operator. It
does not rule out infinite-state or nuclear transfer operators, infinitely
many roof values, non-locally-constant potentials, nonamenable property-\(\tau\)
towers, or a separately proved infinite determinant of non-finite exponential
type. The project also does not derive its graph system from the
area-preserving Hénon map; it is the deliberate system-level pivot requested
after the Hénon and solenoid lanes reached structural obstructions.
