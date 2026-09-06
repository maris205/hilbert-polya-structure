# Fourteenth bounded slate — definitions fixed before code

Date: 2026-09-06 UTC. Owner/author: `batch197_fifth_scout`.
Write scope is this directory only. The accepted twelfth package is immutable.
OFS/P208 author/gate proof and code are not read, preserving potential B
eligibility. No new ID, central-index edit, Git operation, external upload or
automatic next slate is authorized.

This intake is written before any new pilot code or execution. It screens six
literal deterministic maps on finite matrices, point subsets, binary-operation
tables and group subsets. Three receive fixed full pilots; the other three
are closed analytically before execution. A desk exclusion is not a run or
a distinct admitted research mechanism. No novelty certificate is claimed.

## Frozen definitions and full boxes

### SNC — finite-field rectangular row/column normalization

For positive integers $r,c$ and an odd prime $p$ not dividing $rc$, the carrier
is $M_{r,c}(\mathbb F_p)\cup\{\dagger\}$. The sink is fixed. For a matrix,
first compute every row sum. If any is zero, output $\dagger$. Otherwise
multiply each row so its sum is $c$. In this intermediate matrix compute
every column sum; if any is zero, output $\dagger$. Otherwise multiply each
column so its sum is $r$. The resulting $r\times c$ matrix is the output.
Both normalizations use field arithmetic; there is no positivity test,
zero-denominator repair, transpose, threshold or post-hoc change of targets.

Immutable complete boxes: $(r,c,p)=(2,3,5),(2,3,7)$, including the sink in
each box. State counts are $5^6+1=15,626$ and $7^6+1=117,650$.

### RCI — moving-centroid radial inversion of point subsets

The carrier is all subsets of $V=\mathbb F_p^d$, with $p$ odd and
$Q(v)=\sum_i v_i^2$. If $|S|=0$ in $\mathbb F_p$, output the empty set.
Otherwise put $g=|S|^{-1}\sum_{x\in S}x$ and define

$$
I(S)=\left\{g+\frac{x-g}{Q(x-g)}:x\in S,\ Q(x-g)\ne0\right\}.
$$

This is a set, so repeated output points would merge. Zero-norm vectors are
omitted, not sent to another point or a sink. All tested forms are anisotropic
apart from their zero vector (one-dimensional forms, and the standard plane
over $\mathbb F_3$). The definition itself makes sense without anisotropy.

Immutable complete boxes:
$(p,d)=(3,0),(3,1),(3,2),(5,1),(7,1),(11,1)$; respectively
$2,8,512,32,128,2048$ subsets, total $2,730$. No $p=5$ plane or larger
dimension is added after observing results.

### RRM — right-return magma feedback

For $X=[n]=\{0,\ldots,n-1\}$, the carrier is every binary operation
$\mu:X^2\to X$, with no associativity, quasigroup or identity assumption.
Define the new table by

$$F(\mu)(x,y)=\mu(\mu(x,y),x).$$

All entries are recomputed from the old table simultaneously. The empty
carrier at $n=0$ has the unique empty operation and is fixed.

Immutable complete boxes: $n=0,1,2,3$, containing $1,1,16,19,683$
operations, total $19,701$. The tables are algebraic operation tables, not
word/rank encodings used to define a coordinate feedback.

### DCS — dihedral commutator-set feedback (desk only)

For $m\ge1$, let $D_{2m}=\langle r,s:r^m=s^2=1,\ srs=r^{-1}\rangle$
be the group of order $2m$. On all subsets put

$$C(S)=\{x^{-1}y^{-1}xy:x,y\in S\}.$$

Repeated elements and $x=y$ are allowed in the defining pair. No subgroup
generation is performed. There are no pilot boxes: the metabelian adapter
below consumes the entire temporal mechanism.

### TLS — ternary collinear triple-sum feedback (desk only)

For $d\ge0$, the carrier is all subsets of $\mathbb F_3^d$. Output the set
of vector sums $a+b+c$ over all unordered triples of distinct collinear
points $a,b,c$ from the input. No triple gives the empty output. There are
no pilot boxes: the characteristic-three line identity already settles
the complete temporal mechanism.

### DPM — diagonal pullback of a magma table (desk only)

On the same full operation-table carriers as RRM, let $d_\mu(x)=\mu(x,x)$
and put

$$P(\mu)(x,y)=\mu(d_\mu(x),d_\mu(y)).$$

No pilot boxes: the exact all-iterate formula below is a generic unary
composition/pullback adapter. This is not counted as a second independent
magma mechanism merely because its literal differs from RRM.

## Source-first deductions already fixed before pilots

1. SNC uses the classical alternating matrix-scaling algorithm with compatible
   target margins. That algorithm, diagonal-equivalence orbits, support/rank
   preservation on nonsink steps, and solving static margin equations all
   receive zero novelty credit. Positive-real convergence theorems do not
   transfer to field arithmetic. Historical ATR instead subtracts row minima
   and transposes; its complete Kuhn–Munkres/retraction adapter is deducted,
   but it is not this rule. Square $2\times2$ field normalization reduces to
   a one-dimensional Möbius action and is not piloted. Binary normalization
   and the square $3\times3/\mathbb F_3$ nonzero-margin degeneracy were
   eliminated analytically, before declaring the rectangular boxes above.
2. More explicitly, on a nonsingular scaling chart of a $2\times c$ input
   with rows $(a_j)$ and $(b_j)$, a column-normalized state has entries
   $r(a_jt,b_j)/(a_jt+b_j)$, with $t\ne0$ and all denominators nonzero.
   The next row-factor ratio is

   $$t'=\frac{\sum_j b_j/(a_jt+b_j)}{\sum_j a_j/(a_jt+b_j)}
         =\frac{cP(t)}{P'(t)}-t,
   \qquad P(t)=\prod_j(a_jt+b_j),$$

   whenever both required row sums are nonzero. This classical scalar
   scaling-factor/reciprocal-polynomial reduction is zero-credit, not an
   independent temporal theorem. For $c=3$ it is a rational map of degree
   at most two after cancellation, with deleted denominator states. No
   full prime-uniform core/clock or evaluated all-target fibre theorem is
   supplied by merely writing this quotient.
3. RCI deducts ordinary sphere/field inversion and affine centering. It is
   not the old circumcenter/orthocenter set or window rule, nor the old XOR
   centroid translation. Inversion about a **fixed** center is involutive;
   this does not prove involutivity after the centroid is recomputed.
   Singletons map to empty. Two-point anisotropic inputs have the same
   centroid after inversion and return in two steps; that slice is fully
   deducted. General subset recurrence and inverse extrema are unproved.
4. RRM is a term-derived binary algebra, so hypersubstitution and the
   familiar travel-groupoid return term are owned context. On left-dependent
   tables $\mu(x,y)=f(x)$ it is unary squaring; this whole slice is deducted.
   No generic all-table power-map conjugacy or full temporal/fibre theorem
   has been established for the stated right-return rule.

Two tempting proposals were **excluded rather than piloted or counted**:
the diagonal-feedback commutator is already exactly P175 (up to sign), and
$\mu(x,y)\mapsto\mu(\mu(x,y),\mu(y,x))$ is squaring in the classical
$\operatorname{Bin}(X)$ semigroup. For the latter, the pair map
$\Phi_\mu(x,y)=(\mu(x,y),\mu(y,x))$ is sent to $\Phi_\mu^2$, so the
entire time axis is generic self-map powering. Its direct primary definition
was checked before this intake. No OFS/P208 proof or current thirteenth-slate
proof was used. Partitions/hooks, conjugators, matching-support, gradients,
polarity/closure, neighbourhood-count and word/rank candidates are excluded
as requested; SNC's scalar gradient-like quotient is explicitly deducted.

## Complete analytic desk exclusions

**DCS — PROVABLE AS STATED; generic derived-series collapse.** The quotient
$D_{2m}/\langle r\rangle$ is abelian, so every commutator lies in the
abelian rotation subgroup. If $S\ne\varnothing$, the output contains the
identity because $[x,x]=1$. Therefore $C^2(S)=\{1\}$ for every nonempty
$S$, while $C(\varnothing)=\varnothing$. These two states are fixed and
form the complete core. This is the generic metabelian commutator-set
collapse, not an untransferred clock. No pilot is warranted.

**TLS — PROVABLE AS STATED; one-bit linear-summary erasure.** Every affine
line over $\mathbb F_3$ is $\{a,a+v,a+2v\}$ for some nonzero $v$, and
the sum of its three points is zero. Thus the first output is $\{0\}$ if
the input contains a line and empty otherwise. Both outputs next go to
empty. Hence the second iterate is constant empty and the only recurrent
state is empty. The zero-output fibre is precisely the static family of
cap sets. Its enumeration is not a new temporal axis. No pilot is warranted.

**DPM — PROVABLE AS STATED; generic unary-power pullback.** Let $d=d_\mu$.
The new diagonal is $d^2$, where powers mean ordinary composition. Induction
gives, for every $t\ge0$,

$$d_{P^t\mu}=d^{2^t},\qquad
(P^t\mu)(x,y)=\mu(d^{2^t-1}(x),d^{2^t-1}(y)).$$

The base case has exponent zero. For the induction step substitute
$d^{2^t}(x),d^{2^t}(y)$ into the previous table formula; the exponents add
to $2^{t+1}-1$. Thus every iterate is an ordinary functional-graph
composition power followed by coordinate pullback. Any cycle-clock
decoration has exactly this standard origin. No pilot is warranted.

## Execution and admission boundary

Only SNC, RCI and RRM may run, exactly **12 full boxes / 155,707 states**
per execution. No random subsampling, GPU, tuning or expanded cutoff is
used. Estimated CPU time is below one minute per full execution. Two fresh
isolated runs must preserve complete raw stdout, stderr, actual commands,
exit statuses, runtime settings, before/after pins and a byte-exact
comparison; failed evidence is retained. Each producer uses two distinct
implementations of the literal rule or an independently derived coordinate
identity, plus functional-graph and image-chain checks.

A survivor needs proved all-parameter temporal/recurrent structure and a
materially separate evaluated inverse/extremal theorem **after** all stated
deductions, then the actual independent source/value gate. A finite census
is not such a proof. Otherwise close this bounded slate `NO_PROMOTION`;
do not enlarge an original box or start another slate automatically.
