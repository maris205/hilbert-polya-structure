# HCS-C28 research question

## Frozen question

For every odd prime \(p\), let \(\mathcal L_{s,p}\) be the source-locked
HCS-C27 AGY transfer operator twisted by the full \(p^2\)-dimensional finite
Weil representation.  Can these fixed-prime operators be assembled into one
prime-order-independent Fredholm determinant without erasing chronological
Rauzy dynamics?  If an undamped assembly fails, what is the exact amount of
prime damping required?

The question is divided into four theorem gates.

1. **Local-size gate.** Determine the sharp Schatten growth of
   \(\mathcal L_{s,p}\) as \(p\to\infty\), rather than extrapolating the
   C27 trace-norm upper bound.
2. **Undamped and normalized gates.** Test the unweighted Hilbert direct sum
   and the normalized fibre trace.  These are distinct operations and may
   not be silently interchanged.
3. **Prime-graded repair gate.** For

   \[
   \mathfrak L_{s,z}
   =\bigoplus_{p\ {\rm odd}}p^{-z}\mathcal L_{s,p},
   \]

   determine the exact Schatten and ordinary Fredholm domains.
4. **Arithmetic and dynamical gate.** Verify that the resulting trace keeps
   each chronological word \(g_w\), uses \(\Theta_p(g_w^r)\) under
   repetition, and does not manufacture a common Dirichlet character across
   orbit-dependent discriminants.

## Decisive outcomes

- **Sharp positive repair:** prove
  \(\|\mathcal L_{s,p}\|_{S_q}\asymp p^{2/q}\), and hence
  \(\mathfrak L_{s,z}\in S_q\) exactly when \(q\operatorname{Re}z>3\).
- **Canonicality obstruction:** show that the undamped direct sum is
  noncompact while the normalized-trace large-prime determinant germ loses
  every nonempty positive-word moment and becomes \(1\).
- **Ambient singular control:** determine whether a fixed-plane Rauzy orbit
  makes dimension-normalized marked prime sums diverge.  Any such orbit must
  be scoped to the ledger in which it occurs; it may not be relabeled as a
  C26 induced branch.
- **Route closure:** if a nontrivial determinant requires \(p^{-z}\), then
  \(z\log p\) is an additional clock not derived from the AGY roof.  The
  construction is a prime-graded Dirichlet--Fredholm family, not an adelic
  Weil representation or Hilbert--Pólya operator.

## Scope

This round does not enlarge the small-prime scan, fit Riemann zeros, average
transition matrices, reorder cocycle products, or invoke Route B.  A genuine
adelic oscillator representation would require local \(p\)-adic
representations, an adelic Schwartz space, compatible splittings, and
almost-everywhere reference vectors; residue-field fibres in a direct sum do
not supply those data.
