# HCS-C57 narrative report

Status: **RELEASE_FROZEN; DOCS_FINAL_NO_MORE_EDITS; PAPER_COMPILED;
PAPER_HOSTILE_PASS; theorem narrative locked; machine
PREFREEZE_CODE_RESULTS_PASS.**

## 1. From a cubic surface to a minimal cohomological jump

HCS-C55 extracted a Q-defined cubic surface from the four-dimensional
equivariant Yukawa tensor. HCS-C56 then computed the full arithmetic of its
27 lines: one connected degree-27 line field and a normal closure with Galois
group \(W(E_6)\).

That result creates a precise next obstruction. Over \(\mathbf Q\), the full
Weyl action leaves no algebraic Brauer class. The natural question is not
merely whether some large extension creates a class, but how early a
2-primary class can appear and whether it can be written down.

C57 answers this with a divisibility theorem:

\[
\left(
\operatorname{Br}(Y_L)/\operatorname{im}\operatorname{Br}(L)
\right)[2]\ne0
\Longrightarrow
36\mid[K\cap L:\mathbf Q]\mid[L:\mathbf Q].
\]

Degree 36 is attained by the fixed field of a double-six stabilizer. The
result is sharpened by a canonical quaternion representative.

## 2. Why the universal proof has two branches

A tempting shortcut is to say that every nonzero 2-primary class stabilizes
one double-six. That is too broad. The complete classical theorem separates:

\[
\mathbf Z/2\longrightarrow U_1\text{ of index }36,
\]

\[
(\mathbf Z/2)^2\longrightarrow U_3\text{ of index }720.
\]

Both indices are divisible by 36, which proves the main divisibility. Only
the first branch can attain degree 36. This distinction is essential: the
machine can verify the selected \(U_1\), but the universal quantifier over all
finite extensions comes from the complete source theorem.

## 3. The attaining field

Write the unordered double-six as
\(D=\{\mathcal E,\mathcal G\}\), where \(\mathcal E\) and \(\mathcal G\)
denote the effective sums of its two sixers. It has stabilizer

\[
U_1\cong S_6\times C_2.
\]

Its index-two subgroup

\[
U_1^+=\operatorname{Stab}(\mathcal E)\cap
\operatorname{Stab}(\mathcal G)\cong S_6
\]

preserves the two sixers separately.

Its fixed field

\[
F_D=K^{U_1}
\]

has degree 36. The 36 conjugate embedded fields correspond exactly to the 36
double-sixes and form one Q-isomorphism type.

Two exact invariants describe the same field:

\[
\mathbf Q(\theta_D)=F_D=\mathbf Q(\delta_D).
\]

The first records the unordered twelve-line configuration. The second is the
square of an oriented invariant. Their equality is a Galois-stabilizer
theorem. The unfinished large computation of an expanded
\(\delta=P(\theta)\) is deliberately excluded.

## 4. From twelve lines to a compact quartic

The selected double-six consists of twelve lines. Over \(F_D\), their
\(d\)-coordinates form an exact degree-12 factor \(A_{12}\) of the HCS-C56
degree-27 eliminant.

One could try to print a huge quartic with 31 coefficients in the
degree-36 field. C57 instead gives a canonical determinant definition.

First, quartics are reduced modulo the cubic equation. The four deleted
monomials form a valid gauge because the relevant \(4\times4\) block is
triangular with diagonal

\[
75081586157
\]

and nonzero determinant

\[
31778526453059635681033276764499400992765201.
\]

Restricting the remaining 31 monomials to the twelve lines gives 60 linear
conditions. A locked nonzero 30-by-30 minor and a geometric upper bound prove
that the matrix has rank 30. Normalizing one coefficient to one then defines
the unique quartic \(Q_D\) by Cramer's rule.

## 5. Why the divisor is exact

The restriction equations show that \(Q_D\) vanishes on the twelve lines, but
that alone does not exclude a residual curve. Let \(H_Y\) denote the
hyperplane class on \(Y\). The divisor has class \(4H_Y\) and degree 12.
Twelve distinct line components already have degree 12, so there is no room
for residual components or multiplicity:

\[
\operatorname{div}_{Y_{F_D}}(Q_D)=\mathcal E+\mathcal G\sim4H_Y.
\]

This degree-exhaustion step converts a linear-algebra output into a geometric
theorem.

## 6. The quaternion class

The index-two subgroup \(U_1^+\cong S_6\) separates the two sixers and gives

\[
F_D'=K^{U_1^+}=F_D(\sqrt{\delta_D}).
\]

Put \(\mathcal L_0=\operatorname{div}_Y(u_0)\). Then

\[
\operatorname{div}_{Y_{F_D}}(Q_D/u_0^4)
=\mathcal E+\mathcal G-4\mathcal L_0
=\operatorname{Norm}_{F_D'/F_D}
(\mathcal E-2\mathcal L_0).
\]

Thus

\[
(\delta_D,Q_D/u_0^4)
\]

is unramified. Its cocycle is the standard nonzero double-six cocycle, so the
class generates

\[
\operatorname{Br}(Y_{F_D})/\operatorname{im}\operatorname{Br}(F_D)
\cong\mathbf Z/2.
\]

Unramifiedness, nontriviality, and local evaluation are three different
questions. C57 proves the first two and makes no claim about the third.

## 7. Novelty boundary

The 36 double-sixes, their stabilizer, the order-two classification, and
general degree-36 resolver constructions are prior mathematics. The bounded
screen did not locate the exact field, orientation square, determinant
quartic, and quaternion package for this frozen surface.

Accordingly the contribution is presented as an exact instance theorem and a
sharp organizing divisibility result. It is not described as the first
double-six resolver.

## 8. Current state

The mathematical route is locked, and the project-local machine certificate,
strict schema, independent checker, scoped manifest, 33/33 tests, and 535/535
rebound pass at `PREFREEZE_CODE_RESULTS_PASS`. The official 18-file paper
source, 24-page PDF, compilation report, independent hostile paper audit, final
root audit, external formal-package binding, implementation identity,
self-excluding 64-entry manifest, and byte-identical archived Route also pass.
P57 therefore records `RELEASE_FROZEN` and `DOCS_FINAL_NO_MORE_EDITS` while
preserving the machine layer. Temporary feasibility and `/tmp` transport
results cannot be cited as release provenance.

No later-batch topic has been selected.
