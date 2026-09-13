# Claims--Evidence Matrix

## Reading key

This matrix distinguishes new Paper 19 claims from predecessor results,
standard tools, and permanently forbidden upgrades.

- `AUTHOR PROOF` means a complete derivation appears in `PROOF_PACKAGE.md`.
- `EXT-L` is Laurent's qualitative torus Mordell--Lang theorem, the sole
  indispensable external proof input.
- `BG17` is a Paper 17 predecessor theorem, not a new Paper 19 claim.
- `PV16--PV18` are internal portfolio-provenance bindings.
- `STOP-S1` is a false conjecture retained for negative provenance.

No row is supported by computation, CAS output, finite enumeration, code,
data, or figures.

## Claim matrix

| ID | Exact claim | Hypotheses | Evidence chain | External or predecessor role | Status / forbidden upgrade |
|---|---|---|---|---|---|
| `C01` | The scalar recurrence, `V_m`, `T_m`, and the projection bijection use exactly `m` equations and `m+1` states. | `k>=2`, `1<=nu<k`, `a!=0`. | Proof Package Sec. 1. | None. | Supported; do not shift the endpoint by one. |
| `C02 / BG17` | Every anchored `s>=2` connected translate in `V_m`, `0<=m<=k`, has dimension at most `k-m`. | Actual collected support, `a,c,b_l!=0`, char. 0. | Group-algebra middle collapse and saturated relation lattice, Proof Sec. 3. | Owned by Paper 17. | Background only; not a Paper 19 novelty bullet. |
| `C03 / TA1` | If an anchored translate has dimension `k-m`, its subgroup is exactly `H_m`. | `1<=m<k`, hypotheses of C02. | Equal kernel rank plus saturation of `L_m`, Proof Sec. 4. | Extends BG17's equality construction to rigidity. | Supported; not a classification of lower-dimensional or inclusion-maximal cosets. |
| `C04 / TA2` | Normalized maximum-dimensional translates are in bijection with geometric points of the explicit scheme `E_m`. | C03, normalized free initial scalars. | Necessity, reconstruction, and uniqueness, Proof Sec. 5. | No external theorem. | Supported; `E_m` is not called Hilbert/Fano/fine moduli. |
| `C05` | `A_m=[max(0,m-nu),min(m,k-nu))` and `alpha_m=min(m,k-m,nu,k-nu)`. | `1<=m<k`. | Direct residue membership and interval length, Proof Sec. 5.2. | None. | Supported; no gcd hypothesis. |
| `C06 / TA3a` | `E_m` is nonempty for every permitted anchored coefficient tuple and every `1<=m<k`. | `Omega` algebraically closed char. 0, actual support fixed. | Each root assignment leaves an irreducible torus minus finitely many proper closed sets; Proof Sec. 6. | None. | Supported; do not replace by an unproved one-root explicit construction. |
| `C07 / TA3b` | If `P` is squarefree of degree `delta`, `E_m` has `delta^alpha` smooth geometric irreducible components of dimension `m-alpha`. | C06 plus squarefree `P`. | Root assignments and open irreducible tori, Proof Sec. 6. | Standard root-scheme facts only. | Supported; squarefree is mandatory. |
| `C08 / TA3c` | If `P` has `r` distinct roots, `E_m^red` has `r^alpha` geometric components; active multiple roots give natural nilpotent directions. | C06, arbitrary `P` with `c!=0`. | Reduction and completed local equations, Proof Secs. 6--7. | Standard local factorization. | Supported; geometric-fiber statement only. |
| `C09 / TA4` | Over the fixed-support coefficient torus, the universal normalized translate scheme is an open in `Z(P)^alpha x G_m^(m-alpha)`, flat relative lci and smooth over the discriminant complement. | Base `Spec Q[a^+-1,c^+-1,b_l^+-1]`; support fixed. | Finite locally free root scheme and open product, Proof Sec. 7. | Standard finite-flat/lci/smoothness criteria. | Supported; no coefficient-zero boundary and no total singular-locus theorem. |
| `C10 / TA4-local` | At active root multiplicities `mu_i`, the completed fiber local ring is the free power-series ring modulo `z_i^(mu_i)`. | Fixed coefficient fiber and a point of `E_m`. | Local factorization by units, Proof (7.4). | Standard completion fact. | Supported; say completed **fiber** local ring. |
| `C11 / CA1` | For every anchored coefficient tuple, a compatible finite extension and finitely generated group make `T_(k-1)` infinite, while `T_k` is finite for every finite-rank group. | Part A hypotheses. | `E_(k-1)` nonempty, saturated one-torus, parameter `2^N`, BG17 plus EXT-L; Proof Sec. 8. | BG17 owns terminal finiteness; EXT-L transfers geometry to arithmetic. | Supported; not every original field or every fixed `Gamma`. |
| `C12 / TB1` | Every support-one local character identity has exactly one exclusive label `A`, `B`, `C`, or `Z`, with the displayed scalar conditions. | `P=c+bX^d`, `a,b,c!=0`, `d>=2`. | Four-term group-algebra partition, Proof Sec. 9. | Standard character independence is the tool. | Supported; `A/B/C` require a nonzero `v` and cannot overlap `Z`. |
| `C13 / TB2--TB3` | The recurrence splits into `g` core residues; every colored scaling component has an integer height and satisfies `F_(j+q)=F_j+T F_(j+L)`. | `g=gcd(k,nu)`, `q=k/g`, `L=(k-nu)/g`; torsion-free character lattice. | Residue offsets, cycle-weight audit, colored free module; Proof Sec. 10. | None. | Supported; colors must not be replaced by accidental equality of values in `M`. |
| `C14 / TB4` | `q^2` consecutive core equations force every involved character to be zero. | C12--C13, `q>=2`, `gcd(q,L)=1`. | Minimum height, `B` persistence, triangular zeros, `qL=Lq`; Proof Sec. 11. | None. | Supported for arbitrary actual character rank. |
| `C15 / TB5` | With `q^2-1` core equations there is one nonzero configuration up to its character generator: one colored component, central delta block, and the explicit Laurent formulas. | C12--C13. | Central-block coverage, component intersection at `N_*`, generating functions (12.7)--(12.10), semigroup uniqueness; Proof Sec. 12. | None. | Supported; not a finite enumeration or rank-one ansatz. |
| `C16 / TB6--TB8` | At `m=kq-1`, only residue `g-1` can carry C15; for `q>=3` its seven labels force `bc^(d-1)=-1`, `a=-1`, then `2c=0`, so `V_(kq-1)` has no positive-dimensional translate. | Support-one hypotheses, char. 0, `q>=3`. | Original residue counts, selected-label formulas, scalar contradiction; Proof Secs. 14--16. | None. | Supported; this is not an exact/optimal/minimal clock. |
| `C17 / TB9` | For `q=2`, `V_(kq-1)` has a positive-dimensional translate iff `a=-1` and `bc^(d-1)=-1`; the core is `CBA`, and inactive residues admit a generic `Phi` fill. | Support-one hypotheses, `q=2` so `L=1`. | Core necessity/sufficiency, primitive exponent, polynomial-automorphism avoidance; Proof Sec. 17. | Planar `g=1` endpoint owned by Paper 16. | Supported; `CBA` itself is not a novelty claim. |
| `C18 / CB1` | For finite-rank groups, `T_(kq)` is always finite; `T_(kq-1)` is finite for `q>=3` and for nonresonant `q=2`, while resonant `q=2` admits compatible infinitude. | C14--C17 and arbitrary char.-0 field bridge. | EXT-L plus Proof Sec. 18. | EXT-L supplies qualitative transfer only. | Supported; no effective count except the separate Paper 16 theorem. |

## Provenance and negative-history rows

| ID | Bound artifact or event | Scientific ownership consequence | Status |
|---|---|---|---|
| `PV16` | Paper 16 terminal review SHA-256 `e355172b4533011d549453d02ee9939fb2dabc16fef035206ad4911fdf18eb76`; PDF SHA-256 `b4ffdaf30e2d0684b875863393e6937c26f51ce89c6f47567a24ed9a123e5e4f`. | Owns planar support-one `CBA`, exact `T_4/T_3`, and stronger effective bound. | Binding predecessor provenance. |
| `PV17` | Paper 17 terminal review SHA-256 `941e8b47e4436fdd9bff6f48ebf6e8c1174d07f545a220ead9ad02d73b23ed9d`; PDF SHA-256 `080282e18b085cc87bb590db239c4c8f8f80fd86147ded1aa775e67504b17f2e`. | Owns anchored `k-m` law, special equality family, `T_k` finiteness, and special-coefficient sharpness. | Binding predecessor provenance. |
| `PV18` | Paper 18 terminal review SHA-256 `251d78d2989c0c76b6f1a3090c9aeccf9c66a7171829ca6b795c9ca97d359713`; PDF SHA-256 `e9044c2a9e6452b58b9e345a17c33a211feed909414798fa4696e169b24be06b`. | Marked trace/ramification work has no theorem-level collision. | Boundary checked. |
| `STOP-S1` | Initial conjecture that every `q^2-1` shadow lifts and makes `kq` exact; refuted first at `(k,nu,d)=(3,1,2)` and then universally for `q>=3`. | False scalar-sharpness language is permanently forbidden. | STOP / retained as negative provenance. |

## AC01--AC18 cross-reference

| Anti-claim | Forbidden combination |
|---|---|
| `AC01` | `T_m` + geometric dimension language. |
| `AC02` | `TA1/TA2` + all lower-dimensional or inclusion-maximal cosets. |
| `AC03` | “maximum-dimensional” with any meaning other than `dim=k-m`. |
| `AC04` | `E_m` + Hilbert scheme, Fano scheme, or fine moduli functor. |
| `AC05` | Geometric component counts over an arbitrary nonclosed ground field without qualification. |
| `AC06` | Smooth `delta^alpha` statement without squarefree `P`. |
| `AC07` | Universal-family claim while coefficients may vanish or actual support changes. |
| `AC08` | Relative discriminant boundary + irreducibility/reducedness/complete total singular-locus claims. |
| `AC09` | `CA1` + every fixed group or no field extension. |
| `AC10` | `EXT-L` + effective cardinality. |
| `AC11` | `C16` + exact, optimal, shortest, or minimal scalar clock. |
| `AC12` | Planar `q=2` `CBA` + Paper 19 novelty. |
| `AC13` | BG17 results + Paper 19 headline novelty. |
| `AC14` | Standard character/root/discriminant machinery + priority claim. |
| `AC15` | Positive characteristic, a zero coefficient, or `d=1`. |
| `AC16` | Rational/Laurent support or arbitrary polynomial automorphisms. |
| `AC17` | Bounded negative search + absolute priority. |
| `AC18` | Effective enumeration, heights, periodic classification, or any external lifecycle effect. |

## Evidence balance

The package has two independent proof-heavy contributions.

- Part A uses the predecessor lattice only as its entry point. Its new mass is
  the equality-kernel rigidity, exact scalar reconstruction, fixed-fiber
  branch geometry, universal fixed-support family, and coefficientwise
  arithmetic sharpness.
- Part B supplies an arbitrary-rank component theorem, not a rank-one guess.
  The colored-height reduction, two generating functions, seven labels, and
  scalar contradiction form one dependency chain. The `q=2` endpoint is kept
  for completeness and exact boundary consistency, with its Paper 16
  ownership explicit.

Every scientific row is either author-proved or has one precisely delimited
external/predecessor role. No claim depends on a missing computation.
