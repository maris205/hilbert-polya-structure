# R5 A2: the excluded unicritical congruence

## Frozen exact obligation

For every odd prime $p$, $k=\overline{\mathbf F}_p$, every integer
$d\ge2$ with $d\equiv1\pmod p$, every $c\in k$, and
$f(x)=x^d+c$, determine whether

$$K_f=\{Q\circ f-Q:Q\in k[x]\},$$

where $K_f$ consists of the polynomials whose sums on every ordinary
primitive $f$-orbit are zero. One application of $f$ is the native
clock. The implication from polynomial coboundaries to zero sums is
telescoping. Completion requires either the reverse implication with
all these quantifiers, or an explicit noncoboundary satisfying all
ordinary primitive sums. A special value of $c$ or $d$ is not a proof
of the full positive claim. A method counterexample is not a theorem
counterexample.

This is a continuation of the same PC424-L contract, not a new paper
slot. The accepted R4 proof and all older records remain read-only.

## Initial status and cheap discriminator

**NOT CURRENTLY JUSTIFIED.** This is the status before new proof work,
not a negative conclusion about the exact obligation.

The first exact mechanism to test is the reduced fixed polynomial for
$c=0$ and return lengths prime to $p$. The coordinator suggested that
the reduction removes the constant factor $p^{v_p(d-1)}$ from the
exponential degree and may preserve a long-necklace detector. This is
an unproved proposed mechanism at this freeze. The initial success
criterion is a coefficient detector that genuinely descends to the
ordinary periodic quotient; failure is an exact aliasing or loss of
coefficient isolation, not merely the already known Jacobian blindness.
Only after evaluating this mechanism will an all-$c$ extension or a
different precisely stated mechanism be pursued.

## Subtracted inputs and execution boundary

The actual [R4 proof](../../continuation_round4/a2_unicritical_carry_extension/PROOF_PACKAGE.md)
provides the $d$-ary normal form, full cyclic digit basis, leading-digit
detector, and stable carry coefficients. Its Section 10 already proves
that, when $c=0$ and $h=x$, every Jacobian divisibility test passes
although the fixed point $1$ has nonzero ordinary sum. That accepted
example is not new and does not settle this round's question.

The proof-writer skill governs claim normalization and honest status;
the repository batch workflow governs ownership and review. No
mathematical program, nested agent, Git operation, shared/old-file
edit, manuscript, or external model/API use is allocated. New writes
are confined to this report and, if a full proof is obtained, the
same-directory `PROOF_PACKAGE.md`. Source work, if needed, must use
actual relevant primary statements; no novelty or quota claim is made.

## Final author outcome

**PROVABLE AS STATED — full author proof complete, nonauthor review pending.**
The initial status above records the pre-proof freeze and is superseded
by this outcome. The complete [proof package](PROOF_PACKAGE.md) retains
every allocated $p,d,c,h$ and establishes $K_f=B_f$ for the entire
excluded congruence class. Combined with the accepted, unchanged R4
theorem, the author results now cover every integer degree $d\ge2$
for every odd characteristic. That combined conclusion remains within
the same PC424-L contract; this report does not make an admission or
publication-priority decision.

For $P=p^{v_p(d-1)}$, $\deg h\le M$, $M\ge1$, the new
certificate uses the two return levels

$$n=7\lfloor\log_d(PM)\rfloor+22,\qquad n+1.$$

Polynomial coboundary, ordinary-root trace vanishing at both levels,
and the two divisibilities

$$F_j\mid D^{[P]}F_j\,\widetilde H_j(h)^P\qquad(j=n,n+1)$$

are equivalent. A noncoboundary has a detecting ordinary primitive
period at most $7\lfloor\log_d(PM)\rfloor+23$. The iterate degree
bound $d^{23}(PM)^7$ is not a claim about optimized computation.

### What changed the proof mechanism

Ordinary-root vanishing always gives
$F_n\mid D^{[E]}F_n\,\widetilde H_n(h)^E$ for every positive
integer $E$, because Hasse differentiation lowers each root order by
at most $E$. Taking $E=P$ is particularly useful here: the Taylor
expansion of $x^d+c$ has no terms of orders $2,\ldots,P-1$,
and its first non-linear term has nonzero coefficient
$\alpha=(d-1)/P\bmod p$.

The resulting Hasse derivative of an iterate is a sum of products with
one marked site. Their backgrounds are $P(d-1)$ before the mark,
$d-P$ at the mark, and $d-1$ after it. The target digit string has
a long block of $d-1$, followed by the digits of $PD-1$ and a long
zero block. Adaptive cuts and the nonpositive-excess recurrence
localize every observable source near the end of the long block.

Inserting one more $d-1$ site pairs every old marked path with
weight one. The newly inserted mark resets the subsequent low-block
carry to zero, so an exact integer weighted-degree identity isolates
the source of leading degree $D$. Its contribution is
$\alpha a_D^P\ne0$. Thus the two target coefficients differ by
this nonzero scalar, contradicting the two Hasse certificates.
The full proof includes all wraparound branches; an overflowing
adaptive cut leaves its digit at most one and cannot contribute a
target cut digit $d-1\ge3$.

This replaces the R4 comparison of the scalars $d^n,d^{n+1}$,
which coincide in this congruence class. No upper bound on periodic
root multiplicities is used.

## The cheap monomial check, proved separately

The coordinator's first proposed test succeeds for every $c=0$ in
the allocated congruence class. Let $P=p^{v_p(d-1)}$, write
$d=1+PA$ with $p\nmid A$, and take $n$ prime to $p$.
The binomial expansion gives

$$\frac{d^n-1}{P}\equiv nA\not\equiv0\pmod p.$$

Thus, with $R=(d^n-1)/P$ prime to $p$,

$$F_n=x^{d^n}-x=x(x^R-1)^P.$$

Its ordinary squarefree part is $x(x^R-1)$, of exact degree
$R+1$. Zero has multiplicity one and every other root has
multiplicity $P$.

If a normal polynomial $v$ has all ordinary cycle sums zero,
$\widetilde H_n(v)$ vanishes at all these roots, whence

$$F_n\mid\widetilde H_n(v)^P=\widetilde H_n(v^P).$$

If $v$ has positive leading degree $D$, then $v^P$ remains
normal because $\gcd(d,P)=1$. For an arbitrarily large $n$
prime to $p$ with $n>2\lfloor\log_d(PD)\rfloor$, the accepted
R4 leading-digit detector gives a nonzero coefficient of
$H_n(v^P)$ in the full cyclic algebra, a contradiction. The
remaining constant is zero at the ordinary fixed point $0$.
This proves the entire monomial subfamily, not merely $d=p+1$.
It was an intermediate proof, not a replacement for the all-$c$
obligation now addressed by the Hasse-carry package.

## The multiplicity route that was not assumed

There is a useful conditional alternative. For a fixed map with
$p\nmid d$, let $e_n$ be the largest ordinary-root multiplicity
of $F_n$, and let $E_n$ be the least $p$-power at least $e_n$.
If an unbounded sequence satisfies

$$n-2\log_d E_n\longrightarrow+\infty,$$

ordinary-root vanishing gives $F_n\mid\widetilde H_n(v)^{E_n}$.
The R4 normal leading-digit detector applied to $v^{E_n}$ then
excludes every positive normal part, since for its fixed degree $D$
one eventually has $n>2\lfloor\log_d(E_nD)\rfloor$.

No such all-$c$ multiplicity estimate was established or imported
in this investigation. In particular, prime-to-$p$ return lengths
do not themselves exclude long primitive multiplier-one cycles.
The structural identity

$$F_n'=\left(\left(\prod_{i=0}^{n-1}f^{\circ i}(x)\right)^A-1\right)^P$$

does not by itself bound common root orders. This conditional
alternative is not a premise of the completed Hasse proof.

## Source and verification record

The proof-writer skill led to an exact initial freeze, explicit status,
and a complete proof with separate dependencies. The repository batch
workflow retained disjoint write ownership and the same-paper boundary.
The research-lit skill was used for a narrow check for a genuine
positive-characteristic multiplicity theorem, after the monomial test.

No Zotero or Obsidian tool was available in tool discovery. The local
library filename check found no relevant primary PDF; unrelated
research-stream PDFs were not opened. No `arxiv_fetch.py` was found
in the two specified local search locations, so an arXiv-specific
web query was used. Five discovery queries covered positive-
characteristic periodic multiplicities, tame polynomial dynamics,
finite-field polynomial Livšic, and Hasse derivatives of periodic
polynomials. No returned source was promoted from a search snippet
to an applicable theorem. In particular, no characteristic-zero
Fatou or fixed-point multiplicity theorem is used. These searches
are not an exhaustive priority check.

The actual R4 normal-form and digit-basis proof, including its
excluded-case control, was reread. Its classical residue/Jacobian
antecedents and the earlier quadratic carry proof remain subtracted.
The present elementary Hasse identity and the marked-carry proof are
self-contained; the report makes no claim that Hasse differentiation
itself is new. A separate closest-source/admission review, if desired,
belongs to the coordinator.

The complete 517-line proof was read back after writing. New writes
are exactly this report and `PROOF_PACKAGE.md` in the allocated R5
directory, through `apply_patch`. Mathematical executions, nested
agents, Git operations, old/shared-file edits, manuscript/PDF work,
and external model/API calls: zero. Nonauthor mathematical review is
the remaining verification gate, especially for adaptive cuts, source
localization, and the all-mark insertion/deletion bijection.
