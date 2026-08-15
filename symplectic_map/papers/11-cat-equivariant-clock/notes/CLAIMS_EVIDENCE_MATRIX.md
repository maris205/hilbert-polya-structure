# Claims--Evidence Matrix

## Frozen status

- Candidate: `cat_equivariant_retention_tradeoff_v1`.
- Feasibility: `GO_SCOPED_BOUNDARY_NOTE_LOW_NOVELTY`.
- Required certificate:
  `EQUIVARIANT_RETENTION_COMPRESSION_TRADEOFF_CERTIFIED /`
  `A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC / ROUTE_B_NOT_OPENED`.
- Evidence state: source theorem drafted; no Paper-11 code, registered run,
  result, figure, or manuscript is authorized.

## Claim matrix

| ID | Frozen claim | Proof evidence | Closest literature / collision | Later exact audit | Status / boundary |
|---|---|---|---|---|---|
| G1 | For $X=\coprod_Kn_K(C/K)$ and $H=\langle a\rangle$, translation period on $C/K$ is $d_K=[H:H\cap K]$ with $[C:HK]$ cycles | orbit--stabilizer | elementary; 2008/2013/2015 equivariant carriers | symbolic formula tests; no new modulus | `PROVED_GENERAL_HIERARCHY` |
| G2 | Source and coarse zetas are $\prod_K(1-t^{d_K})^{-n_K[C:HK]}$ and $(1-t)^{-\sum n_K}$ | G1 and identity quotient action | Gusein-Zade et al.; Zegowitz | exact structural records | `PROVED_PRIOR_COROLLARY` |
| G3 | Point exact classes are $P_m^C=\sum_{d_K=m}n_K[C/K]$ and depend only on $H$, while orbit exact data are $\widetilde P_1=[X]$ | fixed points versus fixed $C$-orbits | 2008 rational and 2015 integral definitions | exact Burnside basis coefficients | `PROVED_DEFINITION_SEPARATION` |
| G4 | On $C/K$, the $C$-permutation stabilizer is $\widehat K_a=\langle0\times K,(1,a^{-1})\rangle$ and all orbit types recover $a$ only modulo the action kernel $N=\cap K$ | direct stabilizer calculation | Gusein-Zade 2013 | exact cosets/kernel | `PROVED_CONDITIONAL_TWIST_RECOVERY` |
| G5 | $[X/C]\simeq\coprod_Kn_KBK$; inertia has $\sum n_K|K|$ static sectors | quotient groupoids; $C$ abelian | orbifold/inertia literature; Ebeling--Gusein-Zade 2018 | sector and identity-action counts | `PROVED_STABILIZER_WITHOUT_CLOCK` |
| G6 | The effective action $C_6/C_2\sqcup C_6/C_3$ recovers its labelled generator in the $C$-permutation invariant but has source zeta $(1-t^3)^{-1}(1-t^2)^{-1}$, no period-$6$ factor, coarse zeta $(1-t)^{-2}$, and five static inertia sectors | G1--G5 with $C_2\cap C_3=1$ | direct diagnostic, not a novel theorem | proof/development control only; not a modulus row | `PROVED_COUNTEREXAMPLE` |
| C1 | $X_q=\mathrm{CV}_q$ is the regular $G_q=C_q$-torsor and $\phi_q=L_{a_q}$ with $a_q=A$ | Bound Paper-10 terminal theorem | Paper 10; BNR 2013 upstream | reproduce upstream sets and action without rerunning Paper 10 | `BOUND_UPSTREAM` |
| C2 | Every point of $X_q$ has exact $\phi_q$-period $r_q=\operatorname{ord}_q(A)$ and there are $m_q=n_q/r_q$ cycles | cancellation in the regular group | elementary | exact cycle partition | `PROVED` |
| C3 | $L^{G_q}(\phi_q^k)=\mathbf u_q$ iff $r_q\mid k$ and is zero otherwise | fixed translation criterion | fixed-point equivariant Lefschetz class used by the 2008 rational construction and contrasted with the alternative in 2015 | exact sequence for $1\le k\le2r_q$ plus divisor inversion | `PROVED_PRIOR_DEFINITION` |
| C4 | The point-order Burnside zeta is $(1-t^{r_q})^{-\mathbf u_q/r_q}$ | C3 and divisor inversion | Gusein-Zade--Luengo--Melle-Hernández 2008; reviewed in 2015 | formal support/coefficient record | `PROVED_LOW_NOVELTY` |
| C5 | The untwisted point-order zeta depends on $a_q$ only through $r_q$ | C3 | definition consequence | compare symbolically after replacing $a_q$ by any enumerated same-order element only in unit tests, not a new candidate | `PROVED_NONINJECTIVE_IN_GENERATOR` |
| C6 | $\widetilde L^{G_q}(\phi_q^k)=\mathbf u_q$ for every $k\ge1$ | unique setwise fixed $G_q$-orbit | Gusein-Zade et al. 2015 orbit-counting version | exact sequence | `PROVED_PRIOR_DEFINITION` |
| C7 | The integral orbit-order zeta is $(1-t)^{-\mathbf u_q}$ | C6 and divisor inversion | Gusein-Zade et al. 2015, especially the case monodromy lies in $G$ | formal support/coefficient record | `PROVED_CLOCK_COLLAPSE` |
| C8 | The regular Burnside marks are $n_q$ at $K=1$ and zero for every nontrivial $K\le G_q$ | freeness | Burnside mark theory | enumerate every subgroup of the fixed finite matrix group and every fixed set | `PROVED_STABILIZER_PROFILE` |
| C9 | Exact-period cardinality reduction of the point-order zeta is $(1-t^{r_q})^{-m_q}$ | $\kappa_q(\mathbf u_q)=n_q$; reduction is applied to exponent classes, not assumed to preserve every Burnside power | ordinary source zeta | exact exponent pair $(r_q,m_q)$ | `PROVED_MULTIPLICITY_RETURNS` |
| C10 | Additive exact-period orbifold reduction of the point-order zeta is $(1-t^{r_q})^{-1/r_q}$ | $G_q$ abelian and $\Phi_q([G_q/1])=1$; no multiplicativity or power-structure preservation is used | Gusein-Zade et al. 2015 | exact rational exponent | `PROVED_FRACTIONAL_EXPONENT` |
| C11 | Cardinality of the orbit-order zeta is $(1-t)^{-n_q}$ | same maps | 2015 | exact exponent pair $(1,n_q)$ | `PROVED` |
| C12 | Additive exact-period orbifold reduction of the orbit-order zeta is $(1-t)^{-1}$ | same exponentwise additive map | 2015 | exact exponent pair $(1,1)$ | `PROVED_ONE_FACTOR_NO_CLOCK` |
| C13 | $L^{G_q}(g\phi_q^k)=\mathbf u_q$ iff $g=a_q^{-k}$ | twisted translation criterion | Gusein-Zade 2013 | enumerate all $g\in G_q$ for $0\le k<r_q$ | `PROVED_STRONGER_INVARIANT_INPUT` |
| C14 | The 2013 $G_q$-permutation triple is $(1,1,a_q^{-1})$ | stabilizer $\{(k,a_q^{-k})\}$ | Gusein-Zade 2013 $(\mathbb Z\times G)$-set classification | exact stabilizer/twist comparison | `PROVED_TWIST_RETAINED` |
| C15 | The twist recovers exact $a_q$ only after the effective labelled regular $G_q$-action is fixed | C14; kernel is trivial | 2013 classification uses $C_G(H)/H$ | verify action kernel is trivial; record coefficient-ring identity | `PROVED_CONDITIONAL_RETENTION` |
| C16 | The enhanced class is $\widehat X_{1,1,a_q,1}$ | free orbit, quotient period one, return twist $a_q$, trivial character | Ebeling--Gusein-Zade 2018 | exact tuple and order | `PROVED_PRIOR_CARRIER` |
| C17 | The enhanced orbifold zeta is $(1-t)^{-1}$ | only identity fixed sector; quotient point | Ebeling--Gusein-Zade 2018 | enumerate all fixed sectors | `PROVED_INERTIA_COLLAPSE` |
| C18 | $G_q\ltimes X_q\simeq*$ and $F_{a_q}\cong\operatorname{Id}$ | free transitivity; natural transformation labelled $a_q$ | elementary action-groupoid fact | finite groupoid checks and naturality table | `PROVED_MORITA_BOUNDARY` |
| C19 | A Morita/$2$-isomorphism invariant of the quotient stack must equal its one-fixed-point value | C18 and functoriality assumption | quotient-stack formalism | categorical booleans only; no universal zeta implementation | `CONDITIONAL_THEOREM` |
| C20 | Each source cycle shortens by $1/r_q$ and $m_q$ cycles glue | orbit intersection has size $r_q$ | Zegowitz 2017 | exact intersection, shortening, gluing | `PROVED_PRIOR_COROLLARY` |
| C21 | None of the four audited scalar reductions has both source support $r_q$ and unit exponent | C9--C12 | direct comparison | exact four-row signature | `PROVED_RETENTION_COMPRESSION_TRADEOFF` |
| C22 | The stronger carriers retain $a_q$ only in varying labelled coefficient categories | C14--C16 | 2013/2018 constructions fix one ambient $G$ | record ring/group fingerprints and absence of comparison map | `PROVED_CONSTRUCTION_COST` |
| C23 | $r_q$ is not a modulus clock: $r_2=r_4=3$ and $r_6=r_9=12$ | bound Paper-10 exact ledger | elementary counterexample | reproduce exact collision groups | `PROVED_MODULUS_NONINJECTIVITY` |
| C24 | The entire construction applies to composite $q$ | Paper-10 all-$q$ torsor plus definition-only arguments | BNR rational lattices; Paper 10 | fixed composites $4,6,9,10$ | `PROVED_PROVES_TOO_MUCH` |
| C25 | Specializing $t=q^{-s}$, raising by $r_q$, or comparing the varying rings is extra data | no such datum occurs in C1--C24 | semantic consequence; Gusein-Zade distinctions | mandatory external-operation flags; no numeric evaluation | `A0_FAIL_COMPONENT` |
| C26 | The terminal decision is A0 failure and Route B stays closed | C21--C25 | project decision rule | exact machine certificate only after all gates | `FORMAL_DECISION` |

## Proof-derived fixed ledger

The audit order is exactly

$$
(2,3,5,7,11,4,6,9,10).
$$

| $q$ | $n_q$ | $r_q$ | $m_q$ | point Burnside support | orbit Burnside support | $\kappa$(point) exponent | $\Phi$(point) exponent | $\kappa$(orbit) exponent | $\Phi$(orbit) exponent | $G$-perm twist | enhanced tuple | stack period |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| 2 | 3 | 3 | 1 | 3 | 1 | 1 | $1/3$ | 3 | 1 | $A^{-1}$ | $(1,1,A,1)$ | 1 |
| 3 | 8 | 4 | 2 | 4 | 1 | 2 | $1/4$ | 8 | 1 | $A^{-1}$ | $(1,1,A,1)$ | 1 |
| 5 | 20 | 10 | 2 | 10 | 1 | 2 | $1/10$ | 20 | 1 | $A^{-1}$ | $(1,1,A,1)$ | 1 |
| 7 | 48 | 8 | 6 | 8 | 1 | 6 | $1/8$ | 48 | 1 | $A^{-1}$ | $(1,1,A,1)$ | 1 |
| 11 | 100 | 5 | 20 | 5 | 1 | 20 | $1/5$ | 100 | 1 | $A^{-1}$ | $(1,1,A,1)$ | 1 |
| 4 | 12 | 3 | 4 | 3 | 1 | 4 | $1/3$ | 12 | 1 | $A^{-1}$ | $(1,1,A,1)$ | 1 |
| 6 | 24 | 12 | 2 | 12 | 1 | 2 | $1/12$ | 24 | 1 | $A^{-1}$ | $(1,1,A,1)$ | 1 |
| 9 | 72 | 12 | 6 | 12 | 1 | 6 | $1/12$ | 72 | 1 | $A^{-1}$ | $(1,1,A,1)$ | 1 |
| 10 | 60 | 30 | 2 | 30 | 1 | 2 | $1/30$ | 60 | 1 | $A^{-1}$ | $(1,1,A,1)$ | 1 |

Here every occurrence of $A$ means its exact reduction in the matrix group
$G_q$, not an abstract symbol shared across coefficient rings.

## Primary-source map

| Key | Verified primary record | Allowed use | Forbidden inference |
|---|---|---|---|
| `GuseinZadeLuengoMelle2008` | AMS Translations Series 2, vol. 224, 139--146; arXiv `0803.3708` | rational point-order Burnside/power-structure predecessor | that 2015 or Paper 11 originated it |
| `GuseinZadeLuengoMelle2015` | *Arnold Math. J.* 1(2), 127--140; DOI `10.1007/s40598-015-0012-8`; arXiv `1203.3344` | separate fixed-point and fixed-orbit Lefschetz/zeta definitions; orbifold reductions | that the two definitions are one invariant or that Paper 11 invents them |
| `GuseinZade2013` | *Funct. Anal. Appl.* 47(1), 14--20; arXiv `1207.2282` | $(\mathbb Z\times G)$-set/$G$-permutation invariant and triple $(H,m,\alpha)$ | that an untwisted Burnside series already retains the generator |
| `EbelingGuseinZade2018` | *J. Algebra Appl.* 17(10), 1850181; DOI `10.1142/S0219498818501815`; arXiv `1506.05604` | enhanced carrier and enhanced orbifold fixed-sector formula | new enhanced or orbifold theory |
| `Zegowitz2017` | *ETDS* 37(7), 2337--2352; DOI `10.1017/etds.2016.3`; arXiv `1502.02693` | exact shortening/gluing terminology and formulas | new quotient-orbit theorem |
| `Walton2018` | *JNT* 189, 202--223; DOI `10.1016/j.jnt.2018.03.023`; arXiv `1705.09034` | finite-field quotient/twist scope boundary | direct composite-residue-ring support |
| `Miles2017` | *Monatsh. Math.* 182(3), 683--708; DOI `10.1007/s00605-016-0909-x`; arXiv `1506.08555` | infinite acting-group zeta boundary | a finite-$G_q$ implementation without a new extension |
| `HochsSaratchandran2023` | arXiv `2303.00312` | current equivariant Ruelle context | finite-torsor Burnside formula |
| `HochsSaratchandran2025` | arXiv `2502.08367` | current equivariant trace-formula context | Paper-11 trace/Fredholm claim |
| `HochsPirie2025` | arXiv `2507.06792` | current equivariant Fried context | Paper-11 analytic torsion claim |
| `Rahmati2024` | *Contemp. Math.* 5(2), 1820--1842; DOI `10.37256/cm.5220244455` | current orbifold cohomological/Mackey zeta boundary | finite internal-permutation formula |
| `AyalaMazelGeeRozenblyum2025` | *Adv. Math.* 466, 110170; DOI `10.1016/j.aim.2025.110170`; arXiv `2405.03897` | current cyclic-nerve/marked-loop boundary | finite Burnside zeta claim |
| `GuseinZade2026` | *Handbook of Geometry and Topology of Singularities VIII*, 289--316; DOI `10.1007/978-3-031-99571-2_7` | current monodromy-zeta survey context | originality evidence |

## Evidence-policy locks

1. Paper-10 terminal artifacts are immutable upstream evidence, not data to
   rerun or tune.
2. The only modulus tuple is the inherited nine-entry tuple above.
3. No prime generation, composite replacement, Riemann-zero access, network
   access during a registered audit, numerical $s$, numerical $\log q$, or
   numerical $q^{-s}$ is allowed.
4. Point-order, orbit-order, $G$-permutation, enhanced, orbifold, and stack
   outputs must have distinct schema keys.
5. The abstract $C_6$ counterexample is a proof/development control, not a
   tenth modulus, a candidate, or a registered arithmetic data point.
6. The inverse convention in the 2013 triple is frozen by
   $(k,g)x=ga_q^kx$, giving $a_q^{-1}$.
7. All-q statements are proof-derived; nine finite controls are
   falsification/implementation checks only.
8. A pass cannot increase novelty or open transfer, Fredholm, Hecke,
   quantization, Ruelle/Fried, prime/zero, RH, or Route-B claims.

## Terminal wording lock

If and only if source, deployment, result-integrity, and later manuscript
gates pass, the result may say:

> Standard equivariant refinements retain different pieces of the regular
> centralizer torsor.  The point-order Burnside zeta retains source order but
> restores multiplicity under cardinality; the integral orbit-order zeta has
> quotient period one; the $G$-permutation and enhanced carriers retain the
> translating element only in a labelled modulus-dependent category; and the
> orbifold/free-stack images are one fixed point.  Composite moduli satisfy
> the same formulas, so no intrinsic prime/modulus clock is produced.

The exact machine classification is

`EQUIVARIANT_RETENTION_COMPRESSION_TRADEOFF_CERTIFIED /`
`A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC / ROUTE_B_NOT_OPENED`.
