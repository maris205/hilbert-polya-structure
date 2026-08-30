# Hostile Review A — P120 round 0

Date: 2026-08-30  
Role: independent non-author Reviewer A  
Scope: round-0 manuscript and paper-local controls only  
External status: **HOLD**

## Provisional verdict

**GO INTERNAL AFTER TARGETED REPAIR; EXTERNAL HOLD.**

There is **no theorem-threatening issue** in the round-0 claim package.  I
found no false definition, recurrence, elimination identity, fixed-point
criterion, or cycle count.  I do, however, require one owner/citation
traceability repair before this can be treated as a clean archival draft,
and I recommend four smaller mathematical/auditability clarifications.

Severity summary:

- **CRITICAL:** none.
- **MAJOR (mathematics):** none.
- **MAJOR (owner/citation scope):** one local but release-blocking item,
  concerning missing arXiv identifiers in the rendered bibliography.
- **MINOR:** four items.

## Independent reconstruction of the mathematics

### 1. Definition, simultaneous update, and invariants — PASS

Location: main.tex, lines 118–144 and 146–179.

For a nonempty plane rooted tree
\[
T=[T_1,\ldots,T_k],
\]
the displayed recursion applies the same map to every old child subtree and
reverses the resulting root list exactly when $|T|$ is odd.  Recursing down
the old tree is therefore equivalent to simultaneously reversing the child
list at every vertex whose old fringe order is odd.  No updated parity is
read during the step.

The update changes only sibling order.  Hence it preserves total order and
the underlying nonplane rooted tree.  With the natural recursively induced
vertex transport, it also preserves each individual fringe order, so every
trigger is unchanged after one step.  The theorem is correct, subject to the
wording repair in Minor 1 below.

### 2. The involution law $\mathsf M^2=\mathrm{id}$ — PASS

Location: main.tex, lines 171–176.

After one application, every vertex has the same trigger.  At an even root,
the second step applies $\mathsf M^2$ to the children in place.  At an odd
root, it applies $\mathsf M^2$ to the children and reverses the root list a
second time.  Induction returns the original ordered tuple.  The alternative
description as commuting reversals of distinct child lists is also sound
once vertices are transported through the first update.

### 3. Fixed twisted-palindrome criterion — PASS

Location: main.tex, lines 152–160 and 177–178.

At an even root,
\[
\mathsf M(T)=[\mathsf M(T_1),\ldots,\mathsf M(T_k)],
\]
so tuple equality holds exactly when each $T_i$ is fixed.  At an odd root,
\[
\mathsf M(T)=[\mathsf M(T_k),\ldots,\mathsf M(T_1)],
\]
so equality is equivalent, in both directions, to
\[
T_i=\mathsf M(T_{k+1-i})\qquad(1\le i\le k).
\]
If $k$ is odd, this correctly forces the central child to be fixed.

### 4. Coupled $E/O$ functional system — PASS

Location: main.tex, lines 191–234.

For an even-order fixed root, the children are an arbitrary sequence of
fixed trees whose total order is odd.  Since $F=E+O$ and $F(-x)=E-O$, the
odd part of $\operatorname{SEQ}(F)$ is
\[
\frac12\left(\frac1{1-F(x)}-\frac1{1-F(-x)}\right)
=\frac{O}{(1-E)^2-O^2}.
\]
Multiplying by the root marker gives
\[
E=\frac{xO}{(1-E)^2-O^2}.
\]

For an odd-order fixed root, the off-centre children occur uniquely as
twisted pairs
\[
(T_1,\ldots,T_r,\mathsf M(T_r),\ldots,\mathsf M(T_1)).
\]
Each pair contributes $A(x^2)$.  An optional central child must be fixed and,
because the root's children have even total order, must itself have even
order.  Thus the centre contributes $1+E$, giving
\[
O=\frac{x(1+E)}{1-A(x^2)}.
\]
There is no overcount: the first half of an ordered tuple uniquely determines
the second half.

### 5. Degree-six elimination and branch uniqueness — PASS

Location: main.tex, lines 241–280.

I reconstructed the elimination independently.  With
\[
\begin{aligned}
H_1&=(F+G)(1-F)(1-G)-x(F-G),\\
H_2&=(1-B+x)G-(1-B-x)F+2x,\\
H_3&=B^2-B+x^2,
\end{aligned}
\]
exact symbolic arithmetic gives
\[
\operatorname{Res}_{B}\!\left(
  \operatorname{Res}_{G}(H_1,H_2),H_3
\right)=4x^2P(x,F)
\]
with exactly the displayed polynomial $P$.  Thus the cancellation of
$4x^2$ is legitimate in the domain $\mathbb Q[[x]]$.

The branch statement is also correct:
\[
P(0,y)=y(y-1)^3(y+3),\qquad P_y(0,0)=-3.
\]
The formal implicit-function theorem therefore gives exactly one branch in
$\mathbb Q[[x]]$ with constant term zero.  Calling $P$ a “degree-six
annihilating equation” is safe: its $y^6$ coefficient $2x^2-x$ is nonzero,
while the manuscript explicitly disclaims irreducibility and minimality.

### 6. Ordinary mirror separation — PASS

Location: main.tex, lines 181–187.

With $L=[]$, $U=[L]$, $A=[L,U]$, and $B=[U,L]$:

- $|A|=|B|=4$, $\mathsf M(A)=A$, and
  $\mathsf J(A)=B\ne A$.
- $\mathsf M(B)=B$.
- The tree $[A,B]$ has order nine, so
  $\mathsf M([A,B])=[B,A]\ne[A,B]$.
- Since $\mathsf J(A)=B$ and $\mathsf J(B)=A$,
  $\mathsf J([A,B])=[A,B]$.

The two fixed sets are therefore genuinely incomparable.  These are literal
witnesses, not merely differing recursions.

### 7. Cycle census, iterate-fixed counts, and zeta — PASS

Location: main.tex, lines 316–359.

An involution on the finite carrier $\mathcal P_n$ has only one- and
two-cycles.  Hence $f_n$ fixed states leave $a_n-f_n$ states paired into
$(a_n-f_n)/2$ two-cycles.  Odd iterates fix only the one-cycles, while even
iterates fix the full carrier.  Substitution in the Artin–Mazur definition
gives
\[
\zeta_{\mathsf M,n}(z)
=(1-z)^{-f_n}(1-z^2)^{-(a_n-f_n)/2}.
\]
The separately adjoined empty state and the one-vertex tree both correctly
give $(1-z)^{-1}$.

## Required repairs

### MAJOR (owner/citation scope) 1 — the two key preprints are not identifiable in the rendered bibliography

Locations:

- references.bib, lines 12–20 and 34–42;
- rendered PDF, page 5, references [2] and [4];
- generated main.bbl, lines 14–26.

The BibTeX records contain arXiv identifiers, DOI fields, and URLs, but
amsplain drops those fields for the current misc entries.  The PDF therefore
renders the two closest current owners only as author, title, and year:
the 2025 Bousquet-Mélou–Krattenthaler paper and the 2026
Claesson–Kitaev–Steingrímsson–Wang paper have no arXiv number, DOI, or URL in
the bibliography.  This is especially serious for the latter because the
text calls it the “strongest current owner objection.”

**Repair:** make an identifier render, for example with a note or
howpublished field containing “arXiv:2512.18656” and
“arXiv:2607.06247”, then rebuild and visually confirm both identifiers on
page 5.  The source claims themselves are accurate: the
[2026 primary source](https://arxiv.org/html/2607.06247) explicitly maps the
three-leaf star to the depth-three path and proves that $h$ has no positive
even-size fixed points; the
[2025 primary source](https://arxiv.org/abs/2512.18656) studies root-corner,
leaf, nonleaf-corner, and fixed-degree-corner rotations, not parity-selected
child-list reversal.

This is release-blocking owner traceability, but it is **not a mathematical
defect** and does not change the theorem package.

### MINOR 1 — “corresponding vertex” is undefined and the verifier checks only a multiset

Locations:

- main.tex, lines 149–150 and 166–169;
- code/verify.py, lines 87–91 and 303–308.

The theorem makes a pointwise statement about fringe order “at the
corresponding vertex,” but no correspondence is defined.  The verifier
instead sorts all fringe orders and checks only multiset equality.  The
stronger pointwise statement is true.

**Repair:** define the induced transport recursively: root maps to root; at
an even root child position $i$ maps to position $i$, at an odd root it maps
to position $k+1-i$, and inside each transported child use its recursively
induced transport.  State that corresponding fringe subtrees have equal
orders.  Then either add a pointwise verifier lane or weaken the theorem to
multiset preservation.  Defining the transport is preferable because the
proof already supports the stronger claim.

### MINOR 2 — the empty lane is inside an imprecise theorem quantifier

Locations: main.tex, lines 125–126 and 146–163.

The theorem says “For every $T\in\mathcal P_n$” after adjoining
$\mathcal P_0=\{\boldsymbol\varepsilon\}$.  Item 1 then refers to the
underlying rooted tree and corresponding vertices, notions not defined for
the separate empty state.

**Repair:** state item 1 for $n\ge1$ (or for nonempty $T$), and state
separately that $\mathsf M(\boldsymbol\varepsilon)=\boldsymbol\varepsilon$
and $\mathsf M^2(\boldsymbol\varepsilon)=\boldsymbol\varepsilon$.  The
current formulas for $n=0$ remain unchanged.

### MINOR 3 — specify the formal ring and make coupled uniqueness explicit

Locations:

- main.tex, lines 197–208 and 231–233;
- main.tex, lines 251–252 and 274–280.

“Unique zero-constant formal solution” should say in which ring it is
unique and which Catalan branch is used.  The coefficient-recursion sentence
for the coupled system is correct but compressed.

**Repair:** say explicitly that $A,E,O,F\in\mathbb Q[[x]]$, with $A(0)=0$.
For the coupled system, either display the coefficient induction after
clearing the unit denominators or note that the Jacobian with respect to
$(E,O)$ at $(x,E,O)=(0,0,0)$ is the identity.  For the scalar equation,
say “the unique $F\in\mathbb Q[[x]]$ with $F(0)=0$.”  No coefficient or
claim changes.

### MINOR 4 — the finite residual control does not audit the exact resultant

Locations:

- main.tex, lines 268–272 and 412–420;
- code/verify.py, lines 183–201 and 267–268;
- CLAIMS_EVIDENCE.md, line 12.

The verifier checks $P(x,F(x))=0$ only through $x^{30}$.  It does not
reconstruct the asserted exact resultant $4x^2P$.  The paper does not confuse
the finite check with proof, and my independent exact calculation passes, so
this is not a theorem defect.  It is nevertheless the most transcription-
sensitive formula in the paper.

**Repair:** add a small exact sparse-polynomial elimination lane, or display
enough of the intermediate resultant/substitution calculation to make the
identity independently auditable without trusting the final polynomial.
Continue to describe the order-30 residual only as a falsification control.

## Owner subtraction and claim ceiling

The bounded primary-source audit supports the stated distinctions:

- [Chen–Shapiro–Yang (2006)](https://doi.org/10.1016/j.ejc.2004.07.013)
  use an illegal-vertex search and sibling/subtree transfer to reverse leaf
  parity; this is not the present simultaneous fringe-parity mirror.
- [Deutsch (2000)](https://doi.org/10.1006/jcta.1999.3027) gives an
  ordered-tree bijection producing statistic equidistributions.
- [Li–Lin–Zhao (2024)](https://doi.org/10.1016/j.aam.2024.102677) study
  transported mirror/statistic involutions on binary and plane trees.
- [Claesson–Kitaev–Steingrímsson–Wang (2026)](https://arxiv.org/html/2607.06247)
  own the abstract Catalan involution $h$, its fixed census, reversal
  factorization, and Donaghey connection.  The manuscript's star/path and
  even-size separation claims are exact.
- [Bousquet-Mélou–Krattenthaler (2025)](https://arxiv.org/abs/2512.18656)
  own the cited cyclic actions and their fixed-set/cyclic-sieving analysis.

Four bounded query formulations combining “fringe subtree,” “subtree size
parity,” “reverse children,” “local mirror,” “plane tree,” and “involution”
returned adjacent parity involutions and fringe-subtree literature, but no
primary source for the literal update in Definition 2.1.  This is only a
**bounded no-hit**, not evidence of novelty or priority.

The claim ceiling is otherwise disciplined.  The draft explicitly assigns
zero credit to mirror symmetry, Catalan enumeration, symbolic/context-free
algebraicity, resultants, involution cycle conversion, and Artin–Mazur zeta
bookkeeping.  It claims no asymptotic, irreducibility, minimal polynomial,
general Catalan action, priority, owner-clearance certificate, or
release-readiness.  The residual conjunction is stated narrowly enough for
internal review.

## Fresh computational and build audit

I ran the canonical verifier from scratch with bytecode writing disabled.
It passed with:

- **1,072,729 exact assertions**;
- **82,501 enumerated states**;
- exhaustive orders $0$ through $12$;
- series checks through order $30$;
- exact agreement with all displayed carrier, fixed, and two-cycle counts;
- both ordinary-mirror separation witnesses;
- zero coupled and degree-six residuals through $x^{30}$;
- canonical stdout byte-identical to code/verification_output.txt
  (**14 lines, 577 bytes**).

I then copied only main.tex and references.bib to an isolated temporary
directory and ran the full LaTeX–BibTeX–LaTeX–LaTeX build.  Results:

- **5 A4 pages**, **378,895 bytes**;
- SHA-256
  **82ad6fbe993211a3ac20051c838b2752a7d57e215db56e183b37e53084e0a4dc**,
  byte-identical to the repository PDF and to main_round0_original.pdf;
- zero LaTeX warnings, undefined references/citations, overfull boxes, or
  underfull boxes;
- 9/9 cited bibliography entries present;
- all **30/30 fonts embedded, subsetted, and Unicode-mapped**;
- Author metadata empty, A4 page box, no date metadata, forms, JavaScript,
  encryption, or page rotation;
- all **5/5 pages** visually inspected: equations, the degree-six display,
  both tables, references, headers, and page breaks are clean.

The manuscript is anonymous: the visible author is “Anonymous,” PDF Author
metadata is empty, and I found no affiliation, email address, grant,
acknowledgment, placeholder, or identity leak.

## Actionable disposition

Before the next freeze:

1. make both arXiv identifiers render in the bibliography;
2. define the vertex correspondence and align the verifier with the chosen
   pointwise/multiset statement;
3. separate the empty-state quantifier;
4. specify $\mathbb Q[[x]]$ and add one rigorous sentence for coupled
   uniqueness;
5. add an exact resultant audit lane or an auditable intermediate identity.

After those repairs, I see no mathematical reason to block the paper from
the next internal round.  External dissemination remains **HOLD**, and this
review makes no novelty or priority certification.
