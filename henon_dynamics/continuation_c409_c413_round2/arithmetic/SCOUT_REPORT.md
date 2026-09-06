# Round-two arithmetic lane: finite-lattice census

Status: one fully derived candidate, **ownership still gated**. This report
does not add a fifth accepted result, allocate a C-number, start a manuscript,
or evaluate a Riemann target. Date: 2026-09-06.

## Outcome

The best candidate is a complete inverse theorem for the ordinary finite-lattice
fixed-point census of hyperbolic matrices in \(\mathrm{SL}_2(\mathbb Z)\).
The entire labelled array
\[
 F_A(q,n)=\#\operatorname{Fix}
    (A^n\mid(\mathbb Z/q\mathbb Z)^2)
\]
is determined by the two period rows \(n=1,2\), and two matrices have the same
array exactly when
\[
 (\operatorname{tr}A,\ c(2A-\operatorname{tr}(A)I))
\]
agrees. Both positive and negative hyperbolic traces are included.

There is a complete classification of the observation's fibres over the
established local-conjugacy classes: each contains one or two such classes,
and the two-class condition is an explicit 2-adic congruence. The proof realizes
every admissible label, proves minimal absolute collision trace 18, and gives
an infinite family. These are not extrapolations from a parameter census.

The full author derivation and a bounded exact diagnostic are ready.
The source audit is not cleared: the original BF literature points to older
two-dimensional results whose precise theorem text has not been retrieved.
The correct present disposition is to retain the candidate without admitting
it to the target count.

## Original shortlist and stopping decisions

Four distinct contracts were considered before the parent narrowed the lane
to the first one. The other three were dropped at concept screening; no
proof, full novelty clearance or numerical test is claimed for them.

| Initial contract | Cheap decisive consideration | Disposition |
| --- | --- | --- |
| Inverse finite-lattice census for hyperbolic \(\mathrm{SL}_2(\mathbb Z)\), retaining every modulus and period label | The standard trace/determinant/matrix-gcd invariant implies census equality, but need not be recovered by it. Odd/even power factorization produced a candidate complete quotient; an explicit pair realizes its non-injectivity. | Advanced to complete author proof and source audit. |
| Rational periodic points of multiplication-induced Lattès maps, classified through torsion and quadratic twists | If the \(x\)-coordinate returns under multiplication by \(m^n\), its lift satisfies \([m^n]P=\pm P\); hence it is torsion. A rational \(x\)-coordinate gives a point over a field of degree at most two. No mechanism beyond this standard torsion reduction was identified. [DeMarco–Wang–Ye](https://arxiv.org/abs/1311.1792) explicitly place Lattès preperiodicity in the torsion setting. | Dropped for lack of a separated residual theorem; not a claim that every possible uniform rational classification is already proved. |
| Ordinary periodic counts of a hyperbolic toral action descended to the Cayley cubic | The torus/inversion quotient reduces a fixed quotient point to \(A^nP=P\) or \(A^nP=-P\), with stabilizer corrections. A new formula without an additional inverse or ramification mechanism would risk being only a quotient-counting specialization. | Dropped before a full source/proof audit. No discovery claim or universal formula was recorded. |
| Local-global detection of a power-map orbit meeting a torus translate | The initially proposed power-map/torus-translate branch is already in the explicitly stated scope of [Hsia–Silverman, *On a dynamical Brauer–Manin obstruction*](https://www.numdam.org/articles/10.5802/jtnb.668/) (2009). | Dropped as an overlap at the proposed scope; no attempt to broaden the subvariety class. |

No new arithmetic candidate was opened after the parent instructed this lane
to focus exclusively on the finite-lattice inverse and its BF ownership.

## Complete fibre statement

Write \(t=\operatorname{tr}A,\ h=c(2A-tI)\), and
\(g=\gcd(A_{12},A_{21},A_{22}-A_{11})\).
Local conjugacy is governed by the classical BRW invariant \((t,\det A,g)\);
that theorem is credited, not claimed.

- If \(t\) is odd, the possible \(h\)'s are exactly the positive odd integers
  with \(h^2\mid t^2-4\). The census fibre has one local class, \(g=h\).
- If \(t=2T\), write \(h=2r\). The possible \(r\)'s are exactly the positive
  integers with \(r^2\mid T^2-1\). Put \(D=(T^2-1)/r^2\).
  The fibre has the class \(g=r\), and also the class \(g=2r\) precisely when
  \(D\equiv1\pmod4\). There are no further local classes.

For instance,
\[
 A=\begin{pmatrix}1&4\\4&17\end{pmatrix},\qquad
 B=\begin{pmatrix}5&8\\8&13\end{pmatrix}
\]
have the same array for every \(q,n\), but \(B\equiv5I\pmod8\) while \(A\)
is nonscalar modulo 8. Their failure of local linear conjugacy is therefore
immediate. This differs from the familiar \(A\) versus \(A^{-1}\) ambiguity:
inversion stays inside the same BRW local-conjugacy class.

The key elementary identities, with \(u_0=0,u_1=1\) and
\(u_{m+1}=tu_m-u_{m-1}\), are
\[
 A^{2m+1}-I=(u_{m+1}+u_m)A^m(A-I),\qquad
 A^{2m}-I=u_mA^m(2A-tI).
\]
They control the first Smith invariant at every period. The content of
\(A-I\) is then proved redundant, leaving only \((t,h)\).

## Deliverables and reproducible checks

- [FINITE_LATTICE_CENSUS_PROOF.md](FINITE_LATTICE_CENSUS_PROOF.md):
  all-quantifier proof, admissibility, explicit representatives, minimality,
  infinite family, and precise observation/clock limitations.
- [finite_lattice_exact_checks.py](finite_lattice_exact_checks.py):
  standard-library-only exact diagnostic; writes no files.
- [SOURCE_AUDIT.md](SOURCE_AUDIT.md):
  inspected primary material, exact BF distinctions, retrieval limits,
  and the material older-source gate.

Run from this directory:

~~~sh
python -B finite_lattice_exact_checks.py
~~~

The diagnostic passes 72 Smith-content identities on six fixed signed matrices,
1,080 directly enumerated kernels at \(1\le n\le12,\ 2\le q\le16\), the positive
and negative trace-18 pair comparisons, the scalar/non-scalar obstruction
modulo 8, and six selected admissibility/representative cases.
It is deliberately not an expanded parameter census. Universal quantifiers
and the absence of additional fibre classes rest on the proof, not the script.
No frozen first-round result was re-tested.

## Scope and required next decision

The owner is the ordinary forward map on each labelled finite lattice.
The iteration clock is \(n\). The modulus \(q\) is not a second iteration clock
and is not a prime selected to fit a target spectrum. At each fixed \(q\),
the ordinary finite-set zeta has reciprocal
\(\det(I-zP_{A,q})\), where \(P_{A,q}\) is the finite permutation matrix.
That determinant is not a Hilbert–Pólya operator or a Riemann determinant.

No Euler-prime bridge, target zeros, gamma factor, functional equation, same-owner
Weil form, or target quantization is supplied. Canonical Route-A controls and
target metrics have not been run; absence of them is not a positive score.
No formal evaluator output is created.

An independent mathematical/substantive review belongs to the parent.
The author-side source recommendation is **PRIORITY_NOT_CLEARED**:
obtain the exact older BF recurrence statements and decide the residual
contribution against them before any fifth-slot or manuscript decision.
The applicable proof-writer and source-verification workflows were used to
separate universal proof, finite diagnostics, attributed ingredients, and
publication priority; none substitutes for another.
