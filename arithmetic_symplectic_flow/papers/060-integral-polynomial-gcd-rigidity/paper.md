# Origin-fixed integral polynomial automorphisms cannot dynamically create primitivity

**Paper ID:** `060-integral-polynomial-gcd-rigidity`  
**Record ID:** `ASFS-METHOD-20260914-08`  
**Status:** `2026-09-14; METHOD THEOREM / PRE-P0 STOP RULE`  
**Route state:** No P0 or Route-A evaluation; Route B `NOT INVOKED`.

## Theorem

Let `F:R^2->R^2` be a polynomial automorphism with `F,F^{-1}` in `Z[x,y]^2` and `F(0)=0`. For an integer vector `v`, write `g(v)` for the positive gcd of its coordinates.

**Theorem.** `g(F(v))=g(v)` for every `v in Z^2`. Consequently every gcd stratum `V_d={v:g(v)=d}` is invariant.

**Proof.** If `d=g(v)`, each monomial in either component of `F` has positive total degree because `F(0)=0`; substituting coordinates divisible by `d` gives both output coordinates divisible by `d`. Thus `d` divides `g(F(v))`. Apply the same argument to `F^{-1}` and integer vector `F(v)` to obtain the reverse divisibility. ∎

If additionally `det DF=1`, the map is symplectic for `dx wedge dy`; this geometric condition changes neither divisibility argument.

## Candidate consequence

The result includes the nonlinear Hénon map in 059. Within this algebraic class, an analyst may call `V_1` primitive or visible, but the same map preserves `V_2`, every `V_d`, and every chosen union of them. The map therefore has no map-level rule distinguishing the prime-divisibility decoration from its controls. A proposed A0 mechanism based only on selecting `V_1` is static and fails ownership.

The conclusion is deliberately narrow. It does not prohibit a map in this class from possessing another, explicitly defined arithmetic mechanism, and it does not address maps with nonzero constants, nonintegral inverse, nonpolynomial arithmetic, or nonlinear carriers beyond the stated class.

**Portfolio position: fork.** Stop treating origin-fixed integral polynomial lifts of visible lattice points as new A0 candidates unless they add an independently internal arithmetic rule. Continue the breadth search outside this static-stratum class.
