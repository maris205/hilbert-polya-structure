# HCS-C60 narrative report

Status: **`PREFREEZE_CODE_RESULTS_PASS`; `POSTREFRESH_PASS`;
`FORMAL_DOCS_PASS`; `PAPER_PENDING`; `NOT_RELEASED`.**

Scope literal: `NO_BAD_EULER_OR_ROOT_NUMBER`.

The official machine handoff binds `code13 / results8 / live21 / scoped20`,
two exact $53/53$ test cycles, eight executed gates, $9{,}310$ payload scalar
leaves, $9{,}339/9{,}339/14$ value/type/structural mutations, actual
group/resolver/evidence/artifact/total hostile rebounds $6/4/10/2/12$, and
$39$ child snapshot rebind checks. The canonical payload SHA-256 is
`dca8dbbf269735e78b0435799b0d9c8c9ffad8bdd0470b9262ef64005ff0dead`;
the certificate, schema, check-report, manifest, group-evidence,
resolver-evidence, and official-refresh-log SHA-256 values are respectively
`d325de1bb0388ccc0c2e81d41fbc6c8fffd692ff777f23647d9e88367d6c2518`,
`c7ddb4ff8fa890f9f801d615158c9038299487affa3808f25fe5d73c987791a5`,
`25bc9c1c656da742359814054b66c05e18a304ca85741776c055152a30a98e44`,
`f8d44a1929b6f873d4f1b4e7317222c0f06e927ba1977f00f493b8fb004cfec7`,
`dcdb9a8be954d4ea5376220d55fcbae9bbb08eb49d03d98d57d790c319ad5fb2`,
`f115125725c9160ee3d02f1996147098c234226bdc81eaa670460802a8d827da`,
and `5f5d788a1493c16a8eec86ec0cb40bfed2dea72fa2257bddf50eed1be2c43239`.
These machine facts alone are not a formal-document, paper, or release verdict;
the separate independent formal audit has now supplied `FORMAL_DOCS_PASS`.

## 1. What C59 left behind

C59 produced two concrete degree-$320$ fields inside one released
$W(E_6)$-extension. They are nonisomorphic but have equal Dedekind zeta
functions, exact common global arithmetic, and different $3$-adic algebra
structures in either retained decomposition-group branch.

The successor question is not to find another Gassmann pair. It is to study
the additional structure already forced around the released pair.

## 2. The common degree-$160$ core

The two subgroup normalizers have order $324$. After the exact transport, the
two order-$162$ subgroups sit inside the same self-normalizing $N$ with index
two. A third index-two subgroup $H_0$ appears, and all three meet in the
derived subgroup $J$ of order $81$.

Reversing the subgroup lattice produces a degree-$160$ field $M$, three
degree-$320$ quadratic extensions of $M$, and a degree-$640$ field $L$ with
$L/M$ biquadratic. This is new tower structure, not a relabelling of C59.

## 3. Why explicit generators matter

An abstract $V_4$ lattice would be too thin for C60. The target requires
integral invariants in the same labelled line coordinates used by C59:

- a quadratic trace-like carrier for $M$;
- a cubic carrier for the third companion $F_0$; and
- a two-color quadratic carrier for $L$.

At the frozen split prime, the carriers have 160, 320, and 640 distinct
values. The official producer/checker tuple reproduced those facts
independently. The written primitive-field bridge has now passed the formal
documents audit and supports the formal theorem claim.

## 4. The quadratic obstruction and cubic escape

The third subgroup $H_0$ is invisible to formal invariants of degree at most
two: it and $N$ have the same point and unordered-pair partitions. This forces
their fixed spaces to agree in degrees zero, one, and two. One exact orbit of
$27$ squarefree cubic monomials breaks the symmetry and has stabilizer
$H_0$.

This is an invariant-theory statement on formal commuting coordinates. It is
not a universal claim after all algebraic relations among the actual roots
are imposed.

## 5. The $V_4$ zeta balance

The elementary permutation-character identity for $V_4$ becomes

$$
[G/J]+2[G/N]=[G/H_+]+[G/H_0]+[G/H_3].
$$

Artin formalism then balances the four Dedekind zeta functions. Since the two
transported C59 twins retain equal zeta functions, the relation simplifies to
a new identity involving $M,F_0,L$ and one twin. The generic formalism is
classical; the proposed contribution is this explicit instance inside the
released C59 extension and its full arithmetic realization.

## 6. Relative arithmetic concentrated at three

The absolute discriminants inherit C59's eight-prime support. After removing
the appropriate powers of the degree-$160$ base discriminant, every relative
factor outside $3$ cancels. The target relative norms are

$$
3^8,\quad 3^{16},\quad 3^8,\quad 3^{32}.
$$

Both retained local branches explain these values by complete relative
tables. Every relative ramified row has $e=2,d=1$, so the quadratic
ramification is tame over the residue-character-$3$ base completions.

## 7. Why this is one theorem-sized step

The common normalizer alone is a note. The generic $V_4$ relation alone is
prior art. A single primitive carrier or a single local branch is a fragment.
The C60 target is their inseparable conjunction:

1. exhaustive unique envelope;
2. explicit primitive fields;
3. formal invariant-degree gap;
4. fixed-field and zeta relations;
5. exact absolute and relative arithmetic; and
6. both complete local branches.

Failure of any component kills the integrated target.

## 8. Current state

The chronology is unchanged: adaptive target selection and its pilots came
first, hostile non-salami review locked the target, and the integrated
`TARGET_LOCK_FORMAL_INPUT` layer then became historical input to the machine
assembly. Those pilots and target-lock files were never theorem authority.
The source-stable project-local tuple now has
`PREFREEZE_CODE_RESULTS_PASS`, and the authorized refresh plus mandatory
nonmutating replay has `POSTREFRESH_PASS`. The narrative above and the complete
13-root package have passed the independent formal-documents hostile audit.
No paper or C60 release is claimed: the current states are
`FORMAL_DOCS_PASS / PAPER_PENDING / NOT_RELEASED`.
