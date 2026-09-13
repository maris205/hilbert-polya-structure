# Batch 06 — Paper 24 Candidate Review R2 Arithmetic Correction

## Immutable source binding

This append-only correction binds the immutable blind offline review
`BATCH_06_PAPER24_CANDIDATE_REVIEW_R2.md` exactly as follows:

- SHA-256: `914b92255cd9aae2b8be4707484ebf63a72d1b40e1cf1fc356dd365676ed25bd`
- Bytes: `19672`
- LF: `769`
- Terminal line: `PAPER24_CANDIDATE_GATE_PASS_R2`

The bound review remains immutable. This file corrects exactly two local
formula transcriptions found during the parent complete readback. The blind
reviewer's selector, carry, leading-form, visibility, monodromy, spectrum,
wall-gap, recurrence, boundary, portfolio, score, and PASS conclusions are
unchanged.

## Correction 1 — right-branch distance below the wall

Section 2.3 states the correct branch

\[
\ell_m(r)=
\frac{(2m+1)((m-1)r+2)}{m(mr+1)}.
\]

Direct subtraction gives

\[
\boxed{
2-\ell_m(r)
=
\frac{(m+1)(r-2)}{m(mr+1)},
}
\]

not the same fraction without the factor \(m+1\). The corrected expression
is strictly positive for \(m\ge2\) and \(r>2\). The review's conclusion
\(\ell_m(r)<2\) is therefore unchanged. Its displayed formula

\[
\ell_m(r)-1
=
\frac{(m^2-m-1)r+3m+2}{m(mr+1)}
\]

is correct.

## Correction 2 — second coordinate at the third complete step

Section 2.9 correctly states

\[
d_3=u_{3,1}
=8m^4(m+1)(2m+1)s^3.
\]

Its subsequent displayed vector has the correct first coordinate but an
incorrect second coordinate. From

\[
u_2=
\begin{pmatrix}
2m(m+1)(2m-1)(2m+1)s^2\\
4m^3(m+1)s^2
\end{pmatrix}
\]

and

\[
u_3=s
\begin{pmatrix}
0&2m(2m+1)\\
m&m(2m-1)
\end{pmatrix}u_2,
\]

the controlling vector is

\[
\boxed{
u_3=
\begin{pmatrix}
8m^4(m+1)(2m+1)s^3\\
2m^2(m+1)(2m-1)(2m^2+2m+1)s^3
\end{pmatrix}.
}
\]

For \(m=2,s=1\), this gives \(u_3=(1920,936)\), agreeing with the blind
review's own exact falsification table. It also gives

\[
u_{3,1}-2u_{3,2}=2ms\,(s^2L),
\qquad L=2m(m+1),
\]

in agreement with the review's independently derived wall-gap identity.
Only the unused transcription of \(u_{3,2}\) changes; \(d_3\), the visible
degree recurrence, and every headline conclusion remain intact.

## Disposition and unchanged authority

The corrected R2 scores remain:

- proof confidence: `9.3 / 10`;
- standalone value: `7.8 / 10`.

The exact terminal disposition remains PASS for the frozen theorem and its
locked nonclaims. This correction creates no project, source lock,
manuscript, build, release, or external effect.

PAPER24_CANDIDATE_GATE_PASS_R2_CORRECTED
