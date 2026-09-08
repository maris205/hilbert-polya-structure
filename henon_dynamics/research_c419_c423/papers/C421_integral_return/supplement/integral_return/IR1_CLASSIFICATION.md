# IR1 complete classification and native-clock level counts

2026-09-07. Computer-assisted theorem candidate, pending independent
review. The analytic exhaustion is in `IR1_PROOF.md`; the single complete
finite certification is `certify_ir1_core.py` and its preserved outputs.
No C-number or admission decision is made here.

## Theorem: all parameters, levels and ordinary integer points

For `a in Z`, every periodic point of
`T_a(x,y,z)=(y,z,yz+a-x)` is obtained by taking consecutive triples
of one of the following repeated scalar words. Each table entry denotes
one *oriented native orbit*, with precisely the listed least period.
The stated parameter ranges remove all duplicate orbits. A cyclic
rotation is the same orbit; time reversal is not automatically identified.

| Least period | Parameter condition and one scalar word per orbit | Invariant level `k=K_a` |
| --- | --- | --- |
| 1 | `(r)`, `r in Z`, `a=2r-r^2` | `r^2(2r-3)` |
| 2 | `(u,v)`, `u<v`, `a=u+v-uv` | `uv(u+v-3)` |
| 3 | `(-2,-2,t)`, `a=2t-4`, `t!=-2` | `8-(t-4)^2` |
| 4 | `(-1,t,-1,a+1-t)`, `2t<a+1` | `t^2-(a+1)t+2a+2` |
| 5 | `(-1,t,0,0,-1-t)`, `a=-1`, `t in Z except -1` | `t(t+1)` |
| 5 | `(-4,-2,-3,-3,-2)`, `a=-13` | `-64` |
| 6 | `(0,0,t,0,0,-t)`, `a=0`, `t>=1` | `t^2` |
| 8 | `(-1,t,1,t,-1,-t-2,1,-t-2)`, `a=-1`, `t>=0` | `(t+1)^2+1` |
| 9 | `(-2,-1,0,0,-1,-2,0,-1,0)`, `a=-2` | `-1` |
| 12 | `(1,m,1,m-1,-1,-m,1,1-m,1,-m,-1,m-1)`, `a=0`, `m>=1` | `m^2-m+2` |

The result includes singular ordinary points. No normalization,
multiplicity weighting, branch removal, compactification, blow-up or
scheme-theoretic fixed locus replaces the specified integer point set.
All possible least periods are exactly `1,2,3,4,5,6,8,9,12`.
Thus `T_a^360` fixes the entire integral periodic locus; this does **not**
assert that `T_a` has finite order on its full phase space.

## Why the words are exhaustive

Sections 1–3 of `IR1_PROOF.md` prove, without a computation or parameter
bound, that every unlisted orbit has `1<=D<=100` and
`|x_i+1|<=3D`, where `D=max |x_(i+2)-x_i|`.
Section 4 proves that the finite extremal seed loops cover this entire
residual periodic locus and that exact iteration terminates, without a
chosen period cutoff. The completed certificate gives:

- 74,866 admissible seeds; 25,907 return to their start.
- 30,335 certified difference exits and 18,624 certified height exits.
- After adding both native time orientations and removing cyclic
  rotations, 25,851 distinct finite-certificate cycles.
- The existing symbolic families account for all but the two exceptional
  words in the table, at `a=-13` and `a=-2`.

The maximum observed iteration length was 12, but no 12-step or other
period limit exists in the code. The complete cycle-list SHA-256 is
`352ffd5b5b188e32c347a4083559680e5d1bad12c8e6c6d7cd3dad6324935805`.
The first-run code SHA-256 is
`750b4dbb54cacd1df11cc3929ed436cf8de9877048545f212cecc9bc03b75330`.
Those files remain unchanged. The finite output is not claimed to count
all global cycles: the table parametrizes the unbounded families exactly.

## Least returns and uniqueness of representatives

Every displayed word satisfies the scalar recurrence by direct
substitution, including its wraparound. A length `l` scalar word yields
`l` distinct consecutive triples precisely when its least scalar period
is `l`, so the scalar and native triple clocks agree.

For lengths 1 and 2 the statements are immediate. The length-3 word
is constant only at `t=-2`. For F4, the two free parameters are exchanged
by a two-step rotation; its only shorter-period case is
`2t=a+1`, already in periods 1 or 2. The strict inequality selects one
of each pair and removes that shorter case.

F5 has prime length 5 and is never constant. When `t notin {0,-1}`,
the displayed occurrence of `-1` is unique. Equality of two cyclic words
therefore forces equality of their parameters. For `t=0,-1` the two
words are cyclic rotations of one another. This is the sole duplication,
removed by omitting `t=-1`. In particular, replacing `t` by `-1-t`
usually gives a *different*, reversed oriented cycle; these are both
retained. The exceptional length-5 word is at a different parameter.

For F6, `t!=0` excludes periods 1, 2 and 3. A three-step rotation sends
`t` to `-t`, and no other identification is possible, so `t>=1` is exact.
For F8, a four-step rotation sends `t` to `-t-2`; period 4 would require
`t=-1`. Once `t>=0`, positions carrying `-1` occur exactly four apart,
so this is the complete identification. Periods 1 or 2 would also imply
period 4. Its excluded value `t=-1` is already F4 at level 1.

For F12 with `m>=2`, the entries in positions 0, 1, 2 are `1,m,1`.
Period 1 or 2 is impossible because of the later `-1`; period 3 is
impossible by comparing positions 1 and 4; period 4 by comparing
positions 0 and 4; period 6 by comparing positions 1 and 7.
For `m=1` the word is `1,1,1,0,-1,-1,1,0,1,-1,-1,0`;
comparing positions 0/3, 0/4 and 1/7 excludes periods 3, 4 and 6,
and periods 1 and 2 are immediate. These exhaust the proper divisors
of 12. The level `m^2-m+2` increases strictly for `m>=1`, so two
different standard parameters cannot represent the same orbit.

The exceptional length-5 word is nonconstant; the length-9 word has
different entries in positions 0 and 3, so is not period 3 or 1.
Each reversed exceptional word is a cyclic rotation: for E5 it is
rotation by one, for E9 it is rotation by six. Thus the certificate
does not conceal additional reverse-oriented exceptions.
Different least periods cannot overlap, and the two length-5 rows use
different `a`. This establishes the disjointness of the table.

## Explicit numbers of cycles on any invariant level

Fix any integers `a,k`. Let `c_l(a,k)` count native oriented cycles of
least length `l` on `K_a=k`; all unlisted lengths have count zero.
The following rules involve only integer square tests and at most two
quadratic roots; no orbit search remains.

1. `c_1` is the number of integers `r` with
   `a=2r-r^2` and `k=r^2(2r-3)`.
   Test `r=1±sqrt(1-a)` when that square root is integral, deduplicating
   the two roots when it is zero.
2. Let `P` run over the **distinct integer roots** of
   `P^2+(a-3)P-k=0`. For each put `S=P+a`.
   Add one to `c_2` exactly when `S^2-4P` is a strictly positive
   integer square `h^2` and `h≡S (mod 2)`.
   This gives `u=(S-h)/2<v=(S+h)/2` and is valid even at `a=1`.
3. `c_3=1` exactly when `a` is even, `t=(a+4)/2!=-2`, and
   `k=8-(t-4)^2`; otherwise it is zero.
4. `c_4=1` exactly when `(a+1)(a-7)+4k` is a strictly positive
   integer square `h^2` with `h≡a+1 (mod 2)`; otherwise it is zero.
5. For `a=-1`, `c_5=1` if `k=0`, and `c_5=2` if `k>0` and
   `4k+1` is an integer square; otherwise this family contributes zero.
   Add one for `(a,k)=(-13,-64)`.
6. `c_6=1` exactly when `a=0` and `k` is a positive integer square.
7. `c_8=1` exactly when `a=-1` and `k-1` is a positive integer square.
8. `c_9=1` exactly when `(a,k)=(-2,-1)`.
9. `c_12=1` exactly when `a=0` and `4k-7` is a positive integer square.
   Since it is congruent to 1 modulo 4, its square root is automatically
   odd and gives `m=(1+sqrt(4k-7))/2>=1`.

All other counts in items 6–9 are zero. The two-root rule in item 2
follows from `a=S-P`, `k=P(S-3)=P(P+a-3)`; it does not lose the
factor-zero case in the simpler equation `(u-1)(v-1)=1-a`.
The invariant levels in the table follow by direct polynomial
substitution, not by a source-theorem import.

The level contains only finitely many integral periodic points:
the displayed formulas are finite for every `a,k`. Hence for every
integer `n>=1`, the exact ordinary fixed-point count is

`#Fix(T_a^n | K_a=k, Z^3) = sum_(l | n) l*c_l(a,k)`,

where only `l in {1,2,3,4,5,6,8,9,12}` contribute. The native-clock
Artin–Mazur zeta function of this integer level is the finite rational
product

`zeta_(a,k)(z) = product_l (1-z^l)^(-c_l(a,k))`.

There is no unrestricted all-level fixed-count zeta assertion: F4 gives
infinitely many four-periodic points when levels are not fixed.
These are dynamical cycle factors, not arithmetic Euler factors of an
elliptic curve or an L-function. Source arithmetic is distinct from
target arithmetic; `NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional.
