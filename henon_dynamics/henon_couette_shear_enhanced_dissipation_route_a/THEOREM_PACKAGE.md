# Theorem package: exact Couette shear semigroup

Let `T=R/(2pi Z)` and let

```text
partial_t f + a y partial_x f = nu (partial_x^2+partial_y^2) f
```

on `L2(T x R)`, with `a in R`, `nu>=0`, and physical time `t>=0`. Freeze

```text
f_hat_k(eta)=integral_T integral_R f(x,y) exp(-i(kx+eta y)) dy dx/(2pi).
```

Then

```text
partial_t f_hat_k-a k partial_eta f_hat_k=-nu(k^2+eta^2)f_hat_k
```

and, for every `k,eta,t`,

```text
S_t f_hat_k(eta)
 = exp{-nu[k^2 t+t(eta+a k t/2)^2+a^2 k^2 t^3/12]}
   f_hat_k(eta+a k t).
```

## Consequences

1. The exact, sharp sector norm is

   ```text
   exp{-nu[k^2 t+a^2 k^2 t^3/12]}.
   ```

   Frequency translation is unitary, and the multiplier has essential
   supremum equal to the displayed value at the unique maximizing frequency
   `eta=-a k t/2`. If `nu*t>0`, this singleton is a null set, so no nonzero
   `L2` vector attains the operator norm; normalized packets localized in
   shrinking frequency intervals about that point approach it. If `nu*t=0`,
   the multiplier is identically one and the unitary evolution attains its
   norm on every nonzero vector.

2. Writing the exponent as `D_t(eta)`, direct expansion gives

   ```text
   D_t(eta)+D_s(eta+a k t)=D_(t+s)(eta),
   ```

   hence `S_t S_s=S_(t+s)`.

3. For `a!=0`, `nu>0`, and `k!=0`, the exact cubic scale is
   `(nu a^2 k^2)^(-1/3)` up to the displayed factor twelve. The ordinary
   heat term `nu k^2 t` remains present.

4. At `nu=0`, `S_t` is the unitary shear group and
   `f_k(y,t)=exp(-i a k t y)f_k(y,0)`. Nonzero modes mix weakly against
   integrable products but do not decay in `L2`.

5. At `a=0` the family is heat flow; at `k=0` it is one-dimensional heat;
   at `t=0` it is the identity.

6. If `nu>0`, `S_T f=f`, `T>0`, implies `f=0`. For `k!=0` use the strict
   sector contraction. For `k=0`, the equality multiplier is supported only
   at `eta=0`, a null set. If `nu=0` and `aT!=0`, Fourier translation makes
   every nonzero `k` component an `L2(R)` periodic function of `eta`, hence
   zero; precisely the streamwise means remain.

7. The `k=0` heat multiplier is a nonzero multiplication operator on the
   nonatomic space `L2(R)`, hence is noncompact. Therefore the full semigroup
   is noncompact and not trace class; no ordinary Fredholm determinant is
   available.

The inviscid same-clock unitary yields only `A4_FORMAL_HINT`. There is no
arithmetic origin or primitive orbit owner, so all earlier gates fail.

## Executable precision contract

All rational exponents remain exact. The producer evaluates only the
exponential multiplier and sector-norm fields at 100 working decimal digits
and serializes each of those 1,350 fields to 82 significant digits. The
checker and SymPy path lock both numbers and the serialized digit count.
