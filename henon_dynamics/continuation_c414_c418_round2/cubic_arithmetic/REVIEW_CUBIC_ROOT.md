# Nonauthor cubic proof, certificate and substance adjudication

Status: **PASS; ADMIT ONE SUBSTANTIAL CONTRACT**. This is the coordinator's
independent internal review, not human peer review or a global-priority
certificate. The cubic author did not write this review or its independent
checker. The admission is one contract, not seven papers for seven templates.
Manuscript, evaluation and release gates remain separate.

## Reviewed inputs and mathematical boundary

Read in full: the 499-line [proof](PROOF_PACKAGE.md),
[source audit](SOURCE_AUDIT.md), [scout report](SCOUT_REPORT.md),
and the producer, cross-check and exploratory scripts. Proof SHA256:

```text
d7288267e81a6389f1e71e4999cdc3c1056b754bb22a816b050253422e1f753f
```

The theorem concerns every monic integral polynomial
$f(t)=t^3+bt^2+ct+a$ and the determinant-$+1$ map
$H_f(x,y)=(y,f(y)-x)$ on all of $\mathbb Q^2$. The review certifies
the seven exact cycle templates, least periods $1,2,3,4,6$, the per-cycle
three-symbol property, sharp total bound eleven and its entire integer
translation equality locus. It does not extend to nonintegral rational
coefficients, determinant $-1$, nonmonic cubics or number fields.

## 1. Infinite-family reduction checked independently

At every finite prime, a cyclic coordinate of maximal absolute value
$T>1$ makes the monic cubic term have size $T^3$, while the recurrence's
neighbor sum has size at most $T$. This proves integrality. At the real
place the displayed coefficient-dependent radius is valid for every
cycle; finitely many lattice pairs lie in that radius. Thus extrema can
legitimately be taken over the **entire** periodic set before it is
normalized. No maximum over a merely hypothesized finite set is used.

For translated extrema $0,D$, both endpoint images belong to $[0,2D]$.
Divisibility of $g(D)-g(0)$ by $D$ proves integral $q\in[-2,2]$.
The third root $r=-B-D$ of $g(t)-A-qt$ is an integer. The secant is
between its endpoint values, so subtracting it from $g(t)$ at an
actual coordinate proves $|t(t-D)(t-r)|\le2D$ with the correct
factor two. This is necessary for every coexisting cycle.

The affine-root case uses at most nine pairs. The homogeneous matrices
at traces $-1,0,1$ have orders three, four and six. The two parabolic
traces require the separate periodicity arguments supplied in the
proof; in particular trace two forces $A=0$ and then constant first
differences vanish. Empty, one-symbol and diameter-one cases are not
silently passed to the finite computation.

For $D\ge10$, an extra nonroot symbol in $[3,D-3]$ contradicts
$3(D-3)>2D$. The four endpoint exceptions force exactly the five
lower values of $r$ or their reflected values. I checked the reflected
polynomial, including $\widetilde A=(2-q)D-A$ and
$\widetilde r=D-r$; it preserves the monic family and ordinary time.
For each of the five lower cases the stated $T_r$ retains every
possible extra symbol. No single-cycle root hypothesis replaces this
global argument.

For $D\ge16$, endpoint sums are affine polynomials in $D$ with
constant part at most six. The constant discrepancy in an edge is
at most fourteen. Therefore a numerical equality at such a $D$ is
equivalent to a literal affine-polynomial identity: a nonzero integral
slope discrepancy cannot be cancelled by a constant of magnitude less
than $D$. This justifies uniform symbolic graphs, not a representative
large-diameter sample. The proof's looser bounds $6,5,12,8,14$ are
valid even though exact endpoint-compatible maxima are $4,3,8,8,14$.

For $2\le D\le15$, if more than two symbols occur then an interior
one exists; its secant inequality gives $-3\le r\le D+3$. Those
are complete remaining ranges, not an original-coefficient cutoff.
Requiring both endpoints among graph cycles is only a necessary filter.
The proof correctly avoids concluding that a filtered graph has no
periodic points outside its interval. Such a conclusion is unnecessary
because the actual full-set extrema already contain all cycles.

## 2. Independent exact reconstruction

I wrote [reviewer_check_cubic.py](reviewer_check_cubic.py) without importing
any producer module. Its independent finite-graph principle is this:
for a partial injection on $N$ vertices, every noncyclic component is
a chain of length less than $N$, while cyclic components are disjoint
cycles. Hence the domain of the $m$th iterate for $m\ge N$ is exactly
the periodic set. The program computes this domain by repeated squaring
of the partial map, checks invariant bijectivity there, and reads cycles
only on that remaining set.

The small computation uses the whole $(D+1)^2$ square, not the producer's
secant-filtered alphabet; loops are expressed in original normalized
cubic coefficients $B,C,A$. The large computation represents affine
polynomials by their evaluations at zero and one. Equality of both
values certifies a polynomial identity because each edge expression
is affine, not because two samples prove arbitrary polynomial equality.
The separate no-carry argument above connects this representation to
every $D\ge16$.

Actual command, from `/root/autodl-tmp/hilbert-polya-structure`:

```sh
PYTHONDONTWRITEBYTECODE=1 python henon_dynamics/continuation_c414_c418_round2/cubic_arithmetic/reviewer_check_cubic.py
```

It exited **0**, using Python **3.12.3**, standard library only, on
Linux **5.15.0-78-generic**. Script SHA256 printed by that run:

```text
2f6aef4adb1b30f26662ff47641c5978ffb46479c1caca01dc2a5da1ec507751
```

The complete returned output was inspected. All fourteen small-diameter
rows agree with the proof: 9,373 endpoint-compatible tuples, 1,235
retained tuples, and 3,474 cycles before the endpoint filter. The computed
maximum is eleven, attained only at $(D,r,A,q)=(4,2,6,-1)$, with
words $(2),(0,3),(1,4),(0,2,4),(0,4,2)$. All observed periods and
all per-cycle symbol maxima agree. The ninety symbolic cases give
maxima $4,4,6,8,6$, and all 29 endpoint-using pattern cases agree
with the five baseline rows plus four exceptional rows in the proof.
The symbolic pattern words agree up to ordinary cyclic rotation; their
different encoded sort order is not an orientation quotient.

No unchanged producer script, old certificate or old paper build was
run by this reviewer. The original exploratory scan is not evidence
for infinite-family exhaustion. This is an exact integer finite
certificate after proven reductions, not a proof-assistant verification.

## 3. Template exhaustion, least periods and equality locus

The two-symbol words follow from distinct ordered pairs and the
recurrence. For three-symbol four-cycles, adjacent repeats force a
false equality of distinct symbols. For six-cycles with no adjacent
repeats, all six off-diagonal pairs would be visited. At each symbol,
its two equal neighbor sums force the two other symbols as neighbors,
which closes a three-cycle instead. An adjacent double therefore
exists; its equal neighbor forces the form $(p,p,h,q,q,h)$.
The author's enumeration of the remaining two positions covers every
way to introduce the third symbol, including forbidden triple repeats.

The reciprocal lemma is valid for distinct nonzero integers: opposite
signs give absolute sum less than one; same signs give a strictly
nonintegral sum after choosing positive ordered representatives. Its
application to the quadratic interpolant's coefficient is legitimate
because subtracting the monic root product leaves an integer quadratic
coefficient. This forces the midpoint condition in both centered rows.
I checked each resulting polynomial identity against the recurrence,
the integer ranges preventing lower periods, and the two distinct
orientations of a three-distinct-symbol three-cycle.

No large case reaches eleven. The unique normalized maximizing tuple
gives $g(t)=(t-2)^3-5(t-2)+4$; reversing the integer translation
gives exactly $f(t)=(t-h)^3-5(t-h)+2h$. The displayed disjoint
$1+2+2+3+3$ cycles at $h=0$ prove sufficiency. The upper bound then
rules out additional cycles, so the equality argument is not circular.

## 4. Source verification and substance decision

I independently accessed the [original Pezda journal record](https://dml.cz/handle/10338.dmlcz/120574)
and, after browser PDF timeouts, read the original PDF through a
read-only `curl` to `pdftotext` stream. Printed pages 95–96, Theorem
2.1 and adjacent definitions distinguish cycle length from the total
periodic set. Its general integral-map period list includes
$8,9,12,16,18,24$ as well as the five surviving cubic periods.
It does not make a fixed-degree sharp total-point assertion there.
No claim about every uninspected theorem in the literature is made.

I also read [Ingram's v1 introduction](https://arxiv.org/pdf/1111.3609v1),
including Theorems 1.2/1.4, the Pezda attribution and the determinant-$-1$
quadratic conjecture. Those are distinct from this monic integral,
determinant-$+1$ cubic theorem. The source audit's journal/preprint date
distinctions are retained; its wider source accesses remain attributed
to their author rather than claimed as new full-paper reads by me.
The current batch's already verified [Kim et al. v2](https://arxiv.org/html/2412.01668v2)
uses rational-coefficient integer-valued polynomials; its cubic member
$(t^3-7t)/6$ is not the present monic integral-coefficient family.

Targeted repository comparison deducts C412's monic integrality,
coordinate encoding and finite-complement methodology. The independent
increment here is the full cubic coexistence closure through an integral
third secant root, the exhaustive coefficient/word templates, and the
sharp eleven-point/equality theorem for every original coefficient triple.
It is not admission merely for changing the degree or extending a table.
Fresh exact-title/cubic-eleven searches returned mostly unrelated
real bifurcation or Hénon–Heiles material; these are not evidence of
novelty or sources for this result.

**Adjudication:** the full theorem and independent finite certificate
close the specified question, with a substantial residual result after
the accessed classical and repository ownership is subtracted. Admit
one contract. No mathematical repair is required. Source-bounded
priority uncertainty remains explicit. Source arithmetic is not target
Euler factors, root numbers, automorphy or Hilbert–Pólya progress;
`NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional.

## 5. Producer receipts: separate provenance

The author supplied additional fresh, read-only receipt runs at
2026-09-06 19:53:28–19:53:35 UTC; these were not hashes retained from
the earlier executions. With bash `set -o pipefail`, each of
`PYTHONDONTWRITEBYTECODE=1 python .../certify_cubic.py | sha256sum`
and the corresponding `crosscheck_cubic.py` pipeline exited zero.
The respective stdout digests were
`4fe4a21b9d535a6b6ae8e650ee87bff29a5e6b9295feb7fce3d9b98d68c14cce`
and `fbc7616b97fef9d7c0f183515faa09c38c31407f35d866911ccebe4a91c5d636`.
Inputs were producer SHA
`0495b17b6cc0be05e11a3cf86ca3df5806cf0eae82db51456978d441e25b95c3`
and cross-check SHA
`df07f88baedfc026e9d8d0b9e3eb3b70050de25f1983001fe113dc2cb9c5bb4a`.
These are explicitly author-side executions, not the independent run
in Section 2 and not retroactive evidence of a historical stdout hash.
