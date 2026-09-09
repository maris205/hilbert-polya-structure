# R5 E1 — Native-12 mechanism and finite-family diagnostic review

## Verdict and binding

**Lemmas A–C: PROVABLE AS STATED. Zero open mathematical or source-applicability
must-fixes.** One provenance wording repair was required and closed, with
no mathematical change. The height bound and the complete finite-graph diagnostic
are also correct at their stated scope. The recorded single producer
execution supports absence of native periods $12,24$ in exactly the
specified $10,201$-map family. I did not run that program or an independent
implementation.

The unrestricted construction of native $12$ or $24$ in the integral tame
group remains **NOT CURRENTLY JUSTIFIED** here. None of the mechanism
obstructions or the finite-family result is a full-spectrum exclusion,
an independent contract, a priority claim, or paper admission.

This review binds the complete author artifacts:

| Artifact | SHA-256 |
| --- | --- |
| [PROOF_PACKAGE.md](../../c1_native12_tame_witness/PROOF_PACKAGE.md) | `35ca6132cdbbeb7a72c9d2569ce7eda476a8a1e1bb4baefd12bc8c1e05f4b55d` |
| [REPORT.md](../../c1_native12_tame_witness/REPORT.md) | `679da5cd309a635d53ef7b3e28ae8d651bd4c2be1e1cf11a5ba549b4e4adf3d5` |
| Source extracted between the report's designated markers | `acaa8a811a329dec8206f33a0e920bf4b644871b01cd3a782f29d63130a38608` |

I read both author files completely, including all code and the full JSON
receipt, and performed the report's read-only source-extraction/hash check.
Byte identity is distinct from the proof and code arguments below. The
one author wording repair in §1 has been read back; no further author
change is required.

## 1. Exact objects and the imported C428 boundary

Throughout,
$$
I_q(x,y)=(x,q(x)-y),\qquad J_p(x,y)=(p(y)-x,y),
\qquad p,q\in\mathbb Z[t],\qquad T=J_p\circ I_q.
$$
These are integral triangular involutions, so their product is an integral
tame automorphism. One full $T$ is one native tick. The auxiliary claims
refer either to selected actual integer cycles or to the explicitly
prescribed staircase, not to arbitrary interpolations over $\mathbb Q$.

I read the actual [C428 theorem and hypotheses](../../../../research_c424_c428/papers/C428_integer_period_spectrum/sections/01_theorem_sources.tex)
and its [evidence/scope statement](../../../../research_c424_c428/papers/C428_integer_period_spectrum/sections/07_evidence_scope.tex).
Its positive-Jacobian conclusion is
$$
\bigcup_{\substack{f\in\mathbb Z[t]\\\deg f\ge2}}
\operatorname{Spec}_{\mathbb Z}\bigl((y,f(y)-x)\bigr)
=\{1,2,3,4,6\}.
$$
It covers all integer coefficients and all degrees at least two, at integer
points, for one factor. It is not a theorem about arbitrary compositions,
rational coefficients or all rational points. Its already-accepted
computer-assisted exclusions are imported; their old programs are not rerun
or independently reconstructed in this task.

**Evidence wording repair — closed.** The original unqualified sentence
was replaced by the author with:

> No new R5 mathematical execution is a dependency of Lemmas A–C; the imported C428 theorem retains its accepted historical certificate dependencies.

I read back the exact new sentence and verified that substituting only
the old sentence back into the final proof, in a read-only stream,
reproduces the original proof digest
`8dbe4db1d868b31a1a5ee9328d0df49fd1d1c0a8c2b23ac2b35eedf3fd881901`.
The final proof digest is bound above; the report and extracted source
digests are unchanged. This is one closed provenance wording repair,
not a formula, proof, code or execution change. The new hand deductions
retain the accepted C428 certificate dependency; their entire transitive
proof chain is not being called computation-free.

The low-degree case is not silently included in that theorem. I also read
the actual [C2 padding proof, §§1–4](../../c2_composition_exact_spectrum/PROOF_SUPPLEMENT.md).
For a selected cycle of $(y,f(y)-x)$ with $\deg f<2$, let $E\subset\mathbb Z$
be its finite nonempty second-coordinate support. Replacing $f$ by
$$
\widetilde f(t)=f(t)+t^{\max(0,2-|E|)}\prod_{e\in E}(t-e)
$$
produces an integral polynomial of degree at least two: the added monic
term cannot cancel with $f$. It vanishes at every required input, including
when $0\in E$. Every transition of the selected cycle is unchanged, so its
same distinct points have the same least period under the single padded
factor. The zero polynomial is included. This justifies C428's use below
without requiring the new C2 period-16 argument or changing the native clock.

## 2. Lemma A: affine-centre collapse and all degeneracies

For $p(t)=kt+c$, $k\ne0$, the affine map
$$
L(x,y)=(ky-x+c,x)
$$
has determinant $-k$, maps $\mathbb Z^2$ into $\mathbb Z^2$, and is
injective over $\mathbb Q$. Its inverse need not preserve the whole integer
lattice. That is irrelevant: the forward image of each selected integer
cycle is an integer cycle, and injectivity prevents its least period from
collapsing.

Writing $u=ky-x+c$, $v=x$ gives $ky=u+v-c$. Direct substitution yields
$$
LTL^{-1}(u,v)=(v,kq(v)-2v+2c-u).
$$
The scalar polynomial is integral and the resulting Hénon sign is exactly
$+1$. C428, with the preceding padding when necessary, therefore excludes
native $12$ and $24$. There is no unsupported integral-conjugacy assertion.

For $k=0$, the proof correctly replaces the singular proposed change by
$$
T^2(x,y)=(x,y+q(c-x)-q(x)).
$$
The first coordinate remains fixed under $T^2$, so its iterates translate
the second coordinate by integer multiples of the same quantity. At a
periodic point, a positive multiple must vanish in characteristic zero;
the quantity is zero and the period divides two.

If $p$ only agrees with $kt+c$ at the intermediate inputs of a selected
orbit, replacing $p$ leaves every transition of that orbit unchanged.
The same proof then applies to that orbit, without claiming global
conjugacy for the original nonlinear $p$.

The report's wording “one centre” also has a precise symmetric
justification. For the integer swap $S(x,y)=(y,x)$,
$$
ST^{-1}S=J_q\circ I_p.
$$
Thus if $q$ is the affine centre instead, apply Lemma A to this conjugate
of the inverse. Inversion and the swap preserve least periods. For an
orbitwise affine agreement, first replace that centre on its actual finite
input support; the same conclusion follows. This symmetry does not extend
the conclusion to two genuinely nonlinear centres.

## 3. Exact staircase and the ordered-AP contradiction

The points
$$
P_{2i}=(x_i,y_i),\qquad P_{2i+1}=(x_i,y_{i+1}),\qquad 0\le i\le5,
$$
are pairwise distinct when the six $x_i$ and seven $y_j$ are separately
distinct. The specified involution matchings are equivalent to
$$
q(x_i)=y_i+y_{i+1},
$$
$$
p(y_0)=2x_0,\quad p(y_i)=x_{i-1}+x_i\ (1\le i\le5),
\quad p(y_6)=2x_5.
$$
The product then follows the exact order
$$
P_0,P_2,P_4,P_6,P_8,P_{10},P_{11},P_9,P_7,P_5,P_3,P_1,P_0.
$$
There are twelve distinct states before return, so this would be least
period twelve, not merely a period dividing twelve. The equations for
integral polynomials remain a genuine realization condition.

For ordered arithmetic progressions $x_i=b+ai$, $y_i=d+ci$ with
$a,c\in\mathbb Z\setminus\{0\}$, two successive $q$ values differ by
$2c$. Integer-polynomial value divisibility therefore gives $a\mid2c$.
The first four $p$ values are $2b,2b+a,2b+3a,2b+5a$; their third
forward difference is $-a$.

For unrestricted-degree $p\in\mathbb Z[t]$, the coefficient of $t^m$
in $p(d+ct)$ is a multiple of $c^m$. The third difference of $t^m$
at zero is zero for $m<3$ and $6S(m,3)$ for $m\ge3$, where the
Stirling number is integral. Thus the whole difference is divisible by
$6c^3$, proving $6c^3\mid a$. Negative spacings cause no exception:
$$
6|c|^3\le|a|\le2|c|
$$
is impossible for a nonzero integer $c$. This proves Lemma B for the
specified ordered template. It does not exclude arbitrary unordered or
non-AP supports. I do not use the report's brief nine-vertex analogy as
an additional classification result in this review.

## 4. Lemma C: all permutations of the two consecutive supports

All seven required $p$ values belong to $[0,10]$, regardless of the
permutation order of the $x_i$ and $y_j$. Monic division by
$\prod_{j=0}^6(t-j)$ produces an integral remainder $r$ of degree at
most six, agreeing at every relevant input. Write $r_j=r(j)$.

The following exact coefficient tests successively lower its degree.
In each row the leading coefficient is an integer and the absolute bound
is strictly smaller than its displayed multiplier.

| Current degree bound | Exact functional | Absolute bound |
| --- | --- | --- |
| Six | $720a_6=r_6-6r_5+15r_4-20r_3+15r_2-6r_1+r_0$ | $320$ |
| Five | $240a_5=-r_0+4r_1-5r_2+5r_4-4r_5+r_6$ | $100$ |
| Four | $360a_4=4r_0-9r_1+10r_3-9r_5+4r_6$ | $180$ |
| Three | $48a_3=r_6-3r_4+3r_2-r_0$ | $40$ |

The second row adds the two fifth differences. The third uses the fourth
divided difference at $0,1,3,5,6$; its unscaled denominators are
$90,-40,36,-40,90$, giving precisely the stated weights. The last row
is a third difference of step two. The bounds follow from $0\le r_j\le10$
and the equal positive/negative coefficient totals in each functional.
Thus all four high coefficients vanish. This is an all-degree argument,
not a restriction to searching quadratic input polynomials.

For $r(t)=at^2+bt+c$, the identity
$18a=r_6-2r_3+r_0$ gives $a\in\{-1,0,1\}$. If $a=1$, the endpoint
difference forces $b\in\{-7,-6,-5\}$. The outer two choices have range
width twelve on these nodes and cannot fit in $[0,10]$. The middle choice
leaves $(t-3)^2$ or $(t-3)^2+1$. Applying this reasoning to $10-r$ gives
the two downward quadratic possibilities as well.

Summing the seven staircase equations, using $\sum x_i=15$, yields
$$
\sum_{j=0}^6r_j=30+x_0+x_5,\qquad 1\le x_0+x_5\le9.
$$
The four candidates fail as follows:

| Candidate | Contradiction |
| --- | --- |
| $(t-3)^2$ | Sum $28$ would require endpoint sum $-2$. |
| $(t-3)^2+1$ | Sum $35$ requires endpoint sum $5$; the only even values are $2,10$, forcing the distinct endpoints $1,5$, whose sum is $6$. |
| $9-(t-3)^2$ | Sum $35$ again requires $5$; even values $0,8$ force endpoints $0,4$, whose sum is $4$. |
| $10-(t-3)^2$ | Sum $42$ requires endpoint sum $12$. |

The remaining affine remainder agrees with $p$ at every intermediate
$J_p$ input, so Lemma A contradicts the exact twelve-cycle forced by
the matching equations. All $6!7!$ arrangements are covered by these
value-set and sum arguments, without enumerating them.

Integer translations and independent sign reflections preserve the
involution form. Under $(x,y)=(\varepsilon X+a,\delta Y+b)$,
$\varepsilon,\delta\in\{\pm1\}$, the new centres are
$\delta q(\varepsilon X+a)-2\delta b$ and
$\varepsilon p(\delta Y+b)-2\varepsilon a$, still integral polynomials.
This verifies the stated conjugacy extension of the two support sets.

## 5. Complete height bound and the native-word direction

For the diagnostic only, $p_A(t)=t^2-A$, $q_B(t)=t^2-B$ with
$0\le A,B\le100$. On a periodic native orbit,
$$
x_i^2-B=y_i+y_{i+1},\qquad y_{i+1}^2-A=x_i+x_{i+1}.
$$
The involution intermediate state is $(x_i,y_{i+1})$. Consequently the
maximum $M$ of the absolute values of native coordinates also bounds all
intermediate coordinates. A maximal $x_i$ uses the first equation; a
maximal $y_j$ uses the second at index $j-1$. Both give
$$
M^2\le2M+\max(A,B)\le2M+100,
\qquad M\le1+\sqrt{101}<12.
$$
In fact integer coordinates have absolute value at most eleven; the
chosen radius twelve is a harmless conservative bound. It covers every
integer periodic orbit of every map in the stated family, of every period.

The exact conjugacy is
$$
W_{A,B}=H_{p_A}\circ H_{q_B}=S T_{A,B} S,
\qquad H_f(x,y)=(y,f(y)-x),\quad S(x,y)=(y,x).
$$
The rightmost $H_{q_B}$ acts first. On the swapped native state
$(y_i,x_i)$ it gives $(x_i,y_{i+1})$, the same intermediate state as
the involution presentation. Thus native periods and the intermediate
state convention are correct; no half-step or factor-period substitution
is made. For $A=B$, the word is $H_{p_A}^2$. C428's possible periods
$1,2,3,4,6$ then become $m/\gcd(m,2)\in\{1,2,3\}$, validating the
diagonal control's expected subset.

## 6. Full code and graph-scope audit, without execution

The inspected source matches its recorded digest. Its two `range(101)`
loops include all ordered pairs and all $101$ diagonal pairs. The state
list uses $x$ as outer and $y$ as inner coordinate on the $25\times25$
box. Therefore the image index
$$
(\mathrm{next\_x}+12)\,25+(\mathrm{next\_y}+12)
$$
is exactly the inverse indexing rule, whenever both coordinates lie in
the box. The code computes the stated integer map with the correct
constants and signs. Rejecting an edge whose second coordinate already
leaves the box is safe. Every periodic orbit is contained in the box by
§5; for a retained edge its intermediate coordinates are also in the box.

The graph traversal maintains a path and the first position of each
visited vertex on that path. It stops at an exiting edge, an already
completed vertex, or a repeated vertex of the current path. Only the last
case contributes a cycle, namely the suffix beginning at that first
position. That suffix has distinct states and is the cycle's least
period. Marking the entire completed path prevents later duplication;
starting from every not-yet-completed vertex finds every directed cycle.
No guessed period bound or target-only cutoff is present.

Counts are accumulated for every discovered period, not merely $12,24$.
Finding a target would only record its first witness; it would not end
the parameter or graph search. Canonical rotation changes a cycle's
starting point, not its orientation or length. The witness routine's
native, intermediate, swap and closing-edge formulas are correct by
inspection. Since the actual run found no target, that routine's target
assertions were not exercised; I do not claim a tested witness path or
an independent witness verification.

Each parameter pair is fully traversed before its statistics are committed.
The alarm is masked during the short counter commit and restored afterward,
so the intended timeout path does not mix a partial last pair into the
completed-pair totals. Completion assertions check the planned pair count,
diagonal count and sum of cycle counts. The recorded run completed normally;
no independent timeout/error-path execution is claimed here.

All arithmetic and graph decisions use exact Python integers and discrete
indices. The clock is used for the resource cap and receipt only. The
planned number of pair-state image constructions is correctly
$10,201\cdot625=6,375,625$. The source contains no project-file writes,
network operations, automatic range enlargement or repeat run.

## 7. Recorded execution and what its result establishes

The report preserves the approved extracted source, actual command, full
standard-output JSON, exit code zero and distinct timing fields. The
receipt gives `COMPLETE`, all $10,201$ ordered pairs, all $101$ diagonal
pairs and no error. Its counts are:

| Native period | Cycle occurrences across all parameter pairs | Diagonal-control occurrences |
| --- | ---: | ---: |
| $1$ | $286$ | $38$ |
| $2$ | $546$ | $20$ |
| $3$ | $37$ | $19$ |
| $12$ | $0$ | $0$ |
| $24$ | $0$ | $0$ |

The complete all-period count dictionary has no other keys. The total
$286+546+37=869$ is consistent with the reported total; $689$ parameter
pairs have at least one cycle. These are cycle occurrences counted once
per cycle per ordered parameter pair, not a total of periodic points or
a deduplication of geometric cycles across different maps.

The program time $3.69179403$ seconds, tool wall time $3.576800944$
seconds and enclosing $3.9$-second display are separately identified in
the report. Its raw UTC timestamp is preserved rather than rewritten to
match the preparation-date label. I do not convert those recorded fields
into an independently reproduced benchmark.

With the height proof and the checked graph algorithm, the complete
producer receipt establishes the finite-family negative result, not just
failure in an arbitrary spatial window. The reviewer contribution is
independent hand checking of the proofs and source algorithm plus receipt
and byte-binding checks. There is one recorded authorized mathematical
execution by the author and **zero mathematical executions by this reviewer**.

## 8. Disposition and remaining boundary

Accept Lemmas A–C as auxiliary mechanism obstructions, and accept the
diagnostic's complete finite-family scope with its single-run provenance.
Required repairs: zero mathematical; one provenance wording repair,
closed by actual author revision and targeted readback in §1. Zero open
mathematical, source-applicability or evidence-wording repairs remain.
The statements about arbitrary degrees, $k=0$, orbitwise affine agreement,
negative AP spacings, arbitrary support permutations and low-degree padding
all survive unchanged.

Do not promote these conclusions to nonconsecutive supports, repeated-height
matching configurations, extra factors, unrestricted constants or arbitrary
integral tame words. No genuine native-$12$ or native-$24$ integer witness
was produced. A hypothetical $24$-cycle would indeed give a $12$-cycle for
the explicitly selected new map $T^2$, but no such input exists in this
handoff. The general R5-C2 spectrum and any independent-paper judgment
remain outside this auxiliary review.

The `research-review` and `proof-writer` instructions guided exact-claim
normalization, edge-case checks and separation of proof from computation.
Current-team/no-upload restrictions supersede historical external-review
examples. Only this newly assigned review was written. No C1 author file,
earlier scout or review, shared file, Git object or PDF was modified by
this reviewer; no
new agent, API/model upload, old-certificate rerun or new mathematical
program was invoked. `NO_BAD_EULER_OR_ROOT_NUMBER` remains in force.
