# Independent nonauthor review of the AS1 all-depth auxiliary proof

2026-09-08 UTC. Reviewer: the nonlinear-scout lane, which did not author
the AS1 proof. This is internal mathematical review, not journal peer
review or a worldwide-priority certificate. The reviewer writes only this
review file and has not edited the AS1 author proof or any admission file.

## Verdict

**PASS for the auxiliary claims as stated**, under the expressly inherited
C14/AS1 inputs. No mandatory mathematical correction was identified.

**The original whole-secondary-circle contract is not proved and must
remain `NOT CURRENTLY JUSTIFIED` / not admitted.** The proof correctly
separates that question from its finite-depth spectral theorem and the
radial residues of the complete weighted sum.

The strongest new conclusion actually verified is
$$
\lim_{r\uparrow1}(1-r)Q(r\zeta)=
\begin{cases}
17/24,&\zeta=1,\\
5/24,&\zeta=-1,\\
0,&\zeta\in S^1\setminus\{1,-1\},
\end{cases}
$$
where $Q(u)=uP'(u)$ is the normalized full correction series from the
author proof. Thus the previously proposed **dense nonzero aggregate
radial-residue** route is genuinely eliminated, at all congruence depths.
This conclusion says neither that the remaining directions are regular
nor that they are singular.

## Frozen artifacts and actual reading

The reviewer read the complete following files, not just an author summary:

1. [AS1_PROOF_PACKAGE.md](../spectral_scout/AS1_PROOF_PACKAGE.md), all
   **432 lines**, SHA-256
   `29e5bef3a8eb37489cd3baaa0e42cf3c1288c8c9c7a506c08e235a5880d73713`.
2. [Original FROZEN_CONTRACTS.md](../../arithmetic_spectral/FROZEN_CONTRACTS.md),
   all 106 lines; AS1 retains the fixed matrices, based-word clock and
   complete secondary-boundary question. The unrelated AS2 section was
   present in that read but supplies no AS1 input.
3. [Inherited PROOF_STATUS.md](../../arithmetic_spectral/solenoid_review/PROOF_STATUS.md),
   all 295 lines, including the mod-eight identity, analytic remainder,
   old two-real-point theorem and the precise proposed aggregate-residue
   route.
4. [Inherited SOURCE_APPLICABILITY.md](../../arithmetic_spectral/solenoid_review/SOURCE_APPLICABILITY.md),
   completely, as a local ownership/applicability record. Direct source
   accesses made by this reviewer are listed separately below; the older
   record's accesses are not claimed as the reviewer's own.

The requested hash was confirmed before review. A source-formula correction
in the reviewer's separate, already-authored AY scout briefly interrupted
this task; it did not modify the AS1 proof or contribute to its authorship.
That correction is not an AS1 source or mathematical dependency.

The author's frozen opening/closing labels saying that independent review
is pending are preserved in that snapshot. **This report supersedes those
pending-review labels for the pinned auxiliary claims only.** It does not
supersede or weaken the author's `NOT CURRENTLY JUSTIFIED` label for the
original entire-circle question.

`research-review` governs the adversarial claims audit and `proof-writer`
the stepwise proof checking. Repository/batch instructions and the explicit
task select the current internal model, replacing legacy external-model
examples. No external review API, GPU, mathematical program, residue
enumeration, numerical eigenvalue computation or old check was run.

## Claim-by-claim decision

| Actual claim | Decision | Essential check |
| --- | --- | --- |
| Unique odd characteristic root and exact determinant valuation for every active word | PASS | Binary lifting and the even root's unit complement work at every $n\ge1$, including $n=1$. |
| Quadratic irrationality and multiplicative relation implies zero total signed length | PASS | Positive expanding real eigenvalues exclude the only possible rational odd roots; the common-field norm treats negative exponents and shared fields. |
| Finite-character approximation of any finite prescribed length phases | PASS | The positive-kernel argument uses only finite character orthogonality and exact relations; it does not assume an infinite-word character. |
| Exact projective transfer trace at all lengths/depths | PASS | One projective fixed residue per active based word, with chronological order preserved; no short-length correction is missing. |
| Full finite-depth peripheral character criterion | PASS | The $b,ab$ unit-root quotient generates the complete $1+8\mathbb Z_2$ image, while the closed graph is irreducible and aperiodic. |
| Algebraic simplicity for the full finite matrix | PASS | The closed block has a simple Perron eigenvalue; all other graph states are transient. An explicit nilpotence verification is given below. |
| Exact odd/even limits $1/2,11/12$ | PASS | The character multiplicities at $k=1,2,3$ and the geometric tail are correct, and dominated passage through the weighted tower is justified. |
| Complete weighted radial residues and two logarithmic coefficients | PASS | The $o(1)$ coefficient remainder is uniformly negligible for normalized radial limits; no uniform spectral gap is assumed. |
| Whole-circle meromorphic continuation or natural boundary | NOT PROVED | Zero radial residue is not regularity; $o(1)$ coefficients are not exponential decay; no crossing-annulus or noncancellation theorem is supplied. |

## 1. Unit roots, irrationality and signed lengths

For each active word, the inherited odd trace gives the two distinct roots
$0,1$ modulo two of $X^2-t_wX+8^n$. The derivative is odd at both, so
binary lifting gives one odd root $\lambda_w$ and one even root $\mu_w$.
Their product is $8^n$ and $1-\mu_w$ is a two-adic unit. Therefore
$$
v_2(D_w)=v_2((1-\lambda_w)(1-\mu_w))
=v_2(1-\lambda_w).
$$
Also $\mu_w$ is divisible by eight for every $n\ge1$, so
$\lambda_w\equiv t_w\equiv(-1)^n\pmod8$. Neither step requires the
length to be large relative to the depth.

The least singular value check is valid: $A$ is symmetric positive
definite with eigenvalues $4,2$, and $B$ with eigenvalues
$(7\pm\sqrt{17})/2$. Their smaller singular values exceed one.
The product inequality remains valid for noncommuting products. Positive
entries give strictly positive discriminant; positive trace and determinant
then make both real eigenvalues positive. Applying the singular-value
bound to each real eigenvector makes both greater than one.

A rational characteristic root would be an integer, and an odd integer
dividing $8^n$ is $\pm1$. Both are excluded. Thus each root has degree two
and norm $8^n$. In the finite compositum $K\subset\mathbb Q_2$ the tower
law gives
$$
N_{K/\mathbb Q}(\lambda_w)=8^{n[K:\mathbb Q]/2}.
$$
This identity is legitimate even when some quadratic fields coincide or
the word is a repetition. Norm multiplicativity also holds for negative
integer exponents. Taking the norm of a root relation forces its total
signed length to vanish, exactly as claimed. No converse relation theorem
or independence assertion is needed or proved.

## 2. The finite-character positive-kernel argument

The evaluation image $E_k$ is a finite subgroup of $(S^1)^m$. Averaging
over this image is equivalent to averaging over $\widehat U_k$, because
the evaluation homomorphism has equal-size fibres. Inflation gives nested
images. For every exponent vector $\nu\in\mathbb Z^m$, finite character
orthogonality gives the claimed indicator of
$\prod_j\lambda_j^{\nu_j}\equiv1\pmod{2^k}$.

For a fixed $\nu$, that indicator tends to one exactly when the product
equals one in $\mathbb Q_2$. In that case the signed-length lemma ensures
the target phase satisfies $t^\nu=1$. The proof does not replace
two-adic approximate relations by exact relations at a finite depth.

For the displayed kernel, the coefficients of the Laurent expansion are
nonnegative before translation. If $a_j$ are the coefficients of the
$s$th power of the geometric polynomial, their sum is $N^s$ and their
number is at most $sN$. Thus
$C_N=\sum a_j^2\ge N^{2s-1}/s$. The bounds
$$
K_N(z)\le sN,\qquad
K_N(z)\le s(2/\varepsilon)^{2s}N^{-(2s-1)}
\quad\text{when }|z-1|\ge\varepsilon
$$
have the correct powers. Outside the target neighborhood, one factor
uses the second bound and the other $m-1$ factors use the first, producing
$N^{m-2s}\to0$.

For each fixed $N$, the product has finitely many Fourier terms. Its
limiting average retains only exact-relation terms, on which the phase
translation is one. Those terms are nonnegative and include constant
coefficient one. This contradicts avoidance. The quantifier order is
sound: first choose the finite family/accuracy, then $N$, then sufficiently
large depth. Nothing here controls that depth in terms of word memory.

## 3. Projective trace, closed walks and chronology

Direct multiplication of $(1,r)^T$ by $B$ or by the allowed $A$ gives
exactly the stated multipliers and fractional-linear maps. The denominators
are odd on their stated domains. The determinant-eight difference formula
therefore proves a factor-$2^{-3}$ contraction for every allowed step.

The parity rule is exact: $B$ sends any residue to an even one, and $A$
sends an even residue to an odd one. Hence closed walks have no cyclic
$aa$. Conversely, an active word beginning with $A$ must end with $B$ and
maps the complete even ball into itself. A word beginning with $B$ is
defined everywhere and its image lies in a fixed parity ball. The
contraction fixed-point argument applies in both cases.

At depth $k$, two fixed residues for a length-$n$ word would satisfy
$$
\delta=8^n u\delta\pmod{2^k}
$$
for an odd $u$. Since $1-8^nu$ is a unit, $\delta=0$. Reduction of the
two-adic fixed point supplies existence. This confirms all short lengths,
not merely $3n\ge k$.

For an edge sequence labelled $w_1,\ldots,w_n$ the vector identity is
$$
M_{w_n}\cdots M_{w_1}(1,r_0)^T
=\left(\prod_{j=0}^{n-1}h_{w_{j+1}}(r_j)\right)(1,r_n)^T.
$$
Thus the row/function convention for $T_{\chi,k}$ has the correct
chronological order. At a closed residue, the multiplier is an odd
characteristic root modulo $2^k$ and hence the unique lifted odd root.
The trace counts one starting projective state for each based word.
Repetitions are retained and no primitive-necklace division appears.

The original solenoid formulation's transpose is consistent with the
inherited chronological determinant convention; this finite transfer
construction uses the actual column action of the displayed $A,B$. It
does not reverse a word to assert a false product identity. Character
orthogonality then gives the exact all-$n$ formula for $b_{n,k}$.

## 4. Peripheral spectrum, zero-state issues and simplicity

The positive test vector is correct: an even row has successors of
weights $\varphi$ and $1$, so its row value is
$\varphi+1=\varphi^2$; an odd row has only the even $B$ successor.
This gives the weighted norm bound $\varphi$ for every character.

Repeated $B$ steps send every residue to $r_B$ as soon as $3\ell\ge k$.
Hence every closed strongly connected component contains $r_B$. Every
state reachable from it can return by $B$ steps, proving that its component
is itself closed and unique. Its $B$ self-loop makes it aperiodic.

An active word's projective cycle lies in that component: from $r_B$,
repetition of the word is admissible and eventually reaches the unique
fixed residue of the word. Every vertex of the cycle is then reachable
from $r_B$ and can return to it. This verifies that the $b$ and $ab$
cycles used in the equality argument are not in some irrelevant block.

At a global weighted-modulus maximum of a peripheral eigenvector, equality
forces every allowed successor to share that maximum and every edge term
to share its phase. Propagating to the closed component gives a nonzero
constant-modulus phase function there. Multiplication around a closed walk
gives $\chi(\lambda_w)=e^{in\theta}$.

The hand root reductions are correct:
$$
\lambda_b\equiv15,\quad\lambda_{ab}\equiv9,\quad
\lambda_b^2/\lambda_{ab}\equiv9\pmod{16}.
$$
The two characteristic polynomials use trace $7$ and $25$, respectively;
the latter trace agrees for $AB$ and $BA$ without claiming those matrices
are equal. The quotient $g_0$ has $v_2(g_0-1)=3$. Repeated squaring raises
that valuation by exactly one, proving that its image has order
$2^{k-3}$ for $k\ge4$, precisely the size of $H_k$. At $k\le3$, $H_k$
is trivial. Thus necessity really excludes every character nontrivial on
$H_k$, not merely a selected family of characters.

Conversely, a character trivial on $H_k$ has all cycle products equal to
$\epsilon^n$, where $\epsilon=\chi(-1)\in\{1,-1\}$. Dividing the edge
weights by $\epsilon$ gives a unit-modulus cocycle with trivial products
on every directed closed walk. A path product from a fixed base vertex
is independent of the path: append the same return path to compare two
choices. Its diagonal gauge identifies the closed block with
$\epsilon S_k|_{C_k}$. Perron–Frobenius applies because that finite block
is irreducible, aperiodic and has the positive eigenvector already given.

There is an additional direct verification of the transient assertion:
**the graph outside $C_k$ is acyclic**. Otherwise its directed cycle
would be an active closed walk, which the preceding argument places in
$C_k$, a contradiction. Its weighted adjacency block is therefore
nilpotent for every $\chi$. This is stronger than the strict spectral
inequality used in the author's text and verifies that no transient
eigenvalue or Jordan block can increase the algebraic multiplicity of
$\epsilon\varphi$. This clarification was sent to the author as optional;
the existing proof needs no mandatory revision for it.

### Explicit checks at the three smallest depths

In even/odd order the closed components and blocks are
$$
\begin{array}{c|c|c}
k&C_k&T_{\chi,k}|_{C_k}\\\hline
1&\{0,1\}&\begin{pmatrix}1&1\\1&0\end{pmatrix}\\
2&\{2,3\}&\begin{pmatrix}\chi(-1)&1\\1&0\end{pmatrix}\\
3&\{6,3\}&\begin{pmatrix}\chi(-1)&1\\1&0\end{pmatrix}
\end{array}
$$
These are direct modular hand substitutions, not a numerical spectrum
run. For $k=2,3$ the two eigenvalues are
$\chi(-1)\varphi$ and $-\chi(-1)\varphi^{-1}$, consistent with all
characters being trivial on $H_k$. The one-letter $a$ word is not counted;
$b$ supplies the self-loop. No negative-time length or empty word enters
the trace series.

## 5. Parity limits, infinite-layer interchange and radial signs

At a fixed depth there are finitely many characters and eigenvalues, so
the strict finite-depth spectral bound permits one $\rho_k<\varphi$.
Tracing a Jordan block contributes its size times $\lambda^n$; polynomial
growth from its off-diagonal nilpotent part does not enter the trace.
The author's $O(2^k\rho_k^n)$ bound follows after averaging the characters.
No $k$-uniform spectral gap is hidden in this step.

Character orthogonality on $U_k/H_k$ gives the displayed table. In
particular, $|U_1|=1$, $|U_2|=2$, $|U_3|=4$, and for $k\ge4$ there
are four characters trivial on $H_k$ among $2^{k-1}$ characters. Half
give each sign at $-1$ for $k\ge2$. The resulting even coefficient is
$2^{3-k}$ for $k\ge4$, while the odd one vanishes.

The uniform elementary majorant
$0\le b_{n,k}\varphi^{-n}\le2$ and the summable weight $2^{-k}$ justify
dominated convergence separately on odd and even lengths. The even tail
is
$$
\sum_{k\ge4}2^{3-2k}=\frac1{24},
$$
so the even limit is $7/8+1/24=11/12$, while the odd limit is $1/2$.
Their average and half-difference are $17/24$ and $5/24$.

For $\eta_n\to0$, the bound
$$
\sup_{|\zeta|=1}(1-r)\left|\sum_{n\ge1}\eta_n r^n\zeta^n\right|
\le(1-r)\sum_{n\ge1}|\eta_n|r^n\longrightarrow0
$$
is valid by the fixed-head/small-tail split. The remaining two geometric
series give exactly the three radial cases in the verdict. In particular
the residue at $-1$ is **positive** $5/24$, not its negative. The
logarithmic integration uses the same split with $r^n/n$ and gives the
claimed positive logarithmic coefficients at the two real directions.

These are conclusions about the complete weighted $P$, not about an
isolated layer. The analytic $E$ and nonvanishing rational prefactor in
the inherited decomposition do not alter these logarithmic coefficients.
The old no-meromorphic-extension proof at the two real points remains
valid and is sharpened, not replaced by an unproved exponentiation step.

## 6. Original scope, classical ownership and remaining gap

Relative to the inherited proof, the new mathematical content is a
uniform classification over **all depths**, rather than another finite
layer sample, and exact aggregate constants rather than intervals. It
also decisively disproves one previously sufficient proposed route to
the full-circle theorem. This is genuine auxiliary progress.

The methods themselves are classical: field norms, finite character
orthogonality/positive trigonometric approximation, fractional-linear
contraction, cycle-cocycle gauges, finite Perron–Frobenius theory and
Abelian limit arguments. Their local application does not turn them
into new general theorems. The original C14 object, active-word support,
archimedean prefactor, initial growth radius, finite tower and the old
two-real-point obstruction remain inherited ownership.

The unchanged original question concerns meromorphic continuation of the
**exponentiated full switching zeta on the entire secondary circle**.
The reviewed proof deliberately supplies none of the following:

- a conductor-versus-memory bound for the finite-character approximation;
- a uniform spectral/resolvent estimate as the projective matrices grow;
- a normally convergent representation on an annulus crossing a nonreal
  arc;
- a proof that near-peripheral poles survive aggregation across layers;
- an exponential bound for $\eta_n$;
- a verified finite-adelic-distortion representation for this switching
  sequence or its secondary correction.

The absence of these results is not a defect in the stated auxiliary
theorem, but it prevents an AS1 admission. Zero normalized radial residues
away from $\pm1$ are compatible with unresolved weaker singularities;
they are not a proof of meromorphic continuation there.

### Bounded direct source applicability check

The review performed **zero AS1 search-query formulations**. It directly
opened the two existing primary targets below and located their relevant
statements. The two web queries during the separate AY correction are
logged in that lane and are not AS1 searches.

1. [Bell–Miles–Ward, 1307.2369v1](https://arxiv.org/html/1307.2369v1):
   actual HTML access covered the introductory setup, Lemma 1 and its
   proof, the higher-dimensional setup, Proposition 14 and Theorem 15.
   The dichotomy assumes one ergodic solenoid automorphism with its
   fixed field/place formula; it is not a theorem about a sum over
   noncommuting based words. The logarithmic-derivative identity is
   inherited background, not a new AS1 mechanism. No full-paper proof
   verification is claimed. The arXiv version date, not the generated
   HTML header date, identifies the version.
2. [Byszewski–Cornelissen–Houben, 2209.00085v2](https://arxiv.org/html/2209.00085v2):
   actual HTML access covered Section 7.1 Definitions 12–13 and equation
   (7.1), Theorem 11.3.3, and the displayed opening of its proof. The
   FAD representation is one global finite-data formula. Finiteness of
   every projective congruence graph does not establish that formula.
   The hyperbolic FAD theorem therefore does not fill the present gap.
   The full theorem proof was not independently reread in this review.

This limited applicability check does not certify worldwide novelty of
the explicit all-depth classification. It is sufficient to reject a
shortcut that would import either boundary theorem without its hypotheses.
No new manuscript, formal evaluation, target Euler factors, root number,
automorphy or zero correspondence follows.

## Final disposition

- Auxiliary theorem: **PASS**, no mandatory mathematical revisions.
- Original full-circle AS1 contract: **NOT CLOSED / NOT ADMITTED**.
- Old dense-nonzero-radial-residue route: **ELIMINATED FOR THIS SYSTEM**.
- Computation: **zero mathematical program executions and zero old reruns**.
- Author proof and global admission state: **not edited by this reviewer**.

Any later change to the character criterion, the trace convention, the
claimed analytic conclusion or an imported input requires checking the
affected argument; this review is pinned to the stated 432-line artifact.
