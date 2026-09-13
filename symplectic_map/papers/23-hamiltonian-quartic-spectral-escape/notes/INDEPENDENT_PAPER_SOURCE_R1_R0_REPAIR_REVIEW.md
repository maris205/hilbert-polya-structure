# Independent Paper-Source R1 Review after the R0 Hyperref Repair

## 1. Verdict, role, and method

Verdict: **PASS**.  I found no mathematical, source-contract,
repair-custody, bibliographic, anonymity, static-LaTeX, inventory, identity,
or permission blocker in the repaired Paper 23 source.

I am the first fresh post-repair reviewer.  I authored none of the source,
locks, earlier reviews, blocker evidence, repair bytes, or diagnostic build
roots, and I did not act as the R0 builder.  I read all twenty-six opening
project files and all three current governing roots through EOF.  Earlier
reviews were treated as immutable custody records, not as substitutes for
the derivations below.  My review was local and read-only until this report:
I did not run TeX, BibTeX, another build engine, or a scientific experiment;
I did not edit source or evidence; and I did not browse or cause an external
effect.  This report is my sole write.

## 2. Controlling roots and opening state

The three controlling regular files were stable at opening and immediately
before this write:

| Root | SHA-256 | Bytes | LF | Mode |
|---|---|---:|---:|---:|
| `BATCH_06_STATUS.md` | `663fef56404b93c23fd4cdaea7096bfdcf90695134c3768a47f1a8da91739675` | 76,337 | 1,132 | 0644 |
| `BATCH_06_IDEA_REPORT.md` | `a3a31fa445a04489724d04b1928ef1fa14d897543e6d33e5e79c739f7ef444d2` | 118,742 | 2,298 | 0644 |
| `BATCH_06_PAPER23_PUBLICATION_LOCK_REVIEW_CORRECTION.md` | `27615c425261aa72caa4c880b6bc7f54ecfa98c99399a2d7efc78ed19d8282c4` | 8,524 | 245 | 0644 |

The live gate is exactly `PAPER23_SOURCE_R1_R0_REPAIR_REVIEW_OPEN`, and the
Paper 23 queue state is exactly
`R0_HYPERREF_REPAIR_FROZEN_SOURCE_R1_REVIEW_OPEN`.  The correction root ends
`PAPER23_PUBLICATION_LOCK_REVIEW_CORRECTED_PASS` and supersedes only the two
false ordinary-kernel transcriptions in the immutable publication-lock
review.  It does not alter a lock, theorem, source byte, or other conclusion.

The opening project inventory was exactly 26 regular files, four child
directories (`experiments`, `notes`, `paper`, and `refine-logs`), zero
symbolic links, and zero other objects.  Every regular file was mode 0644,
UTF-8/LF-clean, and had one terminal LF.  This is the complete opening
ledger:

| Relative path | SHA-256 | Bytes | LF | Mode |
|---|---|---:|---:|---:|
| `experiments/EXPERIMENT_PLAN.md` | `b37132e282cceeb04a36723d75f48c4af6f3361836067850496cf52b8ad603e8` | 6,015 | 151 | 0644 |
| `experiments/EXPERIMENT_TRACKER.md` | `85724a53e161bfbbb45af305af66454a757771330157694ff5d7f85215ffcb31` | 2,927 | 55 | 0644 |
| `experiments/publication_lock.json` | `6f1830f14413c49cad0945facc7b10c081be1a36d4884e5768205273fce200c4` | 51,578 | 1 | 0644 |
| `experiments/source_lock.json` | `5956a7e6c2e12a9be287b2ead2922e135c4a64da738757a0b55884e16974b248` | 32,889 | 1 | 0644 |
| `notes/BUILD_R0_BLOCKER.md` | `8d395e7fdeb2103370b1b1700c1bd54301f0f1206c5a3eea4352298cdd1c5384` | 8,900 | 180 | 0644 |
| `notes/CITATION_VERIFICATION.md` | `fcf71a2364fe6b1624ac99189dd61a6655551928989a75bd2b338cea3d059da6` | 7,269 | 90 | 0644 |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | `e3d6165b7429880cbe4407c6918ce25d6d8872ee05a48dfe457b5559f4df48c6` | 7,107 | 123 | 0644 |
| `notes/INDEPENDENT_PAPER_PLAN_REVIEW.md` | `d491d6fa2fe3ca0d5b03195006f86021f65f6cf56529f592b46730086504b2d9` | 22,954 | 651 | 0644 |
| `notes/INDEPENDENT_PAPER_SOURCE_R1_REVIEW.md` | `aad55320dc0645931be2c0019327cd4255aaa56d77f94cd48e1a3702b10fb9bb` | 30,329 | 785 | 0644 |
| `notes/INDEPENDENT_PUBLICATION_LOCK_REVIEW.md` | `0ecfdc71a2de08e37311cb4683e393e397bb8e87854b01eb021a7db7f4d46dec` | 23,481 | 633 | 0644 |
| `notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md` | `8711ba1e5e6daaef5c008f773cd5a5a0751eb1794b8595befc4c8bd5e4df88fb` | 15,589 | 483 | 0644 |
| `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md` | `c6ae173c45d0e8fbe073395abf366a33e3f4b24bf97c1ab97ad39cdb245e356e` | 17,851 | 441 | 0644 |
| `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md` | `8828364af81e829ee13201e5e8c63b1b92cb33df462c598ec3b615057545ec8c` | 23,668 | 586 | 0644 |
| `notes/NOVELTY_ASSESSMENT.md` | `3ba35e3a336360e22f054c4821801c9b55e61dd4e9bc50e6aa57150dbca59dca` | 6,992 | 141 | 0644 |
| `notes/PROOF_PACKAGE.md` | `0d0ffb5a7d540c987d37a93ec38c7a7736ac8445f6a82c5096e471ebcc34c040` | 24,560 | 1,184 | 0644 |
| `notes/PUBLICATION_STAGE_SCOPE.md` | `fa0aef81669da75eacbe604614d86ae4a18610ef2ce70ba58391a47657f29b31` | 44,575 | 1,269 | 0644 |
| `notes/R0_HYPERREF_SOURCE_REPAIR.md` | `a0fe52acf07aed30dc8571b86a48602e74dc7cd15105ea4d69cd701f2e80bbe4` | 15,841 | 222 | 0644 |
| `notes/RESEARCH_QUESTION.md` | `3cd1e22973e443c47a1672a82431c14c3b86ceba685330234d19085e65acdb5c` | 5,492 | 135 | 0644 |
| `notes/SOURCE_R1_ABSTRACT_INTEGER_REPAIR.md` | `f5bea1184027da2afe9c1cc6810c000b72fb058cc6cb527a30222866b521ef3b` | 8,168 | 136 | 0644 |
| `paper/PAPER_PLAN.md` | `fa7e5a7ea6693b0d8ef10651da317d253f5a1ba199e3b026a3b92c8104b6c974` | 44,881 | 799 | 0644 |
| `paper/main.tex` | `1ac57197ff87b2c1c6ec2cea7cf644021e629e519e4215d4b32e9e4420aa46b0` | 67,408 | 1,776 | 0644 |
| `paper/math_commands.tex` | `a69565204428ce95abbcab5afb3833290004110e2718c074fbc805f7d1bdcb0d` | 420 | 13 | 0644 |
| `paper/references.bib` | `ba0156abd7eb399de532b9bc1eefa81b3bb1be7868eed6ee4b42f8cd3371c782` | 2,812 | 99 | 0644 |
| `refine-logs/FINAL_PROPOSAL.md` | `aa1221ef198ed1fe8c21da2e24107efb5671cc0f4fb70a7cd657a21c73e1f47b` | 5,531 | 185 | 0644 |
| `refine-logs/INITIAL_PROPOSAL.md` | `485fd5b98e69338aae9a681548ac906e698d98adcd3af8dbf9e42622df9471b4` | 5,158 | 146 | 0644 |
| `refine-logs/REVIEW_SUMMARY.md` | `c02b85e92727134a2cd65789c4034bbef7c047811d3e03314c9e598e5a054bf3` | 4,395 | 101 | 0644 |

## 3. R0 blocker and repair custody

The blocker receipt has identity
`8d395e7fdeb2103370b1b1700c1bd54301f0f1206c5a3eea4352298cdd1c5384`,
8,900 bytes, 180 LF, mode 0644, and ends exactly `R0_BLOCKED`.  It records
successful command exit vectors but one fatal-to-the-gate hyperref warning:
the math shift in the old line-1560 subsection title was removed while
forming a PDF string.  The builder correctly persisted no success output.

The repair receipt has identity
`a0fe52acf07aed30dc8571b86a48602e74dc7cd15105ea4d69cd701f2e80bbe4`,
15,841 bytes, 222 LF, mode 0644, and its required repair-author terminal is
exact and unique.  The repaired line 1560 is exactly

```latex
\subsection{The restricted boundary at \texorpdfstring{\(g=9\)}{g=9}}
```

The old line is absent and the repaired line occurs once.  The old line is
47 bytes and the repaired line 69 bytes, excluding LF.  Thus this is the
sole changed line, a `+22`-byte, zero-LF change.  The repaired source is
`1ac57197ff87b2c1c6ec2cea7cf644021e629e519e4215d4b32e9e4420aa46b0`,
67,408 bytes, 1,776 LF, mode 0644.  Replacing only that repaired literal by
the old literal produces 67,386 bytes and SHA-256
`ec7c4be7195b7e0875a56e873a936629713bc5326e01ed5d5f4f6acf8a6d759c`;
the result equals the immutable root-A `main.tex` byte for byte.  The visible
heading and mathematics are unchanged, while the second argument supplies
plain bookmark text.  `hyperref` is loaded before the document body, so the
command is statically available at its use.

Both retained diagnostic roots remain immutable mode-0700 directories with
exactly 13 regular direct children and no directory, link, or other child:

| Root | Path | Inode | Inventory |
|---|---|---:|---:|
| A | `/tmp/paper23-r0-A.DyWKGR` | 10,422,234 | 13 / 0 / 0 / 0 |
| B | `/tmp/paper23-r0-B.dsQvTx` | 538,009,127 | 13 / 0 / 0 / 0 |

Each paired child has the same identity in A and B and still matches the
repair receipt:

| Relative child | SHA-256 | Bytes | LF | Mode |
|---|---|---:|---:|---:|
| `command-1.log` | `6d916d3f68e6a8ef6d1de37b39eea69859300a298efce6b8767713315c792112` | 18,265 | 601 | 0644 |
| `command-2.log` | `7b0a0a8d2f1749b44546479273ee9d474d9656cc2a276630ff83cc8a72044dc9` | 158 | 4 | 0644 |
| `command-3.log` | `2078f53209c7485ec4b3b417562a7ef7df6e2a2444ccc4109b1eca2e759a428a` | 8,504 | 162 | 0644 |
| `command-4.log` | `2c4df138d84bd55c6966f941398793ac05722cfd837ee096f285c6149ac20873` | 7,395 | 117 | 0644 |
| `main.aux` | `888b09e906d5784d4517a6541e066e321348b2db8860edf073ec3cc8f270fadc` | 14,049 | 165 | 0644 |
| `main.bbl` | `baa229dd7d35d96b27d7dfb18a844db73c98b752df3be4c008d748636f199cf9` | 2,881 | 73 | 0644 |
| `main.blg` | `be7e80a71c65ef8bbfcc2e43c3aadcc0b89cb8216e61a785ca24403ec6c04c34` | 900 | 46 | 0644 |
| `main.log` | `ae161baf177ac232b2fa313b6e2d3db7a38acee58dca30dd8005de2091c1976d` | 27,769 | 705 | 0644 |
| `main.out` | `14be6d78b541eb75e29cec5bf18d1e9a26bfb0c128ddaa5f4c26ab00d315bb94` | 6,226 | 28 | 0644 |
| `main.pdf` | `ae37679ef3ee4fa0b86f41e073f374920499f4959a196e289829e654b3d12d37` | 492,452 | 2,724 | 0644 |
| `main.tex` | `ec7c4be7195b7e0875a56e873a936629713bc5326e01ed5d5f4f6acf8a6d759c` | 67,386 | 1,776 | 0644 |
| `math_commands.tex` | `a69565204428ce95abbcab5afb3833290004110e2718c074fbc805f7d1bdcb0d` | 420 | 13 | 0644 |
| `references.bib` | `ba0156abd7eb399de532b9bc1eefa81b3bb1be7868eed6ee4b42f8cd3371c782` | 2,812 | 99 | 0644 |

The companion source hashes are unchanged.  No root or diagnostic file was
written or reused, and the historical PDF remains failed diagnostic evidence,
not an accepted project artifact.

## 4. Independent theorem and proof audit

### 4.1 Shears, supports, and matrices

For

\[
V=q_1^2q_2^2q_3^2q_4^2+q_1^g+q_2^{g-1},\qquad
W=p_1^2p_2^2p_3^2p_4^2+p_3^{g-1}+p_4^g,
\]

the eight derivative exponent supports are, in phase order,

\[
\begin{array}{c|c}
\partial_{q_1}V&(1,2,2,2),(g-1,0,0,0)\\
\partial_{q_2}V&(2,1,2,2),(0,g-2,0,0)\\
\partial_{q_3}V&(2,2,1,2)\\
\partial_{q_4}V&(2,2,2,1)\\
\partial_{p_1}W&(1,2,2,2)\\
\partial_{p_2}W&(2,1,2,2)\\
\partial_{p_3}W&(2,2,1,2),(0,0,g-2,0)\\
\partial_{p_4}W&(2,2,2,1),(0,0,0,g-1).
\end{array}
\]

The derivative coefficients are the stated positive integers.  The shear
inverses are obtained by subtracting the same gradients.  Their triangular
Jacobians have Hessian off-diagonal blocks, so Hessian symmetry gives
\(J^{\mathsf T}\Omega J=\Omega\) for each shear and hence for
\(F=T^+\circ S^+\).  No ordering of the characteristic-zero field is used.

Strictly choosing the two pure rows in each appropriate phase gives

\[
A=\begin{pmatrix}g-1&0&0&0\\0&g-2&0&0\\2&2&1&2\\2&2&2&1\end{pmatrix},
\quad
B=\begin{pmatrix}1&2&2&2\\2&1&2&2\\0&0&g-2&0\\0&0&0&g-1\end{pmatrix},
\]

and the phase order gives, by direct multiplication,

\[
C=BA=\begin{pmatrix}
g+7&2g+4&6&6\\
2g+6&g+6&6&6\\
2g-4&2g-4&g-2&2g-4\\
2g-2&2g-2&2g-2&g-1
\end{pmatrix}.
\]

### 4.2 Selectors, all six walls, and carries

Write \(u=u_1(1,x,y,z)^{\mathsf T}\),
\(a=(g-1)/(g-2)\), and \(H=(g-5)/2\).  The source cone

\[
u_1>0,\quad1\le x\le a,\quad1\le y\le z\le ay,\quad y+z<H
\]

contains the ordinary seed for every integer \(g\ge10\).  Literal
pure-minus-mixed subtraction gives exactly

\[
\Delta_{S,1}=g-2-2x-2y-2z,
\quad
\Delta_{S,2}=(g-3)x-2-2y-2z,
\]
\[
\Delta_{T,3}=-8-6x+(g-7)y+(2g-8)z,
\quad
\Delta_{T,4}=-6-4x+(2g-6)y+(g-6)z.
\]

The first two are positive from \(x\le a\), \(x\ge1\), and
\(y+z<H\).  For the last two, \(a\le9/8\) gives the respective strict
lower bounds \((12g-119)/4\) and \((6g-45)/2\).  Thus all four selectors
are strict on the whole cone, including its closed walls.

For \(Cu=u_1(D,N_2,N_3,N_4)^{\mathsf T}\), direct row subtraction gives
the six required target numerators:

\[
\begin{array}{c|l|l}
X'\ge1&N_2-D=(g-1)-(g-2)x&\ge0\\
X'<a&(g-1)D-(g-2)N_2&\ge2g+25>0\\
Y'>1&N_3-D=g-11-8x+(g-8)y+(2g-10)z&\ge4g-38>0\\
Z'>Y'&N_4-N_3=2+2x+gy-(g-3)z&>0\\
Z'\le aY'&(g-1)N_3-(g-2)N_4=(g-1)(g-2)(z-y)&\ge0\\
Y'+Z'<H&(g-5)D-2(N_3+N_4)&>3g^2-31g+26>0.
\end{array}
\]

For the last line the expanded numerator is
\(g^2-6g-23+(2g^2-14g-8)x-22y-20z\); using \(x,z\ge1\) and
\(y+z<H\) yields the displayed strict bound.  These identities prove
\(C\mathcal K_g\subseteq\mathcal K_g\) with exactly the weak/strict faces
stated in the source.

The base first carry is
\(A\mathbf1=(g-1,g-2,7,7)^{\mathsf T}>\mathbf1\).  Every entry of
\(C-I_4\) is positive for \(g\ge10\), so complete steps strictly outrun
the old \(q\)-coordinates.  For later first phases,
\(u_n-u_{n-1}=(C-I_4)u_{n-1}>0\), and nonnegative \(A\), with a positive
entry in each row, gives \(A(u_n-u_{n-1})>0\).  This closes both temporal
carries without conflating them with support selection.

Every forward coordinate begins in and remains in the nonnegative-integer
coefficient semiring: only positive-sign addition, multiplication, and the
positive derivative coefficients occur.  A selected leading monomial has a
positive integer coefficient; coincident products add rather than cancel.
The injection \(\mathbb Z\hookrightarrow K\) in characteristic zero keeps
that coefficient nonzero.  Hence the formal candidates are the actual
degree vectors

\[
u_n=C^n\mathbf1\quad(n\ge0),\qquad
v_n=AC^{n-1}\mathbf1\quad(n\ge1).
\]

### 4.3 Visibility and exact degree

The matrix \(C-A\) is entrywise positive.  The fourth complete-step row
minus the first three rows, evaluated at \((1,x,y,z)\), gives

\[
g-9-6x+(2g-8)y+(g-7)z,
\]
\[
-8+(g-8)x+(2g-8)y+(g-7)z,
\]
\[
2+2x+gy-(g-3)z.
\]

The cone bounds make these strictly positive; the third is the already
strict ordering wall.  Thus \(q_4\) beats the other three \(q\)-degrees,
and \(C-A>0\) then makes it beat all four final \(p\)-degrees.  This proves
unique seven-competitor visibility for every \(n\ge1\).  At \(n=0\) all
eight identity coordinates have degree one, and no strict claim is made.
Consequently the uniform exact identity is

\[
\deg(F_g^n)=e_4^{\mathsf T}C^n\mathbf1\qquad(n\ge0).
\]

### 4.4 Minors, determinant, quartic, recurrence, and Perron pairing

Direct determinant expansion gives the complete nontrivial principal-minor
ledger:

\[
\begin{array}{c|rrrrrr}
I&12&13&14&23&24&34\\\hline
\det C_I&-3g^2-7g+18&g^2-7g+10&g^2-6g+5&g^2-8g+12&g^2-7g+6&-3g^2+9g-6
\end{array}
\]

and

\[
\begin{array}{c|rrrr}
I&123&124&134&234\\\hline
\det C_I&-3g^3+23g^2-52g+36&-3g^3+20g^2-35g+18&-3g^3+12g^2-15g+6&-3g^3+15g^2-24g+12.
\end{array}
\]

Their sums are
\(e_1=4g+10\), \(e_2=-2g^2-26g+45\), and
\(e_3=-12g^3+70g^2-126g+72\).  Block expansion gives

\[
\det A=\det B=-3(g-1)(g-2),\qquad
\det C=9(g-1)^2(g-2)^2.
\]

Therefore

\[
R_g(t)=t^4-(4g+10)t^3+(-2g^2-26g+45)t^2
+(12g^3-70g^2+126g-72)t+9(g-1)^2(g-2)^2,
\]

and direct evaluation gives
\(R_g(1)=3g(g-1)(3g^2-11g+4)>0\).  Cayley--Hamilton, paired on the
left with \(e_4^{\mathsf T}\) and on the right with \(C^n\mathbf1\),
gives exactly

\[
\begin{aligned}
d_{n+4}={}&(4g+10)d_{n+3}+(2g^2+26g-45)d_{n+2}\\
&-(12g^3-70g^2+126g-72)d_{n+1}
-9(g-1)^2(g-2)^2d_n.
\end{aligned}
\]

All entries of \(C\) are positive.  Perron--Frobenius gives a simple
positive dominant root \(\rho\), and its positive left/right vectors pair
nontrivially with \(\mathbf1\) and \(e_4\).  Hence
\(e_4^{\mathsf T}C^n\mathbf1\sim c\rho^n\) with \(c>0\), proving
\(\lambda_1(F_g)=\rho(C)\), without an entropy claim.

### 4.5 Modulo five, boundary, and kernels

For \(g\equiv3\pmod5\), coefficient reduction is exactly

\[
f(t)=t^4-2t^3-t^2+1\in\mathbb F_5[t].
\]

Its values at \(0,1,2,3,4\) are \((1,4,2,4,3)\), so no linear factor
exists.  In a hypothetical monic quadratic factorization, coefficient
comparison gives
\(a+c=3\), \(ac+b+d=4\), \(ad+bc=0\), and \(bd=1\).  The four possible
ordered pairs \((b,d)=(1,1),(2,3),(3,2),(4,4)\) each contradict one of the
middle equations exactly as stated in the source.  Thus \(f\) is
irreducible.  Gauss's lemma and positivity make the parameters
\(g=13,18,23,\ldots\) an infinite quartic Perron subfamily.  Distinctness
follows because the \(t^3\) coefficient determines \(g\).

At \(g=9\), the selector margins are exactly \((1,0,-2,5)\), and the seed
also has \(y+z=H_9=2\).  The paper correctly restricts the conclusion to
failure of this seed and selected itinerary; it makes no global low-parameter
claim.

Finally, row reduction gives

\[
\ker(A+I_4)=\operatorname{span}(0,0,1,-1)^{\mathsf T},\qquad
\ker(B+I_4)=\operatorname{span}(1,-1,0,0)^{\mathsf T}.
\]

Their intersection is zero.  The nonzero determinants above independently
give \(\ker A=\ker B=\{0\}\).  These are the corrected frozen statements;
the manuscript does not repeat the immutable publication-review
transcription error.  The common-kernel lemma is correctly presented as an
elementary explanatory mechanism, not a novel classification or a
sufficient full-rank-to-quartic theorem.

## 5. Publication contract and static source audit

The title is exactly **Four-Mode Hamiltonian Product Shears Beyond Cubic
Collapse: Exact Degree Growth and Quartic Perron Subfamilies** in both source
and PDF-title metadata.  The visible/source author is exactly `Anonymous`,
the source date is empty, and the PDF author, creator, and producer fields
are empty.  Date/trailer suppression is present.  The public trio has no
private path, hash, lifecycle token, internal paper number, affiliation,
email, ORCID, acknowledgment, funding, or identity disclosure.

The abstract interior has 197 detex-visible words, lies in the locked
190--230 band, contains zero citations, and explicitly says that \(g\ge10\)
is an integer.  It includes the positive-sign family, four phase selectors,
exact visible matrix degree, quartic, residue-class Perron statement,
\(n\ge1\) visibility restriction, and \(n=0\) identity formula.

The article has exactly nine numbered sections in the locked order, nineteen
subsections, four enumerated introduction contributions, three permitted
hand-mathematical tables (supports, cone walls, principal minors), zero
figures, zero appendices, and no generated or empirical content.  Direct
detex of the current repaired source, with the macro input resolved, yields
6,647 tokens; the extra plain bookmark fallback is mathematically and
visibly inert.  Together with 67,408 source bytes and 1,776 LF, this is
credible proof-first mass for the locked 22--30-page band.  It is not a
compiled-page claim.

Comment-stripped static analysis independently found:

- 95 labels, all unique;
- 116 `ref`/`eqref` uses, all defined;
- nine citation commands using nine distinct keys;
- exactly the same nine distinct bibliography keys, with no uncited tenth
  record;
- balanced begin/end counts for every environment, including 72 `equation`,
  16 `aligned`, one `abstract`, one `document`, and three `table` pairs;
- 57 matched display-bracket pairs and 459 matched inline-math-parenthesis
  pairs;
- balanced nonescaped braces with no negative prefix and zero unescaped
  dollar delimiters;
- zero figure, appendix, algorithm, listing, minted, or `includegraphics`
  occurrence; and
- no source comment, TODO/TBD/FIXME/XXX, placeholder, unresolved `??`, or
  missing terminal `\end{document}`.

The nine exact citation keys are
`BlancVanSantenAffineTriangular`, `ShaoSunDimensionFour`,
`HenonOpenProblems`, `BergerTuraevHamiltonianMaps`,
`ForstnericComplexSymplectic`, `KochLomeliStraightLineFlows`,
`RangarajanPolynomialSymplectic`, `DesertiDegreeGrowthExamples`, and
`DangFavreSpectralInterpretations`.  The bibliography has eight `article`
records and the required one `misc` record.  Authors, ordering, diacritics,
titles, years, journals, volumes, issues, pages, arXiv version, and DOI
identities match the publication lock and scope, including the literal
collective S03 author, Hans Koch before Héctor E. Lomelí in S06, and the
corrected S04 and S07 version-of-record titles and S07 DOI.  DOI case
normalization does not change an identifier.  Citations remain bounded
context only and transfer no proof.

The article consistently limits itself to the displayed characteristic-zero,
integer-parameter, fixed positive-sign, fixed-support, fixed-order family.
It makes no arbitrary-sign/coefficient/support, positive-characteristic,
maximal-cone, global \(g=9\), all-parameter irreducibility/minimal-recurrence,
general full-rank-quartic, entropy, integrability, conjugacy, genericity,
minimal-dimension, optimal-sparsity, priority, firstness, or exhaustive
noncollision claim.  Its Paper-22 relationship is a bounded cubic-collapse
comparison; no predecessor theorem is republished as a new contribution.

## 6. Failure-atomic close and authority boundary

Before this report, throughout the audit, and immediately before its sole
write, all nine success-only project paths were absent:

1. `paper/BUILD_METADATA_R0.json`;
2. `paper/BUILD_RECEIPT_R0.json`;
3. `paper/main.aux`;
4. `paper/main.bbl`;
5. `paper/main.blg`;
6. `paper/main.log`;
7. `paper/main.out`;
8. `paper/main.pdf`; and
9. `paper/main_round0.pdf`.

No build was attempted.  All twenty-six opening files, all three roots, and
both diagnostic roots were rechecked stable immediately before this report.
Creation of this one regular file changes only the project count, from
26/4/0/0 to 27/4/0/0.  It authorizes no source mutation, compilation,
successful R0 persistence, rebuild, revision, release, Paper 24 action,
submission, upload, transport, messaging, identity disclosure, or other
external effect.  Any eligibility for the second independent repaired-source
review is a separate parent-governance decision.

Every conjunctive obligation is satisfied.

PAPER_SOURCE_R1_R0_REPAIR_PASS
