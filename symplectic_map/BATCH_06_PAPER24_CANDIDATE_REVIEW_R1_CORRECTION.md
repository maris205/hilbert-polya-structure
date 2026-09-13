# Batch 06 — Paper 24 Candidate Review R1 Arithmetic Correction

## Immutable source binding

This append-only correction binds the immutable review
`BATCH_06_PAPER24_CANDIDATE_REVIEW_R1.md` exactly as follows:

- SHA-256: `b2802f24ca5de3d91b7ea5a1726a0cf12d6f36053055e24e3759124bfc8709c1`
- Bytes: `30703`
- LF: `878`
- Terminal line: `PAPER24_CANDIDATE_GATE_PASS_R1`
- Date scope: 2026-08-25 UTC

The bound review remains immutable. This file corrects exactly two local
arithmetic/transcription statements found during the parent complete
readback. Neither correction changes a selector, chamber image, carry
inequality, degree vector, monodromy matrix, eigenvalue, recurrence, score,
scope restriction, or PASS disposition.

## Correction 1 — right-chamber lower bound

Section 2.3 of the bound R1 gives the correct branch

\[
\ell_m(r)=
\frac{(2m+1)((m-1)r+2)}{m(mr+1)}.
\]

Its displayed numerator for \(\ell_m(r)-1\) omits the term \(-mr\). The
controlling identity is

\[
\boxed{
\ell_m(r)-1
=
\frac{(m^2-m-1)r+3m+2}{m(mr+1)}.
}
\]

Indeed,

\[
(2m+1)(m-1)-m^2=m^2-m-1,
\]

and

\[
2(2m+1)-m=3m+2.
\]

For every \(m\ge2\) and \(r>2\), the corrected numerator is strictly
positive. The bound review's conclusion \(\ell_m(r)>1\) is therefore
unchanged. Its separate identity

\[
2-\ell_m(r)=
\frac{(m+1)(r-2)}{m(mr+1)}
\]

is already correct.

## Correction 2 — negative-chamber visibility equality

Section 2.6 compares the first complete \(q\)-degree with the second final
\(p\)-degree in the \(r<2\) chamber. If \(v=A_-u\), then

\[
u_1'=s(2m+1)v_1,
\qquad
u_2'=smv_2,
\qquad
h_m(r)=\frac{u_1'}{u_2'}.
\]

Consequently the controlling relation is the equality

\[
\boxed{u_1'=sm\,h_m(r)v_2,}
\]

not a strict inequality at that first comparison. Visibility is still
strict because \(s\ge1\), \(m\ge2\), and \(h_m(r)>2\), so

\[
u_1'=sm\,h_m(r)v_2>v_2.
\]

Also \(u_1'=s(2m+1)v_1>v_1\). Thus \(q_1\) remains strictly larger than
both final \(p\)-coordinates, exactly as required by the frozen theorem.

## Disposition and unchanged authority

The corrected R1 scores remain:

- novelty: `7.9 / 10`;
- standalone scope: `8.0 / 10`;
- proof plausibility: `9.4 / 10`.

The frozen candidate remains the characteristic-zero family

\[
V_m=Aq_1^m q_2^2+Bq_1q_2^{2m},
\qquad
W_{m,s}=Cp_1^{s(2m+1)+1}+Dp_2^{sm+1},
\]

with \(m\ge2\), \(s\ge1\), and \(A,B,C,D\ne0\). All R1 nonclaims and
downstream authoring requirements remain unchanged. This correction creates
no project, source lock, manuscript, build, release, or external effect.

PAPER24_CANDIDATE_GATE_PASS_R1_CORRECTED
