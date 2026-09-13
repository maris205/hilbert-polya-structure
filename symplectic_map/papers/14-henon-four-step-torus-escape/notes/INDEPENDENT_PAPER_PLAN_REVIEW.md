# PAPER_PLAN_PASS

## Review identity and frozen review gate

This is the fresh independent Paper 14 `PAPER_PLAN.md` review dated
2026-08-16. The reviewer was instantiated before the author-stop signal but,
under the review contract, did not open or stat `paper/PAPER_PLAN.md` until
the author supplied an explicit stop/freeze message and a stable SHA-256.
Before that signal, all work was limited to the allowlisted source-lock,
proof, citation, novelty, and proposal records.

The frozen plan reviewed here is:

- `paper/PAPER_PLAN.md`
- SHA-256:
  `6a0e16e3688714c43c9e9d87054c501d44989e59a523c6ff084eac4c9db3a88f`
- bytes: `30112`
- lines: `679`
- final newline: present

The review is bound to the already-passing source-lock authority:

- `experiments/source_lock.json`
- SHA-256:
  `f2077d20262f6a068da58a2227c405573dd34fa8b844461b3d057da94e9eaa0c`

and to the independent source-lock review:

- `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md`
- SHA-256:
  `ea6d13c1ec74bbad0ac8c6cd850d0f0b8c33992d05b5e428308eef3347a18308`
- canonical verdict: `SOURCE_LOCK_PASS`

Before this file was written, the `paper/` inventory contained exactly one
regular file, `paper/PAPER_PLAN.md`, and zero symbolic links, matching the
author-stop message.

## Mandate and decision rule

The plan was reviewed against the exact Paper 14 contract:

1. exact theorem and quantifier preservation;
2. proof completeness at the outline level;
3. claims-evidence alignment against the frozen source package;
4. pure-mathematics narrative and page feasibility;
5. correct main-text versus appendix allocation;
6. exact citation-role boundaries and no priority overclaim;
7. explicit limitations;
8. zero experimental, numerical, graphical, machine, or data-derived
   evidence;
9. anonymous-submission controls; and
10. closed downstream permissions.

The plan also had to preserve, visibly and early, all of the following:

- the exact title and one-sentence contribution;
- PC1 as the dominant `T_4` theorem;
- PC2 as the co-primary `T_3` sharpness theorem;
- COR1 as the subordinate whole-orbit periodic consequence;
- the `0<=j<=m` convention;
- fixed-coefficient ESS over `Gamma^3` of rank `3r`;
- the `BA`, `CB`, and exceptional `CBA` chains; and
- the explicit `81d^2` degenerate contribution.

## Exact-pass findings

### 1. Title, contribution sentence, and contribution hierarchy

PASS. The plan contains the exact locked title

> Four-Step Escape from Finite-Rank Tori for Monomial Henon Maps

and a correct one-sentence contribution that presents:

- the coefficient-uniform four-transition bound;
- the rank-one infinite-`T_3` sharpness family; and
- the weighted whole-orbit periodic corollary in subordinate language.

The claim hierarchy is explicit and correct:

- PC1 is the dominant primary claim;
- PC2 is co-primary sharpness, not a side remark; and
- COR1 is derived and subordinate.

No unsupported coefficient-stratification theorem is promoted.

### 2. Exact theorem lock and quantifiers

PASS. The plan preserves the theorem lock exactly:

- `K` is an arbitrary characteristic-zero field;
- `d>=2`;
- `a,b,c in K^*`;
- `Gamma <= K^*` has finite rank `r`, with no finite-generation assumption;
- `T_m(H,Gamma)` is defined with `0<=j<=m`;
- `T_4` is explicitly interpreted as five states and four transitions; and
- the PC1 bound is exactly
  `4d exp(18^9(3r+1)) + 81d^2`.

The periodic corollary correctly requires exact-period orbits wholly contained
in `Gamma^2`, and does not drift into the forbidden larger set of periodic
points with only one representative in `Gamma^2`.

### 3. Fixed-coefficient ESS and rank-`3r` control

PASS. The plan correctly preserves the fixed-coefficient ESS formulation:

- the normalized equation is
  `(1/c)x_(i+1) - (b/c)x_i^d - (a/c)x_(i-1) = 1`;
- the variable triple is `(x_(i+1), x_i^d, x_(i-1))`;
- the variable group is `Gamma^3`, of rank `3r`; and
- `1/c`, `-b/c`, and `-a/c` remain fixed coefficients in `K^*`.

The plan explicitly forbids the false coefficient-membership rewrite and
forbids enlarging `Gamma` to absorb the coefficients.

### 4. Proof completeness and main-text visibility

PASS. The outline carries the full logical spine of the proof in the main
text, not merely in appendices. In particular, it requires main-text treatment
of:

- the inverse map and injectivity;
- the nondegenerate `4dE(3,3r)` contribution;
- exhaustive `A/B/C` degeneracy labels;
- the nine-transition lemma;
- the `BA` closure;
- the `CB` compatibility and the exceptional `CBA` chain;
- the per-word bound;
- the simultaneous-degeneracy covering argument;
- the `3^4 = 81` word union bound giving `81d^2`; and
- the short-period check showing no extra term is needed.

This is exactly the required proof allocation. Appendix A and Appendix B are
used only for expanded table/algebra verification and are expressly forbidden
from carrying any missing logical implication.

### 5. Claims-evidence alignment

PASS. The claims-to-evidence matrix is consistent with the frozen source
package:

- every theorem-level mathematical claim is tied either to the proof package
  or to one precisely delimited primary source;
- all evidence columns correctly record `None (0)` for computational or
  experimental support; and
- the literature-positioning statement is correctly classified as a bounded
  comparison rather than theorem evidence.

No experimental, numerical, symbolic-CAS, or search-engine output is promoted
to mathematical evidence.

### 6. Citation-role boundaries and nonclaim discipline

PASS. The plan keeps the critical boundary sources in their exact roles:

- Evertse--Schlickewei--Schmidt, published Theorem 1.1, is the sole imported
  proof theorem;
- Bell--Ghioca remains a fixed-orbit / finitely-generated-subgroup return-time
  boundary, with the regular clause described correctly;
- Kim--Krieger--Postolache--Szeto remains a general-polynomial Hénon
  rational-periodic abundance boundary with exact theorem-range constraints;
- Mello--Yasufuku remains conditional on `Hyp_epsilon`, with the main-theorem
  large-`epsilon` range distinguished from the Vojta-based small-`epsilon`
  theorem.

The plan also explicitly bans:

- global priority claims;
- silent replacement of finite rank by finite generation;
- false regular-self-map inferences on `G_m^2`;
- false coefficient-membership assumptions; and
- the claim that Mello--Yasufuku's Vojta-based theorem verifies the general
  hypothesis of their main theorems.

### 7. Pure-math narrative, page feasibility, and appendix split

PASS. The plan is unmistakably a proof-first arithmetic-dynamics article, not
an ML-conference or experimental template. The page allocation is coherent:

- approximately `13.20` pages for front matter, main text, and references;
- `3--4` pages for verification appendices; and
- six main-text pages allocated to the degenerate-locus proof core.

The compression rule is also correct: exposition and related work compress
before any proof ingredient is moved out of the main text.

### 8. Limitations, anonymity, and downstream-permission closure

PASS. The plan records the required limitations:

- the ESS exponential is coarse;
- the `81d^2` term is coarse;
- no full `T_2/T_3` stratification is claimed;
- no general-polynomial Hénon theorem is claimed; and
- PC2 is sharp only in transition length, not in the numerical constants.

Anonymous-submission controls are explicit. Downstream permissions are also
explicitly closed: the plan authorizes only a future anonymous prose draft
after a separate planning review, and authorizes no manuscript source, no
bibliography file, no figure, no build, no code, no experiment, no result,
and no submission action.

## Zero-issue conclusion

No line-level repair is required. The frozen plan satisfies the Paper 14 plan
review contract without theorem drift, proof-gap outsourcing, citation
overreach, evidence contamination, or permissions leakage.

The exact canonical verdict is:

**PAPER_PLAN_PASS**
