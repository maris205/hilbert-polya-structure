# Fresh hostile re-entry gate: repaired CEF V2

**Decision:** `GREEN_OWNER_THIN`  
**Severity:** **0 Critical / 0 Major / 3 minor**  
**M1 disposition:** **CLOSED**  
**Paper allocation:** eligible to freeze at the claim ceiling below  
**External status:** `HOLD_EXTERNAL`

## 1. Frozen V2 object and independence

The following author files were read as untrusted, read-only evidence.  Their
hashes were pinned before calculation and were unchanged at the end of the
audit.

| author file | bytes | SHA-256 |
|---|---:|---|
| `scouting/root_cyclic_equality_feedback/SCOUT.md` | 7,996 | `343d9c47cceb5017be88c3b293e54d94347f3bfd8de1e14ad953ff6b0f3532cc` |
| `scouting/root_cyclic_equality_feedback/OWNER_SEARCH_LOG.md` | 3,668 | `35ccbf17d775f718d992db77c5d38b3295bd528fc3c0817b33cc436094c52f33` |
| `scouting/root_cyclic_equality_feedback/verify_scout.py` | 10,242 | `8f7673886b09cb2838845a75bf26f98fdf145a0f14f2f0b611b01ee7f26f5aa4` |
| `scouting/root_cyclic_equality_feedback/CANONICAL.txt` | 693 | `270783de0d78e8b35bea6bd2f8b1eba6349089ffe43a5b3de6aac4165fdb3bd0` |
| prior `cef_hostile_gate/AUTHOR_REPAIR_RESPONSE.md` | 1,128 | `95bd6cf74c3a2f6a68cc2fa5ccaf3c6555eab04647c127d3f7c2f58a8363fde7` |

The new verifier imports no author module and reads no author transcript.  It
starts from the literal q-ary map, uses a separately written packed cyclic
operator, constructs affine syndrome profiles from scratch, and checks the
Walsh formula with the transpose operator independently.

## 2. Cold re-derivation of the inherited contract

Let

```text
c(w)_i = 1{w_i != w_(i+1)},   D=I+S over F_2.
```

The first update is `T_q(w)=1+c(w)`.  On a binary state `b`, equality is the
complement of XOR, so `T_q(b)=1+Db`.  Since `D1=0`, induction gives

```text
T_q^t(w)=1+D^(t-1)c(w),  t>=1.                         (A)
```

For `n=2^m`,
`F_2[x]/(x^n-1)=F_2[x]/((x+1)^n)`.  Multiplication by `x+1` is one
nilpotent block; hence `D^n=0`, `dim ker D^j=j`, and
`im D^j=ker D^(n-j)`.

For a fixed change mask of weight `r`, contract every equality edge and
properly colour the remaining cyclic changes.  The exact source count is

```text
chi_q(c)=(q-1)^r+(-1)^r(q-1).                         (B)
```

For `q>=3`, this is zero exactly at `r=1`, equals `q` at `r=0`, and is
positive at every other weight.  This proves the exceptional first image and
also makes the later support repair valid: a coset represented by a forbidden
unit mask contains its complement of weight `n-1`, which is feasible when
`n>=4`.

Consequently:

- the all-one word is the unique recurrent state;
- a nonconstant source has depth
  `1+min{j:D^j c(w)=0}`, while the other `q-1` constants have depth one;
- the depth CDF is the q-weighted homogeneous kernel enumerator, and shells
  are its successive differences;
- at a dyadic checkpoint `j<n`, kernel words are length-`j` blocks repeated
  `n/j` times, giving
  `(1+(q-1)^(n/j))^j+(q-1)2^j`;
- the last shell is
  `(q^n-(q-2)^n)/2-(q-1)2^(n-1)>0`, so height `n+1` is sharp;
- `|im T_q|=2^n-n`, while for `t>=2`, with
  `j=min(t-1,n)`, the image is `1+im D^j` and has size `2^(n-j)`;
- summing (B) over the affine class `D^j c=y+1` gives every binary target
  fibre; nonbinary targets have fibre zero at positive time;
- the Fourier display is ordinary character orthogonality and is correct;
  it receives no contribution credit;
- the sink's one-step fibre has size `q`, and sharp height minus one is `n`,
  so the functional graph recovers `(q,n)`.

The independent exhaustive checks found no defect in these inherited
statements.

## 3. New theorem 1: complete time-two class spectrum

Put `d=y+1` and `a=q-1`.  The image of `D` is the even-weight hyperplane and
`ker D={0,1}`.  Therefore `Dc=d` is feasible exactly when `wt(d)` is even;
when feasible its solutions are the complementary pair `{c,c+1}`.

If `wt(c)=k`, set `rho(d)=min(k,n-k)`.  As `n` is even, `k`, `n-k`, and
`rho` have the same parity.  Summing (B) over the two solutions yields

```text
|(T_q^2)^(-1)(y)|
 = a^rho + a^(n-rho) + 2a(-1)^rho.                    (C)
```

Complementary pairs with `rho=r<n/2` are in bijection with the
`binom(n,r)` masks of weight `r`.  At `r=n/2`, every pair is counted twice,
so the class count is `binom(n,n/2)/2`.  These classes partition all
`2^(n-1)` supported targets, and the class-weighted fibre mass sums to `q^n`.

This derivation verifies both the integrated-radius statistic and the exact
binomial class multiplicities.  It also exposes a precision point missed in
the author prose: different classes can have the same numerical value.  For
`n=4,q=4`, (C) is `24` at both `r=1` and `r=2`; the numerical multiplicity is
therefore `4+3=7`, not either binomial count separately.  The parameter-class
description is nevertheless complete and determines the aggregated spectrum
exactly.

## 4. New theorem 2: midpoint class spectrum

Let `h_0=n/2` and consider time `t=h_0+1`.  Frobenius in characteristic two
gives

```text
D^h_0=(I+S)^h_0=I+S^h_0.
```

Thus a feasible deviation is exactly `d=(u,u)`.  Write `h=wt(u)`.  In each
coordinate pair `(i,i+h_0)`, a zero bit of `u` requires equal mask bits and
contributes `1+a^2` to the affine weight enumerator; a one bit requires
unequal mask bits and contributes `2a`.  Hence

```text
W_d(a)=(1+a^2)^(h_0-h)(2a)^h,
W_d(-1)=2^h_0(-1)^h.
```

Substitution into `W_d(q-1)+(q-1)W_d(-1)` gives exactly

```text
|(T_q^(n/2+1))^(-1)(1+d)|
 = (1+(q-1)^2)^(n/2-h) (2(q-1))^h
   +(q-1)2^(n/2)(-1)^h.                                (D)
```

There are `binom(n/2,h)` choices of `u` with that parameter.  The classes
partition all `2^(n/2)` supported targets, and their fibre mass again sums to
`q^n`.  Numerical collisions occur here too: for `n=4,q=4`, `h=1,2` both
give fibre value `48`.  As in Section 3, this affects only how equal values
are aggregated, not formula (D) or the class census.

## 5. Boundary and counterexample pressure

| attack | result |
|---|---|
| `t=0` | Identity on the full q-ary carrier with singleton fibres; excluded from every positive-time binary formula. |
| `t=1` | Exactly the complements of unit masks are absent; all other binary targets occur. |
| `t=2` | Support exactly the even deviations, including `d=0`; all (C) values are positive for `q>=3`. |
| `t=n/2+1` | Support exactly duplicated half-words; endpoints `h=0,n/2` and the alternating sign correction pass. |
| `t>=n+1` | Only the all-one target remains, with fibre `q^n`. |
| `c=0`, unit, `n-1`, all-one | Multiplicities respectively `q`, `0`, positive, positive; the unit/complement support repair behaves as claimed. |
| `q=2` | At `n=4`, the first image has size 8 rather than 12.  The stated lower bound is essential. |
| `n=2` | At `q=3`, the time-two image has size 1 rather than 2.  The stated `n>=4` bound is essential. |
| nondyadic `n=6` | `D^6` is nonzero on an explicit unit mask.  Dyadicity is essential. |
| direction/transpose | Direct profiles and independently coded transpose-Walsh sums agree in all audited cells. |

No counterexample survives within the theorem domain.

## 6. Independent executable evidence

Run:

```bash
python3 docs/papers162_166_sequence/phase1/cef_reentry_gate/verify_reentry.py
```

The verifier checked:

- 6 literal q-ary boxes, `(4,3),(4,4),(4,5),(4,7),(8,3),(8,4)`, totalling
  75,460 source words;
- every literal trajectory through the stable cap, every change mask, every
  depth shell, image, and binary target fibre in those boxes;
- 4,928 independently summed Walsh evaluations;
- both special spectra in 12 boxes with `n in {4,8,16}` and
  `q in {3,4,5,7}`, covering 132,720 supported spectral targets;
- class counts, aggregated numerical-value counts, target mass, source mass,
  collision sentinels, and four excluded-boundary sentinels.

Receipt:

```text
assertions             1,696,072
verifier SHA-256       805a09efbd74eab0427c20cbf606deb4f7db938b7002e7bc3bf2a1b9816e8373
canonical SHA-256      011d62a7e8b61f5a65489e2dc950c9b2db0030e527349e6b3edcbae7991038bf
fresh replay 1         byte-match; 011d62a7e8b61f5a65489e2dc950c9b2db0030e527349e6b3edcbae7991038bf
fresh replay 2         byte-match; 011d62a7e8b61f5a65489e2dc950c9b2db0030e527349e6b3edcbae7991038bf
py_compile             PASS
math status            PASS
```

## 7. M1 re-entry decision

The prior Major was not a complaint that affine Fourier inversion was false;
it was that a named affine enumerator plus an unevaluated exponential sum did
not classify target dependence and therefore did not supply a second theorem
axis after homogeneous repeated-root weights were removed.

V2 closes that exact defect:

1. (C) evaluates every time-two target by an intrinsic syndrome statistic and
   counts every statistic class.
2. (D) independently evaluates every midpoint target by a different local
   pair statistic and counts every class.
3. Neither result follows from the homogeneous `d=0` weight distribution
   alone: both require affine cosets, the nonlinear q-dependent pullback
   weight (B), and a census of target syndromes.
4. Rule-102/153 owners supply `D` and its powers; Zhao supplies the homogeneous
   code structures.  Neither supplies the q-ary equality front, the weighted
   target fibres, or these target multiplicities.

The proofs are short because the special kernels are repetition/direct-sum
codes.  Shortness is not the same as owner collapse.  The residual remains
owner-thin, but it is now an evaluated target-resolved axis rather than a
renamed Fourier sum.  **M1 is genuinely closed.**

## 8. Findings and repair requests

### Critical

None.

### Major

None.

### minor m1 -- distinguish class multiplicities from numerical-value multiplicities

`SCOUT.md` Section 4A calls (15)--(16) a complete value-and-multiplicity
spectrum.  The class statements are correct, but values are not always
distinct across classes, as the `n=4,q=4` sentinels above show.

**Repair before paper freeze:** say “parameter-class spectrum,” and add
`mult(v)=sum_{r:F_r=v} m_r` (and its midpoint analogue), or explicitly state
that equal class values must be merged to obtain the ordinary numerical
spectrum.  No theorem formula changes.

### minor m2 -- V2 evidence receipts in `SCOUT.md` are stale

The opening paragraph reports `1,546,353` assertions, while the current V2
canonical reports `1,547,369`.  Section 5 still prints the pre-repair hashes
`15dd...c9db` and `f848...081f5`; the pinned V2 hashes are instead
`8f7673...f5aa4` and `270783...b3bd0`.

**Repair before paper freeze:** refresh the assertion count, verifier hash,
canonical hash, and both replay receipts from the frozen V2 artifacts.  No
mathematics changes.

### minor m3 -- cite the direct periodic Rule-102 owner

`OWNER_SEARCH_LOG.md` correctly subtracts the binary CA lane and correctly
names Rule 102/153, but its bibliography stops at broader additive/XNOR
sources.  Kim's 2011 paper directly studies powers of uniform Rule 102 with
periodic boundary conditions and states the power-of-two vanishing theorem.

**Repair before paper freeze:** add the Kim primary source (and optionally the
2023 Ducci/Rule-102 exposition) and assign zero credit to the periodic-ring
power formulas.  This strengthens an already correct firewall and does not
reopen M1.

## 9. Claim ceiling and verdict

CEF may proceed only as the literal owner-subtracted package:

- q-ary equality feedback and its change-mask pullback;
- exact q-weighted depth/image/fibre laws;
- the exceptional first image;
- the integrated-radius time-two spectrum and the half-weight midpoint
  spectrum, with collisions aggregated correctly;
- parameter recovery.

It must not claim a new Rule-102/153 theorem, repeated-root code weight
distribution, general affine-code transform, cycle chromatic formula, or
absolute novelty/priority.

**Final verdict: `GREEN_OWNER_THIN — 0C / 0M / 3m`.**  The three repairs are
paper-freeze hygiene, not reasons to withhold internal allocation.
`HOLD_EXTERNAL` remains in force.
