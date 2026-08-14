# HCS-C56 methodology blueprint

Status: **DOCS_FINAL_NO_MORE_EDITS; method executed and bound into the project
RELEASE_FROZEN.**

## 1. Research mode

HCS-C56 is an exact computational-algebraic proof.  Its evidence has three
layers:

1. **external theorems:** the 27-line/simple-zero theorem, the
   \(W(E_6)\) subgroup criterion, and Hochschild–Serre;
2. **written deductions:** scheme-length comparison, modular subset-sum
   irreducibility, the Frobenius-to-\(W(E_6)\) chain, Picard invariants, and
   field-degree consequences;
3. **instance computation:** the chart equations, eliminant,
   back-substitutions, modular factors, and Weyl/Picard enumeration.

No layer substitutes for another.  In particular, a CAS cannot prove the
applicability of an external theorem, and a cited theorem cannot certify the
large instance coefficients.

## 2. Unit of analysis

The sole object is the exact projective cubic surface \(Y/\mathbf Q\) imported
from HCS-C55.  The canonical machine input is the ordered 20-row primitive
coefficient array, not a rendered equation and not a temporary eliminant.

The upstream status contract is stratified:

- Route: RELEASE_FROZEN;
- documentation: DOCS_FINAL_NO_MORE_EDITS;
- machine artifacts: intentionally RELEASE_CANDIDATE.

The importer validates this combination and does not reinterpret it as a
pending C55 release.

## 3. Scheme lane

### 3.1 Global control

Define \(F_1(Y)\) as the zero scheme of
\(\sigma_F\in H^0(\operatorname{Gr}(2,4),
\operatorname{Sym}^3(\mathcal S^\vee))\).  Use Kass–Wickelgren Theorem 2
(equivalently the classical total of 27) for the total rank, and Corollary 53
only for simplicity of the zeros, to prove finite étale rank 27.

### 3.2 Main-chart construction

Generate the four restricted line equations from the imported sparse cubic.
Store complete primitive coefficient arrays for:

- \(g(d)\);
- \(\lambda_a a+h_a(d)\);
- \(\lambda_b b+h_b(d)\);
- \(\lambda_c c+h_c(d)\).

The independent checker substitutes the three back-solutions into all four
line equations and performs sparse rational remainder arithmetic.  It does
not trust the producer's Gröbner transformation matrix.

### 3.3 Global equality

The direct map produces a closed immersion only into the main-chart open.
Because the global line scheme is finite étale, that open is open-and-closed.
The rank-27 chart subscheme is therefore globally closed; equal finite ranks
force an isomorphism.  Five complementary-chart unit ideals serve as an
independent convention audit.

## 4. Arithmetic lane

### 4.1 Irreducibility

At each selected good prime:

- leading coefficient survives;
- complete monic factors and multiplicities are stored;
- factors multiply back;
- \(\gcd(\bar g,\bar g')=1\);
- factor-degree subset sums are recomputed.

The only accepted conclusion is from the exact intersection
\(\{0,27\}\).  A rational CAS factorization may corroborate but is not the
paper proof.

### 4.2 Galois maximality

The chain is:

$$
\text{irreducible }g
\Longrightarrow G\text{ transitive}
\Longrightarrow
\begin{cases}
G=U,\\
G=W(E_6),
\end{cases}
\tag{M.1}
$$

after an order-five witness.  The exact enumeration shows that every element
of target Frobenius type \((2,5,5,5,10)\) lies outside \(U\).

The producer and checker construct \(W(E_6)\) from the Picard lattice rather
than importing a black-box named permutation group.  They enumerate 51840
elements and find all 5184 target-type elements outside \(U\), with zero
inside.  Every element of \(W(E_6)\) induces an even permutation of the 27
lines, so ordinary \(S_{27}\) sign is forbidden as the parity test.

## 5. Picard lane

Use the blow-up basis \(H,E_1,\ldots,E_6\), the intersection form, canonical
class, simple roots, and all 27 line classes.  Verify:

- the reflection group order;
- preservation of the line set and incidence;
- fixed-space rank one.

Then apply Hochschild–Serre only after tensoring with \(\mathbf Q\).
The obstruction to integral descent lands in the torsion Brauer group, so the
conclusion is rank equality.

## 6. Independence architecture

The checker must:

- share no producer modules;
- rebuild the imported cubic and all line equations;
- use an independent exact arithmetic implementation/backend where feasible;
- derive every theorem boolean rather than copying it;
- reject unknown/missing fields, duplicate keys, floats, booleans in integer
  slots, noncanonical integers, optimized Python, and oversized input;
- compare the entire canonical payload.

Expensive immutable contexts may be cached within a checker run, but the
semantic result for every leaf must still be independently determined.

## 7. Adversarial validation

The all-leaf rebound suite mutates each scalar leaf, recomputes exposed
envelope hashes, and requires semantic rejection.  Targeted mutations include:

- every C55 coefficient and exponent;
- chart labels and \(p_{01}\) equations;
- every coefficient of \(g,h_a,h_b,h_c\);
- primes, factor coefficients, multiplicities, and subset sums;
- roots, line classes, generators, parity, counts, orders, and fixed rank;
- every status and theorem boolean.

A hash mismatch alone is not semantic protection.

## 8. Source method

Primary full texts are preferred.  Each cited theorem is recorded with an
exact named locator and a statement-to-claim mapping.  The recent-neighbor
search is query/date bounded and is never converted into an exhaustive
novelty claim.

## 9. Validity threats

| Threat | Control |
|---|---|
| stale C55 normalization | committed-object import plus canonical 20-row digest |
| chart convention drift | regenerate equations and five complement checks |
| false irreducibility from partial primes | full factors, squarefreeness, subset-sum proof |
| \(U\) mistaken for full \(W(E_6)\) | explicit target-class Coxeter parity |
| \(S_{27}\) sign confusion | schema/firewall rejects ordinary sign as oddness |
| Picard integral overclaim | rank-only Hochschild–Serre wording |
| \(E=K\) conflation | separate schema fields, degrees, and closure relation |
| prose outruns computation | exact claims require certified semantic gates; release wording remains separate from prefreeze evidence |

## 10. Reproducibility and release

The cwd-independent rollback-atomic runner, independent checker,
deterministic schema, and scoped code/results manifest pass at prefreeze:
10/10 semantic gates, 2684/2684 rebound cases, and 15/15 tests.  Their exact
identifiers are recorded in `README.md` and `INTEGRITY_REPORT.md`.  The
official paper compilation passes and the project is `RELEASE_FROZEN` at
implementation commit `b32402f1dd276a2684d3e849dae26150ebb595e1`.
The scoped manifest remains the default code/results identity; a separate
46-entry self-excluding full-project manifest is verified externally for the
release-wide tree.  The provenance commit remains null/external, and no
temporary report is promoted.
