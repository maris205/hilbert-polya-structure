# Research-question briefs

## Batch question

Which five genuinely different symbolic dynamical systems admit a concrete,
falsifiable short-paper theorem after subtracting P1--P66 and the nearest
primary literature?

The batch question scores `4.3/5` under FINER: feasible `5`, interesting `4`,
novel `3`, ethical `5`, relevant `4.5`.  The novelty score is deliberately
provisional.  The work is theoretical, uses no human/animal data and requires
no preregistration; exact formulas and constructive proofs are the evidentiary
standard.

## P67 -- two geometries of a multiplicative plaquette subshift

**Question.**  For coprime `a,b>=2` and a prime `p`, what exact finite language
laws are forced by

\[
x_n-x_{an}-x_{bn}+x_{abn}=0\quad(n\ge1)
\]

on `F_p^N`, and how does ordinary prefix growth differ from growth inside an
`(a,b)`-exponent component?

**Concrete answer targeted.**  Restriction to coordinates not divisible by
`ab` is a complete set of free coordinates, giving

\[
|\pi_{[1,N]}X|=p^{N-\lfloor N/(ab)\rfloor}.
\]

Each component `r a^i b^j`, with `a` and `b` not dividing `r`, is a rank-one-sum
plaquette field `u_i+v_j`; hence an `M x N` exponent rectangle has exactly
`p^(M+N-1)` names.  The same compact system therefore has positive arithmetic
prefix rate and, as `min(M,N)->infinity`, a zero-area exact boundary law in
exponent geometry.

**Boundary.**  The prefix rate is not called topological entropy of the
multiplicative action.  Prime-valuation symbolic models already exist; the
paper lives or dies on the exact residual for this equation.

## P68 -- finite dependence across the bipartite phase

**Question.**  For `X=Hom(Z^d,K_(m,n))` with `m,n,d>=2`, exactly when does a
subgroup action admit a finitely dependent invariant probability, and what are
the language, entropy and maximal-entropy measures?

**Concrete answer targeted.**  Every configuration has one of two global
orientations.  If

\[
E=\{v\in\mathbb Z^d:\sum_i v_i=0\pmod2\},
\]

then there exists an `L`-invariant finitely dependent probability exactly when
`L` is contained in `E`; in that case a fixed-orientation product process is
0-dependent.  If `L` contains an odd vector, invariance forces a fair global
orientation bit, whose value is detected at arbitrarily separated sites.
For every finite connected `F`,

\[
|\mathcal L_F(X)|
=m^{|F\cap E|}n^{|F\setminus E|}
 +n^{|F\cap E|}m^{|F\setminus E|}.
\]

Thus `h_top(X)=1/2 log(mn)`, and the full `Z^d` action has a unique MME: the
equal mixture of the two orientation-product measures.

**Boundary.**  The two-line phase obstruction alone is too thin.  The subgroup
dichotomy and full measure/entropy classification are mandatory, and the
recent hom-shift finite-dependence paper must be subtracted precisely.

## P69 -- square-root slow entropy from a Rudin--Shapiro cocycle

**Question.**  For the generalized `[T,T^-1]` skew product whose base is the
four-letter Rudin--Shapiro subshift and whose cocycle takes values `+1,-1`, can
the subexponential orbit-name growth be computed with exact square-root
constants rather than only an order estimate?

**Concrete answer targeted.**  Use

\[
a\mapsto ab,\quad b\mapsto ac,\quad c\mapsto db,\quad d\mapsto dc,
\qquad
\kappa(a)=\kappa(b)=1,\quad \kappa(c)=\kappa(d)=-1,
\]

and define `F(y,x)=(Sy,sigma^(kappa(y_0))x)` over the full `q`-shift.  For a
base factor `w=w_0...w_(n-1)`, let

\[
r(w)=1+\max_{0\le j\le n}\sum_{i<j}\kappa(w_i)
       -\min_{0\le j\le n}\sum_{i<j}\kappa(w_i),
\qquad R(n)=\max_{w\in\mathcal L_n(Y)}r(w).
\]

For the finite edge partition recording the current base symbol and both fibre
endpoints of the cocycle step, the names above `w` number exactly `q^(r(w))`.
Since the base has linear factor complexity, the exact edge-name count
`C_q(n)` satisfies

\[
\log C_q(n)=R(n)\log q+O(\log n).
\]

Writing `rho(m)=M(m)+1` for the owned Rudin--Shapiro abelian complexity/maximal
factor-sum sequence, sign symmetry and two-sided factor extension give the
key reduction

\[
R(n)=\max_{1\le m\le n}\rho(m).
\]

The first exact target is

\[
R(2^j)=
\begin{cases}
3\,2^{j/2}-1,&j\text{ even},\\
2^{(j+3)/2}-1,&j\text{ odd}.
\end{cases}
\]

It is verified computationally through `2^8`.  The published first-occurrence
recurrence for `rho` supplies the following all-length proof spine:

\[
\limsup R(n)/\sqrt n=3,
\qquad
\liminf R(n)/\sqrt n=3\sqrt{3/5},
\]

and the accumulation set is the whole interval `[3 sqrt(3/5),3]`.
Multiplying by `log q` gives the corresponding edge-name-growth interval.  A
formal proof memo with exact citations remains to be written before manuscript
work, but the Stage-1 issue is now paper mass rather than the constants.

**Boundary.**  The general slow-entropy transfer and substantial
Rudin--Shapiro maximal-sum/abelian-complexity recurrences already have owners.
Carrasco--Vargas already writes essentially the same exponential range sum in
the general framework, so the full-shift specialization by itself is too thin.
The paper survives only if Stage 2 adds a genuinely new dynamical layer (for
example a measure/topological gap or a broader cocycle-family theorem).  Its
base is substitutional, but no language/frequency claim from P54 or P62 may be
recycled.

## P70 -- cyclotomic field dependence and a characteristic jump

**Question.**  What is the exact fixed-space dimension of the finite-field
principal shift `ker(1+a+b)` on congruence quotients of the discrete Heisenberg
group, and does the answer detect the field characteristic?

**Concrete answer targeted.**  For odd primes `ell!=p`, with `N_ell` the
kernel of reduction to `Heis(F_ell)`, prove

\[
\dim_{\mathbb F_p}\operatorname{Fix}_{N_\ell}X_p
=D_{p,\ell}+\ell(\ell-1)\mathbf1_{p=3},
\]

where

\[
D_{p,\ell}=\deg\gcd_{\mathbb F_p}
 (t^\ell-1,(-1-t)^\ell-1).
\]

The `D` term comes from one-dimensional characters and may itself depend on
`p`; every nonlinear Schrödinger block has determinant `3`, producing an
additional universal characteristic-3 jump.

**Boundary.**  Principal Heisenberg actions are owned.  The residual is this
finite-field congruence formula, not a generating-partition/open-problem claim
and not a first-Heisenberg-action headline.

## P71 -- what information does a nonuniform full zip shift forget?

**Question.**  For a surjection `tau:S->Z` whose positive fibre sizes are not
all equal, which invariants of the full one-block zip map are invisible to its
natural extension, and which classify the noninvertible maps themselves?

**Concrete answer targeted.**  The original map remembers the fibre profile
`k_z=|tau^-1(z)|`: two full zip maps are topologically conjugate if and only if
their multisets `{k_z}` agree.  Necessity is recovered from local degrees on
fixed points; sufficiency is coordinate relabeling.  Its natural extension is
the full two-sided `|S|`-shift, which supplies the complete invariant-measure
simplex and the usual unique MME as supporting consequences.  The latter is
not a novelty headline: intrinsic ergodicity of uniform `n`-to-one full zip
shifts already has an owner.  A degree-decorated periodic identity gives

\[
\sum_{x\in\operatorname{Fix}(\sigma_\tau^n)}
 \prod_{j=0}^{n-1}g(d(\sigma_\tau^j x))
=\left(\sum_{z\in Z}k_zg(k_z)\right)^n.
\]

**Boundary.**  Existing zip papers own the definition, local-homeomorphism,
mixing/shadowing, a periodic-count statement and uniform-fibre intrinsic
ergodicity.  The profile classification is short, and the periodic identity
is determined by its `n=1` specialization; Stage 2 must find independent mass
in the variable-degree classification neighborhood or replace P71.
