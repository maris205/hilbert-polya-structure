# Paper 21 Phase-2 effective-Chebotarev source screen

Date: **2026-08-24**

Status: **SOURCE PASS / REVISE FOR A STRUCTURAL CONDUCTOR SPECIALIZATION**

This is a Phase-2 source and feasibility report.  It verifies exact density
and black-box effective bounds, but it does not yet authorize a standalone
paper or claim that the generic bounds are new.

## 1. Search protocol

Search date: **2026-08-24**.

Searches covered primary/official records at AMS, Springer, Elsevier,
Numdam, MSP, institutional repositories, arXiv, author repositories, and the
complete Paper-15 proof package.  Exact query families included:

```text
effective Chebotarev least prime conjugacy class Lagarias Montgomery Odlyzko
Bach Sorenson explicit bounds Chebotarev GRH 4 log discriminant
Kadiri Wong Chebotarev all number fields exponent 310
Thorner Zaman explicit least prime relative conductor
new bound relative error Chebotarev Thorner Zhang
Kummer cyclotomic field discriminant explicit conductor
distribution order index reductions algebraic numbers Proposition 13
Moree primes d divides ord_p(g) Frobenius condition
multiplicative order exact valuation Kummer Chebotarev
```

Load-bearing inclusion required a primary article or official manifestation
with an exact theorem locator for unconditional/GRH Chebotarev, least primes,
explicit constants, relative conductors, Kummer--cyclotomic discriminants, or
multiplicative orders.  A current-landscape comparator could be retained from
an official abstract/metadata record only when labeled non-load-bearing and
never used for a formula.  Textbooks and tertiary pages were excluded from
load-bearing claims; primitive-root and divisibility results were not treated
as exact-order results.

## 2. Frozen field and target class

For fixed distinct primes `p,r` and `m>=1`, put

```text
q = r^(m+1),
E = Q(zeta_q, p^(1/r)).
```

For odd `r`, this is the Paper-15 compositum of
`F=Q(zeta_r)`, `F(p^(1/r))`, and `Q(zeta_q)`.  For `r=2`, read the radical as
`sqrt(p)`.  Paper 15 already proves the required intersections and the exact
translation from the target Frobenius class to

```text
v_r(ell-1)=m,
v_r(ord_ell(p))=m.
```

It does not claim the density or an effective least witness.

The independent field/group reconstruction gives

```text
n = [E:Q] = r phi(r^(m+1)) = r^(m+1)(r-1).
```

For odd `r`, `Gal(E/Q)` is the appropriate semidirect product of the Kummer
`C_r` with `(Z/qZ)^x`.  The condition `v_r(ell-1)=m` permits the `r-1`
cyclotomic components

```text
a_c = 1 + c r^m mod r^(m+1),       c in F_r^x.
```

For each `a_c`, the nonzero Kummer components form one conjugacy class of
size `r-1`.  The full exact-order condition is therefore the disjoint union
of `r-1` such classes, containing `(r-1)^2` group elements.  For `r=2`
there is one admissible cyclotomic component and one class of size one.
Chebotarev consequently gives the exact natural density

```text
delta_(p,r,m) = (r-1)/r^(m+1).
```

For `r=2` this specializes to `2^(-(m+1))`.  Paper 15's single frozen choice
`c=1` has density `r^(-(m+1))`; that subfamily already suffices for existence
and for every least-prime bound below, but it is not the density of all
solutions to the two exact valuation conditions.  The total density is
independent of `p` for the fixed allowed parameters.  It is a new consequence
relative to Paper 15, not yet a novelty claim relative to the full literature.

## 3. Source matrix

| Source | Exact use | Verification |
|---|---|---|
| Lagarias--Odlyzko, *Effective versions of the Chebotarev density theorem* (1977), pp. 409--464 | TeXromancers full retypeset: Theorem 1.1 and Corollary 1.2 (PDF p. 4) give the GRH error term and least-prime corollary; Theorem 1.3 (PDF pp. 4--5) gives unconditional counting with a possible exceptional zero | **VERIFIED FROM FULL RETYPESET; NONPUBLISHER MANIFESTATION** |
| Lagarias--Montgomery--Odlyzko, *A bound for the least prime ideal in the Chebotarev density theorem*, Invent. Math. 54 (1979), 271--296, DOI `10.1007/BF01390234` | Deep Blue publisher scan, Theorem 1.1 (statement PDF p. 2 / printed p. 272; formal proof begins PDF p. 13 / printed p. 283, Section 3): unconditional effective existence in a target class with an absolute computable exponent | **VERIFIED** |
| E. Bach, J. Sorenson, *Explicit bounds for primes in residue classes*, Math. Comp. 65 (1996), 1717--1735, DOI `10.1090/S0025-5718-96-00763-6` | Cor. 3.3 (AMS PDF p. 5; printed p. 1721) extends the input to arbitrary Galois conjugacy classes; Thm. 5.1 (PDF p. 13; printed p. 1729) gives the explicit ERH least-prime formula | **VERIFIED FROM FULL OFFICIAL AMS PDF** |
| L. Grenié, G. Molteni, *An explicit Chebotarev density theorem under GRH*, JNT 200 (2019), 441--485, DOI `10.1016/j.jnt.2018.12.005` | Theorem 1.1 (author-hosted theorem extract PDF p. 2) gives numerical GRH error terms for counting functions | **VERIFIED** |
| H. Kadiri, P.-J. Wong, with Fiori appendix, *Primes in the Chebotarev density theorem for all number fields*, JNT 241 (2022), 700--737, DOI `10.1016/j.jnt.2022.03.012` | Thm. 1 (printed p. 701; author-hosted journal PDF p. 2) gives the all-field unconditional bound `N p <= D_L^310` | **VERIFIED FROM FULL JOURNAL PDF** |
| J. Thorner, A. Zaman, *An explicit bound for the least prime ideal in the Chebotarev density theorem*, ANT 11 (2017), 1135--1197, DOI `10.2140/ant.2017.11.1135` | Eq. (1-6) defines `Q(L/K)` and Thm. 1.1 (both printed p. 1137; publisher PDF p. 5) gives the fixed-field-discriminant/relative-conductor bound when an abelian subgroup meets the class | **VERIFIED FROM FULL PUBLISHER PDF; STRUCTURAL ROUTE** |
| J. Thorner, Z. Zhang, *A new bound on the relative error in the Chebotarev density theorem*, Forum Math. 38 (2026), 1513--1541, DOI `10.1515/forum-2025-0281` | newest AHC/subgroup comparison; no automatic gain is inferred for this already-abelian relative subgroup | **VERIFIED FROM PUBLISHER ABSTRACT; NON-LOAD-BEARING COMPARATOR** |
| P. Sgobba, *On the distribution of the order and index for the reductions of algebraic numbers*, JNT 223 (2021), 132--152, DOI `10.1016/j.jnt.2020.11.008` | Thm. 1 (repository author-preprint PDF p. 2) handles order conditions under GRH; Prop. 13 (PDF p. 8; proof continues on p. 9) supplies the cyclotomic--Kummer discriminant bound used below | **VERIFIED FROM FULL AUTHOR/INSTITUTIONAL-REPOSITORY PREPRINT** |
| P. Moree, *On primes p for which d divides ord_p(g)*, FACM 33 (2005), 85--95, DOI `10.7169/facm/1538186603` | closest order-divisibility density comparator | **VERIFIED; NON-LOAD-BEARING AND NOT AN EXACT-VALUATION THEOREM** |

Primary/official links:

- Lagarias--Odlyzko author bibliography and TeXromancers full retypeset:
  <https://websites.umich.edu/~lagarias/zeta.html>,
  <https://aareyanmanzoor.github.io/assets/articles/lagarias-odlyzko.pdf>
- Lagarias--Montgomery--Odlyzko Deep Blue publisher scan:
  <https://deepblue.lib.umich.edu/items/7fccbe0a-3a17-4fdc-9ca1-10d448eda150>
- <https://www.ams.org/journals/mcom/1996-65-216/S0025-5718-96-00763-6/S0025-5718-96-00763-6.pdf?download=1>
- <https://air.unimi.it/handle/2434/634041>
- <https://sites.unimi.it/molteni/research/papers-pdf/44-molteni-An_explicit_Chebotarev_density_theorem_under_GRH.pdf>
- <https://www.sciencedirect.com/science/article/pii/S0022314X22000865>
- <https://www-math.nsysu.edu.tw/~pjwong/stuff/leastprimeALL.pdf>
- <https://msp.org/ant/2017/11-5/ant-v11-n5-p04-p.pdf>
- <https://doi.org/10.1515/forum-2025-0281>
- <https://www.sciencedirect.com/science/article/pii/S0022314X20303371>
- <https://orbilu.uni.lu/bitstream/10993/43472/1/Sgobba1.pdf>
- <https://arxiv.org/abs/math/0407421>

The older `D_L^12577` and sufficiently-large-discriminant variants were
screened but are superseded for the uniform all-field black-box statement by
Kadiri--Wong's exponent `310`.  Hooley/Artin primitive-root, family-average,
and divisibility-only results have mismatched quantifiers or conclusions.

## 4. Correct black-box bounds

Sgobba's discriminant estimate gives

```text
log |D_E| <= B(p,r,m),

B(p,r,m) = n ((m+2) log r + 2 log p).
```

Kadiri--Wong therefore yields an unconditional rational-prime witness

```text
ell <= exp(310 B(p,r,m)).
```

Under the exact ERH/GRH hypotheses of Bach--Sorenson, their explicit
least-prime bound yields

```text
ell <= (4 B(p,r,m) + 2.5 n + 5)^2.
```

The base field is `Q`, so the prime ideal norm in these applications is a
rational prime.  Neither formula is to be called sharp.  The first is an
all-field unconditional black box, and the second must retain its stated
L-function hypothesis.

The counting form under GRH can be supplied by Grenie--Molteni, but a
counting error term and a least-prime theorem must remain separately labeled.

## 5. Why this is not yet a standalone paper

The exact density is a useful addition, and the two explicit bounds are
correct.  However, deriving them uses Paper 15's existing field and class
followed by direct substitution into general theorems.  That meets the
standard for a short quantitative corollary, not the frozen standalone
threshold.

The sole credible structural improvement is relative-conductor reduction.
Put

```text
F = Q(zeta_r),
H = Gal(E/F),                 |H|=r^(m+1).
```

Then `H` is abelian and contains the target element.  For odd `r`, the
intersection calculation identifies `H` with `C_r x C_(r^m)`.  For `r=2`,
it is instead the product of the extra quadratic Kummer factor with the
abelian group `Gal(Q(zeta_(2^(m+1)))/Q)`; no false cyclic decomposition is
used.  In both branches,

```text
[F:Q]=r-1,
|D_F|=r^(r-2)                    (F=Q when r=2).
```

Thorner--Zaman can therefore use

```text
Q(E/F) = max_(chi in H^) Norm_(F/Q)(f_chi)
```

instead of only the full `D_E`.  To promote, Paper 21 must compute all local
Artin conductors at the primes above `p` and `r`, obtain a uniform explicit
formula or sharp bound for `Q(E/F)`, and show that the resulting least-prime
bound is nonvacuously stronger on a genuine parameter range.

The 2026 Thorner--Zhang extension does not automatically improve this case:
the target already lies in a natural abelian subgroup, and its class/degree
parameters do not obviously satisfy the newer improvement regime.

## 6. Binding next gate

1. Compute the different/relative discriminant and the Artin conductor of
   every character of `Gal(E/F)` at `p` and `r`.
2. Treat odd `r` and `r=2`, including small `m`, separately where necessary.
3. Derive `Q(E/F)` exactly or with an explicit uniform sharp bound.
4. Substitute it into Thorner--Zaman without turning its computable implicit
   constant into a printed numerical constant.
5. Compare the result with both `exp(310B)` and the GRH quadratic bound.
6. If no genuine improvement survives, downgrade to a short note containing
   only the density and black-box corollaries.

## 7. Phase-2 verdict

```text
SOURCE_VERIFICATION=PASS
SELECTED_CLASS_DENSITY=r^(-(m+1))
EXACT_TARGET_DENSITY=(r-1)/r^(m+1)
UNCONDITIONAL_BLACK_BOX_BOUND=PASS
GRH_BLACK_BOX_BOUND=PASS
STANDALONE_INCREMENT=REVISE
RELATIVE_CONDUCTOR_SPECIALIZATION=NOT_STARTED
STOP=FALSE
MANUSCRIPT=NOT_AUTHORIZED
ROUTE_ADVANCEMENT=NONE
```

Paper 21 remains a live proof candidate.  Its next phase is not another
general literature search; it is the explicit local conductor calculation.
