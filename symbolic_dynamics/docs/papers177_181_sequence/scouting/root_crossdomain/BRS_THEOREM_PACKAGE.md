# BRS theorem package — bilinear radial scaling

**Status:** `THEOREM SPIKE / OWNER AMBER / HOLD_EXTERNAL`.

Let `V=F_q^m` with the standard nondegenerate dot product and define

```text
Phi(u,v)=(c u,c v),       c=<u,v>.
```

Put `a_t=(3^t-1)/2`.  Bilinearity gives the exact iterate

```text
Phi^t(u,v)=(c^{a_t}u,c^{a_t}v),   <Phi^t(u,v)>=c^{3^t}.
```

Let `Q=q^{m-1}(q^m-1)` be the number of pairs on each nonzero dot-product
level and `Z=q^{2m-1}+q^m-q^{m-1}` the size of the null cone.

1. Zero is fixed and every other null pair has tail one.  For `c!=0` of
   multiplicative order `r=3^a s`, `(s,3)=1`, the tail is exactly `a` and the
   eventual period is `ord_{2s}(3)`.
2. For any nonzero target `(x,y)` with `d=<x,y>` and any `t>=1`, the number
   of `t`-step predecessors is the number of `3^t`-th roots of `d` in
   `F_q^*`: it is `gcd(3^t,q-1)` when `d` lies in the corresponding power
   subgroup and zero otherwise.  The zero target has exactly `Z`
   predecessors at every positive time; a nonzero null target has none.
3. If `q-1=3^A h`, `(h,3)=1`, then the nonzero-dot tail-`a` population is
   `2*3^{a-1}hQ` for `1<=a<=A`, while `hQ` nonzero-dot states are recurrent.
   Together with the null cone this gives every transient layer and the sharp
   maximum tail `max(1,A)`.
4. The image has
   `1+(q-1)Q/gcd(3,q-1)` states.  Nonzero image fibres are uniform of size
   `gcd(3,q-1)`, whereas zero has size `Z` and is the unique largest fibre.

Finite-field cyclicity, power-map root counts, and static bilinear level counts
are zero credit.  The retained claim is their exact lift to this polynomial
pair dynamics.  Any literal or conjugate owner kills the spike.
