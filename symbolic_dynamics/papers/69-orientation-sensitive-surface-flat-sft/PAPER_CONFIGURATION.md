# Paper configuration

- **Internal identifier:** P69
- **Working title:** Orientation-Sensitive Periodic Spectra of Surface-Group Flat-Connection Shifts
- **Article type:** short theoretical paper
- **Language:** English manuscript; separate Chinese abstract supplied
- **Authorship:** anonymous internal draft
- **Venue posture:** journal-neutral `amsart`, 11 pt, A4, target 10--15 pages
- **Freeze date:** 2026-08-25 UTC
- **Official Round-2 core proof audit:** **PASS**
- **Round-2 package synchronization:** **PASS after author replay; see `FINAL_QA.md`**
- **Stage 2.5:** **PENDING -- specialist novelty/collision and topology-convention review**
- **Release status:** **HOLD -- no specialist, priority, submission, or release clearance**

## Frozen system

Let

```text
Lambda = <x_1,x_2,x_3 | x_1^2 x_2^2 x_3^2 = 1>
```

be the fundamental group of the closed nonorientable surface of genus three,
and let `K` be a finite group.  The alphabet is `K^3`: at every vertex of the
Cayley 2-complex, a symbol labels the three positively oriented generator
edges.  A finite-radius rule requires trivial ordered holonomy around every
translate of the single relator.  The resulting left shift is denoted `X_K`.

## Frozen subgroup families

Define `f: Lambda -> Z` by

```text
f(x_1)=1,  f(x_2)=-1,  f(x_3)=0.
```

Let `omega: Lambda -> Z/2` send every `x_i` to `1`.  The two
divisibility-directed families are

```text
H_n = ker(Lambda --f--> Z --> Z/n),                 n >= 1,
L_m = ker(ker(omega) --f--> Z --> Z/m),             m >= 1.
```

Thus `H_n` has index `n` and is the group of a nonorientable surface of genus
`n+2`; `L_m` has index `2m` and is the group of an orientable surface of genus
`m+1`.

## Main theorem contract

For irreducible complex characters `chi` of `K`, write `d_chi=chi(1)` and
`nu_chi in {-1,0,1}` for the Frobenius--Schur indicator.  The manuscript must
prove

```text
O_K(m) := |Fix_{L_m}(X_K)|
        = |K|^(4m) sum_chi d_chi^(-2m),

N_K(n) := |Fix_{H_n}(X_K)|
        = |K|^(2n) sum_chi nu_chi^(n+2) d_chi^(-n).
```

The joint sequences determine `|K|` and the multiset
`{(d_chi,nu_chi)}`.  Conversely, those data determine both sequences.

## Mandatory firewalls

- The surface homomorphism formulas belong to Frobenius--Schur and Mednykh;
  Klug is the modern source/account used for exact normalization.
- Carroll--Penland supply group-SFT periodic-point context, not the theorem of
  this paper.
- Cohen--Goodman-Strauss supply surface-group SFT context, not the flat-shift
  count.
- No priority, uniqueness, or first-example claim is permitted.
- The finite verifier is regression evidence only; the proof is symbolic.
- `D_8` means the order-eight dihedral group.
- The paper distinguishes the chosen groups only through the recovered
  character-theoretic signature.  It does not claim that the signature
  classifies finite groups.
- P70's finite-Heisenberg modular-nullity argument is not used here.  P69 uses
  surface topology, nonabelian flat connections, complex characters,
  Frobenius--Schur indicators, and finite moment inversion.
- The rejected Rudin--Shapiro candidate is quarantined in
  `RUDIN_SHAPIRO_OWNER_MEMO.md` and is not manuscript content.
