# Official Experiment Results

**Candidate:** `cat_centralizer_cyclic_torsor_v1`  
**Date:** 2026-08-15 UTC  
**Evidence role:** exact finite falsification and implementation control; not
an empirical or all-$q$ proof.

## Registered lifecycle

- Source lock SHA-256:
  `aa99218099f2e2c3e14367bfe75f9da881d8b204689c07c6fa963f9582b696e2`.
- Independent source review SHA-256:
  `a551784d205d9ef52ce6a493ab66cb7295a4a9dadbeb8bb2353fc58e3011dff5`.
- Reviewed execution tree SHA-256:
  `87b08f11fc67eae47bdf745f8286700376f3debc5ac3fd190075a5fa2632f436`.
- Pre-execution JUnit SHA-256:
  `5a5b82c5aaed3dd5aca2c180bd4d1bf589e3b9a8ae4cc3dc9bf30cb04787227b`
  (`12/12` passing).
- Independent two-round code review SHA-256:
  `990b1762e2aea6c379288854cca918cc4bbe87b7ea7ccadef7458ecfcf6988f0`.
  Its byte-exact Round-1 failure prefix is preserved; Round 2 issued the
  hash-bound `DEPLOYMENT_PASS` after the hollow-row semantic gate was fixed.
- Authorized pre-execution audit SHA-256:
  `d0aea91f5a95797f3edfcb5b30d49c50f18a16dd20cde1a44b58fe32c6f9cc99`.
- Durable registered claim SHA-256:
  `48d767edd9e3dc8f67ba1563ec03d50ef53983447263d0ce8857cfd7ff3326da`.
- Raw official result SHA-256:
  `8dceb1b8a63db462c1fd55a242ea35de974f73b6c80da68517b91c9eebb214ff`.
- Certified terminal SHA-256:
  `6cebc4224d3f275edc2ee6a847f1f7ba71d2f7793959281bcfe853fdb708ffe3`.
- Post-run JUnit SHA-256:
  `c0124c04106ba81c12ad89814e1547d6e16d3f7eb1f9864d21ec0178ca7e8195`
  (`12/12` passing).

Exactly one registered audit was claimed and completed.  No registered
rerun was performed.

## Raw exact ledger

| $q$ | type | $|E_q|$ | $|\mathrm{CV}_q|$ | discard | $|C_q|$ | $|C_q^1|$ | $\operatorname{ord}_q(A)$ | cyclic $A$-orbits | $\mathrm{CV}_q/C_q$ | $\mathrm{CV}_q/C_q^1$ | $E_q/C_q$ | $E_q/C_q^1$ | prime reversing shell orbits |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | binary inert | 3 | 3 | 0 | 3 | 3 | 3 | 1 | 1 | 1 | 1 | 1 | 1 |
| 3 | inert | 8 | 8 | 0 | 8 | 4 | 4 | 2 | 1 | 2 | 1 | 2 | 1 |
| 5 | ramified | 24 | 20 | 4 | 20 | 10 | 10 | 2 | 1 | 2 | 2 | 4 | 2 |
| 7 | inert | 48 | 48 | 0 | 48 | 8 | 8 | 6 | 1 | 6 | 1 | 6 | 1 |
| 11 | split | 120 | 100 | 20 | 100 | 10 | 5 | 20 | 1 | 10 | 3 | 12 | 2 |
| 4 | binary inert lift | 12 | 12 | 0 | 12 | 6 | 3 | 4 | 1 | 2 | 1 | 2 | -- |
| 6 | binary/inert CRT | 24 | 24 | 0 | 24 | 12 | 12 | 2 | 1 | 2 | 1 | 2 | -- |
| 9 | inert lift | 72 | 72 | 0 | 72 | 12 | 12 | 6 | 1 | 6 | 1 | 6 | -- |
| 10 | binary/ramified CRT | 72 | 60 | 12 | 60 | 30 | 30 | 2 | 1 | 2 | 2 | 4 | -- |

Every row passed all of the following exact comparisons:

1. brute-force matrix commutant versus the independent $aI+bA$ algebra;
2. invertible commutant versus algebra units;
3. determinant-one centralizer versus the norm-one subgroup;
4. direct cyclic determinant locus versus the torsor image of $e_1$;
5. matrix determinant versus $a^2+3ab+b^2$ at every algebra element;
6. $C_q^1$ orbit partition versus the $\Delta_q$ fibers;
7. exact shell, cyclic locus, discard, $A$-orbit, quotient, and full-shell
   orbit counts versus the frozen proof ledger; and
8. prime-only reversing group construction versus the brute reversing
   relation, including no cyclic/noncyclic mixing.

## Key findings

1. **The positive algebraic mechanism is exact.**  For all nine fixed
   controls, $\operatorname{Cent}_{\mathrm{Mat}_2(R_q)}(A)=R_q[A]$ in the
   finite check, and $U\mapsto Ue_1$ is a free and transitive map from
   $C_q$ onto $\mathrm{CV}_q$.  This reproduces the proof-derived torsor.

2. **The full quotient removes multiplicity but also removes the clock.**
   Every $\mathrm{CV}_q/C_q$ has one class, while the induced $A$ transition
   is exactly the identity.  Its native primitive period is one for every
   $q$; the specialization $z=q^{-s}$ is therefore an external modulus
   label.

3. **The symplectic restriction retains norm multiplicity.**  The observed
   quotient counts are
   `1,2,2,6,10,2,2,6,2`, equal to the exact norm-image sizes in frozen
   order.  Thus the full one-class compression uses the larger local
   $\mathrm{GL}_2$ centralizer, while $C_q^1$ does not generally compress to
   one class.  Its induced $A$ transition is still identity.

4. **The cyclic locus is not always the complete shell.**  The ramified
   controls $q=5,10$ discard $4,12$ shell points, respectively, and the split
   prime $11$ discards $20$.  Full-shell orbit counts therefore remain
   distinct from cyclic-locus quotient counts.

5. **The mechanism is not prime-specific.**  Each predeclared composite
   $q=4,6,9,10$ also has a one-class full-centralizer cyclic quotient and
   identity induced dynamics.  The construction supplies neither an
   intrinsic prime selector nor a native $\log q$ clock.

## Integrity counters

All forbidden-operation counters are exact zero: network access, external
data loading, generated prime/modulus targets, random draws, numerical
$s$, $\log q$, and $q^{-s}$ evaluation, matrix/parameter search,
equivariant/stacky/twisted construction, and Hecke/transfer/Fredholm/quantum
construction.  External prime tables and Riemann-zero data were not accessed.

## Terminal result

`CENTRALIZER_CYCLIC_TORSOR_CERTIFIED /`
`A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC / ROUTE_B_NOT_OPENED`

No additional Paper-10 experiment is authorized.  Equivariant, Burnside,
orbifold, stacky, groupoid, and twisted-sector refinements remain outside
scope rather than being ruled out; they form the separately source-locked
question for Paper 11.
