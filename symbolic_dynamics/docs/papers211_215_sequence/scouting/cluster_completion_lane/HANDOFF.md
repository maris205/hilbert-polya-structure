# CLU completion lane: exact-old negative reception packet

Author scout: `/root/round211_rational_scout`, 2026-09-08 UTC.
Status: **NO_PROMOTION / EXACT_OLD_LITERAL**. This is an author scouting
closure, not an independent review or admission PASS.

## Literal and counting boundary

The only instantiated literal is, for every odd prime $p$,
$$C_p:\mathbb F_p^2\longrightarrow\mathbb F_p^2,\qquad
C_p(x,y)=(y,(1+y^2)\operatorname{inv}_0(x)),$$
where $\operatorname{inv}_0(0)=0$ and
$\operatorname{inv}_0(x)=x^{-1}$ for $x\ne0$.
The state carrier includes both axes; the update is autonomous and total.

Count this as **one repeated literal desk attempt, zero fresh candidates,
zero retained candidates, zero reserves, zero scientific runs and zero
new paper numbers**. No exponent, parameter, field-extension, boundary-only,
or conjugate variants were instantiated as additional attempts. No pilot was
preregistered or executed. The project skill's exact-collision/known-engine
subtraction stopped this lane before experimentation.

## Actual collision originals and reading boundaries

The following repository-root paths were opened as actual originals, not
merely inferred from a recovery summary. Their complete byte contents are
pinned in `INPUT_PINS.sha256`; a full-file hash does not imply a full-file
mathematical reading. Native excerpts are in `raw/02` through `raw/06`.

| Original | Actual relevant reading and consequence |
|---|---|
| `docs/papers152_156_sequence/scouting/algebraic_replacement2/SCOUT.md` | Introductory contract, Section 7 (lines 237–266), and frozen status lines 382–405. Section 7 defines exactly $C_p$, gives $K=(x^2+y^2+1)/(xy)$ and $z=Ky-x$, and closes it as `KILL_OWNED_ENGINE`; it expressly rejects splitting off its singular boundary as a second axis. |
| Same directory, `OWNER_SEARCH_LOG.md` | CLU ownership discussion, lines 175–230: rank-two cluster provenance and the regular linear recurrence are already deducted. This packet does not pretend that every source cited in that old log was newly read. |
| Same directory, `verify_algebraic_replacement2.py` | `verify_clu`, lines 270–306: the exact same totalized update, with ten old odd-prime instances. The implementation was inspected as text, never executed in this lane. |
| Same directory, `CANONICAL.txt` | All ten CLU rows, selected by native `rg`. These are old recorded outputs, not newly reproduced experiments; they report image size and maximum fibre size, not a maximizing-target census. |
| `docs/papers197_201_sequence/scouting/fifth_fresh_20260905/BREADTH_AND_KILL_LEDGER.md` | Lines 1–90, including the explicit CLU exact-repeat warning. This led to the original check; it was not substituted for the original. |

The regular identity follows directly by substituting the displayed $K$:
$(1+y^2)/x=Ky-x$ when $xy\ne0$. Iterating a regular invariant cannot justify
the zero-denominator completion without checking each singular transition.
No new full-carrier, all-prime temporal/recurrent classification is claimed.
Regardless of that open analysis, the literal has already been scouted and
closed; its return cannot occupy a fresh seat.

## Narrow correction of old maximizing-fibre prose

The old Section 7 says the split case has a unique fibre of size $p$.
That uniqueness statement is false; all historical files remain unchanged.
Here is an elementary author proof that isolates the correction.

For a target $(u,v)$, the first coordinate forces $y=u$. Put $a=1+u^2$.
If $a\ne0$, inversion with the specified zero convention is a permutation
of the whole field, so the second equation has the unique solution
$x=\operatorname{inv}_0(v/a)$. If $a=0$, the second output is zero for
every one of the $p$ values of $x$. Thus, for every target,
$$|C_p^{-1}(u,v)|=
\begin{cases}
p,&u^2=-1,\ v=0,\\
0,&u^2=-1,\ v\ne0,\\
1,&u^2\ne-1.
\end{cases}$$
This is a direct symbolic deduction, not a scientific run.

For $p\equiv1\pmod4$ there are two distinct roots $i,-i$ of $u^2=-1$.
The maximum is $p$, attained at exactly the **two** targets $(i,0)$ and
$(-i,0)$, and the image has $p^2-2(p-1)$ elements. For
$p\equiv3\pmod4$ all $p^2$ targets have one source, so the image is the
whole carrier and every target attains the maximum one. For example, the
symbolic $p=5$ witness consists of $(2,0)$ and $(3,0)$, each with five
sources. No enumeration program was run to obtain that example.

The old recorded maxima and image cardinalities are consistent with this
law; they cannot establish the incorrect uniqueness sentence because the
old output has no maximizing-target count. This correction neither promotes
CLU nor claims a new independent inverse mechanism: it is a one-coordinate
zero-multiplier calculation. No accepted manuscript was changed, and no
downstream manuscript-wide impact audit is claimed here.

## Primary source and strict evidence ceiling

Andrew N. W. Hone, *Growth of Mahler Measure and Algebraic Entropy of Dynamics
with the Laurent Property* (Experimental Mathematics, online 31 March 2025),
[publisher DOI](https://doi.org/10.1080/10586458.2025.2470946) and
[Kent-hosted original](https://kar.kent.ac.uk/id/document/3459160).
The initial browser response exposed the repository cover, title page,
abstract and introductory text through its displayed line 192. It identifies
rank-two cluster dynamics and the affine-type Kronecker case as established
objects. This is direct primary-source context, not a newly read proof of
the exact regular invariant or a finite-field zero-completion theorem.

The requested deeper equations (2.14)–(2.15) were **not** reached. Browser
find/open requests failed; native acquisition returned HTTP 401 and curl
exit 22, with zero downloaded bytes, so PDF text extraction was skipped.
An earlier arXiv HTML access returned HTTP 406. Exact available browser
responses, headers, native streams and boundaries are retained. No claim
here depends on pretending the unreachable equations were read. No further
retrieval or candidate expansion was warranted after the exact-old collision.
AI-assisted author reasoning and retrieval were used; no external manuscript
upload, specialist contact, independent review, or publication action occurred.

## Artifact reception

`capture_native.py` is artifact/source acquisition only. `NATIVE_RECEIPT.json`
binds its source hash, interpreter and executable hashes, exact native argv,
timestamps, exit codes and raw output bytes. Nine native commands ran:
eight exited zero, the primary-source curl exited 22. The old-input hash
lists were captured before and after and compared by native `cmp` with
exit zero. Historical inputs, central indexes, the prior rational lane and
Git were not edited. `FAILURES_AND_LIMITS.md` preserves additional tool-only
failures and corrects an inaccurate intermediate status-code statement.

`seal_artifacts.py` provides an author-only integrity check, not a scientific
verification or independent review. The complete non-self `MANIFEST.sha256`
contains every regular payload file below this directory and excludes only
itself. Root can check it from this directory with `sha256sum -c
MANIFEST.sha256` and check the historical pins from the repository root.
