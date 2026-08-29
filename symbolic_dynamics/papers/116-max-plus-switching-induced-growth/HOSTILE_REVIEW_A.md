# Hostile Review A: *Switching-Induced Growth for a Neutral Max-Plus Pair*

**Role:** independent non-author review from raw matrices  
**Review date:** 2026-08-29  
**Provisional verdict:** **MAJOR REVISION / EXTERNAL DISSEMINATION HOLD**  
**Novelty and priority:** **HOLD; no positive determination**

## 1. Executive verdict

I reconstructed the manuscript from the two displayed matrices rather than trusting the narrative or verifier. The generator powers, literal projective dynamics, reward lumping, finite transform, characteristic cubic, stationary law, drift, Poisson variance, Perron derivatives, pressure, large-deviation mechanism, word extrema, temperature limits, and deterministic endpoints all survive that reconstruction. I found no counterexample to those principal theorem formulas.

I did find a serious false statement in the scope firewall. The paper says that there is no reset word or regeneration time because both generators have tropical rank two. That inference is invalid, and this particular semigroup already contains **four tropical-rank-one products of minimal length three**. Thus the interior process has synchronizing/reset patterns and supports a regenerative/coupling interpretation. This is a CRITICAL mathematical and scope defect because the false sentence is used to separate the paper from an occupied reset mechanism.

A second CRITICAL production defect appears in Proposition 4.3: a missing backslash causes the literal word `qquad` to be printed inside the Perron-derivative display. TeX reports no warning because it treats the letters as ordinary mathematical variables. The error is visible on page 5 and in fresh PDF text extraction.

The exact pair-specific formulas remain viable after these repairs, but the owner subtraction is materially incomplete. Finite projective reductions, induced Markov chains, mean performance of max-plus automata, Bernoulli max-plus Lyapunov exponents, and randomly switching max-plus systems all have direct primary owners that are not presently cited. Search absence is not novelty. External circulation must remain on hold.

## 2. Reconstruction from the raw generators

The chronological convention is that a word `X_1...X_n` acts as

\[
 M_n=X_n\otimes\cdots\otimes X_1.
\]

I used that convention throughout. It agrees with the manuscript's `A,A,B` sentinel.

### 2.1 Generator powers and deterministic endpoints

For

\[
 A=\begin{pmatrix}-2&-1\\1&-1\end{pmatrix},\qquad
 B=\begin{pmatrix}-1&1\\-1&-2\end{pmatrix},
\]

the loop and two-cycle means are respectively `(-2,-1,0)` for `A` and `(-1,-2,0)` for `B`. Hence both tropical spectral radii are zero. In each case the diagonal cross-sum is `-3` and the off-diagonal cross-sum is `0`, so each displayed generator has tropical rank two under the stated finite `2 x 2` convention.

Direct multiplication gives, for `m>=1`,

\[
 A^{\otimes2m}=\begin{pmatrix}0&-2\\0&0\end{pmatrix},\qquad
 B^{\otimes2m}=\begin{pmatrix}0&0\\-2&0\end{pmatrix},
\]

and for `m>=1`,

\[
 A^{\otimes(2m+1)}=\begin{pmatrix}-1&-1\\1&-1\end{pmatrix},\qquad
 B^{\otimes(2m+1)}=\begin{pmatrix}-1&1\\-1&-1\end{pmatrix},
\]

with `A` and `B` themselves treated separately at exponent one. Thus both power sequences are bounded and their entrywise maxima equal `n mod 2`. The endpoint pressure is zero for each fixed tilt, and the endpoint `sqrt(n)` fluctuation is degenerate. These claims are correct and do not use an interior stationary law.

### 2.2 Literal gap and strong reward lumping

Writing a projective representative as `(d,0)^T`, raw multiplication gives

\[
 A(d,0)^T=(\max\{d-2,-1\},\max\{d+1,-1\})^T,
\]

\[
 B(d,0)^T=(\max\{d-1,1\},\max\{d-1,-2\})^T.
\]

Subtracting the old coordinate maximum reconstructs the complete local table:

| old gap | under `A`: new gap, reward | under `B`: new gap, reward |
|---:|---:|---:|
| `-3` | `(0,-1)` | `(3,+1)` |
| `-2` | `(0,-1)` | `(3,+1)` |
| `0` | `(-2,+1)` | `(2,+1)` |
| `2` | `(-3,+1)` | `(0,-1)` |
| `3` | `(-3,+1)` | `(0,-1)` |

All five values are genuinely reachable from zero: `A` and `B` reach `-2` and `2`, while `AB` and `BA` reach `3` and `-3`. Negative gaps, zero, and positive gaps therefore lump to `N,Z,P`, including the reward. The accumulated reward equals the maximum coordinate of `M_n(0,0)^T`, hence equals the maximum matrix entry. This part of the tropical route is sound.

### 2.3 Tilted kernel, finite transform, and cubic

With row states ordered `(N,Z,P)`, the reconstructed reward kernel is

\[
 Q_p(y)=
 \begin{pmatrix}
 0&p/y&qy\\
 py&0&qy\\
 py&q/y&0
 \end{pmatrix}.
\]

Starting from `Z` gives

\[
 \mathbb E[y^{H_n}]=e_Z^TQ_p(y)^n\mathbf1.
\]

The determinant is

\[
 \det(rI-Q_p(y))
 =r^3-(p^2+q^2+pqy^2)r-pqy
 =r^3+(2pq-1-pqy^2)r-pqy.
\]

The orientation, reward signs, row-vector convention, and cubic all agree. The formula is valid at `n=0` and at `p=0,1` for `y>0`.

### 2.4 Stationarity, drift, Poisson variance, and Perron derivatives

For `0<p<1`, the untilted kernel is primitive. Solving `pi P=pi` gives

\[
 \pi_N=\frac p{1+p},\qquad
 \pi_Z=\frac{1-pq}{2+pq},\qquad
 \pi_P=\frac q{1+q}.
\]

The only negative transitions are `N --A--> Z` and `P --B--> Z`, so

\[
 \mu_p=1-2(p\pi_N+q\pi_P)=\frac{3pq}{2+pq}>0.
\]

The proposed Poisson solution

\[
 h_N=-\frac{2p}{1+p},\qquad h_Z=0,\qquad
 h_P=-\frac{2q}{1+q}
\]

satisfies `(I-P)h=f-mu 1` state by state. The corrected rewards form bounded martingale differences, and their stationary second moment simplifies to

\[
 \sigma_p^2=
 \frac{4pq(1-pq)(5-2pq)}{(2+pq)^3}>0.
\]

Independent implicit differentiation of

\[
 F(r,t)=r^3+(2a-1-ae^{2t})r-ae^t,\qquad a=pq,
\]

at `(r,t)=(1,0)` gives

\[
 F_r=2+a,\quad F_t=-3a,\quad F_{rr}=6,
 \quad F_{rt}=-2a,\quad F_{tt}=-5a,
\]

and recovers both `mu_p` and `sigma_p^2`. The algebra is sound; the printed statement is not, because of CRITICAL item C2.

### 2.5 Pressure, LDP, words, and temperature edges

For each finite real `t`, `Q_p(e^t)` is primitive. Perron--Frobenius theory therefore yields

\[
 \Lambda_p(t)=\log\rho_{PF}(Q_p(e^t)),
\]

and analytic perturbation gives a real-analytic pressure. Since the limiting log moment-generating function is finite and differentiable on all of `R`, and `H_n/n` is supported in a fixed compact interval, the cited Gärtner--Ellis route does yield the stated full LDP. The proof should name these hypotheses explicitly; see M-MATH-2.

Every reward is `+1` or `-1`, a negative reward lands at `Z`, and the next reward from `Z` is positive. Negative rewards are therefore isolated, giving

\[
 n\bmod2\le H_n\le n.
\]

Avoiding all negative rewards forces the two alternating words. Constant words attain the lower bound. The two alternating-word masses and the even minimum mass are

\[
 \mathbb P(H_n=n)=
 \begin{cases}2(pq)^{n/2},&n\text{ even},\\
 (pq)^{(n-1)/2},&n\text{ odd},
 \end{cases}
\]

\[
 \mathbb P(H_{2m}=0)=(p^2+q^2)^m.
\]

Finally, scaling `Q_p(y)` by `y` as `y` tends to infinity gives Perron root `sqrt(pq)`. At `y` tending to zero, conjugation by `diag(y^{-1},1,y^{-1})` gives limiting Perron root `sqrt(p^2+q^2)`. Hence

\[
 \Lambda_p(t)-t\to\tfrac12\log(pq),\qquad
 \Lambda_p(t)\to\tfrac12\log(1-2pq).
\]

These formulas are correct for `0<p<1`; the manuscript correctly treats deterministic endpoints separately.

## 3. CRITICAL

### C1. The “no reset word / no regeneration” firewall is false

The manuscript reasons from the rank of the two generators to a property of their whole semigroup. Products of tropical-rank-two matrices can have tropical rank one, and they do here. Under the manuscript's chronological word convention, the four length-three switching words give

\[
\begin{array}{c|c|c}
\text{word}&X_3\otimes X_2\otimes X_1&\text{forced projective gap}\\ \hline
ABA&\begin{pmatrix}0&-2\\3&1\end{pmatrix}&-3\\[3pt]
ABB&\begin{pmatrix}1&-1\\1&-1\end{pmatrix}&0\\[3pt]
BAA&\begin{pmatrix}-1&1\\-1&1\end{pmatrix}&0\\[3pt]
BAB&\begin{pmatrix}1&3\\-2&0\end{pmatrix}&3
\end{array}
\]

In every matrix the two rows differ by an additive scalar, equivalently the diagonal and off-diagonal cross-sums agree. Thus all four products have tropical rank one. Direct enumeration shows that no word of length one or two has this property, so reset length three is minimal.

At the three-state level, these words send every starting state respectively to `N,Z,Z,P`. For `0<p<1`, each pattern has positive probability. Occurrence of such a word erases the prior projective state and supplies a coupling/regeneration mechanism.

**Consequences and required repair:**

1. Delete the false statement that there is no reset word or regeneration time.
2. Add a short proposition giving the four minimal rank-one words and their reset states.
3. Add verifier assertions that all length-one/two products have rank two and that exactly these four length-three words have rank one.
4. Reassess the P89 firewall. A valid distinction may still exist at the state space and observable level, but it cannot be “absence of reset/regeneration.” Any internal overlap decision belongs to the sequence owner, not this review.
5. Strengthen owner subtraction: memory loss and regenerative limit theory apply even more directly than the manuscript admits.

This false firewall is the only factual counterexample I found; it does not invalidate the displayed drift, variance, pressure, or word formulas.

### C2. Proposition 4.3 prints the literal variable string `qquad`

The source line after the first derivative is

```tex
(\log\rho_p)'(0)=\mu_p,qquad
```

and is missing the backslash before `qquad`. The page-5 PDF therefore displays

```text
(log rho_p)'(0) = mu_p, qquad(log rho_p)''(0) = sigma_p^2.
```

This is part of a theorem statement, not an invisible source typo. It survives a warning-free build because TeX accepts the letters as ordinary math variables.

**Required repair:** change the token to `\qquad`, rebuild from a clean directory, extract the PDF text, and visually inspect page 5. A clean log alone is not a sufficient check.

## 4. MAJOR (mathematics and claim support)

### M-MATH-1. Either prove the claimed “exact word interval” or stop calling it an interval

The theorem proves two sharp bounds and identifies extremizers. The introduction and conclusion go further and call this an “exact word interval,” which ordinarily asserts that every parity-compatible intermediate height occurs. That assertion is true but currently unproved. A one-line construction fixes it: for every `0<=k<=floor(n/2)`, concatenate `k` blocks `AA`, each contributing rewards `(+1,-1)` and returning to `Z`, with an alternating suffix of length `n-2k`. The resulting height is `n-2k`. Add this construction and state the exact support, or replace “interval” everywhere by “sharp bounds.”

### M-MATH-2. State the exact Gärtner--Ellis hypotheses used for the full LDP

The LDP conclusion is correct, but “differentiable with full domain” is presented too tersely for a central theorem. State that the limiting cumulant generating function is finite, lower semicontinuous, and differentiable on all of `R`; its effective domain has no finite boundary, so the steepness condition is vacuous; and the deterministic support bound gives exponential tightness. Cite the precise theorem version. This also makes clear why the Legendre transform controls the boundary points rather than merely exposed interior slopes.

### M-MATH-3. Do not call the two routes independent end to end

The spectral route takes `Q_p(y)` from the literal reward-lumping route, so the routes are complementary, not independent proofs of the original cocycle. There are independent *calculations* of the variance after the kernel is fixed (Poisson versus Perron differentiation). Rename the subsection and contribution language accordingly.

## 5. MAJOR (owner and scope control)

### 5.1 Bounded primary-source audit

I searched exact matrix entries, exact title phrases, random and Bernoulli max-plus products, finite projective semigroups, induced Markov chains, max-plus Lyapunov exponents, random switching, and pressure/large deviations. I checked primary publisher, DOI, author-preprint, or journal records. This is a bounded audit, not an ownership clearance.

| Primary source | Owned or neighboring material | Required treatment |
|---|---|---|
| Gaubert, “Performance Evaluation of (max,+) Automata,” *IEEE TAC* 40 (1995), DOI [10.1109/9.478227](https://doi.org/10.1109/9.478227) | Projectively finite max-plus representations reduced to additive costs on a finite dynamical system; mean performance via the Kolmogorov equation of an induced Markov chain. | Direct engine owner for finite projective reduction and mean-rate computation. Must be cited and receive zero credit. |
| Mairesse, “Products of Irreducible Random Matrices in the (Max,+) Algebra,” *Adv. Appl. Probab.* 29 (1997), DOI [10.2307/1428012](https://doi.org/10.2307/1428012) | Stationary projective regimes, coupling, and random max-plus products. | Direct projective/stationary owner missing from the bibliography. |
| Baccelli and Hong, “Analytic Expansions of Max-Plus Lyapunov Exponents,” *Ann. Appl. Probab.* 10 (2000), DOI [10.1214/aoap/1019487510](https://doi.org/10.1214/aoap/1019487510) | Bernoulli iid max-plus products and analytic dependence of their Lyapunov exponent. | Mandatory near-owner for the Bernoulli parameter and analytic pressure/growth language. |
| Blondel, Gaubert, and Tsitsiklis, “Approximating the Spectral Radius of Sets of Matrices in the Max-Algebra is NP-hard,” *IEEE TAC* 45 (2000), DOI [10.1109/9.880644](https://doi.org/10.1109/9.880644) | Average max-algebraic spectral radius; explicitly records the induced projective Markov-chain method when the chain is finite and generating-series methods in special cases. | Direct computation-method owner and useful boundary on what is generic versus pair-specific. |
| Merlet, “Semigroup of Matrices Acting on the Max-Plus Projective Space,” *Linear Algebra Appl.* 432 (2010), DOI [10.1016/j.laa.2009.03.029](https://doi.org/10.1016/j.laa.2009.03.029) | Projective semigroup structure and CLT consequences for stochastic recursions. | More specific than the current generic Merlet citations; particularly relevant after the rank-one-word correction. |
| Goverde, Heidergott, and Merlet, “A Coupling Approach to Estimating the Lyapunov Exponent of Stochastic Max-Plus Linear Systems,” *EJOR* 210 (2011), DOI [10.1016/j.ejor.2010.09.035](https://doi.org/10.1016/j.ejor.2010.09.035) | Coupling-based computation/estimation of stochastic max-plus Lyapunov exponents. | Cite as a computational and coupling neighbor; distinguish the present exact finite quotient from estimation. |
| van den Boom and De Schutter, “Modeling and Control of Switching Max-Plus-Linear Systems with Random and Deterministic Switching,” *Discrete Event Dynamic Systems* 22 (2012), DOI [10.1007/s10626-011-0123-x](https://doi.org/10.1007/s10626-011-0123-x) | Established “switching max-plus-linear systems” terminology, including stochastic switching. | Mandatory terminology/system-class neighbor. Pair-specific formulas may remain residual, but “switching max-plus” is not newly owned. |
| Kordonis, Maragos, and Papavassilopoulos, “Stochastic Stability in Max-Product and Max-Plus Systems with Markovian Jumps,” *Automatica* 92 (2018), DOI [10.1016/j.automatica.2018.03.008](https://doi.org/10.1016/j.automatica.2018.03.008) | Randomly switching max-plus systems and asymptotic growth bounds. | Relevant stochastic-switching neighbor; not the same iid exact pair. |

The manuscript already credits the basic max-plus framework, Merlet's generic limit theory, and a general LDP source. That is necessary but not sufficient. The sources above show that the specific engine “finite projective quotient -> induced Markov/additive chain -> mean/transform” is classical, not merely generic probability folklore.

### O-SCOPE-1. Rewrite the contribution after engine subtraction

No credit should be assigned to finite projective Markov reduction as a general method, stationary balance, Poisson martingale CLTs, tilted finite kernels, Perron pressure, Gärtner--Ellis, or switching max-plus terminology. The defensible residual is the arithmetic conjunction for these two matrices: the explicit five-gap quotient, rational drift and variance, cubic, exact support/extremal masses, and temperature constants. That residual remains owner-HOLD pending a broader exact-pair search.

### O-SCOPE-2. Reopen the internal reset firewall

Because length-three products are rank one, this system does use synchronizing/reset mechanics. Do not preserve an internal distinction that has been falsified. A revised firewall must compare the actual state, reset map, observable, and theorem engine with the occupied system and obtain a sequence-owner decision.

### O-SCOPE-3. Search absence is not novelty

The bounded search did not locate the identical displayed pair or all of its closed forms. That miss does not establish novelty or priority. Keep all “new,” “first,” “novel,” and equivalent language prohibited, and retain external HOLD.

## 6. MINOR

1. The phrase “five literal gaps” should explicitly exhibit one word reaching each nonzero value; the proof table makes this easy.
2. The transfer identity is stated only for `y>0` because `Q_p(y)` contains reciprocal powers. Calling it the “full PGF” is acceptable only with that domain qualification; at `y=0`, use polynomial continuation if needed.
3. Define the endpoint centered fluctuation explicitly as `(H_n-n*0)/sqrt(n)` rather than “the centered fluctuation.”
4. Cite a precise finite-state martingale CLT for the conditional-quadratic-variation step.
5. “Sharp switching boundary” should always be qualified as the endpoint/interior dichotomy for this displayed pair, not a classification or robustness claim.
6. Keep the noncommutation of the deterministic endpoint and interior temperature regimes visible.
7. The verifier currently checks only the rank of `A` and `B`, not the rank of products. Its lane description must not imply semigroup-rank coverage until the reset regression is added.

## 7. Fresh exact-verifier audit

I ran `code/verify.py` in a fresh Python process with bytecode output disabled and redirected stdout to a new temporary file outside the repository. A direct byte-for-byte comparison with `code/verify.out` returned equality.

| Item | Fresh result |
|---|---:|
| Status | `PASS` |
| Exact assertions | `1,182,943` |
| Literal words | `131,071` through `n<=16` |
| Biased law/PGF horizon | `n<=32` |
| Fresh/stored transcript sizes | `799 / 799 bytes` |
| Direct byte comparison | equal |

All recorded lanes reproduce. The missing semigroup-rank lane explains why the false no-reset statement escaped this otherwise extensive test suite. The finite computation supports the displayed formulas but does not repair the scope error or establish asymptotic ownership.

## 8. Fresh isolated build, fonts, and all-page visual inspection

I copied only the TeX sources and bibliography into a fresh temporary directory and ran `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`. The workspace package was not touched.

| Build item | Fresh result |
|---|---:|
| PDF pages | 8 |
| PDF size | 410,006 bytes |
| Final-pass LaTeX/package warnings | 0 |
| BibTeX `warning$` count | 0 |
| Overfull / underfull boxes | `0 / 0` |
| Undefined references/citations | 0 |
| Font rows | 29 |
| Embedded / subset / Unicode | all yes |
| Deterministic date/ID metadata controls | active; title/author metadata blank |

I rendered and inspected all eight pages. There is no clipping, collision, missing font, broken table, or unreadable page. Page 7 has substantial lower white space but no layout failure. Page 5 visibly prints `qquad` in Proposition 4.3, demonstrating why log checks must be paired with visual and text inspection.

## 9. Actionable repair list

Before the paper may leave HOLD, the author must:

- delete the false no-reset/no-regeneration assertion;
- state and verify the four minimal length-three tropical-rank-one words;
- reopen the internal P89 mechanism comparison with the actual reset structure;
- fix the page-5 `qquad` token and visually inspect the rebuilt derivative display;
- prove full parity-compatible height support or remove “exact word interval”;
- make the Gärtner--Ellis hypotheses for a full LDP explicit;
- rename the two proof routes as complementary and reserve “independent” for the Poisson/Perron variance calculations;
- add the direct primary owners for finite projective Markov reduction, Bernoulli max-plus exponents, and stochastic switching;
- rewrite contribution prose under strict engine subtraction;
- add semigroup-rank/reset assertions to the verifier and preserve the exact assertion total in its transcript;
- fresh-run and byte-compare the updated verifier output;
- rebuild in isolation and repeat warning, font, text-extraction, and eight-page visual checks;
- keep external dissemination, novelty, and priority on HOLD.

## 10. Provisional verdict

**MAJOR REVISION / EXTERNAL DISSEMINATION HOLD.**

The pair-specific theorem formulas are largely correct, but the current package contains a concrete false firewall assertion and a visibly corrupted theorem display. The false reset claim is not cosmetic: it changes the correct proof-engine and internal-collision description. The primary owner boundary also omits direct finite-projective, Bernoulli-Lyapunov, and switching-max-plus sources. No public, novelty, or priority clearance is warranted until the reset structure, owner subtraction, verifier coverage, and PDF are repaired.
