# Paper 20 Phase-2 arithmetic and source screen

Date: **2026-08-24**

Status: **TECHNICAL COROLLARY / MERGE INTO PAPER 15**

This report is a Phase-2 feasibility and source investigation.  It is not a
proof lock, manuscript, Route evaluation, or claim of publication novelty.

## 1. Frozen search protocol

Search date: **2026-08-24**.

Sources searched:

- arXiv and author-hosted preprints;
- AMS, Springer, Elsevier, and DOI landing pages;
- official university publication records;
- the existing Paper-15 source and proof ledgers;
- targeted web discovery used only to locate primary papers.

Exact query families included:

```text
simultaneous Wieferich primes two bases
double Wieferich pairs primes
common Wieferich primes bases
Fermat quotient injectivity primes
v_r(a^(r-1)-1) two bases
higher order Wieferich base
prime bases Fermat quotient valuation exact density arithmetic progressions
On Wieferich and Non-Wieferich Primes with Prime Bases
Statistical distribution of Fermat quotients
joint distribution Fermat quotient valuations prime bases
Solutions of the congruence a^(p-1)=1 mod p^r Keller Richstein
```

Inclusion criteria:

1. primary mathematical papers or official/author-hosted copies;
2. exact results on Fermat quotients, Wieferich pairs, prime bases, value
   sets, or primes in arithmetic progressions;
3. sources that constrain whether a finite search can prove separation;
4. the exact Paper-15 definition and classification theorem.

Exclusion criteria:

- encyclopedia and sequence pages as theorem evidence;
- numerical tables without a proved inference relevant to the frozen owner;
- fixed-base heuristics promoted to unconditional theorems;
- function-field, elliptic, or number-field analogues unless used only to
  document the general difficulty boundary;
- claims about marked packets, flows, traces, operators, or Route status.

## 2. Source matrix

| Source | Manifestation inspected | Evidence used here | Verification |
|---|---|---|---|
| Paper 15, *Wieferich signatures and Ulm classification for bare packet-base groups* | local current manuscript and proof ledger | exact piecewise definition of `kappa_r(p)` and `B_p ~= B_q iff kappa(p)=kappa(q)`; universal recovery explicitly left unresolved | **VERIFIED** |
| A. V. Sutherland, MIT 18.785 Lecture 18, *Dirichlet L-functions, primes in arithmetic progressions* | official MIT PDF, Theorem 18.1 and its equidistribution discussion | infinitude and equal asymptotic weight of each reduced residue class for a fixed modulus | **VERIFIED** |
| W. Keller and J. Richstein, *Solutions of the congruence a^(p-1) congruent 1 (mod p^r)*, Math. Comp. 74 (2005), 927--936, DOI `10.1090/S0025-5718-04-01666-7` | official AMS PDF, Theorem 1, p. 930 | exact odd-prime valuation-stratum class count; the local count below is a special case and not new | **VERIFIED / MAXIMUM PRIOR** |
| R. Ernvall and T. Metsankyla, *On the p-divisibility of Fermat quotients*, Math. Comp. 66 (1997), 1353--1365, DOI `10.1090/S0025-5718-97-00843-0` | full article mirror plus DOI metadata | fixed-modulus Fermat-quotient kernel, computations, and the distinction between varying the modulus and varying the base | **VERIFIED** |
| R. Crandall, K. Dilcher, C. Pomerance, *A search for Wieferich and Wilson primes*, Math. Comp. 66 (1997), 433--449, DOI `10.1090/S0025-5718-97-00791-6` | author-hosted full article | finite searches and random-model heuristics do not establish infinitude or injectivity | **VERIFIED** |
| I. E. Shparlinski, *Fermat quotients: exponential sums, value set and primitive roots*, Bull. LMS 43 (2011), arXiv `1104.3909` | full arXiv text | value-set and image-size theory for Fermat quotients; literature scope is not an all-coordinate prime-signature injectivity theorem | **VERIFIED** |
| V. Alexandru, C. Cobeli, M. Vajaitu, A. Zaharescu, *Statistical distribution of Fermat quotients*, Chaos Solitons Fractals 161 (2022), 112335, DOI `10.1016/j.chaos.2022.112335` | publisher abstract, introduction, and displayed theorem material | prime bases, Fermat-quotient matrices, GRH coverage, and pair-size statistics are close precedents | **VERIFIED FOR THE INSPECTED CLAIMS** |
| V. Alexandru, C. Cobeli, M. Vajaitu, A. Zaharescu, *On Wieferich and Non-Wieferich Primes with Prime Bases*, Mediterr. J. Math. 20 (2023), Paper 93, DOI `10.1007/s00009-023-02298-1` | official publisher metadata and abstract; full text was not accessible in this pass | very close precedent on prime-base density, partitions, and Wieferich-pair-free sets | **PARTIAL -- FULL TEXT REQUIRED BEFORE A NOVELTY CLAIM** |
| H. Graves and B. Weiss, *The abc conjecture implies infinitely many non-Wieferich places for fixed bases in number fields*, arXiv `2503.19144` | full arXiv text | recent statement of the unconditional fixed-base difficulty ceiling and conditional growth results | **VERIFIED** |

Primary links:

- <https://math.mit.edu/classes/18.785/2019fa/LectureNotes18.pdf>
- <https://doi.org/10.1090/S0025-5718-04-01666-7>
- <https://doi.org/10.1090/S0025-5718-97-00843-0>
- <https://math.dartmouth.edu/~carlp/PDF/paper111>
- <https://arxiv.org/abs/1104.3909>
- <https://doi.org/10.1016/j.chaos.2022.112335>
- <https://doi.org/10.1007/s00009-023-02298-1>
- <https://arxiv.org/abs/2503.19144>

## 3. What the original question reduces to

For fixed prime coordinate `r` and varying rational prime `p`, Paper 15 gives

```text
kappa_r(p) = 0                              if p=r;
kappa_r(p) = v_r(p^(r-1)-1)-1              if r is odd and p!=r;
kappa_2(p) = v_2(p^2-1)-3                   if r=2 and p is odd.
```

At the two diagonal cross-coordinates of distinct odd primes `p,q`, equality
of signatures would force

```text
v_p(q^(p-1)-1)=1,
v_q(p^(q-1)-1)=1.
```

Thus a directed Wieferich relation immediately separates the pair, while the
generic non-Wieferich case does not.  Proving a separating coordinate for
every pair would require genuinely new information across infinitely many
moduli.  The recent literature still treats even fixed-base Wieferich and
non-Wieferich infinitude as difficult, often conditionally.  A finite search
does not by itself close this gap unless accompanied by a proved finite-
reduction theorem.

## 4. Surviving theorem candidate

The source screen exposes a faster, rigorous structural center that is within
the frozen owner and is stronger than a table of collisions.

Let `S` be a finite set of prime coordinates and let
`a=(a_r)_(r in S)` be any vector of nonnegative integers.  Define

```text
P(S,a) = { prime p notin S : kappa_r(p)=a_r for every r in S }.
```

### Candidate theorem: finite-dimensional distribution

For a set `A` of rational primes, write its relative prime density as

```text
d_P(A) = lim_(X->infinity) #{p<=X:p in A} / pi(X),
```

when the limit exists.  This is not ordinary natural density as a subset of
the integers.  For each **fixed** finite `S` and fixed `a`, the relative
prime density of `P(S,a)` exists and is

```text
product_(r in S) delta_r(a_r),

delta_2(k) = 1/2^(k+1),
delta_r(k) = (r-1)/r^(k+1)       for odd r.
```

Consequently:

1. every finite signature pattern occurs for infinitely many rational primes;
2. every finite-coordinate projection of `p |-> kappa(p)` has infinite,
   positive-density fibers;
3. every fixed finite-coordinate projection is noninjective; exhaustive
   comparison restricted to a fixed finite set of coordinates cannot by
   itself certify global injectivity;
4. for any fixed `r` and `k!=l`, the two disjoint positive-relative-density
   sets `A_(r,k)={p!=r:kappa_r(p)=k}` and `A_(r,l)` are separated at
   coordinate `r`.

Equivalently, the prime-indexed signatures have finite-dimensional limiting
distributions given by independent geometric local variables.  This is only
a fixed-finite-dimensional statement: it gives no uniformity when `S`, the
values `a_r`, or the resulting modulus grow with `X`.  It is not universal
prime recovery.

## 5. Proof-owner precheck

For odd `r`, put `n=k+1`.  Modulo `r^(n+1)`, exactly

```text
(r-1)^2
```

reduced residue classes satisfy

```text
v_r(x^(r-1)-1)=n.
```

Indeed, the `r-1` roots modulo `r^n` have `r` lifts each, while exactly one
lift per root remains a root modulo `r^(n+1)`.  Dividing by
`phi(r^(n+1))=(r-1)r^n` gives `(r-1)/r^n`.  This exact count is the
`R=k+2`, `s=k+1` case of Keller--Richstein, Theorem 1, itself credited there
to Meyer; it is included here as a derivation, not claimed as a new local
theorem.

For `r=2`, modulo `2^(k+4)` exactly four odd residue classes have

```text
v_2(x^2-1)=k+3,
```

giving density `4/phi(2^(k+4))=1/2^(k+1)`.

For fixed `S,a`, use the fixed modulus

```text
M(S,a) = product_(odd r in S) r^(a_r+2)
         * (2^(a_2+4) if 2 in S else 1).
```

The Chinese remainder theorem multiplies the admissible class counts, and
the fixed-modulus prime number theorem in arithmetic progressions gives the
stated product density.  The exceptional primes `p in S` are precisely the
relevant nonreduced diagonal exceptions; removing or restoring finitely many
primes does not change the density.

A detached arithmetic check over primes up to `500000`, normalized in each
row by the number of primes up to that bound outside its displayed coordinate
set `S`, agreed with the exact predictions:

| Coordinates and values | Empirical proportion | Exact prediction |
|---|---:|---:|
| `(kappa_2,kappa_3)=(0,0)` | `0.334987` | `1/3` |
| `(kappa_2,kappa_3)=(1,0)` | `0.166386` | `1/6` |
| `(kappa_3,kappa_5)=(1,0)` | `0.177677` | `8/45` |
| `(kappa_2,kappa_3,kappa_5)=(0,0,0)` | `0.268039` | `4/15` |

These computations are checks, not theorem evidence.

## 6. Novelty and maximum-prior boundary

The bounded search found no source stating the exact joint finite-coordinate
`kappa` packaging or its positive-density-fiber consequence for the Paper-15
classifier.  This is only a bounded negative finding, not proof of novelty.
The odd-coordinate depth distribution itself is exact prior art in
Keller--Richstein, and the CRT/PNT-AP product step is standard.  What remains
is a new application and packaging around Paper 15, not a new local counting
engine.

The 2022 and 2023 Alexandru--Cobeli--Vajaitu--Zaharescu papers are the nearest
precedents.  The 2023 full article must be obtained and compared theorem by
theorem before any novelty sentence or manuscript gate.  Even if the joint
statement survives that comparison, the appropriate output is a focused
technical corollary or theorem-level companion to Paper 15, not a standalone
full-length Paper 20.

## 7. Phase-2 verdict

```text
ORIGINAL_GLOBAL_OR_BROAD_INFINITE_CLASS_SEPARATION=HOLD
FINITE_SEARCH_AS_CERTIFICATE=STOP
ARITHMETIC_FORMULA=PASS
FINITE_PROJECTION_DENSITY_OBSTRUCTION=TECHNICAL_COROLLARY_CANDIDATE
FIXED_FINITE_PROJECTION_ONLY=TRUE
UNCONDITIONALITY=PASS
OWNER_BOUNDARY=PASS
KELLER_RICHSTEIN_SUBTRACTION=PASS
MAXIMUM_PRIOR=INCOMPLETE_PENDING_2023_ACVZ_FULL_TEXT
DISPOSITION=PASS_WITH_NOVELTY_CLEARANCE_INCOMPLETE
STANDALONE_PAPER20=STOP_OR_MERGE
MANUSCRIPT=NOT_AUTHORIZED
ROUTE_ADVANCEMENT=NONE
```

Paper 20 should therefore be merged into Paper 15 as an exact
finite-dimensional-distribution corollary, or retained as a short technical
companion only.  Its arithmetic count and CRT/PNT-AP proof have passed an
independent audit, but a standalone manuscript is stopped by maximum-prior
subtraction and the inaccessible 2023 near-neighbor.
