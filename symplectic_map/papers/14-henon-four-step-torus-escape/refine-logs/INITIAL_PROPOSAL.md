# Initial Proposal

## Lifecycle

**SOURCE_DESIGN_DRAFT / PENDING_INDEPENDENT_REVIEW / NO_CODE / NO_RESULTS / NO_MANUSCRIPT**

## Historical starting point

The initial candidate concerned

\[
H(x,y)=(x^d+a y+c,x)
\]

over a characteristic-zero field, with a finite-rank subgroup
\(\Gamma\le K^\ast\) and the additional assumptions

\[
-1,a,c\in\Gamma.
\]

Its intended conclusion was a periodic-point bound

\[
\#\operatorname{Per}_{\Gamma}(H)
\le
4dE(3,3r)+81d^2,
\]

where the notation was meant to count points on periodic orbits whose every
coordinate lies in \(\Gamma\).

This historical statement was mathematically promising but not yet the right
paper:

- periodicity was unused by the proof;
- the orbit-containment notation was easy to misread;
- the coefficient-membership assumptions hid the fixed-coefficient form of
  ESS;
- the coefficient \(b\) of \(x^d\) was unnecessarily normalized to one;
- the four-step threshold and its sharp three-step failure were not
  foregrounded;
- two incompatible \(A/B/C\) naming conventions were possible.

## Original proof intuition

Writing

\[
x_{i+1}=x_i^d+a x_{i-1}+c
\]

produces a three-term unit equation at each local index. Nondegenerate
solutions should be bounded by Evertse--Schlickewei--Schmidt. Degenerate
solutions should be controlled by a finite transition graph on three labels.

The initial audit verified this idea in the normalized \(b=1\) setting and
found:

- at most \(dE(3,3r)\) local states over a nondegenerate index;
- four relevant local indices for a four-step window;
- three degeneracy types;
- a finite four-letter closure;
- a rank-one family with infinitely many three-step survivors.

## Defects requiring refinement

### 1. The main object was too weak

The proof never used a closing relation \(H^n(P)=P\). The natural object is

\[
T_4(H,\Gamma),
\]

and the periodic statement is only a corollary.

### 2. Orbit containment needed an exact definition

The set

\[
\operatorname{Per}(H)\cap\Gamma^2
\]

is not controlled by the proof. One point of an orbit may lie in
\(\Gamma^2\) while the next does not. The correct periodic objects are exact
periodic orbits \(\mathcal O\subseteq\Gamma^2\).

### 3. Coefficient membership was artificial

The unsafe normalization placed quantities such as

\[
\frac{b x_i^d}{x_{i+1}}
\]

inside \(\Gamma\), which would require coefficient membership. The correct
equation is

\[
\frac1c x_{i+1}
-\frac bc x_i^d
-\frac ac x_{i-1}=1.
\]

Here the variables lie in \(\Gamma^3\) and the coefficients are fixed. ESS
therefore uses rank \(3r\) with no enlarged group.

### 4. The full monomial coefficient should be retained

The same proof works for

\[
H(x,y)=(b x^d+a y+c,x)
\]

with arbitrary \(b\ne0\). This is a genuine strengthening and makes the
coefficient-free formulation transparent.

### 5. Degeneracy labels needed source-level locking

The final convention is

\[
\begin{aligned}
A&:a x_{i-1}+c=0,\\
B&:b x_i^d+c=0,\\
C&:b x_i^d+a x_{i-1}=0.
\end{aligned}
\]

Under this convention, the free adjacent chains are \(BA\) and \(CB\), and
the unique free three-letter chain is \(CBA\).

### 6. Sharpness needed headline status

The construction

\[
b=1,\quad a=-1,\quad c^{d-1}=-1,\quad
\Gamma=\langle2,c,-1\rangle
\]

shows that \(T_3\) is infinite in rank one for every \(d\ge2\). The paper is
therefore about a sharp window threshold, not merely periodic-point
finiteness.

## Initial nonclaims

Even at the starting stage, no claim was intended for:

- all rational or integral periodic points;
- positive characteristic;
- \(d=1\);
- \(abc=0\);
- arbitrary \(p(x)+ay\);
- numerical optimality;
- computations or scans.

The refined package adds further explicit nonclaims for the unproved
\(T_2/T_3\) hierarchy and the separate quartic Paper 15 reserve.

## Refinement decision

Replace the historical periodic-only candidate by the coefficient-free
four-step theorem, keep the explicit rank-one three-step family as the
sharpness theorem, and demote periodicity to the weighted orbit-contained
corollary.

