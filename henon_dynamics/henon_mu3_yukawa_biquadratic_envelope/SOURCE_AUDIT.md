# HCS-C60 primary-source and novelty audit

Status: **BOUNDED SOURCE AUDIT; `PREFREEZE_CODE_RESULTS_PASS`;
`POSTREFRESH_PASS`; `FORMAL_DOCS_PASS`; `PAPER_PENDING`;
`NOT_RELEASED`.**

Search boundary: **2026-08-16 UTC, bounded instance/topic search.** Negative
search evidence does not prove absolute priority.

## 1. Claim/source matrix

| source | authorized use | not supplied |
|---|---|---|
| Austen A. James, *A Bayesian Approach to Computing Brauer Groups of Cubic Surfaces* (Rice PhD thesis, 2022), §3.1, printed p. 22, [repository record](https://hdl.handle.net/1911/114191) | $350$ subgroup classes, $339$ profiles, exactly eleven $W(E_6)$ Gassmann collisions | no C60 common-normalizer envelope, fields, invariants, or relative arithmetic |
| Robert Perlis, “On the equation $\zeta_K(s)=\zeta_{K'}(s)$,” *JNT* 9 (1977), 342--360, Theorem 1, printed p. 351, DOI 10.1016/0022-314X(77)90070-1 | classical Gassmann/arithmetic-equivalence and character/zeta bridge | no released cubic-surface instance or C60 tower |
| Wieb Bosma and Bart de Smit, “On arithmetically equivalent number fields of small degree,” ANTS V (2002), 67--79, introduction, printed p. 68, DOI 10.1007/3-540-45455-1_6 | arithmetic-equivalence invariants and permutation-character computational context | no C60 instance |
| classical Burnside/rational representation theory of $V_4$ | the generic three-quadratic-subfield permutation relation | no novelty for the explicit C60 envelope |
| Richard P. Stauduhar, “The Determination of Galois Groups,” *Mathematics of Computation* 27 (1973), 981--996, opening resolvent setup, pp. 981--984, DOI 10.1090/S0025-5718-1973-0327712-4 | classical construction of resolvents from ordered roots and subgroup invariants | no C60 carrier or certificate |
| Claus Fieker and Jürgen Klüners, “Computation of Galois Groups of Rational Polynomials,” *LMS Journal of Computation and Mathematics* 17 (2014), 141--158, §1, §2, and Remark 2.1 | relative invariants, stabilizers, and resolvent computation | no C60 carrier or certificate |
| [Prasad, integral refinements of arithmetic equivalence](https://arxiv.org/abs/1409.3173) | integral-equivalence context | no C60 theorem |
| [Klüners--Nicolae, Artin $L$-function determination](https://arxiv.org/abs/1509.06883) | limits and refinements of $L$-function data | no C60 theorem |
| [Li--Rudnick, pair arithmetical equivalence](https://arxiv.org/abs/2007.13147) | pair-equivalence context | no C60 instance |
| [Phagan, corresponding abelian extensions](https://arxiv.org/abs/2408.09666) | recent integral/correspondence context | no C60 instance |
| GAP 4.11.1, TomLib 1.2.9, CTblLib 1.3.1, SmallGrp 1.4.1 documentation/data | exact finite computation and frozen locators | no literature novelty and no durable field definition by locator alone |

## 2. Prior art that C60 must not rebrand

The following are not new:

- the eleven $W(E_6)$ Gassmann collision buckets;
- the $301/303$ Gassmann character equality itself;
- Gassmann/Perlis arithmetic equivalence and Artin formalism;
- the generic $V_4$ Brauer/permutation-character relation;
- normalizer/core formulas for fixed fields and automorphisms;
- conductor-discriminant and relative discriminant-tower formulas;
- relative invariants, orbit sums, and resolvent methods; and
- the general possibility of strengthening arithmetic equivalence by
  integral or local data.

## 3. Bounded new contribution

The only authorized novelty statement is:

> In the one released cubic-surface $W(E_6)$ extension, the C59 twins determine
> the unique collision-table case with a common transported normalizer of
> index two over both members; this envelope admits explicit primitive
> degree-$160/320/640$ line-coordinate fields, a formal quadratic/cubic
> invariant gap for the third companion, and complete exact relative
> arithmetic in both retained decomposition branches.

The bounded search found no source containing this exact conjunction. The
eventual paper may say only that no such conjunction was found in the bounded
search. It may not claim “first.”

## 4. Candidate funnel and salami boundary

| candidate | target decision | reason |
|---|---|---|
| common degree-$160$ core, $V_4$ envelope, invariant gap, relative arithmetic | GO | integrated new tower with explicit generators and both branches |
| arithmetic atlas of all eleven collisions | DEFER/KILL | James owns collision count; high degrees make it atlas-like |
| integral/local integral permutation inequivalence of C59 pair | KILL standalone | crowded refinement area and too close to a C59 corollary without a new theorem |
| resolve $D_3$ and compute bad Artin Euler data | KILL | branch-only salami risk, not execution-ready, violates firewall |
| class numbers, regulators, maximal orders, trace forms | KILL now | no feasible exact expanded arithmetic infrastructure |

Candidate 1 remains one paper only if all group, primitive, invariant,
character, global/relative, and both-local-branch components survive.

## 5. Exact uniqueness wording

The authorized finite-table statement is:

> Among the eleven frozen C59 collision buckets, $301/303$ is the only pair
> whose normalizers are conjugate in $G$ and have index two over both
> subgroups.

Do not shorten this to “unique $V_4$ envelope.” The $112/120$ bucket has a
different transported generated/intersection configuration and is not
excluded by the narrower claim.

## 6. Explicit-field and invariant boundary

Durable one-based arrays and exact formal carriers define the C60 fields;
ToM values are versioned checks. Product-form orbit polynomials are exact,
but no expanded characteristic-zero coefficients are claimed.

The degree obstruction applies to commutative $\mathbf Q$-coefficient formal
polynomials in the labelled coordinates. It does not classify all evaluated
expressions after imposing algebraic relations.

## 7. Arithmetic and local wording boundary

The absolute and relative discriminants follow from exact permutation
conductors and tower formulas. The local rows summarize exhaustive double
cosets and filtrations. They do not classify an individual high-degree local
field up to isomorphism and do not resolve the decomposition branch.

The zeta identity uses character formalism. It supplies no new bad Euler
factor, decomposition Frobenius, epsilon factor, root number, holomorphy, or
automorphy result.

## 8. Negative source gates

Reject:

- “first $W(E_6)$ Gassmann collision”;
- “new $V_4$ Brauer relation”;
- “new relative resolvent method”;
- “unique $V_4$ configuration” without the exact index-two predicate;
- “ToM locators define the fields”;
- any theorem statement based only on target-selection pilots;
- any integral-equivalence, maximal-order, class-number, or regulator claim;
- any selected local branch or converse $(n,e,f,d)$ classification; and
- any forbidden analytic, geometric, RH, or Hilbert--Polya inference.

## 9. Scope and current status

`NO_BAD_EULER_OR_ROOT_NUMBER` remains absolute.

The bounded search continues to support target lock and the non-salami
decision only; it is not theorem authority and its negative search does not
prove absolute priority. The integrated target-lock formal package and Pilot
A/B evidence retain their exact historical role as machine inputs, never as
substitutes for the official tuple.

That official tuple now binds `code13 / results8 / live21 / scoped20`, two
exact $53/53$ test cycles, eight executed gates, $9{,}310$ payload scalar
leaves, $9{,}339/9{,}339/14$ value/type/structural mutations, actual hostile
rebound counts $6/4/10/2/12$, and $39$ child snapshot rebind checks. It binds
payload
`dca8dbbf269735e78b0435799b0d9c8c9ffad8bdd0470b9262ef64005ff0dead`,
certificate
`d325de1bb0388ccc0c2e81d41fbc6c8fffd692ff777f23647d9e88367d6c2518`,
schema `c7ddb4ff8fa890f9f801d615158c9038299487affa3808f25fe5d73c987791a5`,
check report
`25bc9c1c656da742359814054b66c05e18a304ca85741776c055152a30a98e44`,
manifest
`f8d44a1929b6f873d4f1b4e7317222c0f06e927ba1977f00f493b8fb004cfec7`,
group evidence
`dcdb9a8be954d4ea5376220d55fcbae9bbb08eb49d03d98d57d790c319ad5fb2`,
resolver evidence
`f115125725c9160ee3d02f1996147098c234226bdc81eaa670460802a8d827da`,
and official refresh log
`5f5d788a1493c16a8eec86ec0cb40bfed2dea72fa2257bddf50eed1be2c43239`.

The machine layer is therefore
`PREFREEZE_CODE_RESULTS_PASS / POSTREFRESH_PASS`. Source wording and proof
bridges have passed the independent formal-documents audit; paper and release
remain `PAPER_PENDING / NOT_RELEASED`.
