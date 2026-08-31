# Claims and evidence

## Claim ceiling

The defensible ceiling is:

1. an exact all-degree OGF for depth at most `t`, for every finite field
   `F_(p^a)` and every `0<=t<=p-1`;
2. exact depth layers by consecutive differences;
3. a unique graded terminal-core/unit-fibre split;
4. the unit-fibre OGF and its coefficients; and
5. every exact-degree and degree-capped fibre over every invariant target.

Everything else is setup, a boundary check, or zero-credit background.

## Evidence map

| ID | manuscript statement | formal evidence | mechanical evidence | owner/internal subtraction |
|---|---|---|---|---|
| C1 | local depth equals longest positive cyclic run | Lemma 3.1, using the sliding-minimum induction | literal/window equality and direct residual depth in three fields | sliding window and clock zero credit; only its use in the census is residual |
| C2 | `R_(p,t)=tr(M_t(u)^p)` | fixed labelled cut and the unique cyclic state assignment for each support containing a zero | literal truncated `M_t(y/(1-y))` trace versus direct residual-vector enumeration for `p=2,3`, every `t`, weights `0..9` | transfer technique zero credit |
| C3 | `H_(q,p,t)` counts every degree with depth at most `t` | Theorem 3.2, unique factorization over translation orbits | all coefficient cells in available F4/F8/F9 boxes | `b_d`, `a_d`, fixed ring all zero credit inputs |
| C4 | consecutive differences give exact depth | Corollary 3.3 | exhaustive depth CDFs | immediate from C3 |
| C5 | unique `f=h r`, `h=Q(f)`, `Q(r)=1` | Proposition 4.1 by orbit exponents | divisibility and quotient reconstruction for every state | set-theoretic, not a monoid quotient |
| C6 | unit-fibre OGF `(1-qz^p)/(1-qz)` | graded product bijection | exact degree coefficients | term “kernel” forbidden |
| C7 | exact target fibre is `U_(N-deg h)` | restricted identity `Q(hr)=hQ(r)` for invariant `h` | every target/degree cell | target refinement is residual |
| C8 | capped target formula | summation of C7 | every bounded target sum | residual corollary |

## Pinned gate provenance

The independent pre-paper gate evidence is:

```text
HOSTILE_GATE_TRANSLATION_GCD.md
c447bc55296f8923415bdc2d784035aac16dbaa809d3bf959b63a62fd8c50e23

verify_translation_gcd_extensions.py
f2035f158049e880ce8c9471d85cf9bfe170a8faf076c147498232357b692b92

TRANSLATION_GCD_EXTENSIONS_CANONICAL.txt
826a73769c453b5227a4f7af0ab9fd2ced417c0ea15b6492b2910cc3e984677f
```

The paper-local verifier is a terminology-repaired copy of the independent
extension-field falsifier.  Its own post-copy hashes are recorded in
`CONTROL_RESULTS.md` and later frozen by `SHA256SUMS`.

## Round1 repair evidence

- A1 is visible in the proof of Lemma 3.1: the coordinate cut is labelled
  and fixed, its cyclic state assignment is unique, and the trace is stated
  not to quotient by rotations or multiply by the number of zeros.
- A2 is implemented independently of `residual_vector_series`: the verifier
  builds the truncated polynomial entries of `M_t(y/(1-y))`, performs matrix
  powering, takes the trace, and compares all weights `0..9` for every
  tested `p,t`.  The 50 new comparisons raise the canonical total to
  `180453`; a fresh run agrees byte-for-byte with the canonical transcript.
- A3 is a terminology-only ceiling repair: the infinite expression is the
  **formal orbit Euler product**, with no analytic-convergence claim.

## Boundaries and counterexamples

| boundary | required behavior |
|---|---|
| degree zero | `1` is fixed and the unit-fibre coefficient is `1` |
| `p=2` | only depth `0` and `1`; all formulas remain literal |
| `q=p^a` | the acting translation has order `p`, not `q` |
| repeated factors | exponent minima and arbitrary positive heights apply |
| target too large | fibre is zero when `N<deg h` |
| final threshold | `H_(p-1)=1/(1-qz)` |
| false homomorphism | `Q(x)=Q((x^p-x)/x)=1`, but `Q(x^p-x)=x^p-x` |

## Evidence limits

The paper-local verifier makes 180,453 deterministic assertions over 17,523
monic states in explicit models of F4, F8, and F9.  These are falsification
controls only.  They do not prove the theorems, establish novelty, or replace
the owner audit.  External status is `HOLD_EXTERNAL`.
