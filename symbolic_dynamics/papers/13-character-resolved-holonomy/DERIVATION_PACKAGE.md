# SD-C15 Derivation Package

## Object-to-formula chain

```text
tensor-prime full shifts F_p
  -> entropy order and loop roof log p
  -> recurrent adjacent atom graph
  -> positive cross-step cocycle kappa in Z
  -> autonomous Z-skew symbolic extension
  -> Bloch fibers L_s(exp(i theta))
  -> one character-resolved Fredholm family
  -> Euler determinant in Fourier degree zero
  -> charged mixed returns in positive Fourier degrees.
```

## Periodic-orbit expansion

For small `z`,

```text
log det(I-zL_s(w))
 = -sum_(r>=1) z^r Tr(L_s(w)^r)/r.
```

Every matrix monomial is a length-`r` closed base word.  Its `w` exponent is
the cocycle displacement of the lifted word.  Degree zero therefore counts
periodic lifted words.  Since the cocycle is zero on loops and positive on
cross edges, this coefficient contains exactly the pure atom repetitions.

## Why this is not coordinatewise splicing

The lifted shift, the deck translation, the Fourier transform, every Bloch
fiber, and the coefficient-zero trace all belong to one translation-invariant
symbolic transfer object.  We do not import Paper 06's Gamma factor, Paper
07's separate chiral determinant, Paper 08's free-group trace, or Paper 12's
Fuglede--Kadison magnitude.

## What the new variable means

The character is dual to the intrinsic cross-step displacement.  It is not a
phase selected from target zeros.  Nonzero Fourier degree measures how many
cross steps a recurrent base word makes before closing in the base; degree
zero measures which such words actually close in the skew extension.

## Exact obstruction at reversal

For a two-edge return, the product of character labels is
`w^(q+qbar)`.  Positive labels keep it outside the target coefficient.  An
inverse label makes the exponent zero.  The same operation that restores
edge reversal therefore restores the unwanted mixed periodic lift.

## Claim boundary

The construction is an analytic, character-resolved symbolic determinant in
the Euler half-plane.  It does not prove that any resolved zero is a Riemann
zero, and no individual unitary character fiber retains the exact Euler
ledger.  It does not authorize a zero census or provide a canonical character
slice.  Generic controls decide whether transverse motion is
arithmetically informative; they do not alter the exact tensor-prime A0
source.
