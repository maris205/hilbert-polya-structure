# HCS-C59 theorem package

Status: **PREFREEZE_CODE_RESULTS_PASS; POSTREFRESH_PASS;
FORMAL_DOCS_PASS; PAPER_PENDING; NOT_RELEASED.**

This file states the integrated theorem and the exact premises certified by
the promoted C59 machine tuple. C59-EXACT-0--7 have project-local
`PREFREEZE_CODE_RESULTS_PASS`, and the promoted bytes have an independent
`POSTREFRESH_PASS`; these edited theorem roots also have an independent
`FORMAL_DOCS_PASS`.

## 1. Released object and exact subgroups

Let $Y/\mathbf Q$ be the released smooth cubic surface, let $E$ be its
degree-(27) line field, and let (K) be the released normal closure:

\[
G=\operatorname{Gal}(K/\mathbf Q)=W(E_6),\qquad |G|=51840.
\tag{1.1}
\]

The following cycles define exact subgroups of the released labelled
27-point action. They, not their ToM positions, are the formal definitions:

```text
H_+ = Group(
 (1,16,23,10,7,15)(2,27,11,14,5,22)(3,13,20,19,9,24)
   (4,12,18,17,8,25)(6,26,21),
 (3,19,6)(4,21,17)(5,20,16)(7,24,27)(8,11,23)(12,15,22),
 (1,26,10)(2,13,25)(3,22,8)(4,20,27)(5,24,17)(6,15,23)
   (7,21,16)(9,14,18)(11,19,12)
);

H_- = Group(
 (1,5,3,6,4,2)(7,10,17,18,20,13)(8,21,16,15,9,14)
   (11,19,12)(22,26,24,27,25,23),
 (1,7,16,11,22,10)(2,15,27)(3,13,9,20,24,19)
   (4,12,8,18,25,17)(5,26,23,21,14,6),
 (1,16,22)(2,23,21)(3,9,24)(4,8,25)(5,26,15)(6,27,14)
);
```

The promoted evidence carrier serializes the same permutations as exact
27-entry image arrays and compares them with these cycle definitions. Their
certified invariants are:

| invariant | (H_+) | (H_-) |
|---|---:|---:|
| frozen-version TomLib locator | 301 | 303 |
| order / index | (162/320) | (162/320) |
| SmallGroup ID | `[162,11]` | `[162,19]` |
| abelianization | `[2,3]` | `[2]` |
| derived subgroup order | 27 | 81 |
| core in (G) | 1 | 1 |
| normalizer order | 324 | 324 |

## 2. Primitive integral orbit sums

Let $g(d)\in\mathbf Z[d]$ be the released nonmonic degree-$27$ line
eliminant, let $L>0$ be its leading coefficient, and let $d_1,\ldots,d_{27}$
be the roots in the released labelling. Put

\[
\alpha_i=Ld_i.
\tag{2.1}
\]

Every (alpha_i) is integral: substituting (y=Ld) in (g(d)) and
multiplying by (L^{26}) gives a monic integer polynomial for (y).

Define pair supports

\[
\mathcal S_+=H_+\!\cdot\!\{1,2\}\sqcup
H_+\!\cdot\!\{1,9\},\qquad |\mathcal S_+|=27+27=54,
\tag{2.2}
\]
\[
\mathcal S_-=H_-\!\cdot\!\{1,2\},\qquad |\mathcal S_-|=81,
\tag{2.3}
\]

and

\[
\eta_+=\sum_{\{i,j\}\in\mathcal S_+}\alpha_i\alpha_j,
\qquad
\eta_-=\sum_{\{i,j\}\in\mathcal S_-}\alpha_i\alpha_j.
\tag{2.4}
\]

In every C59 artifact, (eta) means the scaled integral invariant (2.4).
If the unscaled sum is useful, it is denoted
$\widetilde\eta_\pm$, so that

\[
\eta_\pm=L^2\widetilde\eta_\pm.
\tag{2.5}
\]

The exact product-form resolvents are

\[
R_\pm(T)=\prod_{gH_\pm\in G/H_\pm}(T-g\eta_\pm).
\tag{2.6}
\]

By C59-EXACT-1 and the written primitivity lemma, these are monic
integral irreducible separable degree-(320) minimal polynomials. No expanded
characteristic-zero coefficient vector or coefficient hash is claimed.

## 3. C59-EXACT-0 through C59-EXACT-7

### C59-EXACT-0: released-authority rebind — `PREFREEZE_CODE_RESULTS_PASS`

The producer and independent checker bind complete C56 and C58 release
inventories, self-excluding manifests, live/archive Route identity,
certificates, schemas, check reports, the eliminant and lex shapes, labelled
(W_{27}), exact C58 (D,I,P,Q) arrays, the current Batch target, and the
protected guard. No certificate-selected arbitrary path is accepted.

### C59-EXACT-1: primitive integral orbit-sum resolvents — `PREFREEZE_CODE_RESULTS_PASS`

The promoted tuple certifies:

1. the exact support sizes (27,27,81), disjointness of the two (H_+)
   components, and support stabilizers exactly (H_+,H_-);
2. 320 support conjugates for each family;
3. primality and good denominator conditions at (p=692717);
4. a squarefree complete split (1^{27}) of the eliminant;
5. exact reconstruction of all 27 lines and zero substitution in every one of
   the four chart line equations;
6. a 27-vertex, 135-edge, 10-regular incidence graph;
7. structural equality
   $\operatorname{Aut}(\text{Schlaefli graph})=W(E_6)$ as equality with the
   released 51,840-element permutation set;
8. 320 distinct values for both (eta_+) and (eta_-); and
9. complete 321-coefficient modular products with hashes

   ```text
   H+  21b304679d3b77a7b1fae4182e203d8f2652588efffa4a160cccd98ac3e81257
   H-  76fa8081c92e58839f60659fa7c9979d9b002fae5408cc30777341d21665acb2
   ```

The bounded graph and split-prime pilots available at target selection remain
historical feasibility evidence only. The complete promoted G1 lanes, not
those pilots, supply this machine PASS.

### C59-EXACT-2: complete Gassmann/minimality certificate — `PREFREEZE_CODE_RESULTS_PASS`

The promoted group lane enumerates all 350 subgroup conjugacy classes and
recovers exactly these eleven two-class collision buckets:

```text
[12,15], [17,21], [29,36], [31,39], [41,42], [46,48],
[57,58], [59,64], [112,120], [132,140], [301,303].
```

The full induced trivial characters, not samples, agree for 301/303. The last
pair alone has minimum index 320. The exact subgroup invariants in section 1,
package versions, and transport to the released action were recomputed
independently. James is credited for the prior complete collision count.

### C59-EXACT-3: fixed-field and zeta bridge — `PREFREEZE_CODE_RESULTS_PASS`

The promoted tuple certifies support invariance, 320 distinct
characteristic-zero conjugates, fixed-field equality, common normal closure
from trivial cores, nonisomorphism from nonconjugacy, and equality of Dedekind
zeta functions from the full rational permutation-character identity.

### C59-EXACT-4: signed discriminant, signature, and support — `PREFREEZE_CODE_RESULTS_PASS`

The promoted tuple recomputes on both degree-(320) coset carriers the
orbit-count vector

```text
I3,P3,Q3,I5,P5,tame-C3,reflection-C2,C-infinity
36,56,112,16,64,128,160,168.
```

It derives exponents `(624,496,192,160)`, signature `(16,152)`, positive sign,
and exact support

```text
3,5,181,283,997,1801,2346241,
14932047182473291995860108491583652133938007263719.
```

The 11,658-digit positive discriminant has unsigned no-newline decimal digest
`7f3ed0f731e5905f9af8254df2114ad15c2bb7d96cfa9a8b464a58ae8ea3ae70`.

### C59-EXACT-5: complete ToM-140 local algebra — `PREFREEZE_CODE_RESULTS_PASS`

The promoted tuple enumerates every double coset and certifies the first table
in section 5, including (n=ef), 36 factors, total degree 320, and total
(sum fd=624).

### C59-EXACT-6: complete ToM-206 local algebra — `PREFREEZE_CODE_RESULTS_PASS`

The promoted tuple proves the unique normal embedded ToM-140 inertia and the
exact normal lower filtration in each ToM-206 candidate. It certifies the
second table in section 5, including (n=ef), 18 factors, total degree 320,
total (sum fd=624), and branch-independent local separation. The
branch-selection leaf is false.

### C59-EXACT-7: independent checker, envelope, novelty, scope, release discipline — `PREFREEZE_CODE_RESULTS_PASS`

The implementation has disjoint producer/checker theorem call graphs, strict
schemas and exact key sets, scalar/structural/type-confusion mutations,
pre/post child source rebound, deterministic replay, hardened atomic promotion
and rollback, a self-excluding scoped manifest, exact source credits, and
explicit false scope leaves. Common utilities are restricted to canonical
I/O, fingerprints, and backend preflight.

## 4. Certified integrated theorem

### Theorem A: primitive minimum-index Gassmann fields

C59-EXACT-0 through C59-EXACT-3 are certified. Therefore the exact subgroups
(H_+,H_-) are core-free, nonconjugate, nonisomorphic, and have equal full
rational transitive permutation characters. Within the complete (W(E_6)) subgroup
table, their collision is the unique minimum-index collision, of index 320.
Moreover,

\[
F_+=\mathbf Q(\eta_+)=K^{H_+},\qquad
F_-=\mathbf Q(\eta_-)=K^{H_-}.
\tag{4.1}
\]

The fields have degree 320, common normal closure (K), are not
$\mathbf Q$-isomorphic, and satisfy

\[
\zeta_{F_+}(s)=\zeta_{F_-}(s).
\tag{4.2}
\]

### Theorem B: exact global arithmetic

C59-EXACT-4 is also certified. Put

\[
q=14932047182473291995860108491583652133938007263719,
\]
\[
A=181\cdot997\cdot2346241=423395612137,
\]
\[
B=283\cdot1801\cdot q
=7610610604104534884325967676315830570581925356194091077.
\]

Then both fields have signature ((16,152)), exact finite ramified support

\[
\{3,5,181,283,997,1801,2346241,q\},
\tag{4.3}
\]

and signed discriminant

\[
\operatorname{Disc}(F_+)=\operatorname{Disc}(F_-)
=+3^{624}5^{496}A^{192}B^{160}.
\tag{4.4}
\]

### Theorem C: branch-independent local inequivalence

C59-EXACT-5 and C59-EXACT-6 are also certified. For either C58-permitted
decomposition group (D_3), the finite etale algebras

\[
F_+\otimes_{\mathbf Q}\mathbf Q_3
\quad\text{and}\quad
F_-\otimes_{\mathbf Q}\mathbf Q_3
\]

are not isomorphic. Consequently (F_+) and (F_-) are arithmetically
equivalent but not locally equivalent and have nonisomorphic adele rings.

Theorems A--C form one certified integrated theorem. They may not be split
into separate fallback papers.

## 5. Complete local tables

For a fixed prime of (K) above 3 and a double-coset representative, let

\[
J=D\cap gHg^{-1},\quad
n=[D:J],\quad e=[I:I\cap J],\quad f=[D:IJ].
\tag{5.1}
\]

Then $n=ef$, and the factors of $K^H\otimes\mathbf Q_3$ are indexed by
$D\backslash G/H$. Each displayed row is `(n,e,f,d)^multiplicity`.

If $D_3=\mathrm{ToM} 140=I_3$:

| field | complete rows |
|---|---|
| (F_+) | `(1,1,1,0)^8`, `(6,6,1,11)^10`, `(9,9,1,18)^8`, `(18,18,1,37)^10` |
| (F_-) | `(2,2,1,1)^4`, `(3,3,1,5)^12`, `(6,6,1,11)^4`, `(9,9,1,18)^4`, `(18,18,1,37)^12` |

Each line has 36 factors, total degree 320, and total (sum fd=624).
(F_+) has eight degree-one factors; (F_-) has none.

If $D_3=\mathrm{ToM} 206$, with unique normal inertia ToM 140:

| field | complete rows |
|---|---|
| (F_+) | `(2,1,2,0)^4`, `(12,6,2,11)^5`, `(18,9,2,18)^4`, `(36,18,2,37)^5` |
| (F_-) | `(4,2,2,1)^2`, `(6,3,2,5)^6`, `(12,6,2,11)^2`, `(18,9,2,18)^2`, `(36,18,2,37)^6` |

Each line has 18 factors, total degree 320, and total (sum fd=624).
(F_+) has four unramified quadratic factors; (F_-) has no degree-two
factor.

Different factor-degree multisets suffice for nonisomorphism. The tuple
`(n,e,f,d)` is not claimed to determine an individual high-degree local field
up to isomorphism.

## 6. Exact proof and authority boundary

The finite exact premises belong to the promoted project-local producer,
independent checker, evidence tuple, schema, mutation suite, and scoped
manifest. The implications from those premises to Theorems A--C are written
mathematics and are detailed in `PROOF_PACKAGE.md` and `DERIVATION.md`.

Target-selection pilots establish only historical feasibility. They are not
substituted for the promoted C59-EXACT-0--7 evidence or its independent
post-refresh hostile audit.

## 7. Nonclaims

`NO_BAD_EULER_OR_ROOT_NUMBER`.

No expanded characteristic-zero coefficients, characteristic-zero
coefficient hash, integral basis, maximal order, monogenicity, equality of
polynomial and field discriminants, individually classified high-degree
completion, selected (D_3), integral permutation equivalence, ring-of-
integers isomorphism, class-number equality, local or adelic equivalence,
bad Euler/Frobenius/epsilon/root-number data, Artin holomorphy, automorphy,
rational-point theorem, Brauer--Manin conclusion, motive, RH, or
Hilbert--Polya operator is asserted.

“Primitive” refers only to field generation by $\eta_\pm$.

## 8. Current status

All C59-EXACT machine premises have `PREFREEZE_CODE_RESULTS_PASS`, and the
promoted bytes have `POSTREFRESH_PASS`. The exact inventory is 13 code files,
8 result files, 21 live leaves, and a 20-entry self-excluding scope; all 48
source tests passed. The checker rebuilt 10,412 payload leaves and rejected
20,894 certificate mutations plus 8 self-consistent evidence-rebound
mutations. It binds:

```text
payload  a6428addfb14f00f3ed45781d9ba0944be177cfb7c257c958e7fa538fcaf366b
shape    788aa5e58d51f0d4edfa7a4e58de5748bd5a1ad1d28445d91045d5dd72c850d2
G0       ac445822702b5e376eed6fbfa86a4df81c7f8177ca35c8211282dca830123d5d
cert     3c4c756d912d49653353503701f5b8be412d0da53383ac9c9830b6e7a953ed9a
check    271d0123b170bef1317b63e97e3f679179b6e794185b78facd571150ba2123d3
schema   07a817bb2eade24862f0cf4dca8d1d0248eb4f473a137c07bd0200efeea8c6b4
group    0b01f9d47e5141d2bff88fbe4d58ed049d88751cbf8ab1df5469009b684c4958
resolver 667e0eeb04e5724b620bf513f9556a321dfd39f9215396ed1840ca83879ec6a6
manifest c4145ea23b57b1adcd8cfddb18c41c703e93ca8a6f84eeecb9457e0f4e046dda
```

The edited formal roots have `FORMAL_DOCS_PASS`. Paper, implementation
commit, full-project manifest, Route archive, promotion, and release remain
pending.
