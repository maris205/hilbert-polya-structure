# Independent cross-hostile review A — P110

Audit date: 2026-08-29 UTC.  This is an independent team-internal audit of
the post-Review-B tree, not an external referee report.  The reviewer did not
author P110.  No novelty, priority, submission, or public-release endorsement
is implied.

Verdict: **GO_INTERNAL / HOLD_EXTERNAL**.  CRITICAL: 0.  Mathematical MAJOR:
0.  Unresolved MAJOR: 0.  Repaired MINOR: 2.

## Independent theorem reconstruction

### Join convention, exact iterates, and subgroup endpoint

The manuscript orders partitions by refinement, so `pi join sigma` is the
least common coarsening.  Thus `J(pi)=pi join rho(pi)` moves monotonically
upward.  Because relabelling by `rho` is a lattice automorphism,

```text
J^t(pi) = join_(j=0)^t rho^j(pi).
```

This fixes the potentially dangerous off-by-one convention: time `t` uses
exactly `t+1` consecutive translates.  Joining all `n` translates identifies
zero with every within-block difference and therefore with the subgroup
`H(pi)` they generate.  Every translated edge has a difference in `H(pi)`, so
the join cannot cross an `H(pi)`-coset.  The endpoint is exactly `Q_H(pi)`.

If `J(pi)=pi`, then `rho(pi)<=pi`; equal block counts force equality.  A
rotation-invariant partition for the regular cyclic action has a subgroup as
its zero-block and all its other blocks are cosets.  Monotone coarsening rules
out nontrivial temporal cycles.  Hence the recurrent set consists of the
`tau(n)` coset partitions, every positive iterate has `tau(n)` fixed points,
and

```text
zeta_J(z) = (1-z)^(-tau(n)).
```

### Subgroup order, Möbius direction, and Bell basins

The basin parameter `h` is the **order** of the endpoint subgroup, not its
index.  The order-`h` subgroup has `n/h` cosets, each of size `h`.  A partition
whose generated subgroup is contained in it is precisely an independent
partition inside each coset, so

```text
F_n(h) = B_h^(n/h) = sum_(d|h) b_n(d).
```

Divisor-lattice Möbius inversion therefore has the direction printed in the
paper:

```text
b_n(h) = sum_(d|h) mu(h/d) B_d^(n/d).
```

The endpoint checks are consistent: `b_n(1)=1`; `b_p(p)=B_p-1` for prime
`p`; and summing the exact basins over `h|n` gives `B_n`.

### Sharp upper depth

For a chord of difference `d`, put `g=gcd(d,n)` and `ell=n/g`.  Its full
translate graph is a union of `g` cycles of length `ell`.  If `ell>=3`, the
first `n-1` translates omit one edge of one cycle and leave that component
connected.  If `ell=2`, every undirected edge occurs twice, so omitting one
translate removes no edge.  Consequently `J^(n-2)(pi)` is already terminal
for every `n>=3`.

### Two-defect lemma and deepest-shell converse

Assume a nonconstant cut `f=1_S` admits a chord `{a,a+d}` through shifts
`0,...,n-3`.  Its defect set

```text
D_d(f)={x:f(x)!=f(x+d)}
```

is contained in `{a-2,a-1}`.  Every cycle of `x -> x+d` contains an even
number of binary changes.  When `gcd(d,n)>1`, the two candidate defects lie in
different cycles because their difference is one, so both vanish and `d` is
a nonzero period of the cut.  When `d` is a unit, there is one Hamilton cycle;
nonconstancy and parity force both defects.  The cut is then one proper
interval of that cycle and has trivial translational stabilizer.

For uniqueness, let `s=|S|` and `q=d^(-1) mod n`.  The two defect starts are
one ordinary step apart, hence `q` steps apart in the `d`-cycle.  The two
interval sizes are `q` and `n-q`, so `s` is one of them and

```text
d = +/- s^(-1) mod n.
```

This fixes the undirected difference.  The two boundary edges then fix the
initial chord by shifting them forward two places.  Reversing orientation
does not create a second chord.

If a state has depth `n-2`, a component of its time-`n-3` graph is a proper
piece of one terminal coset and supplies such a cut.  If all initial chords
were nonprimitive, the cut would be invariant under their generated subgroup,
contradicting that proper containment.  Hence a primitive chord occurs.  Its
trivial cut stabilizer excludes every additional nonprimitive chord, and
uniqueness excludes another primitive chord.  Since each block contributes
all internal chords, the initial partition is exactly one primitive
two-element block and singletons.

### Unordered count and small parameters

For `n>=3`, there are `n*phi(n)` oriented pairs `(a,d)` with `d` a unit.  The
only two representations of the same undirected chord are `(a,d)` and
`(a+d,-d)`.  A primitive element cannot have order two when `n>=3`, so there
is no exceptional self-reversal and the count is `n*phi(n)/2`.

- `n=1`: the unique partition is fixed, so maximum depth is zero.
- `n=2`: both partitions are rotation invariant and fixed; the deepest-shell
  count is two, and the primitive-chord formula is correctly not asserted.
- `n=3`: a primitive atom changes between times zero and one, giving depth
  one and three deepest states.
- The order-two chord lane for even `n` is covered by the duplicated-edge
  case in the upper-bound proof.

Thus the complete maximum-depth statement is
`max_pi tau_n(pi)=max(0,n-2)`, with the primitive-chord classification exactly
for `n>=3`.

## Findings and implemented repairs

### MINOR — unsupported global open-problem wording

The conclusion previously said that the noncyclic regular-action analogue
“remains open.”  A bounded search cannot certify a global open problem.  The
sentence in `main.tex` now describes that extension only as a natural next
problem.  No theorem or proof changed.

### MINOR — same-batch collision firewall was incomplete

The post-Review-B package explicitly separated P110 from P97 and P105 but did
not record all four neighbouring systems in P107--P111.  `README.md` and
`CLAIMS_EVIDENCE.md` now state the full action-level firewall:

- P107: annihilator--power dynamics on residue-ring ideals;
- P108: capped Fibonacci dynamics on an integer square;
- P109: nilpotent-image dynamics on finite-field subspaces;
- P110: cyclic relabelling followed by join on the full set-partition lattice;
- P111: a random positive-Heisenberg word-area cocycle.

P97 acts on subsets by nonlinear sumset squaring and P105 acts on labelled
permutations by cycle-minimum pruning.  Shared lattice language, cyclic
labels, Bell numbers, Möbius inversion, transient clocks, or zeta bookkeeping
are noncredit-bearing.  No internal action is a parameter variant of P110.

## Owner and bibliography audit

The four bibliography records and their stated scopes were checked against
publisher or primary records.

- The Cambridge article page for Anagnostopoulou-Merkouri, Bailey, and Cameron
  confirms DOI
  [`10.1017/fms.2025.10126`](https://doi.org/10.1017/fms.2025.10126), the
  invariant-partition/subgroup correspondence, and that join corresponds to
  generated subgroup.  P110 correctly assigns those mechanisms to
  background.
- The De Gruyter Brill record confirms Britnell--Wildon, *Orbit coherence in
  permutation groups*, Journal of Group Theory 17 (2014), 73--109, DOI
  [`10.1515/jgt-2013-0029`](https://doi.org/10.1515/jgt-2013-0029), and its
  join/meet coherence scope.
- The Artin--Mazur metadata are correct: *Annals of Mathematics* 81 (1965),
  82--99, DOI
  [`10.2307/1970384`](https://doi.org/10.2307/1970384).
- Cambridge confirms Stanley, *Enumerative Combinatorics*, Volume 1, second
  edition, DOI
  [`10.1017/CBO9781139058520`](https://doi.org/10.1017/CBO9781139058520).

Targeted searches for the exact temporal update and for the displayed
Möbius--Bell/depth conjunction found no direct owner.  This negative result is
not exhaustive and supplies neither novelty nor priority.  The existing
structural subtraction is adequate for internal use; specialist owner review
is still required before any external circulation.

## Fresh exact control and stored-output comparison

The canonical verifier passed Python syntax checking and was run twice during
this audit, including once after the scope repairs:

```text
python3 code/verify.py > /tmp/p110-review-a-final-control.txt
cmp CONTROL_OUTPUT.txt /tmp/p110-review-a-final-control.txt
```

The comparison was byte-identical.  The canonical output reports:

```text
cyclic shift--join partition dynamics exact control: PASS
assertions=1916206
partitions_enumerated=142417
exhaustive_n=1..10
closed_formula_n=1..50
binary_cut_defect_n=3..12
temporal_mobius_and_zeta_period=1..60
```

The literal update, accumulated translate join, and direct translated-graph
components are convention-separated.  The exact lanes cover every partition
through `n=10`, all composite subgroup orders in that range, every
nonconstant binary cut through `n=12`, basin convolutions through `n=50`, and
temporal Möbius/zeta recurrences through period 60.  The finite computation is
evidence, not the infinite-family proof.

## Four-stage build, deterministic rebuild, and visual audit

After the repairs I ran

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

and then one additional deterministic `pdflatex` pass.  The two final PDFs
were byte-identical.  The production result is:

- 5 A4 pages, 321,838 bytes, PDF 1.5;
- zero undefined citations or references, LaTeX/package/pdfTeX warnings,
  multiply defined labels, BibTeX warnings, and overfull/underfull boxes;
- 25 of 25 font entries embedded, subsetted, and Unicode-mapped;
- layout-preserving extracted text: 19,535 bytes in 271 lines, with no
  unresolved sentinels;
- all four bibliography entries present and resolved.

All five pages were rendered at 150 dpi and inspected individually.  Page 1
has a complete title/abstract and readable display; pages 2--4 have intact
theorem boxes, equations, proof endings, and page margins; page 5 contains the
complete converse, controls, cautious conclusion, and all four references.
There is no clipping, collision, malformed glyph, orphan reference page, or
illegible material.

## Disposition

- Mathematical theorem package: **GO_INTERNAL**.
- Quantifiers and endpoints, including `n=1,2`: **GO_INTERNAL**.
- Canonical exact evidence and stored stdout: **GO_INTERNAL**.
- Compilation, deterministic rendering, and five-page visual integrity:
  **GO_INTERNAL**.
- External release, public posting, submission, specialist contact, novelty,
  priority, and any global open-problem claim: **HOLD_EXTERNAL** pending
  specialist owner review and later final QA/freeze.
