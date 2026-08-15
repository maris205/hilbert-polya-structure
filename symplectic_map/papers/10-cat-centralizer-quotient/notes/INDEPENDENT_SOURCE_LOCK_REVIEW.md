# Independent Source-Lock Review

## Verdict

**PASS**

Reviewed source lock:

`aa99218099f2e2c3e14367bfe75f9da881d8b204689c07c6fa963f9582b696e2`

Candidate:

`cat_centralizer_cyclic_torsor_v1`

The seven-file Paper-10 design package is internally consistent, its local
and upstream hashes reproduce, and its mathematical claims survive an
independent proof audit over fields, prime-power rings, and composite residue
rings.  The low-novelty positioning is also appropriately conservative.

This is a **source-design PASS only**.  It does not authorize Paper-10 code,
a registered execution, a result claim, or manuscript expansion.  Any change
to one of the seven reviewed files invalidates this verdict until the changed
lock is reviewed again.

## Independence and scope of review

Before reading the final author package, the reviewer independently derived:

- the matrix commutant over an arbitrary ring $\mathbb Z/q\mathbb Z$;
- the cyclic-vector torsor and its stabilizers;
- the $A$-orbit quotient and the loss of the original return clock;
- the full-$\mathrm{GL}_2$ versus symplectic-centralizer distinction;
- the local norm image, including the binary and ramified-five boundaries;
- the inert, split, and ramified prime-shell strata;
- the reversing-symmetry boundary; and
- the prime-power and CRT composite consequences.

Only after that derivation was the final seven-file lock read claim by claim.
No Paper-10 candidate code was present or inspected.  No candidate was run,
no finite module was enumerated by a program, and no prime or Riemann-zero
dataset was accessed.  The numerical ledger below was checked by exact
algebra and CRT, not by executing the planned audit.

The literature audit used primary publisher/arXiv records through the frozen
cutoff of 2026-08-15 UTC.  It is a bounded novelty audit, not an absence or
historical-priority proof.

## Inventory, parsing, and hash integrity

Exactly seven files existed under the candidate directory at review time.
All were regular files.  Strict JSON parsing of `source_lock.json` succeeded
with duplicate-key rejection.

### Final lock and local design bindings

| Artifact | Locked / reproduced SHA-256 | Status |
|---|---|---|
| `experiments/source_lock.json` | `aa99218099f2e2c3e14367bfe75f9da881d8b204689c07c6fa963f9582b696e2` | PASS |
| `notes/RESEARCH_QUESTION.md` | `e1b8c735cd06a33e776220b04c5e8927d9d756aafbaa38783a010b7326d86461` | PASS |
| `notes/NOVELTY_ASSESSMENT.md` | `6ee0fe2aff13c2d4329496e32f2d6aa190a92a3c3b4904168a21828b646de0a5` | PASS |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | `03424a71fc8716618545a6c7c8b0fd05f5ad744cff034255ab0337012da0303d` | PASS |
| `notes/PROOF_PACKAGE.md` | `2eafe71f32c452ff8a20a6818ccb43082e02b866db7353e26c36ff432f1b2a4c` | PASS |
| `experiments/EXPERIMENT_PLAN.md` | `1735bfe8c161d125836529edd17548275368559dee82f00f2a3a616df6f45672` | PASS |
| `experiments/EXPERIMENT_TRACKER.md` | `6fabe06923b242aab4de7735ee0d87bc20edecaeafc9763161d3ac01d184fc6e` | PASS |

### Upstream Paper-9 bindings

All ten named upstream artifacts exist and reproduce the hashes bound in the
Paper-10 source lock.

| Artifact | Reproduced SHA-256 | Status |
|---|---|---|
| Paper-9 source lock | `662809d40f7e409e439983774a36349b90f265616a488061fda3c5b9064c2d49` | PASS |
| Paper-9 proof package | `47216ad4021d3476bfd0850ebec24c9ceafb5af8c0573214182fd2d0da7b2daa` | PASS |
| Paper-9 raw result | `448de06e92bd7ab4e5374e5d1f57413df45859cd3476ff14b2691b63ac364fab` | PASS |
| Paper-9 result manifest | `8ca12744638a47b6e4fa3239a60a19d79229d2b9596ae4fe4b2f66a399618f92` | PASS |
| Paper-9 independent result integrity | `aa0c7db555f11920c7305be508f6cfff62375970e112e9f720111831da20b3bd` | PASS |
| Paper-9 official result report | `66bfefe9dcf5731cb89a0597deed5df322f9bc24f9fc3a592d4790a46d2a4dc0` | PASS |
| Paper-9 official validation report | `32a1758362f94372a83588de63e2b5df33a8f7e45e0646de53154a2ca1afaab4` | PASS |
| Paper-9 final PDF | `96a560712ae7fb34e1d0ecfcd59e9b2c210ad61fe8ee0537c3a5ff5c860b4cd6` | PASS |
| Paper-9 round-2 review | `32cc795c358d979988673658398dd4dbf2768cd9f1b38464b9b438703c2ebd23` | PASS |
| Paper-9 final integrity | `7abbf1d25a3d57ccf3f195aa633237d2e641073ba647dcaacd6a177d7c66a712` | PASS |

The Paper-9 reuse boundary is narrow and explicit: only frozen artifacts and
the previously open centralizer question are inherited.  Nothing in the
Paper-10 plan authorizes a Paper-9 rerun or mutation.

## Independent mathematical audit

### 1. Centralizer equality over nonfields and nonreduced rings: PASS

Let

$$
A=\begin{pmatrix}2&1\\1&1\end{pmatrix},\qquad
X=\begin{pmatrix}r&s\\t&u\end{pmatrix}
$$

over any commutative ring.  Solving $XA=AX$ gives

$$
t=s,\qquad u=r-s,
$$

and no division is used.  Hence

$$
X=\begin{pmatrix}r&s\\s&r-s\end{pmatrix}
=(r-2s)I+sA.
$$

Therefore

$$
\operatorname{Cent}_{\operatorname{Mat}_2(R_q)}(A)=R_q[A]
$$

for every $q\ge2$, including composite and nonreduced $R_q$.  Intersecting
with $\mathrm{GL}_2(R_q)$ gives exactly $R_q[A]^\times$: over a commutative
ring a $2\times2$ matrix is invertible exactly when its determinant is a
unit.  There is no hidden field, separability, or square-free-modulus
assumption.

The proof package's cyclic-basis argument is equivalent and valid.  Indeed,

$$
[e_1,Ae_1]=\begin{pmatrix}1&2\\0&1\end{pmatrix}
$$

has determinant one over every $R_q$.

### 2. Cyclic-vector torsor, freeness, and exact additive order: PASS

Every $v\in R_q^2$ is uniquely $Ue_1$ with $U\in R_q[A]$, because
$(e_1,Ae_1)$ is a basis.  Commutation gives

$$
[Ue_1,AUe_1]=U[e_1,Ae_1],
$$

so

$$
\Delta_q(Ue_1)=\det U.
$$

Thus $v$ is cyclic exactly when $U$ is a unit, and

$$
C_q\longrightarrow \mathrm{CV}_q,\qquad U\longmapsto Ue_1
$$

is bijective.  Left multiplication is consequently free and transitive;
there is no unexamined stabilizer.

A cyclic vector is a member of the basis $(v,Av)$, hence is unimodular.  For
each $p^k\parallel q$, at least one coordinate is a $p$-adic unit, so its
additive order in the $p^k$ component is exactly $p^k$.  CRT then gives exact
global additive order $q$.  Therefore $\mathrm{CV}_q\subseteq E_q$ as
claimed.

### 3. $A$-orbits, residual quotient, and clock loss: PASS

Under $\mathrm{CV}_q\simeq C_q$, $A$ acts by multiplication by
$A\in C_q$.  If $A^kUe_1=Ue_1$, invertibility of $U$ and cyclicity of $e_1$
force $A^k=I$.  All cyclic-vector orbits therefore have exact length
$\operatorname{ord}_q(A)$ and

$$
\Gamma_q^{\mathrm{cyc}}\simeq C_q/\langle A\rangle.
$$

The effective residual group $C_q/\langle A\rangle$ acts simply
transitively, so its coarse quotient is one point.  Equivalently,
$\mathrm{CV}_q/C_q$ is one point.  Since the quotienting group contains $A$,
the induced $A$-map is the identity.  Its ordinary Artin--Mazur zeta is

$$
(1-z)^{-1},
$$

with native primitive period one.  The original period
$\operatorname{ord}_q(A)$ and the original repetition count
$|C_q|/\operatorname{ord}_q(A)$ have both been quotiented away.

Consequently, $z=q^{-s}$ or a length $\log q$ is external data.  Neither is
recoverable from the one-point coarse dynamics.  This is a strict statement,
not merely an interpretation preference.

A non-effective stack quotient of the already formed orbit set by $C_q$
could retain the stabilizer $\langle A\rangle$, while Burnside, equivariant,
orbifold, groupoid, or twisted-sector constructions can retain other data.
Those are genuinely different objects.  The lock correctly leaves them
outside scope and does not promote the coarse-quotient calculation to an
impossibility theorem about them.

### 4. Symplectic-centralizer refinement and norm fibers: PASS

For every commutative ring and every $2\times2$ matrix $D$,

$$
D^t\Omega D=(\det D)\Omega.
$$

Hence $\mathrm{Sp}_2(R_q)=\mathrm{SL}_2(R_q)$.  With

$$
S_q=R_q[T]/(T^2-3T+1),
$$

the cyclic basis identifies $S_q$ with $R_q[A]$.  Direct calculation gives

$$
N_q(a+bT)=\det(aI+bA)=a^2+3ab+b^2.
$$

Therefore $C_q^1=\ker N_q$.  If $v=Ue_1$, then

$$
\Delta_q(v)=N_q(U),
$$

and two cyclic vectors have the same $\Delta_q$ value exactly when their
ratio belongs to $C_q^1$.  The $C_q^1$-orbits are precisely the fibers of
$\Delta_q$, proving

$$
\mathrm{CV}_q/C_q^1\simeq\operatorname{im}N_q.
$$

This verifies the important correction that the quotient is the **image** of
the determinant/norm map, not automatically all of $R_q^\times$.  Since
$A\in C_q^1$, its induced action on this quotient is also the identity.
Restricting to symplectic commuters restores class multiplicity but not a
clock.

### 5. Local norm image, including $p=2$ and $p=5$: PASS

For $p\ne5$, the quadratic algebra is etale.  In the split case its norm is
$(u,v)\mapsto uv$ and is visibly onto.  In the inert case it is the
unramified quadratic extension; the finite-field norm is onto, and the norm
on the principal-unit filtration is onto.  This includes $p=2$, because
$T^2+T+1$ is irreducible over $\mathbb F_2$.  Reduction from the unramified
$2$-adic extension therefore gives a surjective unit norm at every $2^k$.

The $5$-primary boundary can be checked without an appeal to a black-box
count.  Put

$$
\pi=2T-3.
$$

Then $\pi^2=5$ and, since $2$ is invertible over $\mathbb Z/5^k\mathbb Z$,
every algebra element is uniquely $c+d\pi$.  Its norm is

$$
N(c+d\pi)=c^2-5d^2.
$$

For a unit, reduction modulo $5$ is therefore the square $c^2$.  Conversely,
if a base unit has square residue modulo $5$, either chosen nonzero square
root lifts uniquely through all $5^k$ because the derivative $2c$ is a unit;
regarding such a square root as a scalar algebra element realizes the unit as
a norm.  Hence
the local image is exactly

$$
\{u\in(\mathbb Z/5^k\mathbb Z)^\times:
u\bmod5\text{ is a square}\},
$$

an index-two subgroup.

CRT now proves the locked all-$q$ formula

$$
|\operatorname{im}N_q|=
\begin{cases}
\varphi(q),&5\nmid q,\\
\varphi(q)/2,&5\mid q.
\end{cases}
$$

Thus the frozen prime quotient counts are $1$ at $p=2$, $p-1$ at every
$p\ne5$, and $2$ at $p=5$.  The one-class claim genuinely requires the
larger, generally nonsymplectic full $\mathrm{GL}_2(R_q)$ centralizer.

### 6. Prime full-shell strata: PASS

In standard coordinates,

$$
\Delta_p(x,y)=x^2-xy-y^2
$$

has discriminant $5$.

- At $p=2$, the form is nonzero at all three nonzero vectors.
- If $(5/p)=-1$, it is anisotropic, so every nonzero vector is cyclic and
  the field-algebra unit group acts simply transitively.
- If $(5/p)=1$ and $p\ne5$, the zero locus is two punctured eigenlines.
  The cyclic complement has $(p-1)^2$ points.  The diagonal centralizer has
  one orbit on that complement and one on each punctured line, for three
  full-shell orbits.
- At $p=5$, the form is a square of one linear form.  Its punctured zero line
  has four vectors; the cyclic complement has $20$ vectors.  The Jordan
  centralizer has one orbit on the line and one on its complement, for two
  full-shell orbits.

The retained fractions $1$, $(p-1)/(p+1)$, and $5/6$, and the corresponding
discard fractions, are correct.  The source never conflates the cyclic
torsor with the complete shell in the split or ramified cases.

### 7. Reversing group and normalizer boundary: PASS

The fixed matrix

$$
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}
$$

satisfies $JAJ^{-1}=A^{-1}$.  Every reversor differs from $J$ by a commuter,
so the specifically defined reversing group is $C_p\cup JC_p$.  This is a
reversing-symmetry statement, not an unproved classification of the full
normalizer of the cyclic subgroup allowing arbitrary power automorphisms.

In the split case $J$ swaps the two eigenlines, but it preserves their union
and the cyclic complement.  In the ramified case it preserves the unique
eigenline.  Equivalently, direct calculation gives
$\Delta_p(Jv)=-\Delta_p(v)$, which preserves zero versus unit.  Thus the
reversing group cannot mix cyclic and noncyclic strata.  The locked reversing
counts $1,1,2,1,2$ for $p=2,3,5,7,11$ follow.

The package also keeps three distinct layers: the commuting symplectic group
$C_p^1$, the full local commuting group $C_p$, and the group that additionally
permits reversal.  It does not falsely say that all normalizer/reversing
elements preserve the numerical value of $\Delta_p$.

### 8. Prime powers, composites, and lack of prime specificity: PASS

A residue modulo $p^k$ is cyclic exactly when its reduction modulo $p$ is
cyclic.  Each admissible residue has $p^{2(k-1)}$ lifts, giving

$$
|\mathrm{CV}_q|
=\prod_{p^k\parallel q}p^{2(k-1)}c_p
$$

with exactly the locked local values of $c_p$.  Independently,

$$
|E_q|=J_2(q)=q^2\prod_{p\mid q}(1-p^{-2}).
$$

Since the torsor proof holds for every $q$, $\mathrm{CV}_q/C_q$ is one point
for every composite modulus as well as every prime.  The four composite
controls are therefore legitimate proves-too-much controls, not empirical
evidence for an all-$q$ claim.

The full $C_q$ is also correctly labeled a $q$-dependent local group.  The
reduction of $\operatorname{Cent}_{\mathrm{GL}_2(\mathbb Z)}(A)$ lands in
$C_q$, but the lock neither assumes nor claims that every local commuter is
the reduction of a fixed global torus symmetry.

### 9. Frozen exact ledger: PASS

The shell sizes, cyclic-locus sizes, discarded counts, full and symplectic
centralizer sizes, $A$-orders, and quotient counts agree across all seven
files.  The matrix orders can be checked directly from

$$
A^n=
\begin{pmatrix}F_{2n+1}&F_{2n}\\F_{2n}&F_{2n-1}\end{pmatrix}
$$

and CRT.  In frozen order $q=2,3,5,7,11,4,6,9,10$, they are

$$
3,4,10,8,5,3,12,12,30.
$$

The resulting cyclic $A$-orbit counts are

$$
1,2,2,6,20,4,2,6,2,
$$

and the symplectic cyclic-locus quotient counts are

$$
1,2,2,6,10,2,2,6,2.
$$

The auxiliary full-shell $C_q^1$ orbit counts

$$
1,2,4,6,12,2,2,6,4
$$

also check out: on split eigenlines the norm-one torus is separately
transitive; at $p=5$ the condition $a^2=1$ splits the four punctured-line
points into two orbits; and the composite counts factor componentwise by
CRT.

No arithmetic inconsistency was found in the expected ledger.

## Literature and novelty audit

The novelty score of **3/10** is safe and, if anything, generous.  The note's
defensible contribution is the tightly scoped negative decision package, not
any individual algebraic theorem.

1. [Baake--Neumaerker--Roberts (2013)](https://arxiv.org/abs/1205.1003)
   directly covers rational-lattice orbit structure, finite centralizers,
   cyclic-matrix commutants, finite-field normal types, reversing symmetries,
   finite-ring examples, and the cat-map prime-power setting.  This is the
   dominant collision.
2. [Kurlberg--Rudnick (2000)](https://arxiv.org/abs/chao-dyn/9901031)
   supplies the established norm-one/Hecke-centralizer context.  Paper 10
   correctly makes no Hecke, quantum, or equidistribution claim.
3. [Gusein-Zade--Luengo--Melle-Hernandez
   (2015)](https://arxiv.org/abs/1203.3344) is a particularly direct collision
   for the quotient-clock observation: it treats orders in a space versus its
   quotient and explicitly notes that when the transformation belongs to the
   quotienting group, the quotient action is trivial.  Its Burnside and
   orbifold refinements justify the lock's outside-scope boundary.
4. [Gaspari (1994)](https://doi.org/10.1016/0167-2789(94)90105-8) already
   treats common periods, a discrete first integral, and orbit decomposition
   on prime cat lattices.  The present $\Delta_p$ stratification must not be
   advertised as a new prime-lattice invariant theory.
5. [Baake--Roberts--Weiss
   (2008)](https://arxiv.org/abs/0808.3489) covers finite/rational-lattice
   periodic-orbit and Euler-product context, while [Miles
   (2015)](https://arxiv.org/abs/1506.08555) shows that group-action zeta
   constructions are broader than the coarse quotient studied here.
6. [Tan--Li (2025)](https://arxiv.org/abs/2506.20118) gives a current
   prime-power ring cycle/lifting collision, and [Chandra
   (2026)](https://arxiv.org/abs/2607.24857) gives current finite-torus
   transfer/Green-function and cycle-product identities.  Neither supports a
   novelty expansion for Paper 10.

The final package consistently uses the safe verbs “audit,” “derive for the
frozen matrix,” “separate,” and “certify within scope.”  It forbids claims of
first discovery, a new centralizer theorem, a new finite-ring classification,
a native Riemann clock, an equivariant/orbifold impossibility theorem, or
historical priority.  This matches the primary-source record.

## Experimental-design and policy audit

The planned finite audit is appropriately subordinate to the proof.  Its
nine moduli are fixed in advance, the four composites have structural
rationales, and the plan expressly prohibits using finite checks to infer an
all-$q$ theorem or novelty.  The full-$\mathrm{GL}_2$/symplectic distinction,
cyclic/full-shell distinction, induced quotient transition, composite
control, and reversing boundary are mandatory fields rather than optional
interpretation.

The source lock records:

- no code at lock time;
- no registered claim or result;
- execution not authorized;
- no network, RNG, float, analytic-parameter, new-modulus, prime/zero-data,
  transfer, quantization, or equivariant construction; and
- a separate future code-tree review and deployment gate before one
  registered audit.

Those constraints are coherent with the theorem and the project route.  A
future implementation must remain bound to this exact lock and must treat a
registered scientific mismatch as terminal rather than retuning the object.

## Remaining risks and mandatory downstream boundaries

No source-lock repair is required.  The following are boundaries, not
defects:

1. This PASS must not be cited as implementation or execution authorization.
2. The future code review must independently implement the matrix commutant,
   polynomial algebra, norm, shell, and orbit definitions; sharing one faulty
   routine across all checks would defeat the planned falsification.
3. Any stacky, Burnside, equivariant, orbifold, groupoid, twisted-sector, or
   group-action zeta is a new Paper-11 object and requires a new source lock.
4. Norm-one Hecke quantization remains outside scope and Route B remains
   closed.
5. The full-centralizer quotient is a local pseudo-symmetry construction; it
   must not be rewritten later as quotienting by one fixed global symplectic
   centralizer.
6. The only supported analytic statement is that $z=q^{-s}$ is externally
   assigned.  No native $\log q$, prime selector, Riemann local factor,
   prime-zero correspondence, or RH implication has been constructed.

## Final disposition

The reviewed seven-file package supports exactly the locked certificate:

`CENTRALIZER_CYCLIC_TORSOR_CERTIFIED /`
`A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC / ROUTE_B_NOT_OPENED`.

**Final source-lock verdict: PASS.**
