# Quadratic-state shear: all-size proof dossier

**Status:** `SURVIVOR / PROCEED_TO_INDEPENDENT_OWNER_GATE`  
**External status:** `HOLD_EXTERNAL`  
**Snapshot:** 2026-08-30 UTC  
**Paper number:** none

This dossier records a theorem spike, not a novelty certificate.  The finite
verifier is falsification evidence; the proofs below carry the claims.

## 1. Literal system and firewall

Let `(V,Q)` be a nonsingular quadratic space of dimension `2m` over
`F_2`.  Its polar form is

\[
 B(x,y)=Q(x+y)+Q(x)+Q(y).
\]

On the finite phase space `V x V`, define the basis-free, orthogonal-group
equivariant self-map

\[
 \Phi(x,y)=\bigl(y,\;x+Q(x)y\bigr).                 \tag{1}
\]

Thus the departing vector is merely swapped when it is singular and triggers
one elementary shear when it is nonsingular.  Put

\[
 N=|V|=2^{2m},\qquad
 S=\sum_{x\in V}(-1)^{Q(x)}=\varepsilon 2^m,
 \qquad \varepsilon\in\{+1,-1\}.                  \tag{2}
\]

For `m=0` only the plus convention occurs and the unique state is fixed.  For
`m>=1`, the two values of `epsilon` are the two Witt types.

This is not a graph, word, permutation, partition, tree, Ferrers, Catalan,
peeling, closure, power, nilpotent, Fibonacci, record, odd-component, or colon
system.  It also is not an orthogonal transvection: a characteristic-two
orthogonal transvection adds a multiple determined by the polar pairing with a
fixed root, while (1) uses the quadratic state of the *departing vector* and
updates an ordered pair.  In particular, (1) is not bijective.

## 2. Pointwise theorem

For a state `(x,y)`, write

\[
 a=Q(x),\qquad b=Q(y),\qquad c=B(x,y).
\]

Then `c` is invariant and the three-bit quotient evolves by

\[
 (a,b,c)\longmapsto \bigl(b,\;a(1+b+c),\;c\bigr). \tag{3}
\]

The complete pointwise classification is:

| `c` | `(a,b)` | quotient itinerary | pointwise fate |
|---:|:---:|:---|:---|
| 0 | 00 | `00 -> 00` | recurrent; period 1 iff `x=y`, otherwise 2 |
| 0 | 01 | `01 <-> 10` | recurrent; period 2 iff `x=0`, otherwise 4 |
| 0 | 10 | `10 <-> 01` | recurrent; period 2 iff `y=0`, otherwise 4 |
| 0 | 11 | `11 -> 10` | depth 1; eventual period 2 iff `x=y`, otherwise 4 |
| 1 | 00 | `00 -> 00` | recurrent of exact period 2 |
| 1 | 01 | `01 -> 10 -> 00` | depth 2, eventual period 2 |
| 1 | 10 | `10 -> 00` | depth 1, eventual period 2 |
| 1 | 11 | `11 -> 11` | recurrent of exact period 3 |

Consequently every orbit has transient depth at most `2` and eventual period
in `{1,2,3,4}`.  Depth 2 occurs for both Witt signs when `m>=2`, and for the
plus plane when `m=1`; the minus plane has maximum depth 1.  The bound is zero
for the zero-dimensional boundary.

### Proof

If `(u,v)=Phi(x,y)`, polarization gives

\[
 Q(v)=Q(x+ay)=a+ab+ac=a(1+b+c),
 \qquad B(u,v)=B(y,x+ay)=c,
\]

which proves (3).  On each recurrent row the successive updates are products
of the two matrices

\[
 \begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
 \begin{pmatrix}0&1\\1&1\end{pmatrix}
 \quad\text{over }\mathbb F_2.
\]

Multiplying the words prescribed by (3) gives orders `1,2,3,4` exactly as in
the table.  The stated exceptional shorter periods follow by solving the
corresponding equality: they reduce to `x=y`, `x=0`, or `y=0`.  In the
`c=1,00` row, `x=y` is impossible because `B(x,x)=0`; in the `c=1,11` row,
the order-three matrix has no admissible fixed pair.  This also proves that no
unlisted period or transient can occur.

## 3. Exact reverse dynamics and image tower

For every target `(u,v)`, the complete fibre is

\[
 \Phi^{-1}(u,v)
 =\bigl\{(v,u):Q(v)=0\bigr\}
  \mathbin{\cup}
  \bigl\{(u+v,u):Q(u+v)=1\bigr\}.                 \tag{4}
\]

The two displayed candidates are distinct whenever both exist.  Hence

\[
 |\Phi^{-1}(u,v)|
 =\mathbf 1_{\{Q(v)=0\}}+\mathbf 1_{\{Q(u+v)=1\}}
 \in\{0,1,2\}.                                   \tag{5}
\]

Across all `N^2` targets, the numbers of fibres of size `0,1,2` are

\[
 d_0=d_2=\frac{N(N-1)}4,
 \qquad d_1=\frac{N(N+1)}2.                       \tag{6}
\]

The image tower stabilizes after two steps:

\[
 |\operatorname{im}\Phi^0|=N^2,
 \qquad |\operatorname{im}\Phi|=\frac{N(3N+1)}4,
 \qquad
 |\operatorname{im}\Phi^t|=\frac{N(5N-S+4)}8
 \quad(t\ge2).                                    \tag{7}
\]

### Proof

Writing an unknown preimage as `(x,u)`, equation (1) says
`v=x+Q(x)u`.  The two possible values of `Q(x)` give exactly the candidates
in (4), and substituting them proves sufficiency.  Formula (5) follows.  Its
value on target type `(Q(u),Q(v),B(u,v))=(a,b,c)` is

| `c` | `00` | `01` | `10` | `11` |
|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 2 | 0 |
| 1 | 2 | 0 | 1 | 1 |

Combining this table with the pair census in Section 4 gives (6).  It also
shows directly that every depth-one state in type `c=0,11` and every depth-two
state in type `c=1,01` has no preimage, while every `c=1,10` depth-one state
has its unique predecessor in `c=1,01`.  Thus the first image consists of the
recurrent set plus the `c=1,10` layer, and the second image is precisely the
recurrent set.  This proves (7).

## 4. Pair types and exact temporal layers

Let

\[
 C_{abc}=\#\{(x,y):Q(x)=a,\ Q(y)=b,\ B(x,y)=c\}.
\]

The eight counts collapse to four quantities:

\[
\begin{aligned}
 H&=C_{000}=\frac{N(N+3S+4)}8,\\
 M&=C_{010}=C_{100}=C_{110}=\frac{N(N-S)}8,\\
 A&=C_{001}=C_{011}=C_{101}=\frac{N(N+S-2)}8,\\
 Z&=C_{111}=\frac{N(N-3S+2)}8.                   \tag{8}
\end{aligned}
\]

Therefore the exact depth layers `L_j=#{state: depth=j}` are

\[
 L_0=\frac{N(5N-S+4)}8,
 \qquad L_1=\frac{N(N-1)}4,
 \qquad L_2=\frac{N(N+S-2)}8.                    \tag{9}
\]

### Character-sum proof of (8)

Indicator expansion gives

\[
\begin{split}
 C_{abc}=\frac18\bigl[&N^2+(-1)^aNS+(-1)^bNS
      +(-1)^{a+b}S^2\\
 &+(-1)^cN\{1+(-1)^a+(-1)^b+(-1)^{a+b}S\}\bigr]. \tag{10}
\end{split}
\]

Indeed, when the Fourier variable of `B(x,y)` is zero the sums factor.  When
it is one, nondegeneracy gives the four sums `N,N,N,NS`; the last identity is
`Q(x)+Q(y)+B(x,y)=Q(x+y)`.  Since `S^2=N`, (10) reduces to (8).  Reading the
transient rows from the pointwise table gives (9).

### Independent hyperplane-count route

There is also a direct finite-geometry derivation without the three-variable
transform.  For fixed nonzero `x` of type `a`, character orthogonality and
completion of the square give

\[
 \#\{y:Q(y)=b,\ B(x,y)=c\}
 =\frac14\bigl[N+(-1)^bS+(-1)^{a+b+c}S\bigr].    \tag{11}
\]

The case `x=0` is separated explicitly.  Multiplying (11) by the numbers of
nonzero singular and nonsingular choices for `x` gives (8).  This route also
works naturally with the reverse-fibre table, so it is a genuinely separate
way to reconstruct (6)--(9).

## 5. Complete decorated-cycle decomposition

Put `N_0=(N+S)/2` and `N_1=(N-S)/2`.  Every connected component of the
functional graph has exactly one of the following six shapes:

| shape | number of components |
|:---|---:|
| bare fixed point | `N_0` |
| bare 2-cycle | `(H-N_0)/2` |
| 2-cycle with one leaf attached to one cycle vertex | `N_1` |
| 2-cycle with one length-two tail at each cycle vertex | `A/2` |
| bare 3-cycle | `Z/3` |
| 4-cycle with one leaf at each of two alternating vertices | `(M-N_1)/2` |

There are no other component shapes.  In particular, if `c_j` is the number
of cycles of exact length `j`, then

\[
\begin{aligned}
 c_1&=\frac{N+S}{2},\\
 c_2&=\frac{N^2+2NS+3N-6S}{8},\\
 c_3&=\frac{N(N-3S+2)}{24},\\
 c_4&=\frac{N^2-NS-4N+4S}{16}.                  \tag{12}
\end{aligned}
\]

The finite-map zeta function is therefore

\[
 \zeta_\Phi(t)
 =(1-t)^{-c_1}(1-t^2)^{-c_2}
  (1-t^3)^{-c_3}(1-t^4)^{-c_4}.                 \tag{13}
\]

### Proof from reverse dynamics

The fibre-size table after (5) supplies the component geometry, not merely
its total mass.  In `c=0`, type `10` has one recurrent predecessor in type
`01` and one leaf in type `11`; all other recurrent target types have only
their cycle predecessor.  The exceptional mixed pairs with a zero coordinate
form `N_1` two-cycles, while the others form four-cycles.  In `c=1`, every
type `00` cycle vertex has one additional type `10` predecessor, and that
predecessor has one type `01` predecessor; type `11` has only its cycle
predecessor.  This forces precisely the six displayed shapes.  Substitution
of (8) yields (12), and the standard cycle product yields (13).

This reverse proof is logically independent of the forward matrix-word proof
of the period ceiling: one begins from the complete inverse formula and
reconstructs every component, while the other follows individual states
through the eight-state quotient.

## 6. Exact verifier

The standard-library verifier is
[`replacement_quadratic_shear_verify.py`](replacement_quadratic_shear_verify.py),
with canonical stdout in
[`replacement_quadratic_shear_verify.out`](replacement_quadratic_shear_verify.out).
It exhausts the zero-dimensional boundary and both Witt signs for
`1<=m<=5`, i.e. all ordered pairs through dimension `10`.  It checks:

- polarization and the literal update for every state;
- polar invariance and every quotient transition;
- the exact pointwise depth and period for every state;
- every one-step fibre against (4), not only aggregate counts;
- all eight pair-type formulas, all depth layers, and the image tower;
- exact cycle and decorated-component censuses.

Canonical result: **20,133,012 exact assertions, PASS**.

Run and compare with:

```bash
python3 docs/papers122_126_sequence/scouting/replacement/replacement_quadratic_shear_verify.py \
  > /tmp/replacement_quadratic_shear_fresh.out
cmp -s /tmp/replacement_quadratic_shear_fresh.out \
  docs/papers122_126_sequence/scouting/replacement/replacement_quadratic_shear_verify.out
```

## 7. Bounded owner gate and zero-credit boundary

Searches were run with exact and equivalent forms, including
`(x,y)->(y,x+Q(x)y)`, `x+Q(x)y`, `quadratic-state shear`, singular/nonsingular
conditional addition, finite quadratic-space pair dynamics, quadratic-form
Yang--Baxter maps, and 2025--2026 transvection/orbit formulations.  No source
located in this bounded pass states the literal map (1), its nonuniform fibres,
or the six-shape functional graph.  This is only
`BOUNDED_NO_DIRECT_HIT`, never a priority claim.

The following receive **zero contribution credit**:

- static representation counts and quadratic-form classification in
  characteristic two, including Fulton's
  [*Representations by Quadratic Forms in a Finite Field of Characteristic
  Two*](https://doi.org/10.1002/mana.19770770117);
- the singular/nonsingular vector census, Witt sign, orthogonal two-space
  types, and associated 3-transposition geometry, as used explicitly by Hall
  and Shpectorov in
  [*The spectra of finite 3-transposition groups*](https://doi.org/10.1007/s40065-021-00329-x);
- symplectic/orthogonal transvections and their orbit machinery, including
  Sjostrand's 2025
  [*Orbits under dual symplectic transvections*](https://doi.org/10.1016/j.laa.2025.02.010);
- generic bijective pair maps and set-theoretic Yang--Baxter background,
  including Etingof--Schedler--Soloviev,
  [*Set-theoretical solutions to the quantum Yang--Baxter equation*](https://doi.org/10.1215/S0012-7094-99-10007-X).

The residual is only the exact conjunction for the nonbijective self-map (1):
the three-bit temporal quotient, pointwise fibre formula, complete image tower,
Witt-sensitive depth/cycle census, and six decorated component shapes.

**Owner risk: medium-high.**  The formula is short enough that it could occur
under the vocabulary of finite orthogonal geometry, nonlinear feedback, a
degenerate switch, or a nonbijective quadratic set.  A specialist owner gate
must therefore precede any paper allocation.  Discovery of the same literal
map, or a conjugacy that transports an owned functional-graph classification
to (1), is an immediate kill.

## 8. Gate decision

This candidate clears the requested breadth-to-theorem threshold:

1. it has an all-dimension pointwise temporal theorem;
2. it has a second engine stronger than a fixed-point count--the exact fibres,
   image tower, and complete decorated-component census;
3. the proof has forward and reverse routes;
4. the exact pilot actively checks every state and every fibre through
   dimension ten;
5. its carrier and mechanism are disjoint from P001--P121 and the current
   record/odd-component/cross-colon candidates.

**Internal score: 8.2/10.  Recommendation:
`PROCEED_TO_INDEPENDENT_OWNER_GATE`, external HOLD.**  Do not freeze a paper
number until the specialist owner search confirms the bounded non-hit.
