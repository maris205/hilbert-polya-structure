# Literature and novelty audit

Search cutoff: 2026-08-17 UTC.

## Exact claim searched

The audit searched for prior work proving, for Knauf's exact rooted label
`h(w)=1^T M_w e_1`, any of:

- failure to descend from rooted words to cyclic necklaces;
- failure of `h(w^r)=h(w)^r`;
- non-descent of the trailing-zero colimit's right append-one action;
- failure of `lambda(h(w))` to be a cyclic repetition character;
- identification of the source partition trace with a same-object primitive
  Fredholm determinant.

The bounded search did not locate a primary source stating this exact
four-witness conjunction.  This is a search result, not a proof that no such
source exists.

## Primary-source matrix

| Source | Verified role | Collision decision |
|---|---|---|
| A. Knauf, *The Number-Theoretical Spin Chain and the Riemann Zeroes*, CMP 196 (1998), 703--731, [official MPI record](https://www.mis.mpg.de/publications/preprint-repository/article/1997/issue-15), [DOI](https://doi.org/10.1007/s002200050441) | Original arithmetic spin-chain/Riemann-zero program; official abstract relates the question to Markov spectral radii, Ramanujan graphs, and a modular Lewis equation. | Source owner and nearest collision. It does not, in the metadata/full-source checks used here, state the exact rooted-to-necklace witness theorem. All inherited results remain attributed. |
| A. Knauf, 1999 erratum, [DOI](https://doi.org/10.1007/s002200050715), [official FAU record](https://cris.fau.de/publications/106651644/) | Required correction accompanying the 1998 source. | Must be cited; no novelty credit. |
| A. Knauf, *Phases of the Number-Theoretic Spin Chain*, J. Stat. Phys. 73 (1993), [official FAU record](https://cris.fau.de/publications/109359844/?lang=en_GB), [DOI](https://doi.org/10.1007/BF01052771) | Identifies `zeta(s-1)/zeta(s)` as the partition function and studies its phase transition. | Strong partition-function prior art; supports the decision not to claim the quotient itself. |
| A. Knauf, *The Spectrum of an Adelic Markov Operator*, [arXiv:1305.6410](https://arxiv.org/abs/1305.6410) | Primary normalization source used by the existing implementation; defines a distinct adelic Markov transition operator and studies its spectrum. | Separate operator/object. It cannot be imported as the missing `SD-C06` primitive operator. |
| P. Kleban and A. E. Oezluek, *A Farey Fraction Spin Chain*, [arXiv:cond-mat/9808182](https://arxiv.org/abs/cond-mat/9808182), [DOI](https://doi.org/10.1007/s002200050629) | Introduces a translation-invariant Farey spin chain and proves that its free energy equals that of a related non-translation-invariant number-theoretic chain. | Critical collision: equal free energy does not mean the same finite clock/object. The cyclic trace repair is already a distinct literature model. |
| J. Fiala, P. Kleban, A. Oezluek, *The Phase Transition in Statistical Models Defined on Farey Fractions*, [arXiv:math-ph/0203048](https://arxiv.org/abs/math-ph/0203048) | Proves several Farey-fraction models have the same free energy and links thermodynamics to a transfer operator. | Reinforces the free-energy/object firewall: thermodynamic equivalence does not transfer a primitive ledger. |
| J. Fiala and P. Kleban, *Generalized Number Theoretic Spin Chain—Connections to Dynamical Systems and Expectation Values*, [arXiv:math-ph/0503030](https://arxiv.org/abs/math-ph/0503030), [DOI](https://doi.org/10.1007/s10955-005-7579-8) | Introduces a parameterized generalization and connects its recursions to an intermittent transfer operator and the Lewis equation. | A changed generalized object/operator, not an in-place rooted `h` descent. |
| T. Prellberg, J. Fiala, P. Kleban, *Cluster Approximation for the Farey Fraction Spin Chain*, [arXiv:cond-mat/0507662](https://arxiv.org/abs/cond-mat/0507662), [DOI](https://doi.org/10.1007/s10955-006-9034-x) | The source explicitly defines energy using a matrix trace, notes that cyclic trace invariance makes the model translation invariant, and distinguishes its energy matrices from the generalized Knauf-chain quantities despite equal zero-field free energy. | Directly supports the changed-clock firewall. The trace repair is not Paper-41 novelty. |
| M. Technau, *Remark on the Farey fraction spin chain*, [arXiv:2304.08143](https://arxiv.org/abs/2304.08143) | Studies counts of products of the two Farey matrices having a prescribed **trace**. | Recent trace-model collision, not the rooted first-column-sum label. |

## Recent-window check

Queries covering 2024--2026 included combinations of:

```text
Knauf number-theoretical spin chain primitive cycles determinant
Knauf spin chain cyclic rotation Fredholm determinant
rooted word h(w) Farey matrix product Liouville
number theoretic spin chain trace model 2024 2025 2026
```

A 2024 McGill thesis on Farey matrix-product measures and the number-theoretic
spin chain was located in the institutional repository.  Its abstract centers
on measures, entropy functionals, the Conway box/question-mark function, and
matrix-product descriptions; it is contextual and does not establish the
exact four-witness theorem.  No 2024--2026 primary paper located by these
queries closed the frozen rooted-to-necklace descent.

## Internal Route collision audit

| Prior record | Overlap | Paper-41 firewall |
|---|---|---|
| Paper 1 / `SD-C06` | Owns the recursion, zeta quotient, external Liouville status, and statement that the primitive ledger is missing. | Paper 41 may claim only the explicit exact non-descent proof and repair typing. |
| Paper 33 / `SD-C35` | Proves an inherited graph-step operator fails to descend to a Manin-relation quotient. | Different object and relation; cite as methodological precedent, not mathematical source. |
| Paper 35 / `SD-C37` | Proves the general diagonal partition trace is a first trace-log coefficient rather than the same graph determinant. | T4 is a comparison lemma with zero novelty credit. |
| Paper 40 research seal / proposed `SD-C42` | Proves Gauss/Mayer pair-ledger and projection firewalls after corrections. | Different candidate. No Paper-40 correction, counterexample, or chronology is used as Paper-41 novelty. It only confirms that a cyclic trace/Mayer repair leaves `SD-C06`. |

The full 42-record integrated census is in `ROUTE_RECORD_CENSUS.md`.

## Search strategy and limits

Searches used title/abstract discovery across arXiv and the web, followed by
official institutional or arXiv records wherever available.  Exact-source
claims were checked against primary full text when accessible; metadata-only
records are not used to infer a missing theorem.  Citation chaining focused
on the Knauf chain, Farey trace chain, generalized chain, transfer-operator
connections, and recent trace-product counts.

Limits:

- no claim of exhaustive MathSciNet/Zentralblatt coverage;
- no universal negative claim from a failed keyword search;
- terminology varies between “number-theoretic”, “number-theoretical”,
  “Knauf”, and “Farey” chains;
- an independent bibliography reviewer should repeat citation chaining from
  Knauf 1998/1999 and the trace-chain papers before integration.

## Novelty assessment

- Source/function novelty: **none**; fully prior art.
- General partition-trace firewall novelty: **none**; already internal Paper
  35 and standard Fredholm algebra.
- Exact `SD-C06` four-witness non-descent theorem: **moderate, bounded**.
- Broad mechanism novelty: **low**; this is a closure theorem, not a positive
  Riemann mechanism.
- Selector/chronology novelty: **none**; the Boolean rule is retrospective and
  all witness outcomes were known before it was sealed.
- Collision risk: **medium**, because the Farey/Knauf literature contains
  multiple thermodynamically equivalent but object-distinct formulations.

Decision: `PROCEED_WITH_CAUTION_TO_INDEPENDENT_DA`.  Publishability depends on
keeping the exact source-specific theorem visible and refusing broader
novelty language.  No discovery priority follows from final-package ordering.
