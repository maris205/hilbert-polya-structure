# Hostile Review A — P114

## Review status and decision

- Role: independent nonauthor reviewer. I did not participate in this draft.
- Review target: the existing author-stage manuscript and its existing support files.
- Review-B firewall: no Review B file was read or used.
- Provisional decision: **GO_INTERNAL_AFTER_REPAIR**.
- External status: **HOLD**. This review does not authorize posting, submission,
  priority, or novelty language.

The central enumerative package is mathematically viable, and the fresh exact
control passes. I found no counterexample to the root-set basin formula, the
height CDF, the local fibre formula, the periodic census, or the `n!` deepest
count in its correctly qualified range `n >= 2`. The present text is not ready
even for an internal green light, however, because it makes an undefined claim
on the empty state, makes a false unqualified extremal claim in the abstract,
uses an undefined `h=-1` term for the depth-zero shell, and omits direct temporal
owners for leaf erasure/stripping.

## Reconstruction from the definition

I rebuilt the claims without relying on the verifier.

1. A state is a partial parent map on `S subseteq [n]` whose only directed
   cycles are loops. Every nonempty component therefore has exactly one loop,
   its root. A root is excluded from `L(F)` by definition.
2. If a deleted nonroot leaf `w` points to `p(w)`, then `p(w)` cannot itself be
   a deleted leaf: it has child `w`. Hence restriction of `p` after deletion is
   well defined. Roots are never deleted.
3. For a nonroot vertex `v`, let `H_F(v)` be the largest downward distance from
   `v` to a descendant leaf. Induction from the leaves gives deletion round
   `H_F(v)+1`. Thus, for a nonempty forest, the last deletion time is the maximum
   root-to-vertex distance. Every nonfixed update strictly reduces `|S|`, so
   there are no nontrivial cycles and the endpoint is the edgeless forest on the
   original root set.
4. With a prescribed root set of size `r > 0` and `k` chosen nonroots, the
   all-minors matrix-tree determinant is
   `det((r+k) I_k - J_k) = r(r+k)^(k-1)` for `k >= 1`; `k=0` is the empty
   forest and contributes one. Choosing the `k` labels gives `B_(n,r)`. For
   `r=0`, validity of the parent map forces the unique state to be empty.
5. A fixed marked root with total height at most zero supports no nonroot
   labels, so `A_0=1`. A height-at-most-`h` root supports a labelled set of
   objects `X*A_(h-1)`, hence `A_h=exp(x A_(h-1))`. The product `A_h^r`
   therefore counts a prescribed `r`-root forest of entry time at most `h`.
   There is no EGF offset error: stars first appear in `A_1`, exactly matching
   one peeling round.
6. If `T(F)=G` and `L=V(F)\V(G)`, every new point must be a leaf and must point
   into `V(G)`. Two new points cannot point to one another: the target of such
   an arrow would have a child and survive the parallel update. A new self-loop
   would be a root and also survive. Conversely, the only old vertices that
   need protection are the `s` nonroot leaves of `G`; each must receive a new
   child. Inclusion-exclusion on functions `L -> V(G)` that hit those `s`
   vertices, followed by the binomial sum over `L`, gives
   `sum_j (-1)^j binom(s,j)(m-j+1)^(n-m)`.
7. Fixed points are precisely the edgeless forests on subsets of `[n]`, so
   every iterate has `2^n` fixed points and the zeta function is
   `(1-z)^(-2^n)`. For `n >= 2`, depth `n-1` forces a single component using all
   labels and having no branch, hence a rooted Hamilton path. Ordering labels
   from the opposite leaf to the root gives exactly `n!` states.

This reconstruction validates the intended arbitrary-`n` arguments after the
boundary repairs below.

## Targeted hostile boundary audit

| Attack | Result | Reason |
|---|---|---|
| Empty state | **FAIL as written** | The empty forest is allowed, but Theorem 1(i) calls its entry time “the maximum root--vertex distance”; that maximum is over an empty set and no empty-forest height convention is given. The actual entry time is `0`. |
| Roots undeletable / update closed | **PASS** | Roots are excluded from `L(F)`, and the parent of a deleted leaf has that leaf as a child, so it is not simultaneously deleted. |
| Height clock | **PASS for nonempty forests** | Subtree-height induction is correct; define the empty height as zero or state the empty case separately. |
| Cayley basin | **PASS with a boundary proof repair** | The determinant argument is correct for `r>0, k>=1`; the `k=0` empty determinant must be split off instead of invoking a nonexistent all-ones eigenspace of a `0 x 0` matrix. `r=0` has only the empty basin. |
| EGF depth offset | **PASS for CDF; FAIL for shell at `h=0`** | `A_0=1` and `A_h=exp(xA_(h-1))` have the right time indexing. But the displayed “exact depth-`h` shell” uses `B^(h-1)` at `h=0`, while `B^(-1)` is undefined. |
| Can new fibre points point to one another? | **NO; proof is sound** | The pointed-to new point would survive because it has a child. Cycles are disallowed and a new loop would survive as a root. |
| Empty local target | **Formula PASS; exposition incomplete** | Its only predecessor is empty. The per-`L` formula contains `0^ell`; isolate `ell=0`/`L=empty` rather than silently relying on `0^0=1`. |
| `n=0` | **FAIL in abstract only; formulas otherwise PASS after convention** | The only state has depth `0`; the unqualified abstract phrase “maximum depth is `n-1`” would say `-1`. |
| `n=1` | **FAIL in abstract and extremal proof paragraph** | Fresh enumeration gives two depth-zero states (empty and the singleton root), not `1!=1`. Theorem 1(iv) correctly restricts the `n!` claim to `n>=2`, but the abstract and lines 148--152 do not. |
| Deepest `n!` | **PASS exactly for `n>=2`** | The Hamilton-path bijection is correct in that range. |

## Findings by severity

### CRITICAL

None that destroys the central basin/fibre theorem after local repair.

### MAJOR (math)

1. **The empty-state clock is undefined in the main theorem.** At main.tex
   lines 73 and 85--89 the paper both allows the empty forest and quantifies over
   every `n>=0`, but “maximum root--vertex distance” has no value for the empty
   state. Action: define the height/maximum of the empty forest to be `0`, or
   separate `F=empty` in Theorem 1(i), the clock lemma, and the proof.
2. **The abstract's sharp-depth sentence is false at `n=0,1`, and the proof
   silently drops the theorem's `n>=2` hypothesis.** The fresh `n=1` lane is
   `depths={0: 2}`. Action: add “for `n>=2`” in the abstract and at the start of
   the extremal paragraph; explicitly record maximum depth `0` for `n=0,1`,
   with respectively one and two deepest states.
3. **The depth-zero shell is not defined.** Theorem 1(ii) asserts
   `B^(h)-B^(h-1)` without restricting `h`, although `B^(-1)` was never
   defined. Action: set `B_(n,r)^(-1)=0`, or state the difference only for
   `h>=1` and give the depth-zero shell as `B_(n,r)^(0)=1`.

### MAJOR (owner-scope)

1. **A direct temporal owner exists and is absent.** Kovchegov and Zaliapin,
   *Dynamical Pruning of Rooted Trees with Applications to 1-D Ballistic
   Annihilation*, J. Stat. Phys. 181 (2020), 618--672,
   [DOI 10.1007/s10955-020-02593-1](https://doi.org/10.1007/s10955-020-02593-1),
   Example 1, explicitly treats pruning by tree height as unit-speed erasure
   from leaves and records its semigroup property; it in turn identifies older
   tree-erasure ownership. This directly owns the height-clock dynamical
   primitive, although its binary metric-tree setting does not own this
   manuscript's labelled-forest basin/fibre enumeration. Action: cite it and
   subtract height pruning/semigroup dynamics explicitly.
2. Addario-Berry, Brandenberger, Briend, Broutin, and Lugosi,
   *Leaf Stripping on Uniform Attachment Trees*,
   [arXiv:2410.06481](https://arxiv.org/abs/2410.06481), published as
   [DOI 10.1002/rsa.70023](https://doi.org/10.1002/rsa.70023), recursively
   removes all leaves in parallel for a prescribed number of rounds. Its
   unrooted probabilistic root-finding question differs materially, but it is
   a direct recent temporal/terminological neighbor and must be discussed.
3. The labelled height enumeration is older than the generic species
   citations suggest. Rényi--Szekeres,
   [DOI 10.1017/S1446788700004432](https://doi.org/10.1017/S1446788700004432),
   explicitly enumerates labelled trees by height and gives nested functional
   recurrences, building on Riordan. Action: add a primary height-enumeration
   citation and give the EGF, Cayley forest determinant, height clock, and
   inclusion-exclusion zero novelty credit individually. The potentially
   residual claim is only the exact conjunction for this chosen finite phase.

### MINOR

1. In the matrix-tree proof, treat `k=0` as the empty determinant before the
   eigenvalue sentence; its stated `(k-1)`-dimensional complement is otherwise
   nonsensical at `k=0`.
2. In the local-fibre proof, dispatch `m=0` explicitly before (4.1). This avoids
   an unstated `0^0=1` convention and makes “empty target has only itself” a
   proof rather than an afterthought.
3. Once the owner repairs are made, replace “specialist priority search remains
   open” with a reproducible statement of what was searched and what was not.
   Search incompleteness is not evidence of novelty.

## Zero-credit ledger and residual scope

The following receive **zero novelty/priority credit** in this review:

- roots survive and leaf erasure is governed by height;
- absence of nontrivial cycles under strict vertex loss;
- the specified-root Cayley forest count and the total phase count;
- labelled-tree height EGFs and coefficient extraction;
- inclusion-exclusion for functions hitting prescribed targets;
- fixed-point-to-zeta conversion;
- the Hamilton-path extremal classification as an elementary consequence of
  height at most `n-1`.

I did not locate, in the bounded search, a primary source stating this exact
ambient-subset finite map together with endpoint-resolved basin sums, all depth
CDFs, and the `(m,s)` local fibre formula. That negative search result is **not**
a novelty finding. The only defensible residual scope at this stage is the
conjunction and organization of those elementary/classical parts.

Direct temporal owner found: **YES for the height-pruning primitive**; **not
found for the exact labelled finite-map conjunction in this bounded audit**.

## Fresh exact-control audit

Executed from the repository root:

```text
fresh=$(mktemp /tmp/p114_verify.XXXXXX.txt)
python3 papers/114-rooted-forest-leaf-peeling/code/verify.py > "$fresh"
cmp -s "$fresh" papers/114-rooted-forest-leaf-peeling/code/verification_output.txt
wc -l -c "$fresh"
tail -n 2 "$fresh"
```

Results:

- verifier exit: `0`;
- `cmp` exit: `0` — fresh stdout is byte-for-byte identical to stored stdout;
- stdout: 8 lines, 422 bytes;
- terminal assertion: `PASS: 400,105 exact assertions`;
- exhaustive lanes: `0<=n<=6`; the largest contains 26,830 states;
- decisive boundary witness: `n=1: depths={0: 2}`.

The verifier genuinely enumerates valid parent maps, literal updates, endpoints,
depths, all target fibres, and exact rational EGF coefficients. It is strong
falsification evidence. It does not repair the undefined empty maximum or
establish ownership.

## Fresh build, warning/font scan, and all-page visual inspection

The build was performed in an isolated temporary directory so that no author
artifact was changed:

```text
build=$(mktemp -d /tmp/p114_build.XXXXXX)
cp papers/114-rooted-forest-leaf-peeling/{main.tex,references.bib} "$build"/
(cd "$build" && \
  pdflatex -interaction=nonstopmode -halt-on-error main.tex && \
  bibtex main && \
  pdflatex -interaction=nonstopmode -halt-on-error main.tex && \
  pdflatex -interaction=nonstopmode -halt-on-error main.tex)
rg 'LaTeX Warning|Package .*Warning|Overfull|Underfull|Font Warning|undefined references|multiply defined' "$build/main.log"
pdffonts "$build/main.pdf"
pdftoppm -png -r 150 "$build/main.pdf" "$build/page"
```

Results:

- all four LaTeX/BibTeX stages exited `0`;
- PDF: 3 A4 pages, PDF 1.5, 305,536 bytes;
- final log: 0 warnings, 0 overfull boxes, 0 underfull boxes, 0 undefined
  citations/references;
- BibTeX diagnostics: 0 warnings/errors;
- all reported fonts are embedded and subsetted; all three pages were rendered
  and inspected at 150 dpi;
- visual result: no clipping, collision, missing glyph, blank page, or malformed
  display. The theorem's continuation onto page 2 is readable. Page 3 has ample
  white space but no production defect.

## Bounded owner-search record

The audit used exact-title/phrase searches for `parallel leaf peeling`, `leaf
stripping rooted tree height`, `dynamical pruning rooted trees`, `tree erasure
from leaves`, `labelled trees height generating function`, and the exact local
fibre vocabulary, restricted where possible to publisher pages, DOI records,
and author/arXiv primary texts. I followed only the immediate reference trail
from the direct pruning and height sources. This was a bounded audit, not a
systematic-review claim.

## Repair gate

Internal GO requires all of the following:

1. define the empty-state height/entry-time convention;
2. correct the `n=0,1` extremal wording in the abstract and proof;
3. define the depth-zero shell convention;
4. isolate `k=0` and the empty local target in their proofs;
5. cite and subtract the direct height-pruning/leaf-stripping owners and a
   primary labelled-height source;
6. retain external **HOLD** and make no novelty inference from the bounded
   search.

After those repairs, I see no mathematical reason to stop the internal draft.
