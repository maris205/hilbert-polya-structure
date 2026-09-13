# SOURCE_LOCK_PASS

## Review identity and frozen object

This is the fresh independent Paper 14 source-lock review dated 2026-08-16.
The reviewer was instantiated after the source lock was frozen and authored
none of the eighteen bound inputs: none of the thirteen local source-package
files and none of the five upstream provenance files. The reviewer also did
not author the source lock. All checks before this report were read-only.

The reviewed lock is

`experiments/source_lock.json`

with exact frozen identity

```text
SHA-256  f2077d20262f6a068da58a2227c405573dd34fa8b844461b3d057da94e9eaa0c
Bytes    10,716
```

This report is the sole project write made by the reviewer and is at the
lock-authorized path `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md`. No code,
scientific execution, result, figure, paper, manuscript, or other artifact was
created or modified.

## Canonical JSON gate

The lock passed an independent strict parse and canonical round trip:

- UTF-8 decoding is strict;
- the file has exactly one terminal LF and contains no CR;
- every object is recursively ordered by Unicode code point;
- there is no insignificant whitespace;
- a duplicate-key-rejecting parser accepted the lock, and the same parser
  rejected a synthetic duplicate-key object;
- a nonfinite-number-rejecting parser accepted the lock, and the same parser
  rejected synthetic `NaN`, `Infinity`, and `-Infinity` values;
- all numbers present in the parsed object are finite; and
- compact re-encoding with recursive key sorting and one terminal LF is
  byte-for-byte identical to the frozen lock.

The lock has the expected seventeen top-level keys. Self bytes and self hash
are excluded explicitly and consistently. The authorization object has eight
keys, and its unique true value is `source_design_frozen`; code, experiment,
figure, implementation, manuscript, registered execution, and result
authorization are all false.

## Bound-input and inventory closure

All thirteen local bindings were rehashed independently from the Paper 14
project root. Their observed byte counts and SHA-256 values equal the lock:

| Local bound input | Bytes | SHA-256 |
|---|---:|---|
| `experiments/EXPERIMENT_PLAN.md` | 5,522 | `709b32fa83e7cf1502e57393e4b46daf33c83ccb88832a498e223d084eabbd95` |
| `experiments/EXPERIMENT_TRACKER.md` | 2,139 | `da117759e1e6a95579fcae16f27c3c868bd67b6d0b8b5d98e936b456a9354a97` |
| `notes/CITATION_VERIFICATION.md` | 12,919 | `0c9b08f566eedb1e9f344f6fb07dfcf0c87015daa566435d0c989ac722d4e2af` |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | 5,902 | `d1887968e8626c1a8e30c9cb1675a13277c76662ca0fee8834ea024123650f6e` |
| `notes/INDEPENDENT_CITATION_PRECISION_AUDIT.md` | 21,470 | `7e625c593267545088320459b65e990fdea5e347ed779416a6ce334d5a131f17` |
| `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md` | 18,618 | `e3dc9864c72d150e0f7a69d08aad9f4e24f0dde1c6115fe3d428b129ade4573c` |
| `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW_R2.md` | 12,836 | `8bde838d4bd18426f291eb793f5c822fbd6d70d604fc7097c5761c02bb309ef0` |
| `notes/NOVELTY_ASSESSMENT.md` | 8,660 | `2fafbef234a7e7cc8fbe10b25e0b920188b3c35472538fcbaf023da8d357bac1` |
| `notes/PROOF_PACKAGE.md` | 13,728 | `c43d8377707e0ee69aa6447984b77c2b5ef6d1d79bc1d56c6b5ab72ea4c8f5aa` |
| `notes/RESEARCH_QUESTION.md` | 6,371 | `782b48dfec973d877bf87c964a3bdd7227b52a21101b68a9a576929441bedb9c` |
| `refine-logs/FINAL_PROPOSAL.md` | 7,814 | `719214a159f1e36676d059c626dcefab7fe11b012e44146243db8aa500eb38a0` |
| `refine-logs/INITIAL_PROPOSAL.md` | 4,045 | `ecb3a5151c75dba6ac4b8415d000f9a9a3c36ff80af5b651b9de7ecbad7a6e22` |
| `refine-logs/REVIEW_SUMMARY.md` | 6,383 | `ac2a75bb0f393de1255958705bbcd2e75fa1e0800805d420f048cb0f72c5d54f` |

All five upstream bindings were independently resolved from the workspace
root and also match exactly:

| Upstream bound input | Bytes | SHA-256 |
|---|---:|---|
| `BATCH_04_IDEA_REPORT.md` | 18,550 | `1c432d14391f209196ab86e0e3ebd866db2df19efeeb88a90f11264139d125cc` |
| `BATCH_04_STATUS.md` | 13,908 | `0f9dcbd6944bae079ce4416d8bdc577ff635ce4864b415a25abbf143c185baa4` |
| `README.md` | 4,448 | `56d83385facdad0c99f17b757d24d0e03a0025d7a3d7f87a4d0432a28c18c079` |
| `docs/candidate_registry.md` | 7,394 | `786b55185ff6a050d66b2cae2d5cafb4e05e184ced023362ebb9dd377667f006` |
| `papers/13-henon-primitive-cycle-cover/paper/reviews/final_integrity_review.md` | 16,396 | `5896285e99d7ac551c44f8e0215e1202193535a70603a87b531180a97a138748` |

Before this report was written, the project contained exactly fourteen
regular files: the thirteen local bound inputs and the lock. It had exactly
three directories below the project root (`experiments`, `notes`, and
`refine-logs`), zero symbolic links, and no unbound regular file. The future
review path was absent. The forbidden `code`, `figures`, `manuscript`,
`output`, `paper`, `results`, and `source` directories were absent.

Thus the declared counts of thirteen local inputs, five upstream inputs,
eighteen non-self bound inputs, and nineteen artifacts when the lock itself
is included are coherent.

## Theorem and quantifier gate

The lock and theorem-bearing inputs agree on the exact statement. Let (K)
be any field of characteristic zero, let (d\geq2) be an integer, let
(a,b,c\in K^\ast), and let Γ be any finite-rank subgroup of (K^\ast)
of rank (r). Finite generation is not assumed. For

\[
H(x,y)=(b x^d+a y+c,x)
\]

and

\[
T_m(H,Γ)=
\{P\inΓ^2:H^j(P)\inΓ^2\text{ for every }0\leq j\leq m\},
\]

the locked upper bound is

\[
\#T_4(H,Γ)
\leq
4d\exp\!\bigl(18^9(3r+1)\bigr)+81d^2.
\]

The indexing convention is unchanged: (T_4) has five states and four
transitions, furnishing local recurrence equations at indices (0,1,2,3);
(T_3) has four states and three transitions. Shifting the definition to
(0\leq j\leq m-1) would be false for the claimed (T_4) theorem and is
expressly excluded.

For every (d\geq2), the lock also correctly states the existential
rank-one sharpness family with

\[
b=1,\quad a=-1,\quad c^{d-1}=-1,\quad
K=\mathbb Q(c),\quad Γ=\langle2,c,-1\rangle,
\quad P_t=(t,t^d),\quad t=2^n,
\]

which gives infinitely many points of (T_3(H,Γ)). The periodic
corollary counts only exact-period orbits whose whole orbit is contained in
(Γ^2), and its weighted sum has the same upper bound. No theorem is
claimed for a periodic orbit having only one representative in (Γ^2).

## Independent proof replay

### Fixed-coefficient ESS part

Writing (H^j(P)=(x_j,x_{j-1})) gives

\[
x_{i+1}=b x_i^d+a x_{i-1}+c
\]

and the fixed-coefficient equation

\[
\frac1c x_{i+1}-\frac bc x_i^d-\frac ac x_{i-1}=1.
\]

The variable triple
((x_{i+1},x_i^d,x_{i-1})) lies in (Γ^3), whose rank is (3r).
The scalars (1/c,-b/c,-a/c) are arbitrary fixed nonzero coefficients;
they need not lie in (Γ), and no coefficient-enlarged group is used.
Evertse--Schlickewei--Schmidt, published Theorem 1.1, therefore gives at
most

\[
E(3,3r)=\exp\!\bigl(18^9(3r+1)\bigr)
\]

nondegenerate triples at one index. Each triple fixes (x_i^d), so at most
(d) values of (x_i) remain. Since (a\ne0), (H) is an automorphism,
and (P\mapsto H^i(P)) is injective. The union over the four indices is at
most (4dE(3,3r)).

### Degenerate part

The three nonzero ESS summands show that local degeneracy is exhausted by

\[
\begin{aligned}
A_i&:a x_{i-1}+c=0,\\
B_i&:b x_i^d+c=0,\\
C_i&:b x_i^d+a x_{i-1}=0.
\end{aligned}
\]

An independent derivation of all nine adjacent transitions gives bounds

\[
\begin{array}{c|ccc}
&A&B&C\\ \hline
A&1&d^2&d^2-1\\
B&\text{free}&d^2&d^2\\
C&1&\text{free}&1
\end{array}
\]

with the fixed index direction in the package. Hence only `BA` and `CB` can
carry a free parameter.

For `BA`, the compatibility (b(-c/a)^d=-c) leaves one parameter, but
`BAA`, `BAB`, and `BAC` impose equations of degree at most (d^2); every
branch closes at the third letter. For `CB`, the compatibility is
(bc^{d-1}=-1). The `CBB` and `CBC` extensions impose degree-(d)
equations, while `CBA` remains free only when (a=-1). Under
(a=-1) and (bc^{d-1}=-1), the fourth labels `CBAA`, `CBAB`, and
`CBAC` impose equations of degree at most (d^2). Thus every word in
({A,B,C}^4) has at most (d^2) initial states, giving (81d^2).

If two labels hold at one index, the normalized summands are a permutation
of ((-1,1,1)). Triple degeneracy is impossible in characteristic zero.
Choosing any valid label covers every fully degenerate point; multiple
labels only overcount the union. No short-period correction is needed because
the proof never assumes that the five states are distinct.

Finally, direct substitution in the rank-one family gives

\[
H(P_t)=(c,t),\qquad
H^2(P_t)=(-t,c),\qquad
H^3(P_t)=((-t)^d,-t),
\]

and (c,-1) are torsion while (2) is non-torsion. The construction and
the weighted whole-orbit periodic corollary therefore replay exactly as
locked.

## Citation-repair and novelty gate

The review chain is coherent. The initial mathematical source-design review
is frozen at

`e3dc9864c72d150e0f7a69d08aad9f4e24f0dde1c6115fe3d428b129ade4573c`.

The later citation-precision audit is frozen at

`7e625c593267545088320459b65e990fdea5e347ed779416a6ce334d5a131f17`.

It retained the proof but required citation repairs R1--R5. The narrow R2
review at

`8bde838d4bd18426f291eb793f5c822fbd6d70d604fc7097c5761c02bb309ef0`

verified those repairs and returned `SOURCE_DESIGN_PASS`. The proof package
remained byte-identical throughout.

Independent checks against the primary sources confirm the corrected scope:

- Evertse--Schlickewei--Schmidt supplies the finite-rank,
  fixed-coefficient nondegenerate bound and is the only imported proof
  theorem;
- Bell--Ghioca Theorem 1.1(i)--(ii) concerns the return times of one fixed
  orbit of a rational self-map of a semiabelian variety to a finitely
  generated subgroup. The regular clause replaces the Banach-density-zero
  residual set by a finite set; it does not make the arithmetic-progression
  part disappear or supply an all-initial-state count;
- Kim--Krieger--Postolache--Szeto Theorem A is for odd (d>2), uses a
  general rational polynomial (s_d) of degree at most (d), and gives at
  least ((d-4)^2) rational periodic points. Theorem B, for
  (d\equiv1\pmod6), gives an integer cycle of length ((8d+10)/3). This
  is not the monomial-plus-constant Paper 14 family; and
- Mello--Yasufuku Theorems 1.1--1.2 and Corollary 1.3 require
  \(\mathrm{Hyp}_\epsilon\) with ε at least ((1+c)/2), whereas
  Theorem 4.2, under additional divisor hypotheses and Vojta's Main
  Conjecture, yields the relevant non-density only for sufficiently small
  ε. It therefore does not verify the general main hypothesis.

The Bell--Ghioca V7A insertion and the corrected Kim and Mello--Yasufuku
roles are present in `CITATION_VERIFICATION.md`, `NOVELTY_ASSESSMENT.md`, and
`FINAL_PROPOSAL.md`. Boundary theorem numbers are recorded without importing
those results into the proof.

A fresh targeted primary-source search found no direct theorem combining the
three-coefficient monomial Hénon family, arbitrary finite-rank multiplicative
groups, an all-initial-state coefficient-uniform four-transition cardinality
bound depending only on degree and rank, and rank-one failure at the
immediately shorter window. This is only a bounded search conclusion through
2026-08-16, not an absolute priority claim. The locked novelty score of
`7.0/10` remains advisory and is not theorem evidence.

The nonclaim boundary is preserved: there is no claim for all rational or
integral periodic points, one-representative orbit intersections, arbitrary
polynomial Hénon maps, (d=1), positive characteristic, zero coefficients,
optimal constants, effective enumeration, height bounds, a complete
(T_2/T_3) classification, periodicity of the sharp family, computational
verification, or the separate Paper 15 quartic candidate.

## Lifecycle gate

Exactly ten prelock design files retain the historical header

`SOURCE_DESIGN_DRAFT / PENDING_INDEPENDENT_REVIEW / NO_CODE / NO_RESULTS / NO_MANUSCRIPT`.

The bound upstream dashboards retain their historical source-lock-authoring
snapshot. These are provenance, not competing current authorities. The
current lifecycle authority is the frozen lock, with status

`SOURCE_LOCKED / PENDING_INDEPENDENT_SOURCE_LOCK_REVIEW / NO_CODE / NO_RESULTS / NO_MANUSCRIPT`.

No scientific experiment, scan, result, code, figure, paper, or manuscript
exists in the project. This review certifies the source lock only and does
not alter any authorization boolean or authorize a downstream artifact by
itself.

## Final disposition

All required gates pass: canonical JSON safety, exact self identity, all
eighteen input hashes and byte counts, exact inventory, reviewer
independence, theorem quantifiers, window semantics, ESS applicability,
degeneracy closure, sharpness, whole-orbit periodic semantics, citation
repair history, novelty boundary, nonclaims, and lifecycle authority.

The exact canonical verdict is

**SOURCE_LOCK_PASS**
