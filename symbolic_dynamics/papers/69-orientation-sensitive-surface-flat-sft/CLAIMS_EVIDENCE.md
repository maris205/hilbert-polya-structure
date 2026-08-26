# Claims and evidence ledger

| ID | Manuscript claim | Evidence/proof | External owner or control | Release note |
|---|---|---|---|---|
| C1 | The relator-holonomy rule defines an SFT over `Lambda` | The rule reads six edge variables in a fixed finite set; see Proposition 3.1 | Definition-level | Safe |
| C2 | `|Fix_H(X_K)|=|K|^([Lambda:H]-1)|Hom(H,K)|` | Explicit rooted spanning-tree gauge bijection in Proposition 3.2 | Finite enumeration checks selected covers | Proof is internal |
| C3 | `H_n` covers are nonorientable genus `n+2`; `L_m` covers are orientable genus `m+1` | Orientation character, explicit map `f`, index multiplication, Euler characteristic | Standard covering-space classification | Proof is internal |
| C4 | `O_K(m)=|K|^(4m) sum d^(-2m)` | C2+C3 and orientable surface formula | Mednykh formula; Klug, Corollary 1 and the closed-surface display following Theorem 3, is the modern source used | Classical owner credited |
| C5 | `N_K(n)=|K|^(2n) sum nu^(n+2)d^(-n)` | C2+C3 and nonorientable surface formula | Frobenius--Schur formula; Klug, Corollary 1 and the closed-surface display following Theorem 3, is the modern source used | Classical owners credited |
| C6 | Joint spectra recover order and the pair multiset | Root limit plus three finite moment inversions; the odd moments at indices `m=0,...,r-1` first recover `(c_d^+-c_d^-)/d`, then multiplication by known `d` recovers the signed difference | Exact rational controls for `D_8,Q_8,C_3,S_3` | Main internal theorem |
| C7 | `D_8/Q_8` orientable equality and odd nonorientable separation | Character tables reduced to `(d,nu)` and substituted in C4--C5 | Direct brute-force tuple counts in `code/verify_surface_flat_sft.py` | Example, not classification claim |
| C8 | P69 and P70 use distinct proof engines | Object/invariant/field/proof comparison in Section 7 | Cross-package scope audit | No novelty implication |

## Negative claims and exclusions

- The signature `(|K|,{(d_chi,nu_chi)})` is not asserted to determine `K` up
  to isomorphism.
- A single one of the two families is not asserted to recover all indicators.
- The paper does not claim all surface-group SFT periodic spectra have a
  character interpretation.
- No priority claim is made for the construction or the inversion mechanism.
- The rejected Rudin--Shapiro computation is not evidence for this paper.
