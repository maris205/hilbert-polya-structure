# P189 Hostile Review A — Round 1

## Verdict

`PASS`

| severity | count |
|---|---:|
| Critical | 0 |
| Major | 0 |
| Minor | 0 |

No actionable mathematical, source, control, or rendered-artifact defect was
found in the bound Round-0 manuscript.  This is a process-separated review,
not a claim that errors are statistically independent and not a novelty or
publication-clearance decision.  `OWNER_AMBER / HOLD_EXTERNAL` remains in
force.

## Immutable material reviewed

```text
main.tex SHA-256:
c9c4417012fcc9663ac3c3ac3fe9f5113fdf4fe4213846d2a6815b7657724457

main_round0_original.pdf SHA-256:
6ba00f6b542fdbefd4789e8f23f2d683c642132e989ff7af828436da063d6a81

live main.pdf SHA-256:
6ba00f6b542fdbefd4789e8f23f2d683c642132e989ff7af828436da063d6a81

references.bib SHA-256:
fbed4d833c2855548bc721b793ad74da2e5fcf994fccbc35e2fdbae74bb1ac4c
```

The verifier hard-fails if either theorem source or Round-0 PDF changes, and
also requires the live PDF to remain byte-identical to the frozen PDF.  No
author file was modified during this review.

## Process and representation firewall

The reviewer did not author P189.  The reviewer-owned implementation imports
no author or scouting module and does not call the author verifier.  Its state
is a tuple of row-support `frozenset` objects, rather than the author's packed
integer matrix.  It performs the literal rule in two explicit stages:
left-compress each row support, then transpose support membership.

Recurrence and depth are not inferred from the proposed normal form.  They are
recovered independently from the complete directed graph by indegree peeling
and reverse breadth-first search.  Actual one- and two-step indegrees are then
compared target by target with separately coded formulas.

Two fresh Python processes reproduced `CANONICAL.txt` byte for byte:

```text
complete binary-matrix carriers: n=1,2,3,4 (66,066 states total)
direct weighted/depth transfers: n=1,...,12
direct partition/conjugation/inverse-mass controls: n=1,...,10
exact assertions: 1,493,113
transition digest:
267b78505e8a5e3feea15c49d05b50cb43511efb0b6742e47e41528915d17c66
verifier SHA-256:
4954766bcdf4a56f15544b7157f1be7afa607b5ea6ab58c419cbb87ab06d5b8b
canonical SHA-256:
7fed29f8dd04c2493772596e788a9763222dc5a31d7be70ecdbef28e8d717139
canonical lines/bytes: 32 / 2,111
```

## Formal claim attack

| target | hostile question | result |
|---|---|---|
| Definition, `main.tex:63–77` | Are labels, transpose direction, row/column indices, and synchronous semantics consistent? | PASS.  Explicit support transposition gives exactly `F(A)_{ij}=1{i<=r_j(A)}` for every state in all complete boxes. |
| Height calculus, `main.tex:90–120` | Can `D` lose labelled information, or can double threshold fail away from partitions? | PASS.  Column supports recover each labelled height, and direct cell-set transposition gives `(h*)*=h_down` for every tested vector. |
| All-time form, `main.tex:122–153` | Do the quantifiers include every `A`, every `n>=1`, and every `q>=1`; is the correct identity really `F^4=F^2`? | PASS.  The first six literal epochs match the stated even/odd phases for every complete state.  The minimal reviewer witness `00/10` at `n=2` falsifies both tempting strengthenings `F^2=F` and `F^3=F`, while satisfying the manuscript's identity. |
| Recurrent set, `main.tex:166–208` | Is cancellation on cycles legitimate; can a non-Ferrers cycle or a period above two survive? | PASS.  Independent indegree peeling returns precisely the Ferrers states, and every nonfixed cyclic state has literal period two.  Counts are `C(2n,n)`, `2^n`, and their residual half. |
| Depth partition, `main.tex:157–216` | Does labelled row order disappear too early; does the coefficient formula count exactly depth at most one; are the extremal examples valid? | PASS.  Reverse graph distance equals the displayed `L_0,L_1,L_2` predicate state by state.  Direct decreasing-partition sums equal the coefficient extraction through `n=10`, and the coefficient transfer reaches `n=12`.  Height is zero only at `n=1` and exactly two thereafter. |
| Time-one fibres, `main.tex:225–252` | Are all targets covered, including holes, zero/full columns, and empty fibres? | PASS.  Every target in each complete carrier is checked against its literal indegree; positivity gives `(n+1)^n` images and the mass is `2^(n^2)`. |
| Time-two fibres, `main.tex:236–265` | Should multiplicities belong to `mu` or `lambda=mu*`; are row assignments labelled; are non-Ferrers fibres really zero? | PASS.  The required row-sum multiset is independently reconstructed as `mu*`.  The multinomial and row-support factors equal every literal two-step indegree, including repeated zeros and boundary shapes. |
| Control claims, `main.tex:269–292` | Do the table, assertion count, ranges, and counterexample claims agree with author artifacts? | PASS.  All displayed rows agree with both complete re-enumeration and the bound author canonical transcript. |
| Scope/declarations, `main.tex:294–317` | Are square, labelled, synchronous, and external-release boundaries explicit? | PASS.  No theorem silently extends to rectangular, asynchronous, sorted-input, random, or unlabelled variants; AI use and `HOLD_EXTERNAL` are disclosed. |

## Boundary and mass audit

- `n=1`: the two matrices are both recurrent and fixed; depths are `(2,0,0)`,
  both image sizes are two, and every fibre has size one.
- `n=2`: complete peeling gives six recurrent states, four fixed states, one
  strict two-cycle, and depths `(6,5,5)`; thus both nonzero depth layers really
  occur at the first allowed dimension.
- Zero and full column-height vectors, repeated heights, unsorted labelled row
  sums, and targets with a hole in a column are all included.
- Fibre mass is checked only after every target equality: both fibre families
  sum to `2^(n^2)` independently.
- The direct second-fibre mass and self-conjugate census were carried through
  every partition in the `n x n` square for `n<=10`.

## Citation and owner attack

The exact four manuscript cite keys equal the four bibliography keys.  The
following primary or authoritative records were rechecked:

- Andrews, *The Theory of Partitions*, Cambridge record and book DOI
  `10.1017/CBO9780511608650`, for partition/conjugation background;
- Miller, *Discrete Mathematics* 313(4), 550–562, DOI
  `10.1016/j.disc.2012.11.027`, for generalized conjugates and line-sum
  criteria;
- Koutecký–Onn, arXiv `2011.09932`, whose primary record gives the title,
  authors, 2020 submission, and 2021 journal reference, for line-sum and
  monotonicity background;
- Das–Das–Sen, *Discrete Mathematics* 339(2), 1028–1051, DOI
  `10.1016/j.disc.2015.10.010`, for established Ferrers-matrix/bigraph
  terminology.

The cited sources own background only, and the manuscript explicitly assigns
that material zero contribution credit.  Formula-level searches included

```text
"transpose row compression" binary matrix Ferrers dynamics
"left-compress" rows transpose binary matrix Ferrers
site:arxiv.org Ferrers matrix row compression transpose dynamics
site:doi.org binary matrix row compression transpose Ferrers
```

The inspected results concerned Ferrers matrices, line sums, unrelated sparse
storage, or unrelated matrix transposition; none stated the literal autonomous
map together with the clock and both fibre laws.  Search coverage is bounded.
This non-hit is not novelty, priority, completeness, freedom-to-operate, or
release evidence.  The owner's amber gate is therefore correctly preserved.

## Rendered and control-artifact audit

The frozen PDF is four A4 pages (`595.276 x 841.89 pt`, 363,099 bytes), with
blank identifying metadata, no encryption, forms, JavaScript, or metadata
stream.  All 29 font rows are embedded, subsetted, and Unicode mapped.  Every
page was rasterized to `1819 x 2573` pixels at 220 dpi in reviewer-temporary
storage and inspected at original resolution.  There is no clipping, overlap,
blank/truncated page, malformed formula or table, broken citation, bibliography
collision, or header/footer/page-number defect.  The short fourth-page
bibliography leaves white space but is neither blank nor defective.

The final author log has no warning, bad box, unresolved citation/reference,
or error.  Earlier first-pass build logs retain expected pre-BibTeX/rerun
warnings; those do not occur in the settled log and do not contradict the
Round-0 receipt.

## Finding ledger

### Critical

None.

### Major

None.

### Minor

None.

The `PASS` verdict applies only to the exact bound Round-0 source/PDF and the
claims actually stated there.  It authorizes no paper repair or external
action.
