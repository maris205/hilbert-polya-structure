# Cyclic equality-feedback dynamics at dyadic lengths

**Handle:** `CEF`  
**Decision after fresh independent gate:** `GREEN_OWNER_THIN`  
**External status:** `HOLD_EXTERNAL`

## Outcome first

Fix `q>=3` and a dyadic length `n=2^m>=4`.  On the full alphabet
`A_q={0,...,q-1}` define the cyclic equality-feedback map

```text
T_q(w)_i = 1{w_i=w_(i+1)},             i in Z/nZ.            (1)
```

The first update is genuinely `q`-ary and nonlinear; every later state is
binary.  The early exact signal is a clean interface between the colour-change
mask of a cyclic word and a single nilpotent cyclic-difference block.  It
gives a sharp `n+1` clock, exact depth CDF checkpoints, the complete image
staircase, and an every-target affine-code fibre formula.

The author verifier exhausts six `(n,q)` boxes, 74,355 words and all targets
at every audited time: `1,547,369` assertions, two byte-identical replays,
`STATUS PASS`.

## 1. Nonlinear-to-linear iterate

For a word `w`, let its binary change mask be

```text
c(w)_i=1{w_i != w_(i+1)}.
```

On `F_2^n` let `S` be cyclic shift and `D=I+S`.  Since the complement of a
binary word `b` is its deviation from the all-one word,

```text
T_q^t(w) = 1 + D^(t-1)c(w),                     t>=1.        (2)
```

In `F_2[x]/(x^n-1)`, dyadic `n` gives `x^n-1=(x+1)^n`, so `D^n=0` and

```text
dim ker D^j=j,              0<=j<=n.                         (3)
```

The all-one word is the sole recurrent point.  A nonconstant word has exact
depth

```text
1 + min{j:D^j c(w)=0};                                      (4)
```

all other constant words have depth one.  Thus every state is absorbed by
time `n+1`.

## 2. Exact depth laws and the sharp last layer

A fixed binary mask `c` with `r=|c|` is realized by exactly

```text
chi_q(c)=(q-1)^r+(-1)^r(q-1)                                (5)
```

cyclic `q`-ary words.  This includes `chi_q(0)=q` and automatically vanishes
for the impossible one-change masks.

Define the kernel weight enumerator

```text
W_(n,j)(a)=sum_(c in ker D^j) a^|c|,
C_(n,j)(q)=W_(n,j)(q-1)+(q-1)W_(n,j)(-1).                   (6)
```

Then `C_(n,j)(q)` is exactly the number of words of depth at most `j+1`.
Consequently

```text
N_0=1,   N_1=q-1,
N_(j+1)=C_(n,j)(q)-C_(n,j-1)(q),       1<=j<=n.             (7)
```

This is a full all-parameter depth census.  At every dyadic checkpoint
`j=2^r<n`, the kernel consists of `j` freely chosen bits repeated `n/j`
times, hence

```text
C_(n,j)(q)=(1+(q-1)^(n/j))^j+(q-1)2^j.                     (8)
```

Moreover `ker D^(n-1)` is the even-weight hyperplane.  The last layer is

```text
N_(n+1)
 = (q^n-(q-2)^n)/2 - (q-1)2^(n-1) > 0.                    (9)
```

Thus the height `n+1` is sharp, with its complete equality census rather
than merely one witness.

## 3. Images and every-target fibres

At time one the image is every binary word except the `n` targets whose
complement has weight one, so

```text
|im T_q|=2^n-n.                                             (10)
```

For `t>=2`, put `j=min(t-1,n)`.  Every coset of `ker D^j` contains a valid
change mask: if a representative is a forbidden unit vector, adding the
all-one kernel vector gives weight `n-1`.  Therefore

```text
im T_q^t = 1 + im D^j,             |im T_q^t|=2^(n-j).      (11)
```

For a binary target `y`, set `d=y+1` and introduce the affine weight
enumerator

```text
W_(j,d)(a)=sum_(c:D^j c=d) a^|c|.                           (12)
```

The exact every-target source fibre is

```text
|T_q^(-t)(y)|
 = W_(j,d)(q-1)+(q-1)W_(j,d)(-1),              t>=1,       (13)
```

with `j=t-1` capped at `n`; nonbinary targets have fibre zero.  Formula (12)
is explicit without enumeration through Fourier inversion:

```text
W_(j,d)(a)=2^(-n) sum_(lambda in F_2^n) (-1)^(lambda dot d)
 (1+a)^(n-|((D^j)^T lambda)|)
 (1-a)^|((D^j)^T lambda)|.                                 (14)
```

At `t=1`, (13) is exactly (5); at `t>=2`, support is equivalently
`D^(n-j)d=0`.  All post-absorption times and the all-one target are included.
The one-step fibre of the all-one target is exactly `q`, so the labelled
functional graph recovers the alphabet size; the sharp height then recovers
`n`.

## 4. Owner and internal ceiling

The additive/XNOR subsystem, nilpotent cyclic modules, linear-CA functional
graphs, cycle chromatic polynomial, and finite Fourier inversion receive zero
credit.  The only residual candidate package is their precise interface for
the literal `q`-ary equality feedback: change-mask multiplicities (5), sharp
full depth law (6)--(9), the exceptional time-one support, and the
target-resolved nonlinear-to-affine fibre atlas (13).

P98 owns a different reversible equal-block-sum recurrence and the general
finite-field repeated-root/fixed-cycle toolkit.  It does not supply the
nonlinear first image, colour-mask multiplicity, absorption layers or (13).
The killed AQN candidate quotients cyclic differences and rotates according
to their number; it neither feeds equality indicators back nor has a
nilpotent CA tail.  These separation claims require independent hostile
review.

A bounded search found direct sources for the entire binary additive/XNOR
tail, but no source stating the `q`-ary map (1) with the conjunction above.
This non-hit is not a novelty or priority claim.  `HOLD_EXTERNAL` remains.

## 4A. Post-hostile repair: two complete target-fibre spectra

The first hostile gate correctly objected that the generic affine Fourier sum
did not itself evaluate target dependence.  The following two special-time
theorems close that gap; neither is needed for the clock census.

At time (t=2), a target (y) occurs precisely when (d=y+\boldsymbol1)
has even weight.  The equation (Dc=d) has the complementary pair
\(\{c,c+\boldsymbol1\}\).  Define

\[
 \rho(d)=\min\{|c|,n-|c|\}\in\{0,\ldots,n/2\}.
\]

Then the complete target fibre spectrum is

\[
 |(T_q^2)^{-1}(y)|
  =(q-1)^{\rho(d)}+(q-1)^{n-\rho(d)}
       +2(q-1)(-1)^{\rho(d)}.                              \tag{15}
\]

For (0\le r<n/2), exactly \(\binom nr\) targets have class (r); at
\(r=n/2\), exactly \(\frac12\binom n{n/2}\) targets do.  Thus (15) is a
complete parameter-class spectrum, not a named affine enumerator.  Different
parameters can produce the same numerical fibre value (for example
`n=4,q=4,r=1,2`).  The ordinary numerical multiplicity of a value `v` is the
sum of the displayed class multiplicities over all `r` for which the
right-hand side of (15) equals `v`.

There is a second closed spectrum at (t=n/2+1).  Here
\(D^{n/2}=I+S^{n/2}\), so a feasible deviation is exactly
\(d=(u,u)\) with \(u\in\mathbb F_2^{n/2}\).  If (h=|u|), then

\[
 \begin{split}
 |(T_q^{n/2+1})^{-1}(\boldsymbol1+d)|
  ={}&\bigl(1+(q-1)^2\bigr)^{n/2-h}
        \bigl(2(q-1)\bigr)^h\\
    &+(q-1)2^{n/2}(-1)^h .                                \tag{16}
 \end{split}
\]

Exactly \(\binom{n/2}{h}\) targets have parameter (h).  This is again a
parameter-class spectrum: equal numerical values from different `h` classes
must be merged by summing their binomial multiplicities.  To prove (16),
pair coordinates (i,i+n/2): a zero bit of (u) forces equal mask bits and
contributes (1+a^2), while a one bit forces unequal bits and contributes
\(2a\); evaluate at (a=q-1) and (a=-1).  Equations (15)--(16) explicitly
classify target fibres by two different geometric statistics and expose the
endpoint parity correction.  They are the required repair, subject to a fresh
process-separated gate.

## 5. Exact evidence

Run

```bash
python3 docs/papers162_166_sequence/scouting/root_cyclic_equality_feedback/verify_scout.py
```

The script independently iterates (1), checks (2)--(4) on every word,
recounts every change mask by (5), tests all depth layers and dyadic CDFs,
compares every target fibre at every time with (13), and checks every value
and class multiplicity in (15)--(16).  Receipts are refreshed after V2 replay.

```text
assertions       1547369
verifier sha256  8f7673886b09cb2838845a75bf26f98fdf145a0f14f2f0b611b01ee7f26f5aa4
canonical sha256 270783de0d78e8b35bea6bd2f8b1eba6349089ffe43a5b3de6aac4165fdb3bd0
fresh replay 1   270783de0d78e8b35bea6bd2f8b1eba6349089ffe43a5b3de6aac4165fdb3bd0
fresh replay 2   270783de0d78e8b35bea6bd2f8b1eba6349089ffe43a5b3de6aac4165fdb3bd0
py_compile       PASS
```

## Author-side gate

```text
CEF       GREEN_OWNER_THIN
MATH      PASS_AUTHOR_EXACT
EXTERNAL  HOLD_EXTERNAL
```
