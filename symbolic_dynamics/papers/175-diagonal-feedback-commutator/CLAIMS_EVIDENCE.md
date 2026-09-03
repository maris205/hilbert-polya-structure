# P175 claims–evidence ledger

**Round:** final Round 2; dual hostile reviews closed  
**External state:** `HOLD_EXTERNAL`  
**Rule:** exact enumeration is falsification evidence; the uniform argument is
the proof.

## Claim C1 — literal entry formula and two-step collapse

For (A\in M_n(\mathbb F_q)),

\[
\Phi(A)_{ij}=(a_{ii}-a_{jj})a_{ij},\qquad \Phi^2(A)=0.
\]

- **Proof:** direct multiplication by the diagonal matrix; every first image
  has zero diagonal, so its extracted diagonal is zero.
- **Paper location:** equations (1)–(2), Theorem 3.
- **Exact control:** every source arrow in all eleven boxes; zero output
  diagonal and literal second iterate tested separately.
- **Boundary witness:** (n=1) has height one; for (n\ge2), two distinct
  diagonal values and one nonzero off-diagonal entry produce a nonzero first
  image, so height two is sharp.

## Claim C2 — exact every-target fibre

If (B) has nonzero diagonal then its fibre is empty.  If its diagonal is
zero and (G_B) is its undirected off-diagonal support, then

\[
|\Phi^{-1}(B)|=
\sum_{c\in\operatorname{Col}_q(G_B)}
q^{\sum_\alpha n_\alpha(c)(n_\alpha(c)-1)}.
\]

The labelled occupation refinement is the coefficient statement for

\[
\mathcal P_{G,q}(X;\boldsymbol z)=
\sum_{c\in\operatorname{Col}_q(G)}
X^{m(c)}\prod_\alpha z_\alpha^{n_\alpha(c)}.
\]

- **Proof:** freeze (c_i=a_{ii}).  For each ordered (i\ne j), the equation
  ((c_i-c_j)a_{ij}=b_{ij}) has one solution if the colours differ, (q)
  solutions if they agree and (b_{ij}=0), and no solution if they agree
  and (b_{ij}\ne0).  Properness is exactly the simultaneous consistency
  condition.
- **Paper location:** Theorem 1.
- **Exact control:** every codomain target in every box; aggregate indegree
  and each labelled occupation class checked independently.
- **Prime-power control:** includes the explicit field
  (\mathbb F_4=\mathbb F_2[x]/(x^2+x+1)).
- **Exact owner identity:** with complete-graph Potts activities `-1` on
  support edges and `X^2-1` on nonedges,
  `Z_Potts(K_n)=P_{G,q}(X;1)`.  Stanley's chromatic symmetric function owns
  the labelled proper-colouring occupation enumerator; the `X` weight is a
  deterministic coefficient transform.  All three graph-polynomial steps
  receive zero credit.
- **Residual:** the state-extracted diagonal converts each ordered matrix
  equation into this support-colouring evaluation for every target.

## Claim C3 — image criterion and support-only fibres

\[
B\in\operatorname{im}\Phi
\iff \operatorname{diag}(B)=0\text{ and }\chi(G_B)\le q.
\]

For zero-diagonal targets the fibre size depends on (B) only through
(G_B).

- **Proof:** all summands in C2 are positive integers, so the sum is nonzero
  exactly when a proper (q)-colouring exists.
- **Paper location:** Theorem 1, equation (7).
- **Exact control:** membership compared target by target; all targets with a
  common support compared with the same independently computed graph sum.

## Claim C4 — exact image and zero-fibre formulas

\[
I_{n,q}=\sum_{\substack{G\subseteq K_n\\\chi(G)\le q}}
(q^2-1)^{|E(G)|},
\]

\[
\kappa_{n,q}=\sum_{\substack{(r_\alpha)\ge0\\\sum r_\alpha=n}}
\binom n{(r_\alpha)}q^{\sum_\alpha r_\alpha(r_\alpha-1)}.
\]

- **Proof for the image:** choose the labelled support graph.  Each support
  edge carries an ordered pair in (\mathbb F_q^2\setminus\{(0,0)\}), hence
  (q^2-1) independent choices.
- **Proof for the zero fibre:** every colouring is allowed for the empty
  support; group it by its labelled occupation vector.
- **Paper location:** Corollary 2.
- **Exact control:** the verifier constructs the actual support census, then
  compares it with a separate enumeration of all simple support masks.  The
  weak-composition sum is also evaluated independently.

## Claim C5 — zero is the unique maximum fibre

- **Proof:** any nonzero zero-diagonal target has a support edge, so its
  proper-colouring set is a strict subset of the colourings contributing to
  the zero fibre; all weights are positive.  A target with nonzero diagonal
  has fibre zero.
- **Paper location:** Corollary 2.
- **Exact control:** maximum and uniqueness tested in all eleven boxes.
- **Boundary:** includes (n=1), where every nonzero target has nonzero
  diagonal and is unreachable.

## Claim C6 — whole functional graph and all-time fibres

The only recurrent state is zero.  The depth layers are

\[
(D_0,D_1,D_2)=(1,\kappa_{n,q}-1,q^{n^2}-\kappa_{n,q}).
\]

There are (I_{n,q}-1) nonzero depth-one branch vertices and
(\kappa_{n,q}-I_{n,q}) depth-one leaves.  A branch vertex of support (G)
has (\mathcal P_{G,q}(q;\boldsymbol1)) depth-two leaf predecessors.  For
(t\ge2), every state maps to zero, so the only nonempty time-(t) fibre is
the zero fibre, of size (q^{n^2}).

- **Proof:** C1 gives (\operatorname{im}\Phi\subseteq\Phi^{-1}(0)); combine
  this with C2–C4 and partition the carrier.
- **Paper location:** Theorem 3 and equation (15).
- **Exact control:** literal depth of every source, fixed points of the first
  and second iterates, second image, and total depth-two mass all checked.

## Claim C7 — zeta bookkeeping

All iterates have exactly one fixed point, hence
(\zeta_\Phi(z)=(1-z)^{-1}).

- **Proof:** C1 and the definition of the Artin–Mazur zeta function.
- **Paper location:** equation (16).
- **Owner:** the zeta conversion is explicitly credited to Artin–Mazur; it
  is not counted as a new mechanism.

## Computational certificate

- Program: `verify_p175.py` (Python standard library only).
- Settled boxes:
  ((1,2),(1,3),(1,4),(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(3,4),(4,2)).
- Expected settled count: **2,111,465 assertions**.
- The canonical transcript and edge digest are frozen in
  `verification_output.txt` after two byte-identical fresh runs.

## Ownership and status guard

The following receive zero contribution credit: the elementary diagonal
commutator identity; classical additive matrix commutator results; general
group commutator image/fibre results; Bier's fixed-regular triangular Engel
mechanism and its internal P119 use; proper colouring, the exact multivariate
Potts specialization, Stanley's occupation enumerator, its deterministic
weight transform; and the Artin–Mazur zeta conversion.  The residual is the
literal matrix-to-support reduction, its every-target application, and the
consequent rooted tree.  The source search was bounded, so it cannot
establish novelty.  Status remains `HOLD_EXTERNAL`.

Hostile Review B independently passed 2,559,272 assertions, including
genuine `GF(4/8/9/16)` fields and the exact Potts/occupation transforms.  It
found no mathematical defect; its sole Major finding is this owner reframe.
