# C187 source and ownership audit

## Primary source lock

Brendon Rhoades, “Cyclic sieving, promotion, and representation theory,”
*Journal of Combinatorial Theory, Series A* 117(1), 38--76 (2010), DOI
`10.1016/j.jcta.2009.03.017`, arXiv `1005.2568`.

The journal metadata and author/arXiv text were checked.  The precise locks are:

- Theorem 1.3 uses, for a rectangular partition `lambda` of `N`,
  `F(q)=[N]_q!/product_[c in lambda][h(c)]_q`.  There is **no q-shift** in
  this standard-tableau theorem.  The nearby column-strict theorem has a
  different shifted Schur specialization and is not substituted here.
- Corollary 3.6 states that every rectangular standard tableau is fixed by
  the `N`th power of promotion.
- Remark 3.2 explicitly warns that the order need not equal `N`; one-row and
  one-column tableaux have order one, and `(2,2)` is another counterexample.
- Section 7 records `e j e=j^{-1}` for evacuation and promotion, with the
  corresponding dihedral action.

Mark D. Haiman, “Dual equivalence with applications, including a conjecture
of Proctor,” *Discrete Mathematics* 99, 79--113 (1992), DOI
`10.1016/0012-365X(92)90368-P`, is the classical promotion-order background
cited in Rhoades's Corollary 3.6 discussion.

## Convention lock

The package uses Rhoades's promotion convention on standard tableaux: remove
the maximum entry `N`, move the hole northwest by jeu de taquin, increment the
retained entries, then insert `1`.  The more common remove-`1` convention is
the inverse map.  They have the same cycle counts, but silently switching them
would break the frozen clock and the executable reversor test.

## Claim-level ownership

- **Classical source theorem:** rectangular promotion has `j^N=id`, and
  `(SYT(b^a), <j>, F_ab(q))` exhibits the CSP.
- **Classical source structure:** evacuation is an involution conjugating
  promotion to its inverse.
- **Package derivation:** fixed counts are converted by Möbius inversion into
  exact periods and cycles, and then into the finite zeta, Koopman determinant,
  trace and root-of-unity multiplicities.
- **Executable evidence:** cyclotomic reconstruction and small direct
  enumeration test those consequences.  They are not offered as a proof of
  Rhoades's all-rectangle theorem.
- **Not claimed:** priority for any classical result, a literature-wide
  novelty certificate, or external peer review.

The bibliography population is two.  Neither source supplies target zeros,
prime tables, arithmetic local data, Euler factors, root numbers, automorphy,
or a Hilbert--Polya operator.
