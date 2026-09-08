# New nonadditive positive-characteristic contracts

Frozen 2026-09-07 UTC before any new polynomial or finite-field computation.
These are AI-generated scouting questions, not admitted theorems. At most
the following two candidates are considered in this lane. The previously
admitted M1 and AS2 contracts are unchanged.

## NC1 — logarithmic-differential polynomial dynamics

**Object and full family.** For every odd prime $p$, every
$\lambda\in\overline{\mathbb F}_p^\times$, let
$f_\lambda(x)=\lambda x(1+x)^p$. The degree is $p+1$, and the
polynomial is nonadditive and separable. Every parameter lies in a finite
extension, but no field of definition or exceptional parameter is dropped.

**Domain and native clock.** The affine geometric point set
$\overline{\mathbb F}_p$ with ordinary forward powers $f_\lambda^n$.
The parameter $n$ is iteration time. It is neither extension degree nor
inverse-tree height. Infinity is not counted in the affine observable.

**Observable and one complete question.** Classify the distinct ordinary
fixed counts
$N_n(\lambda)=\#\{x:f_\lambda^n(x)=x\}$ and the local multiplicities
needed to obtain them, for all $n\ge1$ and all displayed parameters.
The intended residual would be a closed arithmetic law with completely
resolved exceptional strata, rather than an instruction to factor an
exponentially growing iterate. A rationality/transcendence statement for
the ordinary Artin–Mazur series is a possible consequence, not an assumed
premise or a separately counted contract.

**Mechanism to investigate.** The identity
$f_\lambda^*(dx/x)=dx/x$ forces multiplier one at every nonzero
periodic point. It prevents an ordinary degree count from answering the
question. The proposed useful structure is global nonadditive wild
periodicity, not the previously scouted local residue-zero germ.

**Cheap falsifier.** First check primary sources on invariant
differentials, dynamically affine maps and periodic-point multiplicity.
Then test the tempting intermediate hypothesis that every nonzero point
of primitive period two has multiplicity exactly $p$ in $f_\lambda^2-x$.
An exact symbolic family of exceptional parameters or one certified
counterexample suffices to reject that hypothesis. If needed, a single
small finite-extension calculation may check the symbolic identities.
No larger census is authorized as a substitute for the full classification.

**Replacement/admission boundary.** A general source theorem that already
settles this family, or a short consequence of its hypotheses, defeats the
substantial gate. If exceptional parameters lead to an unresolved
all-period multiplicity problem, record HOLD/NOT ADMISSIBLE rather than
discarding those parameters, counting scheme degree, restricting to a
convenient local germ, or promoting a two-period calculation. No extension
of PC-F's residue-zero tower is intended.

**Arithmetic bridge boundary.** Wild multiplicity and a complete native
period law would be source arithmetic. An invariant differential or source
zeta alone is not target Euler/root-number, zero correspondence or
Hilbert–Pólya evidence. No A1/A2 grade is assigned here.

## NC2 — nonadditive Artin–Schreier skew return over all finite extensions

**Object and full family.** For every odd prime $p$ and every
$a\in\mathbb F_p$, put
$h_a(x)=x^{p+1}+a x^2$ and
$S_{p,a}(x,y)=(x^p,y+h_a(x))$.

**Domain and native clock.** For every $r\ge1$, use the finite set
$X_r=\mathbb F_{p^r}^2$ and ordinary powers of the same displayed map.
This is a permutation of each $X_r$. Extension degree $r$ and iteration
time $n$ are kept separate. No algebraic-closure fixed-point count is
claimed for this two-coordinate skew map.

**Observable and one complete question.** Determine all
$\#\operatorname{Fix}(S_{p,a}^n|X_r)$ and hence all exact cycle numbers,
uniformly for every $p,a,r,n$. Determine whether the nonadditive skew
coupling leaves any substantial arithmetic classification after ordinary
trace and Artin–Schreier point-count formulas are deducted.

**Mechanism to investigate.** The fibre return is the additive orbit sum
of the nonlinear function $h_a$. On a Frobenius orbit that sum is a trace
of a quadratic form. The associated curve is
$C_a:Y^p-Y=X^{p+1}+aX^2$, a member of the classical $Y^p-Y=X R(X)$
family with additive $R(X)=X^p+aX$.

**Cheap falsifier.** Derive the return sum on
$\mathbb F_{p^{\gcd(n,r)}}$, including the case $p\mid n/\gcd(n,r)$.
Check whether the full requested answer then follows from a standard
quadratic-form zero count or an existing Artin–Schreier theorem. If so,
reject as classical reconstruction without a CPU run. Only an identified
nonclassical residual can justify a short diagnostic.

**Replacement/admission boundary.** No promotion of a Frobenius trace
identity to a new determinant theorem; no split of different $a,p,r$ into
papers; no replacement of the finite-set cycles by scheme multiplicity.
If the full observable is already a direct classical consequence, record
that collision and stop this candidate.

**Arithmetic bridge boundary.** Any curve numerator would belong to the
explicit source curve. The skew-map construction does not by itself
supply an independent target arithmetic dictionary or a chronological
interpretation of another system's Frobenius.

## Execution and source boundaries

The initial screen uses two to three targeted formulations per candidate
and at least five distinct fresh formulations across this lane. Searches
may include foundational primary papers as well as recent work; no claim
of worldwide priority follows from search silence. The source audit will
name actual theorem conditions, reading scope and local collisions.

Only this `new_charp` directory may be written. No old checks, accepted
contracts, Git/global state, manuscripts, formal evaluations, C-numbers,
GPU jobs or paid/external model APIs are touched. The deliverables are a
scout report and source audit; a complete proof package is written only
if a substantive viable contract survives.
