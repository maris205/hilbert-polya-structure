# P121 Round-Three Independent Signoff

**Date:** 2026-08-30  
**Role:** independent nonauthor follow-up reviewer  
**Internal disposition:** **GO_INTERNAL**  
**External disposition:** **HOLD**

## Scope and conclusion

This was a narrow follow-up after the residual owner-gate rewrite.  I inspected
the current manuscript, bibliography, owner-gate audit, claim/evidence table,
plan, narrative, build record, verifier and all seven rendered pages.  I also
checked the relevant statements against the primary Andriantiana--Wagner--Wang,
Chang--Fuchs, Rosenberg and Disanto et al. ownership record.

The requested repairs are present and mutually consistent.  I found no
remaining round-three fix and no regression in the strict higher-moment theorem,
its hard claim ceiling, the exact verifier, or the reproducible build.  P121 is
therefore suitable for continued **internal** use.  Novelty, priority and
external dissemination remain **HOLD** pending specialist review.

## Owner-gate repairs

### 1. Fixed-tree cardinality marker

**Resolved.**  The manuscript now explicitly credits
Andriantiana--Wagner--Wang for counting antichains of specified cardinality in a
fixed rooted tree (equivalently, the associated root-containing subtree leaf
statistic).  Lemma 3.1 and the surrounding text no longer present that marker as
residual.  The surviving bounded residual is correctly restricted to averaging
the owned marker under the Yule/uniform ordered-history law, deriving

```text
A_z = A^2 + s/(1-z)^2,
```

and solving that averaged equation in the displayed Euler closed form.  This
boundary is stated consistently in the abstract, introduction, Section 3,
conclusion, `README.md`, `CLAIMS_EVIDENCE.md`, `PAPER_PLAN.md`,
`NARRATIVE_REPORT.md`, `BUILD.md`, and `OWNER_GATE_RESIDUAL.md`.

### 2. Arbitrary-order moment identity

**Resolved.**  Proposition 4.1 is now titled “Mechanical all-order moment
interface.”  Its text says that the identity is the one-line binomial expansion
of the directly owned distributional recurrence, assigns it zero contribution
credit, and retains it only as the interface used by the strict continuation
proof.  The abstract, residual list, support documents and conclusion agree:
the all-order identity itself is not claimed as an advance.

### 3. Caterpillar minimum and exact mass

**Resolved.**  Proposition 5.2 is now explicitly a “Fully owned caterpillar
normalization.”  The manuscript credits Disanto et al. for the minimizing shape,
Chang--Fuchs Table 1 for the literal Yule--Harding probability

```text
2^(n-2)/(n-1)!,
```

and Rosenberg for the earlier caterpillar-pattern analysis.  The post-proof
paragraph assigns the entire proposition zero contribution credit.  The
ordered-history derivation is presented only as a translation/control, not as a
distinct residual.  The minimum atom has been removed from the abstract's
residual summary, the introduction's contribution list, and the conclusion's
residual statement.  The support documents make the same subtraction.

## Theorem ceiling and mathematical regression check

**No regression found.**  Theorem 4.2 still makes the precise residual statement
that begins at `r >= 3`:

- the positive radii form a strict ladder `rho_r < rho_{r-1}`;
- `F_r` has local form `1/(rho_r-z) + O(1)`, hence a positive simple pole with
  unit residue;
- positivity, Pringsheim and Cauchy--Hadamard identify the convergence radius
  and give only the exact exponential `limsup`;
- the cases `r=1,2` are retained only as directly owned bases.

The proof still has the needed chain: isolate the forcing `G_r`, obtain its
inverse-square lower bound from the preceding unit pole, apply Sturm comparison
to force a first positive zero of `U_r` before `rho_{r-1}`, use ODE uniqueness to
make that zero simple, and use Pringsheim to rule out a smaller positive
convergence radius.  Remark 4.3 preserves the hard ceiling: for `r >= 3` the
paper does **not** assert uniqueness of a dominant complex singularity or a full
coefficient asymptotic such as `E X_n^r ~ rho_r^(-n)`.  The owned order-one
stronger asymptotic remains clearly separated.

The exact coupling `X_n=R_n+1`, the empty-antichain convention, finite-law
recurrence, marked transform, mean normalization, minimum control, and proof
dependency statement remain intact.  No ownership repair silently broadened a
mathematical claim.

## Mechanical evidence

### Exact verifier

I reran

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
```

from the package.  The output is byte-identical to `code/verify.out` (536 bytes)
and reports:

```text
product_plus_one verifier: PASS
exact assertions: 139,589
history enumeration: every boundary order through n <= 9
finite laws/moments/minimum atom: n <= 12, raw moments r <= 6
moment hierarchy: coefficientwise r <= 6, n <= 60
marked antichains: coefficientwise n <= 60, histories n <= 9
mean Euler linearization: coefficientwise n <= 60
coefficient artifact: byte-parsed and exactly matched through n <= 12
arithmetic: integers and fractions.Fraction only
scope sentinel: r>=3 pole/radius and all ownership claims are noncomputational
```

The sentinel correctly prevents finite computation from being misreported as a
proof of the analytic or ownership claims.

### Isolated four-stage build

I copied the package into a fresh `/tmp/p121-round3-*` directory and ran, in
order,

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The isolated output and all three package snapshots (`main.pdf`,
`main_round2.pdf`, `main_round3.pdf`) are byte-identical:

```text
SHA-256  7a187c9e7152a191fe951bea389d9a40dc56f7988a50e6a134f41547790abd8c
size     395,037 bytes
pages    7 (A4)
refs     12/12 bibliography entries rendered
fonts    30/30 embedded and 30/30 subset
```

The final logs contain no LaTeX/package warnings, undefined citations or
references, overfull/underfull boxes, rerun requests, or BibTeX errors.  The only
matches for generic warning strings are package-identification lines for
`infwarerr` and `rerunfilecheck`, not diagnostics.

### Seven-page visual inspection

I rendered all seven isolated-build pages at 144 dpi and inspected each page.
The title/abstract, theorem displays, long equations, Table 1, dependency chain,
conclusion and 12-entry bibliography are legible and complete.  I found no
cropping, overlap, broken glyphs, blank unintended page, malformed hyperlink,
or visibly unresolved citation.  Page 7's lower whitespace is normal after the
completed bibliography rather than missing content.

## Final gate

**GO_INTERNAL.**  All requested owner repairs are resolved, and no source,
theorem-ceiling, verification or build regression remains.

**EXTERNAL HOLD.**  This signoff is an internal consistency and owner-subtraction
audit, not a novelty or priority certificate.  The two residual claims remain
bounded no-direct-owner findings and require specialist external review before
circulation.
