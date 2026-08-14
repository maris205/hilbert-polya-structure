# Proof Package — SD-C28

## 1. Setup and conventions

Let `A_m={a_1,...,a_m}` and let `A_m^+` be its nonempty words.  For
`w in A_m^+`, put

\[
 \chi_m(w)=\mathbf 1_{\{|\operatorname{supp}(w)|=1\}}.
\]

This is a cyclic function and `chi_m(w^r)=chi_m(w)` for every `r>=1`.
Two extensions at the identity are used: the character convention
`chi_m(1)=m` and the language convention `chi_m(1)=0`.  All determinant
statements depend only on positive words.

For each `i`, let `L_i` be the one-dimensional module over the free algebra
`R=C<A_m>` satisfying `a_j|L_i=delta_ij`.  Let `L_0` be the dormant module on
which every letter acts by zero, and put `Lambda_m=direct-sum_i L_i`.

## 2. Exact positive constructions

### Lemma 2.1 — support-Euler selector

For a nonempty word `w` with support `S`, let

\[
 Q_S=\ker\!\left(\mathbb C^S\xrightarrow{\sum}\mathbb C\right).
\]

With exterior degree as parity,

\[
 \operatorname{Str}(I\mid\Lambda^\bullet Q_S)
 =\sum_{j=0}^{|S|-1}(-1)^j\binom{|S|-1}{j}
 =(1-1)^{|S|-1}=\chi_m(w).
\]

The convention in the singleton case is `0^0=1`.  Since support is invariant
under cyclic rotation and repetition, so is this coefficient.  The fiber
depends on the completed support and is therefore an orbitwise rule rather
than a fixed stationary branch representation.

### Proposition 2.2 — stationary projector selector

On `V_m=C^m`, define `P_i=e_i e_i^*`.  Then

\[
 P_iP_j=\delta_{ij}P_i,
 \qquad
 \operatorname{Tr}(P_{i_1}\cdots P_{i_r})=\chi_m(a_{i_1}\cdots a_{i_r}).
\]

Indeed, a monochromatic product is `P_i`, of trace one; a mixed product
contains adjacent unequal projectors after cyclic rotation and is zero.

## 3. Minimal recognizable memory

### Theorem 3.1 — Hankel ranks

The Hankel rank is `m` under `chi_m(1)=m` and `m+1` under `chi_m(1)=0`.

**Proof.**  The submatrix with row and column indices `a_1,...,a_m` is the
identity, hence the rank is at least `m`.  After a nonempty pure prefix, the
left residual is one of the `m` color residuals; a mixed prefix gives zero.
Under the character convention the empty residual is the sum of the color
residuals, so the rank is at most `m`.  Under the language convention the
empty residual is independent: it vanishes at the empty suffix whereas every
color residual takes value one there.  Thus the rank is `m+1`.  The projector
realization, with one dormant correction for the language convention, attains
the bounds.  ∎

### Theorem 3.2 — syntactic algebras

Over `C`,

\[
 \mathcal A_{\chi_m}\cong
 \begin{cases}
 \mathbb C^m,&\chi_m(1)=m,\\
 \mathbb C^{m+1},&\chi_m(1)=0.
 \end{cases}
\]

**Proof.**  In the first convention map `a_i` to the primitive coordinate
idempotent `e_i in C^m` and use `tau(v)=sum_i v_i`.  The pairing
`(v,w) -> tau(vw)` is the standard nondegenerate diagonal pairing, so the
largest context-invisible ideal is precisely the kernel of this map.

For the language convention use `C e_0 direct-sum C^m`, map the algebra unit
to `(1,...,1)`, every letter `a_i` to `e_i`, and set
`tau_0(v)=sum_{i=1}^m v_i-m v_0`.  Then `tau_0(1)=0`, nonempty pure words have
value one, mixed words have value zero, and the diagonal pairing has nonzero
weights `(-m,1,...,1)`.  It is nondegenerate in characteristic zero.  ∎

**Corollary 3.3.**  No fixed-dimensional linear recognizer realizes this
selector for arbitrarily many supplied colors.

## 4. Character rigidity

### Lemma 4.1 — target character

For every nonempty word,

\[
 \chi_m(w)=\operatorname{Tr}(w\mid\Lambda_m),
\]

and the identity trace of `Lambda_m` is `m`.

### Theorem 4.2 — ordinary semisimple rigidity

Let `rho:R->End(V)` be finite-dimensional and suppose
`Tr rho(w)=chi_m(w)` for every positive word.  Then

\[
 V^{\mathrm{ss}}\cong
 \Lambda_m\oplus L_0^{\oplus(\dim V-m)}.
\]

In particular `dim V>=m`.

**Proof.**  Put `d=dim V-m`.  The trace difference between `V` and
`Lambda_m` vanishes on the augmentation ideal.  If `d>=0`, compare `V` with
`Lambda_m direct-sum L_0^d`; their traces agree on the identity and all
positive words, hence by linearity on the entire free algebra.  If `d<0`,
compare `V direct-sum L_0^{-d}` with `Lambda_m`.

Both sides factor through the finite-dimensional combined image algebra.
After quotienting its Jacobson radical, the algebra is a product of matrix
algebras.  The irreducible trace functionals on its blocks are linearly
independent, so equal characters give isomorphic semisimplifications.  The
case `d<0` would put a positive `L_0` multiplicity on the left and none on the
right, which is impossible in the free basis of simple-module classes.
Therefore `d>=0` and the displayed decomposition follows.  ∎

### Theorem 4.3 — graded virtual rigidity

Let `V=V_+ direct-sum V_-` be finite-dimensional and let every letter act
evenly.  If `Str rho(w)=chi_m(w)` for every positive word, then in `K_0(R)`

\[
 [V_+^{\mathrm{ss}}]-[V_-^{\mathrm{ss}}]
 =\sum_{i=1}^m[L_i]+d[L_0],
 \qquad d=\dim V_+-\dim V_- -m.
\]

Equivalently, there are a semisimple module `W` and `a,b>=0`, `a-b=d`, such
that

\[
 V_+^{\mathrm{ss}}\cong W\oplus\Lambda_m\oplus L_0^a,
 \qquad
 V_-^{\mathrm{ss}}\cong W\oplus L_0^b.
\]

**Proof.**  Add the required number of dormant modules to the smaller side so
that the identity traces agree.  Positive-word traces already agree because
`L_0` vanishes on the augmentation ideal.  Apply the same finite-image
Brauer–Nesbitt argument, then cancel common simple multiplicities.  ∎

### Proposition 4.4 — radical extensions refute literal splitting

Let the `N_i` be strictly upper triangular in a basis compatible with the
projector diagonal and set `A_i=P_i+N_i`.  Every word product has the same
diagonal as the corresponding projector word.  Hence every word trace equals
`chi_m(w)`, although the matrices may be noncommuting and the module
nonsplit.  Adding an arbitrary representation identically in even and odd
degree gives a second invisible freedom.  Theorems 4.2–4.3 classify the
semisimplified (virtual) character, not the literal matrices.

## 5. Full determinant and the wordwise firewall

### Theorem 5.1 — determinant collapse

Let `T_±(x)=sum_i x_i rho_±(a_i)` in independent commuting variables.  Under
the hypotheses of Theorem 4.3,

\[
 \operatorname{Str}T(x)^r=\sum_{i=1}^m x_i^r
\]

for every `r>=1`, and

\[
 \frac{\det(I-zT_+(x))}{\det(I-zT_-(x))}
 =\prod_{i=1}^m(1-zx_i).
\]

**Proof.**  Expand `T^r` over ordered words.  Each mixed word has supertrace
zero and the unique monochromatic word of color `i` has supertrace one,
giving the power identity.  Substitute it into

\[
 \log\frac{\det(I-zT_+)}{\det(I-zT_-)}
 =-\sum_{r\ge1}\frac{z^r}{r}\operatorname{Str}T^r
\]

and use `-sum_r (zx_i)^r/r=log(1-zx_i)`.  The formal identity is exact for
finite matrices.  ∎

This quotient is a Berezinian/graded determinant.  The ordinary determinant
of the ungraded block sum is the product, not the quotient, of the two
degreewise determinants.

### Proposition 5.2 — aggregate powers are insufficient

Let `R_0=E_12`, `R_1=E_23`, `R_2=E_31`.  Place atom projectors plus `R_i` in
even degree and `R_i^T` in odd degree.  Transposition makes the non-atom
contribution to every commuting-pencil power trace cancel.  Nevertheless

\[
 \operatorname{Str}(A_0A_1A_2)=1,
 \qquad
 \operatorname{Str}(A_2A_1A_0)=-1.
\]

Thus a commutative aggregate product can be correct while its oriented word
ledger is wrong.  Theorem 5.1 requires equality before abelianization.

## 6. Canonical complexes

### Proposition 6.1 — shared bar failure

In the free one-object renewal algebra all letter strings are composable, so
the cyclic bar complex contains mixed necklaces.  In a polynomial/Koszul
model, mixed exterior classes remain.  The support-Euler construction has
the correct alternating number, but with zero differential it cancels mixed
classes virtually rather than making them acyclic.

### Theorem 6.2 — separable color collapse

Let `B_m=C^m=direct-sum_i C e_i` with `e_i e_j=delta_ij e_i`.  The
separability idempotent `sum_i e_i tensor e_i` contracts the normalized bar
resolution in positive degrees.  Therefore

\[
 HH_0(B_m)\cong B_m,
 \qquad HH_q(B_m)=0\quad(q>0).
\]

Left multiplication by `e_i` is `P_i`.  The surviving homology basis is
exactly the supplied atom list.  A one-object algebra with `m` loops retains
mixed words; the successful `m`-idempotent algebra is the disjoint
architecture in algebraic form.

## 7. Holomorphic tensor

Retain Paper25's logarithmic return branches and canonical zero-/one-form
operators `U_{n,0}`, `U_{n,1}`.  For every branch word, their analytic
supertrace equals one after scalar branch weights are removed.

### Theorem 7.1 — finite tensor selector

On the total parity of the color complex tensor the de Rham complex,

\[
 \operatorname{Str}(A_w\otimes U_w)
 =\operatorname{Str}(A_w)\operatorname{Str}(U_w)=\chi_m(w).
\]

Thus both local holomorphic stability denominators and mixed label words are
cancelled at every repetition.  The determinant remains a ratio of honest
total-even and total-odd determinants.

### Theorem 7.2 — countable projector family

For a countable inventory `S`, let `K_S=ell^2(S)` and `P_n` be coordinate
projectors.  Put

\[
 b_n(s,u)=u^{\ell(n)}n^{-s},
 \qquad
 \mathcal T^k_{S,s,u}
 =\sum_{n\in S}b_n(s,u)P_n\otimes U_{n,k}.
\]

If `sum_n |b_n(s,u)|<infinity`, the degreewise sums are trace class.  Indeed,
Paper25's common compact-containment bound gives `||U_{n,k}||_1<=C`, so

\[
 \|\mathcal T^k_{S,s,u}\|_1
 \le C\sum_{n\in S}|b_n(s,u)|.
\]

Orthogonality gives, for all `r>=1`,

\[
 \operatorname{Str}(\mathcal T_{S,s,u})^r
 =\sum_{n\in S}b_n(s,u)^r,
\]

and hence

\[
 D_{\mathrm{gr},S}(s,u,z)
 =\prod_{n\in S}\left(1-z u^{\ell(n)}n^{-s}\right).
\]

For `|u|<=1`, `Re(s)>1` is a uniform trace-class domain.  The unitary
identification

\[
 \ell^2(S)\otimes\mathcal H^k
 \cong\bigoplus_{n\in S}\mathcal H^k
\]

turns the construction into one private holomorphic block per supplied
label.  ∎

## 8. Main collapse theorem

### Theorem 8.1 — pure-power selector atom collapse

For a finite supplied color set over `C`, the all-repetition monochromatic
cyclic coefficient is recognizable and admits exact exterior and projector
realizations.  Its character-normalized observable algebra is `C^m`.  Any
ordinary matrix-trace realization semisimplifies to one color character per
label plus dormant modules; any finite even graded realization has that
virtual class up to matched parity sectors.  Radical extensions are
trace-invisible.  Consequently every full cyclic graded determinant is the
color-block product.  Tensoring with the logarithmic-code holomorphic de Rham
sector gives an honest trace-class family on `Re(s)>1`, but its operator is
unitarily and cohomologically the disjoint supplied atom inventory.

**Proof.**  Combine Lemma 2.1, Proposition 2.2, Theorems 3.1–3.2,
Theorems 4.2–4.3, Theorem 5.1, Theorem 6.2, and Theorems 7.1–7.2.  The
qualifications follow from Proposition 4.4 and Proposition 5.2.  ∎

## 9. Scope boundary

The theorem does not cover arbitrary infinite-dimensional nuclear trace
representations, odd letter maps, unbounded derived objects, or nonlocal
word-dependent weights.  It does not infer literal projector matrices from
trace data.  It makes no analytic-continuation, self-adjointness, RH, or
Hilbert–Pólya claim.

