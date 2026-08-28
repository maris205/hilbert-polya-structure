# Paper 28 — ARS Stage 2 manuscript audit

Audit date: 2026-08-28
Manuscript: *An Exact Systole and Finite Enumeration Certificate for a
Nonarithmetic Genus-Two Octagon*
Stage status: **ARS Stage 2 draft complete; Stage 2.5 awaiting user
confirmation.** This report does not claim Stage 2.5 passage.

## 1. Deliverable and structure audit

| Check | Result |
|---|---|
| manuscript.tex, references.bib, paper.pdf | PASS |
| English abstract | PASS, 222 visible words by `detex` |
| Independent Traditional-Chinese abstract | PASS, 338 Han characters |
| Keywords | PASS, 6 English and 6 Traditional-Chinese terms |
| Introduction and related work | PASS |
| Exact geometry and source lock | PASS |
| Exact PSU(1,1) normal form | PASS |
| Tile-chain completeness theorem and proof | PASS |
| Exact systole theorem and primitive-witness proof | PASS |
| Implementation, certificate, adversarial and Route-A sections | PASS |
| Limitations and conclusion | PASS |
| Funding, conflict, CRediT, availability, ethics, AI disclosure | PASS |

The deterministic root audit counts **5,127 English body words**, beginning at
the Introduction and ending before the bibliography after LaTeX command
stripping. This lies within the frozen 4,000–6,500-word range. The English
abstract count treats hyphenated compounds as one word. The
Traditional-Chinese count removes LaTeX commands, mathematics, Latin text,
punctuation and digits, then counts Unicode Han characters.

The manuscript uses author **Liang Wang**, the specified Huazhong University
of Science and Technology affiliation and postal address, and
wangliang.f@gmail.com.

## 2. Citation existence and support audit

All six cited records were rechecked against primary or authoritative
repository/publisher pages on 2026-08-28. Every LaTeX citation has an auditable
locator.

| Key and locator | Existence and DOI verification | Supported claim | Boundary |
|---|---|---|---|
| Nazarenko2013, eqs. (10)–(18) | [Official arXiv v1](https://arxiv.org/abs/1301.5446v1); DOI 10.48550/arXiv.1301.5446; source tar hash-locked in Round 7 | Two-parameter genus-two octagon family, the `alpha=pi/4` slice, side-pairing convention, explicit generators and presentation | Does not prove this specialization nonarithmetic, its systole, guard or counts |
| AigonDupuyEtAl2005, abstract | [EPFL metadata](https://infoscience.epfl.ch/entities/publication/eb38a039-e625-41a3-a9a6-4fb5a81f7d7d); DOI 10.1063/1.1850177 | Peer-reviewed family-level context for hyperbolic octagons and genus-two Teichmüller space | Metadata/abstract support only; no Round-8 theorem attributed |
| Takeuchi1975, Theorem 1(i) | [J-STAGE article](https://www.jstage.jst.go.jp/article/jmath1948/27/4/27_4_600/_article); DOI 10.2969/jmsj/02740600 | Necessary algebraic trace-field condition for arithmetic cofinite Fuchsian groups | Does not supply the octagon or transcendence calculation |
| Popescu2024, Corollary 3.2 | [Springer chapter](https://link.springer.com/chapter/10.1007/978-3-031-51959-8_16) and [author arXiv v2](https://arxiv.org/abs/2306.14352v2); DOI 10.1007/978-3-031-51959-8_16 | Transcendence of exp(alpha) for nonzero algebraic alpha, used at alpha=-1/5 | Only the Lindemann–Weierstrass input |
| Voight2009, Sections 1–4 | [NUMDAM article](https://www.numdam.org/articles/10.5802/jtnb.683/); DOI 10.5802/jtnb.683 | Exact fundamental-domain algorithm context | Algebraic input setting; not this transcendental certificate |
| DespreEtAl2023, Sections 2–3 | [Dagstuhl DROPS article](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2023.27); DOI 10.4230/LIPIcs.SoCG.2023.27 | Polygon-input hyperbolic surface and Dirichlet-domain context | Does not supply the interval signs, radius lemma or systole |

Citation closure:

- unique cited keys: **6**;
- bibliography entries: **6**;
- cited keys missing from the bibliography: **0**;
- orphan bibliography entries: **0**;
- entries lacking DOI: **0**;
- style: natbib with plainnat, numeric and sorted/compressed.

The literature is not credited for project-derived results. The 18,533-state
component, 108,616 rejected boundary, exact signs and systole theorem are tied
to the project proof and certificate.

## 3. Mathematical and claim-boundary audit

The manuscript contains a continuous proof chain:

1. source-locked octagon and four side-pairing matrices;
2. exact inverse-pair and eight-factor relator checks;
3. transcendence-based nonarithmeticity through the invariant trace field;
4. canonical Gaussian-integer polynomial matrix normal form;
5. axis recentering and side-adjacent tile-chain proof;
6. completeness of the identity-connected centre sublevel component for every
   conjugacy class of length at most 21/10;
7. exact trace-polynomial comparison with
   2 acosh(1/(2 exp(-1/5)-1));
8. exhaustive finite classification and exact witness g0 g3;
9. global contradiction and primitive-root argument.

Symbolic results are marked **PROVED** and exhaustive exact finite execution is
marked **NUMERICALLY CERTIFIED**. Decimals carry no proof burden.

The manuscript states repeatedly that **144 counts distinct canonical group
elements in the finite component**. It is not an owner, conjugacy-class,
inverse-paired, orientation or geometric-geodesic count. No owner
classification is inferred.

Negative scope is explicit: no Bolza census, control conjugacy census,
Bolza-control census, magnetic comparison, target arithmetic labels,
determinant experiment, A2 evaluation or Route B. The formal full Route-A
tuple remains unassigned. The displayed bounded proxy is historical and
exploratory, not promoted.

## 4. Computational verification

### Historical suite

Command:

    PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s code -p 'test_*.py' -v

Result: **104/104 passed**, 0 failures and 0 errors in 1.111 s. This is the
complete historical suite: Round 2 (7), Round 3 (8), Round 4 (12), Round 5
(14), Round 6 (17), Round 7 (22), Round 8 (24).

### Round-8 verify-only reproducer

Command:

    PYTHONDONTWRITEBYTECODE=1 ./experiments/reproduce_round8.sh

Result: **PASS**. Its 24/24 tests passed. Two isolated builds were
byte-identical:

- run-1 tree SHA-256:
  c30beebdd2e832d9375f55f1eab700868b7b967dfb5ee43fcecc0ba5f60919ac;
- run-2 tree SHA-256: identical;
- byte_identical=true.

### Additional isolated certificate build

A third build in /tmp/p28-round9-third.FWxBM7 used explicit temporary outputs.
Each file compared byte-for-byte with the checked-in canonical artifact:

| Artifact | SHA-256 | cmp |
|---|---|---|
| finite-ball certificate JSON | c1bf68a8a1485665680dba01d0012fb691c7ca1a795e36334639e34bbbdbcb1f | PASS |
| systole source matrix CSV | 40bc9d12340b0b7c5619f862e8a087bffe3ae98f14e629d4c781969f6aa5eba6 | PASS |
| validation JSON | 4bf132b0d53e2cec329b26d0963f0e0f721c4c98fd4c58873b781bb5053e00c4 | PASS |

The replay confirms 18,533 included states, 108,616 distinct rejected boundary
states, 18,388 strict signs, 144 exact equality polynomials and no shorter
state. It does not enlarge the authorized scope.

## 5. Compilation, PDF and hashes

Build:

    lualatex -jobname=paper -interaction=nonstopmode -halt-on-error manuscript.tex
    bibtex paper
    lualatex -jobname=paper -interaction=nonstopmode -halt-on-error manuscript.tex
    lualatex -jobname=paper -interaction=nonstopmode -halt-on-error manuscript.tex

Toolchain: LuaHBTeX 1.14.0, BibTeX 0.99d (TeX Live 2022/Debian), Python
3.12.3, and display-only `mpmath` 1.3.0. All theorem-changing decisions use
standard-library exact integer or `Fraction` arithmetic; `mpmath` is not in
the decision path.

Final compilation: **PASS**. The final paper.log has zero Warning, Overfull,
Underfull, Missing character, undefined or Error matches. Text extraction
recovered both abstracts, body, declarations and references. Pages 1 and 13
were visually sampled for readable glyphs, equations, URLs and layout.

PDF:

- valid PDF 1.5, A4;
- **14 pages**, 319,392 bytes;
- SHA-256:
  6bbda36564994ac8dcc16c962655867f6c427b6aeb19d7071922c6e07678e688.

Source hashes:

- manuscript.tex:
  864d2f6ce0f76245d4d4237ba2981b3e82fc8e31f7991f1f331817f7c028aec7;
- references.bib:
  42474f492f261e97883f7b8e0577fc7a42ce58db7e084f456d92045b5788d284;
- paper.log:
  49c80b173a770c7a1d75fa80c8e64a59588de36cf741dae0fb9bcde1fc123bd3.

## 6. Independent review and patch disposition

Independent read-only review found **0 Blocker and 0 Major** issues and four
Minor metadata/scope items. The two-parameter family is now described
precisely as its `alpha=pi/4` one-parameter slice; the Nazarenko locator is
corrected to equations (10)–(18); the DROPS author metadata now names Benedikt
Kolbe; and the implementation section distinguishes exact standard-library
decision arithmetic from display-only `mpmath` 1.3.0. The post-patch 104/104
historical tests, 24/24 verify-only replay, four-pass build, log scan, and root
structural audit are clean. No theorem, state count, certificate, or Route-A
verdict changed.

## 7. Declarations and limitations

Declarations are complete:

- no external funding;
- no conflict of interest;
- full confirmed CRediT roles;
- repository and principal certificate named in data/code availability;
- no human, personal, animal or biological data; ethics approval and consent
  not applicable;
- AI-Assisted Research Disclosure names drafting, editing, LaTeX, consistency
  and metadata assistance; author responsibility and non-authorship stated.

Limitations retained:

- one fixed parameter, not a uniform family theorem;
- completeness through 21/10, not a full length spectrum;
- the identity-connected guard component is certified, not global guard
  connectivity;
- 144 equality elements are not classified into owners or conjugacy classes;
- no census, magnetic comparison, A2 or Route-B result.

**Stage decision:** the Stage-2 manuscript package is internally complete and
reproducible. It is held at the required checkpoint: **Stage 2.5 awaits
explicit user confirmation and has not been passed.**
