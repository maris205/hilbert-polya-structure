# HCS-C56 paper plan

Title: **The Twenty-Seven-Line Field of the Fourth Hénon Yukawa
Surface**

Status: **DOCS_FINAL_NO_MORE_EDITS; official 19-page paper build PASS for the
project RELEASE_FROZEN.**

One-sentence target contribution: **For the exact cubic surface produced by
HCS-C55, certify that its Fano scheme is one degree-27 finite étale field
point, that its normal closure has Galois group \(W(E_6)\), and that its
geometric and arithmetic Picard ranks are \(7\) and \(1\).**

Paper type: arithmetic geometry plus exact symbolic certification.

No venue or format is selected.  Drafting began only after the complete exact
producer/checker handoff passed independent source review.

## 0. Claims--evidence matrix

| Intended claim | Conceptual evidence | Instance evidence required | Current state |
|---|---|---|---|
| \(F_1(Y)\) is finite étale of rank 27 | Grassmann line section; total-27 theorem; simple-zero theorem | exact C55 source rebind and smoothness replay | PASS |
| \(F_1(Y)\cong\operatorname{Spec}(E)\), \([E:\mathbf Q]=27\) | chart morphism, clopen global step, equal-rank argument | eliminant, back-substitutions, direct remainders, complement charts | PASS |
| \(g\) is irreducible | modular subset-sum lemma | complete factors, multiplication, gcds, subset sums | PASS |
| \(\operatorname{Gal}(K/\mathbf Q)=W(E_6)\) | Elsenhans--Jahnel subgroup criterion and parity distinction | Frobenius pattern and independent 51840-element enumeration | PASS |
| Picard ranks are \(7/1\) | cubic-surface lattice and rank-only Hochschild--Serre descent | fixed-space rank one plus written rank bridge | PASS |
| no rational line and \(27\mid[L:\mathbf Q]\) for a line field \(L\) | field-point universal property | connected degree-27 line scheme | PASS |

Every right-hand evidence gate is certified at code/results prefreeze.  The
paper states them as exact prefreeze results while keeping release provenance
and official-build status explicit.

## 1. Planned paper-level theorem

Let \(Y/\mathbf Q\) be the frozen C55 Yukawa cubic surface, let
\(F_1(Y)\) be its line scheme, and let \(E\) be the residue field defined by
the certified eliminant. Prove

$$
F_1(Y)=\operatorname{Spec}(E),\qquad [E:\mathbf Q]=27,
$$

identify the splitting field \(K\) with the common normal line field, and
prove

$$
\operatorname{Gal}(K/\mathbf Q)\cong W(E_6),\qquad [K:\mathbf Q]=51840.
$$

Then derive geometric/arithmetic Picard ranks \(7/1\), absence of a
\(\mathbf Q\)-line, and the degree-divisibility statement for every finite
line-definition field.

## 2. Proposed section structure

### Abstract

- identify the exact C55 cubic surface without repeating its Hodge theorem;
- state the connected degree-27 line scheme;
- state the full \(W(E_6)\) normal closure and Picard ranks;
- state the exact-computation boundary and avoid rationality claims.

### 1. Introduction

- motivate the arithmetic of the 27-line configuration;
- explain why C56 is logically independent of C55;
- distinguish \(E\) from \(K\);
- state Theorems A--B and Corollaries C--D;
- list the main firewalls and bounded novelty scope.

### 2. The fixed cubic and its Fano scheme

- reproduce the exact primitive cubic and its C55 source lock;
- define \(F_1(Y)\) via
  \(\operatorname{Sym}^3(\mathcal S^\vee)\);
- separate the total count of 27 from simple zeros;
- conclude finite étaleness before using any chart.

### 3. A degree-27 chart presentation

- fix the \(U_{01}\) convention;
- display \(f_0,f_1,f_2,f_3\);
- present \(g,h_a,h_b,h_c\) and their normalizations;
- prove direct membership by four zero remainders;
- pass from the chart to the global scheme using the clopen step and equal
  rank;
- record the five complementary-chart checks as an independent guard.

### 4. Exact irreducibility

- state and prove the modular subset-sum lemma;
- give complete factor tables at the four selected good primes;
- show squarefreeness and multiplication-back identities;
- display the four subset-sum sets and intersection \(\{0,27\}\);
- conclude that \(E\) is a field and the 27-line action is transitive.

### 5. The full Weyl Galois group

- recall the Schläfli configuration and \(W(E_6)\) containment;
- define the index-two subgroup \(U\) by Coxeter determinant;
- explain why ordinary \(S_{27}\) sign is useless;
- derive an order-five element from the target Frobenius type;
- apply Elsenhans--Jahnel Lemma 8;
- exclude \(U\) with exact enumeration of every target-type element;
- identify \(K\) and its degree.

### 6. Picard ranks and fields of definition

- construct the blow-up basis, canonical class, roots, reflections, and line
  classes;
- compute the fixed subspace;
- apply Hochschild--Serre only at the rank level;
- prove the degree-27 divisibility and no-rational-line corollary;
- state projective invariance.

### 7. Exact replay and hostile validation

- define the canonical payload and schema;
- separate producer and independent checker;
- report all-leaf classification and rebound outcomes;
- report rollback, nonmutation, resource, and deterministic replay checks;
- list machine-assisted facts versus conceptual deductions.

### 8. Context and limitations

- compare with the classical and computational literature on 27 lines;
- describe the bounded recent-neighbor search;
- state that no generic-family theorem is inferred;
- separate rational lines from rational points and rationality;
- exclude motivic, VHS, Calabi--Yau, and global arithmetic overclaims.

### Appendix A. Primary-source locator ledger

- Elsenhans--Jahnel Fact 3, Remarks 4--5, Lemma 8, Algorithm 10,
  Remarks 11--13;
- Kass--Wickelgren Definition 41, Theorem 2, Corollaries 53--54;
- the Hochschild--Serre low-degree exact sequence and rank wording.

### Appendix B. Chart coefficient tables

- the full primitive coefficient array of \(g\) and compact chart invariants;
- summaries of the \(h_a,h_b,h_c\), direct-remainder, and complementary-chart
  gates, whose complete large arrays remain in the exact machine certificate.

### Appendix C. Modular and lattice tables

- full modular factors and subset sums;
- roots, line classes, reflection matrices, target-type counts, and fixed-rank
  computation.

## 3. Planned theorem numbering

- Theorem A: complete connected finite étale line scheme.
- Theorem B: maximal line-field Galois group.
- Corollary C: Picard ranks and degrees of line-definition fields.
- Corollary D: rational projective invariance.

## 4. Planned tables

1. claim/source/internal-certificate boundary;
2. C55 source-lock and cubic normalization;
3. main-chart shape and remainder ledger;
4. complementary-chart coverage;
5. complete modular factorizations;
6. subset-sum intersection;
7. Weyl-group/parity enumeration;
8. Picard-lattice fixed-rank calculation;
9. semantic mutation and rollback outcomes.

No decorative figure is planned. A Schläfli incidence diagram is admissible
only if it clarifies the certified group action and can be generated from the
same exact line-label data.

## 5. Writing gates

The drafting gates have passed:

1. C56-EXACT-0 through C56-EXACT-4 are certified;
2. producer and independent checker agree on the canonical payload;
3. the all-leaf rebound and runner audits pass;
4. all formal documents are promoted consistently from conditional to
   certified wording;
5. an independent source reviewer confirms every locator and inference.

The sources are byte-stable, the fresh isolated compile audit passes, and the
official final build has no TeX/BibTeX errors, undefined references or
citations, duplicate destinations, rerun requests, or overfull/underfull box
warnings. Fonts, extracted text, metadata, and all page visuals also pass.

## 6. Current paper artifacts

| Artifact | Value |
|---|---|
| paper source | `5db4cfd2650485001d00fc2f52681d4cfaf8e739f4924b331df7ccc06a851cb3` |
| bibliography | complete; 6 cited entries; BibTeX warnings 0 |
| PDF | `750c1da7366701495fa3bf1f37014000d56fcb59a556f896224a5611b622a923` |
| log | `9f2845fdc37011aa259085810595703819741844be0d0ff15cdfc78c94e41a07` |
| extracted text | `217ca51b1b0b4e6637f3d8405f23671aa89775d30e37ac964cb0684b548c2856` |
| compilation report | `fd7c17d5121d4661b4fb385e2ab420882cfced172f9c5098c4152d68c6d5a3c8` |
| independent paper audit | source semantics, isolated compile, and final artifact audit PASS |

The controlled bootstrap, former documentation build, and superseding frozen
status-repair build are complete.  No further paper edit or compilation is
authorized in this lane.
