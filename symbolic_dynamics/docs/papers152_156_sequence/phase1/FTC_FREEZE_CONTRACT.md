# FTC final freeze contract — factorial-collapse skew dynamics

**Contract date:** 2026-09-02 UTC.  
**Literal system:** `T(x,y)=(x+1,xy)` on `F_p^2`, for odd primes `p`.  
**Decision:** `PASS_PAPER_SIZED_OWNER_THIN`.  
**External state:** `HOLD_EXTERNAL`.

This contract fixes the largest internally admissible theorem package.  The
coordinate-swapped map is an exact specialization of the triangular family of
Ostafe--Shparlinski.  The construction, family membership, rising-factorial
iterate, and generic finite-field/triangular-map language therefore receive
zero contribution credit.  The retained object is the conjunction below; no
novelty, priority, or release claim follows from this freeze.

## Frozen theorem ceiling

Put

```text
P_t(X)=product_(j=0)^(t-1)(X+j),
C_t(u)=product_(r=1)^t(u-r),
r_t=min(t,p).
```

The paper may prove exactly the following package.

1. **Iterate and collapse:**
   `T^t(x,y)=(x+t,yP_t(x))` and `T^p(x,y)=(x,0)`.
2. **Complete functional graph:** the axis is one `p`-cycle.  For each
   `a in F_p^*` there is one arm of length `p` entering `(1,0)`, with
   depth-`s` state
   `v_(a,s)=(1-s,a/[(-1)^(s-1)(s-1)!])`; its leaf is `(1,-a)`.
3. **Sharp temporal polynomial:**
   `p+(p-1)(z+...+z^p)`.
4. **All-time every-target fibres:** for target `(u,v)`, the unique possible
   source abscissa is `u-t`; the fibre has size one if `C_t(u)!=0`, size `p`
   if `C_t(u)=v=0`, and size zero if `C_t(u)=0` and `v!=0`.
5. **Images and inverse boundary:**
   `|im T^t|=p(p-r_t)+r_t`; the initial ordinate is identifiable exactly
   when `C_t(u)!=0`.
6. **Periodic data:** `#Fix(T^n)=p` exactly when `p|n`, there is one cycle of
   least period `p`, and `zeta_T(z)=1/(1-z^p)`.

The paper must be led by the progressive all-time inverse atlas and the
factorial collapse schedule, not by generic graph/zeta terminology already
occupied by P150.

## Required boundaries and controls

- The quantifier is odd **prime** `p`; no unproved prime-power extension.
- `P_p(X)=X^p-X` is a polynomial identity, while its vanishing is pointwise
  on `F_p`; those statements must not be conflated.
- Tail counts include the collapse transition.  Every off-axis orbit enters
  at `(1,0)`.
- Wilson's theorem gives the leaf sign `(1,-a)`, not `(1,a)`.
- For `t>=p`, every `C_t(u)` vanishes and the image is exactly the axis.
- The target counts `N_1=p(p-r_t)`, `N_p=r_t`, and `N_0=r_t(p-1)` must satisfy
  both target partition and source-mass conservation.
- Enumeration is exact falsification pressure, never proof or ownership
  evidence.

## Proof dependency and evidence seal

```text
literal triangular update
    -> induction for the rising-factorial iterate
    -> full-residue zero at time p
    -> first-zero schedule -> arms and temporal polynomial
    -> target equation v=y C_t(u)
       -> every-target fibres -> images and inverse boundary
    -> translation on the axis -> fixed iterates and zeta.
```

The deterministic verifier covers 25 odd primes through 101, 75,993 states,
and 18,942,551 assertions.  Its frozen profile SHA-256 is
`b44a7815c886a98409b5f56a0c26ce24f8644fa4f6b57a238d5a50d8a2d83810`.
The complete derivation, owner ledger, and collision analysis remain in
`FTC_FOCUSED_AUDIT.md` and `../scouting/ftc/OWNER_LOG.md`.

