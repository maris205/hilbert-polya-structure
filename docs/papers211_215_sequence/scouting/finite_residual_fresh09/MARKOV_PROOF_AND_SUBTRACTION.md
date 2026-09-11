# Bounded Markov descent: exact proof, exact old-literal collision

Status: the statements below are PROVABLE AS STATED, as author deductions.
Research disposition: NO_NOMINATION. Author:
`/root/round211_finite_matching_scout/p213_title_record_check`.
No scientific execution or independent review is claimed.

## Literal, carrier and dependencies

For an integer B>=1 let
$$
 X_B=\{(a,b,c)\in\mathbb Z_{>0}^3:
 1\le a\le b\le c\le B,\quad a^2+b^2+c^2=3abc\}.
$$
The root r=(1,1,1) is fixed. At every other state set
$$
 D_B(a,b,c)=\operatorname{sort}(a,b,3ab-c).
$$
The carrier has actual sorted triples, not Markov numbers alone; equal
largest numbers in different triples are not identified. There is no
Frobenius uniqueness assumption, reduction modulo B, scheduler or added
clock. Dependencies are integer Vieta factorization, monotonicity of the
larger quadratic root and the Fibonacci recurrence.

## 1. Totality, strict descent and recurrent set

Put g(t)=t^2-3ab t+a^2+b^2. Its roots are c and
$$
 d=3ab-c=(a^2+b^2)/c>0.
$$
Thus d is a positive integer and the Vieta replacement preserves the
equation. Moreover
$$
 g(b)=a^2-(3a-2)b^2\le0,
$$
with equality exactly when a=b=1: for a=1 this is 1-b^2,
while a>=2 gives a strictly negative value since b>=a.
Except at a=b=1, the point b lies strictly between the two roots, so
0<d<b<c. For a=b=1 the equation is c^2-3c+2=0:
the only states are r and (1,1,2), the latter descending to r.
Every nonroot step therefore strictly lowers the largest coordinate and
the sum. In particular D_B maps X_B into X_B.

Since X_B is finite, strict descent terminates at r and no nonroot state
can recur. The recurrent/fixed set is exactly {r}. This argument also
proves that each sorted triple has a unique parent without requiring any
uniqueness theorem about individual Markov numbers.

## 2. Full every-target inverse, including the root and the cap

For a target t=(a,b,c) define
$$
 C_1(t)=(a,c,3ac-b),\qquad C_2(t)=(b,c,3bc-a).
$$
Then, as a SET (not a multiset),
$$
 D_B^{-1}(t)=
 \{C_1(t):3ac-b\le B\}\cup
 \{C_2(t):3bc-a\le B\}\cup
 \begin{cases}\{r\},&t=r,\\ \varnothing,&t\ne r.\end{cases} \tag{1}
$$
A repeated child occurs when a=b and is counted once.

Proof of sufficiency. Both replacements satisfy the Markov equation by
Vieta. For C_1, the old coordinate b is the smaller root of
z^2-3ac z+a^2+c^2. At z=c this quadratic is
a^2-(3a-2)c^2, negative except when a=c=1. Hence the other root
3ac-b is strictly larger than c. At the exception t=r it equals 2>1.
The same argument with b in place of a proves 3bc-a>c.
Thus the children are already sorted, are nonroot, and descend exactly
to t. The indicated cap tests are the only extra membership conditions.

Proof of necessity. Let s=(u,v,w) be a nonroot predecessor. The descent
proof gives w>v, and its new coordinate is at most v (strictly less
except at (1,1,2)). Therefore the largest coordinate of its target is
v=c. The two other target entries are u and 3uv-w, so
(u,3uv-w) is (a,b) or (b,a). Solving for w gives exactly the two
children. The only root source is r and only for target r. This proves
both directions and exhaustiveness of (1).

Since
$$
 (3bc-a)-(3ac-b)=(b-a)(3c+1)\ge0,
$$
the larger-child cap condition implies the smaller one.
Every nonroot fibre has size at most two. The root fibre has size one
for B=1 and size two for B>=2: r and (1,1,2).
Consequently the sharp full-carrier maximum is 1 if B=1 and 2 if B>=2.
For B>=2 the complete maximizing-target description is r together with
those nonroot targets satisfying a<b and 3bc-a<=B.
Indeed a<b makes the two children distinct; a=b makes them identical.
No enumeration of Markov numbers is used.

## 3. Exact worst entrance time under a coordinate cap

Let F_0=0,F_1=1,F_(k+2)=F_(k+1)+F_k and set r_d=F_(2d+1).
Thus r_0=1,r_1=2 and r_(d+1)=3r_d-r_(d-1) for d>=1.
Repeated Vieta extension from (1,1,1) produces
$$
 t_0=(1,1,1),\qquad t_d=(1,r_{d-1},r_d)\quad(d\ge1).
$$
The recurrence and Vieta identity prove these are Markov triples and
D(t_d)=t_(d-1). Their depth is exactly d. Positivity and strict growth
of r_d follow inductively from r_1>r_0>0 and the recurrence.

For any parent whose maximum coordinate is c, every child has form
(u,c,w), with 1<=u<=c and w the larger root, hence
$$
 w=\frac{3uc+\sqrt{u^2(9c^2-4)-4c^2}}2
 \ \ge\ h(c):=\frac{3c+\sqrt{5c^2-4}}2. \tag{2}
$$
For c>=1 the radical is real; both terms strictly increase with u>=1.
Also h strictly increases on c>=1. The displayed branch gives
h(r_d)=r_(d+1), including h(1)=2: for d>=1 its consecutive
Markov triples make r_(d-1) and r_(d+1) the two quadratic roots.

Induction on depth now shows that every depth-d triple has maximum
coordinate at least r_d. The case d=0 is r. If the claim holds for a
parent at depth d, (2) bounds every depth-(d+1) child by r_(d+1).
The t_d branch attains the bound at every depth. Therefore the exact
maximum entrance time on the full capped carrier is
$$
 \boxed{H(B)=\max\{d\ge0:F_{2d+1}\le B\}.} \tag{3}
$$
There are no ceiling/logarithm rounding assumptions, and B=1 gives zero.
The elementary derivation of this particular cap formula is recorded
here without a priority claim.

## 4. Exact historical subtraction and primary ownership

The original
[old VMD ledger](../../../papers157_161_sequence/scouting/replacement_probabilistic_geometric/SCOUT.md)
at its VMD row explicitly gives sorted positive Markoff triples with the
unique sum-decreasing Vieta mutation and kills it as the classical tree.
Section 1 proves that this is precisely the largest-coordinate replacement
used here away from the root. Root fixation totalizes its stopping state;
X_B is a forward-invariant coordinate-cap restriction. This is not a new
update concealed by a new cap parameter.

The classical equation, Vieta moves and generation from (1,1,1) are stated
on pp. 1–2 of Bourgain–Gamburd–Sarnak,
[Markoff Triples and Strong Approximation](https://arxiv.org/pdf/1505.06411).
The binary-tree child mechanism is also stated in the introduction of
Lagisquet–Pelantová–Tavenas–Vuillon,
[On the Markov numbers: fixed numerator, denominator, and sum conjectures](https://arxiv.org/pdf/2010.10335);
its Section 2.2.2 identifies the classical odd-indexed Fibonacci branch.
Only these basic owner facts are used, not those papers' strong-approximation
or monotonicity/uniqueness results.

The older simultaneous finite-field SMV map (yz-x,zx-y,xy-z) is different:
its actual proof package shows it does not preserve the usual Markoff
level set. It is not a conjugacy claim for this integer descent.
The old finite-field Vieta rotor is also a different bijective update.
Those distinctions do not rescue this literal, since VMD is an exact hit.

Both (1) and (3) are readouts of the same old rooted-tree parent/child
structure. The sharp cap calculation does not supply a materially new
two-mechanism research contract. Stop negatively; no experiment is needed.
