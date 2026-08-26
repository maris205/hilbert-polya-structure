# Batch review: HCS-C174--HCS-C178

Date: 2026-08-26

Source commit: `100e5f601a0196710d53784bdeef40d2bff89fa8`.

Evaluator authority: `flow_systems/skills/route-a-evaluator.md` version 0.2.0, SHA-256 `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.

Common scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

Recommendation: **retain all five enlarged source theorems and their exact obstructions as Route-A research progress; keep every candidate rejected and Route B unauthorized.**

## Completed paper outputs

### C174 -- odd-affine 2-adic parity renewal

For every odd integer pair \((a,b)\), C174 separates three clocks that were previously conflated. The original map has one fixed point for each based binary word,
\[
\#\operatorname{Fix}(T_{a,b}^n)=2^n,
\qquad \zeta_{AM}(z)=\frac1{1-2z}.
\]
On the odd cross-section, the return symbol is \(k=v_2(ax+b)\), has conditional Haar law \(2^{-k}\), and produces a countable full shift after the countable null exceptional set is removed. Its accelerated time-one map already has countably many fixed points and no ordinary Artin--Mazur zeta. Restoring original time through roof \(r(k)=k\) gives
\[
\zeta_{\rm roof}(z)=\frac{1-z}{1-2z};
\]
the omitted all-zero orbit restores \((1-2z)^{-1}\). The reciprocal 2-adic stability weight gives \(W_n=1\) and \(\zeta_{\rm stab}=(1-z)^{-1}\) for every odd \((a,b)\), proving parameter blindness. The classical parity conjugacy is explicitly attributed as prior foundation. The legal \((3,1)\) cycle through \(1/5\) is used to prove that the result does not advance the positive-integer Collatz conjecture.

### C175 -- cyclic Rule 184 traffic dynamics

C175 proves the all-size, all-density periodic-core theorem. Below half density the periodic words are exactly those without cyclic `11` and Rule 184 becomes right rotation; above half density the holes are isolated and the core is left rotation. A gap-zero Lyapunov proof gives entry in at most \(m^2\) steps for \(m=\min(k,N-k)\). With \(g=\gcd(N,n)\), \(q=N/g\), and
\[
I(g,r)=\frac{g}{g-r}\binom{g-r}{r},
\]
the all-iterate fixed count is \(I(g,m/q)\) when \(q\mid m\), and zero otherwise. Möbius inversion yields every exact period, primitive cycle, zeta, and periodic-core determinant. The whole sector is a rotation permutation exactly for \(m\le1\); for \(m\ge2\), genuine transients prevent full-system unitarity.

### C176 -- recurrent Abelian sandpile translations

For every finite connected undirected loopless sink multigraph and nonnegative addition vector, C176 proves that actual addition--stabilization on recurrent stable configurations is critical-group translation. With \(D=\det\Delta\) and \(L=\operatorname{ord}([b])\), two exact coordinate systems agree:
\[
L=\operatorname{lcm}_i\frac{d_i}{\gcd(d_i,(Ub)_i)}
=\frac{D}{\gcd(D,(\operatorname{adj}\Delta b)_1,\ldots)}.
\]
Every recurrent orbit has exact length \(L\), there are \(D/L\) cycles, and
\[
\#\operatorname{Fix}(T_b^n)=D\mathbf1_{L\mid n},
\quad \zeta=(1-z^L)^{-D/L},
\quad \det(I-zU_b)=(1-z^L)^{D/L}.
\]
Every \(L\)-th root occurs with multiplicity \(D/L\); group inversion reverses the clock; the finite Koopman unitary is self-adjoint exactly for \(L\le2\). The \(r=0\), \(b=0\), multigraph, and all-stable-state boundaries are explicit. A two-state path collapse prevents recurrent permutation structure from being laundered into the full stable space.

### C177 -- integer expanding circle endomorphisms

C177 joins orbit, operator, and mixing layers for every \(b\ge2\):
\[
\#\operatorname{Fix}(T_b^n)=b^n-1,
\quad \zeta_{AM,b}(z)=\frac{1-z}{1-bz},
\quad U_b\simeq1\oplus S^{(\aleph_0)}.
\]
Every nonzero Fourier index has a unique chain root \(m=rb^j\), \(b\nmid r\), giving the complete Wold decomposition and Perron filter. The Koopman operator is a proper noncompact isometry, lies in no finite Schatten class, and has no ordinary Fredholm determinant. For mean-zero \(f\in\dot H^s\),
\[
|\langle f,U_b^ng\rangle|\le b^{-ns}\|f\|_{\dot H^s}\|g\|_2,
\]
and the one-mode witness attains equality. Prime and composite degrees obey the identical theorem, which is the decisive A0 control.

### C178 -- harmonic-oscillator strobes and quantization

C178 freezes physical time \(\theta\in\mathbb R\). Classically, every nonresonant iterate fixes only the origin, while a resonant iterate fixes the whole plane. Irrational \(\theta/(2\pi)\) has \(\zeta_{AM}=(1-z)^{-1}\); every rational angle has uncountable fixed sets at multiples of its denominator and no ordinary Artin--Mazur series. On Gaussian \(L^2\), the Laguerre--angular basis gives eigenvalues \(e^{im\theta}\) with infinite radial multiplicity. The natural quantum oscillator satisfies exact Egorov and Hermite spectral formulas at the same real clock. Crucially, the final theorem retains the metaplectic cover:
\[
Q_{\theta+2\pi}=-Q_\theta,
\qquad Q_{\theta+4\pi}=Q_\theta.
\]
Thus the quantum family is not a single-valued unitary family on the classical \(2\pi\) quotient. Both physical unitaries are noncompact, non-Schatten, and lack ordinary trace-class Fredholm determinants; heat/Wick evolution is a different clock.

## Strict Route-A record

| paper | A0 | A1 | A2 | A3 | A4 | overall |
|---|---|---|---|---|---|---|
| C174 | `A0_FAIL` | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C175 | `A0_FAIL` | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C176 | `A0_FAIL` | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_NATURAL_QUANTIZATION` | `ROUTE_A_REJECTED` |
| C177 | `A0_FAIL` | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C178 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_NATURAL_QUANTIZATION` | `ROUTE_A_REJECTED` |

All coordinates remain local to their source. In particular, the natural recurrent sandpile permutation and quantum oscillator propagator are different operators and cannot be combined. A4 never compensates for A0--A3. Every `route_b_invocation_allowed` value is false.

## Uniform release audit

| paper | checker assertions | SymPy checks | hostile rejections | payload closure | PDF pages |
|---|---:|---:|---:|---:|---:|
| C174 | 272,693 | 911 | 26/26 | 27/27 | 3 |
| C175 | 34,545 | 25,563 | 17/17 | 27/27 | 3 |
| C176 | 135,049 | 5,248 | 17/17 | 27/27 | 3 |
| C177 | 3,980 | 3,927 | 19/19 | 27/27 | 2 |
| C178 | 26,271 | 10,465 | 65/65 | 27/27 | 2 |
| **total** | **472,538** | **46,114** | **144/144** | **135/135** | **13** |

Every final package contains exactly 27 content-addressed payloads and one self-excluded manifest. Producer-independent checkers do not import producer implementations. Separate SymPy paths reconstruct headline identities. Canonical replay binds the released evidence bytes. Semantic mutations repair payload hashes before rejection, while stale-hash attacks are separate.

All five manuscripts preserve three pairwise-distinct drafting rounds with `main.pdf == main_round2.pdf`. Fresh fixed-epoch builds reproduce the released final bytes, every listed font is embedded/subset, final logs are clean, and all 13 rendered pages have been inspected. C174 contains two verified ownership citations; the other four citation and reference populations are zero. No paper makes a universal novelty, external-review, reviewer-independence, journal-readiness, or acceptance-score claim.

## Content-addressed release ledger

| paper | evidence SHA-256 | PDF SHA-256 | manifest SHA-256 |
|---|---|---|---|
| C174 | `9cdedc898e8624b00c73ccde4bd316fb4bb2cb948720d7201bed16e0bcd81004` | `5d236849a52afa5d54d7f9d6423020754bf9d0565bd4b8fb7215a4eb0f886e24` | `b0abb41007bbf5a3719506406ecf16a9a0e270d1235af0966f9853d7f6221d29` |
| C175 | `3979dbf048351370a4bd56c8b7324f89012777dac8807b004130622a06692597` | `be7df400f168b6665022994655ad7a04a452dac552b6741e232371880867f80d` | `932465aa253cb238fc5186ce5161fb848efebd0573f092b7056106ab2247e86d` |
| C176 | `abc7cb819a1a2b3547576c85b8f02c54c6aa39e4909e001a38efcabbbdce89b5` | `e17ed450d618f5a17c151207d3fddccb667cd24496ec329fb4a209a2cc1bdcf6` | `095c76300a1bae1d13461ffbf219c73ce9c1904b379fcd28bb027451d308f5f5` |
| C177 | `0188a062036ff4aaa39b71cebcd67a4f989c3854a7babe289d6eea100ab8ce30` | `7ff51b4deb6c31f2eb2c7eac52850de79bb91bf1d20460bc7ae3fa0be20e5069` | `28a6169adc8cf0566b5e3d76488f8937ffe3bc277b6ff14bda0047b96abdf62d` |
| C178 | `8b3027501091c474a5566059467052f22d3f7c6beed3e3831c624b119b9041bd` | `936b9aa851d26114e4131a649460ad84e7522e7e6dbfa21907558810113d3fb3` | `8bc1b09fe152ff44d86e3153ac5515a0b765cfbcb4a22fe643a376557e2c6cf7` |

## Internal cross-review and repair ledger

These are evidence-anchored internal theorem, scope, and release audits. They are not external peer review and do not claim reviewer or error-process independence.

- **C174:** the review refuses to count the classical parity conjugacy as new, expands the exceptional set from the single point \(-b/a\) to every eventually-zero parity tail, distinguishes accelerated time from roof time, and keeps the noninteger \((3,1)\) cycle as a hard Collatz boundary.
- **C175:** an independent exhaustive scan through \(N=18\) checks 524,286 states and finds no counterexample to the periodic-core equivalence, \(m^2\) attraction, core rotations, or the \(m\le1\) whole-sector bijection boundary.
- **C176:** the review requires the physical recurrent-representative bridge before abstract translation, checks both order formulas, retains the \(r=0\) and \(b=0\) cases, and uses the path collapse to separate recurrent and all-stable operators.
- **C177:** the review expands Möbius/Wold controls to \(b,n\le30\), Fourier modes through \(|m|\le5000\), and 19,800 random finite-support correlation tests. It also repaired the evaluator YAML to include every v0.2 required input and authority field and removed generated build auxiliaries before final 27+1 closure.
- **C178:** the first internal audit caught the missing metaplectic double-cover boundary. The source was repaired from an angle quotient to real physical time, with the \(2\pi\) sign and \(4\pi\) return regenerated in evidence, checker, SymPy, mutations, YAML, manuscript, and manifest. A second audit repaired a source-lock sentence so that both classical and Gaussian Koopman projections, not only the classical map, are explicitly \(2\pi\)-periodic.

## ARS Stage 2.5 failure-mode audit

1. **Implementation bug passing self-review: CLEAR.** Five producer-independent checkers, five symbolic paths, byte replays, hostile mutations, expanded cross-audits, and explicit edge cases agree with final evidence.
2. **Hallucinated citation: CLEAR.** C174's two ownership references are verified and narrowly scoped. The other citation and reference populations are zero.
3. **Hallucinated result: CLEAR AT PROOF LAYER.** Every headline has an all-parameter proof; finite tables remain deterministic sentinels.
4. **Shortcut reliance: CLEAR.** No finite cutoff proves an infinite statement. The C178 parameter-cover error was fixed rather than hidden projectively.
5. **Bug reframed as insight: CLEAR.** Failed candidate gates and rejected mutations are not promoted to mathematics.
6. **Methodology fabrication: CLEAR.** Every producer, checker, SymPy, replay, mutation, build, font, visual, and manifest procedure is executable and artifact-bound.
7. **Frame-lock: CLEAR.** Every candidate remains rejected at A0, and positive A4 structure is never used to replace failed orbit or arithmetic gates.

## ARS Stage 4.5 post-manuscript audit

The seven modes were repeated against the final PDFs and manifests. Final source claims, evidence fields, evaluator records, and release ledgers agree. All corrections triggered full evidence/manifest regeneration where bytes changed. The five PDFs retain limitations, nonclaims, declarations, and source-specific clocks. No target table, target divisor, target functional equation/counting law, arithmetic local datum, Euler factor, root number, automorphy object, Hilbert--Pólya operator, or Route-B input appears as an affirmative claim.

## Batch conclusion

The batch achieves the requested larger steps by changing subtype and enlarging theorem scope in every paper. It also yields a consistent negative lesson: exact orbit ledgers, exact mixing, a physical finite permutation, or a genuine same-clock quantum lift can each exist without an intrinsic prime carrier. Future Route-A candidates must pass A0 from their source definition before any determinant resemblance can matter.
