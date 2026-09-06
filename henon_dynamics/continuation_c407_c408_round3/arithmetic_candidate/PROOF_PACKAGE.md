# Thin Cantor orbit-limit sets for hyperbolic FAD systems

Status: complete proof admitted as C407 for manuscript development after
independent internal checking; not a finalized release or human peer-reviewed
paper. Date: 2026-09-06. The attribution clarification below changes no
mathematical statement or proof step in the reviewed snapshot.

## 1. Scope and main statement

Fix a finite set `S` of primes, a real `Lambda>1`, and a positive periodic
sequence `(r_n)`. For each `p in S`, let `(s_{p,n})` and `(t_{p,n})` be
periodic sequences taking nonnegative real values, with a common period
`m_p` coprime to `p`. Let `w` be any common period of all these sequences.
Allow negative indices by periodic extension. Remove a prime from `S` if
both of its exponent sequences are identically zero, and write `d=|S|`.

For `s,t>=0`, define the continuous radial kernel on `Z_p`

`H_{p;s,t}(z) = p^(-s v_p(z)-t p^(v_p(z)))` for `z != 0`.

At zero set `H(0)=0` if `(s,t)!=(0,0)` and `H(0)=1` otherwise. In particular
`H_{p;0,0}` is the constant one function. All kernels take values in `[0,1]`.

Let

`D = closure{(n mod w,(n)_{p in S}): n in Z}
      subset (Z/wZ) x product_{p in S} Z_p`.

For `(a,x) in D`, put

`Phi(a,x) = sum_{l>=0} Lambda^(-l) r_{a-l}
              product_{p in S} H_{p;s_{p,a-l},t_{p,a-l}}(x_p-l)`.  (1)

The series converges uniformly, so `Phi` is continuous. The exponent data
have finite range, but no lower bound on a nonzero exponent uniform across
different systems is assumed or needed.

**Theorem 1 (quantitative image theorem).** For the fixed data above:

1. If `d=0`, then `Phi(D)` is the finite set
   `{(sum_{l=0}^{w-1} r_{a-l} Lambda^(-l))/(1-Lambda^(-w)):
   a in Z/wZ}`.
2. If `d>0`, `Phi(D)` is a nonempty compact perfect nowhere dense subset of
   `R`, hence a Cantor set.
3. For `d>0`, there are constants `C,epsilon_0>0`, depending only on the
   fixed data, such that its covering number by real intervals of length
   `epsilon` satisfies
   `N_epsilon(Phi(D)) <= C (1+log(1/epsilon))^(2d)` for
   `0<epsilon<epsilon_0`. Consequently its upper box and Hausdorff dimensions
   are zero.

The positive periodic sequence need not be a gcd sequence for this theorem.
The coprime-period assumption on the exponent sequences is used for the
perfectness assertion, not for the covering bound.

**Corollary 2 (hyperbolic FAD orbit counting).** Let `(X,f)` be a FAD system
of positive entropy, hyperbolic in BCH Definition 10.3.9. For
`Pi_f(N)=N pi_f(N)/Lambda^N`, its accumulation set `L_f` has precisely the
description in Theorem 1. In particular every genuinely distorted such
system has a zero-upper-box-dimensional Cantor accumulation set, including
arbitrary finite sets of distortion primes and nonzero wild exponent
sequences.

Proof of the corollary from Theorem 1: BCH Theorem 12.4.3(ii) identifies
`L_f` with the image of its detector function, equation (12.4). In the
hyperbolic case BCH explicitly prove `u=1`; the dominant root is positive
and unique, so the archimedean phase coordinate is trivial. Their detector
function is exactly (1), and their FAD hypotheses are stronger than the
periodicity hypotheses here. No assertion about general nonhyperbolic
detector images is used. QED, conditional only on Theorem 1 below and the
stated, already proved BCH input.

## 2. Adaptive valuation partitions

**Lemma 3.** Let `p` be prime and let `E` be a set of at most `L` integer
centers in `Z_p`. For an integer `K>=1`, there is a finite clopen partition
of `Z_p` into at most `1+(p-1)LK` atoms such that every function
`z -> min(v_p(z-e),K)`, `e in E`, is constant on every atom.

Proof. Start with the root ball `Z_p`. At depths `j=0,...,K-1`, split a
current ball of depth `j` into its `p` children if it contains a center of
`E`. At each depth there are at most `L` balls containing centers, hence
at most `LK` splits in all; each split adds `p-1` leaves. The leaves are a
clopen partition with the claimed count. If a leaf has depth below `K`,
it contains no center, so the valuation to every center is constant on it.
On a depth-`K` leaf each truncated valuation is constant as well. QED.

**Lemma 4 (uniform tail control in valuation).** For each fixed prime and
the finite list of exponent pairs occurring in (1), constants `c_p>0`
exist such that, for every active pair and every integer `K>=1`,

`sup_{v_p(z)>=K} H_{p;s,t}(z) <= exp(-c_p K)`.

Proof. For a pair with `s>0`, take the bound `p^(-sK)`. For a pair with
`s=0,t>0`, use `p^(-t p^K) <= p^(-t K)`. Take `c_p` to be the minimum
of the finitely many positive constants `s log p` or `t log p` so obtained.
The convention at zero obeys the same bound. QED.

**Proof of the covering part of Theorem 1.** Write `R=max r_n` and
`B=R/(1-Lambda^(-1))`. Fix `0<epsilon<1`. Choose

`L=ceil(log(8B/epsilon)/log Lambda)`, enlarged to at least one,

so that the tail of (1), starting at `l=L`, is at most `epsilon/8`.
Choose for every active prime

`K_p=max(1,ceil(log(8dB/epsilon)/c_p))`.

Apply Lemma 3 to centers `E={0,...,L-1}` and depth `K_p` in each
coordinate. If two points are in the same product atom, then for any
`l<L` and any coordinate either their valuations at center `l` agree
below `K_p`, or both are at least `K_p`. In the first case the associated
kernel values agree. In the second case an inactive kernel is constant
one; for an active kernel the two values both belong to
`[0,epsilon/(8dB)]`, by Lemma 4. Thus their difference is bounded by that
quantity in every case.

For numbers in `[0,1]`, telescoping products gives
`|product u_p - product v_p| <= sum_p |u_p-v_p|`.
For a fixed finite residue `a`, the variation of the first `L` summands
of (1) on one product atom is therefore at most `epsilon/8`; the
variation of the two tails is at most `epsilon/4`. Its image has diameter
less than `epsilon`, and is covered by one interval of length `epsilon`.
Restricting atoms to `D` can only remove empty atoms. Their total number
is at most

`w product_{p in S}(1+(p-1)LK_p)
   <= C (1+log(1/epsilon))^(2d)`.

The standard definition
`upperdim_B E = limsup_{epsilon->0} log N_epsilon(E)/log(1/epsilon)`
now gives zero. An interval has positive upper box dimension, so the
compact image contains no nondegenerate interval and is nowhere dense.
The same covers give zero Hausdorff dimension directly: for every `alpha>0`,
`N_epsilon(E) epsilon^alpha -> 0`. QED.

## 3. Positive radial sums cannot be locally constant

This section supplies a new nonconstancy proof, without importing an
injectivity claim or an integrality restriction from BCH Lemma 12.5.4.

For a prime `p`, use Haar probability measure `dz` on `Z_p` and the
character `chi_k(z)=exp(2 pi i (z mod p^k)/p^k)`, of conductor `p^k`,
where `k>=1` and the representative modulo `p^k` lies in `[0,p^k)`.
For every fixed integer `j`, `chi_k(j)->1` as `k->infinity`.

**Lemma 5 (radial Fourier coefficients).** For an active pair `(s,t)`, put
`h(v)=p^(-sv-t p^v)`, `v>=0`, and

`A_{s,t}(k)=sum_{j>=k} p^(-j)(h(j-1)-h(j))`.

Then `A_{s,t}(k)>0`, and

`integral H_{p;s,t}(z) conjugate(chi_k(z)) dz = -A_{s,t}(k)`.  (2)

For `t=0,s>0`,

`A_{s,0}(k) = (p^s-1) p^(-(s+1)k)/(1-p^(-(s+1)))`.  (3)

For `t>0,s>=0`,

`A_{s,t}(k) ~ p^(-k-s(k-1)-t p^(k-1))`.  (4)

Proof. Since `h(v)` decreases strictly to zero, writing
`delta_j=h(j-1)-h(j)>0` gives the uniformly convergent expansion

`H(z)=h(0)-sum_{j>=1} delta_j 1_{p^j Z_p}(z)`.

The Fourier integral of the indicator is zero for `j<k` and is `p^(-j)`
for `j>=k`, which proves (2). For `t=0`, summing the resulting geometric
series gives (3). For `t>0`, the first term in `A` divided by
`p^(-k)h(k-1)` tends to one, because
`h(k)/h(k-1)=p^(-s-t(p-1)p^(k-1))->0`. The remaining terms are bounded by

`sum_{j>=k+1} p^(-j)h(j-1)
 <= p^(-k-1)h(k)/(1-p^(-1))`,

which is negligible relative to `p^(-k)h(k-1)`. This proves (4). QED.

**Lemma 6 (positive radial series).** Let `T` be a finite set of active
pairs `(s,t)` of nonnegative real numbers. Let integers `j_i`, types
`theta_i in T`, and positive real coefficients `b_i` be indexed by a
nonempty finite or countable set, with `sum_i b_i<infinity`. Then

`F(z)=sum_i b_i H_{p;theta_i}(z-j_i)`

is not constant on `Z_p`.

Proof. Choose `theta_*=(s_*,t_*)` among the types actually present by first
minimizing `t`, then minimizing `s`. Formulas (3)–(4) imply

`A_theta(k)/A_theta_*(k) -> 1` if `theta=theta_*`, and `->0` otherwise.

All ratios are bounded uniformly in `k>=1` and in the finite set of types:
each ratio converges and each denominator is positive. By (2), absolute
summability, and dominated convergence,

`hat F(chi_k)/A_theta_*(k)
 = -sum_i b_i conjugate(chi_k(j_i)) A_theta_i(k)/A_theta_*(k)
 -> -sum_{i:theta_i=theta_*} b_i < 0`.

The precise convention for the translation character changes only the
complex conjugate, not the limit. Consequently nontrivial Fourier
coefficients of `F` are nonzero for all sufficiently large `k`; a constant
function has zero integral against every nontrivial character. QED.

**Lemma 7 (local form).** Let a uniformly convergent positive weighted
sum of radial kernels have integer centers `l>=0`, finite exponent types,
and summable positive coefficients. On a ball `a+p^K Z_p`, with
`0<=a<p^K`, suppose at least one center in that ball has an active type.
Then the sum is nonconstant on that ball.

Proof. A center outside the ball has constant distance from the ball and
contributes a constant. An inactive center also contributes a constant.
For an active center in the ball write `l=a+p^K j`, where `j>=0`, and
write `z=a+p^K y`. Then

`H_{p;s,t}(z-l) = p^(-sK) H_{p;s,t p^K}(y-j)`.

The transformed types still form a finite active set; the positive
coefficients remain summable, since `p^(-sK)<=1`. Lemma 6 applies to the
nonempty active part. QED.

## 4. Every detector cylinder has nonconstant image

BCH already uses a negative ordinary integer in the other coordinates in
the proof of Theorem 12.5.1 (printed pp. 132–133). That slice choice is
classical input here. The additional argument applies Lemmas 6–7 on every
detector cylinder, rather than merely finding a slice with continuum image.

**Lemma 8 (detector group).** With `v_p(w)=nu_p`,

`D = {(a,x): x_p == a mod p^(nu_p) for every p in S}`.  (5)

Proof. The congruences hold on all diagonal integer points and hence on
their closure. Conversely, prescribing `a mod w` and any compatible
finite list `x_p mod p^(K_p)` is one solvable CRT system. An arithmetic
progression supplies integers in every such neighborhood. QED.

Every nonempty relative open subset of `D` therefore contains a product
cylinder

`U={a} x product_{p in S}(b_p+p^(K_p) Z_p)`,

with `K_p>=nu_p` and `b_p==a mod p^(nu_p)`. Increase depths if needed and
use the canonical representatives `0<=b_p<p^(K_p)`.

Fix any active prime `p_0`. For every other prime `q`, choose a negative
ordinary integer `m_q` in its prescribed ball; this is possible by
subtracting a sufficiently large multiple of `q^(K_q)`. Hold these
coordinates fixed and vary only `x_{p_0}`. On that slice, (1) becomes

`sum_{l>=0} c_l H_{p_0;s_{p_0,a-l},t_{p_0,a-l}}(x_{p_0}-l)`,

where

`c_l=Lambda^(-l) r_{a-l}
       product_{q!=p_0} H_{q;s_{q,a-l},t_{q,a-l}}(m_q-l)`.

Each `c_l` is strictly positive: `m_q<0<=l`, so no argument of a kernel
is zero. Also `c_l<=R Lambda^(-l)`, so these coefficients are summable.

Since `p_0` is active, some residue `n_0 mod m_{p_0}` has a nonzero
exponent pair. Because `gcd(m_{p_0},p_0)=1`, CRT supplies `l>=0` satisfying

`l == b_{p_0} mod p_0^(K_{p_0})` and
`a-l == n_0 mod m_{p_0}`.

Thus there is an active center inside the varying coordinate ball.
Lemma 7 proves nonconstancy on the slice, and consequently on `U`.
This proves that `Phi` is nowhere locally constant on `D` when `d>0`.

If a value `y` were an isolated point of `Phi(D)`, the nonempty preimage
`Phi^(-1)({y})` would be open in `D`, contradicting the preceding paragraph.
Thus the image is perfect. It is compact and nonempty by continuity and
compactness. The covering proof shows that it contains no interval; a
subset of `R` with no nondegenerate interval is totally disconnected.
The standard Cantor-space characterization now completes Theorem 1.
For `d=0`, summation by residues proves the finite formula directly. QED.

## 5. Scope checks and nonclaims

- A continuous image of a Cantor set need not be a Cantor set. That invalid
  shortcut is not used: Section 2 excludes intervals, while Sections 3–4
  independently exclude isolated image values.
- Zero Hausdorff dimension alone does not imply perfectness; it is not
  used in place of the Fourier lemma.
- No global or local injectivity of `Phi` is claimed.
- No nonatomicity of the pushforward Haar distribution is claimed.
- Positivity matters in Lemma 6. The proof does not apply unchanged to
  signed or complex periodic orbit weights.
- Finiteness of `S` is essential to the finite-product covering bound.
- If exponent periods divisible by their own prime are allowed, some
  cylinders may contain no active center; perfectness is not asserted in
  that wider class. The covering estimate still holds.
- No continuous archimedean phase factor is allowed in Theorem 1. General
  nonhyperbolic FAD systems may have interval images, as BCH prove.
- No sharp logarithmic covering exponent, positive Hausdorff gauge measure,
  or explicit homeomorphism of `L_f` with `Z_p` is claimed.
- Classical fixed-point counts and the detector representation are inputs,
  not new contributions. The candidate contribution is the quantitative
  geometry and perfectness of the full hyperbolic detector image.

## 6. Exact primary-source dependency map

Primary source: J. Byszewski, G. Cornelissen, M. Houben, *Dynamics of
endomorphisms of algebraic groups*, arXiv:2209.00085v2 (19 April 2024),
https://arxiv.org/abs/2209.00085 and https://arxiv.org/pdf/2209.00085v2.

The browser-rendered original PDF, not a secondary summary, was inspected
at Definition 7.1.1–7.1.2; Definition 10.3.9; the text preceding Theorem
12.4.3; equation (12.4) and Theorem 12.4.3; Theorem 12.5.2 and Remark
12.5.3; Lemma 12.5.4 and its proof; and Problem 14.1.1.

Their Theorem 12.5.2(ii) treats one prime with no wild term and gives a
finite-set/Cantor-set union. Their Remark 12.5.3 and Problem 14.1.1 leave
the additional hyperbolic regimes in question. Our covering/Fourier
argument is not a use of their one-prime injectivity conclusion outside
its scope. In particular the real-exponent case is proved here directly.

The bounded later-source audit is in `SOURCE_AUDIT.md`. Independent review
found no mathematical blocker in this proof or its 2024 source reduction.
Neither check certifies that no post-April-2024 solution or updated final
book treatment exists.
