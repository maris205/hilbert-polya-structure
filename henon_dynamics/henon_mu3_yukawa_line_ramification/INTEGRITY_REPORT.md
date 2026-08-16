# HCS-C58 prefreeze integrity report

Status: **PREFREEZE_CODE_RESULTS_PASS; POSTREFRESH_PASS;
FORMAL_DOCS_PASS; PAPER_PENDING; NOT_RELEASED.**

Audit date: 2026-08-16.

## 1. Verdict

**PASS for the machine code/results layer, its post-refresh hostile audit, and
the independent formal-document audit; paper and release are not yet passed.**

The 13 root documents and Route-A record a single coherent target:
filtered inertia at every bad prime, the associated Artin and Swan characters,
the conductors of \(V_6\) and \(V_{20}\), and the discriminants of the
degree-27 field \(E\) and its \(W(E_6)\)-closure \(K\).

The exact formulas were reproduced by G0--G7, independently checked, atomically
refreshed, cleanly replayed without mutation, and given `POSTREFRESH_PASS`.
There is still no C58 release commit, paper hash, full-project release
manifest, archive, or promotion authorization. The external formal aggregate
is frozen in Route without a self-hash cycle.

## 2. Scope and ownership audit

The Phase-1 documentation owns:

- the theorem and non-theorem boundary;
- the source locators and use restrictions;
- gates G0–G7;
- the exact local and global targets;
- the alternative kill ledger;
- truthful pending-state fields.

It does not own or modify:

- frozen C55, C56, or C57 files;
- C58 code, results, or paper artifacts;
- Codex state;
- C59–C61 candidate selection;
- a release commit, manifest, or archive.

The only permitted batch change is the C58 slot and the minimum global wording
needed to show that C58 is locked while C59–C61 remain unselected.

## 3. Claim-to-evidence matrix

| Claim family | Phase-1 basis | Required C58-local closure | Current state |
|---|---|---|---|
| Nine-prime surface divided-discriminant envelope | Dual exact determinant engines | G1 exact factorization | PREFREEZE_CODE_RESULTS_PASS |
| Eight-prime ramified support and `Disc(E)` vector | Maximal order, local rows, core-free p=2 bridge | G1–G2 | PREFREEZE_CODE_RESULTS_PASS |
| \(p=3\) filtration | Complete D/I scan, ToM 6x2/7/8 `Fraction`, Serre inversion | G3–G4 | PREFREEZE_CODE_RESULTS_PASS |
| \(p=5\) filtration | Hits 147/247/295 and Sylow normality filter | G3–G4 | PREFREEZE_CODE_RESULTS_PASS |
| Tame \(C_3\) primes | Theta-only Krasner authority, bounds 24/24 | G2–G4 | PREFREEZE_CODE_RESULTS_PASS |
| Reflection primes | Four-chart ODP, Hensel, regularity, Picard–Lefschetz, ToM 2 | G1/G4 | PREFREEZE_CODE_RESULTS_PASS |
| Local Artin/Swan tuples | Exact fixed spaces and filtration sums | G5 | PREFREEZE_CODE_RESULTS_PASS |
| Global conductors and \(\operatorname{Disc}(K)\) | Symbolic and regular-representation closure | G6 | PREFREEZE_CODE_RESULTS_PASS |
| Infinity types | Signature, `polsturm`, subgroup ToM 5/element 17, CTblLib 1.3.1 | G6 | PREFREEZE_CODE_RESULTS_PASS |

## 4. Mathematical consistency audit

Let

\[
A=181\cdot997\cdot2346241=423395612137,\qquad
B=283\cdot1801\cdot
14932047182473291995860108491583652133938007263719.
\]

The locked exponents obey

\[
(11,35)+(7,29)+3(6,12)+3(1,5)
\]

prime by prime in the intended conductor factors, and in particular

\[
\mathfrak N(V_6)\mathfrak N(V_{20})
=3^{46}5^{36}A^{18}B^6
=\operatorname{Disc}(E).
\]

The surface divided-discriminant bad-prime envelope is
`{2,3,5,181,283,997,1801,2346241,q}`, while the exact ramified support of
both \(E\) and \(K\) is the eight-prime set obtained by deleting 2. In that
nine-prime order the `Disc(E)` exponent vector is
`(0,46,36,18,6,18,6,18,6)`.

Theta is the sole degree-36 `KRASNER_CERTIFIED_AUTHORITY`. Its tame
precisions `[20,30,40]` clear bounds 24/24; its wild precisions
`[900,950,1000]` clear p=3 bounds 886/538 and p=5 bounds 746/246. Delta is
`BOUNDED_NON_RESULT_NONDEPENDENCY`; tame bounds 840/408 are not cleared at
precision 40, and delta supplies neither a premise nor a cross-check.

At \(3\), the Swan exponents \((5,18)\) plus the tame fixed-space
codimensions \((6,17)\) give Artin exponents \((11,35)\).
At \(5\), \((3,12)+(4,17)=(7,29)\).
The permutation decomposition

\[
\mathbf Q[27]\simeq \mathbf 1\oplus V_6\oplus V_{20}
\]

therefore agrees with the conductor–discriminant identity for \(E\).

At \(2\), the permutation conductor is zero.  Inertia therefore fixes every
coset of the line stabilizer.  The faithful 27-line action says precisely that
this stabilizer has trivial core, so inertia is trivial in the Galois closure
\(K\).  The theorem does not skip this non-Galois-to-Galois bridge.

For the regular representation, the class targets give

\[
\operatorname{Disc}(K)=
3^{106560}5^{80352}A^{34560}B^{25920}.
\]

G5–G6 regenerated every regular-character codimension and weighted filtration
sum, yielding a 1,931,353-digit positive integer with decimal-newline SHA-256
`951c2969...`.

## 5. Serre and \(p=3\) integrity audit

The complete p=3 orbit-pattern hits in the 350-class `U4(2).2` Table of Marks
are ToM 140/order 18, ToM 142/order 18, and ToM 206/order 36. ToM 206 has a
noncyclic putative tame quotient and is a possible decomposition overgroup
only. The exhaustive valid triples are
`(140,140,1)`, `(142,142,1)`, `(206,140,2)`, `(206,142,2)`.

For every valid pair the exact deep-profile inventory is ToM 6 with
multiplicity two, ToM 7 once, and ToM 8 once. Base vector `(2,5,8,8)`,
\(C_3^2\) vector `(1,2,4,4)`, and deep vectors
`(1/3,2/3,1,1)`, `(0,0,1,1)`, `(1/3,2/3,1,1)` give formal `Fraction`
solutions `(7,-18)`, `(1,6)`, `(7,-18)`. Hence only deep ToM 7 admits a
nonnegative filtration: \(I_1=C_3^2\),
\(I_2=\cdots=I_7=C_3\), \(I_8=1\).

The operative locator is Jean-Pierre Serre, Local Fields, Chapter IV, §2,
Proposition 9, printed pages 69–70:

\[
\theta_i(s\tau s^{-1})
=\theta_0(s)^i\theta_i(\tau).
\]

For \(i=7\), the tame involution acts as \((-1)^7=-1\) on
\(G_7/G_8\simeq C_3\).  Thus the deep \(C_3\) must be inverted.
This distinguishes ToM 140, \((C_3^2):C_2\), from ToM 142,
\(C_3\times S_3\), whose relevant \(C_3\) is central.

This determines filtered inertia ToM 140 and leaves exactly
`(D,I)=(140,140)` and `(206,140)`. Thus \(|D_3|\in\{18,36\}\) is unresolved
but independent of every stated inertia, conductor, and discriminant result.

## 6. Decomposition-group firewall

`NO_BAD_EULER_OR_ROOT_NUMBER`: C58 proves no decomposition Frobenius, bad
Euler polynomial or factor, local epsilon factor, local or global root number,
Artin holomorphy, automorphy, analytic continuation, or functional equation.
The D-order ambiguity is irrelevant to the certified conclusions, and even a
later resolution of \(D_3\) would not authorize those independent claims.

### Reflection and infinity integrity

At \(283,1801,q\), exact singular-locus elimination on all four charts gives
one reduced point in chart 0 and unit ideals elsewhere. Gradient vanishing,
unit affine Hessian, the unique Hensel critical lift modulo \(p^2\),
critical-value congruence, valuation-one smoothing, and regular total space
feed odd-characteristic Picard--Lefschetz. The resulting tame root reflection
is subgroup ToM 2, with line/double-six types
\(1^{15}2^6\)/\(1^{16}2^{10}\), Artin \((1,5)\), Swan \((0,0)\), and no
local \(e/f\) row claim.

At infinity, signature \((3,12)\) and `polsturm(theta36)=4` yield line type
\(1^3 2^{12}\) and double-six type \(1^4 2^{16}\). The subgroup match is
ToM 5; the separate `CharacterTable("U4(2).2")` element-class index is 17,
with class size 540 and centralizer 96. CTblLib 1.3.1 fixes this convention,
and the signatures are \((3,3)\) on \(V_6\) and \((11,9)\) on \(V_{20}\).

## 7. Alternative and false-positive audit

- The ordered-Steiner degree-240 field has the first natural nonzero
  \(H^1\simeq\mathbf Z/3\) after the degree-40, 80, and 120 false doors, but no
  new arithmetic consequence has yet been certified.  It is deferred.
- The quaternion lane has no executable common-field evaluation model.
  Square and nonsquare values at \(p=1373\) alone do not prove a nonconstant
  Hilbert evaluation.  It is killed for C58.
- A tame-only note is mathematically valid but below the intended contribution
  threshold.
- A 27-carrier-only proof is incomplete; the degree-36 carrier is mandatory.

No killed or deferred alternative is smuggled into the theorem.

## 8. Reproducibility and absence ledger

| Item | Current value |
|---|---|
| Project-local implementation | `PREFREEZE_CODE_RESULTS_PASS` |
| Unique refresh plus mandatory nonmutating default replay | PASS |
| Independent checker | `PASS_PREFREEZE_CODE_RESULTS`, `64454700...` |
| Machine inventory | code 14; results 8; live 22; scoped 21 |
| Machine identities | cert `456a4813...`; payload `fba2df...`; schema `ccbc20eb...`; evidence `e374d3...`/`0e0b3f...`; manifest `a1874229...` |
| Machine hostile audit | `POSTREFRESH_PASS` |
| Formal-document hostile audit / aggregate | `FORMAL_DOCS_PASS` / frozen externally in Route |
| Paper source/PDF | absent and pending |
| Paper hostile audit | pending |
| Release commit | null |
| Full manifest/archive | null |
| Promotion authorization | false |

The prefreeze tuple has eight gates, 1149 payload leaves, 1199 rejected rebound
mutations, and 45 passing tests. Exploratory observations remain nonauthorities.

## 9. Phase transition rule

The machine-to-document handoff, independent hostile audit, and external
formal aggregate are complete. Release still requires a compiled/audited
paper, commit, consistent full-project manifest, archive, and explicit
promotion authority.

C59–C61 remain contingent and unselected.
