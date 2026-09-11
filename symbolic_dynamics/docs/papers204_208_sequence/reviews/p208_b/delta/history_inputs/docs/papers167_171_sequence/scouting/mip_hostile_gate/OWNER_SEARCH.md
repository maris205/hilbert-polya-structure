# Bounded primary-source owner search — MIP hostile gate

**Search date:** 2026-09-03 UTC  
**Decision:** `PASS_OWNER_THIN`, never a novelty or priority finding  
**External status:** `HOLD_EXTERNAL`

## 1. Exact object searched

The search froze the convention before querying:

```text
M(f)(i)=the least position j with f(j)=i when i is present,
        i                                    when i is absent,
```

with `M` iterated as a self-map of the complete endofunction set `[n]^[n]`.
This identity-on-missing convention is material.  A source that discusses an
arbitrary extension of a section outside `im(f)` does not own the resulting
iteration unless it also fixes this extension.

## 2. Bounded query log

The web pass used exact, algebraic, word-combinatorial, and dynamical
rewrites.  Representative queries were:

| lane | queries | result |
|---|---|---|
| exact inverse position | `"min f^{-1}" transformation semigroup canonical inverse`; `"least preimage" endofunction iteration finite dynamics`; `"least preimage" pseudoinverse function finite set` | no primary source stating the literal self-map or its iteration |
| kernel transversal | `canonical transversal kernel classes full transformation semigroup inverse`; `"minimum of each kernel class" transformation semigroup`; `"least element of each kernel class" transformation semigroup`; `"minima of the kernel classes" transformation` | direct background owners for kernel transversals and least representatives; no identity-default iteration |
| first occurrence | `"first occurrence" map word transformation semigroup inverse`; `"first occurrence" restricted growth words set partitions paper`; `"iterate" "first occurrence" map endofunction` | direct owners for first-occurrence/RGF and block-minimum encodings; no map on endofunctions |
| inverse dynamics | `"iterated" "kernel transversal" transformation semigroup`; `"dynamics" "inverse transversal" finite transformation`; `full transformation semigroup inverse matching` | inverse/permutation matching and regular-semigroup literature, but its maps are not this nonbijective selector |
| functional graph | `random mapping statistics functional digraph components`; `labelled functional digraph cycles rooted trees exponential generating function` | classical functional-digraph and labelled-species background only |
| exact theorem phrases | `"2n-2" least preimage dynamics`; `Bell maximum fibre first occurrence map`; `path reversal minimum preimage endofunction` | no literal owner hit in the bounded indexed corpus |

Search results were opened at the publisher, repository, DOI, or author
preprint page.  Secondary search-result snippets were used only to locate the
primary records below, not as mathematical authority.

## 3. Primary owners and mandatory subtraction

### 3.1 Transformation-semigroup inverses and transversals

- Peter M. Higgins,
  [*Involution matchings, the semigroup of orientation-preserving and
  orientation-reversing mappings, and inverse covers of the full
  transformation semigroup*](https://doi.org/10.1007/s00233-019-10018-z),
  *Semigroup Forum* 98 (2019), 669--689, studies matchings that send regular
  semigroup elements to inverses and explicitly places the full
  transformation semigroup in that setting.
- Peter M. Higgins,
  [*Finite regular semigroups with permutations that map elements to
  inverses*](https://doi.org/10.1007/s00233-024-10430-0), *Semigroup Forum*
  109 (2024), 141--147, records the inverse-matching/transversal framework and
  the kernel-class organization of `T_n`.
- V. H. Fernandes, G. M. S. Gomes, and M. M. Jesus,
  [*Congruences on monoids of transformations preserving the orientation on
  a finite chain*](https://doi.org/10.1016/j.jalgebra.2008.11.005), *Journal
  of Algebra* 321 (2009), 743--757, explicitly forms the transversal of a
  transformation's kernel from the minimum element of every kernel class.

These sources own the full-transformation carrier, inverse/transversal
language, and the use of least kernel representatives.  They receive zero
credit in any MIP contribution statement.

They do not close the present gate.  `M(f)` is an inner inverse extension in
the one-sided sense `f M(f) f=f`, but generally is not a mutual inverse.  For
`f=(0,0)`, `M(f)=(0,1)` and `M(f) f M(f)=f!=M(f)`.  Nor is `M` a permutation
matching on `T_n`: it has fibres as large as `B_n`.  The specific extension
`M(f)(i)=i` for a missing symbol is exactly what creates the path splits on
later iterations.

### 3.2 First occurrences, block minima, and Bell encodings

Christian Bean, Paul C. Bell, and Abigail Ollson,
[*The Insertion Encoding of Restricted Growth
Functions*](https://doi.org/10.1007/s00026-026-00832-y), *Annals of
Combinatorics* (2026), states the first-occurrence characterization of
restricted growth functions, their bijection with set partitions, and the
standard ordering of blocks by smallest element.  It is a recent primary
check on the exact combinatorial vocabulary used here.

This literature owns first-occurrence encodings and the Bell-number
partition mechanism.  MIP's identity fibre is precisely a block-minimum
labelling and therefore gets no novelty credit merely for producing `B_n`.
The inspected paper does not iterate the vector of first positions with
identity defaults, derive the path reversal/splitting rule, or state the
every-target fibre product.

### 3.3 Functional digraphs, labelled components, and zeta

- Philippe Flajolet and Andrew M. Odlyzko,
  [*Random Mapping Statistics*](https://doi.org/10.1007/3-540-46885-4_34),
  EUROCRYPT '89 / LNCS 434, gives classical functional-digraph component
  language and random-mapping enumeration.
- Michael Artin and Barry Mazur,
  [*On Periodic Points*](https://www.jstor.org/stable/1970384), *Annals of
  Mathematics* 81 (1965), 82--99, owns the periodic-point zeta construction.

Functional-digraph decomposition, labelled `SET`/cycle EGF conversion,
involution numbers, Bell numbers, and the formal zeta conversion are all
background.  The residual can only be the conjunction specific to the
literal selector: component reversal/splitting, sharp clocks, restricted
recurrent species, and target-resolved inverse product.

## 4. Literal non-hit and its limited meaning

No inspected primary record stated all of the following:

1. the minimum preimage selected for every present value;
2. the value itself used as the missing-value default;
3. iteration of that resulting endofunction;
4. the `2n-2` / `2n-3` sharp clock pair;
5. the recurrent path/cycle species; and
6. the every-target product formula with Bell maximum.

This is only a bounded non-hit.  It is not evidence that the map or theorem
package is new, and it is not a freedom-to-operate search.  A specialist
transformation-semigroup check remains mandatory before any external use.

## 5. Owner decision

`GREEN_OWNER_THIN / HOLD_EXTERNAL`.

The exact formulas survive and no direct literal owner was located, so the
candidate need not be killed.  The owner margin is thin because its first
step is a canonical least-transversal inner inverse and its Bell extremum is
a classical block-minimum partition encoding.  Any paper must foreground the
specific *iteration under the identity-on-missing extension* and subtract all
of the ingredients above.
