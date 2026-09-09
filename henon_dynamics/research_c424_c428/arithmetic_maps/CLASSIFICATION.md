# AM1 complete author classification and exact certificate receipt

2026-09-08 UTC. **Author proof complete, computer-assisted; nonauthor proof
and substantive-increment reviews pending. Zero paper admission.**
This completes the original AM1 question after the coordinator authorized
the within-contract analytic reduction and one proved finite-core computation.
It does not reopen AM2 or AM3.

## Exact theorem

For every $a\in\mathbb Z$, set
$$F_a(x,y)=\left(y,\frac{y(y+1)}2+a-x\right),\qquad (x,y)\in\mathbb Q^2.$$
All rational periodic points are integral. Their complete oriented cycles
are the parametric words below, with $k\in\mathbb Z_{\ge0}$, together
with the eleven exceptional words in the second table. A word denotes
its consecutive coordinate pairs and is identified only under cyclic
rotation. At a parameter satisfying multiple rows, take their union.
All listed cycles are distinct and have the stated exact least periods;
no hidden degeneracy exclusions are needed.

| Parameter $a$ | Coordinate words | Least period |
| --- | --- | --- |
| $1-k(k+1)/2$ | $(1-k)$, $(k+2)$ | $1$ each |
| $-7-k(k+1)/2$ | $(-k-3,k-2)$ | $2$ |
| $-3-k(k+1)/2$ | $(-k-3,k,k)$, $(k-2,-k-1,-k-1)$ | $3$ each |
| $-1-k(k+1)/2$ | $(-k-1,-k-1,k,k)$ | $4$ |

| Parameter $a$ | Exceptional word, canonically rotated | Least period |
| --- | --- | --- |
| $-12$ | $(-6,-1,-6,4,4)$ | $5$ |
| $-11$ | $(-5,-2,-5,1)$ | $4$ |
| $-8$ | $(-4,-2,-3,-3,-2,-4,0)$ | $7$ |
| $-6$ | $(-3,-2,-2,-3,-1)$ | $5$ |
| $-5$ | $(-4,-1,-1,-4,2,2)$ | $6$ |
| $-3$ | $(-3,-1,0,-2,-2,0,-1,-3,1,1)$ | $10$ |
| $-2$ | $(-2,-1,0,-1,-2,0,0)$ | $7$ |
| $-1$ | $(-2,-1,1,1,-1,-2,1,2,1)$ | $9$ |
| $-1$ | $(-2,0,1,0)$ | $4$ |
| $0$ | $(-1,-1,1,2,2,1)$ | $6$ |
| $0$ | $(-1,0,1,1,0)$ | $5$ |

The complete set of possible least periods is
$$\{1,2,3,4,5,6,7,9,10\},$$
and the sharp point bound is
$$\#\operatorname{Per}(F_a,\mathbb Q)\le17,$$
with equality exactly at $a=-1$. This does not classify every
rational-coefficient quadratic Hénon map.

## Proof and the finite dependency

The [analytic package](PROOF_PACKAGE.md) proves integrality, the complete
$a\ge1$ boundary, validity and exact periods of every parametric word,
and uniform exhaustion for every $a\le-146$. The checked threshold is
$r\ge35/2$, not an unproved smaller bound. Its local symbol equations
are C412's, whose classification is deducted and reproduced explicitly.
Only $-145\le a\le0$ remains; $a=1$ is included in the computation as
a separately proved control.

The [finite-core contract](FINITE_CORE_CONTRACT.md) was frozen before the
first mathematical execution. It proves that all periodic points in odd
coordinates $z=2x+1$ lie in $S_a^2$, where
$$B_a=4+\lfloor\sqrt{9-8a}\rfloor,\qquad
S_a=\{z\in\mathbb Z:z\text{ odd},\ |z|\le B_a,
                     |z^2+8a+7|\le8B_a\}.$$
The odd-lattice bijection is
$$G_a(z,w)=\left(w,\frac{w^2+8a+7}{4}-z\right).$$
Repeatedly replacing $V$ by $\{P\in V:G_a(P)\in V\}$ preserves every
periodic point, terminates, and produces an injective finite self-map.
Its stable set is therefore exactly the complete periodic locus.
Neither this argument nor the code imposes a period cutoff.

The single execution of [certify_am1_core.py](certify_am1_core.py) succeeded
with exit code zero and produced [FINITE_CORE_RESULTS.json](FINITE_CORE_RESULTS.json).
All 147 parameter records contain their full alphabets, every strict pruning
cardinality and every primitive oriented cycle word. Assertions check the
integer recurrence, distinct states within each cycle, disjoint/full stable
set equality with expanded words, and inclusion of all parametric families.
The unmatched output is precisely the eleven exceptional words above.
Every residual parameter is thus exhausted, completing the all-$a$ proof.
This computation is a finite proof dependency, not a sample extrapolation.

Parametric rows have different least periods, except the two fixed points
and the two three-cycles explicitly separated in the analytic proof.
The exceptional four-cycles differ from the parametric four-cycle at their
respective parameters, as the full state-set certificate also checks.
All other exceptional periods lie outside the parametric list. Thus the
table has no duplicate cycles or unexplained shorter-period degeneracies.

All nine listed periods occur in the tables. For $a\le-146$, the center
$k$ is unique and only one of $s=-4,0,4,12$ is possible; hence each such
parameter has at most six periodic points. Parameters $a\ge2$ have none.
The complete finite output has maximum seventeen solely at $a=-1$, where
the disjoint cycles have lengths four, four and nine. This proves the
global bound and the exact equality locus.

## All-parameter cycle and return counts

For an integer $b$, let $\tau(b)=1$ if $b=k(k+1)/2$ for an integer
$k\ge0$, and zero otherwise. Equivalently $b\ge0$ and $8b+1$ is an odd
square. Write $[a\in E]$ for a finite-set indicator. The oriented cycle
counts $C_d(a)$ of least period $d$ are
$$\begin{aligned}
C_1(a)&=2\tau(1-a),& C_2(a)&=\tau(-7-a),\\
C_3(a)&=2\tau(-3-a),& C_4(a)&=\tau(-1-a)+[a\in\{-11,-1\}],\\
C_5(a)&=[a\in\{-12,-6,0\}],& C_6(a)&=[a\in\{-5,0\}],\\
C_7(a)&=[a\in\{-8,-2\}],& C_9(a)&=[a=-1],\\
C_{10}(a)&=[a=-3],
\end{aligned}$$
with every other $C_d(a)=0$. No overlap subtractions are needed. Therefore
for every positive integer $n$,
$$\#\operatorname{Fix}(F_a^n,\mathbb Q)=\sum_{d\mid n}dC_d(a),\qquad
\zeta_{F_a,\mathbb Q}(z)=\prod_d(1-z^d)^{-C_d(a)}.$$
These are ordinary-time finite-orbit consequences, not a separate
arithmetic/spectral theorem and not target Euler factors.

## Entire integer-valued quadratic class

Let $P\in\mathbb Q[t]$ have degree two and take integer values at every
integer; put $G_P(x,y)=(y,P(y)-x)$ on all $\mathbb Q^2$. Write uniquely
$$P(t)=m\frac{t(t-1)}2+nt+r,\qquad m,n,r\in\mathbb Z,\quad m\ne0.$$
The analytic package, Step 7, proves the following exact conjugacies.

- For $m=2k$ even, $(x,y)\mapsto(kx,ky)$ sends $G_P$ to the monic
  integral map $(u,v)\mapsto(v,v^2+(n-k)v+kr-u)$, classified by C412.
- For $m$ odd, set $q=n-(m+1)/2$ and $A=mr+(3q-q^2)/2$.
  Then $(x,y)\mapsto(mx+q,my+q)$ sends $G_P$ to $F_A$.

The inverse affine maps recover all rational periodic points and their
exact periods. Original coordinates need not be integers. The universal
sharp point bound for this entire integer-valued quadratic class is
seventeen. Equality holds exactly when $m$ is odd and
$$mr+\frac{3q-q^2}{2}=-1,\qquad q=n-\frac{m+1}{2}.$$
Even $m$ cannot attain it because C412 has at most eight points. The
complete set of possible least periods over this class is the same nine
above. No extension to arbitrary non-integer-valued rational polynomials
is made.

## One-run receipt and ownership boundary

The execution time recorded by the program was
2026-09-08T14:25:24.330685+00:00. It used Python 3.12.3 (Anaconda,
GCC 11.2.0), standard library only. Across the 147 different parameter
maps the output contains 306 points and 113 oriented cycles; those totals
are not the maximum for one map. The largest alphabet has sixteen
coordinates, the largest starting graph 256 states, and the largest
number of strict pruning reductions sixteen. There was one mathematical
execution, no failures and no retry. Later result inspection/hash checks
did not rerun the mathematics. The author read a lossless compact rendering
of every parameter record and the complete metadata/summary.

| Artifact | SHA-256 |
| --- | --- |
| [Frozen contract](FINITE_CORE_CONTRACT.md) | `20abae0a2d2755578f535656f31db00de74d3121b9a47935ce2c2b040f524350` |
| [Executed script](certify_am1_core.py) | `f80ffcf177fd7a8e98b8ea4d3112b7cca5ef986b5725025e70c836aa088132a0` |
| [Exact output](FINITE_CORE_RESULTS.json) | `44ccf0f5d062587eb07d2837c455a9c3843c3ce0b9e0c8df033d2223d227196a` |

The earlier unclosed mathematical gap is now closed in the author package.
Admission remains a different question. The proof reuses C412's
maximum/annulus strategy, identical six-symbol equations and finite
partial permutations; integer-valued normalization is elementary. Neither
these methods nor the eleven exceptions alone are advertised as new.
The strongest residual claim is the complete missing nonintegral-coefficient
normal form and resulting full degree-two integer-valued rational atlas,
with its changed sharp bound and native period set. A nonauthor must decide
whether this complete extension is substantial enough after all deductions
to support a new paper rather than a short companion result. No independent
review, worldwide priority, formal Route A evaluation or admission is claimed.
