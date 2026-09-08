# Nonauthor proof and incremental-contribution review

Date: 2026-09-07 UTC. Reviewer: coordinator /root.
Author: scout_nonlinear_return. Review type: current-team AI-assisted
internal review, not human peer review or external-model review.

Verdict: **ADMIT ONE SUBSTANTIVE SOURCE-CLASSIFICATION CONTRACT**.
All four claims in the frozen proof survive this independent review.
There is no required mathematical correction. This admits one research
contract, not a completed paper, target-arithmetic result or five-paper
batch. No C-number is assigned here.

## Inputs and actual work

Immutable inputs under continuation_c414_c418_round2/mapping_class:

- [PROOF_PACKAGE.md](../../continuation_c414_c418_round2/mapping_class/PROOF_PACKAGE.md):
  all 526 lines read, including all ten steps and limitations;
  SHA256 619172d8a1d9a99015917069df6fe9d648a689dd680b4bd8bf6e05962628409e.
- [SOURCE_AUDIT.md](../../continuation_c414_c418_round2/mapping_class/SOURCE_AUDIT.md):
  read completely and primary claims revisited in the
  [fresh source audit](SOURCE_AUDIT.md);
  SHA256 8699961aac4b7d73138ff72263a8041418a8963f5482bd13fac75df50ec9854e.
- [classify_word.py](../../continuation_c414_c418_round2/mapping_class/classify_word.py):
  complete static reading against the proof;
  SHA256 65f61434a4acb513f3d46d2546a68f6661fca8459f4685e821f567323debcbbc.
- The complete author scout report, check receipt and line_automaton.py
  were read as evidence context. C413's theorem and relevant initial
  sections were read for the claimed collision only.

The review independently followed the algebra, exhaustive branch
arguments, domain, clocks and quantifiers below. No old census, test,
classifier execution or PDF build was repeated. The old diagnostic
receipt is historical finite evidence, not a new execution or the proof
of an infinite assertion. Hashes identify reviewed bytes only.
New review files do not change any sealed predecessor.

## Exact admitted contract

\[
A(x,y,z)=(x,z,xz-y),\quad B(x,y,z)=(z,y,yz-x),\quad
K=x^2+y^2+z^2-xyz.
\]

Domain: all of \(\mathbb Z^3\), on every integer level of \(K\).
Parameters: every finite positive word containing both \(A,B\).
For chronological \(w=\ell_1\cdots\ell_s\), the map is
\(W=\ell_s\circ\cdots\circ\ell_1\); one application of \(W\) is the
ordinary clock. The observable is ordinary periodic points and cycles,
not scheme lengths, group-orbit size, letter length or trace weights.

The single complete question is to classify ordinary integer
periodicity uniformly over that word family and all levels.
The answer is the exact 39-line-plus-four-point universal locus,
its realization by positive-word fixed sets, a levelwise at-most-40-point
classifier, and the two-sided escape alternative. These parts constitute
one theorem package and may not be split into separate papers.

## Independent proof audit

| Dependency | Counterexample/gap sought and resolution |
|---|---|
| Step 1: maps and matrix order | The inverses give integer bijections preserving \(K\). Substitution row vectors give the reversed chronological matrix product used by the scripts. Positive words containing both letters have matrix trace at least three. This is matrix hyperbolicity, not uniform hyperbolicity of every real surface orbit. |
| Step 2: common cone | For absolute coordinates \(a,b,c\) with \(c\) maximal, the new third modulus is \(ac-b\ge c\). Equality requires \(a=2,b=c\). A bounded plateau cannot survive recurring occurrences of both letters: the other letter forces \(c^2-2>c\). Cone orbits therefore properly escape, including the equality boundary. |
| Step 3: exhaustive large-coordinate descent | Negative product enters the cone. Third-coordinate maxima are covered, with the four signed all-two points removed. For a strict first maximum, the wrong letter enters the cone and the other gives \(d=bc-a\). The branches \(d\le-2\), \(\lvert d\rvert\le1\), \(d\ge\max(b,c)\), and \(2\le d<\max(b,c)\) respectively force subsequent cone entry, a small coordinate, cone/exceptional behavior, or strict integral descent. Tied maxima and the coordinate-swap case are covered. The negative branch is not incorrectly called immediate descent. |
| Step 4: every periodic phase is small | A periodic letter expansion cannot enter the cone. After reaching the small set, exiting under either letter gives a strict cone inequality. A small third coordinate alone is impossible on a periodic expansion, since its predecessor has all coordinates large. The necessary predecessor constraint is present. |
| Step 5: 39 lines | Orders \(4,6,3\) on planes with fixed coordinate \(0,1,-1\) give the displayed rotations. The next occurrence of the other letter either finds a second small coordinate or enters the cone. Exceptional small combinations yield exactly two six-line families in addition to 27 coordinate-parallel lines. Signs and the \(c=-1\) case are included. |
| Step 6: existential converse | \(F=B^{12}\circ A^{12}\) fixes points with first two coordinates small. Each listed line is carried into that set by \(G^r\), \(r\in\{0,1,2\}\), on a plane where \(G^{12}\) is the identity. Thus \(G^{12-r}\circ F\circ G^r\) is a positive word with both letters fixing the original line. The four exceptional points are fixed by \(B^2\circ A^2\). This proves an existential union, not periodicity under every word. |
| Step 7: all levels | Restricting \(K\) gives three quadratic forms with line multiplicities 3, 16 and 20. Cross-family overlaps occur only at treated low levels. For \(k>4\) the possible nonzero candidate cardinalities are 6, 32 and 40; low-level sets have sizes \(1,6,16,26\) at \(k=0,1,2,4\). Deduplication and negative integer parameters are included. |
| Step 8: ordinary classifier | Each letter gives an injective partial map of \(X_k\). Keeping every intermediate phase is essential; chronological row-action matrix multiplication implements this. A finite partial injection has cycles and nilpotent chains. Its cycles are precisely the ordinary \(W\)-cycles. The trace/determinant product is a classical deduction. |
| Steps 9–10: proper two-sided escape | A cone-free forward expansion eventually enters the same finite level core; injectivity turns eventual recurrence into periodicity. The common involution \(R(x,y,z)=(x,y,xy-z)\) satisfies \(RAR=A^{-1}\), \(RBR=B^{-1}\). The reversed word yields \(W^{-1}=RUR\); inverse letters are not incorrectly commuted. Properness follows since \(R\) is its own polynomial inverse. Nonperiodic points escape in both ordinary directions. |

## Static implementation audit

The classifier constructs the 27 plus 6 plus 6 lines directly.
Quadratic coefficients from parameters \(0,1,-1\) are exact because
Step 7 proves degree at most two. Integer square roots and divisibility
recover all roots; a set removes duplicate points and adds the four
exceptional points only on their actual level. Both letters are required.
Every intermediate letter phase is checked before adding a word edge.
The cycle traversal cannot merge a tail into an existing cycle because
of partial injectivity, not a heuristic depth cutoff.

The separate 45-state generic-line automaton is diagnostic context,
not the admitted classifier. A generic affine line return need not fix
its integer parameter. Do not replace pointwise periodicity by that
diagnostic or turn an observed period list into a sharp global theorem.
Script assertions are development checks, not a security guarantee.

## Substantive-increment decision

General trace-map structure, escape methods, small-coordinate rotations,
periodic curves and elementary determinant construction are deducted.
C413's single Fibonacci map and owned families are also deducted.
The residual is an exact all-word arithmetic exhaustion and a new
word-dependent finite classifier, not another sampled word or parameter.

Two independently checked separators matter:

1. \(A^6\circ B^6\) fixes \((1,1,m)\), whereas \(A\circ B\) carries it
   to \((m,m-1,m^2-m-1)\), in the escape cone for \(m\ge3\).
   Whole-group finite-orbit theorems cannot replace this classification.
2. Chronological \(ABB\), namely \(B^2\circ A\), has the four-cycle
   \((1,m,m)\), \((-1,m,-m)\), \((1,-m,-m)\), \((-1,-m,m)\) for
   \(m\ne0\), on \(K=m^2+1\). Its substitution matrix has trace four;
   this is not merely a power of the old Fibonacci map.

The threshold is met by the complete infinite-family reduction and
classification, not the numbers 39, 40 or a finite computation.
The source audit did not locate that output in the inspected closest
statements. Unavailable follow-up texts remain a coverage limitation;
no worldwide first-result language is authorized.

## Claims matrix and remaining work

| Claim | Decision |
|---|---|
| Exact universal integer locus for all positive words containing both letters | Admitted as proved in the reviewed package |
| Existential positive-word realization of every listed point | Admitted; retain quantifier |
| Complete ordinary cycle classifier and bound 40 | Admitted; no sharpness or realizable 40-cycle assertion |
| Every nonperiodic integer orbit properly escapes both ways | Admitted with the stated word/lattice hypotheses |
| Rational, complex-scheme, finite-field or all-group classification | Outside the contract |
| New generators, general escape method or determinant identity | Not a contribution |
| Target Euler factors, root numbers, Riemann-zero matching, Hilbert–Pólya model | Not established; NO_BAD_EULER_OR_ROOT_NUMBER remains active |

No additional proof experiment is required by this review; no compute
is imposed just to repeat PASS. Next gates: four other independent
contracts; manuscript with these boundaries; unchanged formal Route A
evaluation; nonauthor manuscript/source review; deterministic PDF
verification and eventual release. No manuscript approval, evaluation
tuple, build result or synchronization is asserted by this file.
