# Source Verification Record

核验日期：2026-08-13。关键书目信息通过 DOI resolver、Crossref 返回元数据和期刊/出版社正式页面交叉核对；arXiv 仅用于获取开放全文或作者综述。Semantic Scholar batch API 在本轮返回 HTTP 429，因此按研究流程披露为不可用，并使用 Crossref/出版社回退，没有把缺失的聚合器记录当作引用失败。

| Identifier | Title check | Venue/year check | Status |
|---|---|---|---|
| `10.1016/j.indag.2024.05.007` | Dynamical systems for arithmetic schemes | Indagationes Mathematicae 37(1), 2026, 25--136 | VERIFIED; publisher + Crossref |
| `arXiv:2301.11643` | Primes, knots and periodic orbits | author survey, 2023 | VERIFIED; arXiv primary author text |
| `10.4171/LEM/66-3/4-2` | Dynamics of geodesics, and Maass cusp forms | L'Enseignement Mathématique 66 | VERIFIED; DOI + arXiv 1906.01067 |
| `10.18311/JIMS/1956/16985` | Harmonic analysis and discontinuous groups... | J. Indian Math. Soc. 20, 1956 | VERIFIED; DOI/archive |
| `10.1007/BFb0061302` | The Selberg Trace Formula for PSL(2,R), Vol. 2 | LNM 1001, 1983 | VERIFIED; Springer |
| `10.1016/0022-314X(82)90028-2` | Class numbers of indefinite binary quadratic forms | J. Number Theory 15, 1982 | VERIFIED; DOI + Crossref |
| `10.1007/BF01403069` | Zeta-functions for expanding maps and Anosov flows | Invent. Math. 34, 1976 | VERIFIED; DOI + author archive |
| `10.24033/asens.1515` | The zeta functions of Ruelle and Selberg. I | Ann. Sci. ENS 19, 1986 | VERIFIED; Numdam |
| `10.4007/annals.2013.178.2.6` | Anosov flows and dynamical zeta functions | Annals 178, 2013 | VERIFIED; journal page |
| `arXiv:2203.04917` | Erratum to Anosov flows and dynamical zeta functions | 2022 | VERIFIED; arXiv; continuation theorem unaffected |
| `10.24033/asens.2290` | Dynamical zeta functions for Anosov flows via microlocal analysis | Ann. Sci. ENS 49, 2016 | VERIFIED; Numdam |
| `10.2307/2006982` | An analogue of the prime number theorem for closed orbits of Axiom A flows | Annals 118, 1983 | VERIFIED; journal page |
| `10.1090/S0273-0979-1991-16023-4` | The thermodynamic formalism approach to Selberg's zeta function for PSL(2,Z) | Bull. AMS 25, 1991 | VERIFIED; AMS DOI |
| `10.1007/BF01405172` | The spectrum of positive elliptic operators and periodic bicharacteristics | Invent. Math. 29, 1975 | VERIFIED; DOI + Crossref |
| `10.1063/1.1665596` | Periodic orbits and classical quantization conditions | J. Math. Phys. 12, 1971 | VERIFIED; AIP DOI |
| `10.1070/IM1972v006n01ABEH001866` | Sur les formules explicites de la théorie des nombres | Math. USSR Izv. 6, 1972 | VERIFIED; MathNet/DOI |
| `10.1137/S0036144598347497` | The Riemann zeros and eigenvalue asymptotics | SIAM Review 41, 1999 | VERIFIED; SIAM DOI |

## Local-PDF integrity boundary

项目六份 prior-work PDF 均由 `pdfinfo` 确认未加密且页数可读，并使用 `pdftotext -f/-l` 逐页定位；环境缺少 `pypdf`，ARS PDF preflight 返回 `UNAVAILABLE`。因此本项目引用物理页码，但不声称完成了完整 PDF 对象/字体/附件完整性认证。
