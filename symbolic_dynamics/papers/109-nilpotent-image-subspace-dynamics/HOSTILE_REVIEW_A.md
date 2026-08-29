# Independent hostile review A — P109

Review date: 2026-08-29 UTC.  Scope: `main.tex`, `references.bib`, all
claim/control/build documents, both verifier entry points, stored stdout, and
the rebuilt PDF.  This is an independent proof and production review, not a
final-QA seal.  External status remains **HOLD**.

## Verdict

**GO_INTERNAL / HOLD_EXTERNAL.**  The theorem package is **PROVABLE AS
STATED**.  My original pass found no critical or major mathematical defect
and repaired one minor collision-firewall omission.  The later independent
review B found a material owner/scope omission, but no mathematical major;
that owner repair and its two minor repairs are incorporated in the current
tree.  Only the explicitly bounded temporal conjunction can carry residual
credit.

## Severity ledger

- **CRITICAL: 0.**
- **ORIGINAL-PASS MAJOR: 0.**
- **ORIGINAL-PASS MINOR: 1, repaired.**  The manuscript distinguished the rejected
  saturation map and a Jordan-block substitution, but did not explicitly
  subtract the nearest P99 and P103 internal neighbours.  I rewrote the
  firewall paragraph in `main.tex` and added matching statements to
  `README.md` and `CLAIMS_EVIDENCE.md`: P73 evolves symbolic substitution
  patterns, P99 applies an invertible shear to fixed-index integer
  sublattices, and P103 applies double adjugation on full matrix space.  None
  shares P109's phase, update, or transient fibre statistic.
- **POST-A CHRONOLOGY: 1 owner/scope MAJOR and 2 MINOR, all repaired by
  review B.**  The current manuscript subtracts Bender--Coley--Robbins--
  Rumsey's dimension-sequence enumeration and Ram's finite-field subspace-
  profile theory, makes the impossible values `r-s<0` and `r-s>t` explicit
  before entering the graph parametrization, and uses a BibTeX name form
  that renders “Howard Rumsey, Jr.” correctly.  These later findings do not
  alter the proof reconstruction below, but they supersede this pass's
  initial owner-search conclusion and production metrics.

## Proof reconstruction

### Iterates, fibres, and transition counts

For `A=N^t`, the restricted map `A|_U` has kernel `U intersect K_t`; hence
`dim(U intersect K_t)=r-s` whenever `dim U=r` and `A(U)=W` has dimension
`s`.  Fixing `R=U intersect K_t`, the exact sequence

```text
0 -> K_t -> A^{-1}(W) -> W -> 0
```

splits linearly.  Modulo `R`, every admissible `U` is the graph of exactly
one map `W -> K_t/R`.  Thus the choices are

```text
[t choose r-s]_q * q^(s(t-r+s)).
```

Multiplication by the number `[d-t choose s]_q` of targets in `im N^t`
gives the stated joint transition formula.  This derivation survives all
zero conventions: `t=0` gives identity fibres; `t=d` permits only `W=0` and
returns `[d choose r]_q`; `r<s`, `r-s>t`, and `W` outside the image give zero.

The second analytic route is genuinely separate.  Slicing by a hyperplane
containing a fixed `t`-space gives

```text
C(d,t;r,k)=C(d-1,t;r,k)+q^(d-r) C(d-1,t;r-1,k).
```

The coefficient is the exact difference between all lines in `V/U_0` and
those in `H/U_0`.  Gaussian Pascal solves this recurrence as
`[t choose k]_q [d-t choose r-k]_q q^((t-k)(r-k))`; setting `k=r-s`
recovers the transition formula without the quotient-graph parametrization.

### Absorption, recurrence, and rigidity

`N^t(U)=0` is equivalent to `U <= ker N^t`.  A regular nilpotent block has
kernel dimension `min(t,d)`, so the absorption CDF is exactly
`G_min(t,d)(q)` and successive differences give all layers.  A cyclic top
line is not absorbed before time `d`, proving sharpness.

If `T^n(U)=U`, then `N^(mn)U=U` for every `m`; choosing `mn>=d` forces
`U=0`.  Thus every iterate has one fixed point and the formal Artin--Mazur
series is `(1-z)^(-1)`.  Conjugacy preserves the absorption layers: their
last index recovers `d`, and for `d>=2` their CDF at time two is
`G_2(q)=q+3`, recovering `q`.  At `d=1` every field yields the same two-state
map, exactly as stated.

## Ownership and collision attack

My initial exact-phrase search for an induced nilpotent image dynamics on the
full finite-field subspace lattice did not locate a direct owner of the full
temporal map.  Review B subsequently found the closer dimension-sequence and
subspace-profile literature of Bender--Coley--Robbins--Rumsey and Ram.  The
current manuscript cites and subtracts both, in addition to the invariant-
subspace owners Brickman--Fillmore and Fripertinger and the Gaussian-
enumeration background of Goldman--Rota and Prasad.  No credit is assigned to
regular-nilpotent profile enumeration.  The residual claim is limited to the
combined pointed-fibre, local functional-graph, absorption, periodic, and
recovery package.  Neither search pass is a novelty certificate; status
therefore remains **HOLD**.

The P1--P106 collision gate was rechecked against the closest systems:
P73 (symbolic Jordan-block substitution), P99 (bijective arithmetic
sublattice shear), and P103 (double-adjugate matrix dynamics).  Their phase
spaces, update rules, and headline invariants are all distinct at the system
level.

## Exact-control replay

From the paper directory I ran:

```text
python3 code/verify.py > /tmp/p109-fresh.txt
diff -u code/verification_output.txt /tmp/p109-fresh.txt
```

The diff was empty.  The final line is `PASS: 515,379 exact assertions`.
All 28 RREF lanes, including `F_4`, `F_8`, `F_9`, and `F_16`, reproduced.
The literal side materializes subspaces and applies the Jordan shift; it does
not call either analytic proof.  Python syntax checks passed for both scripts.

## Build and PDF replay

After review B froze its repairs, I reran the exact control (again obtaining
an empty byte diff and 515,379 assertions) and the complete sequence
`pdflatex -> bibtex -> pdflatex -> pdflatex` on the current tree.  Result:

- 5 A4 pages, 302,089 bytes, PDF 1.5;
- zero undefined citations or references;
- zero LaTeX/package/pdfTeX warnings;
- zero overfull or underfull boxes and zero BibTeX warnings;
- all 22 font entries embedded, subsetted, and Unicode-mapped;
- 17,773 layout-preserving extracted-text bytes in 267 lines and no
  unresolved sentinels;
- all five rendered pages visually checked: no clipping, overlap, malformed
  formulas, malformed bibliography names, or orphan material.

## Residual risks

1. A specialist may regard the temporal package as a short corollary of
   standard finite-Grassmannian intersection counts.  This is an ownership
   and contribution-size risk, not a correctness defect.
2. The paper proves only the regular single-block family.  Its final paragraph
   mentions the general-kernel-dimension fibre extension but expressly does
   not claim a general nilpotent depth theorem.
3. No external release, novelty, or priority conclusion is authorized.

Final decision: **GO_INTERNAL / HOLD_EXTERNAL**.
