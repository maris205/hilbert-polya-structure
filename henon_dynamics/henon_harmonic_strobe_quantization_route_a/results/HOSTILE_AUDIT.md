# Hostile mathematical audit

This audit was performed before the paper skeleton, repeated after the
round-two manuscript, and repeated once more after the real-time/metaplectic
parameter correction.

## Attacks and resolutions

1. **Could a nonidentity planar rotation fix a nonzero vector?**  No.  Its
   matrix minus identity has determinant \(4\sin^2(\theta/2)>0\).
2. **Does irrationality prove the absence of every resonance?**  Yes.  If
   \(n\theta\in2\pi\mathbb Z\), then \(\theta/(2\pi)\) is rational.
3. **Could a rational resonant plane be assigned one fixed component?**  No.
   Artin--Mazur uses fixed-point cardinality, not component count.
4. **Is the zero-angle edge missing?**  No.  It is the reduced fraction
   \(0/1\), and the series fails at its first coefficient.
5. **Is the Gaussian measure normalized and invariant?**  Yes.  Radial
   integration gives total mass one, and the rotation preserves both radius
   and Jacobian.
6. **Is the angular sign consistent with the Hamilton flow?**  Yes.  The
   frozen coordinate is \(q-ip=re^{i\varphi}\), which advances by
   \(\theta\), so the Koopman phase is \(e^{im\theta}\).
7. **Does the Laguerre coefficient really normalize the basis?**  Yes.  The
   exact generalized-Laguerre integral cancels \(k!/(k+|m|)!\).
8. **Does density of irrational eigenvalues imply a dense eigenspace?**  No.
   The claim concerns the eigenvalue set; the basis separately proves that
   the whole Gaussian space is pure point.
9. **Does each eigenvalue have infinite multiplicity?**  Yes.  The radial
   index \(k\) is unrestricted.  Rational angles also identify infinitely
   many angular indices modulo \(b\).
10. **Could either unitary nevertheless be compact?**  No.  Each maps an
    infinite orthonormal sequence to another orthonormal sequence.
11. **Is the quantum time the classical time?**  Yes.  The exact Egorov
    identities rotate \((\widehat q,\widehat p)\) by the same \(\theta\).
12. **Could the oscillator zero-point phase be silently removed?**  No.  The
    frozen generator is \(\widehat H=N+1/2\); no scalar phase convention is
    changed after inspection.
13. **Does the classical \(2\pi\) period make the quantum unitary
    \(2\pi\)-periodic?**  No.  Physical time is \(\theta\in\mathbb R\), and
    the Hermite phases give \(Q_{\theta+2\pi}=-Q_\theta\) and
    \(Q_{\theta+4\pi}=Q_\theta\).  Only the projective quantum class has the
    classical period.
14. **Can rational quantum phases be indexed only by an angle modulo one?**
    No.  For the exact real-time representative
    \(\theta/(2\pi)=a/b\), the phase set is the \(b\)-th roots rotated by
    \(e^{-i\pi a/b}\).  Replacing \(a\) by \(a+b\) retains the classical
    strobe but multiplies the quantum operator by \(-1\).
15. **Does complex conjugation reverse the propagator?**  Yes.  It fixes
    \(\widehat H\) but conjugates the scalar \(i\).
16. **Can heat damping supply the missing determinant?**  It supplies a
    determinant for a different imaginary-time trace-class operator, not for
    either physical unitary.
17. **Can A4 repair the failed arithmetic and orbit gates?**  No.  Route-A
    coordinates belong to one candidate but do not substitute for one
    another; A0--A3 remain failed.
18. **Do finite sentinels prove the theorem?**  No.  They only detect drift in
    formulas that are proved for all indices and angles.

## Verdict

The unified spectral ledger survives.  It is a complete source theorem and
a decisive determinant/arithmetic obstruction, not a target-spectrum or
Hilbert--Pólya construction.
