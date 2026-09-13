# Independent Source-Design Review

Date: 2026-08-19 UTC

Project: `papers/19-shiftlike-translate-gcd-obstruction`

Role: fresh post-author independent source-design reviewer

## Verdict and authority boundary

I read the exact ten-file author package to EOF after the author stopped, and
then independently replayed the definitions, index conversions, relation
lattices, scalar reconstruction, family geometry, arbitrary-rank character
argument, generating functions, selected labels, arithmetic bridge,
predecessor ownership, and bounded literature comparison. I did not treat any
candidate-stage review as proof evidence.

All nine required audit blocks `E1--E9` pass. There are zero blocking,
required, cosmetic, or advisory findings. The fresh literature refresh found
no direct external collision. That is a bounded negative result, not a claim
of priority or an exclusion of unindexed, non-English, unpublished, or private
work.

This review authorizes only the source-design verdict on the frozen ten author
files. It does not create or authorize a source lock, paper plan, bibliography,
TeX source, appendix, figure, code, data, computation, build, PDF, release,
submission, upload, repository push, external message, dashboard transition,
or identity disclosure.

## Exact author input and independent binding

Immediately before this review was added, the project contained exactly ten
regular files in exactly three descendant directories, with zero symlinks and
zero other entry types. The independently measured ledger is:

| Relative path | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `experiments/EXPERIMENT_PLAN.md` | `85a38df6f2fbf056aa2ca38de02566e3ddf3d165704c17446e6c05c74779ef2f` | 8,034 | 197 |
| `experiments/EXPERIMENT_TRACKER.md` | `cbf456ab962ba39e9a9f5b1abbc8c68f078e73caf5928661cb1a2304359ff480` | 3,237 | 103 |
| `notes/CITATION_VERIFICATION.md` | `6bc87aaac7caaf47b448d0f1e8a9da886999c8990cdec0f7d8bf47119be84a06` | 10,897 | 200 |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | `dd26db0e9446e9258734ec5f10d2cc05aef5e921a9a487bfd0051c849cbf0aae` | 10,474 | 88 |
| `notes/NOVELTY_ASSESSMENT.md` | `612fb2a1e0168e314e5f00872e23a88bfd44a577e56153695e0664305fda7e9b` | 10,172 | 195 |
| `notes/PROOF_PACKAGE.md` | `619d9fde3bbf206ae404b8c5f6bbf8f20ab08904f14026dd7ccd31d2951e600b` | 32,247 | 892 |
| `notes/RESEARCH_QUESTION.md` | `9a7c5039f19f1b86a09b1eb25b32bfd8e05a39903c8899bb02169818129df715` | 21,278 | 580 |
| `refine-logs/FINAL_PROPOSAL.md` | `d863f893f41d74f5ed46ff0448d3424c44057a448cbd06f407be0e50f5ec08b7` | 10,765 | 328 |
| `refine-logs/INITIAL_PROPOSAL.md` | `21a72723d938fe860ee68e8f522e8ab50a0f0b86537598303bd39354ee2e7980` | 8,338 | 246 |
| `refine-logs/REVIEW_SUMMARY.md` | `aae1fcc983ec32b52d006e93f2e99253e260571b114c769f0742d11dae6e619b` | 12,404 | 332 |

Total author input: 127,846 bytes and 3,161 LF.

Using exactly the sorted byte records

`relative-path<TAB>sha256<TAB>bytes<TAB>LF<LF>`,

the ten-file author aggregate is

`5d963e353fa915a0832adeb380cd69c1f8cc76becf8825a546bf243f83937fea`.

This was recomputed independently rather than copied from the author handoff.

## D1--D8 convention replay

The author prose groups `D1--D3` and separately labels `D6`; it does not invent
literal theorem labels for the other conventions. I therefore audited the
complete eight-obligation convention ledger directly:

1. `D1` passes: geometric containment is over an algebraically closed field
   `Omega` of characteristic zero, while arithmetic conclusions retain an
   arbitrary characteristic-zero field.
2. `D2` passes: the type-`nu` map has the stated coordinate orientation and
   inverse
   `a^(-1)(w_k-P(w_(k-nu))),w_1,...,w_(k-1)`.
3. `D3` passes: zero-based coordinates give
   `x_(n+k)=P(x_(n+k-nu))+a x_n` with no reversal of `nu`.
4. `D4` passes: `V_m` has ambient coordinates `x_0,...,x_(k+m-1)` and exactly
   the equations `0<=n<m`; `V_0` is the full initial torus.
5. `D5` passes: `T_m` contains states at times `0,...,m`, and forward
   uniqueness makes projection from `V_m intersect Gamma^(k+m)` a bijection.
   No dimension language is transferred to `T_m`.
6. `D6` passes: a coset of `H_m` has one and only one representative whose
   free initial scalars equal one.
7. `D7` passes: a translate uses a connected closed subtorus, and restrictions
   of ambient coordinate characters surject onto the actual `X*(H)`.
8. `D8` passes: finite rank allows arbitrary torsion, is reduced to a division
   hull of a finitely generated subgroup, and is transferred through a
   finitely generated coefficient-and-generator field rather than by falsely
   embedding the whole ground field in `C`.

## E1--E4 and Part A replay

### E1: orientation and windows -- PASS

Substitution into the displayed inverse returns every input coordinate, and
the scalar recurrence has the stated middle index. At `m=kq`, the last
original equation is `kq-1`, so the last possible future coordinate is
`u_(kq+k-1)`. The incorrect endpoint `u_(2kq-1)` agrees only accidentally in
special dimensions and is nowhere used as the theorem endpoint.

### E2: `TA1--TA2` -- PASS

For the anchored polynomial with at least two actual nonconstant monomials,
if the middle character is nonzero, the `s+1>=3` distinct characters
`0,e_1u,...,e_su` cannot all be paired by two endpoint terms. Thus every
middle character is zero. The remaining identity gives both relation families

`epsilon_(k+n-nu)` and `epsilon_(k+n)-epsilon_n`.

After quotienting by the copy relations, the first family kills exactly the
distinct initial residues

`R_m={n-nu mod k:0<=n<m}`.

The quotient is free on the other `k-m` initial indices. Hence `L_m` is
saturated of rank `2m`; at equality, the actual character kernel has the same
rank and must equal `L_m`. This proves the embedded subgroup identity
`H=H_m`, not merely an isogeny or equality of dimensions.

For a normalized representative, direct residue membership gives

`A_m=[max(0,m-nu),min(m,k-nu))`

and the four endpoint-order cases give

`alpha_m=min(m,k-m,nu,k-nu)`.

The reconstruction is exhaustive. For `n<nu`, `y_n` is the killed initial
middle scalar. For `n>=nu`, the earlier recurrence gives

`xi_(n-nu)=a^(-1)(y_n-P(y_(n-nu)))`.

Outputs are `xi_(k+j)=P(y_j)+a xi_j`. Outputs already occurring as later
`y` coordinates agree by substitution. The first open condition is precisely
nonvanishing of the solved killed initials. An output not already a later `y`
is either automatically `a` at an active index or, for `k-nu<=j<m`, requires

`P(y_j)+a y_(j+nu-k)!=0`.

Thus no scalar coordinate or open condition is omitted or duplicated, and
geometric points of `E_m` classify exactly normalized translates of dimension
`k-m`.

### E3: `TA3--TA4` geometry -- PASS

For every active root tuple, either side of an inequality separated by `nu`
or by `k-nu` contains a free variable: the active interval has length at most
both separations. Each forbidden zero set is therefore proper (and can be
empty). Their finite union cannot cover the remaining irreducible torus. If
`alpha_m=m`, then `m<=nu` and `m<=k-nu`, so both inequality index sets are
empty. This proves coefficientwise and root-tuple-wise nonemptiness without a
one-root shortcut.

For squarefree `P` of degree `delta`, the disjoint root assignments give
exactly `delta^alpha_m` nonempty smooth irreducible open-torus components of
dimension `m-alpha_m`. With `r` distinct roots, reduction gives exactly
`r^alpha_m` geometric components.

Over the fixed actual-support coefficient torus, the leading and constant
coefficients are units. Dividing by the leading coefficient makes the root
algebra monic and free on `1,X,...,X^(delta-1)`; the unit constant term makes
`X` invertible. The root scheme is finite locally free of degree `delta`.
The universal translate scheme is the stated open in its `alpha_m`-fold
product with the free torus, so it is flat and relative lci, and it is smooth
over the discriminant complement.

At active multiplicities `mu_i`, local factorization by units gives the
completed fiber ring

`Omega[[t_1,...,t_(m-alpha_m),z_1,...,z_(alpha_m)]]`

`/(z_1^(mu_1),...,z_(alpha_m)^(mu_(alpha_m)))`.

The inequalities are units at the chosen point. This is correctly a completed
fiber statement, not a classification of the total singular locus. The term
“normalized translate scheme” is warranted; Hilbert-, Fano-, and fine-moduli
claims are not.

### E4: `CA1` -- PASS

At `m=k-1`, `alpha_(k-1)=1`, `E_(k-1)` is nonempty for every coefficient
tuple, and each represented subgroup has dimension one and is saturated. A
geometric translating point has finitely many algebraic coordinates, hence
lies over a finite algebraic extension of the coefficient field. Adjoining
those scalars and the infinite-order element `2` gives a finitely generated
compatible group. Varying the one-torus parameter through `2^N` gives
distinct points and, by projection, infinite `T_(k-1)`. Paper 17 owns the
terminal `T_k` finiteness theorem. The package never upgrades this to every
fixed group or to no field extension.

## E5--E8 and Part B replay

### E5: labels, signs, gcd, and original counts -- PASS

The four group-algebra terms have nonzero coefficients. A vanishing sum has no
singleton character class, so its partition is either all-zero `Z` or one of
the three pairings `A/B/C`. Recombining coefficients gives exactly:

- `A`: future `=b middle^d`, and `a old=-c`;
- `B`: future `=a old`, and `b middle^d=-c`;
- `C`: future `=c`, and `a old=-b middle^d`; and
- `Z`: the full scalar recurrence.

The nonzero `v` in `A/B/C` makes the labels exclusive, and their supports give
`s_(j+q)=s_j+s_(j+L)` over `F_2`.

With `g=gcd(k,nu)`, `q=k/g`, and `L=(k-nu)/g`, one has `q>=2`,
`1<=L<q`, and `gcd(q,L)=1`. At `m=kq=gq^2`, every original residue receives
`q^2` equations. At `m=kq-1`, residues `0,...,g-2` receive `q^2`, while
residue `g-1` receives `q^2-1`. The ambient endpoint is respectively
`kq+k-1` or `kq+k-2`, and every coordinate in each residue is covered by the
corresponding core word.

### E6: arbitrary-rank colored components and `TB4` -- PASS

The directed weights are `+1` from middle to future for `A`, `0` from old to
future for `B`, and `+1` from middle to old for `C`. A nonzero signed cycle
would imply `v=d^s v` in the torsion-free rationalized character lattice; since
`d>=2`, its signed weight must be zero. Integer heights therefore exist on
every connected component. Distinct formal colors are necessary and correctly
prevent accidental equality of actual character values from merging
disconnected components. Label by label, the colored word satisfies

`F_(j+q)=F_j+T F_(j+L)`.

For any chosen nonzero component, a minimum-height vertex traces backward as
an output only through `B` labels until an index `r in [0,q-1]`. Forward at
the minimum height again forces `B`; its middle character is globally zero,
not merely absent from the chosen color. Consecutive zeros separated by `q`
therefore propagate the genuine triangular zero set

`u_(r+tL+jq)=0`, `1<=t<=q`, `0<=j<=q-t`.

At `t=q` this kills `r+qL`, whereas the `B` column keeps `r+Lq` nonzero.
The equality `qL=Lq` is the contradiction. This argument can be repeated for
each component and does not assume rank one.

The notation `u_i=0/!=0` in the proof is sound in this componentwise passage:
once the minimum vertex forces label `B`, exclusivity makes the middle actual
character zero and connects the future to the same component. Replacing it by
only a selected-color coefficient would be weaker and is not needed for
closure.

### E7: `TB5`, generating functions, actual `X*(H)`, and seven labels -- PASS

With only `q^2-1` core equations, `r<=q-2` would leave the full contradiction
inside the window, so `r=q-1`. For each `s in [0,q-2]`, choose the unique
`t in [1,q-1]` with `tL=s+1 mod q`, write `tL=hq+s+1`, and put
`j=L-1-h`. The inequalities `h<=L-1` and `h>=t+L-q` give
`0<=j<=q-1-t`, and

`Lq+s=(q-1)+tL+jq`.

Thus the triangle covers exactly `[Lq,(L+1)q-2]`. Its last neighboring
coordinate `N_*=(L+1)q-1` is nonzero on the persistence column. Applying this
to every component would place the same vertex `N_*` in every component;
components are disjoint vertex sets, so exactly one nonzero component remains.

After `F_(N_*)=1`, the central block is `(0,...,0,1)`. Backward and forward
recurrence calculations give, with `p=q-L`,

`G(z)=(1+Tz^L)/(1+Tz^L+z^q)`

and

`H(z)=z^(q-1)/(1+Tz^p+z^q)`.

In the backward range down to coordinate zero, the coefficient formula uses
`D=t-q<=Lq-1`. In the forward range through coordinate `q^2+q-2`, it uses
`D=t-q+1<=pq-1`. Since two nonnegative representations
`alpha q+beta s=D` with `gcd(q,s)=1` would force `D>=qs`, every coefficient
in both complete ranges is zero or one monomial. At the next degree `D=pq`,
the only representations are `(alpha,beta)=(p,0)` and `(0,q)`, producing
`1+T^q`; this is the first collision.

The original `m=kq-1` bookkeeping kills every other residue. All remaining
ambient characters are zero or `d^beta w`, and `w` itself occurs at `N_*`.
Because ambient coordinate characters generate the actual lattice, one gets
`X*(H)=Z w`, not merely a cyclic subgroup inside an unused over-lattice.
Consequently `w` is primitive and the actual torus has dimension one.

For `q>=3`, putting `z_*=N_*-2L` gives the independently recomputed table:

| Equation | Colored triple | Label |
|---:|---|---|
| `L-1` | `(T^(q-1),T^(q-2),0)` | `C` |
| `q-1` | `(1,0,1)` | `B` |
| `z_*-q` | `(T^2,T,0)` | `C` |
| `z_*+L-q` | `(T,1,0)` | `C` |
| `z_*` | `(0,0,0)` | `Z` |
| `z_*+L` | `(0,1,T)` | `A` |
| `z_*+q` | `(0,T,T^2)` | `A` |

If `2L<q`, the relevant forward degree at `z_*` is below `p`; if `2L>q`,
the backward degree `2L-q` is below `L`. Neither has a semigroup
representation. Equality `2L=q` is incompatible with coprimality for `q>=3`.
The lowest selected equation is `(q-2)L-1>=0`, and the distance from the
highest to `q^2-2` is `(q-2)(q-L)-1>=0`. The only possible small-parameter
coincidence is between displayed `C` indices and creates no label conflict.

The first `C/B` shared scalar gives `bc^(d-1)=-1`. The later `C/A` shared
scalar gives `a=-1`. Adjacent `C/C/A` rules give
`eta_(z_*)=eta_(z_*+L)=eta_(z_*+q)=c`. The `Z` recurrence then reads

`c=c+bc^d+ac=-c`,

contradicting characteristic zero and `c!=0`. Thus the only penultimate
character shadow has no scalar lift for `q>=3`. No shorter-window survivor is
proved, so no exact, optimal, shortest, or minimal scalar clock follows.

### E8: `q=2`, the actual `Phi`, and full general-`g` fill -- PASS

For `q=2`, coprimality forces `L=1`; the three equations have character word
`(dw,w,0,w,dw)` and labels `CBA`. The shared coordinates make
`a=-1` and `bc^(d-1)=-1` necessary. Under those conditions,

`(b s^d,s,c,-s,b(-s)^d)`

satisfies all three identities for every nonzero `s`. Its exponent vector
contains `1`, so the one-torus is primitive and saturated.

For `g>1`, each inactive residue has four equations and six scalar
coordinates. The required scalar recurrence is exactly the orbit recurrence
of

`Phi(x,y)=(y,c+b y^d-x)`,

whose inverse is `(c+b u^d-v,u)`. Every coordinate in the finitely many
required iterates is a nonzero polynomial because it is a coordinate of a
polynomial automorphism. Over the infinite field, the finite union of their
proper zero hypersurfaces cannot cover `A^2`; generic initial pairs therefore
give nonzero six-coordinate segments. Combining those zero-character
segments with the active residue constructs a translate in the whole original
`V_(kq-1)`, not only a five-coordinate core. At `m=kq`, `TB4` still closes
every residue. The planar `g=1,k=2` endpoint remains Paper 16's result.

## EXT-L and `CB1` replay

Laurent's 1984 theorem is used only in its qualitative torus form: an
intersection with the division group of a finitely generated subgroup is a
finite union of intersections with contained torus translates. If there is no
positive-dimensional translate, all such translates are points and the
intersection is finite.

For a finite-rank group with arbitrary torsion, choose representatives of a
`Q`-basis after tensoring. Clearing denominators leaves an individual torsion
element; killing its finite order puts a positive power in the finitely
generated subgroup. Thus the whole group lies elementwise in its division
hull. The field generated by the finitely many coefficients and generators is
finitely generated over `Q` and embeds in `C`; every remaining group element
is algebraic over it. Extending this embedding to an algebraic closure proves
the arbitrary-characteristic-zero-field transfer without embedding the whole
ground field.

Accordingly, `T_(kq)` is finite for all `q>=2`; `T_(kq-1)` is finite for
`q>=3` and for nonresonant `q=2`; and on the resonant `q=2` locus a compatible
finite extension and finitely generated group meet the saturated translate
infinitely while the next window is finite. None of these consequences is
effective.

## E9: primary sources, collision matrix, and portfolio provenance -- PASS

The source check was refreshed through 2026-08-19 using publisher records,
original journal/preprint pages, exact-formula searches, and title/abstract
queries across algebraic-torus cosets, sparse polynomials, shift-like maps,
Fano/Hilbert parameter spaces, `S`-units, recurrences, and dynamical
Mordell--Lang. Search-result snippets were used only to locate primary pages.

| Claim neighborhood | Primary sources checked | Collision judgment |
|---|---|---|
| Qualitative arithmetic transfer | Laurent, *Invent. Math.* 78 (1984), DOI `10.1007/BF01388597` | External input, not a recurrence theorem; partial framework only. |
| Translated subtori and unlikely intersections | Suciu--Yang--Zhao, arXiv:1109.1023; Habegger, DOI `10.1007/s00208-008-0242-3`; Corvaja--Levin--Zannier, DOI `10.1090/tran/8470`; Dill--Gallinaro, arXiv:2506.07550 | Intersections with given cosets/subgroups, not exact entire-coset containment in these recurrence windows. No direct collision. |
| Sparse polynomials and torsion cosets | Amoroso--Sombra--Zannier, arXiv:1412.8059; Martínez, arXiv:1509.05898; Leroux, arXiv:0911.2594 | General sparse-factor, torsion-coset, and algorithmic theory only. No direct collision. |
| Fano-scheme terminology | Ilten--Zotine, arXiv:1605.05745; Ilten--Kelly, arXiv:1910.05593 | Parameterize projective linear spaces, so they support the package's terminology restriction rather than `E_m` as a Fano scheme. |
| Shift-like dynamics | Bedford--Pambuccian, DOI `10.1090/S1088-4173-98-00027-7`; Bera, arXiv:1805.03142; Bera--Verma, arXiv:1309.3392; Kaur, arXiv:2604.27832 | Map-class provenance, Fatou/Julia/entire-map dynamics, not finite-rank survivor cosets. No collision. |
| Orbit and `S`-unit dynamics | Bell--Chen--Hossain, arXiv:2005.04281; Bell--Ghioca, arXiv:2210.03152; Ji--Xie--Zhang, arXiv:2511.13443; Mello--Yasufuku, arXiv:2604.03745 | Fixed-orbit hitting, density, integrality, or dependence; different quantifiers from all-initial-state finite windows. No collision. |
| Fresh 2026 recurrence boundary | Zhang, “Rank-two recurrence results for polynomials and questions of dynamical Mordell--Lang type,” arXiv:2605.27058 | Semilinearity of pairs of iteration exponents for one-variable maps; neither shift-like survivor varieties nor contained torus translates. No collision. |

No checked primary source states `H_m` equality rigidity, the explicit
normalized scheme `E_m`, its activity formula, the arbitrary-rank colored
`q^2` theorem, the unique central Laurent shadow, or the seven-label
`q>=3` scalar obstruction. The added Zhang source is a useful fresh boundary
check but does not require a theorem or attribution change. The package already
requires another refresh at any future source-lock date.

The predecessor identities were also recomputed from the live local files:

| Predecessor | Terminal-review SHA-256 | PDF SHA-256 | Binding conclusion |
|---|---|---|---|
| Paper 16 | `e355172b4533011d549453d02ee9939fb2dabc16fef035206ad4911fdf18eb76` | `b4ffdaf30e2d0684b875863393e6937c26f51ce89c6f47567a24ed9a123e5e4f` | Owns planar `CBA`, exact `T_4/T_3`, and the stronger effective bound. |
| Paper 17 | `941e8b47e4436fdd9bff6f48ebf6e8c1174d07f545a220ead9ad02d73b23ed9d` | `080282e18b085cc87bb590db239c4c8f8f80fd86147ded1aa775e67504b17f2e` | Owns `dim H<=k-m`, the special equality family, terminal `T_k` finiteness, and special-coefficient sharpness. |
| Paper 18 | `251d78d2989c0c76b6f1a3090c9aeccf9c66a7171829ca6b795c9ca97d359713` | `e9044c2a9e6452b58b9e345a17c33a211feed909414798fa4696e169b24be06b` | Marked trace/ramification work has no theorem-level collision. |

The net Paper 19 contribution begins after these deductions: Part A adds
equality-kernel rigidity, complete normalized scalar classification,
fixed-fiber/universal geometry, and coefficientwise compatible-group
sharpness; Part B adds the all-`g`, arbitrary-rank character theorem and the
universal `q>=3` scalar obstruction. The planar `CBA` core receives no novelty
credit.

## `STOP-S1`, `AC01--AC18`, page mass, and zero-science audit

`STOP-S1` is preserved as negative provenance: the false implication from a
unique character shadow to a universal scalar lift is stated, the first
counterexample is retained, and the corrected universal no-lift theorem is
separated from exact character extinction. The literal marker occurs in every
author document assigned a theorem, proposal, review, tracker, or no-run
negative-history role; its sole absence is the citation ledger, which makes no
scalar-sharpness claim. No active theorem revives the false exact clock.

All eighteen locked exclusions pass:

1. `AC01`: `T_m` receives no geometric dimension.
2. `AC02`: no lower-dimensional or inclusion-maximal coset classification is
   asserted.
3. `AC03`: “maximum-dimensional” means exactly dimension `k-m` in Part A.
4. `AC04`: `E_m` is not promoted to a Hilbert, Fano, or fine moduli scheme.
5. `AC05`: component counts are geometric over the algebraic closure.
6. `AC06`: the smooth `delta^alpha` count retains squarefreeness.
7. `AC07`: the universal family fixes actual support and unit coefficients.
8. `AC08`: no reducedness, irreducibility, or total singular-locus claim is
   made for the discriminant boundary.
9. `AC09`: sharpness retains compatible-extension and compatible-group
   quantifiers.
10. `AC10`: Laurent supplies no effective cardinality.
11. `AC11`: `kq-1` for `q>=3` is not called an exact, optimal, shortest, or
    minimal scalar threshold.
12. `AC12`: planar `q=2` `CBA` is assigned to Paper 16.
13. `AC13`: Paper 17's dimension and terminal arithmetic theorems remain
    predecessor results.
14. `AC14`: character, root-scheme, discriminant, and lci machinery is not
    marketed as new.
15. `AC15`: positive characteristic, zero coefficients, and `d=1` remain out
    of scope.
16. `AC16`: no rational/Laurent polynomial support or arbitrary polynomial
    automorphism extension is asserted.
17. `AC17`: bounded collision control is not absolute priority.
18. `AC18`: no effective enumeration, height theorem, periodic classification,
    or external lifecycle effect is claimed.

The proposed section budget sums exactly to 29 substantive pages and has a
credible compression floor of 26. Part A contributes approximately 14 pages
of proof geometry and Part B approximately 13 pages of character/scalar proof,
joined by the same character-versus-scalar-lift question. No appendix,
oversized background, figure, code, data, or formatting padding is required.

The exact author inventory contains Markdown only. It contains no code, data,
result, figure, asset, TeX, bibliography, build, lock, PDF, or generated cache.
The proof uses general symbolic derivations; exploratory small cases are
explicitly excluded from evidence. This independent review used only read-only
text, hash, arithmetic-identity, predecessor, and primary-source checks. No
scientific, numerical, symbolic-enumeration, or external-service experiment
was run and no empirical claim is present.

## Independent scores and final disposition

| Axis | Fresh score | Required gate | Result |
|---|---:|---:|---|
| Portfolio-adjusted novelty | 8.2/10 | 7.5 | PASS |
| Standalone article value | 8.4/10 | 7.5 | PASS |
| Proof/source readiness | 9.2/10 | 9.0 | PASS |
| Article unity and 26--29-page feasibility | 8.8/10 | substantive and unpadded | PASS |

Part A alone would remain too close to Paper 17, and `q=2` alone would collide
with Paper 16. The corrected combined article clears the gates because the
arbitrary-rank `q^2/q^2-1` theorem and universal `q>=3` scalar obstruction add
substantial independent mass, while Part A supplies the complementary complete
lift space. The proof is closed under the displayed hypotheses, the ownership
deductions are explicit, and the source boundaries are conservative.

SOURCE_DESIGN_PASS
