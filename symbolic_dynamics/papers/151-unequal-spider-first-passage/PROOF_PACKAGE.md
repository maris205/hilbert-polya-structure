# P151 proof package

## Claim

Let `r>=2` paths of positive integer edge lengths
`ell_1,...,ell_r` share one centre.  Simple random walk starts at the centre
and is absorbed at the first leaf.  Write `I` for its labelled absorbing leaf
and `T` for the absorption time.  The frozen P151 contract asks for:

1. the arbitrary unequal-arm leaf-marked probability generating functions;
2. the compact variance formula;
3. the sharp fixed-`(r,L)` mean extrema and equality classes; and
4. the exact endpoint-only dilation ambiguity and endpoint-plus-mean recovery.

The endpoint probabilities and the mean themselves are prior background and
are used only as inputs to items 2--4.

## Status

`PROVABLE AS STATED`.

The contract survives unchanged.  The inverse claim is explicitly restricted
to a known labelled spider topology and the fixed simple-random-walk kernel.

## Assumptions

- `r>=2` and every `ell_i` is a positive integer.
- The centre chooses each arm with probability `1/r`.
- At every non-leaf arm vertex, the walk chooses its two neighbours fairly.
- All leaves are absorbing, arm labels are observed, and time is discrete.
- For the inverse result, the object is known a priori to be a labelled
  finite spider with the transition rule above; only its integer arm lengths
  are unknown.

## Notation

- `P_0=0`, `P_1=1`, `P_2=2`, and
  `P_l=2P_(l-1)-z^2 P_(l-2)`.
- `P=prod_j P_(ell_j)` and
  `D=rP-z^2 sum_i P_(ell_i-1)prod_(j!=i)P_(ell_j)`.
- `F_i(z)=E[z^T 1_{I=i}]`.
- `H=sum_i 1/ell_i`, `L=sum_i ell_i`, and `C=sum_i ell_i^3`.

## Proof strategy

The transform follows from one-dimensional killed excursions joined by a
renewal at the centre.  Excursion moments then give the variance without
requiring an opaque second derivative of the common denominator.  Integer
unit transfers prove both sharp extremizers.  Finally, endpoint ratios give
the primitive arm-length ray, and the mean fixes its common scale.

## Dependency map

1. The marked transform depends on the two killed-path transforms in Lemma A
   and the centre renewal equation in Lemma B.
2. Parity and the first atom follow respectively from bipartiteness and the
   unique shortest path.
3. The variance depends on the one-excursion first and second moments in
   Lemma C and the stopped-renewal second-moment identity in Lemma D.
4. The fixed-mass theorem depends only on the prior mean formula `L/H` and
   strict reciprocal unit-transfer inequalities.
5. The inverse boundary depends only on the prior endpoint law and mean,
   plus primitive integer normalization.

## Proof

### Lemma A: killed-path transforms

On the path `{0,1,...,ell}`, start at `1` and stop on first reaching
`{0,ell}`.  Let `A_ell(z)` mark absorption at `ell` and `B_ell(z)` mark
absorption at `0`, with the path time not including the preceding
centre-to-`1` step.  Solving

`u_k=(z/2)(u_(k-1)+u_(k+1))`

with the corresponding boundary values gives

`A_ell(z)=1/U_(ell-1)(1/z)=z^(ell-1)/P_ell(z)`

and

`B_ell(z)=U_(ell-2)(1/z)/U_(ell-1)(1/z)
          =z P_(ell-1)(z)/P_ell(z)`.

Here `P_ell(z)=z^(ell-1)U_(ell-1)(1/z)` as a polynomial identity; it
satisfies the displayed continuant recurrence.  The formulas also cover
`ell=1` under `P_0=0`: success is immediate after the centre step and return
is impossible.

### Lemma B: centre renewal and the marked transform

One attempt first selects arm `j`, takes one centre step, and then either
returns to the centre or reaches leaf `j`.  Its successful marked transform
on arm `i` is

`(1/r) z A_(ell_i)(z)=z^ell_i/(r P_(ell_i)(z))`,

while the transform of a failed attempt is

`Q(z)=(1/r)sum_j z B_(ell_j)(z)
     =(z^2/r)sum_j P_(ell_j-1)(z)/P_(ell_j)(z)`.

After a failure the process restarts from the centre.  Therefore

`F_i(z)=[z^ell_i/(rP_(ell_i))]/[1-Q(z)]`.

Multiplication by `r prod_j P_(ell_j)` yields exactly

`F_i(z)=z^ell_i prod_(j!=i)P_(ell_j)(z)/D(z)`.

Every `P_ell` is a polynomial in `z^2`.  The rational power series for
`F_i` hence uses only exponents congruent to `ell_i` modulo two.  At time
`ell_i`, the walk must take the unique monotone path down arm `i`; its
probability is `1/(r 2^(ell_i-1))`.

### Lemma C: one-attempt moments

Fix an arm of length `ell`.  Let `D_ell` be the duration of a complete
attempt on that arm, including the initial centre step, and let `R_ell`
denote return to the centre.  Standard finite-difference equations on
`{0,...,ell}` give

`P(R_ell^c)=1/ell`,

`E D_ell=ell`,

`E D_ell^2=ell(ell^2+2)/3`,

`E[D_ell 1_{R_ell}]=2(ell^2-1)/(3ell)`.

For completeness, the first identity solves the harmonic recurrence with
boundary values zero and one.  For the remaining identities, solve the
recurrences for `E_k tau`, `E_k tau^2`, and
`E_k[tau 1_{X_tau=0}]`, then put `k=1` and add the initial centre step.
Substitution into those recurrences verifies each displayed polynomial.

### Lemma D: stopped renewal moments

Average a single attempt over the uniform arm choice.  With `B` indicating
success at a leaf, put

`p=E B=H/r`, `mu=E D=L/r`,

`nu=E D^2=(C+2L)/(3r)`, and

`rho=E[D(1-B)]=2(L-H)/(3r)`.

Let `(T',I')` be an independent restart after failure.  Pathwise,

`T=D+(1-B)T'`.

Taking first moments gives `E T=mu/p=L/H`.  Squaring before taking
expectations gives

`p E T^2=nu+2rho E T`.

Consequently

`E T^2=(C+2L)/(3H)+4L(L-H)/(3H^2)`.

Subtracting `(L/H)^2` gives

`Var(T)=(C-2L)/(3H)+L^2/(3H^2)`.

The endpoint law follows either from `F_i(1)` or by competing successful
attempts: `P(I=i)=ell_i^(-1)/H`.  It is stated as background, not as a new
contribution.

### Fixed-mass extremizers

Fix `r` and `L>=r`.  Since `E T=L/H`, minimizing the mean is equivalent to
maximizing `H`.  If `2<=a<=b`, the outward unit transfer
`(a,b)->(a-1,b+1)` changes the reciprocal sum by

`1/[a(a-1)]-1/[b(b+1)]>0`.

Repeated transfers leave exactly one part above one.  Strictness shows that
the only maximizers of `H` are permutations of
`(L-r+1,1,...,1)`.

Maximizing the mean is equivalent to minimizing `H`.  If `b>=a+2`, the
inward transfer `(a,b)->(a+1,b-1)` strictly decreases `H` because

`1/[a(a+1)]-1/[b(b-1)]>0`.

Thus the unique labelled equality class up to permutation is balanced.  If
`L=qr+s`, `0<=s<r`, it contains `r-s` arms of length `q` and `s` arms of
length `q+1`.  Substitution yields the two contract bounds and both equality
classes.  When `L=r`, both classes reduce to the all-one vector, so the
boundary case is included.

### Coarse-data inverse boundary

Let `pi_i=P(I=i)`.  Then

`pi_i/pi_j=ell_j/ell_i`.

The labelled vector `pi` therefore determines the unique primitive positive
integer vector `d=(d_i)` on the same rational ray as `ell`, but not the common
integer dilation: `ell=c d` leaves `pi` unchanged for every positive integer
`c`.  Conversely, equality of two labelled endpoint vectors forces equality
of all arm-length ratios, hence exactly such a common dilation after primitive
normalization.

For `ell=c d`, the prior mean formula becomes

`E T=c^2 (sum_i d_i)/(sum_i 1/d_i)`.

Thus

`c^2=E T (sum_i 1/d_i)/(sum_i d_i)`.

Data generated by a valid integer spider make the right-hand side the square
of a unique positive integer, so the mean resolves the scale.  This argument
does not recover an unknown topology or transition kernel.

## Corrections or missing assumptions

None.  The known labelled-spider topology, positive integer arms, and fixed
simple-walk kernel must remain explicit in every inverse statement.

## Open risks

- The source search is bounded and cannot certify novelty or priority.
- Equal-arm transforms and all general-tree endpoint/mean statements must be
  presented as owned background.
- The common denominator may have algebraic cancellations for special arm
  profiles; the displayed rational identity remains valid and no reduced-form
  denominator claim is made.
- No weighted arms, biased transitions, cover times, unknown topology, or
  statistical-noise recovery theorem is proved.

