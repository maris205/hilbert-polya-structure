# Experiment plan — analytic only

This project has **zero numerical experiments**.  The word “experiment” denotes
reproducible symbolic checks of a fixed proof package, not data generation.

1. Recompute the three gradients and the shear inverses by hand and by a
   transparent line-by-line derivation in the manuscript.
2. Enumerate every gradient monomial and its exponent row in
   ℕ\(^6\), ordered ((q_1,q_2,q_3,p_1,p_2,p_3)).
3. Verify the two selector margins
   \(M_S=(g-2)-2x-2y\) and
   \(M_T=(2g-6)x+(g-6)y-6\); there is no third independent face gap.
4. Verify cone invariance using (U'_2-U'_1), (U'_3-U'_1), and (H), with
   the (g=8..11) and (g\ge12) coefficient split.
5. Prove old-term induction and characteristic-zero ℕ-semiring no-cancellation.
6. Check (C_g-A_g), (e_3)-visibility, the exact degree formula, PF limit,
   row-sum bound, characteristic polynomial, and the mod-5 irreducibility
   residues (g\equiv2,3,4\pmod5).
7. Record the (g=7) boundary failure and anti-examples.

No CAS, network, GPU, benchmark, or external experiment is authorized.  Any
future computation must be a separately approved deterministic proof check.

## Reproducibility worksheet

The following worksheet is copied into the later source lock.  It fixes the
order of the hand checks and prevents an apparently harmless change in the
selector from changing the theorem.

### W1: gradient rows

For each of the six rows, record (i) source potential, (ii) differentiated
variable, (iii) coefficient, and (iv) exponent row.  The coefficients are

\[
(2,g,2,2,2,2,2,g)
\]

in the order (V_1)-mixed, (V_1)-pure, (V_2), (V_3), (W_1), (W_2),
(W_3)-mixed, (W_3)-pure; these eight entries occupy six derivative rows.
Check that no row contains a negative exponent.

### W2: selector faces

The only independent face comparisons are the S face
\(M_S=(g-2)-2x-2y\) and the T face
\(M_T=(2g-6)x+(g-6)y-6\).  The region is
\(x,y\ge1, x+y<(g-3)/2\).  At (g=8), evaluate both at the limiting corner
and record positive slack; then show monotonicity in (g,x,y).  Do not invent
a third face gap or reuse a stale expression.

### W3: matrix and degree

Multiply (B_gA_g) entry by entry, then compare every row of (A_g) with
the three rows of (C_g).  Record (C_g-A_g), prove its entries positive,
and separately check the (e_3) carry.  The degree line must read exactly
\(e_3^TC_g^n\mathbf1\), not a maximum over an unproved collection of rows.

### W4: boundary and exclusions

The seed ((1,1)) for (g=7) is on the boundary (x+y=2), although its S
face gap is (1).  This is a domain boundary, not a tie.  Record this exact
wording in every later review.  Verify that all anti-claims (genericity,
entropy, periodic points, torus/conjugacy, arithmetic, positive characteristic,
priority) remain absent from title, abstract, theorem, and conclusion.

### W5: page budget

The planned manuscript has 24–29 substantive pages: two pages setup, five
pages selector and cone, six pages support induction, four pages matrix/degree,
three pages algebraic corollary, two pages collision and limitations, and two
to seven pages references/appendix.  A page count outside this interval is a
source-review blocker, not an invitation to weaken the proof.
