# P133 hostile review — Round A

**Manuscript:** *Source Phases and Target Fibres for Totient--Complement
Dynamics on Squarefree Divisors*  
**Review date:** 2026-08-31 UTC  
**Reviewer role:** independent hostile reviewer; no participation in the
round-0 draft  
**Calibration:** `NOT_CALIBRATED`; `criteria_binding_unavailable`, so this
report makes no venue-fit claim  
**External status:** `HOLD_EXTERNAL`  
**Verdict:** **`REPAIR`** — the mathematical gate passes with no Critical or
Major finding; the proof-object ledger must be repaired before Round B.

Severity summary: **CRITICAL 0; MAJOR 0; MINOR 1**.

## 1. Frozen snapshot and reproducibility

I reviewed the complete round-0 source, bibliography, paper-local verifier,
canonical stdout, narrative/evidence files, build record, settled LaTeX
artifacts, and all three PDF pages.  I did not modify the manuscript,
bibliography, verifier, canonical transcript, or PDF.

| artifact | SHA-256 at review |
|---|---|
| `main.tex` | `3f62efbd5a23a5a0a811e92f4f975ba643cd4262b958c6c6ab0804920f602835` |
| `references.bib` | `3311a309139704fb8712bb152895ce5dec7e0ddbe087d44e4a20504976b83e2d` |
| `code/verify.py` | `841ed6f77091e0d0e6721c24dc334891f8bc3b54701717153da49ecbb391262a` |
| `code/verification_output.txt` | `1c90aea14a3c45d084ec9cd6d86e951d3508494d94fa04afa6bd6ec12692b99d` |
| `main.pdf` | `bbb869d485230bc0165bbe49ff43929de61700c1e0acc960a541b64b23651d7b` |
| `main_round0_original.pdf` | `bbb869d485230bc0165bbe49ff43929de61700c1e0acc960a541b64b23651d7b` |

Fresh replay of `code/verify.py` matched the frozen stdout byte for byte
(`cmp=0`) and reported 4,774 exact assertions over 226 states and all 226
targets.  I also ran a separate implementation that did not import the paper
code.  It exhausted all 1,099 directed acyclic graphs compatible with a
fixed topological order through five vertices, covering 33,866 state cells
and 33,866 target cells.  It checked the phase decoder, exact recurrent set,
period two, the `h+1` entry bound, decoder compatibility at time `h+1`, and
the every-target inclusion--exclusion formula in 256,469 assertions:
`STATUS=PASS`.

A fresh four-stage isolated build from only `main.tex` and
`references.bib` produced a PDF byte-identical to the frozen artifact.  It
has three A4 pages and 346,509 bytes.  The settled log has no actionable
warning, undefined citation/reference, or bad box.  All 28 reported font
rows are embedded, subsetted, and Unicode-mapped; metadata fields are blank;
the visible author is `Anonymous`.  Extracted text contains no literal
`qquad`, and visual inspection of every page found no clipping, collision,
bad glyph, malformed display, or bibliography defect.

## 2. Hostile reconstruction of the theorem

### 2.1 Literal arithmetic reduction — survives

For squarefree `d`, the factor `n/d` supplies a target prime `p` exactly
when `p` is absent from the source support.  If `p` is present, it can enter
the output only through a factor `q-1` of
`phi(d)=product_(q in S)(q-1)`.  Thus the support update really is

\[
                 S\longmapsto(P\setminus S)\cup N(S).
\]

There is no missing self-edge: `p` never divides `p-1`.  The orientation
`q -> p` strictly lowers the prime, so the parent relation is acyclic and
every vertex is downstream of at least one no-incoming-edge source.

### 2.2 Source-phase decoder — survives

Complemented coordinates obey

\[
 y_p(t+1)=(1-y_p(t))\prod_{q\in\operatorname{Par}(p)}y_q(t).
\]

Sources therefore toggle.  For a nonsource, every parent phase pair has
product zero, so the two parent conjunctions `A_p^0,A_p^1` cannot both be
one.  Solving the two local phase equations in the three possible cases
gives uniquely

\[
                    (y_p^0,y_p^1)=(A_p^1,A_p^0).
\]

Topological induction is legitimate because all parents precede the child.
The decoder retains the arbitrary source bits, hence is injective.  Since a
nonempty finite DAG has a source, the two phases differ and no decoded state
can be fixed.

### 2.3 The `h+1` interface — survives, including phase compatibility

The identity `y_p(t)y_p(t+1)=0` implies, for every nonsource,

\[
                         y_p(t+2)=A_p(t+1).
\]

If every parent is two-periodic from its level plus one, then for
`t >= delta(p)+1` the products at `t+1` and `t-1` agree.  Consequently the
child is two-periodic from `delta(p)+1`.  At `h+1` the whole state satisfies
`F^2(x)=x`, so it is already recurrent rather than merely eventually
periodic.  The singleton boundary `h=0` is safe: its actual tail is zero and
the claimed upper bound is one.  Disconnected components cause no mismatch,
because `h` is the maximum component height.

There is also no hidden phase mismatch.  At time `h+1`, take the actual
source coordinates as phase zero.  Topological uniqueness forces the full
state to be precisely the decoder's phase-zero state and its successor to
be phase one.  The independent ordered-DAG exhaustion checked this stronger
compatibility explicitly.

### 2.4 Every-target fibre — survives

A zero at output coordinate `p` is equivalent to the event

\[
 E_p=\{x_p=1\text{ and }x_q=0\text{ for all }q\in\operatorname{Par}(p)\}.
\]

For `U=Z union T`, simultaneous occurrence of the selected events forces
`U` to one and `Par(U)` to zero.  The intersection is empty exactly when
these sets overlap; otherwise it leaves
`|P|-|U|-|Par(U)|` free bits.  Inclusion--exclusion over target-one
coordinates is therefore exactly equation (3).  Nothing in the derivation
assumes that the target is in the image, so zero-fibre targets are covered
without a separate case.  I found no incompatibility between this inverse
formula and the decoder or transient theorem.

## 3. Critical and Major findings

**None.**  No counterexample or broken inference was found in the support
conjugacy, source-phase extension, recurrent census, `h+1` entry bound, or
all-target fibre formula.

## 4. Minor finding

### `P133-A-m1` — the evidence ledgers point to theorem labels that do not exist

The frozen manuscript has Proposition 2.1, Lemmas 3.1--3.2,
Proposition 3.3, and the Section 4 fibre derivation under Theorem 1.1.  In
contrast, `PAPER_PLAN.md` and `CLAIMS_EVIDENCE.md` refer to objects such as
“Theorem 3.1,” “Corollary 3.2,” “Lemma 4.1,” “Theorem 4.2,” and “Theorem
5.1.”  Several of these locators do not exist in `main.tex`.  This does not
damage the proof, but it breaks the package's claim-to-evidence traceability.

**Evidence anchor:** absence: `main.tex` theorem structure — expected the
proof objects named by the two evidence ledgers; checked theorem/lemma/
proposition declarations and both Markdown matrices.  
**Severity:** Minor.  
**Confidence:** 5/5 — direct source comparison.

**Required repair:** update both ledgers to the frozen source labels.  A
minimal exact mapping is:

- C1: Proposition 2.1;
- C2: equations (6)--(7), Lemma 3.1, and the completeness paragraph after
  Proposition 3.3;
- C3: Lemma 3.1 plus the census paragraph after Proposition 3.3;
- C4: Lemma 3.2 and Proposition 3.3;
- C5: Theorem 1.1(iv) and the derivation in Section 4.

Do not renumber the sound manuscript merely to make the stale ledgers true.

## 5. Scope and owner boundary

The manuscript correctly assigns zero contribution credit to Euler's
product, prime-chain/Pratt geometry, signed AND--NOT representation, generic
DAG propagation, inclusion--exclusion, and finite-map bookkeeping.  This
Round-A review did not perform a new unbounded novelty search.  The existing
bounded non-hit must not be converted into novelty or priority evidence.
`HOLD_EXTERNAL` remains mandatory.

## 6. Round-A repair checklist

- [ ] Correct the proof-object locators in `PAPER_PLAN.md` and
  `CLAIMS_EVIDENCE.md`.
- [ ] Fresh raw verifier replay remains `cmp=0`.
- [ ] Four-stage isolated build remains byte-reproducible or any intended
  PDF change receives a new frozen round artifact.
- [ ] Preserve `Anonymous` and `HOLD_EXTERNAL`.

**Round-A disposition:** the theorem-level gate passes.  After the one
traceability repair, P133 is eligible for Round B without mathematical
reconstruction.
