---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-mvp2-corpus-frontier-synthesis"
canonical_tex: "zeta_mvp0/papers/RH-MVP2-corpus-frontier-synthesis/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-MVP2-corpus-frontier-synthesis/main.pdf"
source_sha256: "32d0826c731ab7aa5273529e1e9d7b9652cbef775334b23acce28ad7156e6913"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Conditional Prime Dynamics: a Corpus Frontier Synthesis Provenance, branch separation, and the unpaid theorem budget in RH-1--RH-361

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-MVP2-corpus-frontier-synthesis>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-MVP2-corpus-frontier-synthesis/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-MVP2-corpus-frontier-synthesis/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-MVP2-corpus-frontier-synthesis/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The conditional prime-dynamics program has produced 361 numbered RH papers, many of them intentionally narrow reviews, certificates, or scoped negative results. This document is a provenance-preserving synthesis rather than a replacement corpus: the numbered papers remain the atomic source of every claim. We compress the corpus into five functional phases, separate the actual noisy branch from the deterministic counterloop branch, and state the exact common-clock identities that prevent promotion between them. The latest source-locked frontier is the unnormalised same-clock head budget $$D_{4k}(R)=\sum_{2\le n<4k}|h_{\sigma,n}-s_{k,n}|R^n/n\longrightarrow0,$$ which is assumed by the RH-355--RH-360 transfer statements and proved by none of the sources. The synthesis therefore records `NOT_TESTABLE` for the next numbered route. All five Gates A--E remain false/open. No Hilbert--Polya operator, Riemann-zero identification, von Mangoldt trace, completed-zeta divisor identity, or proof of the Riemann Hypothesis is claimed.
author:
- Liang Wang
date: August 2026
title: |
  **Conditional Prime Dynamics: a Corpus Frontier Synthesis**\
  Provenance, branch separation, and the unpaid theorem budget in RH-1--RH-361
```

## Markdown 正文

# Purpose and status vocabulary

This paper changes altitude, not the mathematics. It is intended to make a large research record readable before a new idea is attempted. It does not delete, rewrite, or silently merge any numbered paper. A machine-readable inventory records all unique numbers $1,\ldots,361$ and the four historical duplicate directory groups. The inventory hashes selected source files and checks presence; it is not a re-proof of the corpus.

We use five non-interchangeable labels:

proved

:   an analytic theorem in the scope written in its source paper;

certified

:   a finite exact or outward-rounded computation;

conditional

:   a valid implication whose physical hypotheses remain open;

scoped negative

:   a proved non-implication or obstruction for the named route, not for every possible model;

open/NOT\_TESTABLE

:   the required source, identification, clock, or uniform estimate is absent.

# Provenance topology

The filesystem contains 361 unique numerical labels and 365 directories matching the numerical naming pattern. The difference is explained by four empty historical aliases at RH-302, RH-303, RH-304, and RH-306. The audit therefore identifies a source by its full canonical directory path and a SHA-256 digest, never by its number alone. It chooses the candidate containing the README, TeX source, and PDF, and records the empty alternative as an alias rather than deleting it.

There are 29 established review anchors:

> RH-71, 81, 91, 100, 119, 129, 139, 149, 159, 171, 181, 191, 201, 211, 221, 231, 241, 251, 261, 271, 281, 291, 301, 311, 321, 331, 341, 351, and 361.

Their declared input ranges cover 349 of the 361 numbered IDs. The twelve exceptions are RH-101--RH-109, RH-150, RH-160, and RH-161. They are not discarded: RH-MVP1 covers RH-1--RH-160, while RH-161 is the independent packet-to-Riesz relative determinant assembly feeding the next phase. This matters because the review batches are not all identical ten-paper windows. For example, RH-159 audits RH-151--RH-158 and leaves RH-150 separate, while RH-171 audits RH-162--RH-170 and leaves RH-161 separate.

The canonical inventory is a surjection from 361 numerical labels to 361 nonempty source directories, together with four recorded empty aliases. The synthesis changes neither a source hash nor the logical status attached to a source claim.

The executable inventory enumerates every numerical label from 1 through 361, requires a README, TeX source, and PDF in the chosen directory, and hashes the available README, manuscript, theorem ledger, roadmap, and result record. The archive verifier replays all 1,356 selected source hashes. This proves presence and identity only; it deliberately does not claim to re-prove the source theorems.

# Five functional phases

The numbered sequence can be read as the following dependency map. The intervals are navigation ranges, not claims that every paper in an interval has the same logical strength.

  range         role                                                         durable content and boundary
  ------------- ------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  RH-1--160     symbolic, determinant, packet, reset, and MVP architecture   corrected sieve--kneading coordinates, parity and determinant hygiene, finite/continuum certificates, and a conditional five-interface roadmap; no all-level intrinsic determinant, self-adjoint generator, arithmetic trace, or RH conclusion.
  RH-161--241   physical Riesz and trace-envelope frontier                   packet/transport and regularised determinant analyses, culminating in the moving noisy all-order envelope question; RH-241 explicitly leaves the uniform envelope and coefficient anchor open.
  RH-242--271   deterministic numerator and analytic-tail tools              deterministic coefficient anchors, all-order envelopes, sharp radii, and quotient/tail certificates; these are target-side results and do not identify a moving noisy head.
  RH-272--341   prefix, annular, endpoint, spectral, and alias routes        exact typed decompositions, rate-free or conditional diagonal bridges, endpoint and alias obstructions, and information-class negatives; no common physical full-prefix budget is closed.
  RH-342--361   signed completion and counterloop frontier                   selected/normalised actual $p,Y$ results, an unconditional deterministic counterloop $s$ branch, and the exact typed separation theorem; the physical head-defect bridge remains open.

# What the intermediate frontiers establish

## Foundation and Stage-A architecture: RH-1--RH-160

RH-MVP1 already compresses this range into a rigorous foundation $F$ and five missing interfaces A--E. The foundation includes the corrected symbolic coordinate, parity-resolved deterministic trace geometry, fixed-noise regularised determinants, continuum bridges, and finite certification tools. Its conditional spectral-divisor closure is a valid implication, but none of its five macro premises is supplied merely by the 160-layer audit. The first unpaid interface is still the canonical all-level determinant A.

## Physical clouds and trace envelopes: RH-161--RH-241

This range passes through packet-to-Riesz assembly, history/cycle identities, biorthogonal clocks, source-channel quartets, divisor-first transport, and rank-growing clouds. The later batches establish finite and local structure for projection-free regularised determinants. RH-241 records 7,280 finite ledger items and a subunit trace envelope for orders 2--12, but explicitly leaves the moving all-order noisy envelope and coefficient identification open. Repeating or extending the finite atlas is not an all-order theorem.

## Deterministic target closure: RH-242--RH-281

The superloop and selector papers isolate which finite anchored completions are unavailable. RH-263 gives the deterministic numerator coefficient anchor; RH-267 gives a certified unified all-order deterministic trace envelope; RH-268 gives the sharp deterministic coefficient radius. RH-281 adds the deterministic counterloop bridge. These are genuine all-order target-side results, but they do not identify the moving noisy cloud, actual head, or full-trace coefficient.

## Noisy tails, annuli, and endpoint spectra: RH-282--RH-321

This range contains genuine finite modulus-complete noisy heads, analytic complement tails, weighted-prefix clock thresholds, and exact annular criteria. It also gives sharp synthetic spectral endpoint realisability and saturation results. The distinctions are decisive: RH-294 has a rate-free weighted full-trace diagonal on an unspecified slow clock; RH-300 is a sufficient annular criterion; and RH-321 is sharp for the declared synthetic spectral class. None identifies the physical logarithmic clock with the complete actual head required at the later first-alias frontier.

## First alias and signed completion: RH-322--RH-361

RH-322--RH-341 build exact local physical formulas and transfer criteria but leave the aggregate actual obligations open. RH-342--RH-351 then prove information-class non-identifiability and signed-completion results; these are scoped negatives, not pairs of physical noisy operators. Finally, RH-352--RH-361 isolate the actual selected/normalised branch from the unconditional deterministic counterloop branch. This is the current endpoint used below.

# The current two-branch statement

On the source-locked Hardy clock $$k=\frac{\log(1/\sigma)}{2\log\lambda}+O(1),\qquad 2\le n<4k,$$ write $p$ for the actual direct coefficient, $q$ for the full-trace coefficient, $h$ for the actual modulus-complete head, and $s$ for the deterministic graded counterloop. The source papers give the typed identities $$p=\tau-a=q-d,\qquad d=h-s,
 \qquad q=p+d,\qquad h=s+d. \label{eq:typed}$$

The actual branch (RH-352--RH-354) controls selected or normalised $p$ and $Y$ quantities. The deterministic branch (RH-355--RH-360) closes a sequence of budgets for $s$, including terminal localisation, logarithmic inversion, and an exponential-tilt phase diagram. Equation [\[eq:typed\]](#eq:typed){reference-type="eqref" reference="eq:typed"} is an identity, not an inclusion of spectra and not a physical realisation of $s$.

The information supplied by the current corpus does not imply a physical bound for $q$ or $h$ from the proved selected/normalised $p$ results and the deterministic $s$ results alone. Any such promotion requires an independent estimate of the defect $d$ on the same clock and order range.

The identities in [\[eq:typed\]](#eq:typed){reference-type="eqref" reference="eq:typed"} show that both promotions contain the unpaid term $d$. RH-361 gives the finite coefficient-fibre calculation $d[e]=e$, $q[e]=p+e$, and $h[e]=s+e$ for arbitrary signed arrays $e$. This is an information-class non-implication. The construction does not assert that every fibre is realised by a noisy operator; therefore it is not a physical counterexample and cannot be used to promote or refute a spectral claim.

# The first missing leaf

Every actual-head inheritance statement in RH-355--RH-360 assumes the unnormalised budget $$D_{4k}(R)=\sum_{2\le n<4k}|h_{\sigma,n}-s_{k,n}|R^n/n\to0. \label{eq:defect}$$ The selected windows and normalisations in RH-352--RH-354 do not pay the loss in [\[eq:defect\]](#eq:defect){reference-type="eqref" reference="eq:defect"}; absolute majorants do not replace signed aggregate cancellation. RH-287 and RH-294 provide slower or unspecified diagonal results without identifying the physical clock. RH-241 still lacks the moving noisy all-order envelope and its no-over-extraction coefficient bridge.

Relative to the source files and claim firewall recorded in `RH_HANDOFF.md` at the current endpoint RH-361, no admissible source proves [\[eq:defect\]](#eq:defect){reference-type="eqref" reference="eq:defect"}, proves a genuine physical obstruction to it, or supplies an independent same-type full-trace $q/E_{\rm off}$ theorem on the common clock. Consequently RH-362 is not activated by the existing corpus.

The RH-361 review and its source-lock/auditor records list RH-355--RH-360 as conditional on [\[eq:defect\]](#eq:defect){reference-type="eqref" reference="eq:defect"}; they explicitly distinguish the normalised upper-band quantity from the unnormalised full prefix. The alternative-route scan records that RH-287/294 use a different diagonal clock, while RH-334, RH-339, RH-344, RH-346, and RH-348 give typed identities without an aggregate bound. The remaining admissible triggers in the handoff are exactly these missing leaves. This is a repository audit theorem, not a claim that no mathematical route exists outside the corpus.

# Durable non-promotions

Several recurring shortcuts are already excluded by source type or by a proved scoped negative result. A synthesis must keep them visible:

  invalid promotion                                                     unpaid information
  --------------------------------------------------------------------- --------------------------------------------------------------------
  finite rows $\Rightarrow$ all-order theorem                           a uniform moving-order estimate and asymptotic quantifiers
  fixed or synthetic spectrum $\Rightarrow$ actual noisy operator       a physical realisation and identification theorem
  slow diagonal clock $\Rightarrow$ logarithmic physical clock          a quantitative lower clock bound and common order range
  normalised tail $\Rightarrow$ unnormalised prefix                     the removed exponential scale and all omitted orders
  selected window $\Rightarrow$ complete $E_{\rm off}$                  odd, lower, critical, and upper-alias coordinates on one type
  separate absolute bounds $\Rightarrow$ signed aggregate obstruction   a signed cancellation or lower-bound theorem
  coefficient fibre $\Rightarrow$ physical counterexample               realisability by noisy operators with the required ranks and roots
  deterministic $s$ $\Rightarrow$ actual $h$ or $q$                     the common-clock defect $d=h-s$

# Gate matrix and claim firewall

  Gate   object                                               status       reason for non-promotion
  ------ ---------------------------------------------------- ------------ -------------------------------------------------
  A      canonical intrinsic dynamical determinant            false/open   no typed all-level moving-cloud assembly
  B      order-sensitive scattering/unitary completion        false/open   no canonical orientation-preserving completion
  C      self-adjoint generator and intrinsic $T\log T$ law   false/open   no proved generator or counting law
  D      von Mangoldt-weighted prime-power trace              false/open   no target-independent arithmetic trace identity
  E      completed-zeta spectral divisor equality             false/open   no no-missing/no-spurious divisor theorem

In particular, finite rows are reproduction checks; synthetic spectra are not physical noisy operators; conditional criteria are inactive until their hypotheses hold on one common clock; and deterministic shells are not actual root sets, ranks, or spectral submultisets. The synthesis does not construct a Hilbert--Polya operator, identify Riemann zeros, prove the von Mangoldt trace, prove completed-zeta divisor equality, or prove RH.

# What would justify a new numbered paper?

The shortest admissible reopen triggers are:

1.  a physical same-clock proof of [\[eq:defect\]](#eq:defect){reference-type="eqref" reference="eq:defect"}, or a genuine physical obstruction to it;

2.  a typed actual full-trace $q$ or complete $E_{\rm off}$ aggregate theorem;

3.  a complete unnormalised direct prefix including orders below the RH-354 moving cut;

4.  the RH-241 moving noisy all-order envelope plus a valid coefficient bridge; or

5.  another independent source-backed theorem edge.

More computation of finite rows, reparameterisation of RH-358--RH-360, normalisation changes, or relabelling a coefficient called $q$ does not meet one of these triggers.

# One umbrella and four long-form volumes

The present manuscript is the short umbrella: it fixes vocabulary, provenance, phases, Gates, and the current stop. The long-form publication layer consists of four independently auditable volumes without changing any theorem status:

1.  Volume I, RH-1--RH-160: foundations and the conditional A--E architecture, retained in RH-MVP1;

2.  Volume II, RH-161--RH-241: physical Riesz packets, temporal clouds, relative determinants, and the trace-envelope frontier;

3.  Volume III, RH-242--RH-281: deterministic numerator anchors, selectors, analytic tails, and counterloops;

4.  Volume IV, RH-282--RH-361: noisy heads, weighted/annular endpoints, first alias, and actual-versus-deterministic signed completion.

The four ranges are disjoint and cover RH-1--RH-361. This division is preferable to one purported mega-theorem because each volume exposes its data types, clocks, and independently auditable boundary.

# Conclusion

The corpus can therefore be treated as one coherent research map without pretending that it is one theorem. The useful compression is semantic: preserve the individual sources, expose the two typed branches, record the unpaid defect budget, and stop the numbered sequence until a new edge appears. That leaves room for genuinely new ideas while preventing old finite or conditional evidence from being recycled as a full-order result.
