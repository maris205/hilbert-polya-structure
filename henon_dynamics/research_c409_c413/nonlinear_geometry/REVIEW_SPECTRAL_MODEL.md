# Independent review of the classical model moment proof

Date: 2026-09-06. Reviewed the full `spectral/MODEL_MOMENT_PROOF.md`, including
the subsequently appended ALT source receipt and endpoint clarification.
Also inspected its integration into `spectral/PROOF_DRAFT.md`.
The reviewer did not edit either author file.

## Claim and status

For the positive integral Hankel operator with kernel

$$
E(t+s)=\int_1^\infty e^{-(t+s)\lambda}\,\frac{d\lambda}{\lambda},
$$

the claim is

$$
\lim_{q\downarrow0}q^2\operatorname{Tr}(H_E^q)=\frac1{\pi^2},
\qquad
N(e^{-L};H_E)\sim\frac{L^2}{2\pi^2}.
$$

**Status: PROVABLE AS STATED, using the explicitly declared classical
Hilbert-space ALT inequality.** No counterexample, reversed inequality,
uncontrolled constant, circular trace-class assumption, or missing Tauberian
argument was found in the reviewed proof. The original claim survives
unchanged. This is a correctness assessment of a classical model input,
not a new model theorem or a novelty/admission decision.

The ALT source is the one external operator inequality. Its precise
specialization is checked below. This reviewer has not independently obtained
Araki's subscription full text; the updated author's source receipt accurately
distinguishes that limitation from the readable Hilbert-space statement
checked by the coordinator.

## Assumptions and dependency map

- The Fourier transform is unitary with normalization $(2\pi)^{-1/2}$.
- All traces of positive operators may initially be interpreted as extended
  nonnegative traces. Their finiteness is then proved by the upper bound.
- The coherent-state concavity argument uses $0<q<1$.
- An even integer $M\ge2$ is fixed before taking $q\downarrow0$.
- A strip width $s\in(\pi/2,\pi)$ is fixed, for example $s=3\pi/4$.

The dependencies are: Laplace/coordinate factorization; ALT for the lower
moment bound; a positive form majorant and Gaussian coherent-state Jensen
inequality for the upper bound; the ordered $q,M$ limits; and the explicitly
proved positive-measure Tauberian lemma. No model Weyl law is assumed.

## 1. Factorization, Fourier multiplier, and normalization

For a nonnegative density $\sigma$, define the Laplace map with kernel
$e^{-t\lambda}\sqrt{\sigma(\lambda)}$. Its squared Hilbert–Schmidt norm is

$$
\int_0^\infty\int_0^\infty e^{-2t\lambda}\sigma(\lambda)
\,d\lambda\,dt
=\frac12\int_0^\infty\frac{\sigma(\lambda)}{\lambda}\,d\lambda.
$$

Its products therefore have the same positive eigenvalues, and the product
on the $\lambda$ space has the kernel displayed in the draft. The unitary
map to the line is $(Uf)(x)=e^{x/2}f(e^x)$, which gives

$$
\frac{e^{(x+y)/2}}{e^x+e^y}
=\frac1{2\cosh((x-y)/2)}.
$$

The nonunitary Fourier transform of this convolution kernel is
$\pi/\cosh(\pi\xi)$: substituting $r=e^u$ gives the beta integral with
exponent $1/2-i\xi$. Thus the draft's multiplier and all factors of $2\pi$
are consistent. For $\sigma_E(\lambda)=\lambda^{-1}1_{[1,\infty)}(\lambda)$,
the resulting weight is $a_E(x)=e^{-x}1_{[0,\infty)}(x)$ and the trace is
$1/2$.

Minor exposition point only: for the opening statement about an arbitrary
integrable density, an unbounded $a$ makes the sandwich notation naturally
a form/Gram extension. Both weights actually used in this proof are bounded,
so no domain problem enters any subsequent step.

## 2. ALT orientation and infinite-dimensional scope

The required form is

$$
\operatorname{Tr}(A^{1/2}BA^{1/2})^q
\ge \operatorname{Tr}(A^{q/2}B^qA^{q/2}),\qquad 0<q<1.
$$

There are two exact ways to match the source parameters. In the standard
ALT trace form

$$
\operatorname{Tr}(Y^{r/2}X^rY^{r/2})^p
\ge\operatorname{Tr}(Y^{1/2}XY^{1/2})^{rp},
\qquad r\ge1,\ p>0,
$$

take $X=B^q$, $Y=A^q$, $r=1/q$, and $p=q$. The free outer exponent is
essential; citing only an outer-exponent-one Lieb–Thirring statement would
not by itself justify this substitution.

The source receipt instead uses
$\|UV\|_{pr}^{p}\le\|U^pV^p\|_r$. Taking
$U=b(D)^{q/2}$, $V=a_E(X)^{q/2}$, $p=1/q$, $r=2q$, and raising to $2q$
gives precisely the same inequality. The exponent $2q$ is allowed to be
less than one, so a statement restricted to Banach Schatten norms would be
insufficient; the recorded source explicitly allows every positive exponent.

Here $A=a_E(X)$ and $B=b(D)$ are bounded positive operators on $L^2(\mathbb R)$.
The right side is the squared Hilbert–Schmidt norm of
$b(D)^{q/2}a_E(X)^{q/2}$. Its Fourier-space kernel gives

$$
\frac1{2\pi}\int a_E(x)^q\,dx\int b(\xi)^q\,d\xi.
$$

No cyclic manipulation of a non-trace-class product is needed. Since
$\int a_E^q=1/q$ and $q\int b^q\to2/\pi$, the lower constant is $1/\pi^2$.

There is also a useful logical safeguard: Section 3 proves the finiteness of
$\operatorname{Tr}(H_E^q)$ independently of ALT. Therefore, if one prefers a
source convention requiring the Schatten quantity on the right of the norm
inequality to be finite, apply the lower-bound argument after Section 3.
No approximation identity for compressed fractional powers is required.

## 3. Soft majorant: comparison in the correct space

For $\lambda\ge1$,

$$
\frac{\sigma_E(\lambda)}{\sigma_M(\lambda)}
=\left(1+\frac1\lambda\right)^M\le2^M;
$$

for $0<\lambda<1$ the left density is zero. For every vector in the original
$t$ space, the Laplace quadratic forms consequently satisfy

$$
\langle f,H_Ef\rangle\le2^M\langle f,H_Mf\rangle.
$$

This proves the advertised operator comparison. It does not presume that
$\sqrt a\,b(D)\sqrt a$ is operator-monotone as a function of the pointwise
weight. Positive compact-operator eigenvalue monotonicity then proves the
trace-power comparison for every positive power.

As an independent normalization check,
$\int a_M(x)\,dx=B(1,M-1)=1/(M-1)$, so
$\operatorname{Tr}H_M=1/[2(M-1)]<\infty$. The restriction $M\ge2$ matters:
$M=1$ would leave a nondecaying negative spatial tail.

## 4. Uniform complex-strip and coherent-state estimates

The Gaussian states have norm one and the stated resolution of the identity.
Spectral Jensen gives
$\langle\psi,K^q\psi\rangle\le\langle\psi,K\psi\rangle^q$ for $0<q<1$.
Integrating the left side gives $\operatorname{Tr}K^q$ by a nonnegative
orthonormal-basis sum and Tonelli. This remains valid before trace finiteness
is known.

For $s\in(\pi/2,\pi)$, the two quantitative input bounds are correct:

$$
|1+e^{-r-iv}|\ge\cos(s/2)(1+e^{-r}),\qquad |v|\le s,
$$

$$
(\log a_M)'(r)=-1+\frac{M}{1+e^r},\qquad
|(\log a_M)'(r)|\le M-1.
$$

The complex Gaussian contributes at most $e^{s^2/2}$. Consequently one may
take, up to its fixed Gaussian normalization, the constant in (3.4) to be
$e^{s^2/2}\cos(s/2)^{-M/2}$. The integral controlling its Fourier transform is

$$
I_M=\int_{\mathbb R}
e^{(M-1)|u|/2-u^2/2}\,du<\infty,
$$

which has no $x$, $\xi$, or $q$ dependence. For example,
$I_M\le2\sqrt{2\pi}\,e^{(M-1)^2/8}$. Contour shifting is legitimate because
the denominator has no zeros in the closed smaller strip and the Gaussian
forces the vertical ends to vanish for each fixed center and frequency.
The resulting Fourier estimate is uniform in the center.

Finally, the triangle inequality yields

$$
\int e^{-\pi|\eta|}e^{-2s|\eta-\xi|}\,d\eta
\le\frac2{2s-\pi}e^{-\pi|\xi|}.
$$

The strict inequality $2s>\pi$ is used exactly here. Thus (3.3) holds with
a constant depending only on $M$ and the chosen $s$, and the phase-space
integral in (3.6) is finite for every $0<q<1$.

## 5. The ordered limits and the coefficient

Direct substitution gives

$$
\int_{\mathbb R}a_M(x)^q\,dx
=\int_0^\infty r^{q-1}(1+r)^{-Mq}\,dr
=B(q,(M-1)q).
$$

The gamma-function expansion at zero gives
$qB(q,(M-1)q)\to M/(M-1)$. Hence for each fixed even $M$,

$$
\limsup_{q\downarrow0}q^2\operatorname{Tr}H_E^q
\le\frac1{\pi^2}\frac{M}{M-1}.
$$

Both $2^{Mq}$ and $C_M^q$ tend to one at this stage. Only afterwards is
$M$ sent to infinity. The possible rapid growth of $C_M$ is therefore
irrelevant. Together with the lower bound this proves the exact moment
limit, without assuming any uniformity in $M$.

## 6. Tauberian step, including escaped mass and endpoints

The supplied proof of the required Tauberian statement is complete. For
$\nu_L(B)=L^{-2}\mu(LB)$, its Laplace transforms tend to $C/s^2$.
After tilting by $e^{-x}$ and pushing forward to $y=e^{-x}$, the moments,
including the zeroth moment, tend to $C/(m+1)^2$.

The limiting finite measure on $[0,1]$ can be written explicitly as
$C(-\log y)\,dy$ on $(0,1)$. It has total mass $C$ and no atom at either
endpoint. The zeroth-moment convergence supplies the uniform total-mass
bound needed to pass from polynomial tests to continuous tests; it also
prevents an unaccounted additional limiting mass at $y=0$.

The bounded function
$y^{-1}1_{[e^{-1},1]}(y)$ has a discontinuity set of limiting measure zero.
Weak convergence therefore permits this test, and its integral is exactly
$\nu_L([0,1])$. The limit is

$$
\int_{e^{-1}}^1\frac{C(-\log y)}y\,dy
=C\int_0^1x\,dx=\frac C2.
$$

For the eigenvalue application, compactness implies local finiteness of the
positive-eigenvalue energy counting measure. In fact $\|H_E\|\le1/2$ already
makes its energies positive, so the allowed fixed shift is harmless rather
than necessary. The upper moment bound establishes finite Laplace transforms.
The added strict/closed threshold sandwich is correct. Monotone inversion
then gives $\log\lambda_n=-\pi\sqrt{2n}+o(\sqrt n)$.

## 7. Integration and remaining scope

The updated main proof now derives the model constant through this moment
proof before its Laguerre/Widom historical comparison. Its transfer step
therefore no longer needs either conflicting reported Widom coefficient.
The remaining old paragraph invoking W is inside that optional classical
comparison; labeling it explicitly as an alternative route would improve
readability but is not needed to repair a mathematical gap.

The source receipt's norm-form parameter substitution has been checked
against the actual factors in this proof. The receipt links the official
[Araki record](https://link.springer.com/article/10.1007/BF01045887) and the
readable [Lafleche notes, Section 5.5.4](https://laurent-lafleche.perso.math.cnrs.fr/docs/Semiclassical%20dynamics.pdf),
while honestly recording that the original subscription full text was not
retrieved. No original-source access is claimed by this review.

**Handoff:** this model supplement passes the internal mathematical audit.
The source-ownership and standalone-substantiality gate for the complete
Dirichlet-germ transfer remains separate. This supplement creates no second
spectral contract and does not alter the earlier ownership report.

## 8. Requested nonauthor standalone-substantiality decision

**MATHEMATICAL AUDIT: PASS. STANDALONE C409–C413 ADMISSION: REJECT.**
Preserve the complete transfer proof as a mathematical short note, with the
model supplement and honest attribution. Do not allocate a formal paper
contract to its current claim set. This is an explicit substantive assessment,
not an inference that a missing exact search match proves either novelty or
non-novelty.

The batch plan requires a substantial independent question and expressly
excludes short consequences of classical spectral theory. Applying that
criterion, I do not consider the current remaining increment sufficient:

1. **The novel part is a transfer criterion, not a new spectral mechanism.**
   The logarithmic-germ assumption fixes the complete leading local singular
   type. The remainder is analytic at the only relevant corner and has the
   half-plane tail control forced by the positive Dirichlet representation.
   The remaining proof is a useful dyadic approximation estimate followed by
   variational perturbation. It closes a real proof obligation, but this is
   the natural application layer of the already owned analytic-approximation
   and classical-model mechanisms, rather than a separate difficult question
   about these operators.

2. **Complete quantifiers make the result valid and reusable, but do not by
   themselves supply the missing substance.** The theorem accommodates
   arbitrary positive weights and locally finite frequencies satisfying the
   strong same-type germ hypothesis. It does not classify which data have
   that germ, establish a converse, determine a maximal spectral universality
   class, or analyze a transition where the model ceases to govern. The
   generality is conditional on precisely the local structure used by the
   comparison proof.

3. **The prime/AP application is genuine but does not close an additional
   arithmetic problem.** For each fixed modulus and selected reduced classes,
   classical character orthogonality, Euler products, and nonvanishing at one
   supply the premise. The conclusion is independent of the class density
   and membership. There is no uniform varying-modulus result, arithmetic
   secondary term, recovery of class data, new cancellation estimate, or
   arithmetic inverse statement. Adding more fixed prime selections would
   not change this assessment.

4. **The model supplement must not inflate the increment.** Its independent
   ALT/coherent-state proof successfully resolves the disputed-coefficient
   dependency and is worth retaining. It reproves a classical model law,
   however. The determinant asymptotic is then an integration consequence of
   the same counting law, not another independent closure.

This does not mean the transfer theorem is false, valueless, or certainly
already published. A self-contained short note can be useful. My rejection
is specifically of counting it as one of the five substantial independent
contracts under this batch's stronger threshold. The proof gap that the
analytic lemma fills is real; equating every real proof gap with a sufficient
research-paper increment would nevertheless weaken that threshold.

The most concrete reason to change this decision would be a genuinely new
mathematical question closed by these operators, whose answer is not already
fixed by the assumed logarithmic corner model—for example an arithmetic
observable surviving beyond the universal leading term, with its own complete
proof. This is not an instruction to append speculative claims or split off
more model variations. Without such a question, the current disposition is
**saved short note, zero admitted contracts**.
