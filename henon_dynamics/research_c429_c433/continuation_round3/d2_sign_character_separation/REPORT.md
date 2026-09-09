# R3 D2: the Fricke cycle-sign separation question

2026-09-09 UTC. First-pass and round-2 artifacts are read-only accepted
inputs. The coordinator has accepted NI, its ordinary all-period count,
and D2's reviewed algebra as auxiliary results. No higher full wreath
group is assumed.

## Frozen question: SF2 and no larger claim

Let $k=\mathbb Q(A,B,C,D)$ with algebraically independent parameters,
let

$$
S:\quad x^2+y^2+z^2-xyz-Ax-By-Cz=D,\qquad T=s_zs_ys_x,
$$

and let one entire right-to-left word $T$ be the native tick.
$L_n/k$ is the splitting field of all ordinary points of exact native
least period $n$. FG2 defines a degree-$11$ cycle field $E/k$ and its
nontrivial trace-discriminant squareclass $d_2$. Write
$F_2=k(\sqrt{d_2})$.

**SF2.** Is

$$
F_2\not\subseteq L_3\cdots L_N\qquad\text{for every finite }N\ge3?
$$

Keep the geometric version over $\overline{\mathbb Q}(A,B,C,D)$ separate.
The target is this independence subquestion only, not the complete FI2
classification after a nontrivial intersection occurs.

Success means proving this actual all-$N$ exclusion or finding an
actual generic inclusion with a specified finite $N$. A restricted
slice identity, an abstract possible character, or a failed finite
specialization is not either conclusion. The accepted NI/trichotomy,
Goursat reduction and count bounds will not be reproved here.

## Distinct assignment and first source subtraction

C4 owns whole-higher-cover unramifiedness at a smooth two-cycle fold.
This lane instead examines exact Fricke symmetry restrictions of the
cycle-sign cover and the validity of a specialization obstruction.
There is no mathematical execution allocation.

Cantat–Loray's *Holomorphic dynamics, Painlevé VI equation and Character
Varieties* describes the even-sign/coordinate symmetries in §3.1 and
the special quadratic transformation between two-dimensional Fricke
subfamilies in §9.4. The latter is equivariant only with the explicit
group-word transformations of Remark 9.13; it is not an identification
of our fixed native return with another clock. These passages were
read in the [primary paper](https://arxiv.org/pdf/0711.1579).

Doyle, Krieger, Obus, Pries, Rubinstein-Salzedo and West's *Reduction of
dynatomic curves* distinguishes point and cycle covers in §3.2 and
primitive versus satellite parabolic parameters in §3.4. Those are
one-variable polynomial-family statements, not a branch-disjointness
theorem for this Fricke surface return. The relevant passages were
read in the [primary paper](https://arxiv.org/pdf/1703.04172).

The previous round already source-subtracted Bridy–Garton's
one-variable disjoint-branch proof; it is not imported as a Fricke
independence result. The local source inventory contained no matching
paper-library file; no PDF or external-model upload was written.

## Bounded proof plan

1. Restrict the actual eleven-cycle finite étale algebra to
   $A=B=C=0$ and then to $A=B=0$, using the accepted FG2 coordinate
   chart and its explicitly treated omitted chart.
2. Compute its trace-discriminant squareclass by character identities,
   retaining all cycle components and phase distinctions.
3. State exactly when a generic inclusion must survive a slice
   specialization, and determine what all-higher-layer input that
   test would still require.
4. Do not assert that every quadratic character of an unknown
   higher-layer group extends from the ambient wreath group.

## Proved exact restricted characters

The complete proof is [PROOF_PACKAGE.md](PROOF_PACKAGE.md). With
$\Sigma=\{A=B=0\}$ and $K=\mathbb Q(C,D)$ it establishes

$$
\left.d_2\right|_\Sigma=[D^2-C^2],\qquad
\left.p_2\right|_\Sigma=[C^2+4D].
\tag{R}
$$

Restriction is defined through the finite étale character covers,
not by substituting into an arbitrary rational squareclass
representative. The two classes remain independent after extending
constants to $\overline{\mathbb Q}$.

The full eleven-cycle algebra decomposes into dimensions
$1+2+4+4$. The one-dimensional part is the $z$-axis cycle. The
two-dimensional part is the omitted $r=-1$ chart:
$z=0$, $xy=-C$, and $\xi=x^2$ satisfies
$\xi^2-D\xi+C^2=0$. For each $\varepsilon=\pm1$, the remaining
four-dimensional part is

$$
(D-2\varepsilon C)q^2+(3+\varepsilon C)q-1=0,\qquad
X^2=(1-\varepsilon Cq)/q^2,\quad
Y=\varepsilon X,\quad Z=\varepsilon/q.
$$

Its cycle-discriminant contribution is
$(D+\varepsilon C)/(D-2\varepsilon C)$ modulo squares.
Multiplication with the omitted chart's $D^2-4C^2$ gives the first
identity (R). The full twenty-two-point discriminant computes phase
parity and gives the second identity. Omitting the $r=-1$ chart
would produce the wrong sign character.

On the fully symmetric line $A=B=C=0$, these become $1$ and $[D]$.
The cycle-sign character is therefore invisible on that line, even
though it is nontrivial in the generic four-parameter family. It
also splits over the formal ring $\mathbb Q(D)[[C]]$ inside
$\Sigma$, by Hensel lifting the square root of $D^2-C^2$ from $C=0$.
Neither a symmetric specialization nor all of its formal jets
supplies the desired exclusion.

## One-way transfer and the exact missing input

Let $M_n/K$ denote the specialized native-coordinate splitting field
of the generic exact-$n$ cover on $\Sigma$. Accepted NI ensures that
these whole covers, with all point coordinates distinct, legitimately
specialize at the generic point of $\Sigma$: it passes through the
Cayley point where every higher cover is étale.

Proposition 3 proves the implication

$$
\left[
K(\sqrt{D^2-C^2})\not\subseteq M_3\cdots M_N
\ \text{for every }N\ge3
\right]
\quad\Longrightarrow\quad \mathrm{SF2}.
\tag{ST}
$$

Its geometric counterpart is separate. The argument uses no high
full-wreath hypothesis and makes no claim about compositum constants.
A generic inclusion must survive this nontrivial finite étale
specialization. The converse does not hold: distinct quadratic
extensions can coincide on a slice.

The bracketed exclusion in (ST) remains **NOT CURRENTLY JUSTIFIED**.
It requires an actual control of the higher specialized fields at
the character branches $D=C$ and $D=-C$, or another exclusion
mechanism for their full finite composita. Identifying branch
polynomials of the two layer-two characters does not supply it.
Nor can unknown higher-layer characters be assumed to extend from
the ambient wreath group.

There is a concrete higher-layer reason for this caution. On
$\Sigma$, $g(x,y,z)=(-x,-y,z)$ commutes with $T$ and has fixed
points only of native period at most two. For every odd $n\ge3$,
$h=gT$ therefore acts freely with orbit length $2n$ on $P_n$.
The Galois action has a canonical sign character $\psi_n$ on the
$\nu_n/(2n)$ paired native-cycle orbits. In the resulting
$C_{2n}\wr S_{\nu_n/(2n)}$ upper bound, native cycle sign is
total rotation parity, while $\psi_n$ is the separate block
permutation sign. The latter does not extend to the original
$C_n\wr S_{\nu_n/n}$ upper bound. Its restriction to the actual
specialized Galois group may be trivial or may satisfy relations;
neither possibility has been decided. Proposition 4 proves this
exact higher-character interface without asserting group fullness.

The points $D=-\varepsilon C$ on this slice are symmetry-enhanced
collisions where two nonaxis cycle labels meet the axis label.
C4 separately studies the global critical component and whole
higher-cover behavior; this proof does not assume an identification
with its isolated smooth fold.

## Outcome and ownership

SF2 remains open: no generic relation and no all-level exclusion
has been proved. The exact restricted characters, symmetric-line
blindness and legitimate two-parameter sufficient test are auxiliary
interfaces, not a replacement question or new-paper admission.

| Source actually read | Owned content used or excluded |
|---|---|
| Cantat–Loray, arXiv:0711.1579, inspected 2007 version, §§3.1 and 9.4 | Fricke sign symmetries and special quadratic transformations; no native-clock equivalence inferred from finite-index equivariance. |
| Doyle et al., arXiv:1703.04172, inspected 2017 preprint, §§3.2 and 3.4 | Point/cycle quotient distinction and primitive/satellite branches for one-variable polynomial families; no Fricke disjointness inferred. |
| Accepted FG2, §§3.4–3.7 | Original cycle coordinates, omitted-chart equations and a full étale two-cycle fibre. |
| Accepted R2 NI and D2 algebra | Legitimate whole-cover higher specialization and the identification of the actual layer-two quadratic characters. |

The proof-writer checks required every omitted chart and specialization
hypothesis to remain explicit. The batch workflow keeps these results
auxiliary while the frozen all-level condition is unproved. Zero
mathematical programs, old reruns, PDF builds, Git/shared edits or
external-model uploads were performed. Only this new R3 directory
was written.
