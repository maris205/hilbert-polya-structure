# Paper Plan

Status: immutable internal Round 0 retained; accepted Review-A repair is the
current four-page manuscript under `OWNER_RED_AMBER/HOLD_EXTERNAL`.

## Purpose and audience

The document is a short, self-contained algebraic-combinatorics theorem note for readers familiar with permutations, transpositions, parking functions, and Hurwitz moves. Its purpose is to analyze one literal deterministic scheduler. It is not a novelty announcement.

One-sentence contribution contract:

> This note analyzes the least lower-endpoint-collision Hurwitz scheduler on minimal long-cycle factorizations, proving its sharp transient structure, fixed census, and complete labelled one-step inverse atlas.

## Claim hierarchy

The paper should keep four results at theorem level:

1. strict increase of executed indices, fixed-only recurrence, and the sharp (n-2) tail;
2. the exact fixed count ((n-1)^{n-2});
3. the every-target inverse-Hurwitz fibre formula;
4. maximum indegree (n-1) with a unique labelled maximizer.

The history-set law must remain a visibly separated conjecture. Its only evidence is exhaustive (n\le8) computation and an independent (n=9) stream. No abstract, introduction, conclusion, caption, or table may phrase it as proved for all (n).

## Current section architecture

### Abstract

Define the map in one sentence, state the four proved axes, quarantine the history law, subtract the classical ingredients, and display the owner gate. Avoid words such as "novel", "new", "first", or "complete" when they could be read as priority claims; "complete labelled fibre" is allowed only as a mathematical completeness claim for the proved atlas.

### 1. Convention, map, and subtraction

Freeze product order, long-cycle orientation, right Hurwitz convention, lower-endpoint order, and least-index scheduling. Identify classical ingredients and give them zero contribution credit. State the bounded-owner-search limitation explicitly.

### 2. Strictly advancing collisions

Lead with the local pair calculation. Prove that previous comparisons stay unchanged and the active equality disappears. Derive termination, fixed-only recurrence, and tail bound. Finish with the explicit sharp witness.

### 3. Exact fixed-state census

Invoke the classical lower-endpoint parking-function bijection. Translate fixedness to adjacent inequality. Give the circular parking count with its translation orbit size and unique normalization.

### 4. Every-target inverse Hurwitz atlas

Define the target's first collision and reverse admissibility. Derive the unique inverse pair, prove necessity and sufficiency of the scheduler condition, then establish the global bound and uniqueness of the maximizer.

### 5. A verified history law left open

State the exact history-set formula as a conjecture. Record finite evidence and the missing bijective step. Explicitly withhold theorem status from the binomial depth law, unique deepest-state consequence, and any basin formula derived from it.

### 6. Controls and limitations

Explain which properties the verifiers check and which conventions they freeze. Reiterate that computation is regression pressure, not proof or novelty evidence. End with `HOLD_EXTERNAL`.

## Proof dependency order

The manuscript's logical spine is:

\[
\text{local collision algebra}
\Longrightarrow \text{increasing histories}
\Longrightarrow \text{termination and sharp tail},
\]

while the other axes branch independently:

- classical lower-endpoint bijection + Pollak model \(\Longrightarrow\) fixed census;
- inverse Hurwitz algebra + least-index test \(\Longrightarrow\) every-target fibre;
- fibre atlas + parking inequalities \(\Longrightarrow\) unique maximum indegree.

The conjectural history law is downstream of none of these proofs and must not be used to prove them.

## Length and presentation

The immutable Round-0 cold build is three A4 pages. The current accepted-repair
cold build is four A4 pages after adding the nearest-source subtraction and
explicit boundary cases; it remains a compact theorem note. No mandatory
figure is needed. Equations, the sharp witness, and the reverse-admissibility
test carry the exposition.

## Round-1 gates

Before a Round-1 circulation candidate:

- conduct and freeze a query-by-query external exact-scheduler owner search;
- have an independent reader check the product/orientation convention and inverse atlas;
- either prove the history-set law bijectively or keep it a conjecture without derived theorem language;
- decide whether the internal owner risk is acceptable after external subtraction;
- rerun both canonical transcripts and the deterministic cold build.

No venue targeting, submission positioning, or novelty language is authorized in Round 0.
