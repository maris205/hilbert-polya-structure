# GDN final freeze contract — dihedral subgroup-normalizer dynamics

**Contract date:** 2026-09-02 UTC.  
**Literal system:** `H -> N_(D_(2n))(H)` on all subgroups, `n>=3`.  
**Decision:** `PASS_PAPER_SIZED_OWNER_THIN`.  
**External state:** `HOLD_EXTERNAL`.

Classical subgroup classification and the complete one-step odd/even
normalizer formula have direct owners and receive zero contribution credit.
The retained result is only their full dynamical synthesis: the iterated
forest, every-time target fibres, an iff graph signature, and arithmetic
non-identifiability.  This is an internal theorem ceiling, not a novelty,
priority, authorship, or release statement.

## Frozen theorem ceiling

Write

```text
D_(2n)=<r,s | r^n=s^2=1, srs=r^(-1)>,
R_d=<r^d>,
H_(d,j)=<r^d,r^j s>,  0<=j<d,
n=2^a m,  m odd.
```

The paper may prove exactly the following conjunction.

1. **Owned bridge, visibly subtracted:**
   `N(R_d)=D_(2n)` and
   `N(H_(d,j))=H_(d/gcd(d,2), j mod (d/gcd(d,2)))`.
2. **Complete iterated forest:** the dihedral states form `sigma(m)` full
   binary inverse trees of height `a`; every rotation subgroup is an extra
   depth-one source entering the distinguished root.  Thus
   `depth(R_d)=1`, `depth(H_(d,j))=v2(d)`, and
   `D_n(z)=sigma(m)+tau(n)z+sigma(m)sum_(k=1)^a 2^k z^k`.
3. **All-time images:** for `t>=1`,
   `|im N^t|=sigma(m)(2^(max(a-t,0)+1)-1)`.
4. **Every-target fibres:** rotations have empty positive-time fibres;
   a level-`k>=1` dihedral target has fibre `2^t` when `k+t<=a` and zero
   otherwise; a fixed root has fibre
   `2^(min(t,a)+1)-1`, plus `tau(n)` only at the distinguished root.
5. **Exact unlabelled-graph inverse:**
   two maps are graph-conjugate iff their signatures
   `(v2(n),sigma(odd(n)),tau(n))` agree.
6. **Sharp information loss:** the maps for polygon parameters 33 and 35 are
   conjugate although the ambient dihedral groups have different orders; the
   collision persists after multiplying both parameters by any common power
   of two.

## Mandatory proof repair and boundaries

- Signature necessity must recover
  `tau(n)=|V|-sigma(m)(2^(a+1)-1)`.  The invalid shortcut comparing the
  distinguished root with “other roots” is forbidden because `m=1` has only
  one root.
- The `a=0` versus `a=1` maximum-tail ambiguity must be separated by the
  predecessor structure when `n>=3`; no unstated use of `n=1,2`.
- Graph conjugacy is unlabelled functional-graph conjugacy, not group
  isomorphism or subgroup-lattice isomorphism.
- All `tau(n)` rotation leaves enter only `H_(1,0)=D_(2n)`.
- The 33/35 result must include a commuting bijection, not merely equal state
  counts.
- Enumeration is bounded falsification pressure, never an all-parameter proof
  or ownership certificate.

## Proof dependency and evidence seal

```text
owned subgroup carrier + owned parity-halving normalizer
    -> exact t-fold halving
    -> binary inverse forests
       -> depth polynomial, images, all-target fibres
       -> recover a and sigma(m)
       -> vertex remainder recovers tau(n)
       -> iff graph signature
       -> 33/35 and all common 2-power lifts.
```

The original literal replay covers 44 parameters and 29,590 assertions, with
profile SHA-256
`6eed12ce0c63f2d20f734ac1fa67634ce445140372dfc53e779a389de023b782`.
An independent normalizer/signature audit spans every `3<=n<=120`, 6,903
parameter pairs, and no false positive or false negative.  A separate
temporal/fibre scan records 55,799 passing assertions.  The full proof and
owner pressure are preserved in `GDN_FOCUSED_AUDIT.md`,
`GDN_INDEPENDENT_AUDIT.md`, and `../scouting/gdn/OWNER_SEARCH_LOG.md`.

