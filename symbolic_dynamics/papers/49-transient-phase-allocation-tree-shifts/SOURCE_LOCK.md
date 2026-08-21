# Source and Citation Lock

## Purpose

This writer overlay uses only the source boundary already established by the
three immutable proof/audit inputs and a separate primary-metadata check.  It
does not use a citation as a substitute for any theorem proof in the paper.
The bibliography frozen at `paper/references.bib` contains six items and has
SHA-256 `dd27e0b7ae5056347fabae5bf70e572fd41aacd573bfdddc757b5ce7066a875b`.

## Primary metadata ledger

| Citation key / role | Primary bibliographic metadata | Persistent identifier |
|---|---|---|
| Aubrun--Béal, tree-shifts of finite type | *Theoretical Computer Science* 459 (2012), 16--25 | DOI `10.1016/j.tcs.2012.07.020` |
| Petersen--Salama, tree-shift topological entropy | *Theoretical Computer Science* 743 (2018), 64--71 | DOI `10.1016/j.tcs.2018.05.034` |
| Petersen--Salama, entropy on regular trees | *Discrete and Continuous Dynamical Systems* 40(7) (2020), 4453--4477 | DOI `10.3934/dcds.2020186` |
| Ban--Chang--Hu--Wu, reducible tree-shift entropy | *Journal of Differential Equations* 292 (2021), 325--353 | DOI `10.1016/j.jde.2021.05.016` |
| Ban--Chang--Hu--Wu, shifts over integers and trees | *Theoretical Computer Science* 930 (2022), 24--32 | DOI `10.1016/j.tcs.2022.07.007` |
| Ban--Lai--Wu, irreducible Markov hom tree-shifts | *Journal of the London Mathematical Society* 111(6) (2025), e70198 | DOI `10.1112/jlms.70198` |

The independently checked title, author, venue, year, volume, page/article,
and DOI fields agree with the frozen BibTeX.  No unverified URL, private
communication, unpublished priority assertion, or placeholder citation is
present.

## Owner subtraction

- Aubrun--Béal and Petersen--Salama supply field terminology and entropy
  background, not the paper's dimension formulas.
- Ban--Chang--Hu--Wu (2021, 2022) own the neighboring phenomenon that
  reducible tree-shift topological entropy need not be a component maximum.
  The paper does not repackage that entropy result as a contribution.
- Ban--Lai--Wu own the rooted-tree metric and irreducible Hausdorff-dimension
  background.  The writer imports the metric vocabulary only.  It does not
  import any version-sensitive irreducible equality or nonlinear
  Perron--Frobenius clause: the complete-cyclic formula and all transient
  formulas are derived from exact cylinders and a written Frostman argument.
- The residual claims start with the unrestricted one-level phase-allocation
  optimizer, its saturation arithmetic, canonical forced-chain convergence,
  and the explicit Hausdorff cyclic-essential-SCC obstruction.

## Scope and novelty wording

The bounded search found no exact collision with the frozen optimizer and
forced-chain results, but it cannot establish priority.  Accordingly, the
manuscript uses no “first,” exhaustive-novelty, or priority language.  Its
claims are restricted to complete cyclic cores with an unrestricted
one-level feeder, explicitly declared finite-composition one-level variants,
the canonical unrestricted forced chain, and the stated balanced-access
restricted extension.  Arbitrary reducible matrices and arbitrary finite
strict-transient feeder shapes remain outside scope.

## Reference gate

The two-round GPT-5.4/xhigh review identified no missing or incorrect required
reference.  It noted only that a standard Frostman citation would be optional
for a venue that requests one; the paper needs none for correctness because
the full mass-distribution argument is included.
