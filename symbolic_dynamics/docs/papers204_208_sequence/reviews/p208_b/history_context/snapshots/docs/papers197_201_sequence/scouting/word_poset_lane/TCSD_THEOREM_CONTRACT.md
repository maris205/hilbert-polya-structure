# TCSD theorem contract

Status: `PROMOTE_SPIKE / OWNER_AMBER / HOLD_EXTERNAL`.

This is a candidate contract, not a novelty, priority, authorship, venue, or
release claim.  Generic cellular-automaton, subshift, transfer-matrix, and
Möbius-inversion machinery receives zero contribution credit.

## 1. Literal map and boundary conventions

Fix `n>=1`, index coordinates by `Z/nZ`, and put

```text
X_n={-1,0,1}^{Z/nZ},
D(x)_i=sgn(x_(i+1)-x_i),
sgn(z)=-1,0,1 according as z<0,z=0,z>0.
```

All comparisons use the old word.  Let `rho` be left cyclic shift,
`rho(x)_i=x_(i+1)`.  This orientation is frozen.  At `n=1`, all three input
letters map to `0`; the unique recurrent state is `0` and the maximum tail is
one.

For a finite open word `w=w_0...w_r`, write `delta(w)_i` for the same sign
difference without wraparound.  Thus `delta^t(w)` has length `r+1-t`.

## 2. Recurrent core and pointwise clock

Define the five-block subshift

```text
K_n={x in X_n : D^4(x)=rho^2(x)}.                    (2.1)
```

### Theorem A: exact core and sharp attraction

For every `n>=1`:

1. `K_n` is exactly the recurrent set of `D`.
2. On `K_n`, `D` is bijective with explicit inverse
   `D^{-1}=rho^{-2}D^3`.
3. The pointwise tail is

   ```text
   tau(x)=min{t>=0 : D^(t+4)(x)=rho^2 D^t(x)}.        (2.2)
   ```

4. If `x` is nonconstant and `R(x)` is its longest cyclic constant run, then
   `tau(x)<=R(x)`.
5. The sharp maximum is

   ```text
   H_1=1;
   H_n=n-1,  n even;
   H_n=n-2,  n odd and n>=3.                          (2.3)
   ```

The proof is short once the finite local lemma in
`TCSD_LOCAL_CERTIFICATE.md` is isolated.  A zero-run of `D(x)` comes from an
equal-letter run of `x`, while a `+`-run or `-`-run comes from a strict chain
in the three-element alphabet.  Hence, for a nonconstant word,

```text
R(Dx) <= max(R(x)-1,2).                               (2.4)
```

If `R(x)=1`, a length-six local check gives `D(x) in K_n`.  If `R(x)<=2`,
the certified length-seven identity

```text
delta^6(w)_0=delta^2(w_2w_3w_4)_0                    (2.5)
```

gives `D^2(x) in K_n`.  Iterating (2.4) proves `tau(x)<=R(x)`.
Equation (2.1) is forward invariant because `D` commutes with `rho`; its
displayed inverse proves recurrence.  Since every orbit enters `K_n`, a
recurrent point cannot lie outside it.

For sharpness take a word with one exceptional letter,
`x=a^(n-1)b`, `a!=b`, and let `s=sgn(b-a)`.  Up to rotation,

```text
D(x)=0^(n-2) s (-s),
D(0^r Alt_l(s))=0^(r-1) Alt_(l+1)(s),                (2.6)
```

as long as `r>=1`, where `Alt_l(s)=s,-s,s,...`.  For even `n` this reaches
the full alternating recurrent word after exactly `n-1` steps.  For odd `n`
it reaches the recurrent word `0 Alt_(n-1)(s)` after exactly `n-2` steps.
Indeed a full even alternating word satisfies `D(y)=-y` and `rho^2y=y`.
A direct four-phase junction calculation gives the sharper test

```text
0^r Alt_l(s) lies in K  iff  r=0, or r=1 and l is even. (2.7)
```

Along (2.6), all preceding phases have `r>=2`; at even length the `r=1`
phase has odd `l` as well.  Thus none enters `K` early, while the `r=0`
even-length word and the odd-length `r=1,l=n-1` word do enter.  This proves
that the displayed entrance times are exact, rather than merely giving upper
bounds.
The upper bound follows from (2.4); the only case not already bounded by
`R<=n-2` is `R=n-1`, which is precisely the one-exception form just computed.

## 3. Exact depth enumerator

For `t>=0`, let `A_t` be the zero-one de Bruijn matrix whose vertices are
words of length `t+4` over `{-1,0,1}`.  There is an edge from
`u_0...u_(t+3)` to `u_1...u_(t+4)` precisely when their overlap agrees and
the combined block `w=u_0...u_(t+4)` satisfies

```text
delta^(t+4)(w)_0 = delta^t(w_2...w_(t+2))_0.         (3.1)
```

Then, for every `n,t`, including wraparound and small-period coincidences,

```text
#{x in X_n : tau(x)<=t}=tr(A_t^n),                   (3.2)
#{x in X_n : tau(x)=t}=tr(A_t^n)-tr(A_(t-1)^n),      (3.3)
```

where the second term is zero at `t=0`.  This is an exact all-parameter
depth enumerator, not a finite-data extrapolation.  The matrix can be
minimized after the theorem is secured; the unreduced form keeps the local
meaning transparent.

For `t=0`, exactly 165 of the 243 length-five blocks are allowed.  The
81-state matrix `A_0` has nonzero characteristic factor

```text
(z-1)(z^3-z^2-2z-1)(z^3+z^2+2z+1).                  (3.4)
```

Consequently, if `R_n=|K_n|`, then

```text
R_1,...,R_7 = 1,3,13,27,41,93,225,
R_n = R_(n-1)+R_(n-2)+3R_(n-3)+2R_(n-4)
      -2R_(n-5)-3R_(n-6)-R_(n-7).                   (3.5)
```

## 4. Periods and exact cycle census

On `K_n`, (2.1) gives

```text
D^(4n/gcd(n,2))=id.                                  (4.1)
```

Thus every period divides `4n/gcd(n,2)`.  This is only a period bound, not a
claim that every divisor occurs.

There is also an exact census.  For `p>=1`, form the de Bruijn matrix `C_p`
on length-`p` words, allowing the edge associated with a length-`p+1` block
`w` exactly when

```text
delta^p(w)_0=w_0.                                    (4.2)
```

Then

```text
Fix_n(D^p)=tr(C_p^n),
Per_n(p)=sum_(d|p) mu(p/d) Fix_n(D^d),
Cycles_n(p)=Per_n(p)/p.                              (4.3)
```

Equations (4.1)--(4.3) separate the complete cycle census from the depth
enumerator.  In the exhaustive boxes the observed period sets are

```text
n=3:  1,12                 n=8:  1,2,8,16
n=4:  1,2,8                n=9:  1,12,36
n=5:  1,20                 n=10: 1,2,5,10,20
n=6:  1,2,3,12             n=11: 1,44
n=7:  1,28                 n=12: 1,2,3,8,12,24.
```

## 5. Every labelled one-step fibre

Index rows and columns by `-1,0,1` and define

```text
M_-(a,b)=1{b<a},   M_0(a,b)=1{b=a},   M_+(a,b)=1{b>a}. (5.1)
```

Thus `M_-` is strict lower triangular, `M_0=I`, and `M_+` is strict upper
triangular.  For every labelled target `y=y_0...y_(n-1)`, including targets
outside the image,

```text
|D^{-1}(y)|=tr(M_(y_0) ... M_(y_(n-1))).             (5.2)
```

This counts closed three-level walks with the prescribed comparisons and is
independent of the forward run proof.

Deleting the zero symbols of `y` gives its strict-sign skeleton.  The target
is in the image precisely when either it is all zero, or the cyclic skeleton
contains both signs and has no sign-run of length three.  Equality edges may
be contracted without changing (5.2).

### Theorem B: sharp fibre maximum and all maximizers

For `n>=2`,

```text
max_y |D^{-1}(y)| = L_(2 floor(n/2)),                 (5.3)
```

where `L_j` is the Lucas sequence (`L_0=2,L_1=1`).  For even `n>=4`, the
only maximizers are the two alternating sign words.  For odd `n>=5`, they
are the `2n` targets with exactly one zero and alternating remaining signs.
At `n=2`, the two alternating targets and `00` tie; at `n=3`, the six
one-zero alternating targets and `000` tie.

For a fixed number `r` of strict signs, the rank-one/Fibonacci matrix normal
form proved in `TCSD_FIBRE_CERTIFICATE.md` gives

```text
max over strict skeletons = L_r     if r is even,
                            F_(r-1) if r is odd.       (5.4)
```

In the even case equality forces alternation.  For odd `r>=3` it forces
exactly one doubled sign-run; at `r=1` both formal one-sign skeletons have
the zero maximum and lie outside the image.  Moreover

```text
tr((M_+M_-)^m)=tr([[2,1],[1,1]]^m)=L_(2m).           (5.5)
```

Comparing (5.4) over `0<=r<=n`, with the all-zero fibre three handled
separately, proves (5.3) and the stated equality cases.

## 6. Exact evidence and claim boundary

The small boundary boxes, which must not be hidden inside an asymptotic
formula, are

| `n` | image | recurrent | max tail | periods | max fibre / maximizers |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 | 1 | 3 / 1 |
| 2 | 3 | 3 | 1 | 1,2 | 3 / 3 |
| 3 | 13 | 13 | 1 | 1,12 | 3 / 7 |

In particular, the `n=1` tail exception and the `n=2,3` fibre ties are part
of the theorem statement.

Fresh enumeration covers every one of the `3^n` states for `1<=n<=12`.
The final five boxes are:

| `n` | states | image | recurrent | max tail | max fibre |
|---:|---:|---:|---:|---:|---:|
| 8 | 6,561 | 2,203 | 459 | 7 | 47 |
| 9 | 19,683 | 5,773 | 949 | 7 | 47 |
| 10 | 59,049 | 15,123 | 2,093 | 9 | 123 |
| 11 | 177,147 | 39,601 | 4,533 | 9 | 123 |
| 12 | 531,441 | 103,681 | 9,621 | 11 | 322 |

The verifier checks 3,238,990 exact assertions.  Two fresh processes produce
the byte-identical output hash
`2b47662aaeab35569a9720896846537c58e040a4b82b9197c4a8b698e7479132`.

The literal map and theorem package still require an external owner search.
Nothing here converts a bounded internal non-collision into originality.
There is one exact internal factor which must be disclosed: on the `q=3`
front of P164,

```text
1{x_i=x_(i+1)}=1{D(x)_i=0}.
```

The separation claim is only that this projection does not retain TCSD's
oriented recurrent core, clock, or Lucas equality cases; it is not a claim
that no factor relation whatsoever exists.  Equations (3.2)--(3.3) and
(4.3) are exact finite-matrix enumerators whose dimensions grow with time,
not efficient fixed-size closed forms or a simple classification of which
period divisors occur.  Equation (5.2) is a one-step every-target theorem;
no all-time every-target fibre atlas is claimed.
