# Arithmetic/spectral first pass: no paper admission

2026-09-08 UTC. Three frozen questions screened. Final outcome:
**zero paper-retained candidates, one auxiliary complete candidate proof,
two short scoped obstructions.** No mathematical program, TeX, Git mutation,
external model transport, formal Route-A evaluation, or old build ran.

The full starting objects are in [FROZEN_SCOUTS.md](FROZEN_SCOUTS.md).
[SOURCE_AUDIT.md](SOURCE_AUDIT.md) records local deductions, 39 actual query
formulations, versions, read scopes and failed accesses. Findings below
are current-team judgments, not worldwide novelty or human review claims.

| Question | Final disposition | Decisive reason |
| --- | --- | --- |
| AS424-I: repeat-stable mixed-prime cyclic kernels | Auxiliary proof only; NOT PAPER-RETAINED | The exact transfer realization works, but is the classical geometric U family plus elementary active-support cancellation. |
| AS424-D: ordinary rational-Witt packet trace | REJECT as a new paper | The ordinary Haar packet has infinite invariant multiplicity; the resulting short obstruction does not resolve the global cohomological trace question. |
| AS424-B: standard Bost--Connes Liouvillian | REJECT as a new paper | Complete all-number-field low-temperature calculation is an immediate diagonal-spectrum consequence, with no substantial residual. |

## AS424-I: proof exists; operator and substance collision

For any characteristic p, any full prime-to-p level M>=3 and any finite
nonempty prime set L prime to pM, use the finite supersingular marked graph.
Edges are individual degree-l quotients carrying the full level; domain is
the entire finite complex state space. Native observables are chronological
closed-word counts and their primitive product, with edge clock one and
intrinsic log-degree specialization x_l=l^(-s).

The full proof and exact controls are in
[AS424_I_ANALYTIC_PACKAGE.md](AS424_I_ANALYTIC_PACKAGE.md). Its key criterion is

    ker(alpha_w^k) cyclic for all k>=1
      iff gcd(Trd(alpha_w),deg(alpha_w))=1.

The criterion is invariant under representative isomorphism and cyclic
starting vertex; the latter uses isogeny conjugacy, not inversion of a
singular torsion action. For each active prime one remembers a surviving
line. Summing support-specific traces with inclusion-exclusion removes
closed lifts on unused torsion lines, yielding an exact rational
determinant product and the honest primitive chronological Euler product.

Two exact hand controls on E:y^2=x^3-x in characteristic 7, M=3, L={2,5}:
alpha=1+3i has degree10 and a cyclic kernel, but alpha^2=-8+6i kills E[2].
Thus one-pass cyclicity is insufficient. Beta=4+3i has degree25 and trace8;
beta^2=7+24i acts identically on E[2]. Its all-5 length-four word has three
unused-2 memory lifts, so the support correction is necessary. No numerical
sampling or formal experiment is being substituted for the proof.

The positive source collision is [Hida's geometric U correspondence,
Section 1.5, formula (1.3)](https://www.math.ucla.edu/~hida/PSoffprint.pdf).
The remembered line is Gamma_0(l) level; the allowed quotient kernel is
disjoint from it. The package proves that different U_l commute by the
coprime isogeny square. For e_l>=1 and n=sum e_l the coefficient is just

    n!/(product e_l!) Tr(product U_l^e_l).

Hence chronological ordering alone contributes a standard multinomial
factor. Also gcd(t,N)=1 makes t^2-4N a unit at each active prime, placing
the induced quadratic order in the regular split/conductor-free case.
This explicitly avoids the hard conductor-dividing examples in S1.
Single-prime volcano rims, marked isogeny graphs, abstract Ihara corrections,
and ordinary finite determinant identities are all deducted (S1--S3/S8).
Building-lattice translation zetas (S10) are structural neighbors, not
asserted identical formulas; their weighting/hypothesis differences do not
automatically create a paper-level increment.

Replacement boundary: a future question would need a separately frozen,
substantial invariant or theorem beyond this source-owned U construction.
An infinite-prime limit is neither defined nor proved. For fixed finite L,
the old HEN-O29 finite-clock divisor obstruction remains applicable. No
native unique arithmetic-prime trace weight, target factor, target-zero
correspondence or meaningful A2 conclusion is obtained. AS1 is not reopened.

## AS424-D: a scoped ordinary packet obstruction

Take exactly Deninger's rational-Witt dynamical construction for Spec Z,
with its positive-real scaling flow. For a rational prime p the source's
degree-one packet has coordinates G_p times the circle of period log p,
where

    G_p=(product_{q!=p} Z_q^*) / closure(<p>).

Use its Haar probability measure, H_p=L2(G_p times R/(log p)Z), and ordinary
Koopman translation U_t in the circle coordinate. Equivalently its generator
is -i d/dtau on the periodic Sobolev domain, tensored with the identity on
L2(G_p). For f in C_c^infinity(R), define the bounded smoothing
T_f=integral f(t)U_t dt. These are source-native objects, not a packet mass
chosen to reproduce an arithmetic trace. Packet geometry and the period
are supplied by [Deninger, Sections 5--6](https://arxiv.org/pdf/1807.06400);
the following obstruction is the scout's elementary deduction.

For each odd q!=p, reduction followed by the quadratic character surjects
Z_q^* onto F_2. The product map is surjective onto the infinite product of
these F_2 factors. The closure of the powers of p maps into the subgroup
generated by one element, of order at most two. Thus G_p has an infinite
quotient, so L2(G_p) is infinite-dimensional. Functions independent of the
circle coordinate form an infinite-dimensional invariant subspace. On it,
T_f acts as (integral f) times the identity. If integral f is nonzero,
T_f is not compact and therefore not trace class. This holds for every p.

This closes the frozen ordinary question, but not a substantial new paper.
It says nothing against Deninger's prospective global cohomological or
regularized trace, and does not prove that all packet-normalization
procedures are impossible. Morishita's 2025 comparison (S5) was checked to
avoid claiming the underlying arithmetic dynamical comparison as new.
Replacement by a global cohomological trace would be a materially different
question, not an automatic continuation of this short obstruction.

## AS424-B: complete standard-spectrum calculation, not a paper

For every number field K, beta>1 and every extremal low-temperature
arithmetic parameter, use the ideal representation H_K=l2(J_K^+),
H e_a=log(Na)e_a, and rho_beta=zeta_K(beta)^(-1)e^(-beta H).
This native norm dynamics and Gibbs representation are source-owned by
[Laca--Larsen--Neshveyev, Section 2](https://arxiv.org/html/0710.3452v2).
On the Hilbert--Schmidt space define physical-time

    L(T)=HT-TH,
    D(L)={T: sum_{a,b}|log(Na/Nb)|^2 |T_ab|^2 < infinity}.

This is the maximal self-adjoint diagonal realization; the associated
unitary is T -> exp(itH) T exp(-itH). Matrix units E_ab form a complete
orthonormal eigenbasis with eigenvalues log(Na/Nb). Consequently every
spectral measure is atomic. Every eigenvalue has countably infinite
multiplicity: multiplying both a and b by the same varying integral
principal ideal gives infinitely many different orthogonal matrix units
at the same eigenvalue, while the whole space is separable.

The operator spectrum, as a closed subset of R, is all R. Indeed if
d=[K:Q], principal rational-integer ideals give the eigenvalues
d log(m/n), m,n positive integers, a dense set. Points in the closure not
in the countable eigenvalue set are continuous-spectrum points; this does
not contradict atomic spectral measures in a complete eigenbasis.
In particular ker L is infinite-dimensional, the resolvent is not compact,
and exp(-tL^2) is not trace class for any t>0. The modular logarithm is
log Delta=-beta L with this convention; beta does not remove multiplicity.

This is a whole-family calculation but only a short consequence of the
existing diagonal Hamiltonian. It does not cover non-extremal or
high-temperature representations, altered hopping Hamiltonians, or
regularized traces. No such expansion is made here. The previous local
Bost--Connes deformation scouts are deducted, and no new paper is retained.

## Handoff and preservation

Only this lane's directory was written. The initial proof-retention idea
was explicitly superseded after the positive U-operator source collision;
the auxiliary proof is preserved for reuse and independent checking.
All exclusions are scoped. Source arithmetic and a native log norm are
not target Euler factors, root numbers, automorphy or a Hilbert--Polya
realization. The lane contributes zero of the five required papers.
