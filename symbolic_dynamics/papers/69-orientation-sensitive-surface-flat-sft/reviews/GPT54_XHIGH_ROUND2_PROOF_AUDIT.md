# GPT54_XHIGH_ROUND2_PROOF_AUDIT

## Provenance

- Model role requested: `gpt-5.4`, `xhigh`, official second-round hostile mathematical reviewer for P69 only
- Review mode actually used here: local independent proof audit over the frozen package, with no manuscript edits
- Review date: 2026-08-25 UTC
- Scope audited: the current manuscript source `main.tex` and `sections/0_abstract.tex` through `sections/8_conclusion.tex`; `PROOF_PACKAGE.md`; `CONTROL_RESULTS.md`; `CLAIMS_EVIDENCE.md`; `ARGUMENT_BLUEPRINT.md`; `NARRATIVE_REPORT.md`; `CITATION_AUDIT.md`; `PAPER_CONFIGURATION.md`; `PAPER_PLAN.md`; `BILINGUAL_ABSTRACT.md`; `FINAL_QA.md`; `BUILD.md`; `PAPER_IMPROVEMENT_LOG.md`; prior hostile reviews and resolutions under `reviews/` and `rounds/`; the exact control script `code/verify_surface_flat_sft.py`
- Independent rerun performed: `python3 papers/69-orientation-sensitive-surface-flat-sft/code/verify_surface_flat_sft.py`
- Rerun result: terminal status `ALL CHECKS PASS`

## Overall verdict

- Core mathematics: `PASS`
- Re-derivation of the gauge formula, the orientable/nonorientable families, the Frobenius--Schur substitutions, the recovery mechanism, and the `D_8/Q_8` separation: `PASS`
- Round-1 fix audit as an exact full-package compliance claim: `PARTIAL FAIL`
- Reason for the partial failure: the requested “families, not chains” cleanup is correct in the current manuscript source, but it is not fully synchronized across the complete frozen package
- External release: `HOLD`

I found no critical or major mathematical defect. I found one minor but real package-synchronization issue, described below. I do not invent any further defect.

## Severity-ranked issues

### MINOR 1 — the “families not chains” Round-1 fix is correct in the manuscript but not fully synchronized across the frozen package

- The current manuscript source uses the corrected terminology. See `sections/1_introduction.tex:46-55` and `sections/4_subgroup_counts.tex:7-12,44-46`.
- `PROOF_PACKAGE.md` is also synchronized on this point. See `PROOF_PACKAGE.md:35-48`.
- However, the frozen package still contains chain-language outside the manuscript:
  - `BILINGUAL_ABSTRACT.md:29` uses `子群链`
  - `BILINGUAL_ABSTRACT.md:40` uses `非定向链`
  - stale extracted-text QA artifacts also retain the superseded wording, including `qa/final_text.txt` and `qa/final_text.new.txt`
- This matters because `rounds/GPT54_XHIGH_ROUND1_RESOLUTION.md:29` claims the terminology was replaced throughout author-facing manuscript and package material, and `rounds/GPT54_XHIGH_ROUND1_RESOLUTION.md:59-61` states that active manuscript and standing package sources use only the corrected terminology. That package-level claim is too strong.
- Mathematical impact: none
- Audit impact: the exact Round-1 package-wide cleanup claim does not fully pass

No other issue survived hostile reconstruction.

## Independent proof reconstruction

### 1. Local SFT and the general periodic formula

Let

```text
Lambda = <x_1,x_2,x_3 | x_1^2 x_2^2 x_3^2 = 1>.
```

For a finite group `K`, a configuration `A in (K^3)^Lambda` assigns labels
`A_i(g)` to the positively oriented edge `g -> g x_i`. The reverse edge is
labeled by `A_i(g)^(-1)`. The relator loop at `g` uses exactly the six labels

```text
A_1(g), A_1(gx_1), A_2(gx_1^2), A_2(gx_1^2x_2), A_3(gx_1^2x_2^2), A_3(gx_1^2x_2^2x_3).
```

Requiring their ordered product to equal `1` reads only a fixed finite support,
so the admissible set is an SFT. This matches `sections/3_flat_shift.tex:7-42`.

Now let `H <= Lambda` have finite index `V`. Under the left shift convention
used in `sections/2_background.tex:24-39`, `H`-fixed configurations are exactly
those constant on left cosets `H\Lambda`, so they descend to `K`-edge labels on
the finite cover `Y = H\backslash \widetilde N_3`. The local relator condition
becomes trivial face holonomy on every lifted 2-cell. Thus `Fix_H(X_K)` is the
set of raw flat `K`-connections on `Y`.

Choose a root vertex `v_0` and a spanning tree `T` in the 1-skeleton of `Y`.
A based gauge is a vertex map `u` with `u(v_0)=1`; there are exactly
`|K|^(V-1)` such maps. With the gauge action

```text
(u.A)(v -> w) = u(v) A(v -> w) u(w)^(-1),
```

the based action is free: if `u.A=A`, then along any oriented tree edge
`v -> w` one gets

```text
u(w) = A(v -> w)^(-1) u(v) A(v -> w),
```

and recursion from `u(v_0)=1` forces `u=1` on all vertices.

Every flat connection has a unique based gauge representative that is trivial
on all tree edges. Existence comes from the forward recursion
`u(w)=u(v)A(v->w)` along the tree. Uniqueness is the same tree recursion used
for freeness.

For a tree-trivial flat connection, holonomy on based loops is invariant under
cellular homotopy because inserting or deleting a face boundary contributes the
identity by flatness, and tree segments contribute nothing by tree triviality.
Hence a tree-trivial flat connection defines a homomorphism
`pi_1(Y,v_0) -> K`. Since `Y` is the cover associated with `H`,
`pi_1(Y,v_0) ≅ H`.

Conversely, a homomorphism `H -> K` determines labels on the non-tree
1-cells after collapsing the tree to the root, and the 2-cell relations are
satisfied because the relators map to `1`. Re-expanding the tree with identity
labels gives a tree-trivial flat connection.

Therefore the set of flat connections factors as

```text
{based gauges} x Hom(H,K),
```

and

```text
|Fix_H(X_K)| = |K|^(V-1) |Hom(H,K)|
             = |K|^([Lambda:H]-1) |Hom(H,K)|.
```

This rederives `sections/3_flat_shift.tex:57-111` and `PROOF_PACKAGE.md:17-33`.

### 2. The two finite-index families

The homomorphism `f: Lambda -> Z` defined by

```text
f(x_1)=1, f(x_2)=-1, f(x_3)=0
```

is well-defined because the relator has `f`-value `2-2+0=0`. Let
`omega: Lambda -> Z/2` send each `x_i` to `1`.

#### Nonorientable family

Define

```text
H_n = ker(Lambda --f--> Z --> Z/n).
```

Because `f` is onto, `[Lambda:H_n]=n`. Also `x_3 in H_n` since `f(x_3)=0`,
but `omega(x_3)=1`, so `H_n` is not contained in the orientation kernel. By
the standard criterion for surface covers, the associated cover is
nonorientable.

Since `chi(N_3)=2-3=-1`, the `n`-sheeted cover has Euler characteristic `-n`.
If its nonorientable genus is `ell`, then `2-ell=-n`, so `ell=n+2`.

#### Orientable family

Let `Lambda^+ = ker omega`. This is the orientation double-cover subgroup, of
index `2`. Its cover has Euler characteristic `2 chi(N_3) = -2`, hence it is
the orientable surface `Sigma_2`.

The restriction `f|_{Lambda^+}` is onto because `x_1 x_3^(-1)` lies in
`Lambda^+` and has `f`-value `1`. Define

```text
L_m = ker(Lambda^+ --f--> Z --> Z/m).
```

Then `[Lambda^+ : L_m]=m`, hence `[Lambda:L_m]=2m`. Since `L_m <= Lambda^+`,
its associated cover is orientable. Its Euler characteristic is `-2m`, so
`2-2g=-2m`, giving `g=m+1`.

This rederives `sections/4_subgroup_counts.tex:4-46` and
`PROOF_PACKAGE.md:35-48`. The index and genus conventions are coherent.

### 3. Orientable and nonorientable fixed-point laws

I accept the Frobenius--Schur--Mednykh formulas as cited classical input, not
as new work:

```text
|Hom(pi_1(Sigma_g),K)| = |K|^(2g-1) sum_chi d_chi^(2-2g),
|Hom(pi_1(N_ell),K)|   = |K|^(ell-1) sum_chi nu_chi^ell d_chi^(2-ell).
```

These are stated in `sections/2_background.tex:60-79`.

For `L_m`, one has `V=2m` and `g=m+1`. Therefore

```text
|Fix_{L_m}(X_K)|
= |K|^(2m-1) |Hom(L_m,K)|
= |K|^(2m-1) * |K|^(2m+1) sum_chi d_chi^(-2m)
= |K|^(4m) sum_chi d_chi^(-2m).
```

For `H_n`, one has `V=n` and `ell=n+2`. Therefore

```text
|Fix_{H_n}(X_K)|
= |K|^(n-1) |Hom(H_n,K)|
= |K|^(n-1) * |K|^(n+1) sum_chi nu_chi^(n+2) d_chi^(-n)
= |K|^(2n) sum_chi nu_chi^(n+2) d_chi^(-n).
```

The exponent audit is clean:

- gauge exponents: `2m-1` and `n-1`
- Hom exponents: `2m+1` and `n+1`
- total fixed-point exponents: `4m` and `2n`
- nonorientable indicator power: `n+2`
- degree power in the nonorientable family: `-n`

This rederives `sections/4_subgroup_counts.tex:48-103` and
`PROOF_PACKAGE.md:50-65`.

### 4. Recovery of `|K|` and the multiset `(d_chi, nu_chi)`

Let

```text
t_d  = c_d^+ + c_d^- + c_d^0,
s_d  = c_d^+ + c_d^-,
delta_d = c_d^+ - c_d^-.
```

#### Step 1: recover `|K|`

From the orientable formula,

```text
O_K(m) = |K|^(4m) sum_chi d_chi^(-2m).
```

Because the trivial character has degree `1`,

```text
1 <= sum_chi d_chi^(-2m) <= |Irr(K)|.
```

Taking `4m`-th roots gives

```text
|K| = lim_{m->infty} O_K(m)^(1/(4m)).
```

#### Step 2: recover the occurring degrees and total multiplicities

Normalize

```text
P_m = O_K(m) / |K|^(4m) = sum_d t_d (d^(-2))^m.
```

The bases `d^(-2)` are distinct nonzero numbers, and the coefficients `t_d`
are positive for occurring degrees. The finite exponential-moment lemma
therefore recovers the unordered pairs `(d^(-2), t_d)`, hence the degree set
and each `t_d`.

#### Step 3: recover self-dual multiplicities

At even nonorientable indices,

```text
Q_m = N_K(2m) / |K|^(4m)
    = sum_d (c_d^+ + c_d^-) (d^(-2))^m
    = sum_d s_d (d^(-2))^m.
```

Characters with `nu=0` vanish from `Q_m`. Known bases and any `r`
consecutive moments recover all coefficients `s_d`, including zero ones.

#### Step 4: recover the signed self-dual difference

At odd nonorientable indices `n=2m+1`,

```text
R_m = N_K(2m+1) / |K|^(4m+2)
    = sum_d (c_d^+ - c_d^-) d^(-(2m+1))
    = sum_d ((c_d^+ - c_d^-)/d) (d^(-2))^m.
```

This is the exact place where Round 1 had required a repair. The current text
now gets it right. The recovered coefficient is not `delta_d` directly; it is

```text
b_d = (c_d^+ - c_d^-)/d.
```

Because the bases are already known, and because the lemma now explicitly
allows `m_0=0`, the values `R_0,...,R_{r-1}` recover all `b_d`. Since each
degree `d` is already known, multiplication by `d` gives

```text
delta_d = d b_d = c_d^+ - c_d^-.
```

Then

```text
c_d^+ = (s_d + delta_d)/2,
c_d^- = (s_d - delta_d)/2,
c_d^0 = t_d - s_d.
```

This rederives `sections/5_moment_recovery.tex:7-127` and
`PROOF_PACKAGE.md:67-115`.

#### `nu=0` branch

The zero-indicator case is now handled coherently everywhere it needs to be:

- theorem/proof level: `sections/5_moment_recovery.tex:88-125`
- control narrative: `sections/7_scope_controls.tex:48-77`
- claims ledger: `CLAIMS_EVIDENCE.md:8-10`
- proof package: `PROOF_PACKAGE.md:77-112`

Indicator-zero characters disappear from all nonorientable moments, but their
multiplicity is still recovered because `c_d^0 = t_d - s_d`. This is the
correct mechanism.

### 5. `D_8/Q_8` separation

Both groups have degree multiset

```text
{1,1,1,1,2}.
```

All four linear characters are real, hence have indicator `+1`. The unique
two-dimensional irreducible has indicator `+1` for `D_8` and `-1` for `Q_8`.
I independently rechecked the square counts:

- in `D_8`, the six elements `1, r^2`, and the four reflections square to `1`,
  while `r` and `r^3` square to `r^2`, giving `nu=+1`
- in `Q_8`, the two elements `±1` square to `1`, and the other six square to
  `-1`, giving `nu=-1`

Substituting into the fixed-point laws yields

```text
O_{D_8}(m)=O_{Q_8}(m)=8^(4m)(4+2^(-2m)),
N_{D_8}(n)=8^(2n)(4+2^(-n)),
N_{Q_8}(n)=8^(2n)(4+(-1)^n 2^(-n)).
```

Hence the orientable spectra agree, the even nonorientable spectra agree, and
the odd nonorientable spectra differ at every odd level. This matches
`sections/6_dihedral_quaternion.tex:1-76` and `PROOF_PACKAGE.md:117-129`.

## Small-group and convention checks

The independent rerun of `code/verify_surface_flat_sft.py` confirms:

- `D_8` and `Q_8` satisfy the predicted orientable equality and even/odd
  nonorientable split
- `C_3` has exact one-dimensional indicator signature `[1,0,0]`
- for `C_3`,

  ```text
  O_{C_3}(m)=3^(4m+1),  N_{C_3}(n)=3^(2n)
  ```

  and normalized moments reconstruct `(c_1^+,c_1^-,c_1^0)=(1,0,2)`
- `S_3` gives a separate orientable control at genera `1,2,3`

This directly exercises the exponent conventions `4m`, `2n`, `n+2`, and the
`nu=0` branch. See `code/verify_surface_flat_sft.py:121-156,183-252` and
`CONTROL_RESULTS.md:13-64`.

## Round-1 fix audit

| Round-1 item to audit exactly | Current evidence | Round-2 verdict |
|---|---|---|
| Allow and use moment index zero coherently | `sections/5_moment_recovery.tex:14-17,112-117`; `PROOF_PACKAGE.md:77-80,103-105`; `sections/1_introduction.tex:99-103` | `PASS` |
| Recover `b_d=(c_d^+-c_d^-)/d` first, then multiply by known `d` | `sections/5_moment_recovery.tex:107-123`; `PROOF_PACKAGE.md:97-106`; `CLAIMS_EVIDENCE.md:10` | `PASS` |
| Handle `nu=0` in theorem, proof, controls, and claims | `sections/5_moment_recovery.tex:88-125`; `sections/7_scope_controls.tex:48-77`; `CONTROL_RESULTS.md:21-26,43-60`; `code/verify_surface_flat_sft.py:183-225`; `CLAIMS_EVIDENCE.md:10` | `PASS` |
| Use families rather than falsely nested chains | current manuscript source passes; `PROOF_PACKAGE.md` passes; frozen package still has `BILINGUAL_ABSTRACT.md:29,40` and stale QA extracts with chain-language | `PARTIAL FAIL` |
| Maintain owner/source boundaries | `sections/1_introduction.tex:31-35`; `sections/2_background.tex:55-58`; `sections/7_scope_controls.tex:13-20`; `CITATION_AUDIT.md:1-68`; `PROOF_PACKAGE.md:133-136` | `PASS` |

## Pass/fail summary

- Proposition-level and theorem-level mathematics now pass hostile reconstruction.
- The Round-1 Step-4 repair is correct and complete.
- The `nu=0` branch is now genuinely exercised and correctly explained.
- The owner/source boundary is maintained; I found no historical-ownership regression.
- The exact claim that the terminology cleanup was completed across the whole frozen package does not pass.

## Remaining specialist and priority gates

These are still real release gates even after the mathematical pass:

- independent specialist review of the symbolic-dynamics literature
- independent specialist review of the surface-topology covering conventions
- independent specialist review of the finite-group / Frobenius--Schur framing
- continued no-priority posture unless an external collision search is repeated by humans

## Explicit verdict

- Core proof audit: `PASS`
- Exact Round-1 fix audit over the complete frozen package: `PARTIAL FAIL`
- If the question is whether the mathematical manuscript source is now sound on its own terms: `PASS`
- If the question is whether every Round-1 correction claim in the frozen package is literally true package-wide: `NO`

## EXTERNAL RELEASE HOLD

`EXTERNAL RELEASE HOLD` remains in force.

Reason:

1. the package itself still requires specialist external review by its own release rules; and
2. the exact Round-1 terminology-cleanup claim is not yet fully true across the complete frozen package, even though the current manuscript mathematics now passes.
