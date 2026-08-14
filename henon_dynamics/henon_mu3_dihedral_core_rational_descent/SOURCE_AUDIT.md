# HCS-C53 source audit

Status: primary-locator audit; chronology preserved from C51 and C52.

## Frozen computational source

- C52 implementation commit:
  `208feef86365cd92ace8dad02904acff6623eeec`.
- Frozen C52 certificate SHA-256:
  `a2b0b281bfb311f979c7ed65e441a184ebe338b05f5fec8a60768610965c9c94`.
- The group convention inherited here is order 24:
  \(D_{12}=\operatorname{Dih}(C_{12})\), with a rotation of order 12.
  Accordingly the Reynolds coefficient is \(1/24\), never \(1/12\).

## Descent and Chow transfer

- Stacks Project, Tag `02VL`, Lemma 35.23.29: smoothness is fpqc local on
  the base. Used only after smoothness of the source row is known.
- Stacks Project, Tag `0CDQ`, Lemma 35.6.1: quasi-coherent/Galois descent
  locator for cocycle language.
- Stacks Project, Tag `0CCI`, Lemma 39.25.2: an effectivity result under its
  finite-locally-free and affine-open hypotheses. It is not cited as an
  automatic theorem for arbitrary projective descent data.
- Stacks Project, Tag `08KE`: cautionary counterexample motivating the
  explicit fixed-basis construction.
- Fulton, *Intersection Theory*, §§1.4, 1.7 and Proposition 1.7:
  proper pushforward, flat pullback, and degree formulas used for
  restriction/corestriction.
- Stacks Project, Tag `02RF`, Lemmas 42.15.1--2 (alternatively Tag `0EPC`,
  Lemmas 82.11.1--2): cycle pull-push formulas.
- Bruno Kahn, arXiv:2312.01825, Theorem 1 and Theorem 7.1: optional modern
  category-level locator for rational pure-motive descent. The elementary
  graph-sum and pull-push proof is retained as the operative proof.

## Compatible systems and local factors

- Katz--Messing, *Some consequences of the Riemann hypothesis for
  varieties over finite fields*, Invent. Math. 23 (1974), 73--77,
  Theorem 2(2), pp. 76--77, DOI `10.1007/BF01405203`: comparison of
  correspondence traces used to obtain \(\ell\)-independent rational
  projected characteristic polynomials.
- SGA 4 III, Exposé XII, Theorem 5.1, and Exposé XVI: smooth/proper base
  change locators used in spreading and specialization.
- Deligne, *Les constantes des équations fonctionnelles des fonctions
  \(L\)*, LNM 349 (1973), §3, Proposition 3.8(i),(ii), and §§8--9:
  induction/additivity of local factors and compatibility locators for the
  quadratic Artin identities.

Integrality is not attributed to denominator clearing. It follows only
after compatibility gives monic factors of \(\det(U-F_p)\) in
\(\mathbf Q[U]\): the full smooth-projective characteristic polynomial is
monic in \(\mathbf Z[U]\), and algebraic integrality/Gauss's lemma puts
each rational factor in \(\mathbf Z[U]\). Reversing coefficients gives
\(\det(1-F_pT)\in\mathbf Z[T]\); the latter is not called monic.
Tate-normalized local polynomials are kept at the \(\mathbf Q[U]\) level.
All local formulas use geometric Frobenius, with
\(F_p\mid\mathbf Q_\ell(-1)=p\), consistently with C49--C52.

## Prior geometry and novelty boundary

- Favero--Iliev--Katzarkov, *On the Griffiths groups of Fano manifolds of
  Calabi--Yau Hodge type*, arXiv:1212.2608, §5.1 equation (6) and §5.4
  equation (8): prior Hodge-number and Cayley-ring context for a smooth
  \((2,3)\) fivefold in \(\mathbf P^7\).
- Vial, New York J. Math. 19 (2013), Example 4.12: finite-dimensional
  motive context for smooth \((2,3)\) fivefolds. This is background, not
  needed for the explicit projector descent proof.
- Laterveer, arXiv:2105.02224: the cited ambient-even hypothesis does not
  cover the present \(\mathbf P^7\) case.

Targeted exact-equation and recent-literature searches found no matching
construction combining this Hénon-derived rational form, the twisted
order-24 Reynolds descent, and the rank-10 rational projector. This is a
bounded no-match statement, not a claim of absolute priority.

## Explicitly pending or outside scope

- No source is invoked for semisimplicity, automorphy, analytic
  continuation, or a functional equation; none is claimed.
- No theorem identifying the rank-10 motive with an actual Calabi--Yau
  threefold or Prym motive is claimed.
- No conic-bundle/Prym theorem is used. Any quadric-bundle or
  intersection-motive route is future work and needs an independent
  flatness theorem and separate source audit.
- A one-prime irreducibility certificate and the full rank-10 Frobenius
  polynomial are not yet available; the criterion in `PROOF_PACKAGE.md` is
  conditional and scoped to rational projectors visible in the chosen
  realization.
