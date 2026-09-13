# Independent Source-Design Review

## Review identity and authority

This is the fresh independent review of the Paper 15 source-design package
at

`papers/15-henon-quartic-trace-fibers`.

The reviewer did not author any of the ten bound source-design files. Before
the explicit `AUTHOR STOP`, the reviewer did not open, list, stat, or inventory
this project root. After the stop, the reviewer was authorized to read exactly
the ten files listed below and, only if every gate passed, to create this one
review artifact.

No code, CAS, symbolic engine, parameter scan, periodic-point enumeration,
finite-field check, manuscript build, or scientific execution was used. The
mathematical replay was performed from the displayed definitions, exact
finite recurrences, frozen Paper 12 proof, and primary sources.

## Bound snapshot

The pre-review snapshot was rehashed before reading. All ten identities and
byte counts matched the author's stable handoff:

| Path | SHA-256 | Bytes |
|---|---|---:|
| `experiments/EXPERIMENT_PLAN.md` | `c30436a0389c88df8f51fe6e226347bfe108aa84b5032841ec0033ffa7a987fb` | 8354 |
| `experiments/EXPERIMENT_TRACKER.md` | `d0e46a2c9a691c33e6f6e523f85367f00e8060c124044e2f011016c0a68f9efb` | 2955 |
| `notes/CITATION_VERIFICATION.md` | `d84f4b523a7fee3e8f5fa8f2c4c898dbf62e3fd9528154fdd991d82c150c3609` | 13630 |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | `928f0923bbfddd9294508a427bfcbcbd259591cac4c136bd4effb15bd86ed109` | 9343 |
| `notes/NOVELTY_ASSESSMENT.md` | `c0b7a102d0d63dcb71d58bdbe460e59988fbf303a10f540a0221275fd34c5eb2` | 9878 |
| `notes/PROOF_PACKAGE.md` | `f99d14bc18bd160e5d55e6254e4a2957dda40adbc2a680970506a6ecca5a42ed` | 29436 |
| `notes/RESEARCH_QUESTION.md` | `a287da2bebfa89b02dd7a83d13129e442b51d5780ccbc01c90eca93ad169e082` | 8641 |
| `refine-logs/FINAL_PROPOSAL.md` | `97daded29a79a1b19b828c4704187fa9c70bdac7448382a72b1df8c0f773ab21` | 9331 |
| `refine-logs/INITIAL_PROPOSAL.md` | `043ca69894386ab5040099138780cc6801ba39ff0b088a2ba3f274ef263cb1a0` | 4842 |
| `refine-logs/REVIEW_SUMMARY.md` | `ab479b99e6fbf1b8f66b719df01d8abfbc97da30a8feb1c0fb1b77bab16ac0bb` | 7112 |

The pre-review inventory was exactly 10 regular files, 3 subdirectories, 0
symlinks, 103522 bytes, and 3576 lines. There was no source lock, code,
result, figure, paper directory, or manuscript.

## Binary verdict and scores

The strengthened, unified three-theorem package passes all frozen gates.
The naked statement (P_{\mathcal H^1}(4)=3) remains a standalone-size
failure and is not what is certified here.

| Dimension | Frozen threshold | Independent score | Verdict |
|---|---:|---:|---|
| theorem novelty | 6.5 | **6.8/10** | PASS |
| standalone size | 6.0 | **6.4/10** | PASS |
| proof confidence | 9.0 | **9.3/10** | PASS |

The novelty score is deliberately conservative because Cantat--Dujardin
already supply the general rigidity theorem, an unspecified finite cutoff,
the exceptional quartic family, and its period-one/two blindness. The
residual contribution that clears the gate is the combined pure-trace
Jacobian lemma, exact lower non-quasi-finite locus, and global sharp quartic
cutoff. A bounded search through 2026-08-17 found no indexed primary source
stating this unified result; that is not a priority or universal-absence
claim.

## P1--P17 conjunctive audit

| Gate | Independent finding | Status |
|---|---|---|
| P1 scope and trace convention | Part A is algebraically closed characteristic zero; Parts B--C are over \(\mathbb C\); the source is single-factor \(\mathcal H^1_4\); formal cycles and symmetric products are used; no injectivity claim appears. | PASS |
| P2 fixed algebra | The fixed equations give \(s=1-a\), \(q=p-sx\), \(A_q=k[x]/(q)\), and the derivative trace is \(p'\). Thus pure \(\operatorname{Trace}_1\) determines \(C_f(T)=\det(T-M_{p'})\). | PASS |
| P3 derivative identity | Both the squarefree residue argument and the nonreduced local-factor argument prove \(C_f'(s)=0\). No division by \(C_f(s)\) occurs in the nonreduced case. | PASS |
| P4 candidate count | In characteristic zero, \(C_f'\) has degree \(d-1\). Since \(J=-a=s-1\), there are at most \(d-1\) Jacobians and at most 3 in degree four. | PASS |
| P5 Cantat--Dujardin scope | The May 10, 2026 author PDF was opened and checked. Theorem 4.2 is used only over \(\mathbb C\), with fixed Jacobian, for \(a\ne1\), after P4. Theorem 3.7 supplies no explicit \(P(4)\). | PASS |
| P6 formal period two | On \(a=1\), \(A_2=A_1\otimes A_1\) has length 16 and trace element \(2+p'(x)p'(y)\). Removing the length-4 formal fixed cycle leaves a formal length-12 multiset determined by \(\operatorname{Trace}_1\), including nonreduced multiplicity. | PASS |
| P7 \([1111]\) | For \(h=x+p\), simple roots give multipliers \(1+p'(\alpha)\ne1\), so Sugiyama's \(V_4\) theorem applies. Sugiyama is not used on a singular stratum. | PASS |
| P8 singular partitions | The formulas for \([31]\) and \([211]\), including ordering choices and finite recovery, were rederived directly. | PASS |
| P9 boundaries and \(E\) | Every boundary lands in \([31]\), \([22]\), or \([4]\); \([22]\cup[4]\) is exactly \(p=(x^2-L)^2\); fixed trace \(0^4\) has no other centered quartic. | PASS |
| P10 lower bad locus | All lower fibers outside \(E\) are finite; every point of \(E\) lies on the positive-dimensional fiber \((0^4,2^{12})\). Hence the exact non-quasi-finite locus is \(E\). | PASS |
| P11 period-three intersection | The cyclic signs, determinant, derivative trace, rank 64, and exponent \(\operatorname{Tr}(M_{t^2})=\operatorname{Res}(t^3)\) were checked. | PASS |
| P12 two-term support | The weight equation gives four initial monomials; the separated algebra removes \(L^9\), and the two possible nonfixed Puiseux cluster types plus the diagonal branch remove \(L^6\varepsilon^2\). | PASS |
| P13 coefficient ledgers | The finite \(H/A\) certificate, all displayed \(\rho\) and \(\mu\) values, \(\mathcal C_{2,0}=-6\), the recurrence table, and all six constant contributions were replayed without CAS. Both routes give \(D_2=-1572864\), and the constant is \(C_2=-1296000\). | PASS |
| P14 subtraction and length | On the fixed algebra \(q^2=0\), hence \(t_\varepsilon^2=0\). Formal elimination gives local order \(r\) for \(r=2,4\), leaving no residual fixed support. The formal pointwise length is 60, and division by 3 occurs only afterwards. | PASS |
| P15 quotient and quasi-finiteness | The action is \(L\mapsto\zeta L\), with invariant \(L^3\). Full \(\operatorname{Trace}_3\) equality forces second-moment equality and hence finite \(L\)-fibers. Finite geometric fibers plus finite type give quasi-finiteness; the quotient argument is valid. | PASS |
| P16 citations and collision search | Controlling primary records were reopened; theorem roles and field scopes match the ledger. No direct collision was found in the repeated bounded search. Classical residue and formal-cycle methods receive no novelty credit. | PASS |
| P17 publication and anti-claims | Paper 15 absorbs and supersedes the overlapping Paper 12 external-paper route. Parallel overlapping submission is forbidden. No global injectivity, exact degree, all-degree cutoff, composition, positive-characteristic, or one-moment-global-classification claim appears. | PASS |

## Independent mathematical replay

### A. Pure fixed trace really controls finitely many Jacobians

For

\[
f_{a,p}(x,y)=(ay+p(x),x),\qquad s=1-a,\qquad q=p-sx,
\]

the fixed algebra is (A_q=k[x]/(q)), and (p'=q'+s). If (q) is
squarefree, then

\[
\frac{C_f'(s)}{C_f(s)}
=-\sum_{q(\alpha)=0}\frac1{q'(\alpha)}=0.
\]

The last equality follows by comparing the (x^{d-1})-coefficient in the
Lagrange interpolation identity for the constant polynomial (1). If
(q) has a root of local length (m\ge2), multiplication by (q') is
nilpotent on that local Artin factor. Multiplication by (p') is therefore
(sI+N), so ((T-s)^m\mid C_f(T)). This proves (C_f'(s)=0) in the
nonreduced case as well. Because (C_f') is nonzero of degree (d-1), the
candidate bound is exactly the asserted finite bound. The proof does not
smuggle the Jacobian into the input.

### B. The five quartic partitions close the entire lower fiber

On (a=1), formal period two is functorially determined by fixed trace.
The simple-root stratum is finite by Sugiyama on (V_4). The two singular
finite strata are self-contained:

\[
[31]:\quad p=(x-r)^3(x+3r),\qquad p'(-3r)=-64r^3,
\]

and

\[
[211]:\quad
A=u^2(u-v),\quad B=-v^2(u-v),\quad
\frac BA=-\left(\frac vu\right)^2.
\]

After choosing one of two orderings of (A,B), there are at most two
choices for (v/u), then at most three choices for (u); (v) and (r)
follow. The boundary cases are explicitly absorbed by the lower
partitions. Only ([22]) and ([4]) remain positive-dimensional, and
centering makes them exactly (p=(x^2-L)^2), including (L=0). The
additional identity (C_f(T)=T^4\Rightarrow 4s^3=0) proves that the common
lower trace fiber cannot acquire an (a\ne1) component.

### C. The period-three formal calculation has the correct multiplicities

The complete intersection has standard monomials (0\le e_i<4), hence
rank 64. Its Jacobian determinant is

\[
t_\varepsilon=q_0q_1q_2+arepsilon^2(q_0+q_1+q_2),
\]

and at (arepsilon=1) this equals the trace of the product of the three
derivative matrices. The trace--residue exponent is consequently (t^3),
not (t^2) or (t^4), for the second power moment.

The finite slope certificate gives

\[
H(2,1)=2,qquad A_{2,2}=-2,qquad A_{2,1}=0,
\]

so (D_2=3\cdot4^9(-2)=-1572864). Independently, the Laurent ledger has
three cyclic ((2,1,1)) denominator placements, each contributing (-2),
so (mathcal C_{2,0}=-6) and (D_2=4^9(-6)). The other Laurent terms
vanish for the stated polynomial-versus-negative-power reasons.

The normal-form recurrence table is consistent with the defining signs.
In particular,

\[
R(9,6,6)=2,\quad R(9,9,9)=-6,\quad R(6,6,3)=-1,
\]

while the required ((9,3,3)), ((9,0,0)), and ((6,3,0)) patterns
vanish. The six grouped contributions sum to

\[
-1572864+294912-18432+384=-1296000.
\]

Finally, the invertible transverse ((u,v))-Jacobian at fixed support
reduces the remaining local equation to
(3p_L(\alpha+\delta)+O(\delta^{2r-1})), of exact order (r). Thus the
prime-period subtraction removes length 4 from length 64 with no residual
fixed support. The pointwise moment is

\[
-1296000-1572864L^3,
\]

and the cyclewise moment is its quotient by three. Equality of the full
period-three multiset therefore makes (L^3) finite, which is exactly what
the global quasi-finite argument requires; it does not assert global
injectivity or global separation by one moment.

## Primary-source and version audit

The controlling Cantat--Dujardin PDF was retrieved from the authors' site,
has 51 pages, is dated May 10, 2026, and has SHA-256
`707edeb33d0b5ef4b97fa6c73f2c0c95d73d975f5d119d0e3bc5c10eefbd8cc2`.
Its formal-period definitions in Sections 3.1--3.2, Theorem 3.7, Theorem
4.2, and Example 4.3 were inspected directly. Theorem 4.2 is a complex,
fixed-Jacobian theorem and is not widened here.

Sugiyama I and II were inspected in their primary arXiv/journal versions.
Their (V_d) domain excludes multiplier (1), so the package's
\([1111]\)-only use is correct. The explicit \([31]\) and \([211]\)
proofs avoid any questionable singular-fiber extension. The
Friedland--Milnor publisher record, Cattani--Dickenstein--Sturmfels primary
record, Hutz journal paper, Huguin primary record, and Stacks Tags 02NH and
02VI were also reopened in their limited roles.

The repeated current searches for the quartic period-three cutoff, the
pure-trace derivative identity, and the exact coefficients returned the
Cantat--Dujardin neighbor but no primary-source collision with the unified
three-theorem package. This remains a bounded, date-specific search result.

## Publication and lifecycle disposition

The source design is internally coherent and may proceed to its next
separately authorized source-lock stage. This review does not itself create
a source lock and does not authorize code, results, figures, a paper plan,
manuscript writing, compilation, submission, upload, or external release.

If an external manuscript is ever authorized, Paper 15 must be the unified
vehicle for the overlapping quartic theorem and Paper 12 calculation.
Paper 12 may remain internal provenance, but the two overlapping central
claims must not be submitted as parallel papers.

No mathematical or source-scope blocker remains at the source-design gate.

SOURCE_DESIGN_PASS
