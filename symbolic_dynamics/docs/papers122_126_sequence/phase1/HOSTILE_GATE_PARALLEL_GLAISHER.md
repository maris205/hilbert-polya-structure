# Hostile gate — parallel Glaisher compression

Date: 2026-08-30 UTC  
Role: independent nonauthor proof/owner/value gate  
Reviewed objects (pinned at the start and again before this report was written):

- `proof_spikes/PARALLEL_GLAISHER_REPORT.md`, SHA-256
  `4676a452cb0cd44f181ab7234da453bef61c6ba386383a97114d1569e7c2bdbf`;
- `proof_spikes/verify_parallel_glaisher.py`, SHA-256
  `4c8c7d8f821e8622e56ff50072bdee2707f024b3c500cf4696cf7578ec2c8bfb`;
- `proof_spikes/PARALLEL_GLAISHER_CANONICAL.txt`, SHA-256
  `d149ce6cf8da19c1d4215fe47d503301cbac6ae4c75c7765748462d84dc29670`.

I did not author the proof dossier and did not change it, the verifier, or the
canonical output. No paper directory, paper number, shared ledger, or Git state
was touched.

## Gate decision

**KILL / CORRECT BUT DIRECTLY MECHANIZED / NOT PAPER-SCALE AFTER OWNER
SUBTRACTION.**

External status remains **HOLD_EXTERNAL**. No novelty, priority, posting, or
submission claim is authorized.

This is primarily an owner/value kill, not a mathematical falsification. The
sharp clock, the one-step fibre product, the composite-base tower
decomposition, and the iterated-image criterion are all correct. A fresh run
also agrees byte-for-byte with the canonical output. The fatal issue is that
each tower is exactly the classical \(b\)-ary-partition firing system studied
as a discrete dynamical model by Latapy, while the global carrier is the
classical Glaisher decomposition into those towers. The proposed deterministic
map merely chooses the maximal bulk-parallel schedule for those already-owned
local firings. Its residual formulas are the immediate quotient/remainder
calculus of that schedule:

1. the sharp time is one carry level per round;
2. the fibre is a product of independent choices of a remainder;
3. the \(t\)-th image consists of states whose first \(t\) tower coordinates
   are legal base-\(b\) digits; and
4. the image OGF is a direct restricted-part product which, for \(b=2\), is
   already the generalized-POD class studied by Ballantine--Welch.

A bounded search did not find a paper stating this exact *bulk-synchronous
self-map* together with these three formulas. That bounded non-hit does not
repair the direct mechanism ownership or create enough theorem distance for a
standalone paper.

## 1. Literal map and conventions

Fix an integer \(b\ge2\). On the finite set \(\mathcal P_n\) of integer
partitions of \(n\), write \(m_j=m_j(\lambda)\) for the multiplicity of the
part \(j\), and define

\[
 m'_j=(m_j\bmod b)+\mathbf 1_{b\mid j}
          \left\lfloor\frac{m_{j/b}}b\right\rfloor .       \tag{1}
\]

Equivalently, using the *old* multiplicities at every size, replace every one
of the \(\lfloor m_j/b\rfloor\) disjoint batches of \(b\) copies of \(j\) by
one copy of \(bj\), simultaneously for all \(j\). Incoming copies at \(bj\)
are not merged again until the next round. This last sentence is necessary to
make “simultaneously” unambiguous.

Weight is preserved. The part count changes by

\[
 \ell(\Phi_b\lambda)-\ell(\lambda)
 =-(b-1)\sum_{j\ge1}\left\lfloor\frac{m_j}b\right\rfloor . \tag{2}
\]

Hence a nonfixed update strictly decreases the number of parts. Every orbit
terminates and there are no nontrivial cycles. A state is fixed exactly when

\[
 m_j<b\qquad\text{for every }j.                            \tag{3}
\]

For \(n=0\), the empty partition is fixed and the maximum depth is \(0\). The
display \(\lfloor\log_b n\rfloor\) must never be applied to \(n=0\). For
\(1\le n<b\), every partition is fixed.

## 2. Composite bases and the tower product

The dossier is correct for composite \(b\), but the convention is important.
Every positive integer has a unique representation

\[
 j=q b^k,\qquad k=\max\{r:b^r\mid j\},\qquad b\nmid q.     \tag{4}
\]

The condition is \(b\nmid q\), **not** \(\gcd(q,b)=1\). For example, when
\(b=4\), the tower containing \(2\) is
\(2,8,32,\ldots\); its root is not coprime to \(4\). Uniqueness follows
because two representations with distinct exponents would force the root at
the smaller exponent to be divisible by \(b\).

For a fixed root \(q\), put \(a_k=m_{qb^k}\). Equation (1) becomes

\[
 a'_0=a_0\bmod b,
 \qquad
 a'_k=(a_k\bmod b)+\left\lfloor\frac{a_{k-1}}b\right\rfloor
 \quad(k\ge1).                                             \tag{5}
\]

Different \(q\)-towers neither exchange weight nor interact. A tower preserves
\(q\sum_k a_kb^k\). A zero-weight target tower can only have the zero source,
so the global map is genuinely the finite product over the nonzero tower
weights. None of this uses primality of \(b\).

This also shows why the composite-base extension adds little independent
value: Latapy's \(b\)-ary-partition model is stated for arbitrary integer
\(b>1\), and the classical Glaisher theorem is likewise not restricted to
prime bases.

## 3. Sharp global clock — theorem is correct

Let \(a_k^{(t)}\) be a tower after \(t\) rounds. Induction in (5) gives

\[
 a_k^{(t)}<b\qquad(0\le k<t).                              \tag{6}
\]

Indeed, level \(0\) is reduced modulo \(b\) in the first round. If levels
below \(t\) are already below \(b\), then they send no later carry, and the
next update reduces level \(t\) modulo \(b\).

If the state after \(t\) rounds is nonfixed, some level \(k\ge t\) contains
at least \(b\) copies. That single tower then has weight at least

\[
 q\,b\,b^k\ge b^{t+1}.                                    \tag{7}
\]

For \(n\ge1\), taking \(r=\lfloor\log_b n\rfloor\) therefore proves

\[
 \max_{\lambda\vdash n}\tau_b(\lambda)\le r.              \tag{8}
\]

The dossier's witness is valid. With \(s=n-b^r\), it is

\[
 \lambda_{n,b}=1^{b+s}\prod_{i=1}^{r-1}(b^i)^{b-1}.
                                                                    \tag{9}
\]

Its weight is

\[
 b+s+(b-1)\sum_{i=1}^{r-1}b^i
 =b+s+(b^r-b)=n.
\]

The initial instability at level \(0\) sends a carry into the seeded
\(b-1\) copies at level \(1\); one round later that level sends a carry into
the seeded \(b-1\) copies at level \(2\), and so on. Thus the state remains
nonfixed through time \(r-1\), while (8) forces stabilization at time \(r\).

There is an even simpler sharp witness: \(1^n\). After \(t\) rounds its first
\(t\) coordinates are the first \(t\) base-\(b\) digits of \(n\), and its
level-\(t\) coordinate is \(\lfloor n/b^t\rfloor\). It is therefore unstable
for \(t<r\) and fixed at \(t=r\). This simplification reinforces, rather than
weakens, the hostile value finding: the sharp clock is exactly ordinary
parallel carry propagation.

**Clock verdict:** proved for every \(n\ge1\); \(n=0\) only needs an explicit
separate convention. No counterexample exists in the tested range.

## 4. One-step fibres — theorem is correct and coordinatewise

Fix one target tower \(y=(y_k)_{k\ge0}\). Write a source coordinate uniquely
as

\[
 x_k=bc_k+\epsilon_k,qquad 0\le\epsilon_k<b.
\]

Equation (5) is equivalent to

\[
 y_0=\epsilon_0,
 \qquad y_k=\epsilon_k+c_{k-1}\quad(k\ge1).                \tag{10}
\]

Thus there is no source when \(y_0\ge b\). If \(y_0<b\), then, independently
for each \(k\ge1\), one may choose

\[
 0\le\epsilon_k\le\min(b-1,y_k),
 \qquad c_{k-1}=y_k-\epsilon_k.                            \tag{11}
\]

The zero tail forces a zero source tail, so every choice gives finite support
and every preimage occurs exactly once. Hence one tower contributes

\[
 \mathbf 1_{y_0<b}\prod_{k\ge1}\min(b,y_k+1).              \tag{12}
\]

Multiplication across independent towers gives exactly the dossier formula

\[
 |\Phi_b^{-1}(\lambda)|=
 \begin{cases}
 0,&\text{if some }q\text{ with }b\nmid q\text{ has }m_q\ge b,\\[2mm]
 \displaystyle\prod_{b\mid j}\min(b,m_j+1),&\text{otherwise}.
 \end{cases}                                                \tag{13}
\]

The product may be taken over all positive \(j\), since absent parts
contribute \(1\). Weight preservation by \(\Phi_b\) puts every reconstructed
source back in \(\mathcal P_n\).

**Fibre verdict:** exact. It is nevertheless a one-line independent-remainder
product once the owned carry coordinates are written down. It is not a
second structural engine of paper-scale weight.

## 5. All iterated images — true, but the dossier proof is too compressed

Necessity is immediate from (6): after \(t\) rounds the first \(t\) levels of
each tower are below \(b\). Since these are precisely the part sizes not
divisible by \(b^t\),

\[
 \lambda\in\operatorname{Im}\Phi_b^t
 \Longrightarrow
 m_j(\lambda)<b\quad\text{whenever }b^t\nmid j.            \tag{14}
\]

The converse in the dossier is stated as an informal reverse induction. It
is correct, but an eventual proof would need the following explicit right
inverse. If \(y_j=m_j(\lambda)\) satisfies the right side of (14), define

\[
 x_j=\mathbf 1_{b^t\nmid j}y_j+b^t y_{b^t j}.              \tag{15}
\]

In words, leave each low-level target part in place and expand every target
part divisible by \(b^t\) into \(b^t\) copies \(t\) levels lower. On a tower,
(15) is

\[
 x_k=\mathbf 1_{k<t}y_k+b^t y_{k+t}.                       \tag{16}
\]

After \(s\) rounds, \(0\le s\le t\), direct induction in (5) gives

\[
 (\Phi_b^s x)_k=
 \begin{cases}
 y_k,&k<s,\\
 \mathbf 1_{k<t}y_k+b^{t-s}y_{k+t-s},&k\ge s.
 \end{cases}                                                \tag{17}
\]

The assumption \(y_k<b\) for \(k<t\) is exactly what prevents those retained
terms from carrying. At \(s=t\), (17) is \(y\). Also

\[
 \sum_j jx_j
 =\sum_{b^t\nmid j}jy_j+
   \sum_{j\ge1}j b^t y_{b^t j}
 =\sum_j jy_j,
\]

so the right inverse remains in the fixed-weight phase. Therefore

\[
 \boxed{\lambda\in\operatorname{Im}\Phi_b^t
 \iff m_j(\lambda)<b\text{ for every }b^t\nmid j}.         \tag{18}
\]

This proves the advertised OGF

\[
 I_{b,t}(x)=
 \prod_{b^t\nmid j}(1+x^j+\cdots+x^{(b-1)j})
 \prod_{b^t\mid j}\frac1{1-x^j}.                         \tag{19}
\]

There is, however, an owner/value-revealing cancellation which the dossier
does not display:

\[
 \begin{aligned}
 I_{b,t}(x)
 &=\frac1{\prod_{j\ge1}(1-x^j)}
   \prod_{b^t\nmid j}(1-x^{bj})\\
 &=\frac{\displaystyle
   \prod_{\substack{b\mid k\\ b^{t+1}\nmid k}}(1-x^k)}
   {\displaystyle\prod_{k\ge1}(1-x^k)}.                  \tag{20}
 \end{aligned}
\]

Thus \(|\operatorname{Im}\Phi_b^t|\) is also the number of partitions
avoiding every part \(k\) with \(b\mid k\) but \(b^{t+1}\nmid k\). Formula
(20) is an elementary cancellation of ordinary restricted-part products. At
\(b=2\), (18) is exactly the class “parts not divisible by \(2^t\) distinct,
parts divisible by \(2^t\) unrestricted,” a generalized POD class explicitly
studied by Ballantine--Welch.

**Image verdict:** the setwise theorem is true. The current sufficiency prose
must be replaced by (15)--(17) in any archival use. After (20) and the POD
subtraction, the enumerator has low residual value.

## 6. Fresh exact controls

The corrected current verifier was rerun without modifying or wrapping its
source. I captured stdout in memory and compared it with the canonical file:

```text
parallel Glaisher compression verifier: PASS
exact assertions: 18,981,700
bases: 2..10; exhaustive boundary partitions: n<=36
literal fibres/depths: bases 2..6, n<=30
iterated images: bases 2..6, n<=26, t<=5
image products: bases 2..6, coefficients n<=120, t<=6
```

The complete stdout comparison returned `cmp` exit status `0`. Fresh stdout
had SHA-256
`d149ce6cf8da19c1d4215fe47d503301cbac6ae4c75c7765748462d84dc29670`,
identical to the canonical-file hash.

The verifier correctly:

- implements simultaneous old-state multiplicities;
- checks closure, weight, fixed points, strict part-count descent, and depth;
- constructs every literal one-step fibre before comparing (13);
- compares literal and predicted \(\operatorname{Im}\Phi_b^t\) sets;
- compares (19) coefficientwise; and
- includes composite bases in its boundary lane.

As an independent hostile control, I used the explicit right inverse (15),
not the dossier's reverse routine, for composite bases
\(b=4,6,8,9,10,12\), all partitions through \(n=26\), and \(1\le t\le5\).
I also tested the simpler witness \(1^n\) for \(2\le b\le15\) and
\(1\le n\le200\). All **852,460** explicit review-side checks passed. This
control was run inline; no additional proof-spike file was created.

The exact program remains evidence, not a proof or owner certificate.

## 7. Primary-source owner audit

Only primary papers, author/venue copies, arXiv records, and official
publisher pages were used to make owner conclusions. Searches were run in
English with exact and mechanism-level variants, including:

- `"parallel Glaisher" partitions simultaneous`;
- `"Glaisher map" iteration partitions`;
- `"merge all" "equal parts" Glaisher`;
- `integer partition dynamics merge equal parts simultaneously`;
- `b-ary partitions parallel chip firing`;
- `parallel convergence time b-ary partition`;
- `image/fibres of Glaisher map`;
- `parts not divisible by b^t multiplicity less than b`;
- `2025 2026 Glaisher bijection dynamics`; and
- `2025 2026 equal-part merging carry partitions`.

The search was bounded and is not a priority certificate. Its decisive
results are as follows.

| Source | What is directly owned | Residual after subtraction |
|---|---|---|
| J. W. L. Glaisher, *A theorem in partitions*, Messenger of Math. 12 (1883), 158--170; modern algorithmic restatement in [Pathak (2020)](https://arxiv.org/abs/2003.08220) | General-\(b\) repeated merging of \(b\) equal parts, base-\(b\) multiplicity digits, terminal bijection between parts not divisible by \(b\) and multiplicities below \(b\) | No credit for the carrier rewrite, fixed class, terminal normalization, or terminal product |
| M. Latapy, [*Partitions of an Integer into Powers*](https://doi.org/10.46298/dmtcs.2279), DMTCS Proceedings AA (2001), 215--228 | The exact one-tower phase \(a=(a_0,a_1,\ldots)\), arbitrary integer base \(b>1\), and the local firing \(a_i\mapsto a_i-b,\ a_{i+1}\mapsto a_{i+1}+1\), explicitly as a discrete dynamical model; also the full \(b\)-ary-partition reachability poset/lattice | Only the choice to fire every possible batch at every site in one synchronous macro-step, plus consequences of that schedule |
| A. Pathak, [*Glaisher's Partition Problem*](https://arxiv.org/abs/2003.08220) | For every \(q\) not divisible by \(b\), the matrix of base-\(b\) digits of multiplicities of \(qb^j\); this is the same tower decomposition and it allows composite \(b\) | No credit for tower coordinates or composite-base decomposition |
| W. J. Keith, [*A bijection for partitions simultaneously \(s\)-regular and \(t\)-distinct*](https://arxiv.org/abs/2207.13840), INTEGERS 23 (2023), A9 | Glaisher maps, part-frequency matrices, and iteration questions for compositions of generalized Glaisher maps | Not the literal synchronous map, but a close warning against presenting “iterated Glaisher dynamics” as an unoccupied phrase |
| C. Ballantine and A. Welch, [*Generalizations of POD and PED partitions*](https://doi.org/10.1016/j.disc.2024.114150), Discrete Math. 347 (2024), 114150 | Partitions whose nonmultiples of \(r\) are distinct while multiples of \(r\) are unrestricted, with their product identities; at \(r=2^t\) this is exactly (18) for \(b=2\) | Binary temporal interpretation only; the binary image classes and their enumeration receive zero credit |
| T. McConville, J. Propp, and B. E. Sagan, [*Hyperbinary partitions and \(q\)-deformed rationals*](https://doi.org/10.1017/fms.2026.10182), Forum Math. Sigma 14 (2026), e30 | Power-of-two multiplicity states, the refinement/chip-firing move “two chips at level \(m\) become one at \(m+1\),” and the resulting poset/lattice neighborhood | Not the bulk-synchronous timing, but a current 2025--2026 direct carrier/mechanism neighbor |
| G. E. Andrews and A. Dhar, [*On Glaisher's Partition Theorem*](https://arxiv.org/abs/2512.12346) (2025/2026) | Current finite/infinite series and refinements of the classical Glaisher product | Checked through the current horizon; no exact synchronous clock/fibre/image theorem found there |

### Direct-owner conclusion

I found **no exact literal owner** for the single deterministic macro-update
that fires \(\lfloor a_i/b\rfloor\) times at every tower site simultaneously,
nor for the exact conjunction (8), (13), and (18). That is only a bounded
non-hit.

I did find a **direct mechanism owner** strong enough to fail the intended
value gate: Latapy already places the identical tower state and identical
elementary firing inside a discrete dynamical model. Glaisher/Pathak own the
product over towers, and Ballantine--Welch own the binary image classes.
“Parallelize all legal owned firings and read off carry propagation” is not
sufficient residual distance for a new short paper.

## 8. P1--P121 internal collision audit

There is no literal duplicate map in P1--P121. The collision is instead a
high-risk conjunction of three already-used internal engines.

| Internal paper | Collision | Honest firewall |
|---|---|---|
| P100, least-valuation digit erasure | Base-\(p\) digit coordinates, a monotone transient, a sharp arithmetic clock, terminal periodic blindness | P100 deletes one least nonzero digit on a finite residue ring; this candidate propagates carries on partition multiplicities. Different maps, but the digit-clock narrative is already occupied. |
| P113, principal-hook partition dynamics | Same finite carrier \(\mathcal P_n\), an owned one-step image and product fibre, and a sharp global clock | P113 regroups Ferrers cells into principal hooks; this candidate merges equal parts. The carrier/theorem-package collision remains substantial even though the update differs. |
| P115, bounded Cartier dynamics | Independent index towers, every iterated image, exact fibres, and logarithmic sharp depth from one-step index propagation | P115 acts on bounded finite-field polynomials and has a nontrivial Frobenius core. This candidate is nonlinear only because of quotient/remainder notation and has fixed recurrence only. The proof architecture is nevertheless very close. |
| P48/P77/P100 digit/carry neighborhood | Radix and digit towers are already a recurring portfolio mechanism | P48/P77 are not integer-partition self-maps, so this is thematic rather than a literal collision. |
| P110/P121 partition/merger neighborhood | Partition language and merging already occur internally | P110 uses labelled set partitions and lattice joins; P121 is a random nonassociative adjacent coalescence. Neither is a direct map collision. |

The strongest firewall is therefore true but not enough: “unlabelled integer
partitions plus synchronous Glaisher carries” is distinct objectwise from each
one of P100, P113, and P115, yet it recombines their most visible mechanisms
(digit tower, partition fibre product, complete image tower/log clock) without
a comparably new structural engine.

## 9. Severity-ranked findings

### CRITICAL — direct mechanism owner omitted from the dossier

The dossier mentions classical sequential Glaisher merging but does not name
Latapy's 2001 \(b\)-ary-partition dynamical model. On each \(q\)-tower,
Latapy's state and firing are literally the carrier and elementary move from
which (5) is built. Any archival text would have to put this source in the
first ownership paragraph and assign zero credit to the tower dynamics,
reachability carrier, stable base-\(b\) state, and local firing.

### CRITICAL — residual is below paper scale

After the preceding subtraction, the surviving claims are scheduling facts
for ordinary carries. The clock has the universal witness \(1^n\), the fibre
is (11), and image sufficiency has the explicit expansion (15). Formula (20)
reduces the alleged temporal enumerator to an elementary forbidden-part
product. There is no pointwise depth formula, nontrivial depth-layer
enumerator, aggregate iterated-fibre theory, new asymptotic regime, or
component geometry left to supply a second independent engine.

This cannot be repaired by stronger novelty wording, a longer introduction,
or the addition of the trivial fixed-point zeta, whose exponent is the number
of fixed states in \(\mathcal P_n\). The current candidate is killed as a
standalone paper.

### MAJOR (proof) — image sufficiency is asserted too tersely

The claim is true, but “reverse one carry round while requiring the first
\(t-1\) levels to be below \(b\)” does not prove that all reverse choices are
compatible or preserve finite support. Equations (15)--(17) are the required
repair if the result is retained as an internal lemma or example.

### MAJOR (owner/scope) — the image product has an owned binary lane

For \(b=2\), every \(t\)-image is exactly Ballantine--Welch's generalized-POD
class with nonmultiples of \(2^t\) distinct and multiples unrestricted. The
class and product must receive zero credit; only its realization as an image
at time \(t\) is residual. For general \(b\), (20) still makes the enumeration
an immediate Glaisher-style product cancellation.

### MINOR — boundary and terminology controls

- State the \(n=0\) maximum depth separately; \(\log_b0\) is undefined.
- Continue to use \(b\nmid q\), never “\(q\) coprime to \(b\),” for composite
  bases.
- Say “bulk-parallel” or explicitly state that all
  \(\lfloor m_j/b\rfloor\) batches are fired. Standard parallel chip-firing
  often means one firing per unstable site, which is a different schedule.
- In the fibre product, specify that zero-multiplicity factors equal \(1\).

## 10. Claim ceiling and re-entry condition

The material may be archived as a correct worked proposition about a
bulk-parallel schedule on the classical Glaisher/Latapy carry towers. Its
defensible ceiling is:

1. definition and part-count Lyapunov;
2. maximum depth \(\lfloor\log_b n\rfloor\) for \(n\ge1\);
3. the pointwise one-step fibre formula (13); and
4. the image criterion/right inverse (18) and product (19), with (20) and all
   classical restricted-part identities assigned zero credit.

That is not a paper contract. Re-entry would require a genuinely nonlocal
second engine not forced coordinatewise by Euclidean division—for example an
all-depth fibre/layer theory with a nontrivial new structure—and a new owner
gate against Latapy, generalized POD/PED work, and the 2026 hyperbinary
literature. Merely deriving more Euler products from (18), adding zeta, or
renaming the parallel schedule does not qualify.

## Final verdict

**KILL.** Mathematical correctness: high. Exact-literal-owner risk: bounded
but not decisive. Direct mechanism ownership: fatal. Internal distinctness:
insufficient. Standalone paper value after subtraction: below threshold.

**HOLD_EXTERNAL remains in force.**
