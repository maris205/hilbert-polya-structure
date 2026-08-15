# Claims--Evidence Matrix

## Frozen status

- Candidate: `cat_centralizer_cyclic_torsor_v1`.
- Feasibility: `GO_SCOPED_NEGATIVE_NOTE_LOW_NOVELTY`.
- Required certificate:
  `CENTRALIZER_CYCLIC_TORSOR_CERTIFIED /`
  `A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC / ROUTE_B_NOT_OPENED`.
- Evidence state at source design: theorem package complete; no Paper-10 code,
  registered run, result, or manuscript authorized.

## Claim matrix

| ID | Frozen claim | Proof evidence | Closest literature / collision | Later exact audit | Boundary / status |
|---|---|---|---|---|---|
| C1 | $e_1$ is cyclic over every $R_q$ because $\det[e_1,Ae_1]=1$ | Direct determinant | BNR 2013 uses cyclic vectors over rational lattices | recompute determinant for every frozen $q$ | `PROVED`; not novel |
| C2 | $\operatorname{Cent}_{\mathrm{Mat}_2(R_q)}(A)=R_q[A]$ and $C_q=R_q[A]^\times$ for all $q\ge2$ | A commuting matrix is determined by its value on the cyclic basis | BNR 2013; standard cyclic-matrix commutant fact | enumerate all commuting matrices at nine frozen moduli and compare exact sets | `PROVED`; no new centralizer theorem |
| C3 | $U\mapsto Ue_1$ is a bijection $C_q\to\mathrm{CV}_q$ | $[Ue_1,AUe_1]=U[e_1,Ae_1]$ and determinant-unit criterion | Elementary torsor corollary; BNR finite-ring symmetry example is close | exact injectivity, surjectivity, freeness, transitivity | `PROVED_TORSOR`; safe packaging delta |
| C4 | $\mathrm{CV}_q\subseteq E_q$ and $|\mathrm{CV}_q|=|C_q|$ | A cyclic vector is unimodular and hence has exact additive order $q$ | Finite-module arithmetic | exact additive-order and cardinality checks | `PROVED` |
| C5 | $\Gamma_q^{\rm cyc}\simeq C_q/\langle A\rangle$ and has $|C_q|/\operatorname{ord}_q(A)$ orbits | Torsor identification; a return of one cyclic vector forces $A^k=I$ | Standard orbit--stabilizer | exact $A$-orbit partition and uniform length | `PROVED` |
| C6 | Quotienting $\Gamma_q^{\rm cyc}$ by the residual centralizer leaves one set class | $C_q/\langle A\rangle$ acts simply transitively | Elementary group action | exact quotient cardinality one | `PROVED_SET_QUOTIENT` |
| C7 | Since $A\in C_q$, the induced $A$ map on $\mathrm{CV}_q/C_q$ is the identity; its native period is $1$, independent of $q$ | Definition of quotient action | Gusein-Zade--Luengo--Melle-Hernández 2015 distinguish order in $X$ and in $X/G$ | verify induced transition is identity and contains no stored modulus clock | `PROVED_CLOCK_KILL`; not a new zeta theorem |
| C8 | Substituting $z=q^{-s}$ into $(1-z)^{-1}$ is an external label, not a quotient return-time law | C7 plus absence of a $q$-dependent quotient period or point potential | Equivariant/orbifold zeta literature shows finer alternatives | schema must label the factor `EXTERNAL_MODULUS_SPECIALIZATION` | `A0_FAIL_COMPONENT` |
| C9 | $C_q\simeq S_q^\times$ and determinant is the norm $N_q(a+bT)=a^2+3ab+b^2$ | Direct algebra isomorphism and determinant | Kurlberg--Rudnick 2000 norm-one Hecke centralizers; BNR 2013 | compare algebra units, centralizer, determinant, and norm exactly | `PROVED`; strong prior collision |
| C10 | $\mathrm{CV}_q/C_q^1\simeq\operatorname{im}N_q$ via $\Delta_q$ | $\Delta_q(Dv)=\det(D)\Delta_q(v)$ and torsor fibers | Kurlberg--Rudnick; standard norm-torus action | enumerate $C_q^1$ orbits and $\Delta_q$ fibers | `PROVED_SYMPLECTIC_BOUNDARY` |
| C11 | $|\operatorname{im}N_q|=\varphi(q)$ if $5\nmid q$ and $\varphi(q)/2$ if $5\mid q$ | CRT; split/unramified norm surjectivity; ramified unit norms have square residue mod $5$ and full principal-unit image | Kurlberg--Rudnick local norm analysis | exact norm image at all nine frozen moduli | `PROVED`; independent review must stress $p=2,5$ |
| C12 | The induced $A$ map on $\mathrm{CV}_q/C_q^1$ is also the identity | $A\in C_q^1$ | General quotient fact | exact class-transition identity | `PROVED`; symplectic restriction does not restore clock |
| C13 | For inert/binary $p$, $\mathrm{CV}_p=E_p$ and $E_p/C_p$ has one class | anisotropy of $x^2-xy-y^2$; $S_p\simeq\mathbb F_{p^2}$ | BNR finite-field type IV; Gaspari prime lattices | $p=2,3,7$ exact profiles | `PROVED`; classical |
| C14 | For split $p\ne5$, $|\mathrm{CV}_p|=(p-1)^2$, two eigenlines are discarded, and $E_p/C_p$ has three classes | factor the discriminant-five form into two lines; diagonal centralizer | BNR finite-field type III | $p=11$: $120/100/20$ counts and $3$ full-centralizer strata | `PROVED`; classical corollary |
| C15 | At $p=5$, $|\mathrm{CV}_5|=20$, four eigenline points are discarded, and $E_5/C_5$ has two classes | double linear factor/Jordan centralizer | BNR type II and Arnold-cat appendix | exact $24/20/4$ counts and $2$ strata | `PROVED`; classical corollary |
| C16 | The fixed reversor $J$ can merge the split eigenlines but the reversing group cannot merge cyclic and noncyclic strata | $JAJ^{-1}=A^{-1}$; split eigenspace swap; ramified generalized eigenline preservation | BNR reversing-symmetry groups | enumerate prime reversing groups only; expected full-shell orbit counts $1,1,2,1,2$ at $2,3,5,7,11$ | `PROVED_CASEWISE`; no universal normalizer theorem claimed |
| C17 | $|\mathrm{CV}_q|=\prod_{p^k\parallel q}p^{2(k-1)}c_p$ with the frozen local $c_p$ | CRT and lifting of nonzero residues | BNR prime-power rational lattices; Tan--Li 2025 | exact counts at $q=4,6,9,10$ | `PROVED`; no new finite-ring cycle theory |
| C18 | Full-centralizer multiplicity-one holds for all composite controls, so it is non-prime-specific | C3 for all $q$; explicit composite counts | Same rational-lattice setting in BNR | each composite has $|\mathrm{CV}_q/C_q|=1$ | `PROVED_PROVES_TOO_MUCH_CONTROL` |
| C19 | The fixed nine-modulus ledger is exact | Proof package arithmetic | Paper-9 inherited prime controls; no literature inference from the table | reproduce every integer and relation byte-for-byte | `AUDIT_ONLY`; finite data do not prove the theorem |
| C20 | The valid terminal classification is A0 failure, not A1/A2 success | C7, C8, C12, C18; Route-A rule against hand-assigned $\log p$ clocks and proves-too-much controls | project Route-A evaluator | validate terminal classification and zero forbidden-route fields | `FORMAL_DECISION` |
| C21 | The full $C_q$ quotient uses a $q$-dependent local pseudo-symmetry group and does not require one fixed global commuting torus automorphism | reduction of the global integral centralizer lands in $C_q$, but the quotient is defined using all modulo-$q$ commuters | BNR local versus global symmetry context | record the local-group scope; do not attempt a global-lift classification | `PROVED_CONSTRUCTION_COST`; no claim that every local element fails to lift |
| X1 | Burnside/equivariant/orbifold zeta may retain information lost by the coarse quotient | not investigated | Gusein-Zade--Luengo--Melle-Hernández 2015 | none | `OUTSIDE_SCOPE_PAPER11`; no impossibility claim |
| X2 | Group-action, stack, groupoid, or twisted-sector factors may differ from the coarse quotient | not investigated | Miles 2015 and equivariant/orbifold literature | none | `OUTSIDE_SCOPE_PAPER11` |
| X3 | Norm-one Hecke quantization may use the symplectic centralizer nontrivially | not investigated | Kurlberg--Rudnick 2000 | none | `OUTSIDE_SCOPE`; Route B remains closed |

## Proof-derived exact control ledger

| $q$ | $|E_q|$ | $|\mathrm{CV}_q|$ | discarded | $|C_q|$ | $|C_q^1|$ | $\operatorname{ord}_q(A)$ | cyclic $A$-orbits | full-$C_q$ CV quotient | $C_q^1$ CV quotient | full-shell $C_q$ orbits |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | 3 | 3 | 0 | 3 | 3 | 3 | 1 | 1 | 1 | 1 |
| 3 | 8 | 8 | 0 | 8 | 4 | 4 | 2 | 1 | 2 | 1 |
| 5 | 24 | 20 | 4 | 20 | 10 | 10 | 2 | 1 | 2 | 2 |
| 7 | 48 | 48 | 0 | 48 | 8 | 8 | 6 | 1 | 6 | 1 |
| 11 | 120 | 100 | 20 | 100 | 10 | 5 | 20 | 1 | 10 | 3 |
| 4 | 12 | 12 | 0 | 12 | 6 | 3 | 4 | 1 | 2 | 1 |
| 6 | 24 | 24 | 0 | 24 | 12 | 12 | 2 | 1 | 2 | 1 |
| 9 | 72 | 72 | 0 | 72 | 12 | 12 | 6 | 1 | 6 | 1 |
| 10 | 72 | 60 | 12 | 60 | 30 | 30 | 2 | 1 | 2 | 2 |

The full-shell symplectic-centralizer orbit counts, useful as an additional
exact check but not needed for the core theorem, are respectively

$$
1,2,4,6,12,2,2,6,4
$$

in the displayed modulus order.

## Primary-source map

| Key | Verified primary record | Allowed use | Forbidden inference |
|---|---|---|---|
| `BaakeNeumaerkerRoberts2013` | Baake, Neumärker, Roberts, *DCDS-A* 33(2), 527--553, DOI `10.3934/dcds.2013.33.527`, arXiv `1205.1003` | rational-lattice symmetries; cyclic commutant; finite-field types; Arnold-cat prime powers | that Paper 10 discovers these groups or cycle classifications |
| `KurlbergRudnick2000` | Kurlberg, Rudnick, *Duke Math. J.* 103(1), 47--77, DOI `10.1215/S0012-7094-00-10314-6`, arXiv `chao-dyn/9901031` | norm-one modular centralizers and Hecke-symmetry context; local norm cases | any Paper-10 quantization or equidistribution result |
| `GuseinZadeLuengoMelle2015` | Gusein-Zade, Luengo, Melle-Hernández, *Arnold Math. J.* 1(2), 127--140, DOI `10.1007/s40598-015-0012-8`, arXiv `1203.3344` | distinction between order in $X$ and $X/G$; finer equivariant/orbifold zetas | that coarse quotient exhausts equivariant, orbifold, or stacky information |
| `Gaspari1994` | Gaspari, *Physica D* 73, 352--372, DOI `10.1016/0167-2789(94)90105-8` | prime-lattice cat-map context | new prime-shell classification |
| `BaakeRobertsWeiss2008` | Baake, Roberts, Weiss, *Nonlinearity* 21, 2427--2446, DOI `10.1088/0951-7715/21/10/012`, arXiv `0808.3489` | finite/rational-lattice orbit and Euler-product context | new finite-lattice zeta theory |
| `Miles2015` | Richard Miles, “A dynamical zeta function for group actions,” arXiv `1506.08555` | group-action zeta outside-scope boundary | direct support for the coarse quotient formula beyond the stated convention |
| `TanLi2025` | Tan, Li, arXiv `2506.20118` | current prime-power cycle/lifting collision | Paper-10 centralizer quotient theorem |
| `Chandra2026` | Chandra, arXiv `2607.24857` | current finite-permutation determinant/cycle-product collision | centralizer torsor, quotient, or Hecke claims |

## Evidence-policy locks

1. The all-$q$ statements are theorem-derived; nine finite controls cannot
   establish them.
2. No external prime table, generated prime array, factor database, or
   Riemann-zero data may be accessed.
3. No numerical $s$, $\log q$, or $q^{-s}$ may be evaluated.
4. The prime set is inherited and fixed; the composite set is structurally
   predeclared and fixed.
5. No matrix, centralizer ambient group, cyclic stratum, or norm convention
   may change after source lock.
6. A failure at any frozen modulus invalidates the registered audit; no
   replacement modulus or post-hoc exception is allowed.
7. A pass cannot increase novelty, open Route B, or support an equivariant,
   stacky, Hecke, transfer, Fredholm, quantum, prime/zero, or RH claim.

## Terminal wording lock

If and only if the source review, code review, and registered exact audit all
pass, the result may say:

> The cyclic-vector locus is a full-centralizer torsor at every modulus.  Its
> coarse full-centralizer quotient has one class but only identity induced
> dynamics; restricting to symplectic centralizers leaves norm classes, and
> composite moduli pass the same multiplicity-one construction.  Hence the
> proposed factor requires an external modulus/prime clock.

The exact machine classification is

`CENTRALIZER_CYCLIC_TORSOR_CERTIFIED /`
`A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC / ROUTE_B_NOT_OPENED`.
