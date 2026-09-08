# LY4 independent internal helper review

2026-09-08 UTC. Reviewer: current-team non-author of the LY4 package.

**Verdict: `PASS_INTERNAL_HELPERS_ONLY`.** No required mathematical
correction was found in the three auxiliary claims or their supplied
proofs. The full classification remains `NOT CURRENTLY JUSTIFIED`.
This is not contract admission, human peer review, global-priority
verification, or independent computational reconstruction.

## Scope and inspected inputs

Read in full:

- [FROZEN_CONTRACT.md](FROZEN_CONTRACT.md).
- [PROOF_PACKAGE.md](PROOF_PACKAGE.md), including Steps 1–5, the
  degenerate branches and the computation/claim boundary.
- [core_falsifier.py](core_falsifier.py), for static algorithm review only.

Selected sections of [FINITE_ALPHABET_RESULT.json](FINITE_ALPHABET_RESULT.json)
were read: the alphabet and sample counterexamples, period-count block,
and trailing scope/execution metadata. The complete cycle list was not
independently recounted or revalidated. The stored counts therefore
remain the author's output, not this reviewer's new certificate.

The following SHA-256 values identify the bytes at review time. Reading
these hashes is a static integrity check, not a mathematical rerun:

| Input | SHA-256 |
|---|---|
| `PROOF_PACKAGE.md` | `8d6449baf10cab57f49de0c5ee48a0d5fea34dadbc19588fc331744e3f7cbe96` |
| `FROZEN_CONTRACT.md` | `b55dc86ccee5408429200456adb5ce261a8a1182679b01524e02be8cde408b7c` |
| `core_falsifier.py` | `62fdbd8aa099ce8b9d0fc8a069a086c26a30f32d18ce6c8b5493d84de9a80773` |
| `FINITE_ALPHABET_RESULT.json` | `a4250ab11dd4f85afa3e57064bdf0298b0e7239d86b5835ef7015a922fa0bfab` |

No mathematical program was run or imported. Only this new review file
was authored; all author proofs, scripts and results were left unchanged.
The source-ownership audit and the author's forthcoming report links
are outside this narrow helper review.

## 1. Identity and clock: PASS

For the ordinary nonzero scalar recurrence
$$x_i x_{i+3}=a+x_{i+1}+x_{i+2},$$
subtracting adjacent equations gives
$$x_{i+1}(x_{i+4}+1)=x_{i+3}(x_i+1).$$
Multiplying this equality by the common factor $x_{i+2}+1$ proves
$\kappa_{i+2}=\kappa_i$ without dividing by a possibly zero plus-factor.
Thus the identity remains valid on the $-1$ stratum.

The four-state successor preserves $a=xw-y-z$ by direct substitution.
Its ordinary nonzero cyclic scalar words satisfy the original equations.
The scalar least period and consecutive-triple least period agree,
since either equality of sequences supplies equality of the triples,
or equality of all iterated triples supplies equality of their first
coordinates. No extra quotient or reversal is introduced.

## 2. Alternating 2-integrals: PASS as stated

All hypotheses used are stated: integer and nonzero scalar coordinates,
periodicity, no coordinate $-1$, and least period greater than two.
Repeating an odd period to obtain an even cyclic presentation is valid;
it does not assert that the resulting presentation length is least.

For any two even indices, subtraction of
$$u x_{i+1}=(x_i+1)(x_{i+2}+1)$$
and the exact product-difference identity give
$|u|_pD_o\leq D_e$. Every odd pair occurs as the successors of an even
pair in the finite cyclic presentation. Odd indices give the second
inequality $|v|_pD_e\leq D_o$. All plus-factors have norm at most one
because the coordinates are integers; the inequality directions are
correct.

If $|u|_p>1$, every odd coordinate is in $p\mathbb Z_p$. Its plus-factor
is therefore a unit, so $|v|_p=1/|x_i|_p\geq1$ for each even coordinate.
Consequently $|uv|_p>1$, the two diameter inequalities force $D_e=0$
and then $D_o=0$, and the scalar period divides two. The contradiction
proves $p$-integrality of $u$, and exchanging the named parities proves
it for $v$. These statements hold for every prime; rationality then
gives $u,v\in\mathbb Z$. Their nonzero property follows from the
excluded $-1$ factors and nonzero denominators.

The period restriction cannot be dropped. For example, the repeated
integer word $(1,3)$ occurs at $a=-1$, has native period two and gives
alternating values $4/3$ and $16$. This boundary check is consistent
with the author's stated exclusion, not a counterexample to the lemma.

## 3. Complete $-1$ stratum at $a\ne1$: PASS

The four-step propagation is justified by the nonzero coordinate that
multiplies $x_{i+4}+1$. A common multiple of the period and four gives
a legitimate cyclic block presentation $(-1,b_j,c_j,d_j)$.

When no $b_j=-1$, multiplying
$$c_j(b_{j+1}+1)=-(b_j+1)$$
is legitimate: all factors being canceled are nonzero. The result
$\prod_jc_j=(-1)^m$ and nonzero integer coordinates force each
$c_j=\pm1$. A single $c_j=-1$ propagates to all blocks. The recurrence
then makes $b_j$ constant and gives the claimed four-word. If all
$c_j=1$, the two formulas for $d_j$ give exactly $2a=2$, excluded by
the statement. There is no missing mixed-sign case.

When some $b_j=-1$, the same identity forces all $b_j=-1$. The remaining
recurrence is
$$c_{j+1}=\frac{a-2}{1-a-c_j}.$$
Its denominator is $d_j$, already nonzero in the ordinary domain.
At $a=2$ it produces a forbidden zero, so that degenerate matrix is
correctly discarded before the invertible Möbius argument.

For $a\ne2$, the representing matrix has eigenvalues $-1$ and $2-a$.
Outside $a=3$ they are distinct. A non-eigenline can be periodic only
if their real quotient is a root of unity; the only exceptional
parameters here are $a=1$ and $a=3$. The former is outside the claim.
At $a=3$ the explicit nontrivial nilpotent part has square zero, and
every positive matrix power has the same unique eigenline. This
correctly rules out additional nonfixed cycles in the Jordan case.

The fixed-point polynomial factors as
$(c+1)(c+a-2)$, yielding precisely the two stated block forms. Each
is a rotation of $(-1,b,-1,1-a-b)$. The converse substitution and the
least-period split into one, two and four cover all cases, provided
the two free-position coordinates remain nonzero as explicitly required.

## 4. Unbounded six-period family: PASS with the stated scope

For $M\geq5$, the six scalar equations for
$$(-M,M-1,1,-2,1,M-1),\qquad a=M,$$
have the six parameter values printed in Step 4; each simplifies to
$M$. No coordinate is zero or $-1$, and $-M$ occurs once. A proper
period dividing six would repeat that occurrence, so the native least
period is six. The height is exactly $M$.

This disproves a constant height bound after excluding only $a=1$,
the $-1$ stratum and periods at most three. The author expressly does
not claim to disprove a finite-core theorem after further unbounded
families are classified and removed. That qualification is necessary
and is present in the inspected proof.

## 5. Static finite-alphabet implementation review

The code constructs all ordered states on exactly the frozen alphabet,
with exact integer division and no successor retained outside it.
The base-16 index formula agrees with the lexicographic product order.
The traversal tags distinguish a cycle in the current path from a
previously visited component; there is no period cutoff. Lexicographic
normalization merges only cyclic rotations.

Every reported word is then checked against the original recurrence
at all cyclic indices, all smaller shifts are tested, state uniqueness
is checked and parameter invariance is checked on every cycle state.
These checks use explicit failure exceptions. The counterexample
predicate matches the frozen hypothesis exactly. Exclusive output
creation does not overwrite the preserved result.

The inspected JSON labels itself finite-alphabet-only, sets its period
cutoff to null, and disclaims both full-height classification and
independent reconstruction. Its stored source hash equals the hash of
the statically inspected script. These are consistency checks, not an
independent confirmation of all stored numerical counts or the execution
environment. No complete run was duplicated for this review.

## 6. Decision boundary and remaining obligation

The transformation $z_i=-x_i-1$ in Step 5 gives the displayed
alternating-coefficient equation. Its inherited ordinary domain is
$z_i\in\mathbb Z\setminus\{0,-1\}$. Integrality of the two coefficients
does not exhaust its periodic channels or prove a global period list.
The proof explicitly keeps this obligation open.

Required fixes: **none found within this bounded review**.
Allowed conclusion: the three auxiliary statements survive unchanged,
and the finite-alphabet program is statically consistent with its frozen
scope. Forbidden conclusion: full classification, fourth admission,
independent CPU certification, or target-arithmetic promotion.

The research-review/proof-writer workflows influenced the explicit
hypothesis, degenerate-case and claim-boundary checks. Current-team
internal review was used under the batch instructions; no external
model, paid API, GPU or human review was represented as having occurred.
