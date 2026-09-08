# C420 bibliography and source verification

2026-09-08 UTC. This author receipt distinguishes new bounded primary
access from earlier team receipts. No paid database, external review API,
manuscript upload or saved external-source PDF was used.

## Journal metadata actually retrieved

DOI content negotiation with Accept: application/x-bibtex succeeded for:

| Key | Verified metadata |
| --- | --- |
| Young2019 | Matthew P. Young; Explicit calculations with Eisenstein series; Journal of Number Theory 199 (2019), 1–48; DOI 10.1016/j.jnt.2018.11.007 |
| BookerLeeStrombergsson2020 | Andrew R. Booker, Min Lee, Andreas Strömbergsson; Twist-minimal trace formulas and the Selberg eigenvalue conjecture; Journal of the London Mathematical Society 102(3) (2020), 1067–1134; DOI 10.1112/jlms.12349 |
| CakoniChanillo2019 | Fioralba Cakoni and Sagun Chanillo; Transmission Eigenvalues and the Riemann Zeta Function in Scattering Theory for Automorphic Forms on Fuchsian Groups of Type I; Acta Mathematica Sinica, English Series 35(6) (2019), 987–1010; DOI 10.1007/s10114-019-8128-8 |
| LevitinStrohmaier2021 | Michael Levitin and Alexander Strohmaier; Computations of Eigenvalues and Resonances on Perturbed Hyperbolic Surfaces with Cusps; International Mathematics Research Notices 2021(6), 4003–4050; DOI 10.1093/imrn/rnz157 |

The last raw BibTeX response used year 2019 because it records the online
publication. A successful direct Crossref work-record lookup explicitly
reported published-online 2019-10-09 and published-print 2021-03-12.
The manuscript uses the issue year 2021 and does not merge it with the
online date. The first work-record attempt failed (jq was absent, and
curl subsequently reported SSL_ERROR_SYSCALL); the replacement used a
JSON parser on standard input and succeeded. This was metadata parsing,
not a mathematical computation.

Bibliographic entries are normalized from these actual responses,
including TeX accents and page-range hyphens. Unnecessary ISSN/publisher
fields are omitted. No field was invented from memory.

## New primary reads during manuscript preparation

- Young, arXiv:1710.03624v2: metadata/version date 2017-11-03,
  definitions in Sections 3.1–3.2, completion, Proposition 4.2 and its
  functional-equation statement, Section 7 including (7.1)–(7.3) and
  their hypotheses, plus relevant fixed Fourier-space discussion and
  historical attribution. Conjugation-sensitive formulas were checked
  in HTML. Journal citation metadata was retrieved separately.
- Booker–Lee–Strömbergsson, arXiv:1803.06016v2: metadata/version date
  2020-04-17, Section 2.7's opening provenance, Lemma 2.19 and Remark
  2.20, the original versus extended-group distinction in that section,
  and the relevant functional-equation/matrix location from the existing
  full proof/source audits. Not a new whole-paper reading.
- DLMF Section 25.15: Euler product/nonvanishing, missing Euler factors,
  primitive functional equation and Gauss-sum convention, equations
  25.15.2 and 25.15.4–25.15.6. The homepage confirmed version 1.2.7,
  release 2026-06-15. A corporate NIST entry with that exact version
  is used; no unverified current editor list is supplied.
- Levitin–Strohmaier, arXiv:1812.05554v2: the squarefree formula (19),
  its explicit prime block and fixed invariant vector, and the Huxley
  bibliography entry. These are the cited facts, not its numerical
  experiments. A guessed Oxford page URL returned an internal error;
  no successful publisher-body reading is claimed.
- Keil's institutional dissertation record confirmed Caroline Keil,
  title, university, submission 2006-12-15 and doctorate 2007-01-25.
  This task read its metadata, not the full dissertation.

Primary URLs:
[Young](https://arxiv.org/html/1710.03624v2),
[Booker–Lee–Strömbergsson](https://arxiv.org/html/1803.06016v2),
[DLMF](https://dlmf.nist.gov/25.15),
[Levitin–Strohmaier](https://arxiv.org/html/1812.05554v2),
[Keil](https://docserv.uni-duesseldorf.de/servlets/DocumentServlet?id=3840).

## Retained provenance and limits

Huxley1984 is reused from the trusted local bibliography and corroborated
in both newly inspected Young and Levitin–Strohmaier bibliographies:
M. N. Huxley, Scattering matrices for congruence subgroups, in Modular
Forms (Durham, 1983), Horwood, Chichester (1984), 141–156.
No public full text was obtained and no claim about absent corollaries
in that chapter is made.

Cakoni–Chanillo's exact Theorem 2.8 access is the earlier coordinator
receipt, read fully here; only its journal metadata was newly retrieved
in this task. The mathematical squarefree control was also independently
read in the Levitin–Strohmaier primary text above.

The existing AS2 and C18 source audits supply additional context and
bounded collision work; they are not restated as fresh external reading.
No fresh search-query submission was made: only direct opens/finds and
DOI/metadata retrieval. No worldwide-priority claim is licensed.
