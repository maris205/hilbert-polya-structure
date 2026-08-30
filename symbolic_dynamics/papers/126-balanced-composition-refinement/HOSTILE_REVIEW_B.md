# Hostile Review B — P126 round-one independent audit

Review date: 2026-08-30.  Role: independent nonauthor Reviewer B.  Reviewed
version: the current round-one source/support package and the frozen artifacts
identified by the hashes at the end of this report.  I read Review A only to
audit its requested repairs; I did not treat Review A's mathematical
reconstruction as evidence for my own.

## Verdict

**GO_INTERNAL.  HOLD_EXTERNAL remains mandatory.**

- **CRITICAL: 0**
- **MAJOR (mathematics): 0**
- **MAJOR (owner/scope): 0**
- **MINOR: 0**

The complete-kernel equivalence, suffix decoder, every-fibre product,
maximum-fibre injection, image bijection and rational OGF all survive an
independent reconstruction, including the empty state and the identity
iterate.  The fresh paper-local verifier made **8,756,710** exact assertions
and its stdout was byte-identical to the canonical transcript.  A separate
cut-set implementation made **116,995** additional assertions without using
the paper verifier.  An isolated four-stage build reproduced the retained PDF
byte for byte.

Review A's two majors and four minors are closed in the current reviewed
bytes.  In particular, the proof-spike provenance labels were briefly
misassigned during this audit, but the current `CLAIMS_EVIDENCE.md` and
`CONTROL_RESULTS.md` now name the three actual artifacts and attach the three
digests in the correct order.  That transient state is not a finding against
the reviewed version.

The strongest remaining objection is one of value and ownership, not
correctness: after the classical rewriting, fragmentation, code, and
restricted-composition interfaces are subtracted, the residual is a compact
elementary conjunction for one literal morphism.  The manuscript states that
ceiling accurately.  The bounded owner search found no direct temporal owner,
but a non-hit is not a novelty certificate; therefore this review authorizes
internal retention only, never posting, priority, or submission.

## 1. Scope and independent reconstruction

For a composition word, the map applies simultaneously to every old part:

\[
  1\longmapsto1,\qquad
  m\longmapsto(\lfloor m/2\rfloor,\lceil m/2\rceil)\quad(m>1).
\]

It preserves total weight.  Every nonfixed update strictly increases word
length, so at fixed positive weight it cannot lie on a nontrivial cycle.  The
only recurrent state is `1^n`; at weight zero it is the empty word `1^0`.
This elementary Lyapunov argument is correct and is not oversold as residual
value.

### 1.1 Codewords and clock

Fix `t>=0`, put `K=2^t`, and let `W_t(m)=Phi^t((m))`.  Splitting a part into
two integers differing by at most one gives:

1. total weight `m`;
2. length `min(m,K)`;
3. final and largest entry `ceil(m/K)`; and
4. `W_t(m)=1^m` exactly when `m<=K`.

The terminal entry follows from the nested-ceiling identity

\[
 \left\lceil {\lceil m/2\rceil\over 2^t}\right\rceil
 =\left\lceil {m\over2^{t+1}}\right\rceil.
\]

If `m>K`, then at every level `j<t` the smallest descendant is at least
`floor(m/2^j)>=2`, so no branch terminates early and all `K` leaves occur.
If `m<=K`, every branch reaches one and weight preservation leaves exactly
`m` symbols.  Hence a nonempty source `a` stabilizes at

\[
  \operatorname{depth}(a)=\lceil\log_2\max_i a_i\rceil.
\]

The maximum over weight `n>=1` is `ceil(log_2 n)`, attained by `(n)`.  The
empty word has depth zero.  Thus the depth-at-most-`t` states are precisely
the compositions with parts at most `K`, counted by `R_K(n)`.  Subtracting
the `t-1` class gives the stated exact layer for `t>=1`.

### 1.2 Complete kernel if and only if

Define `N_K` letterwise by replacing `m<=K` with `m` ones and retaining
`m>K`.  The easy direction is

\[
  \Phi^t(a)=\Phi^t(N_K(a)),
\]

because every small letter has become its weight in ones by time `t`.

For the converse, restrict to the canonical alphabet

\[
  A_K=\{1\}\cup\{K+1,K+2,\ldots\}.
\]

Its image-code alphabet is

\[
  X_t=\{1\}\cup\{W_t(m):m>K\}.
\]

The singleton codeword ends in `1`.  Every long codeword has exactly `K`
symbols and ends in `ceil(m/K)>1`; two long codewords belonging to different
letters have different total weights.  Thus no member of `X_t` is a proper
suffix of another.  More concretely, the right decoder is forced:

- if the unread target ends in `1`, delete that singleton codeword;
- otherwise take the final `K` symbols, let their sum be `m`, and accept the
  block exactly when `m>K` and the block equals `W_t(m)`.

Deletion strictly shortens the unread suffix, so this is an actual terminating
membership algorithm, not merely a uniqueness slogan.  It recovers at most
one canonical source.  Therefore `Phi^t` is injective on canonical forms and

\[
  \Phi^t(a)=\Phi^t(b)
  \quad\Longleftrightarrow\quad
  N_K(a)=N_K(b).
\]

The same-weight hypothesis in the displayed theorem is harmless and in fact
redundant, since equality of images already implies equality of preserved
weights.  At `t=0`, `K=1`, every codeword has length one and the decoder is
the identity, so the argument does not silently assume `t>=1`.

### 1.3 One-run fibre product

Suppose the decoder accepts a target and returns

\[
 z=1^{r_0}m_1 1^{r_1}\cdots m_s1^{r_s},
 \qquad m_i>K.
\]

The complete-kernel theorem reduces the target fibre to `N_K^{-1}(z)`.
Every displayed large letter is forced: a source letter above `K` is retained
literally, while a source letter at most `K` can create only ones in the
normal form.  Inside the `j`-th one-run, a source may be any composition of
weight `r_j` with every part at most `K`.  No grouping can cross a forced
large letter.  The choices are independent, hence

\[
  |(\Phi^t)^{-1}(y)|=\prod_{j=0}^{s}R_K(r_j).
\]

If the decoder rejects, no canonical source and therefore no source exists.
For the empty target the convention `s=0,r_0=0` gives the one-factor product
`R_K(0)=1`, as required.

### 1.4 Maximum fibre

For fixed run weights, concatenate a tuple of restricted compositions of
weights `r_0,...,r_s`.  The cumulative prescribed weights recover every
tuple boundary, including zero-weight empty factors, so this is an injection
into the restricted compositions of weight `sum r_j`.  Appending
`n-sum r_j` ones is then an injection into the restricted compositions of
weight `n`.  Consequently

\[
  \prod_jR_K(r_j)\le R_K\!\left(\sum_jr_j\right)\le R_K(n).
\]

For `y=1^n`, the unique canonical source is `1^n` and every bounded
composition of `n` lifts it, so equality holds.  This validates both the
maximum and its identification with the cumulative depth count.  The
round-zero misuse of “length” in this injection is absent: round one says
“weights” and “total weight.”

### 1.5 Image bijection, OGF, and recurrence

Every source shares its image with its canonical form, and canonical forms
have distinct images.  Thus restriction of `Phi^t` is a weight-preserving
bijection from words over `A_K` to the full `t`-image.  The letter-weight
series is

\[
  x+{x^{K+1}\over1-x}.
\]

The ordinary sequence construction, including the empty sequence, gives

\[
 \sum_{n\ge0}I_{n,t}x^n
 =\frac{1}{1-x-x^{K+1}/(1-x)}
 =\frac{1-x}{1-2x+x^2-x^{K+1}}.
\]

Multiplication by the denominator gives `I_(0,t)=I_(1,t)=1` and, for
`n>=2`,

\[
 I_{n,t}=2I_{n-1,t}-I_{n-2,t}
 +\mathbf 1_{n\ge K+1}I_{n-K-1,t},
\]

with negative-index coefficients zero.  At `t=0`, the `x^2` terms cancel,
leaving `(1-x)/(1-2x)`, so `I_(n,0)=2^(n-1)` for `n>=1` and `I_(0,0)=1`.
When `K>=n`, the only canonical word of weight `n` is `1^n`, giving image
size one.  The Garden count is then the total `2^(n-1)` minus the image size
for positive `n`.  All stated boundary conventions are mutually consistent.

## 2. Review-A repair audit

| Review-A item | Current evidence | Result |
|---|---|---|
| **MAJOR A1:** primary parallel-rewriting/fragmentation/code/restricted-composition subtraction absent | `main.tex` lines 86–101 now names all nine bibliography items by interface, and assigns zero credit to the generic mechanisms, the bounded-part counts/OGFs, and the Chinn–Heubach one-step image | **CLOSED** |
| **MAJOR A2:** P094/P108/P113/P115/P122/P123/P125 firewall absent | `main.tex` lines 109–119 and the support documents state the seven occupied silhouettes and restrict the residual to this literal kernel/run-product/image conjunction | **CLOSED** |
| **MINOR A1:** “lengths” used where integer weights were needed | Theorem 4.1's injection now uses the weights `r_j` and their total weight | **CLOSED** |
| **MINOR A2:** empty and `t=0` conventions incomplete | `R_K(0)=1`, `R_1(r)=1`, the empty decoded word, negative image indices, and the identity OGF/count are explicit | **CLOSED** |
| **MINOR A3:** terminal-marker induction compressed | Lemma 2.1 now displays the nested-ceiling identity and separately proves absence of early leaves for `m>K` | **CLOSED** |
| **MINOR A4:** proof-spike provenance absent | Current `CLAIMS_EVIDENCE.md` and `CONTROL_RESULTS.md` correctly pair REPORT `fe4796...`, verifier `fba237...`, and CANONICAL `c04de4...` with the actual `../../docs/papers122_126_sequence/proof_spikes/` artifacts | **CLOSED** |

All six repairs are substantive in the current package.  No repair changes
the map or inflates the theorem ceiling.

## 3. Owner subtraction: 9/9 audit

I checked the bibliography against primary publisher, journal, author, or
institutional records.  I also searched the literal rule and theorem package
under multiple formulations, including year-qualified 2025–2026 searches:
“synchronous balanced refinement integer compositions,” “balanced splitting
composition morphism iterated fibre,” “canonical kernel composition
morphism,” “suffix decoder iterated image composition,” and “one-run fibre
product.”  No exact temporal owner appeared.  This is a bounded non-hit only.

| Cited source | Directly owned interface and subtraction | Audit |
|---|---|---|
| Lindenmayer–Rozenberg, *Developmental systems and languages*, [ACM DOI](https://doi.org/10.1145/800152.804917) | Simultaneous application of letter rules and the parallel-rewriting/D0L setting | Correctly cited and **zero-credit** |
| Matsoukas, *Stochastic Theory of Discrete Binary Fragmentation*, [publisher DOI](https://doi.org/10.3390/e24020229) | Integer mass split into two integer fragments; generic binary-fragmentation language | Correctly cited as mechanism neighbor and **zero-credit**, not asserted to own the ordered deterministic map |
| Berstel–Perrin, *Theory of Codes*, [publisher record](https://shop.elsevier.com/books/theory-of-codes/berstel/978-0-12-093420-1) | Free-monoid code and unique-decipherability theory | Correct metadata; generic code theory **zero-credit** |
| Honkala, permutation-free morphisms as L-codes, [publisher DOI](https://doi.org/10.1080/00207168708803578) | L-code decidability and ambiguity for morphisms | Correct metadata; generic decoding/ambiguity **zero-credit** |
| Freydenberger–Reidenbach, segmented morphisms, [publisher DOI](https://doi.org/10.1016/j.dam.2009.06.009) | Morphism ambiguity/unambiguity | Correct metadata; generic morphism ambiguity **zero-credit** |
| Heubach–Mansour, compositions with parts in a set, [institutional record](https://cris.haifa.ac.il/en/publications/compositions-of-n-with-parts-in-a-set/) | Parts-in-a-set composition construction and its generic generating functions | Correct metadata; enumeration machinery **zero-credit** |
| Malandro, bounded part sizes, [author deposit](https://arxiv.org/abs/1108.0337) | Bounded-part recurrences, generating functions, and asymptotic toolkit | Correct metadata; all `R_K` enumeration **zero-credit** |
| Banderier–Hitczenko, restricted compositions, [publisher DOI](https://doi.org/10.1016/j.dam.2011.12.011) | Restricted-composition enumeration and analytic context | Correct metadata; surrounding toolkit **zero-credit** |
| Chinn–Heubach, compositions without 2's, [official journal page](https://cs.uwaterloo.ca/journals/JIS/VOL6/Heubach/heubach5.html) | The `t=1` allowed-part image class and its sequence | Direct owner is identified; one-step enumeration **zero-credit** |

The isolated bibliography contains nine `bibitem`s and the auxiliary file
contains nine distinct citation keys: **9/9 closure**.  The defensible
residual is exactly:

1. `N_(2^t)` is the complete equality kernel of every literal iterate;
2. its concrete suffix decoder gives the exact product for each individual
   nonempty fibre and the maximum-fibre/depth-census coincidence; and
3. restriction to canonical forms is the temporal image bijection for every
   `t`.

The restricted-composition recurrence, rational sequence OGF, logarithmic
clock, balanced split, code vocabulary, and the `t=1` no-part-2 sequence are
not residual contributions.

## 4. Internal collision firewall

I checked the cited local packages rather than relying only on P126's
descriptions.

| Prior paper | Occupied silhouette | Why no literal transfer remains |
|---|---|---|
| P094 | marked S-adic morphisms, boundary markers, recognizability | P126 claims no general recognizability theorem; its decoder is the elementary suffix decoder for `W_t(m)` |
| P108 | Fibonacci-named clock and one-step fibre geometry | P126 zero-credits the Fibonacci count and keeps only its literal all-iterate canonical kernel/fibre conjunction |
| P113 | integer-sum carrier, absorption, sharp depth, product-fibre transport | Its map is principal-hook regrouping of partitions; P126's ordered-composition normal form and suffix code are not imported |
| P115 | every iterate, image, fibre, and logarithmic threshold | Its bounded Cartier operator is a finite-field coefficient-chain map; none of its semilinear/Frobenius structure is used |
| P122 | target-local fibre factorization/DP plus image and Garden enumeration | Its carrier is permutations under even record-block reversal; P126's source normal form proves a different run product |
| P123 | component-partition refinement and a refinement-tree clock | Its carrier is labelled graphs under odd-component complementation; generic “refinement” language is explicitly nonvalue |
| P125 | pointwise fibres, image layers, and full functional components | Its carrier is a quadratic-space shear over `F_2`; P126 claims neither that component classification nor its algebraic machinery |

The firewall is accurate.  It also prevents selling absorption, refinement,
normal-form vocabulary, depth, fibres, image layers, or Garden subtraction as
standalone value.  I found no literal internal map collision.

## 5. Fresh exact controls

### 5.1 Paper-local verifier

Run from the paper directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py \
  > /tmp/p126_reviewb_verifier_233703.txt
cmp -s /tmp/p126_reviewb_verifier_233703.txt \
  code/verification_output.txt
```

Results:

```text
balanced composition refinement exact control: PASS
assertions=8756710
verifier_exit=0
canonical_cmp_exit=0
fresh_stdout_sha256=978191ccbc9a120ca34a298ab79f828175a069b7574388823885fb5712bd2090
```

The checked scopes are exactly those reported in the source: literal clocks
through weight 18; kernel maps, targets, decoder, fibres, and maxima through
weight 15 for `t<=5`; codewords through `m<=256,t<=8`; and image recurrence
through weight 90 for `t<=8`.  Inspection of `verify.py` confirms that the
kernel is checked in both directions using `normal -> image` and
`image -> normal` dictionaries, and each literal target fibre is compared
with both the run product and a separate codeword-factorization DP.  The
assertion counter is deterministic and does not count owner claims as proved.

### 5.2 Reviewer-side independent control

I used an ephemeral standard-library implementation that represents a
composition of `n` by its cut subset in the `n-1` internal gaps.  One update
inserts the left middle cut into every old nonsingleton interval.  It did not
import the paper verifier.  It checked:

- codeword length/weight/final marker through `m<=300,t<=7`;
- all states through `n<=12,t<=4`;
- both directions of the canonical-kernel equivalence;
- decoder acceptance and reconstructed canonical source;
- every literal target fibre against the one-run product;
- the all-one maximum and the maximum inequality; and
- the image recurrence through `n<=30`.

Output:

```text
independent cut-set control: PASS
assertions=116995
scope=n<=12,t<=4; codewords m<=300,t<=7; recurrence n<=30
```

These computations are falsification controls; the all-size statements rest
on the proofs reconstructed in Section 1.

## 6. Isolated build, PDFs, fonts, metadata, and visual audit

I copied only `main.tex` and `references.bib` to
`/tmp/p126_reviewb_build_nv8MXg` and ran:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

All four stages returned zero.  The settled log has zero TeX/package/class
warnings, zero overfull or underfull boxes, and no undefined citation,
reference, or rerun request; the BLG has no warning or error.  The isolated
PDF is 4 pages and 319,631 bytes with SHA-256
`e5d7ab3986a635a490804a8a81d7b3873b5c8403456fccf138af30315751ed3e`,
byte-identical to both `main.pdf` and `main_round1.pdf`.

PDF audit:

- `main_round0_original.pdf`: 4 A4 pages, 314,921 bytes, 24 font rows;
- `main_round1.pdf`: 4 A4 pages, 319,631 bytes, 24 font rows;
- every listed font in both PDFs is embedded, subsetted, and Unicode-mapped;
- title, subject, keywords, and author metadata fields are blank; creation and
  modification dates are absent;
- both PDFs are unencrypted, rotation zero, `Form: none`, `JavaScript: no`,
  with no embedded file and no signature;
- `main.pdf` is byte-identical to round one, while round zero remains distinct;
  and
- layout-preserving text extraction contains no `??`, undefined marker,
  draft/reviewer sentinel, TODO, FIXME, or missing-citation token.

I rendered all four pages of each round at 150 dpi and inspected all eight
page images.  Round zero is legible and intentionally sparse on its final
four-reference page.  Round one cleanly accommodates the expanded owner and
firewall discussion and nine references; there is no clipping, overlap,
broken equation, missing glyph, bad running head, isolated heading, or
visually malformed URL.

## 7. Severity-ranked findings

### CRITICAL

None.

### MAJOR (mathematics)

None.

### MAJOR (owner/scope)

None.  The search is bounded, but the manuscript says so and keeps external
release on hold.  All located direct and mechanism owners are subtracted.

### MINOR

None in the current reviewed bytes.  The provenance filename/digest mismatch
seen in an earlier support snapshot is closed by the current
`CLAIMS_EVIDENCE.md` and `CONTROL_RESULTS.md` hashes recorded below.

## 8. Admissible claim ceiling and final disposition

The package may internally retain the exact all-iterate conjunction for this
specific synchronous balanced-composition morphism:

- complete canonical kernel and literal right decoder;
- pointwise one-run fibre product, maximum injection, and its depth-census
  corollary; and
- temporal image bijection and consequent exact image/Garden census.

It may not claim a new parallel-rewriting theory, fragmentation theory,
suffix-code principle, restricted-composition enumeration, Fibonacci family,
divide-and-conquer clock, asymptotic law, novelty, or priority.  Under that
ceiling the provisional decision is **GO_INTERNAL**.  External status remains
**HOLD_EXTERNAL**.

## 9. Reviewed hashes

The verdict applies to these exact inputs:

```text
c93d504af40fbf6e162db4cf3b996457bb7d892ea1ab3e2c8ef89dd7273fd270  main.tex
4272430bd26581c7c6aead83f7ae2cacab37f5177d551e293447a0e071105292  references.bib
28614796f96c547b408058bf204c489a8f19e1d18338635bea25170fa0a0e842  README.md
b5e932841da841994fa6c306f792c3206213b80ddf93a9781d3e62abf64622a9  BUILD.md
d8e3ab53453a770703d6de973ad4d731ff19218f308462500cb405908a319bf7  CLAIMS_EVIDENCE.md
a893751d7bf5b187f16458cd0e12863b0c8539ecd37a7bf1543467f4c1e4d21b  CONTROL_RESULTS.md
9938bccb22053eb7cdd29dffd6c8ddf45c3a3b5271d06ace926292db45df0e79  IMPROVEMENT_LOG.md
3e44958199758c0fb139bc3d0ec821e9da571e499e0585018e1f3dec6f801201  NARRATIVE_REPORT.md
987e2b423dda77c4adb8dbaf75c0360e89ba08342f8f569a9d0f3a1184749886  PAPER_PLAN.md
068f1b47a568421eaa53d779c91daef7705f03210f58ea100c4f8ba6b27109cc  HOSTILE_REVIEW_A.md
5f58da9c3418502d64cd2fc7e3918c9a8bb464c456bc936539bb2afc7ee83ef0  code/verify.py
978191ccbc9a120ca34a298ab79f828175a069b7574388823885fb5712bd2090  code/verification_output.txt
e5d7ab3986a635a490804a8a81d7b3873b5c8403456fccf138af30315751ed3e  main.pdf
d48125fc509fc972b2b705226c33d7915a529523917fd786a5eda2190106ca1e  main_round0_original.pdf
e5d7ab3986a635a490804a8a81d7b3873b5c8403456fccf138af30315751ed3e  main_round1.pdf
06a82a60fe46972e6754a98a868760230efa0deb1bc3c92050ee4abec59d8940  ../../docs/papers122_126_sequence/phase1/HOSTILE_GATE_BALANCED_COMPOSITION_REFINEMENT.md
```

Historical gate inputs independently rechecked from their actual paths:

```text
fe4796bb730ac51c40e3ce2dd36f898ef13910da6ece50561b6a13eacc9f32b7  ../../docs/papers122_126_sequence/proof_spikes/BALANCED_COMPOSITION_REFINEMENT_REPORT.md
fba237ac83d1a6f470f890824406a52b8a6eaa6189d02dca8f31bcfcd12999a2  ../../docs/papers122_126_sequence/proof_spikes/verify_balanced_composition_refinement.py
c04de425fd715d549cdd2bfec5a4dc3a7eaf2c49719076059f2e9fc78b15c3f1  ../../docs/papers122_126_sequence/proof_spikes/BALANCED_COMPOSITION_REFINEMENT_CANONICAL.txt
```
