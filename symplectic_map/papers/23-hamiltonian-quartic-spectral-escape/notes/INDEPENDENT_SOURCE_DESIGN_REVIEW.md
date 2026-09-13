# Paper 23 — Fresh Independent Source-Design Review

- Review date: 2026-08-24 UTC.
- Project: `papers/23-hamiltonian-quartic-spectral-escape`.
- Candidate ID: `hamiltonian_quartic_spectral_escape_v1`.
- Title: **Four-Mode Hamiltonian Product Shears Beyond Cubic Collapse: Exact Degree Growth and Quartic Perron Subfamilies**.
- Reviewer role: fresh source-design reviewer.  I authored none of the ten
  source-design files, the candidate R1 review, the immutable R1 correction,
  or the proof-adversarial R2 review.
- Method: independent hand derivation from the frozen records.  I used no CAS,
  code-generated algebra, finite-iterate sample, modulus sweep, numerical
  spectrum, scientific run, or network lookup as mathematical evidence.

Before reviewing the package I read the complete local instructions in
`proof-writer/SKILL.md`, `research-review/SKILL.md`, and
`novelty-check/SKILL.md`.  The last workflow ordinarily contemplates a current
search, but this gate expressly forbids a new network search.  Accordingly,
the novelty conclusion below is only an audit of the frozen R1 search,
recorded access levels, and internal Papers 20--22 collision boundary.  It is
not an exhaustive or current literature claim.

## 1. Controlling records and opening gate

The following five allowed root records were read through EOF and rehashed
before the package verdict:

| Record | SHA-256 | Bytes | LF | Controlling fact |
|---|---|---:|---:|---|
| `BATCH_06_STATUS.md` | `3489f2fcf1aaa6f8875c6afeb9be763c57ca42b04d6be118016fc0a5880da0aa` | 52,610 | 793 | gate `PAPER23_SOURCE_DESIGN_REVIEW_OPEN`; queue `SOURCE_DESIGN_AUTHOR_STOP_PENDING_INDEPENDENT_REVIEW` |
| `BATCH_06_IDEA_REPORT.md` | `2c10a63d6c7238f5b7d3f0237456b5937e3f78fbac3e9559bb01ea3d30b7eeaf` | 76,878 | 1,562 | exact source-design author stop and ten-file manifest |
| `BATCH_06_PAPER23_CANDIDATE_REVIEW_R1.md` | `a3c9815c2d851c8791a259c4e46a4d33663f06e6ab4faa58a981f89f7ebf3ae7` | 21,915 | 394 | terminal `PAPER23_CANDIDATE_GATE_PASS_R1` |
| `BATCH_06_PAPER23_CANDIDATE_REVIEW_R1_CORRECTION.md` | `2a1278ff35eeeaf7af2f63010c8ad0f10d745cc763a8379d3a833695897f3783` | 9,407 | 231 | positive signs control; terminal `PAPER23_CANDIDATE_GATE_PASS_R1_CORRECTED` |
| `BATCH_06_PAPER23_CANDIDATE_REVIEW_R2.md` | `cb5b3e748fe4cc5b26f51e2b1b4ca7f93ea2e1011a0c4f2f99e47dc6884d5ed8` | 16,028 | 596 | terminal `PAPER23_CANDIDATE_GATE_PASS_R2` |

The corrected positive-sign family and the order
$F_g=T_g^+\circ S_g^+$ control.  The superseded negative-sign sentence in R1
does not control this package.

## 2. Exact frozen package

At opening, the project contained exactly ten regular files in exactly the
three child directories `experiments`, `notes`, and `refine-logs`, with zero
symlinks or other objects.  Their aggregate was exactly 75,446 bytes and
2,311 LF.  Every one of the ten files was read through EOF.

| Frozen path | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `experiments/EXPERIMENT_PLAN.md` | `b37132e282cceeb04a36723d75f48c4af6f3361836067850496cf52b8ad603e8` | 6,015 | 151 |
| `experiments/EXPERIMENT_TRACKER.md` | `85724a53e161bfbbb45af305af66454a757771330157694ff5d7f85215ffcb31` | 2,927 | 55 |
| `notes/CITATION_VERIFICATION.md` | `fcf71a2364fe6b1624ac99189dd61a6655551928989a75bd2b338cea3d059da6` | 7,269 | 90 |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | `e3d6165b7429880cbe4407c6918ce25d6d8872ee05a48dfe457b5559f4df48c6` | 7,107 | 123 |
| `notes/NOVELTY_ASSESSMENT.md` | `3ba35e3a336360e22f054c4821801c9b55e61dd4e9bc50e6aa57150dbca59dca` | 6,992 | 141 |
| `notes/PROOF_PACKAGE.md` | `0d0ffb5a7d540c987d37a93ec38c7a7736ac8445f6a82c5096e471ebcc34c040` | 24,560 | 1,184 |
| `notes/RESEARCH_QUESTION.md` | `3cd1e22973e443c47a1672a82431c14c3b86ceba685330234d19085e65acdb5c` | 5,492 | 135 |
| `refine-logs/FINAL_PROPOSAL.md` | `aa1221ef198ed1fe8c21da2e24107efb5671cc0f4fb70a7cd657a21c73e1f47b` | 5,531 | 185 |
| `refine-logs/INITIAL_PROPOSAL.md` | `485fd5b98e69338aae9a681548ac906e698d98adcd3af8dbf9e42622df9471b4` | 5,158 | 146 |
| `refine-logs/REVIEW_SUMMARY.md` | `c02b85e92727134a2cd65789c4034bbef7c047811d3e03314c9e598e5a054bf3` | 4,395 | 101 |

The author handoff ends exactly `SOURCE DESIGN AUTHOR STOP`; it contains no
inherited independent PASS.

## 3. Positive shears, supports, and phase order

For

$$
S_g^+(q,p)=(q,p+\nabla V_g(q)),\qquad
T_g^+(q,p)=(q+\nabla W_g(p),p),
$$

the inverse maps are the corresponding subtraction shears.  With symmetric
Hessians $H_V,H_W$, the Jacobians are respectively

$$
\begin{pmatrix}I&0\\H_V&I\end{pmatrix},\qquad
\begin{pmatrix}I&H_W\\0&I\end{pmatrix}.
$$

Direct block multiplication against
$\Omega=\left(\begin{smallmatrix}0&I\\-I&0\end{smallmatrix}\right)$ gives
$J^{\mathsf T}\Omega J=\Omega$ in both cases.  Thus the positive signs do not
alter symplecticity, while the subtraction formulas are inverses rather than
alternate theorem families.

Literal differentiation gives the complete eight-row support ledger:

| Row | Supports |
|---|---|
| $\partial_{q_1}V_g$ | $(1,2,2,2)$ and $(g-1,0,0,0)$ |
| $\partial_{q_2}V_g$ | $(2,1,2,2)$ and $(0,g-2,0,0)$ |
| $\partial_{q_3}V_g$ | $(2,2,1,2)$ |
| $\partial_{q_4}V_g$ | $(2,2,2,1)$ |
| $\partial_{p_1}W_g$ | $(1,2,2,2)$ |
| $\partial_{p_2}W_g$ | $(2,1,2,2)$ |
| $\partial_{p_3}W_g$ | $(2,2,1,2)$ and $(0,0,g-2,0)$ |
| $\partial_{p_4}W_g$ | $(2,2,2,1)$ and $(0,0,0,g-1)$ |

Selecting the four pure supports produces

$$
A_g=\begin{pmatrix}
g-1&0&0&0\\0&g-2&0&0\\2&2&1&2\\2&2&2&1
\end{pmatrix},\qquad
B_g=\begin{pmatrix}
1&2&2&2\\2&1&2&2\\0&0&g-2&0\\0&0&0&g-1
\end{pmatrix}.
$$

Because $S_g^+$ is applied first, the complete matrix is $B_gA_g$, not
$A_gB_g$.  Hand multiplication gives

$$
C_g=\begin{pmatrix}
g+7&2g+4&6&6\\
2g+6&g+6&6&6\\
2g-4&2g-4&g-2&2g-4\\
2g-2&2g-2&2g-2&g-1
\end{pmatrix}.
$$

The two seed vectors independently check as

$$
A_g\mathbf1=(g-1,g-2,7,7)^{\mathsf T},\qquad
C_g\mathbf1=(3g+23,3g+24,7g-14,7g-7)^{\mathsf T}.
$$

## 4. Four selectors and the complete ratio-cone certificate

Write $u=u_1(1,x,y,z)^{\mathsf T}$ with $u_1>0$, and put

$$
a_g=\frac{g-1}{g-2},\qquad H_g=\frac{g-5}{2}.
$$

The proposed sufficient cone is

$$
1\le x\le a_g,\qquad 1\le y\le z\le a_gy,\qquad y+z<H_g.
$$

The four pure-minus-mixed selector gaps, with the second phase evaluated at
$A_gu$, recompute to

$$
\begin{aligned}
\Delta_{S,1}&=(g-2)-2x-2y-2z,\\
\Delta_{S,2}&=(g-3)x-2-2y-2z,\\
\Delta_{T,3}&=-8-6x+(g-7)y+(2g-8)z,\\
\Delta_{T,4}&=-6-4x+(2g-6)y+(g-6)z.
\end{aligned}
$$

On the cone they are strictly positive: the first two have lower bounds
$(g-4)/(g-2)$ and a strict zero boundary respectively, while
$a_g\le9/8$, $y,z\ge1$ give
$\Delta_{T,3}\ge(12g-119)/4>0$ and
$\Delta_{T,4}\ge(6g-45)/2>0$.  The ordinary seed belongs to the cone for
every integer $g\ge10$, and its exact selector margins are

$$
(g-8,g-9,3g-29,3g-22).
$$

For $C_gu=u_1(D,N_2,N_3,N_4)^{\mathsf T}$, I obtain

$$
\begin{aligned}
D&=g+7+(2g+4)x+6y+6z,\\
N_2&=2g+6+(g+6)x+6y+6z,\\
N_3&=2g-4+(2g-4)x+(g-2)y+(2g-4)z,\\
N_4&=2g-2+(2g-2)x+(2g-2)y+(g-1)z.
\end{aligned}
$$

All six target walls pass in the required direction:

1. $N_2-D=(g-1)-(g-2)x\ge0$.
2. $(g-1)D-(g-2)N_2=-g^2+4g+5+(g^2-2g+8)x+6(y+z)
   \ge2g+25>0$.
3. $N_3-D=g-11-8x+(g-8)y+(2g-10)z
   \ge4g-29-8a_g\ge2$.
4. $N_4-N_3=2+2x+gy-(g-3)z
   \ge2+2x+((2g-3)/(g-2))y>0$.
5. $(g-1)N_3-(g-2)N_4=(g-1)(g-2)(z-y)\ge0$.
6. For the easily mishandled height wall,
   $$
   E_H=(g-5)D-2(N_3+N_4)
   =g^2-6g-23+(2g^2-14g-8)x-22y-20z.
   $$
   Since $2g^2-14g-8>0$, $x\ge1$, $y+z<H_g$, and $z\ge1$,
   $$
   E_H>3g^2-31g+26=16+(g-10)(3g-1)>0.
   $$

Thus $C_g\mathcal K_g\subseteq\mathcal K_g$.  The proof establishes one
explicit sufficient cone only; it makes no necessity, maximality, uniqueness,
or chamber-classification claim.

## 5. Actual degrees, carry, characteristic zero, and visibility

The base first phase satisfies $A_g\mathbf1>\mathbf1$.  Every entry of
$C_g-I_4$ is positive for $g\ge10$, so each new second-phase row beats the
carried $q$ coordinate.  If $u_n=C_gu_{n-1}$, then
$u_n-u_{n-1}>0$; nonnegativity of $A_g$ and a positive entry in every row give
$A_gu_n-A_gu_{n-1}>0$.  This separately proves the later first-phase carry,
and $(C_g-I_4)u_n>0$ proves the later second-phase carry.  The phase indices
therefore close as

$$
u_n=C_g^n\mathbf1\quad(n\ge0),\qquad
v_n=A_gC_g^{n-1}\mathbf1\quad(n\ge1).
$$

This formal support recurrence is an actual polynomial-degree recurrence.
All frozen forward coefficients are positive integers, and forward iteration
uses only addition and multiplication.  Equal monomials therefore accumulate
positive integer coefficients.  In characteristic zero their images cannot
vanish.  This proves leading-form survival; it is not a sign-invariance
argument and it gives no positive-characteristic extension.

For visibility, $C_g-A_g$ is entrywise positive.  The fourth complete $q$ row
also beats the other three complete $q$ rows because, after division by
$u_1$, its three differences are

$$
\begin{aligned}
q_4-q_1&=g-9-6x+(2g-8)y+(g-7)z
          \ge4g-24-6a_g>0,\\
q_4-q_2&=-8+(g-8)x+(2g-8)y+(g-7)z
          \ge4g-31>0,\\
q_4-q_3&=2+2x+gy-(g-3)z
          \ge2+2x+\frac{2g-3}{g-2}y>0.
\end{aligned}
$$

Combining these three comparisons with $C_g-A_g>0$ checks $q_4$ against all
seven other coordinates.  It is uniquely visible for $n\ge1$; $n=0$ is the
separate eight-way tie.  Hence

$$
\deg(F_g^n)=e_4^{\mathsf T}C_g^n\mathbf1\qquad(n\ge0).
$$

## 6. Independent quartic ledger

The trace is $4g+10$.  I independently expanded the six principal
$2\times2$ minors:

| Indices | Determinant |
|---|---:|
| 12 | $-3g^2-7g+18$ |
| 13 | $g^2-7g+10$ |
| 14 | $g^2-6g+5$ |
| 23 | $g^2-8g+12$ |
| 24 | $g^2-7g+6$ |
| 34 | $-3g^2+9g-6$ |

Their sum is $-2g^2-26g+45$.  The four principal $3\times3$ minors are:

| Indices | Determinant |
|---|---:|
| 123 | $-3g^3+23g^2-52g+36$ |
| 124 | $-3g^3+20g^2-35g+18$ |
| 134 | $-3g^3+12g^2-15g+6$ |
| 234 | $-3g^3+15g^2-24g+12$ |

Their sum is $-12g^3+70g^2-126g+72$.  Block triangularity gives

$$
\det A_g=\det B_g=-3(g-1)(g-2),\qquad
\det C_g=9(g-1)^2(g-2)^2.
$$

Therefore the characteristic polynomial is exactly

$$
\begin{aligned}
R_g(t)={}&t^4-(4g+10)t^3+(-2g^2-26g+45)t^2\\
&+(12g^3-70g^2+126g-72)t
+9(g-1)^2(g-2)^2.
\end{aligned}
$$

The $t$ coefficient also factors as
$2(g-3)(2g-3)(3g-4)$, and direct substitution gives

$$
R_g(1)=3g(g-1)(3g^2-11g+4)>0.
$$

The displayed Cayley--Hamilton recurrence has the correct alternating signs.
Since every entry of $C_g$ is positive, it is primitive.  The seed and the
visible functional pair nontrivially with the positive Perron eigendirections,
so Perron--Frobenius asymptotics give
$\lambda_1(F_g)=\rho(C_g)$ rather than merely a candidate matrix radius.

## 7. Boundary, modular irreducibility, and Perron infinitude

At $g=9$, the seed selector margins are exactly $(1,0,-2,5)$ and the height
condition is at equality $2=(g-5)/2$.  Thus $g=9$ fails this seed and this
four-face itinerary.  The package correctly avoids claiming that no different
smaller-parameter regime can exist.

For $g\equiv3\pmod5$, reduction gives

$$
f(t)=t^4-2t^3-t^2+1\in\mathbf F_5[t].
$$

The hand evaluations at $0,1,2,3,4$ are respectively
$(1,4,2,4,3)$, so no linear factor exists.  In a factorization

$$
f=(t^2+at+b)(t^2+ct+d),
$$

one must have
$a+c=3$, $ac+b+d=4$, $ad+bc=0$, and $bd=1$.  The four possible constant
pairs are $(1,1),(2,3),(3,2),(4,4)$.  Pairs $(1,1)$ and $(4,4)$ contradict
$ad+bc=0$; either middle pair forces $a=c=4$ and then gives
$ac+b+d=1\ne4$.  Thus there is no quadratic factor.  Monicity, reduction
modulo five, and Gauss's lemma prove irreducibility over $\mathbb Q$.

For $g=13,18,23,\ldots$, irreducibility makes every algebraic conjugate of
$\rho(C_g)$ another eigenvalue of the positive matrix, while primitive
Perron--Frobenius makes every other modulus strictly smaller.  Hence the
spectral radius is a quartic Perron number.  Two parameters cannot yield the
same number because equality of their monic irreducible minimal polynomials
would force equality of the $t^3$ coefficient $-(4g+10)$.  The subfamily is
therefore infinite and pairwise distinct.

## 8. Support-kernel explanation only

For
$A=-I_r+\sum_{i=1}^p u_iv_i^{\mathsf T}$ and
$B=-I_r+\sum_{j=1}^q s_jt_j^{\mathsf T}$, a vector in the common covector
kernel satisfies $Ax=Bx=-x$, hence $BAx=x$.  Rank--nullity gives dimension at
least $r-p-q$; this is an explanatory obstruction and not a classification
or sufficient quartic criterion.

For the displayed family, the combined covectors
$e_1^{\mathsf T},e_2^{\mathsf T},\mathbf1^{\mathsf T},e_3^{\mathsf T},e_4^{\mathsf T}$
span the full dual space.  Direct solution gives

$$
\ker(A_g+I)=\operatorname{span}(0,0,1,-1)^{\mathsf T},\qquad
\ker(B_g+I)=\operatorname{span}(1,-1,0,0)^{\mathsf T},
$$

whose intersection is zero.  This only explains removal of Paper 22's common
unit sector.  The independent check $R_g(1)\ne0$ excludes an unrelated unit
eigenvalue, while the quartic conclusion still depends on the selector,
carry, visibility, minor, and modular certificates.

## 9. Citations, novelty, portfolio collision, and anti-claims

The citation ledger accurately preserves the frozen R1 access depths:

- S01, S02, S04, S07, and S08 are limited to abstracts plus the stated
  authoritative, institutional, publisher, author, or journal metadata.
- S03 records the inspected authoritative HTML survey and relevant problem
  and bibliography entries.
- S05 records inspected relevant passages in author-hosted full text.
- S06 records available full text with the abstract and relevant
  shear/factorization passages inspected.
- S09 is only a bibliographic pointer from an inspected authoritative survey.

No abstract-only or bibliographic-only record is inflated into a full-text
noncollision result.  Exact author lists and metadata remain subject to a
future authorized publication-stage recheck.  The only safe source-design
conclusion is that the frozen 24-query R1 screen located no direct match to
the complete corrected package; it does not establish absolute priority.

Internal ownership is also accurate.  Paper 20 owns the two-mode
selector-to-matrix-to-Perron architecture; Paper 21 owns the three-mode phase
matrix, cone, carry, visibility, cubic, and modular-subfamily grammar; Paper
22 owns the arbitrary-mode endpoint-spike common-unit-sector cubic collapse.
Paper 23's bounded increment is the explicit four-spike escape, its visible
quartic matrix, and the infinite irreducible residue-class subfamily.  The
common-kernel lemma, Hamiltonian shears, weighted degrees, matrix recurrences,
visibility technique, Perron--Frobenius, Cayley--Hamilton, and modular
irreducibility are not novelty claims.

The anti-claim ledgers correctly exclude classification, $g\le9$ validity or
global threshold optimality, maximal/necessary cone claims, arbitrary signs,
coefficients, supports or order, positive characteristic, quartic degree for
every $g$, every-full-rank-profile implications, general realization,
minimality, sparsity, entropy, integrability, genericity, conjugacy,
periodicity, finite-sample or computational proof, and absolute priority.

## 10. Standalone mass, zero-science state, and permissions

The corrected R1 supplies an explicit standalone 26-content-page plan.  The
package refines it to a 27-page target inside the same credible 24--28 range
and the required 22--30 band.  The allocation has enough local mass for all
four selectors, all six cone walls, carry, coefficient survival, visibility
against seven coordinates, the ten principal minors, the $g=9$ boundary, and
the complete modular factor exclusion.  It does not outsource a
theorem-critical step to Papers 20--22.

The tracker and complete inventory agree: scientific runs, code, data,
notebooks, scripts, plots, numerical spectra, CAS certificates, parameter or
modulus sweeps, builds, TeX sources, bibliographies, PDFs, and release objects
are absent.  The experiment filenames are zero-science proof-verification
plans only.

This review exercises only the separately opened source-design review gate.
It authorizes no source lock, plan, publication governance, manuscript,
bibliography, figure, code, experiment, build, PDF, release, registry change,
Paper 24 work, submission, upload, hosting, repository push, transport,
message, identity disclosure, or other external effect.

## 11. Non-blocking transcription observation

`notes/PROOF_PACKAGE.md` and `refine-logs/FINAL_PROPOSAL.md` each write
`\mathcal K_g=left\{` once, omitting the backslash before `left`.  The
following braces, inequalities, and every use of the cone make the intended
set definition unambiguous, so this is a Markdown/LaTeX typography defect and
not a mathematical or source-design blocker.  The frozen ten files were not
changed.  Any later authorized manuscript source should render this as
`\mathcal K_g=\left\{`.

## 12. Verdict

All frozen identities match.  The positive-sign symplectic maps, eight-row
support ledger, $B_gA_g$ order, four selectors, seed, all six cone walls,
two temporal carries, characteristic-zero coefficient survival, strict
$q_4$ visibility, ten principal minors, determinant, quartic, $R_g(1)$,
$g=9$ boundary, uniform modulo-five irreducibility proof, Perron infinitude,
support-kernel scope, citation depths, portfolio boundaries, anti-claims,
standalone page mass, zero-science state, and permissions survive independent
review.  No theorem-critical or lifecycle blocker remains at this gate.

The only project mutation made by this reviewer is this review file.  Its
creation changes the project universe from the frozen ten-file opening state
to eleven regular files in the same three directories, with zero symlinks or
other objects; it does not mutate any of the ten author files or any root
record.

SOURCE_DESIGN_PASS
