# Fresh 51: complete-graph unit diffusion — no nomination

Author desk, 2026-09-11. Owned scope: this directory only. No scientific program or pilot was executed; no child agents, central-state changes, paper-number changes or Git operations. This is not an independent review or an admission record.

## Literal candidate and finite restriction

On integer vectors on the labelled complete graph, consider

\[
F(x)_i=x_i+\#\{j:x_j>x_i\}-\#\{j:x_j<x_i\}.
\]

The whole integer state space is infinite. A cube is not automatically invariant: for n ≥ 3, the coordinate M−1 in (M−1,M,…,M) becomes M+n−2. Thus bounded initial labels alone do not define the required finite autonomous system.

For a genuine finite restriction, fix nonempty labelled blocks A,B of sizes a,b, n=a+b, an integer total S and an integer D ≥ n. Retain vectors constant u on A and v on B with au+bv=S and |v−u|≤D. Equivalently, the states are integers

\[
Q=\{d:|d|\le D,\quad S-bd\equiv0\pmod n\},
\qquad u=(S-bd)/n,\quad v=u+d.
\]

Empty parameter instances may be discarded. For d>0, u gains b and v loses a; for d<0 the signs reverse; equality is fixed. Consequently this restriction is conjugate to

\[
T(d)=d-n\operatorname{sgn}(d),\qquad T(0)=0.
\]

Congruence is preserved. If |d|≥n, its absolute value decreases by n; if 0<|d|<n, its new absolute value is n−|d|≤D. This proves finite invariance without an orbit cutoff assumption.

## What the restriction supplies, and why it does not survive subtraction

The recurrent states are exactly d=0 and 0<|d|<n. The former is fixed and the latter have exact period two. Writing |d|=kn+r, 0≤r<n, gives the exact entrance time h(d)=k: before k steps the gap has magnitude at least n; at step k it is zero if r=0 and otherwise has magnitude r. This is just Euclidean division of the one-dimensional translation, not a second mechanism.

The complete one-step inverse also collapses to the same scalar rule:

\[
T^{-1}(y)=\bigl(\{y+n:y+n>0\}\cup\{y-n:y-n<0\}
\cup\{0:y=0\}\bigr)\cap Q.
\]

Here each conditional set is either a singleton or empty. Exhaustiveness follows by splitting a source into positive, negative and zero. Hence every fibre has size at most three. This trivial branch inversion is not an independent research axis.

## Local and primary-source subtraction

Local original evidence read:

- `docs/papers162_166_sequence/scouting/open_fresh_p166_round8/OWNER_SEARCH_LOG.md`, BLM discussion at lines 66–96: strict-local-maximum clockwise transfer is a different literal rule, while parallel diffusion is already an identified ambient owner.
- `docs/papers204_208_sequence/scouting/graph_relation_second/SCOUT_REPORT.md`, GLD discussion at lines 15–38: sending to a selected least lower neighbour is not the present send-to-every-lower-neighbour rule. These are not asserted to be exact duplicates.

Direct primary source: C. Duffy, T. F. Lidbetter, M. E. Messinger and R. J. Nowakowski, [A Variation on Chip-Firing: the diffusion game](https://arxiv.org/pdf/1609.05792), DMTCS 20:1 (2018), #4. The actual PDF was opened and selected passages read. Equation (1), printed p. 2, is exactly F on a general graph. Theorem 3.4 and its proof, printed pp. 12–13, cover two-level complete-graph configurations, preserve each level block, and subtract |A|+|B| from the positive gap until equality or order reversal. Thus the proposed finite restriction and its clock use an already explicit proof mechanism. The floor formula above is recorded as an elementary consequence, not claimed to appear verbatim in the paper. Theorem 3.1's order-reversal criterion was also read; no uninspected general temporal classification is attributed to it.

A second actual primary PDF, [Mullen, Nowakowski and Cox, Complete Graphs and Polyominoes](https://arxiv.org/pdf/2010.07745), was opened at its beginning. It gives the same diffusion rule and announces complete-graph recurrent-configuration enumeration. Its detailed equivalence/counting conventions were not read, so no exact enumeration theorem from it is used here. No claim of exhaustive literature coverage is made.

## Disposition

**NO NOMINATION.** This is a nonprojection dynamics, but both the literal update and the useful two-level temporal mechanism have a direct owner. The honest finite wrapper does not restore novelty, and scalar inverse branching supplies no independent residual. No widening of parameters, execution or manuscript work is justified by this desk. Existing occupied work is not reopened. Native read/search calls supported this author assessment; no immutable raw-source package or fresh verification PASS is claimed.
