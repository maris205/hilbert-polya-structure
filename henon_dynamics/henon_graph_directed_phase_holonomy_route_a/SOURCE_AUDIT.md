# C129 source audit

## Source boundary

This package is source-defined. Its mathematical inputs are the frozen rational
matrix `A`, integer translations, directed graph `B`, rational branch weights,
the radius-three bidisc, and the fixed character `chi(m)=zeta_5^m`. Every
reported coefficient is derived from those bytes by exact rational group-ring
or cyclotomic arithmetic.

No paper, website, numerical database, prime table, zero table, arithmetic
local datum, fitted parameter, or Route-B artifact is used. The package
therefore makes no literature-novelty claim and contains no external citation.

## Frozen source

```text
A = [[3/16,-1/32],[1/4,0]]
t = (-2,0,2); control t' = (0,-2,2)
B = [[1,1,0],[1,0,1],[1,0,0]]
c = (1/2,1/3,1/5)
chi(m) = zeta_5^m, with zeta_5 primitive
W_chi = B diag(c_j chi(t_j))
domain = three copies of D_3^2
clock = one admissible graph edge per iterate
determinant = D_chi(z)=det(I-z L_chi)
```

The theorem has no orbit cutoff. Periods one through eight and Taylor degree
eight are finite replay prefixes only.

## Integrity and interpretation boundary

The producer is checked by an independently written standard-library checker
with closed key schemas for the claim-bearing objects, a fresh SymPy
reconstruction with explicit polynomial finite sections, exact byte replay,
and a 35-case repaired-hash hostile suite. The character records
only translation residues modulo five together with their branch assignment.
Consequently the result is described as position-sensitive under this frozen
character, never as complete geometric recovery.

Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.
