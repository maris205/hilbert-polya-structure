# HCS-C50 primary-source and novelty audit

Only primary papers or official archival records support external
theorem-level inputs. The explicit automorphisms, group relations,
idempotents, Euler coefficient matching, recurrence Gröbner basis, and
fourth-moment formulas are proved internally.

## 1. Idempotents and Jacobian isogenies

Ernst Kani and Michael Rosen, **“Idempotent relations and factors of
Jacobians,”** *Mathematische Annalen* 284 (1989), 307--327,
DOI [10.1007/BF01442878](https://doi.org/10.1007/BF01442878);
[EuDML archival record](https://eudml.org/doc/164555).

Relevant locator: Theorem A identifies rational idempotent relations in the
endomorphism algebra with isogeny relations among their images; the opening
sections develop the group-algebra-to-Jacobian correspondence. This is the
general mechanism behind (rather than a proof of) the C50 decomposition.
C50 verifies the three \(K\)-rational automorphisms, their relations, the
two standard representation blocks, and the primitive idempotents
\(q_\pm\) directly.

## 2. Cyclic trigonal genus-four moduli and closest decomposition prior

Milagros Izquierdo and Daniel Ying, **“Equisymmetric strata of the moduli
space of cyclic trigonal Riemann surfaces of genus 4,”** *Glasgow
Mathematical Journal* 51 (2009), 19--29,
DOI [10.1017/S0017089508004497](https://doi.org/10.1017/S0017089508004497);
[publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/E691D386C77DE11A4F3153EAC28AA7F9/S0017089508004497a.pdf/equisymmetric_strata_of_the_moduli_space_of_cyclic_trigonal_riemann_surfaces_of_genus_4.pdf).

Relevant locator: Theorem 6, pp. 26--28, describes the disconnected
equisymmetric stratification of cyclic trigonal genus-four moduli, including
the higher-automorphism subloci. It supplies moduli context only. It neither
states the \(K\)-rational decomposition of the C48 fibre nor identifies its
Euler counterterm.

Ben Moonen, **“Special subvarieties arising from families of cyclic covers
of the projective line,”** *Documenta Mathematica* 15 (2010), 793--819,
DOI [10.4171/DM/314](https://doi.org/10.4171/DM/314);
[official EMS PDF](https://ems.press/content/serial-article-files/26094).

Relevant locators: §3.4 and Table 1, pp. 801--802, list the twenty positive-
dimensional special cyclic-cover families; Theorem 3.6, p. 801, proves the
list exhaustive up to the paper's equivalence. The C48 cover has monodromy
datum

\[
(m,N,\mathbf a)=(3,6,(1,1,1,2,2,2)),
\]

which is not the genus-four \(m=3,N=6\) entry
\((1,1,1,1,1,1)\). Thus Moonen's theorem does not make the current family a
special/CM family. It also does not forbid an isolated fibre with extra
endomorphisms. C50 claims neither generic CM nor CM for \(E_\pm\).

Leslie Jiménez, **“On the group algebra decomposition of a Jacobian
variety,”** *Revista de la Real Academia de Ciencias Exactas, Físicas y
Naturales. Serie A. Matemáticas* 110 (2016), 185--199,
DOI [10.1007/s13398-015-0226-6](https://doi.org/10.1007/s13398-015-0226-6);
[primary author-repository PDF](https://repositorio.uchile.cl/bitstream/handle/2250/138937/On-the-group-algebra-decomposition-of-a-Jacobian-variety.pdf?isAllowed=y&sequence=1).

Relevant locators: §5.1, pp. 193--194, records the genus-four trigonal
automorphism strata; Theorem 3 and its table, pp. 195--196, include
genus-four reduced-\(D_3\) and reduced-\(D_6\) rows whose Jacobians are
isogenous over \(\mathbf C\) to products of four elliptic curves, with
kernel order \(9\). The reduced-\(D_3\) row has full group
\(D_3\times D_3\); the reduced-\(D_6\) row has full group
\((C_3\times C_3)\rtimes D_4\) of order \(72\). Neither row identifies the
C48 equation or its \(K\)-descent. C50 proves only that three explicit
automorphisms generate an order-\(12\) subgroup \(C_2\times S_3\); it does
not determine \(\operatorname{Aut}(C)\) or claim membership in either
Jiménez row. The table is therefore prior art for complete decomposability,
not a substitute for the C50 proof.

## 3. Modularity of the extracted elliptic factors

Ana Caraiani and James Newton, **“On the modularity of elliptic curves over
imaginary quadratic fields,”** arXiv:2301.10509v3 (27 March 2025),
[primary arXiv PDF](https://arxiv.org/pdf/2301.10509).

Relevant locator: Theorem 1.1 (Corollary 7.1.2), p. 2, proves modularity of
every elliptic curve over an imaginary quadratic field \(F\) when
\(X_0(15)(F)\) is finite; the immediately following text explicitly lists
\(\mathbf Q(\sqrt{-3})\). The final paragraph on p. 2 states that modularity
gives analytic continuation of the elliptic \(L\)-function to the entire
plane.

Scope firewall: this theorem applies separately to \(E_+\) and \(E_-\).
It does not give a functional equation for the complete Hénon Euler object,
does not prove it zero-free, and does not improve individual Frobenius traces
beyond the Weil bound.

Roger Godement and Hervé Jacquet, **Zeta Functions of Simple Algebras**,
Lecture Notes in Mathematics 260, Springer (1972),
DOI [10.1007/BFb0070263](https://doi.org/10.1007/BFb0070263).

Relevant locator: “Global Theory,” pp. 136--184, supplies the standard
analytic continuation and functional equation for automorphic
\(\mathrm{GL}_n\) \(L\)-functions. Together with Caraiani--Newton, this
supports completed functional equations for the two extracted elliptic
automorphic factors. It does not produce a completion or functional equation
for the residual \(H_2\) or the full Hénon Euler object.

## 4. Weights and nonmiddle cohomology

Pierre Deligne, **“La conjecture de Weil. I,”** *Publications
Mathématiques de l'IHÉS* 43 (1974), 273--307;
[official IAS record and PDF](https://publications.ias.edu/node/368).

Relevant locator: Théorème (1.6), pp. 275--277, gives absolute value
\(q^{i/2}\) for Frobenius eigenvalues on \(H^i\) of a smooth projective
variety. C50 applies it only at good reductions to
\(H^6_{\mathrm{prim}}(S)\) and \(H^5(X)\).

A. Grothendieck et al., **SGA 2: Cohomologie locale des faisceaux cohérents
et théorèmes de Lefschetz locaux et globaux**, North-Holland (1968);
[official recomposed PDF](https://www.cmls.polytechnique.fr/perso/laszlo/sga2/sga2original.pdf).

Relevant locator: Exposé XIV, Corollaire 4.6 (recomposed-text p. 184;
original-edition p. 267; physical PDF p. 192), supplies the global
cohomological Lefschetz comparison used for nonmiddle cohomology. The
middle ranks \(86\) and \(168\) are not copied from a classification table:
C50 derives them from the displayed Chern-class expansions and Euler
characteristics.

## 5. Regularized determinant background

Barry Simon, **Trace Ideals and Their Applications**, second edition,
Mathematical Surveys and Monographs 120, American Mathematical Society
(2005), ISBN 978-0-8218-4988-0;
[official AMS record](https://bookstore.ams.org/SURV/120).

Relevant locator: Chapter 9, “Regularized determinants and renormalization
in quantum field theory.” This is classical background only. The
field-degree-normalized faithful semifinite trace, the graded quotient,
the \(L^q(\mathcal M,\tau)\) threshold, and the C50
\(\operatorname{Det}_{10,\tau,\mathrm{gr}}\) identity are inherited and
proved within HCS-C47--C50. Simon does not turn that object into a classical
Fredholm determinant.

## 6. Internal claims and reproducibility boundary

The following claims require repository certificates rather than literature:

- the exact \(C_2\times S_3\) action on the frozen C48 curve;
- the \(K\)-rational idempotents and
  \(\operatorname{Jac}(C)\sim_K E_+^2\times E_-^2\);
- the sign and powers in
  \(\zeta_K(2s+1)^7L(H^1(C/K),2s+1)H_2(s)\);
- the ordered eight-step phase and projective direction identity;
- the exact characteristic-zero recurrence Gröbner basis;
- the \(p=181,\rho=48\) singular negative control;
- the fourth-moment substitution and the \(\Re s>1/5\) normal-convergence
  theorem; and
- the normalized-semifinite \(\operatorname{Det}_{10}\) versus classical
  \(S^{15}\) distinction.

Finite point-count ledgers validate formulas but do not prove the
all-prime statements. Characteristic-zero smoothness plus openness yields
only finitely many bad reductions, exactly as stated.

## 7. Search-bounded novelty and claim firewall

The search through 2026-08-14 supports novelty only for the following
combined, source-locked result:

1. the explicit \(K\)-rational \(C_2\times S_3\) idempotent decomposition
   of the C48 Hénon fibre into two squared elliptic factors;
2. the exact integer-power resummation of its second chronological
   logarithm by \(\zeta_K^7L(H^1(C/K))H_2\); and
3. its combination with the exact fourth-moment cohomological estimate to
   continue the Hénon Euler object to \(\Re s>1/5\).

No novelty is claimed for cyclic trigonal genus-four moduli, special
cyclic-cover families, group-algebra decomposition, completely decomposable
Jacobians, modularity of elliptic curves over \(K\), Deligne bounds, weak
Lefschetz, or regularized determinants.

The project does not claim a full Hénon functional equation, Gamma factor,
Riemann-zero match, natural boundary, global zero-free region, primitive-
orbit/prime correspondence, or self-adjoint Hilbert--Pólya operator.
