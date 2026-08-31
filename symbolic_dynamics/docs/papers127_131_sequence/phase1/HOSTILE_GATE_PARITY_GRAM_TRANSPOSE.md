# Hostile gate: X07 parity--Gram transpose

**Role:** independent nonauthor theorem/owner gate.  **Audit date:**
2026-08-31.  **External status:** `HOLD_EXTERNAL`.  **Hard verdict:**
**GO_INTERNAL_AFTER_MANDATORY_REPAIR** (the `GO` branch of this gate, not a
novelty or priority finding).

The finite-map contract is unusually clean and survives independent
reconstruction.  One statement of the fibre theorem is nevertheless false
if “target” means an arbitrary codomain point, the boundary \(n=0\) is not
controlled, “rank-one” is literally wrong when the parity vector vanishes,
and the current spike supplies only one proof route.  These are mandatory
repairs before any freeze.  After all static rank-one/complementation,
transpose, binary-margin, and functional-graph bookkeeping is assigned zero
credit, the residual is still a coherent small paper: one literal
state-dependent map with its quotient, exact transient/recurrent
decomposition, complete fibres, and component census.

## 1. Evidence reviewed and fresh control

The following frozen scouting evidence was read without modification.

| file | SHA-256 |
|---|---|
| `proof_spikes/PARITY_GRAM_TRANSPOSE_REPORT.md` | `3149fccce7a7dc690eed39fc206a92bf158d782df9f41e7df6990476ca166bbf` |
| `proof_spikes/verify_parity_gram_transpose.py` | `330f0c1ace1dbca2517c7260ffc097307971b3389033e58572e373b9b896ae68` |
| `proof_spikes/PARITY_GRAM_TRANSPOSE_CANONICAL.txt` | `1a8c2bfe5802f39f0b172eab564b317bf750c4cc2728028c250598d3a32e9b03` |
| `phase1/SYSTEM_COLLISION_FIREWALL.md` | `84ed6ed93d308bc9565ba7d7d3629469358ad29287b0dc5fbe69f41eec6e55fc` |

I ran the verifier in a fresh temporary output file and compared bytes:

```bash
python3 docs/papers127_131_sequence/proof_spikes/verify_parity_gram_transpose.py > "$tmp"
cmp -s "$tmp" docs/papers127_131_sequence/proof_spikes/PARITY_GRAM_TRANSPOSE_CANONICAL.txt
sha256sum "$tmp"
```

The comparison passed.  Fresh stdout has SHA-256
`1a8c2bfe5802f39f0b172eab564b317bf750c4cc2728028c250598d3a32e9b03`,
reports **1,138,911 assertions**, and exhausts all \(2^{n^2}\) matrices for
\(1\le n\le4\).  This is strong falsification evidence, not an all-\(n\)
proof.

## 2. Literal definition audit

For \(n\ge1\), let \(e\in\mathbb F_2^n\) be the all-one column, put

\[
r=Ae,\qquad c=A^{\mathsf T}e,\qquad
\tau=e^{\mathsf T}Ae,
\]

and define

\[
\Phi(A)=A^{\mathsf T}+rr^{\mathsf T}.
\]

This is well-defined on all of \(M_n(\mathbb F_2)\).  The prose must call
\(rr^{\mathsf T}\) a **rank-at-most-one** correction: it has rank zero when
\(r=0\).  “Gram” is descriptive only; no general Gram-map result may be
claimed.  It is also useful, and owner-revealing, to record the exact
factorisation

\[
\Phi(A)=(I+r e^{\mathsf T})A^{\mathsf T}.
\]

The map on \(M_0(\mathbb F_2)\) can be defined as the fixed empty matrix, but
the displayed half-space formulas contain \(2^{n^2-1}\) and do not extend to
\(n=0\).  The clean solution is to state every main theorem for \(n\ge1\) and
give the empty case separately.

## 3. Independent reconstruction of every formula

Write \(B=\Phi(A)\).  Direct multiplication, not the pilot, gives

\[
r(B)=c+\tau r,\qquad c(B)=(1+\tau)r,
\qquad \tau(B)=\tau+\tau^2=0.
\]

Thus every image has even total parity.  On the even hyperplane the margin
pair is swapped; on the odd coset it becomes \((c+r,0)\).  The even
hyperplane is invariant and

\[
\Phi^2(A)=A+rr^{\mathsf T}+cc^{\mathsf T},\qquad
\Phi^4(A)=A\quad(\tau=0).
\]

Consequently every even point is recurrent and every odd point has exact
entrance time one.  If \(r\ne c\), the diagonal identity
\(vv^{\mathsf T}\mapsto v\) shows
\(rr^{\mathsf T}\ne cc^{\mathsf T}\), so \(\Phi^2(A)\ne A\); the period is
exactly four.  If \(r=c\), the period divides two.  This establishes, rather
than merely samples, the period set \(\{1,2,4\}\).

### 3.1 The required full fibre trichotomy

For a proposed target \(B\), solving
\(B=A^{\mathsf T}+rr^{\mathsf T}\) gives
\(A=B^{\mathsf T}+rr^{\mathsf T}\).  The row-margin condition becomes

\[
r=c(B)+\tau r.
\]

It follows that the correct codomain-wide statement is

\[
|\Phi^{-1}(B)|=
\begin{cases}
0,&\tau(B)=1,\\
1,&\tau(B)=0\text{ and }c(B)\ne0,\\
2^{n-1}+1,&\tau(B)=0\text{ and }c(B)=0.
\end{cases}
\]

In the last line there is one even preimage, plus one preimage for each of the
\(2^{n-1}\) odd-weight choices of \(r\).  Therefore the image is precisely the
even-total hyperplane, of size \(2^{n^2-1}\), and exactly
\(2^{n(n-1)}\) image points have the large fibre.

The present report instead says without qualification that “a target with
nonzero column parity has one preimage.”  Taken on the stated codomain, that
is false: for \(n=1\), \(B=[1]\) has nonzero column parity and no preimage.
The verifier silently quantifies only over keys already in its `fibres`
counter, so it cannot detect this prose-level quantifier error.  Restricting
the phrase to **an image target** repairs it, but the three-case formula above
is safer and complete.

### 3.2 Margin and component counts

For prescribed row and column parities having the same total parity, the
upper-left \((n-1)\times(n-1)\) entries are free and the final row and column
are then forced.  Hence every feasible margin fibre has
\(2^{(n-1)^2}\) matrices.  There are \(2^{n-1}\) even vectors \(r\), so the
number of recurrent points with equal margins is

\[
2^{n-1}2^{(n-1)^2}=2^{n(n-1)}.
\]

A fixed point satisfies \(A+A^{\mathsf T}=rr^{\mathsf T}\).  Comparing
diagonals forces \(r=0\), after which \(A\) is symmetric with zero row sums.
Choosing its off-diagonal entries on the first \(n-1\) vertices freely and
forcing the last row/column gives dimension \(n(n-1)/2\).  Therefore

\[
F_n=2^{n(n-1)/2},
\]

and the numbers of cycles are exactly

\[
C_{2,n}=\frac{2^{n(n-1)}-F_n}{2},\qquad
C_{4,n}=\frac{2^{n^2-1}-2^{n(n-1)}}{4}.
\]

The odd coset contains \(2^{n^2-1}\) depth-one states.  For fixed \(n\ge1\),
the finite Artin--Mazur zeta function is consequently

\[
\zeta_{\Phi_n}(z)=
(1-z)^{-F_n}(1-z^2)^{-C_{2,n}}(1-z^4)^{-C_{4,n}}.
\]

All formulas survive the checks \(n=1,2\), including the degeneracy of the
four-cycle term.

## 4. Severity-ranked objections

### CRITICAL

None found in the literal map or reconstructed all-(n) identities.

### MAJOR (mathematics and exposition)

1. **The one-step fibre theorem has the wrong visible quantifier.**  Replace
   it by the codomain-wide three-case law above, or say explicitly “among
   image targets.”  Include the \(n=1,B=[1]\) counterexample as a guard.
2. **The proof contract currently has only one route.**  A paper freeze under
   the sequence methodology needs two genuinely different derivations.  One
   acceptable split is (i) the row/column-margin quotient and affine-fibre
   count above, and (ii) the factorisation
   \((I+r e^{\mathsf T})A^{\mathsf T}\), treating \(I+r e^{\mathsf T}\) as an
   involutory transvection when \(\tau=0\) and a singular projection when
   \(\tau=1\), followed by an independent fixed-space calculation.  Merely
   reordering the same parity algebra is not a second proof.
3. **The affine margin count is invoked as “standard” at the exact point on
   which the cycle census depends.**  Supply the explicit
   \((n-1)\times(n-1)\)-core parametrisation and verify the forced corner is
   consistent iff the two total parities agree.

### MAJOR (owner scope and value)

1. The outer product toggles the looped complete submatrix on the odd-row
   vertex set.  Static induced-subgraph complementation, local
   complementation, pivot, loop complementation, and binary symmetric-matrix
   linear algebra must be prominent zero-credit background, not described
   generically as “rank-one perturbation literature.”  Direct neighbors are
   Bouchet's [*Recognizing locally equivalent graphs*](https://doi.org/10.1016/0012-365X(93)90357-Y),
   Traldi's [*On the linear algebra of local complementation*](https://arxiv.org/abs/1101.1246)
   (DOI [10.1016/j.laa.2011.06.048](https://doi.org/10.1016/j.laa.2011.06.048)),
   and Brijder--Hoogeboom's
   [pivot/loop-complementation calculus](https://arxiv.org/abs/0909.4004)
   (DOI [10.1016/j.ejc.2011.03.002](https://doi.org/10.1016/j.ejc.2011.03.002)).
2. Current 2025--2026 neighbors also receive zero credit: Koch--Pardal--dos
   Santos's [subgraph-complementation work](https://arxiv.org/abs/2502.15675)
   and Chen--Ren's
   [modular transpose actions](https://doi.org/10.1016/j.ffa.2026.102824).
   Neither source located in this bounded audit studies the literal
   state-dependent map, but absence from these searches is not novelty.
3. **P125 is a serious portfolio silhouette collision.**  Both are exact
   quadratic finite-state systems over \(\mathbb F_2\) resolved by a small
   quotient, fibres, cycles, and zeta.  The firewall must state the actual
   obstruction to conjugacy: P125 has tail at most two and admits period
   three, while X07 has tail at most one and recurrent periods only
   \(1,2,4\); its carrier is all \(n\times n\) matrices and its quotient is
   the \((2n-1)\)-dimensional feasible-margin space.  P103's double-adjugate
   matrix dynamics and P102's involution-norm language must likewise be
   named and zero-credited.  A shared matrix noun is not a collision, but the
   P125 presentation architecture cannot be advertised as new.

### MINOR

1. Replace every unqualified “rank-one correction” by “rank-at-most-one
   correction.”
2. State \(n\ge1\), and record the fixed empty matrix separately if \(n=0\)
   is retained.
3. Define whether “depth” is distance to the recurrent set or to the first
   periodic point; here the two agree, but that should not be implicit.
4. Display the fixed-\(n\) zeta formula instead of saying only that it
   “follows immediately.”
5. Do not call the even hyperplane an “attractor” without specifying the
   finite discrete convention; “complete recurrent set, reached in at most
   one step” is exact.

## 5. Bounded owner search and subtraction

Searches on 2026-08-31 used the exact formula and the equivalent factorised
form, together with `binary matrix row parity transpose rank one dynamics`,
`(I+A11^T)A^T finite field iteration`, `state dependent subgraph complement
odd rows`, `parity Gram map`, and 2025--2026 transpose/complementation
variants.  I read the primary papers above rather than treating snippets as
owners.  No source in this bounded search stated this literal map or its
finite functional graph.

The subtraction is strict:

- transpose, outer products, transvections, feasible binary margins, and
  affine-space counts: zero credit;
- static local/subgraph/pivot/loop complementation and their matrix
  interfaces: zero credit;
- generic finite-map cycle/zeta conversion: zero credit;
- all P102/P103/P125 proof and presentation templates: zero credit;
- residual only: the exact conjunction for the recomputed row-parity update
  \(A\mapsto A^{\mathsf T}+(Ae)(Ae)^{\mathsf T}\).

This is a bounded non-hit, not a claim of novelty, first discovery, or
priority.

## 6. Allowed claim ceiling and release gate

The admissible paper-scale ceiling is:

1. the literal map for \(n\ge1\) and its exact margin quotient;
2. the even hyperplane as image and complete recurrent set, with exact
   entrance time one from the odd coset;
3. the second/fourth-iterate laws and the exact period trichotomy;
4. the complete three-case one-step fibre theorem;
5. fixed, 2-cycle, 4-cycle, depth-one, and fixed-\(n\) zeta formulas.

No claim is allowed for generic rank-one dynamics, local complementation,
transpose actions, binary margins, general finite fields, asymptotics,
priority, or a broad “Gram transpose” class.  Generalisations to
\(\mathbb F_q\), other bilinear forms, or rectangular matrices require new
proofs and owner gates.

**Mandatory release test:** repair the fibre quantifier, boundary and rank
wording; add the explicit affine-margin proof and a genuinely second route;
install the P125 and external-owner firewalls; then rerun the exact verifier.
If those repairs are made without enlarging the claim ceiling, this gate is
**GO_INTERNAL**.  External release remains **HOLD**.
