# Independent source-design review R2

## Verdict and review census

**Verdict: PASS.** I find the current source-design theorem provable as stated
under its frozen hypotheses. The finding census is:

- blocker: 0;
- major: 0;
- minor: 0;
- evidence or citation defect: 0;
- wording or authority ambiguity: 0.

This review was performed from the exact current R2 package, not from the
original author stop or the superseded R1 package. I was not a candidate
reviewer, source author, repair author, R0/R1 source-design reviewer, or R1
audit role, and had not previously probed the Paper 26 project. I authored no
file under review. The sole write is this independent review.

The reviewed title is **Newton-Envelope Contraction for Planar Hamiltonian
Product Shears: Selector Rigidity and Bidirectional Degree Growth**, candidate
identifier `planar_newton_envelope_bidirectional_degree_v1`.

## Authority and predecessor audit

The opening lifecycle records were read through EOF and remained exact during
the review:

| Record | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `BATCH_06_STATUS.md` | `2dcadd07ceb5ce56d6ce87039f60c45f9e9716f6c39427f8164af91f94f3c42c` | 363581 | 5115 |
| `BATCH_06_IDEA_REPORT.md` | `02863aadf373aa7a215e59fa83f2f78bceb677a838a1c6a3107c9234cab80ef4` | 509642 | 9329 |

Their controlling state is the R2 source-design review gate. The two immutable
candidate reviews were also read through EOF and reproduced exactly:

| Record | SHA-256 | Bytes | LF | Terminal |
|---|---|---:|---:|---|
| `BATCH_06_PAPER26_CANDIDATE_REVIEW_R1.md` | `cc81cc410d9122bdaf6ebf8b20e57bce3cbe4fcaed17c3cc0ed5f596d9844dbe` | 29824 | 611 | `PAPER26_CANDIDATE_GATE_PASS_R1` |
| `BATCH_06_PAPER26_CANDIDATE_REVIEW_R2.md` | `164273106733f611c0d35a60cb693d5ffbf8cf1300ffb658a00abb555fbda2e1` | 26605 | 1112 | `PAPER26_CANDIDATE_GATE_PASS_R2` |

I consumed the recorded R0 zero-write failure, the R1 repair, the R1
zero-write failure, and the bounded R2 repair. Historical candidate-review
shorthand is not being used as proof of the current theorem; every implication
below was checked against the current ten files.

The exact R2 old-to-new provenance is consistent with the controlling ledgers:

| File | Superseded R1 identity | Current R2 identity |
|---|---|---|
| `notes/PROOF_PACKAGE.md` | `4d90be2867c4ce7c94849960f7eac24ab01973d974d8481e16664179a7c076b0`, 40505 bytes / 1411 LF | `e17c0a801e3b19b0c090e96d69562492465ef96ac39fe3219cdeb193b4cd8f7d`, 40986 bytes / 1431 LF |
| `notes/RESEARCH_QUESTION.md` | `6d3d84786de078161ab407d691a3912f065501605f2f0103608eb10fb9a997df`, 9880 bytes / 209 LF | `bb539d56e60987180c362d7d4b076785b40def15408aef08bf8b58403ee81bb4`, 9878 bytes / 209 LF |
| `refine-logs/REVIEW_SUMMARY.md` | `7696dade250eea049ec84575885cf5d80865bb99adff2e4dd419e4a1cd174ce9`, 11086 bytes / 182 LF | `c0f1576dcc3cc3587bc5c726ac6e70fa87f06f3225cf6e6d381e34933f9ff138`, 14062 bytes / 213 LF |

The other seven current identities match the R1 freeze exactly, so the R2
change set is precisely the authorized three-file change set.

## Exact T10 universe and hygiene

Before this review was written, the project contained exactly three child
directories and ten regular files, with no symlink or other node. Directories
were mode 0755; every file was mode 0644 with one hard link. Every file was
valid UTF-8 with no BOM, CR, or NUL and exactly one terminal LF.

| Relative path | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `experiments/EXPERIMENT_PLAN.md` | `7b543388f7c12220aee27605b6cef53df48b7c835798a90495b4706b98a8355f` | 15201 | 394 |
| `experiments/EXPERIMENT_TRACKER.md` | `c35c8cfba39bf8634e11ee91173b6fb2c313babe347ff30fdf0c5f445b65562d` | 7987 | 105 |
| `notes/CITATION_VERIFICATION.md` | `8ebb74149ce7d1eb22151019cd5a868e941df1c78b787ae605794a1c64011d09` | 8311 | 153 |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | `56853a22b9a89e4599cad40a017d659aa50a6ecbf2cb3d52df080bd14b18d6f4` | 9076 | 75 |
| `notes/NOVELTY_ASSESSMENT.md` | `150573d9fe3cbddac7e49bdefc51ca687bd3b7dc51bbd2651f65b8947f1088a3` | 11496 | 185 |
| `notes/PROOF_PACKAGE.md` | `e17c0a801e3b19b0c090e96d69562492465ef96ac39fe3219cdeb193b4cd8f7d` | 40986 | 1431 |
| `notes/RESEARCH_QUESTION.md` | `bb539d56e60987180c362d7d4b076785b40def15408aef08bf8b58403ee81bb4` | 9878 | 209 |
| `refine-logs/FINAL_PROPOSAL.md` | `56447f2b98d64dc9c97b70f3731f03aa1c41ed68a459c07a178e1166320611ba` | 10528 | 241 |
| `refine-logs/INITIAL_PROPOSAL.md` | `65d4e90de9a9db2ea652c26c43a8114ef61f658efca14cb23ce9dd9d8a309711` | 6789 | 159 |
| `refine-logs/REVIEW_SUMMARY.md` | `c0f1576dcc3cc3587bc5c726ac6e70fa87f06f3225cf6e6d381e34933f9ff138` | 14062 | 213 |

The ten contents total 134314 bytes and 3165 LF. Sorting the relative UTF-8
paths bytewise and framing each entry as
`u64be(path length) || path || u64be(content length) || content` gives 288
path bytes, 160 framing bytes, and a 134762-byte stream. Independent Node and
Ruby implementations both gave SHA-256
`b315b3e6f68b04e2fdf5baac772b477b7d980e58dab045a7469314e678dc10f3`.

The independent-review path, both possible source-lock paths, and `paper/`
were absent at preflight. Thus this review is the sole T10-to-L11 addition.

## Independent mathematical reconstruction

### 1. Symplectic maps and phase order

For

\[
S(q,p)=(q,p+\nabla V(q)),\qquad
T(q,p)=(q+\nabla W(p),p),
\]

the derivative matrices are lower and upper unitriangular block matrices whose
off-diagonal blocks are the symmetric Hessians of (V) and (W). Direct
multiplication by the standard symplectic matrix gives
(DS^{\mathsf T}JDS=J) and (DT^{\mathsf T}JDT=J). Each shear fixes the
variables on which its added gradient depends, so subtraction gives its
inverse. Since (F=T\circ S), the actual inverse phase order is

\[
F^{-1}=S^{-1}\circ T^{-1},
\]

meaning that (T^{-1}) acts first. No degree assertion is inferred merely
from symplecticity.

### 2. Full exposed faces and the Hessian coefficient

Let (u>0) and let (P_u) be the polynomial formed from every support point
on the exposed face. A face has a unique point ((x_0,y_0)) of minimal first
coordinate: two tied points with the same first coordinate have the same
second coordinate because the exposing second weight is positive.

To contribute to the coefficient of
(X^{2x_0-2}Y^{2y_0-2}) in
(P_{XX}P_{YY}-P_{XY}^2), a pair of face exponents must have first-coordinate
sum (2x_0). Minimality forces both first coordinates to be (x_0), and
uniqueness then forces the self-pair. Its coefficient is

\[
c_{x_0,y_0}^2x_0y_0(1-x_0-y_0),
\]

which is nonzero because the coefficient is nonzero, (x_0,y_0\ge2), and
the field has characteristic zero. This proof covers one-point, two-point,
and arbitrary multi-point ties and does not assume coefficient positivity.

The determinant is the Jacobian of ((P_X,P_Y)). The characteristic-zero
Jacobian criterion therefore makes those two derivatives algebraically
independent. If (L_1,L_2) are an algebraically independent leading pair,
the substitution (X\mapsto L_1,Y\mapsto L_2) is injective. Composing the
face-gradient embedding with that substitution preserves algebraic
independence; nonzero scalars, signs, and separated positive powers preserve
it as well. Hence the predicted top forms survive every forward and inverse
half-step, including on a wall.

### 3. Exact transforms and strong block visibility

Define

\[
H(u)=\max_{(x,y)\in E}(xu_1+yu_2),\qquad
\mathcal A(u)=(H-u_1,H-u_2)^{\mathsf T}.
\]

Algebraic independence makes this the exact, rather than merely tropical,
gradient-degree transform. Since every support coordinate is at least two,

\[
H-u_1\ge u_1+2u_2>\max(u_1,u_2),
\]

\[
H-u_2\ge2u_1+u_2>\max(u_1,u_2).
\]

The R1 carry concern requires more than componentwise multiplication by
(B=\operatorname{diag}(e,f)). With
(A=(A_1,A_2)^{\mathsf T}=\mathcal A(u)), the current proof correctly adds

\[
2A_1-A_2=H-2u_1+u_2\ge3u_2>0,
\]

\[
2A_2-A_1=H+u_1-2u_2\ge3u_1>0.
\]

Thus (eA_1\ge2A_1>A_2) and
(fA_2\ge2A_2>A_1); each component of (BA) exceeds both components of
(A). This is the exact missing cross-coordinate statement, and equations
(6.3)–(6.4) genuinely prove it.

Forward, the lower phase replaces the momentum top block by
(\mathcal A(u_n^+)), which dominates every carried block. The upper pure
powers then give (B\mathcal A(u_n^+)), whose two components each dominate
the whole new momentum block and the old position block. Consequently

\[
u_{n+1}^+=B\mathcal A(u_n^+),\qquad
\deg(F^n)=\lVert u_n^+\rVert_\infty.
\]

Inverse, (T^{-1}) first gives the fresh position vector (Bv_n^-). The
inductive hypothesis that every current momentum degree dominates every old
position degree makes each fresh coordinate beat its carried position term.
Moreover (max(Bv_n^-)\ge2\max(v_n^-)). The next face-gradient vector
(\mathcal A(Bv_n^-)) has both components above
(max(Bv_n^-)), hence above the fresh position block and the old momentum
block. Therefore

\[
v_{n+1}^-=\mathcal A(Bv_n^-),\qquad
\deg(F^{-n})=\lVert v_n^-\rVert_\infty.
\]

This verifies both inverse carries independently of the forward argument.

### 4. Exact bridge and its exact boundary

For (c_\star=H(\mathbf1)-1), both coordinates of
(\mathcal A(\mathbf1)) equal (c_\star). Positive homogeneity gives the
base identity and induction

\[
u_{n+1}^+=c_\star Bv_n^-\qquad(n\ge0).
\]

Diagonal norm comparison yields

\[
c_\star\min(e,f)\deg(F^{-n})
\le\deg(F^{n+1})
\le c_\star\max(e,f)\deg(F^{-n}),
\]

so the forward and inverse first dynamical degrees agree. The shift, ordinary
seed, and phase order are essential. The diagonal bridge compares vectors and
rates; it does not transfer a recurrence for a scalar maximum.

### 5. Global projective contraction

With (r=u_1/u_2),

\[
\Phi(r)=\max_E(xr+y),\qquad
\phi(r)=\kappa\frac{\Phi(r)-r}{\Phi(r)-1},\qquad \kappa=e/f.
\]

On the branch exposed by ((x,y)),

\[
\phi'(r)=-\kappa\frac{x+y-1}{(xr+y-1)^2}<0.
\]

The absolute logarithmic derivative is

\[
\eta_{x,y}(r)=
\frac{r(x+y-1)}{((x-1)r+y)(xr+y-1)}.
\]

The denominator minus numerator is

\[
x(x-1)r^2+2(x-1)(y-1)r+y(y-1)>0.
\]

For each of finitely many support points, (\eta) extends continuously by
zero at both projective endpoints and attains a maximum strictly below one.
The finite maximum is one common (q<1). The envelope, hence (\phi), is
continuous at every wall; splitting a logarithmic interval at the finitely
many walls patches the derivative estimate globally. Therefore
(t\mapsto\log\phi(e^t)) is a contraction of the complete line.

The inverse ratio map is

\[
\psi(s)=\frac{\Phi(\kappa s)-\kappa s}{\Phi(\kappa s)-1},
\]

and (L(s)=\kappa s) gives (L\circ\psi=\phi\circ L). In particular,
inverse selectors are evaluated using the Newton ratio of (Bv), namely
(r=\kappa s), not the unscaled ratio (s).

### 6. Selector classification and spectra

The contraction has one fixed ray (r_\star) and no nontrivial numerical
periodic orbit. If (r_\star) is in an open Newton chamber, convergence
eventually fixes its selector. If it is a wall, strict decrease maps each side
to the other. A strict orbit therefore alternates the two adjacent chambers
while converging to the wall; injectivity prevents delayed landing. The fixed
wall orbit stays on the full tied face. At a multiple tie, the two extreme
active exponents govern the open sides and the entire face governs the tie.
The alternating selector word is not a numerical two-cycle.

In an interior chamber the tail matrix

\[
C_{x,y}=B\begin{pmatrix}x-1&y\\x&y-1\end{pmatrix}
\]

is a positive integral (2\times2) matrix. Its fixed positive ray is its
Perron ray, so its characteristic polynomial bounds the algebraic degree of
the first dynamical degree by two.

At a wall, choose the primitive positive integral wall vector (w). All tied
exponents have the same score on (w), so the two adjacent matrices satisfy

\[
C_-w=C_+w=\mu w.
\]

The fixed ray makes (\mu) rational; the integral matrix and primitive vector
make it an integer. Positivity identifies it as each adjacent Perron root.
Both two-step products have Perron root (\mu^2), hence the per-step
dynamical degree is the positive integer (\mu). The uniform algebraic-degree
bound is therefore two, with a sharper integral wall case.

### 7. Forward and inverse scalar recurrences

For (ξ=(x,y)), set

\[
A_ξ=\begin{pmatrix}x-1&y\\x&y-1\end{pmatrix},\qquad
C_ξ=BA_ξ,\qquad
D_ξ=A_ξ B=B^{-1}C_ξ B.
\]

In a forward interior tail, Cayley–Hamilton for (C_ξ) gives a coordinate
recurrence of order at most two. If (r_\star\ne1), convergence fixes the
visible coordinate; if (r_\star=1), the ordinary seed is fixed
projectively from time zero and the scalar degree is geometric.

The inverse proof is separate. A chamber is selected by the ratio of
(Bv_n^-), and in that chamber

\[
v_{n+1}^-=D_ξ v_n^-.
\]

For an inverse interior tail, Cayley–Hamilton for (D_ξ), together with
(s_n\to s_\star=r_\star/\kappa), gives a stable visible coordinate when
(s_\star\ne1). If (s_\star=1), the ordinary seed is already the unique
fixed inverse ray and the sequence is geometric.

For a fixed inverse wall seed, the exact condition is that
(\kappa s_\star=r_\star) lies on the Newton wall. The intermediate vectors
(Bv_n^-) remain on that tied Newton ray, so full-face homogeneity gives
geometric growth. A strict ordinary inverse wall orbit necessarily has
(s_\star\ne1). With a step (D_-) followed by (D_+), define

\[
N_+=D_+D_-,\qquad N_-=D_-D_+,
\]

and with the same order define

\[
M_+=C_+C_-,\qquad M_-=C_-C_+.
\]

Then

\[
N_\pm=B^{-1}M_\pm B.
\]

The two parities have common trace (\tau) by cyclicity and common
determinant (\Delta) by multiplicativity. Since (s_\star\ne1), the same
inverse coordinate is eventually visible on both parity tails. Applying
Cayley–Hamilton separately to (N_+) and (N_-) yields

\[
d^-_{n+4}=\tau d^-_{n+2}-\Delta d^-_n
\]

for all sufficiently large indices. The forward wall proof is the analogous
argument for (M_+) and (M_-). Thus interior orders are at most two and
strict-wall orders are at most four in both directions; no minimality is
claimed.

### 8. Exact fixtures

For (E=\{(2,2)\}) and (B=\operatorname{diag}(3,2)),

\[
C=\begin{pmatrix}3&6\\4&2\end{pmatrix},\qquad
\chi_C(t)=t^2-5t-18,
\]

so the Perron value is ((5+\sqrt{97})/2). Also

\[
u_1^+=(9,6),\qquad v_1^-=(7,8),\qquad
u_2^+=(63,48)=3Bv_1^-.
\]

For (E=\{(2,8),(4,5),(5,3)\}) and
(B=\operatorname{diag}(24,11)), the walls are (3/2) and (2). Exact
iteration gives

\[
r_1=24/11>2,\quad r_2=1548/781\in(3/2,2),\quad
r_3=51294/25619>2.
\]

The middle branch maps ((3/2,2)) above (2); the high branch maps
((2,\infty)) into ((3/2,2)), proving the alternating tail rather than
guessing it numerically. The adjacent matrices share (w=(2,1)^{\mathsf T})
with multiplier 132. Their middle-then-high product has trace 17648 and
determinant 3902976, with eigenvalues (17424=132^2) and 224. All these are
exact arithmetic witnesses, not experimental evidence.

## Coherence, evidence, and scope audit

The claims matrix promotes exactly the consequences proved above and assigns
kill conditions. The validation plan and tracker are symbolic protocols, not
claims that a run occurred. In particular, C03/C04/B03 remain supported by
the collected-support Hessian certificate and characteristic-zero boundary;
C11/P4/T07 are supported by the strong cross-component inequalities; and
C24/P7/P8/T14/T19/T20 are supported by the scaled inverse selector and the
separate (D_ξ,N_\pm) recurrence proof. Review-summary issues 2, 5, and 8
are therefore correctly reclosed.

The R0 scalar-recurrence finding is closed because the current proof no longer
uses the diagonal bridge to transfer a maximum. The three R1 obligations are
also closed: the live scope excludes zero coefficients rather than
characteristic zero; equations (6.3)–(6.4) supply strong forward visibility;
and inverse fixed-wall language uses (\kappa s_\star=r_\star) and the tied
ray of (Bv_n^-). The old contradictory phrase occurs only as quoted repair
history in the summary, not as a live theorem boundary.

The citation ledger is explicitly local and contextual. No cited record is a
proof dependency, incomplete Koch–Lomelí metadata is barred from typesetting,
and all entries require primary-record rechecking before publication. The
novelty assessment makes only a local Papers 1–25 portfolio statement and
keeps global novelty unresolved. The local collision subtraction is coherent:
Paper 24 owns its special wall-selector and parity mechanisms, while Paper 25
owns support-rank and unbounded higher-dimensional Perron degree. Paper 26
retains only the combined arbitrary planar face certificate, contraction,
complete selector classification, bidirectional transport, and quadratic cap.

The live anti-claims correctly exclude axes and exponent one, zero or
uncollected coefficients, mixed (W), positive characteristic, dimension at
least three, altered phase/seed bridge statements, nontrivial numerical
two-cycles, recurrence minimality, higher dynamical degrees, compactification,
entropy, integrability, orbit arithmetic, classification, genericity, and
global priority. No manuscript, source lock, bibliography, computation,
build, release, or external effect is authorized by this review.

## Final integrity statement

All ten predecessor files were reread and rehashed immediately before the
write. The two ledgers and two candidate reviews retained their opening
identities; the exact T10 framed digest remained
`b315b3e6f68b04e2fdf5baac772b477b7d980e58dab045a7469314e678dc10f3`;
and every future path remained absent. The proof status is **PROVABLE AS
STATED** under the frozen hypotheses, with the boundaries above forming part
of the statement. This review records source-design closure only and does not
open, create, or authorize a successor artifact.

PAPER26_SOURCE_DESIGN_PASS
