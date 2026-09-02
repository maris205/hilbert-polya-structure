# Owner-search log — GDN general dihedral normalizer dynamics

**Date:** 2026-09-02 UTC  
**Status:** bounded internal search, `HOLD_EXTERNAL`  
**Rule:** a search non-hit is never novelty, priority, or release evidence.

## Literal and theorem queries

The screened queries included:

```text
normalizer map dynamics all subgroups dihedral group functional graph
iterated normalizer subgroups dihedral group normalizer tower
normalizer of every subgroup finite dihedral group formula
"N_{D_n}" "r^i s" subgroup normalizer
"normalizer" "H_{d,j}" dihedral
dihedral subgroup normalizer gcd(d,2) formula
functional graph subgroup normalizer dihedral
dihedral normalizer forest divisor sigma tau
"normalizer graph" "dihedral group" subgroups
"functional graph" "normalizer" subgroups group
"iterated normalizer" "D_{2n}"
"hypernormalizers" dihedral group subgroup
"normalizer dynamics" subgroup lattice
dihedral subgroup normalizer "sigma(n)" "tau(n)"
dihedral subgroup normalizer functional graph binary tree
dihedral normalizer "33" "35" subgroups
```

No screened result stated the complete finite self-map together with its
all-time target fibres, exact graph-conjugacy signature, and arithmetic
collision family.  This is only a bounded non-hit.

## Direct structural owners — zero credit

1. Stephan R. Cavior, *The Subgroups of the Dihedral Group*, Mathematics
   Magazine 48 (1975), 107,
   <https://doi.org/10.1080/0025570X.1975.11976454>.

   This is a direct owner for the cyclic/dihedral subgroup classification.
   The list `R_d,H_(d,j)`, its uniqueness, and the counts `tau(n),sigma(n)`
   receive zero contribution credit.

2. Keith Conrad, *Dihedral Groups II*, author-hosted notes,
   <https://kconrad.math.uconn.edu/blurbs/grouptheory/dihedral2.pdf>.

   Theorem 3.1 gives the same complete subgroup list in the exact
   `r^d,r^i s` coordinates.  This is an authoritative corroborating source,
   not a contribution basis.

3. Peter E. Frenkel, *Fixed point data of finite groups acting on
   3-manifolds*, Algebraic & Geometric Topology 3 (2003), 709--718,
   <https://msp.org/agt/2003/3-2/agt-v3-n2-p03-p.pdf>.

   On p. 713, immediately before Theorem 3.1, Frenkel records for every
   dihedral subgroup `D_k<=D_m` that it is self-normalizing when `m/k` is odd
   and has normalizer `D_(2k)` when `m/k` is even.  In the present step
   coordinate this is exactly the odd/even `d -> d/gcd(d,2)` rule for the
   reflection-containing carrier, albeit used there for a different
   3-manifold fixed-point problem.  The one-step rule and the resulting
   binary branching receive zero credit.

4. Hayder Baqer Ameen (the PDF header uses the surname Shelash), Hasanain
   Hamid Ahmad, and Ahmed J. Obaid, *On characterizations some of subgroups
   of the dihedral group D2n*, Journal of Discrete Mathematical Sciences and
   Cryptography 26 (2023), 1157--1162,
   <https://doi.org/10.47974/JDMSC-1553>;
   publisher full text:
   <https://tarupublications.com/journals/jdmsc/volume/26/issue/4/on-characterizations-some-of-subgroups-of-the-dihedral-group-d2n/pdf>.

   Theorem 1.2 on p. 1159 states the normalizer of a subgroup of `D_(2n)` by
   cases: cyclic rotation subgroups normalize to the ambient group,
   odd-step dihedral subgroups are self-normalizing, and even steps halve.
   Despite difficult PDF extraction, this is a direct published owner of the
   complete one-step update (2.1)--(2.2), so that update receives zero credit.

5. Qayum Khan, dissertation with erratum, Section 5.1 on the infinite
   dihedral group,
   <https://qkhan.pages.iu.edu/research/ARTICLES/Dissertation_wERRATUM.pdf>.

   Proposition 5.1.1 classifies infinite-dihedral subgroups and records that
   the normalizer of `<x_i,t^j>` halves `j` when it is even and is
   self-normalizing when `j` is odd.  Finite quotients inherit the same
   congruence mechanism.  The odd/even normalizer step is therefore treated
   as owned structural background.

6. H. B. Shelash and A. R. Ashrafi, *Wielandt subgroups of certain finite
   groups*, Itogi Nauki i Tekhniki. Sovremennaya Matematika i ee Prilozheniya
   177 (2020), 121--131, DOI
   <https://doi.org/10.36535/0233-6723-2020-177-121-131>;
   primary index and full text:
   <https://www.mathnet.ru/eng/into606>.

   This computes the Wielandt subgroup and Wielandt length of `D_(2n)`; for
   `n=2^r m` it records length `r` through a related sequence of halving
   subgroups.  It is not the pointwise iteration of `H -> N_G(H)` on the full
   subgroup carrier, but it directly owns the two-adic halving clock in a
   nearby aggregate construction.  That temporal intuition receives zero
   credit.

7. Laurent Bartholdi and Said N. Sidki, *The Automorphism Tower of Groups
   acting on Rooted Trees*, arXiv:math/0308127,
   <https://arxiv.org/abs/math/0308127>.

   This owns broad normalizer/automorphism-tower context and includes
   dihedral examples in a different ambient tree-isometry setting.  Generic
   tower terminology and consequences receive zero credit.

## Nearby but non-controlling sources

- Results about the normalizer of a dihedral group inside units of an integral
  group ring concern a different ambient normalizer and do not control the
  self-map on the subgroup lattice.
- The hypernormalizer example for dihedral 2-groups on Mathematics Stack
  Exchange exhibits a single halving chain, but it is not a primary source and
  does not supply an all-subgroup graph.  It is not used as owner evidence.
- Normality-degree formulas count normal subgroups but do not provide the
  iterated normalizer graph.
- Normalizers of a single reflection give the bottom case of the halving
  rule, not the all-subgroup dynamics.

## Bounded non-hit boundary

The independent hostile rerun located direct owners of the complete subgroup
carrier, the complete one-step normalizer formula, the dihedral-subgroup
odd/even rule, and a related two-adic Wielandt-length chain.  It did **not**
locate a primary source that simultaneously constructs the unlabelled
functional graph on every subgroup, gives every-target fibres for all positive
iterates, proves the iff signature
`(v2(n),sigma(odd(n)),tau(n))`, or identifies the `33/35` arithmetic graph
collision.  Search-engine coverage, indexing, terminology, and full-text OCR
are incomplete; this bounded non-hit cannot support novelty or priority.

## Residual claim surface under audit

Only the following conjunction remains eligible for internal credit:

1. complete `sigma(odd(n))`-component binary-forest decomposition;
2. exact depth polynomial and all-time images;
3. every-target fibres of every positive iterate;
4. the iff graph signature `(v2(n),sigma(odd(n)),tau(n))`; and
5. explicit arithmetic collisions such as `33/35` and all common two-power
   lifts.

Any direct or equivalent owner of that conjunction changes the disposition
from `PASS_OWNER_THIN` to `KILL_DIRECT` or a materially narrower reserve.
