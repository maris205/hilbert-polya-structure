# HCS-C56 theorem package

Status: **DOCS_FINAL_NO_MORE_EDITS; exact theorem package in the project
RELEASE_FROZEN.**
The classical implications below are proved, and the instance-specific gates
labelled `C56-EXACT-*` have been independently certified by the current
code/results prefreeze.  This is the exact theorem package of the frozen C56
release; the machine evidence intentionally remains at
`PREFREEZE_CODE_RESULTS_PASS`.

## 1. Fixed surface

Let

$$
Y=V(F)\subset \mathbf P^3_{\mathbf Q},
$$

where, in the frozen HCS-C55 rational tangent coordinates
$u_0,u_1,u_2,u_3$,

$$
\begin{aligned}
F={}&75081586157u_0^3-28576620789u_0^2u_1
-122000922135u_0^2u_2-5364921951u_0^2u_3\\
&+164150208636u_0u_1^2-415458334296u_0u_1u_2
+151070718312u_0u_1u_3\\
&+1158143874300u_0u_2^2+114691988016u_0u_2u_3
+113572676646u_0u_3^2\\
&+6898957820u_1^3+1132596902196u_1^2u_2
-30413540316u_1^2u_3\\
&-2054867641020u_1u_2^2+151980984216u_1u_2u_3
+36794420832u_1u_3^2\\
&+2646295985484u_2^3+560186573940u_2^2u_3
+706181383584u_2u_3^2+1884468968u_3^3.
\end{aligned}
\tag{1.1}
$$

HCS-C55 proves that $F$ is primitive and that $Y$ is smooth and geometrically
irreducible.  The C56 importer reconstructs the exact ordered coefficient
array and verifies its frozen upstream identity rather than trusting this
copied display.

Let $F_1(Y)$ denote the Fano scheme of lines on $Y$.  Scheme-theoretically it
is the zero scheme of the section

$$
\sigma_F\in H^0\!\left(\operatorname{Gr}(2,4),
\operatorname{Sym}^3(\mathcal S^\vee)\right),
\qquad [S]\longmapsto F|_S,
\tag{1.2}
$$

where $\mathcal S$ is the tautological rank-two bundle.

## 2. Certified exact premises

The current prefreeze payload records the following exact premises as strict
certificate leaves, and the independent checker recomputes each gate rather
than trusting producer booleans.

### `C56-EXACT-0`: upstream source lock

The importer verifies the committed C55 theorem, certificate, checker, Route,
and scoped code/results identity.  It accepts the frozen stratified status

$$
\texttt{RELEASE\_FROZEN}/
\texttt{DOCS\_FINAL\_NO\_MORE\_EDITS}/
\texttt{RELEASE\_CANDIDATE},
\tag{2.1}
$$

with the last value applying intentionally to machine artifacts.  It replays
the C55 checker and reconstructs all twenty primitive coefficient rows in the
fixed order, sign, and content-one normalization.

### `C56-EXACT-1`: main-chart shape and direct membership

On the Plücker chart $U_{01}$ write a line as the row span of

$$
M(a,b,c,d)=
\begin{pmatrix}1&0&a&b\\0&1&c&d\end{pmatrix}.
\tag{2.2}
$$

Expanding

$$
F(s,t,as+ct,bs+dt)=f_0s^3+f_1s^2t+f_2st^2+f_3t^3
\tag{2.3}
$$

gives $I_{01}=(f_0,f_1,f_2,f_3)$.  Exact data provide a primitive
$g\in\mathbf Z[d]$ and polynomials $h_a,h_b,h_c\in\mathbf Z[d]$, together
with nonzero integers $\lambda_a,\lambda_b,\lambda_c$, such that

$$
\deg g=27,\qquad \deg h_a,\deg h_b,\deg h_c\le 26,
\tag{2.4}
$$

and the substitutions

$$
a=-h_a(d)/\lambda_a,\quad
b=-h_b(d)/\lambda_b,\quad
c=-h_c(d)/\lambda_c
\tag{2.5}
$$

make every $f_i$ vanish modulo $g$.  The checker verifies the four cleared
numerators and zero remainders directly; a reported FGLM shape alone is not a
proof of ideal membership.

### `C56-EXACT-2`: modular irreducibility certificate

The leading coefficient of $g$ is nonzero modulo each of
$7,19,29,37$.  The stored monic factors multiply back to $g$ modulo the
respective prime, have derivative gcd one, and have degree multisets

$$
\begin{array}{c|c}
p&\text{factor degrees}\\ \hline
7&(3,3,3,3,3,6,6)\\
19&(1,4,4,6,12)\\
29&(1,2,8,8,8)\\
37&(2,5,5,5,10).
\end{array}
\tag{2.6}
$$

The independently recomputed intersection of their subset-sum sets is

$$
\bigcap_{p\in\{7,19,29,37\}}S_p=\{0,27\}.
\tag{2.7}
$$

### `C56-EXACT-3`: global chart replay

The five standard Plücker charts other than $U_{01}$ are generated
independently.  Adding the exact equation $p_{01}=0$ gives the unit ideal in
each chart.  This is a convention and coverage guard; the proof of equality in
Theorem A does not silently assume it.

### `C56-EXACT-4`: Weyl and Picard lattice replay

In the basis $H,E_1,\ldots,E_6$ with intersection form
$\operatorname{diag}(1,-1,\ldots,-1)$, the checker constructs the six simple
roots

$$
E_1-E_2,\ldots,E_5-E_6,\quad H-E_1-E_2-E_3,
\tag{2.8}
$$

their reflections, and the 27 line classes

$$
E_i,\qquad H-E_i-E_j,\qquad
2H-\sum_{j\ne i}E_j.
\tag{2.9}
$$

It verifies

$$
|W(E_6)|=51840,\quad |U|=25920,\quad
\operatorname{rank}\operatorname{Pic}(Y_{\overline{\mathbf Q}})^{W(E_6)}=1,
\tag{2.10}
$$

It enumerates exactly 5184 elements with 27-line cycle type
$(2,5,5,5,10)$ and verifies that every one lies outside $U$; the target
cycle type has count zero inside $U$.

Here $U$ is the index-two Coxeter-even subgroup.  “Outside $U$” is **not**
the ordinary sign of the induced permutation in $S_{27}$; the entire
$W(E_6)$ image in $S_{27}$ is even.

## 3. Prefreeze main theorem

### Theorem A: connected finite étale line scheme

The certified gates `C56-EXACT-0` through `C56-EXACT-3` give

$$
F_1(Y)\cong\operatorname{Spec}(E),
\qquad E=\mathbf Q[d]/(g),
\qquad [E:\mathbf Q]=27.
\tag{3.1}
$$

In particular, $F_1(Y)$ is connected and finite étale of degree $27$, and all
of its geometric points lie in $U_{01}$.

The final clause is a conclusion of the degree comparison, not an input to the
chart calculation.  In that comparison,
$F_1(Y)\cap U_{01}\subset F_1(Y)$ is open-and-closed because the global Fano
scheme is finite étale; thus the chart closed immersion is also a global
closed immersion before equal ranks are invoked.

### Theorem B: maximal line-field Galois group

The gate `C56-EXACT-4` is also certified.  Let $K$ be the splitting field of $g$.
The back-substitution formulas identify $K$ with the least normal field over
which all 27 geometric lines are defined.  Then

$$
\operatorname{Gal}(K/\mathbf Q)\cong W(E_6),
\qquad [K:\mathbf Q]=51840.
\tag{3.2}
$$

The degree-$27$ field $E$ is not $K$ and is not Galois over $\mathbf Q$.

### Corollary C: Picard ranks and fields of definition of lines

Under Theorem B,

$$
\rho(Y_{\overline{\mathbf Q}})=7,
\qquad
\rho(Y/\mathbf Q)=1.
\tag{3.3}
$$

The surface $Y$ has no $\mathbf Q$-rational line.  More generally, if a finite
extension $L/\mathbf Q$ defines any geometric line on $Y$, then a conjugate of
$E$ embeds in $L$, and hence

$$
27\mid [L:\mathbf Q].
\tag{3.4}
$$

### Corollary D: projective invariance

The isomorphism class of $F_1(Y)$, the fields $E$ and $K$ up to
$\mathbf Q$-isomorphism inside a chosen algebraic closure, the Galois action on
the 27 lines, and both Picard ranks are unchanged by a rational projective
coordinate transformation and by multiplying $F$ by a nonzero rational
scalar.

## 4. Status of the proof

The implication

$$
\text{exact premises}\Longrightarrow
\text{Theorems A--B and Corollaries C--D}
\tag{4.1}
$$

is proved in `PROOF_PACKAGE.md`.  The prefreeze certificate and independent
checker pass all 10 semantic gates, the adversarial rebound sweep passes all
2684 classified leaves, and the test suite passes 15/15.  The current exact
identifiers are recorded in `README.md` and `INTEGRITY_REPORT.md`.  The
official paper build and documentation provenance pass.  Accordingly this
file may be cited as the exact theorem package of the project
`RELEASE_FROZEN`, bound to implementation commit
`b32402f1dd276a2684d3e849dae26150ebb595e1`.  The separate provenance commit
remains null/external and is not a theorem input.

## 5. Claim boundary

The theorem does not claim any of the following:

- a new proof of the classical 27-line theorem;
- full $W(E_6)$ for arbitrary Yukawa, symmetric, or Hénon cubic surfaces;
- $S_{27}$ as the Galois group;
- that $E$ is normal or Galois;
- absence of $\mathbf Q$-points on $Y$, nonrationality of $Y$, a failure of the
  Hasse principle, or a Brauer–Manin obstruction;
- an equality of integral Picard groups with Galois invariants (only their
  ranks are compared);
- a motive, polarized VHS, Calabi–Yau realization, automorphy, functional
  equation, or dynamical consequence;
- global novelty based on a finite literature search.
