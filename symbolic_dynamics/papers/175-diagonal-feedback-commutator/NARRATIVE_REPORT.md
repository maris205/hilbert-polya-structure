# P175 narrative report — diagonal-feedback commutator

**Round:** final Round 2; dual hostile reviews closed.  
**Paper type:** anonymous AMS short note.  
**Lifecycle:** `GREEN_OWNER_THIN / HOLD_EXTERNAL`.  
**Figure:** N/A; the exact formulas are clearer than a diagram.

## One-sentence thesis

Extracting a matrix's diagonal and commuting it back against the same matrix
produces a universal two-step functional tree whose image and every-target
fibres are controlled exactly by proper colourings of the target support
graph.

## Literal object

For a finite field (K=\mathbb F_q), set

\[
\Delta(A)=\operatorname{Diag}(a_{11},\ldots,a_{nn}),\qquad
\Phi(A)=[\Delta(A),A]
\]

on all of (M_n(K)).  The standard ordered basis is part of the definition;
the map is not similarity invariant.

## Technical story

The entrywise identity

\[
\Phi(A)_{ij}=(a_{ii}-a_{jj})a_{ij}
\]

drives both halves of the paper.  It immediately erases the diagonal, hence
(\Phi^2=0).  It also turns an inverse problem into a colouring problem:
after fixing the input diagonal (d_i), every nonzero target entry forces
(d_i\ne d_j), while an equal-colour ordered pair makes the corresponding
input entry free.  Thus:

1. a target is reachable exactly when it has zero diagonal and its undirected
   nonzero support graph is (q)-colourable;
2. each proper colouring contributes
   (q^{\sum_\alpha n_\alpha(n_\alpha-1)}) sources;
3. retaining the labelled occupation vector gives a multivariate
   proper-colouring partition sum, not only an aggregate indegree; this sum
   is an exact Potts specialization and Stanley-occupation transform and is
   therefore zero credit;
4. grouping targets by support gives the exact image size; and
5. the zero-target specialization gives the kernel, all depth layers, and
   the complete rooted functional tree.

## Strongest formulas

For a zero-diagonal target (B), let (G_B) join (i,j) when at least one
of (b_{ij},b_{ji}) is nonzero.  For a proper colouring
(c:[n]\to\mathbb F_q), let (n_\alpha(c)=|c^{-1}(\alpha)|) and
(m(c)=\sum_\alpha n_\alpha(c)(n_\alpha(c)-1)).  Then

\[
|\Phi^{-1}(B)|=\sum_{c\in\operatorname{Col}_q(G_B)}q^{m(c)}.
\]

The image and kernel sizes are

\[
I_{n,q}=\sum_{\substack{G\subseteq K_n\\\chi(G)\le q}}
(q^2-1)^{|E(G)|},
\]

and

\[
\kappa_{n,q}=\sum_{r_1+\cdots+r_q=n}
\binom{n}{r_1,\ldots,r_q}
q^{\sum_i r_i(r_i-1)}.
\]

The depth layers are (1,\kappa_{n,q}-1,q^{n^2}-\kappa_{n,q}), and the
all-time fibres collapse to the full carrier over zero from time two onward.

## Owner subtraction

The paper assigns no contribution credit to any of the following:

- the algebra of matrix commutators or the fact that a commutator with a
  diagonal matrix has zero diagonal;
- arbitrary-pair diagonal/zero-diagonal commutator varieties studied by
  Young and by Kadyrsizova--Yerlanov;
- fixed-element group commutator maps or general commutator-fibre questions;
- Bier's fixed-regular triangular Engel image theorem, which directly owns
  the principal input behind internal paper P119;
- proper colourings, the exact complete-graph Potts specialization, Stanley's
  chromatic symmetric occupation enumerator, and its deterministic marked
  transform; and
- the formal Artin--Mazur conversion from cycle counts to a zeta function.

The narrow residual is the matrix-to-support reduction forced by this
state-feedback self-map, its simultaneous every-target application, and the
resulting complete height-two functional tree.  No bounded search miss is
described as novelty.

## Evidence and limits

The proof is uniform in every prime power (q) and every (n\ge1).  An
independent standard-library verifier exhausts prime-field boxes and the
nonprime field (\mathbb F_4), compares every codomain target with the
marked fibre formula, checks the image census by a second graph enumeration,
and reconstructs every depth layer.  Enumeration is falsification evidence,
not the proof.

The temporal axis is deliberately shallow, and the proper-colouring
partition sum is owner-crowded.  Both hostile reviews are now closed, but
these limitations keep external circulation, novelty, priority, and
submission on `HOLD_EXTERNAL`.
