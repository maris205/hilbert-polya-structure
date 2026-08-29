# Hostile Review B — principal-hook partition dynamics

Review date: 2026-08-29  
Reviewer role: independent non-author, second hostile pass  
Release status: **HOLD**  
Provisional verdict: **GO_INTERNAL_AFTER_REPAIR**

I did not consult any Review A artifact. I reconstructed the claims from the
author manuscript, support files, verifier, and primary literature identified
in a bounded search. The verdict is mathematical, computational, and
owner-scope review only; it is not final QA, a novelty clearance, or permission
to circulate.

## Bottom line

I found no counterexample to the finite dynamical claims. The classical image
and fibre formula, the first-part Lyapunov identity, the two-case gap clock,
the sharp `floor(n/2)` depth, the layer offset, the conjugation exception, and
the zeta calculation all reconstruct correctly. The fresh exact run passed
10,110,035 assertions and was byte-for-byte identical to the stored stdout;
the fresh four-page build is clean and visually sound.

There is one release-blocking wording problem: “unique attractor” is not
defined and is stronger or ambiguous under common finite-dynamical definitions.
The proof establishes the exact, definition-free statement that `(n)` is the
unique fixed point and is globally reached by every orbit. The manuscript
should say “unique globally attracting fixed point” unless it supplies a
formal attractor definition. The residual owner language should also avoid
turning a bounded negative search into implied novelty.

## Independent theorem reconstruction

### 1. Definition, classical image, and fibre

For `lambda=(lambda_1,...,lambda_ell)` with Durfee size `d`, the principal
hook lengths are

```text
h_i = lambda_i + lambda'_i - 2i + 1
    = alpha_i + beta_i + 1,       1 <= i <= d.
```

The principal hooks are disjoint and cover the Ferrers diagram, so their sum
is `n`. Strict decrease of the Frobenius arms and legs gives
`h_i-h_{i+1}>=2`. Conversely, a target
`h_1>...>h_r>0` with those gaps is obtained by splitting every
`h_i-1=alpha_i+beta_i` into strict nonnegative arm and leg sequences.

Working from the innermost hook outward gives `h_r` choices at the bottom and
`h_i-h_{i+1}-1` choices at each earlier level. Hence

```text
#H^{-1}(h) = h_r product_{i<r}(h_i-h_{i+1}-1).
```

This is exactly the zero-credit hook-type product in Goupil, not a temporal
result of this draft.

### 2. First-part and gap clocks

The outer principal hook is the first row plus first column with the corner
counted once, so

```text
(H lambda)_1 = lambda_1 + ell(lambda) - 1.
```

Every non-row partition has `ell>=2`; its first part strictly grows. Since the
weight is fixed, every orbit reaches `(n)`, and no other periodic point can
exist.

With `g(lambda)=lambda_1-lambda_2`, padding a row by `lambda_2=0`, the first
two image parts for Durfee size at least two are

```text
h_1 = lambda_1 + ell(lambda) - 1,
h_2 = lambda_2 + lambda'_2 - 3.
```

Therefore

```text
g(H lambda)-g(lambda)
  = ell(lambda)-lambda'_2+2
  = 2 + m_1(lambda) >= 2.
```

If the Durfee size is one, a nonterminal state is `(a,1^b)`, `b>=1`; its
single hook is all `n` cells, and the final gap increment is `b+1>=2`. These
two cases cover every nonterminal state.

### 3. Pointwise and sharp global depth

The terminal gap is `n`. Telescoping the gain of at least two over every
nonterminal step yields

```text
tau(lambda) <= floor((n-g(lambda))/2) <= floor(n/2).
```

For `a>=b>=2`, direct two-row hook calculation gives
`H(a,b)=(a+1,b-1)`, followed by `H(a,1)=(a+1)`. Thus the balanced two-row
partition `(ceil(n/2),floor(n/2))` takes exactly `floor(n/2)` steps. This is
an actual infinite-family proof of sharpness, not an inference from the
enumeration.

### 4. Layer offset and fibre recurrence

Let `A_t(n)` count states of entrance time `t`. The depth-zero state is only
`(n)`. Its classical fibre has size `n`, but contains `(n)` itself, hence

```text
A_0(n)=1,  A_1(n)=n-1.
```

The restriction `t>=2` in the displayed recurrence is essential. If one
naively used the fibre sum at `t=1`, the target `(n)` would contribute `n`,
not `n-1`; the terminal preimage must be removed. For `t>=2`, no such
subtraction occurs, and disjoint fibres give

```text
A_t(n) = sum_{h in image, tau(h)=t-1} #H^{-1}(h).
```

Thus the manuscript's layer offset is correct, including empty sums.

### 5. Conjugation and zeta

Conjugation swaps every Frobenius arm with its leg, so `H(lambda)=H(lambda')`
and all positive-time iterates agree. If neither member of the conjugate pair
is terminal, their depths are both `1+tau(H lambda)`. The sole exception for
`n>1` is `(n)` versus `(1^n)`, with depths zero and one. At `n=1` the pair
coincides.

Strict first-part growth eliminates every nontrivial periodic orbit.
Consequently `#Fix(H^m)=1` for every `m>=1`, and the formal Artin--Mazur zeta
function is

```text
exp(sum_{m>=1} z^m/m) = 1/(1-z).
```

## Targeted hostile tests

| Attack | Independent result |
|---|---|
| `n=1` | Only `(1)`; depth zero; `A_0=1`, `A_1=0`; conjugation exception disappears. |
| `n=2` | `(2)` has depth zero and `(1,1)` maps to `(2)` in one step; maximum depth one. |
| Layer off-by-one | Extending the weighted formula to `t=1` gives the wrong value `n`; the manuscript correctly isolates `A_1=n-1`. |
| Durfee-one terminal step | `(a,1^b)` maps directly to `(a+b)` and gains `b+1` in the padded gap. |
| Deep rectangle claim | `(4,4,4,4)` follows `(7,5,3,1)->(10,5,1)->(12,4)->(13,3)->(14,2)->(15,1)->(16)`, depth `7<8`; `(6^6)` has depth `17<18`. The draft correctly refuses a rectangular classification. |
| Projection overclaim | `(2,2)->(3,1)->(4)`, so `H` is not idempotent; the draft records this. |
| Unconditional depth conjugacy | `(2)` and `(1,1)` have depths zero and one; the draft records precisely this exception. |
| “Attractor” | The proof shows global finite-time capture by `(n)`, but the manuscript supplies no attractor definition. |

## Findings by severity

### CRITICAL

None found in the proved theorem contracts.

### MAJOR (math)

1. **Undefined/possibly overbroad “unique attractor.”** The abstract, Lemma
   3.1, README, and narrative use “unique attractor,” while the proof only
   needs and establishes a globally attracting fixed point. Depending on the
   convention, “attractor” may require a topology, isolating neighborhood,
   minimality, or an omega-limit definition. This is unnecessary exposure.

   **Executable repair:** replace every theorem-level occurrence by “`(n)` is
   the unique fixed point, the unique periodic point, and the globally
   attracting fixed point; every orbit reaches it in finite time.” If the word
   “attractor” is retained, define it before Lemma 3.1 and verify uniqueness
   under that exact definition.

### MAJOR (owner-scope)

1. **Residual temporal claims are not owner-cleared.** The introduction says
   “The contribution begins after this subtraction.” A bounded search did not
   locate a direct owner for iteration, but absence from these searches is not
   evidence of novelty. The existing global HOLD helps, yet “contribution” can
   still be read as originality language.

   **Executable repair:** change this to neutral contract language such as
   “After subtracting the classical one-step facts, the present proof package
   analyzes the following temporal statements.” Retain explicit HOLD and add
   “no external originality conclusion is drawn from the bounded search.”

### MINOR

1. “Fibre-weighted layer recurrence” is exact, but it is not a scalar closed
   recurrence in the numbers `A_t(n)` alone: its right side requires the
   depth-marked image states. Calling it a “state-weighted recursion” once
   would prevent an enumerative overreading.
2. State explicitly next to the definition of `g` that padding is used only
   for evaluating the one-row terminal gap; this convention is already
   mathematically consistent.
3. The rectangle falsifier is useful, but “boundary shell” is verifier-local
   terminology. Keep it out of any claim heading unless formally defined.

## Owner audit and zero-credit ledger

The bounded primary-source search used exact-title and phrase queries for
“principal hooks,” “principal hook lengths,” “central hooks,” “iteration,”
“dynamics,” “regrouping,” and “fixed point.” It also inspected the cited
owner source rather than relying on secondary summaries.

- Goupil's [*A Product of Integer Partitions*](https://arxiv.org/abs/0906.3004)
  defines hook type and gives exactly the product
  `h_r product(h_i-h_{i+1}-1)`. It is a direct owner for the one-step fibre
  formula and supports assigning that formula zero credit.
- Standard Frobenius/principal-hook setup and adjacent-gap image facts are
  background, not residual credit. The manuscript's Andrews and
  [Chern--Yee](https://doi.org/10.37236/10803) references are consistent with
  that treatment.
- Goupil's full text had no match for “iteration” or “dynamics.” Additional
  primary searches found papers using principal-hook decompositions but no
  direct temporal owner for this exact self-map, depth clock, or layer
  recurrence.
- **Negative-search boundary:** no direct iterated-principal-hook owner was
  found in this bounded pass. This does not establish novelty, priority, or
  freedom to disseminate.

Zero credit must remain attached to the image characterization, Frobenius
surjectivity mechanism, fibre product, standard conjugation of Frobenius
coordinates, and the formal zeta definition. The residual paper-specific
contracts are the exact gap increment, its sharp two-row depth consequence,
the depth-marked use of the owned fibres, and the precisely stated conjugacy
exception; even these remain externally unowned/HOLD.

## Fresh computational and build audit

Commands were run from the repository root with all generated output placed
under `/tmp`; no author artifact was overwritten.

```bash
tmp_out=$(mktemp /tmp/p113_verify.XXXXXX.txt)
python3 -B papers/113-principal-hook-partition-dynamics/code/verify.py > "$tmp_out"
cmp -s "$tmp_out" papers/113-principal-hook-partition-dynamics/code/verification_output.txt
```

Result:

- exit status: `0`;
- byte comparison: `0` (identical);
- stdout: 45 lines, 6,053 bytes;
- exact assertions: **10,110,035**;
- fresh wall-clock reading: approximately 12 seconds.

Fresh build procedure:

```bash
build_dir=$(mktemp -d /tmp/p113_build.XXXXXX)
cp main.tex references.bib "$build_dir"/
cd "$build_dir"
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdfinfo main.pdf
pdffonts main.pdf
pdftoppm -png -r 120 main.pdf render/page
```

Settled result:

- **4 pages**, A4;
- all four compilation stages returned zero;
- final LaTeX/BibTeX logs: no substantive warnings, undefined references or
  citations, multiply defined labels, overfull boxes, or underfull boxes;
- every listed font is embedded and subsetted;
- all four rendered pages were inspected at 120 dpi: no clipping, collision,
  missing glyph, broken rule, or unreadable table/equation was observed.

Expected first-pass unresolved references were gone in the settled third
LaTeX pass and are not build defects.

## Repair gate

Before internal GO:

1. replace or formally define “unique attractor” everywhere;
2. neutralize the residual “contribution” wording and retain owner HOLD;
3. clarify that the layer formula is depth-state-weighted, not a closed scalar
   recurrence.

No theorem contraction, verifier rewrite, or page-layout repair is otherwise
required by this review. External status remains **HOLD** after these internal
repairs.
