# Bounded primary-source owner checks

Search date: **2026-09-03 UTC**.  Scope was deliberately bounded to the three
piloted finalists and to exact-rule or nearest-owner queries.  This is a scout,
not a systematic review.  A missing search result is recorded only as a
non-hit and never as novelty evidence.

## Query families

The following query families were run against web/arXiv indexing, with exact
phrases where shown:

- RICS: `"incoming-copy" digraph dynamics`, `directed graph symmetrization
  copy incoming edges update vertex`, `directed graph local update replace
  outgoing edges by incoming edges`, and `directed reciprocity local update
  Markov chain`.
- CGT: `"x+n/gcd(x,n)"`, `"n/gcd(x,n)" iteration modulo n`, `iteration map x
  -> x + m/gcd(x,m) residues`, and `finite ring dynamics gcd map residues`.
- SSC: `de Bruijn automaton subset synchronization suffix shift`, `"suffix
  automaton" "power automaton" de Bruijn synchronization`, and `binary finite
  automata subset synchronization`.

## Primary sources inspected

1. Mei Yin and Lingjiong Zhu, [*Reciprocity in directed
   networks*](https://arxiv.org/abs/1412.2187).  This studies reciprocity via
   microcanonical/canonical/grand-canonical random directed-graph ensembles and
   reciprocal subgraph densities.  It does not state the RICS vertex-copy rule
   or its absorbing conflict deletion.
2. Daniel Cirkovic, Tiandong Wang, and Sidney I. Resnick,
   [*Preferential attachment with reciprocity: properties and
   estimation*](https://doi.org/10.1093/comnet/cnad031).  Its process grows a
   graph and probabilistically adds a reverse edge when an edge is created.  It
   is a relevant reciprocity owner boundary, but not a fixed-carrier operation
   copying an entire incoming star to the outgoing star.
3. Vojtech Vorel, [*Subset Synchronization and Careful Synchronization of
   Binary Finite Automata*](https://arxiv.org/abs/1403.3972).  This is direct
   primary evidence that binary subset synchronization is a mature subject.
   It reinforces the SSC kill; the scout does not attempt to distinguish a
   trivial shift-register instance into a standalone paper.
4. Guangwu Xu and Yi Ming Zou, [*Linear Dynamical Systems over
   Finite Rings*](https://arxiv.org/abs/0810.3164).  This establishes a broad
   owner boundary for finite-ring cycle structure, but concerns linear maps.
   CGT is nonlinear and switches translations by `p`-adic valuation.  The
   source therefore does not discharge the need for a dedicated nonlinear
   owner search.

## Disposition by candidate

### RICS

No exact-rule primary hit was found in the bounded queries.  The nearest
primary sources use reciprocal-edge statistics or graph growth, not the fixed
labelled carrier, incoming-star copy, conflict-graph deletion, or
first-occurrence-order endpoint kernel.

**Status:** internal KEEP; `HOLD_EXTERNAL`.  Non-hit is not novelty.

### CGT

No exact formula hit for `x -> x+p^a/gcd(x,p^a)` was found in the bounded
queries.  Broad finite-ring dynamics sources are not enough because the rule
is nonlinear; a formula-level MathSciNet/zbMATH/Crossref and citation-chain
audit is still required before drafting.

**Status:** conditional internal KEEP; `HOLD_EXTERNAL`.  Non-hit is not
novelty.

### SSC

The bounded search immediately reached primary subset-synchronization work,
and the literal machine is visibly a binary shift register whose every
length-`d` word is a reset word.  Together with the internal P55 title, this is
enough for an internal kill without pretending to settle bibliographic
identity.

**Status:** KILL as a paper candidate.

## Required next external gate

If RICS or CGT is selected, an independent reviewer must search exact formulas,
synonyms, citations, and non-arXiv databases, then bind every claimed
owner/non-owner distinction to inspected sources.  Until then the only valid
label is **HOLD_EXTERNAL**.
