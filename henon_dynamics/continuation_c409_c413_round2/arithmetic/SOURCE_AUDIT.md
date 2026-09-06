# Finite-lattice census: ownership audit

Audit date: 2026-09-06. Author-side source audit, not an independent review or a
claim of exhaustive literature coverage. No result is admitted here.

## Decision

**PRIORITY_NOT_CLEARED — retain the exact proof as an unnumbered research
candidate, but do not count it as the fifth independent result yet.**

The complete observation quotient has been derived in
[FINITE_LATTICE_CENSUS_PROOF.md](FINITE_LATTICE_CENSUS_PROOF.md). The accessible
sources checked below do not explicitly state the same full inverse theorem
and complete fibre classification. That is not enough to certify novelty:
an original 2003 paper explicitly points to older two-dimensional
Bowen–Franks recurrences, and the precise 1996/1999 texts have not been obtained.
A 2003 dissertation in the same line is an additional material retrieval gate.
The broad original result must therefore not be relabelled “new” merely because
it has a short self-contained proof.

## 1. Exact claim being audited

For every hyperbolic \(A\in\mathrm{SL}_2(\mathbb Z)\), the native observation is
\[
 F_A(q,n)=\#\operatorname{Fix}
   \bigl(A^n\mid(\mathbb Z/q\mathbb Z)^2\bigr),\qquad q,n\ge1.
\]
The modulus and period labels are retained. Put
\[
 t=\operatorname{tr}A,\quad h=c(2A-tI),\quad
 g=\gcd(A_{12},A_{21},A_{22}-A_{11}),
\]
where \(c\) is entry content.

The proposed residual contribution is the following package, not its standard
ingredients.

1. Equality of the entire ordinary census is equivalent to equality of the
   two period rows \(n=1,2\), and to equality of \((t,h)\), for both trace signs.
2. The quotient of the established local-conjugacy classification by this
   observation is completely explicit. For odd trace it has one class per
   admissible label. For \(t=2T,\ h=2r,\ r^2\mid T^2-1\), it has the class
   \(g=r\), plus exactly one class \(g=2r\) iff
   \((T^2-1)/r^2\equiv1\pmod4\).
3. Every permitted label and both branches are realized by integer matrices;
   the smallest absolute collision trace is 18, and collisions occur at
   infinitely many traces.

No novelty claim is made for Smith normal form, period counts on the real
torus, the Cayley–Hamilton recurrence, local conjugacy, or the general fact
that an unstructured periodic count loses information.

## 2. Closest sources and their actual scope

| Primary source | Material actually inspected | Ownership implication |
| --- | --- | --- |
| Baake–Roberts–Weiss, *Periodic orbits of linear endomorphisms on the 2-torus and its lattices*, Nonlinearity 21 (2008), 2427–2446, [published author PDF](https://web.maths.unsw.edu.au/~jagr/BRW08.pdf), DOI 10.1088/0951-7715/21/10/012 | Introduction; Cayley–Hamilton formulas; global and local counting definitions; §3.4 including Proposition 3 and proof; §4 including the matrix-gcd classification, Theorem 2 and Corollaries 3–4 with proof. | Owns the native finite-lattice setting, cardinality-to-periodic-group reconstruction, and classification by trace/determinant/matrix gcd. Its same-invariant ⇒ same-statistics result is forward, not the complete inverse being proposed. Its trace-20 example separates integral conjugacy inside one local class; the trace-18 pair here separates local classes. |
| Neumärker, *The arithmetic structure of discrete dynamical systems on the torus* (2012), [German National Library PDF](https://d-nb.info/1023674939/34) | Full §3.3, pp. 11–14, especially Theorem 3.3.1 and Proposition 3.3.3; §3.8.2, pp. 27–29, including Remark 3.13; relevant Fibonacci/Arnold appendix. | Owns the Smith framework and all-modulus recovery of periodic groups. Explicitly distinguishes local conjugacy from equality of orbit counts and discusses the difficulty of controlling Smith forms over varying powers. No complete signed-trace two-period quotient was found in these inspected sections. |
| Baake–Neumärker–Roberts, *Orbit structure and symmetries of toral endomorphisms on the rational lattice*, DCDS 33 (2013), 527–552, [author PDF](https://web.maths.unsw.edu.au/~jagr/BNR13.pdf), [publisher](https://www.aimsciences.org/article/doi/10.3934/dcds.2013.33.527) | Introduction and targeted occurrences concerning matrix gcd, fixed-point statistics, orbit structure and conjugacy. Not a claim to have re-proved every result in the paper. | Establishes nearby orbit/reversibility infrastructure and inherits the forward BRW classification. No explicit complete inverse fibre theorem was located in the inspected material. |
| Rodrigues–Sousa Ramos, *Bowen–Franks groups as conjugacy invariants for \(T^n\) automorphisms*, [2003 original preprint](https://arxiv.org/abs/math/0303185); [2005 published metadata](https://link.springer.com/article/10.1007/s00010-004-2753-7), Aequationes Math. 69, 231–249 | Preprint definitions, principal/generalized and strong equivalence, Lemma 1, Proposition 3; coefficient-ring lattice and §4.1–4.3, including Corollary 1 and Proposition 9; reference list. Publisher summary and dates checked; the 19-page published text was not retrieved, so identity with the 15-page preprint is not assumed. | A decisive prior owner for BF equivalence and the module/local-conjugacy bridge. Its generalized BF equivalence quantifies over all suitable rational polynomials; our census only sees \(X^n-1\). More importantly, its introduction explicitly cites the unresolved older two-dimensional recurrences below. |
| Bakker–Rodrigues, *A Profinite Group Invariant for Hyperbolic Toral Automorphisms*, [arXiv:1102.0839](https://arxiv.org/abs/1102.0839); DCDS 32 (2012), 1965–1976, DOI 10.3934/dcds.2012.32.1965 | Abstract, introduction and the strong-BF/profinite formulation. | The periodic data retain an \(R\)-module action. This is not merely the ordinary array of cardinalities and does not by itself give the proposed forgetful quotient. |
| Bakker–Rodrigues–Moreira, *Local Conjugacy of Irreducible Hyperbolic Toral Automorphisms*, [arXiv:1611.05551](https://arxiv.org/abs/1611.05551) | Introduction, weak-ideal/local-conjugacy statements through Corollary 5, and the rank-two scalar-depth classification around Theorem 20. | Reinforces the prior ownership of the local-conjugacy classification. This part is a dependency, never the new result. |
| Bakker–Rodrigues, *Generalized Bowen–Franks Groups and Profinite Conjugacy for Hyperbolic Toral Automorphisms*, [arXiv:2207.00922](https://arxiv.org/abs/2207.00922) (2022) | Opening three pages: principal/generalized BF definitions, coefficient ring and main strong-principal/profinite-conjugacy equivalence. | Again the main equivalence retains the module action. Equality of abstract groups for every principal polynomial is a weaker observation. This distinction is necessary, but insufficient to clear the older ownership gate. |
| Pacheco, *On the integer matrix conjugacy problem and p-adic numbers* (2021), [official Técnico record and open PDF](https://scholar.tecnico.ulisboa.pt/records/u5JKiiTxlPuTD_Rj8RuhkiAKzTnVsNoPBeGl?lang=pt) | Full §5.3, pp. 48–54; §4.2.1, pp. 31–34; conclusion and bibliography. PDF metadata: 68 pages, 675,418 bytes, readable and unencrypted. | The BF statements are quotient/Smith descriptions and cardinality formulas, with a warning that extending the local field does not add Smith information. The 2-adic case is matrix LTE/order lifting. Neither inspected section states the complete all-modulus inverse or fibre theorem here. |

The word “weak” is particularly unsafe without a definition: weak ideal
equivalence, abstract generalized BF equivalence, abstract principal BF
equivalence, and equality of unlabelled real-torus fixed counts are different
contracts.

For example, the proposed trace-18 matrices have identical principal BF groups,
but the polynomial \(X-5\) distinguishes them even as abstract groups:
\[
 \mathbb Z^2/(A-5I)\mathbb Z^2\simeq
 \mathbb Z/4\mathbb Z\oplus\mathbb Z/16\mathbb Z,\qquad
 \mathbb Z^2/(B-5I)\mathbb Z^2\simeq
 (\mathbb Z/8\mathbb Z)^2.
\]
This follows directly from their entry gcds and common determinant \(-64\).
It explains why the proposed collision does not contradict the old
generalized-BF classification.

## 3. Material older-source gate

The following is one connected historical lead, not three speculative
citations added for appearance.

| Exact source | Verified evidence | Missing evidence and consequence |
| --- | --- | --- |
| Pedro Alves Martins Rodrigues, *Automorfismos Hiperbólicos do Toro*, MSc, Instituto Superior Técnico, 1996 | The [institutional MSc catalog](https://math.tecnico.ulisboa.pt/library/msctheses?lang=pt) identifies entry Nº02/96. It is [MR 96] in the original 2003 BF paper, whose introduction attributes earlier two-dimensional recurrence results to it. | Full thesis not retrieved. The precise BF recurrences and any inverse completeness statements remain unchecked. This is a material gate, not a negative search result. |
| Rodrigues–Sousa Ramos, *Topological and geometrical properties of isentropic torus automorphisms*, Grazer Mathematische Berichte 339 (1999), 251–260 | Exact reference in the original 2003 paper; independently listed in the [coauthor's institutional publication record](https://cfcul.mcmlxxvi.net/equipa/sramos.php). The [Graz series catalog](https://imsc.uni-graz.at/schwaiger/gmb/) confirms the volume. | Only bibliographic/abstract information located, not the paper's theorem text. The citation in the primary 2003 paper directly identifies this as prior two-dimensional work; its content must not be guessed from an abstract mentioning holonomy. |
| Rodrigues, *Classificação topológica dos automorfismos do toro*, PhD, IST, 2003 | [Institutional PhD catalog](https://math.tecnico.ulisboa.pt/library/phdtheses?lang=pt), Nº04/03, and [National Library thesis-abstract collection](https://purl.pt/402/2/UTL2003-Teses.pdf), printed pp. 176–177. The abstract specifies BF groups and their power to distinguish isentropic automorphisms; defense date is 26 September 2003. | The collection is an abstract catalog, not the dissertation. Full dissertation, especially its BF chapter, remains unavailable in the inspected public paths. It could carry or consolidate the earlier recurrence result. |

No login circumvention, purchase, author contact, or library request was made.
Those would require an appropriately scoped next step. “Not retrieved” is not
“does not contain the theorem.”

## 4. Further boundary checks

These records were examined at the stated depth only; they do not close the
material gate.

- Seibt, *A period formula for torus automorphisms*, DCDS 9 (2003),
  1029–1048, DOI 10.3934/dcds.2003.9.1029: publisher abstract concerns an order/
  period formula. Normal public PDF retrieval did not produce a readable PDF;
  no full-text clearance is claimed.
- Sheng Chen, *Generalized Bowen–Franks groups of integral matrices with the
  same zeta function*, LAA 431 (2009), 1397–1406,
  [publisher record](https://www.sciencedirect.com/science/article/pii/S0024379509002766),
  DOI 10.1016/j.laa.2009.05.016: the inspected abstract gives common generalized
  BF Sylow data away from an exceptional integer for its stated class of
  matrices. This is not, on the abstract alone, a complete classification of
  the exceptional 2-adic fibre in rank two. Full-text ownership remains unverified.
- Lei–Müller–Vallières,
  [*Bowen–Franks groups and minus class groups of cyclotomic number fields with
  prime conductor*, arXiv:2605.01398](https://arxiv.org/abs/2605.01398), submitted
  2 May 2026: the official abstract concerns a directed graph and cyclotomic
  class groups, not the hyperbolic rank-two finite-lattice inverse problem.
  This is an abstract-level recent-title collision check, not a full-paper audit.

Searches included the exact candidate invariant and matrix pair, finite-lattice
zeta/orbit equivalence, local integral/profinite conjugacy, principal versus
generalized BF equivalence, two-dimensional recurrence, p-adic and 2-adic BF
groups, and exact Portuguese/English titles in the older citation chain.
Search-engine crawl dates were not used as publication dates. Recent coverage
is expressly bounded; no claim of global literature exhaustion is made.

## 5. Relation to independent mathematical review and next gate

The companion proof is an author derivation. The exact script is a finite
diagnostic, not an independent peer review or a proof of its universal claims.
The parent reviewer performs the separate mathematical and substantive decision.

The candidate should advance to publication planning only if all of the
following are satisfied:

1. An independent reviewer accepts the all-sign/all-parity proof and the exact
   fibre realization, without treating the finite script as the proof.
2. The older BF recurrence texts are obtained, or another verifiable primary
   source locates and precisely reproduces their applicable statements.
3. The residual distinction is assessed as substantive after crediting those
   results. Merely adding the word “inverse” to already equivalent formulas
   would not meet this gate.

Until then, no C-number, fifth accepted slot, manuscript, formal Route-A score,
global registry edit, or reinterpretation as a Riemann determinant is justified.
