# Research Question

## Frozen identity

- Candidate ID: `cat_centralizer_cyclic_torsor_v1`.
- Safe title: **A Centralizer-Quotient Audit for Cat-Map Torsion
  Shells**.
- Date and literature cutoff: **2026-08-15 UTC**.
- Intended paper type: scoped negative mathematical audit.
- Feasibility decision: `GO_SCOPED_NEGATIVE_NOTE_LOW_NOVELTY`.
- Required terminal certificate:
  `CENTRALIZER_CYCLIC_TORSOR_CERTIFIED /`
  `A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC / ROUTE_B_NOT_OPENED`.

This project opens exactly the centralizer escape that Paper 9 left outside
scope.  It does not reopen or alter any Paper-9 source, code, result, or
manuscript artifact.

The symplectic map remains

$$
A=\begin{pmatrix}2&1\\1&1\end{pmatrix}
\in\mathrm{SL}_2(\mathbb Z)=\mathrm{Sp}_2(\mathbb Z),
\qquad T_A(x)=Ax\pmod{\mathbb Z^2}.
$$

For each fixed integer $q\ge2$, put

$$
R_q=\mathbb Z/q\mathbb Z,
\qquad E_q=\{v\in R_q^2:\operatorname{ord}_{+}(v)=q\},
$$

where $E_q$ is the exact additive-order-$q$ shell.  The matrix, the full
modulus list, the two centralizer ambient groups, and every expected finite
control are frozen before implementation.  No modulus, prime, normalization,
group, or stratum may be selected after seeing a registered result.

## The proposed escape

Define the cyclic-vector locus

$$
\mathrm{CV}_q
=\{v\in R_q^2:\Delta_q(v):=\det[v,Av]\in R_q^\times\}.
$$

Because

$$
e_1=\binom10,
\qquad
\det[e_1,Ae_1]=1,
$$

$e_1$ is cyclic over every $R_q$.  The full finite-module centralizer and its
symplectic subgroup are

$$
C_q=\operatorname{Cent}_{\mathrm{GL}_2(R_q)}(A),
\qquad
C_q^1=C_q\cap\mathrm{SL}_2(R_q).
$$

These are **local modulo-$q$ symmetry groups**.  The reduction of the fixed
global centralizer

$$
\operatorname{Cent}_{\mathrm{GL}_2(\mathbb Z)}(A)
$$

lands in $C_q$, but the proposed quotient uses all of $C_q$ and does not
require its elements to lift to one fixed global torus automorphism commuting
with $A$ over $\mathbb Z$.  Thus the mechanism pays a $q$-dependent local
pseudo-symmetry cost even before the symplectic restriction is imposed.

The tempting mechanism is:

> quotient all $A$-orbits in $\mathrm{CV}_q$ by the commuting centralizer,
> obtain one class, and assign one Euler factor to that class.

The audit asks whether this is an intrinsic arithmetic dynamical mechanism or
only a modulus-wise set quotient followed by an external label.

## Questions frozen for proof

### Q1. Is the cyclic locus really one full-centralizer torsor?

Prove for every $q\ge2$, not merely for primes, that

$$
\operatorname{Cent}_{\mathrm{Mat}_2(R_q)}(A)=R_q[A],
\qquad
C_q=R_q[A]^\times,
$$

and that

$$
C_q\longrightarrow\mathrm{CV}_q,
\qquad U\longmapsto Ue_1,
$$

is a bijection.  Equivalently, $\mathrm{CV}_q$ is a simply transitive
$C_q$-set.

### Q2. What happens to the dynamics after quotienting?

Since $A\in C_q$, the $A$-orbit set on the cyclic locus is

$$
\Gamma_q^{\mathrm{cyc}}
=\langle A\rangle\backslash\mathrm{CV}_q
\simeq C_q/\langle A\rangle.
$$

The residual $C_q/\langle A\rangle$ action is simply transitive, so its set
quotient has one element.  However,

$$
\mathrm{CV}_q/C_q=\{*\}
$$

carries the identity map induced by $A$.  Its only native primitive orbit is
a fixed point of period $1$, independent of $q$.  The formal replacement of
the ordinary quotient variable $z$ by $q^{-s}$, or the assignment
$L(*)=\log q$, is therefore an external modulus label.  This distinction
between **one orbit class** and **one arithmetic primitive orbit** is the
main semantic gate.

### Q3. Does the escape stay symplectic?

In dimension two,

$$
\mathrm{Sp}_2(R_q)=\mathrm{SL}_2(R_q).
$$

The full group $C_q$ generally contains nonsymplectic finite-module
automorphisms.  Prove that the genuinely symplectic centralizer does not
usually act transitively.  With

$$
S_q=R_q[T]/(T^2-3T+1),
$$

identify $C_q\simeq S_q^\times$, identify determinant with the quadratic
algebra norm $N_q:S_q^\times\to R_q^\times$, and prove

$$
\mathrm{CV}_q/C_q^1\simeq\operatorname{im}N_q
$$

through the invariant $\Delta_q(v)$.

For this discriminant-five algebra, the required exact count is

$$
|\operatorname{im}N_q|
=
\begin{cases}
\varphi(q),&5\nmid q,\\
\varphi(q)/2,&5\mid q.
\end{cases}
$$

Thus the symplectic quotient retains many classes; the one-class quotient
uses the larger, shell-dependent full $\mathrm{GL}_2(R_q)$ centralizer.
Even after either quotient, $A$ acts trivially on the quotient because
$A$ itself lies in the group being divided out.

### Q4. How much of the exact-order shell is discarded?

In standard coordinates,

$$
\Delta_q(x,y)=x^2-xy-y^2.
$$

For a prime $p$, classify the complete nonzero shell
$E_p=\mathbb F_p^2\setminus\{0\}$:

1. **binary/inert:** $\mathrm{CV}_p=E_p$ and $C_p$ is transitive;
2. **split, $p\ne5$:** the two nonzero eigenlines are noncyclic,
   $|\mathrm{CV}_p|=(p-1)^2$, and the full shell has three $C_p$-orbits;
3. **ramified, $p=5$:** the four nonzero vectors in the Jordan eigenline are
   noncyclic, $|\mathrm{CV}_5|=20$, and the full shell has two $C_5$-orbits.

The retained and discarded fractions are therefore

$$
\frac{|\mathrm{CV}_p|}{p^2-1}
=
\begin{cases}
1,&p\text{ binary or inert},\\
\dfrac{p-1}{p+1},&p\ne5\text{ split},\\
\dfrac{p}{p+1},&p=5,
\end{cases}
$$

with complementary discarded fractions $0$, $2/(p+1)$, and $1/(p+1)$.
The fixed integer reversor

$$
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad JAJ^{-1}=A^{-1},
$$

generates with $C_p$ the prime-field reversing-symmetry group.  It merges the
two split eigenlines, but it cannot merge the cyclic and noncyclic strata;
hence even the reversing layer cannot turn the full split or ramified shell
into one class.  The three symmetry layers must remain distinct:

$$
C_p^1\subset C_p\subset \mathcal R_p(A),
$$

where the first is symplectic, the second is the full commuting local group,
and the third also permits time reversal.

### Q5. Is there any prime specificity?

For every $q\ge2$, $\mathrm{CV}_q$ is nonempty and is contained in $E_q$.
The full-centralizer quotient therefore produces exactly the same one-point
set for composite moduli.  The exact cardinality is

$$
|\mathrm{CV}_q|
=\prod_{p^k\parallel q}p^{2(k-1)}c_p,
$$

where

$$
c_p=
\begin{cases}
p^2-1,&p\text{ binary or inert},\\
(p-1)^2,&p\ne5\text{ split},\\
p(p-1),&p=5.
\end{cases}
$$

Consequently the mechanism supplies no reason to retain only prime $q$.
Selecting the prime moduli, and assigning $\log p$ after the quotient, are
both external arithmetic choices.

## Exact audit frozen in advance

Any later implementation may examine exactly the following nine moduli and no
others:

$$
\mathcal Q_{\rm frozen}=\{2,3,5,7,11,4,6,9,10\}.
$$

- $\{2,3,5,7,11\}$ are inherited Paper-9 controls, not newly searched
  primes.
- $\{4,6,9,10\}$ are predeclared composite controls.  They isolate a binary
  lift, a squarefree inert product, an odd inert lift, and a
  binary--ramified product.  They were selected structurally, not by an
  observed fit.

The audit may use exact integer and modular arithmetic only.  It may enumerate
the already frozen finite modules and matrix groups, but may not scan a new
prime or modulus, evaluate $s$ or $\log q$ numerically, download a prime or
zero table, tune a matrix, or infer an infinite theorem from the nine finite
controls.

The proof-derived expected ledger is:

| $q$ | type | $|E_q|$ | $|\mathrm{CV}_q|=|C_q|$ | $|E_q\setminus\mathrm{CV}_q|$ | $\operatorname{ord}_q(A)$ | $|\Gamma_q^{\rm cyc}|$ | $|\mathrm{CV}_q/C_q^1|$ | $|E_q/C_q|$ |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 2 | binary inert | 3 | 3 | 0 | 3 | 1 | 1 | 1 |
| 3 | inert | 8 | 8 | 0 | 4 | 2 | 2 | 1 |
| 5 | ramified | 24 | 20 | 4 | 10 | 2 | 2 | 2 |
| 7 | inert | 48 | 48 | 0 | 8 | 6 | 6 | 1 |
| 11 | split | 120 | 100 | 20 | 5 | 20 | 10 | 3 |
| 4 | binary inert lift | 12 | 12 | 0 | 3 | 4 | 2 | 1 |
| 6 | binary/inert CRT | 24 | 24 | 0 | 12 | 2 | 2 | 1 |
| 9 | inert lift | 72 | 72 | 0 | 12 | 6 | 6 | 1 |
| 10 | binary/ramified CRT | 72 | 60 | 12 | 30 | 2 | 2 | 2 |

Here

$$
|\Gamma_q^{\rm cyc}|=|C_q|/\operatorname{ord}_q(A).
$$

The later audit must also verify that the induced $A$ map on both
$\mathrm{CV}_q/C_q$ and $\mathrm{CV}_q/C_q^1$ is the identity.  Passing the
finite table is only a falsification control for the proof and implementation.
For the five prime controls only, it must verify reversing-group full-shell
orbit counts $1,1,2,1,2$ in the order $2,3,5,7,11$, and that no reversing
orbit mixes the cyclic and noncyclic strata.

## Required decision and nonclaims

If the theorem and exact audit pass, record exactly

`CENTRALIZER_CYCLIC_TORSOR_CERTIFIED /`
`A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC / ROUTE_B_NOT_OPENED`.

The certificate means:

1. a full-centralizer set quotient can remove multiplicity on the cyclic
   stratum;
2. it does so for every modulus, including composites;
3. it discards noncyclic strata at split and ramified primes;
4. its one-class quotient has only trivial induced dynamics;
5. its Riemann-looking local variable is attached from the outside; and
6. restricting to the symplectic centralizer restores norm-class
   multiplicity; while adjoining the reversor merges only symmetry-related
   noncyclic pieces; and
7. the full quotient uses a $q$-dependent local pseudo-symmetry group rather
   than one fixed global centralizer action.

The project does **not** claim a new centralizer classification, a new cyclic
matrix theorem, a canonical prime selector, a standard dynamical-zeta factor
on the quotient, an impossibility theorem for every quotient construction, a
transfer/Fredholm determinant, a stack or groupoid zeta function, twisted
sectors, an equivariant Lefschetz formula, a Hecke quantization, a prime/zero
correspondence, or historical priority.  Stacky, equivariant, orbifold, and
twisted-sector mechanisms are a genuine outside-scope clue for Paper 11, not
objects ruled out here.
