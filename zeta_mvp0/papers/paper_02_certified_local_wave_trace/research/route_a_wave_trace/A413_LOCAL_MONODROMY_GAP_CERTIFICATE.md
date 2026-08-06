# A4.13 — Uniform transverse monodromy gap on the validated local branch

## Claim

Fix

\[
 a=\frac{51}{50},
 \qquad
 0\leq\epsilon\leq0.101,
 \qquad
 \delta=\epsilon^2,
\]

and let \(\gamma_\epsilon\) be the primitive full-return branch certified in
[A4.12](A412_CONTIGUOUS_FAST_BRANCH_CERTIFICATE.md).  Let

\[
 M_\epsilon
 =D_z\Phi_\epsilon^{T(\epsilon)}(z_\epsilon)
\]

denote the physical four-dimensional, fixed-time monodromy matrix at the
periodic point, and let \(D\Pi_\epsilon\) denote the derivative of the local
return map on the two-dimensional section obtained by intersecting
\(K_\epsilon=1\) with \(P_+=0\).  Then this section is transverse along the
certified branch and

\[
 \boxed{
 \det(I-D\Pi_\epsilon)
 =4-\operatorname{tr}M_\epsilon>3
 }
 \qquad(0\leq\epsilon\leq0.101).
\]

The quantifier is restricted to the A4.12 branch inside its frozen primary
root boxes and guarded bridge hulls.  No assertion is made about periodic
orbits elsewhere on the energy shell.

## Status

**PROVABLE AS STATED — local-branch computer-assisted theorem.**

The proof combines exact Hamiltonian reduction with the accepted
`R401-VAL-L1-MG-V2` interval archive.  Its authorized machine status is
`PASS_LOCAL_MONODROMY_GAP`, with `final_status: null`.

## Assumptions and frozen inputs

1. A4.12 supplies one real-analytic primitive full-return branch covering
   every \(\epsilon\in[0,0.101]\), together with validated CAPD C1
   enclosures of the physical state derivative \(M_\epsilon\).
2. The event hyperplane is \(P_+=0\), and every accepted transcript encloses
   the corresponding phase slope with a strictly positive lower endpoint:
   \(\partial_{Q_+}K_\epsilon>0\).
3. \(\Phi_\epsilon^t\) is the exact autonomous Hamiltonian flow of
   \(K_\epsilon\).  Hence it preserves both \(K_\epsilon\) and the
   symplectic form.
4. The arithmetic and release objects are those frozen in
   `R401_VAL_L1_MONODROMY_GAP_FREEZE.md`; all displayed decimal bounds obey
   the protocol's exact rational floor/ceil policy.

## Proof strategy and dependency map

The proof has two logically separate parts.

1. **Exact reduction.**  Regularity and event transversality identify the
   derivative of the Poincare return with the map induced by
   \(M_\epsilon\) on
   \(\ker dK_\epsilon/\operatorname{span}(X_{K_\epsilon})\).  The resulting
   invariant flag factors the characteristic polynomial without assuming
   diagonalizability of the two unit multipliers.
2. **Validated inequality.**  Exact-rational outward evaluation of
   \(4-\operatorname{tr}M_\epsilon\) on every frozen primary and bridge
   transcript gives a lower endpoint strictly greater than \(3\).

The first part uses only exact Hamiltonian identities and the certified
positive phase slope.  The second part uses the already accepted A4.12
cover and the independently replayed `R401-VAL-L1-MG-V2` proof objects.

## Proof

### Step 1: the energy shell and event section are regular

Fix a point \(z=z_\epsilon\) on the certified periodic orbit and write

\[
 V=T_z\mathbb R^4,
 \qquad
 \alpha=dK_\epsilon(z),
 \qquad
 v=X_{K_\epsilon}(z),
 \qquad
 L=\operatorname{span}\{v\}.
\]

The transcript-level phase gate proves

\[
 \partial_{Q_+}K_\epsilon(z)>0.
\]

Therefore \(\alpha\ne0\), so \(K_\epsilon=1\) is a regular
three-dimensional energy surface near \(z\).  Hamilton's equation gives

\[
 \dot P_+=-\partial_{Q_+}K_\epsilon(z)\ne0.
\]

Thus the hyperplane \(P_+=0\) is transverse to the flow.  Its intersection
with the regular energy shell is a local two-dimensional Poincare section,
and \(D\Pi_\epsilon\) is well defined there.

### Step 2: construct the invariant flag

Because \(dK_\epsilon(X_{K_\epsilon})=0\), one has \(L\subset\ker\alpha\).
Let \(M=M_\epsilon\).  Flow covariance and the full periodic return give

\[
 Mv
 =D\Phi_\epsilon^{T(\epsilon)}(z)X_{K_\epsilon}(z)
 =X_{K_\epsilon}(\Phi_\epsilon^{T(\epsilon)}(z))
 =v.
\]

Energy conservation, differentiated with respect to the initial state at
fixed time \(T(\epsilon)\), gives

\[
 \alpha\circ M=\alpha.
\]

Consequently

\[
 0\subset L\subset\ker\alpha\subset V
\]

is an \(M\)-invariant flag.  The induced map on \(L\) is the identity.  The
induced map on the one-dimensional quotient \(V/\ker\alpha\) is also the
identity, since \(\alpha(Mw-w)=0\) for every \(w\in V\).

### Step 3: identify the middle quotient with the return derivative

The tangent space to the energy shell is \(\ker\alpha\), and changing the
return time changes a variational vector by a multiple of the flow vector
\(v\).  Hence the derivative of the event return is conjugate to the map
induced by \(M\) on

\[
 \ker\alpha/L.
\]

The transversality proved in Step 1 makes this quotient-to-section
identification an isomorphism.  Thus the middle quotient map is precisely
\(D\Pi_\epsilon\), up to this canonical conjugacy.

Characteristic polynomials multiply along an invariant flag.  The identity
maps on the first and last one-dimensional factors therefore give

\[
 \chi_{M_\epsilon}(t)
 =(t-1)^2\chi_{D\Pi_\epsilon}(t),
 \qquad
 \operatorname{tr}M_\epsilon
 =2+\operatorname{tr}D\Pi_\epsilon.
\]

This factorization uses an invariant filtration, not an eigenbasis.  It
therefore remains valid if the unit multiplier has a nontrivial Jordan block
or algebraic multiplicity four.

### Step 4: use the reduced symplectic form

With the Hamiltonian convention used here,
\(\ker\alpha\) is the symplectic orthogonal of \(L\).  The symplectic form
therefore descends to a nondegenerate two-form on \(\ker\alpha/L\).
Since \(M_\epsilon\) is the derivative of an exact Hamiltonian flow, it
preserves this reduced form.  Equivalently, the two-dimensional return
derivative is symplectic, and hence

\[
 \det D\Pi_\epsilon=1.
\]

For any two-by-two matrix \(A\),
\(\det(I-A)=1-\operatorname{tr}A+\det A\).  Combining this identity with
the preceding trace factorization yields the exact equality

\[
 \det(I-D\Pi_\epsilon)
 =2-\operatorname{tr}D\Pi_\epsilon
 =4-\operatorname{tr}M_\epsilon.
\]

### Step 5: apply the validated directional bounds

For each of the 202 accepted CAPD transcripts, the analyzer and the
no-analyzer-import checker parse the decimal endpoints as exact rational
numbers and evaluate outwardly

\[
 [D_M]
 =\left[
 4-\sum_{j=0}^{3}M_{jj}^{+},
 4-\sum_{j=0}^{3}M_{jj}^{-}
 \right].
\]

The physical diagonal entries are the archived flattened indices
\(0,7,14,21\); the augmented parameter and period coordinates are excluded.
All 101 determinant intervals pass at each frozen precision (202 total), and
every paired 128/256-bit interval intersects.  The authoritative minimum lower
endpoints are

\[
 \frac{479499075830964647977619704227032239226154693}
 {125000000000000000000000000000000000000000000}
 >3
\]

at 128 bits and

\[
 \frac{385074196894579469387613658291110538545744780951414621536980801422153198627515135319}
 {100000000000000000000000000000000000000000000000000000000000000000000000000000000000}
 >3
\]

at 256 bits.  Their rigorous 18-place downward displays are, respectively,

\[
 3.835992606647717183,
 \qquad
 3.850741968945794693.
\]

The maximum interval widths have the rigorous upward displays

\[
 0.054493101512001146
 \quad(128\text{ bits}),
 \qquad
 0.025036862429395394
 \quad(256\text{ bits}).
\]

The minimum phase-slope lower endpoint has authoritative exact value

\[
 \frac{111938012055954323433615300299077846499814991}
 {12500000000000000000000000000000000000000000}
\]

and rigorous downward display \(8.955040964476345874\).  Thus the regularity
and transversality premise used in Steps 1--3 also holds uniformly on every
certified job.

The independent checker passes 202/202 determinant replays, 202/202
phase-slope replays, all 815 directed-decimal payloads, and 8302 aggregate checks, with
zero failures.  The full current regression suite passes 74 tests.  Because
the primary slabs cover \([0,0.101]\) and the bridge certificates identify
their local representatives as the single A4.12 branch, the lower bound
holds for every \(\epsilon\) in the claimed interval.  Combining it with the
exact identity in Step 4 proves

\[
 \det(I-D\Pi_\epsilon)>3
 \qquad(0\leq\epsilon\leq0.101).
\]

This proves the claim. \(\square\)

## Audit and claim boundary

The accepted archive is `results/r401_val_l1_monodromy_gap/`, governed by
`R401-VAL-L1-MG-V2`.  Exact numerator/denominator pairs are authoritative;
lower displays are exact decimal floors and upper displays are exact decimal
ceilings.  The independent checker replays stored arithmetic but does not
perform a second validated ODE integration.

The predecessor V1 release is retained as
`results/r401_val_l1_monodromy_gap.attempt1-superseded-nondirected-display/`.
Its exact-fraction \(D>3\) core was not invalidated, but its nearest-float
Markdown bounds lacked directional guarantees and are non-licensing.  Only
the prospectively re-frozen V2 release supports the displayed bounds and
the theorem status used here.

A4.13 closes the uniform \(D>3\) inequality **only on the already validated
local branch**.  It does not supply any of the following:

- an independent event-projected computation of \(D\Pi_\epsilon\);
- the shared-parameter Taylor-model identity remainder below \(2^{-30}\) or
  the alternative identity residual below \(2^{-28}\);
- exclusion of roots in the local-box complement;
- the complete phase tree or global energy-shell cover;
- promotion of \(\delta_{\rm tr}\), \(\delta_{\rm nd}\), or \(P_0\);
- an endogenous prime-time law, a Hilbert--Polya operator, zeta-zero
  reconstruction, or RH.

In particular, the interval widths displayed above are much larger than
\(2^{-30}\).  They suffice for the strict local inequality because their
lower endpoints exceed \(3\), but they do not satisfy the separate frozen
identity-cross-check gate required for a final R401-VAL status.
