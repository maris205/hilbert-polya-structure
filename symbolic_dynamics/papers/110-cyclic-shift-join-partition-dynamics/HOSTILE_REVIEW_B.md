# Independent cross-hostile review B — P110

Audit date: 2026-08-29 UTC.  This is a team-internal independent audit, not
an external referee report.  The reviewer did not author P110.  No novelty,
priority, submission, or release endorsement is implied.

Verdict: **GO_INTERNAL / HOLD_EXTERNAL**.  CRITICAL: 0.  Mathematical MAJOR:
0.  Repaired owner/scope MAJOR: 1.  Repaired MINOR: 2.

## Independent theorem reconstruction

### Time convention and invariant endpoint

With refinement order, `J(pi)=pi join rho(pi)` coarsens `pi`.  Since `rho`
is a lattice automorphism, induction gives the exact time convention

```text
J^t(pi) = join_(j=0)^t rho^j(pi).
```

Thus time zero contains one translate, time `n-2` contains `n-1`
translates, and time `n-1` contains the full cyclic orbit.  For every
within-block pair `x,y`, translating by `-y` joins zero to `x-y`; translating
again joins every vertex to its coset modulo the subgroup `H(pi)` generated
by all such differences.  Conversely every translated edge has difference
in `H(pi)`, so it cannot cross an `H(pi)`-coset.  The endpoint is exactly the
coset partition `Q_H(pi)`.

A fixed partition satisfies `rho(pi)<=pi`.  Relabelling preserves its number
of blocks, so equality holds and the partition is cyclically invariant.  In
the regular cyclic action the block of zero is a subgroup and all blocks are
its cosets.  Monotone coarsening rules out nontrivial cycles.  Hence every
positive iterate fixes the same `tau(n)` coset partitions and

```text
zeta_J(z)=(1-z)^(-tau(n)).
```

### Möbius--Bell basins

Fix the unique subgroup `H` of order `h|n`.  The condition `H(pi)<=H` is
equivalent to every block of `pi` lying inside one `H`-coset.  The `n/h`
cosets can be partitioned independently, giving `B_h^(n/h)` partitions whose
endpoint subgroup has order dividing `h`.  If `b_n(d)` is the exact basin of
the order-`d` endpoint, then

```text
B_h^(n/h) = sum_(d|h) b_n(d).
```

Divisor-lattice Möbius inversion therefore yields

```text
b_n(h)=sum_(d|h) mu(h/d) B_d^(n/d).
```

This checks the exponent, divisor orientation, `h=1` basin of size one, and
prime case `B_p-1`.

### Sharp time and the deepest shell

For a chord of difference `d`, put `g=gcd(d,n)` and `ell=n/g`.  When
`ell>=3`, all translates form `g` disjoint `ell`-cycles, so deleting one
translated edge preserves every component.  When `ell=2`, each undirected
edge occurs twice, so one omitted translate is again redundant.  Therefore
the first `n-1` translates, namely `J^(n-2)`, already give the endpoint.

For the converse, a component cut at time `n-3` makes each initial chord
`{a,a+d}` admissible through translates `0,...,n-3`.  Its defect set

```text
D_d(f)={x:f(x)!=f(x+d)}
```

is contained in `{a-2,a-1}`.  Every `d`-cycle has an even number of binary
changes.  If `gcd(d,n)>1`, the two possible defects lie in distinct cycles,
so both disappear and the cut has the nonzero period `d`.  If `d` is a unit,
the unique Hamilton cycle has exactly the two defects.  The cut is one
proper interval in that cycle and has trivial translational stabilizer.

For uniqueness, let `s` be the interval size and `q=d^(-1) mod n`.  The two
defect starts differ by one in ordinary cyclic order and hence by `q` steps
in the `d`-cycle.  Thus `s` is `q` or `n-q`, so the undirected difference is
forced by `d=+/-s^(-1)`.  The two boundary edges then fix the initial edge as
their translate by two.  Consequently a deepest state cannot contain a
second primitive chord; it cannot contain a nonprimitive chord either,
because that would give the cut a nonzero stabilizer.  Since a partition
block contributes all of its internal chords, the state is exactly one
primitive two-element block plus singletons.  Counting oriented pairs and
dividing by reversal gives `n*phi(n)/2`.  The separate endpoints `n=1,2`
are fixed at time zero.

## Findings and implemented repairs

### MAJOR (owner/scope) — the endpoint mechanism was not fully subtracted

The draft cited invariant-partition and orbit-coherence literature, but its
residual-scope sentence still included the endpoint package without saying
that the least invariant coarsening, cyclic coset classification, and
join/generated-subgroup correspondence are background mechanisms.  That
left too much apparent credit on a direct structural corollary.

The manuscript, README, and claims ledger now explicitly subtract these
mechanisms.  The closest verified sources are:

- Marina Anagnostopoulou-Merkouri, R. A. Bailey, and Peter J. Cameron,
  *Permutation groups, partition lattices and block structures*, Forum of
  Mathematics, Sigma 13 (2025), e180, DOI
  [`10.1017/fms.2025.10126`](https://doi.org/10.1017/fms.2025.10126);
- John R. Britnell and Mark Wildon, *Orbit coherence in permutation groups*,
  Journal of Group Theory 17 (2014), 73--109, DOI
  [`10.1515/jgt-2013-0029`](https://doi.org/10.1515/jgt-2013-0029).

Cambridge's official article page explicitly describes the invariant
partition sublattice and the subgroup correspondence; De Gruyter's official
record confirms the orbit-coherence DOI and metadata.  P110 now limits
residual scope to the bounded temporal conjunction of the Möbius--Bell basin
profile with the sharp depth/deepest-shell theorem.  This is not a novelty
certificate, so external release remains HOLD.

### MINOR — abstract overstated functional-graph completeness

“We determine this finite functional graph” was too broad because the paper
expressly does not enumerate every intermediate depth layer or every
one-step fibre.  It now says only that the paper analyzes the functional
graph; the exact items that follow remain unchanged.

### MINOR — internal collision firewall was absent

The main text, README, and claims ledger now distinguish P110 from the two
closest internal systems: P97 iterates nonlinear sumset squaring on subsets
of a prime cyclic group, while P105 prunes labelled permutation cycles.
P110's phase is the full set-partition lattice and its update is a join with
a cyclic relabelling.  Common cyclic notation, Bell numbers, Möbius
inversion, and zeta bookkeeping receive no credit.

## Endpoint and counterexample attacks

- `n=1`: the sole partition is fixed; the maximum depth is zero.
- `n=2`: both partitions are rotation invariant and fixed; this is why the
  formula `n-2` is not used as a deepest-shell classification there.
- Time indexing: `G_(n-3)` uses exactly `n-2` translates, leaving two;
  `G_(n-2)` uses `n-1`, leaving one redundant translate.
- Difference with order two: undirected translated edges occur twice, so
  omitting one translate does not break a component.
- Nonprimitive differences: the two candidate defects lie in different
  translation cycles because their ordinary difference is one and
  `gcd(d,n)>1`; parity eliminates both.
- Primitive uniqueness: reversal changes `d` to `-d` but not the undirected
  chord, and the `+/-` in `d=+/-s^(-1)` accounts for that convention.
- Composite `n` and nontrivial endpoint subgroups: the basin inversion is on
  subgroup orders, not subgroup indices; the literal lanes include all
  composite values through ten and the formula lane through fifty.

No mathematical counterexample was found.

## Fresh exact control and stored-output audit

On the repaired tree I ran

```text
python3 code/verify.py > /tmp/p110-review-b-final.txt
diff -u CONTROL_OUTPUT.txt /tmp/p110-review-b-final.txt
```

The diff was empty.  The canonical output reports:

```text
cyclic shift--join partition dynamics exact control: PASS
assertions=1916206
partitions_enumerated=142417
exhaustive_n=1..10
closed_formula_n=1..50
binary_cut_defect_n=3..12
temporal_mobius_and_zeta_period=1..60
```

This is 1,916,206 exact assertions over every one of the 142,417 partitions
through `n=10`, plus the stated formula and cut lanes.  The union--find
update, accumulated translate join, and direct graph-components realization
are convention-separated.  As an additional hostile-only range attack, I
called the existing cut lane through `n=15`; all 69,548 registered checks
passed.  That extension is not included in the canonical assertion total
and is not an independent proof.

## Four-stage build and PDF inspection

After the repairs I ran `pdflatex -> bibtex -> pdflatex -> pdflatex`.  The
result is:

- 5 A4 pages, 321,815 bytes, PDF 1.5;
- zero undefined citations or references, LaTeX/package/pdfTeX warnings,
  BibTeX warnings, multiply defined labels, and overfull/underfull boxes;
- all 25 font entries embedded, subsetted, and Unicode-mapped;
- 19,498 extracted-text bytes in 271 lines, with no unresolved sentinels;
- all five pages rendered and visually checked: no clipping, overlap,
  malformed formula, orphan reference page, or illegible material.

## Disposition

- Iterate, endpoint, basin, recurrence, zeta, and sharp-depth mathematics:
  **GO_INTERNAL**.
- Exact control and stored finite evidence: **GO_INTERNAL**.
- Owner language after explicit invariant-closure subtraction: adequate for
  internal use.
- External circulation, public posting, specialist contact, novelty, and
  priority language: **HOLD_EXTERNAL** pending specialist owner review and
  later final QA/freeze.
