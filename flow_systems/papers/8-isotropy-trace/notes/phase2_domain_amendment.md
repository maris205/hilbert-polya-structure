# Paper 8 Phase-2 finite-corner and character-sign amendment

Amendment ID: `P8-PH2-TYPED-AMEND-2026-08-14-v1`  
Date: 2026-08-14  
Status: **INDEPENDENT EXACT-BYTE RE-LOCK PASS**

## 1. Trigger

The Phase-2 one-orbit source chain proves

```text
A_L = C*((R/LZ) rtimes R) ~= C(T) tensor K(H),
H = L2(R/LZ),
```

with `H` infinite dimensional.  The trace source audit then exposed a typed
domain error in the Phase-1 wording: `Z(A_L)=0`.  The copy of `C(T)` is either
the multiplier centre `ZM(A_L)=C(T) tensor 1` or a chosen trace-finite corner,
not a nonzero central subalgebra of `A_L`.

For the character weight `tau_theta=delta_theta tensor Tr`, a positive
multiplier `f tensor 1` has infinite weight whenever `f(theta)>0`.  Thus the
multiplier centre cannot carry the finite point-evaluation witness required by
the no-normal-extension argument.

## 2. Exact repair

After the concrete one-orbit completion and regular representation are proved,
choose a rank-one projection `e in K(H)` and put

```text
p = 1 tensor e in A_L,
p A_L p ~= C(T),
tau_theta(p)=1.
```

The fixed map owning this projection is explicitly

```text
A_L=C*(O rtimes R) -> A_(L,r)=C*_r(O rtimes R) -> M_L^reg.
```

It is not the conditional packet map
`C*(G_p)->C*_r(G_p)->M_(p,nu)^reg`.

The amended P8-6 argument must:

1. prove the image and closure of this same full finite projection in the
   fixed regular representation;
2. compress any hypothetical normal extension of the same extended-positive
   character trace by `p`;
3. obtain a finite normal positive functional on the regular
   `L-infinity(T)` corner; and
4. contradict normality using decreasing continuous peak functions whose
   values at `theta` stay one while their infimum in Haar `L-infinity` is zero.

The projection/trivialization choice is a proof device, not new source data.
The conclusion must be independent of which rank-one projection is used.  A
corner is not called central.  Existence/nonuniqueness of singular state
extensions from `C(T)` to `L-infinity(T)` remains a separate claim from the
no-normal-extension theorem.

## 3. Crosswalk

| Prior wording | Amended wording |
|---|---|
| point evaluation on a continuous central subalgebra | point evaluation on a proved trace-finite full rank-one corner |
| `C(T)` treated as the centre of `C(T) tensor K` | `Z(A_L)=0`; `C(T)` occurs in the multiplier centre or finite corner |
| character weight restricted finitely to the multiplier centre | character weight is generally infinite there |
| point evaluation directly compared with regular `L-infinity` | first compress the same fixed-map trace by a finite projection |
| one-orbit projection compressed inside an unproved packet completion | local corner belongs to `A_L -> M_L^reg`; packet promotion needs a separate same-map bridge |
| `chi_theta` paired with frequencies `(2pi n+theta)/L` and phase `exp(-ir theta)` | sourced induction rule pairs it with `(2pi n-theta)/L` and `exp(+ir theta)` |

The changes are implemented in `research_protocol.md` (Floquet display,
separate local/packet completion gates, P8-6, controls 2/9/14, amendment ledger) and
`candidate_lock.md` (status, frozen sign, and trivial-character finite-corner
gate).

## 4. Simultaneous sign correction

Williams's induced-representation convention realizes
`Ind_(LZ)^R chi_theta` on functions satisfying

```text
xi(u+rL)=chi_theta(rL)^(-1)xi(u)=exp(-ir theta)xi(u),
(U_t xi)(u)=xi(u-t).
```

The orthonormal Floquet modes consequently have frequencies
`(2pi n-theta)/L`.  With the frozen transform
`fhat(xi)=integral f(t)exp(-it xi)dt`, the integrated time operator has
eigenvalues `fhat((2pi n-theta)/L)`.  Scaled shifted Poisson summation gives

```text
sum_n fhat((2pi n-theta)/L)
  = L sum_r f(rL)exp(+ir theta).
```

This is precisely the simultaneous `theta -> -theta` correction preregistered
in the Phase-1 protocol.  It changes neither dual-Haar cancellation nor the
trivial-character value and uses no target data.  Phase 3 must still prove the
representation and Poisson steps on the fixed object; this amendment only
freezes the correct convention.

## 5. Non-changes

This amendment does not change:

- the primary question or its `CONFIRM`/`REFUTE`/`NOT_TESTABLE` outcomes;
- any typed candidate ID;
- the frozen Fourier, Haar, length, or probability normalizations (only the
  character-coordinate sign is corrected simultaneously);
- the local/finite/positive-time domain split;
- P8-1--P8-5 or P8-7--P8-9;
- the packet Hausdorff/LCH source gate;
- the prohibition on target zeros, fitted phases/masses, or proxy transport;
- the A1 ceiling, A2/A3 failure boundary, A4 closure, or Route-B prohibition.

## 6. Evidence ownership

The exact `C(T) tensor K` completion and Williams's induced-function convention
are supported by `phase2_groupoid_source_audit.md` and its retained Williams
source.  The centre/corner distinction and the required fixed-map proof
obligations are recorded in `phase2_trace_source_audit.md`.  The Floquet
diagonalization, shifted Poisson identity on the fixed representation,
rank-one compression, and decreasing-peak contradiction remain Paper-8
Phase-3 lemmas; this amendment proves none of them.

The local no-normal-extension lemma can refute only the one-orbit normal
extension analogue.  It answers the packet-level primary question only after a
separate theorem transports the same trace and finite corner through the
conditional packet completion.  If the packet Hausdorff/LCH or same-map gate
does not close, the registered primary outcome is `NOT_TESTABLE`.

Phase 3 remains blocked until independent reviewers verify the amended bytes,
the unchanged candidate/outcome boundaries, and the exact active hashes.
