# Paper 24 — Initial Proposal and Correction Log

## Starting point

The original discovery thread began with the appealing $m=2$ example:

$$
V_2=Aq_1^2q_2^2+Bq_1q_2^4,
\qquad
W_{2,s}=Cp_1^{5s+1}+Dp_2^{2s+1}.
$$

It already exhibited the key qualitative surprise: the degree orbit did not
stay in one selector chamber but crossed a genuine wall. That was not yet
enough for a new paper. As both candidate reviews stressed, a lone $m=2$
matrix computation would sit too close to Paper 20's two-mode selector grammar
and would look like a bounded extension rather than a standalone theorem.

## Why the singleton was too thin

The $m=2$ singleton was too thin for three independent reasons:

1. it gave only one concrete matrix and one concrete recurrence;
2. it did not explain whether the switching mechanism was accidental or
   forced by support geometry;
3. it left the novelty story vulnerable to the objection “this is just
   another small Perron example.”

The accepted fix was to enlarge from one parameter value to the full
$m$-family and to isolate the wall-fixing mechanism inside the crossed-binomial
/ diagonal-pure-power ansatz.

## Upgrade that made the project standalone

The project became standalone only after two structural moves:

### 1. Generalize from $m=2$ to the full $m$-family

The theorem was upgraded to

$$
V_m=Aq_1^m q_2^2+Bq_1q_2^{2m},
\qquad
W_{m,s}=Cp_1^{s(2m+1)+1}+Dp_2^{sm+1},
$$

for all integers $m\ge2$ and $s\ge1$ with arbitrary nonzero coefficients.
This turns the project from one instance into a support-family theorem.

### 2. Make the wall-fixing ratio explicit

The supporting crossed-binomial lemma proves that strict global chamber
exchange forces the pure-power ratio

$$
\frac ef=\frac{R(L_{\mathrm{wall}}-1)}{L_{\mathrm{wall}}-R},
$$

and for the explicit family forces

$$
\frac ef=\frac{2m+1}{m}.
$$

That rigidity explains why the switching mechanism is structural rather than
decorative.

## Four candidate-review corrections that must stay frozen

The source-design package binds all four arithmetic/logic corrections from the
candidate gate.

### Correction 1 — R1 right-branch lower bound

The corrected identity is

$$
\ell_m(r)-1=
\frac{(m^2-m-1)r+3m+2}{m(mr+1)}.
$$

The theorem must not revert to the earlier incomplete numerator.

### Correction 2 — R1 negative-chamber visibility equality

In the negative chamber, the comparison with the second momentum coordinate is
through the exact equality

$$
u_{n+1,1}=sm\,h_m(r_n)\,v_{n+1,2},
$$

and then the strict inequality follows because $h_m(r_n)>2$. The package must
not write a strict inequality where the equality belongs.

### Correction 3 — R2 right-branch distance below the wall

The corrected identity is

$$
2-\ell_m(r)=
\frac{(m+1)(r-2)}{m(mr+1)}.
$$

The factor $(m+1)$ is part of the true formula and must not be dropped.

### Correction 4 — R2 second coordinate of $u_3$

The corrected third complete-step vector is

$$
u_3=
\begin{pmatrix}
8m^4(m+1)(2m+1)s^3\\
2m^2(m+1)(2m-1)(2m^2+2m+1)s^3
\end{pmatrix}.
$$

Only the first coordinate is visible as $d_3$, but the second coordinate must
still be correct wherever $u_3$ is displayed.

## Rejected expansions

The candidate gate rejected:

- staying at the singleton $m=2$ level;
- heading the paper with the conditional period-$k$ monodromy lemma;
- asserting a theorem on the wall $r=2$;
- going beyond the crossed-binomial / diagonal-pure-power ansatz;
- any period $>2$, automaton, positive-characteristic, inverse-degree,
  entropy, integrability, or priority claim.

## Initial-gate outcome

The corrected candidate survived only as a proof-first explicit-family theorem.
The source-design task is therefore to keep the public story narrow:

$$
\text{forced wall fixing}
\Longrightarrow
\text{strict period-two selector exchange}
\Longrightarrow
\text{two-step monodromy}
\Longrightarrow
\text{exact parity laws}.
$$

No independent source-design verdict is asserted here.
