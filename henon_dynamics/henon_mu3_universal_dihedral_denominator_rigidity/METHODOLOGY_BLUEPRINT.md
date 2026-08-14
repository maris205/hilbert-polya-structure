# HCS-C54 methodology blueprint

## 1. Problem anchor

HCS-C53 changes the rational split exponent of the moment packet from
\(2/n\) over the two \(K\)-places to \(4/n\) on one rational local
factor.  HCS-C54 asks a classification question rather than constructing
another descent:

> Which rows admit an actual rational compatible system realizing the
> complete prescribed split-local factor, and can source symmetry or an
> invisible rational counterpacket enlarge that list?

The answer must preserve the frozen source equations, the two pure weights,
and the good split-prime organization.

Throughout this project, **ordinary** means realizable by an actual
finite-rank compatible system with integral multiplicities.  It does not
refer to \(p\)-adic or Newton-polygon ordinarity.

## 2. Dominant contribution

The dominant contribution is a universal classification:

\[
\boxed{
\operatorname{PMonStab}(C_n,Q_{n,\rho})
=\operatorname{Dih}(C_{3n}),\qquad
\text{ordinary split realization}\iff n\mid4.}
\]

The group identity is unconditional equation algebra for every \(n\ge2\).
The ordinary-realization theorem applies to packet-admissible smooth rows;
the inherited certified rows are \(2,3,4\).

## 3. Supporting contribution

At \(n=3\), the entire common-geometric-group character on both pure rails
is computed.  No nonzero central source-isotypic sector has multiplicity
divisible by three on both rails.  A restriction theorem then shows that a
split-invisible rational virtual counterpacket cannot modify these
\(K\)-side multiplicities.

These results close two plausible escape hatches without changing the Euler
object.

## 4. Evidence hierarchy

| Level | Evidence | Role |
|---|---|---|
| E1 | ideal grading, phase recurrence, parity closure, presentation | proves the all-\(n\) source group |
| E2 | explicit semilinear transport and congruence solutions | proves the rational group form and two rational points |
| E3 | Chebotarev, Brauer--Nesbitt, purity, rank arithmetic | proves the if-and-only-if denominator theorem |
| E4 | exact Cayley quotient and dihedral character inner products | proves the \(n=3\) central-sector no-go |
| E5 | independent exact controls and adversarial mutations | protects the implementation; does not replace E1--E4 |

Finite scans are mutation guards.  They are never presented as proofs of an
all-\(n\) statement.

## 5. Scope partitions

### 5.1 Unconditional all-\(n\) partition

- ideal-to-equation-line lemma;
- full projective monomial stabilizer;
- explicit dihedral presentation and support exact sequence;
- semilinear transport and finite etale rational group form.

### 5.2 Packet-admissible partition

- pure compatible systems with ranks \(e_n,o_n\);
- split-trace and complete split-factor realization;
- Reynolds correspondences on smooth rows.

HCS-C53 certifies this partition only for \(n=2,3,4\).

### 5.3 Third-row common-group partition

- exact characters are computed over \(K\);
- a common rational \(\mathscr G_3\)-form requires twisting the Fermat
  descent datum;
- the no-go is already visible after restriction and is independent of the
  inert rational extension.

## 6. Anti-claims that every artifact must preserve

Every theorem, certificate, paper section, and Route-A record must reject:

- “full automorphism group” without the qualifier projective monomial;
- all-\(n\) smoothness, motives, or packets;
- a Reynolds average over rotations alone;
- a constant rational group of order \(6n\);
- a total-rank-only proof that accepts \(n=3\);
- a common rational group scheme without the Fermat twist caveat;
- injectivity of restriction on virtual classes;
- a global or inert root, automorphy, continuation, FE, or RH.

## 7. Exact-computation policy

- Arithmetic is exact in \(\mathbf Q(\rho)\) or cyclotomic character rings.
- The universal recurrence is proved symbolically; scans through bounded
  ranges are controls.
- The \(n=3\) quotient matrices are constructed from an explicit monomial
  basis and seven exact relations.
- Producer and checker paths must be independent enough to avoid shared-bug
  certification.
- JSON loaders reject duplicate keys and unknown top-level keys.
- The tested local promotion protocol is rollback-atomic and exception-safe
  under injected failures after each write stage.  This is not a power-loss
  or storage-durability atomicity claim.
- Release hashes are recorded only after deterministic replay.

## 8. Primary-source policy

Use primary sources only for theorem-level background:

- Brünjes for Fermat monomial symmetry and one-dimensional sectors;
- Deligne §1.2, especially (1.2.2) and (1.2.5)(i), for purity;
- Serre for Chebotarev density;
- the standard characteristic-zero Brauer--Nesbitt trace-rigidity
  consequence after fixed-\(\ell\) semisimplification; no inherited
  semisimplicity theorem and no unverified theorem-number locator;
- Nagel Proposition 2.16 as the primary locator for the general
  Cayley/Jacobian complete-intersection identification;
- Favero--Iliev--Katzarkov §5.4 only as \((2,3)\) fivefold context.

The simultaneous stabilizer, denominator classification, and exact source
character are supported by the paper's own proofs and exact artifacts.  The
novelty statement is explicitly search-bounded.

## 9. Decision gates

1. **G1: category gate.** The ideal stabilizer proof must not widen to full
   PGL automorphisms.
2. **G2: universal group gate.** Recurrence, closure parity, exhaustive count,
   generator order, and presentation must agree.
3. **G3: rational-form gate.** Transport and fixed-point congruences must give
   a nonconstant rank-\(6n\) group scheme with two rational points.
4. **G4: denominator gate.** Separate weights before taking ranks; the total
   \(n=3\) rank is a mandatory negative control.
5. **G5: equivariant gate.** Include the Cayley residue determinant ratio and
   coefficient-orbit packaging.
6. **G6: counterpacket gate.** Permit a nontrivial virtual restriction kernel,
   but require every kernel class to restrict to zero and have rank zero.
7. **G7: analytic firewall.** Keep every theorem split-local and exclude inert
   and global promotion.

## 10. Success criterion

The project is ready for release only when the symbolic proof package, exact
certificate, independent checker, mutation suite, manuscript, bibliography,
and scope scan all agree on the same category and quantifiers.  A clean code
replay without that agreement is insufficient.
