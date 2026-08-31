# Hostile Review B — P130 crossing-component fibre geometry

**Role and scope.**  This is an independent, nonauthor second review of the
repaired round-one package in
`papers/130-crossing-component-fibre-geometry/`.  I did not author the paper
or Hostile Review A.  I reconstructed the map, inverse and extremal argument
from `main.tex`, then used Review A only as a re-entry checklist.  I did not
edit the manuscript, bibliography, verifier, canonical transcript, PDFs or
support records.

## Decision

**GO_INTERNAL / HOLD_EXTERNAL.**  The two round-zero proof defects are
substantively repaired.  The all-size inverse now has a valid global gluing
argument, and the exact owner subtraction is strong enough to keep the
residual contribution narrow.  I found no false theorem, missing case or
counterexample.  Two nonblocking wording defects remain in the ownership and
internal-firewall prose; they are listed as MINOR and do not alter any
mathematical conclusion.

| Severity | Count | Decision effect |
|---|---:|---|
| CRITICAL | **0** | no core theorem failure |
| MAJOR | **0** | no unresolved all-size proof or owner-ceiling failure |
| MINOR | **2** | two exactness corrections for the next consolidation |

External posting, priority, novelty, authorship and submission remain
**HOLD_EXTERNAL**.  The bounded owner non-hit is not affirmative novelty
evidence.

## Strongest counter-argument and result of the attack

The strongest attack is that the displayed product could be an artefact of
the exhaustive `n<=7` constructor: local noncrossing choices on separate
sibling lists need not automatically glue to one global noncrossing endpoint
partition, and a component-support block need not automatically section into
one immediate-sibling list.  If either implication failed, connected
decorations would not identify the actual crossing components, so both the
pointwise product and the unique-maximizer theorem would collapse.

The repaired proof defeats that attack without enumeration.  In the forward
direction, a parent of any section chord has both endpoints in the outer
cyclic gap of the component-support block and therefore encloses every
section chord.  Distinct parents are nested; the inner one is then a strict
intermediate container below the alleged outer immediate parent.  In the
converse direction, a child selected by a parent-level block contributes an
exact gap, whereas an unselected child's closed support is a strict
subinterval of one gap.  Descendant blocks stay inside those gaps, distinct
children have disjoint intervals, and the same argument at the virtual root
closes the leaf-to-root induction.  The local choices therefore really do
glue globally.

## Review-A re-entry audit

### 1. Step 1: comparable parents and the strict intermediate container

**PASS.**  Theorem 2.1, Step 1 (`main.tex`, lines 188--210) now names
`p_i,p_j`, proves that each enclosing parent must use the outer gap and hence
enclose all section chords, orders distinct parents by nesting, and states
the decisive contradiction: if `p_i` lies strictly inside `p_j`, then `p_i`
strictly contains `x_j` and is a strict intermediate container between
`x_j` and its alleged immediate parent `p_j`.  The top-level alternative is
handled separately and supplies the virtual-root case.  Alternating sibling
indices then give alternating endpoints of two component-support blocks, so
the extracted groups form a noncrossing partition of the sibling list.

### 2. Step 2: exact gap versus strict gap-subinterval

**PASS.**  Step 2 (`main.tex`, lines 213--242) first proves disjointness and
coverage of the constructed even blocks.  For a child `x_i=(a,b)` and a
parent-level block `B_Q` it uses the correct exhaustive split:

- if `i in Q`, `a,b` are consecutive in the sorted `B_Q`, so `(a,b)` is an
  exact gap of `B_Q`;
- if `i notin Q`, the whole `[a,b]` is strictly contained in one gap of
  `B_Q`, including the outer cyclic gap when `Q` lies on one side.

Every lower block is contained in `(a,b)`.  Blocks below different children
have disjoint supports, while the parent-level blocks are already
nonalternating.  The leaf induction and its explicit repetition at the
virtual root therefore prove global noncrossing without the false round-zero
uniform-gap equality.  Sorting each `B_Q` pairs the two endpoints of each
chosen sibling consecutively, so `s(P)=T` exactly; descendant endpoints are
in other blocks and cannot disturb that pairing.

### 3. Connected decoration and mutual inverse

**PASS.**  In Step 3, noncrossing of `P` forbids crossings between distinct
`B_Q`, and the transported decoration is crossing-connected inside `B_Q`.
Thus the crossing components have supports exactly, not merely refining,
the blocks `B_Q`.  Step 4 recovers the unique component-support partition,
the sibling-index blocks and each order-standardized connected decoration.
Conversely, the exact-component statement makes extraction recover every
choice.  This proves both injectivity and surjectivity, including repeated
block sizes, singleton decorations, `d=0`, the virtual root and `n=0`.

### 4. Igusa subtraction

**PASS, subject to MINOR B1 below.**  For the noncrossing partition whose
parts are the target chords, a top-level chord is maximal in Igusa's vertical
order.  Nonempty immediate-sibling families are covered by the same parent
chord, whose two endpoints lie outside the sibling supports; hence no parent
element lies laterally between them.  This is the literal specialization of
Igusa's Definition 1.7.  Definition 1.2 defines adjacency by permissible
union, and Proposition 1.8 states that two parts are adjacent exactly when
they are parallel or one covers the other.  The manuscript therefore
correctly assigns zero credit to the static parallel/sibling localization
and compatible merging and limits the residual to the fixed-cut section,
connected decorations and every-target fibre result.

Primary source checked on 2026-08-31: [Igusa, *A Category of Noncrossing
Partitions*, Definition 1.7 and Proposition
1.8](https://doi.org/10.1007/s10485-025-09838-8).

### 5. Alman--Lian--Tran locators and the all-size sequence identity

**PASS.**  The locators in `main.tex`, lines 305--313 are exact:
Theorem 4.1.6 gives the full-wiring recurrence, Remark 4.1.7 names A111088,
Theorem 4.1.8 gives the coefficient identity, and Theorem 4.2.1 gives the
asymptotic density.  The paper assigns all of this zero credit and makes no
analytic asymptotic claim.

The all-size identification is not being inferred from the eight displayed
coefficients.  Independently, let `D=1+C(uD^2)` be the owned connected
chord-component equation and let `A=1+C(uA)`.  Two applications of formal
Lagrange inversion give

```text
[u^(n-1)] A(u)^n = n/(2n-1) [t^(n-1)](1+C(t))^(2n-1)
                  = n(2n-3)!!,
```

which is precisely Alman--Lian--Tran's Theorem 4.1.8 and recursively
determines the coefficients from constant term one.  Thus `a_d=X_d` holds
for every `d`, not merely through seven.

Primary source checked on 2026-08-31: [Alman--Lian--Tran, author-hosted
journal PDF, Sections 4.1--4.2](https://joshalman.com/AlmanLianTran.pdf),
[DOI 10.1016/j.jcta.2014.11.004](https://doi.org/10.1016/j.jcta.2014.11.004).

## Complete theorem, equation and boundary audit

### Proposition 1.1 and equations (1)--(2)

**PASS.**  Crossing-component supports form the owned noncrossing even-block
partition, and successive pairing gives the literal factorization
`Phi=s o pi`.  Every image is noncrossing and every noncrossing matching has
singleton crossing components, proving retraction, image=fixed set and the
Catalan count.  Idempotence implies every nonfixed state maps to a fixed
state in one step and cannot have a predecessor.  Since every positive
iterate has `Cat_n` fixed points, the fixed-`n` Artin--Mazur zeta function is
`(1-z)^(-Cat_n)`.  The empty matching, `(-1)!!=Cat_0=1`, and `n=0` zeta
boundary are consistent.

### Equations (3)--(6) and Theorem 2.1

**PASS.**  Equation (3) is the standard weighted noncrossing-partition
transform with `a_0=1`; decomposition at the block containing the first
index gives the formal identity `A(u)=1+C(uA(u))`.  No convergence is needed
or claimed.  The four-direction proof above establishes the all-size
bijection (4), so cardinalities multiply independently over every actual
chord vertex plus the virtual root to give the pointwise fibre formula (5).

### Equation (7), Theorem 3.1 and Corollary 3.2

**PASS.**  Juxtaposition injects `A_i x A_j` into `A_(i+j)` for positive
`i,j`.  A one-block partition decorated by the matching `r <-> r+i+j` lies
outside its image and has a complete crossing graph, so the inequality is
strict in every required size.  The virtual-rooted forest has total child
degree `n`; repeated strict merging bounds the fibre product by `a_n`, with
equality only if one vertex has positive degree.  A chord vertex cannot have
all `n` chords as children, so that vertex is the virtual root.  All chords
are then top-level, and noncrossing forces each to join consecutive
endpoints.  This proves the consecutive target is the unique maximizer,
including `n=0`.  Summing the proved pointwise fibres partitions the finite
domain and gives `(2n-1)!!`; the rainbow has only degree-zero/one factors and
therefore fibre one.

### Claim ceiling and collision boundary

**PASS, subject to MINOR B2 below.**  The manuscript does not claim an
unrooted canonical map, a new Catalan/component/transform/A111088 theorem,
generic parallel-part geometry, generic uncrossing, novelty or priority.
The admissible residual remains only the literal fixed-cut decorated inverse,
its pointwise product and its unique largest-fibre target.  The P120/P123 and
P117/P122/P126 distinctions are mechanism-level rather than vocabulary-only.

## Fresh exact-control audit

I read the verifier before running it.  It generates all matchings directly,
constructs crossing components from endpoint alternation, independently
generates noncrossing set partitions from restricted-growth strings, and
constructs inverse sources from sibling lists plus connected decorations.
For every target it separately checks predicted cardinality, no duplicate
construction, exact reconstructed-set equality and literal remapping to the
target.  The control is not an aggregate-census shortcut.

Fresh command:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py > /tmp/p130-reviewb-verification.txt
cmp /tmp/p130-reviewb-verification.txt code/verification_output.txt
```

Result: **PASS, byte-identical canonical stdout**.

```text
n<=7
states=146600
targets=626
reconstructed=146600
assertions=735609
```

```text
abd519009e877fa1fa98ece4e6cc290a5fb55bda47f07d4e79b9ccad43568a3d  code/verify.py
89b6142c21feac945f9d0dd362b5edf78aed78530596330be0c237e9088d60b4  code/verification_output.txt
89b6142c21feac945f9d0dd362b5edf78aed78530596330be0c237e9088d60b4  fresh stdout
```

This is strong finite falsification evidence only; the GO rests on the
all-size proof above.

## Isolated build and PDF QA

I copied only `main.tex` and `references.bib` into a fresh temporary
directory and ran exactly

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

All four stages returned zero.  The settled log/BLG had zero LaTeX/package
warnings, undefined citations/references, rerun requests, errors, overfull
boxes or underfull boxes.  All eight bibliography entries are cited.  The
isolated PDF, `main.pdf` and `main_round1.pdf` are byte-identical:

```text
199e28d4f91d945234e57c375e04fc5679f414c56613122223721069c08defb6  main.tex
276dcdfad779b9802d7e73ee63930198670ef64262b9670e436e906570ad5bae  references.bib
6580b2822113677f5256d0dffcd95b8048e2c0fe6442d434e9fd4b28a1b9a0cb  isolated main.pdf
6580b2822113677f5256d0dffcd95b8048e2c0fe6442d434e9fd4b28a1b9a0cb  main.pdf
6580b2822113677f5256d0dffcd95b8048e2c0fe6442d434e9fd4b28a1b9a0cb  main_round1.pdf
4d914ae6857739b11955dc9ec0db356e8bca5ae5cb67c1fd852ff3d4c2e796c9  main_round0_original.pdf
```

The round-one PDF has **4 A4 pages, 345,749 bytes**, rotation zero and no
encryption, form, JavaScript, custom metadata, metadata stream or embedded
file.  Title, Author, Subject and Keywords metadata are blank; dates are
omitted.  All **25/25** reported fonts are embedded, subsetted and
Unicode-mapped.  Text extraction contains no `??`, `[?]`, `[VERIFY]`, TODO,
filesystem path or stray `qquad` marker.

I rasterized and inspected all four pages individually:

1. title, anonymous byline, abstract, ownership boundary and Proposition 1.1;
2. completion of Proposition 1.1 and Theorem 2.1 through the two-case lemma;
3. completion of the inverse, firewall, formal transform and Theorem 3.1;
4. unique-max proof, census, control ceiling and all eight references.

No clipping, collision, missing glyph, illegible link, broken theorem,
orphaned heading, bad page continuation or anonymity leak is visible.  The
only visible author identity is `Anonymous`.

## MINOR findings

### B1. Qualify the exact Igusa statement at degree zero

`main.tex`, Remark 2.2 says that *each* immediate-sibling list is exactly an
Igusa parallel set.  Igusa defines a parallel set as a complete set of parts;
for a leaf vertex, the `d_T(v)=0` empty child list is an `A_0` bookkeeping
factor, not a nonempty complete parallel class of the ambient partition.
This does not affect the bijection or owner subtraction.

**Action:** say “each nonempty immediate-sibling list (and the nonempty
top-level list)” and state separately that degree-zero vertices contribute
the singleton `A_0`.  The `n=0` empty partition can remain a separate
boundary convention.

### B2. Correct the literal P110 firewall description

`main.tex`, Remark 2.2 calls P110 a “chord-edge update.”  P110's actual state
space is the set-partition lattice of a cyclic set and its update is
`pi -> pi join rho(pi)`; chord language occurs only in its primitive
two-element-block/deepest-shell description.  The present wording does not
create a theorem collision, but it describes the neighboring mechanism
inaccurately.

**Action:** replace that phrase by “the cyclic partition shift--join dynamics
of P110 (whose deepest-shell witness uses one two-element chord block)” or an
equivalent literal description.  Keep the conclusion that no theorem or
update transfers.

## Final gate

The repaired theorem package clears independent internal review.  The two
MINOR wording corrections should be folded into the next mechanical
consolidation, but neither justifies reopening the all-size inverse or exact
control.  Final disposition:

```text
CRITICAL 0
MAJOR    0
MINOR    2
GO_INTERNAL
HOLD_EXTERNAL
```
