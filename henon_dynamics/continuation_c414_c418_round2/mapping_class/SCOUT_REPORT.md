# Scout report: the full positive two-twist semigroup

Status: **RESEARCH_RESERVE_FROZEN; AUTHOR_PROOF_COMPLETE;
INDEPENDENT_PROOF_AND_INCREMENT_REVIEW_PENDING**.
No new paper number, manuscript, Route A evaluation or admission is
claimed here. Only this new `mapping_class/` directory was edited.

The coordinator's first reading found no blocker, but this is not
recorded as an independent formal proof or novelty approval. The two
remaining batch slots are being filled by the cubic and function-field
contracts, so this package is a research reserve, not a sixth paper.
No further work on it is implied without later authorization. The
[freeze receipt](CHECK_RECEIPT.md) binds the six present payload files
and records the already completed checks without rerunning them.

## Frozen contract

The object is the entire family of chronological positive strings in
$$A(x,y,z)=(x,z,xz-y),\qquad B(x,y,z)=(z,y,yz-x),$$
with both letters present, on all of $\mathbb Z^3$ and all integer
levels of $K=x^2+y^2+z^2-xyz$. The clock is ordinary iteration of
the resulting word map. The output is a necessary-and-sufficient
classification of its integer periodic points and periods, not
whole-group finiteness, geometric fixed-scheme length, or finite-field
residual periodicity. The exact row-matrix convention and trace-greater-
than-two verification are in Step 1 of the proof package.

## Decisive cheap probes and the surviving theorem

The first quantifier probe succeeds as a counterexample to an unsafe
shortcut: $A^6\circ B^6$ has hyperbolic matrix trace 38 and fixes
$(1,1,m)$ for every integer $m$. For $m\ge3$, the same point
escapes under $A\circ B$. A theorem about points periodic under
every group element therefore cannot classify these single-word
periodic points. The compact core plus axes is also insufficient.

The actual surviving result is stronger and uniform:

- There is one explicitly displayed union $\mathcal D$ of 39 affine
  lines and four exceptional points $\mathcal E$. Every periodic
  letter phase of every positive two-letter word belongs to it.
- Every point of $\mathcal D\cup\mathcal E$ is fixed by some
  positive two-letter word. Thus it is the exact existential union
  of all such fixed-point sets and of all such periodic-point sets.
- For each level $k$, the candidate set $X_k$ has at most 40 points.
  The only possible levels are $m^2$, $m^2+1$ and $m^2-m+2$.
  Exact quadratic roots construct $X_k$; two partial-permutation
  matrices then classify every input word's ordinary cycles.
- Every nonperiodic integer point tends to infinity in both native
  directions. The finite-graph cycle and zeta formulas are deductions,
  not a separate new contract.

The universal cover is
$$
\begin{aligned}
\mathcal D_0&=\{(t,a,b),(a,t,b),(a,b,t):t\in\mathbb Z,\ a,b\in\{-1,0,1\}\},\\
\mathcal D_x&=\{(c,t,ct+b):t\in\mathbb Z,\ c=\pm1,\ b\in\{-1,0,1\}\},\\
\mathcal D_y&=\{(t,c,ct+b):t\in\mathbb Z,\ c=\pm1,\ b\in\{-1,0,1\}\},\\
\mathcal D&=\mathcal D_0\cup\mathcal D_x\cup\mathcal D_y,\qquad
\mathcal E=\{(2\epsilon,2\eta,2\epsilon\eta):\epsilon,\eta=\pm1\}.
\end{aligned}
$$
An exploratory 45-line superset was reduced by six lines: a periodic
phase with only a small third coordinate would have an all-large
predecessor, which the escape/descent argument excludes. That
directional correction is included in the final statement.

## Independent increment after subtraction

All general trace-map structure, the exact generator pair, matrix
hyperbolicity, finite-order small-trace fibers and the escape mechanism
are classical. Roberts (1996), not just a Fibonacci-only paper, is the
closest methodological predecessor. Humphries' finite-orbit theorem
has the wrong universal group quantifier for this contract. The
[source audit](SOURCE_AUDIT.md) records exact primary locators,
normalizations and access limitations.

The proposed increment is specifically the global integer exhaustion
for *every* positive two-letter word, the exact universal fixed locus,
and the uniform 40-state algebraic classifier for arbitrary words and
levels. This is not a new determinant trick, a new escape region, or
a renaming of a finite census. The full $m^2+1$ level family separates
it concretely from local C413: the chronological word $ABB=B^2\circ A$
has the explicit four-cycle
$$
(1,m,m)\to(-1,m,-m)\to(1,-m,-m)\to(-1,-m,m)\to(1,m,m)
$$
for every nonzero integer $m$. Its matrix has trace four and determinant
one, so it is not a power of the old Fibonacci map. The all-word
theorem, not this one example, is the proposed contract.

Author novelty triage: the three residual claims survive the bounded
primary comparison, but only at **proceed-with-caution** status. The
method-level novelty is low; the all-word arithmetic finding is the
potentially substantive part. A numerical novelty score would not
replace an independent assessment of that distinction. No fallback
question was launched, because the original full-family contract
produced a complete author proof rather than a blocked partial result.

## Artifacts and checks

| File | Purpose and status |
|---|---|
| [PROOF_PACKAGE.md](PROOF_PACKAGE.md) | Ten-step self-contained proof; all-word and all-level quantifiers explicit; independent review pending |
| [SOURCE_AUDIT.md](SOURCE_AUDIT.md) | Primary ownership, clock/domain distinctions, old C413 subtraction, recent search and access limits |
| [classify_word.py](classify_word.py) | Exact quadratic-root candidate construction and complete partial-word cycle classifier; no numerical radius or trial-period cutoff |
| [probe_positive_words.py](probe_positive_words.py) | Cheap bounded falsification checks only, not proof premises |
| [line_automaton.py](line_automaton.py) | Exact symbolic 45-line exploratory graph; first 39 lines are the proved cover; generic graph is not used in place of small-parameter point handling |

The exact classifier's self-test passes. It verifies candidate counts
$1,6,16,0,26,32,40,6,40$ at levels $0,1,2,3,4,5,8,9,14$,
respectively; compares exact cover membership independently on
$[-8,8]^3$; and closes all returned cycles for six test words and
$-20\le k\le100$. All three Python files compile.
An additional exact symbolic check verifies the complete line-realizing
word on all 39 parametrized lines, both common-reverser identities,
and the fourth iterate of the displayed $m^2+1$ cycle. All pass as
polynomial identities, rather than as parameter samples.

The independent falsification probe visits 178,605 point-word pairs
from $[-4,4]^3$ and 245 words. It finds 17,469 periodic pairs and
no cover counterexample. Separate one-step checks on $[-8,8]^3$
find no cone-invariance or small-domain-exit violation. Detected
periods are $1,2,3,4,6,12$, but no universal restriction to that
observed list is claimed. The proved period bound is 40.

Reproduce the exact classifier and bounded checks with:

```bash
python henon_dynamics/continuation_c414_c418_round2/mapping_class/classify_word.py
python henon_dynamics/continuation_c414_c418_round2/mapping_class/classify_word.py --K 101 --word ABB
python henon_dynamics/continuation_c414_c418_round2/mapping_class/probe_positive_words.py
```

The first sample at $k=101$ has 32 candidates and exactly the displayed
four-cycle with $m=10$ for that word. The distinction between a universal
candidate and a point periodic for one word is maintained throughout.

## Review handoff

The highest-value independent checks are the signed all-large descent
in Step 3, the phase/predecessor quantifiers in Steps 4--5, the exact
line-realizing positive words in Step 6, and the low-level overlap
removal giving the 40-state bound in Step 7. The independent reviewer
must also judge the increment after Roberts, Sasaki--Yoshida and C413
are subtracted. This author package alone cannot close the five-contract
gate. Nothing here supplies an Euler factor, root number, automorphic
identification, zero correspondence or Hilbert--Pólya conclusion;
`NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional.
