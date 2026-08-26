# Argument blueprint

```text
local relator holonomy
        |
        v
H-fixed edge labellings on a finite surface cover
        |
        | rooted spanning-tree gauge
        v
|K|^(index-1) * |Hom(surface group,K)|
        |
        +-------------------------+
        |                         |
  orientable family         nonorientable family
        |                         |
  sum d^(-2m)          sum nu^(n+2)d^(-n)
        |                         |
        +------------+------------+
                     |
         finite exponential moments
                     |
                     v
       |K| and multiplicities c_d^+,c_d^-,c_d^0
```

## Dependency order

1. The SFT definition precedes every counting statement.
2. The gauge lemma is independent of representation theory.
3. Cover topology is fixed before the surface homomorphism formulas are
   substituted.
4. Moment inversion uses only the two exact count laws.
5. `D_8/Q_8` is a corollary and a regression control, not a proof premise.

## Fragile points to audit

- Left shifts make fixed configurations constant on left cosets `H\Lambda`.
- The ordered relator product uses labels at successive right-generator
  endpoints.
- Based gauge has cardinality `|K|^(V-1)` and acts freely.
- `x_3 in H_n` is orientation reversing, so the first family is genuinely
  nonorientable for every `n`, including even `n`.
- In odd nonorientable moments the coefficient is
  `(c_d^+-c_d^-)/d`, not merely `c_d^+-c_d^-`.
- Indicator-zero representations disappear from every nonorientable moment
  but are recovered by subtracting the self-dual multiplicity from the total
  degree multiplicity.
