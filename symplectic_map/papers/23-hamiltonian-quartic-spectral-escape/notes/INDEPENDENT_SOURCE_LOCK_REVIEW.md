# Paper 23 — Fresh Independent Source-Lock Review

## 1. Reviewer identity, scope, and verdict

- Review date: 2026-08-24 UTC.
- Project: `papers/23-hamiltonian-quartic-spectral-escape`.
- Candidate ID: `hamiltonian_quartic_spectral_escape_v1`.
- Title: **Four-Mode Hamiltonian Product Shears Beyond Cubic Collapse:
  Exact Degree Growth and Quartic Perron Subfamilies**.
- Role: fresh independent source-lock reviewer. I authored none of the ten
  source-design files, their independent source-design review, candidate R1,
  the immutable R1 correction, candidate R2, the source lock, or either root
  governance record.
- Authorized write universe: this file only, and only after every
  conjunctive check passed.

I read the complete local `research-review/SKILL.md` and
`proof-writer/SKILL.md` instructions before reviewing. I then read the lock,
all ten allowlisted author files, the independent source-design review, all
three candidate records, and both current root governance records through
EOF. The proof was attacked independently rather than accepted from the
author or previous reviewer.

No network lookup, literature refresh, CAS or symbolic-algebra certificate,
finite parameter or modulus scan, numerical spectrum, scientific experiment,
code or data artifact, TeX build, PDF action, Paper 24 work, root-ledger edit,
or external effect was performed. Inline read-only Python and Node programs
were used only for byte identities, strict JSON parsing, canonical encoding,
inventory checks, and deterministic reconstruction of historical governance
bytes; no persistent validation scratch was created.

**Verdict: PASS.** The lock is strict-canonical and internally complete; its
bound files, aggregates, excluded provenance, historical governance state,
mathematics, citation depths, predecessor ownership, typography repair lock,
anti-claims, zero-science counters, inventory, and permissions all survive
fresh review. No blocker remains at this gate.

## 2. Stable lock identity and self exclusion

The reviewed lock is exactly:

| Property | Recomputed value |
|---|---|
| path | `experiments/source_lock.json` |
| SHA-256 | `5956a7e6c2e12a9be287b2ead2922e135c4a64da738757a0b55884e16974b248` |
| bytes | 32,889 |
| LF | 1 |
| mode | `0644` |
| schema | `paper23.source_lock.v1` |
| `status` | `SOURCE_LOCK_AUTHOR_STOP / PENDING_FRESH_SOURCE_LOCK_REVIEW` |
| `lock_status` | `SOURCE_LOCK_AUTHOR_STOP / PENDING_FRESH_SOURCE_LOCK_REVIEW` |

The file is one physical UTF-8 JSON line followed by exactly one terminal LF.
It has no UTF-8 BOM, CR byte, NUL byte, duplicate key, nonfinite number,
noninteger JSON number, trailing record, or symlink substitution. The self
object binds path `experiments/source_lock.json`, sets `self_excluded` to
true, and sets both `sha256` and `bytes` to JSON null. Thus the lock does not
pretend to solve an impossible digest/size self-reference; the final identity
above is supplied externally by this review.

## 3. Two independent strict-canonical implementations

I validated the stable bytes with two separately written implementations.

1. A duplicate-aware CPython parser used an object-pairs hook to reject a
   repeated key, rejected nonfinite constants and every floating-point token,
   decoded UTF-8 strictly, and serialized recursively sorted objects with
   compact separators and literal Unicode.
2. A handwritten Node recursive-descent parser independently implemented
   objects, arrays, strings and escapes, integer-only numbers, literals,
   duplicate-key rejection, safe trailing-input rejection, and a separate
   recursive encoder whose key comparator uses Unicode code points.

Each implementation reproduced the complete 32,889-byte lock byte for byte,
including its sole terminal LF. Both independently enforced recursive key
order, compact separators, declared array order, integer-only JSON numbers,
UTF-8, and the one-record framing rule.

Each implementation also rejected all ten adversarial classes separately:

1. duplicate root key;
2. duplicate nested key;
3. `NaN`;
4. `Infinity`;
5. negative infinity;
6. UTF-8 BOM;
7. CR byte;
8. NUL byte;
9. missing terminal LF; and
10. trailing non-whitespace or a second physical record.

No parser accepted a malformed case, and neither canonical encoder relied on
the other's parse tree or output.

## 4. Twice-recomputed author universe and aggregates

Both the CPython implementation and the independent Node implementation used
no-follow filesystem metadata and independently recomputed every allowlisted
file's SHA-256, byte count, LF count, mode, UTF-8 validity, terminal newline,
BOM/CR/NUL state, and regular-file/non-symlink type.

| Relative author path | SHA-256 | Bytes | LF |
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

All ten are mode `0644`, strict UTF-8, LF-only, terminal-LF regular files
with no BOM, CR, NUL, or link. Their totals are exactly 75,446 bytes and
2,311 LF.

For byte-sorted relative POSIX names, I independently regenerated the textual
records

`SHA-256 bytes LF relative-path LF`.

Both implementations obtained exactly 1,038 ledger bytes and SHA-256
`37a3f9ca95f1fa0312f40263d4825b27467d74eace5d81584831b8e2b7e959fc`.

I also independently regenerated the binary stream

`uint64_be(name-byte-length) || name-UTF8 || uint64_be(content-byte-length) || content`.

Both implementations obtained exactly 75,894 framed bytes and SHA-256
`e5e6e56ffeb42675d8eb2b38a96cbc70dbbc202f32e1301174a97f74a524b5d6`.
The independent source-design review, candidate records, source lock, and
this review are correctly excluded from that ten-file author aggregate.

## 5. Excluded review and candidate provenance

The excluded source-design review and all candidate records were rehashed
twice and read in full:

| Record | SHA-256 | Bytes | LF | Exact terminal |
|---|---|---:|---:|---|
| `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md` | `c6ae173c45d0e8fbe073395abf366a33e3f4b24bf97c1ab97ad39cdb245e356e` | 17,851 | 441 | `SOURCE_DESIGN_PASS` |
| `BATCH_06_PAPER23_CANDIDATE_REVIEW_R1.md` | `a3c9815c2d851c8791a259c4e46a4d33663f06e6ab4faa58a981f89f7ebf3ae7` | 21,915 | 394 | `PAPER23_CANDIDATE_GATE_PASS_R1` |
| `BATCH_06_PAPER23_CANDIDATE_REVIEW_R1_CORRECTION.md` | `2a1278ff35eeeaf7af2f63010c8ad0f10d745cc763a8379d3a833695897f3783` | 9,407 | 231 | `PAPER23_CANDIDATE_GATE_PASS_R1_CORRECTED` |
| `BATCH_06_PAPER23_CANDIDATE_REVIEW_R2.md` | `cb5b3e748fe4cc5b26f51e2b1b4ca7f93ea2e1011a0c4f2f99e47dc6884d5ed8` | 16,028 | 596 | `PAPER23_CANDIDATE_GATE_PASS_R2` |

The immutable R1 correction controls only where original R1 printed a minus
sign or suggested sign invariance. The accepted theorem has addition in both
forward shears, exact order $F_g=T_g^+\circ S_g^+$, positive-integer
coefficient survival, and characteristic-zero scope. R2 and the source-design
PASS agree with that corrected object. R1's bounded scores remain
7.8/8.3/9.1, while R2's proof/standalone scores remain 9.4/8.4 with no public
novelty score.

## 6. Historical governance binding versus the review-opening transition

The lock correctly binds the root records that existed at source-lock
authoring stop, not the later parent transition that legally opened this
review. I verified both states without changing either root file.

### Current review-opening state

| Root record | Current SHA-256 | Bytes | LF | Current fact |
|---|---|---:|---:|---|
| `BATCH_06_STATUS.md` | `5def86250fde8c5fbfbe8aa6a89004c0bd46f6254180d3d11f9f4f2fb7225c17` | 55,499 | 834 | gate `PAPER23_SOURCE_LOCK_REVIEW_OPEN`; queue `SOURCE_LOCK_AUTHOR_STOP_PENDING_INDEPENDENT_REVIEW` |
| `BATCH_06_IDEA_REPORT.md` | `1f44909ed6f773b4481b742461fc06600f1e08aa18bb573a1d40d1e96139c072` | 81,736 | 1,646 | append-only source-lock author-stop addendum present |

### Deterministic in-memory reconstruction of the bound authoring state

For the status record I removed only the final activity bullet beginning
`- 2026-08-24: A distinct Paper 23 source-lock author`, restored the current
gate to `PAPER23_SOURCE_LOCK_AUTHORING_OPEN`, and restored the Paper 23 queue
row to “independent source-design review passed; canonical source-lock
authoring only” with status
`SOURCE_DESIGN_PASS_SOURCE_LOCK_AUTHORING_OPEN`. The resulting bytes are
exactly SHA-256
`6aab90bed0fede73a48efde25dcd4d0a8b17945d9c4b06563502c2d14d6ac532`,
53,777 bytes, and 810 LF.

For the idea report I removed only the separating blank line and final
`## Addendum — Paper 23 Source-Lock Author Stop` section. The resulting bytes
are exactly SHA-256
`b77bebfc70bcb9e520ac35cb9d950df904a174aca849d0edc90ad7cd85ead66d`,
78,766 bytes, and 1,595 LF.

Thus the two identities stored in `governance_bindings` are exact historical
bindings. The newer identities are a valid parent-controlled review-opening
transition, not author-file drift and not a failure of the lock. This reviewer
made no root-governance mutation.

## 7. Positive shears, inverses, and literal support rows

For

$$
S_g^+(q,p)=(q,p+\nabla V_g(q)),\qquad
T_g^+(q,p)=(q+\nabla W_g(p),p),
$$

the subtraction shears are two-sided polynomial inverses. If $H_V$ and
$H_W$ are the two Hessians, their Jacobians are

$$
\begin{pmatrix}I&0\\H_V&I\end{pmatrix},\qquad
\begin{pmatrix}I&H_W\\0&I\end{pmatrix}.
$$

Hessian symmetry makes direct multiplication against
$\left(\begin{smallmatrix}0&I\\-I&0\end{smallmatrix}\right)$ return the same
symplectic matrix. Hence both positive forward shears and their composition
are polynomial symplectic automorphisms. The subtraction formulas certify
inversion and do not enlarge the theorem family.

Literal differentiation gives exactly these eight support rows:

| Gradient row | Exponent supports |
|---|---|
| $\partial_{q_1}V_g$ | $(1,2,2,2)$ and $(g-1,0,0,0)$ |
| $\partial_{q_2}V_g$ | $(2,1,2,2)$ and $(0,g-2,0,0)$ |
| $\partial_{q_3}V_g$ | $(2,2,1,2)$ |
| $\partial_{q_4}V_g$ | $(2,2,2,1)$ |
| $\partial_{p_1}W_g$ | $(1,2,2,2)$ |
| $\partial_{p_2}W_g$ | $(2,1,2,2)$ |
| $\partial_{p_3}W_g$ | $(2,2,1,2)$ and $(0,0,g-2,0)$ |
| $\partial_{p_4}W_g$ | $(2,2,2,1)$ and $(0,0,0,g-1)$ |

Thus exactly four rows are competitive. Selecting the pure row in those four
positions gives

$$
A_g=\begin{pmatrix}
g-1&0&0&0\\0&g-2&0&0\\2&2&1&2\\2&2&2&1
\end{pmatrix},\qquad
B_g=\begin{pmatrix}
1&2&2&2\\2&1&2&2\\0&0&g-2&0\\0&0&0&g-1
\end{pmatrix}.
$$

Because $S_g^+$ acts first, the full matrix is $C_g=B_gA_g$. Independent
row-by-column multiplication gives

$$
C_g=\begin{pmatrix}
g+7&2g+4&6&6\\
2g+6&g+6&6&6\\
2g-4&2g-4&g-2&2g-4\\
2g-2&2g-2&2g-2&g-1
\end{pmatrix}.
$$

The seed vectors are
$A_g\mathbf1=(g-1,g-2,7,7)^{\mathsf T}$ and
$C_g\mathbf1=(3g+23,3g+24,7g-14,7g-7)^{\mathsf T}$.

## 8. Four selectors and the complete simple-ratio cone audit

Normalize $u=u_1(1,x,y,z)^{\mathsf T}$, put
$a_g=(g-1)/(g-2)$ and $H_g=(g-5)/2$, and impose

$$
1\le x\le a_g,\qquad 1\le y\le z\le a_gy,\qquad y+z<H_g.
$$

The two $S$ gaps and the two $T$ gaps, with the latter evaluated at
$v=A_gu$, independently reduce to

$$
\begin{aligned}
\Delta_{S,1}&=(g-2)-2x-2y-2z,\\
\Delta_{S,2}&=(g-3)x-2-2y-2z,\\
\Delta_{T,3}&=-8-6x+(g-7)y+(2g-8)z,\\
\Delta_{T,4}&=-6-4x+(2g-6)y+(g-6)z.
\end{aligned}
$$

For $g\ge10$, the first gap is strictly larger than
$(g-4)/(g-2)$, the second is strictly larger than zero, and $a_g\le9/8$
gives respective lower bounds $(12g-119)/4>0$ and
$(6g-45)/2>0$ for the final two. At the ordinary seed the four exact margins
are $(g-8,g-9,3g-29,3g-22)$, so the seed lies in the cone and all selectors
are strict for every integer $g\ge10$.

Write

$$
C_gu=u_1(D,N_2,N_3,N_4)^{\mathsf T}
$$

with

$$
\begin{aligned}
D&=g+7+(2g+4)x+6y+6z,\\
N_2&=2g+6+(g+6)x+6y+6z,\\
N_3&=2g-4+(2g-4)x+(g-2)y+(2g-4)z,\\
N_4&=2g-2+(2g-2)x+(2g-2)y+(g-1)z.
\end{aligned}
$$

All denominators are positive. Every target face survives independently:

1. $N_2-D=(g-1)-(g-2)x\ge0$.
2. $(g-1)D-(g-2)N_2$
   equals
   $-g^2+4g+5+(g^2-2g+8)x+6(y+z)\ge2g+25>0$.
3. $N_3-D=g-11-8x+(g-8)y+(2g-10)z$
   is at least $4g-29-8a_g\ge2>0$.
4. $N_4-N_3=2+2x+gy-(g-3)z$
   is at least $2+2x+((2g-3)/(g-2))y>0$.
5. $(g-1)N_3-(g-2)N_4=(g-1)(g-2)(z-y)\ge0$.
6. The height numerator is
   $$
   \begin{aligned}
   E_H&=(g-5)D-2(N_3+N_4)\\
      &=g^2-6g-23+(2g^2-14g-8)x-22y-20z.
   \end{aligned}
   $$
   Its $x$ coefficient is positive for $g\ge10$. Using $x\ge1$,
   $y+z<H_g$, and $z\ge1$ gives
   $$
   E_H>3g^2-31g+26=16+(g-10)(3g-1)>0.
   $$

Consequently the six required walls return in the exact closed or strict
direction, and $C_g\mathcal K_g\subseteq\mathcal K_g$. This is one explicit
sufficient cone, not a maximal, necessary, unique, or classified cone.

## 9. Temporal carry, leading forms, and visibility

The selector inequalities do not by themselves prove temporal carry. The
base first-phase inequality is $A_g\mathbf1>\mathbf1$. Every entry of
$C_g-I_4$ is positive for $g\ge10$, so the new second-phase rows beat the
carried $q$ rows. Inductively,

$$
u_n-u_{n-1}=(C_g-I_4)u_{n-1}>0.
$$

Since $A_g$ is nonnegative with a positive entry in every row,
$A_g(u_n-u_{n-1})>0$; this separately proves later first-phase carry. The
same $(C_g-I_4)u_n>0$ proves later second-phase carry. The phase labels close
as

$$
u_n=C_g^n\mathbf1\quad(n\ge0),\qquad
v_n=A_gC_g^{n-1}\mathbf1\quad(n\ge1).
$$

All starting coefficients and all frozen gradient coefficients are
nonnegative integers, and each forward operation uses addition and
multiplication only. Contributions to an equal monomial therefore add to a
positive integer rather than cancel. Characteristic zero keeps each positive
integer nonzero in $K$. This establishes actual polynomial degrees; it is not
a sign-invariance argument and gives no arbitrary-coefficient or
positive-characteristic extension.

The matrix $C_g-A_g$ is entrywise positive. Thus each complete $q_i$ degree
beats the corresponding final $p_i$ degree. The fourth complete row also
beats the other three complete rows because its normalized differences are

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

Chaining these comparisons checks $q_4$ against all seven other coordinates.
It is uniquely visible for every $n\ge1$; at $n=0$ all eight degrees tie at
one. Hence, including the tied identity case,

$$
\deg(F_g^n)=e_4^{\mathsf T}C_g^n\mathbf1\qquad(n\ge0).
$$

## 10. Ten principal minors, quartic, recurrence, and Perron visibility

I expanded every principal minor by hand. The six order-two minors are:

| Indices | Determinant |
|---|---:|
| 12 | $-3g^2-7g+18$ |
| 13 | $g^2-7g+10$ |
| 14 | $g^2-6g+5$ |
| 23 | $g^2-8g+12$ |
| 24 | $g^2-7g+6$ |
| 34 | $-3g^2+9g-6$ |

Their sum is $-2g^2-26g+45$. The four order-three minors are:

| Indices | Determinant |
|---|---:|
| 123 | $-3g^3+23g^2-52g+36$ |
| 124 | $-3g^3+20g^2-35g+18$ |
| 134 | $-3g^3+12g^2-15g+6$ |
| 234 | $-3g^3+15g^2-24g+12$ |

Their sum is $-12g^3+70g^2-126g+72$. The trace is $4g+10$.
Block triangularity gives

$$
\det A_g=\det B_g=-3(g-1)(g-2),\qquad
\det C_g=9(g-1)^2(g-2)^2.
$$

The principal-minor signs therefore give exactly

$$
\begin{aligned}
R_g(t)={}&t^4-(4g+10)t^3+(-2g^2-26g+45)t^2\\
&+(12g^3-70g^2+126g-72)t
+9(g-1)^2(g-2)^2.
\end{aligned}
$$

The linear coefficient factors as
$2(g-3)(2g-3)(3g-4)$, and direct substitution gives

$$
R_g(1)=3g(g-1)(3g^2-11g+4)>0
$$

for $g\ge10$. Applying Cayley--Hamilton to the visible scalar sequence
$d_n=e_4^{\mathsf T}C_g^n\mathbf1$ gives the sign-correct recurrence

$$
\begin{aligned}
d_{n+4}={}&(4g+10)d_{n+3}+(2g^2+26g-45)d_{n+2}\\
&-(12g^3-70g^2+126g-72)d_{n+1}\\
&-9(g-1)^2(g-2)^2d_n.
\end{aligned}
$$

Every entry of $C_g$ is positive for $g\ge10$, so it is primitive. Its left
and right Perron vectors pair positively with $e_4^{\mathsf T}$ and
$\mathbf1$. Perron--Frobenius asymptotics therefore give
$d_n^{1/n}\to\rho(C_g)$ and
$\lambda_1(F_g)=\rho(C_g)$. No entropy statement follows.

## 11. The $g=9$ boundary and uniform modulo-five certificate

At $g=9$, the four seed margins are exactly $(1,0,-2,5)$ and the cone height
is tied at $y+z=2=(g-5)/2$. Thus the second $S$ selector ties and the third
$T$ pure branch loses. The theorem correctly claims sharpness only for this
seed and selected itinerary, not impossibility of every different regime.

For $g\equiv3\pmod5$, coefficient reduction is uniformly

$$
f(t)=t^4-2t^3-t^2+1.
$$

Its values at $0,1,2,3,4$ are $(1,4,2,4,3)$, so it has no linear factor.
If

$$
f=(t^2+at+b)(t^2+ct+d),
$$

then $a+c=3$, $ac+b+d=4$, $ad+bc=0$, and $bd=1$. The only constant pairs
are $(1,1),(2,3),(3,2),(4,4)$. The equal pairs make
$ad+bc=b(a+c)\ne0$; either middle pair forces $a=c=4$ and then
$ac+b+d=1\ne4$. Thus no quadratic factor exists. Reduction modulo five and
Gauss's lemma prove $R_g$ irreducible over $\mathbb Q$.

For $g=13,18,23,\ldots$, the primitive-matrix Perron root is consequently an
algebraic integer of degree four and all its other conjugates have smaller
modulus. The roots are pairwise distinct: equality for two parameters would
force equality of their monic irreducible polynomials, but the $t^3$
coefficient $-(4g+10)$ recovers $g$.

## 12. Support-kernel explanation and its nonnovel scope

For

$$
A=-I_r+\sum_{i=1}^p u_iv_i^{\mathsf T},\qquad
B=-I_r+\sum_{j=1}^q s_jt_j^{\mathsf T},
$$

a vector annihilated by every $v_i^{\mathsf T}$ and $t_j^{\mathsf T}$
satisfies $Ax=Bx=-x$ and therefore $BAx=x$. Rank--nullity gives dimension at
least $r-p-q$ for that common kernel. This is a general explanatory
obstruction, not a classification or sufficient quartic criterion.

For this family,

$$
\ker(A_g+I)=\operatorname{span}(0,0,1,-1)^{\mathsf T},\qquad
\ker(B_g+I)=\operatorname{span}(1,-1,0,0)^{\mathsf T}.
$$

Their intersection is zero, and the combined covectors
$e_1^{\mathsf T},e_2^{\mathsf T},\mathbf1^{\mathsf T},e_3^{\mathsf T},e_4^{\mathsf T}$
span the full dual space. The independent $R_g(1)\ne0$ check excludes an
unrelated unit eigenvalue. This explains escape from Paper 22's unit sector;
it does not replace any selector, carry, visibility, spectral, or modular
proof and is not a Paper 23 novelty claim.

## 13. Citations, collision boundary, typography, and anti-claims

The citation lock preserves the R1 cutoff 2026-08-24 and exact 24-query
bounded screen. Access remains limited as recorded: S01/S02 are
abstract/authoritative-metadata records; S03 is relevant authoritative HTML;
S04 is abstract plus institutional/publisher metadata; S05 is author-hosted
full text with relevant passages inspected; S06 is available full text with
the abstract and relevant passages inspected; S07/S08 are abstract plus the
stated metadata; and S09 remains only a bibliographic pointer from an
inspected authoritative survey. A locator in the lock does not elevate S09's
access or authorize a theorem/noncollision inference. A future authorized
publication stage must reverify current metadata and exact author lists.

No external citation transfers a selector, cone wall, carry, no-cancellation,
visibility, minor, recurrence, or modular proof. The only allowed novelty
position remains that the bounded screen found no direct collision with the
complete corrected package; it is not exhaustive and grants no firstness or
priority.

Internal ownership is also preserved:

- Paper 20 owns the two-mode selector/matrix/Perron architecture;
- Paper 21 owns the three-mode cone, carry, visibility, cubic, and modular
  subfamily proof grammar; and
- Paper 22 owns the arbitrary-mode endpoint-spike common-unit-sector cubic
  collapse.

Paper 23 is limited to the explicit four-spike escape, its visible quartic
matrix, and the certified irreducible residue-class subfamily.

Exactly two frozen author displays contain the literal typography defect
`\mathcal K_g=left\{`: one in `notes/PROOF_PACKAGE.md` and one in
`refine-logs/FINAL_PROPOSAL.md`. Their mathematics is unambiguous and the
frozen author bytes remain immutable. Any later authorized manuscript must
render `\mathcal K_g=\left\{`; propagation of the defect is a STOP condition.

The lock consistently rejects validity for $g\le9$, global threshold
optimality, maximal or classified cones, subtraction/arbitrary signs or
coefficients, reversed phase order, added support, positive characteristic,
quartic irreducibility for every $g$, every-full-rank-profile implications,
novelty of reused machinery, general Perron realization, minimality,
sparsity, conjugacy, genericity, integrability, entropy, periodic-point or
unrelated arithmetic claims, computational proof, and absolute priority.
The credible article allocation remains approximately 24--28 content pages
inside the hard 22--30 band, with every theorem-critical proof local.

## 14. Inventory, zero-science state, and permission closure

Immediately before this review file existed, a no-follow recursive audit
found exactly:

- 12 regular files;
- the three child directories `experiments`, `notes`, and `refine-logs`;
- zero symlinks;
- zero other objects; and
- an absent `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md`.

That regular-file list matches `inventory_lock.regular_files_after_lock`
exactly. All forbidden directories `build`, `code`, `data`, `figures`,
`manuscript`, `paper`, `publication`, `release`, `results`, `submission`, and
`transport` are absent. No TeX, BibTeX, bibliography, PDF, compiled output,
code, data, result, upload, release, submission, transport, or external-action
artifact exists in the project.

The scientific counters consistently remain zero: no build, CAS run,
metadata refresh, code file, dataset, figure, GPU run, modulus or parameter
sweep, network call, numerical run, scientific run, or upload occurred. The
two `experiments` filenames are repository-convention proof-verification
ledgers, not empirical evidence.

The lock authorizes only this fresh source-lock review. It does not authorize
paper-plan creation directly by this reviewer, publication-stage governance,
manuscript, bibliography, build, transport, release, Paper 24, root-ledger
mutation, submission, upload, messaging, identity disclosure, repository
push, or any external effect. Any blocker would have required zero writes;
because every conjunctive check passed, this is the sole permitted artifact.

Its creation changes only the project count from 12 to 13 regular files while
retaining exactly three child directories and zero links or other objects.
No pre-existing project or root byte was modified.

SOURCE_LOCK_PASS
