# P175 source verification

**Checked:** 2026-09-03 UTC  
**Scope:** primary bibliographic records and owner subtraction through Round 2  
**External state:** `HOLD_EXTERNAL`

This is a source-verification ledger, not a novelty certificate.  A query
miss is never interpreted as proof that the literal self-map is new.

## Verified primary records

### Young — additive matrix commutators

- Hsu-Wen Vincent Young, “On Matrix Pairs with Diagonal Commutators,”
  *Journal of Algebra* **570** (2021), 437–451.
- DOI: <https://doi.org/10.1016/j.jalgebra.2020.11.023>
- Bib key: `Young2021`.
- **Use:** establishes a nearby owner region for pairs of matrices whose
  additive commutator has prescribed diagonal form.  It is not cited as a
  study of the feedback self-map (A\mapsto[\Delta(A),A]).

### Kadyrsizova–Yerlanov — commutator-matrix algebraic sets

- Zhibek Kadyrsizova and Madi Yerlanov, “Algebraic Sets Defined by the
  Commutator Matrix,” *Journal of Algebra* **589** (2022), 29–50.
- DOI: <https://doi.org/10.1016/j.jalgebra.2021.09.012>
- Author manuscript: <https://arxiv.org/abs/2006.13514>
- Bib key: `KadyrsizovaYerlanov2022`.
- **Use:** owns algebraic-set questions defined by entries of an arbitrary
  matrix commutator.  No claim is made that it derives P175's finite
  functional graph.

### Baddeley — images of commutator maps

- Robert W. Baddeley, “Images of Commutator Maps,” *Communications in
  Algebra* **22**(8) (1994), 3023–3035.
- DOI: <https://doi.org/10.1080/00927879408825010>
- Bib key: `Baddeley1994`.
- **Use:** primary owner pointer for image questions about group commutator
  maps.  P175 does not claim ownership of commutator-image language.

### Larsen–Lu — commutator-map fibres/flatness

- Michael Larsen and Zhipeng Lu, “Flatness of the Commutator Map over
  (\mathrm{SL}_n),” *International Mathematics Research Notices*
  **2021**(8), 5605–5622.
- DOI: <https://doi.org/10.1093/imrn/rnz285>
- Author manuscript: <https://arxiv.org/abs/1807.07300>
- Bib key: `LarsenLu2021`.
- **Use:** owns a major algebraic-geometric fibre direction for the ordinary
  two-input commutator map.  Its map is not P175's one-input state feedback.

### Bier — fixed regular triangular Engel equations

- Agnieszka Bier, “On Solvability of Engel Equations in the Group of
  Triangular Matrices over a Field,” *Linear Algebra and its Applications*
  **438**(5) (2013), 2320–2330.
- DOI: <https://doi.org/10.1016/j.laa.2012.10.009>
- Bib key: `Bier2013`.
- **Use:** direct owner for the fixed-regular triangular Engel mechanism
  underlying internal paper P119.  P175 assigns zero credit to P119's
  fixed-element commutator update, centralizer-coset fibre engine, and
  filtration tree.  The residual distinction is literal: P175's diagonal
  is extracted from the evolving state, and its inverse equation becomes a
  support-colouring sum rather than a centralizer coset.

### Sokal — Potts/Tutte/chromatic owner region

- Alan D. Sokal, “The Multivariate Tutte Polynomial (Alias Potts Model) for
  Graphs and Matroids,” in *Surveys in Combinatorics 2005*, LMS Lecture Note
  Series 327, 173–226.
- DOI: <https://doi.org/10.1017/CBO9780511734885.009>
- Author manuscript: <https://arxiv.org/abs/math/0503607>
- Bib key: `Sokal2005`.
- **Use:** primary survey/owner pointer for multivariate Tutte–Potts and
  chromatic partition functions.  With complete-graph activities `-1` on
  edges of `G` and `X^2-1` on nonedges, its spin formula is exactly
  `P_{G,q}(X;1)`; this identity receives zero contribution credit.

### Stanley — chromatic symmetric occupation owner

- Richard P. Stanley, “A Symmetric Function Generalization of the Chromatic
  Polynomial of a Graph,” *Advances in Mathematics* **111**(1) (1995),
  166–194.
- DOI: <https://doi.org/10.1006/aima.1995.1020>
- Author manuscript: <https://math.mit.edu/~rstan/pubs/pubfiles/100.pdf>
- Bib key: `Stanley1995`.
- **Use:** the `q`-variable truncation of the chromatic symmetric function is
  the proper-colouring occupation enumerator.  P175's marked polynomial is
  its deterministic coefficientwise transform multiplying occupation
  `r` by `X^(sum r_alpha(r_alpha-1))`; neither object is retained as a new
  combinatorial invariant.

### Artin–Mazur — dynamical zeta bookkeeping

- Michael Artin and Barry Mazur, “On Periodic Points,” *Annals of
  Mathematics* **81**(1) (1965), 82–99.
- DOI: <https://doi.org/10.2307/1970384>
- Bib key: `ArtinMazur1965`.
- **Use:** owner for the periodic-point zeta construction.  The conversion
  of the single fixed point to ((1-z)^{-1}) receives no novelty credit.

## Search and subtraction protocol

The audit used exact-title, DOI, keyword, and map-shape searches around
“diagonal commutator,” “commutator map fibre,” “matrix commutator finite
field,” “state-dependent diagonal commutator,” and weighted
proper-colouring/Potts sums.  Metadata were cross-checked against publisher
or DOI landing records and, where available, author manuscripts.

The following claims are deliberately **not** made:

1. that the identity
   ([\operatorname{Diag}(d),A]_{ij}=(d_i-d_j)a_{ij}) is new;
2. that graph colourability has not appeared in commutator theory;
3. that the marked sum in P175 defines a new Potts model or a new
   occupation enumerator;
4. that P175 improves the ordinary two-input commutator-map literature;
5. that P175 is disjoint from every fixed-element commutator system merely
   because its literal update is different; or
6. that a bounded search miss establishes novelty, priority, or safety to
   circulate.

After Review-B subtraction, the residual is only the literal scalar-equation
reduction from the state-feedback matrix map to target support colourings,
its application simultaneously to every target, and the consequent complete
rooted functional graph.  The exact Potts specialization, chromatic-
symmetric occupation enumerator, and deterministic occupation weighting are
zero credit.  Broader novelty assessment remains open; hence
`HOLD_EXTERNAL`.

## Bibliography hygiene

- Every entry in `references.bib` is cited in `main.tex`.
- Every citation has a defined ownership role above.
- No unverified search result, secondary blog, or generated citation is
  included.
- Eight bibliography entries are present; there are no uncited padding
  references.
