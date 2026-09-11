# MNC author source and mechanism subtraction

2026-09-06 UTC. Author assessment, **not an independent candidate gate**.
The mathematical proof is complete; source/value admission remains for a
nonauthor. MNC/MDE are at most one contrast-family seat. HOLD_EXTERNAL.

## Exact proposed residual

On labeled ternary cycles of every length $n\ge3$, the rule is
$F(x)_i=\min(|x_i-x_{i-1}|,|x_i-x_{i+1}|)$, using ordinary integer distance.
The prospective temporal statement is $F^4=F^3$, the exact colored-pulse
fixed language, and sharp entrance two at $n=3,4$ and three at $n\ge5$.
The prospective second statement is the **case-complete strict comparison**
of every nonzero target with the zero target for $n\ge4$, with the unique
$111$ exception at $n=3$. The inverse walk decoder and the formula for
the zero fibre alone are not independent advances.

## Primary sources actually inspected

1. Henryk Fukś, *Sequences of Preimages in Elementary Cellular Automata*,
   Complex Systems 14 (2003), 29–43, DOI
   [10.25088/ComplexSystems.14.1.29](https://doi.org/10.25088/ComplexSystems.14.1.29).
   Primary PDF: [journal copy](https://content.wolfram.com/sites/13/2023/02/14-1-2.pdf),
   archived as `sources/Fuks2003.pdf`. Read title/abstract and pp. 29–34,
   including Section 3, equation (9), Figure 1(b), and the reference entry
   for Rogers–Want. Equation (9) defines exact emulation; Figure 1(b)
   explicitly identifies binary rule 36 as a second-level identity
   emulator. Thus $G^3=G^2$ is prior. Page 33 and the appendix introduction
   describe many preimage sequences as conjectured from data. Those
   entries are not used as proved arbitrary-iterate counts here.
2. Thomas Rogers and Chris Want, *Emulation and subshifts of finite type
   in cellular automata*, Physica D 70 (1994), 396–414, DOI
   [10.1016/0167-2789(94)90074-4](https://doi.org/10.1016/0167-2789(94)90074-4).
   Read the actual publisher metadata/abstract only. Its announced carrier
   is binary sequence space; Fukś explicitly credits it for the emulator
   classification. Its body was not retrieved. No unseen ternary theorem
   is attributed to it, and its binary result is fully deducted already.
3. Erica Jen, *Enumeration of Preimages in Cellular Automata*, Complex
   Systems 3 (1989), 421–456,
   [primary PDF](https://content.wolfram.com/sites/13/2018/02/03-5-2.pdf),
   archived as `sources/Jen1989.pdf`. Read pp. 421–427 (general finite-
   alphabet recurrence and solved elementary categories), complete
   Sections 5.4–5.5 on pp. 449–451, and appendix pp. 452–454 including
   rule 36. The general endpoint recurrence covers arbitrary finite
   alphabets. Section 5.4 optimizes several binary run formulas and
   relates extremizers to their product/recurrence structure; Section 5.5
   adds forbidden-block constraints. Appendix 36 is a binary open-word
   Fibonacci product with stated endpoint conventions. All these
   representation and optimization methods receive zero credit.
4. Erica Jen, *Scaling of Preimages in Cellular Automata*, Complex
   Systems 1 (1987), 1045–1062,
   [primary PDF](https://wpmedia.wolfram.com/sites/13/2018/02/01-6-2.pdf),
   archived as `sources/Jen1987.pdf`. Read the introduction, general
   recurrence context, and pp. 1049–1051 containing definitions (3.1),
   (3.2), and Lemma 1. Its extremal statistic first fixes an open binary
   word, optimizes over its four two-sided extensions, then sums those
   optimized counts over all fixed words. It is not the maximum single
   labeled cyclic fibre over all ternary targets. The generic recurrence
   and enumeration-of-strings statements are deducted without claiming
   that this different statistic proves or disproves MNC's maximum.
5. Iztok Jeras and Andrej Dobnikar, *Algorithms for computing preimages
   of cellular automata configurations*, Physica D 233 (2007), 95–111,
   [publisher record](https://doi.org/10.1016/j.physd.2007.06.003).
   Read the author's [full preprint](https://rattus.info/al/files/preimages.pdf),
   archived as `sources/JerasDobnikar.pdf`, specifically introduction,
   definitions, Theorem 6 in Section 4.2.2, Section 4.4, and the cyclic
   listing construction in Section 5.2. The method explicitly covers
   arbitrary alphabets, neighborhood size, and cyclic boundaries. Theorem
   6 multiplies local preimage matrices; Section 4.4 sums their diagonal;
   the listing algorithm retains starting overlaps to enforce closure.
   This is a complete generic adapter for the **existence of a decoder
   and complete inverse-set algorithm**, not just a resemblance.
6. Henryk Fukś, *Ternary cellular automata induced by semigroups of
   order 3 are solvable*, [arXiv:2601.00486v1](https://arxiv.org/abs/2601.00486v1)
   (2026 posting; AUTOMATA 2025 proceedings article). Read the abstract,
   introduction and definitions, primary PDF pp. 1–3, archived as
   `sources/Fuks2026_semigroups.pdf`. The literal class is two-input
   associative operations. MNC depends essentially on all three input
   sites: changing $a$ in $(0,1,0)$ to 1 changes the output; changing
   $c$ does likewise; changing the center in $(0,0,0)$ to 1 changes
   the output. A sitewise alphabet bijection or reflection cannot turn
   this literal into a two-input operation. This excludes only that
   direct adapter, not time iterates or higher-block encodings.

## Complete deductions and limits of failed adapters

### Binary restriction: exact ECA 36, zero credit

For $a,b,c\in\{0,1\}$, $F(a,b,c)=(a\oplus b)(b\oplus c)$.
The only one-producing triples are $010$ and $101$, giving ECA number
$2^2+2^5=36$. Its $G^3=G^2$ result transfers to cyclic words at every
length by repeating the cyclic source as a bi-infinite word. The author
checker independently verifies the complete radius-three local identity,
but that is regression evidence for a prior theorem, not fresh credit.
Binary isolated-pulse stabilization and generic permanent-zero barriers
are likewise deducted.

The support projection $p(x)_i=\mathbf1_{x_i>0}$ does **not** satisfy
$pF=Gp$ on the full ternary carrier: local triples $121$ and $111$
have the same support triple, while their MNC outputs are 1 and 0.
Nevertheless the actual proof still reduces positive blocks after an
initial image to binary behavior, apart from fixed isolated twos. The
nonauthor must assess whether this extension plus the small-length sharp
witnesses is substantive or merely an inexpensive wrapper of ECA 36.
Failure of one projection is not itself a value argument.

### Static inverse and zero/all-one languages: zero credit

For a literal three-site rule, Jen's recurrence/Jeras–Dobnikar's diagram
uses overlaps $(x_{i-1},x_i)$ and admits the edge to $(x_i,x_{i+1})$
exactly when its output is the required target symbol. Taking the cyclic
trace and listing the paths gives **all** MNC sources. The distance-word
stratification in proof Step 3 merely refactors this standard construction.
Its $3\times3$ matrices and reflection split evaluate a small static
matrix algebra; no separate inverse-method novelty is claimed.

For the zero target, the unequal source edges form a matching and the
color-block weights are the classical proper-cycle-coloring values
$2^k+2(-1)^k$. The resulting matching polynomial evaluation and
$Z_n=2^n+(-1)^n+4\cos(n\pi/3)$ are routine static enumeration. The
all-one target's forbidden $020/202$ words, unique five-state lift and
three-dimensional trace are also standard finite-language enumeration.
Even the exact relaxed singleton-mask formula in Step 5 is derived by
ordinary path matching and simultaneous diagonalization; those techniques
do not earn a second axis simply because they use three colors.

### Remaining full-target comparison, not automatic clearance

Jen Section 5.4 is the most relevant prior optimization template. An
actual transfer to this candidate must preserve labeled cyclic closure,
the three source levels, and positive target magnitudes, and must prove
all equality cases. The author's proof supplies the following exact
case partition: all mixed targets are contained in their precise
singleton-mask class, whose count is at most $2^{n-1}+2$; every
all-positive target containing 2 has at most $2^{n-2}$ sources; and the
all-one target has count $t_n$ with $t_n=2t_{n-2}+2t_{n-3}$.
These bounds are strictly below $Z_n$ at every $n\ge4$ with the
separate $n=4$ all-one check. At $n=3$, the entire first-image/source
classification instead proves the unique $111$ maximizer.

The inspected primary statements do not themselves state this ternary
cyclic comparison or its small exception. This is a bounded conclusion
about the inspected statements, not proof of priority. A gate can still
find a complete adapter or judge the whole comparison routine and kill
the candidate. The author does not request credit for generic
"optimize a transfer product" as an innovation.

## Internal collision inspection

The search covered manuscript `.tex` originals and selected proof/source
notes for minimum contrast, rule 36, singleton runs, absolute neighboring
differences, cyclic words and local erosion, plus current killed scouts.
Selected original definitions/theorem contexts actually read were:

- P117, `papers/117-odd-run-reversal-cyclic-words/main.tex`: flips every
  odd-length run; its global run parity and shrinking boundary-word
  dynamics differ from the fixed-radius MNC literal. Its run bookkeeping
  and generic coalescence do not add value to MNC.
- P164, `papers/164-cyclic-equality-feedback/main.tex`, equation (T):
  $E(x)_i=\mathbf1_{x_i=x_{i+1}}$. There is an exact first-step relation
  $pF(x)_i=(1-E(x)_{i-1})(1-E(x)_i)$, fully deducted. It is not a
  conjugacy of the complete ternary evolution; $pF$ loses the output
  magnitudes. P164's binary affine Rule 102 tail is not MNC's literal.
- P197, `papers/197-ternary-cyclic-sign-difference/main.tex`, equation
  (map), clock and complete inverse-gap sections: directed **signed**
  differences and a shift-type recurrent core. The signed-edge trace and
  gap-product technique are occupied static mechanisms; replacing them
  by absolute edges followed by a minimum does not earn decoder credit.
- P196, `papers/196-cyclic-godel-implication/main.tex`, implication and
  core definitions: two-input finite-chain implication with a one-step
  shift core. Generic entry into a constrained local language is deducted.
- The current contrast intake and root source note were read in full.
  MDE shares the binary rule and contrast mechanism; it cannot supply a
  second independent seat alongside MNC.

These are concrete direct-literal/factor checks, not an exhaustive proof
that no old system admits a nonlocal encoding.

## Search procedure and unavailable optional review

Actual web formulations included the decimal rule code `112796998038`,
minimum/absolute adjacent contrast, ternary identity emulators, maximal
preimages for three colors, cyclic singleton runs, constrained color-word
counting, and de Bruijn inverse algorithms. Three raw tool-output query
groups are preserved in `sources/search_*.json`; follow-up primary reads
are identified above. Additional focused searches used 2024–2026 wording
and arXiv with a 183-day recency restriction. The search engine sometimes
returned much older papers even with that restriction; this is recorded
as a bounded recent search, not a complete six-month arXiv census.
The 2026 semigroup result was checked despite its January posting being
outside the nominal recent window. Unrelated web hits were not scientific
evidence. No direct Scholar/Semantic Scholar provider was available.

The installed novelty-check skill's optional separate-model MCP step
was not executed: that provider is unavailable, and this project's
configured-process review procedure controls the actual gate. A distinct
nonauthor candidate review is still pending; no review, external upload,
owner clearance, global novelty score or admission is fabricated.

**Author disposition:** complete theorem package ready for a hostile
candidate gate under the narrow residual above; **no author-assigned GO**.
