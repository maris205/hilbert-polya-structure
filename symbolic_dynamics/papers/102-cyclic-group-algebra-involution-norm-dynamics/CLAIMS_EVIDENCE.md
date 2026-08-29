# Claims and evidence — P102

| Claim | Analytic evidence | Independent deterministic control |
|---|---|---|
| one-step symmetric collapse | commutativity gives `(aa*)*=aa*`; on the fixed algebra `T(b)=b^2`, hence `T^k(a)=(aa*)^(2^(k-1))` | literal coefficient reversal, cyclic convolution, symmetry, and repeated powering agree state-by-state in all nine lanes |
| Fourier block normal form | the split DFT sends `*` to `j -> -j` and multiplication to coordinatewise multiplication | every enumerated coefficient vector satisfies both the Fourier reversal rule and `DFT(T(a))_j=â_j â_{-j}` |
| exact fixed sequence | a self block and a synchronized pair both reduce to `z^(2^k)=z`; this has `1+gcd(2^k-1,q-1)` roots | direct iteration over every state agrees for `k=1..12` in seven prime-field and two extension-field lanes |
| recurrent core | scalar squaring is periodic exactly on `{0} union mu_m`; a periodic paired block must be diagonal | literal functional-graph cycles agree with Fourier membership for every enumerated state and have size `(m+1)^o` |
| sharp maximum depth | scalar squaring removes one factor of two from multiplicative order per step; a paired block contributes one synchronization step | full graph distances give `alpha+1_{n>s}`, including `n=1,2`, odd characteristic, and `F_4/F_16` lanes |
| all cycle counts | finite-map Möbius inversion gives `P_k=sum_{d|k} mu(k/d)F_d`, and `C_k=P_k/k` | literal cycle inventories agree with every nonzero Möbius exponent and account exactly for the recurrent core |
| finite zeta product | each length-`k` cycle contributes `(1-z^k)^(-1)`; all periods divide `ord_m(2)` | direct cycle lengths are checked to divide the squaring order, so the stored cycle dictionary is the zeta exponent ledger |
| qualified rigidity | `F_1` gives `o`, the maximum fixed root count gives odd part `m`, depth reconstructs candidate `q`, and phase size resolves candidate `n`; `o=2` has a separate Diophantine exclusion | 85 formula-level lanes cover every divisor `n|(q-1)` for 19 registered prime powers and recover exactly `(q,n)` |

## Two proof/control routes

1. **Algebra-first route.**  The involution identity places the first image in
   the symmetric algebra, after which the system is ordinary Frobenius-style
   squaring.  This proves the iterate formula without choosing roots of unity.
2. **Fourier-block route.**  Split characters into fixed and paired inversion
   orbits.  The block dynamics independently yield fixed points, recurrence,
   depth, cycle support, and the recovery inputs.

The verifier is deliberately coefficient-first: it does not construct the map
from the Fourier formula.  Extension-field lanes use explicit irreducible
polynomials, so agreement there is not a side effect of prime modular
arithmetic.

## Owner-subtracted boundary

- Terras is cited for finite-group Fourier analysis.
- Bovdi–Grishkov are cited for canonical group-algebra involutions and the
  symmetric/unitary-unit setting.
- Vasiga–Shallit and Qureshi–Reis are cited for finite-field/finite-group
  power-map functional graphs.
- Artin–Mazur are cited for periodic-point zeta bookkeeping.

No ownership is claimed for those ingredients.  The residual claim is limited
to their explicit combination for the whole split cyclic group algebra under
`a -> aa*`, including paired synchronization, the full temporal census, sharp
depth, and the stated within-family recovery theorem.  The source search is
bounded rather than exhaustive.  External release and priority language remain
**HOLD**.

Internal firewall: P86's adjacent-product process is a spatial stochastic
two-block factor whose output is a stationary process.  P102 is a finite
deterministic group-algebra self-map; the paired product synchronizes in one
step and is then iterated by squaring.  Only the elementary multiplication
primitive is shared.
