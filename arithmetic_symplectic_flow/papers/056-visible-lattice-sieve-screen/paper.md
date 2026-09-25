# Visible-lattice sieve hull: no nonzero full-periodic packet

**Paper ID:** `056-visible-lattice-sieve-screen`  
**Record ID:** `ASFS-SCOUT-20260914-40`  
**Status:** `2026-09-14; PRE-P0 STOP — SPATIAL FULL-PERIODICITY FAIL`  
**Route state:** No P0 or Route-A evaluation; Route B `NOT INVOKED`.

Let `V={(m,n) in Z^2:gcd(m,n)=1}` and let `X_V` be the closure of its translation orbit in `{0,1}^{Z^2}`. A site survives exactly when it belongs to no sublattice `p Z^2` for prime `p`. This is an endogenous prime-divisibility spatial symbol rule, but has no sequential, Henon, symplectic, roof, or analytic owner.

Call `x in X_V` fully periodic if a finite-index sublattice `L<=Z^2` fixes it.

## Theorem

**Theorem.** The only fully periodic point of `X_V` is `0^{Z^2}`.

**Proof.** Zero lies in the hull: given finite `B<=Z^2`, choose distinct primes `p_b` for `b in B`; coordinatewise CRT gives `t=-b mod p_b` for every `b`, so each `t+b` lies in `p_b Z^2` and is absent from `V`.

Let `x` be fixed by `L` and suppose `x_r=1`. Choose a prime `p` not dividing `[Z^2:L]`. The image of `L` modulo `p` is all `(Z/pZ)^2`. Take translations `t_j` of `V` converging to `x`, pass to a subsequence `t_j=c mod p`, and choose `ell in L` with `ell=-c-r mod p`. Every `t_j+r+ell` lies in `p Z^2`, hence has visible value zero. The limit gives `x_(r+ell)=0`, while `L`-periodicity gives `x_(r+ell)=x_r=1`, a contradiction. ∎

## Gate boundary

The natural finite-cell packet convention thus has only zero. This does not classify points periodic under one chosen translation, and does not identify this hull with a symplectic phase space or borrow a roof.

| Item | Status |
| --- | --- |
| spatial prime-symbolic source | exact control |
| P0/symplectic owner | absent |
| A1 full spatial packets | scoped FAIL |
| one-direction periodicity | `OPEN` |
| roof/repetition/zeta | `NOT EVALUATED` |

**Portfolio position: stop/fork.** A viable spatial candidate needs different endogenous recurrent packets plus a genuine sequential/Henon-to-symplectic owner chain; selecting finite cells here is not a repair.
