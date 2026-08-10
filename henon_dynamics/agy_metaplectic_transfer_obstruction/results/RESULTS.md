# HCS-C25 exact source-lock results

## Outcome

The project-chosen deterministic AGY-admissible section witness passes every
exact algebraic gate, and
the fixed-start Rauzy matrix map has an all-length inverse decoder.  This
removes the proposed same-matrix cancellation escape in the present
four-letter full-rank `H(2)` system and supplies the literal nonzero branch
needed by the registered `C_b^1` and normalized `L^2` metaplectic transfer
obstructions.

This is not an `n=13` extension of the C24 cycle table.  No periodic ledger,
averaged transition matrix, prime/zero data, oscillator cutoff, or heat
regularization is used.

## Exact project-chosen AGY-admissible section witness

The independently reconstructed Rauzy class has seven labeled states and
fourteen directed arrows.  The frozen base state is

```text
state 4
top    1342
bottom 4321
```

with

```text
eta        = tbttbtbb
gamma_star = t^64 eta^8
length     = 128
```

`eta` is a closed complete path: its winner set is `{1,2,3,4}`.  The full
word is exactly split into eight complete pieces, the first being
`t^64 eta` and the remaining seven being copies of `eta`.  Hence it is
8-complete, meeting the AGY threshold

\[
3d-4=3\cdot4-4=8.
\]

The maximal initial `t` run is **65**, not 64: the first letter of `eta`
continues the compressed `t^64` prefix.  Both producer and checker determine
65 by scanning the full released word.  The run is at least half of the
128-letter word, the terminal letter is `b`, and an exact scan finds no
nonempty proper border.  Thus the registered strong-positivity and neatness
conditions pass without a word search.

With `B_e=I+E_(loser,winner)` and later arrows multiplying on the left, the
chronological matrix is

\[
B_{\gamma_*}=
\begin{pmatrix}
18540&1210580&11430&27373\\
24020&1568410&14783&35450\\
50233&3279928&31130&74253\\
38803&2533625&24020&57343
\end{pmatrix}.
\]

Every entry is positive, `det(B)=1`, and at the state-4 crossing form
`Omega_4` the exact identities

\[
B\Omega_4B^{\mathsf T}=\Omega_4,
\qquad
B^{\mathsf T}\Omega_4^{-1}B=\Omega_4^{-1}
\]

hold.

## Statewise symplectic trivialization

The seven Rauzy states do not initially share a single coordinate copy of
the inverse crossing form.  The release now fixes this explicitly.  Put

\[
J_\pi=\Omega_\pi^{-1},
\qquad J_0=J_{\text{state }4}
=\begin{pmatrix}
0&-1&0&0\\
1&0&-1&1\\
0&1&0&-1\\
0&-1&1&0
\end{pmatrix}.
\]

A deterministic breadth-first tree rooted at state 4, with outgoing order
`t,b`, defines integral unimodular frames by

\[
S_4=I,
\qquad S_{\rm dst}=B_eS_{\rm src}
\]

on each newly discovered tree edge.  All seven independently reconstructed
frames satisfy

\[
S_\pi^{\mathsf T}J_\pi S_\pi=J_0.
\]

For every one of the fourteen directed edges, the fixed-fiber matrix

\[
g_e=S_{\rm dst}^{-1}B_eS_{\rm src}
\]

is integral, has determinant one, and obeys

\[
g_e^{\mathsf T}J_0g_e=J_0.
\]

There are seven state frames, fourteen verified fixed-fiber edge matrices,
six identity edge matrices, and eight nonidentity edge matrices.  The six
tree edges necessarily trivialize to the identity; the remaining matrices
retain the loop cocycle in the fixed fiber.

This proves that each labeled edge matrix admits two metaplectic lifts after
trivialization.  Choosing one lift for each directed edge and multiplying in
chronological order defines pathwise coherent lifts.  The certificate does
**not** numerically choose either central sign, identify the two lifts, or
claim a global multiplicative section from `Sp(J_0,Z)` to the metaplectic
group.

## Exact projective branch data

Put `R=B^T` and

\[
h_{\gamma_*}(x)=\frac{Rx}{S(x)},
\qquad S(x)=\mathbf 1^{\mathsf T}Rx.
\]

On the open simplex,

\[
S(x)=1267923x_1+1642663x_2+3435544x_3+2653791x_4.
\]

The deterministic witness point is

\[
x_0=\frac{1}{8999921}
(131596,8592543,81363,194419)^{\mathsf T}.
\]

At this point,

\[
e^{r_{\gamma_*}(x_0)}=S(x_0)
=\frac{15076979616018}{8999921},
\]

and

\[
y_0=h_{\gamma_*}(x_0)
=\frac{1}{15076979616018}
(220463820736,14395387473049,135730480019,325397842214)^{\mathsf T}.
\]

Both vectors lie in the positive simplex.  Direct differentiation in three
independent simplex coordinates verifies

\[
J_{\gamma_*}(x)=\frac{\det R}{S(x)^4}
=e^{-4r_{\gamma_*}(x)}.
\]

The checker evaluates the derivative exactly at `x0`; it does not merely
compare a stored exponent.

## All-length matrix decoder

For a path from a fixed labeled state, write `R=B^T`.  At the current state,
the true first arrow is the unique candidate for which

\[
\operatorname{row}_w(R)-\operatorname{row}_\ell(R)\ge0
\]

componentwise.  Peeling replaces the winner row by this difference and
advances the permutation.  The sum of all matrix entries drops exactly by
the positive loser-row sum at every step.

The two candidate arrows reverse the same rightmost pair.  If both dominance
tests passed, the two rows would be equal, contradicting unimodularity.
Induction on the entry sum therefore makes the decoder a two-sided inverse
on every fixed-start path matrix, at every length.  The released certificate
contains all 128 exact peel steps for `gamma_star`.

Consequences include collision-free central first-return matrices and a free
central-return matrix monoid.  The projected-matrix consequence is scoped:
the decoder first proves injectivity for the full labeled `4 x 4` matrix.
Here `det(Omega)=1` at all seven states, so relative and absolute homology
coincide and the symplectic basis change loses no information.  A Rauzy class
with a nontrivial relative-homology kernel would require a new argument after
projection.

This decoder is positioned as an explicit algorithmic restatement of the
standard simplicial-cylinder coding geometry, not as a blanket novelty
claim.  Return-monoid freeness is its formal fixed-start coding corollary.

The exact central first-return series is

\[
F(z)=\frac{2z^3}{1-z-z^2},
\]

with coefficient `2 F_(n-2)` at elementary length `n`.  It comes from exact
state elimination, not a fitted count sequence.

## Non-proof stress sentinel

Here “central” means based at the reversal seed
`pi_c=(1234)/(4321)`, not at the AGY section base
`pi_*=(1342)/(4321)`.  The stress language is therefore a code regression
test, not the AGY induced-branch language.

As an implementation check, both programs independently replay all central
first returns through elementary length 22:

```text
first-return words        35420
exact decoder recoveries  35420
distinct matrices         35420
collisions                    0
SHA-256  dde0875c4f0b9b18cbcc72137fce99a0a2e6038e537b7f1c255b1a1964e22fe1
```

These numbers are diagnostics only.  The logical result is the entry-sum
induction above.

## Operator conclusion and boundary

The source-specified `gamma_star` branch is a project-chosen AGY-admissible
object used in this AGY application.  A `C^1` bump supported inside its
branch image and point
evaluation isolate a nonzero scalar times its infinite-dimensional
metaplectic unitary.  In the invariant-measure-normalized `L^2` model, the
branch cylinder similarly isolates a nonzero weighted composition tensored
with that unitary.  The theorem package therefore rejects compactness,
nuclearity, and an ordinary nuclear Fredholm determinant on the two
registered unsmoothed realizations: throughout `Re(s)>-sigma_0` for the raw
vector-valued AGY `C_b^1` operator, and throughout `Re(s)>=0` for the
normalized `L^2` operator.  On `s=it`, the latter is a coisometry with
essential norm exactly one.

The normalized \(L^2\) obstruction is a space obstruction rather than an
oscillator-specific novelty: setting every fibre unitary to one still gives
a noncompact scalar operator throughout `Re(s)>=0` by the nonatomic branch
argument; on the imaginary axis it is the adjoint of an isometric Koopman
operator.  The oscillator-specific multi-branch conclusion is the raw
\(C_b^1\) bump/evaluation theorem.

The short central return `ttt` appears only as a sanity check of the simpler
formula `S_ttt(x)=2-x_4`; it is explicitly not identified with the AGY
`gamma_star` section branch.

The result does not close holomorphic or anisotropic spaces without bounded
branch localizers, distributional/flat traces, semifinite determinants, or
geometrically forced continuous smoothing.
